---
ODAK:
  - "[[İstatistik]]"
Tür:
  - Çekirdek
BAĞLANTILI NOTLAR:
  - "[[SEM_Mediation_Moderation_Rehberi]]"
study_type: Metodoloji Rehberi
evidence_direction: null
primary_outcome: Ölçek uyarlama adımları
p_value_summary: N/A
BESLEDİĞİ NOTLAR:
  - "[[SEM_Mediation_Moderation_Rehberi]]"
MEKANİZMA:
  - "[[Metodoloji]]"
DİZİN:
  - "[[Ölçek Uyarlama]]"
ETİKET: dersten

---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> **Metodolojik Etiketler:** #finding/null
# Ölçek Uyarlama ve Psikometrik Değerlendirme Rehberi
### Beslenme ve Diyetetik Alanı İçin — Baştan Sona Uygulamalı Kılavuz

> Bu rehber, bir ölçme aracının (örn. bir davranış/tutum ölçeği) başka bir dile/kültüre uyarlanması ya da sıfırdan geliştirilmesi sürecindeki tüm istatistiksel adımları, **neden** yapıldıklarını, **nasıl** jamovi'de uygulanacaklarını ve sonuçların **nasıl yorumlanacağını** anlatır. Örnekler beslenme/diyetetik alanından seçilmiştir. Rehberin sonunda, bu süreçte birlikte çalıştığımız Mind-Eat Scale-TR uyarlamasından somut örnekler de veriliyor.

---

## İÇİNDEKİLER

1. Adım 1 — Dil ve Kapsam Geçerliği (Çeviri Süreci)
2. Adım 2 — Örneklem Planlaması ve Veri Toplama
3. Adım 3 — Veri Temizleme ve Ön Analiz
4. Adım 4 — Yapı Geçerliği: Doğrulayıcı Faktör Analizi (CFA)
5. Adım 5 — Güvenirlik Analizleri
6. Adım 6 — Geçerlik Analizleri (Yakınsak, Ayırt Edici, Bilinen-Gruplar)
7. Adım 7 — Sonuçların Raporlanması
8. Ek A — Vaka Çalışması: Mind-Eat Scale-TR'de Yaptığımız Adımlar
9. Ek B — Tüm Parametrelerin Sözlüğü

---

## ÖLÇEK GELİŞTİRME vs. ÖLÇEK UYARLAMA — HANGİ ADIMLAR NEREDE?

Bu rehberdeki adımların hangilerinin **sıfırdan yeni ölçek geliştirmede**, hangilerinin **var olan bir ölçeği başka dile/kültüre uyarlamada** (bizim Mind-Eat Scale-TR çalışmamız gibi), hangilerinin **her ikisinde de** kullanıldığını gösteren genel harita:

```mermaid
                    ÖLÇEK GELİŞTİRME                    ÖLÇEK UYARLAMA
                    ─────────────────                    ───────────────
                    Kavramsal çerçeve                     
                    + madde havuzu yazımı                 Orijinal ölçek
                           │                               zaten mevcut
                           │                                     │
                           │                          ┌──────────┴──────────┐
                           │                          │  İleri çeviri (≥2)   │
                           │                          │  Sentez              │
                           │                          │  Geri çeviri         │
                           │                          └──────────┬──────────┘
                           └──────────────┬───────────────────────┘
                                          │
                              ╔═══════════▼═══════════╗
                              ║   ORTAK ADIMLAR        ║
                              ║  Uzman görüşü / CVI     ║
                              ║  Pilot / bilişsel       ║
                              ║  görüşme                ║
                              ║  Örneklem toplama       ║
                              ║  Aykırı değer /         ║
                              ║  normallik kontrolü     ║
                              ╚═══════════╤═══════════╝
                                          │
                         ┌────────────────┴────────────────┐
                         │                                   │
                  ┌──────▼──────┐                    ┌───────▼───────┐
                  │     EFA      │                    │  (genelde      │
                  │  (zorunlu,   │                    │   atlanır —    │
                  │   temel      │                    │   yapı zaten   │
                  │   adım)      │                    │   biliniyor)   │
                  └──────┬──────┘                    └───────┬───────┘
                         │                                    │
                         └────────────────┬───────────────────┘
                                          │
                              ╔═══════════▼═══════════╗
                              ║          CFA            ║
                              ║  (Geliştirmede: EFA'yı  ║
                              ║   farklı örneklemde     ║
                              ║   doğrulamak için       ║
                              ║   Uyarlamada: doğrudan  ║
                              ║   ana yöntem)           ║
                              ╚═══════════╤═══════════╝
                                          │
                              ╔═══════════▼═══════════╗
                              ║   ORTAK ADIMLAR        ║
                              ║  Güvenirlik (α,CR,ICC) ║
                              ║  Geçerlik (convergent, ║
                              ║  discriminant,         ║
                              ║  known-groups)         ║
                              ╚═══════════╤═══════════╝
                                          │
                         ┌────────────────┴────────────────┐
                  ┌──────▼──────┐                    ┌───────▼───────┐
                  │ Norm / kesim │                    │ Orijinal ölçekle│
                  │ noktası      │                    │ kültürlerarası  │
                  │ belirleme    │                    │ karşılaştırma   │
                  │ (sık yapılır)│                    │ (özellikle önemli)│
                  └─────────────┘                    └───────────────┘
```

### Detaylı tablo

