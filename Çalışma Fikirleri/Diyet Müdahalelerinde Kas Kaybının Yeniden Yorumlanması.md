# Çalışma Notu: Diyet Müdahalelerinde "Kilo Kaybının Kalitesi" — Kas/Yağ Oranı Bazlı Karşılaştırmalı Sentez

Durum: Fikir aşaması → protokol geliştirme
Tasarım: Systematic Review without Meta-analysis (SWiM), homojen alt gruplarda keşifsel meta-analiz opsiyonu ile

---

## 1. Araştırma Sorusu ve Gerekçe

**Soru:** Farklı diyet müdahaleleri (standart kalori kısıtlaması, yüksek proteinli KR, ketojenik/çok düşük karbonhidrat, aralıklı oruç/TRE, Akdeniz diyeti), vücut ağırlığı kaybının "kompozisyon kalitesini" — yani kas kütlesinin yağ kütlesine oranını — nasıl farklı şekillerde etkiliyor?

**Gerekçe (literatürdeki konum):**
- **%ML (percentage of weight loss as FFM)** kavramı zaten var (Heymsfield ve ark. 2014, *Int J Obes*) — kilo kaybının ne kadarının FFM'den geldiğini tanımlıyor, kalori kısıtlama derecesiyle ilişkilendiriyor. Diyet *tipine* göre sistematik bir karşılaştırma yapılmamış.
- **MFR / BMFR (muscle-to-fat ratio)** kesitsel bir risk belirteci olarak kurumsallaşmış (sarkopenik obezite, insülin direnci, KBH, mortalite ile ilişkili; Current Obesity Reports 2025 derlemesi). Ama neredeyse hiç **müdahale-sonrası değişim** (pre-post outcome) olarak, diyet tiplerini karşılaştıran bir sentez düzeyinde kullanılmamış.
- **Boşluk:** Bu iki hattı birleştirip, 5 diyet kategorisini MFR-değişimi ve trend-sapma mantığıyla karşılaştıran sistematik bir sentez yok.

**Bilinen matematiksel tuzak (protokolde açıkça ele alınmalı):** FFM/FM oranı, kilo kaybı sırasında yağ kütlesi mutlak olarak kas kütlesinden daha fazla kaybedildiği için *neredeyse mekanik olarak* artar. Ham ΔMFR karşılaştırması yanıltıcıdır — bkz. Bölüm 3, Trend-Sapma Analizi.

---

## 2. Tanımlar

**MFR (Muscle-to-Fat Ratio):**
```
MFR = Kas Kütlesi (kg) / Yağ Kütlesi (kg)
```
Kas kütlesi ölçütü çalışmaya göre değişebilir: FFM (fat-free mass), LBM (lean body mass), ASM (appendicular skeletal muscle mass) veya SMM (skeletal muscle mass). Hangi ölçütün kullanıldığı veri çıkarma tablosunda ayrı bir sütun olarak kaydedilmeli (bkz. Bölüm 6) — bunlar birbirinin yerine geçmez ve alt grup/duyarlılık analizinde ayrıştırılmalı.

**ΔMFR:** MFR(bitiş) − MFR(başlangıç). Çalışma kolu düzeyinde hesaplanan tanımlayıcı bir istatistik; varyans tahmini gerektirmez.

**%ML (Percent Lean/FFM loss):**
```
%ML = (ΔFFM / ΔBW) × 100
```
Heymsfield ve ark. (2014) çerçevesiyle uyumlu, literatürle çapraz doğrulama için kullanılır.

**Trend-Sapma Analizi (bu çalışmanın asıl analitik katkısı):**
Her çalışma kolu, x ekseni = %BW kaybı, y ekseni = ΔMFR olacak şekilde bir dağılım grafiğine yerleştirilir. Tüm noktalardan geçen genel bir referans eğrisi (basit lineer regresyon, LOESS değil — SWiM aşamasında aşırı modelleme yapılmaz) çizilir. Bu eğri, "sadece kilo kaybı büyüklüğünden beklenecek mekanik MFR iyileşmesini" temsil eder. Bir diyet kategorisinin noktaları bu çizginin **belirgin şekilde üzerinde** kümeleniyorsa, o diyetin kilo kaybı büyüklüğünden bağımsız, gerçek bir kas-koruyucu etkisi olduğu öne sürülebilir. Çizginin altında kümelenme ise beklenenden fazla kas kaybını gösterir.

---

## 3. PICOS

| Bileşen | Kriter |
|---|---|
| Popülasyon | Yetişkin (≥18y), fazla kilolu/obez (BMI ≥25 kg/m²) |
| Müdahale | 5 kategori: (1) Standart kalori kısıtlaması, (2) Yüksek proteinli KR, (3) Ketojenik/çok düşük karbonhidrat, (4) Aralıklı oruç/TRE (ADF, 5:2, TRE), (5) Akdeniz diyeti |
| Karşılaştırma | Kategoriler arası + her kategori içinde kontrol/standart diyetle karşılaştırma (varsa) |
| Sonuç | Başlangıç ve bitişte hem FM hem FFM/LBM/ASM (mean±SD), ≥4 hafta müdahale |
| Tasarım | RCT (paralel veya çapraz, ≥2 kol) |
| Dışlama | Hayvan çalışmaları, bariatrik cerrahi, <18 yaş, sadece BMI/çevresel ölçüm raporlayan (FM+FFM yok) çalışmalar |

---

## 4. Arama Terimleri

