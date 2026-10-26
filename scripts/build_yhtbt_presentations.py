#!/usr/bin/env python3
"""
BES 317 Sunumlarını Şifreleme, Entegre Etme ve Yayınlama Motoru
Dr. Caner ÖZYILDIRIM — Kişisel Web Sitesi Altyapısı
"""

import os
import sys
import re
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("/Users/canerozyildirim/Sites/personalwebsite").resolve()
SLIDES_DIR = BASE_DIR / "slides"
ASSETS_DIR = SLIDES_DIR / "assets"
PDF_DIR = SLIDES_DIR / "pdf"
CONTENT_DIR = BASE_DIR / "content"
VAULT_DIR = Path("/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner/Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/Sunumlar")

PASSWORD = "COZYYHTBT2026_"

def encrypt_aes_payload(plaintext: str, password: str) -> str:
    node_script = """
const fs = require('fs');
const CryptoJS = require('crypto-js');
const rawInput = fs.readFileSync(0, 'utf8');
const input = JSON.parse(rawInput);
const ciphertext = CryptoJS.AES.encrypt(input.plaintext, input.password).toString();
console.log(ciphertext);
"""
    payload = {"plaintext": plaintext, "password": password}
    res = subprocess.run(
        ["node", "-e", node_script],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        check=True
    )
    return res.stdout.strip()

# Read minified crypto-js
crypto_js_file = ASSETS_DIR / "crypto-js.min.js"
if not crypto_js_file.exists():
    local_cjs = BASE_DIR / "node_modules/crypto-js/crypto-js.js"
    if local_cjs.exists():
        shutil.copy2(local_cjs, crypto_js_file)
with open(crypto_js_file, "r", encoding="utf-8") as f:
    CRYPTO_JS_CODE = f.read()

LOCK_MODAL_HTML = """
<!-- STUDENT PASSWORD LOCK MODAL -->
<div id="student-lock-modal" style="display:none; position:fixed; inset:0; background:rgba(11,17,29,0.88); backdrop-filter:blur(10px); z-index:99999; align-items:center; justify-content:center; padding:20px; font-family:'Inter', system-ui, sans-serif;">
  <div id="modal-card" style="background:#131d2e; border:1px solid #233554; border-radius:24px; max-width:440px; width:100%; padding:32px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.6); text-align:center; position:relative; color:#f8fafc;">
    <button onclick="closeLockModal()" style="position:absolute; top:16px; right:16px; background:none; border:none; color:#94a3b8; font-size:20px; cursor:pointer; padding:4px 8px; border-radius:8px;">✕</button>
    <div style="width:64px; height:64px; border-radius:18px; background:rgba(217,119,6,0.15); border:1px solid rgba(217,119,6,0.3); color:#fbbf24; display:flex; align-items:center; justify-content:center; font-size:26px; margin:0 auto 16px;">🔒</div>
    <h3 style="font-size:20px; font-weight:700; margin:0 0 8px; color:#ffffff;">Öğrenci Kilit Ekranı</h3>
    <p style="font-size:13px; color:#94a3b8; line-height:1.6; margin:0 0 24px;">10 slaytlık önizleme tamamlanmıştır. Devamını görüntülemek ve ders notlarını indirmek için lütfen BES 317 ders şifrenizi giriniz.</p>
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
        ⚠️ Hatalı şifre! Lütfen ders izlencesindeki şifrenizi kontrol ediniz.
      </div>
      <button type="submit" id="unlock-submit-btn" style="width:100%; background:linear-gradient(135deg, #d97706, #b45309); color:#ffffff; font-weight:700; border:none; border-radius:12px; padding:14px; font-size:14px; cursor:pointer; box-shadow:0 10px 15px -3px rgba(217,119,6,0.3); transition:transform 0.1s;">
        🔓 Şifreyi Çöz & Derse Devam Et
      </button>
    </form>
    <div style="margin-top:20px; padding-top:16px; border-top:1px solid #1e293b; font-size:11px; color:#64748b; display:flex; align-items:center; justify-content:center; gap:6px;">
      <span>🔒</span> <span>Ders İzlencesi ve OBS Şifresi (BES 317)</span>
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

SHARED_CRYPTO_JS_METHODS = """
function getPasswordCandidates(inputStr) {
  const p = (inputStr || '').trim();
  if (!p) return [];
  const set = new Set();
  set.add(p);
  set.add(p.toUpperCase());
  set.add(p.toLowerCase());
  set.add(p.toLocaleUpperCase('en-US'));
  set.add(p.toLocaleUpperCase('tr-TR'));
  if (!p.endsWith('_')) {
    set.add(p + '_');
    set.add(p.toUpperCase() + '_');
    set.add(p.toLocaleUpperCase('en-US') + '_');
  } else {
    const withoutUnderscore = p.replace(/_+$/, '');
    set.add(withoutUnderscore);
    set.add(withoutUnderscore.toUpperCase());
    set.add(withoutUnderscore.toLocaleUpperCase('en-US'));
  }
  return Array.from(set);
}

function decryptPayload(ciphertext, passwordInput) {
  const candidates = getPasswordCandidates(passwordInput);
  for (const cand of candidates) {
    try {
      const bytes = CryptoJS.AES.decrypt(ciphertext, cand);
      const dec = bytes.toString(CryptoJS.enc.Utf8);
      if (dec && dec.length > 0) return dec;
    } catch(e) {}
  }
  throw new Error("Şifre çözülemedi.");
}

function togglePasswordVisibility() {
  const inp = document.getElementById('student-password-input');
  if (inp) inp.type = inp.type === 'password' ? 'text' : 'password';
}