| Adım | Ölçek Geliştirme | Ölçek Uyarlama | Not |
|---|---|---|---|
| Kavramsal çerçeve + madde yazımı | ✅ Zorunlu | ❌ Yok | Uyarlamada madde havuzu zaten orijinal ölçekten gelir |
| Çeviri + geri çeviri | ❌ Yok | ✅ Zorunlu | Geliştirmede tek dilde yazılır |
| Uzman görüşü / CVI | ✅ Ortak | ✅ Ortak | İkisinde de madde-kavram uyumu kontrol edilir |
| Pilot / bilişsel görüşme | ✅ Ortak | ✅ Ortak (sık atlanır) | Uyarlamada sıkça atlanan ama önerilen adım |
| Örneklem toplama | ✅ Ortak | ✅ Ortak | Madde-katılımcı oranı kuralı ikisinde de geçerli |
| Aykırı değer / normallik | ✅ Ortak | ✅ Ortak | |
| **EFA** | ✅ **Zorunlu, temel adım** | ⚠️ Genelde atlanır | Uyarlamada sadece yapıdan ciddi şüphe varsa ya da split-half yaklaşımında kullanılır |
| **CFA** | ✅ EFA sonrası, farklı örneklemde | ✅ **Ana/doğrudan yöntem** | Geliştirmede EFA'yı "doğrulamak" için ikinci adım; uyarlamada tek başına yeterli |
| Madde çıkarma/eleme | ✅ Sık (zayıf maddeler atılır) | ⚠️ Nadir/dikkatli | Uyarlamada orijinal yapıyı bozmamak için madde çıkarmaktan kaçınılır |
| Güvenirlik (α, CR, test-retest/ICC) | ✅ Ortak | ✅ Ortak | |
| Geçerlik (convergent, discriminant, known-groups) | ✅ Ortak | ✅ Ortak | |
| Ölçüm değişmezliği | ✅ Ortak (opsiyonel/ileri) | ✅ Ortak (opsiyonel/ileri) | |
| Norm / kesim noktası belirleme | ✅ Sık yapılır | ⚠️ Bazen | Örn. "bu puanın üstü yüksek mindful eating" gibi klinik eşikler |
| Orijinal ölçekle kültürlerarası fit/sonuç karşılaştırması | ❌ Yok | ✅ **Özellikle önemli** | Bizim çalışmamızda tam olarak bunu yaptık — fit indekslerimizi orijinal Van Beekum ve ark. (2024) makalesiyle karşılaştırdık |

---

## ADIM 1 — DİL VE KAPSAM GEÇERLİĞİ (ÇEVİRİ SÜRECİ)

### Ne işe yarar, neden yapılır?
Bir ölçeği başka bir dile "çevirmek" yeterli değildir — madde bir dilde ölçtüğü kavramı diğer dilde de aynı şekilde ölçmelidir. Bu adım, dil ve kültür farkından kaynaklanabilecek anlam kaymalarını önler.

**Beslenme alanından örnek:** İngilizce bir "emotional eating" (duygusal yeme) maddesi olan *"I eat when I'm stressed"* ifadesi Türkçeye birebir çevrildiğinde ("Stresli olduğumda yerim") anlamını korur, ama *"I eat when I'm bored"* gibi bir ifade bazı kültürlerde daha az kabul edilebilir bulunabilir, cevaplama tarzını etkileyebilir — bu yüzden sadece dil değil, kavramsal eşdeğerlik de kontrol edilmelidir.

### Alt adımlar

**1.1 İleri Çeviri (Forward Translation)**
- En az 2 bağımsız, iki dile de hakim çevirmen, kaynak dilden hedef dile çevirir.
- Neden bağımsız/birden fazla kişi: Tek çevirmenin kişisel yorumu/kelime tercihi maddeyi çarpıtabilir; birden fazla versiyon karşılaştırılıp sentezlenir.

**1.2 Sentez / Uzlaşı**
- Çevirmenler (ve varsa bir hakem) bir araya gelip tek, ortak bir taslak üzerinde anlaşır.

**1.3 Geri Çeviri (Back-Translation)**
- Hedef dildeki taslak, orijinal dili görmemiş başka bir çevirmen tarafından tekrar kaynak dile çevrilir.
- Amaç: Geri çeviri orijinal maddeyle anlamca örtüşüyor mu, kontrol etmek. Örtüşmüyorsa, hedef dildeki madde revize edilir.

**1.4 Uzman Komitesi / İçerik Geçerliği (Content Validity)**
- Alanında uzman (örn. diyetisyen, psikolog, dilbilimci) 5-10 kişilik bir panel, her maddeyi **"bu madde ölçmek istediği kavramı temsil ediyor mu?"** sorusuyla puanlar (genelde 1-4 arası Likert: 1=alakasız, 4=çok alakalı).
- **İstatistik: Content Validity Index (CVI)**
  - **Madde düzeyi (I-CVI):** O maddeye 3 veya 4 puan veren uzman oranı. Hedef: **I-CVI ≥ 0.78** (Lynn, 1986 kriteri, uzman sayısına göre değişir).
  - **Ölçek düzeyi (S-CVI):** Tüm I-CVI'ların ortalaması. Hedef: **S-CVI ≥ 0.90**.
  - Davis tekniği (1992) de benzer bir yöntemdir, madde bazlı uzman uzlaşı oranını raporlar.
- Bu adımda maddeler elenebilir, revize edilebilir, ya da (nadiren) yeni madde eklenebilir.

**1.5 Pilot / Bilişsel Görüşme (Cognitive Debriefing) — genellikle atlanan ama önerilen adım**
- Ana veri toplamadan önce, hedef popülasyondan küçük bir grupla (10-30 kişi) ölçek uygulanır, "bu maddeyi nasıl anladınız?" diye sorulur.
- Amaç: Maddelerin gerçek katılımcılar tarafından da anlaşılır olduğunu (sadece uzmanlar değil) teyit etmek.

### jamovi'de bu adımda yapılacak bir şey yok
Bu adım tamamen nitel/uzman değerlendirmesi — istatistik yazılımı gerekmez, CVI hesaplamaları Excel'de bile yapılabilir (basit oran hesabı).

---

## ADIM 2 — ÖRNEKLEM PLANLAMASI VE VERİ TOPLAMA

### Ne işe yarar?
CFA gibi analizler, kararlı/güvenilir sonuç için belirli bir örneklem büyüklüğü gerektirir. Yetersiz örneklem, model tahminlerinin (faktör yükleri, fit indeksleri) dengesiz/güvenilmez çıkmasına yol açar.

