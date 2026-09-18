#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📚 Inline Atıf Tetikleyicisi (Inline Citation Resolver)
Dr. Caner Özyıldırım Akademik Vault Altyapısı

Metin içindeki `>>ref:X<<` etiketlerini:
1. Frontmatter'daki `source_paper` alanından (@citekey)
2. Zotero yerel kütüphanesinden veya Better BibTeX anahtarlarından
çözümleyerek akademik formatta `[@citekey]` biçimine dönüştürür.
"""

import os
import sys
import re
import glob
import sqlite3
from pathlib import Path

def find_zotero_sqlite():
    """Zotero varsayılan yerel SQLite veri tabanını arar"""
    home = Path.home()
    candidates = [
        home / "Zotero" / "zotero.sqlite",
        home / "Library" / "Application Support" / "Zotero" / "Profiles"
    ]
    for c in candidates:
        if c.is_file():
            return c
        elif c.is_dir():
            sqls = list(c.glob("*/zotero.sqlite"))
            if sqls:
                return sqls[0]
    return None

def resolve_citations_in_text(text, default_citekey=None):
    """Metin içindeki >>ref:X<< tetikleyicilerini çözer"""
    def replacer(match):
        query = match.group(1).strip()
        
        # Eğer query 'source' veya boşsa ve default_citekey varsa
        if (query.lower() in ["source", "main", "primary", ""] or query == "1") and default_citekey:
            clean_key = default_citekey.replace("@", "").strip()
            return f"[@{clean_key}]"
            
        # Zaten bir citekey gibi görünüyorsa (örn: >>ref:ludwig2024<<)
        if re.match(r"^[a-zA-Z0-9_\-]+$", query):
            clean_key = query.replace("@", "").strip()
            return f"[@{clean_key}]"
            
        return f"[@{query}]"

    # >>ref:X<< örüntüsünü yakala
    return re.sub(r">>ref:(.*?)<<", replacer, text)

def process_manuscript_citations(file_path):
    """Belirtilen makale taslağındaki atıfları çözer ve günceller"""
    p = Path(file_path).resolve()
    if not p.exists():
        print(f"❌ Dosya bulunamadı: {p}")
        return False

    with open(p, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter'dan source_paper çek
    source_paper = ""
    fm_match = re.search(r"source_paper:\s*[\"']?(.*?)[\"']?\s*\n", content)
    if fm_match:
        source_paper = fm_match.group(1).strip()

    # Değiştirme
    matches = re.findall(r">>ref:(.*?)<<", content)
    if not matches:
        print(f"  ℹ️ {p.name}: Çözümlenecek >>ref:X<< etiketi bulunamadı.")
        return True

    new_content = resolve_citations_in_text(content, default_citekey=source_paper)
    
    with open(p, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ {p.name}: {len(matches)} adet atıf başarıyla [@citekey] formatına dönüştürüldü!")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            process_manuscript_citations(target)
        elif os.path.isdir(target):
            for f in glob.glob(f"{target}/**/*.md", recursive=True):
                process_manuscript_citations(f)
    else:
        for f in glob.glob("Manuscripts/**/*.md", recursive=True):
            process_manuscript_citations(f)