function closeLockModal() {
  const m = document.getElementById('student-lock-modal');
  if (m) m.style.display = 'none';
  const err = document.getElementById('unlock-error-msg');
  if (err) err.style.display = 'none';
}
"""

def build_konu1():
    print("\n--- 1. Konu: Obezite ve Tıbbi Beslenme Tedavisi İşleniyor ---")
    src = VAULT_DIR / "Konu1_Obezite_Sunum.html"
    out = SLIDES_DIR / "01-obezite-ve-tibbi-beslenme-tedavisi.html"

    with open(src, "r", encoding="utf-8") as f:
        html = f.read()

    # Normalize relative assets
    html = html.replace('../../../Files/Saglik-Bilimleri-Fakultesi-2.png', 'assets/Saglik-Bilimleri-Fakultesi-2.png')

    # Ensure presentation engine and html2pdf scripts are in head
    if "assets/presentation-engine.js" not in html:
        head_inject = """<script src="assets/html2pdf.bundle.min.js"></script>\n<script src="assets/presentation-engine.js"></script>\n"""
        html = html.replace("<head>", "<head>\n" + head_inject, 1)

    # HTTPS redirect
    if "location.protocol==='http:'" not in html:
        https_redir = """<script>if(location.protocol==='http:'&&location.hostname!=='localhost'&&location.hostname!=='127.0.0.1'){location.replace('https:'+location.href.substring(5));}</script>\n"""
        html = html.replace("<head>", "<head>\n" + https_redir, 1)

    # Extract SLIDES
    pos = html.rfind('const SLIDES = [')
    sub = html[pos + len('const SLIDES = ['):]
    end_pos = sub.find('];\n')
    if end_pos == -1: end_pos = sub.find('];')
    slides_data = json.loads('[' + sub[:end_pos] + ']')

    total_slides = len(slides_data)
    public_count = 10
    print(f"  Toplam Slayt: {total_slides} | Açık Önizleme: {public_count} | Kilitli: {total_slides - public_count}")

    public_slides = slides_data[:public_count]
    locked_slides = slides_data[public_count:]

    # Public slide 10 barrier note
    public_slides[9] = {
        "type": "prompt",
        "sec": 0,
        "tag": "🛑 Önizleme Sonu (Slayt 10)",
        "q": "10 slaytlık önizleme tamamlanmıştır.",
        "note": "Devamını görüntülemek ve ders notlarını indirmek için ders şifresi girilmesi gerekmektedir."
    }

    # Encrypt locked slides
    ciphertext = encrypt_aes_payload(json.dumps(locked_slides, ensure_ascii=False), PASSWORD)

    new_public_slides_str = json.dumps(public_slides, indent=2, ensure_ascii=False)
    new_html = html[:pos + len('const SLIDES = ')] + new_public_slides_str + html[pos + len('const SLIDES = [') + end_pos + 1:]

    # Patch topBar PDF button to trigger presentation engine
    new_html = re.sub(
        r'<button id="header-pdf-btn"[^>]*>.*?</button>',
        """<button id="header-pdf-btn" onclick="triggerPresentationPdfDownload()" title="Sunumu PDF Ders Notu Olarak İndir" style="padding:6px 12px; font-size:12px; font-weight:700; display:inline-flex; align-items:center; gap:6px; background:var(--surface); border:1px solid rgba(255,255,255,0.15); color:var(--cream); cursor:pointer; border-radius:8px; transition:all 0.15s ease;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          <span class="hidden sm:inline">PDF İndir</span>
        </button>""",
        new_html,
        flags=re.DOTALL
    )

    # Patch cover slide buttons in renderSlide
    cover_buttons_replacement = """
    if(s.type === 'cover') {
      const coverActions = '<div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-top:22px; flex-wrap:wrap;">' +
        '<button type="button" onclick="openLockModal()" class="cover-lock-btn" style="padding:10px 20px; font-size:13px; font-weight:700; border-radius:10px; background:var(--accent); color:#fff; border:none; cursor:pointer; box-shadow:var(--shadow); display:inline-flex; align-items:center; gap:6px;">🔒 Ders Şifresini Gir &amp; Tüm Sunumu Aç</button>' +
        '<button type="button" onclick="triggerPresentationPdfDownload(\\'4lu\\')" class="pdf-download-btn" style="padding:10px 18px; font-size:13px; font-weight:700; border-radius:10px; background:var(--surface); color:var(--cream); border:1px solid rgba(56,189,248,0.4); cursor:pointer; box-shadow:var(--shadow); display:inline-flex; align-items:center; gap:6px;">📑 Ders Notları (4\\'lü PDF)</button>' +
        '<button type="button" onclick="triggerPresentationPdfDownload(\\'6li\\')" class="pdf-download-btn" style="padding:10px 18px; font-size:13px; font-weight:700; border-radius:10px; background:var(--surface); color:var(--cream); border:1px solid rgba(52,211,153,0.4); cursor:pointer; box-shadow:var(--shadow); display:inline-flex; align-items:center; gap:6px;">📚 Ders Notları (6\\'lı PDF)</button>' +
        '</div>';
      return '<div class="slide cover active">' +
        '<div class="brand-line" style="justify-content:center; margin-bottom:18px;"><div class="brand-dot"></div><div class="brand-text">' + (s.kicker||'') + '</div></div>' +
        '<h1 class="cover-title">' + (s.title||'').replace(/\\n/g, '<br>') + '</h1>' +
        '<p class="cover-sub">' + (s.sub||'') + '</p>' +
        '<div class="cover-byline">' + (s.byline||'') + '</div>' +
        coverActions +
        '</div>';
    }
    """
    new_html = re.sub(
        r"if\(s\.type === 'cover'\) \{[\s\S]*?return '<div class=\"slide cover active\">' \+[\s\S]*?'</div>';\s*\}",
        cover_buttons_replacement.strip(),
        new_html
    )

    # Patch DOM loop and lock globals
    new_html = new_html.replace('const allSlideEls = Array.from(stage.children);', 'let allSlideEls = Array.from(stage.children);')
    new_html = new_html.replace('const total = SLIDES.length;', 'let total = SLIDES.length;')

    lock_globals = f"""/* ===== LOCK ENGINE GLOBALS ===== */
var PUBLIC_SLIDE_COUNT = {public_count};
var isUnlocked = false;
var pendingTargetSlide = null;
var encryptedPayloadCiphertext = "";
/* ================================ */
"""
    go_anchor = "function go(idx){"
    if go_anchor in new_html:
        new_html = new_html.replace(go_anchor, lock_globals + "\n" + go_anchor, 1)

    go_orig = "function go(idx){\n  if(idx<0||idx>=total) return;\n  if(allSlideEls[current]) allSlideEls[current].classList.remove('active');"
    go_patched = """function go(idx){
  if(idx >= PUBLIC_SLIDE_COUNT && !isUnlocked){
    openLockModal(idx);
    return;
  }
  if(idx<0||idx>=total) return;
  if(allSlideEls[current] && current !== idx) allSlideEls[current].classList.remove('active');"""
    new_html = new_html.replace(go_orig, go_patched)

    new_html = new_html.replace(
        "// Initialize on slide 0\ngo(0);",
        "// go(0) is called by the lock engine DOMContentLoaded handler"
    )

    client_engine = f"""
<!-- INLINED ZERO-DEPENDENCY CRYPTOJS ENGINE -->
<script>
{CRYPTO_JS_CODE}
</script>

<!-- AES-256 ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data" type="text/plain">
{ciphertext}
</script>

{LOCK_MODAL_HTML}

<script>
/* ================= STUDENT LOCK & CRYPTOJS DECRYPTION ENGINE ================= */
var PRES_ID = "konu1_obezite_tedavisi_v3";
var TOTAL_SLIDES_COUNT = {total_slides};

document.addEventListener('DOMContentLoaded', () => {{
  const scriptTag = document.getElementById('encrypted-payload-data');
  if(scriptTag) {{
    encryptedPayloadCiphertext = scriptTag.textContent.trim();
  }}
  checkSessionUnlock();
  go(0);
}});

{SHARED_CRYPTO_JS_METHODS}

async function handleUnlockSubmit(e) {{
  e.preventDefault();
  const input = document.getElementById('student-password-input');
  const password = input.value.trim();
  const errorEl = document.getElementById('unlock-error-msg');
  const submitBtn = document.getElementById('unlock-submit-btn');
  const modalCard = document.getElementById('modal-card');

  if (!password) return;
  submitBtn.disabled = true;
  submitBtn.innerHTML = '⏳ Şifre Çözülüyor...';
  errorEl.style.display = 'none';

  let decryptedJson = null;
  try {{
    decryptedJson = decryptPayload(encryptedPayloadCiphertext, password);
  }} catch(authErr) {{
    console.error("Şifre çözme hatası:", authErr);
    errorEl.textContent = '⚠️ Hatalı şifre! Lütfen ders izlencesindeki şifrenizi kontrol ediniz.';
    errorEl.style.display = 'block';
    modalCard.classList.remove('modal-shake');
    void modalCard.offsetWidth;
    modalCard.classList.add('modal-shake');
    input.focus();
    input.select();
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
    return;
  }}

  try {{
    const lockedList = JSON.parse(decryptedJson);
    applyDecryptedSlides(lockedList);
    sessionStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJson);
    isUnlocked = true;
    closeLockModal();
    
    if (typeof updateGlobalLockUI === 'function') updateGlobalLockUI();
    if (window.pendingDownloadPdf) {{
      window.pendingDownloadPdf = false;
      const layout = window.pendingPdfLayout || null;
      setTimeout(() => triggerPresentationPdfDownload(layout), 350);
    }}

    if (pendingTargetSlide !== null && pendingTargetSlide !== undefined) {{
      const target = pendingTargetSlide;
      pendingTargetSlide = null;
      go(target);
    }} else {{
      go(PUBLIC_SLIDE_COUNT);
    }}
  }} catch(renderErr) {{
    console.error("Slayt yükleme hatası:", renderErr);
    errorEl.textContent = '⚠️ İçerik çözüldü fakat eklenirken hata oluştu: ' + renderErr.message;
    errorEl.style.display = 'block';
  }} finally {{
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
  }}
}}

