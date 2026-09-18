---
tags: [sistem, ai, claude, antigravity]
---

# 🚀 AI Başlangıç ve Kasa Master Referans Rehberi — Dr. Caner Özyıldırım

Bu dosyayı her yeni AI / Claude / Antigravity oturumunun başında oku. Kasanın mimarisi, kimlik, aktif projeler ve kurallar bu dosyada tanımlıdır.

---

## 👤 Kimlik ve Bağlam

**Dr. Caner Özyıldırım** — Arş. Gör. Dr., Akdeniz Üniversitesi Beslenme ve Diyetetik Bölümü.
Endokrinoloji kliniğinde araştırma asistanı. Türkçe çalışır, gen/protein kısaltmalarını İngilizce kullanır.

**Temel Araştırma Odakları:** Adipoz doku biyolojisi, aralıklı açlık, kişiselleştirilmiş beslenme, obezite ve metabolik hastalıklar.

**Aktif Projeler:**
- Tamamlanmış 3 kollu RCT (n=102): 6-öğün vs 3-öğün vs TRF, T2DM, 12 hafta — makale yazım aşamasında
- Narratif derleme: "Kişiselleştirilmiş Açlık" — yazım devam ediyor
- INFLAMomx COST Action CA24166 — WG1 üyesi (Dr. Ines Mollet ile temas kuruldu)
- Napoli Federico II ziyaretçi araştırmacı görüşmesi (Dr. Giovanna Muscogiuri)

---

## 📁 Kasa Mimari Yapısı (2026-09-05 Güncel)

```
caner/
├── 00 Kontrol Merkezi/          ← YALNIZCA KULLANICI PANO VE GÜNLÜKLERİ
│   ├── 00_Ana_Kokpit.md         ← Master kontrol paneli (DataviewJS)
│   ├── Dashboard_Gaps_and_Contradictions.md ← Null bulgular ve çelişki panosu
│   ├── Kitaplar.md              ← Notion aktarımlı kitap galerisi ve tablosu
│   ├── İş Takibi.md             ← Aktif görev ve proje listesi
│   ├── Fikir Üretim Logu.md     ← Otonom ve manuel fikir kuluçka günlüğü
│   ├── Katman Analizi Geçmişi.md← Not katman analizleri
│   ├── 01_Graph_View_ve_Gorsellestirme_Rehberi.md ← Graph yapılandırma kılavuzu
│   ├── Bookmarks/               ← Web yer imleri
│   ├── Clippings/               ← Ham web okuma kayıtları
│   ├── Digests/                 ← Nutrition Scout (4 günlük periyot) bülten ve logları
│   └── scripts/                 ← Dataview UI JS bileşenleri (moc_panorama, molecular_radar, notion_book_gallery)
│
├── AI Kontrol Merkezi/          ← YAPAY ZEKA, KURALLAR, OTOMASYON VE PIPELINE MERKEZİ
│   ├── Talimatlar & Kurallar/   ← AI başlangıç, kurallar, süper komutlar ve bakım protokolleri
│   │   ├── _AI_BAŞLANGIÇ.md     ← Bu dosya (Master prompt ve kasa referansı)
│   │   ├── Claude Komut Protokolü.md
│   │   ├── 02_Akademik_Super_Komutlar_ve_Uretim_Playbook.md
│   │   ├── Vault_Bakim_ve_Entegrasyon_Protokolu.md
│   │   ├── Promptlarım.md
│   │   ├── X Aramaları ve Promptlar.md
│   │   └── Vault_Yeniden_Yapilandirma_2026-09-05.md
│   ├── Claude Skills/           ← Claude & AI uzmanlık beceri modülleri (00 - 04)
│   ├── Otomasyon & Scriptler/   ← Python, R, Swift, Shell otomasyon betikleri ve durum dosyaları
│   │   ├── nutrition_scout.py, sync_vault.py, semantic_linker.py
│   │   ├── semantic_connection_engine.py, metadata_processor.py, extract_stats.py
│   │   ├── list_versions.py, list_versions.swift, run_nutrition_scout.sh
│   │   ├── build_dictionary.py, data_inspector.py, r_executor.py, zotero_helper.py
│   │   ├── citation_resolver.py, apply_dictionary.R
│   │   └── .scout_cache.json, .sync_state.json
│   ├── MOC/                     ← AI sentez ve çatı kavram haritaları
│   ├── Veri Pipeline/           ← Ham ve işlenmiş veri giriş hatları (Zotero, NotebookLM, Clippings)
│   ├── Raporlar & Analizler/    ← AI tarafından üretilen kasa analiz ve ders rehberi raporları
│   └── copilot/                 ← Obsidian Copilot eklentisi yapılandırmaları
│
├── Akademik/                    ← COST Actions, Postdoc, Yeni Akreditasyon Yapılanması
├── Çalışma Fikirleri/           ← Araştırma hipotezleri ve çalışma tasarımları (~290+ dosya)
├── Dersler/                     ← Modüler ders sistemi: [Ders Adı]/ (Ders Notları, Sunumlar, Araçlar, Kaynaklar)
│   └── Derslerim.md             ← Dersler ana indeksi
├── Dizin/                       ← Ontolojik çatı dizinler ve MOC'lar (00_..._MOC.md)
├── Excalidraw/                  ← Çizim ve görselleştirme şemaları
├── Files/                       ← Görseller, ekler, PDF'ler ve veri tabloları
├── Kitaplar/                    ← Kitap ve film incelemeleri + _Notion Arsivinden - Kontrol Bekliyor/
├── Manuscripts/                 ← Makale ve araştırma yazım projeleri
├── Notlar/                      ← 4 Katmanlı Zettelkasten not arşivi (~150+ not)
├── Sosyal Medya/                ← Substack yazıları, yayın planları ve bülten taslakları
└── Templates/                   ← Not şablonları ve örnek analiz projeleri
```

