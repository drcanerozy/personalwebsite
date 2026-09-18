---
Tür:
  - Besleyici
ODAK:
  - "[[GLP-1]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[GLP-1'e Giriş]]"
  - "[[GLP-1 İlaçlarının Ortaya Çıkışı ve Kliniğe Girişi]]"
  - "[[Tirzepatide, Kilo ve Yağ Kaybı Sağlasa da Adipoz Doku Disfonksiyonelliğini Düzeltmiyor]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[GLP-1 Araştırmaları Beslenme Araştırmalarını Öteliyor Mu?]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[GLP-1 İlaçlarının Ortaya Çıkışı ve Kliniğe Girişi]]"
  - "[[GLP-1 ve Diyetisyenlik]]"
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
Klinik geliştirme aşamasındaki yeni nesil obezite ve tip 2 diyabet ilaçları, tekli GLP-1 reseptör agonistlerinin (Semaglutid, Liraglutid) açtığı yoldan ilerleyerek obezite tedavisinde çıtayı "bariatrik cerrahi seviyesine" çıkarmayı hedeflemektedir. Bu yeni ajanlar; daha fazla kilo kaybı sağlamak, yan etkileri azaltmak, kas kütlesini korumak ve uygulama kolaylığı sunmak amacıyla geliştirilmektedir.

Tekli GLP-1'lerden neden farklı oldukları, hedefleri, beklenen etkileri ve tedaviye katacakları yenilikler sınıflarına göre şu şekildedir:

**### 1. Çoklu İnkretin Agonistleri (GIP ve Glukagon Entegrasyonu)**

Tekli GLP-1 ilaçları öncelikle iştahı keserek enerji alımını azaltır. Yeni nesil ilaçlar ise aynı molekül üzerinde birden fazla reseptörü uyararak (sinerji yaratarak) birden fazla biyolojik mekanizmayı aynı anda hedefler.

- **GLP-1 / GIP Çift Agonistleri (Örn. Tirzepatid, MariTide, CT-388):**
    - **Hedef ve Etki:** GIP (Glikoza bağımlı insülinotropik polipeptid) hormonunun reseptörlerini hedefler.
    - **Farkı ve Tedaviye Katkısı:** GIP reseptör aktivasyonu, GLP-1'in insülin salgılatıcı etkisini güçlendirir ve yağ dokusunda insülin duyarlılığını artırır. En önemli farklarından biri, GIP'in merkezi sinir sisteminde potansiyel bir **anti-emetik (bulantı önleyici)** etkiye sahip olmasıdır. Bu sayede hastalar, tekli GLP-1'lerde görülen şiddetli mide bulantısı olmadan çok daha yüksek dozları tolere edebilir ve %20'nin üzerinde kilo kaybı yaşayabilirler. MariTide (AMG133) gibi GIP'i bloke eden (antagonist) formlar ise ayda bir enjeksiyonla bile uzun süreli ve kalıcı kilo kaybı sunarak tedavi yükünü inanılmaz derecede hafifletmeyi vaat etmektedir.
