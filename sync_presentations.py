#!/usr/bin/env python3
"""
Obsidian Vault to Academic Website Presentation Synchronizer & AES-256 Encryptor
Dr. Caner ÖZYILDIRIM Website Suite

This script:
1. Copies all simulation files and image assets directly from the Obsidian Vault to slides/assets/.
2. Reads HTML presentation files directly from the Obsidian Vault.
3. Applies AES-256 encryption to slides 11+ (keeping first 10 slides as public preview).
4. Integrates the universal CryptoJS AES decryption engine with flexible candidate matching, student lock modal, and Table of Contents jump interceptor.
5. Updates website markdown entries and compiles the website.
"""

import os
import sys
import re
import json
import shutil
import base64
import hashlib
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
VAULT_DIR = Path("/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner")
SLIDES_OUTPUT_DIR = BASE_DIR / "slides"
SLIDES_ASSETS_DIR = SLIDES_OUTPUT_DIR / "assets"
SLIDES_OUTPUT_DIR.mkdir(exist_ok=True)
SLIDES_ASSETS_DIR.mkdir(exist_ok=True)

# Secure Course Password for Yetişkin Hastalıklarında Beslenme Tedavisi
DEFAULT_PASSWORD = "COZYYHTBT2026_"
# Secure Course Password for Bilgisayar ve Yapay Zeka Uygulamaları
AI_PASSWORD = "COZYBESAI2026_"

def sync_assets():
    """Copies all simulation HTML files, PNG assets, and logos from Vault to slides/assets/ if missing."""
    print("📦 Sunum asset'leri kontrol ediliyor...")
    vault_assets_dir = VAULT_DIR / "Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/Sunumlar/assets"
    ai_assets_dir = VAULT_DIR / "Dersler/Bilgisayar Uygulamaları ve Yapay Zeka/Sunumlar/assets"
    copied_count = 0
    
    if vault_assets_dir.exists():
        for item in vault_assets_dir.iterdir():
            if item.is_file() and not item.name.startswith('.'):
                dest = SLIDES_ASSETS_DIR / item.name
                if not dest.exists():
                    shutil.copy2(item, dest)
                    copied_count += 1

    # AI assets: copy only assets used by active presentations (skip heavy future week assets)
    if ai_assets_dir.exists():
        for item in ai_assets_dir.iterdir():
            if item.is_file() and not item.name.startswith('.') and not item.name.startswith('faz3_') and not item.name.startswith('veri_gudumlu_'):
                dest = SLIDES_ASSETS_DIR / item.name
                if not dest.exists():
                    shutil.copy2(item, dest)
                    copied_count += 1
    print(f"  ✅ {copied_count} yeni asset dosyası '{SLIDES_ASSETS_DIR}' dizinine kopyalandı.")

    # Copy faculty logo
    faculty_logo = VAULT_DIR / "Files/Saglik-Bilimleri-Fakultesi-2.png"
    if faculty_logo.exists():
        dest_logo = SLIDES_ASSETS_DIR / "Saglik-Bilimleri-Fakultesi-2.png"
        if not dest_logo.exists():
            shutil.copy2(faculty_logo, dest_logo)
            print("  ✅ Fakülte logosu kopyalandı.")

def encrypt_aes_payload(plaintext: str, password: str) -> str:
    """Encrypts plaintext with AES-256 via CryptoJS in Node.js."""
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

# Read minified crypto-js library to inline into slides
CRYPTO_JS_FILE = SLIDES_ASSETS_DIR / "crypto-js.min.js"
if not CRYPTO_JS_FILE.exists():
    # Fallback to local node_modules
    local_cjs = BASE_DIR / "node_modules/crypto-js/crypto-js.js"
    if local_cjs.exists():
        shutil.copy2(local_cjs, CRYPTO_JS_FILE)

with open(CRYPTO_JS_FILE, "r", encoding="utf-8") as f:
    CRYPTO_JS_MIN_CODE = f.read()

