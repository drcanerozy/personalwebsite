---
Tür:
  - meta-analiz / derleme
Durum: aktif
Öncelik: Yüksek
Son_Güncelleme:
Konu:
  - Yapay Zeka
Modifiye_Edilme_Tarihi:
TÜR:
ODAK:
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
---
# GLP-1 vs Beslenme Araştırmaları — Metodoloji Protokolü

> [!info] Belge Bilgisi **Versiyon:** v1.0 Taslak  
> **Tarih:** Mart 2026  
> **Durum:** 🟡 Aktif Geliştirme  
> **Hedef Format:** Commentary / Original Research



## 1. Hipotez ve Amaç

> [!abstract] Ana Hipotez Akademik ilginin, fonların ve yayın trendlerinin farmakolojik çözümlere kaymasıyla birlikte, diyet araştırmalarının hem **sayısal (nicel)** olarak azaldığı hem de **metodolojik (nitel)** olarak _"ilaca yardımcı bir unsur"_ seviyesine gerilediği hipotez edilmektedir.

### Çalışmanın Amacı

GLP-1 reseptör agonistlerinin (Semaglutide, Tirzepatide vb.) obezite tedavisindeki küresel popülaritesinin, bağımsız beslenme ve diyet müdahalesi araştırmaları üzerindeki etkisini **nicel ve nitel** olarak analiz etmek.

### Hedef Çıktı

Temel çağrı: Farmakolojik başarılar, beslenme bilimindeki inovasyonu gölgelememeli; aksine **Precision Medical Nutrition Therapy (PMNT)** kavramına daha çok yatırım yapılmalıdır.

---

## 2. Veri Kaynakları Matrisi

### A — Yayın Verileri (Retrospektif)

|Kaynak|Analiz Katmanı|Erişim Yöntemi|Sınırlılık|
|---|---|---|---|
|**PubMed / NLM**|Nicel trend, Evidence-base inflation|Web arayüzü + NCBI E-utilities API|Sadece İngilizce dominant. Grey literature yok.|
|**Scopus**|Normalized share, Dergi kalite filtresi|Kurumsal erişim + "Analyze Results"|Ücretli erişim gerektirir.|
|**Web of Science**|Atıf ağı analizi (ek)|Kurumsal erişim|Scopus ile örtüşür; triangulation için kullan.|
|**Dimensions.ai**|Fon + yayın ilişkisi (**yalnızca triangulation**)|Ücretsiz web + API|Grant kategorileri harmonize değil. Primer kaynak DEĞİL.|

> [!warning] Dimensions.ai Uyarısı Aynı proje birden fazla etiketle indekslenir, para birimleri harmonize edilmemiştir. NIH RePORTER + CORDIS ikilisini **primer**, Dimensions'ı **triangulation** kaynağı olarak kullan.

---

### B — Devam Eden RCT'ler (Prospektif)

|Kaynak|Kapsam|Erişim Yöntemi|Sınırlılık|
|---|---|---|---|
|**ClinicalTrials.gov**|Dünyanın en büyük klinik deneme veritabanı|Advanced Search + CSV export|Sadece kayıtlı çalışmalar. Eksik veri girişleri mevcut.|
|**WHO ICTRP**|Global (Çin, AB, Türkiye dahil)|Web arayüzü + XML export|Veri kalitesi ülkeye göre değişir.|
|**EU Clinical Trials Register (EUCTR)**|AB çalışmaları triangulation|EudraCT + EUCTR arama motoru|CORDIS ile çapraz doğrulama gerektirir.|

> [!tip] Prospektif Analizin Önemi Eğer kayıtlı diyet çalışması sayısı, kayıtlı ilaç çalışmalarının belirgin altında kalırsa → Bu, **"akademik terk hipotezinin en taze kanıtı"** olur. Çünkü kayıt aşamasındaki düşüş, yayın gecikmesiyle açıklanamaz.

---

