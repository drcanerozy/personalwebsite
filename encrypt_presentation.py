#!/usr/bin/env python3
"""
Academic Presentation AES-256 Encryptor & Packager
Dr. Caner ÖZYILDIRIM Website Suite

Functionality:
1. Reads a master presentation HTML containing <section class="slide">...</section> tags.
2. Keeps the first 10 slides (index 0-9) as plaintext public preview.
3. Extracts all subsequent slides (index 10+) and encrypts them using AES-256-GCM + PBKDF2 (100,000 iterations, SHA-256).
4. Generates a standalone, self-contained HTML presentation with client-side Web Crypto API decryption.
"""

import os
import sys
import re
import json
import base64
import hashlib
import argparse
import subprocess
from pathlib import Path

def encrypt_aes_gcm(plaintext: str, password: str) -> dict:
    """
    Encrypts plaintext using AES-256-GCM with PBKDF2 key derivation.
    Outputs salt, iv, and ciphertext (with authentication tag appended) in base64 format.
    Compatible with browser window.crypto.subtle.
    """
    salt = os.urandom(16)
    iv = os.urandom(12)
    iterations = 100000

    # Try Python cryptography library first if available
    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations, dklen=32)
        aesgcm = AESGCM(key)
        ciphertext_bytes = aesgcm.encrypt(iv, plaintext.encode('utf-8'), None)
        return {
            "salt": base64.b64encode(salt).decode('utf-8'),
            "iv": base64.b64encode(iv).decode('utf-8'),
            "ciphertext": base64.b64encode(ciphertext_bytes).decode('utf-8'),
            "iterations": iterations
        }
    except ImportError:
        pass

    # Fallback to Node.js standard built-in crypto (Node 16+)
    try:
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
    except Exception as e:
        raise RuntimeError(f"Şifreleme gerçekleştirilemedi: Python 'cryptography' veya 'node' gereklidir. Hata: {e}")

def process_presentation(input_html: str, password: str, public_slide_count: int = 10) -> str:
    """
    Parses HTML, separates first `public_slide_count` slides,
    encrypts the rest, and injects payload into the presentation template.
    """
    # Find all slide sections: <section class="slide" ...>...</section>
    slide_pattern = re.compile(r'(<section\b[^>]*class=["\'][^"\']*slide[^"\']*["\'][^>]*>.*?</section>)', re.DOTALL | re.IGNORECASE)
    slides = slide_pattern.findall(input_html)

    if not slides:
        # Fallback: look for <div class="slide" ...>
        slide_pattern = re.compile(r'(<div\b[^>]*class=["\'][^"\']*slide[^"\']*["\'][^>]*>.*?</div>\s*<!--\s*end-slide\s*-->)', re.DOTALL | re.IGNORECASE)
        slides = slide_pattern.findall(input_html)

    if not slides:
        raise ValueError("HTML içinde herhangi bir <section class=\"slide\"> veya <div class=\"slide\"> bulunamadı!")

    total_slides = len(slides)
    print(f"📊 Toplam Slayt Sayısı: {total_slides}")
    print(f"🔓 Açık Önizleme Slaytları: 1 - {min(public_slide_count, total_slides)}")

    if total_slides <= public_slide_count:
        print("⚠️ Uyarı: Slayt sayısı belirlenen kilit sınırından (10) az veya eşit. Kilitlenecek slayt bulunamadı.")
        locked_slides = []
    else:
        locked_slides = slides[public_slide_count:]
        print(f"🔒 Şifrelenecek Kilitli Slaytlar: {public_slide_count + 1} - {total_slides} ({len(locked_slides)} slayt)")

    # Prepare locked slides plaintext HTML
    locked_html = "\n".join(locked_slides)

    # Encrypt locked slides
    encrypted_data = encrypt_aes_gcm(locked_html, password)
    encrypted_data["totalSlides"] = total_slides
    encrypted_data["publicSlideCount"] = min(public_slide_count, total_slides)
    encrypted_data["lockedSlideCount"] = len(locked_slides)

    # Build new HTML: replace the slides in input HTML
    public_slides_html = "\n".join(slides[:public_slide_count])
    
    # Payload script tag
    payload_json = json.dumps(encrypted_data, indent=2)
    payload_script = f"""
    <!-- AES-256-GCM ENCRYPTED STUDENT PAYLOAD (Slides {public_slide_count + 1} to {total_slides}) -->
    <script id="encrypted-payload-data" type="application/json">
{payload_json}
    </script>
    """

    # Check if presentation-deck container exists
    deck_match = re.search(r'(<div\b[^>]*id=["\']presentation-deck["\'][^>]*>)(.*?)(</div>\s*<!--\s*end-deck\s*-->|</div>\s*<!--\s*#presentation-deck\s*-->)', input_html, re.DOTALL | re.IGNORECASE)
    if deck_match:
        deck_open = deck_match.group(1)
        deck_close = deck_match.group(3)
        modified_deck = f"{deck_open}\n{public_slides_html}\n    {deck_close}"
        new_html = input_html[:deck_match.start()] + modified_deck + input_html[deck_match.end():]
    else:
        # Replace from first slide start to last slide end
        first_slide_start = input_html.find(slides[0])
        last_slide = slides[-1]
        last_slide_end = input_html.find(last_slide) + len(last_slide)
        new_html = input_html[:first_slide_start] + public_slides_html + input_html[last_slide_end:]

    # Inject or update encrypted payload script
    if 'id="encrypted-payload-data"' in new_html:
        new_html = re.sub(
            r'<script\b[^>]*id=["\']encrypted-payload-data["\'][^>]*>.*?</script>',
            f'<script id="encrypted-payload-data" type="application/json">\n{payload_json}\n    </script>',
            new_html,
            flags=re.DOTALL
        )
    else:
        new_html = new_html.replace('</body>', f'{payload_script}\n</body>')

    return new_html

def main():
    parser = argparse.ArgumentParser(
        description="HTML Ders Sunumları için AES-256 Öğrenci Kilit Ekranı Şifreleme Aracı"
    )
    parser.add_argument("input_file", help="Ham sunum HTML dosyası yolu (örn: master_slide.html)")
    parser.add_argument("-p", "--password", required=True, help="Sunumu açacak öğrenci şifresi")
    parser.add_argument("-o", "--output", help="Şifrelenmiş çıktı HTML dosyası yolu (varsayılan: girdi dosyası üzerine yazar veya output.html)")
    parser.add_argument("-c", "--count", type=int, default=10, help="Açık kalacak önizleme slayt sayısı (varsayılan: 10)")

    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"❌ Hata: '{input_path}' dosyası bulunamadı!")
        sys.exit(1)

    output_path = Path(args.output) if args.output else input_path

    print(f"\n🔐 AES-256 Sunum Şifreleyici Başlatılıyor...")
    print(f"📄 Girdi Dosyası: {input_path}")
    print(f"🎯 Çıktı Dosyası: {output_path}")
    print(f"🔑 Şifre: {'*' * len(args.password)}")
    print(f"👁️ Önizleme Slayt Sayısı: {args.count}")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        encrypted_html = process_presentation(content, args.password, args.count)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(encrypted_html)
        print(f"✅ Başarılı! Şifrelenmiş sunum kaydedildi: {output_path}\n")
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