function checkSessionUnlock() {{
  const cached = sessionStorage.getItem('unlocked_pres_' + PRES_ID);
  if (cached) {{
    try {{
      const lockedList = JSON.parse(cached);
      applyDecryptedSlides(lockedList);
      isUnlocked = true;
      if (typeof updateGlobalLockUI === 'function') updateGlobalLockUI();
    }} catch(e) {{ console.error("Cache okunamadı:", e); }}
  }}
}}

function applyDecryptedSlides(lockedList) {{
  if (isUnlocked) return;
  const stage = document.getElementById('stage');
  lockedList.forEach((s, i) => {{
    const idx = PUBLIC_SLIDE_COUNT + i;
    SLIDES.push(s);
    const wrap = document.createElement('div');
    wrap.innerHTML = renderSlide(s, idx);
    if(wrap.firstElementChild) {{
      stage.appendChild(wrap.firstElementChild);
    }} else {{
      const fallback = document.createElement('div');
      fallback.className = 'slide';
      fallback.innerHTML = eyebrowTitle(s) + '<div class="slide-sub">' + (s.note || '') + '</div>';
      stage.appendChild(fallback);
    }}
  }});
  allSlideEls = Array.from(stage.children);
  total = SLIDES.length;
  isUnlocked = true;
  
  chartQueue.forEach(spec=>{{
    const canvas = document.getElementById(spec.id);
    if(canvas){{ try{{ spec.build(canvas.getContext('2d')); }}catch(e){{}} }}
  }});
  if(window.MathJax && window.MathJax.typesetPromise) window.MathJax.typesetPromise();
  update();
}}

function openLockModal(targetSlide, forPdf) {{
  if (forPdf) window.pendingDownloadPdf = true;
  if (isUnlocked) {{
    if (window.pendingDownloadPdf) {{
      window.pendingDownloadPdf = false;
      const layout = window.pendingPdfLayout || null;
      triggerPresentationPdfDownload(layout);
    }}
    return;
  }}
  if (targetSlide !== undefined && targetSlide !== null) pendingTargetSlide = targetSlide;
  const m = document.getElementById('student-lock-modal');
  if (m) {{
    m.style.display = 'flex';
    setTimeout(() => {{
      const inp = document.getElementById('student-password-input');
      if (inp) inp.focus();
    }}, 80);
  }}
}}
</script>
"""
    new_html = new_html.replace('</body>', f'{client_engine}\n</body>')

    with open(out, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ 01-obezite-ve-tibbi-beslenme-tedavisi.html üretildi ({out.stat().st_size / 1024:.1f} KB)")


def build_konu2():
    print("\n--- 2. Konu: Diyabet ve Tıbbi Beslenme Tedavisi İşleniyor ---")
    src = VAULT_DIR / "Konu2_Diyabet_Sunum.html"
    out = SLIDES_DIR / "03-diyabet-ve-tibbi-beslenme-tedavisi.html"

    with open(src, "r", encoding="utf-8") as f:
        html = f.read()

    # Normalize relative assets
    html = html.replace('../../../Files/Saglik-Bilimleri-Fakultesi-2.png', 'assets/Saglik-Bilimleri-Fakultesi-2.png')

    # Ensure presentation engine and html2pdf scripts are in head
    if "assets/presentation-engine.js" not in html:
        head_inject = """<script src="assets/html2pdf.bundle.min.js"></script>\n<script src="assets/presentation-engine.js"></script>\n"""
        html = html.replace("<head>", "<head>\n" + head_inject, 1)

    # HTTPS redirect
    if "location.protocol==='http:'" not in html:
        https_redir = """<script>if(location.protocol==='http:'&&location.hostname!=='localhost'&&location.hostname!=='127.0.0.1'){location.replace('https:'+location.href.substring(5));}</script>\n"""
        html = html.replace("<head>", "<head>\n" + https_redir, 1)

    # Extract SLIDES
    pos = html.rfind('const SLIDES = [')
    sub = html[pos + len('const SLIDES = ['):]
    end_pos = sub.find('];\n')
    if end_pos == -1: end_pos = sub.find('];')
    slides_data = json.loads('[' + sub[:end_pos] + ']')

    total_slides = len(slides_data)
    public_count = 10
    print(f"  Toplam Slayt: {total_slides} | Açık Önizleme: {public_count} | Kilitli: {total_slides - public_count}")

    public_slides = slides_data[:public_count]
    locked_slides = slides_data[public_count:]

    # Barrier slide at index 10
    barrier_slide = {
        "type": "prompt",
        "tag": "🛑 Önizleme Sınırı (Slayt 10)",
        "q": "10 slaytlık açık önizleme tamamlanmıştır.",
        "note": "Devamını görüntülemek ve ders notlarını indirmek için ders şifresi girilmesi gerekmektedir."
    }
    public_slides_with_barrier = public_slides + [barrier_slide]

    # Encrypt locked slides
    ciphertext = encrypt_aes_payload(json.dumps(locked_slides, ensure_ascii=False), PASSWORD)

    new_public_slides_str = json.dumps(public_slides_with_barrier, indent=2, ensure_ascii=False)
    new_html = html[:pos + len('const SLIDES = ')] + new_public_slides_str + html[pos + len('const SLIDES = [') + end_pos + 1:]

    # Patch topBar PDF button to trigger presentation engine
    new_html = re.sub(
        r'<button id="header-pdf-btn"[^>]*>.*?</button>',
        """<button id="header-pdf-btn" onclick="triggerPresentationPdfDownload()" title="Sunumu PDF Ders Notu Olarak İndir" style="padding:6px 14px; font-size:12px; font-weight:700; display:inline-flex; align-items:center; gap:6px; background:var(--surface); border:1px solid var(--border); color:var(--ink); cursor:pointer; border-radius:8px; transition:all 0.15s ease; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          <span class="hidden sm:inline">PDF İndir</span>
        </button>""",
        new_html,
        flags=re.DOTALL
    )

    # Patch cover slide buttons in renderSlide
    cover_buttons_replacement = """
    if (s.type === 'cover') {
      const coverActions = '<div style="display:flex; align-items:center; justify-content:center; gap:12px; margin-top:28px; flex-wrap:wrap;">' +
        '<button type="button" onclick="openLockModal()" class="cover-lock-btn" style="padding:12px 26px; font-size:14px; font-weight:700; border-radius:10px; background:linear-gradient(135deg, #1A73E8, #1557b0); color:#fff; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(26,115,232,0.3); display:inline-flex; align-items:center; gap:8px;">🔒 Ders Şifresini Gir &amp; Tüm Sunumu Aç</button>' +
        '<button type="button" onclick="triggerPresentationPdfDownload(\\'4lu\\')" class="pdf-download-btn" style="padding:12px 20px; font-size:13px; font-weight:700; border-radius:10px; background:var(--surface); color:var(--ink); border:1px solid rgba(56,189,248,0.5); cursor:pointer; box-shadow:0 2px 6px rgba(0,0,0,0.04); display:inline-flex; align-items:center; gap:8px;">📑 Ders Notları (4\\'lü PDF)</button>' +
        '<button type="button" onclick="triggerPresentationPdfDownload(\\'6li\\')" class="pdf-download-btn" style="padding:12px 20px; font-size:13px; font-weight:700; border-radius:10px; background:var(--surface); color:var(--ink); border:1px solid rgba(52,211,153,0.5); cursor:pointer; box-shadow:0 2px 6px rgba(0,0,0,0.04); display:inline-flex; align-items:center; gap:8px;">📚 Ders Notları (6\\'lı PDF)</button>' +
        '</div>';
      return '<div class="slide cover active">' +
        '<div class="brand-line"><div class="brand-dot"></div><div class="brand-text">Yetişkin Hastalıklarında Beslenme Tedavisi · Konu 2</div></div>' +
        '<h1 class="cover-title">' + s.title + '</h1>' +
        '<p class="cover-sub">' + (s.sub || '') + '</p>' +
        '<div class="cover-byline">' + (s.byline || 'Arş. Gör. Dr. Caner Özyıldırım') + '</div>' +
        coverActions +
        '</div>';
    }
    """
    new_html = re.sub(
        r"if \(s\.type === 'cover'\) \{[\s\S]*?return '<div class=\"slide cover active\">' \+[\s\S]*?'</div>';\s*\}",
        cover_buttons_replacement.strip(),
        new_html
    )

    # Patch go(idx) for lock
    lock_globals = f"""/* ===== LOCK ENGINE GLOBALS ===== */
