# Mikrobiyota Farkındalığı — LPA Çalışma Tasarımı ve Süreç Notu

*Son güncelleme: 2026-08-08*

---

## 1. Araştırma Sorusu ve Genel Tasarım

**Örneklem:** n=1417 (veri temizliği sonrası n=1286, bkz. Bölüm 3.4)

**Değişkenler:** Medeni durum, meslek, sosyoekonomik durum, kronik hastalık, BMI, sigara, alkol, ana/ara öğün sayısı + üç ölçek (SBİTO, KADF, MFO)

**Ana araştırma sorusu:** Mikrobiyota farkındalığı yüksek olan bireyler gerçekten temel beslenme bilgisine (diyet lifi) ve olumlu tutuma sahip mi, yoksa bu farkındalık yüzeysel/trend kaynaklı mı ve altta yatan bilgi/tutumla örtüşmüyor mu? ("Farkında ama bilgisiz" hipotezi)

**Neden bu çerçeve seçildi:** Basit bir 2x2 çapraz tablo (araştırmacı tanımlı gruplar) yerine, grupların **veriden kendiliğinden çıkmasını** sağlayan bir karma model (mixture model) yaklaşımı tercih edildi — bu hem daha savunulabilir hem de hakem gözünde daha ikna edici bir yöntem.

### 1.1 Yöntem Pivotu: LCA → LPA

İlk planda kategorik indicator'larla **Latent Class Analysis (LCA)** kullanılması düşünülmüştü, ancak metodoloji literatürü incelendiğinde iki önemli bulgu ortaya çıktı:
1. Sürekli bir değişkeni yapay olarak kategorize etmek (medyan split dahil) bilgi kaybına, gücün düşmesine ve bazı durumlarda yanlış-pozitif sonuçlara yol açabiliyor (MacCallum ve ark. 2002; "cost of dichotomization" literatürü).
2. Gösterge değişkenler sürekli olduğunda, doğru teknik LCA değil **Latent Profile Analysis (LPA)** — literatürde bu net bir şekilde belirtiliyor.

**Karar:** Üç ölçeğin sürekli toplam skorları (`SBITO_TOPLAM_CANER`, `KADF_toplam_caner`, `MFO_toplam_skor`) kategorize edilmeden, standardize edilmiş haliyle **LPA**'ya (R'da `mclust` paketi) sokulacak. Kesme noktası tartışması tamamen ortadan kalktı. SBİTO'nun resmi 5 kategorisi yalnızca **betimsel/tanımlayıcı** raporlama için (LPA indicator'ı olarak değil) kullanılabilir.

**Analiz planı (3 aşamalı):**
1. **LPA** — SBİTO, KADF, MFO standardize toplam skorlarını (z-skor) indicator olarak kullanarak profil çıkarma
2. **Multinomial lojistik regresyon** — çıkan profilleri BMI, SES, meslek, kronik hastalık ile ilişkilendirme
3. **Keşifsel (gerekirse):** SEM/mediation, quantile regresyon — yalnızca ilk ikisi yetersiz kalırsa, ana çerçeve değil

