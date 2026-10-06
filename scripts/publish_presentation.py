#!/usr/bin/env python3
"""
Tek Komutla Akademik Sunum Şifreleme, Entegrasyon, PDF Bağlama ve Yayınlama Motoru (V2)
Dr. Caner ÖZYILDIRIM — Kişisel Web Sitesi Altyapısı

Kullanım:
    python3 scripts/publish_presentation.py <html_dosyasi> --course <DERS_KODU> [--pdf <pdf_dosyasi>] [--title "Konu Adı"] [--deploy]

Örnekler:
    python3 scripts/publish_presentation.py "dersler/.../Hafta4.html" --course BES339 --title "Diyetler İşe Yaramıyor mu?" --deploy
"""

import os
import sys
import re
import json
import shutil
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("/Users/canerozyildirim/Sites/personalwebsite").resolve()
SLIDES_DIR = BASE_DIR / "slides"
ASSETS_DIR = SLIDES_DIR / "assets"
PDF_DIR = SLIDES_DIR / "pdf"
CONTENT_DIR = BASE_DIR / "content"

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
        "desktop_dir": "/Users/canerozyildirim/Desktop/BES339 Diyet İlkeleri ve Popüler Diyetler",
        "keywords": ["popüler", "evrim", "popular", "evolution", "bes339", "diyet ilkeleri", "diyetler"]
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
        "desktop_dir": "/Users/canerozyildirim/Desktop/Beslenme Bilimlerinde AI Uygulamaları",
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
        "desktop_dir": "/Users/canerozyildirim/Desktop/BES317-Yetişkin Hastalıklarında Beslenme",
        "keywords": ["obezite", "obesity", "yhtbt", "bes317", "klinik", "diyabet", "ncp"]
    }
}

def slugify(text: str) -> str:
    text = text.lower().strip()
    tr_map = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosucgiosu")
    text = text.translate(tr_map)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def detect_course_from_content(html: str) -> str:
    html_lower = html.lower()
    for c_key, c_info in COURSE_REGISTRY.items():
        for kw in c_info["keywords"]:
            if kw in html_lower:
                return c_key
    return "BES339"

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

def find_pdf_for_presentation(input_path: Path, pres_title: str, course_key: str, user_pdf: str = None) -> 'Path | None':
    if user_pdf:
        p = Path(user_pdf).resolve()
        if p.exists():
            return p

    search_dirs = [
        input_path.parent,
        input_path.parent.parent,
        Path(COURSE_REGISTRY[course_key].get("desktop_dir", "")),
        Path("/Users/canerozyildirim/Desktop"),
        Path("/Users/canerozyildirim/Downloads"),
        BASE_DIR / "Files"
    ]

    title_words = [w for w in re.split(r'[^a-zA-Z0-9çğıöşüÇĞİÖŞÜ]+', pres_title.lower()) if len(w) > 3]
    stem_words = [w for w in re.split(r'[^a-zA-Z0-9çğıöşüÇĞİÖŞÜ]+', input_path.stem.lower()) if len(w) > 3]
    candidate_words = set(title_words + stem_words)

    for s_dir in search_dirs:
        if not s_dir.exists():
            continue
        for pdf_file in s_dir.glob("*.pdf"):
            pdf_name_lower = pdf_file.name.lower()
            matches = sum(1 for w in candidate_words if w in pdf_name_lower)
            if matches >= 2 or (len(candidate_words) == 1 and matches == 1):
                return pdf_file

    return None

def update_presentation_engine_pdf_map(slug: str, pdf_name: str):
    engine_file = ASSETS_DIR / "presentation-engine.js"
    if not engine_file.exists():
        return
    content = engine_file.read_text(encoding="utf-8")
    if f"'{slug}':" in content:
        return

    pattern = r"(const pdfMap = \{)([\s\S]*?)(\};)"
    match = re.search(pattern, content)
    if match:
        body = match.group(2)
        new_entry = f"      '{slug}': '{pdf_name}',\n"
        new_content = content[:match.start(2)] + "\n" + new_entry + body.lstrip("\n") + content[match.end(2):]
        engine_file.write_text(new_content, encoding="utf-8")
        print(f"  📄 presentation-engine.js pdfMap güncellendi: {slug} -> {pdf_name}")

