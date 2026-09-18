---
Tür:
  - Besleyici
ODAK:
  - "[[Mikrobiyota]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Mikrobiyota, Genetik ve Epigenetik]]"
  - "[[KZYA Etkileri]]"
  - "[[Makrobesinlerin mikrobiyota üzerinden lipid metabolizmalarıyla ilişkileri]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Mikrobiyota ve Kişiselleştirilmiş Beslenme]]"
  - "[[KZYA Etkileri]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["Açlık Sinyali"] --> B{"Bazal İnsülin Düzeyi"}
>     B -->|Normoinsülinemi| C["FoxO1 Nükleer Translokasyonu → IRF4 Aktivasyonu"]
>     C --> D["ATGL & HSL Aktivasyonu → Yağ Asidi Mobilizasyonu (Lipoliz)"]
>     B -->|Kronik Hiperinsülinemi| E["FoxO1 Dışlanması → IRF4 Baskılanması"]
>     E --> F["Yağ Kilitlenmesi → Kas Proteolizi (Alanin Salınımı) → Glukoneojenez"]
> ```
>
> **Şekil Açıklaması:** Açlık sinyali karşısında bazal insülin düzeyi substrat partisyonunu belirler: Normoinsülinemide FoxO1/IRF4 ekseni üzerinden ATGL ve HSL aktive olarak lipoliz sağlanırken; kronik hiperinsülinemide IRF4 baskılanarak yağ dokusu kilitlenir ve glukoneojenez için iskelet kası proteolizi (kas kaybı) zorunlu hale gelir.

> **Metodolojik Etiketler:** #finding/contradictory
Mikrobiyota, insan gastrointestinal sisteminde yaşayan ve sayıları trilyonları bulan mikroorganizmaların oluşturduğu devasa topluluktur. Sağlıklı bir mikrobiyota yalnızca pasif bir "ortak yaşam" alanı değil; **ekolojik olarak karmaşık, işlevsel olarak yedekli (fonksiyonel yedeği olan) ve metabolik olarak birbirini tamamlayan dinamik bir ekosistemdir**.

Sağlıklı bir mikrobiyota; karbonhidratları, proteinleri, yağları, vitaminleri ve mineralleri vücudun en üst düzeyde emebileceği forma dönüştürür. Bağırsak bariyer bütünlüğünü korur, bağışıklık sistemini düzenler, zararlı patojenlere karşı koruma sağlar ve konakçı (insan) ile metabolik sinyalleşmeyi yönetir. Bu ekosistemin dengesinin bozulmasına ise **disbiyozis** denir. 

--------------------------------------------------------------------------------

**Baskın Filumlar, Aileler/Cinsler ve Öne Çıkan Metabolik Yollar**

Sağlıklı bir yetişkinin bağırsak mikrobiyotasının %90'ından fazlasını dört ana filum oluşturur: Firmicutes, Bacteroidetes, Actinomycetota ve Proteobacteria. Ayrıca ekolojik olarak çok kritik görevleri olan ikincil filumlar da (Verrucomicrobiota gibi) mevcuttur.

|Filum (Phylum)|Öne Çıkan Aile / Cinsler|Birincil Metabolik Yol ve İşlevler|Çıktılar (Metabolitler)|
|---|---|---|---|
|**Firmicutes**|_Faecalibacterium, Roseburia, Ruminococcus, Clostridium, Lactobacillus, Streptococcus_|**Bütirat Sentezi Yolağı:** Asetil-CoA → bütiril-CoA → bütirat yolağı ile lif fermantasyonu. _Clostridium scindens_ ise safra asitlerinin 7α-dehidroksilasyonunu yapar.|**Bütirat** (Kolonositlerin ana enerji kaynağı), İkincil safra asitleri (DCA, LCA), İndol-3-propiyonik asit (IPA).|
|**Bacteroidetes**|_Bacteroides_ (örn. _B. thetaiotaomicron_), _Prevotella_|**Polisakkarit Kullanım Lokusları (PULs):** Hem bitkisel hem de konakçı kaynaklı karmaşık glikanların (dirençli karbonhidratların) parçalanması.|Ağırlıklı olarak **Asetat (C2)** ve **Propiyonat (C3)**.|
|**Actinomycetota**|_Bifidobacterium_ (örn. _B. dentium, B. adolescentis_)|**Şeker/Glikoprotein Fermantasyonu ve Anne Sütü Oligosakkarit (HMO) Sindirimi:** Fruktoz-6P fosfoketolaz enzim yolağı. De novo vitamin sentezi yolları.|**Asetat, Laktat**, Folat (B9) ve Biyotin (B7) vitaminleri.|
|**Proteobacteria**|_Escherichia coli, Desulfovibrio, Bilophila wadsworthia_|**Siderofor Üretimi ve Sülfat İndirgeme:** Demir süpürücü (scavenger) yollar. Kükürt metabolizması (taurin solunumu). _E. coli_ için 'men' yolağı ile vitamin sentezi.|Hidrojen sülfür (H2S), **K2 Vitamini** (Menaquinone), Lipopolisakkarit (LPS).|
|**Verrucomicrobiota**|_Akkermansia muciniphila_|**Müsin Yıkımı (Glikokaliks metabolizması):** Bağırsak astarındaki müsini parçalayıp asetat ve propiyonata çevirerek müsin yenilenmesini tetikleme.|Asetat, Propiyonat, bariyer güçlendirici sinyaller.|

--------------------------------------------------------------------------------
### Tablo 2: Temsili Bağırsak Mikroorganizmaları: Keşif, Niş (Yaşam Alanı), Enzimler ve Besinsel Rolleri

|Organizma|Filum|Yıl (Keşif / Genomik)|Birincil Niş (Yaşam Alanı)|Temel Enzimler / Operonlar|Besin Yan Ürünleri / Konağa Etkisi|
|:--|:--|:--|:--|:--|:--|
|_**Streptococcus mutans**_|Firmicutes|1924|Ağız boşluğu (diş plağı)|Glukoziltransferazlar; Laktat dehidrogenaz|Sükroz $\rightarrow$ glukanlar (biyofilm), laktat (asidojenez)|
|_**Bifidobacterium dentium**_|Actinomycetota|1974|Ağız boşluğu; üst bağırsak|Karbonhidrat aktif enzimler; fruktoz-6P fosfoketolaz|Şekerlerin/glikoproteinlerin fermantasyonu $\rightarrow$ asetat, laktat|
|_**Bacteroides thetaiotaomicron**_|Bacteroidetes|1912 (Cins); 2003 (Genom)|Kolon|Polisakkarit Kullanım Lokusları (PULs; Sus sistemi)|Karmaşık glikanlar $\rightarrow$ asetat, propiyonat (metinden çıkarım)|
|_**Methanobrevibacter smithii**_|Euryarchaeota (Arkeler)|1982|Kolon (metanojen)|Metil-koenzim M redüktaz (mcrA)|H2 + CO2 $\rightarrow$ CH4 (Kısa zincirli yağ asidi (KZY) fermantasyon akışını destekler)|
|_**Clostridium sporogenes**_|Firmicutes|1908|Kolon|Triptofan indirgeme yolağı|Triptofan $\rightarrow$ indol-3-propiyonik asit (IPA)|
|_**Clostridioides difficile**_|Firmicutes|1935|Kolon (patobiyont)|p-HPA dekarboksilaz (HpdBCA)|Tirozin $\rightarrow$ p-kresol (bakteriyostatik etki; epitel stresi)|
|**_Desulfovibrio_ spp.**|Proteobacteria|1948 (Cins)|Kolon (sülfat indirgeyici)|Özümleyici olmayan sülfit redüktaz (dsrAB)|Sistein/taurin/sülfat $\rightarrow$ H2S (yüksek seviyelerde toksisite)|
|_**Bilophila wadsworthia**_|Proteobacteria|1989|Safra açısından zengin nişler|Sülfür metabolizması (taurin solunumu)|H2S; yüksek yağlı diyetlerde safraya adapte olmuş aşırı çoğalma|
|_**Clostridium scindens**_|Firmicutes|1984/85|Kolon (safra asidi uzmanı)|_bai_ operonu ($7\alpha$-dehidroksilasyon)|CA/CDCA (Birincil Safra Asitleri) $\rightarrow$ DCA/LCA (İkincil) (FXR/TGR5 sinyalizasyonu)|
|_**Akkermansia muciniphila**_|Verrucomicrobiota|2004|Mukus tabakası (kolon)|Müsin parçalayıcı enzimler; Amuc dış zar proteinleri|Bariyer desteği; iyileşmiş lipit/glikoz fenotipleri|
|_**Bifidobacterium adolescentis**_|Actinomycetota|1969|Kolon; gıda fermantleri|_fol/bio_ operonları; bazı suşlarda fitaz|Folat/biyotin biyosentezi; fitat hidrolizi|
|_**Lactobacillus plantarum**_|Firmicutes|1919|İnce bağırsak; gıda fermantleri|_rib_ operonu (riboflavin); BSH (Safra tuzu hidrolazı)|Riboflavin üretimi; safra tuzu dekonjugasyonu|
|_**Escherichia coli**_|Proteobacteria|1885|İnce/kalın bağırsak|_men_ yolağı; B12 taşıyıcısı (BtuBFCD)|K2 Vitamini (menakinon-8); kofaktör değişimi|
|_**Clostridium butyricum**_|Firmicutes|1880|Kolon; probiyotik suşlar|_cob/cbi_ operonları (anaerobik B12 biyosentezi)|Kobalamin (nadir görülen _de novo_ (sıfırdan) üretici)|
|_**Oxalobacter formigenes**_|Firmicutes (Betaproteobacteria)|1985|Kolon|Oksalil-CoA dekarboksilaz; formil-CoA transferaz|Oksalat $\rightarrow$ format + CO2 (kalsiyumu çökmeden korur)|
|**_Veillonella_ spp.**|Firmicutes (Negativicutes)|1898 (Cins)|Ağız boşluğu; bağırsak|Laktat kullanımı; nitrat indirgeme|Laktat $\rightarrow$ propiyonat; nitrat $\rightarrow$ nitrit (NO yolağı)|

_(Kısaltmalar: HPA: p-Hidroksifenilasetat, BSH: Safra tuzu hidrolazı, IPA: İndol-3-propiyonik asit, CA/CDCA: Kolik Asit/Kenodeoksikolik Asit, DCA/LCA: Deoksikolik Asit/Litokolik Asit)_

---

### Tablo 3: Disbiyozis Süreçlerinin Özeti: Normal ve Bozulmuş Mikrobiyal İşlevlerin Besin Ekseninde Karşılaştırılması

| Besin Ekseni        | Normal / Sağlıklı İşlev                                                                     | Disbiyotik Değişim (Bozulma)                                                                                 | Besinsel / Metabolik Sonuçlar                                                    | Hastalık Riski                                                     |
| :------------------ | :------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| **Karbonhidratlar** | Polisakkaritlerin dengeli yıkımı ve faydalı fermantasyon                                    | Sakarolitik fermantasyonun çökmesi; proteolizin ve basit şeker toplayıcılığının artması                      | Kısa Zincirli Yağ Asitlerinde (KZY/SCFA) düşüş, epitel hücrelerinde enerji açığı | Obezite, Kolorektal Kanser (CRC), İnsülin direnci                  |
| **Proteinler**      | Dengeli proteoliz; Triptofanın IPA/indollere dönüşümü (AhR aktivasyonu)                     | _C. difficile_ (p-kresol) artışı; Sülfat indirgeyen bakterilerde (H2S) artış; Triptofanın kinürenine kayması | Toksik metabolit birikimi; koruyucu indol sinyalizasyonunda azalma               | Kolit (bağırsak iltihabı), CRC, Duygudurum ve bilişsel bozukluklar |
| **Lipitler**        | BSH (Safra tuzu hidrolazı) ve _bai_ operonu ile safra asidi havuzunun dengelenmesi          | BSH üreten taksaların kaybı; toksik ikincil safra asitlerinde artış; cutC/D enzimleriyle TMAO artışı         | Misel stabilitesinde ve lipit/yağ emiliminde bozulma; toksik lipit metabolitleri | Kardiyometabolik hastalıklar (ASCVD), Mukoza hasarı, NAFLD         |
| **Mineraller**      | Fitaz ve oksalat yıkan mikropların, demir, çinko ve kalsiyumu emilim için serbest bırakması | Fitaz ve oksalat yıkan (örn. _O. formigenes_) mikropların kaybı                                              | Minerallerin emilememesi (şelatlanması)                                          | Anemi, Osteoporoz, Böbrek taşı (Nefrolitiyazis)                    |
| **Mikro Besinler**  | Nitratın Nitrik Okside (NO) dönüşümü; selenyumun selenoproteinlere dönüşümü                 | Nitrat indirgeyicilerin kaybı; selenyum metabolizma yolaklarının bozulması                                   | NO (Nitrik oksit) seviyelerinde düşüş; antioksidan savunmaların zayıflaması      | Hipertansiyon, Redoks (oksidatif stres) dengesizliği               |
**Bir Diyetisyenin Bu Bakteri İsimlerini Neden Bilmesi Gerekir?**

Klinik pratikte hastanın beslenme modelinin hangi bakterileri beslediğini veya hangi hastalık risklerini tetiklediğini anlamak için diyetisyenlerin bu kilit oyuncuları tanıması şarttır:

- **Bacteroides ve Prevotella (Bacteroidetes):** Diyetin ekolojik gücünü en iyi gösteren bakterilerdir. Batı tarzı, düşük lifli diyetlerle beslenenlerde _Prevotella_ azalır, sindirim zayıflar. Bu bakterilerin ürettiği propiyonat, karaciğerde glukoneogenezi düzenler. Diyetisyen, hastanın lif tüketiminin bağırsaklarda nasıl bir metabolik faydaya döneceğini bu bakteriler üzerinden kurgular.
- **Faecalibacterium prausnitzii ve Roseburia (Firmicutes):** Bu bakteriler bağırsağın "iltihap söndürücü (anti-inflamatuar)" itfaiye erleridir. Bağırsak hücrelerinin (kolonositlerin) birincil yakıtı olan **bütiratı** üretirler. Diyetisyen, hastaya dirençli nişasta ve fermente edilebilir lif verdiğinde aslında doğrudan bu bakterileri besleyerek sızdıran bağırsağı (leaky gut) tamir etmeyi ve insülin direncini kırmayı hedefler.
- **Bifidobacterium (Actinomycetota):** Anne sütü oligosakkaritlerini (HMO) sindirme yetenekleri sayesinde bebeklik döneminde kolonizasyonu başlatırlar. Ayrıca folat ve biyotin sentezlerler. Probiyotik ve prebiyotik stratejilerin merkezinde yer alırlar; laktat ve asetat üreterek ortamı asitlendirir ve Firmicutes'lerin bütirat üretmesi için gerekli hammaddeyi (çapraz beslenme) sağlarlar.
- **Akkermansia muciniphila (Verrucomicrobiota):** Mucizevi bir "bağırsak astarı" (müsin) bekçisidir. Sağlıklı yetişkinlerin bağırsağında %1-4 oranında bulunur. Müsini parçalayarak asetat ve propiyonat üretir, bu işlem hücreleri daha fazla müsin üretmeye teşvik ederek bağırsak bariyerini kalınlaştırır. Diyetisyenler için **obezite, tip 2 diyabet ve metabolik sendrom** yönetiminde hayati bir biyobelirteçtir; _Akkermansia_ eksikliği metabolik hastalıkların göstergesidir.
- **Escherichia, Desulfovibrio ve Bilophila wadsworthia (Proteobacteria):** Bu bakteriler bir diyetisyen için **"kırmızı alarm" (hastalık nöbetçileri)** görevi görür. Yüksek yağlı diyetlerde, safra salgısının artmasıyla _Bilophila wadsworthia_ gibi safra toleranslı türler hızla çoğalır. Proteobacteria türleri aşırı arttığında enflamasyona ve endotoksemiye (hücre duvarlarındaki LPS nedeniyle) yol açarlar. Ayrıca yüksek hayvansal protein/sülfat içeren diyetlerde H2S (hidrojen sülfür) üreterek bağırsak epiteline zehirli etki yapabilirler.
- **Clostridium scindens (Firmicutes):** Yağ ve yağda çözünen vitaminlerin (A, D, E, K) emilimini etkileyen safra asitlerini dönüştürür. Birincil safra asitlerini (CA, CDCA), ikincil safra asitlerine (DCA, LCA) dönüştürerek konağın yağ emilimi, enerji dengesi ve glukoz sinyalleşmesini (FXR ve TGR5 reseptörleri üzerinden) yönetir. Yüksek yağlı diyetlerde disbiozis oluşursa, bu bakterilerin ürettiği aşırı ikincil safra asitleri kanserojen etki yaratabilir.

1. Bağırsağın Mekansal (Spatial) Coğrafyası

**Bilimsel Temel:** Bağırsak tek tip bir boru veya homojen bir yaşam alanı değildir; mideden kolona (kalın bağırsağa) doğru ilerledikçe pH, oksijen seviyesi, besin mevcudiyeti ve geçiş süresi (transit time) dramatik şekilde değişir.

- **Üst Sindirim Yolu (Mide, Duodenum, Jejunum):** Burada pH düşüktür (asidiktir), oksijen yüksektir, geçiş çok hızlıdır ve hücreler safra asitlerine maruz kalır. Bu zorlu koşullarda mikrobiyal yük düşüktür (gram başına 102−104 hücre) ve sadece aside/oksijene dayanıklı _Lactobacillus_ ve _Streptococcus_ gibi fakültatif anaeroblar yaşayabilir.
- **Alt Sindirim Yolu (Kolon):** Oksijen tamamen tükenir, geçiş yavaşlar ve pH nötrleşir. Burası gram başına 1011 hücre ile dünyadaki en yoğun mikrobiyal popülasyona ev sahipliği yapar. Sıkı (obligat) anaeroblar olan _Bacteroides, Prevotella, Faecalibacterium_ ve _Roseburia_ gibi bakteriler burada devasa fermantasyon fabrikaları kurarak diyet liflerini kısa zincirli yağ asitlerine (SCFA) dönüştürürler.

**Diyetisyen Pratiğine Çıkarımlar:**

- **Probiyotik Seçimi ve Formülasyonu:** Hastanıza verdiğiniz probiyotiğin nerede çalışmasını istiyorsunuz? Eğer hedefiniz ince bağırsaktaki bir SIBO'yu (Aşırı Bakteri Çoğalması) baskılamak veya safra dekonjugasyonu sağlamaksa, üst yolda hayatta kalabilen _Lactobacillus_ suşlarını seçmelisiniz. Ancak hedefiniz kolondaki bütirat üretimini artırmak ve sızdıran bağırsağı onarmaksa, mide asidinde ölmeyecek şekilde "enterik kaplı" (bağırsağa açılan) kapsüller kullanmalı veya doğrudan kolon bakterilerini besleyen prebiyotik lifler (dirençli nişasta vb.) vermelisiniz.
- **Besin Emilimi Hedeflemesi:** Basit şekerler ve kolay sindirilen proteinler üst yolda hızla emilir ve kolondaki bakterilere ulaşmaz. Kolondaki faydalı bakterilerin açlıktan ölmemesi ve kendi bağırsak astarımızı (müsin) yememesi için, üst yolda sindirilmeyen, kolona kadar sapasağlam ulaşabilen "Makrobesinlere (MAC - Microbiota Accessible Carbohydrates)" yani kompleks liflere ihtiyaç vardır.

2. Çapraz Beslenme (Cross-Feeding/Syntrophy)

**Bilimsel Temel:** Bağırsaktaki hiçbir bakteri tek başına çalışmaz; birinin atığı (veya ürettiği metabolit), diğerinin birincil besinidir. Örneğin, birincil fermenterler olan _Bifidobacterium_ türleri oligosakkaritleri parçalayarak laktat ve asetat üretir. Ancak bu laktatın bağırsakta birikmesi asidoza yol açabilir. İşte burada ikincil fermenterler olan _Eubacterium rectale_ ve _Faecalibacterium prausnitzii_ devreye girerek ortamdaki asetat ve laktatı alır, bunları kolon hücrelerinin ana yakıtı olan "bütirat"a dönüştürürler. Aynı durum vitaminler için de geçerlidir; _Bifidobacterium adolescentis_ folat ve biyotin üretirken, _Lactobacillus plantarum_ riboflavin salgılar ve bu vitaminler diğer bakterilerin hayatta kalması için ortak havuzda paylaşılır.

**Diyetisyen Pratiğine Çıkarımlar:**

- **Çeşitlilik Çeşitliliği Doğurur:** Hastanıza sadece tek tip bir lif (örneğin sadece inülin) vermek, sadece tek bir bakteri grubunu besler ve ekosistemi tek tipleştirir. Farklı kimyasal yapılara sahip liflerin (pektinler, beta-glukanlar, fruktooligosakkaritler, dirençli nişasta) bir arada bulunduğu "gökkuşağı diyeti", çapraz beslenme ağını güçlendirir.
- **"Neden Sadece Bütirat İçeren İlaç/Takviye Vermiyoruz?" Sorusu:** Doğrudan bütirat takviyesi almak yerine (ki üst yolda emilip kaybolma veya kötü koku riski vardır), laktat ve asetat üreten bakterileri prebiyotiklerle besleyerek, bütiratı _doğrudan hedeflenen yerde (kolonda)_ ve sürekli olarak ürettirmek çok daha etkilidir.

3. Bakterilerin Ötesi: Arkealar, Virüsler ve Mantarlar

**Bilimsel Temel:** Mikrobiyom sadece bakterilerden oluşmaz; çok krallıklı (multi-kingdom) bir sistemdir.

- **Arkealar (Örn.** **Methanobrevibacter smithii****):** Yetişkin bağırsağında %0.1-2 oranında bulunur. Bakterilerin fermantasyon yaparken çıkardığı atık gazları (hidrojen ve karbondioksiti) alır ve metan gazına çevirir. Bu gaz temizliği, fermantasyonun yavaşlamasını engeller ve bakterilerin besinlerden _çok daha fazla kalori (enerji) elde etmesini_ sağlar.
- **Virüsler (Bakteriyofajlar):** Bağırsaktaki bakterilerden 10 kat daha fazladırlar (gram dışkıda 109 virüs). "Kazananı öldür" (kill-the-winner) stratejisiyle, çok fazla çoğalan tek bir bakteri türünü enfekte edip öldürerek popülasyon dengesini sağlarlar.
- **Mantarlar (Mikobiyom):** _Candida albicans_ ve _Saccharomyces cerevisiae_ gibi mantarlar bağışıklık sistemini modüle eder.

**Diyetisyen Pratiğine Çıkarımlar:**

- **Dirençli Kilo Verememe (Kilo Platosu) Durumları:** Bir hastanız diyetine harfiyen uymasına rağmen kilo veremiyorsa, bağırsağında metan üreten arkeaların (_M. smithii_) sayısının artmış olabileceğini göz önünde bulundurun. Bu arkealar, hastanın yediği liflerden "maksimum kalori" çekilmesini sağlayarak hastanın enerji alımını gizlice artırıyor olabilir. Bu hastalarda fermantasyon hızını değiştirecek karbonhidrat modifikasyonları (FODMAP kısıtlaması vb.) denenebilir.
- **Şeker-Mantar Döngüsü:** Rafine karbonhidrat ve şekerden zengin diyetler (veya bilinçsiz antibiyotik kullanımı), faydalı bakterileri azaltarak fırsatçı _Candida_ mantarlarının aşırı çoğalmasına yol açar. Bu durum hastada sürekli bir tatlı krizi, şişkinlik ve beyin sisi (brain fog) yaratabilir. Diyetisyenin görevi, antibiyotik sonrası dönemde sadece probiyotik vermek değil, mantarları besleyen basit şekerleri keserek ekosistemi yeniden inşa etmektir.

4. Enzimlerin Özelleşmiş Görevleri

**Bilimsel Temel:** Bakteriler, bizim genetiğimizde olmayan muazzam sindirim enzimlerine sahiptir.

- _Laktik asit bakterileri_ ve _B. adolescentis_, **mikrobiyal fitaz** enzimi salgılayarak bitkilerdeki fitik asidi parçalar ve hapsolmuş demir, çinko ve kalsiyumu serbest bırakır.
- _Oxalobacter formigenes_, sadece okzalatı parçalayan **okzalil-CoA dekarboksilaz** enzimine sahiptir. Bu enzim, okzalatı formata çevirerek kalsiyum ile birleşip böbrek taşı yapmasını (kalsiyum okzalat çökmesini) engeller.
- _Lactobacillus_ ve _Bifidobacterium_, **Safra Tuzu Hidrolazı (BSH)** enzimiyle safra asitlerini dekonjuge eder, bu da lipidlerin emilimini ve kandaki kolesterol seviyesini doğrudan etkiler.
- _Clostridium scindens_, **bai operonu** aracılığıyla 7α-dehidroksilasyon yaparak birincil safra asitlerini ikincil safra asitlerine çevirir ve hastanın FXR/TGR5 reseptörlerini uyararak glikoz-enerji metabolizmasını yönetir.

**Diyetisyen Pratiğine Çıkarımlar:**

- **Vegan/Vejetaryen Beslenmede Biyoyararlanım:** Tamamen bitkisel beslenen bir danışanınızın demir ve çinko depoları tükeniyorsa, sadece takviye vermek yeterli olmayabilir. Geleneksel hazırlama yöntemleri olan ıslatma, filizlendirme, çimlendirme ve ekşi maya (fermantasyon) kullanımı mikrobiyal fitaz aktivitesini uyarır. Hastaya bu mutfak tekniklerini öğreterek, mikrobiyotanın işini "tabakta" başlatabilirsiniz.
- **Böbrek Taşı (Kalsiyum Okzalat) Yönetimi:** Kalsiyum okzalat taşı olan bir hastaya "okzalattan fakir (ıspanak, pancar, çikolata vb. kısıtlaması) diyet" yazmak klasik bir yaklaşımdır. Ancak modern diyetisyenlik pratiğinde, bu hastaların bağırsağında okzalatı parçalayan _O. formigenes_ bakterisinin antibiyotik veya kötü diyetle yok olup olmadığı düşünülmeli, bağırsak ekolojisini (ve kalsiyum biyoyararlanımını) onaracak adımlar atılmalıdır.
- **Yağ Emilimi ve Yağda Çözünen Vitaminler:** Yüksek yağlı veya "Keto" tarzı diyetler uygulayan hastalarda _Bilophila wadsworthia_ gibi safra toleranslı patojenler artabilir. Aynı şekilde BSH enzim dengesi bozulduğunda, yağların ve yağda çözünen vitaminlerin (A, D, E, K) miçel oluşturup emilmesi zorlaşır. Emilim bozukluğu yaşayan hastalarda (kronik ishal, safra problemleri) önce mikrobiyom modülasyonu planlanmalıdır.