Veritabanları: PubMed/MEDLINE, Embase, Cochrane CENTRAL, Web of Science (mevcut IF ve keto meta-analizlerinin kullandığı standart üçlü/dörtlü kombinasyon).

**PubMed taslak string:**
```
(diet* OR "caloric restriction" OR "energy restriction" OR "intermittent fasting" 
OR "time-restricted eating" OR "time-restricted feeding" OR ketogenic OR "low carbohydrate" 
OR "Mediterranean diet" OR "high protein diet")
AND
("body composition" OR "body fat percentage" OR "fat-free mass" OR "fat free mass" OR "lean body mass" 
OR "lean mass" OR "skeletal muscle mass" OR "muscle mass" OR "fat mass")
AND
(randomized controlled trial OR randomised controlled trial OR RCT OR "random allocation")
AND
(obes* OR overweight OR "body mass index" OR "waist circumference" OR "visceral" fat OR "abdominal obesity")
```

**Embase/Web of Science için:** aynı kavram blokları, veritabanına özgü thesaurus terimleriyle uyarlanır (Emtree: 'diet therapy', 'body composition'; WoS: konu başlığı bazlı).

**Filtre önerisi:** İngilizce + son 25 yıl (1999–2026) — MFR/BMFR kavramı esas olarak 2010'lardan sonra literatüre girdiği için, çok eski çalışmalarda FFM ölçüm yöntemleri (BIA teknolojisi vb.) günümüzle kıyaslanabilir olmayabilir; bu bir dışlama kriteri değil, alt grup/duyarlılık analizi konusu olarak not edilmeli.

**Ek kaynak taraması:** Mevcut meta-analizlerin (Leung ve ark. 2025 *Clin Nutr* [keto/düşük karbonhidrat]; 2025 *Nutrition Journal* IF meta-analizi; Heymsfield 2014 %ML derlemesi) referans listeleri elle taranmalı — bu, arama stringinin kaçırabileceği çalışmaları yakalamak için standart pratik.

---

## 5. Veri Çıkarma Planı

Her çalışma kolu için:
- Yazar, yıl, ülke, örneklem büyüklüğü, süre
- Diyet kategorisi (5'ten biri) + tam makro dağılımı
- Ölçüm yöntemi (DXA / BIA / ADP / diğer) — **zorunlu alt grup değişkeni**
- Kas kütlesi ölçütü tipi (FFM / LBM / ASM / SMM) — zorunlu alt grup değişkeni
- Başlangıç: BW, FM, kas kütlesi (mean±SD)
- Bitiş: BW, FM, kas kütlesi (mean±SD)
- Hesaplanan: ΔMFR, %ML, %BW kaybı
- RoB 2 değerlendirmesi (Cochrane risk of bias aracı, RCT'ler için)

---

## 6. Sentez Planı (3 Katman)

1. **Birincil — Trend-Sapma Scatterplotu:** Bölüm 3'te tanımlanan analiz. Diyet kategorisine göre renklendirilmiş noktalar + genel referans eğrisi + kategori bazlı yerel trendler.
2. **Çapraz doğrulama — %ML karşılaştırması:** Yeni bulgunun mevcut %ML literatürüyle tutarlılığını gösterir.
3. **Klinik anlamlılık — Eşik geçişi:** Baseline/endpoint MFR değerleri, literatürdeki sarkopenik-obezite risk eşikleriyle (cinsiyete özgü alt kentil kesim noktaları, örn. Chen ve ark. Taipei Longitudinal Aging Study) karşılaştırılır; kategorik risk grubu geçişi (yüksek risk → düşük risk) raporlanır.

**Keşifsel meta-analiz (opsiyonel, ikinci aşama):** Eğer bir kategoride (muhtemelen IF/TRE, çünkü zaten ~15 RCT'lik homojen bir havuz mevcut) yeterli sayıda çalışma aynı ölçüm yöntemiyle raporluyorsa, o alt grupta korelasyon-imputasyonlu (Cochrane Handbook türetilmiş sonuç formülü, r=0.5 varsayımıyla duyarlılık analizi) formal bir pooled ΔMFR meta-analizi denenebilir.

---

## 7. Değerlendirme Kriterleri / Sınırlamalar (protokolde açıkça belirtilmeli)

- Ölçüm yöntemi heterojenliği (DXA vs BIA) ana sınırlama — alt grup analizi zorunlu.
- MFR'nin mekanik artış eğilimi → trend-sapma analizi olmadan ham ΔMFR yanıltıcı (Bölüm 1-3).
- Kas kütlesi tanımının çalışmalar arası tutarsızlığı (FFM ≠ SMM ≠ ASM) → doğrudan havuzlama yapılmamalı, kategori olarak işaretlenmeli.
- Yayın yanlılığı: diyet karşılaştırma RCT'lerinde tipik.

---

## 8. Sonraki Adımlar

1. PROSPERO'da benzer kayıtlı bir protokol olup olmadığını kontrol et (henüz yapılmadı — önerilir).
2. PICOS ve arama stringini gözden geçir, ikinci bir tarayıcı belirle (RCT sistematik derlemelerinde standart pratik).
3. Pilot arama yap, her kategori için beklenen çalışma sayısını doğrula.
4. Veri çıkarma tablosunu (Excel/Google Sheets) Bölüm 5'teki alanlarla oluştur.

## Bağlantılı Notlar
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
- [[IF-crossover-carryover-protokol]]
- [[Vücut Ağırlığının Matematiği]]
- [[GLP-1 ve Diyetisyenlik]]
- [[enerji gereksiniminin belirlenmesindeki missing part]]