# Shared Modal and Crypto CSS / HTML
LOCK_MODAL_HTML = """
<!-- STUDENT PASSWORD LOCK MODAL -->
<div id="student-lock-modal" style="display:none; position:fixed; inset:0; background:rgba(11,17,29,0.88); backdrop-filter:blur(10px); z-index:99999; align-items:center; justify-content:center; padding:20px; font-family:'Inter', system-ui, sans-serif;">
  <div id="modal-card" style="background:#131d2e; border:1px solid #233554; border-radius:24px; max-width:440px; width:100%; padding:32px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.6); text-align:center; position:relative; color:#f8fafc;">
    <button onclick="closeLockModal()" style="position:absolute; top:16px; right:16px; background:none; border:none; color:#94a3b8; font-size:20px; cursor:pointer; padding:4px 8px; border-radius:8px;">✕</button>
    <div style="width:64px; height:64px; border-radius:18px; background:rgba(217,119,6,0.15); border:1px solid rgba(217,119,6,0.3); color:#fbbf24; display:flex; align-items:center; justify-content:center; font-size:26px; margin:0 auto 16px;">🔒</div>
    <h3 style="font-size:20px; font-weight:700; margin:0 0 8px; color:#ffffff;">Öğrenci Kilit Ekranı</h3>
    <p style="font-size:13px; color:#94a3b8; line-height:1.6; margin:0 0 24px;">10 slaytlık önizleme tamamlanmıştır. Devamını görüntülemek için lütfen ders şifrenizi giriniz.</p>
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
      <span>🔒</span> <span>Ders İzlencesi ve OBS Şifresi</span>
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

def sync_konu1_obezite():
    """Syncs Konu1_Obezite_Sunum.html (185 slides) with AES-256 encryption."""
    src_file = VAULT_DIR / "Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/Sunumlar/Konu1_Obezite_Sunum.html"
    if not src_file.exists():
        print(f"❌ Kaynak dosya bulunamadı: {src_file}")
        return False

    print(f"📖 Konu 1 Obezite Sunumu işleniyor: {src_file.name}")
    with open(src_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Normalize relative faculty logo path
    html = html.replace('../../../Files/Saglik-Bilimleri-Fakultesi-2.png', 'assets/Saglik-Bilimleri-Fakultesi-2.png')

    # Inject HTTPS redirect so students who land on http:// are sent to https://
    # This eliminates the "Not Secure" browser warning
    https_redirect = """<script>if(location.protocol==='http:'&&location.hostname!=='localhost'&&location.hostname!=='127.0.0.1'){location.replace('https:'+location.href.substring(5));}</script>"""
    html = html.replace('<head>', '<head>\n' + https_redirect, 1)

    # Extract SLIDES array
    pos = html.rfind('const SLIDES = [')
    if pos == -1:
        print("❌ 'const SLIDES' bulunamadı!")
        return False

    sub = html[pos + len('const SLIDES = ['):]
    end_pos = sub.find('];\n')
    slides_json_str = '[' + sub[:end_pos] + ']'
    slides_data = json.loads(slides_json_str)

    total_slides = len(slides_data)
    public_count = 10
    print(f"  Toplam Slayt: {total_slides} | Açık Önizleme: {public_count} | Şifrelenecek: {total_slides - public_count}")

    public_slides = slides_data[:public_count]
    locked_slides = slides_data[public_count:]

    # Add public preview barrier note to slide 10
    if len(public_slides) >= 10:
        preview_slide = {
            "type": "prompt",
            "sec": 0,
            "tag": "🛑 Önizleme Sonu (Slayt 10)",
            "q": "10 slaytlık önizleme tamamlanmıştır.",
            "note": "Devamını görüntülemek için ders şifresi girilmesi gerekmektedir."
        }
        public_slides[9] = preview_slide

    # Encrypt locked slides with AES-256 via CryptoJS
    ciphertext = encrypt_aes_payload(json.dumps(locked_slides, ensure_ascii=False), DEFAULT_PASSWORD)

    # Build new public SLIDES string
    new_public_slides_str = json.dumps(public_slides, indent=2, ensure_ascii=False)
    
    # Replace SLIDES array in HTML
    new_html = html[:pos + len('const SLIDES = ')] + new_public_slides_str + html[pos + len('const SLIDES = [') + end_pos + 1:]

    # Ensure slide 0 has active class immediately upon DOM insertion
    orig_dom_loop = "wrap.innerHTML = renderSlide(s, idx);"
    patched_dom_loop = "wrap.innerHTML = renderSlide(s, idx);\n  if(idx === 0 && wrap.firstElementChild) wrap.firstElementChild.classList.add('active');"
    new_html = new_html.replace(orig_dom_loop, patched_dom_loop)

    # Patch allSlideEls & total
    new_html = new_html.replace('const allSlideEls = Array.from(stage.children);', 'let allSlideEls = Array.from(stage.children);')
    new_html = new_html.replace('const total = SLIDES.length;', 'let total = SLIDES.length;')
    
    # Inject lock globals BEFORE go() so go() can reference them at first call time.
    # PUBLIC_SLIDE_COUNT, isUnlocked, pendingTargetSlide are normally defined in the
    # LOCK ENGINE <script> block appended to </body>, which is parsed AFTER the main
    # <script> block. If go(0) is called at the end of the main script, these vars
    # are undefined and the browser throws a ReferenceError, breaking everything.
    lock_globals_injection = f"""/* ===== LOCK ENGINE GLOBALS (injected before go()) ===== */