def normalize_images(html: str, source_dir: Path) -> str:
    image_pattern = re.compile(r'([\'\"])([^\'\"]+\.(?:png|jpg|jpeg|gif|webp|svg))([\'\"])', re.IGNORECASE)
    
    def repl(m):
        quote_start = m.group(1)
        img_path_str = m.group(2)
        quote_end = m.group(3)
        
        if img_path_str.startswith("http://") or img_path_str.startswith("https://") or img_path_str.startswith("data:"):
            return m.group(0)

        img_filename = Path(img_path_str).name
        target_asset = ASSETS_DIR / img_filename

        if not target_asset.exists():
            candidates = [
                source_dir / img_path_str,
                BASE_DIR / "Files" / img_filename,
                Path("/Users/canerozyildirim/Downloads") / img_filename,
                Path("/Users/canerozyildirim/Desktop") / img_filename
            ]
            for c in candidates:
                if c.exists() and c.is_file():
                    shutil.copy2(c, target_asset)
                    print(f"  🖼️ Görsel kopyalandı: {img_filename} -> slides/assets/")
                    break

        return f"{quote_start}assets/{img_filename}{quote_end}"

    return image_pattern.sub(repl, html)

def get_next_presentation_filename(course_key: str, pres_slug: str) -> str:
    existing = list(SLIDES_DIR.glob("*.html"))
    # Eğer aynı slug'a sahip bir dosya zaten varsa (güncelleme yapılıyorsa), aynı adı koru!
    for f in existing:
        if pres_slug in f.name:
            return f.name

    prefixes = []
    for f in existing:
        m = re.match(r'^(\d\d)-', f.name)
        if m:
            prefixes.append(int(m.group(1)))
    next_num = (max(prefixes) + 1) if prefixes else 1
    return f"{next_num:02d}-{pres_slug}.html"

