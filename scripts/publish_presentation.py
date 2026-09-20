#!/usr/bin/env python3
"""
Tek Komutla Akademik Sunum Şifreleme, Entegrasyon ve Yayınlama Motoru
Dr. Caner ÖZYILDIRIM — Kişisel Web Sitesi Altyapısı

Kullanım:
    python3 scripts/publish_presentation.py <html_dosyasi> [opsiyonlar]

Örnekler:
    python3 scripts/publish_presentation.py slides/yeni_sunum.html --course BES339 --deploy
    python3 scripts/publish_presentation.py slides/hafta2.html --course BES200 --title "Makine Öğrenmesi" --deploy
"""

import os
import sys
import re
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("/Users/canerozyildirim/Sites/personalwebsite").resolve()
SLIDES_DIR = BASE_DIR / "slides"
ASSETS_DIR = SLIDES_DIR / "assets"
CONTENT_DIR = BASE_DIR / "content"

# DERS VE ŞİFRE KAYIT MATRİSİ
COURSE_REGISTRY = {
    "BES339": {
        "name_tr": "Diyet İlkeleri ve Popüler Diyetler",
        "name_en": "Principles of Nutrition and Popular Diets",
        "code": "BES 339",
        "code_en": "NUT 339",
        "badge_tr": "Lisans Modülü",
        "badge_en": "Undergraduate Module",
        "password": "COZYPOP2026_",
        "tr_teaching_file": "content/tr/teaching/04-diyet-ilkeleri-ve-populer-diyetler.md",
        "en_teaching_file": "content/en/teaching/04-dietary-principles-and-popular-diets.md",
        "pres_prefix": "04",
        "keywords": ["popüler", "evrim", "popular", "evolution", "bes339", "diyet ilkeleri"]
    },
    "BES200": {
        "name_tr": "Beslenme ve Diyetetikte Bilgisayar ve Yapay Zeka Uygulamaları",
        "name_en": "Computer & AI Applications in Nutrition",
        "code": "BES 200",
        "code_en": "NUT 200",
        "badge_tr": "Lisans Modülü",
        "badge_en": "Undergraduate Module",
        "password": "COZYBESAI2026_",
        "tr_teaching_file": "content/tr/teaching/01-bilgisayar-ve-yapay-zeka.md",
        "en_teaching_file": "content/en/teaching/01-computer-and-ai-applications.md",
        "pres_prefix": "03",
        "keywords": ["yapay zeka", "ai", "bilgisayar", "bes200", "genai", "prompt"]
    },
    "BES317": {
        "name_tr": "Yetişkin Hastalıklarında Diyet Tedavisi (Teorik & Uygulama)",
        "name_en": "Medical Nutrition Therapy in Adult Diseases",
        "code": "BES 317 - BES 318",
        "code_en": "NUT 317",
        "badge_tr": "Lisans Dersi",
        "badge_en": "Clinical Lecture",
        "password": "COZYYHTBT2026_",
        "tr_teaching_file": "content/tr/teaching/06-yetiskin-hastaliklarinda-diyet-tedavisi.md",
        "en_teaching_file": "content/en/teaching/06-medical-nutrition-therapy.md",
        "pres_prefix": "01",
        "keywords": ["obezite", "obesity", "yhtbt", "bes317", "klinik", "diyabet", "ncp"]
    }
}

def slugify(text: str) -> str:
    text = text.lower().strip()
    tr_map = str.maketrans("çğıöşü", "cgiosu")
    text = text.translate(tr_map)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def detect_course_from_content(html: str) -> str:
    html_lower = html.lower()
    for c_key, c_info in COURSE_REGISTRY.items():
        for kw in c_info["keywords"]:
            if kw in html_lower:
                return c_key
    return "BES339"  # Varsayılan

def encrypt_aes_payload(plaintext: str, password: str) -> str:
    node_script = """
const CryptoJS = require('crypto-js');
const input = JSON.parse(process.argv[1]);
const ciphertext = CryptoJS.AES.encrypt(input.plaintext, input.password).toString();
console.log(ciphertext);
"""
    payload = {"plaintext": plaintext, "password": password}
    res = subprocess.run(
        ["node", "-e", node_script, json.dumps(payload)],
        capture_output=True,
        text=True,
        check=True
    )
    return res.stdout.strip()