var PUBLIC_SLIDE_COUNT = {public_count};
var isUnlocked = false;
var pendingTargetSlide = null;
var encryptedPayloadCiphertext = "";
/* ======================================================= */
"""
    go_anchor = "function go(idx){"
    go_first_pos = new_html.find(go_anchor)
    if go_first_pos != -1:
        new_html = new_html[:go_first_pos] + lock_globals_injection + new_html[go_first_pos:]

    # Intercept go(idx) for lock & smooth activation
    go_orig = "function go(idx){\n  if(idx<0||idx>=total) return;\n  if(allSlideEls[current]) allSlideEls[current].classList.remove('active');"
    go_patched = """function go(idx){
  if(idx >= PUBLIC_SLIDE_COUNT && !isUnlocked){
    openLockModal(idx);
    return;
  }
  if(idx<0||idx>=total) return;
  if(allSlideEls[current] && current !== idx) allSlideEls[current].classList.remove('active');"""
    new_html = new_html.replace(go_orig, go_patched)

    # Remove the naked go(0) call at the end of the main script block.
    # It runs BEFORE the CryptoJS lock engine <script> is parsed (ReferenceError).
    # Initialization is handled by DOMContentLoaded in the lock engine instead.
    new_html = new_html.replace(
        "// Initialize on slide 0\ngo(0);",
        "// go(0) is called by the lock engine DOMContentLoaded handler"
    )

    # Client-side script with inlined CryptoJS
    client_crypto_script = """
<!-- INLINED ZERO-DEPENDENCY CRYPTOJS ENGINE -->
<script>
""" + CRYPTO_JS_MIN_CODE + """
</script>

<!-- AES-256 ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data" type="text/plain">
""" + ciphertext + """
</script>

""" + LOCK_MODAL_HTML + """

<script>
/* ================= STUDENT LOCK & CRYPTOJS DECRYPTION ENGINE ================= */
// NOTE: PUBLIC_SLIDE_COUNT, isUnlocked, pendingTargetSlide, encryptedPayloadCiphertext
// are declared with 'var' in the main <script> block above (before go() function),
// so that go() can reference them even when called from the main script.
// Redeclaring them here with const/let would cause a SyntaxError.
var PRES_ID = "konu1_obezite_tedavisi";
var TOTAL_SLIDES_COUNT = """ + str(total_slides) + """;

document.addEventListener('DOMContentLoaded', () => {
  const scriptTag = document.getElementById('encrypted-payload-data');
  if(scriptTag) {
    encryptedPayloadCiphertext = scriptTag.textContent.trim();
  }
  checkSessionUnlock();
  go(0);
});

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

async function handleUnlockSubmit(e) {
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
  try {
    decryptedJson = decryptPayload(encryptedPayloadCiphertext, password);
  } catch(authErr) {
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
  }

  try {
    const lockedList = JSON.parse(decryptedJson);
    applyDecryptedSlides(lockedList);
    localStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJson);
    isUnlocked = true;
    closeLockModal();
    
    // Jump directly to requested slide (e.g. slide 25 or 120)!
    if (pendingTargetSlide !== null && pendingTargetSlide !== undefined) {
      const target = pendingTargetSlide;
      pendingTargetSlide = null;
      go(target);
    } else {
      go(PUBLIC_SLIDE_COUNT);
    }
  } catch(renderErr) {
    console.error("Slayt yükleme hatası:", renderErr);
    errorEl.textContent = '⚠️ İçerik çözüldü fakat eklenirken hata oluştu: ' + renderErr.message;
    errorEl.style.display = 'block';
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
  }
}

function checkSessionUnlock() {
  const cached = localStorage.getItem('unlocked_pres_' + PRES_ID);
  if (cached) {
    try {
      const lockedList = JSON.parse(cached);
      applyDecryptedSlides(lockedList);
      isUnlocked = true;
    } catch(e) { console.error("Cache okunamadı:", e); }
  }
}

function applyDecryptedSlides(lockedList) {
  if (isUnlocked) return;
  const stage = document.getElementById('stage');
  lockedList.forEach((s, i) => {
    const idx = PUBLIC_SLIDE_COUNT + i;
    SLIDES.push(s);
    const wrap = document.createElement('div');
    wrap.innerHTML = renderSlide(s, idx);
    if(wrap.firstElementChild) {
      stage.appendChild(wrap.firstElementChild);
    } else {
      const fallback = document.createElement('div');
      fallback.className = 'slide';
      fallback.innerHTML = eyebrowTitle(s) + '<div class="slide-sub">' + (s.note || '') + '</div>';
      stage.appendChild(fallback);
    }
  });
  allSlideEls = Array.from(stage.children);
  total = SLIDES.length;
  isUnlocked = true;
  
  // Re-run chart initializations & MathJax
  chartQueue.forEach(spec=>{
    const canvas = document.getElementById(spec.id);
    if(canvas){ try{ spec.build(canvas.getContext('2d')); }catch(e){} }
  });
  if(window.MathJax && window.MathJax.typesetPromise) window.MathJax.typesetPromise();
  update();
}

function openLockModal(targetSlide) {
  if (isUnlocked) return;
  if (targetSlide !== undefined) pendingTargetSlide = targetSlide;
  const m = document.getElementById('student-lock-modal');
  m.style.display = 'flex';
  setTimeout(() => document.getElementById('student-password-input').focus(), 80);
}

function closeLockModal() {
  const m = document.getElementById('student-lock-modal');
  m.style.display = 'none';
  document.getElementById('unlock-error-msg').style.display = 'none';
}