### C — Fon ve Hibe Verileri

|Kaynak|Kapsam|Erişim Yöntemi|Sınırlılık|
|---|---|---|---|
|**NIH RePORTER**|ABD federal fonları|Export Tool → Excel; R ile analiz|Çift sayım riski: Bir proje hem "Obesity" hem "Nutrition" etiketli olabilir.|
|**CORDIS (EU)**|Horizon projeleri|Download Results → CSV/Excel|Para birimi harmonizasyonu gerekir (EUR→USD).|

> [!warning] NIH Çift Sayım Riski Primary MeSH / Project Terms hiyerarşisinde **dominant etikete** göre "principal focus" filtresi uygula. Bu metodoloji bölümünde şeffafça açıklanmalı.

---

## 3. Metodoloji — Üç Katman

### Katman A — Nicel Trend Analizi

#### A1. PubMed Sorgu Şablonları

İki dönem için ayrı ayrı çalıştır: **2015–2020 (Pre-Hype)** ve **2021–2026 (GLP-1 Era)**

```
# Obezite — Diyet (Ana İnceleme Grubu)
(Obesity[MeSH Terms] OR "Weight Loss"[MeSH Terms]) 
AND ("Dietary Intervention"[Title/Abstract] OR "Caloric Restriction"[Title/Abstract]) 
AND (Clinical Trial[Filter] OR Randomized Controlled Trial[Filter])
```

```
# Obezite — GLP-1 (Ana Karşılaştırma Grubu)
(Obesity[MeSH Terms] OR "Weight Loss"[MeSH Terms]) 
AND ("GLP-1 Receptor Agonists"[MeSH Terms] OR Semaglutide OR Tirzepatide) 
AND (Clinical Trial[Filter] OR Randomized Controlled Trial[Filter])
```

```
# T2DM — Diyet (Baseline / Kontrol Grubu 1)
("Diabetes Mellitus, Type 2"[MeSH Terms]) 
AND ("Dietary Intervention"[Title/Abstract]) 
AND (Clinical Trial[Filter] OR Randomized Controlled Trial[Filter])
```

```
# CAD — Diyet (Baseline / Kontrol Grubu 2)
("Coronary Artery Disease"[MeSH Terms]) 
AND ("Dietary Intervention"[Title/Abstract]) 
AND (Clinical Trial[Filter] OR Randomized Controlled Trial[Filter])
```

---

#### A2. Senaryo Analizi — Displacement Hipotezi

|Senaryo|Gözlemlenen Örüntü|Yorum|Hipoteze Destek|
|---|---|---|---|
|**A — Spesifik Displacement**|Obezite diyet RCT azalır; T2DM & CAD stabil kalır|"Obezite için ilaç varken diyet çalışmaya gerek yok" algısı. Displasma obeziteye özgü.|🟢 Güçlü|
|**B — Genel Farmakolojik Baskı**|Üç alanda da diyet çalışmaları düşer|Beslenme bilimi genel olarak farmakolojiye teslim olmaktadır. Sistemik dönüşüm.|🟡 Orta|
|**C — Asimetrik Düşüş**|T2DM/CAD da düşer ama obezitedeki düşüş belirgin daha derin|Hype yoğunluğu ile displacement derinliği orantılı.|🔵 Çok Güçlü (nüanslı)|

> [!note] Görselleştirme Notu Overlay analizde **mutlak sayı değil, normalized share** kullan. T2DM'nin daha büyük literatür tabanı obezite karşılaştırmasını gölgeler.

---

#### A3. Metrikler

- **Relative Growth Index (RGI):** Her grubun 2021–2026 yıllık yayın sayısı ÷ 2015–2020 ortalaması
- **Share of Voice (SoV):** Diyet çalışmalarının toplam obezite literatüründeki yıllık yüzdesi
- **Normalized Share:** Her alanın kendi toplam literatürüne oranı

---

### Katman B — Nitel Değerlendirme (Methodological Erosion)