def get_lock_modal_html(course_code: str, course_name: str) -> str:
    return f"""
<!-- STUDENT PASSWORD LOCK MODAL -->
<div id="student-lock-modal" style="display:none; position:fixed; inset:0; background:rgba(11,17,29,0.88); backdrop-filter:blur(10px); z-index:99999; align-items:center; justify-content:center; padding:20px; font-family:'Inter', system-ui, sans-serif;">
  <div id="modal-card" style="background:#131d2e; border:1px solid #233554; border-radius:24px; max-width:440px; width:100%; padding:32px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.6); text-align:center; position:relative; color:#f8fafc;">
    <button type="button" onclick="closeLockModal()" style="position:absolute; top:16px; right:16px; background:none; border:none; color:#94a3b8; font-size:20px; cursor:pointer; padding:4px 8px; border-radius:8px;">✕</button>
    <div style="width:64px; height:64px; border-radius:18px; background:rgba(217,119,6,0.15); border:1px solid rgba(217,119,6,0.3); color:#fbbf24; display:flex; align-items:center; justify-content:center; font-size:26px; margin:0 auto 16px;">🔒</div>
    <h3 style="font-size:20px; font-weight:700; margin:0 0 8px; color:#ffffff;">Öğrenci Kilit Ekranı</h3>
    <p style="font-size:13px; color:#94a3b8; line-height:1.6; margin:0 0 24px;">10 slaytlık açık önizleme tamamlanmıştır. Dersin devamını görüntülemek için lütfen {course_code} ders şifrenizi giriniz.</p>
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
        ⚠️ Hatalı şifre! Lütfen {course_code} ders izlencesindeki şifrenizi kontrol ediniz.
      </div>
      <button type="submit" id="unlock-submit-btn" style="width:100%; background:linear-gradient(135deg, #d97706, #b45309); color:#ffffff; font-weight:700; border:none; border-radius:12px; padding:14px; font-size:14px; cursor:pointer; box-shadow:0 10px 15px -3px rgba(217,119,6,0.3); transition:transform 0.1s;">
        🔓 Şifreyi Çöz &amp; Derse Devam Et
      </button>
    </form>
    <div style="margin-top:20px; padding-top:16px; border-top:1px solid #1e293b; font-size:11px; color:#64748b; display:flex; align-items:center; justify-content:center; gap:6px;">
      <span>🔒</span> <span>{course_code} • {course_name}</span>
    </div>
  </div>
</div>
<style>
@keyframes modalShake {{
  0%, 100% {{ transform: translateX(0); }}
  20%, 60% {{ transform: translateX(-8px); }}
  40%, 80% {{ transform: translateX(8px); }}
}}
.modal-shake {{ animation: modalShake 0.4s ease-in-out; }}
</style>
"""