function togglePasswordVisibility() {
  const inp = document.getElementById('student-password-input');
  inp.type = inp.type === 'password' ? 'text' : 'password';
}
</script>
"""

    # Insert client_crypto_script before </body>
    new_html = new_html.replace('</body>', f'{client_crypto_script}\n</body>')

    out_file = SLIDES_OUTPUT_DIR / "01-obezite-ve-tibbi-beslenme-tedavisi.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ Kaydedildi: {out_file} ({os.path.getsize(out_file) / 1024:.1f} KB)\n")
    return True

def sync_obezite_uygulama():
    """Syncs 1.hafta Obezite-Uygulama Sunumu.html with AES-256 encryption."""
    src_file = VAULT_DIR / "Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/Sunumlar/1.hafta Obezite-Uygulama Sunumu.html"
    if not src_file.exists():
        print(f"❌ Kaynak dosya bulunamadı: {src_file}")
        return False

    print(f"📖 Obezite Uygulama Sunumu işleniyor: {src_file.name}")
    with open(src_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Normalize relative faculty logo path
    html = html.replace('../../../Files/Saglik-Bilimleri-Fakultesi-2.png', 'assets/Saglik-Bilimleri-Fakultesi-2.png')

    # Inject HTTPS redirect so students on http:// are sent to https://
    https_redirect_uy = """<script>if(location.protocol==='http:'&&location.hostname!=='localhost'&&location.hostname!=='127.0.0.1'){location.replace('https:'+location.href.substring(5));}</script>"""
    html = html.replace('<head>', '<head>\n' + https_redirect_uy, 1)

    # Find the split points in slide registration vs navigation motor
    pos_end = html.find('/* ---- Egzersiz 3 (Set B, eşit gramaj) ---- */')
    pos_nav = html.find('/* ============================================================\n   NAVİGASYON MOTORU')
    if pos_nav == -1:
        pos_nav = html.find('NAVİGASYON MOTORU')

    if pos_end != -1 and pos_nav != -1:
        public_head = html[:pos_end]
        locked_js = html[pos_end:pos_nav]
        engine_html = html[pos_nav:]

        # Add preview end slide registration to public head
        preview_reg = """
addSlide('🛑 Önizleme Sınırı', 'Önizleme Sonu (Slayt 10)', 'Önizleme Sonu',
  slideIntro('🔒', '10 Slaytlık Önizleme Tamamlanmıştır', 'Devamını görüntülemek için ders şifresi girilmesi gerekmektedir.'));
"""
        public_head = public_head + preview_reg

        # Encrypt locked JS registration script ONLY with AES-256 via CryptoJS
        ciphertext = encrypt_aes_payload(locked_js, DEFAULT_PASSWORD)

        client_crypto_script = """
<!-- INLINED ZERO-DEPENDENCY CRYPTOJS ENGINE -->
<script>
""" + CRYPTO_JS_MIN_CODE + """
</script>

<!-- AES-256 ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data-uygulama" type="text/plain">
""" + ciphertext + """
</script>

""" + LOCK_MODAL_HTML + """

<script>
/* ================= STUDENT LOCK & CRYPTOJS DECRYPTION ENGINE ================= */
const PRES_ID = "obezite_uygulama_hafta1";
const PUBLIC_SLIDE_COUNT = 10;
let isUnlocked = false;
let pendingTargetSlide = null;
let encryptedPayloadCiphertext = "";

document.addEventListener('DOMContentLoaded', () => {
  const scriptTag = document.getElementById('encrypted-payload-data-uygulama');
  if(scriptTag) {
    encryptedPayloadCiphertext = scriptTag.textContent.trim();
  }
  checkSessionUnlock();
});

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

async function handleUnlockSubmit(e) {
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

  let decryptedJs = null;
  try {
    decryptedJs = decryptPayload(encryptedPayloadCiphertext, password);
  } catch(authErr) {
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
  }

  try {
    applyDecryptedUygulama(decryptedJs);
    localStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJs);
    isUnlocked = true;
    closeLockModal();
    
    if (pendingTargetSlide !== null && pendingTargetSlide !== undefined) {
      const target = pendingTargetSlide;
      pendingTargetSlide = null;
      goTo(target);
    } else {
      goTo(PUBLIC_SLIDE_COUNT);
    }
  } catch(renderErr) {
    console.error("Uygulama render hatası:", renderErr);
    errorEl.textContent = '⚠️ İçerik çözüldü fakat eklenirken hata oluştu: ' + renderErr.message;
    errorEl.style.display = 'block';
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
  }
}

function checkSessionUnlock() {
  const cached = localStorage.getItem('unlocked_pres_' + PRES_ID);
  if (cached) {
    try {
      applyDecryptedUygulama(cached);
      isUnlocked = true;
    } catch(e) { console.error("Cache hatası:", e); }
  }
}

function applyDecryptedUygulama(jsCode) {
  if (isUnlocked) return;
  const initialSlideCount = SLIDES.length;
  // Execute decrypted registration script in global scope
  const runner = new Function(jsCode);
  runner();

  // Render newly added slide shells
  const root = document.getElementById('slidesRoot');
  for (let i = initialSlideCount; i < SLIDES.length; i++) {
    root.appendChild(buildSlideShell(SLIDES[i], i));
  }
  populateJump();
  isUnlocked = true;
}

function openLockModal(targetSlide) {
  if (isUnlocked) return;
  if (targetSlide !== undefined) pendingTargetSlide = targetSlide;
  const m = document.getElementById('student-lock-modal');
  m.style.display = 'flex';
  setTimeout(() => document.getElementById('student-password-input').focus(), 80);
}

