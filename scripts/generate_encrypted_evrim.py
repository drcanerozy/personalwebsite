#!/usr/bin/env python3
import os
import sys
import re
import json
import subprocess
from pathlib import Path

BASE_DIR = Path("/Users/canerozyildirim/Sites/personalwebsite")
SLIDES_DIR = BASE_DIR / "slides"
SOURCE_HTML = SLIDES_DIR / "beslenmenin_evrimi_sunum.html"
TARGET_HTML_1 = SLIDES_DIR / "01-beslenmenin-evrimi.html"
TARGET_HTML_2 = SLIDES_DIR / "beslenmenin_evrimi_sunum.html"

PASSWORD = "COZYPOP2026_"
PRES_ID = "beslenmenin_evrimi_bes339"
PUBLIC_COUNT = 10

def encrypt_aes_payload(plaintext: str, password: str) -> str:
    node_script = """
const CryptoJS = require('crypto-js');
const input = JSON.parse(process.argv[1]);
const ciphertext = CryptoJS.AES.encrypt(input.plaintext, input.password).toString();
console.log(ciphertext);
"""
    payload = {
        "plaintext": plaintext,
        "password": password
    }
    res = subprocess.run(
        ["node", "-e", node_script, json.dumps(payload)],
        capture_output=True,
        text=True,
        check=True
    )
    return res.stdout.strip()