#### B1. İki Katmanlı Örneklem Protokolü

|Katman|Seçim Kriteri|Amaç|
|---|---|---|
|**Katman 1 — Diyet Tarafı**|Nutrition & Dietetics'te SJR Top 10 (Scimago). 2021–2026 GLP-1 bileşenli makaleler.|"Beslenme bilimi kendi alanına mı hapsoldu?" sorusunu yanıtlar.|
|**Katman 2 — GLP-1 Tarafı**|General Medicine / Endocrinology'de SJR Top 10 (NEJM, Lancet, Nature Medicine). GLP-1 obezite RCT'leri.|Bu çalışmalardaki LSM protokolünün derinliğini ölçer.|

---

#### B2. LSM Protokol Derinlik Rubriği (0–3)

|Puan|Kategori|Tanım|Örnek İfade|
|---|---|---|---|
|**0**|Yüzeysel Geçiş|Diyet 1 satırda geçip "standart tavsiye verildi" denilmiş.|_"Participants received standard dietary counseling."_|
|**1**|Kısmi Tanımlama|Kalori hedefi verilmiş, kişiselleştirme yok.|_"A 500 kcal/day deficit diet was prescribed."_|
|**2**|Yapılandırılmış Protokol|Makrobesin dağılımı, diyet paterni ve diyet uzmanı desteği tanımlanmış.|_"Mediterranean diet with 30% fat, monthly dietitian sessions."_|
|**3**|Kişiselleştirilmiş / Precision|Bireysel enerji gereksinimi, mikrobiom/genetik uyum veya teknoloji destekli izleme.|_"Personalized nutrition based on CGM response and gut microbiome profiling."_|

> [!important] Inter-Rater Güvenilirlik İki bağımsız gözlemci tarafından puanlama yapılmalı. **Cohen's kappa** ile inter-rater güvenilirlik hesaplanmalı.

---

#### B3. Evidence-Base Inflation — Lag Analizi

Temel RCT yayın yılı ile o RCT'yi kapsayan **ilk sistematik derlemenin yayın yılı** arasındaki fark ölçülecek.

- GLP-1 tarafında lag **< 12 ay** → _"Sonuçlar olgunlaşmadan başarı hikayesi yazılıyor"_ tezi desteklenir
- Diyet tarafında lag **uzun** → Alan "yavaş ve göz ardı edilen birikim" modeline dönmüştür
- Bu asimetri **tek başına bir Şekil** olarak sunulabilir

---

### Katman C — Vizyonel Analiz (Precision Nutrition Gap)

#### C1. NIH Fonlama Analizi

1. NIH RePORTER'dan "Obesity" anahtar kelimesiyle tüm projeleri Excel olarak indir
2. "Nutrition" vs. "GLP-1/Pharmacotherapy" etiketlerine göre filtrele
3. R ile yıllık bütçe payı (%) hesapla
4. Çift sayım için **primary focus filtresi** uygula

#### C2. Prospektif Kayıt Analizi

**ClinicalTrials.gov Advanced Search parametreleri:**

- Status: All Studies
- Study Start Date: 2022–2025
- Intervention: "Dietary" **vs.** "GLP-1 OR Semaglutide OR Tirzepatide"

Aynı sorguyu **WHO ICTRP** ve **EUCTR**'de de çalıştır → Global triangulation.

---

## 4. Adım Adım Uygulama Planı

### Faz 1 — Veri Toplama (Hafta 1–3)

- [ ] **Adım 1** — PubMed: 4 MeSH sorgusunu iki dönem için çalıştır. NCBI E-utilities API ile yıllık sayım çek.
    - Çıktı: `Excel — yıllık sayım tablosu (4 grup × 12 yıl)`
    - Süre: 3–4 gün
