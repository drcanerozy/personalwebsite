---
Tür:
  - Besleyici
ODAK:
  - "[[İstatistik]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[İki Grup Karşılaştırması için ANOVA Kullanmak?]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[Biyoistatistik]]"
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[SEM_Mediation_Moderation_Rehberi]]"
  - "[[Olcek_Uyarlama_Istatistik_Rehberi]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["GLP-1 Reseptör Agonizmi"] --> B["Santral İştah Baskılanması (POMC/CART)"]
>     A --> C["Gastrik Boşalmada Yavaşlama"]
>     B & C --> D["Spontan Kalori Kısıtlaması & Hızlı Kilo Kaybı"]
>     D --> E{"Yetersiz Protein & Direnç Egzersizi Yokluğu"}
>     E -->|Miyosteatoz & Katabolizma| F["İskelet Kası Kaybı (Sarkopenik Obezite)"]
>     E -->|Yüksek Protein & Egzersiz| G["Yağsız Kas Kütlesinin Korunması"]
> ```
>
> **Şekil Açıklaması:** GLP-1 reseptör agonizminin sağladığı santral iştah baskılanması ve gecikmiş gastrik boşalma hızlı kilo kaybı yaratır. Bu süreçte yetersiz protein alımı ve direnç egzersizi yokluğu miyosteatoz ve iskelet kası kaybına (sarkopenik obezite) yol açarken; hedefe yönelik yüksek protein ve direnç antrenmanı yağsız dokuyu korur.

> **Metodolojik Etiketler:** #finding/contradictory
MR, bir maruziyetin (örneğin, plazmadaki belirli bir besin ögesi seviyesi) bir sonuç (örneğin, kronik bir hastalık) üzerinde **nedensel** bir etkisi olup olmadığını araştırmak için genetik varyantları (SNP'ler 💎 gibi) 'araç' olarak kullanan bir epidemiyolojik yöntemdir.

Temel fikri, doğanın bize bir tür 'rastgele kontrollü deneme' (RCT) sunmasıdır. Tıpkı bir RCT'de katılımcıların rastgele olarak 'tedavi' veya 'kontrol' grubuna atanması gibi, bireyler de ebeveynlerinden rastgele bir şekilde genetik varyantlar alırlar. Bu genetik varyantlar, ömür boyu belirli bir maruziyete (örneğin, daha yüksek LDL kolesterol seviyelerine) eğilimli olmamıza neden olabilir.

MR'ın en büyük gücü, geleneksel gözlemsel çalışmalarda (kesitsel, kohort vb.) karşılaştığımız **karıştırıcı faktörler (confounding)** ve **tersine nedensellik (reverse causation)** gibi temel sorunların üstesinden gelmeye yardımcı olmasıdır.

Bu konuyu nasıl derinleştirmek istersiniz? Size rehberlik etmem için birkaç başlangıç noktası önerebilirim:

1. **MR'ın Temel Varsayımları:** Bir genetik varyantın 'geçerli bir araç' (instrumental variable) olması için hangi üç temel koşulu sağlaması gerektiğini ve bu koşullar ihlal edildiğinde ne olacağını inceleyebiliriz.
    
2. **Beslenme Alanından Örnekler:** Bu yöntemin sizin alanınızda (örneğin, vitamin D seviyeleri ve kanser riski veya alkol tüketimi ve kardiyovasküler hastalıklar arasındaki nedensel ilişki) nasıl kullanıldığına dair somut çalışmalara bakabiliriz.
    
3. **MR Türleri ve Analizi:** "Tek örneklemli" (one-sample) ve "iki örneklemli" (two-sample) MR arasındaki farkların ne olduğunu ve bu analizlerin pratikte nasıl yapıldığını konuşabiliriz.

**1. MR'ın Temel Varsayımları**.

Mendelian Randomizasyon'un (MR) merkezinde, kullandığımız genetik varyantın (genellikle bir SNP) geçerli bir "araç" (Instrumental Variable - IV) olması fikri yatar. Bir aracın geçerli sayılması için karşılaması gereken, birbiriyle bağlantılı üç katı kural vardır.

Bu kuralları bir üçgen olarak düşünebiliriz:

- **A Köşesi:** Genetik Araç (SNP 🧬)
    
- **B Köşesi:** Maruziyet (Örn: D Vitamini Seviyesi ☀️)
    
- **C Köşesi:** Sonuç (Örn: Hastalık Riski 🩺)
    

İşte bu üçgenin sağlam durması için gereken 3 temel varsayım:

### 1. İlgi Varsayımı (The Relevance Assumption)

- **Ne anlama gelir?** Genetik araç (A 🧬), araştırdığımız maruziyet (B ☀️) ile **güçlü** bir şekilde ilişkili olmalıdır.
    
- **Neden önemlidir?** Eğer SNP'niz, ilgilendiğiniz D vitamini seviyesini zar zor etkiliyorsa, o SNP'yi bir araç olarak kullanmak zayıf ve güvenilmez sonuçlar verir. Tıpkı bir vidayı gevşek bir tornavidayla sıkmaya çalışmak gibi.
    
- **Kontrolü:** Bu, genellikle Geleneksel Gözlemsel Çalışmalarda (GWAS gibi) istatistiksel olarak (F-istatistiği > 10 gibi) kontrol edilir.
    

### 2. Bağımsızlık Varsayımı (The Independence Assumption)

- **Ne anlama gelir?** Genetik araç (A 🧬), sonucu (C 🩺) etkileyebilecek **karıştırıcı faktörlerden** (confounders) bağımsız olmalıdır.
    
- **Neden önemlidir?** Örneğin, hem D vitamini seviyesini (B ☀️) hem de hastalık riskini (C 🩺) etkileyen bir faktör düşünelim (mesela sosyoekonomik durum veya fiziksel aktivite). Eğer bizim seçtiğimiz genetik araç (A 🧬), bu karıştırıcı faktörle de ilişkiliyse (örn. belirli bir genetik varyant, kişilerin daha az dışarı çıkmasına neden oluyorsa), o zaman MR'ın tüm amacı bozulur.
    
- **Kontrolü:** Genetik araçların, bilinen karıştırıcı faktörlerle ilişkili olup olmadığına bakılarak kısmen kontrol edilebilir.
    

### 3. Dışlama Kısıtlaması Varsayımı (The Exclusion Restriction)

- **Ne anlama gelir?** Bu en kritik varsayımdır. Genetik araç (A 🧬), sonucu (C 🩺) **yalnızca ve yalnızca** bizim ilgilendiğimiz maruziyet (B ☀️) üzerinden etkileyebilir.
    
- **Neden önemlidir?** Eğer genetik aracın, maruziyetten bağımsız olarak sonuca giden "ikinci bir yolu" varsa, buna **pleiotropi** denir.
    
- **Örnek:** Seçtiğimiz SNP (A 🧬), evet D vitamini seviyesini (B ☀️) etkiliyor olabilir. Ama _aynı zamanda_, D vitamininden _bağımsız_ olarak, doğrudan hücre çoğalmasını (C 🩺) da etkileyen başka bir mekanizmayı tetikliyorsa (pleiotropi), o zaman genin sonuç üzerindeki toplam etkisinin ne kadarının D vitamininden, ne kadarının bu ikinci yoldan geldiğini bilemeyiz.
    
- **Kontrolü:** İstatistiksel yöntemlerle (örn: MR-Egger, Weighted Median) pleiotropi test edilmeye çalışılır.

### Örnek 1: Süt Tüketimi ve Kemik Sağlığı 🥛🦴

- **Gözlemsel Sorun:** Gözlemsel çalışmalar, süt içen kişilerin kemiklerinin daha sağlıklı olduğunu _gösterebilir_. Ancak bu bir yanılsama olabilir. Belki de süt içen insanlar, aynı zamanda daha fazla egzersiz yapıyor, daha iyi bir genel diyete sahipler veya sağlıklarına daha fazla dikkat ediyorlardır (Bunlar karıştırıcı faktörlerdir).
    
- **MR Çözümü:**
    
    - **Genetik Araç (A 🧬):** LCT genindeki (Laktaz geni) bir varyant. Bu varyant, bireylerin yetişkinlikte laktozu sindirip sindirememesini (Laktaz Kalıcılığı) belirler.
        
    - **Maruziyet (B 🥛):** Süt tüketimi. Laktaz kalıcılığı olanlar (laktozu sindirebilenler) rahatça süt içerken, laktoz intoleransı olanlar (genin farklı bir versiyonu) doğal olarak çok daha az süt tüketirler.
        
    - **Sonuç (C 🦴):** Kemik mineral yoğunluğu veya kırık riski.
        
- **MR Mantığı:** Doğa, insanları rastgele "süt içebilen" (tedavi grubu) ve "süt içemeyen" (kontrol grubu) olarak ikiye ayırmıştır. Bu genetik ayrım, kişinin "sağlıklı yaşam tarzı" seçimlerinden etkilenmez.
    
- **Bulgu:** MR çalışmaları, bu genetik aracı kullanarak süt tüketiminin kemik kırıkları üzerinde _nedensel_ bir koruyucu etkisi olmadığını veya çok az olduğunu göstermiştir. Bu, gözlemsel bulguların karıştırıcı faktörlerden kaynaklanmış olabileceğini düşündürmektedir.
    

---

### Örnek 2: D Vitamini Seviyeleri ve Kanser Riski ☀️♋

- **Gözlemsel Sorun:** Kan D vitamini seviyesi düşük olan kişilerde bazı kanser türlerinin daha sık görüldüğü gözlemlenmiştir. Peki, D vitamini düşüklüğü mü kansere neden oluyor (nedensellik)? Yoksa kanser hastalığı mı kişinin D vitamini seviyesini düşürüyor (tersine nedensellik)? Veya ikisine de neden olan üçüncü bir faktör mü var (örn. kapalı alanda çalışma, obezite)?
    
- **MR Çözümü:**
    
    - **Genetik Araç (A 🧬):** D vitamini metabolizmasıyla (sentezi, taşınması veya yıkımıyla) ilgili genlerdeki (örn. _DHCR7_, _CYP2R1_) SNP'ler.
        
    - **Maruziyet (B ☀️):** Plazma 25(OH)D (D vitamini) seviyeleri.
        
    - **Sonuç (C ♋):** Belirli bir kanser türünün riski.
        
- **MR Mantığı:** Bu SNP'lere sahip olan kişilerin, yaşam tarzlarından _bağımsız_ olarak, ömür boyu genetik olarak biraz daha düşük (veya yüksek) D vitamini seviyelerine sahip olma eğilimi vardır.
    
- **Bulgu:** Çoğu MR çalışması, genetik olarak belirlenmiş D vitamini seviyelerinin, birçok kanser türü (örn. meme, prostat) üzerinde nedensel bir koruyucu etkisi _bulamamıştır_. Bu, gözlemsel olarak bulunan ilişkinin muhtemelen nedensel olmadığını, tersine nedensellik veya karıştırıcı faktörlerden kaynaklandığını göstermektedir.
    

Bu örnekler, MR'ın gözlemsel epidemiyolojideki bulguları nasıl "sorgulamak" veya "doğrulamak" için kullanıldığını gösteriyor.

Şimdi 3. adıma geçmeden önce kısa bir ara soru: Bu yöntemi kendi çalışmalarınızda (mesela ultra işlenmiş gıdalar, insülin direnci veya GLP-1 gibi konularda) nasıl kullanabileceğinize dair bir fikir oluşmaya başladı mı? (Bu sadece bir düşünce egzersizi, cevabı 3. adımdan sonra da düşünebiliriz.)

**MR Türleri ve Analizi**.

Pratikte MR çalışmalarının nasıl yapıldığına baktığımızda, karşımıza temelde iki yaklaşım çıkar:

### 1. Tek Örneklemli MR (One-Sample MR)

- **Nedir?** Hem genetik aracın (A 🧬) maruziyetle (B ☀️) ilişkisini hem de genetik aracın (A 🧬) sonuçla (C 🩺) ilişkisini **aynı katılımcı grubundan** (aynı veri seti) elde ettiğiniz durumdur.
    
- **Avantajı:** Tüm veriler aynı kişilerden geldiği için daha tutarlıdır.
    
- **Dezavantajı:** Her iki ilişkiyi de (A->B ve A->C) güçlü bir şekilde tahmin edebilmek için _çok_ büyük ve _tüm_ bu ölçümlere (genetik, maruziyet ve sonuç) sahip tek bir veri seti bulmak zordur.
    

### 2. İki Örneklemli MR (Two-Sample MR)

Bu, günümüzde MR çalışmalarının ezici çoğunluğunun yapıldığı yöntemdir ve devrim niteliğindedir.

- **Nedir?** İki farklı veri setini (örneklemi) "birleştirirsiniz".
    
    1. **Örneklem 1 (GWAS-Maruziyet):** Genetik aracın (A 🧬) maruziyetle (B ☀️) ilişkisini belirlemek için _sadece_ bu ilişkiye bakan devasa bir GWAS (Genom Boyu İlişkilendirme Çalışması) özet verisi kullanırsınız. (Örn: Yüz binlerce kişide D vitamini seviyeleri ile ilişkili SNP'leri bulan bir çalışma.)
        
    2. **Örneklem 2 (GWAS-Sonuç):** Genetik aracın (A 🧬) sonuçla (C 🩺) ilişkisini belirlemek için, _tamamen bağımsız_, başka bir devasa GWAS özet verisi kullanırsınız. (Örn: Yüz binlerce kişide kanser riski ile ilişkili SNP'leri bulan farklı bir çalışma.)
        
- **Avantajı:** İnanılmaz bir istatistiksel güce ulaşırsınız. Kendi başınıza toplamanızın imkansız olacağı (örn. 500.000 kişilik) verileri, herkese açık bu özet (summary-level) verileri kullanarak analiz edebilirsiniz.
    

---

### Analiz Yöntemleri (Çok Kısa Bir Bakış)

Bu verileri birleştirdiğinizde, nedensel etkiyi tahmin etmek için çeşitli istatistiksel yöntemler kullanılır:

1. **Temel Yöntem (IVW - Inverse-Variance Weighted):**
    
    - Bu, ana nedensel etki tahminini veren standart yöntemdir.
        
    - Ancak bu yöntemin "doğru" sonuç vermesi için **tüm varsayımların** (özellikle 3. varsayım olan pleiotropi olmaması) geçerli olduğunu varsayar.
        
2. **Duyarlılık Analizleri (Sensitivity Analyses):**
    
    - Peki ya 3. varsayım (pleiotropi) ihlal edildiyse? Yani ya gen (A 🧬), sonucu (C 🩺) maruziyet (B ☀️) dışında _başka yollardan_ da etkiliyorsa?
        
    - İşte bu olasılığı kontrol etmek için **MR-Egger** ve **Weighted Median** gibi ek testler yapılır.
        
    - Eğer bu testlerin sonuçları da ana IVW yöntemiyle benzer bir yönü gösteriyorsa, bulgularınıza olan güveniniz artar. Eğer farklı çıkarlarsa, "Dikkat, burada pleiotropi olabilir!" alarmı verir.
        

### Özetle

Mendelian Randomizasyon, genetiği bir "doğal deney" olarak kullanarak gözlemsel verilerdeki nedensellik sorularına (acaba X, Y'ye neden oluyor mu?) cevap aramamızı sağlayan güçlü bir araçtır.

Artık üç adımı da tamamladık:

1. **Varsayımlar** (Üç temel kural)
    
2. **Örnekler** (Süt ve D vitamini)
    
3. **Türler ve Analiz** (Tek/İki Örneklem ve IVW/MR-Egger)

"İki Örneklemli MR" (Two-Sample MR) çalışması yapmak, temelde herkese açık (public) olan devasa genetik veri setlerini bir araya getirme işidir.

Süreci bir "yemek tarifi" gibi düşünebiliriz. İki ana "malzemeye" ihtiyacımız var:

1. **Malzeme 1: Maruziyet (Exposure) Verisi**
    
    - İlgilendiğiniz maruziyet (örn: kafein tüketimi, plazma C-peptid seviyeleri, vb.) üzerine yapılmış büyük bir GWAS (Genom Boyu İlişkilendirme Çalışması) bulmanız gerekir.
        
    - **Amacınız:** Bu çalışmadan, maruziyetinizle _güçlü_ şekilde ilişkili olan genetik varyantları (SNP'leri 🧬) ve onların etki büyüklüklerini (beta katsayıları) almaktır.
        
2. **Malzeme 2: Sonuç (Outcome) Verisi**
    
    - İlgilendiğiniz sonuç (örn: Tip 2 Diyabet riski, miyokard enfarktüsü, vb.) üzerine yapılmış, _farklı ve bağımsız_ bir popülasyondan gelen başka bir büyük GWAS bulmanız gerekir.
        
    - **Amacınız:** Maruziyet için bulduğunuz o SNP'lerin (Malzeme 1), bu veri setindeki sonuçla olan ilişkilerini ve etki büyüklüklerini almaktır.
        

---

### Pratik Adımlar ve Kaynaklar

Bu malzemeleri bulmak için en sık kullanılan iki platform şunlardır:

- **GWAS Catalog:** Çeşitli özellikler (traits) için yayınlanmış tüm GWAS çalışmalarının bir kataloğudur.
    
- **MR-Base Platformu (ve "TwoSampleMR" R paketi):** Bu, süreci çok kolaylaştıran bir platformdur. Binlerce GWAS özet verisini kendi içinde barındırır. Siz sadece "Benim maruziyetim X, sonucum Y" dersiniz, o sizin için Malzeme 1 ve 2'yi bulur, verileri çeker, analiz eder ve sonuçları verir.
    

İş akışı genellikle şöyledir:

1. **Araçları (SNP'leri) Seç:** MR-Base'e gidersiniz ve maruziyetiniz (örn. "coffee consumption") için en güçlü SNP'leri seçersiniz.
    
2. **Sonuç Verisini Seç:** Platformdan sonuç verinizi (örn. "type 2 diabetes") seçersiniz.
    
3. **Harmonizasyon:** Paket, otomatik olarak SNP'lerin her iki veri setinde de aynı alele (A, T, C, G) göre kodlandığından emin olur (bu kritik bir teknik adımdır).
    
4. **Analiz:** Verileri birleştirir ve ana MR analizlerini (IVW, MR-Egger, vb.) çalıştırır.
    

Bu pratik adımlar, devasa veri setlerine erişimi nasıl demokratikleştirdiğini gösteriyor.


### Pleiotropi Nedir?

Basitçe, **bir genetik varyantın (A 🧬) birden fazla, görünüşte birbiriyle ilişkisiz, özelliği (fenotipi) etkilemesi**durumudur.

### MR İçin Neden Büyük Bir Sorun?

Hatırlarsanız, 3. Temel Varsayımımız ("Dışlama Kısıtlaması") vardı. Bu varsayım diyordu ki:

> "Genetik araç (A 🧬), sonucu (C 🩺) **yalnızca ve yalnızca** bizim ilgilendiğimiz maruziyet (B ☀️) üzerinden etkileyebilir."

Pleiotropi, bu varsayımı doğrudan ihlal eder. Genetik aracımıza, sonucu etkilemek için "gizli bir arka kapı" veya "ikinci bir yol" açar.

Bu "sorunlu" pleiotropi türüne **Yatay Pleiotropi (Horizontal Pleiotropy)** denir.

Görselleştirelim:

- **İstediğimiz Yol (Geçerli MR):** A 🧬 → B ☀️ (Maruziyet) → C 🩺 (Sonuç)
    
- **Pleiotropik Yol (Geçersiz MR):** A 🧬 → B ☀️ (Maruziyet) → C 🩺 (Sonuç) **VE AYNI ZAMANDA** A 🧬 → D ❓ (Başka bir mekanizma) → C 🩺 (Sonuç)
    

Eğer böyle bir durum varsa, gen (A) ile sonuç (C) arasında bulduğumuz ilişkinin ne kadarının bizim maruziyetimizden (B) geldiğini, ne kadarının o "diğer yoldan" (D) geldiğini bilemeyiz.

### Beslenmeden Somut Bir Örnek

- **Soru:** Kahve tüketimi (B ☕) kalp hastalığı (C ❤️) riskini etkiler mi?
    
- **Araç:** Kahve metabolizmasını (kafein yıkımını) etkileyen bir SNP (A 🧬) bulduk.
    
- **Pleiotropi Riski:** Ya bu SNP (A 🧬), kahve tüketiminden (B ☕) _tamamen bağımsız_ olarak, _doğrudan_ kan lipid seviyelerini (D lipid) de etkiliyorsa?
    
- **Sonuç:** Biz SNP ile kalp hastalığı arasında bir ilişki bulduğumuzda, "İşte, kahve tüketimi kalp hastalığına neden oluyor/koruyor!" deriz. Ama belki de bu etkinin tamamı, genin lipidler üzerindeki etkisinden (A → D → C yolu) kaynaklanıyordur ve kahveyle (A → B → C yolu) hiçbir ilgisi yoktur.
    

### Nasıl Tespit Edilir? (Duyarlılık Analizleri)

İşte burada "İki Örneklemli MR" analizinde gördüğümüz **MR-Egger** ve **Weighted Median** gibi testler devreye girer.

1. **MR-Egger Intercept Testi:**
    
    - Bu testin temel bir çıktısı vardır: "intercept" (kesişim noktası).
        
    - Eğer bu "intercept" değeri istatistiksel olarak **sıfırdan (0) farksızsa**, bu iyi bir haberdir. "Yatay pleiotropi yoktur veya dengelidir." anlamına gelir.
        
    - Eğer bu "intercept" değeri sıfırdan **anlamlı derecede farklıysa**, bu büyük bir kırmızı bayraktır 🚩. "Genleriniz, maruziyetinizden bağımsız olarak sonucu etkileyen başka yollara sahip olabilir!" demektir.
        
2. **Weighted Median (Ağırlıklı Medyan):**
    
    - Bu yöntem, kullandığınız SNP'lerin (araçların) en az yarısı (%50'si) pleiotropik _olmadığı_ sürece size yine de güvenilir bir sonuç verebilir.
        

Bu testler, MR bulgularımızın ne kadar sağlam olduğunu kontrol etmemizi sağlayan "güvenlik kontrolleridir".