def process_and_encrypt(input_path: Path, course_key: str, custom_password: str = None) -> tuple[Path, int, str]:
    with open(input_path, "r", encoding="utf-8") as f:
        html = f.read()

    course_info = COURSE_REGISTRY[course_key]
    password = custom_password or course_info["password"]
    pres_id = slugify(input_path.stem)

    # 1. Başlık ve Slayt Yapısını Çözümle
    title_m = re.search(r'<title>(.*?)(?:\|.*)?</title>', html, re.IGNORECASE)
    pres_title = title_m.group(1).strip() if title_m else input_path.stem.replace('_', ' ').title()

    crypto_js_file = ASSETS_DIR / "crypto-js.min.js"
    with open(crypto_js_file, "r", encoding="utf-8") as f:
        crypto_js_code = f.read()

    # JSON TABANLI SUNUM MİMARİSİ (const SLIDES = [...])
    if "const SLIDES = [" in html:
        pos = html.find("const SLIDES = [")
        sub = html[pos + len("const SLIDES = ["):]
        end_pos = sub.find("];\n")
        if end_pos == -1: end_pos = sub.find("];")
        slides_json_str = "[" + sub[:end_pos] + "]"
        all_slides = json.loads(slides_json_str)
        total_slides = len(all_slides)
        public_slides = all_slides[:10]
        locked_slides = all_slides[10:]

        ciphertext = encrypt_aes_payload(json.dumps(locked_slides, ensure_ascii=False), password)
        
        # HTML içine sadece ilk 10 slaytı yerleştir
        public_slides_str = json.dumps(public_slides, indent=2, ensure_ascii=False)
        new_html = html[:pos + len("const SLIDES = ")] + public_slides_str + html[pos + len("const SLIDES = [") + end_pos + 1:]
        
        # Slayt sayısını ve motoru güncelle
        new_html = new_html.replace("const totalSlides = SLIDES.length;", f"let totalSlides = {total_slides};")

        # Kilit Banner'ı
        banner_code = f"""
            if (!isUnlocked && num === 10) {{
                const lockBanner = document.createElement('div');
                lockBanner.className = 'mt-6 p-4 rounded-2xl bg-amber-50/90 border border-amber-300 flex flex-col sm:flex-row items-center justify-between gap-3 select-none';
                lockBanner.innerHTML = `
                    <div class="flex items-center space-x-3 text-left">
                        <span class="text-2xl shrink-0">🔒</span>
                        <div>
                            <p class="text-xs font-bold text-amber-950 font-serif">10 Slaytlık Açık Önizleme Sınırı</p>
                            <p class="text-[11px] text-amber-800">Devamındaki modüller (Slayt 11-{total_slides}) {course_info['code']} öğrenci şifresiyle korunmaktadır.</p>
                        </div>
                    </div>
                    <button type="button" onclick="openLockModal(10)" class="w-full sm:w-auto px-4 py-2 bg-gradient-to-r from-amber-700 to-amber-800 hover:from-amber-800 hover:to-amber-900 text-white text-xs font-bold rounded-xl transition shadow-sm shrink-0 flex items-center justify-center space-x-2 cursor-pointer">
                        <span>🔓</span>
                        <span>Ders Şifresini Gir &amp; Devam Et</span>
                    </button>
                `;
                bodyEl.appendChild(lockBanner);
            }}
"""
        pos_split = new_html.find("bodyEl.appendChild(split);")
        if pos_split != -1:
            new_html = new_html.replace("bodyEl.appendChild(split);", "bodyEl.appendChild(split);\n" + banner_code)

        # Navigasyon kancaları
        new_html = new_html.replace(
            "function nextSlide() {\n            if (currentSlideIdx < totalSlides - 1) {",
            "function nextSlide() {\n            if (!isUnlocked && currentSlideIdx >= 9) { openLockModal(10); return; }\n            if (currentSlideIdx < totalSlides - 1) {"
        )
        new_html = new_html.replace(
            "function goToSlide(idx) {\n            if (idx >= 0 && idx < totalSlides) {",
            "function goToSlide(idx) {\n            if (!isUnlocked && idx >= 10) { openLockModal(idx); return; }\n            if (idx >= 0 && idx < totalSlides) {"
        )

        modal_html = get_lock_modal_html(course_info["code"], course_info["name_tr"])
        client_script = f"""
<!-- INLINED CRYPTOJS ENGINE -->
<script>
{crypto_js_code}
</script>

<script id="encrypted-payload-data" type="text/plain">
{ciphertext}
</script>

{modal_html}

<script>
var PRES_ID = "{pres_id}";
var PUBLIC_SLIDE_COUNT = 10;
var TOTAL_SLIDES_COUNT = {total_slides};
var isUnlocked = false;
var pendingTargetSlide = null;
var encryptedPayloadCiphertext = "";

document.addEventListener('DOMContentLoaded', () => {{
  const scriptTag = document.getElementById('encrypted-payload-data');
  if (scriptTag) encryptedPayloadCiphertext = scriptTag.textContent.trim();
  checkSessionUnlock();
}});

function getPasswordCandidates(inputStr) {{
  const p = (inputStr || '').trim();
  if (!p) return [];
  const set = new Set([p, p.toUpperCase(), p.toLowerCase(), p.toLocaleUpperCase('tr-TR')]);
  if (!p.endsWith('_')) set.add(p + '_');
  else set.add(p.replace(/_+$/, ''));
  return Array.from(set);
}}

function decryptPayload(ciphertext, passwordInput) {{
  for (const cand of getPasswordCandidates(passwordInput)) {{
    try {{
      const dec = CryptoJS.AES.decrypt(ciphertext, cand).toString(CryptoJS.enc.Utf8);
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
  submitBtn.disabled = true;
  submitBtn.innerHTML = '⏳ Şifre Çözülüyor...';
  if (errorEl) errorEl.style.display = 'none';

  try {{
    const decryptedJson = decryptPayload(encryptedPayloadCiphertext, password);
    const lockedList = JSON.parse(decryptedJson);
    applyDecryptedSlides(lockedList);
    try {{ localStorage.setItem('unlocked_pres_' + PRES_ID, decryptedJson); }} catch(e) {{}}
    closeLockModal();
    if (pendingTargetSlide !== null) {{
      const target = pendingTargetSlide;
      pendingTargetSlide = null;
      goToSlide(target);
    }} else {{
      goToSlide(PUBLIC_SLIDE_COUNT);
    }}
  }} catch(err) {{
    if (errorEl) {{
      errorEl.textContent = '⚠️ Hatalı şifre! Lütfen {course_info["code"]} ders şifrenizi kontrol ediniz.';
      errorEl.style.display = 'block';
    }}
    if (modalCard) {{
      modalCard.classList.remove('modal-shake');
      void modalCard.offsetWidth;
      modalCard.classList.add('modal-shake');
    }}
  }} finally {{
    submitBtn.disabled = false;
    submitBtn.innerHTML = '🔓 Şifreyi Çöz &amp; Derse Devam Et';
  }}
}}

function checkSessionUnlock() {{
  try {{
    const cached = localStorage.getItem('unlocked_pres_' + PRES_ID);
    if (cached) applyDecryptedSlides(JSON.parse(cached));
  }} catch(e) {{}}
}}

function applyDecryptedSlides(lockedList) {{
  if (isUnlocked) return;
  isUnlocked = true;
  if (SLIDES.length <= PUBLIC_SLIDE_COUNT) {{
    lockedList.forEach(s => SLIDES.push(s));
  }}
  totalSlides = SLIDES.length;
  const totalCounter = document.getElementById('counter-total');
  if (totalCounter) totalCounter.innerText = String(totalSlides);
  if (typeof buildOverviewGrid === 'function') buildOverviewGrid();
  if (typeof renderSlide === 'function') renderSlide();
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
        body_pos = new_html.rfind("</body>")
        final_html = new_html[:body_pos] + client_script + "\n" + new_html[body_pos:]
    else:
        # Standart HTML section tabanlı mimari
        total_slides = 50 # varsayılan
        final_html = html

    # Dosyayı kaydet
    out_name = f"{slugify(pres_title)}.html"
    if not out_name.startswith("0") and not out_name.startswith("1"):
        out_name = f"01-{out_name}"
    out_path = SLIDES_DIR / out_name

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    # Orijinal dosyayı da koru/senkronize et
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    return out_path, total_slides, pres_title

def update_course_and_presentations(course_key: str, slide_path: Path, total_slides: int, pres_title: str):
    c_info = COURSE_REGISTRY[course_key]
    rel_slide_url = f"slides/{slide_path.name}"
    today_str = datetime.now().strftime("%Y-%m-%d")

    # 1. TR Presentation Markdown
    pres_slug = slugify(pres_title)
    tr_pres_file = CONTENT_DIR / f"tr/presentations/{c_info['pres_prefix']}-{pres_slug}.md"
    tr_pres_file.parent.mkdir(parents=True, exist_ok=True)
    with open(tr_pres_file, "w", encoding="utf-8") as f:
        f.write(f"""---
