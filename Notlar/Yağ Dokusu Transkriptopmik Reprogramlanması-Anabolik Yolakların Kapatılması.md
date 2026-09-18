---
Tür:
  - Besleyici
ODAK:
  - "[[Adipoz Doku]]"
MEKANİZMA:
DİZİN:
  - "[[Yağ Metabolizması]]"
  - "[[İnsülin Hassasiyeti]]"
  - "[[Notlar/Otofaji|Otofaji]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Açlıkta Adipoz Doku Lipolizi - Adrenerjik Sinyal, TNF-TNFR1 Ekseni ve Sirkadiyen Zamanlama]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Açlığın Adipoz Doku Üzerindeki Transkriptomik İmzası]]"
  - "[[Adipoz Doku Endokrin Fonksiyonu ve Dinamikleri]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Enerji Kısıtlaması / Açlık"] --> B["AMPK Aktivasyonu"]
>     B -->|Katabolik Sinyal| C["Lipoliz ve Yağ Oksidasyonu"]
>     B -->|Geri Bildirim| D["TBK1 İndüksiyonu"]
>     D -.->|İnhibisyon / Fren| B
>     E["Kronik Düşük Dereceli İnflamasyon"] -->|Sürekli Yüksek| D
> ```
>
> **Şekil Açıklaması:** Enerji kısıtlaması veya açlıkta aktive olan AMPK, lipoliz ve yağ oksidasyonunu uyarırken aynı zamanda TBK1 indüksiyonunu tetikleyerek negatif bir geri bildirim freni oluşturur; kronik düşük dereceli inflamasyon varlığında ise TBK1 sürekli yüksek kalarak AMPK'yi baskılar ve katabolik yağ yıkımını kilitler.

### İçindekiler

- [[#Lipojenez ve Trigliserid Sentezi]]
- [[#Glikoliz ve Kolesterol Sentezi]]
- [[#İnsülin Sinyali ve PPAR Sinyali Ayrışan İki Yolak]]
- [[#TCA Döngüsü ve Oksidatif Fosforilasyon]]
- [[#Proteazomal Degradasyon ve Otofaji]]
- [[#Ekstraselüler Matriks ve Kollajen Genleri]]
- [[#Genel Değerlendirme]]
- [[#Bibliyografya]]

---

### Lipojenez ve Trigliserid Sentezi

Açlığın adipoz dokudaki transkriptomik imzası, ilk bakışta basit bir "anabolizmayı kapat" komutu gibi görünüyor. Ama Defour et al. (2020)'un insan-fare karşılaştırması, bu kapanmanın hangi yolaklarda **evrensel bir refleks**, hangilerinde ise **türe özgü bir tercih** olduğunu ayırt etmemizi sağlıyor — ve bu ayrım, fare çalışmalarından insana genelleme yaparken nerede temkinli olunması gerektiğine dair somut bir harita sunuyor.

**Normal Fizyoloji:** Beslenmiş durumda, insülin-SREBP1 ekseni üzerinden yağ asidi ve trigliserid sentezi (lipojenez) aktif tutulur. Anahtar genler arasında FASN, ACACA, DGAT1/DGAT2, ELOVL6 (uzatma), THRSP (Spot14) ve transkripsiyon faktörü SREBF1 (SREBP1) yer alır.

**Açlıkta Ne Değişir:** Bu yolak, insan-fare karşılaştırmasında en tutarlı biçimde **konserve** bulunan modüllerden biri. _FASN, ACLY, DGAT2, THRSP_ ve _SREBF1_ iki türde de açlıkla baskılanıyor; ortak baskılanan 173 genlik listenin EnrichR analizinde "triglyceride and fatty acid synthesis" en güçlü enrichment gösteren temalardan biri. Ancak **şiddet** düzeyinde büyük fark var — kat-değişimi (fold-change) neredeyse her zaman farede çok daha keskin. Örneğin _FASN_ ve _THRSP_ iki türde de düşüyor, ama farede düşüş kat be kat daha belirgin. Bu, "yön aynı, büyüklük farklı" örüntüsünün klasik bir tezahürü — derlemenin genelinde tekrar eden bir motif.

---

### Glikoliz ve Kolesterol Sentezi

**Normal Fizyoloji:** Glikoliz genleri (HK2, PFKFB1, PFKFB3 gibi) glukozun hücre içi yakalanması ve parçalanmasını; kolesterol sentez yolağı (HMGCS2'nin ketogenik kolu dışında, mevalonat yolağı genleri) hücresel kolesterol üretimini yönetir.

**Açlıkta Ne Değişir:** Glikoliz ve kolesterol sentezi de 173 genlik konserve baskılanma listesinde güçlü şekilde temsil ediliyor — EnrichR'da "Cholesterol Biosynthesis Pathway," "Mevalonate pathway" ve glikoliz/TCA temaları en yüksek enrichment skorlarına sahip. Ama burada da tür-içi ayrışan istisnalar var: glikojen/gliserol-fosfat metabolizmasının iki geni, GPD1 (gliserol-3-fosfat dehidrogenaz 1) ve PYGB (glikojen fosforilaz B), farede açlıkla belirgin şekilde baskılanırken insanda **neredeyse hiç değişmiyor**. Bu, "genel yön konserve ama belirli düğüm noktaları türe özgü" ilkesinin bir başka örneği — ve aşağıda ele alınan PCK1 farkıyla doğrudan bağlantılı (bkz. Sistemik Enerji Metabolizması).

---

### İnsülin Sinyali ve PPAR Sinyali: Ayrışan İki Yolak

**Normal Fizyoloji:** İnsülin sinyali, IRS1 üzerinden glukoz alımını ve anabolik programı destekler; IRS2 farklı bir işlevsel dala (özellikle lipolizin insülin tarafından baskılanmasına) aracılık eder. PPAR ailesi (PPARA, PPARD, PPARG) yağ asidi metabolizması ve adipogenez ile ilgili çok sayıda hedef geni düzenler.

**Açlıkta Ne Değişir:** Bu iki yolak, Defour'un ΔSLR (insan-fare SLR farkı) analizinde tam ters yönlerde öne çıkıyor. **İnsülin sinyal yolağı** (AMPK ve FOXO ile birlikte), ΔSLR>1 grubunda güçlü enrichment gösteriyor — yani bu yolak **farede çok daha güçlü baskılanıyor**, insanda ya hiç baskılanmıyor ya da çok hafif kalıyor. _IRS1_ her iki türde de aynı yönde (aşağı) değişse de, yolağın bütünü insanda büyük ölçüde korunuyor. Buna karşılık **PPAR sinyali ve yağ asidi biyosentezi**, ΔSLR<-1 grubunda öne çıkıyor — yani **farede güçlü indükleniyor, insanda ya değişmiyor ya da zayıf kalıyor**. PPAR hedef genlerinin bu farklı davranışı, reseptör ekspresyon düzeyindeki bir farktan kaynaklanmıyor — PPARA/PPARD/PPARG bazal ekspresyonu iki türde benzer. Dikkat çekici bir istisna: **_PPARG_ mRNA'sı açlıkla insanda düşerken farede değişmiyor** — reseptörün kendisi bir hedef gen gibi davranan tek örnek. Sonuç olarak insülin sinyalinin baskılanması "fare-ağırlıklı" bir yanıt, PPAR aktivasyonu ise "fare-özel" bir yanıt gibi görünüyor; ikisi birlikte, fare adipoz dokusunun açlığa insan dokusundan çok daha "agresif" bir transkripsiyonel reprogramlama ile yanıt verdiği genel örüntüyü pekiştiriyor.

---

### TCA Döngüsü ve Oksidatif Fosforilasyon

**Normal Fizyoloji:** Mitokondriyal TCA döngüsü ve oksidatif fosforilasyon (OXPHOS), hücrenin ATP üretim merkezidir; adipoz dokuda bu yolakların aktivitesi kısmen lipojenez için gereken redükleyici eşdeğerlerin (NADPH) üretimiyle de bağlantılıdır.

**Açlıkta Ne Değişir:** Bu yolak da konserve baskılanan 173 genlik listede güçlü temsil buluyor — TCA döngüsü genleri hem insan hem fare adipoz dokusunda açlıkla tutarlı biçimde düşüyor. Bu bulgu, Suchacki et al. (2023)'ün **karaciğerde** bulduğu tabloyla ilginç bir tezat oluşturuyor: orada CR, TCA/OXPHOS aktivitesini erkeklerde **artırıyor** (dişilerde değil) — ama bu karaciğer, farklı bir doku ve farklı bir metabolik rol (glukoneogenez merkezi). Adipoz dokuda TCA'nın basitçe kapanması, karaciğerin TCA'yı seçici biçimde yeniden yönlendirmesinden temelde farklı bir stratejiyi yansıtıyor — aynı yolağın farklı dokularda açlığa taban tabana zıt yönde yanıt verebileceğinin somut bir hatırlatıcısı.

---

### Proteazomal Degradasyon ve Otofaji

**Normal Fizyoloji:** Proteazom, hasarlı/gereksiz proteinlerin ubikitin-bağımlı yıkımını yürütür; otofaji (ATG genleri, GABARAP ailesi) ise daha büyük hücresel bileşenlerin (organeller, protein agregatları) lizozomal yıkımını sağlar.

**Açlıkta Ne Değişir:** İnsan sWAT'ında proteazomal genlerin geniş bir seti açlıkla anlamlı şekilde baskılanıyor (GSEA ile doğrulanmış); yazarlar bunu, lipolizi ve diğer temel adiposit işlevlerini desteklemek için değerli proteinlerin yıkımdan korunması olarak yorumluyor. **Bu, mevcut veride farede doğrudan gösterilmiş bir bulgu değil** — konserve 173 genlik listede proteazom teması yer almıyor; dolayısıyla bu bulguyu insana özgü olarak ele almak, iki türde ortak olduğunu varsaymaktan daha isabetli. Otofaji tarafında ise genel bir aktivasyon **yok** — çoğu ATG geni değişmiyor; yalnızca **GABARAPL1** ve **DAPK2** güçlü şekilde indükleniyor. Yazarlar, otofajinin adipoz dokuda trigliserid hidrolizindeki rolünün hâlâ kanıtlanmamış olduğunu vurguluyor — yani "açlık = otofaji açılır" genellemesi, en azından adipoz doku düzeyinde, bu veriyle desteklenmiyor.

---

### Ekstraselüler Matriks ve Kollajen Genleri

**Normal Fizyoloji:** Adipoz dokunun ekstraselüler matriksi, kollajen ağı (COL genleri) aracılığıyla dokunun yapısal bütünlüğünü ve adipositlerin genişleme/büzülme kapasitesini destekler.

**Açlıkta Ne Değişir:** Kollajen kodlayan genler (COL11A1, COL15A1, COL5A1, COL5A3, COL3A1) iki türde de tutarlı biçimde baskılanıyor. Yazarlar bunu, lipoliz sırasında adipositlerin küçülmesine (shrinkage) eşlik eden yapısal bir yeniden düzenleme olarak yorumluyor — bariatrik cerrahi sonrası yağ kaybında görülen kollajen kompozisyon değişiklikleriyle (Liu et al. 2016) paralellik kuruluyor. Bu, açlığın yalnızca metabolik değil, dokunun fiziksel mimarisini de yeniden şekillendiren bir süreç olduğunu gösteriyor.

---

### Genel Değerlendirme

Bu not tek bir kaynağa (Defour et al. 2020) dayandığı için protokol-tipi (TRF/ADF/CR) veya süre ekseninde bir karşılaştırma yapmak mümkün değil — burada tek bir "doz" var: insanda 26 saat, farede 16 saat, ikisi de tek-seferlik açlık (kronik tekrar yok). Bu, Sistemik Enerji Metabolizması notundaki Cagigas verisiyle (10 günlük kronik açlık) doğrudan karşılaştırılabilecek bir süre eşleşmesi sunmuyor — biri transkriptomik anlık görüntü, diğeri metabolomik uzun-vadeli adaptasyon. Diyet kompozisyonu burada da sabit (standart chow, insan tarafında standardize tek öğün) — yüksek yağ/fruktoz diyetinin bu yolakları nasıl değiştirebileceği test edilmemiş. En önemli çıkarım tür ekseninde: **yön çoğunlukla korunuyor, şiddet ve bazı düğüm noktaları (PCK1, PPARG, GPD1/PYGB, proteazom) türe özgü**. Bu, "farede kanıtlandı" ifadesinin insana otomatik genellenemeyeceğinin somut bir gerekçesi — özellikle PPAR sinyali ve insülin sinyali gibi terapötik hedef olarak öne çıkan yolaklarda.

---

### Bibliyografya

- Defour M, Michielsen CCJR, O'Donovan SD, Afman LA, Kersten S. (2020). Transcriptomic signature of fasting in human adipose tissue. _Physiological Genomics_ 52:451–467.