var PUBLIC_SLIDE_COUNT = {public_count};
var isUnlocked = false;
var pendingTargetSlide = null;
var encryptedPayloadCiphertext = "";
/* ================================ */
"""
    go_anchor = "function go(idx){"
    if go_anchor in new_html:
        new_html = new_html.replace(go_anchor, lock_globals + "\n" + go_anchor, 1)

    go_orig = "function go(idx){\n  if(idx<0||idx>=total) return;\n  current = idx;"
    go_patched = """function go(idx){
  if(idx >= PUBLIC_SLIDE_COUNT && !isUnlocked){
    openLockModal(idx);
    return;
  }
  if(idx<0||idx>=total) return;
  current = idx;"""
    new_html = new_html.replace(go_orig, go_patched)

    client_engine = f"""
<!-- INLINED ZERO-DEPENDENCY CRYPTOJS ENGINE -->
<script>
{CRYPTO_JS_CODE}
</script>

<!-- AES-256 ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data" type="text/plain">
{ciphertext}
</script>

{LOCK_MODAL_HTML}

<script>
/* ================= STUDENT LOCK & CRYPTOJS DECRYPTION ENGINE ================= */
var PRES_ID = "konu2_diyabet_tedavisi_v3";
var TOTAL_SLIDES_COUNT = {total_slides};

document.addEventListener('DOMContentLoaded', () => {{
  const scriptTag = document.getElementById('encrypted-payload-data');
  if(scriptTag) {{
    encryptedPayloadCiphertext = scriptTag.textContent.trim();
  }}
  checkSessionUnlock();
  go(0);
}});

{SHARED_CRYPTO_JS_METHODS}

async function handleUnlockSubmit(e) {{
  e.preventDefault();
  const input = document.getElementById('student-password-input');
  const password = input.value.trim();
  const errorEl = document.getElementById('unlock-error-msg');
  const submitBtn = document.getElementById('unlock-submit-btn');
  const modalCard = document.getElementById('modal-card');

  if (!password) return;
  submitBtn.disabled = true;
  submitBtn.innerHTML = '⏳ Şifre Çözülüyor...';
  errorEl.style.display = 'none';

  let decryptedJson = null;
  try {{
    decryptedJson = decryptPayload(encryptedPayloadCiphertext, password);
  }} catch(authErr) {{
    console.error("Şifre çözme hatası:", authErr);
    errorEl.textContent = '⚠️ Hatalı şifre! Lütfen ders izlencesindeki şifrenizi kontrol ediniz.';
    errorEl.style.display = 'block';
    modalCard.classList.remove('modal-shake');
    void modalCard.offsetWidth;
    modalCard.classList.add('modal-shake');
    input.focus();
    input.select();
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
    return;
  }}

  try {{
    const lockedList = JSON.parse(decryptedJson);
    applyDecryptedSlides(lockedList);
    sessionStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJson);
    isUnlocked = true;
    closeLockModal();
    
    if (typeof updateGlobalLockUI === 'function') updateGlobalLockUI();
    if (window.pendingDownloadPdf) {{
      window.pendingDownloadPdf = false;
      const layout = window.pendingPdfLayout || null;
      setTimeout(() => triggerPresentationPdfDownload(layout), 350);
    }}

    if (pendingTargetSlide !== null && pendingTargetSlide !== undefined) {{
      const target = pendingTargetSlide;
      pendingTargetSlide = null;
      go(target);
    }} else {{
      go(PUBLIC_SLIDE_COUNT);
    }}
  }} catch(renderErr) {{
    console.error("Slayt yükleme hatası:", renderErr);
    errorEl.textContent = '⚠️ İçerik çözüldü fakat eklenirken hata oluştu: ' + renderErr.message;
    errorEl.style.display = 'block';
  }} finally {{
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
  }}
}}

function checkSessionUnlock() {{
  const cached = sessionStorage.getItem('unlocked_pres_' + PRES_ID);
  if (cached) {{
    try {{
      const lockedList = JSON.parse(cached);
      applyDecryptedSlides(lockedList);
      isUnlocked = true;
      if (typeof updateGlobalLockUI === 'function') updateGlobalLockUI();
    }} catch(e) {{ console.error("Cache okunamadı:", e); }}
  }}
}}

function applyDecryptedSlides(lockedList) {{
  if (isUnlocked) return;
  isUnlocked = true;
  window.isUnlocked = true;

  // 1. Remove preview barrier slide at index 10
  if (SLIDES.length > 10 && SLIDES[10].type === 'prompt' && SLIDES[10].tag && SLIDES[10].tag.includes('Önizleme')) {{
    SLIDES.splice(10, 1);
  }}

  // 2. Append locked slides
  lockedList.forEach(s => SLIDES.push(s));
  total = SLIDES.length;

  // 3. Re-render
  go(current >= 10 ? current : 10);
  if (typeof updateGlobalLockUI === 'function') updateGlobalLockUI();
}}