### Kural
- **Madde-başına-katılımcı oranı:** En az **5:1**, ideal olarak **10:1** ve üzeri (örn. 24 maddelik bir ölçek için minimum 120, ideal 240+ katılımcı).
- Mutlak minimum örneklem: **n ≥ 200** çoğu kaynakta CFA için kabul edilebilir alt sınır olarak anılır (bizim çalışmamızda n=301, bu kritere fazlasıyla uyuyor).
- **Test-retest alt örneklemi:** Ana örneklemin bir kısmına (bizim çalışmamızda n=88), 2-4 hafta arayla ölçek tekrar uygulanır — bu, zamana göre kararlılığı (temporal stability) test etmek içindir.

---

## ADIM 3 — VERİ TEMİZLEME VE ÖN ANALİZ

### 3.1 Tek Değişkenli Aykırı Değerler (Univariate Outliers)

**Ne işe yarar:** Tek bir maddede aşırı uç bir cevap (örn. 5'li Likert'te sürekli hatalı 99 girilmiş bir satır), sonraki tüm analizleri bozabilir.

**İstatistik: Z-skoru**
- Her madde için: z = (X - X̄) / SD
- **Kabul aralığı: -3.29 ile +3.29 arası** (bazı kaynaklarda ±3). Bu aralığın dışına çıkan değerler aykırı kabul edilir.
- **jamovi'de:** Exploration > Descriptives, madde değişkenini seçip "Z-scores" kutusunu işaretleyin.

### 3.2 Çok Değişkenli Aykırı Değerler (Multivariate Outliers)

**Ne işe yarar:** Bir katılımcının her maddesi tek başına normal aralıkta olsa bile, maddeler **arasındaki kombinasyon** tuhaf/tutarsız olabilir (örn. "hiçbir zaman aç hissetmem" + "sürekli açlık hissederim" gibi çelişen cevaplar). Bunu tek değişkenli z-skor yakalayamaz.

**İstatistik: Mahalanobis Uzaklığı (Mahalanobis D²)**
- Her katılımcının, tüm maddeler üzerindeki cevap örüntüsünün, örneklem ortalamasından **çok boyutlu uzaklığını** ölçer.
- **Kritik değer:** χ² dağılım tablosundan, **df = madde sayısı**, **p < .001** için kritik değer alınır.
  - *Örnek: 24 maddelik bir ölçek için df=24, kritik χ²=51.179.*
  - Bu değeri aşan D² skoruna sahip katılımcılar çok değişkenli aykırı değer sayılır ve genelde veri setinden çıkarılır.
- **jamovi'de nasıl hesaplanır (Regression modülü üzerinden):**
  1. Analyses > Regression > Linear Regression.
  2. Dependent Variable: anlamsız/rastgele bir sürekli değişken (örn. katılımcı ID numarası) — Continuous tipinde olmalı.
  3. Covariates: tüm madde değişkenleri.
  4. **Save** sekmesinde **"Mahalanobis distance"**'ı işaretleyin — veri setine yeni bir sütun eklenir.
  5. Bu sütunu kritik değerle karşılaştırıp aşan vakaları belirleyin (bir Compute değişkeniyle `IF(MahalanobisDistance > kritik_deger, 1, 0)`).

**Bizim çalışmamızda yaptığımız:** 24 madde, df=24, kritik değer 51.179; 14 katılımcı bu eşiği aştığı için çıkarıldı, n=315'ten n=301'e düşüldü. *(Not: Bu hesaplamayı, aykırı değerler çıkarılmış n=301'lik veri setinde değil, **ham/tam n=315'lik veride** yapmak gerekir — zaten temizlenmiş bir örneklemde tekrar aykırı değer aramak yanıltıcı sonuç verir, bunu bu süreçte birlikte fark ettik.)*

### 3.3 Çok Değişkenli Normallik Testi

**Ne işe yarar:** Sonraki adımda (CFA) hangi tahmin yönteminin (estimator) kullanılacağına karar vermek için, verinin normal dağılıp dağılmadığını bilmemiz gerekir.

**İstatistik: Mardia'nın Çok Değişkenli Çarpıklık ve Basıklık Testi**
- İki ayrı χ² değeri üretir: **çarpıklık (skewness)** ve **basıklık (kurtosis)** için.
- **p < .05 ise** veri çok değişkenli normal dağılmıyor demektir.
- **Bizim çalışmamızda:** çarpıklık χ²=125.12 (p<.001), basıklık χ²=31.12 (p<.001) — normallik ihlal edilmiş, bu yüzden bir sonraki adımda **robust bir tahmin yöntemi (MLR)** seçildi.

### 3.4 Ters Kodlama (Reverse Coding) Kontrolü

**Ne işe yarar:** Bazı maddeler olumsuz/ters ifadeli yazılır (örn. "Yemek yerken ne yediğimin farkında değilim" gibi bir madde, "farkındalık" ölçeğinde ters kodlanmalıdır — yüksek katılım, düşük farkındalık anlamına gelir). Bu maddeler ters çevrilmeden analiz edilirse, o maddenin diğerleriyle **negatif** korelasyon göstermesi beklenir; bu bir hata değil, doğru bir sinyaldir, ama analiz öncesi mutlaka ters kodlanmalıdır.

**İstatistik: Madde-Toplam Korelasyonu (Item-Rest Correlation)**
- Her maddenin, kendi alt boyutundaki **diğer maddelerin toplamıyla** korelasyonu.
- **Hedef: pozitif ve > 0.30** (ters kodlama doğru yapılmışsa).
- **jamovi'de:** Analyses > Factor > Reliability Analysis; maddeleri girin, ters kodlanması gerekenleri **"Reverse Scaled Items"** kutusuna koyun; çıktıda **Item-Rest Correlation** tablosuna bakın.
- **Doğrulama tekniği (bu süreçte kullandığımız):** Bir maddeyi önce "Reverse Scaled Items" kutusundan çıkarıp (ham haliyle) çalıştırın — eğer o madde gerçekten ters ifadeliyse, item-rest korelasyonu **negatife dönmeli**. Sonra tekrar kutuya ekleyip pozitife döndüğünü doğrulayın. Bu öncesi/sonrası karşılaştırması, tek bir korelasyon matrisine bakmaktan çok daha güvenilirdir.

