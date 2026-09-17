#!/usr/bin/env python3
"""
Obsidian Vault to Academic Website Presentation Synchronizer & AES-256 Encryptor
Dr. Caner ÖZYILDIRIM Website Suite

This script:
1. Copies all simulation files and image assets directly from the Obsidian Vault to slides/assets/.
2. Reads HTML presentation files directly from the Obsidian Vault.
3. Applies AES-256-GCM + PBKDF2 encryption to slides 11+ (keeping first 10 slides as public preview).
4. Integrates the Web Crypto API decryption engine with flexible candidate matching, student lock modal, and Table of Contents jump interceptor.
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

def sync_assets():
    """Copies all simulation HTML files, PNG assets, and logos from Vault to slides/assets/."""
    print("📦 Sunum asset'leri ve simülasyonları kopyalanıyor...")
    vault_assets_dir = VAULT_DIR / "Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/Sunumlar/assets"
    copied_count = 0
    
    if vault_assets_dir.exists():
        for item in vault_assets_dir.iterdir():
            if item.is_file() and not item.name.startswith('.'):
                dest = SLIDES_ASSETS_DIR / item.name
                shutil.copy2(item, dest)
                copied_count += 1
        print(f"  ✅ {copied_count} asset dosyası '{SLIDES_ASSETS_DIR}' dizinine kopyalandı.")
    else:
        print(f"  ⚠️ Vault assets dizini bulunamadı: {vault_assets_dir}")

    # Copy faculty logo
    faculty_logo = VAULT_DIR / "Files/Saglik-Bilimleri-Fakultesi-2.png"
    if faculty_logo.exists():
        dest_logo = SLIDES_ASSETS_DIR / "Saglik-Bilimleri-Fakultesi-2.png"
        shutil.copy2(faculty_logo, dest_logo)
        print("  ✅ Fakülte logosu kopyalandı.")

def encrypt_aes_gcm(plaintext: str, password: str) -> dict:
    """Encrypts plaintext with PBKDF2 + AES-256-GCM (Web Crypto API compatible)."""
    salt = os.urandom(16)
    iv = os.urandom(12)
    iterations = 100000

    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations, dklen=32)
        aesgcm = AESGCM(key)
        cipher_bytes = aesgcm.encrypt(iv, plaintext.encode('utf-8'), None)
        return {
            "salt": base64.b64encode(salt).decode('utf-8'),
            "iv": base64.b64encode(iv).decode('utf-8'),
            "ciphertext": base64.b64encode(cipher_bytes).decode('utf-8'),
            "iterations": iterations
        }
    except ImportError:
        node_script = """
const crypto = require('crypto');
const input = JSON.parse(process.argv[1]);
const salt = Buffer.from(input.salt, 'base64');
const iv = Buffer.from(input.iv, 'base64');
const key = crypto.pbkdf2Sync(input.password, salt, input.iterations, 32, 'sha256');
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
let encrypted = cipher.update(input.plaintext, 'utf8');
encrypted = Buffer.concat([encrypted, cipher.final(), cipher.getAuthTag()]);
console.log(JSON.stringify({
    salt: input.salt,
    iv: input.iv,
    ciphertext: encrypted.toString('base64'),
    iterations: input.iterations
}));
"""
        payload = {
            "salt": base64.b64encode(salt).decode('utf-8'),
            "iv": base64.b64encode(iv).decode('utf-8'),
            "plaintext": plaintext,
            "password": password,
            "iterations": iterations
        }
        res = subprocess.run(
            ["node", "-e", node_script, json.dumps(payload)],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(res.stdout.strip())

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
      <span>🛡️</span> <span>Web Crypto API (AES-256-GCM) ile yerel çözülür.</span>
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

    # Encrypt locked slides
    encrypted_payload = encrypt_aes_gcm(json.dumps(locked_slides), DEFAULT_PASSWORD)
    encrypted_payload["totalSlides"] = total_slides
    encrypted_payload["publicSlideCount"] = public_count
    encrypted_payload["lockedSlideCount"] = len(locked_slides)
    encrypted_payload["presId"] = "konu1_obezite_tedavisi"

    # Build new public SLIDES string
    new_public_slides_str = json.dumps(public_slides, indent=2, ensure_ascii=False)
    
    # Replace SLIDES array in HTML
    new_html = html[:pos + len('const SLIDES = ')] + new_public_slides_str + html[pos + len('const SLIDES = [') + end_pos + 1:]

    # Client-side script
    payload_json = json.dumps(encrypted_payload, indent=2)
    client_crypto_script = """
<!-- AES-256-GCM ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data" type="application/json">
""" + payload_json + """
</script>

""" + LOCK_MODAL_HTML + """