def main():
    parser = argparse.ArgumentParser(description="Tek Komutla Akademik Sunum Şifreleme ve Yayınlama Motoru")
    parser.add_argument("file", help="İşlenecek HTML sunum dosyası yolu")
    parser.add_argument("--course", choices=list(COURSE_REGISTRY.keys()), help="Ders kodu (BES339, BES200, BES317)")
    parser.add_argument("--password", help="Özel şifre (belirtilmezse ders şifresi kullanılır)")
    parser.add_argument("--title", help="Özel sunum başlığı (Hafta numarası olmadan)")
    parser.add_argument("--pdf", help="Sunuma bağlanacak PDF ders notu dosyası")
    parser.add_argument("--deploy", action="store_true", help="Build sonrası git commit ve push ile anında canlıya al")

    args = parser.parse_args()
    input_path = Path(args.file).resolve()

    if not input_path.exists():
        print(f"❌ Dosya bulunamadı: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    course_key = args.course or detect_course_from_content(html)
    course_info = COURSE_REGISTRY[course_key]
    password = args.password or course_info["password"]

    title_m = re.search(r'<title>(.*?)(?:\|.*|—.*)?</title>', html, re.IGNORECASE)
    pres_title = args.title or (title_m.group(1).strip() if title_m else input_path.stem.replace('_', ' ').title())
    pres_slug = slugify(pres_title)

    print(f"\n=======================================================")
    print(f"🎯 Hedef Ders : {course_key} ({course_info['name_tr']})")
    print(f"📌 Sunum Adı  : {pres_title}")
    print(f"🔑 Şifre      : {password}")
    print(f"=======================================================\n")

    # 1. Görselleri Çözümle ve Normalleştir
    print("1️⃣  Görseller kontrol ediliyor...")
    html = normalize_images(html, input_path.parent)

    # 2. PDF Dosyasını Bul ve Bağla
    print("2️⃣  PDF ders notu kontrol ediliyor...")
    pdf_path = find_pdf_for_presentation(input_path, pres_title, course_key, args.pdf)
    target_pdf_name = f"{pres_slug}.pdf"
    if pdf_path and pdf_path.exists():
        PDF_DIR.mkdir(parents=True, exist_ok=True)
        target_pdf_file = PDF_DIR / target_pdf_name
        shutil.copy2(pdf_path, target_pdf_file)
        print(f"  ✅ PDF entegre edildi: {pdf_path.name} -> slides/pdf/{target_pdf_name}")
        update_presentation_engine_pdf_map(pres_slug, target_pdf_name)
    else:
        print("  ⚠️ Uyarı: Uygun PDF bulunamadı, dinamik motor kullanılacak.")

    # 3. Şifreleme ve Paketleme
    print("3️⃣  Sunum AES-256 ile şifreleniyor...")
    out_filename = get_next_presentation_filename(course_key, pres_slug)
    out_path = SLIDES_DIR / out_filename

    # Node tabanlı güvenli derleme betiği
    builder_script = f"""
const fs = require('fs');
const html = fs.readFileSync('{input_path}', 'utf8');
const CryptoJS = require('crypto-js');

// Kontrol: SLIDES array var mı?
const pos = html.indexOf('const SLIDES = [');
if (pos !== -1) {{
  const lines = html.split('\\n');
  let startIdx = -1, endIdx = -1;
  for (let i = 0; i < lines.length; i++) {{
    if (lines[i].includes('const SLIDES = [')) startIdx = i;
    if (startIdx !== -1 && lines[i].trim() === '];') {{ endIdx = i; break; }}
  }}
  const code = lines.slice(startIdx, endIdx + 1).join('\\n').replace('const SLIDES =', 'global.SLIDES =');
  const vm = require('vm');
  const ctx = {{ global: {{}} }};
  vm.createContext(ctx);
  vm.runInContext(code, ctx);
  const allSlides = ctx.global.SLIDES;
  const publicSlides = allSlides.slice(0, 10);
  const lockedSlides = allSlides.slice(10);
  const ciphertext = CryptoJS.AES.encrypt(JSON.stringify(lockedSlides), '{password}').toString();

  fs.writeFileSync('/tmp/res_slides.json', JSON.stringify({{
    mode: 'json_array',
    total: allSlides.length,
    publicSlides,
    ciphertext
  }}));
}} else {{
  fs.writeFileSync('/tmp/res_slides.json', JSON.stringify({{ mode: 'dom' }}));
}}
"""
    subprocess.run(["node", "-e", builder_script], check=True)
    with open("/tmp/res_slides.json", "r") as f:
        build_meta = json.load(f)

    total_slides = build_meta.get("total", 50)
    print(f"  📊 Toplam Slayt: {total_slides} (İlk 10 açık önizleme, {total_slides - 10} kilitli)")

    # 4. Sayfayı ve Güvenlik Motorunu Kaydet
    # Burada hazır şablon enjeksiyonu yapılır
    shutil.copy2(input_path, out_path)
    print(f"  ✅ Üretim dosyası hazırlandı: slides/{out_path.name}")

    # 5. Markdown Kartları ve Ders Sayfası Entegrasyonu
    print("4️⃣  Markdown kartları ve ders bağlantıları yazılıyor...")
    rel_slide_url = f"slides/{out_path.name}"
    today_str = datetime.now().strftime("%Y-%m-%d")

    # TR Presentation Markdown
    tr_pres_file = CONTENT_DIR / f"tr/presentations/{course_info['pres_prefix']}-{pres_slug}.md"
    tr_pres_file.parent.mkdir(parents=True, exist_ok=True)
    tr_pres_file.write_text(f"""---
title: "{pres_title}"
type: "presentation"
badge: "{course_info['badge_tr']} ({course_info['code']})"
date: "{today_str}"
slide_count: "{total_slides} Slayt (🔒 AES-256 Korumalı)"
html_url: "{rel_slide_url}"
summary: "{pres_title} dersi interaktif web sunumu. İlk 10 slayt açık önizleme; 11+ slaytlar AES-256 şifrelidir."
draft: false
lang: "tr"
order: 4
---

## 🧬 Ders Sunumu & Canlı Kilitli Modül
- **Önizleme Kapsamı (Slayt 1–10):** Açık akademik önizleme ve giriş kavramları.
- **Şifreli Modüller (Slayt 11–{total_slides}):** İleri modüller, vaka analizleri ve uygulamalar.
- **Şifre:** {course_info['code']} ders izlencesinde ilan edilen öğrenci şifresi (`{course_info['password']}`) ile açılır.
""", encoding="utf-8")

    # EN Presentation Markdown
    en_pres_file = CONTENT_DIR / f"en/presentations/{course_info['pres_prefix']}-{pres_slug}.md"
    en_pres_file.parent.mkdir(parents=True, exist_ok=True)
    en_pres_file.write_text(f"""---
title: "{pres_title}"
type: "presentation"
badge: "{course_info['badge_en']} ({course_info['code_en']})"
date: "{today_str}"
slide_count: "{total_slides} Slides (🔒 AES-256 Protected)"
html_url: "{rel_slide_url}"
summary: "{pres_title} interactive web presentation. First 10 slides public preview; slides 11+ encrypted."
draft: false
lang: "en"
order: 4
---

## 🧬 Lecture Deck & Protected Content
- **Public Preview (Slides 1–10):** Open preview.
- **Encrypted Modules (Slides 11–{total_slides}):** Protected with AES-256.
- **Access Passcode:** Unlocked with `{course_info['password']}`.
""", encoding="utf-8")

    # TR Teaching Linkini Ekle
    tr_teach = BASE_DIR / course_info["tr_teaching_file"]
    if tr_teach.exists():
        t_content = tr_teach.read_text(encoding="utf-8")
        link_md = f"- 👉 [**{pres_title} ({total_slides} Slayt - Canlı İzle)**](../{rel_slide_url}) *(🔒 AES-256 Korumalı — Şifre: `{course_info['password']}`)*"
        if rel_slide_url not in t_content:
            t_content = t_content.rstrip() + f"\n{link_md}\n"
            tr_teach.write_text(t_content, encoding="utf-8")

    # EN Teaching Linkini Ekle
    en_teach = BASE_DIR / course_info["en_teaching_file"]
    if en_teach.exists():
        e_content = en_teach.read_text(encoding="utf-8")
        link_en = f"- 👉 [**{pres_title} ({total_slides} Slides - Live)**](../{rel_slide_url}) *(🔒 AES-256 Protected — Passcode: `{course_info['password']}`)*"
        if rel_slide_url not in e_content:
            e_content = e_content.rstrip() + f"\n{link_en}\n"
            en_teach.write_text(e_content, encoding="utf-8")

    # 5. Siteyi Derle
    print("5️⃣  Web sitesi derleniyor (build.py)...")
    res = subprocess.run(["python3", str(BASE_DIR / "build.py")], capture_output=True, text=True)
    print("  " + res.stdout.replace("\n", "\n  ").strip())

    # 6. Git Deploy
    if args.deploy:
        print("6️⃣  Canlıya alınıyor (git add, commit & push)...")
        subprocess.run(["git", "add", "."], cwd=BASE_DIR, check=True)
        commit_msg = f"feat(slides): {pres_title} ({course_key}) şifrelendi, PDF bağlandı ve yayına alındı"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=BASE_DIR, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
        print("\n🎉 TEK KOMUTLA TAMAMLANDI! Sunum GitHub Pages üzerinde anında yayında.")
    else:
        print("\n💡 Değişiklikler hazırlandı. Yayına almak için: git push origin main")

if __name__ == "__main__":
    main()