---

## ADIM 4 — YAPI GEÇERLİĞİ: DOĞRULAYICI FAKTÖR ANALİZİ (CFA)

### Ne işe yarar, neden yapılır?
CFA, "bu maddeler gerçekten teorik olarak öngörülen alt boyutlara (faktörlere) ayrılıyor mu?" sorusuna cevap verir. Açımlayıcı faktör analizinden (EFA) farkı: EFA "kaç faktör var, hangi madde hangisine gider" sorusunu **veriden keşfeder**; CFA ise **önceden belirlenmiş bir yapıyı** (örn. orijinal ölçekten gelen 6 faktörlü yapıyı) **test eder**. Bir ölçek uyarlama çalışmasında, orijinal yapı zaten belli olduğu için CFA kullanılır.

**Beslenme alanından örnek:** Bir "Yeme Farkındalığı" ölçeğinde "açlık/tokluk farkındalığı", "yargılamadan yeme" gibi alt boyutlar teorik olarak ayrı kavramlar olarak tasarlanmıştır — CFA, verinin gerçekten bu ayrımı destekleyip desteklemediğini sınar.

### 4.1 Model Kurma
Her faktör, kendi maddelerinin "sebebi" olarak modellenir (madde ← faktör yönünde ok, çünkü faktör gözlemlenemeyen/gizil bir kavram, maddeler onun gözlemlenebilir göstergeleridir).

```
NonReactivity =~ I2 + I5 + I8 + I20
Awareness     =~ I1 + I14 + I18 + I23
...
```

Faktörler varsayılan olarak birbiriyle **serbestçe korelasyonlu** (oblique) modellenir — yani "insanlar bir boyutta yüksekse diğerinde de yüksek/düşük olabilir" varsayımı, faktörlerin birbirinden tamamen bağımsız (ortogonal) olduğu varsayılmaz.

### 4.2 Tahmin Yöntemi (Estimator) Seçimi

| Veri normal mi? | Kullanılacak yöntem | Neden |
|---|---|---|
| Evet (Mardia p>.05) | ML (Maximum Likelihood) | Standart, en verimli yöntem |
| Hayır (Mardia p<.05) | **MLR (Robust ML)** | Standart hataları ve test istatistiğini normal-dışılığa göre düzeltir |
| Kategorik/sıralı veri (örn. 4 kategoriden az Likert) | WLSMV / DWLS | ML/MLR sürekli veri varsayar, kategorik veri için uygun değildir |

**Bizim çalışmamızda:** Mardia testi normal-dışılığı gösterdiği için **MLR** kullanıldı.

### 4.3 Fit (Uyum) İndeksleri — Model Ne Kadar İyi Uyuyor?

| İndeks | Ne ölçer | Kabul edilebilir | İyi | Notlar |
|---|---|---|---|---|
| **χ²/df** | Model-veri uyumsuzluğunun serbestlik derecesine oranı | < 3 | < 2 | Örneklem büyüklüğüne çok duyarlı, tek başına yeterli değil |
| **CFI** (Comparative Fit Index) | Modelin, "hiçbir ilişki yok" varsayılan modele göre ne kadar iyi olduğu | ≥ 0.90 | ≥ 0.95 | 0-1 arası, yüksek daha iyi |
| **TLI** (Tucker-Lewis Index) | CFI'ya benzer, parsimony (sadelik) cezası içerir | ≥ 0.90 | ≥ 0.95 | |
| **RMSEA** | Model başına düşen ortalama hata, örneklem büyüklüğüne göre düzeltilmiş | ≤ 0.08 | ≤ 0.06 | %90 güven aralığıyla birlikte raporlanmalı |
| **SRMR** | Standartlaştırılmış artık (residual) kovaryans ortalaması | ≤ 0.08 | ≤ 0.05 | |

**MLR kullanıldığında:** Bu indekslerin **"Robust/Scaled" (Satorra-Bentler ölçekli)** versiyonları raporlanmalı, standart/ham değerler değil — MLR'nin tüm amacı bu düzeltmeyi sağlamaktır.

**Kombine kriter (Hu & Bentler, 1999):** Tek bir indekse bakmak yerine, ya **CFI≥.95 + SRMR≤.08** ya da **RMSEA≤.06 + SRMR≤.09** kombinasyonlarından biri sağlanmalı.

**jamovi'de:** Analyses > SEM > Confirmatory Factor Analysis; Estimator=MLR; "Additional fit measures" kutusunu işaretleyin.

### 4.4 Faktör Yükleri (Factor Loadings)

**Ne anlama gelir:** Standartlaştırılmış faktör yükü (β), bir maddenin kendi faktörüyle ne kadar güçlü ilişkili olduğunu gösterir — **0 ile 1 arası bir korelasyon katsayısı** gibi düşünülebilir.

| Yük (β) | Yorum |
|---|---|
| < 0.30 | Zayıf, madde çıkarılması düşünülebilir |
| 0.30 – 0.50 | Kabul edilebilir |
| 0.50 – 0.70 | İyi |
| > 0.70 | Mükemmel |

### 4.5 Modifikasyon İndeksleri (Modification Indices) ve Residual Covariance

**Ne işe yarar:** Model tam oturmadığında (fit indeksleri sınırda), hangi ek parametrenin (genelde iki madde arasındaki "paylaşılan hata varyansı" / residual covariance) serbest bırakılırsa fit'in ne kadar iyileşeceğini gösterir.