**Yazılım:** R (`mclust` paketi, tidyLPA'nın da temel aldığı standart araç) — final/raporlanan analiz için. Jamovi yalnızca hızlı keşifsel önizleme için kullanıldı.

**Bağlantı — bu yöntem araştırma sorusuna nasıl cevap verecek:** LPA'dan çıkan profillerden biri "MFO yüksek ama SBİTO ve KADF düşük/orta" görünüyorsa, bu doğrudan "farkında ama bilgisiz" hipotezinin ampirik kanıtı olur. Sonraki adımda (multinomial lojistik regresyon), bu profile düşme olasılığı BMI, SES, meslek, kronik hastalıkla ilişkilendirilecek — yani "kimler bu yanıltıcı farkındalık grubuna düşüyor" sorusuna cevap verilecek.

---

## 2. Ölçekler ve Puanlama Yöntemleri

### 2.1 SBİTO (Sağlıklı Beslenmeye İlişkin Tutum Ölçeği)

- 21 madde, 5'li Likert (1-5)
- **4 alt boyut:**
  - Beslenme Hakkında Bilgi (BHB): M1-M5, düz kodlu
  - Beslenmeye Yönelik Duygu (BYD): M6-M11, **ters kodlu**
  - Olumlu Beslenme Alışkanlığı (OB): M12-M16, düz kodlu
  - Kötü Beslenme Alışkanlığı (KB): M17-M21, **ters kodlu**
- Ters kodlama formülü: 1↔5, 2↔4, 3=3
- **Toplam skor aralığı:** 21-105
- Yorumlama bantları (betimsel raporlama için): 21=çok düşük, 23-42=düşük, 43-63=orta, 64-84=yüksek, 85-105=ideal yüksek
- `SBITO_TOPLAM_CANER` sütunu **ampirik olarak doğrulandı** (R'da varyant karşılaştırmasıyla, n=1286'da fark=0): ham (ters çevrilmemiş) madde sütunları kullanılarak, ters kodlama toplam formülünün içinde doğru uygulanmış.

### 2.2 KADF (Diyet Lifi Bilgi Ölçeği)

- Orijinal 22 madde, ancak **EFA/CFA sonrası nihai yapı 8 maddeye indirgenmiş**: KADF_1, KADF_2, KADF_7, KADF_9, KADF_13, KADF_16, KADF_19, KADF_22
- **2 alt boyut:**
  - Diyet Lifinin Kaynakları (SDF): Q1, Q2, Q7, Q9 (Q9 ters kodlu)
  - Diyet Lifi ve Sağlığın Geliştirilmesi (DFPH): Q13, Q16, Q19, Q22, düz kodlu
- ⚠️ **ÖNEMLİ:** `KADF_toplam_caner` ve iki alt boyut, TOPLAM değil **ORTALAMA (mean)** olarak hesaplanmış — bu R'da ampirik olarak doğrulandı (4 varyant test edildi: ham/ters × toplam/ortalama; "ters Q9, ORTALAMA" varyantı n=1286'nın tamamında fark=0 ile eşleşti). **Skor aralığı 1-5'tir, 8-40 değil.** Makale metodolojisinde bu açıkça belirtilmeli.

### 2.3 MFO (Mikrobiyota Farkındalık Ölçeği)

- 20 madde, **4 faktör** (EFA/CFA doğrulamalı):
  - Genel Bilgi: M1, M2, M4, M5, M6, M13
  - Ürün Bilgisi: M17, M18, M19, M20
  - Kronik Hastalık: M8, M10, M12, M14, M16
  - Probiyotik ve Prebiyotik: M3, M7, M9, M11, M15
- **Geliştiriciler alt boyutlar yerine TOPLAM skorun kullanılmasını tavsiye ediyor** — bu çalışmada da ana analiz değişkeni `MFO_toplam_skor`, alt boyutlar ikincil/tamamlayıcı.
- **Puanlama (3 farklı madde tipi):**
  - M1-M16: düz 5'li Likert, ters kodlama yok (aralık 16-80)
  - M17-M18: checkbox — her doğru işaretleme +1, her yanlışı boş bırakma +1 (aralık 0-5 her biri)
    - M17 (Probiyotik): doğru=kefir/sirke/boza, yanlış=çay/yumurta
    - M18 (Prebiyotik): doğru=badem/muz/yulaf/soğan, yanlış=kırmızı et
  - M19-M20: açık uçlu, doğru cevap sayısına göre 1-5 arası yeniden kodlanmış (0 doğru=1, 1 doğru=2, 2 doğru=3, 3 doğru=4, 4+ doğru=5)
- **Toplam skor aralığı: 18-100**, ampirik olarak doğrulandı (min=21, max=98, aralık içinde)
- jamovi'de oluşturulan nihai değişken adları: `MFO_madde17_skor`, `MFO_madde18_skor`, `MFO_madde19_skor`, `MFO_madde20_skor`, `MFO_genel_bilgi`, `MFO_kronik_hastalik`, `MFO_pro_pre`, `MFO_urun_bilgisi`, `MFO_toplam_skor`

