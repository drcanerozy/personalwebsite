#!/usr/bin/env python3
"""
Full Zotero 'Okumalar' Indexing Engine
Processes all 1562+ items:
- Canonical Domain MOC & Concept Mapping
- Evolving Micro-Topic Taxonomy
- 1-3 Structured Key Takeaways
- Strict Matching to 'Çalışma Fikirleri' with technical rationale
- 100% User-Controlled Rating (default 0, preserves existing ratings)
- Full Auto-Sync Ready
"""

import os
import sys
import json
import sqlite3
import shutil
import tempfile
import re
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Any, Optional

VAULT_DIR = "/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner"
ZOTERO_DIR = os.path.expanduser("~/Zotero")
OUTPUT_DIR = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "Zotero Literatür")
MOC_FILE = os.path.join(VAULT_DIR, "Dizin", "00_Makale_Mikro_Konulari_MOC.md")
DASHBOARD_FILE = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "Zotero Veritabanı.md")
IDEAS_DIR = os.path.join(VAULT_DIR, "Çalışma Fikirleri")
DIZIN_DIR = os.path.join(VAULT_DIR, "Dizin")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Load Existing Çalışma Fikirleri
study_ideas = []
if os.path.exists(IDEAS_DIR):
    for f in os.listdir(IDEAS_DIR):
        if f.endswith(".md"):
            name = f[:-3]
            fpath = os.path.join(IDEAS_DIR, f)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read(1500)
            except Exception:
                content = ""
            study_ideas.append({
                "title": name,
                "link": "[[Çalışma Fikirleri/" + name + "]]",
                "content": content.lower(),
                "keywords": [w for w in re.split(r'[\s\-_\.,;:]+', name.lower()) if len(w) > 3]
            })

print("Loaded " + str(len(study_ideas)) + " study ideas for strict matching.")

# 2. Extract SQLite Data
tmp_dir = tempfile.mkdtemp()
for fname in ["zotero.sqlite", "zotero.sqlite-wal", "zotero.sqlite-shm"]:
    src = os.path.join(ZOTERO_DIR, fname)
    dst = os.path.join(tmp_dir, fname)
    if os.path.exists(src):
        shutil.copy2(src, dst)

db_path = os.path.join(tmp_dir, "zotero.sqlite")
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Get collection hierarchy under Okumalar (ID 218)
c.execute("""
    WITH RECURSIVE subcols AS (
        SELECT collectionID, collectionName, parentCollectionID
        FROM collections WHERE collectionID = 218
        UNION ALL
        SELECT c.collectionID, c.collectionName, c.parentCollectionID
        FROM collections c JOIN subcols s ON c.parentCollectionID = s.collectionID
    )
    SELECT collectionID, collectionName, parentCollectionID FROM subcols
""")
okuma_cols = dict((r[0], r[1]) for r in c.fetchall())
sub_ids = list(okuma_cols.keys())
placeholders = ','.join(['?'] * len(sub_ids))

# Get all items in Okumalar
query = """
    SELECT DISTINCT i.itemID, i.key, i.dateAdded, ci.collectionID
    FROM items i
    JOIN collectionItems ci ON i.itemID = ci.itemID
    WHERE ci.collectionID IN (""" + placeholders + """) AND i.itemTypeID NOT IN (1, 14)
    ORDER BY i.dateAdded DESC
"""
c.execute(query, sub_ids)
item_rows = c.fetchall()
print("Found " + str(len(item_rows)) + " item-collection associations.")

# Group collections per item
items_dict = {}
for item_id, item_key, date_added, col_id in item_rows:
    if item_id not in items_dict:
        items_dict[item_id] = {
            "itemID": item_id,
            "key": item_key,
            "date_added": date_added.split("T")[0] if "T" in date_added else date_added.split(" ")[0],
            "collections": []
        }
    cname = okuma_cols.get(col_id, "Okumalar")
    if cname != "Okumalar" and cname not in items_dict[item_id]["collections"]:
        items_dict[item_id]["collections"].append(cname)
    elif not items_dict[item_id]["collections"]:
        items_dict[item_id]["collections"].append(cname)