with open(SOURCE_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Read minified crypto-js
crypto_js_file = SLIDES_DIR / "assets/crypto-js.min.js"
with open(crypto_js_file, "r", encoding="utf-8") as f:
    crypto_js_code = f.read()

# 2. Extract SLIDES array
pos = html.find("const SLIDES = [")
if pos == -1:
    raise ValueError("const SLIDES = [ bulunamadı!")

sub = html[pos + len("const SLIDES = ["):]
end_pos = sub.find("];\n")
if end_pos == -1:
    end_pos = sub.find("];")

slides_json_str = "[" + sub[:end_pos] + "]"
all_slides = json.loads(slides_json_str)
total_slides_count = len(all_slides)
print(f"Toplam slayt sayısı: {total_slides_count}")

public_slides = all_slides[:PUBLIC_COUNT]
locked_slides = all_slides[PUBLIC_COUNT:]

print(f"Açık slaytlar: {len(public_slides)}, Kilitli slaytlar: {len(locked_slides)}")

# Encrypt locked slides JSON
locked_json_str = json.dumps(locked_slides, ensure_ascii=False)
ciphertext = encrypt_aes_payload(locked_json_str, PASSWORD)
print(f"Ciphertext üretildi (Uzunluk: {len(ciphertext)} bayt)")

# Prepare metadata for overview modal while locked (to show locked slide placeholders with titles)
locked_metadata = []
for s in locked_slides:
    locked_metadata.append({
        "orderNum": s.get("orderNum"),
        "origSlideNum": s.get("origSlideNum"),
        "category": s.get("category"),
        "title": s.get("title"),
        "subtitle": s.get("subtitle", "")
    })
locked_meta_json = json.dumps(locked_metadata, ensure_ascii=False)

# Replace SLIDES array with public_slides ONLY
public_slides_str = json.dumps(public_slides, indent=2, ensure_ascii=False)
new_html = html[:pos + len("const SLIDES = ")] + public_slides_str + html[pos + len("const SLIDES = [") + end_pos + 1:]

# Inject HTTPS redirect if not already present
if "location.protocol==='http:'" not in new_html:
    https_redirect = """<script>if(location.protocol==='http:'&&location.hostname!=='localhost'&&location.hostname!=='127.0.0.1'){location.replace('https:'+location.href.substring(5));}</script>"""
    new_html = new_html.replace('<head>', '<head>\n    ' + https_redirect, 1)

# Patch totalSlides
new_html = new_html.replace(
    "const totalSlides = SLIDES.length;",
    f"let totalSlides = {total_slides_count};"
)

# Patch renderSlide for slide 10 preview barrier banner
render_banner_code = """
            // 10 Slaytlık Açık Önizleme Kilit Bannerı
            if (!isUnlocked && num === 10) {
                const lockBanner = document.createElement('div');
                lockBanner.className = 'mt-6 p-4 rounded-2xl bg-amber-50/90 border border-amber-300 flex flex-col sm:flex-row items-center justify-between gap-3 select-none';
                lockBanner.innerHTML = `
                    <div class="flex items-center space-x-3 text-left">
                        <span class="text-2xl shrink-0">🔒</span>
                        <div>
                            <p class="text-xs font-bold text-amber-950 font-serif">10 Slaytlık Açık Önizleme Sınırı</p>
                            <p class="text-[11px] text-amber-800">Neolitik Devrim, Beslenme Dönüşümü ve Diyet Modellerini içeren devam slaytları (Slayt 11-101) öğrenci şifresiyle korunmaktadır.</p>
                        </div>
                    </div>
                    <button type="button" onclick="openLockModal(10)" class="w-full sm:w-auto px-4 py-2 bg-gradient-to-r from-amber-700 to-amber-800 hover:from-amber-800 hover:to-amber-900 text-white text-xs font-bold rounded-xl transition shadow-sm shrink-0 flex items-center justify-center space-x-2 cursor-pointer">
                        <span>🔓</span>
                        <span>Ders Şifresini Gir & Devam Et</span>
                    </button>
                `;
                bodyEl.appendChild(lockBanner);
            }
"""

pos_body_split = new_html.find("split.appendChild(rightCol);\n            bodyEl.appendChild(split);")
if pos_body_split != -1:
    target_str = "split.appendChild(rightCol);\n            bodyEl.appendChild(split);"
    new_html = new_html.replace(target_str, target_str + "\n" + render_banner_code)
else:
    pos_body_split = new_html.find("bodyEl.appendChild(split);")
    new_html = new_html.replace("bodyEl.appendChild(split);", "bodyEl.appendChild(split);\n" + render_banner_code)

# Patch nextSlide
orig_next = """        function nextSlide() {
            if (currentSlideIdx < totalSlides - 1) {
                currentSlideIdx++;
                triggerSlideTransition();
            }
        }"""

patched_next = """        function nextSlide() {
            if (!isUnlocked && currentSlideIdx >= 9) {
                openLockModal(10);
                return;
            }
            if (currentSlideIdx < totalSlides - 1) {
                currentSlideIdx++;
                triggerSlideTransition();
            }
        }"""
new_html = new_html.replace(orig_next, patched_next)

# Patch goToSlide
orig_goto = """        function goToSlide(idx) {
            if (idx >= 0 && idx < totalSlides) {
                currentSlideIdx = idx;
                triggerSlideTransition();
                closeOverviewModal();
            }
        }"""

patched_goto = """        function goToSlide(idx) {
            if (!isUnlocked && idx >= 10) {
                openLockModal(idx);
                return;
            }
            if (idx >= 0 && idx < totalSlides) {
                currentSlideIdx = idx;
                triggerSlideTransition();
                closeOverviewModal();
            }
        }"""
new_html = new_html.replace(orig_goto, patched_goto)

# Patch buildOverviewGrid to display locked slides gracefully
orig_grid = """        function buildOverviewGrid() {
            const container = document.getElementById('overview-grid');
            container.innerHTML = '';

            SLIDES.forEach((s, idx) => {
                const card = document.createElement('div');
                card.onclick = () => goToSlide(idx);
                card.className = `p-3.5 rounded-2xl border transition cursor-pointer flex flex-col justify-between space-y-2 overview-item ${
                    idx === currentSlideIdx 
                        ? 'bg-amber-100/70 border-amber-500 shadow-xs' 
                        : 'bg-white border-stone-200/80 hover:border-amber-400 hover:shadow-2xs'
                }`;

                card.innerHTML = `
                    <div class="flex items-center justify-between">
                        <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-md bg-stone-100 text-stone-700">#${String(s.orderNum).padStart(2, '0')}</span>
                        <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-amber-800 truncate max-w-[140px]">${s.category}</span>
                        ${s.images.length > 0 ? '<i class="fa-regular fa-image text-stone-400 text-xs shrink-0"></i>' : ''}
                    </div>
                    <h5 class="text-xs font-serif font-bold text-stone-900 line-clamp-2">${s.title}</h5>
                    <div class="flex items-center justify-between text-[10px] font-mono text-stone-400 pt-1 border-t border-stone-100">
                        <span class="truncate italic">${s.subtitle || ''}</span>
                        <span class="shrink-0 text-stone-300">PPT #${s.origSlideNum}</span>
                    </div>
                `;
                container.appendChild(card);
            });
        }"""

patched_grid = """        const LOCKED_META = """ + locked_meta_json + """;

        function buildOverviewGrid() {
            const container = document.getElementById('overview-grid');
            container.innerHTML = '';

            // 1. Render currently active SLIDES
            SLIDES.forEach((s, idx) => {
                const card = document.createElement('div');
                card.onclick = () => goToSlide(idx);
                card.className = `p-3.5 rounded-2xl border transition cursor-pointer flex flex-col justify-between space-y-2 overview-item ${
                    idx === currentSlideIdx 
                        ? 'bg-amber-100/70 border-amber-500 shadow-xs' 
                        : 'bg-white border-stone-200/80 hover:border-amber-400 hover:shadow-2xs'
                }`;

                card.innerHTML = `
                    <div class="flex items-center justify-between">
                        <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-md bg-stone-100 text-stone-700">#${String(s.orderNum).padStart(2, '0')}</span>
                        <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-amber-800 truncate max-w-[140px]">${s.category}</span>
                        ${s.images && s.images.length > 0 ? '<i class="fa-regular fa-image text-stone-400 text-xs shrink-0"></i>' : ''}
                    </div>
                    <h5 class="text-xs font-serif font-bold text-stone-900 line-clamp-2">${s.title}</h5>
                    <div class="flex items-center justify-between text-[10px] font-mono text-stone-400 pt-1 border-t border-stone-100">
                        <span class="truncate italic">${s.subtitle || ''}</span>
                        <span class="shrink-0 text-stone-300">PPT #${s.origSlideNum}</span>
                    </div>
                `;
                container.appendChild(card);
            });

            // 2. If locked, render placeholders for locked slides
            if (!isUnlocked && SLIDES.length <= 10) {
                LOCKED_META.forEach((s, lIdx) => {
                    const idx = 10 + lIdx;
                    const card = document.createElement('div');
                    card.onclick = () => openLockModal(idx);
                    card.className = "p-3.5 rounded-2xl border transition cursor-pointer flex flex-col justify-between space-y-2 overview-item bg-stone-50 border-stone-200/80 hover:border-amber-500 hover:bg-amber-50/40 opacity-80 hover:opacity-100";

                    card.innerHTML = `
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-md bg-stone-200 text-stone-600">#${String(s.orderNum).padStart(2, '0')}</span>
                            <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-stone-500 truncate max-w-[140px] flex items-center gap-1">
                                <i class="fa-solid fa-lock text-amber-600"></i> ${s.category}
                            </span>
                        </div>
                        <h5 class="text-xs font-serif font-bold text-stone-700 line-clamp-2">${s.title}</h5>
                        <div class="flex items-center justify-between text-[10px] font-mono text-amber-700 pt-1 border-t border-stone-200/60 font-semibold">
                            <span class="truncate italic"><i class="fa-solid fa-key mr-1 text-[9px]"></i>Ders Şifresiyle Aç</span>
                            <span class="shrink-0 text-stone-400">PPT #${s.origSlideNum}</span>
                        </div>
                    `;
                    container.appendChild(card);
                });
            }
        }"""

new_html = new_html.replace(orig_grid, patched_grid)

# Prepare Lock Modal HTML
lock_modal_html = """
<!-- STUDENT PASSWORD LOCK MODAL -->
<div id="student-lock-modal" style="display:none; position:fixed; inset:0; background:rgba(11,17,29,0.88); backdrop-filter:blur(10px); z-index:99999; align-items:center; justify-content:center; padding:20px; font-family:'Inter', system-ui, sans-serif;">
  <div id="modal-card" style="background:#131d2e; border:1px solid #233554; border-radius:24px; max-width:440px; width:100%; padding:32px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.6); text-align:center; position:relative; color:#f8fafc;">
    <button type="button" onclick="closeLockModal()" style="position:absolute; top:16px; right:16px; background:none; border:none; color:#94a3b8; font-size:20px; cursor:pointer; padding:4px 8px; border-radius:8px;">✕</button>
    <div style="width:64px; height:64px; border-radius:18px; background:rgba(217,119,6,0.15); border:1px solid rgba(217,119,6,0.3); color:#fbbf24; display:flex; align-items:center; justify-content:center; font-size:26px; margin:0 auto 16px;">🔒</div>
    <h3 style="font-size:20px; font-weight:700; margin:0 0 8px; color:#ffffff;">Öğrenci Kilit Ekranı</h3>
    <p style="font-size:13px; color:#94a3b8; line-height:1.6; margin:0 0 24px;">10 slaytlık açık önizleme tamamlanmıştır. Dersin devamını görüntülemek için lütfen BES 339 ders şifrenizi giriniz.</p>
    <form onsubmit="handleUnlockSubmit(event)" style="display:flex; flex-direction:column; gap:16px;">
      <div style="text-align:left;">
        <label for="student-password-input" style="display:block; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; color:#cbd5e1; margin-bottom:6px;">Ders Şifresi:</label>
        <div style="position:relative;">
          <input type="password" id="student-password-input" placeholder="Şifrenizi yazınız..." required autocomplete="current-password"
            style="width:100%; box-sizing:border-box; background:#0b1320; border:1px solid #334155; border-radius:12px; padding:12px 42px 12px 14px; font-size:14px; color:#ffffff; outline:none; font-family:monospace;">
          <button type="button" onclick="togglePasswordVisibility()" style="position:absolute; right:12px; top:50%; transform:translateY(-50%); background:none; border:none; color:#94a3b8; cursor:pointer; font-size:14px;">👁️</button>
        </div>
      </div>
      <div id="unlock-error-msg" style="display:none; font-size:12px; color:#f87171; background:rgba(127,29,29,0.4); border:1px solid #991b1b; border-radius:10px; padding:10px; text-align:center;">
        ⚠️ Hatalı şifre! Lütfen BES 339 ders izlencesindeki şifrenizi kontrol ediniz.
      </div>
      <button type="submit" id="unlock-submit-btn" style="width:100%; background:linear-gradient(135deg, #d97706, #b45309); color:#ffffff; font-weight:700; border:none; border-radius:12px; padding:14px; font-size:14px; cursor:pointer; box-shadow:0 10px 15px -3px rgba(217,119,6,0.3); transition:transform 0.1s;">
        🔓 Şifreyi Çöz &amp; Derse Devam Et
      </button>
    </form>
    <div style="margin-top:20px; padding-top:16px; border-top:1px solid #1e293b; font-size:11px; color:#64748b; display:flex; align-items:center; justify-content:center; gap:6px;">
      <span>🔒</span> <span>BES 339 • Diyet İlkeleri ve Popüler Diyetler</span>
    </div>
  </div>
</div>
<style>
@keyframes modalShake {
  0%, 100% { transform: translateX(0); }
  20%, 60% { transform: translateX(-8px); }
  40%, 80% { transform: translateX(8px); }
}
.modal-shake { animation: modalShake 0.4s ease-in-out; }
</style>
"""

# Client script
client_lock_script = f"""
<!-- INLINED ZERO-DEPENDENCY CRYPTOJS ENGINE -->
<script>
{crypto_js_code}
</script>

<!-- AES-256 ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data-evrim" type="text/plain">
{ciphertext}
</script>

{lock_modal_html}

<script>
/* ================= STUDENT LOCK & CRYPTOJS DECRYPTION ENGINE ================= */
var PRES_ID = "{PRES_ID}";
var PUBLIC_SLIDE_COUNT = {PUBLIC_COUNT};
var TOTAL_SLIDES_COUNT = {total_slides_count};
var isUnlocked = false;
var pendingTargetSlide = null;
var encryptedPayloadCiphertext = "";

document.addEventListener('DOMContentLoaded', () => {{
  const scriptTag = document.getElementById('encrypted-payload-data-evrim');
  if (scriptTag) {{
    encryptedPayloadCiphertext = scriptTag.textContent.trim();
  }}
  checkSessionUnlock();
}});

function getPasswordCandidates(inputStr) {{
  const p = (inputStr || '').trim();
  if (!p) return [];
  const set = new Set();
  set.add(p);
  set.add(p.toUpperCase());
  set.add(p.toLowerCase());
  set.add(p.toLocaleUpperCase('en-US'));
  set.add(p.toLocaleUpperCase('tr-TR'));
  if (!p.endsWith('_')) {{
    set.add(p + '_');
    set.add(p.toUpperCase() + '_');
    set.add(p.toLocaleUpperCase('en-US') + '_');
  }} else {{
    const withoutUnderscore = p.replace(/_+$/, '');
    set.add(withoutUnderscore);
    set.add(withoutUnderscore.toUpperCase());
    set.add(withoutUnderscore.toLocaleUpperCase('en-US'));
  }}
  return Array.from(set);
}}

function decryptPayload(ciphertext, passwordInput) {{
  const candidates = getPasswordCandidates(passwordInput);
  for (const cand of candidates) {{
    try {{
      const bytes = CryptoJS.AES.decrypt(ciphertext, cand);
      const dec = bytes.toString(CryptoJS.enc.Utf8);
      if (dec && dec.length > 50) return dec;
    }} catch(e) {{}}
  }}
  throw new Error("Şifre çözülemedi.");
}}

function handleUnlockSubmit(e) {{
  if (e && e.preventDefault) e.preventDefault();
  const input = document.getElementById('student-password-input');
  const password = input ? input.value.trim() : '';
  const errorEl = document.getElementById('unlock-error-msg');
  const submitBtn = document.getElementById('unlock-submit-btn');
  const modalCard = document.getElementById('modal-card');

  if (!password) return;
  if (submitBtn) {{
    submitBtn.disabled = true;
    submitBtn.innerHTML = '⏳ Şifre Çözülüyor...';
  }}
  if (errorEl) errorEl.style.display = 'none';

  let decryptedJson = null;
  try {{
    decryptedJson = decryptPayload(encryptedPayloadCiphertext, password);
  }} catch(authErr) {{
    console.error("Şifre çözme hatası:", authErr);
    if (errorEl) {{
      errorEl.textContent = '⚠️ Hatalı şifre! Lütfen BES 339 ders izlencesindeki şifrenizi kontrol ediniz.';
      errorEl.style.display = 'block';
    }}
    if (modalCard) {{
      modalCard.classList.remove('modal-shake');
      void modalCard.offsetWidth;
      modalCard.classList.add('modal-shake');
    }}
    if (input) {{
      input.focus();
      input.select();
    }}
    if (submitBtn) {{
      submitBtn.disabled = false;
      submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
    }}
    return;
  }}

  try {{
    const lockedList = JSON.parse(decryptedJson);
    applyDecryptedEvrimSlides(lockedList);
    try {{
      localStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJson);
    }} catch(e) {{}}
    closeLockModal();
    
    if (pendingTargetSlide !== null && pendingTargetSlide !== undefined) {{
      const target = pendingTargetSlide;
      pendingTargetSlide = null;
      goToSlide(target);
    }} else {{
      goToSlide(PUBLIC_SLIDE_COUNT);
    }}
  }} catch(renderErr) {{
    console.error("Slayt yükleme hatası:", renderErr);
    if (errorEl) {{
      errorEl.textContent = '⚠️ İçerik çözüldü fakat eklenirken hata oluştu: ' + renderErr.message;
      errorEl.style.display = 'block';
    }}
  }} finally {{
    if (submitBtn) {{
      submitBtn.disabled = false;
      submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
    }}
  }}
}}

function checkSessionUnlock() {{
  try {{
    const cached = localStorage.getItem('unlocked_pres_' + PRES_ID);
    if (cached) {{
      const lockedList = JSON.parse(cached);
      applyDecryptedEvrimSlides(lockedList);
    }}
  }} catch(e) {{ console.error("Cache okunamadı:", e); }}
}}

function applyDecryptedEvrimSlides(lockedList) {{
  if (isUnlocked) return;
  isUnlocked = true;
  if (SLIDES.length <= PUBLIC_SLIDE_COUNT) {{
    lockedList.forEach(s => SLIDES.push(s));
  }}
  totalSlides = SLIDES.length;
  document.getElementById('counter-total').innerText = String(totalSlides);
  buildOverviewGrid();
  renderSlide();
}}

function openLockModal(targetSlide) {{
  if (isUnlocked) return;
  if (targetSlide !== undefined) pendingTargetSlide = targetSlide;
  const m = document.getElementById('student-lock-modal');
  if (m) {{
    m.style.display = 'flex';
    setTimeout(() => {{
      const inp = document.getElementById('student-password-input');
      if (inp) inp.focus();
    }}, 80);
  }}
}}

function closeLockModal() {{
  const m = document.getElementById('student-lock-modal');
  if (m) m.style.display = 'none';
  const err = document.getElementById('unlock-error-msg');
  if (err) err.style.display = 'none';
}}

function togglePasswordVisibility() {{
  const inp = document.getElementById('student-password-input');
  if (inp) inp.type = inp.type === 'password' ? 'text' : 'password';
}}
</script>
"""

# Append before </body>
body_close_pos = new_html.rfind("</body>")
if body_close_pos != -1:
    final_html = new_html[:body_close_pos] + client_lock_script + "\n" + new_html[body_close_pos:]
else:
    final_html = new_html + client_lock_script

# Write to both target files
with open(TARGET_HTML_1, "w", encoding="utf-8") as f:
    f.write(final_html)
print(f"✅ Yazıldı: {TARGET_HTML_1} ({len(final_html)} bayt)")

with open(TARGET_HTML_2, "w", encoding="utf-8") as f:
    f.write(final_html)
print(f"✅ Yazıldı: {TARGET_HTML_2} ({len(final_html)} bayt)")
print("✨ Beslenmenin Evrimi şifrelendi ve başarıyla paketlendi!")