---

## 🧬 4 Katmanlı Not Sistemi

```yaml
TÜR: Çekirdek | Besleyici
ODAK: [[Ana ilgi alanı]]
MEKANİZMA: [[Bağlayıcı mekanizma]]
DİZİN: [[Terim]]
ETİKET: makaleden | internetten | dersten
BESLEDİĞİ NOTLAR: [[Doğrudan üstüne inşa ettiği / derinleştirdiği çekirdek veya ana not]]
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
```

**Odak Alanları:** Adipoz Doku · Aralıklı Açlık · Ketojenik Diyet · Popüler Diyetler · Mikrobiyota · UPF · Obezite · Fonksiyonel Besinler · GLP-1 · Yapay Zeka · İstatistik ve Metodoloji · Beslenme ve Sosyal Faktörler · Longevity

**Mekanizmalar:** Kilo Kaybı · Kilo Kazanımı · Kilo Döngüsü · Proinflamatuvar · Antiinflamatuvar · Disbiyozis · Nutrient Sensing · Metabolic Flexibility · Biyokimya/Metabolizma · İnsülin Duyarlılığı

---

## 📚 Dersler Yapısı

| Kod | Ders | Klasör Yolu |
|-----|------|-------------|
| BES339 | Diyet İlkeleri ve Popüler Diyetler | `Dersler/Diyet İlkeleri ve Popüler Diyetler/` |
| BES326 | İmmün Sistem ve İmmünonutrisyon | `Dersler/İmmün Sistem ve İmmünonutrisyon/` |
| BES420 | Enteral ve Parenteral Beslenme | `Dersler/Enteral Parenteral Beslenme/` |
| — | Yetişkinlerde Beslenme Tedavisi Uygulaması | `Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/` |
| — | Beslenmenin Psikososyal Yönleri | `Dersler/Beslenmenin Psikososyal Yönleri/` |
| — | Beslenme ve Medya | `Dersler/Beslenme ve Medya/` |
| — | Biyoistatistik | `Dersler/Biyoistatistik/` |
| — | Kanıta Dayalı Bilgelik | `Dersler/Kanıta Dayalı Bilgelik/` |
| — | Bilgisayar Uygulamaları ve Yapay Zeka | `Dersler/Bilgisayar Uygulamaları ve Yapay Zeka/` |
| — | 1. Sınıf Danışmanlıkları / Çocuk Hastalıkları | `Dersler/.../` |

---

## 📊 Dashboard ve Otomasyon Motorları

1. **Akademik Ana Kokpit (`00 Kontrol Merkezi/00_Ana_Kokpit.md`)**:
   - Master kontrol paneli: Görev ilerlemeleri, MOC yoğunluk sıralaması, hub notlar, odak/mekanizma dağılımı, yetim not radarı ve otonom kuluçka sayacı.
2. **Canlı Literatür & Digest Takip Motoru (`nutrition_scout.py`)**:
   - **Konum:** `AI Kontrol Merkezi/Otomasyon & Scriptler/nutrition_scout.py`
   - **Runner:** `AI Kontrol Merkezi/Otomasyon & Scriptler/run_nutrition_scout.sh`
   - **Pencere:** Son 4 gün (`LOOKBACK_DAYS = 4`).
   - **Kapsam:** FDA/EFSA/WHO resmi uyarıları, ASN/ESPEN/EASO rehberleri, 10 tematik PubMed matrisi, multi-omiks, Reddit trendleri ve COST/Erasmus çağrıları.
   - **Çıktı & Log:** `00 Kontrol Merkezi/Digests/Digest_YYYY-MM-DD.md` ve `scout_runner.log`.
3. **Otonom Senkronizasyon & Kuluçka Motoru (`sync_vault.py`)**:
   - **Konum:** `AI Kontrol Merkezi/Otomasyon & Scriptler/sync_vault.py`
   - **İşlev:** Her 10 yeni notta MOC köprülerini ve yeni araştırma/Substack hipotezlerini otonom kuluçkalar.

---

## ⌨️ Temel Komut Referansı

| Komut | Ne Yapar |
|-------|----------|
| `"Vault'u analiz et"` | Notlar klasörü tarama, Geçmiş + Fikir Logu güncelle |
| `"[dosya] clipping'ini işle"` | Clippings → AI Kontrol Merkezi şablonuyla işle |
| `"Zotero notlarını işle"` | Zotero Ham → Türkçe + katmanlı not |
| `"NotebookLM notunu işle"` | NotebookLM Ham → işlenmiş not |
| `"[konu] için MOC oluştur"` | AI Kontrol Merkezi/MOC'a tematik harita |
| `"AI Kontrol Merkezini analiz et"` | Dashboard güncelle, karar öner |
| `"Bağlantıları güncelle"` | Yeni notların YAML bağlantılarını tamamla |

---

## 🔧 AI Davranış ve Çalışma Kuralları

- **Kontrol Merkezi Ayrımı:** `00 Kontrol Merkezi` sadece Caner Hoca'nın panolarına ve günlüklerine aittir. AI talimatları, kuralları, scriptleri ve pipeline'ları daima `AI Kontrol Merkezi` altında yer alır.
- **Kök Dizin Disiplini:** Kök dizine yeni script, geçici test veya başıboş dosya bırakma. AI ile ilgili her şey `AI Kontrol Merkezi` altındaki uygun klasöre yazılmalıdır.
- **Wikilink Bütünlüğü:** Notlar ve kavramlar bağlanırken `[[Dosya Adı]]` formatı kullanılır.
