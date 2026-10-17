import os
import re
import json
import urllib.request
from pathlib import Path

BASE_DIR = Path("/Users/canerozyildirim/Sites/personalwebsite")
OBSIDIAN_DIR = Path("/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner/Sosyal Medya/Substack")
ARTICLES_CONTENT_DIR = BASE_DIR / "content" / "tr" / "articles"
IMAGES_DIR = BASE_DIR / "assets" / "images" / "articles"

ARTICLES_CONTENT_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# 1. Fetch Substack Archive
api_url = "https://drcaner.substack.com/api/v1/archive?sort=new&limit=50"
req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    posts = json.loads(resp.read().decode("utf-8"))

# Filter only newsletters (articles)
newsletters = [p for p in posts if p.get("type") == "newsletter" and not p.get("podcast_url")]
print(f"Toplam Newsletter Sayısı: {len(newsletters)}")

# Mapping between Substack slug and Obsidian file
# Let's inspect titles and map them accurately
mapping = [
    {
        "slug": "aralkl-aclk-yapyorsunuz-ama-ise-yaramyor",
        "obsidian": "ONLINE aralikli-aclik-isle-yaramiyor-mu-bagirsaklariniz.md",
        "tags": ["Aralıklı Açlık", "Mikrobiyota", "Metabolizma"]
    },
    {
        "slug": "beslenme-tarznz-yllar-oncesinden",
        "obsidian": "ONLINE Beslenme Tarzınız, Yıllar Öncesinden Karaciğerinizi Kansere Programlıyor Olabilir.md",
        "tags": ["Karaciğer", "Onkoloji", "Klinik Beslenme"]
    },
    {
        "slug": "besinlerle-glp-1-salglatmak-mumkun",
        "obsidian": "ONLINE GLP2-Doğal Ozempic Diye Bir Şey Var Mı?.md",
        "tags": ["GLP-1", "İnkretinler", "Besin Etkileşimi"]
    },
    {
        "slug": "glp-1-ilaclarna-direncli-bir-grup",
        "obsidian": "ONLINE glp1-direncli-hastalar.md",
        "tags": ["GLP-1", "Obezite Farmakoterapisi", "Direnç Mekanizmaları"]
    },
    {
        "slug": "kan-sekerini-yukselten-hormon-nasl",
        "obsidian": "ONLINE GLP4-Kan Şekerini Yükselten Hormon Nasıl Zayıflatıyor?.md",
        "tags": ["Glukagon", "Metabolizma", "GLP-1"]
    },
    {
        "slug": "glp-1den-cks-plan-ilac-braktgnzda",
        "obsidian": "ONLINE GLP3-GLP1 için Çıkış Planı İlacı Bıraktığınızda Ne Olur?.md",
        "tags": ["GLP-1", "Kilo Koruma", "Klinik Takip"]
    },
    {
        "slug": "glp-1-ile-gelen-kas-dokusu-panigi",
        "obsidian": "ONLINE GLP-1 ile Kas Dokusu Paniği- Kaslarımız Mı Eriyor, Vücudumuz Mu Küçülüyor?.md",
        "tags": ["Kas Kütlesi", "Sarkopeni", "GLP-1"]
    },
    {
        "slug": "glp-1-ilaclar-kilo-vermekle-obeziteyi",
        "obsidian": "ONLINE GLP-1 İlaçları Kilo Vermekle Obeziteyi Tedavi Etmek Aynı Şey Mi?.md",
        "tags": ["Obezite Tedavisi", "Kronik Hastalık", "Farmakoterapi"]
    },
    {
        "slug": "glp-1-kullanrken-tok-hissetmeniz",
        "obsidian": "ONLINE GLP1-GLP-1 Kullanırken Tok Hissetmeniz, Aç Olduğunuz Gerçeğini Değiştirmiyor.md",
        "tags": ["Malnütrisyon", "Klinik Beslenme", "GLP-1"]
    }
]

def clean_wikilinks(text):
    # [[Target|Label]] -> Label
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text)
    return text

def calculate_read_time(text):
    words = len(text.split())
    minutes = max(3, round(words / 180))
    return f"{minutes} dk"

for item in mapping:
    slug = item["slug"]
    obs_file = OBSIDIAN_DIR / item["obsidian"]
    if not obs_file.exists():
        print(f"HATA: Dosya bulunamadı -> {obs_file}")
        continue
    
    # Substack post metadata
    spost = next((p for p in newsletters if p.get("slug") == slug), None)
    if not spost:
        print(f"HATA: Substack post bulunamadı -> {slug}")
        continue
    
    title = spost.get("title", "").strip()
    date_raw = spost.get("post_date", "")[:10]
    cover_url = spost.get("cover_image", "")
    summary = spost.get("description", "").strip()
    substack_url = spost.get("canonical_url") or f"https://drcaner.substack.com/p/{slug}"

    # Download cover image
    ext = ".jpg"
    if ".png" in cover_url.lower():
        ext = ".png"
    elif ".webp" in cover_url.lower():
        ext = ".webp"
    
    local_img_name = f"{slug}{ext}"
    local_img_path = IMAGES_DIR / local_img_name
    rel_img_url = f"assets/images/articles/{local_img_name}"

    if cover_url:
        try:
            print(f"İndiriliyor: {cover_url} -> {local_img_name}")
            img_req = urllib.request.Request(cover_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(img_req, timeout=10) as r, open(local_img_path, "wb") as f_out:
                f_out.write(r.read())
        except Exception as e:
            print(f"Görsel indirme hatası ({slug}): {e}")
            rel_img_url = cover_url # fallback to remote
    else:
        rel_img_url = ""

    # Read Obsidian file and clean frontmatter
    with open(obs_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove old frontmatter
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].strip()
    
    body = clean_wikilinks(body)
    
    if not summary:
        # Extract first paragraph
        paras = [p.strip() for p in body.split("\n\n") if p.strip() and not p.strip().startswith("#")]
        if paras:
            summary = paras[0][:230] + "..."

    read_time = calculate_read_time(body)

    safe_title = title.replace('"', '\\"')
    safe_summary = summary.replace('"', '\\"')

    # Format new frontmatter
    tags_formatted = json.dumps(item["tags"], ensure_ascii=False)
    
    new_md = f"""---
title: "{safe_title}"
slug: "{slug}"
date: "{date_raw}"
summary: "{safe_summary}"
cover_image: "{rel_img_url}"
substack_url: "{substack_url}"
read_time: "{read_time}"
badge: "Bilimsel Analiz"
tags: {tags_formatted}
draft: false
---

{body}
"""
    dest_path = ARTICLES_CONTENT_DIR / f"{slug}.md"
    with open(dest_path, "w", encoding="utf-8") as out:
        out.write(new_md)
    print(f"Kaydedildi: {dest_path.name}")

print("\nTüm makaleler başarıyla aktarıldı!")