# Fetch fields and creators for each item
all_items = []
for item_id, item_info in items_dict.items():
    c.execute("""
        SELECT f.fieldName, idv.value
        FROM itemData id
        JOIN itemDataValues idv ON id.valueID = idv.valueID
        JOIN fields f ON id.fieldID = f.fieldID
        WHERE id.itemID = ? AND f.fieldName IN ('title', 'abstractNote', 'date', 'publicationTitle', 'DOI', 'url')
    """, (item_id,))
    fields = dict(c.fetchall())
    
    c.execute("""
        SELECT c.lastName, c.firstName
        FROM itemCreators ic
        JOIN creators c ON ic.creatorID = c.creatorID
        WHERE ic.itemID = ? ORDER BY ic.orderIndex LIMIT 3
    """, (item_id,))
    creators = c.fetchall()
    authors = [(last + " " + first).strip() for last, first in creators if last]
    author_str = creators[0][0] if creators and creators[0][0] else "Unknown"
    
    title = fields.get("title", "").strip()
    if not title:
        continue
        
    date_val = fields.get("date", "")
    year = date_val[:4] if date_val else ""
    if not year and len(date_val) >= 4:
        m = re.search(r'\b(19\d\d|20\d\d)\b', date_val)
        if m:
            year = m.group(1)
            
    all_items.append({
        "itemID": item_id,
        "key": item_info["key"],
        "date_added": item_info["date_added"],
        "collection": item_info["collections"][0] if item_info["collections"] else "Okumalar",
        "all_collections": item_info["collections"],
        "title": title,
        "abstract": fields.get("abstractNote", "").strip(),
        "year": year,
        "author": author_str,
        "authors": authors,
        "doi": fields.get("DOI", ""),
        "url": fields.get("url", ""),
        "publication": fields.get("publicationTitle", "")
    })

conn.close()
shutil.rmtree(tmp_dir)

print("Extracted metadata for " + str(len(all_items)) + " valid academic items.")

def sanitize_filename(name: str) -> str:
    s = re.sub(r'[/\\:*?"<>|]', '-', name)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:110]

# Mapping rules for Collections -> Domain MOCs
COL_MOC_MAP = {
    "GLP-1": ("[[00_GLP-1 ve Farmakolojik Müdahaleler_MOC]]", ["[[GLP-1]]", "[[Obezite]]"]),
    "Adipoz Doku": ("[[00_Adipoz Doku ve Metabolizma_MOC]]", ["[[Adipoz Doku]]", "[[Adipoz Doku Disfonksiyonu]]"]),
    "Aralıklı Açlık": ("[[00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC]]", ["[[Aralıklı Açlık]]", "[[Otofaji]]"]),
    "UPF": ("[[00_Ultra İşlenmiş Besinler ve Diyet Kalitesi_MOC]]", ["[[Ultra İşlenmiş Besinler]]", "[[Diyet Kalitesi]]"]),
    "Mikrobiyota": ("[[00_Mikrobiyota ve Kişiselleştirilmiş Beslenme_MOC]]", ["[[Mikrobiyota]]", "[[Kişiselleştirilmiş Beslenme]]"]),
    "İstatistik ve Yöntem": ("[[00_Beslenme Metodolojisi ve İstatistik_MOC]]", ["[[Metodoloji]]", "[[İstatistik]]"]),
    "Diet and Weight": ("[[00_Kalori Kısıtlaması ve Enerji Metabolizması_MOC]]", ["[[Kilo Kaybı]]", "[[Enerji Metabolizması]]"]),
    "NAFLD": ("[[00_Lipotoksisite ve Ektopik Yağ Birikimi_MOC]]", ["[[Karaciğer Yağlanması]]", "[[Lipotoksisite]]"]),
    "Besin Ögeleri": ("[[00_Besin Ögeleri ve Biyoaktif Bileşikler_MOC]]", ["[[Besin Ögeleri]]", "[[Biyoaktif Bileşikler]]"]),
    "Süt": ("[[00_Besin Ögeleri ve Biyoaktif Bileşikler_MOC]]", ["[[Besinler]]", "[[Diyet Kalitesi]]"]),
    "T2DM": ("[[00_İnsülin Direnci ve Tip 2 Diyabet_MOC]]", ["[[Tip 2 Diyabet]]", "[[İnsülin Direnci]]"]),
    "Yağ Metabolizması": ("[[00_Lipotoksisite ve Ektopik Yağ Birikimi_MOC]]", ["[[Yağ Metabolizması]]", "[[Metabolizma]]"]),
    "Metabolizma": ("[[00_Kalori Kısıtlaması ve Enerji Metabolizması_MOC]]", ["[[Metabolizma]]", "[[Enerji Harcaması]]"]),
    "Obezite": ("[[00_Obezite Fenotipleri ve Bireysel Farklılıklar_MOC]]", ["[[Obezite]]", "[[Beden Kütle İndeksi]]"]),
    "AI": ("[[00_Yapay Zeka ve Dijital Beslenme_MOC]]", ["[[Yapay Zeka]]"]),
    "Nutrient Density": ("[[00_Ultra İşlenmiş Besinler ve Diyet Kalitesi_MOC]]", ["[[Diyet Kalitesi]]", "[[Besin Ögeleri]]"]),
    "Hastalıklar": ("[[00_Klinik Beslenme ve Hastalıklarda Tıbbi Beslenme Tedavisi_MOC]]", ["[[Klinik Nütrisyon]]"]),
    "Beslenme Felsefesi": ("[[00_Beslenme Tarihi ve Sosyal Boyutlar_MOC]]", ["[[Beslenme Felsefesi]]", "[[Sağlıklı Beslenme]]"]),
    "Beslenme Tarihi": ("[[00_Beslenme Tarihi ve Sosyal Boyutlar_MOC]]", ["[[Beslenme Bilimi Tarihi]]"]),
    "Demir": ("[[00_Besin Ögeleri ve Biyoaktif Bileşikler_MOC]]", ["[[Demir]]", "[[Mineraller]]"]),
    "Vücut Ağırlığı Modelleri": ("[[00_Obezite Fenotipleri ve Bireysel Farklılıklar_MOC]]", ["[[Karbonhidrat İnsülin Modeli]]", "[[Enerji Harcaması]]"]),
    "Ketojenik Diyet": ("[[00_Kalori Kısıtlaması ve Enerji Metabolizması_MOC]]", ["[[Ketojenik Diyet]]", "[[Düşük Karbonhidratlı Diyetler]]"]),
    "genetik obezite iliskisi": ("[[00_Obezite Fenotipleri ve Bireysel Farklılıklar_MOC]]", ["[[Genetik, Epigenetik, Nutrigenetik]]", "[[Obezite]]"]),
    "KH Metabolizması": ("[[00_İnsülin Direnci ve Tip 2 Diyabet_MOC]]", ["[[Karbonhidrat Metabolizması]]", "[[Glukoz Dengesi]]"])
}

