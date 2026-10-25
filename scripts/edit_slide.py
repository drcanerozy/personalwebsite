#!/usr/bin/env python3
"""
Akıllı Slayt Görüntüleyici ve Düzenleyici (Instant Slide Editor)
Dr. Caner ÖZYILDIRIM — Kişisel Web Sitesi Altyapısı

Kullanım:
    # 1. Slaytları listele (başlıklar ve numaralar):
    python3 scripts/edit_slide.py <sunum_dosyasi_veya_adi> --list

    # 2. Belirli bir slaytın içeriğini göster:
    python3 scripts/edit_slide.py <sunum_dosyasi_veya_adi> --slide <NO>

    # 3. Belirli bir slaytta metin değiştir (1 saniyede anında uygular):
    python3 scripts/edit_slide.py <sunum_dosyasi_veya_adi> --slide <NO> --find "eski metin" --replace "yeni metin" [--deploy]
"""

import os
import sys
import re
import json
import argparse
import subprocess
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

BASE_DIR = Path("/Users/canerozyildirim/Sites/personalwebsite").resolve()
SLIDES_DIR = BASE_DIR / "slides"

PASSWORDS = {
    "BES339": "COZYPOP2026_",
    "BES200": "COZYBESAI2026_",
    "BES317": "COZYYHTBT2026_",
}

ALL_PASSWORDS = list(PASSWORDS.values())

def find_presentation_file(name_or_path: str) -> Path:
    p = Path(name_or_path)
    if p.exists():
        return p.resolve()
    
    # slides/ altında ara
    for cand in sorted(SLIDES_DIR.glob("*.html")):
        if name_or_path.lower() in cand.name.lower():
            return cand
            
    print(f"❌ Sunum dosyası bulunamadı: {name_or_path}")
    sys.exit(1)

def decrypt_payload(ciphertext: str, password: str) -> Optional[list]:
    node_code = """
const CryptoJS = require('crypto-js');
const args = JSON.parse(process.argv[1]);
try {
  const bytes = CryptoJS.AES.decrypt(args.ciphertext, args.password);
  const decryptedData = bytes.toString(CryptoJS.enc.Utf8);
  if (!decryptedData) {
    process.exit(1);
  }
  console.log(decryptedData);
} catch (e) {
  process.exit(1);
}
"""
    try:
        res = subprocess.run(
            ["node", "-e", node_code, json.dumps({"ciphertext": ciphertext, "password": password})],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(res.stdout.strip())
    except Exception:
        return None

def encrypt_payload(slides_list: list, password: str) -> str:
    node_code = """
const CryptoJS = require('crypto-js');
const args = JSON.parse(process.argv[1]);
const ciphertext = CryptoJS.AES.encrypt(JSON.stringify(args.slides), args.password).toString();
console.log(ciphertext);
"""
    res = subprocess.run(
        ["node", "-e", node_code, json.dumps({"slides": slides_list, "password": password})],
        capture_output=True,
        text=True,
        check=True
    )
    return res.stdout.strip()

def load_presentation(file_path: Path):
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    
    # 1. Açık Slaytları Bul (const SLIDES = [...];)
    m = re.search(r'const SLIDES\s*=\s*(\[[\s\S]*?\]);', text)
    public_slides = []
    if m:
        try:
            public_slides = json.loads(m.group(1))
        except Exception:
            node_code = f"const s = {m.group(1)}; console.log(JSON.stringify(s));"
            res = subprocess.run(["node", "-e", node_code], capture_output=True, text=True)
            if res.returncode == 0:
                public_slides = json.loads(res.stdout)

    # 2. Şifreli Slaytları Bul
    ciphertext = None
    enc_match = re.search(r'<script id="encrypted-payload-data"[^>]*>([\s\S]*?)</script>', text)
    if enc_match:
        ciphertext = enc_match.group(1).strip()
    
    locked_slides = []
    used_password = None
    if ciphertext:
        for pw in ALL_PASSWORDS:
            dec = decrypt_payload(ciphertext, pw)
            if dec:
                locked_slides = dec
                used_password = pw
                break

    # Önizleme kilit slaytı var mı kontrol et
    clean_public = []
    lock_slide = None
    for s in public_slides:
        if "Önizleme Sonu" in str(s.get("title", "")) or "Önizleme Sonu" in str(s.get("tag", "")):
            lock_slide = s
        else:
            clean_public.append(s)

    all_slides = list(clean_public) + list(locked_slides)
    return text, clean_public, locked_slides, all_slides, used_password, lock_slide

def get_slide_title(s: dict) -> str:
    candidates = [s.get("title"), s.get("kicker"), s.get("eyebrow"), s.get("tag"), s.get("q"), s.get("type")]
    for c in candidates:
        if c:
            clean = re.sub(r'<[^>]+>', '', str(c)).replace('\n', ' ').strip()
            if clean:
                return clean
    return "(Başlıksız Slayt)"

def replace_in_slide(obj, old_text, new_text):
    found = False
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and old_text in v:
                obj[k] = v.replace(old_text, new_text)
                found = True
            elif isinstance(v, (dict, list)):
                if replace_in_slide(v, old_text, new_text):
                    found = True
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, str) and old_text in item:
                obj[i] = item.replace(old_text, new_text)
                found = True
            elif isinstance(item, (dict, list)):
                if replace_in_slide(item, old_text, new_text):
                    found = True
    return found

