#!/usr/bin/env python3
"""
Dynamic XML Sitemap & robots.txt Generator for canerozy.com
- Computes accurate per-file lastmod using `git log -1 --format=%cs`
- Injects xhtml:link hreflang (tr, en, x-default=TR) for all bilingual pairs
- Includes homepage, course pages, article detail pages, article list pages, and lecture slides
- Omits deprecated changefreq & priority tags
"""

import os
import subprocess
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()

COURSE_PAIRS = {
    "01-bilgisayar-ve-yapay-zeka.html": "01-computer-and-ai-applications.html",
    "02-beslenmenin-psikososyal-boyutlari.html": "02-psychosocial-aspects-of-nutrition.html",
    "03-beslenme-ve-medya.html": "03-nutrition-and-media.html",
    "04-diyet-ilkeleri-ve-populer-diyetler.html": "04-dietary-principles-and-popular-diets.html",
    "05-immun-sistem-ve-immunonutrisyon.html": "05-immune-system-and-immunonutrition.html",
    "06-yetiskin-hastaliklarinda-diyet-tedavisi.html": "06-medical-nutrition-therapy.html",
    "07-enteral-ve-parenteral-beslenme.html": "07-enteral-and-parenteral-nutrition.html",
}

INDEXABLE_SLIDES = [
    "slides/01-beslenmenin-evrimi.html",
    "slides/01-bilgisayar-ve-yapay-zeka.html",
    "slides/01-obezite-ve-tibbi-beslenme-tedavisi.html",
    "slides/02-diyetler-ise-yaramiyor-mu.html",
    "slides/02-hafta-2-yapay-zeka-beslenme-bilimini-nasil-donusturuyor.html",
    "slides/02-obezite-uygulama.html",
    "slides/03-diyabet-ve-tibbi-beslenme-tedavisi.html",
]

def get_git_lastmod(file_rel_path, fallback_date=None):
    try:
        res = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(file_rel_path)],
            capture_output=True, text=True, check=True, cwd=str(BASE_DIR)
        )
        mod = res.stdout.strip()
        if mod:
            return mod
    except Exception:
        pass
    return fallback_date or date.today().isoformat()

def build_sitemap(tr_articles=None, en_articles=None):
    today = date.today().isoformat()
    urls = []
    
    # 1. Homepage (TR & EN)
    tr_home_mod = get_git_lastmod("index.html", today)
    en_home_mod = get_git_lastmod("en/index.html", today)
    
    urls.append({
        "loc": "https://canerozy.com/",
        "lastmod": tr_home_mod,
        "tr": "https://canerozy.com/",
        "en": "https://canerozy.com/en/"
    })
    urls.append({
        "loc": "https://canerozy.com/en/",
        "lastmod": en_home_mod,
        "tr": "https://canerozy.com/",
        "en": "https://canerozy.com/en/"
    })

    # 2. Articles List Pages (TR & EN)
    tr_list_mod = get_git_lastmod("yazilar/index.html", today)
    en_list_mod = get_git_lastmod("en/articles/index.html", today)
    
    urls.append({
        "loc": "https://canerozy.com/yazilar/",
        "lastmod": tr_list_mod,
        "tr": "https://canerozy.com/yazilar/",
        "en": "https://canerozy.com/en/articles/"
    })
    urls.append({
        "loc": "https://canerozy.com/en/articles/",
        "lastmod": en_list_mod,
        "tr": "https://canerozy.com/yazilar/",
        "en": "https://canerozy.com/en/articles/"
    })

    # 3. Courses (TR & EN with reciprocal hreflang)
    for tr_fname, en_fname in COURSE_PAIRS.items():
        tr_rel = f"dersler/{tr_fname}"
        en_rel = f"en/courses/{en_fname}"
        tr_mod = get_git_lastmod(tr_rel, today)
        en_mod = get_git_lastmod(en_rel, today)
        
        tr_url = f"https://canerozy.com/dersler/{tr_fname}"
        en_url = f"https://canerozy.com/en/courses/{en_fname}"
        
        urls.append({
            "loc": tr_url,
            "lastmod": tr_mod,
            "tr": tr_url,
            "en": en_url
        })
        urls.append({
            "loc": en_url,
            "lastmod": en_mod,
            "tr": tr_url,
            "en": en_url
        })

    # 4. Bilingual Articles
    if tr_articles:
        en_lookup = {a.get("slug"): a for a in (en_articles or [])}
        for a in tr_articles:
            if not a.get("is_local"):
                continue
            tr_slug = a.get("slug")
            en_slug = a.get("en_slug", tr_slug)
            
            tr_rel = f"yazilar/{tr_slug}.html"
            en_rel = f"en/articles/{en_slug}.html"
            
            tr_mod = get_git_lastmod(tr_rel, a.get("date", today))
            en_art = en_lookup.get(en_slug, {})
            en_mod = get_git_lastmod(en_rel, en_art.get("date", today))
            
            tr_url = f"https://canerozy.com/yazilar/{tr_slug}.html"
            en_url = f"https://canerozy.com/en/articles/{en_slug}.html"
            
            urls.append({
                "loc": tr_url,
                "lastmod": tr_mod,
                "tr": tr_url,
                "en": en_url
            })
            urls.append({
                "loc": en_url,
                "lastmod": en_mod,
                "tr": tr_url,
                "en": en_url
            })

    # 5. Indexable Interactive Presentation Slides
    for slide_rel in INDEXABLE_SLIDES:
        slide_path = BASE_DIR / slide_rel
        if slide_path.exists():
            mod = get_git_lastmod(slide_rel, today)
            urls.append({
                "loc": f"https://canerozy.com/{slide_rel}",
                "lastmod": mod
            })

    # Generate XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
    ]
    
    for u in urls:
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{u['loc']}</loc>")
        xml_lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        if "tr" in u and "en" in u:
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="tr" href="{u["tr"]}"/>')
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{u["en"]}"/>')
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{u["tr"]}"/>')
        xml_lines.append("  </url>")
        
    xml_lines.append("</urlset>\n")
    
    sitemap_path = BASE_DIR / "sitemap.xml"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    print(f"  ✅ Generated: sitemap.xml ({len(urls)} URLs indexed)")
    
    robots_content = """User-agent: *
Allow: /

Sitemap: https://canerozy.com/sitemap.xml
"""
    with open(BASE_DIR / "robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_content)
    print("  ✅ Generated: robots.txt")

if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(BASE_DIR))
    import build
    tr_articles = build.load_section_items(build.CONTENT_DIR / "tr", "articles")
    en_articles = build.load_section_items(build.CONTENT_DIR / "en", "articles")
    build_sitemap(tr_articles, en_articles)