- **GLP-1 / Glukagon Çift Agonistleri (Örn. Survodutid, Pemvidutid, Mazdutid):**
    - **Hedef ve Etki:** Glukagon reseptörlerini de hedefler.
    - **Farkı ve Tedaviye Katkısı:** GLP-1 sadece enerji alımını düşürürken, glukagon **enerji harcamasını (metabolizma hızını) artırır** ve karaciğerdeki yağların doğrudan yıkımını (lipoliz) uyarır. Bu ilaçların tedaviye en büyük katkısı, MASLD/MASH gibi metabolik karaciğer yağlanması ve fibrozis hastalıklarında karaciğer yağını eşsiz bir hızda temizlemeleridir (Pemvidutid ile karaciğer yağında %68.5'e varan azalma görülmüştür).
- **Üçlü Agonistler (Retatrutid):**
    - GLP-1, GIP ve Glukagon reseptörlerinin üçünü birden hedefler. Faz 2 çalışmalarında 48 haftada **%24.2'lik rekor bir kilo kaybı** sağlayarak farmakolojik olarak bariatrik cerrahinin tahtına ortak olmuştur.

### **2. Amilin ve Kalsitonin Tabanlı İlaçlar**

- **Örn. Cagrilintid, CagriSema, Petrelintid, Amycretin:**
    - **Hedef ve Etki:** Pankreastan salgılanan bir tokluk hormonu olan amilin ve kalsitonin reseptörlerini (DACRA) hedefler.
    - **Farkı ve Tedaviye Katkısı:** Amilin, beynin GLP-1'den çok daha farklı bölgelerindeki (ödül ve motivasyon merkezleri) reseptörleri uyarır. Bu farklı etki yollarının birleşimi (Örn. Semaglutid ve Cagrilintid kombinasyonu olan _CagriSema) sinerjik bir tokluk yaratır. Bu kombinasyon, tekli GLP-1'lerin ulaştığı plato (kilo vermenin durması) evresini aşarak, Faz 3 çalışmalarında 68 haftada %22-25 dolaylarında ciddi bir kilo kaybı sunmaktadır.

### **3. Oral (Ağızdan Alınan) Küçük Moleküller**

- **Örn. Orforglipron, Danuglipron, CT-996:**
    - **Hedef ve Etki:** GLP-1 reseptörlerini ağızdan alınan, peptit (protein) yapısında olmayan "küçük moleküller" ile uyarmak.
    - **Farkı ve Tedaviye Katkısı:** Piyasada halihazırda bulunan oral semaglutid (Rybelsus) bir peptittir; emilimi zordur, aç karnına ve katı su kısıtlamasıyla alınması gerekir. Yeni nesil küçük moleküller (örneğin Orforglipron) ise yiyeceklerden bağımsız olarak içilebilir. Ayrıca soğuk zincir gerektirmedikleri, üretim maliyetleri çok düşük olduğu ve enjeksiyon kalemi montajına ihtiyaç duymadıkları için, GLP-1 ilaçlarının dünyadaki kronik tedarik krizini çözerek bu ilaçları çok daha erişilebilir ve ucuz hale getirmeyi vaat etmektedir.

### 4. Kas Koruyucu ve Hedefli (Targeted) Tedaviler

Hızlı ve büyük çaplı kilo kayıplarının (özellikle %20'yi aşan kayıpların) en büyük tehlikesi, giden kilonun büyük bir kısmının yağsız vücut kütlesinden (kas içi proteinlerden) gitmesidir (sarkopeni).

- **Kas Koruyucular (Örn. Bimagrumab, Azelaprag):**
    - **Hedef ve Etki:** Miyostatin veya Aktivin Tip II reseptörlerini bloke ederek kas yıkımını engeller.
    - **Farkı ve Tedaviye Katkısı:** GLP-1 ilaçlarıyla kombine edildiklerinde, ağırlık kaybının sadece yağ dokusundan (fokuslu) olmasını sağlar, kas kütlesini ve fiziksel fonksiyonları koruyarak "sağlıklı zayıflama" profilini garanti altına alırlar.
- **Hücreye Spesifik Hedefleme (Conjugates):**
    - GLP-1 molekülünün ucuna östrojen veya NMDA reseptör antagonistleri gibi ilaçlar (kargo) eklenerek, bu ilaçların vücutta sadece GLP-1 reseptörü olan spesifik hücrelere girmesi sağlanmaktadır. Bu sayede, örneğin östrojenin sistemik kanserojen yan etkileri olmadan, sadece beynin iştah merkezlerindeki hücrelerde nöroplastisite (yeniden yapılanma) ve kilo kaybı yaratması hedeflenmektedir.

**Özetle:** Tekli GLP-1'ler iştahı keserek mucizevi bir temel atmış olsa da; klinik aşamadaki bu yeni ilaçlar **bariatrik cerrahiye tam alternatif olmayı, spesifik organ onarımını (karaciğer), kas kütlesini koruyarak sağlıklı yaşlanmayı ve iğnesiz-ucuz erişimi** tedaviye ekleyecektir.

Obezite farmakoterapisi, sadece GLP-1'e bağımlı olmaktan çıkıp **"Çoklu Agonistler (Polyagonists)"** ve **"Farklı İletim Yolları"**dönemine giriyor. Yakın gelecekte kullanıma girecek en önemli ajanlar şunlardır:

- **Retatrutid (Üçlü Agonist - 'Triple-G'):** GLP-1, GIP ve Glukagon (GCG) reseptörlerinin üçünü birden uyaran bu molekül, obezite tedavisinde ulaşılan en son zirvedir. Faz 2 çalışmalarında 48 haftada **%24.2'ye varan (bariatrik cerrahiye eşdeğer) devasa bir kilo kaybı** sağlamıştır. İçeriğindeki glukagon sayesinde sadece iştahı kesmekle kalmaz, aynı zamanda bazal metabolizmayı (enerji harcamasını) artırır ve karaciğerdeki yağı doğrudan yakar.
- **CagriSema (GLP-1 + Amilin):** Semaglutid ile bir amilin analoğu olan cagrilintid'in tek bir enjeksiyonda birleştirilmiş halidir. Amilin, beynin farklı bölgelerindeki (GLP-1'den bağımsız) tokluk merkezlerini uyararak etki gösterir ve bu kombinasyonun %25'in üzerinde bir ağırlık kaybı sağlaması hedeflenmektedir.
- **MariTide (AMG 133 - Paradoks İlaç):** Tıp dünyasını şaşkına çeviren bu ilaç, GLP-1'i uyarırken GIP reseptörünü _bloke eden (antagonist)_ bir antikordur. En büyük özelliği **ayda bir kez** enjekte edilmesidir. Daha da önemlisi, ilk Faz 1 verilerine göre hastalar ilacı bıraktıktan sonra bile (5 ay boyunca) verdikleri kiloyu korumaya devam etmişlerdir (rebound etkisini kırabileceğine dair ilk güçlü sinyal). Tirzepatid gibi GIP "uyarıcı" ilaçların sürekli ve kronik kullanımı, aslında yağ dokusundaki GIP reseptörlerini zamanla duyarsızlaştırır (desensitizasyon). Yani kronik agonizm, vücutta işlevsel olarak "antagonizmi (bloke edici etkiyi)" taklit ediyor olabilir. Tek çekirdekli RNA dizileme (snRNA-seq) çalışmaları, GIP antagonizmasının (blokajının) tek başına çalışan bir mekanizma olmadığını, beyindeki GLP-1 sinyal yollarını daha da güçlendirerek (baskılanmış GLP-1 nöronlarını serbest bırakarak) kilo kaybını tetiklediğini göstermektedir. GIP reseptörünün uyarılmasının, GLP-1 ilaçlarının yarattığı mide bulantısını (anti-emetik etkiyle) beyin düzeyinde hafiflettiği, bu sayede hastaların dozu daha fazla artırabildiği ve daha çok kilo verebildiği de öne sürülmektedir.
- **Orforglipron ve Yüksek Doz Oral Semaglutid:** İğne gerektirmeyen, doğrudan hap (oral küçük molekül) olarak yutulan ilaçlardır. Faz 2 çalışmalarında orforglipron %15'e varan, 50 mg'lık yüksek doz oral semaglutid ise enjeksiyona eşdeğer oranda kilo kaybı sağlamıştır.
- **Bimagrumab (Kas Koruyucu/Büyütücü):** Aktivin tip II reseptörünü bloke eden bu antikor, GLP-1'lerin en büyük yan etkisi olan "kas kaybını (sarkopeni)" çözmek için geliştirilmiştir. GLP-1 ilaçları ile birlikte (kombine) kullanılarak hastanın **yağ kütlesini eritirken kas kütlesini koruması ve hatta artırması** hedeflenmektedir.

- **PYY (Peptide YY) Analogları ve GLP-1 Kombinasyonları**
- **Mekanizması ve Hedefi:** PYY, yemekten sonra bağırsaklardaki L-hücrelerinden GLP-1 ile birlikte salgılanan doğal bir tokluk hormonudur. Beyindeki Y2 reseptörlerini (Y2R) uyararak gıda alımını şiddetle baskılar ve tokluk hissini artırır,.
- **Beklenen Etkisi:** Tek başına PYY analoglarının (intranazal gibi yollarla) aniden kana karışması şiddetli bulantı ve kusmaya yol açtığı için dar bir terapötik pencereye sahiptir; bu nedenle farmakoloji dünyası yavaş ve sabit salınımlı PYY analogları geliştirmeye odaklanmıştır.
- **Geliştirilen İlaçlar:** Novo Nordisk tarafından geliştirilen (ancak güncel raporlarda durdurulduğu belirtilen) PYY-1875, Zihipp firmasının Y14 peptidi, Lilly'nin nisotirotide'i ve Boehringer'in BI-1820237 molekülleri Faz 1 ve Faz 2 aşamalarında test edilmektedir,. Genellikle iştahı daha da güçlü kesmek için semaglutid veya liraglutid gibi GLP-1 ilaçlarıyla kombine edilerek (Örn: NNC0165-1875 + Semaglutid) incelenmektedirler

**2. Bu İlaçların Gelmesi Hangi Açılardan Önemli? (Neden Devrim Niteliğindeler?)**

Bu ilaçların piyasaya çıkışı, sunumunuzun önceki bölümlerinde anlattığınız engelleri şu şekillerde yıkacak:

- **Bariatrik Cerrahinin Tahtını Sarsması:** Yeni nesil ilaçlar (Retatrutid, CagriSema vb.) %20-25+ oranında kilo kaybı sağlayarak obezite cerrahisiyle (Tüp mide / Gastrik bypass) arasındaki etki farkını tamamen kapatmaktadır.
- **Küresel Üretim, Maliyet ve Tedarik Krizinin Çözümü:** Şu anki GLP-1 ilaçları karmaşık peptitler olduğu ve soğuk zincir gerektiren plastik enjeksiyon kalemleriyle satıldığı için küresel bir tedarik kıtlığı ve aşırı yüksek maliyet yaşanmaktadır. _Orforglipron_ gibi oral (hap) küçük moleküllerin üretimi çok ucuzdur, soğuk zincir gerektirmez ve obezite tedavisini tüm sosyoekonomik sınıflar için küresel olarak erişilebilir (demokratik) hale getirecektir.
- **"Sağlıklı Kilo Kaybı" (Healthy Weight Loss) Konseptine Geçiş:** Bimagrumab gibi kas koruyucu ajanların devreye girmesiyle odak noktası sadece "tartıdaki rakamı düşürmek" olmaktan çıkıp, vücut kompozisyonunu onarmaya (yağı yakıp kası korumaya) evrilecektir.
- **Adherence (İlaca Uyum) Probleminin Aşılması:** Hastaların yan etkiler veya her hafta iğne olma yorgunluğu nedeniyle tedaviyi bırakması sorunu, _MariTide_ gibi **ayda sadece 1 kez** vurulan veya _Orforglipron_ 

**Kişiselleştirilmiş Tıp Bağlamında Yeni İlaçlar**:
**Karaciğer Yağlanması (MASLD/MASH) Olanlar**: Sadece GLP-1 yerine, Glukagon (GCG) reseptörünü de uyaran ikili veya üçlü ilaçlar (örn. Retatrutid, Pemvidutid, Survodutid) seçilecektir. Çünkü glukagon, doğrudan karaciğeri hedef alarak yağ yakımını (lipid oksidasyonunu) hızlandırır ve karaciğer yağını %70'in üzerinde oranlarda temizleyebilir.
Tip 2 Diyabeti Ağır Basanlar: İnsülin direnci ve diyabeti ön planda olan hastalarda, her ikisi de insülin salgısını artıran GLP-1 ve GIP hormonlarının "ikiz inkretin (twincretin)" etkisinden faydalanmak için Tirzepatid gibi ajanlar hedeflenecektir.

**Uyku Apnesi ve Kalp Yetersizliği Olanlar**: Obeziteyle birlikte obstrüktif uyku apnesi (OSA) ve korunmuş ejeksiyon fraksiyonlu kalp yetersizliği (HFpEF) olan hastalarda Tirzepatid ve Semaglutid, sağladıkları spesifik yararlar doğrultusunda ilk basamakta yer alacaktır.
Kas Kaybı (Sarkopeni) Riski Taşıyanlar: Yaşlılarda veya kas kütlesi düşük olanlarda (sarkopenik obezite), hızlı kilo kaybı kas erimesi riskini getirir. Bu kişilere sadece iştah kesen GLP-1'ler değil, eş zamanlı olarak kas kütlesini koruyan veya artıran (örn. miyostatin inhibitörleri veya bimagrumab gibi Aktivin Tip II reseptör blokerleri) hedefe yönelik anabolik kombinasyonlar reçete edilebilecektir.

**Gastrointestinal Hassasiyeti (Bulantı) veya İğne Fobisi Olanlar**: Mide bulantısı ve kusma nedeniyle tedaviyi sürdüremeyen hastalarda GIP kombinasyonları veya amilin analogları (CagriSema vb.) denenebileceği gibi; iğne kullanmak istemeyen hastalarda her gün içilebilen düşük maliyetli oral (hap) GLP-1 molekülleri (örn. Orforglipron) devreye girecektir.

**Farmakogenomik Profilleme**: Gelecekte, genetik testler ile bireylerin GLP-1R, GIPR veya TCF7L2 genlerindeki varyasyonlarına bakılarak; hastanın hangi moleküle tam yanıt vereceği (responder) veya hangisine dirençli olacağı (non-responder) önceden tahmin edilerek, deneme-yanılma yapmadan en doğru ilaç seçilebilecektirgibi ağızdan yutulan ilaçlarla aşılacaktır.


