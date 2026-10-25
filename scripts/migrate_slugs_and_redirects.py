#!/usr/bin/env python3
"""
Slug Refactoring & 301-Equivalent Meta Refresh Generator
Upgrades Turkish & English article slugs and leaves redirect files at all legacy URLs.
"""

import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()

MAPPINGS = [
    {
        "old_tr": "aralkl-aclk-yapyorsunuz-ama-ise-yaramyor",
        "new_tr": "aralikli-aclik-yapiyorsunuz-ama-ise-yaramiyor",
        "old_en": "aralkl-aclk-yapyorsunuz-ama-ise-yaramyor",
        "new_en": "intermittent-fasting-gut-microbiome",
    },
    {
        "old_tr": "besinlerle-glp-1-salglatmak-mumkun",
        "new_tr": "besinlerle-glp-1-salgilatmak-mumkun",
        "old_en": "besinlerle-glp-1-salglatmak-mumkun",
        "new_en": "can-nutrients-naturally-stimulate-glp-1",
    },
    {
        "old_tr": "beslenme-tarznz-yllar-oncesinden",
        "new_tr": "beslenme-tarziniz-karacigeri-kansere-programliyor",
        "old_en": "beslenme-tarznz-yllar-oncesinden",
        "new_en": "diet-epigenetically-programming-liver-cancer",
    },
    {
        "old_tr": "glp-1-ilaclar-kilo-vermekle-obeziteyi",
        "new_tr": "glp-1-ilaclari-kilo-vermek-obezite-tedavisi",
        "old_en": "glp-1-ilaclar-kilo-vermekle-obeziteyi",
        "new_en": "glp-1-agonists-weight-loss-vs-obesity-treatment",
    },
    {
        "old_tr": "glp-1-ilaclarna-direncli-bir-grup",
        "new_tr": "glp-1-ilaclarina-direncli-bir-grup-var",
        "old_en": "glp-1-ilaclarna-direncli-bir-grup",
        "new_en": "patients-resistant-to-glp-1-therapies",
    },
    {
        "old_tr": "glp-1-ile-gelen-kas-dokusu-panigi",
        "new_tr": "glp-1-ile-gelen-kas-dokusu-panigi",
        "old_en": "glp-1-ile-gelen-kas-dokusu-panigi",
        "new_en": "muscle-mass-panic-with-glp-1",
    },
    {
        "old_tr": "glp-1-kullanrken-tok-hissetmeniz",
        "new_tr": "glp-1-kullanirken-tok-hissetmeniz-ac-oldugunuz-gercegi",
        "old_en": "glp-1-kullanrken-tok-hissetmeniz",
        "new_en": "feeling-full-on-glp-1-cells-starving",
    },
    {
        "old_tr": "glp-1den-cks-plan-ilac-braktgnzda",
        "new_tr": "glp-1den-cikis-plani-ilaci-biraktiginizda-ne-olacak",
        "old_en": "glp-1den-cks-plan-ilac-braktgnzda",
        "new_en": "glp-1-exit-strategy-discontinuing-therapy",
    },
    {
        "old_tr": "insulin-direnciniz-varken-ac-kalmak",
        "new_tr": "insulin-direnciniz-varken-ac-kalmak",
        "old_en": "insulin-direnciniz-varken-ac-kalmak",
        "new_en": "fasting-with-insulin-resistance",
    },
    {
        "old_tr": "kan-sekerini-yukselten-hormon-nasl",
        "new_tr": "kan-sekerini-yukselten-hormon-nasil-zayiflatiyor",
        "old_en": "kan-sekerini-yukselten-hormon-nasl",
        "new_en": "glucagon-paradox-blood-sugar-raising-hormone-weight-loss",
    },
    {
        "old_tr": "uyku-diyetsel-bir-risk-faktoru-olmaya",
        "new_tr": "uyku-diyetsel-bir-risk-faktoru-olmaya-aday-mi",
        "old_en": "uyku-diyetsel-bir-risk-faktoru-olmaya",
        "new_en": "is-sleep-a-dietary-risk-factor",
    }
]