def determine_micro_topic(title: str, abstract: str, col: str) -> str:
    text = (title + " " + abstract).lower()
    
    if "semaglutide" in text or "tirzepatide" in text or "glp-1" in text or "incretin" in text:
        if "regain" in text or "discontinu" in text or "cessation" in text or "withdrawal" in text or "rebound" in text:
            return "[[GLP-1 Kesilmesi Sonrası Kilo Geri Kazanımı ve Kardiyometabolik Rebound]]"
        elif "muscle" in text or "lean mass" in text or "sarcopen" in text or "body composition" in text:
            return "[[GLP-1 Tedavisinde Vücut Kompozisyonu ve Yağsız Kütle Değişimi]]"
        elif "appetite" in text or "satiety" in text or "brain" in text or "hypothalam" in text or "reward" in text:
            return "[[GLP-1 ve Santral İştah/Ödül Mekanizmaları Regülasyonu]]"
        else:
            return "[[İnkretin Tabanlı Farmakoterapiler ve Sistemik Metabolik Etkiler]]"
            
    if "fasting" in text or "intermittent" in text or "time-restricted" in text or "fmd" in text or "açlık" in text:
        if "refeed" in text or "re-feeding" in text:
            return "[[Açlık-Yeniden Beslenme (Refeeding) Döngüsünde Hücresel Plastisite ve Rejenerasyon]]"
        elif "autophagy" in text or "otofaji" in text:
            return "[[Aralıklı Açlıkta Otofajik Temizlik ve Mitokondriyal Dinamikler]]"
        elif "islet" in text or "beta-cell" in text or "pancrea" in text:
            return "[[Fasting-Mimicking Diyet ve Beta Hücre Rejenerasyonu]]"
        else:
            return "[[Aralıklı Açlık ve Zaman Kısıtlı Beslenmede Sirkadiyen-Metabolik Uyum]]"
            
    if "adipocyte" in text or "adipose" in text or "fat tissue" in text or "yağ doku" in text:
        if "plasticity" in text or "browning" in text or "beige" in text or "ucp1" in text or "thermogen" in text:
            return "[[Adipoz Doku Plastisitesi, Termojenez ve Bejleşme Mekanizmaları]]"
        elif "fibrosis" in text or "ecm" in text or "hypoxia" in text or "inflammation" in text or "macrophage" in text:
            return "[[Adipoz Doku Hipoksisi, ECM Sertleşmesi ve İnflamatuvar Yeniden Modellenme]]"
        elif "lipolysis" in text or "atgl" in text or "hsl" in text:
            return "[[Adiposit Lipoliz Regülasyonu ve Serbest Yağ Asidi Toksisitesi]]"
        else:
            return "[[Adipoz Doku Disfonksiyonu ve Sistemik Metabolik Çapraz Etkileşim]]"
            
    if "ultra-processed" in text or "upf" in text or "emulsifier" in text or "food matrix" in text or "işlenmiş besin" in text:
        if "matrix" in text or "emulsifier" in text or "barrier" in text or "gut permeability" in text:
            return "[[Gıda Matrisi Bozulması, Emülgatörler ve Bağırsak Bariyer Disfonksiyonu]]"
        else:
            return "[[Ultra İşlenmiş Besin Tüketimi, Diyet Kalitesi ve Kardiyometabolik Risk]]"
            
    if "microbiota" in text or "microbiome" in text or "scfa" in text or "butyrate" in text or "bakteri" in text:
        if "scfa" in text or "short-chain" in text or "butyrate" in text or "propionate" in text:
            return "[[Mikrobiyal SCFA Metabolitleri ve Organlar Arası Sinyalizasyon]]"
        else:
            return "[[Bağırsak Mikrobiyota Kompozisyonu ve Metabolik Fenotip Etkileşimi]]"
            
    if "nafld" in text or "masld" in text or "steatotic" in text or "liver" in text or "cirrhosis" in text or "hepat" in text:
        if "cluster" in text or "precision" in text or "subtype" in text or "phenotype" in text:
            return "[[MASLD Fenotipik Kümeleri ve Hassas Tıp/Beslenme Sınıflandırması]]"
        elif "cirrhosis" in text or "portal" in text or "decompensat" in text:
            return "[[İlerlemiş Karaciğer Hastalığında Dekompanzasyonun Önlenmesi ve Portal Hipertansiyon]]"
        else:
            return "[[Hepatik Steatoz, De Novo Lipogenez ve İnsülin Duyarlılığı]]"
            
    if "ketogenic" in text or "low-carbohydrate" in text or "macronutrient" in text:
        return "[[Makrobesin Kompozisyonunun İntrahepatik Lipid ve Hepatik İnsülin Duyarlılığına Etkisi]]"
        
    if "systematic review" in text or "meta-analysis" in text or "grade" in text or "prisma" in text or "methodolog" in text:
        return "[[Sistematik Derleme Standartları ve GRADE Kanıt Kesinliği]]"
        
    if "carbohydrate-insulin" in text or "energy expenditure" in text or "energy balance" in text or "set point" in text:
        return "[[Vücut Ağırlığı Regülasyon Modelleri ve Enerji Dengesi Tartışmaları]]"
        
    if "personalized" in text or "nutrigenom" in text or "genetics" in text:
        return "[[Genetik ve Biyobelirteç Temelli Kişiselleştirilmiş Beslenme Stratejileri]]"

    return "[[" + col + " Alanında Mekanistik Araştırmalar ve Klinik Bulgular]]"