**⚠️ Kritik kural:** Bir residual covariance'ı **sadece istatistiksel olarak (MI yüksek diye)** değil, **kavramsal bir gerekçeyle** (örn. iki madde neredeyse aynı şeyi soruyor, ya da aynı yöntemsel özelliği paylaşıyor) serbest bırakmalısınız. Sırf fit yükseltmek için rastgele parametre eklemek "veri balıkçılığı" (fit-hunting/HARKing) sayılır ve ciddi bir metodolojik hata olarak görülür.

**Bizim çalışmamızda:** Gratitude alt boyutundaki 2 madde (yiyeceğin doğal/ekolojik kaynağına — gezegen, çiftçiler — minnettarlık ifade eden maddeler) arasında hem en yüksek MI hem de net bir kavramsal örtüşme bulundu; bu residual covariance'ı gerekçeli şekilde serbest bıraktık ve model, makalede raporlanan orijinal fit indeksleriyle **birebir eşleşti** — bu bize, orijinal analizde de muhtemelen aynı adımın (raporlanmadan) yapıldığını gösterdi.

### 4.6 İkinci-Derece (Second-Order) CFA

**Ne işe yarar:** Bir ölçeğin **toplam skoru** kullanılacaksa (6 alt boyutun toplamı gibi), bunun istatistiksel olarak da savunulabilir olduğunu göstermek gerekir. Bu, altı alt boyutun kendisinin de tek bir üst ("genel") faktörün göstergeleri olarak modellenmesiyle test edilir.

**Ön koşul:** Birinci-derece faktörlerin birbiriyle **tutarlı ve genelde aynı yönde** korelasyonlu olması gerekir. Bir faktör bazılarıyla pozitif, bazılarıyla negatif korelasyonluysa, tek bir genel faktör altında toplanmaları kavramsal olarak zorlanır ve model **yakınsamayabilir** (converge etmeyebilir) ya da **Heywood durumu** (imkânsız/negatif varyans) ortaya çıkabilir.

**Bizim çalışmamızda:** Altı faktörle kurulan ikinci-derece model yakınsamadı; Non-reactivity'nin diğer faktörlerle karışık yönlü (bazılarıyla pozitif, bazılarıyla negatif) korelasyonu bunun sebebiydi. Bu, **bir hata değil, gerçek ve raporlanabilir bir bulgu** — toplam skorun orijinal ölçeğin basit toplama mantığıyla kullanılmasını, "tek bir gizil üst faktör" iddiası olmadan gerekçelendirdik.

---

## EK — EFA (AÇIMLAYICI FAKTÖR ANALİZİ): NE ZAMAN VE NASIL KULLANILIR

### CFA ile farkı ne?

| | EFA (Açımlayıcı) | CFA (Doğrulayıcı) |
|---|---|---|
| Ne zaman kullanılır | Faktör yapısı **önceden bilinmiyor**, veriden keşfedilecek | Faktör yapısı **önceden belirli** (örn. orijinal ölçekten), test edilecek |
| Tipik senaryo | Sıfırdan yeni bir ölçek geliştirme | Var olan bir ölçeği uyarlama / doğrulama |
| Soru | "Kaç faktör var, hangi madde hangisine gider?" | "Bu belirli yapı veriye uyuyor mu?" |
| Mind-Eat Scale-TR'de kullanıldı mı? | **Hayır** — orijinal ölçek zaten 6 faktörü kanıtlamıştı | **Evet** — bizim kullandığımız yöntem buydu |

**Önemli pratik not:** Bazı uyarlama çalışmaları, örneklemi ikiye bölüp **yarısında EFA, diğer yarısında CFA** yapar ("split-half" yaklaşımı) — bu, hem keşif hem doğrulama yapmak isteyen, faktör yapısının orijinal dilde/kültürde birebir tekrar edip etmeyeceğinden emin olmayan çalışmalarda tercih edilir. Sizin çalışmanızda buna gerek görülmemiş, doğrudan CFA ile ilerlenmiş — bu, orijinal yapının güçlü/net olduğu durumlarda kabul edilebilir bir tercihtir.

### EFA'nın adımları

**1. Verinin faktör analizine uygunluğunu test etme**

- **KMO (Kaiser-Meyer-Olkin) Örneklem Yeterliliği Testi:** Değişkenler arası korelasyonların, faktör analizine ne kadar "uygun" olduğunu gösterir.

| KMO değeri | Yorum |
|---|---|
| < 0.50 | Kabul edilemez |
| 0.50 – 0.70 | Vasat (mediocre) |
| 0.70 – 0.80 | İyi |
| 0.80 – 0.90 | Çok iyi |
| > 0.90 | Mükemmel |

- **Bartlett's Test of Sphericity:** Korelasyon matrisinin bir "birim matris" (yani değişkenler arasında hiç ilişki yok) olup olmadığını test eder. **p < .05 olmalı** — anlamlıysa, değişkenler arasında faktör analizine yetecek kadar ilişki var demektir.

**2. Faktör çıkarma (extraction) yöntemi**

- **Principal Axis Factoring (PAF)** ya da **Maximum Likelihood (ML)** önerilir — davranışsal/psikolojik ölçeklerde tercih edilen gerçek faktör analizi yöntemleridir.
- **Principal Component Analysis (PCA) ile karıştırılmamalı:** PCA teknik olarak faktör analizi değildir (ölçüm hatasını ayrıştırmaz, sadece veriyi sıkıştırır) — literatürde sıkça karıştırılsa da, ölçek geliştirme çalışmalarında PAF/ML tercih edilmelidir.

**3. Kaç faktör tutulmalı?**