### 2.4 MFO_19/20 Açık Uçlu Soru Puanlama Sözlüğü

Probiyotik (M19) ve prebiyotik (M20) açık uçlu sorularının serbest metin yanıtları, R'da (fuzzy matching + substring arama, splitting yapılmadan) bir referans sözlüğüyle otomatik puanlandı. Sözlük Caner ile birlikte madde madde onaylandı:

**Probiyotik doğru:** kefir, yoğurt, turşu, sirke, ayran, şalgam, boza, tarhana, quark, kombucha, Activia (marka)
**Probiyotik yanlış:** süt, yumurta, muz, yulaf, et, peynir, soğan, badem, çay, sarımsak, elma, genel "probiyotik" ifadesi, takviye/hap, bakteri cinsi adları (Akkermansia, bifido vb.), Reflör/Enterogermina (marka/takviye)

**Prebiyotik doğru:** muz, yulaf, soğan, badem, sarımsak, elma, enginar, keten tohumu, baklagiller/bakliyat, pırasa, chia tohumu, kuşkonmaz, lahana, ceviz, yaban mersini, tam tahıl, brokoli, müsli, akasya gamı
**Prebiyotik yanlış:** kefir, yoğurt, et/kırmızı et, turşu, süt, sirke, yumurta, ayran, genel "meyve"/"sebze"/"ekmek"/"kuruyemiş" ifadeleri, şalgam, peynir, havuç, domates, portakal, kayısı, fındık, boza, quark, genel "prebiyotik" ifadesi, maydanoz, mandalina, ıspanak

---

## 3. Veri Kalitesi Kontrolleri (Aşama 1-3)

### 3.1 Genel Envanter
- 1417 satır, 117 sütun
- **0 duplicate** (tüm satır ve ID bazlı)
- BMI hazır sütun, ağırlık/boydan hesaplananla **birebir tutarlı** (fark=0)

### 3.2 Mantık Dışı Değer Taraması
- Yaş: 18-65, imkânsız değer yok
- Ağırlık: 40-160 kg, Boy: 145-200 cm, imkânsız değer yok
- BMI: 14.2-53.5, fizyolojik olarak imkânsız değer yok

### 3.3 Kategorik Değişken Hücre Doluluğu
Tüm kategorilerde (cinsiyet, medeni durum, meslek, SES, kronik hastalık, sigara, alkol, öğün sayıları) yeterli doluluk var, n<10 gibi kritik küçük hücre yok.

### 3.4 Eksik Veri — ÖNEMLİ BULGU
**131 katılımcı (%9.2), SBİTO+KADF+MFO'nun TAMAMINDA aynı anda eksik** (paralel/blok eksiklik — muhtemelen anketin o bölümünü hiç görmemiş/tamamlamamış kişiler). **Karar: bu 131 kişi veri setinden çıkarıldı**, kalan analiz örneklemi **n=1286**. Tüm kontroller bu temiz örneklemde tekrarlandı; %5 üstü eksik veri kalmadı (%0).

Eksik olan 131 kişinin ID listesi `Eksik_131_Katilimci_ID.csv` olarak kaydedildi.

### 3.5 Ölçek Güvenirliği (Cronbach's Alpha, n=1286)

| Ölçek/Alt Boyut | Alpha |
|---|---|
| SBİTO toplam | 0.798 |
| SBİTO - BHB | 0.963 |
| SBİTO - BYD | 0.793 |
| SBİTO - OB | 0.843 |
| SBİTO - KB | 0.834 |
| KADF toplam (8 madde) | 0.731 |
| KADF - SDF | **0.644 ⚠️ (eşik altı)** |
| KADF - DFPH | 0.930 |
| MFO toplam (M1-16) | 0.971 |
| MFO - Genel Bilgi | 0.941 |
| MFO - Kronik Hastalık | 0.922 |
| MFO - Probiyotik-Prebiyotik | 0.924 |

**Not:** KADF'nin SDF alt boyutu (0.644) kabul edilebilir eşiğin (0.70) altında — makalede sınırlılık olarak belirtilmeli. Toplam skorları kullanacağımız için LPA'yı engellemiyor.