- [ ] **Adım 2** — PubMed: Aynı sorguları `Study Type = Systematic Review / Meta-Analysis` filtresiyle tekrarla.
    - Çıktı: `Excel — piramit analiz tablosu (RCT vs SR/MA)`
    - Süre: 2 gün
- [ ] **Adım 3** — ClinicalTrials.gov: Advanced Search ile prospektif kayıt analizi. CSV export.
    - Çıktı: `CSV — prospektif kayıt karşılaştırma tablosu`
    - Süre: 1–2 gün
- [ ] **Adım 4** — WHO ICTRP: Aynı kriterleri tekrarla. Global ülke dağılımı tablosu oluştur.
    - Çıktı: `CSV — global kayıt tablosu`
    - Süre: 1 gün
- [ ] **Adım 5** — NIH RePORTER: "Obesity" projelerini Excel olarak indir. Yıllık bütçe payı hesapla.
    - Çıktı: `Excel — NIH bütçe dağılım tablosu`
    - Süre: 2–3 gün
- [ ] **Adım 6** — CORDIS: Horizon projelerini CSV olarak çek. EUR→USD dönüşümü uygula.
    - Çıktı: `CSV — CORDIS bütçe tablosu`
    - Süre: 1–2 gün

---

### Faz 2 — Nitel Analiz (Hafta 4–5)

- [ ] **Adım 7** — Scimago (SJR): Nutrition & Dietetics ve General Medicine kategorilerinde Top 10 dergileri belirle.
    - Çıktı: `Dergi listesi (Katman 1 + Katman 2)`
    - Süre: 1 gün
- [ ] **Adım 8** — PubMed / Scopus: Her iki katmandaki dergilerden 2021–2026 GLP-1 çalışmalarını çek. Full-text erişim sağla.
    - Çıktı: `20–40 çalışma full-text listesi`
    - Süre: 3–4 gün
- [ ] **Adım 9** — Full-text analiz: Her çalışmadaki LSM protokolünü rubrik ile puanla (0–3). Beslenme biliminin rolünü kaydet.
    - Çıktı: `LSM puanlama tablosu + Cohen's kappa`
    - Süre: 5–7 gün
- [ ] **Adım 10** — Lag analizi: İlk 20–30 temel RCT için RCT yayın yılı vs. ilk SR/MA yayın yılı farkını ölçtür.
    - Çıktı: `Lag analizi tablosu + Şekil taslağı`
    - Süre: 2–3 gün

---

### Faz 3 — Analiz ve Görselleştirme (Hafta 6–7)

- [ ] **Adım 11** — R / Python: Normalized Share ve RGI hesaplamaları. Overlay trend grafiği. Senaryo A/B/C tespiti.
    - Çıktı: `Şekil 1 (trend) + Şekil 2 (piramit) + Şekil 3 (lag)`
    - Süre: 5–7 gün
- [ ] **Adım 12** — Excel / R: NIH + CORDIS bütçe verilerini birleştir. Precision Nutrition funding gap görselleştir.
    - Çıktı: `Şekil 4 (bütçe dağılımı)`
    - Süre: 2–3 gün
- [ ] **Adım 13** — LSM Rubrik ortalamalarını hesapla. Yüksek impaktlı GLP-1 çalışmalarında "Puan 0–1" oranını raporla.
    - Çıktı: `Şekil 5 (LSM rubrik dağılımı)`
    - Süre: 2 gün

---

### Faz 4 — Yazım ve Gözden Geçirme (Hafta 8–10)

- [ ] **Adım 14** — Taslak yazımı: Introduction → Methods → Results → Discussion → PMNT Çağrısı.
    - Çıktı: `İlk tam taslak (3.000–5.000 kelime)`
    - Süre: 7–10 gün
- [ ] **Adım 15** — Kör peer review simülasyonu: "Korelasyon ≠ nedensellik" eleştirisine karşı Methods bölümünü güçlendir.
    - Çıktı: `Revize edilmiş taslak`
    - Süre: 3–4 gün