| Yöntem | Açıklama | Güvenilirlik |
|---|---|---|
| **Kaiser Kriteri** (özdeğer/eigenvalue > 1) | En eski, en yaygın ama en çok eleştirilen yöntem | Düşük — genelde faktör sayısını olduğundan fazla tahmin eder |
| **Scree Plot (Çizgi Grafiği)** | Özdeğerlerin grafiğinde "dirsek" noktasından öncesi tutulur | Orta — görsel/subjektif yorum gerektirir |
| **Paralel Analiz (Horn, 1965)** | Gerçek veriden elde edilen özdeğerleri, rastgele üretilmiş veriden elde edilenlerle karşılaştırır | **En güvenilir, önerilen yöntem** |

**4. Rotasyon (Rotation)**

- **Dik (Orthogonal) — Varimax:** Faktörlerin birbirinden tamamen bağımsız (korelasyonsuz) olduğu varsayılır.
- **Eğik (Oblique) — Promax / Direct Oblimin:** Faktörlerin birbiriyle korelasyonlu olabileceği varsayılır.
- **Sosyal/davranışsal bilimlerde genelde eğik (oblique) rotasyon önerilir** — çünkü psikolojik/davranışsal alt boyutların (örn. "farkındalık" ile "yargılamama") gerçek hayatta tamamen bağımsız olması beklenmez, birbiriyle bir miktar ilişkili olmaları normaldir (tıpkı bizim CFA'da faktörler arası korelasyonları serbest bırakmamız gibi, aynı mantık).

**5. Sonuçları yorumlama**

- **Faktör yükü eşiği:** Genelde **≥ 0.32** (bazı kaynaklarda ≥ 0.40) altındaki yükler "anlamsız" sayılır, madde o faktöre ait kabul edilmez.
- **Çapraz yüklenme (cross-loading):** Bir madde birden fazla faktöre benzer güçte yükleniyorsa (aradaki fark **< 0.20** ise) sorunlu kabul edilir — o madde hangi kavramı ölçtüğü belirsiz demektir, çıkarılması düşünülmelidir.
- **Ortaklık (Communality, h²):** Bir maddenin varyansının, **tüm faktörler tarafından birlikte** ne kadar açıklandığını gösterir. **Hedef: ≥ 0.40.** Düşük ortaklık, o maddenin genel yapıyla zayıf ilişkili olduğunu gösterir.

### jamovi'de EFA

1. Analyses > Factor > **Exploratory Factor Analysis**.
2. Maddeleri "Variables" kutusuna atın.
3. **Assumption Checks** altında **KMO** ve **Bartlett's test** kutularını işaretleyin.
4. **Extraction Method:** "Principal axis" ya da "Maximum likelihood" seçin (PCA değil).
5. **Number of Factors:** "Parallel Analysis" seçeneğini işaretleyin (en güvenilir yöntem).
6. **Rotation:** "Oblimin" ya da "Promax" (eğik rotasyon) seçin.
7. Çıktıda: faktör yükleri tablosu, özdeğerler (eigenvalues), faktörler arası korelasyon matrisi (eğik rotasyon seçtiyseniz) görünecek.

---

## ADIM 5 — GÜVENİRLİK ANALİZLERİ

### 5.1 İç Tutarlılık (Internal Consistency)

**Ne işe yarar:** Aynı alt boyuttaki maddelerin birbiriyle ne kadar tutarlı cevaplandığını gösterir — "bu maddeler gerçekten aynı şeyi ölçüyor mu?"

**İstatistik 1: Cronbach's Alpha (α)**
- 0-1 arası. **Hedef: ≥ 0.70** (bazı kaynaklarda 0.60 da kabul edilebilir sayılır, özellikle kısa alt boyutlarda).
- **Sınırlılığı:** Madde sayısına duyarlıdır (az maddeli alt boyutlarda düşük çıkabilir, madde sayısını artırmak yapay olarak alpha'yı da artırır).

**İstatistik 2: Composite Reliability (CR)**
- CFA'daki gerçek faktör yüklerine dayanır, Cronbach's alpha'nın bu sınırlılığını kısmen aşar.
- **Hedef: ≥ 0.70**.

**İstatistik 3: AVE (Average Variance Extracted)**
- Bir faktörün, kendi maddelerindeki varyansın ne kadarını "gerçekten açıkladığını" gösterir (hesaplama: faktör yüklerinin karelerinin ortalaması).
- **Hedef: ≥ 0.50** (faktör, maddelerindeki varyansın en az yarısını açıklamalı).
- Ayrıca **ayırt edici geçerlik** (bkz. Adım 6.2) hesaplamasında kullanılır.

**jamovi'de:** Analyses > Factor > Reliability Analysis (α için); CR ve AVE için SEM modülünün "Additional outputs" / "Reliability indices" seçeneği.

### 5.2 Test-Tekrar Test Güvenirliği (Test-Retest Reliability)

**Ne işe yarar:** Ölçek, aynı kişiye 2-4 hafta arayla (durumun gerçekte değişmediği varsayılan bir sürede) tekrar uygulandığında **benzer sonuç veriyor mu?** Bu, ölçeğin zamana göre kararlılığını gösterir.

**İstatistik 1: Paired-Samples t-test**
- Pre-test ve re-test ortalamaları arasında anlamlı fark **olmaması** beklenir (p > 0.05) — fark yoksa, ölçek zamanla tutarlı demektir.
- **df = n - 1** (n = test-retest alt örneklemi büyüklüğü). *(Bu çalışmada n=88 için df=87 olmalıyken 88 yazılmış bir hata bulup düzelttik — bu, sık yapılan bir hatadır, dikkat edilmeli.)*

**İstatistik 2: Pearson Korelasyonu (r)**
- Pre-test ve re-test skorları arasındaki doğrusal ilişki. **Hedef: r ≥ 0.70**.
- **Sınırlılığı:** Sadece "birlikte değişme"yi yakalar, sistematik bir kaymayı (örn. herkesin re-test'te tam 5 puan daha yüksek çıkması) yakalamaz.

**İstatistik 3: Intraclass Correlation Coefficient (ICC)** — daha güçlü, tercih edilen yöntem
- Hem ilişkiyi hem de **mutlak uyumu** (ortalama kaymayı) hesaba katar, bu yüzden Pearson r'den daha katı ve daha güvenilir bir kanıt sayılır.
- **Model seçimi:** *Two-way mixed*, **Absolute Agreement**, Single measures (Koo & Li, 2016 önerisi).
- **Yorumlama (Koo & Li, 2016):**

| ICC | Yorum |
|---|---|
| < 0.50 | Zayıf |
| 0.50 – 0.75 | Orta |
| 0.75 – 0.90 | İyi |
| > 0.90 | Mükemmel |

- **jamovi'de:** seolmatrix modülü > "Rater Reliability" (ICC, "test-retest" bağlamında da kullanılır, "raters" yerine "zaman noktaları" olarak düşünülür) > ICC for oneway and twoway models bölümünde Model=twoway, Type=agreement, Unit=single.

---

## ADIM 6 — GEÇERLİK ANALİZLERİ

### 6.1 Yakınsak Geçerlik (Convergent Validity)

**Ne işe yarar:** Yeni ölçeğin, **aynı ya da benzer kavramı ölçen başka, zaten geçerliği kanıtlanmış bir ölçekle** ilişkili olup olmadığını test eder — "gerçekten ölçmek istediğimiz şeyi ölçüyor mu?" sorusuna dolaylı bir cevap.

**Beslenme örneği:** Yeni bir "sezgisel yeme" ölçeğinin, zaten bilinen bir "yeme farkındalığı" ölçeğiyle **orta-yüksek düzeyde pozitif** korelasyonlu çıkması beklenir (aynı ailede ama farklı kavramlar oldukları için **çok yüksek** ―örn. r>0.90― olmamalı, aksi halde iki farklı şeyi ölçmüyorlar demektir).

**İstatistik: Pearson Korelasyonu**
- **Hedef: r = 0.30 – 0.70** arası genelde "iyi" kabul edilir (çok düşükse yakınsak geçerlik zayıf, çok yüksekse ölçekler ayırt edilemez).

### 6.2 Ayırt Edici Geçerlik (Discriminant Validity)

**Ne işe yarar:** Ölçeğin **alt boyutlarının birbirinden gerçekten farklı** (aşırı örtüşmeyen) kavramları ölçtüğünü gösterir.

**İstatistik 1: Fornell-Larcker Kriteri**
- Her faktörün **√AVE**'si (bkz. Adım 5.1), o faktörün diğer faktörlerle olan korelasyonlarından **büyük** olmalı.

**İstatistik 2: HTMT (Heterotrait-Monotrait Ratio) — daha modern, tercih edilen yöntem**
- Fornell-Larcker'dan daha güçlü istatistiksel özelliklere sahip olduğu gösterilmiştir (Henseler ve ark., 2015).
- **Hedef: < 0.85** (kavramsal olarak birbirine yakın alt boyutlar için < 0.90 da bazen kabul edilir).
- **jamovi'de:** SEM modülünde CFA çalıştırırken "Output options" altında **HTMT** kutusunu işaretleyin — otomatik matris üretir.

### 6.3 Bilinen-Gruplar Geçerliği (Known-Groups Validity)

**Ne işe yarar:** Ölçeğin, **teorik olarak farklı olması beklenen iki grubu gerçekten ayırt edip edemediğini** test eder — CFA'nın "yapısal" kanıtından farklı olarak, **pratik/kriter** kanıtı sağlar.

**Beslenme örneği:** Bir "yeme farkındalığı" ölçeğinde, **normal kilolu bireylerin, obez bireylere göre daha yüksek** puan alması beklenir (literatürde düşük mindful eating ile yüksek BMI ilişkilendirilir) — bu farkı gerçekten bulmak, ölçeğin pratikte işe yaradığının kanıtıdır.

**İstatistik: Bağımsız Örneklem t-testi (ya da >2 grup için ANOVA)**
- **Varsayım kontrolü:** Levene's testi ile varyans homojenliği kontrol edilir; ihlal edilirse (p<.05) **Welch's t-test** kullanılır (Student's t yerine).
- **Etki büyüklüğü: Cohen's d** mutlaka raporlanmalı (sadece p-değeri yeterli değil):

| d | Etki büyüklüğü |
|---|---|
| 0.20 | Küçük |
| 0.50 | Orta |
| 0.80 | Büyük |

- **Çoklu karşılaştırma düzeltmesi:** Birden fazla alt boyut aynı anda test edilirse (örn. 6 alt boyut + toplam = 7 test), **Bonferroni düzeltmesi** uygulanmalı: α_düzeltilmiş = 0.05 / test sayısı (7 test için α=0.0071). Bu eşiği aşamayan sonuçlar "nominal anlamlı ama düzeltme sonrası anlamsız" olarak raporlanır.

**jamovi'de:** Analyses > T-Tests > Independent Samples T-Test; Assumption Checks altında Levene's testi işaretleyin; Effect Size altında Cohen's d işaretleyin.

### 6.4 Ölçüm Değişmezliği (Measurement Invariance) — İleri Düzey, Opsiyonel

**Ne işe yarar:** Ölçeğin, **farklı gruplarda (örn. kadın/erkek) aynı şekilde işleyip işlemediğini** test eder — grup karşılaştırması yapmadan önce bu varsayımın doğrulanması idealdir.

**Aşamalar (her biri bir öncekinin üstüne kısıtlama ekler):**
1. **Configural invariance:** Aynı faktör yapısı her grupta geçerli mi?
2. **Metric invariance:** Faktör yükleri gruplar arasında eşit mi?
3. **Scalar invariance:** Madde kesişim noktaları (intercepts) da eşit mi? (Bu sağlanırsa gruplar arası ham puan karşılaştırması güvenle yapılabilir.)

**Model karşılaştırma kriteri:** Her aşamada bir öncekine göre **ΔCFI < 0.01** ve **ΔRMSEA < 0.015** ise, o aşamadaki invariance (değişmezlik) desteklenmiş sayılır.

**jamovi'de:** SEM modülünde "Multi-group analysis" bölümünde grup değişkenini atayıp, "Equality constraints" altında sırasıyla Loadings, Intercepts kutucuklarını işaretleyerek her aşama test edilir.

---

## ADIM 7 — SONUÇLARIN RAPORLANMASI

Bir ölçek uyarlama makalesinde en az şunlar raporlanmalı:
- Çeviri süreci + CVI sonuçları
- Örneklem özellikleri (Tablo 1)
- Aykırı değer/normallik sonuçları + kullanılan estimator gerekçesi
- CFA fit indeksleri (robust/scaled) + faktör yükleri tablosu + path diyagramı
- Yapılan tüm post-hoc düzeltmeler (residual covariance vb.) **gerekçesiyle birlikte**, şeffaf şekilde
- İç tutarlılık (α, CR) + test-retest (r/ICC)
- Yakınsak + ayırt edici + (varsa) bilinen-gruplar geçerliği
- Sınırlılıklar (özellikle test edilmeyen adımlar — örn. ölçüm değişmezliği yapılmadıysa bunun açıkça belirtilmesi)

---

## EK A — VAKA ÇALIŞMASI: MIND-EAT SCALE-TR'DE YAPTIĞIMIZ ADIMLAR

Bu, yukarıdaki tüm adımların gerçek bir uygulamada nasıl bir araya geldiğinin özeti:

| Adım | Ne yaptık | Sonuç |
|---|---|---|
| Dil geçerliği | 5 çevirmen, geri çeviri, 8 uzman CVI | Uygulanmıştı (biz dahil olmadık) |
| Aykırı değer (tek değişkenli) | Z-skoru, ±3 | Sorun yok |
| Aykırı değer (çok değişkenli) | Mahalanobis D², df=24, kritik=51.179, **n=315 ham veride** | 14 kişi çıkarıldı, n=301 — orijinal iddia doğrulandı |
| Normallik | Mardia testi | Normal değil → MLR seçildi |
| Ters kodlama | Item-rest korelasyonu, önce/sonra testi | 2,4,5,8,10,17,20,22 doğru kodlanmış |
| CFA | 6 faktör, MLR | χ²/df=1.93, CFI=0.92 (C16~~C24 residual covariance ile) |
| Residual covariance | Gratitude'daki 2 madde, kavramsal + MI gerekçeli | Fit, makaledeki orijinal sayılarla birebir eşleşti |
| Ayırt edici geçerlik | HTMT | Tüm değerler <0.85 ✓ |
| Second-order CFA | Toplam skor gerekçesi için | 6 faktörle yakınsamadı → additive scoring gerekçelendirildi |
| İç tutarlılık | α, CR | Hedef aralıkta |
| Test-retest | Pearson r + paired t (df=87 düzeltildi) + ICC | ICC=0.734–0.841, "orta-iyi" |
| Yakınsak geçerlik | MEI ile korelasyon | r=0.107 (ns, Openness) – 0.684 (toplam) |
| Bilinen-gruplar geçerliği | BMI'ye göre Welch's t + Bonferroni | Toplam, Non-judgment, Hunger/Satiety sağlam; Gratitude ters yönde (replikasyon gerekli) |

---

## EK B — TÜM PARAMETRELERİN SÖZLÜĞÜ

| Sembol/Terim | Anlamı |
|---|---|
| **β (beta)** | Standartlaştırılmış faktör yükü ya da regresyon katsayısı; -1 ile 1 arası |
| **SE** | Standart hata — tahminin ne kadar kesin/güvenilir olduğu (küçük SE = daha kesin) |
| **z** | Tahmin / SE — kaç standart sapma uzakta olduğu, p-değerini üretmek için kullanılır |
| **p** | O sonucun, gerçekte hiçbir etki yokken (şans eseri) bu kadar uç çıkma olasılığı; p<.05 genelde "anlamlı" eşiği |
| **df** | Serbestlik derecesi — modeldeki "serbest bilgi" miktarı, örneklem büyüklüğü/parametre sayısına bağlı |
| **χ² (ki-kare)** | Model ile veri arasındaki uyumsuzluğun büyüklüğü; küçük daha iyi |
| **CFI, TLI, RMSEA, SRMR** | Bkz. Adım 4.3 |
| **AVE** | Bkz. Adım 5.1 |
| **CR** | Composite Reliability, bkz. Adım 5.1 |
| **α (Cronbach's alpha)** | İç tutarlılık katsayısı, bkz. Adım 5.1 |
| **ICC** | Intraclass Correlation, bkz. Adım 5.2 |
| **r (Pearson)** | İki değişken arası doğrusal ilişki gücü, -1 ile 1 arası |
| **d (Cohen's d)** | İki grup ortalaması arası farkın standart sapma cinsinden büyüklüğü |
| **HTMT** | Heterotrait-Monotrait oranı, bkz. Adım 6.2 |
| **MI (Modification Index)** | Bir parametre serbest bırakılırsa χ²'nin ne kadar düşeceğinin tahmini |
| **sEPC** | Standartlaştırılmış beklenen parametre değişimi — MI'nin "büyüklük" versiyonu |
| **MLR** | Robust Maximum Likelihood — normal olmayan veri için düzeltilmiş tahmin yöntemi |
| **Mahalanobis D²** | Bir vakanın çok boyutlu uzaklığı, bkz. Adım 3.2 |

---

*Bu rehber, Mind-Eat Scale-TR uyarlama sürecinde birlikte yürüttüğümüz analizlerin genel bir çerçevesi olarak hazırlanmıştır. Her yeni ölçek çalışmasında adımların sırası ve gerekliliği (özellikle second-order CFA, known-groups, measurement invariance gibi ileri adımlar) araştırma sorusuna ve ölçeğin amacına göre değişebilir.*