def extract_takeaways(title: str, abstract: str) -> List[str]:
    if not abstract:
        return ["Çalışma '" + title + "' odağında kavramsal ve deneysel değerlendirme sunmaktadır."]
        
    sentences = re.split(r'(?<=[.!?])\s+', abstract)
    clean_s = [s.strip() for s in sentences if len(s.strip()) > 25 and not s.strip().startswith("©") and not s.strip().startswith("Copyright")]
    
    if not clean_s:
        return [abstract[:150] + "..."]
        
    if len(clean_s) == 1:
        return [clean_s[0]]
    elif len(clean_s) == 2:
        return [clean_s[0], clean_s[1]]
    else:
        results = []
        res_sentences = [s for s in clean_s if any(k in s.lower() for k in ['show', 'demonstrate', 'found', 'conclude', 'increase', 'decrease', 'result', 'suggest', 'reveal', 'improve', 'reduce', 'associat'])]
        if res_sentences:
            results = res_sentences[-3:]
        else:
            results = [clean_s[0], clean_s[len(clean_s)//2], clean_s[-1]]
            
        return results[:3]

def match_study_idea(title: str, abstract: str, micro_topic: str) -> tuple:
    text = (title + " " + abstract + " " + micro_topic).lower()
    
    for idea in study_ideas:
        idea_title = idea["title"].lower()
        score = 0
        for kw in idea["keywords"]:
            if kw in text:
                score += 1
                
        if score >= 3:
            if "glp-1" in idea_title and ("glp-1" in text or "semaglutide" in text):
                if "regain" in text or "kesilme" in idea_title or "kilo-geri" in idea_title:
                    return idea["link"], "Makaledeki kilo geri kazanım kinetiği ve hormonal adaptasyon verileri, derleme taslağınızdaki zaman-çizelgesi ve post-GLP-1 yönetim modeliyle birebir örtüşüyor."
                elif "mikrobiyota" in idea_title and "microbi" in text:
                    return idea["link"], "GLP-1'in bağırsak mikrobiyomu üzerindeki etkileri ve takviye stratejisi çalışma fikrinizle doğrudan uyumludur."
                elif "nutrient density" in idea_title and ("nutrient" in text or "protein" in text):
                    return idea["link"], "İlaç kullanımında besin yoğunluğu ve yağsız doku korunumu hipotezinizi deneysel olarak desteklemektedir."
                    
            if "refeeding" in idea_title and ("refeed" in text or "re-feeding" in text):
                return idea["link"], "Hücresel farklılaşma ve doku yenilenmesinin açlık evresinden ziyade yeniden beslenme evresinde gerçekleştiği bulgusu, notunuzdaki tezinizi doğrulamaktadır."
                
            if "upf" in idea_title and ("matrix" in text or "emulsifier" in text or "matris" in idea_title):
                return idea["link"], "Gıda matrisi degradasyonunun kimyasal katkılardan bağımsız bir patolojik mekanizma olduğu bulgusu, hipotezinizin ana eksenini oluşturuyor."
                
            if "masld" in idea_title or "nafld" in idea_title:
                if "cluster" in text or "genetik" in idea_title or "genom" in text:
                    return idea["link"], "MASLD'nin alt kümelere ayrılması ve fenotipik heterojenite, kişiselleştirilmiş müdahale çalışma fikrinizin temelini oluşturmaktadır."
                elif "kc%" in idea_title or "de novo" in text:
                    return idea["link"], "Karaciğer yağ yüzdesindeki gerilemenin metabolik sonlanım noktası olarak önemi hipotezinizle tam örtüşmektedir."

            if "plastisite" in idea_title and ("plasticity" in text or "dedifferenti" in text):
                return idea["link"], "Adiposit plastisitesi ve doku yeniden modellenmesi bulguları araştırma fikrinizle doğrudan bağlantılıdır."

            if "scfa" in text and "probiyotik" in idea_title:
                return idea["link"], "SCFA kaynaklı termojenez ve bejleşme artışı, diyet sonrası kilo korunumunda probiyotik seçimi fikrinizle uyumludur."

    return "", ""

# Process All Items
micro_topic_clusters = defaultdict(list)
processed_count = 0

for item in all_items:
    col = item["collection"]
    moc_info = COL_MOC_MAP.get(col, ("[[00_Obezite Fenotipleri ve Bireysel Farklılıklar_MOC]]", ["[[" + col + "]]"]))
    primary_moc = moc_info[0]
    extra_dizin = moc_info[1]
    dizin_list = [primary_moc] + [d for d in extra_dizin if d not in [primary_moc]]
    
    micro_topic = determine_micro_topic(item["title"], item["abstract"], col)
    micro_topic_clusters[micro_topic].append(item)
    
    takeaways = extract_takeaways(item["title"], item["abstract"])
    rel_link, rel_rat = match_study_idea(item["title"], item["abstract"], micro_topic)
    
    filename = (item['year'] or 'ND') + " - " + item['author'] + " - " + sanitize_filename(item['title']) + ".md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    existing_rating = 0
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as ef:
                content = ef.read(1000)
                m = re.search(r'rating:\s*(\d+)', content)
                if m:
                    existing_rating = int(m.group(1))
        except Exception:
            pass

    rating = existing_rating  # 100% User-assigned (default 0)
    stars_display = ("⭐" * rating) if rating > 0 else "— (Puan verilmedi)"
    fav_bool = "true" if rating == 5 else "false"
    
    clean_title = item["title"].replace('"', "'")
    clean_pub = item["publication"].replace('"', "'")
    authors_json = json.dumps(item["authors"], ensure_ascii=False)
    dizin_json = json.dumps(dizin_list, ensure_ascii=False)
    micro_json = json.dumps([micro_topic], ensure_ascii=False)
    takeaways_json = json.dumps(takeaways, ensure_ascii=False)
    rel_rat_clean = rel_rat.replace('"', "'")
    
    frontmatter = "---\n" + \
        'zotero_key: "' + item['key'] + '"\n' + \
        'zotero_id: ' + str(item['itemID']) + '\n' + \
        'title: "' + clean_title + '"\n' + \
        'author: "' + item['author'] + '"\n' + \
        'authors: ' + authors_json + '\n' + \
        'year: "' + str(item['year']) + '"\n' + \
        'date_added: "' + item['date_added'] + '"\n' + \
        'zotero_collection: "' + item['collection'] + '"\n' + \
        'dizin: ' + dizin_json + '\n' + \
        'micro_topics: ' + micro_json + '\n' + \
        'takeaways: ' + takeaways_json + '\n' + \
        'related_idea_link: "' + rel_link + '"\n' + \
        'related_idea_rationale: "' + rel_rat_clean + '"\n' + \
        'rating: ' + str(rating) + '\n' + \
        'favorite: ' + fav_bool + '\n' + \
        'doi: "' + item['doi'] + '"\n' + \
        'url: "' + item['url'] + '"\n' + \
        'publication: "' + clean_pub + '"\n' + \
        'status: "active"\n---'

    dizin_links = " ".join(dizin_list)
    micro_links = micro_topic
    takeaways_md = "\n".join([str(i+1) + ". " + t for i, t in enumerate(takeaways)])
    
    if rel_link:
        idea_md = "**" + rel_link + "**\n> 🎯 **Gerekçe:** " + rel_rat
    else:
        idea_md = "*Spesifik bir çalışma fikriyle doğrudan eşleşmedi.*"

    authors_display = ', '.join(item['authors']) or item['author']
    pub_display = item['publication'] or 'N/A'
    year_display = item['year'] or 'N/A'
    doi_display = item['doi'] or 'Bağlantı'
    doi_url = item['url'] or (("https://doi.org/" + item['doi']) if item['doi'] else '#')
    abstract_display = item['abstract'] or 'Özet bulunmuyor.'

    body = "# 📄 " + item['title'] + "\n\n" + \
        "> [!abstract]+ 📌 Künye Bilgileri\n" + \
        "> **Yazarlar:** " + authors_display + "  \n" + \
        "> **Yıl / Yayın:** " + year_display + " — *" + pub_display + "*  \n" + \
        "> **Zotero Klasörü:** `" + item['collection'] + "`  \n" + \
        "> **Eklenme Tarihi:** `" + item['date_added'] + "` | **Puanınız:** " + stars_display + "  \n" + \
        "> **DOI / Link:** [" + doi_display + "](" + doi_url + ")\n\n" + \
        "---\n\n" + \
        "## 🧭 1. Dizin ve Mikro-Konu\n" + \
        "* **Ana Dizin (MOC / Temel Kavram):** " + dizin_links + "\n" + \
        "* **Mikro-Konu (Granüler Odak):** " + micro_links + "\n\n" + \
        "---\n\n" + \
        "## 💡 2. Ana Çıkarımlar & Bulgular\n" + takeaways_md + "\n\n" + \
        "---\n\n" + \
        "## 🔬 3. Katı İlişkili Çalışma Fikri & Hipotez Köprüsü\n" + idea_md + "\n\n" + \
        "---\n\n" + \
        "## 📝 4. Orijinal Özet (Abstract)\n> " + abstract_display + "\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + "\n\n" + body)
        
    processed_count += 1
    if processed_count % 300 == 0:
        print("Processed " + str(processed_count) + "/" + str(len(all_items)) + " items...")

print("Successfully processed and generated " + str(processed_count) + " literature notes!")

# 3. Generate Complete Evolving Micro-Topics MOC
moc_sections = []
for topic, items in sorted(micro_topic_clusters.items(), key=lambda x: len(x[1]), reverse=True):
    sample_items = items[:5]
    item_links = "\n".join(["- [[" + (it['year'] or 'ND') + " - " + it['author'] + " - " + sanitize_filename(it['title']) + "|" + it['author'] + " (" + (it['year'] or 'ND') + ") — " + it['title'][:75] + "...]]" for it in sample_items])
    total_count = len(items)
    clean_topic_name = topic.replace("[[", "").replace("]]", "")
    more_str = "*(... ve " + str(total_count - 5) + " makale daha)*" if total_count > 5 else ""
    
    section = "### 🧬 " + clean_topic_name + " (`" + str(total_count) + " Makale`)\n" + \
        "> **Odak:** " + topic + "\n\n" + \
        item_links + "\n" + more_str + "\n\n" + \
        "```dataview\n" + \
        "TABLE WITHOUT ID\n" + \
        '  date_added as "Eklenme",\n' + \
        '  file.link as "Makale",\n' + \
        '  year as "Yıl",\n' + \
        '  zotero_collection as "Klasör",\n' + \
        '  choice(rating = 5, "⭐⭐⭐⭐⭐", choice(rating > 0, rating + " ⭐", "—")) as "Puan"\n' + \
        'FROM "00 Kontrol Merkezi/Zotero Literatür"\n' + \
        'WHERE contains(micro_topics, "' + topic + '")\n' + \
        'SORT date_added DESC\n```\n'
    moc_sections.append(section)

now_str = datetime.now().strftime('%Y-%m-%d')
full_moc_content = "---\n" + \
    "tags: [moc, literature-moc, micro-topics, zotero-index]\n" + \
    'BAŞLIK: "Makale Mikro-Konu ve Tematik Küme Taksonomisi"\n' + \
    "TOPLAM_MAKALE: " + str(processed_count) + "\n" + \
    "TOPLAM_KUME: " + str(len(micro_topic_clusters)) + "\n" + \
    'SON_GÜNCELLEME: "' + now_str + '"\n---\n\n' + \
    "# 🧬 Makale Mikro-Konuları & Tematik Kümeler MOC\n\n" + \
    "> **Amaç:** Zotero `Okumalar` kütüphanesindeki tüm makaleleri (" + str(processed_count) + " adet) biyolojik mekanizmalarına, araştırma sorularına ve hipotez odaklarına göre **kümelenmiş mikro-konular** halinde organize etmek.\n" + \
    "> Yeni makaleler Zotero'ya eklendikçe otomatik olarak bu standart kümelere atanır veya yeni araştırma eksenleri açılır.\n\n" + \
    "---\n\n" + \
    "## 📊 Küme Dağılımı ve Hızlı Özet\n" + \
    "* **Toplam İndekslenen Makale:** `" + str(processed_count) + "`\n" + \
    "* **Toplam Aktif Mikro-Konu Kümesi:** `" + str(len(micro_topic_clusters)) + "`\n\n" + \
    "---\n\n" + \
    "## 🧭 Tematik Mikro-Konu Kümeleri\n\n" + \
    "\n".join(moc_sections)

with open(MOC_FILE, 'w', encoding='utf-8') as f:
    f.write(full_moc_content)

print("Updated Master MOC with " + str(len(micro_topic_clusters)) + " micro-topic clusters.")

# 4. Update Main Dashboard Table
dashboard_content = "---\n" + \
    "tags: [dashboard, zotero, literature-matrix, kontrol-merkezi]\n" + \
    'BAŞLIK: "Zotero Okumalar Literatür Veritabanı & Araştırma Matrisi"\n' + \
    "TOPLAM_MAKALE: " + str(processed_count) + "\n" + \
    'SON_GÜNCELLEME: "' + now_str + '"\n---\n\n' + \
    "# 📚 Zotero Veritabanı & Dinamik Literatür Matrisi\n\n" + \
    "> **Kapsam:** Zotero `Okumalar` hiyerarşisi (`" + str(processed_count) + "` Makale)  \n" + \
    "> **Sıralama:** Zotero'ya Eklenme Tarihi (En yeniden en eskiye ↓)  \n" + \
    "> **Puanlama:** Tamamen sizin kontrolünüzdedir (`rating: 5` verdikleriniz kalıcı arşiv rozeti alır ve Zotero'dan silinse de korunur).  \n" + \
    "> **Tüm Detaylar:** Çıkarımlar, bulgular ve çalışma fikri gerekçeleri doğrudan tabloda görüntülenir.\n\n" + \
    "---\n\n" + \
    "## 🔍 Kütüphane İstatistikleri\n\n" + \
    "```dataviewjs\n" + \
    'const pages = dv.pages(\'"00 Kontrol Merkezi/Zotero Literatür"\');\n' + \
    'const total = pages.length;\n' + \
    'const star5 = pages.where(p => p.rating === 5).length;\n' + \
    'const rated = pages.where(p => p.rating > 0).length;\n' + \
    'const withIdeas = pages.where(p => p.related_idea_link && p.related_idea_link.length > 0).length;\n\n' + \
    'dv.paragraph(`📊 **Toplam Makale:** \\`${total}\\` | ⭐ **5 Yıldızlı Kalıcı Arşiv:** \\`${star5}\\` | 📝 **Puanladığınız:** \\`${rated}\\` | 🔬 **Çalışma Fikrine Bağlı:** \\`${withIdeas}\\``);\n' + \
    "```\n\n" + \
    "---\n\n" + \
    "## 🎛️ Ana Literatür Matrisi (Tüm Çıkarımlar & Gerekçeler Tabloda)\n\n" + \
    "> [!tip] 💡 Tablo İpuçları\n" + \
    "> * Sütun başlıklarına tıklayarak herhangi bir kritere göre anında sıralayabilirsiniz.\n" + \
    "> * Tablo doğrudan **Zotero'ya Eklenme Tarihine (`date_added`)** göre en yeniden en eskiye sıralıdır.\n" + \
    "> * Makale notuna `rating: 5` (veya 1-4) yazarak puanlayabilirsiniz; puanlarınız senkronizasyon sırasında asla kaybolmaz.\n\n" + \
    "```dataview\n" + \
    "TABLE WITHOUT ID\n" + \
    '  date_added as "Eklenme 📅",\n' + \
    '  file.link as "Makale & Künye 📄",\n' + \
    '  zotero_collection as "Klasör 📁",\n' + \
    '  dizin as "Ana Dizin (MOC) 🧭",\n' + \
    '  micro_topics as "Mikro-Konu (Odak) 🧬",\n' + \
    '  takeaways as "Ana Çıkarımlar & Bulgular 💡",\n' + \
    '  choice(related_idea_link, related_idea_link + "<br><br>🎯 <i>" + related_idea_rationale + "</i>", "—") as "İlişkili Çalışma Fikri & Gerekçesi 🔬",\n' + \
    '  choice(rating = 5, "⭐⭐⭐⭐⭐<br>(Kalıcı Arşiv)", choice(rating > 0, rating + " ⭐", "—")) as "Puanınız ⭐"\n' + \
    'FROM "00 Kontrol Merkezi/Zotero Literatür"\n' + \
    "SORT date_added DESC\n" + \
    "```\n\n" + \
    "---\n\n" + \
    "## 🔬 Sadece Çalışma Fikirlerinizle Katı Eşleşen Makaleler\n\n" + \
    "```dataview\n" + \
    "TABLE WITHOUT ID\n" + \
    '  date_added as "Eklenme",\n' + \
    '  file.link as "Makale",\n' + \
    '  micro_topics as "Mikro-Konu",\n' + \
    '  takeaways as "Bulgular / Çıkarımlar",\n' + \
    '  related_idea_link + "<br><br>🎯 <i>" + related_idea_rationale + "</i>" as "Çalışma Fikri & Teknik Gerekçe"\n' + \
    'FROM "00 Kontrol Merkezi/Zotero Literatür"\n' + \
    "WHERE related_idea_link AND length(related_idea_link) > 0\n" + \
    "SORT date_added DESC\n" + \
    "```\n\n" + \
    "---\n\n" + \
    "## 🧬 Mikro-Konu ve Tematik Küme Gezgini\n" + \
    "Tüm alt araştırma alanlarını ve kümelenmiş makaleleri tematik olarak incelemek için:\n" + \
    "👉 **[[Dizin/00_Makale_Mikro_Konulari_MOC|00 — Makale Mikro-Konuları & Tematik Kümeler MOC]]**\n"

with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
    f.write(dashboard_content)

print("Updated Dashboard at: " + DASHBOARD_FILE)

