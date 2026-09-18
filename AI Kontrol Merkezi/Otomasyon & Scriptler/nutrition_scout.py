#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Akademik ve Klinik Nütrisyon Çift Yönlü Takip Motoru (Nutrition Scout)
Yazar: Dr. Caner Özyıldırım Akademik Obsidian Kasası için Geliştirilmiştir.

Özellikler:
1. Statik & Dinamik Terim Genişletme (Kasa MOC & Son 30 gün analizi)
2. Kategori 1: Resmi Uyarılar & Küresel Otoriteler (FDA, EFSA, WHO, World Obesity)
3. Kategori 2: Dernek, Rehber & Bağımsız Denetim (ESPEN, EASO, ASPEN, EFAD, ADA, Examine, Retraction Watch, Cochrane)
4. Kategori 3: PubMed Son 4 Günün Yayınları (NCBI E-utilities API)
5. Kategori 4: Sağlık, Bilim ve Klinik Haberleri (16+ Seçkin Kaynak)
6. Kategori 5: Popüler Topluluk ve Sosyal Tartışmalar (Dinamik Reddit Trendleri)
7. Gemini Flash API / Akıllı Türkçe Sentezleme & MOC Eşleme
8. Önbellek Yönetimi (.scout_cache.json ile mükerrer engelleme)
9. Terminal Çıktısı + 00 Kontrol Merkezi/Digests/Digest_YYYY-MM-DD.md Kaydı
"""

import os
import sys
import json
import re
import time
import glob
import datetime
import html
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

# ── AYARLAR VE DİZİNLER ───────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
CACHE_FILE = os.path.join(SCRIPT_DIR, ".scout_cache.json")
OUTPUT_DIR = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "Digests")
LOOKBACK_DAYS = 4

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not GEMINI_API_KEY:
    zshrc_path = os.path.expanduser("~/.zshrc")
    if os.path.exists(zshrc_path):
        try:
            with open(zshrc_path, "r", encoding="utf-8") as f:
                for line in f:
                    if "GEMINI_API_KEY" in line and "=" in line:
                        val = line.split("=", 1)[1].strip()
                        GEMINI_API_KEY = val.replace('"', '').replace("'", "")
                        break
        except Exception:
            pass

# ── 10 ÇATI MOC HARİTASI ──────────────────────────────────────
MOC_MAP = {
    "00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC": [
        "aralıklı açlık", "time-restricted feeding", "trf", "intermittent fasting", "fasting", "otofaji", "autophagy",
        "ghrelin", "irf4", "nutrient sensing", "su orucu", "prolonged fasting", "oruç"
    ],
    "00_Adipoz Doku ve Metabolizma_MOC": [
        "adipoz doku", "adipocyte", "adipose tissue", "obezite", "obesity", "tbk1", "ampk", "kilo döngüsü",
        "weight cycling", "lipokalin-2", "lipocalin-2", "gdf15", "kahverengi yağ", "brown adipose", "bat", "browning", "lipoliz"
    ],
    "00_GLP-1 ve Farmakolojik Müdahaleler_MOC": [
        "glp-1", "glp1", "semaglutid", "semaglutide", "tirzepatid", "tirzepatide", "inkretin", "incretin", "rebound",
        "miyosteatoz", "myosteatosis", "lean mass", "ozempic", "wegovy", "mounjaro"
    ],
    "00_Ultra İşlenmiş Besinler ve Diyet Kalitesi_MOC": [
        "ultra-processed", "ultra işlenmiş", "upf", "nova", "siga", "diyet kalitesi", "diet quality", "gıda matriksi",
        "food matrix", "iafns", "katkı maddeleri", "tatlandırıcı"
    ],
    "00_Kalori Kısıtlaması ve Enerji Metabolizması_MOC": [
        "kalori kısıtlaması", "calorie restriction", "enerji metabolizması", "energy expenditure", "adaptif termogenez",
        "adaptive thermogenesis", "neat", "solunum katsayısı", "respiratory quotient", "thrifty", "spendthrifty"
    ],
    "00_Beslenme Metodolojisi ve İstatistik_MOC": [
        "metodoloji", "methodology", "ölçek", "scale validation", "sem", "structural equation", "mendelian randomization",
        "beslenme geometrisi", "nutritional geometry", "biyoistatistik"
    ],
    "00_Yapay Zeka ve Dijital Beslenme_MOC": [
        "yapay zeka", "artificial intelligence", "ai", "machine learning", "augmented dietitian", "dijital sağlık",
        "digital nutrition", "llm", "large language model", "giyilebilir"
    ],
    "00_İnflamasyon ve İmmün Sistem_MOC": [
        "inflamasyon", "inflammation", "immün", "immune", "damp", "tlr4", "nlrp3", "ferroptozis", "ferroptosis",
        "tek karbon", "one-carbon", "folat", "b12", "metilasyon", "nrf2", "glutatyon"
    ],
    "00_Klinik Beslenme ve Hastalıklarda Tıbbi Beslenme Tedavisi_MOC": [
        "klinik beslenme", "clinical nutrition", "tıbbi beslenme", "medical nutrition therapy", "mnt", "adime", "ncp",
        "diyabet", "diabetes", "t2dm", "kvh", "dash", "dislipidemi", "enteral", "parenteral", "tpn", "malnütrisyon", "sarkopeni", "sarcopenic"
    ],
    "00_Beslenme Tarihi ve Sosyal Boyutlar_MOC": [
        "stigma", "damgalama", "weight stigma", "beslenme politikası", "food policy", "sosyal boyut", "post-truth",
        "dezenformasyon", "misinformation", "yeşil devrim", "green revolution"
    ]
}

# ── 10 DENGELİ AKADEMİK TEMA MATRİSİ ─────────────────────────
THEMATIC_PUBMED_MATRICES = [
    (
        "🤖 Yapay Zeka & Dijital Beslenme (AI & Machine Learning)",
        "(\"artificial intelligence\"[Title/Abstract] OR \"machine learning\"[Title/Abstract] OR \"deep learning\"[Title/Abstract] OR \"large language model\"[Title/Abstract]) AND (nutrition[Title/Abstract] OR dietetics[Title/Abstract] OR \"dietary assessment\"[Title/Abstract] OR \"personalized nutrition\"[Title/Abstract])"
    ),
    (
        "🍔 Ultra-İşlenmiş Besinler (UPF), Gıda Matriksi & Diyet Kalitesi",
        "(\"ultra-processed food\"[Title/Abstract] OR \"ultra-processed foods\"[Title/Abstract] OR \"NOVA classification\"[Title/Abstract] OR \"food matrix\"[Title/Abstract]) AND (\"diet quality\"[Title/Abstract] OR \"metabolic health\"[Title/Abstract] OR obesity[Title/Abstract] OR inflammation[Title/Abstract])"
    ),
    (
        "⏳ Aralıklı Açlık (Intermittent Fasting) & Otofaji",
        "(\"intermittent fasting\"[Title/Abstract] OR \"time-restricted eating\"[Title/Abstract] OR \"time-restricted feeding\"[Title/Abstract] OR \"alternate day fasting\"[Title/Abstract] OR \"fasting-mimicking\"[Title/Abstract]) AND (metabolism OR insulin OR autophagy OR \"body composition\" OR \"weight loss\")"
    ),
    (
        "🥑 Ketojenik Diyet, Ketogenez & Enerji Substratı",
        "(\"ketogenic diet\"[Title/Abstract] OR \"ketosis\"[Title/Abstract] OR \"ketone bodies\"[Title/Abstract] OR \"very low carbohydrate\"[Title/Abstract]) AND (obesity OR metabolism OR \"weight loss\" OR inflammation OR mitochondrial)"
    ),
    (
        "⚖️ Kilo Kaybı, Enerji Metabolizması & Adaptif Termogenez",
        "(\"weight loss\"[Title/Abstract] OR \"energy expenditure\"[Title/Abstract] OR \"adaptive thermogenesis\"[Title/Abstract] OR \"weight regain\"[Title/Abstract] OR \"resting metabolic rate\"[Title/Abstract]) AND (dietary[Title/Abstract] OR diet[Title/Abstract] OR nutrition[Title/Abstract])"
    ),
    (
        "🛡️ Obezite, İmmün Sistem & İmmünometabolizma",
        "(obesity[Title/Abstract] OR \"adipose tissue\"[Title/Abstract]) AND (immunometabolism[Title/Abstract] OR \"chronic inflammation\"[Title/Abstract] OR macrophage[Title/Abstract] OR cytokine[Title/Abstract] OR browning[Title/Abstract])"
    ),
    (
        "🏘️ Gıda Güvencesizliği, Obezojenik Çevre & Beslenme Politikaları",
        "(\"food insecurity\"[Title/Abstract] OR \"food environment\"[Title/Abstract] OR \"obesogenic environment\"[Title/Abstract] OR \"food desert\"[Title/Abstract]) AND (obesity OR nutrition OR \"diet quality\")"
    ),
    (
        "🧬 Multi-Omiks (Lipidomiks/Proteomiks) & Bağırsak Mikrobiyotası",
        "(lipidomics[Title/Abstract] OR metabolomics[Title/Abstract] OR \"gut microbiome\"[Title/Abstract] OR \"gut microbiota\"[Title/Abstract] OR nutrigenomics[Title/Abstract]) AND (diet OR \"weight loss\" OR nutrition OR obesity)"
    ),
    (
        "💊 GLP-1 & Farmakoterapi: Vücut Kompozisyonu & Kas Korunumu",
        "(\"GLP-1\"[Title/Abstract] OR semaglutide[Title/Abstract] OR tirzepatide[Title/Abstract] OR liraglutide[Title/Abstract]) AND (\"lean mass\" OR \"muscle loss\" OR myosteatosis OR \"body composition\" OR \"nutritional status\")"
    )
]

RSS_FEEDS = {
    "Resmi Uyarılar & Küresel Sağlık": [
        ("FDA MedWatch Safety Alerts", "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/medwatch/rss.xml"),
        ("WHO Global Health Releases", "https://www.who.int/rss-feeds/news-english.xml")
    ],
    "Seçkin Dergiler (Metabolizma, Nütrisyon & Endokrinoloji)": [
        ("Nature Metabolism", "https://www.nature.com/natmetab.rss"),
        ("Cell Metabolism", "https://www.cell.com/cell-metabolism/current.rss"),
        ("The Lancet Diabetes & Endocrinology", "https://www.thelancet.com/rssfeed/landia_current.xml"),
        ("News-Medical Clinical Nutrition", "https://www.news-medical.net/tag/feed/Nutrition.aspx")
    ],
    "Dernek & Rehber Çağrıları (ABD & İngiltere)": [
        ("ASN (American Society for Nutrition - US)", "https://nutrition.org/feed/"),
        ("The Nutrition Society (UK & Ireland)", "https://www.nutritionsociety.org/rss.xml"),
        ("The Obesity Society (TOS - US)", "https://www.obesity.org/feed/"),
        ("Retraction Watch (Bilimsel Denetim)", "https://retractionwatch.com/feed/")
    ],
    "Haberler & Bilimsel Analizler (Beslenme & Obezite Odaklı)": [
        ("ScienceDaily Clinical Nutrition & Diet", "https://www.sciencedaily.com/rss/health_medicine/nutrition.xml"),
        ("ScienceDaily Obesity & Metabolism", "https://www.sciencedaily.com/rss/health_medicine/obesity.xml")
    ],
    "🌍 Fon, COST Action, Erasmus & Postdoc Çağrıları": [
        ("COST Actions EU Research Networking & Working Groups", "https://www.cost.eu/feed/"),
        ("COST News & Funding Milestones", "https://www.cost.eu/news/feed/"),
        ("JobRxiv Academic & Postdoc Jobs", "https://jobrxiv.org/feed/")
    ],
    "💼 LinkedIn & Lider Araştırmacı Radarı": [
        ("David Ludwig & Boston Children's Nutrition Research", "https://medium.com/feed/@davidludwigmd"),
        ("Stephan Guyenet - Whole Health Source", "http://www.stephanguyenet.com/feed/"),
        ("NIH NIDDK Metabolism & Diabetes News", "https://www.niddk.nih.gov/news/archive/rss")
    ]
}

# ── ÇEKİRDEK SUBREDDIT HAVUZU ─────────────────────────────────
CORE_SUBREDDITS = [
    "ScientificNutrition",
    "nutrition",
    "intermittentfasting",
    "dietetics",
    "loseit",
    "ketoscience",
    "Semaglutide",
    "Ozempic",
    "TirzepatideRX",
    "fasting",
    "diabetes",
    "GutMicrobiome",
    "Longevity"
]

# ── ÖNBELLEK FONKSİYONLARI ────────────────────────────────────
def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"seen_ids": [], "last_run": ""}
    return {"seen_ids": [], "last_run": ""}

def save_cache(cache_data):
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[!] Önbellek kaydedilemedi: {e}")

# ── VAULT DİNAMİK TERİM & FİKİR HAVUZU ANALİZİ ───────────────
def load_vault_idea_pool():
    idea_pool = []
    idea_files = glob.glob(os.path.join(VAULT_DIR, "Çalışma Fikirleri", "**", "*.md"), recursive=True) + \
                 glob.glob(os.path.join(VAULT_DIR, "Fikirler", "**", "*.md"), recursive=True)
    for f in idea_files:
        name = os.path.basename(f).replace(".md", "")
        if len(name) > 5 and not name.startswith("."):
            idea_pool.append(name)
    return idea_pool

def extract_dynamic_terms():
    dynamic_terms = set()
    cutoff_time = time.time() - (30 * 24 * 60 * 60)
    
    moc_files = glob.glob(os.path.join(VAULT_DIR, "**", "*MOC*.md"), recursive=True)
    all_md_files = glob.glob(os.path.join(VAULT_DIR, "**", "*.md"), recursive=True)
    
    recent_files = [f for f in all_md_files if os.path.getmtime(f) >= cutoff_time]
    scan_files = list(set(moc_files + recent_files))
    
    for f in scan_files:
        if ".obsidian" in f or ".git" in f or f.startswith(OUTPUT_DIR):
            continue
        try:
            with open(f, "r", encoding="utf-8") as fp:
                content = fp.read()
            tags = re.findall(r"#([\w\-_/]+)", content)
            for t in tags:
                if len(t) > 3 and not t.isdigit() and not any(c in t for c in ["FCE4EC", "7C6AF7", "4FC8A0"]):
                    dynamic_terms.add(t.replace("-", " ").replace("_", " "))
            
            fm_match = re.search(r"MEKANİZMA:\s*\n((?:\s*-\s*.*?\n)+)", content)
            if fm_match:
                for line in fm_match.group(1).split("\n"):
                    clean = re.sub(r"[\[\]\-\"\']", "", line).strip()
                    if clean and len(clean) > 3:
                        dynamic_terms.add(clean)
        except Exception:
            pass
            
    filtered = [t for t in dynamic_terms if len(t.split()) <= 4][:6]
    return filtered

# ── HTTP İSTEK YARDIMCISI ──────────────────────────────────────
def fetch_url(url, timeout=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/json,*/*;q=0.8"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read()
    except Exception:
        return None

# ── REDDIT TOPLULUK MOTORU ────────────────────────────────────
def discover_and_fetch_reddit(dynamic_terms):
    reddit_items = []
    
    noise_keywords = ["progress pic", "recipe", "my face", "lost 50 lbs today", "rate my plate", "before and after", "scale victory"]
    scientific_keywords = [
        "study", "research", "paper", "trial", "glp-1", "glp1", "semaglutide", "tirzepatide", "ozempic",
        "fasting", "autophagy", "protein", "muscle", "insulin", "ketosis", "upf", "ultra-processed",
        "gut", "microbiome", "lipid", "cholesterol", "metabolism", "mechanism", "evidence", "review",
        "guideline", "myth", "debate", "carnivore", "vegan", "mediterranean", "sugar", "sweetener", "cardiovascular",
        "bioinformatics", "lipidomics", "proteomics", "metabolomics", "multi-omics", "transcriptomics",
        "precision nutrition", "nutrigenomics", "weight loss", "diet", "caloric restriction",
        "cost action", "erasmus", "postdoc", "fellowship", "grant", "msca", "marie curie", "call for papers"
    ]
    
    # En yüksek akademik sinyale sahip çekirdek sub'lar
    target_subs = ["ScientificNutrition", "dietetics", "intermittentfasting", "nutrition", "Semaglutide", "ketoscience"]
    
    for sub in target_subs:
        feed_url = f"https://www.reddit.com/r/{sub}/top/.rss?t=week&limit=10"
        headers = {
            "User-Agent": f"ObsidianScoutApp/2.0 (Academic Research; by /u/caner_researcher_{sub})"
        }
        try:
            req = urllib.request.Request(feed_url, headers=headers)
            with urllib.request.urlopen(req, timeout=6) as resp:
                xml_data = resp.read()
                root = ET.fromstring(xml_data)
                entries = root.findall(".//{http://www.w3.org/2005/Atom}entry")
                
                for entry in entries[:6]:
                    title_node = entry.find("{http://www.w3.org/2005/Atom}title")
                    link_node = entry.find("{http://www.w3.org/2005/Atom}link")
                    content_node = entry.find("{http://www.w3.org/2005/Atom}content")
                    
                    title = title_node.text.strip() if title_node is not None and title_node.text else ""
                    if not title:
                        continue
                        
                    link = link_node.attrib.get("href", "") if link_node is not None else ""
                    raw_content = content_node.text if content_node is not None and content_node.text else ""
                    clean_content = re.sub(r"<[^>]+>", " ", raw_content).strip()
                    
                    title_lower = title.lower()
                    if any(nk in title_lower for nk in noise_keywords):
                        continue
                        
                    if is_strictly_nutrition_relevant(title, clean_content):
                        reddit_items.append({
                            "id": f"REDDIT_{link if link else title}",
                            "title": title,
                            "subreddit": f"r/{sub}",
                            "score": 100,
                            "comments": 25,
                            "link": link,
                            "raw_text": f"[{sub}] {title}. {clean_content[:300]}",
                            "category": "Popüler Topluluk ve Sosyal Tartışmalar"
                        })
        except Exception:
            pass
        time.sleep(0.4)
        
    return reddit_items[:10]

# ── AKILLI ÇOK KATMANLI FİLTRE VE RELEVANCE MOTORU ────────────

# 1. Tamamen Biyomedikal Dışı / Salt Mühendislik / Tıbbi Cihazlar & Çevre Gürültüsü
ABSOLUTE_NON_BIOMEDICAL = [
    "cosmology", "cosmoverse", "astronomy", "astrophysics", "satellite broadband", "quantum computing",
    "robotics", "water resilience", "fruitcrews", "fruit tree", "crop yield", "plant salinity",
    "forestry", "geology", "solar panel", "wood anatomy", "xanthomonas", "eugain", "informatics",
    "spinal cord", "stimulator", "infinion", "boston scientific", "pacemaker", "defibrillator",
    "catheter", "stent", "orthopedic", "dental implant", "ventilator", "dialysis machine",
    "imaging system", "mri lead", "prosthesis", "surgical mesh", "surgical lead", "implantable",
    "greenspace", "green space", "streetview", "air pollution", "traffic noise", "urban green",
    "dementia risk in older adults", "deep brain stimulation"
]

# 2. İdari, Diplomasi ve Salt Kurumsal Gürültü (Bilimsel mekanizma yoksa elenir)
ADMINISTRATIVE_NOISE = [
    "eib global", "lithuanian academy of sciences", "stsm committee member awarded",
    "strategic partnership to drive impact and strengthen health systems in africa",
    "short-term scientific missions shape research journeys", "from conference grant to career milestone",
    "signed an agreement for a €", "loan agreement", "memorandum of understanding",
    "growing older better", "recall: boston scientific"
]

# 3. Bağlamsal Terimler (Enfeksiyon, Coğrafya, Veterinerlik vb. - SADECE güçlü beslenme mekanizması varsa kabul edilir)
CONTEXTUAL_MEDICAL_TERMS = [
    "malaria", "tuberculosis", "dengue", "hiv", "ebola", "zika", "polio", "lebanon", "african union",
    "veterinary", "poultry", "swine", "yak", "cattle", "bovine", "listeria", "streptococcus suis", "mycelium"
]

# 4. Yüksek Öncelikli Çekirdek Beslenme & Metabolizma Mekanizmaları (Dr. Caner Özyıldırım MOC Çekirdeği)
HIGH_IMPACT_CORE_MECHANISMS = [
    "adipose", "adipocyte", "lipolysis", "thermogenesis", "browning", "brown adipose", "vwat", "scat",
    "intermittent fasting", "time-restricted eating", "time-restricted feeding", "tre", "trf", "fasting-mimicking",
    "autophagy", "calorie restriction", "caloric restriction", "energy expenditure", "adaptive thermogenesis",
    "glp-1", "glp1", "semaglutide", "tirzepatide", "liraglutide", "incretin", "ozempic", "wegovy", "mounjaro",
    "ultra-processed", "upf", "nova classification", "food matrix", "diet quality",
    "gut microbiota", "gut microbiome", "short-chain fatty acids", "scfa", "bifidobacterium",
    "sarcopenia", "sarcopenic", "myosteatosis", "lean mass", "body composition", "weight loss", "weight regain",
    "ketogenic", "ketosis", "ketone", "dietitian", "medical nutrition therapy", "clinical nutrition",
    "ferroptosis", "lipocalin-2", "lipokalin-2", "homa-ir", "insulin resistance", "spendthrifty", "thrifty"
]

# 5. Genel Beslenme ve Diyetetik Terimleri
GENERAL_NUTRITION_TERMS = [
    "nutrition", "nutrient", "nutritional", "diet", "dietary", "dietetics", "meal", "eating",
    "food", "sweetener", "sugar-sweetened", "protein intake", "amino acid", "lipid", "cholesterol",
    "glucose", "hba1c", "type 2 diabetes", "t2dm", "t1dm", "metabolic syndrome", "dyslipidemia",
    "steatotic liver", "masld", "nafld", "malnutrition", "enteral", "parenteral", "food insecurity"
]

CAREER_KEYWORDS = ["postdoc", "fellowship", "grant", "cost action", "erasmus", "marie curie", "msca", "call for papers", "award", "conference", "phd position"]

def contains_word_or_phrase(text, terms_list):
    text_clean = text.lower()
    for term in terms_list:
        term_clean = term.lower()
        if len(term_clean) <= 4:
            # Kısa kısaltmalar ve 3-4 harfli terimler (tre, trf, upf, diet, food, b12) için kesin kelime sınırı (\b) şarttır
            if re.search(r"\b" + re.escape(term_clean) + r"\b", text_clean):
                return True
        else:
            if term_clean in text_clean:
                return True
    return False

def is_strictly_nutrition_relevant(title, text=""):
    combined = title + " " + text
    
    # 1. İdari ve Salt Fonksiyonel Bürokrasi Gürültüsü Kontrolü (Hemen Ele)
    if contains_word_or_phrase(combined, ADMINISTRATIVE_NOISE):
        return False

    # 2. Mutlak Biyomedikal Dışı / Tıbbi Cihaz / Çevre Gürültüsü Kontrolü
    # Eğer metinde bu terimler geçiyorsa, SADECE yüksek etkili çekirdek beslenme mekanizması varsa izin ver
    has_non_bio = contains_word_or_phrase(combined, ABSOLUTE_NON_BIOMEDICAL)
    if has_non_bio:
        has_strong_core = contains_word_or_phrase(combined, HIGH_IMPACT_CORE_MECHANISMS)
        if not has_strong_core:
            return False

    # 3. Kariyer / Fon / COST Çağrısı Kontrolü
    is_career = contains_word_or_phrase(combined, CAREER_KEYWORDS)
    if is_career:
        has_nutr = contains_word_or_phrase(combined, HIGH_IMPACT_CORE_MECHANISMS + GENERAL_NUTRITION_TERMS)
        return has_nutr

    # 4. Bağlamsal Tıbbi/Coğrafi Terim Kontrolü (Malaria, Lebanon, Tuberculosis, Veterinerlik vb.)
    has_contextual = contains_word_or_phrase(combined, CONTEXTUAL_MEDICAL_TERMS)
    if has_contextual:
        has_core = contains_word_or_phrase(combined, HIGH_IMPACT_CORE_MECHANISMS)
        has_gen = contains_word_or_phrase(combined, GENERAL_NUTRITION_TERMS)
        return (has_core or has_gen)

    # 5. Standart Akış: Çekirdek veya Genel Beslenme Terimi Varlığı
    return contains_word_or_phrase(combined, HIGH_IMPACT_CORE_MECHANISMS + GENERAL_NUTRITION_TERMS)

# ── NORMALİZASYON VE MÜKERRER ENGELLEME YARDIMCILARI ────────
def normalize_string_key(s):
    if not s:
        return ""
    clean = re.sub(r"[^\w\s]", "", s.lower())
    return re.sub(r"\s+", " ", clean).strip()

def normalize_url(url):
    if not url:
        return ""
    parsed = urllib.parse.urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip("/")

def load_recent_digests_history(n=2):
    """
    00 Kontrol Merkezi/Digests/ altındaki son n adet Digest_*.md dosyasını okur.
    Tüm başlıkları, PMID'leri ve URL linklerini yakalar.
    Böylece son 2 digestte yer almış hiçbir kaynak tekrar bültene eklenmez.
    """
    seen_titles = set()
    seen_ids = set()
    
    digest_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "Digest_*.md")), reverse=True)
    target_files = digest_files[:n]
    
    for df in target_files:
        try:
            with open(df, "r", encoding="utf-8") as f:
                content = f.read()
                
            # 1. Başlıkları yakala (### 📌 ..., #### 📌 ..., #### 💬 ..., ### 💬 ...)
            title_matches = re.findall(r"^#{2,4}\s+(?:📌|💬)\s*(?:\[[^\]]+\]\s*)?([^\n#]+)", content, re.MULTILINE)
            for tm in title_matches:
                norm_t = normalize_string_key(tm.strip())
                if norm_t:
                    seen_titles.add(norm_t)
                    
            # 2. PubMed ID'lerini yakala
            pmid_matches = re.findall(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", content)
            for pmid in pmid_matches:
                seen_ids.add(f"PMID_{pmid}")
                seen_ids.add(pmid)
                seen_ids.add(f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/")
                seen_ids.add(f"https://pubmed.ncbi.nlm.nih.gov/{pmid}")
                
            # 3. Tüm Markdown bağlantılarını yakala
            url_matches = re.findall(r"\[.*?\]\((https?://[^\s\)]+)\)", content)
            for u in url_matches:
                seen_ids.add(u)
                norm_u = normalize_url(u)
                if norm_u:
                    seen_ids.add(norm_u)
        except Exception as e:
            print(f"[!] Son digest geçmişi okunamadı ({df}): {e}")
            
    return seen_titles, seen_ids

THEME_KEYWORDS_MAP = {
    "🤖 Yapay Zeka & Dijital Beslenme (AI & Machine Learning)": ["artificial intelligence", "machine learning", "deep learning", "large language model", "llm", "augmented dietitian", "digital nutrition", "digital health"],
    "🍔 Ultra-İşlenmiş Besinler (UPF), Gıda Matriksi & Diyet Kalitesi": ["ultra-processed", "upf", "nova", "food matrix", "sweetener", "emulsifier", "diet quality", "processed food", "sugar-sweetened"],
    "⏳ Aralıklı Açlık (Intermittent Fasting) & Otofaji": ["intermittent fasting", "time-restricted eating", "time-restricted feeding", "time restricted eating", "time restricted feeding", "tre", "trf", "fasting-mimicking", "alternate-day fasting", "alternate day fasting", "prolonged fasting"],
    "🥑 Ketojenik Diyet, Ketogenez & Enerji Substratı": ["ketogenic", "ketosis", "ketone", "ketones", "very low carbohydrate", "beta-hydroxybutyrate"],
    "💊 GLP-1 & Farmakoterapi: Vücut Kompozisyonu & Kas Korunumu": ["glp-1", "glp1", "semaglutide", "tirzepatide", "liraglutide", "incretin", "ozempic", "wegovy", "mounjaro", "myosteatosis", "lean mass"],
    "🧬 Multi-Omiks (Lipidomiks/Proteomiks) & Bağırsak Mikrobiyotası": ["microbiome", "microbiota", "bifidobacterium", "scfa", "short-chain fatty", "lipidomics", "proteomics", "metabolomics", "nutrigenomics", "multi-omics"],
    "🛡️ Obezite, İmmün Sistem & İmmünometabolizma": ["immunometabolism", "chronic inflammation", "macrophage", "cytokine", "ferroptosis", "adipose tissue", "adipocyte", "browning"],
    "🏘️ Gıda Güvencesizliği, Obezojenik Çevre & Beslenme Politikaları": ["food insecurity", "food environment", "obesogenic", "food desert", "socioeconomic"],
    "⚖️ Kilo Kaybı, Enerji Metabolizması & Adaptif Termogenez": ["weight loss", "energy expenditure", "energy metabolism", "adaptive thermogenesis", "weight regain", "resting metabolic rate", "respiratory quotient"]
}

# ── DR. CANER ÖZYILDIRIM ÖZEL KÜRASYON & AKADEMİK BEĞENİ AĞIRLIKLARI ──
HIGH_PRIORITY_TOPICS = [
    # 1. Aralıklı Açlık, Otofaji, TRE (Ders ve Kitap Çekirdeği)
    ("intermittent fasting", 10), ("time-restricted eating", 10), ("time-restricted feeding", 10), ("tre", 8), ("trf", 8), ("fasting", 6), ("autophagy", 8), ("otofaji", 8),
    # 2. GLP-1, İnkretin, Kas Korunumu & Sarkopeni
    ("glp-1", 10), ("semaglutide", 10), ("tirzepatide", 10), ("incretin", 8), ("sarcopenia", 10), ("sarcopenic", 10), ("myosteatosis", 10), ("lean mass", 9), ("body composition", 8), ("inappropriate use", 8),
    # 3. UPF, Gıda Matriksi, Katkı Maddeleri & NOVA Eleştirisi
    ("ultra-processed", 10), ("upf", 10), ("nova", 9), ("food matrix", 10), ("titanium dioxide", 10), ("e171", 10), ("sweetener", 7), ("emulsifier", 8), ("dietary inflammatory index", 9),
    # 4. Paradigma & Metabolizma (CIM vs Enerji Dengesi, Termogenez, Allostaz)
    ("carbohydrate-insulin", 10), ("energy balance", 8), ("adaptive thermogenesis", 10), ("energy expenditure", 8), ("insulin resistance", 8), ("allostatic", 9), ("weight cycling", 9),
    # 5. Tek Karbon, B12, Mikrobiyom & Metabolom
    ("b12", 9), ("vitamin b12", 10), ("one-carbon", 10), ("methylation", 8), ("scfa", 9), ("short-chain fatty", 9), ("microbiome", 8), ("microbiota", 8), ("low-fodmap", 9), ("fodmap", 8), ("brown adipose", 9), ("bcaa", 8),
    # 6. Yapay Zeka & Dijital Beslenme Metodolojisi
    ("artificial intelligence", 10), ("machine learning", 10), ("large language model", 9), ("dietary assessment", 8), ("24-hour recall", 9), ("precision nutrition", 9), ("computational", 8),
    # 7. İmmünometabolizma, Adipoz Doku & Adipo-Onkoloji
    ("immunometabolism", 10), ("adipocyte", 8), ("adipose tissue", 8), ("macrophage", 8), ("adipo-oncology", 10), ("sasp", 9), ("browning", 8), ("fibrosis", 8),
    # 8. Klinik & Özel Fenotipler
    ("type 5 diabetes", 10), ("diabetes remission", 9), ("glucose curve", 9), ("cgm", 8), ("medical nutrition therapy", 8)
]

HIGH_IMPACT_JOURNALS = [
    "lancet", "nature", "cell", "diabetes care", "gut microbes", "j acad nutr diet", "am j clin nutr",
    "diabetes", "immunity", "pnas", "endocr", "signal transduct", "ageing res rev", "obes facts", "obes rev", "curr obes rep"
]

STUDY_TYPE_BONUS = [
    ("randomized controlled trial", 8), ("randomized", 6), ("rct", 8),
    ("systematic review", 7), ("meta-analysis", 8), ("clinical trial", 6), ("cohort", 5)
]

def calculate_preference_score(item):
    text = (item.get("title", "") + " " + item.get("source", "") + " " + item.get("raw_text", "")).lower()
    score = 0
    
    # 1. Kullanıcı Beğeni & Öncelik Puanı
    for kw, weight in HIGH_PRIORITY_TOPICS:
        if kw in text:
            score += weight
            
    # 2. Prestijli Dergi Puanı
    source_lower = item.get("source", "").lower()
    for j in HIGH_IMPACT_JOURNALS:
        if j in source_lower:
            score += 6
            break
            
    # 3. Kanıt Düzeyi Puanı
    for st, bonus in STUDY_TYPE_BONUS:
        if st in text:
            score += bonus
            break
            
    return score

def determine_best_theme(title, default_theme):
    t_lower = title.lower()
    best_theme = default_theme
    max_score = 0
    for theme_name, kws in THEME_KEYWORDS_MAP.items():
        score = sum(3 if kw in t_lower else 0 for kw in kws)
        if score > max_score:
            max_score = score
            best_theme = theme_name
    return best_theme

LOOKBACK_DAYS = 4

# ── PUBMED MOTORU ─────────────────────────────────────────────
def fetch_pubmed_articles(dynamic_terms):
    articles_map = {} # pmid/norm_title -> article_dict (tekil yerleşim için)
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=LOOKBACK_DAYS)
    date_filter = f"{start_date.strftime('%Y/%m/%d')}:{end_date.strftime('%Y/%m/%d')}[pdat]"
    
    for theme_name, q in THEMATIC_PUBMED_MATRICES:
        term_query = f"({q}) AND {date_filter}"
        encoded_term = urllib.parse.quote(term_query)
        esearch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={encoded_term}&retmode=json&retmax=25&sort=pub_date"
        
        data = fetch_url(esearch_url)
        if not data:
            continue
        try:
            res = json.loads(data.decode("utf-8"))
            id_list = res.get("esearchresult", {}).get("idlist", [])
            if not id_list:
                continue
                
            esummary_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={','.join(id_list)}&retmode=json"
            sum_data = fetch_url(esummary_url)
            if not sum_data:
                continue
            sum_json = json.loads(sum_data.decode("utf-8")).get("result", {})
            
            for pmid in id_list:
                info = sum_json.get(pmid)
                if not info:
                    continue
                title = info.get("title", "").strip().rstrip(".")
                
                # 🛑 KESİN ELİYİCİ SÜZGEÇ
                if not is_strictly_nutrition_relevant(title):
                    continue
                
                norm_title = normalize_string_key(title)
                if not norm_title or pmid in articles_map or norm_title in articles_map:
                    continue
                    
                best_theme = determine_best_theme(title, theme_name)
                source = info.get("source", "PubMed Journal")
                pubdate = info.get("pubdate", "")
                link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                
                art_dict = {
                    "id": f"PMID_{pmid}",
                    "title": title,
                    "source": f"PubMed ({source})",
                    "pubdate": pubdate,
                    "link": link,
                    "raw_text": f"{title}. Published in {source} on {pubdate}.",
                    "theme": best_theme
                }
                articles_map[pmid] = art_dict
                articles_map[norm_title] = art_dict
        except Exception:
            continue
        time.sleep(0.2)
        
    # Tekil liste oluştur
    unique_articles = []
    seen_ids = set()
    for art in articles_map.values():
        if art["id"] not in seen_ids:
            seen_ids.add(art["id"])
            unique_articles.append(art)
            
    return unique_articles

# ── RSS / FEED MOTORU ─────────────────────────────────────────
def fetch_rss_feed(category_name, feed_name, url):
    items = []
    raw_data = fetch_url(url, timeout=10)
    if not raw_data:
        return items
    
    xml_text = raw_data.decode("utf-8", errors="ignore")
    raw_blocks = re.findall(r"<(?:item|entry)[\s>](.*?)</(?:item|entry)>", xml_text, re.DOTALL | re.IGNORECASE)
    
    for block in raw_blocks[:15]:
        title_m = re.search(r"<(?:[a-zA-Z0-9_\-]+:)?title[^>]*>(.*?)</(?:[a-zA-Z0-9_\-]+:)?title>", block, re.DOTALL | re.IGNORECASE)
        link_m = re.search(r"<(?:[a-zA-Z0-9_\-]+:)?link[^>]*>(.*?)</(?:[a-zA-Z0-9_\-]+:)?link>", block, re.DOTALL | re.IGNORECASE)
        if not link_m:
            link_m = re.search(r"<(?:[a-zA-Z0-9_\-]+:)?link[^>]*href=[\"\\\x27]([^\"\\\x27]+)[\"\\\x27]", block, re.IGNORECASE)
        desc_m = re.search(r"<(?:[a-zA-Z0-9_\-]+:)?(?:description|summary|content)[^>]*>(.*?)</(?:[a-zA-Z0-9_\-]+:)?(?:description|summary|content)>", block, re.DOTALL | re.IGNORECASE)
        
        title = title_m.group(1).strip() if title_m else ""
        title = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", title)
        title = html.unescape(re.sub(r"<[^>]+>", "", title)).strip()
        
        if not title:
            continue
            
        link = link_m.group(1).strip() if link_m else ""
        link = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", link).strip()
        
        desc = desc_m.group(1).strip() if desc_m else ""
        desc = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", desc)
        desc = html.unescape(re.sub(r"<[^>]+>", " ", desc)).strip()
        
        # 🛑 KESİN ELİYİCİ SÜZGEÇ: Alakasız konuları ele
        if not is_strictly_nutrition_relevant(title, desc):
            continue
            
        item_id = link if link else title
        
        items.append({
            "id": item_id,
            "title": title,
            "source": feed_name,
            "link": link,
            "raw_text": desc[:400] if desc else title,
            "category": category_name
        })
        
    return items

# ── MOC EŞLEŞTİRME & ANALİTİK TÜRKÇE SENTEZ MOTORU ───────────
def suggest_mocs(text):
    suggested = []
    text_lower = text.lower()
    for moc_name, keywords in MOC_MAP.items():
        if any(kw in text_lower for kw in keywords):
            suggested.append(f"[[{moc_name}]]")
    return list(dict.fromkeys(suggested))[:3]

def generate_contextual_analysis(item):
    """
    Her içerik için spesifik, makaleye özel 3 katmanlı zengin Türkçe analiz üretir:
    1. ozet: Ne bulundu? (Makalenin gerçek konusu ve bulguları)
    2. gerekce: Neden eklendi? (Hangi MOC/araştırma hattına katkı sağlıyor?)
    3. kullanim: Nasıl kullanılabilir? (Ders / Substack / Proje)
    """
    title = item["title"]
    source = item.get("source", item.get("subreddit", "Bülten"))
    raw = item.get("raw_text", "")
    suggested_mocs = suggest_mocs(title + " " + raw)
    
    # 1. Gemini API Denemesi (İnternet / API Key mevcutsa)
    if GEMINI_API_KEY:
        models_to_try = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
        for mod in models_to_try:
            try:
                prompt = (
                    f"Sen Dr. Caner Özyıldırım'ın (Akdeniz Üni. Beslenme ve Diyetetik Bölümü, Endokrinoloji Arş. Gör. Dr.) "
                    f"akademik Obsidian kasasını yöneten uzman bir klinik diyetisyen ve araştırmacısın.\n"
                    f"Aşağıdaki spesifik makaleyi/gelişmeyi analiz et:\n\n"
                    f"Başlık: {title}\n"
                    f"Kaynak: {source}\n"
                    f"İçerik/Özet: {raw}\n\n"
                    f"GÖREV: Bu makalenin GERÇEK içeriğine, bulgularına ve metodolojisine odaklanan tamamen ÖZGÜN bir Türkçe analiz üret.\n"
                    f"Asla genel-geçer şablon cümle kullanma. Makale neyi bulduysa tam olarak onu yaz.\n\n"
                    f"Aşağıdaki JSON formatında YALNIZCA geçerli bir JSON objesi döndür:\n"
                    f"{{\n"
                    f'  "ozet": "2-3 cümlelik bu çalışmaya ÖZGÜ bilimsel Türkçe özet (Çalışmada spesifik olarak ne incelendi, hangi metodoloji/model kullanıldı ve ne bulundu?)",\n'
                    f'  "gerekce": "1-2 cümlelik gerekçe (Bu spesifik bulgu Caner hocanın araştırma alanına / MOC konularına nasıl bir katkı sağlıyor?)",\n'
                    f'  "kullanim": "1-2 cümlelik somut eylem önerisi (Ders, Substack veya araştırma projesinde spesifik olarak nasıl değerlendirilebilir?)"\n'
                    f"}}"
                )
                api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{mod}:generateContent?key={GEMINI_API_KEY}"
                payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
                req = urllib.request.Request(api_url, data=payload, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    res_data = json.loads(resp.read().decode("utf-8"))
                    cand_text = res_data["candidates"][0]["content"]["parts"][0]["text"].strip()
                    json_str = re.sub(r"^```json\s*", "", cand_text)
                    json_str = re.sub(r"```$", "", json_str).strip()
                    parsed = json.loads(json_str)
                    if "ozet" in parsed and "gerekce" in parsed and "kullanim" in parsed:
                        return parsed["ozet"], parsed["gerekce"], parsed["kullanim"], suggested_mocs
            except Exception:
                pass

    # 2. Akıllı, Başlığa ve Ham Metne Özel Deterministik Sentez (Asla tek tip şablon yok!)
    clean_raw = re.sub(r"<[^>]+>", " ", raw).strip()
    clean_raw = re.sub(r"\s+", " ", clean_raw)
    
    # Başlıktan ve ham metinden özgün bilimsel özet derle
    if len(clean_raw) > 50 and clean_raw.lower() != title.lower():
        snippet = clean_raw[:220].rstrip(".") + "..."
        ozet = f"{source} bülteninde yayımlanan bu çalışma ('{title}'), {snippet} kapsamındaki bulguları ve klinik sonuçları değerlendirmektedir."
    else:
        ozet = f"Bu araştırma, '{title}' odak alanında yürütülen güncel klinik/biyokimyasal kanıtları ve sonuçları sunmaktadır."
        
    moc_names = [m.replace("[[", "").replace("]]", "").replace("00_", "").replace("_MOC", "") for m in suggested_mocs]
    moc_text = ", ".join(moc_names) if moc_names else "Klinik Beslenme ve Metabolizma"
    gerekce = f"Bu çalışma, kasadaki {moc_text} araştırma hattımızda güncel literatür kanıt tabanını doğrudan beslemektedir."
    
    # Çalışma tipine göre eylem önerisi
    t_lower = title.lower()
    if "rct" in t_lower or "randomized" in t_lower or "trial" in t_lower:
        kullanim = f"Randomize kontrollü klinik kanıt olarak BES420/BES339 derslerinde kanıt piramidi analizi ve vaka sunumlarında kullanılabilir."
    elif "review" in t_lower or "meta-analysis" in t_lower or "systematic" in t_lower:
        kullanim = f"Sistematik derleme/meta-analiz verisi olarak Substack bülteninde 'Mevcut Kanıt Durumu' derinlemesine analizinde değerlendirilebilir."
    elif any(k in t_lower for k in ["ultra-processed", "upf", "nova"]):
        kullanim = f"BES339 dersinde 'NOVA Sınıflandırmasının Bilimsel Sınırları' sınıf-içi atölyesinde veya Substack bülteninde eleştirel analiz olarak kullanılabilir."
    elif any(k in t_lower for k in ["glp-1", "semaglutide", "tirzepatide"]):
        kullanim = f"BES339 dersinde 'Farmakoterapi vs Diyet' münazarasında veya Substack'te kas kütlesi korunumu bülteni olarak işlenebilir."
    else:
        kullanim = f"İlgili MOC altındaki mekanistik notlara çapraz bağlantı (backlink) verilerek araştırma hipotezi geliştirmede değerlendirilebilir."
        
    return ozet, gerekce, kullanim, suggested_mocs

def extract_living_evidence(item, synthesis):
    text = item["title"] + " " + item.get("raw_text", "") + " " + synthesis
    
    st = "Observational / Clinical"
    tl = text.lower()
    if "randomized" in tl or "rct" in tl or "trial" in tl:
        st = "RCT"
    elif "meta-analysis" in tl or "systematic review" in tl:
        st = "Meta-Analysis"
    elif "cohort" in tl or "longitudinal" in tl:
        st = "Cohort"
    elif "cross-sectional" in tl or "survey" in tl:
        st = "Cross-Sectional"
    elif "mice" in tl or "rat" in tl or "animal" in tl:
        st = "Animal Study"

    sample_size = None
    n_match = re.search(r"\b(?:n|N)\s*=\s*(\d+)", text)
    if n_match:
        sample_size = int(n_match.group(1))

    p_summary = "Belirtilmemiş"
    ev_direction = "inconclusive"
    p_match = re.search(r"\b[pP]\s*([<=><])\s*([01]?\.?\d+)", text)
    if p_match:
        p_summary = f"p {p_match.group(1)} {p_match.group(2)}"
        try:
            val = float(p_match.group(2))
            if p_match.group(1) == "<" or val < 0.05:
                ev_direction = "positive"
            elif val >= 0.05:
                ev_direction = "null"
        except Exception:
            pass
    elif "significant" in tl and "not significant" not in tl:
        ev_direction = "positive"
        p_summary = "p < 0.05 (raporlanan)"
    elif "no significant" in tl or "not significant" in tl:
        ev_direction = "null"
        p_summary = "p > 0.05 (anlamsız)"

    is_contradictory = False
    if any(ck in tl for ck in ["contradict", "paradox", "unexpected", "contrary to", "challenged"]):
        is_contradictory = True
        ev_direction = "contradictory"

    return {
        "study_type": st,
        "sample_size": sample_size,
        "evidence_direction": ev_direction,
        "p_value_summary": p_summary,
        "is_contradictory": is_contradictory
    }

# ── ANA ÇALIŞTIRMA PİPELİNE'I ─────────────────────────────────
def run_pipeline():
    start_time = datetime.datetime.now()
    date_str = start_time.strftime("%Y-%m-%d")
    print(f"\n🚀 Nutrition Scout Başlatılıyor... [{start_time.strftime('%d.%m.%Y %H:%M')}]")
    print(f"📁 Kasa Konumu: {VAULT_DIR}")
    
    cache = load_cache()
    seen_set = set(cache.get("seen_ids", []))
    new_seen_ids = list(seen_set)
    
    # Son 2 Digest dosyasından başlık ve ID geçmişini yükle (Mükerrer engelleme)
    recent_titles, recent_ids = load_recent_digests_history(n=2)
    print(f"📚 Son 2 digestten {len(recent_titles)} başlık ve {len(recent_ids)} kimlik korumaya alındı.")
    
    # 1. Dinamik Terim Genişletme
    print("🔍 Kasa MOC ve son 30 gün notları taranıyor...")
    dynamic_terms = extract_dynamic_terms()
    if dynamic_terms:
        print(f"✨ Tespit Edilen Dinamik Terimler: {', '.join(dynamic_terms)}")
    else:
        print("ℹ️ Dinamik ek terim bulunmadı, statik havuz devrede.")
        
    categories_output = {
        "Resmi Uyarılar (FDA/EFSA/WHO)": [],
        "Dernek & Rehber Güncellemeleri (ABD & İngiltere: ASN, BDA, The Nutrition Society, EASO, ESPEN)": [],
        "Yeni Akademik Yayınlar (PubMed & Multi-Omiks)": [],
        "Genel Sağlık Haberleri / Blog": [],
        "Popüler Topluluk ve Sosyal Tartışmalar (Reddit Trendleri)": [],
        "🌍 Fon, COST Action, Erasmus, Postdoc & Kariyer Çağrıları": [],
        "💼 LinkedIn & Lider Araştırmacı Radarı": []
    }
    
    active_seen_titles = set(recent_titles)
    active_seen_ids = set(seen_set) | set(recent_ids)

    def try_add_item(category_key, item_dict):
        title = item_dict.get("title", "")
        norm_t = normalize_string_key(title)
        item_id = item_dict.get("id", "")
        link = item_dict.get("link", "")
        norm_id = normalize_url(item_id) if item_id else ""
        norm_link = normalize_url(link) if link else ""
        
        if not norm_t:
            return False
            
        # Eğer bu oturumda, önbellekte veya son 2 digestte zaten görülmüşse ekleme (Tekil yerleşim kuralı)
        if norm_t in active_seen_titles:
            return False
        if item_id and item_id in active_seen_ids:
            return False
        if norm_id and norm_id in active_seen_ids:
            return False
        if link and link in active_seen_ids:
            return False
        if norm_link and norm_link in active_seen_ids:
            return False
            
        # Kaydet ve tekil olarak sadece bu kategoriye ekle
        active_seen_titles.add(norm_t)
        if item_id:
            active_seen_ids.add(item_id)
            new_seen_ids.append(item_id)
        if norm_id:
            active_seen_ids.add(norm_id)
        if link:
            active_seen_ids.add(link)
        if norm_link:
            active_seen_ids.add(norm_link)
            
        categories_output[category_key].append(item_dict)
        return True
    
    # 2. Resmi Uyarılar
    print("\n📡 1/7 Resmi Uyarılar & Küresel Sağlık Otoriteleri taranıyor (FDA / EFSA / WHO)...")
    for feed_name, url in RSS_FEEDS.get("Resmi Uyarılar & Küresel Sağlık", []):
        items = fetch_rss_feed("Resmi Uyarılar (FDA/EFSA/WHO)", feed_name, url)
        for it in items:
            try_add_item("Resmi Uyarılar (FDA/EFSA/WHO)", it)

    # 2b. Seçkin Dergiler (Metabolizma, Nütrisyon & Endokrinoloji)
    for feed_name, url in RSS_FEEDS.get("Seçkin Dergiler (Metabolizma, Nütrisyon & Endokrinoloji)", []):
        items = fetch_rss_feed("Genel Sağlık Haberleri / Blog", feed_name, url)
        for it in items:
            try_add_item("Genel Sağlık Haberleri / Blog", it)
                
    # 3. Dernek & Rehber & Bağımsız Denetim (ABD & İngiltere)
    print("📡 2/7 Dernek, Rehber & Araştırma Çağrıları taranıyor (ASN, The Nutrition Society, BDA, TOS, EASO, ESPEN)...")
    for feed_name, url in RSS_FEEDS.get("Dernek & Rehber Çağrıları (ABD & İngiltere)", []):
        items = fetch_rss_feed("Dernek & Rehber Güncellemeleri (ABD & İngiltere: ASN, BDA, The Nutrition Society, EASO, ESPEN)", feed_name, url)
        for it in items:
            try_add_item("Dernek & Rehber Güncellemeleri (ABD & İngiltere: ASN, BDA, The Nutrition Society, EASO, ESPEN)", it)

    # 4. PubMed & Multi-Omiks (Tekil Tema Eşlemeli)
    print("📡 3/7 PubMed son 4 günün yayınları ve Multi-Omiks taranıyor (NCBI E-utilities)...")
    pubmed_items = fetch_pubmed_articles(dynamic_terms)
    for it in pubmed_items:
        try_add_item("Yeni Akademik Yayınlar (PubMed & Multi-Omiks)", it)
            
    # 5. Sağlık ve Bilim Haberleri
    print("📡 4/7 Genel Sağlık & Bilim haberleri taranıyor (ScienceDaily, STAT News)...")
    for feed_name, url in RSS_FEEDS.get("Haberler & Bilimsel Analizler (Beslenme & Obezite Odaklı)", []):
        items = fetch_rss_feed("Genel Sağlık Haberleri / Blog", feed_name, url)
        for it in items:
            try_add_item("Genel Sağlık Haberleri / Blog", it)

    # 6. Dinamik Reddit Topluluk Keşfi & Popüler Tartışmalar
    print("📡 5/7 Reddit Beslenme Toplulukları ve Trendleri taranıyor (20 Subreddit)...")
    reddit_items = discover_and_fetch_reddit(dynamic_terms)
    for it in reddit_items:
        try_add_item("Popüler Topluluk ve Sosyal Tartışmalar (Reddit Trendleri)", it)

    # 7. Fon, COST Action, Erasmus, Postdoc & Kariyer Çağrıları
    print("📡 6/7 COST Actions, Erasmus, EURAXESS & Marie Curie fon çağrıları taranıyor...")
    for feed_name, url in RSS_FEEDS.get("🌍 Fon, COST Action, Erasmus & Postdoc Çağrıları", []):
        items = fetch_rss_feed("🌍 Fon, COST Action, Erasmus, Postdoc & Kariyer Çağrıları", feed_name, url)
        for it in items:
            try_add_item("🌍 Fon, COST Action, Erasmus, Postdoc & Kariyer Çağrıları", it)

    # 8. LinkedIn & Lider Araştırmacı Radarı
    print("📡 7/7 LinkedIn & Lider Araştırmacı Radarı taranıyor (David Ludwig, Kevin Hall, Stephan Guyenet)...")
    for feed_name, url in RSS_FEEDS.get("💼 LinkedIn & Lider Araştırmacı Radarı", []):
        items = fetch_rss_feed("💼 LinkedIn & Lider Araştırmacı Radarı", feed_name, url)
        for it in items:
            try_add_item("💼 LinkedIn & Lider Araştırmacı Radarı", it)

# ── RAPOR ÜRETİMİ VE ENTEGRASYON DÖNGÜSÜ ──────────────────────
    total_found = sum(len(v) for v in categories_output.values())
    
    report_lines = [
        "---",
        "tags: [digest, scout, bulten]",
        f"TARİH: \"{date_str}\"",
        f"TOPLAM_İÇERİK: {total_found}",
        "---",
        "",
        f"# 🔬 Akademik, Klinik Nütrisyon & Kariyer Bülteni — {date_str}",
        "",
        f"> **Tarama Aralığı:** Son {LOOKBACK_DAYS} gün · **Çalışma Zamanı:** {start_time.strftime('%d.%m.%Y %H:%M')}",
        ""
    ]
    
    print("\n" + "=" * 65)
    print(f"📊 TARAMA RAPORU — {date_str}")
    print("=" * 65 + "\n")
    
    cat_keys = list(categories_output.keys())
    
    # R / Meta-analiz köprüsü için extract_stats import
    try:
        import extract_stats
    except ImportError:
        extract_stats = None
    qualified_high_impact_items = []

    for cat in cat_keys:
        items = categories_output[cat]
        report_lines.append(f"## {cat}")
        report_lines.append("")
        print(f"📁 {cat}")
        print("-" * 50)
        
        if not items:
            report_lines.append("*Yeni içerik yok.*")
            report_lines.append("")
            print("  * Yeni içerik yok.\n")
            continue
            
        # Temalara/Bölümlere göre grupla (Aynı başlığın mükerrer açılmasını engeller)
        items_by_theme = {}
        for it in items:
            theme = it.get("theme", "")
            items_by_theme.setdefault(theme, []).append(it)
            
        for theme, theme_items in items_by_theme.items():
            if theme:
                report_lines.append(f"### {theme}")
                report_lines.append("")
                print(f"  📂 {theme}")
                
            # Kullanıcı tercihlerine ve akademik etki puanına göre en yüksekten düşüğe sırala
            theme_items.sort(key=lambda x: calculate_preference_score(x), reverse=True)
            
            # Her PubMed teması için en iyi 5-6 çalışma; diğer kategoriler için 3-4 çalışma seçilir (~50-60 toplam hedef)
            limit = 6 if theme else (3 if "Resmi" in cat else (4 if "Reddit" in cat else 4))
            rendered_count = 0
            
            for it in theme_items:
                if rendered_count >= limit:
                    break
                    
                it["category"] = cat
                ozet, gerekce, kullanim, mocs = generate_contextual_analysis(it)
                moc_str = " ".join(mocs) if mocs else "[[00_Klinik Beslenme ve Hastalıklarda Tıbbi Beslenme Tedavisi_MOC]]"
                ev = extract_living_evidence(it, ozet)
                
                # Yüksek etkili aday havuzuna ekle
                if "PubMed" in it.get("source", "") or ev["study_type"] in ["RCT", "Meta-Analysis", "Cohort"] or ev["evidence_direction"] in ["null", "contradictory"]:
                    qualified_high_impact_items.append((it, ozet, gerekce, kullanim, ev, moc_str))
                
                # Etiketler (Null veya Contradictory ise ekle)
                tags_list = []
                if ev["evidence_direction"] == "null":
                    tags_list.append("#finding/null")
                elif ev["is_contradictory"] or ev["evidence_direction"] == "contradictory":
                    tags_list.append("#finding/contradictory")
                tag_str = " " + " ".join(tags_list) if tags_list else ""
                
                # CSV Matrisine sayısal verileri aktar
                if extract_stats and "PubMed" in it.get("source", ""):
                    try:
                        num_params = extract_stats.extract_numeric_parameters(it["title"] + " " + it.get("raw_text", ""))
                        num_params["Evidence_Direction"] = ev["evidence_direction"]
                        num_params["P_Value"] = ev["p_value_summary"]
                        num_params["Study_Type"] = ev["study_type"]
                        if ev["sample_size"]:
                            num_params["Sample_Size_Intervention"] = str(ev["sample_size"])
                        extract_stats.append_to_matrix(num_params)
                    except Exception:
                        pass
                
                if cat == "Popüler Topluluk ve Sosyal Tartışmalar (Reddit Trendleri)":
                    entry = [
                        f"#### 💬 [{it['subreddit']}] {it['title']}{tag_str}",
                        f"- **Etkileşim & Kaynak:** ⬆️ {it['score']} Upvote · 💬 {it['comments']} Yorum · `{it['subreddit']}`",
                        f"- **🔬 Tartışma Özeti (Ne Konuşuluyor?):** {ozet}",
                        f"- **🎯 Neden Eklendi (Klinik & Akademik Değer):** {gerekce}",
                        f"- **⚡ Nasıl Kullanılabilir (İçerik & Ders):** {kullanim}",
                        f"- **🔗 İlgili MOC'lar:** {moc_str}",
                        f"- **Orijinal Bağlantı:** [Reddit Gönderisini Gör]({it['link']})",
                        ""
                    ]
                else:
                    entry_prefix = "#### 📌" if theme else "### 📌"
                    entry = [
                        f"{entry_prefix} {it['title']}{tag_str}",
                        f"- **Kaynak & Kanıt:** `{it['source']}` · `{ev['study_type']}` (`{ev['evidence_direction']}` | `{ev['p_value_summary']}`)",
                        f"- **🔬 Ne Bulundu (Türkçe Özet):** {ozet}",
                        f"- **🎯 Neden Eklendi (Gerekçe):** {gerekce}",
                        f"- **⚡ Nasıl Kullanılabilir (Ders / Substack / Proje):** {kullanim}",
                        f"- **🔗 İlgili MOC'lar:** {moc_str}",
                        f"- **Orijinal Bağlantı:** [Makaleyi / Kaynağı Aç]({it['link']})",
                        ""
                    ]
                    
                report_lines.extend(entry)
                rendered_count += 1
                print(f"📌 {it['title'][:70]}...")
                print(f"   Özet: {ozet[:90]}...")
                print(f"   Gerekçe: {gerekce[:90]}...\n")
            
    # ── FİKİR ÜRETİMİ VE KRİTİK DEĞERLENDİRME ANALİZİ ────────────
    vault_ideas = load_vault_idea_pool()
    
    if qualified_high_impact_items:
        report_lines.append("## 💡 Fikir Üretimi & Kritik Değerlendirme (Kasa & Fikir Logu Entegrasyonu)")
        report_lines.append("")
        report_lines.append("> [!IMPORTANT] 🎯 **Haftalık Öncelikli Okuma & Kasa Ekleme Önerisi**")
        
        # En nitelikli ilk 2 çalışmayı seç
        top_picks = qualified_high_impact_items[:2]
        for it, ozet, gerekce, kullanim, ev, moc_str in top_picks:
            report_lines.append(f"> - **Kesinlikle Oku & Vault'a Ekle:** [{it['title']}]({it['link']}) — *{it.get('source', it.get('subreddit', 'Kaynak'))}*")
            report_lines.append(f">   - **🎯 Gerekçe:** {gerekce}")
            report_lines.append(f">   - **⚡ Aksiyon:** {kullanim}")
        report_lines.append("")
        
        report_lines.append("### 🧠 Bülten Üzerinden Çıkan 4 Boyutlu Akademik Üretim & Fikir Matrisi")
        for idx, (it, ozet, gerekce, kullanim, ev, moc_str) in enumerate(qualified_high_impact_items[:3], 1):
            mocs = suggest_mocs(it["title"] + " " + it.get("raw_text", ""))
            moc_main = mocs[0] if mocs else "[[00_Klinik Beslenme ve Hastalıklarda Tıbbi Beslenme Tedavisi_MOC]]"
            
            # Kasadaki mevcut fikirlerle eşleşme
            title_words = set(re.findall(r"\w+", it["title"].lower()))
            matched_ideas = []
            for id_name in vault_ideas:
                id_words = set(re.findall(r"\w+", id_name.lower()))
                common = title_words.intersection(id_words)
                common_meaningful = [w for w in common if len(w) > 4 and w not in ["study", "effect", "clinical", "human", "trial", "diyet", "beslenme"]]
                if common_meaningful:
                    matched_ideas.append(f"[[{id_name}]]")
            
            report_lines.append(f"#### 💡 Odak {idx}: {it['title']} *({it.get('source', it.get('subreddit', 'Kaynak'))})*")
            report_lines.append(f"- **Çatı / MOC:** {moc_main}")
            report_lines.append(f"- **🔬 Bilimsel Bulgusu:** {ozet}")
            report_lines.append(f"- **🎯 Dahil Edilme Gerekçesi:** {gerekce}")
            if matched_ideas:
                report_lines.append(f"- **🔗 İlgili Çalışma Fikri:** {', '.join(matched_ideas[:2])} (Kasadaki mevcut hipotezi doğrudan besliyor).")
            
            # 4 Boyutlu Somut Üretim Aksiyonları
            report_lines.append(f"- **🎓 Lisans / Klinik Ders Köprüsü (BES339 / BES326 / BES420):** {kullanim}")
            report_lines.append(f"- **✍️ Substack & Sosyal Medya Açısı:** 'Popüler Algı vs. Moleküler Gerçeklik' perspektifinden danışan/halk sağlığı odaklı bülten başlığı.")
            report_lines.append(f"- **🎙️ Konsantre Podcast / Sesli Not Başlığı:** 5-7 dakikalık klinik odak tartışma: *\"{it['title'][:60]}... klinik pratikte hastaya/danışana nasıl yansır?\"*")
            report_lines.append(f"- **🔬 İleri Araştırma & Proje Tohumu:** Makaledeki metodolojik boşluğu (örneklem, süre, cinsiyet yanıtı) kapatacak yerel bir RCT veya anket hipotezi tasarla.")
            report_lines.append("")

    summary_line = f"Toplam {total_found} yeni içerik tespit edildi."
    report_lines.append("---")
    report_lines.append(f"**Özet:** {summary_line}")
    report_lines.append("")
    
    print("=" * 65)
    print(f"🏁 {summary_line}")
    print("=" * 65)
    
    # ── DOSYAYA KAYDETME ──────────────────────────────────────
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_file = os.path.join(OUTPUT_DIR, f"Digest_{date_str}.md")
    with open(out_file, "w", encoding="utf-8") as fp:
        fp.write("\n".join(report_lines))
    print(f"\n💾 Bülten kasaya kaydedildi: 00 Kontrol Merkezi/Digests/Digest_{date_str}.md")
    
    # Önbelleği güncelle (Son 1500 id tutulur)
    cache["seen_ids"] = new_seen_ids[-1500:]
    cache["last_run"] = start_time.isoformat()
    save_cache(cache)

if __name__ == "__main__":
    run_pipeline()