title: "{pres_title}"
type: "presentation"
badge: "{c_info['badge_tr']} ({c_info['code']})"
date: "{today_str}"
slide_count: "{total_slides} Slayt (🔒 AES-256 Korumalı)"
html_url: "{rel_slide_url}"
download_url: ""
summary: "{pres_title} dersi interaktif web sunumu. İlk 10 slayt açık önizleme; 11+ slaytlar AES-256 şifrelidir."
draft: false
lang: "tr"
order: 4
---

## 🧬 Ders Sunumu & Canlı Kilitli Modül
- **Önizleme Kapsamı (Slayt 1–10):** Açık akademik önizleme ve giriş kavramları.
- **Şifreli Modüller (Slayt 11–{total_slides}):** İleri modüller, vaka analizleri ve uygulamalar.
- **Şifre:** {c_info['code']} ders izlencesinde ilan edilen öğrenci şifresi (`{c_info['password']}`) ile açılır.
""")

    # 2. EN Presentation Markdown
    en_pres_file = CONTENT_DIR / f"en/presentations/{c_info['pres_prefix']}-{pres_slug}.md"
    en_pres_file.parent.mkdir(parents=True, exist_ok=True)
    with open(en_pres_file, "w", encoding="utf-8") as f:
        f.write(f"""---
title: "{pres_title}"
type: "presentation"
badge: "{c_info['badge_en']} ({c_info['code_en']})"
date: "{today_str}"
slide_count: "{total_slides} Slides (🔒 AES-256 Protected)"
html_url: "{rel_slide_url}"
download_url: ""
summary: "{pres_title} interactive web presentation. First 10 slides public preview; slides 11+ encrypted."
draft: false
lang: "en"
order: 4
---

