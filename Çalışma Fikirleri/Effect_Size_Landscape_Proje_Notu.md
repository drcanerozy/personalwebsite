# Effect-Size Landscape: Sistemik Kilo Kaybı ve Hücresel/Klinik Yanıt Arasındaki İlişkinin Çok Boyutlu Haritalanması

*Personalized Fasting derlemesinin (Paralel Filtreleme Modeli) doğrudan bir ampirik takip çalışması olarak tasarlanmıştır.*

## 1. Gerekçe ve Araştırma Sorusu

Ana derleme, sistemik ve hücresel yanıtların sıklıkla ayrıştığını (dissociation) ve bu ayrışmanın rastgele değil, sistematik (eşik, ikili kapı, yön belirleyici, zaman penceresi) olduğunu savunuyor. Ancak bu iddia şu ana kadar yalnızca vaka-vaka anlatılan örneklerle destekleniyor — sistematik, nicel bir haritalama yapılmadı.

**Araştırma sorusu:** Açlık müdahalelerinde, sistemik kilo kaybı etki büyüklüğü ile hücresel/klinik iyileşme etki büyüklüğü arasındaki ilişki, mevcut literatürde doğrusal mi, eşik-bağımlı (basamaklı) mı, yoksa hiçbir tutarlı örüntü göstermiyor mu?

**İkincil soru:** Bu ilişkinin yönü ve gücü, baseline fenotip (yaş, cinsiyet, bazal metabolik durum) ve protokol türüne göre nasıl değişiyor?

## 2. Çalışma Tipi

Meta-analiz DEĞİL — tür/protokol/uç nokta heterojenliği nedeniyle tek bir özet etki büyüklüğü çıkarmak yanıltıcı olur. Bunun yerine:

**Sistematik scoping review + çok boyutlu görsel sentez** (PRISMA-ScR uyumlu), isteğe bağlı olarak segmented regression / change-point analizi ile desteklenmiş.

## 3. Literatür Taraması Stratejisi

### 3.1. Popülasyon kapsamı: insan / hayvan / karma?

Öneri: **İkisi de dahil edilmeli, ama ayrı katmanlar (strata) olarak** — birleştirilmiş (pooled) analiz yapılmamalı.

- İnsan ve hayvan verileri aynı matriste **ayrı panel/facet** olarak gösterilmeli, asla aynı eksende doğrudan karşılaştırılmamalı (biyolojik ölçek farkı, doz-yanıt farkı çok büyük).
- Gerekçe: ana derlemenin kendisi de insan ve hayvan bulgularını birbirini destekleyen ama ayrı kanıt hatları olarak ele alıyor; bu tutarlılığı korumak metodolojik olarak daha savunulabilir.
- Alt katman önerisi: (i) yalnızca insan, (ii) yalnızca kemirgen, (iii) her ikisinde de aynı bulgunun tekrarlandığı "yakınsama" vakaları ayrı bir kategori olarak işaretlenebilir (bu, modelin dış geçerliliği için özellikle değerli bir alt küme olur).

### 3.2. Ölçüm tekniği/yöntemi stratifikasyonu — evet, kritik bir boyut

Bu, atlanırsa ciddi bir "elma-armut" karşılaştırma riski taşıyan bir nokta. Aynı kavram (örn. "insülin duyarlılığı" veya "enflamasyon") çok farklı araçlarla ölçülüyor ve bunlar doğrudan aynı eksende birleştirilemez:

| Parametre | Olası ölçüm yöntemleri (birbirine indirgenemez) |
|---|---|
| Kilo/adipozite | Tartı/BMI vs. DXA/MRI ile yağ kütlesi vs. kaliper |
| İnsülin duyarlılığı | HOMA-IR vs. klemp (gold standard) vs. OGTT-türevi indeksler |
| Enflamasyon | Dolaşımdaki hsCRP/sitokin vs. doku gen ekspresyonu (RT-PCR/RNA-seq) vs. IHC/protein düzeyi |
| Lipoliz | Plazma gliserol/FFA vs. doku eksplant lipoliz testi vs. gen ekspresyonu (ATGL/HSL) |
| Hücresel yeniden biçimlenme | Transkriptomik vs. histoloji/morfometri vs. tek hücre analizi |

**Öneri:** Her bir uç nokta kategorisi için ayrı bir "ölçüm yöntemi" etiketi extraction formunda zorunlu alan olmalı. Analiz/görselleştirme aşamasında ya (a) yalnızca aynı yöntemle ölçülmüş çalışmalar aynı panelde karşılaştırılmalı, ya da (b) yöntem, bubble'ın şekli/kenar stiliyle kodlanarak görsel olarak ayırt edilebilir kılınmalı — ama asla sayısal olarak birleştirilmemeli (örn. HOMA-IR değişimi ile klemp-türevi değişim aynı "insülin duyarlılığı etki büyüklüğü" sütununa doğrudan girmemeli).

