---
Tür:
  - Besleyici
ODAK:
  - "[[Adipoz Doku]]"
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
  - "[[Adipoz Doku, Enerji Kısıtlamasında Yağ Yıkımını Azaltmak için Sinyaller (TBK1) Üretiyor]]"
  - "[[İnsülin–IRF4 Ekseni Açlıkta Yağ mı Kas mı Kaybedilir?]]"
  - "[[Kilo Döngüsü ve İmmün Hafıza]]"
  - "[[Otofaji]]"
  - "[[Hiperinsülinemi Açlık için Bir Fren Olabilir!]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "null"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "p > 0.05 (anlamsız)"
BESLEDİĞİ NOTLAR:
  - "[[Adipoz Doku Lipolizi]]"
  - "[[Adipoz Doku, Enerji Kısıtlamasında Yağ Yıkımını Azaltmak için Sinyaller (TBK1) Üretiyor]]"
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

> **Metodolojik Etiketler:** #finding/null
---

## İçindekiler
- [[#Normal Fizyoloji]]
- [[#Açlıkta Ne Değişir]]
- [[#Çapraz-Tema Başlıkları]]
  - [[#İnflamasyon ↔ Metabolik Fren Kilitlenmesi]]
  - [[#Plazma ↔ Doku Ayrışması]]
  - [[#Depot-Spesifiklik]]
  - [[#Protokol Dozu ↔ Doku Yanıt Eşiği]]
  - [[#Genotip x Tedavi Etkileşimi]]
  - [[#Terapötik Co-Targeting Mantığı]]
- [[#Genel Değerlendirme]]
- [[#Bibliyografya]]

---

## Normal Fizyoloji

Adipositte enerji dengesi, hücre içi AMP/ATP oranını sürekli izleyen AMPK üzerinden yönetilir. Beslenmiş (fed) durumda, düşük AMP/ATP oranı ve yüksek insülin sinyali AMPK'yı büyük ölçüde inaktif tutar; bu da lipogenezin serbestçe ilerlemesine, lipoliz genlerinin (*Pnpla2/ATGL*, *Lipe/HSL*) baskılı kalmasına ve enerjinin trigliserid olarak depolanmasına izin verir. Bu tokluk durumunda TBK1 (TANK-binding kinase 1) de düşük bazal aktivitede seyreder; TBK1 klasik olarak innate immün sinyalizasyonla (virüs/patojen algılama, IRF3 fosforilasyonu) ilişkilendirilse de, adipoz dokuda ayrıca nutrient-duyarlı bir rol üstlenir — ancak bu rol yalnızca AMPK aktive olduğunda devreye girer, dolayısıyla fed durumda "sessiz" kalır.

Bu iki kinaz arasındaki ilişki, aslında bir güvenlik mekanizmasıdır: AMPK, enerji stresine yanıt olarak katabolik bir program (lipoliz, yağ asidi oksidasyonu, mitokondriyal biyogenez) başlattığında, bu programın kontrolsüz şekilde devam edip enerji rezervini tüketmesini önleyecek bir "kendini sınırlama" devresine ihtiyaç vardır. TBK1, işte bu devrenin geç-devreye-giren freni olarak konumlanır.

---

## Açlıkta Ne Değişir

Açlık başladığında AMP/ATP oranı yükselir ve AMPK, Thr172 kalıntısı üzerinden fosforillenerek aktive olur. Bu aktivasyon 24-48 saatlik açlıkta hem inguinal (iWAT) hem epididimal (eWAT) yağ dokusunda güçlü şekilde gözlenir ve downstream hedefleri (pS79 ACC, pS555 ULK1, pS792 Raptor) üzerinden lipolizi ve otofajiyi tetikler (Wisessaowapak et al. 2026).

Burada devreye giren ikinci katman, AMPK'nın **transkripsiyonel** bir programı da harekete geçirmesidir: AMPK, koaktivatörü PGC1a üzerinden NRF1 (nuclear respiratory factor 1) ile birlikte çalışarak *Tbk1* geninin promotöründeki NRF1 bağlanma motifine bağlanmasını sağlar (ChIP-qPCR ve luciferase reporter deneyleriyle doğrulanmıştır). Bu, *Tbk1* mRNA'sının stabilitesinde değil, doğrudan transkripsiyonunda bir artış yaratır — aktinomisin D deneyleri mRNA yarı ömründe değişiklik olmadığını, sikloheksimid deneyleri ise de novo protein sentezinin (muhtemelen NRF1 veya bir aracı faktörün yeniden üretimi) gerekli olduğunu göstermiştir.

Bu zincirin kritik özelliği **zamanlamasıdır**: AMPK'nın posttranslasyonel aktivasyonu açlığın ilk saatlerinde (0-12 saat) gerçekleşen hızlı bir yanıtken, *Tbk1* transkripsiyonel indüksiyonu 24-48 saatte belirginleşen **gecikmeli bir adaptif kontrol noktasıdır**. Yani TBK1, açlığın "erken alarm sistemi" değil, "uzun süreli açlığa karşı frenleme mekanizmasıdır" — enerji deposunun aşırı tükenmesini önlemek üzere devreye girer. Aktive olan TBK1 (p-Ser172), bir fosforilasyon kaskadı yoluyla AMPK aktivitesini baskılayarak devreyi kapatır; *Tbk1*<sup>AKO</sup> (adiposit-spesifik TBK1 nakavt) farelerde bu fren kaldırıldığında, AMPK sinyali (pT172 AMPK, pS79 ACC, pS792 Raptor) WT'ye kıyasla çok daha yüksek ve **sürdürülebilir** kalır — yani fren, hem aktivasyonun tepe noktasını hem de süresini sınırlamaktadır.

---

## Çapraz-Tema Başlıkları

### İnflamasyon ↔ Metabolik Fren Kilitlenmesi

Obezite bu devreyi köklü şekilde bozar, ancak bunu AMPK'yı doğrudan hedefleyerek değil, **TBK1'in bazal düzeyini kronik olarak yükselterek** yapar. TBK1, obezitede kronik düşük dereceli inflamasyona bağlı olarak zaten yüksek bazal ekspresyon ve fosforilasyon (p-Ser172) göstermektedir — bu, TBK1'in klasik innate immün/inflamatuar rolüyle örtüşen bir özelliğidir. Sonuç olarak obez farelerde açlık, TBK1'i *daha da* indükleyemez (tavan etkisi), ve zaten yüksek olan TBK1 aktivitesi AMPK'yı tonik olarak baskılamaya devam eder. Bu, yağsız farelerde gözlenen güçlü açlık-AMPK aktivasyonunun obez farelerde büyük ölçüde köreldiği anlamına gelir; hatta farmakolojik AMPK agonisti AICAR (500 mg/kg) bile obez farelerde AMPK'yı yeterince aktive edememektedir — kronik TBK1 yüksekliği, AMPK aktivasyonunu doğrudan antagonize etmektedir. Bu bulgu, inflamasyonun yalnızca insülin direncini değil, **AMPK sinyaline direnci de** (bir tür "AMPK resistance") tetikleyebileceğini göstermesi bakımından önemlidir; mekanizma insülin reseptörü düzeyinde değil, doğrudan bir kinaz-kinaz feedback döngüsü üzerinden işlemektedir.

### Plazma ↔ Doku Ayrışması

Bu çalışma, sistemik (vücut ağırlığı) ve doku düzeyi (yağ kütlesi) yanıtlarının obezitede birbirinden ayrıştığını göstermektedir: yağsız fareler açlıkta belirgin vücut ağırlığı, iWAT, eWAT ve karaciğer kütle kaybı yaşarken, obez fareler bu kayıplara büyük ölçüde direnç göstermektedir — yani obezitede "adaptif direnç" yalnızca metabolik parametrelerde değil, doğrudan doku kütle kaybında da ortaya çıkmaktadır. Korelasyon analizleri bunu sayısal olarak da destekler: yağsız farelerde pT172 AMPK düzeyi, vücut ağırlığı kaybının büyüklüğüyle güçlü korelasyon gösterirken (R²=0.18) ve eWAT kütlesiyle ters korelasyon (R²=0.40) sergilerken, obez farelerde bu ilişkiler belirgin şekilde zayıflamaktadır (eWAT için R²=0.041, anlamsız).

### Depot-Spesifiklik

Fasting yanıtının büyüklüğü ve TBK1 indüksiyonunun derinliği, iWAT ve eWAT depoları arasında farklılık göstermektedir; her iki depo da açlıkla *Tbk1*, TBK1 protein ve p-Ser172 TBK1 artışı sergilese de, bu artışın kinetiği ve obezitede bozulma derecesi depo bazında değişkenlik taşır. Tek hücre RNA-seq verileri, obez farelerin hem eWAT hem iWAT adipositlerinde yüksek bazal *Tbk1* ekspresyonunu doğrulamakta; insan biyopsi verileri ise bu depot-spesifik örüntünün hem subkutan hem viseral dokuda BMI ile paralel şekilde arttığını göstererek bulguyu insana taşımaktadır.

### Protokol Dozu ↔ Doku Yanıt Eşiği

Bu mekanizma net bir doz-yanıt ve süre-yanıt ilişkisi sergilemektedir. Akut açlıkta 24 saat ile 48 saat arasında *Tbk1* indüksiyonu kademeli olarak artmakta; farmakolojik ajanlarda da benzer bir eşik etkisi görülmektedir — tek başına AMPK aktivasyonu (AICAR) kompansatuar TBK1 artışını tetiklediğinden sınırlı etkili kalırken, sub-optimal dozda TBK1 inhibisyonu (amlexanox, 25 mg/kg) ile AMPK aktivasyonunun (AICAR, 100 mg/kg) **kombinasyonu**, tek ajanlardan çok daha güçlü ve daha erken başlayan (gün 14 vs gün 18) bir yanıt üretmektedir. Bu, "frenin kaldırılması" ile "gaza basılması"nın ayrı ayrı sınırlı, birlikte ise sinerjik olduğu bir eşik/kapasite ilişkisine işaret etmektedir.

### Genotip x Tedavi Etkileşimi

Üç farklı adiposit-spesifik nakavt modeli ($Prkaa1/2^{AKO}$, $Tbk1^{AKO}$, $Ppargc1a^{AKO}$) bu devrenin her bir bileşeninin zorunlu olduğunu göstermektedir: AMPK olmadan açlık *Tbk1*'i indükleyemez; PGC1α olmadan hem açlık hem AICAR *Tbk1*'i artıramaz; TBK1 olmadan AMPK sinyali baskılanamaz ve fren ortadan kalkar. Bu üçlü epistatik ilişki, devrenin doğrusal ve zorunlu bir zincir (AMPK→PGC1α→NRF1→TBK1⊣AMPK) olduğunu, herhangi bir düğümün eksikliğinin tüm devreyi durdurduğunu göstermektedir.

### Terapötik Co-Targeting Mantığı

Bu mekanizmanın en pratik çıkarımı, tek-ajan AMPK aktivasyonunun (örn. metformin benzeri stratejiler veya AICAR-tipi ajanlar) obezitede neden sınırlı etkili kaldığına dair bir açıklama sunmasıdır: AMPK aktivasyonu kendi kompansatuar frenini (TBK1) tetiklediği için, tek başına sürdürülebilir bir enerji harcaması sağlayamaz. TBK1/IKKε inhibisyonu (amlexanox) ile AMPK aktivasyonunun birlikte uygulanması, bu kendi kendini sınırlayan döngüyü kırarak kilo kaybı, glukoz toleransı, hepatik yağlanma ve adipoz doku inflamasyonu (crown-like structure sayısı) üzerinde belirgin sinerji yaratmaktadır.

---

## Genel Değerlendirme

Bu kaynak, "açlık" kavramını değil, **akut/farmakolojik enerji stresi** paradigmasını incelemektedir — TRF, ADF veya 5:2 gibi tekrarlayan davranışsal protokoller değil, tek seferlik 24-72 saatlik su açlığı veya AICAR/amlexanox ile farmakolojik taklit kullanılmıştır. Süre ekseninde veri yalnızca akut aralığı (24-72 saat) ve kronik farmakolojik tedaviyi (2-3 hafta) kapsamakta; haftalar-aylar süren tekrarlayan aralıklı oruç protokollerinin bu devre üzerindeki etkisi bu çalışmada test edilmemiştir — bu, İnsülin-IRF4 Ekseni notunda ele alınan 10 haftalık 5:2 IF modelleriyle doğrudan karşılaştırılabilir bir veri sunmadığı anlamına gelir.

Diyet kompozisyonu açısından çalışma, standart chow/normal diyet (ND) ile %60 yağ içerikli HFD karşılaştırmasına dayanmaktadır; bu karşıtlık, mekanizmanın obezite tarafından nasıl "kilitlendiğini" göstermek için güçlü bir tasarımdır, ancak fruktoz veya orta-düzey diyet kompozisyonu varyasyonlarına dair veri yoktur.

Bireysel faktörler açısından en belirgin sınırlılık, çalışmanın yalnızca erkek fareleri kullanmasıdır (fenotipik varyasyonu azaltmak gerekçesiyle) — bu nedenle cinsiyet farkına dair hiçbir çıkarım yapılamaz. Yaşlanma değişkeni test edilmemiştir. Tür açısından ise fare bulguları, insan biyopsi/scRNA-seq verisiyle (BMI ile TBK1 ekspresyonu ilişkisi) korelatif düzeyde desteklenmiş, ancak insanda müdahale (klinik deney) düzeyinde doğrulanmamıştır — dolayısıyla bu mekanizmanın insan açlık fizyolojisine ne ölçüde genellenebileceği hâlâ açık bir sorudur.

---

## Bibliyografya

- Wisessaowapak, C. et al. (2026). A nutrient-responsive AMPK/TBK1 circuit restricts adipocyte catabolism. *JCI Insight*, 11(9):e200168. Wisessaowapak et al. 2026