def make_redirect_html(lang, new_canonical_url, is_tr=True):
    title = "Yönlendiriliyor…" if is_tr else "Redirecting…"
    link_text = "Yazıya git" if is_tr else "Go to article"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <link rel="canonical" href="{new_canonical_url}">
  <meta name="robots" content="noindex,follow">
  <meta http-equiv="refresh" content="0; url={new_canonical_url}">
  <script>location.replace("{new_canonical_url}");</script>
</head>
<body><a href="{new_canonical_url}">{link_text}</a></body>
</html>
"""

def update_frontmatter(file_path, slug, en_slug=None, tr_slug=None):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("---", 2)
    if len(parts) < 3:
        return
        
    fm_lines = parts[1].splitlines()
    new_fm_lines = []
    
    slug_found = False
    en_slug_found = False
    tr_slug_found = False
    date_modified_found = False
    
    for line in fm_lines:
        if line.strip().startswith("slug:"):
            new_fm_lines.append(f'slug: "{slug}"')
            slug_found = True
        elif line.strip().startswith("en_slug:"):
            if en_slug:
                new_fm_lines.append(f'en_slug: "{en_slug}"')
                en_slug_found = True
        elif line.strip().startswith("tr_slug:"):
            if tr_slug:
                new_fm_lines.append(f'tr_slug: "{tr_slug}"')
                tr_slug_found = True
        elif line.strip().startswith("date_modified:"):
            new_fm_lines.append('date_modified: "2026-10-23"')
            date_modified_found = True
        else:
            new_fm_lines.append(line)
            
    if not slug_found:
        new_fm_lines.append(f'slug: "{slug}"')
    if en_slug and not en_slug_found:
        new_fm_lines.append(f'en_slug: "{en_slug}"')
    if tr_slug and not tr_slug_found:
        new_fm_lines.append(f'tr_slug: "{tr_slug}"')
    if not date_modified_found:
        new_fm_lines.append('date_modified: "2026-10-23"')
        
    new_content = "---" + "\n".join(new_fm_lines) + "\n---" + parts[2]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    redirects_rows = ["old_url,new_url,status"]
    
    tr_articles_dir = BASE_DIR / "content" / "tr" / "articles"
    en_articles_dir = BASE_DIR / "content" / "en" / "articles"
    
    # 1. Rename files and update frontmatter
    for m in MAPPINGS:
        old_tr_file = tr_articles_dir / f"{m['old_tr']}.md"
        new_tr_file = tr_articles_dir / f"{m['new_tr']}.md"
        old_en_file = en_articles_dir / f"{m['old_en']}.md"
        new_en_file = en_articles_dir / f"{m['new_en']}.md"
        
        # TR rename
        if old_tr_file.exists() and old_tr_file != new_tr_file:
            subprocess.run(["git", "mv", str(old_tr_file), str(new_tr_file)], check=True, cwd=str(BASE_DIR))
        update_frontmatter(new_tr_file, m["new_tr"], en_slug=m["new_en"])
        
        # EN rename
        if old_en_file.exists() and old_en_file != new_en_file:
            subprocess.run(["git", "mv", str(old_en_file), str(new_en_file)], check=True, cwd=str(BASE_DIR))
        update_frontmatter(new_en_file, m["new_en"], tr_slug=m["new_tr"])
        
        # Record redirects
        if m["old_tr"] != m["new_tr"]:
            old_url = f"/yazilar/{m['old_tr']}.html"
            new_url = f"/yazilar/{m['new_tr']}.html"
            redirects_rows.append(f"{old_url},{new_url},301-meta-refresh")
            
        if m["old_en"] != m["new_en"]:
            old_url = f"/en/articles/{m['old_en']}.html"
            new_url = f"/en/articles/{m['new_en']}.html"
            redirects_rows.append(f"{old_url},{new_url},301-meta-refresh")

    # Write redirects.csv
    redirects_csv_path = BASE_DIR / "redirects.csv"
    with open(redirects_csv_path, "w", encoding="utf-8") as f:
        f.write("\n".join(redirects_rows) + "\n")
    print(f"✅ Generated redirects.csv with {len(redirects_rows)-1} entries.")

if __name__ == "__main__":
    main()