function openLockModal(targetSlide, forPdf) {{
  if (forPdf) window.pendingDownloadPdf = true;
  if (isUnlocked) {{
    if (window.pendingDownloadPdf) {{
      window.pendingDownloadPdf = false;
      const layout = window.pendingPdfLayout || null;
      triggerPresentationPdfDownload(layout);
    }}
    return;
  }}
  if (targetSlide !== undefined && targetSlide !== null) pendingTargetSlide = targetSlide;
  const m = document.getElementById('student-lock-modal');
  if (m) {{
    m.style.display = 'flex';
    setTimeout(() => {{
      const inp = document.getElementById('student-password-input');
      if (inp) inp.focus();
    }}, 80);
  }}
}}
</script>
"""
    new_html = new_html.replace('</body>', f'{client_engine}\n</body>')

    with open(out, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ 03-diyabet-ve-tibbi-beslenme-tedavisi.html üretildi ({out.stat().st_size / 1024:.1f} KB)")


def build_konu3():
    print("\n--- 3. Konu: KVH, Hipertansiyon ve Tıbbi Beslenme Tedavisi İşleniyor ---")
    src = VAULT_DIR / "Konu3_KVH_HT_Sunum.html"
    out = SLIDES_DIR / "04-kardiyovaskuler-hastaliklar-ve-hipertansiyon.html"

    with open(src, "r", encoding="utf-8") as f:
        html = f.read()

    # Ensure presentation engine and html2pdf scripts are in head
    if "assets/presentation-engine.js" not in html:
        head_inject = """<script src="assets/html2pdf.bundle.min.js"></script>\n<script src="assets/presentation-engine.js"></script>\n"""
        html = html.replace("<head>", "<head>\n" + head_inject, 1)

    # HTTPS redirect
    if "location.protocol==='http:'" not in html:
        https_redir = """<script>if(location.protocol==='http:'&&location.hostname!=='localhost'&&location.hostname!=='127.0.0.1'){location.replace('https:'+location.href.substring(5));}</script>\n"""
        html = html.replace("<head>", "<head>\n" + https_redir, 1)

    # Extract all 135 slides from SLIDES.push(...)
    pushes_raw = re.findall(r'SLIDES\.push\(([\s\S]*?)\);\s*\n', html)
    slides_data = [json.loads(p) for p in pushes_raw]

    total_slides = len(slides_data)
    public_count = 10
    print(f"  Toplam Slayt: {total_slides} | Açık Önizleme: {public_count} | Kilitli: {total_slides - public_count}")

    public_slides = slides_data[:public_count]
    locked_slides = slides_data[public_count:]

    # Barrier slide at index 10
    barrier_slide = {
        "type": "prompt",
        "ch": "00",
        "tag": "🛑 Önizleme Sınırı (Slayt 10)",
        "title": "10 Slaytlık Açık Önizleme Sınırı",
        "body": "<p style='font-size:16px; color:var(--ink-soft); line-height:1.6;'>Kardiyovasküler hastalıklar, koroner arter hastalığı, kalp yetersizliği, hipertansiyon ve kanıta dayalı diyet modellerini (DASH, Akdeniz, Portföy) içeren devam modülleri <b>AES-256</b> şifresiyle korunmaktadır.</p>",
        "box": {
            "type": "info",
            "title": "Öğrenci Kilit Ekranı",
            "text": "Sunumun devamını incelemek veya ders notlarını PDF olarak indirmek için lütfen ders şifrenizi giriniz."
        }
    }
    public_slides_with_barrier = public_slides + [barrier_slide]

    # Encrypt locked slides
    ciphertext = encrypt_aes_payload(json.dumps(locked_slides, ensure_ascii=False), PASSWORD)

    # Replace the SLIDES definition block in HTML
    first_push_pos = html.find('const SLIDES = [];')
    last_push_m = list(re.finditer(r'SLIDES\.push\([\s\S]*?\);\s*\n', html))
    last_push_end = last_push_m[-1].end()

    new_slides_js = "const SLIDES = [];\n" + "\n".join([f"SLIDES.push({json.dumps(s, ensure_ascii=False)});" for s in public_slides_with_barrier]) + "\n"
    new_html = html[:first_push_pos] + new_slides_js + html[last_push_end:]

    # Update topBar to add PDF and Lock buttons
    topbar_buttons = """
    <div style="display:flex; align-items:center; gap:8px;">
      <button id="header-pdf-btn" onclick="triggerPresentationPdfDownload()" title="Sunumu PDF Ders Notu Olarak İndir" class="nav-btn" style="display:inline-flex; align-items:center; gap:6px; cursor:pointer;">
        <span>📄</span> <span class="hidden sm:inline">PDF İndir</span>
      </button>
      <button id="header-lock-btn" onclick="openLockModal()" title="Ders şifresini gir ve tüm sunumu aç" class="nav-btn" style="display:inline-flex; align-items:center; gap:6px; background:rgba(217,119,6,0.15); border:1px solid rgba(217,119,6,0.3); color:#d97706; cursor:pointer;">
        <span>🔒</span> <span class="hidden sm:inline">Ders Şifresi</span>
      </button>
    </div>
"""
    new_html = new_html.replace(
        '<button class="nav-btn" id="btn-prev" title="Önceki Slayt (Sol Ok)">← Önceki</button>',
        topbar_buttons + '\n    <button class="nav-btn" id="btn-prev" title="Önceki Slayt (Sol Ok)">← Önceki</button>'
    )

    # Patch cover slide in renderSlide
    cover_buttons_replacement = """
    return '<div class="cover-card">' +
      '<div class="cover-badge"><div class="badge-dot"></div><span>' + kicker + '</span></div>' +
      '<h1 class="cover-title">' + s.title + '</h1>' +
      (s.subtitle ? '<p class="cover-sub">' + s.subtitle + '</p>' : '') +
      '<div class="cover-meta">' + metaHtml + '</div>' +
      '<div style="display:flex; align-items:center; justify-content:center; gap:12px; margin-top:32px; flex-wrap:wrap;">' +
      '<button type="button" onclick="openLockModal()" class="cover-lock-btn" style="padding:12px 24px; font-size:14px; font-weight:700; border-radius:10px; background:linear-gradient(135deg, #d97706, #b45309); color:#fff; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(217,119,6,0.3); display:inline-flex; align-items:center; gap:8px;">🔒 Ders Şifresini Gir &amp; Tüm Sunumu Aç</button>' +
      '<button type="button" onclick="triggerPresentationPdfDownload(\\'4lu\\')" class="pdf-download-btn" style="padding:12px 20px; font-size:13px; font-weight:700; border-radius:10px; background:var(--surface); color:var(--ink); border:1px solid rgba(56,189,248,0.5); cursor:pointer; box-shadow:0 2px 6px rgba(0,0,0,0.04); display:inline-flex; align-items:center; gap:8px;">📑 Ders Notları (4\\'lü PDF)</button>' +
      '<button type="button" onclick="triggerPresentationPdfDownload(\\'6li\\')" class="pdf-download-btn" style="padding:12px 20px; font-size:13px; font-weight:700; border-radius:10px; background:var(--surface); color:var(--ink); border:1px solid rgba(52,211,153,0.5); cursor:pointer; box-shadow:0 2px 6px rgba(0,0,0,0.04); display:inline-flex; align-items:center; gap:8px;">📚 Ders Notları (6\\'lı PDF)</button>' +
      '</div>' +
      '</div>';