### 3.3. Veri tabanları ve arama terimleri (taslak)

- PubMed/MEDLINE, Web of Science, Europe PMC (ana derlemeyle aynı üçlü, tutarlılık için)
- Tarih aralığı: ana derlemeyle örtüşen veya onu genişleten bir pencere (örn. 2015–2026) — burada geriye daha çok gidilebilir çünkü artık amaç kavramsal keşif değil, nicel veri toplamak
- Boolean kümeleri: (i) protokol terminolojisi (aynı), (ii) adipoz/metabolik uç nokta terminolojisi (aynı + "HOMA-IR", "clamp", "DXA", "hsCRP" gibi yöntem-spesifik terimler eklenerek), (iii) **"effect size" OR "mean difference" OR "pre-post" OR "baseline vs endpoint"** gibi nicel raporlama terimleri — bu üçüncü küme, ham sayısal veri raporlamayan çalışmaları elemeye yardımcı olur

### 3.4. Dahil etme / dışlama kriterleri (taslak)

**Dahil:**
- Hem sistemik (kilo/BMI/yağ kütlesi) hem hücresel/klinik (belirtilen bir kategoriden en az biri) uç noktayı aynı çalışmada raporlayan
- Ham sayısal veri (ortalama ± SD/SE, veya grafikten çıkarılabilir) sunan
- Baseline ve endpoint (veya değişim) değerlerini ayrı ayrı raporlayan

**Dışla:**
- Yalnızca tanımlayıcı/kalitatif sonuç bildiren (sayısal veri yok)
- Tek bir uç nokta türü (yalnızca sistemik veya yalnızca hücresel) raporlayan
- Kanser kaşeksisi, T1DM, anoreksiya, akut cerrahi travma (ana derlemeyle tutarlı dışlama)

## 4. Veri Çıkarma (Extraction) Planı

Her çalışma için çift etki büyüklüğü çıkarılacak:
- Sistemik etki büyüklüğü (standardize edilmiş — Hedges' g veya % değişim, ölçüm birimine göre normalize)
- Hücresel/klinik etki büyüklüğü (aynı şekilde standardize, ama yöntem etiketiyle birlikte)
- Örneklem büyüklüğü (bubble boyutu için)
- Güven aralığı / SE (mümkünse — "sıfıra yakın ama gerçek sıfır mı, güç yetersizliği mi" ayrımı için)
- Baseline fenotip: yaş, cinsiyet, bazal metabolik durum (obez/sağlıklı/diyabetik)
- Protokol türü, süre, sıklık
- Tür (insan/kemirgen) ve doku/örnekleme kaynağı

## 5. Görsel Sentez — Matris Tasarımı

- **X ekseni:** sistemik etki büyüklüğü
- **Y ekseni:** hücresel/klinik etki büyüklüğü (uç nokta kategorisine göre ayrı panel)
- **Bubble boyutu:** örneklem büyüklüğü
- **Renk:** protokol türü
- **Panel/facet:** (i) insan vs. kemirgen, (ii) ölçüm yöntemi kategorisi, (iii) baseline fenotip

## 6. Analitik Yaklaşım (isteğe bağlı, ikinci aşama)

- Doğrusal korelasyon yerine **segmented regression / change-point analizi** — modelin "eşik" iddiasını doğrudan test eder
- Baseline fenotip × etki büyüklüğü etkileşimi için moderatör analizi — "yön belirleyici" iddiasını test eder

## 7. Ana Metodolojik Riskler

- Extraction yükü ağır: iki bağımsız etki büyüklüğünü standardize etmek zaman alıcı, bazı çalışmalarda ham veri eksikliği nedeniyle imkânsız olabilir
- Yöntem heterojenliği (bkz. 3.2) yeterince katı stratifiye edilmezse yanıltıcı görsel örüntüler ortaya çıkabilir
- İnsan-hayvan verisinin yanlışlıkla aynı eksende birleştirilme riski — extraction formunda tür alanı zorunlu olmalı

## Sonraki Adımlar (henüz karar verilmedi)

- Hedef dergi belirlenmedi
- OSF ön kaydı gerekip gerekmediği değerlendirilmeli
- Pilot extraction (5-10 çalışma) ile formun işlerliği test edilmeli

## Bağlantılı Notlar
- [[IF-crossover-carryover-protokol]]
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
- [[Olcek_Uyarlama_Istatistik_Rehberi]]
- [[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]
- [[Mendelian Randomizasyon Nedir?]]