function closeLockModal() {
  const m = document.getElementById('student-lock-modal');
  m.style.display = 'none';
  document.getElementById('unlock-error-msg').style.display = 'none';
}

function togglePasswordVisibility() {
  const inp = document.getElementById('student-password-input');
  inp.type = inp.type === 'password' ? 'text' : 'password';
}
</script>
"""

        # Intercept goTo(idx) in engine_html
        orig_goto = "function goTo(idx){\n  if (idx < 0 || idx >= SLIDES.length) return;"
        patched_goto = """function goTo(idx){
  if (idx >= PUBLIC_SLIDE_COUNT && !isUnlocked){
    openLockModal(idx);
    return;
  }
  if (idx < 0 || idx >= SLIDES.length) return;"""
        engine_html = engine_html.replace(orig_goto, patched_goto)

        new_html = public_head + engine_html
        new_html = new_html.replace('</body>', f'{client_crypto_script}\n</body>')
    else:
        new_html = html

    out_file = SLIDES_OUTPUT_DIR / "02-obezite-uygulama.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ Kaydedildi: {out_file} ({os.path.getsize(out_file) / 1024:.1f} KB)\n")
    return True

def sync_bilgisayar_yapay_zeka():
    """Syncs Hafta1_AI_ile_Tanisma_Sunum.html (79 slides) with AES-256 encryption."""
    src_file = VAULT_DIR / "Dersler/Bilgisayar Uygulamaları ve Yapay Zeka/Sunumlar/Hafta1_AI_ile_Tanisma_Sunum.html"
    if not src_file.exists():
        print(f"❌ Kaynak dosya bulunamadı: {src_file}")
        return False

    print(f"📖 Hafta 1 Yapay Zeka Sunumu işleniyor: {src_file.name}")
    with open(src_file, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Normalize faculty logo and asset paths
    html = html.replace('../../../Files/Saglik-Bilimleri-Fakultesi-2.png', 'assets/Saglik-Bilimleri-Fakultesi-2.png')

    # 2. Inject HTTPS redirect so students on http:// are sent to https://
    https_redirect = """<script>if(location.protocol==='http:'&&location.hostname!=='localhost'&&location.hostname!=='127.0.0.1'){location.replace('https:'+location.href.substring(5));}</script>"""
    html = html.replace('<head>', '<head>\n' + https_redirect, 1)

    # 3. Neutralize MQTT & QR script tags and functions (no live poll needed on website)
    html = re.sub(r'<script src="[^"]*mqttws31[^"]*"></script>', '', html)
    html = re.sub(r'<script src="[^"]*qrcode[^"]*"></script>', '', html)
    html = html.replace('initH1QrCodes();', '/* initH1QrCodes(); disabled */')
    html = html.replace('connectH1DeckMQTT();', '/* connectH1DeckMQTT(); disabled */')

    # 4. Extract slides from container
    slides_m = re.search(r'(<div class="slides" id="slides">)(.*?)(</div>\s*<footer class="chrome">)', html, re.DOTALL)
    if not slides_m:
        print("❌ 'slides' container bulunamadı!")
        return False

    prefix = html[:slides_m.start(2)]
    slides_inner = slides_m.group(2)
    suffix = html[slides_m.end(2):]

    slide_chunks = re.findall(r'(<section class="slide.*?</section>)', slides_inner, re.DOTALL)
    total_slides = len(slide_chunks)
    print(f"  Toplam Slayt: {total_slides}")

    # 5. Clean Slide 3: remove live MQTT badge, QR card, empty response streams; arrange S1 & S4 in 2-col
    s3 = slide_chunks[2]
    header_part = """    <section class="slide"><div class="slide-inner">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:16px;">
        <div>
          <p class="eyebrow">Sınıf İçi Deneyim &amp; Dijital Araç Dağılımı</p>
          <h1 class="slide-title" style="margin-bottom:4px;">Önce <em>birbirimizi tanıyalım</em></h1>
        </div>
      </div>"""

    s1_m = re.search(r'(<!-- S1: KULLANILAN ARAÇLAR DAĞILIMI -->\s*<div class="card" id="h1ToolsCard".*?</div>\s*</div>\s*</div>)', s3, re.DOTALL)
    s4_m = re.search(r'(<!-- S4: PROMPT DÜZEYİ 1-5 HİSTOGRAMI -->\s*<div class="card" id="h1HistCard".*?</div>\s*</div>\s*</div>)', s3, re.DOTALL)

    if s1_m and s4_m:
        s3_clean = f"""{header_part}
      <div class="grid-wrap two-col" style="gap:24px; margin-top:12px;">
        {s1_m.group(1)}
        {s4_m.group(1)}
      </div>
    </div></section>"""
        slide_chunks[2] = s3_clean

    # 6. Clean Slide 79 (Kapanış): remove live MQTT badges and QR card
    s79 = slide_chunks[78]
    s79_header = """    <section class="slide"><div class="slide-inner">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:12px;">
        <div>
          <p class="eyebrow">Ders Sonu Değerlendirmesi · Kapanış Analizi</p>
          <h1 class="slide-title" style="margin-bottom:4px;">Prompt Yetkinliğiniz <em>Nasıl Değişti?</em></h1>
        </div>
      </div>"""

    left_col_m = re.search(r'(<!-- SOL: DERS BAŞI VS DERS SONU HİSTOGRAMLARI -->.*?)(?=\s*<!-- SAĞ:)', s79, re.DOTALL)
    score_card_m = re.search(r'(<!-- ORTALAMA DEĞİŞİM KARTI -->\s*<div class="card".*?</div>\s*</div>)', s79, re.DOTALL)

    if left_col_m and score_card_m:
        s79_clean = f"""{s79_header}
      <div class="grid-wrap two-col" style="gap:24px;">
        {left_col_m.group(1)}
        <div style="display:flex; flex-direction:column; gap:16px; justify-content:center;">
          {score_card_m.group(1)}
        </div>
      </div>
    </div></section>"""
        slide_chunks[78] = s79_clean

    # 7. Setup Public vs Locked Slides
    public_preview_slide = """    <section class="slide" id="slide_preview_lock"><div class="slide-inner" style="text-align:center; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:clamp(50px, 8vh, 90px) 20px;">
      <div style="width:72px; height:72px; border-radius:20px; background:rgba(30,111,92,0.12); border:1px solid rgba(30,111,92,0.25); color:var(--teal); display:flex; align-items:center; justify-content:center; font-size:32px; margin:0 auto 20px;">🔒</div>
      <p class="eyebrow" style="justify-content:center;">Önizleme Sınırı · Slayt 10</p>
      <h1 class="slide-title" style="margin:0 auto 16px; max-width:24ch; text-align:center;">10 Slaytlık Açık Önizleme <em>Tamamlanmıştır</em></h1>
      <p class="lede" style="max-width:640px; margin:0 auto 28px; text-align:center;">Dersin devamındaki üretken yapay zeka modülleri, vaka analizleri ve klinik simülasyonları görüntülemek için lütfen ders şifrenizi giriniz.</p>
      <button onclick="openLockModal(10)" style="background:linear-gradient(135deg, var(--teal), var(--teal-deep)); color:#ffffff; font-weight:700; border:none; border-radius:12px; padding:14px 32px; font-size:15px; cursor:pointer; box-shadow:var(--shadow); transition:transform .15s ease;">
        🔓 Şifreyi Gir &amp; Derse Devam Et
      </button>
    </div></section>"""

    public_slides = slide_chunks[:9] + [public_preview_slide]
    locked_slides = slide_chunks[9:]

    print(f"  Açık Önizleme: {len(public_slides)} | Şifrelenen Slayt: {len(locked_slides)}")

    locked_html_str = "\\n".join(locked_slides)
    ciphertext = encrypt_aes_payload(locked_html_str, AI_PASSWORD)

    # Reconstruct HTML with public slides
    public_slides_html = "\\n" + "\\n".join(public_slides) + "\\n"
    new_html = prefix + public_slides_html + suffix

    # 8. Intercept go(d) and jump(i) in navigation script
    orig_jump = "function jump(i){\\n  cur = i; render();\\n  var frags = getFragments(slides[cur]);\\n  fragIndex = frags.length; frags.forEach(revealFragment);\\n}"
    patched_jump = """function jump(i){
  if(i >= 9 && !isUnlocked){
    openLockModal(i);
    return;
  }
  cur = i; render();
  var frags = getFragments(slides[cur]);
  fragIndex = frags.length; frags.forEach(revealFragment);
}"""
    new_html = new_html.replace(orig_jump, patched_jump)

    orig_go = "function go(d){\\n  var slideEl = slides[cur];"
    patched_go = """function go(d){
  if(d > 0 && cur >= 9 && !isUnlocked){
    openLockModal(10);
    return;
  }
  var slideEl = slides[cur];"""
    new_html = new_html.replace(orig_go, patched_go)

    # 9. Client lock script and CryptoJS engine
    ai_lock_script = f"""
<!-- INLINED ZERO-DEPENDENCY CRYPTOJS ENGINE -->
<script>
{CRYPTO_JS_MIN_CODE}
</script>

<!-- AES-256 ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data-ai" type="text/plain">
{ciphertext}
</script>

{LOCK_MODAL_HTML}

<script>
/* ================= STUDENT LOCK & CRYPTOJS DECRYPTION ENGINE (AI COURSE) ================= */
const PRES_ID = "bes_ai_hafta1";
const PUBLIC_SLIDE_COUNT = 10;
let isUnlocked = false;
let pendingTargetSlide = null;

document.addEventListener('DOMContentLoaded', () => {{
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

function handleUnlockSubmit(e) {{
  if (e && e.preventDefault) e.preventDefault();
  const inp = document.getElementById('student-password-input');
  const val = inp ? inp.value : '';
  const scriptTag = document.getElementById('encrypted-payload-data-ai');
  if (!scriptTag) return;
  const ciphertext = scriptTag.textContent.trim();

  const candidates = getPasswordCandidates(val);
  let decrypted = null;
  for (const cand of candidates) {{
    try {{
      const bytes = CryptoJS.AES.decrypt(ciphertext, cand);
      const dec = bytes.toString(CryptoJS.enc.Utf8);
      if (dec && dec.length > 50) {{
        decrypted = dec;
        break;
      }}
    }} catch(err) {{}}
  }}

  if (decrypted) {{
    applyDecryptedAiSlides(decrypted);
    closeLockModal();
    const target = (pendingTargetSlide !== null && pendingTargetSlide >= 0) ? pendingTargetSlide : 9;
    pendingTargetSlide = null;
    jump(Math.min(target, slides.length - 1));
  }} else {{
    const errEl = document.getElementById('unlock-error-msg');
    if (errEl) errEl.style.display = 'block';
    const card = document.getElementById('modal-card');
    if (card) {{
      card.classList.remove('modal-shake');
      void card.offsetWidth;
      card.classList.add('modal-shake');
    }}
  }}
}}

function applyDecryptedAiSlides(decryptedHtml) {{
  if (isUnlocked) return;
  const lockSlide = document.getElementById('slide_preview_lock');
  const slidesContainer = document.getElementById('slides');
  if (lockSlide && lockSlide.parentNode) {{
    lockSlide.parentNode.removeChild(lockSlide);
  }}
  if (slidesContainer) {{
    slidesContainer.insertAdjacentHTML('beforeend', decryptedHtml);
  }}
  slides = document.querySelectorAll(".slide");
  if (dotsWrap) {{
    dotsWrap.innerHTML = "";
    slides.forEach(function(_, i){{
      const b = document.createElement("button");
      b.addEventListener("click", function(){{ jump(i); }});
      dotsWrap.appendChild(b);
    }});
  }}
  isUnlocked = true;
  try {{
    localStorage.setItem('unlocked_html_' + PRES_ID, decryptedHtml);
  }} catch(e) {{}}
  render();
}}

function checkSessionUnlock() {{
  try {{
    const cached = localStorage.getItem('unlocked_html_' + PRES_ID);
    if (cached) {{
      applyDecryptedAiSlides(cached);
    }}
  }} catch(e) {{}}
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
    new_html = new_html.replace('</body>', f'{ai_lock_script}\\n</body>')

    out_file = SLIDES_OUTPUT_DIR / "01-bilgisayar-ve-yapay-zeka.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ Kaydedildi: {out_file} ({os.path.getsize(out_file) / 1024:.1f} KB)\\n")
    return True

def update_markdown_and_rebuild():
    """Updates presentation cards and markdown files, then triggers build.py."""
    print("📝 Web sitesi markdown dosyaları güncelleniyor...")
    
    tr_pres_1 = BASE_DIR / "content/tr/presentations/01-obezite-ve-tibbi-beslenme-tedavisi.md"
    tr_pres_1.parent.mkdir(parents=True, exist_ok=True)
    with open(tr_pres_1, "w", encoding="utf-8") as f:
        f.write("""---
title: "Obezite ve Tıbbi Beslenme Tedavisi (Konu 1)"
type: "presentation"
badge: "Lisans Dersi (BES 317)"
date: "2026-03-01"
slide_count: "185 Slayt (🔒 AES-256 Korumalı)"
html_url: "slides/01-obezite-ve-tibbi-beslenme-tedavisi.html"
download_url: ""
summary: "Kronik, nüksedici ve nörometabolik bir hastalığın biyolojisinden kliniğe, tanıdan davranış değişikliğine tam yolculuk. İlk 10 slayt açık önizleme; 11+ slaytlar AES-256 şifrelidir."
draft: false
lang: "tr"
order: 1
---

## 💻 Ders Sunumu & Canlı Kilitli Modül
- **Önizleme Kapsamı (Slayt 1–10):** Giriş, küresel epidemiyoloji, Türkiye obezite haritası ve paradigma değişimi.
- **Şifreli Modüller (Slayt 11–185):** Etiyoloji, patogenez, EASO 2024 evreleme sistemleri, medikal/cerrahi tedavi, TBT stratejileri ve klinik vaka analizleri.
- **Şifre:** Ders izlencesi ve OBS duyuru panosunda ilan edilen öğrenci şifresi ile açılır.
""")

    tr_pres_2 = BASE_DIR / "content/tr/presentations/02-obezite-uygulama.md"
    with open(tr_pres_2, "w", encoding="utf-8") as f:
        f.write("""---
title: "Obezite ve Tıbbi Beslenme Tedavisine Giriş Uygulaması (1. Hafta)"
type: "presentation"
badge: "Klinik Uygulama (BES 317)"
date: "2026-03-01"
slide_count: "59+ Slayt (🔒 AES-256 Korumalı)"
html_url: "slides/02-obezite-uygulama.html"
download_url: ""
summary: "Kalorimetri tarihi, besin değişim listeleri, interaktif makro besin hesaplama simülatörü ve ambalajlı gıda analizleri. İlk 10 slayt açık önizleme; 11+ slaytlar AES-256 şifrelidir."
draft: false
lang: "tr"
order: 2
---

## 💻 Klinik Uygulama Sunumu
- **Önizleme Kapsamı (Slayt 1–10):** Kalori tarihi, Lavoisier ve Atwater kalorimetreleri, besin değişim sistemleri temelleri.
- **Şifreli Modüller (Slayt 11+):** İnteraktif vaka hesaplayıcıları, makro besin optimizasyonları ve sınav pratikleri.
- **Şifre:** Ders izlencesinde paylaşılan öğrenci şifresi ile açılır.
""")

    tr_pres_3 = BASE_DIR / "content/tr/presentations/03-bilgisayar-ve-yapay-zeka.md"
    with open(tr_pres_3, "w", encoding="utf-8") as f:
        f.write("""---
title: "Bilgisayar ve Yapay Zeka Uygulamaları (1. Hafta: AI ile Tanışma)"
type: "presentation"
badge: "Lisans Dersi (BES 200)"
date: "2026-03-01"
slide_count: "79 Slayt (🔒 AES-256 Korumalı)"
html_url: "slides/01-bilgisayar-ve-yapay-zeka.html"
download_url: ""
summary: "Yapay zekanın beslenme bilimine girişi, temel kavramlar matruşkası, makine öğrenmesi, derin öğrenme, üretken AI (GenAI) ve diyetisyenlik uygulamaları. İlk 10 slayt açık önizleme; 11+ slaytlar AES-256 şifrelidir."
draft: false
lang: "tr"
order: 3
---

## 💻 Ders Sunumu & Canlı Kilitli Modül
- **Önizleme Kapsamı (Slayt 1–10):** Yapay zekanın beslenme bilimine girişi, temel kavramlar matruşkası (AI, ML, DL, GenAI) ve diyetisyenlik vizyonu.
- **Şifreli Modüller (Slayt 11–79):** LLM anatomisi, prompt mühendisliği, besin analizinde yapay zeka, klinik vaka uygulamaları ve etik ilkeler.
- **Şifre:** Ders izlencesi ve OBS duyuru panosunda ilan edilen öğrenci şifresi (`COZYBESAI2026_`) ile açılır.
""")

    # English cards
    en_pres_1 = BASE_DIR / "content/en/presentations/01-obesity-medical-nutrition-therapy.md"
    en_pres_1.parent.mkdir(parents=True, exist_ok=True)
    with open(en_pres_1, "w", encoding="utf-8") as f:
        f.write("""---
title: "Obesity and Medical Nutrition Therapy (Topic 1)"
type: "presentation"
badge: "Undergraduate Lecture (NUT 317)"
date: "2026-03-01"
slide_count: "185 Slides (🔒 AES-256 Protected)"
html_url: "slides/01-obezite-ve-tibbi-beslenme-tedavisi.html"
download_url: ""
summary: "From biology to clinic, diagnosis to behavioral modification in obesity. First 10 slides public preview; slides 11+ encrypted with AES-256-GCM."
draft: false
lang: "en"
order: 1
---
""")

    en_pres_2 = BASE_DIR / "content/en/presentations/02-obesity-clinical-practice.md"
    en_pres_2.parent.mkdir(parents=True, exist_ok=True)
    with open(en_pres_2, "w", encoding="utf-8") as f:
        f.write("""---
title: "Introduction to Obesity & Medical Nutrition Therapy Practice (Week 1)"
type: "presentation"
badge: "Clinical Practice (NUT 317)"
date: "2026-03-01"
slide_count: "59+ Slides (🔒 AES-256 Protected)"
html_url: "slides/02-obezite-uygulama.html"
download_url: ""
summary: "Calorimetry history, food exchange systems, interactive macro simulator, and packaged food analyses. First 10 slides public preview; slides 11+ encrypted."
draft: false
lang: "en"
order: 2
---
""")

    en_pres_3 = BASE_DIR / "content/en/presentations/03-computer-and-ai-applications.md"
    en_pres_3.parent.mkdir(parents=True, exist_ok=True)
    with open(en_pres_3, "w", encoding="utf-8") as f:
        f.write("""---
title: "Computer & AI Applications in Nutrition (Week 1: Intro to AI)"
type: "presentation"
badge: "Undergraduate Lecture (NUT 200)"
date: "2026-03-01"
slide_count: "79 Slides (🔒 AES-256 Protected)"
html_url: "slides/01-bilgisayar-ve-yapay-zeka.html"
download_url: ""
summary: "Introduction of artificial intelligence to nutritional sciences, core concepts, ML, DL, generative AI, and dietetic practice. First 10 slides public preview; slides 11+ encrypted."
draft: false
lang: "en"
order: 3
---
""")

    # Rebuild website
    print("🚀 Web sitesi yeniden derleniyor (build.py)...")
    res = subprocess.run(["python3", str(BASE_DIR / "build.py")], capture_output=True, text=True)
    print(res.stdout)

def main():
    print("🔄 Obsidian Vault -> Web Sitesi Sunum Senkronizasyonu Başlatılıyor...\n")
    print(f"🔑 Şifreler: YHTBT: {DEFAULT_PASSWORD} | BES AI: {AI_PASSWORD}\n")
    sync_assets()
    sync_konu1_obezite()
    sync_obezite_uygulama()
    sync_bilgisayar_yapay_zeka()
    update_markdown_and_rebuild()
    print("🎉 Senkronizasyon ve AES-256 Şifreleme Tamamlandı!")

if __name__ == "__main__":
    main()