"""
    new_html = re.sub(
        r"return '<div class=\"cover-card\">' \+[\s\S]*?'</div>';\s*\}",
        cover_buttons_replacement.strip() + "\n  }",
        new_html
    )

    # Patch showSlide(i) for lock guard
    show_slide_orig = "function showSlide(i){\n  if(i<0 || i>=SLIDES.length) return;"
    show_slide_patched = """function showSlide(i){
  if(i >= PUBLIC_SLIDE_COUNT && !isUnlocked){
    openLockModal(i);
    return;
  }
  if(i<0 || i>=SLIDES.length) return;"""
    new_html = new_html.replace(show_slide_orig, show_slide_patched)

    client_engine = f"""
<!-- INLINED ZERO-DEPENDENCY CRYPTOJS ENGINE -->
<script>
{CRYPTO_JS_CODE}
</script>

<!-- AES-256 ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data" type="text/plain">
{ciphertext}
</script>

{LOCK_MODAL_HTML}

<script>
/* ================= STUDENT LOCK & CRYPTOJS DECRYPTION ENGINE ================= */
var PRES_ID = "konu3_kvh_ht_tedavisi_v1";
var TOTAL_SLIDES_COUNT = {total_slides};
var PUBLIC_SLIDE_COUNT = {public_count};
var isUnlocked = false;
var pendingTargetSlide = null;
var encryptedPayloadCiphertext = "";

document.addEventListener('DOMContentLoaded', () => {{
  const scriptTag = document.getElementById('encrypted-payload-data');
  if(scriptTag) {{
    encryptedPayloadCiphertext = scriptTag.textContent.trim();
  }}
  checkSessionUnlock();
}});

{SHARED_CRYPTO_JS_METHODS}

async function handleUnlockSubmit(e) {{
  e.preventDefault();
  const input = document.getElementById('student-password-input');
  const password = input.value.trim();
  const errorEl = document.getElementById('unlock-error-msg');
  const submitBtn = document.getElementById('unlock-submit-btn');
  const modalCard = document.getElementById('modal-card');

  if (!password) return;
  submitBtn.disabled = true;
  submitBtn.innerHTML = '⏳ Şifre Çözülüyor...';
  errorEl.style.display = 'none';

  let decryptedJson = null;
  try {{
    decryptedJson = decryptPayload(encryptedPayloadCiphertext, password);
  }} catch(authErr) {{
    console.error("Şifre çözme hatası:", authErr);
    errorEl.textContent = '⚠️ Hatalı şifre! Lütfen ders izlencesindeki şifrenizi kontrol ediniz.';
    errorEl.style.display = 'block';
    modalCard.classList.remove('modal-shake');
    void modalCard.offsetWidth;
    modalCard.classList.add('modal-shake');
    input.focus();
    input.select();
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
    return;
  }}

  try {{
    const lockedList = JSON.parse(decryptedJson);
    applyDecryptedSlides(lockedList);
    sessionStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJson);
    isUnlocked = true;
    closeLockModal();
    
    if (typeof updateGlobalLockUI === 'function') updateGlobalLockUI();
    if (window.pendingDownloadPdf) {{
      window.pendingDownloadPdf = false;
      const layout = window.pendingPdfLayout || null;
      setTimeout(() => triggerPresentationPdfDownload(layout), 350);
    }}

    if (pendingTargetSlide !== null && pendingTargetSlide !== undefined) {{
      const target = pendingTargetSlide;
      pendingTargetSlide = null;
      showSlide(target);
    }} else {{
      showSlide(PUBLIC_SLIDE_COUNT);
    }}
  }} catch(renderErr) {{
    console.error("Slayt yükleme hatası:", renderErr);
    errorEl.textContent = '⚠️ İçerik çözüldü fakat eklenirken hata oluştu: ' + renderErr.message;
    errorEl.style.display = 'block';
  }} finally {{
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
  }}
}}

function checkSessionUnlock() {{
  const cached = sessionStorage.getItem('unlocked_pres_' + PRES_ID);
  if (cached) {{
    try {{
      const lockedList = JSON.parse(cached);
      applyDecryptedSlides(lockedList);
      isUnlocked = true;
      if (typeof updateGlobalLockUI === 'function') updateGlobalLockUI();
    }} catch(e) {{ console.error("Cache okunamadı:", e); }}
  }}
}}

function applyDecryptedSlides(lockedList) {{
  if (isUnlocked) return;
  isUnlocked = true;
  window.isUnlocked = true;

  // 1. Remove preview barrier slide at index 10 from SLIDES array and from DOM
  if (SLIDES.length > 10 && SLIDES[10].type === 'prompt' && SLIDES[10].tag && SLIDES[10].tag.includes('Önizleme')) {{
    SLIDES.splice(10, 1);
    const barrierEl = document.getElementById('slide-10');
    if (barrierEl && barrierEl.parentNode) barrierEl.parentNode.removeChild(barrierEl);
  }}

  // 2. Append locked slides to SLIDES array and DOM
  const vp = document.getElementById('viewport');
  lockedList.forEach((s) => {{
    const idx = SLIDES.length;
    SLIDES.push(s);
    const div = document.createElement('div');
    div.className = 'slide';
    div.id = 'slide-' + idx;
    div.innerHTML = renderSlide(s, idx);
    vp.appendChild(div);
  }});

  // 3. Rebuild TOC and update counter
  buildToc();
  updateCounter();
  updateSecRail();

  // 4. Render
  showSlide(currentIndex >= 10 ? currentIndex : 10);
  if (typeof updateGlobalLockUI === 'function') updateGlobalLockUI();
}}

function openLockModal(targetSlide, forPdf) {{
  if (forPdf) window.pendingDownloadPdf = true;
  if (isUnlocked) {{
    if (window.pendingDownloadPdf) {{
      window.pendingDownloadPdf = false;
      const layout = window.pendingPdfLayout || null;
      triggerPresentationPdfDownload(layout);
    }}
    return;
  }}
  if (targetSlide !== undefined && targetSlide !== null) pendingTargetSlide = targetSlide;
  const m = document.getElementById('student-lock-modal');
  if (m) {{
    m.style.display = 'flex';
    setTimeout(() => {{
      const inp = document.getElementById('student-password-input');
      if (inp) inp.focus();
    }}, 80);
  }}
}}
</script>
"""
    new_html = new_html.replace('</body>', f'{client_engine}\n</body>')

    with open(out, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ 04-kardiyovaskuler-hastaliklar-ve-hipertansiyon.html üretildi ({out.stat().st_size / 1024:.1f} KB)")


def update_content_markdown():
    print("\n--- Markdown Kartları ve Ders Sayfaları Güncelleniyor ---")
    today_str = datetime.now().strftime("%Y-%m-%d")

    # 1. Konu 1 Markdown Cards
    tr_card1 = CONTENT_DIR / "tr/presentations/01-obezite-ve-tibbi-beslenme-tedavisi.md"
    tr_card1.write_text(f"""---
title: "Obezite ve Tıbbi Beslenme Tedavisi"
type: "presentation"
badge: "Lisans Dersi (BES 317 - BES 318)"
date: "{today_str}"
slide_count: "193 Slayt (🔒 AES-256 Korumalı)"
html_url: "slides/01-obezite-ve-tibbi-beslenme-tedavisi.html"
summary: "Obezite ve Tıbbi Beslenme Tedavisi interaktif ders sunumu. İlk 10 slayt açık önizleme; 11+ slaytlar AES-256 şifrelidir."
draft: false
lang: "tr"
order: 4
---

## 🧬 Ders Sunumu & Canlı Kilitli Modül
- **Önizleme Kapsamı (Slayt 1–10):** Açık akademik önizleme ve giriş kavramları.
- **Şifreli Modüller (Slayt 11–193):** İleri patofizyoloji, tanı & evreleme, enerji harcaması, MNT protokolleri ve ADIME klinik vakaları.
- **Şifre:** BES 317 - BES 318 ders izlencesinde ilan edilen öğrenci şifresi (`{PASSWORD}`) ile açılır.
""", encoding="utf-8")

    en_card1 = CONTENT_DIR / "en/presentations/01-obesity-medical-nutrition-therapy.md"
    en_card1.write_text(f"""---
title: "Obesity and Medical Nutrition Therapy"
type: "presentation"
badge: "Clinical Lecture (NUT 317)"
date: "{today_str}"
slide_count: "193 Slides (🔒 AES-256 Protected)"
html_url: "slides/01-obezite-ve-tibbi-beslenme-tedavisi.html"
summary: "Obesity and Medical Nutrition Therapy interactive lecture deck. First 10 slides public preview; slides 11+ encrypted."
draft: false
lang: "en"
order: 4
---