### 3.6 Dağılım ve Çarpıklık (n=1286)

| Skor | Ortalama | SS | Çarpıklık | Yorum |
|---|---|---|---|---|
| SBİTO_TOPLAM_CANER | 73.6 | 11.7 | 0.16 | Neredeyse simetrik |
| KADF_toplam_caner | 3.1 | 0.7 | 0.00 | Mükemmel simetrik |
| MFO_toplam_skor | 69.0 | 16.2 | -0.89 | Orta derecede sola çarpık — histogramda ~45-50 civarı bir "çukur" ve iki ayrı yığılma var, LPA için umut verici bir işaret |

### 3.7 Local Independence Kontrolü

**Kavramsal analiz:** Madde içerik örtüşmeleri belirlendi (KADF Q19/MFO M15 - kabızlık; KADF Q16/MFO M8 - bağırsak kanseri; KADF Q22/MFO M10 - diyabet; KADF Q1&Q7/MFO M18&M20 - bitkisel kaynak/prebiyotik; SBİTO M14&M15/KADF Q1,Q7,Q13 - meyve-sebze davranışı/lif kaynağı bilgisi; SBİTO M2&M16/KADF Q2 - protein davranışı/hayvansal gıda-lif bilgisi).

**Ampirik doğrulama:** Bu madde-düzeyi örtüşmeler bir SEM/CFA modeli için risk oluştursa da, bizim modelimiz madde düzeyinde değil, **3 toplam skoru indicator olarak kullanıyor**. Üç toplam skor arasındaki korelasyon matrisi (n=1286):

| | SBİTO | KADF | MFO |
|---|---|---|---|
| SBİTO | 1.00 | 0.28 | 0.41 |
| KADF | 0.28 | 1.00 | 0.59 |
| MFO | 0.41 | 0.59 | 1.00 |

Hiçbir korelasyon 0.70 eşiğini aşmıyor → **local independence varsayımı 3-indicator tasarımı için makul ölçüde karşılanıyor.** KADF-MFO arası 0.59 (en yüksek) beklenen bir ilişki (ikisi de "bilgi" ölçeği). Not: LPA'da tam serbest kovaryans (VVV) modeli seçilirse, bu korelasyon zaten modelin bir parçası olarak hesaba katılabilir (bkz. Bölüm 3.9).

### 3.8 Aykırı Değer Taraması ve Standardizasyon (n=1286)

**Tek değişkenli (z-skor, |z|>3.29):** SBİTO'da 2 kişi (ID 142, ID 1113); KADF ve MFO'da 0 kişi.

**Tek değişkenli (IQR yöntemi):** KADF'de 127, MFO'de 65 "hafif aykırı" işaretlendi — ancak bunlar muhtemelen ölçeklerin kuantize/sivri (leptokurtik) dağılım yapısından kaynaklanan **yöntemsel bir artefakt**, gerçek aykırılık değil (z-skor yönteminde aynı kişiler işaretlenmedi). Bu kişiler çıkarılmadı.

**Çok değişkenli (Mahalanobis mesafesi, df=3, p<.001, kritik değer=16.27):** 2 kişi işaretlendi — ID 1113 (SBİTO=29 çok düşük, KADF=4.5 çok yüksek, MFO=83 yüksek) ve ID 94 (SBİTO=74 normal, KADF=4.5 çok yüksek, MFO=39 düşük). Değerlerin hiçbiri fizyolojik/mantık dışı değil, nadir ama **geçerli profil kombinasyonları** olarak değerlendirildi — çıkarılmadı. (ID 94 özellikle ilginç: yüksek lif bilgisi + düşük mikrobiyota farkındalığı, ana hipotezin ayna görüntüsü bir vaka.)

**Standardizasyon:** `SBITO_z`, `KADF_z`, `MFO_z` oluşturuldu (her biri ortalama=0, SS=1, doğrulandı). LPA'nın indicator'ları bunlar olacak.