- [ ] **Adım 16** — Hedef dergi seçimi ve submission hazırlığı. Cover letter + COI beyanı.
    - Çıktı: `Gönderime hazır makale paketi`
    - Süre: 2 gün

---

## 5. Metodolojik Riskler

|Risk|Mitigasyon|Öncelik|
|---|---|---|
|**Korelasyon ≠ nedensellik**|T2DM + CAD baseline ile "spesifik displacement" ayrıştırılır. "Güçlü ilişki" iddiası yapılır, nedensellik değil.|🔴 Kritik|
|**Çift sayım (NIH)**|Primary MeSH'te dominant etiket belirlenir. "Principal focus" filtresi Methods'ta şeffafça açıklanır.|🟠 Yüksek|
|**Dergi örneklem seçimi**|SJR Top 10, iki kategoride (Nutrition / General Medicine) ayrı ayrı tanımlanır.|🟠 Yüksek|
|**Yayın gecikmesi itirazı**|ClinicalTrials.gov prospektif analizi: Kayıt aşamasındaki düşüş, lag ile açıklanamaz.|🟡 Orta|
|**ABD merkezlilik**|WHO ICTRP + CORDIS + EUCTR ile multi-regional triangulation yapılır.|🟡 Orta|
|**LSM puanlama subjektivitesi**|İki bağımsız gözlemci + Cohen's kappa.|🟡 Orta|

---

## 6. Beklenen Çıktılar ve Hedef Dergiler

### Şekiller ve Tablolar

|#|İçerik|Kaynak|Kritik Bulgu|
|---|---|---|---|
|**Şekil 1**|Overlay trend grafiği: Obezite, T2DM, CAD diyet RCT vs GLP-1 (2015–2026)|PubMed yıllık sayım|Senaryo A/B/C tespiti|
|**Şekil 2**|Evidence-Base Inflation: SR/MA vs RCT oranı yıllara göre|PubMed study type|Kanıt enflasyonu|
|**Şekil 3**|Lag analizi: RCT→SR/MA gecikme süresi (GLP-1 vs Diyet)|PubMed tarih karşılaştırması|Asimetrik birikim|
|**Şekil 4**|Bütçe dağılımı: Nutrition vs Pharmacotherapy (NIH + CORDIS)|NIH RePORTER + CORDIS|Ekonomik güç kayması|
|**Şekil 5**|LSM Rubrik dağılımı: Puan 0–3 yüzdeleri (Katman 1 vs 2)|Full-text nitel analiz|Methodological Erosion|
|**Tablo 1**|Veri kaynakları matrisi|—|Metodoloji şeffaflığı|
|**Tablo 2**|Senaryo A/B/C karşılaştırma tablosu|—|Hipotez çerçevesi|

---

### Hedef Dergiler

|Öncelik|Dergi|Format|Gerekçe|
|---|---|---|---|
|🥇 1|Lancet / Nature Medicine|Commentary veya Perspective|En geniş etki. Metodoloji tam olgunlaştığında hedeflenir.|
|🥈 2|Obesity Reviews|Systematic Review veya Original Research|Obezite alanının premier dergisi. Tam metodolojik makale için ideal.|
|🥉 3|IJBNPA|Original Research|Beslenme ve davranış odaklı. Katman B için uygun.|
|4|JAMA Internal Medicine|Research Letter / Viewpoint|Kısa formatta hızlı etki. Pilot bulgular yeterli.|

---

> [!quote] Temel Çağrı _"Farmakolojik başarılar, beslenme bilimindeki inovasyonu gölgelememeli; aksine ilacın etkinliğini artıracak ve sürdürülebilirliği sağlayacak **Precision Medical Nutrition Therapy (PMNT)** kavramına daha çok yatırım yapılmalıdır."_

---

_v1.0 — Mart 2026 — Taslak_

## Bağlantılı Notlar
- [[GLP-1 Nutrient Density ve Vücut Kompozisyonu]]