## 🧬 Lecture Deck & Protected Content
- **Public Preview (Slides 1–10):** Open academic preview.
- **Encrypted Modules (Slides 11–193):** Advanced pathophysiology, staging, MNT protocols, and ADIME case management.
- **Access Passcode:** Unlocked with `{PASSWORD}`.
""", encoding="utf-8")

    # 2. Konu 2 Markdown Cards
    tr_card2 = CONTENT_DIR / "tr/presentations/07-diyabet-ve-tibbi-beslenme-tedavisi.md"
    tr_card2.write_text(f"""---
title: "Diyabet ve Tıbbi Beslenme Tedavisi"
type: "presentation"
badge: "Lisans Dersi (BES 317 - BES 318)"
date: "{today_str}"
slide_count: "123 Slayt (🔒 AES-256 Korumalı)"
html_url: "slides/03-diyabet-ve-tibbi-beslenme-tedavisi.html"
summary: "Diyabet ve Tıbbi Beslenme Tedavisi dersi interaktif web sunumu. İlk 10 slayt açık önizleme; 11+ slaytlar AES-256 şifrelidir."
draft: false
lang: "tr"
order: 7
---

## 🧬 Ders Sunumu & Canlı Kilitli Modül
- **Önizleme Kapsamı (Slayt 1–10):** Açık akademik önizleme ve sindirim fizyolojisi.
- **Şifreli Modüller (Slayt 11–123):** İnsülin direnci anahtarları, glukotoksisite, komplikasyonlar, karbonhidrat sayımı ve ADIME vakaları.
- **Şifre:** BES 317 - BES 318 ders izlencesinde ilan edilen öğrenci şifresi (`{PASSWORD}`) ile açılır.
""", encoding="utf-8")

    en_card2 = CONTENT_DIR / "en/presentations/07-diabetes-and-medical-nutrition-therapy.md"
    en_card2.write_text(f"""---
title: "Diabetes and Medical Nutrition Therapy"
type: "presentation"
badge: "Clinical Lecture (NUT 317)"
date: "{today_str}"
slide_count: "123 Slides (🔒 AES-256 Protected)"
html_url: "slides/03-diyabet-ve-tibbi-beslenme-tedavisi.html"
summary: "Diabetes and Medical Nutrition Therapy interactive web presentation. First 10 slides public preview; slides 11+ encrypted."
draft: false
lang: "en"
order: 7
---

## 🧬 Lecture Deck & Protected Content
- **Public Preview (Slides 1–10):** Open preview; digestion physiology and insulin regulation.
- **Encrypted Modules (Slides 11–123):** Insulin resistance molecular switches, acute/chronic complications, carbohydrate counting, and ADIME case prescriptions.
- **Access Passcode:** Unlocked with `{PASSWORD}`.
""", encoding="utf-8")

    # 3. Konu 3 Markdown Cards
    tr_card3 = CONTENT_DIR / "tr/presentations/08-kardiyovaskuler-hastaliklar-ve-hipertansiyon.md"
    tr_card3.write_text(f"""---
title: "Kardiyovasküler Hastalıklar, Hipertansiyon ve Tıbbi Beslenme Tedavisi"
type: "presentation"
badge: "Lisans Dersi (BES 317 - BES 318)"
date: "{today_str}"
slide_count: "135 Slayt (🔒 AES-256 Korumalı)"
html_url: "slides/04-kardiyovaskuler-hastaliklar-ve-hipertansiyon.html"
summary: "Kardiyovasküler Hastalıklar ve Hipertansiyon interaktif ders sunumu. İlk 10 slayt açık önizleme; 11+ slaytlar AES-256 şifrelidir."
draft: false
lang: "tr"
order: 8
---

## 🧬 Ders Sunumu & Canlı Kilitli Modül
- **Önizleme Kapsamı (Slayt 1–10):** Açık akademik önizleme, risk faktörleri, endotel ve moleküler mekanizmalar.
- **Şifreli Modüller (Slayt 11–135):** Ateroskleroz, KAH, İnme, Kalp Yetersizliği, Hipertansiyon, ADIME vaka yönetimi ve kanıta dayalı diyet modelleri (DASH, Akdeniz, Portföy).
- **Şifre:** BES 317 - BES 318 ders izlencesinde ilan edilen öğrenci şifresi (`{PASSWORD}`) ile açılır.
""", encoding="utf-8")

    en_card3 = CONTENT_DIR / "en/presentations/08-cardiovascular-diseases-and-hypertension.md"
    en_card3.write_text(f"""---
title: "Cardiovascular Diseases, Hypertension and Medical Nutrition Therapy"
type: "presentation"
badge: "Clinical Lecture (NUT 317)"
date: "{today_str}"
slide_count: "135 Slides (🔒 AES-256 Protected)"
html_url: "slides/04-kardiyovaskuler-hastaliklar-ve-hipertansiyon.html"
summary: "Cardiovascular Diseases and Hypertension interactive lecture deck. First 10 slides public preview; slides 11+ encrypted."
draft: false
lang: "en"
order: 8
---

## 🧬 Lecture Deck & Protected Content
- **Public Preview (Slides 1–10):** Open preview; vascular biology, endothelial dysfunction, and molecular risk pathways.
- **Encrypted Modules (Slides 11–135):** Atherosclerosis, CAD, stroke, heart failure, cardiac cachexia, hypertension, ADIME process, and evidence-based dietary patterns (DASH, Mediterranean, Portfolio).
- **Access Passcode:** Unlocked with `{PASSWORD}`.
""", encoding="utf-8")

    # 4. Teaching Pages
    tr_teach = CONTENT_DIR / "tr/teaching/06-yetiskin-hastaliklarinda-diyet-tedavisi.md"
    tr_teach_content = f"""---
title: "Yetişkin Hastalıklarında Diyet Tedavisi (Teorik & Uygulama)"
type: "teaching"
code: "BES 317 - BES 318"
badge: "Lisans Modülü"
semester: "Güz & Bahar"
icon: "fa-notes-medical"
summary: "Yetişkinlerde kardiyometabolik, gastrointestinal, onkolojik, renal ve hepatik hastalıklarda Nutrisyonel Bakım Süreci (NCP) basamaklarıyla kanıta dayalı klinik diyet tedavisi ve vaka simülasyonları."
topics: "Antropometri ve klinik biyokimya yorumlama, Obezite ve kilo yönetimi, Tip 2 Diyabette glisemik kontrol ve karbonhidrat sayımı, Kardiyovasküler hastalıklar, Hipertansiyon, Akdeniz ve DASH diyeti, GIS hastalıkları (Reflü, Gastrit, Çölyak, IBD), Kanser kaşeksisi ve onkolojik nütrisyon, Akut/kronik böbrek yetmezliği ve diyaliz, Karaciğer hastalıkları (MASLD/MASH, Siroz), safra kesesi ve pankreatit."
lab_ai_practice: "Gerçek klinik vaka senaryoları üzerinden Nutrisyonel Bakım Süreci (NCP) modellemesi, dinamik biyokimyasal parametre takibi, menü ve değişim listesi tasarımı."
classroom_practices: "Akdeniz & DASH Diyet Planlama Atölyesi (Güz dönemi) ve GLP-1 Reseptör Agonisti kullanan metabolik sendromlu bireylere yönelik Yapay Zeka Destekli Klinik Vaka Simülasyonları (Bahar dönemi)."
learning_outcomes: "Karmaşık metabolik ve kronik tablolarda hastaya özgü tıbbi beslenme tedavisi reçete edebilme, klinik bulguları doğru yorumlayarak tedavi sürecini ve multidisipliner vaka yönetimini başarıyla yürütme."
slides_url: "../slides/01-obezite-ve-tibbi-beslenme-tedavisi.html"
slides_title: "BES 317: Obezite ve Tıbbi Beslenme Tedavisi (193 Slayt)"
slides_badge: "İlk 10 slayt açık önizleme • 🔒 AES-256 Korumalı • Şifre: COZYYHTBT2026_"
draft: false
lang: "tr"
order: 1
---