## 🧬 Lecture Deck & Protected Content
- **Public Preview (Slides 1–10):** Open preview.
- **Encrypted Modules (Slides 11–{total_slides}):** Protected with AES-256.
- **Access Passcode:** Unlocked with `{c_info['password']}`.
""")

    # 3. TR Teaching Dosyasını Güncelle
    tr_teach = BASE_DIR / c_info["tr_teaching_file"]
    if tr_teach.exists():
        with open(tr_teach, "r", encoding="utf-8") as f:
            t_content = f.read()

        # Frontmatter slides_url güncelle
        if "slides_url:" in t_content:
            t_content = re.sub(r'slides_url:\s*".*?"', f'slides_url: "../{rel_slide_url}"', t_content)
            t_content = re.sub(r'slides_title:\s*".*?"', f'slides_title: "{c_info["code"]}: {pres_title} ({total_slides} Slayt - Canlı İzle)"', t_content)
        else:
            t_content = t_content.replace("draft: false", f'slides_url: "../{rel_slide_url}"\nslides_title: "{c_info["code"]}: {pres_title} ({total_slides} Slayt - Canlı İzle)"\nslides_badge: "İlk 10 slayt açık önizleme • 🔒 AES-256 Korumalı • Şifre: {c_info["password"]}"\ndraft: false')

        # Link satırını güncelle veya ekle
        link_md = f"- 👉 [**{pres_title} ({total_slides} Slayt - Canlı İzle)**](../{rel_slide_url}) *(🔒 AES-256 Korumalı — Şifre: `{c_info['password']}`)*"
        if "## 📊 İnteraktif Ders Sunumları" in t_content or "## 📊 İnteraktif Ders Sunumu" in t_content:
            if rel_slide_url not in t_content:
                t_content = re.sub(r'(## 📊 İnteraktif Ders Sunum[^\n]*\n[^\n]*\n)', r'\1\n' + link_md + '\n', t_content)
        else:
            t_content += f"\n\n## 📊 İnteraktif Ders Sunumları & Öğrenci Kilit Ekranı\nBu dersin canlı ve interaktif web sunumuna aşağıdaki bağlantıdan erişebilirsiniz.\n\n{link_md}\n"

        with open(tr_teach, "w", encoding="utf-8") as f:
            f.write(t_content)

def main():
    parser = argparse.ArgumentParser(description="Sunum Şifreleme, Entegrasyon ve Yayınlama Motoru")
    parser.add_argument("file", help="İşlenecek HTML sunum dosyası yolu")
    parser.add_argument("--course", choices=list(COURSE_REGISTRY.keys()), help="Ders kodu (BES339, BES200, BES317)")
    parser.add_argument("--password", help="Özel şifre (belirtilmezse ders şifresi kullanılır)")
    parser.add_argument("--title", help="Özel sunum başlığı")
    parser.add_argument("--deploy", action="store_true", help="Build sonrası git push ile anında canlıya al")

    args = parser.parse_args()
    input_path = Path(args.file).resolve()

    if not input_path.exists():
        print(f"❌ Dosya bulunamadı: {input_path}")
        sys.exit(1)

    course_key = args.course or detect_course_from_content(input_path.read_text(encoding="utf-8", errors="ignore"))
    print(f"🎯 Hedef Ders: {course_key} ({COURSE_REGISTRY[course_key]['name_tr']})")
    print(f"🔑 Kullanılacak Şifre: {args.password or COURSE_REGISTRY[course_key]['password']}")

    # 1. Şifreleme ve Paketleme
    out_slide_path, total_slides, pres_title = process_and_encrypt(input_path, course_key, args.password)
    if args.title: pres_title = args.title
    print(f"✅ Sunum şifrelendi: {out_slide_path.name} ({total_slides} slayt)")

    # 2. Markdown Kartları ve Ders Sayfası Entegrasyonu
    update_course_and_presentations(course_key, out_slide_path, total_slides, pres_title)
    print("✅ Ders ve sunum markdown dosyaları güncellendi.")

    # 3. Web Sitesi Derleme
    print("🚀 Web sitesi derleniyor (build.py)...")
    res = subprocess.run(["python3", str(BASE_DIR / "build.py")], capture_output=True, text=True)
    print("  " + res.stdout.replace("\n", "\n  ").strip())

    # 4. Git Deploy
    if args.deploy:
        print("🌐 Canlıya alınıyor (git commit & push)...")
        subprocess.run(["git", "add", "."], cwd=BASE_DIR, check=True)
        commit_msg = f"feat(slides): {pres_title} ({course_key}) şifrelendi ve yayına alındı"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=BASE_DIR, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
        print("🎉 Başarıyla GitHub Pages'e deploy edildi ve yayına girdi!")
    else:
        print("💡 Değişiklikler hazırlandı. Yayına almak için: git push origin main")

if __name__ == "__main__":
    main()