<script>
/* ================= STUDENT LOCK & WEB CRYPTO API ENGINE ================= */
const PRES_ID = "konu1_obezite_tedavisi";
const PUBLIC_SLIDE_COUNT = """ + str(public_count) + """;
const TOTAL_SLIDES_COUNT = """ + str(total_slides) + """;
let isUnlocked = false;
let pendingTargetSlide = null;
let encryptedPayload = null;

document.addEventListener('DOMContentLoaded', () => {
  const scriptTag = document.getElementById('encrypted-payload-data');
  if(scriptTag) {
    try { encryptedPayload = JSON.parse(scriptTag.textContent); } catch(e){}
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

async function decryptWithCandidate(cand) {
  const saltBytes = Uint8Array.from(atob(encryptedPayload.salt), c => c.charCodeAt(0));
  const ivBytes = Uint8Array.from(atob(encryptedPayload.iv), c => c.charCodeAt(0));
  const cipherBytes = Uint8Array.from(atob(encryptedPayload.ciphertext), c => c.charCodeAt(0));
  const iterations = encryptedPayload.iterations || 100000;

  const enc = new TextEncoder();
  const baseKey = await window.crypto.subtle.importKey(
    "raw", enc.encode(cand), { name: "PBKDF2" }, false, ["deriveKey"]
  );
  const derivedKey = await window.crypto.subtle.deriveKey(
    { name: "PBKDF2", salt: saltBytes, iterations: iterations, hash: "SHA-256" },
    baseKey, { name: "AES-GCM", length: 256 }, false, ["decrypt"]
  );
  const decryptedBuf = await window.crypto.subtle.decrypt(
    { name: "AES-GCM", iv: ivBytes }, derivedKey, cipherBytes
  );
  return new TextDecoder("utf-8").decode(decryptedBuf);
}

async function decryptPayload(passwordInput) {
  if (!encryptedPayload) return null;
  const candidates = getPasswordCandidates(passwordInput);
  let lastErr = null;
  for (const cand of candidates) {
    try {
      const res = await decryptWithCandidate(cand);
      if (res) return res;
    } catch(err) {
      lastErr = err;
    }
  }
  throw lastErr || new Error("Şifre çözülemedi.");
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

  try {
    const decryptedJson = await decryptPayload(password);
    const lockedList = JSON.parse(decryptedJson);
    applyDecryptedSlides(lockedList);
    sessionStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJson);
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
  } catch(err) {
    console.error("Şifre çözme hatası:", err);
    errorEl.style.display = 'block';
    modalCard.classList.remove('modal-shake');
    void modalCard.offsetWidth;
    modalCard.classList.add('modal-shake');
    input.focus();
    input.select();
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
  }
}

function checkSessionUnlock() {
  const cached = sessionStorage.getItem('unlocked_pres_' + PRES_ID);
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
    }}
  );
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

    # Patch allSlideEls & total
    new_html = new_html.replace('const allSlideEls = Array.from(stage.children);', 'let allSlideEls = Array.from(stage.children);')
    new_html = new_html.replace('const total = SLIDES.length;', 'let total = SLIDES.length;')
    
    # Intercept go(idx) for lock
    go_orig = "function go(idx){\n  if(idx<0||idx>=total) return;"
    go_patched = """function go(idx){
  if(idx >= PUBLIC_SLIDE_COUNT && !isUnlocked){
    openLockModal(idx);
    return;
  }
  if(idx<0||idx>=total) return;"""
    new_html = new_html.replace(go_orig, go_patched)

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

    # Find the split point in slide registration
    pos_end = html.find('/* ---- Egzersiz 3 (Set B, eşit gramaj) ---- */')
    pos_boot = html.find('function boot(){')

    if pos_end != -1 and pos_boot != -1:
        public_head = html[:pos_end]
        locked_js = html[pos_end:pos_boot]
        rest_html = html[pos_boot:]

        # Add preview end slide registration to public head
        preview_reg = """
addSlide('🛑 Önizleme Sınırı', 'Önizleme Sonu (Slayt 10)', 'Önizleme Sonu',
  slideIntro('🔒', '10 Slaytlık Önizleme Tamamlanmıştır', 'Devamını görüntülemek için ders şifresi girilmesi gerekmektedir.'));
"""
        public_head = public_head + preview_reg

        # Encrypt locked JS registration script
        encrypted_payload = encrypt_aes_gcm(locked_js, DEFAULT_PASSWORD)
        encrypted_payload["presId"] = "obezite_uygulama_hafta1"
        payload_json = json.dumps(encrypted_payload, indent=2)

        client_crypto_script = """
<!-- AES-256-GCM ENCRYPTED STUDENT PAYLOAD -->
<script id="encrypted-payload-data-uygulama" type="application/json">
""" + payload_json + """
</script>

""" + LOCK_MODAL_HTML + """

<script>
/* ================= STUDENT LOCK & WEB CRYPTO API ENGINE ================= */
const PRES_ID = "obezite_uygulama_hafta1";
const PUBLIC_SLIDE_COUNT = 10;
let isUnlocked = false;
let pendingTargetSlide = null;
let encryptedPayload = null;

document.addEventListener('DOMContentLoaded', () => {
  const scriptTag = document.getElementById('encrypted-payload-data-uygulama');
  if(scriptTag) {
    try { encryptedPayload = JSON.parse(scriptTag.textContent); } catch(e){}
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

async function decryptWithCandidate(cand) {
  const saltBytes = Uint8Array.from(atob(encryptedPayload.salt), c => c.charCodeAt(0));
  const ivBytes = Uint8Array.from(atob(encryptedPayload.iv), c => c.charCodeAt(0));
  const cipherBytes = Uint8Array.from(atob(encryptedPayload.ciphertext), c => c.charCodeAt(0));
  const iterations = encryptedPayload.iterations || 100000;

  const enc = new TextEncoder();
  const baseKey = await window.crypto.subtle.importKey(
    "raw", enc.encode(cand), { name: "PBKDF2" }, false, ["deriveKey"]
  );
  const derivedKey = await window.crypto.subtle.deriveKey(
    { name: "PBKDF2", salt: saltBytes, iterations: iterations, hash: "SHA-256" },
    baseKey, { name: "AES-GCM", length: 256 }, false, ["decrypt"]
  );
  const decryptedBuf = await window.crypto.subtle.decrypt(
    { name: "AES-GCM", iv: ivBytes }, derivedKey, cipherBytes
  );
  return new TextDecoder("utf-8").decode(decryptedBuf);
}

async function decryptPayload(passwordInput) {
  if (!encryptedPayload) return null;
  const candidates = getPasswordCandidates(passwordInput);
  let lastErr = null;
  for (const cand of candidates) {
    try {
      const res = await decryptWithCandidate(cand);
      if (res) return res;
    } catch(err) {
      lastErr = err;
    }
  }
  throw lastErr || new Error("Şifre çözülemedi.");
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

  try {
    const decryptedJs = await decryptPayload(password);
    applyDecryptedUygulama(decryptedJs);
    sessionStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJs);
    isUnlocked = true;
    closeLockModal();
    
    if (pendingTargetSlide !== null && pendingTargetSlide !== undefined) {
      const target = pendingTargetSlide;
      pendingTargetSlide = null;
      goTo(target);
    } else {
      goTo(PUBLIC_SLIDE_COUNT);
    }
  } catch(err) {
    console.error("Şifre çözme hatası:", err);
    errorEl.style.display = 'block';
    modalCard.classList.remove('modal-shake');
    void modalCard.offsetWidth;
    modalCard.classList.add('modal-shake');
    input.focus();
    input.select();
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz & Derse Devam Et';
  }
}

function checkSessionUnlock() {
  const cached = sessionStorage.getItem('unlocked_pres_' + PRES_ID);
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
  // Execute decrypted registration script in memory
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

        # Intercept goTo(idx)
        orig_goto = "function goTo(idx){\n  if (idx < 0 || idx >= SLIDES.length) return;"
        patched_goto = """function goTo(idx){
  if (idx >= PUBLIC_SLIDE_COUNT && !isUnlocked){
    openLockModal(idx);
    return;
  }
  if (idx < 0 || idx >= SLIDES.length) return;"""
        rest_html = rest_html.replace(orig_goto, patched_goto)

        new_html = public_head + rest_html
        new_html = new_html.replace('</body>', f'{client_crypto_script}\n</body>')
    else:
        new_html = html

    out_file = SLIDES_OUTPUT_DIR / "02-obezite-uygulama.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ Kaydedildi: {out_file} ({os.path.getsize(out_file) / 1024:.1f} KB)\n")
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

    # Rebuild website
    print("🚀 Web sitesi yeniden derleniyor (build.py)...")
    res = subprocess.run(["python3", str(BASE_DIR / "build.py")], capture_output=True, text=True)
    print(res.stdout)

def main():
    print("🔄 Obsidian Vault -> Web Sitesi Sunum Senkronizasyonu Başlatılıyor...\n")
    print(f"🔑 Şifre: {DEFAULT_PASSWORD}\n")
    sync_assets()
    sync_konu1_obezite()
    sync_obezite_uygulama()
    update_markdown_and_rebuild()
    print("🎉 Senkronizasyon ve AES-256 Şifreleme Tamamlandı!")

if __name__ == "__main__":
    main()