## 🩺 Bu Dersi Nasıl İşliyoruz? Sınıf İçi Deneyim & Uygulamalar
- **🌿 Akdeniz & DASH Diyet Tasarım Atölyesi:** Öğrencilerimiz kardiyovasküler ve hipertansiyon vakalarında sadece kalori kısıtlaması değil; Akdeniz ve DASH modellerinin porsiyonlama kriterlerini, yerel mutfak uyarlamalarını ve mikro besin ögesi dengelerini analitik olarak modellemektedir.
- **🤖 GLP-1 İlaçları ve Yapay Zekalı Vaka Simülasyonu:** GLP-1 agonisti tedavisi alan hastalarda gastrointestinal semptom yönetimi, kas kütlesinin korunması (sarkopenik obezite önleme) ve protein/enerji hedeflerinin yapay zeka simülasyonları ile modellenmesi.
- **Vaka Bazlı Nutrisyonel Bakım Süreci (NCP):** Gerçek hasta laboratuvar bulguları üzerinden adım adım beslenme tanısı koyma (PES cümlesi), karbonhidrat sayımı simülasyonları ve tıbbi beslenme reçetesi hazırlama.

## 📊 İnteraktif Ders Sunumları & Öğrenci Kilit Ekranı
Bu dersin canlı ve interaktif web sunumlarına aşağıdaki bağlantılardan erişebilirsiniz. **İlk 10 slayt açık önizleme** olarak sunulmakta; ileri modüller, vaka analizleri ve simülatörler **AES-256-GCM** öğrenci şifresiyle korunmaktadır.

- 👉 [**1. Konu: Obezite ve Tıbbi Beslenme Tedavisi (193 Slayt - Canlı İzle)**](../slides/01-obezite-ve-tibbi-beslenme-tedavisi.html) *(🔒 AES-256 Korumalı)*
- 👉 [**1. Hafta: Obezite ve Tıbbi Beslenme Tedavisine Giriş Uygulaması (59+ Slayt - Canlı İzle)**](../slides/02-obezite-uygulama.html) *(🔒 AES-256 Korumalı)*
- 👉 [**2. Konu: Diyabet ve Tıbbi Beslenme Tedavisi (123 Slayt - Canlı İzle)**](../slides/03-diyabet-ve-tibbi-beslenme-tedavisi.html) *(🔒 AES-256 Korumalı)*
- 👉 [**3. Konu: Kardiyovasküler Hastalıklar, Hipertansiyon ve Tıbbi Beslenme Tedavisi (135 Slayt - Canlı İzle)**](../slides/04-kardiyovaskuler-hastaliklar-ve-hipertansiyon.html) *(🔒 AES-256 Korumalı)*
"""
    tr_teach.write_text(tr_teach_content, encoding="utf-8")

    en_teach = CONTENT_DIR / "en/teaching/06-medical-nutrition-therapy.md"
    en_teach_content = f"""---
title: "Medical Nutrition Therapy in Adult Diseases (Theory & Practice)"
type: "teaching"
code: "BES 317 - BES 318"
badge: "Undergraduate Module"
semester: "Fall & Spring"
icon: "fa-notes-medical"
summary: "Evidence-based clinical diet therapy and case simulations across cardiometabolic, GI, oncologic, renal, and hepatic diseases using the Nutrition Care Process (NCP)."
topics: "Antropometric and clinical biochemistry interpretation, obesity management, glycemic control & carbohydrate counting in Type 2 Diabetes, CVD, hypertension, Mediterranean & DASH diets, GI disorders (celiac, IBD, GERD), cancer cachexia & oncologic nutrition, acute/chronic renal disease & dialysis, liver diseases (MASLD/MASH, cirrhosis), and pancreatitis."
lab_ai_practice: "Clinical case simulations utilizing Nutrition Care Process (NCP: Assessment, Diagnosis, Intervention, Monitoring & Evaluation), personalized menu planning, and dynamic biochemical tracking."
classroom_practices: "Comprehensive Mediterranean & DASH Diet Workshop (Fall semester) and AI-powered Interactive Clinical Case Simulations for patients on GLP-1 Receptor Agonist therapy (Spring semester)."
learning_outcomes: "Prescribe patient-tailored medical nutrition therapies in complex metabolic conditions, interpret clinical findings accurately, and lead multidisciplinary case management."
draft: false
lang: "en"
order: 1
---

## 🎯 Course Objectives & Vision
- **🌿 Mediterranean & DASH Diet Workshop:** Analytical diet modeling beyond caloric restriction, accounting for portion dynamics and local biodiversity.
- **🤖 GLP-1 Therapy & AI Case Simulations:** Modeling gastrointestinal symptom management, lean mass preservation, and precision macronutrient targets via AI-assisted simulations.
- **Nutrition Care Process (NCP):** Formulating evidence-based PES diagnoses, carbohydrate counting, and tailored clinical diet prescriptions.

## 📊 Interactive Lecture Slides & Student Lock Screen
Access the live interactive web presentations via the links below. The **first 10 slides are public preview**, while slides 11+ are encrypted with **AES-256-GCM** and unlocked with the course password.

- 👉 [**Topic 1: Obesity & Medical Nutrition Therapy (193 Slides - Live)**](../../slides/01-obezite-ve-tibbi-beslenme-tedavisi.html) *(🔒 AES-256 Protected)*
- 👉 [**Week 1: Introduction to Obesity & Medical Nutrition Therapy Practice (59+ Slides - Live)**](../../slides/02-obezite-uygulama.html) *(🔒 AES-256 Protected)*
- 👉 [**Topic 2: Diabetes & Medical Nutrition Therapy (123 Slides - Live)**](../../slides/03-diyabet-ve-tibbi-beslenme-tedavisi.html) *(🔒 AES-256 Protected)*
- 👉 [**Topic 3: Cardiovascular Diseases & Hypertension (135 Slides - Live)**](../../slides/04-kardiyovaskuler-hastaliklar-ve-hipertansiyon.html) *(🔒 AES-256 Protected)*
"""
    en_teach.write_text(en_teach_content, encoding="utf-8")
    print("  ✅ Markdown kartları ve ders bağlantıları yazıldı.")


def main():
    print("=======================================================")
    print("🚀 BES 317 SUNUM GÜNCELLEME VE YAYINLAMA MOTORU")
    print("=======================================================")
    build_konu1()
    build_konu2()
    build_konu3()
    update_content_markdown()

    print("\n--- Web Sitesi Derleniyor (build.py) ---")
    res = subprocess.run(["python3", str(BASE_DIR / "build.py")], capture_output=True, text=True)
    print("  " + res.stdout.replace("\n", "\n  ").strip())

    print("\n✨ TÜM SUNUMLAR VE SAYFALAR BAŞARIYLA DERLENDİ!")

if __name__ == "__main__":
    main()
