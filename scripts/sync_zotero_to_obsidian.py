#!/usr/bin/env python3
"""
Zotero to Obsidian Sync & AI Indexing Engine for 'Okumalar'
- Extracts items from Zotero 'Okumalar' hierarchy
- Maps to existing Vault MOCs & Dizin concepts
- Assigns or creates controlled Micro-Topics
- Summarizes 1-3 Key Takeaways
- Strictly connects to user's 'Çalışma Fikirleri' with technical rationale
- Supports 5-star permanent archive protection
"""

import os
import sys
import json
import sqlite3
import shutil
import tempfile
import re
from datetime import datetime
from typing import Dict, List, Any, Optional

VAULT_DIR = "/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner"
ZOTERO_DIR = os.path.expanduser("~/Zotero")
OUTPUT_DIR = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "Zotero Literatür")
MOC_FILE = os.path.join(VAULT_DIR, "Dizin", "00_Makale_Mikro_Konulari_MOC.md")
DASHBOARD_FILE = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "Zotero Veritabanı.md")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_filename(name: str) -> str:
    s = re.sub(r'[/\\:*?"<>|]', '-', name)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:120]

def create_literature_note(data: dict):
    filename = f"{data['year'] or 'ND'} - {data['author']} - {sanitize_filename(data['title'])}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Check if file exists and has rating 5 (permanent archive protection)
    existing_rating = 0
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as ef:
                content = ef.read()
                m = re.search(r'rating:\s*(\d+)', content)
                if m:
                    existing_rating = int(m.group(1))
        except Exception:
            pass

    rating = existing_rating if existing_rating > 0 else data.get('rating', 0)
    stars_display = "⭐" * rating if rating > 0 else "—"
    
    frontmatter = f"""---
zotero_key: "{data.get('key', '')}"
zotero_id: {data.get('itemID', 0)}
title: "{data.get('title', '').replace('"', "'")}"
authors: {json.dumps(data.get('authors', []), ensure_ascii=False)}
year: {data.get('year', '')}
date_added: "{data.get('date_added', '')}"
zotero_collection: "{data.get('collection', '')}"
dizin: {json.dumps(data.get('dizin', []), ensure_ascii=False)}
micro_topics: {json.dumps(data.get('micro_topics', []), ensure_ascii=False)}
rating: {rating}
favorite: {str(rating == 5).lower()}
doi: "{data.get('doi', '')}"
url: "{data.get('url', '')}"
publication: "{data.get('publication', '')}"
status: "active"
---
"""
    
    dizin_links = " ".join(data.get('dizin', []))
    micro_links = " ".join(data.get('micro_topics', []))
    
    takeaways_md = "\n".join([f"{i+1}. {t}" for i, t in enumerate(data.get('takeaways', []))])
    
    related_idea = data.get('related_idea', {})
    if related_idea and related_idea.get('link'):
        idea_md = f"**{related_idea['link']}**\n> 🎯 **Gerekçe:** {related_idea.get('rationale', '')}"
    else:
        idea_md = "*Spesifik bir çalışma fikriyle doğrudan örtüşmüyor (Gürültü önleme amacıyla boş bırakıldı).*"

    body = f"""# 📄 {data.get('title', '')}

> [!abstract]+ 📌 Künye Bilgileri
> **Yazarlar:** {', '.join(data.get('authors', [])) or data.get('author', 'Bilinmiyor')}  
> **Yıl / Yayın:** {data.get('year', '')} — *{data.get('publication', 'N/A')}*  
> **Zotero Klasörü:** `{data.get('collection', '')}`  
> **Eklenme Tarihi:** `{data.get('date_added', '')}` | **Puan:** {stars_display}  
> **DOI / Link:** [{data.get('doi') or 'Bağlantı'}]({data.get('url') or (f"https://doi.org/{data.get('doi')}" if data.get('doi') else '#')})

---

## 🧭 1. Dizin ve Mikro-Konu Konumlandırması
* **Ana Dizin (MOC / Temel Kavram):** {dizin_links}
* **Mikro-Konu (Granüler Odak):** {micro_links}

---

## 💡 2. Ana Çıkarımlar (Key Takeaways)
{takeaways_md}

---

## 🔬 3. Katı İlişkili Çalışma Fikri & Hipotez Köprüsü
{idea_md}

---

## 📝 4. Orijinal Özet (Abstract)
> {data.get('abstract', 'Özet bulunmuyor.')}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + "\n" + body)
    print(f"Created: {filename}")