def main():
    parser = argparse.ArgumentParser(description="Hızlı Slayt Görüntüleyici ve Düzenleyici")
    parser.add_argument("file", help="Sunum dosya yolu veya dosya adının bir kısmı (örn: 01-obezite)")
    parser.add_argument("--list", action="store_true", help="Tüm slaytların numaralarını ve başlıklarını listeler")
    parser.add_argument("--slide", type=int, help="İşlem yapılacak slayt numarası (1 tabanlı)")
    parser.add_argument("--find", help="Aranacak / Değiştirilecek eski metin")
    parser.add_argument("--replace", help="Yerine konulacak yeni metin")
    parser.add_argument("--deploy", action="store_true", help="Değişiklikten sonra siteyi build edip git push yap")

    args = parser.parse_args()
    file_path = find_presentation_file(args.file)
    print(f"📄 Seçilen Sunum: {file_path.name}")

    text, clean_public, locked_slides, all_slides, used_pw, lock_slide = load_presentation(file_path)

    if not all_slides:
        print("⚠️ Bu dosyada yapılandırılmış slayt dizisi bulunamadı.")
        sys.exit(1)

    print(f"📊 Toplam Gerçek Slayt: {len(all_slides)} (Açık: {len(clean_public)}, Kilitli: {len(locked_slides)})")

    # 1. LİSTELEME
    if args.list:
        print("\n" + "="*70)
        print("SLAYT LİSTESİ")
        print("="*70)
        for idx, s in enumerate(all_slides, 1):
            lock_icon = "🔓" if idx <= len(clean_public) else "🔒"
            stype = s.get("type", "slide")
            title = get_slide_title(s)
            print(f"[{idx:03d}] {lock_icon} [{stype:^9}] {title[:65]}")
        print("="*70)
        return

    # 2. SLAYT GÖRÜNTÜLEME VEYA DEĞİŞTİRME
    if args.slide:
        idx = args.slide - 1
        if idx < 0 or idx >= len(all_slides):
            print(f"❌ Geçersiz slayt numarası! (1 ile {len(all_slides)} arasında olmalı)")
            sys.exit(1)

        target_slide = all_slides[idx]
        print(f"\n🎯 Slayt {args.slide} Seçildi: {get_slide_title(target_slide)}")

        # DEĞİŞTİRME
        if args.find and args.replace is not None:
            print(f"🔄 '{args.find}' -> '{args.replace}' aranıyor...")
            success = replace_in_slide(target_slide, args.find, args.replace)
            if not success:
                print(f"❌ HATA: '{args.find}' metni Slayt {args.slide} içinde bulunamadı!")
                print("Mevcut slayt içeriği:")
                print(json.dumps(target_slide, indent=2, ensure_ascii=False))
                sys.exit(1)

            print(f"✅ Slayt {args.slide} başarıyla güncellendi!")

            # Dosyayı yeniden paketle
            # İlk n tane açık (clean_public kadar), gerisi kilitli
            num_pub = len(clean_public)
            new_public = list(all_slides[:num_pub])
            if lock_slide:
                new_public.append(lock_slide)
            new_locked = list(all_slides[num_pub:])

            # JSON array'i metinde güncelle
            new_text = re.sub(
                r'const SLIDES\s*=\s*\[[\s\S]*?\];',
                'const SLIDES = ' + json.dumps(new_public, indent=2, ensure_ascii=False) + ';',
                text
            )

            if new_locked and used_pw:
                new_cipher = encrypt_payload(new_locked, used_pw)
                new_text = re.sub(
                    r'(<script id="encrypted-payload-data"[^>]*>)([\s\S]*?)(</script>)',
                    rf'\g<1>\n{new_cipher}\n\g<3>',
                    new_text
                )

            file_path.write_text(new_text, encoding="utf-8")
            print(f"💾 Dosya kaydedildi: {file_path.name}")

            if args.deploy:
                print("🚀 Deploy ediliyor...")
                subprocess.run(["python3", "build.py"], cwd=BASE_DIR, check=True)
                subprocess.run(["git", "commit", "-am", f"fix(slide): {file_path.name} Slayt {args.slide} güncellendi"], cwd=BASE_DIR, check=True)
                subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
                print("🎉 Canlıya alındı!")

            return

        # SADECE İÇERİĞİ GÖSTER
        print("\n--- Slayt İçeriği ---")
        print(json.dumps(target_slide, indent=2, ensure_ascii=False))
        print("---------------------\n")
        return

    parser.print_help()

if __name__ == "__main__":
    main()