**İkili serpilme grafikleri:** SBİTO-MFO ve KADF-MFO grafiklerinde ana bulutun altında görsel olarak ayrı bir alt küme var (düşük-düşük bölgesinde yoğunlaşma) — MFO'nun çarpıklığıyla tutarlı, LPA'nın anlamlı profiller bulma ihtimalini destekliyor. SBİTO-KADF'de böyle net bir ikincil küme yok (beklenen, çünkü aralarındaki korelasyon en düşük: r=0.28).

### 3.9 Kovaryans Yapısı Kararı (LPA'ya Özgü)

Literatür taraması (tidyLPA/mclust standart pratiği) sonucunda, uygulamalı psikoloji/sağlık literatüründe yaygın olarak karşılaştırılan **4 model** belirlendi:

| Model | Varyans | Kovaryans | mclust kodu |
|---|---|---|---|
| 1 | Eşit | Sıfır | EEI |
| 2 | Değişken | Sıfır | VVI |
| 3 | Eşit | Eşit | EEE |
| 6 | Değişken | Değişken | VVV |

Bu 4 model, 2-5 sınıf aralığında BIC'e göre karşılaştırılacak (Aşama 4). **Uyarı:** Tam serbest (VVV) modelin bazen sahte/yapay ekstra sınıflar üretebileceği literatürde belirtiliyor (Bauer & Curran) — BIC en düşük çıksa bile çıkan sınıfların yorumlanabilirliği ayrıca kontrol edilecek, sadece istatistiğe körü körüne güvenilmeyecek.

---

## 4. Aşama 4 — LPA Model Karşılaştırması (SIRADA)

**Durum:** R kodu hazırlandı (`Asama4_LPA_Model_Karsilastirma.R`), henüz çalıştırılmadı.

**Kullanılan veri seti:** `Mikrobiyota_Analiz_LPA_hazir.sav` (standardize edilmiş `SBITO_z`, `KADF_z`, `MFO_z` içeriyor)

**Script'in yaptıkları:**
1. 4 model (EEI, VVI, EEE, VVV) × 2-5 sınıf BIC karşılaştırma tablosu (`mclustBIC`)
2. En iyi modeli otomatik seçme
3. Her sınıf sayısı için entropy (>0.80 hedef) ve minimum sınıf büyüklüğü raporu
4. BLRT (bootstrap likelihood ratio test, 99 tekrar)
5. Nihai modelin sınıf profilleri — **orijinal (standardize edilmemiş) ölçekte** ortalama SBİTO/KADF/MFO skorları
6. Görselleştirme: BIC grafiği + 2 sınıf-renkli serpilme grafiği
7. Sonuç veri seti: `Mikrobiyota_Analiz_LPA_sonuc.sav` (sınıf atamalarıyla)

**Bundan sonraki adım:** Script çalıştırılıp rapor + grafikler paylaşıldığında, seçilen modelin/sınıf sayısının anlamlılığı ve "farkında ama bilgisiz" profilinin gerçekten çıkıp çıkmadığı birlikte değerlendirilecek.

---

## 5. Aşama 5-6 (LPA Sonrası, Henüz Başlanmadı)

- Sınıflara/profillere isim verme, içerik geçerliliği kontrolü (veri neyi gösteriyorsa onu raporlama, hipoteze zorlamadan)
- 3-step yaklaşımıyla (BCH veya ML method — naif "en yüksek olasılıklı sınıfı ata" yöntemi KULLANILMAYACAK) profil üyeliğini BMI, SES, meslek, kronik hastalık ile multinomial lojistik regresyonla ilişkilendirme
- Kovaryatlar arası VIF kontrolü

## 6. Diğer Notlar

- Veri setinde `AdınızSoyadınız` (gerçek ad-soyad, PII) sütunu var — analiz dışı tutulacak, paylaşım/arşivlemede çıkarılmalı
- Ek potansiyel dışlama kriteri sütunları mevcut: ilaç kullanımı, vitamin/mineral takviyesi, bariatrik cerrahi geçmişi, yeme bozukluğu öyküsü — ileride exclusion criteria olarak değerlendirilebilir
