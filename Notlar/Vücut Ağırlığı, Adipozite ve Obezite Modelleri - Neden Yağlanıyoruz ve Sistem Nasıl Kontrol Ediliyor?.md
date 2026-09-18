---
Tür:
  - Çekirdek
ODAK:
  - "[[Obezite]]"
MEKANİZMA:
DİZİN:
  - "[[Karbonhidrat İnsülin Modeli]]"
  - "[[Kalori Kısıtlaması]]"
ETİKET:
BAĞLANTILI NOTLAR: "[[Vücut Ağırlığının Matematiği]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[Diyet İlkeleri ve Popüler Diyetler]]"
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "null"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "p > 0.05 (anlamsız)"
BESLEDİĞİ NOTLAR:
  - "[[Vücut Ağırlığının Matematiği]]"
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

> **Metodolojik Etiketler:** #finding/null
# 1.VÜCUT AĞIRLIĞI MODELLEMESİNE GİRİŞ

## 1.1. Obezite Nedir ve Neden Küresel Bir Krizdir?
Obezite, sağlığı bozacak ölçüde aşırı yağ birikimi ile karakterize kronik bir hastalıktır. Gözlemsel veriler, obezite prevalansının özellikle 1980'lerden itibaren küresel çapta dramatik bir şekilde arttığını göstermektedir; örneğin ABD'de 1980'de yetişkin popülasyonun %14'ü obez kategorisindeyken bu oran günümüzde %42'ye ulaşmıştır. Bu artış, obezitenin tip 2 diyabet, kardiyovasküler hastalıklar, hipertansiyon ve çeşitli kanser türleri gibi bulaşıcı olmayan kronik hastalıklar ile olan nedensel ilişkisi nedeniyle küresel bir halk sağlığı krizi olarak tanımlanmasına yol açmıştır. Obezite ile ilişkili hastalıklar tüm nedenlere bağlı ölümleri artırmakta ve sağlık sistemleri üzerinde ağır bir ekonomik yük oluşturmaktadır.

## 1.**2. Enerji Dengesi ve Termodinamik** 
Vücut ağırlığının ve enerji regülasyonunun bilimsel temelleri 18. yüzyılın sonlarında Antoine Lavoisier'nin kalorimetriyi icat etmesi ve oksijenin fizyolojik yanma (solunum) süreçlerindeki rolünü keşfetmesiyle atılmıştır. 19. yüzyılın ortalarında ise enerjinin korunumu yasası (Termodinamiğin Birinci Yasası) fizyolojiye entegre edilmiş ve fizyolojik enerji dengesi denklemi (alınan enerji - harcanan enerji = depolanan enerji) kurulmuştur.

Bu fiziksel ilkeye dayanarak, L.H. Newburgh ve M.W. Johnston 1930 yılında obezitenin "her zaman harcanandan fazla enerji alınmasından" (pozitif enerji dengesi) kaynaklandığını öne süren ilk klinik öneriyi sunmuşlardır,. Bu görüş, obezite tedavisinde yıllarca standart olarak kalacak olan "kalori kısıtlaması" (daha az yemek) ve "artan fiziksel aktivite" (daha çok hareket etmek) tavsiyelerinin temelini oluşturmuştur,. Ancak termodinamiğin birinci yasası, insan vücudu gibi açık sistemlerde kütle ve enerjinin korunacağını hesaplasa da; alınan kalorilerin neden aşırı tüketildiğine veya vücudun bu kalorileri neden hücrelerde okside etmek yerine yağ dokusunda depolamayı seçtiğine dair etiyolojik ve biyolojik bir nedensellik açıklamaz,,.

## 1.3. "Çok Faktörlü" Bir Hastalık Olarak Obezite ve Biyolojik Kırılma Noktaları

19.yüzyılın sonları ve 20. yüzyılın başlarında Claude Bernard ve Walter Cannon tarafından fizyolojik parametrelerin dar sınırlar içinde aktif olarak düzenlendiğini ifade eden "homeostazi" kavramı geliştirilmiştir. 1953 yılında G.C. Kennedy, bu konsepti vücut ağırlığına uyarlayarak yağ kütlesinin homeostatik olarak düzenlendiğini belirten "lipostaz" (set-point/ayar noktası) teorisini ortaya atmıştır,.

Obezitenin çok faktörlü biyolojik yapısının anlaşıldığı en önemli kırılma noktalarından biri genetiktir. 1970'lerde A.J. Stunkard ve arkadaşlarının yürüttüğü ikiz ve evlat edinme çalışmaları, vücut kitle indeksi (VKİ) varyasyonunun %40 ila %75 oranında genetik faktörlere bağlı olduğunu kanıtlamıştır,. 1973 yılında Douglas Coleman'ın genetik olarak obez (ob/ob ve db/db) fareler üzerinde yaptığı parabiyoz (dolaşım sistemlerinin birleştirilmesi) deneyleri, yağ depoları ile beyin arasında iletişim kuran dolaşımdaki bir faktörün varlığını ortaya koymuştur. 1994 yılında Jeffrey Friedman ve ekibi tarafından bu faktörün, yağ dokusundan salgılanan "leptin" hormonu olarak keşfedilmesiyle (klonlanmasıyla), yağ dokusunun yalnızca pasif bir depo değil, aktif bir endokrin organ olduğu kesinleşmiştir,.

Öte yandan, insan gen havuzunun son kırk yılda belirgin bir değişime uğramadığı bilinmektedir,. Bu nedenle genetik yatkınlığın, hızla değişen "obesojenik" çevre (artan ultra işlenmiş gıdalar, makrobesin kompozisyonundaki değişimler, uyku kalitesi ve endokrin bozucu kimyasallar) ile olan karmaşık etkileşimi (ekspozom) modern obezitenin etiyolojik çerçevesini oluşturmaktadır.

# 2.BİYOLOJİK ALTYAPI
## 2.1.Homeostatik ve Hedonik Kontrol
Canlılarda iç dengenin korunması anlamına gelen "homeostazi" kavramı, ilk olarak 19. yüzyılın sonlarında Claude Bernard ve 20. yüzyılın başlarında Walter Cannon tarafından fizyoloji literatürüne kazandırılmıştır,. Beslenme bağlamında homeostazi, hücresel ATP oranlarını ve dolaşımdaki enerji substratlarını sabit tutmayı amaçlar.

Modern nörobiyolojik çalışmalar, beslenme davranışının iki temel nöral ağ tarafından yönetildiğini göstermiştir:

- **Homeostatik Beslenme:** Fizyolojik enerji ihtiyacını karşılamayı hedefler. Hipotalamustaki arkuat çekirdek (ARC) bu sistemin merkezidir,.
- **Hedonik Beslenme:** Gıdanın duyusal özelliklerinden alınan haz (ödül) ile motive edilen beslenmedir. Dopamin, opioid ve endokannabinoid sistemleri tarafından yönetilir ve ventral tegmental alan (VTA) ile prefrontal korteks (PFC) gibi beyin bölgelerini içerir,,. Günümüz obesojenik ortamlarında, enerji yoğun ve yüksek lezzetli gıdaların varlığı, hedonik sistemin homeostatik sinyalleri baskılamasına (override) ve fizyolojik ihtiyaçtan bağımsız kalori alımına neden olmaktadır,.

## 2.2 Minnesota Açlık Deneyi ve Kıtlık (Starvation) Yanıtı (1944-1950)
İnsan vücudunun enerji kısıtlamasına verdiği yanıtı inceleyen en kapsamlı ve imza niteliğindeki çalışma, Ancel Keys ve ekibi tarafından gerçekleştirilen ve 1950'de yayımlanan "Minnesota Açlık Deneyi"dir,,. Çalışmada, 32 sağlıklı erkek gönüllü yaklaşık 6 ay boyunca şiddetli kalori kısıtlamasına (yarı-açlık) maruz bırakılmış ve başlangıç ağırlıklarının yaklaşık %24'ünü kaybetmişlerdir. Bu süreçte:

- Vücut ağırlığı kaybı ilk haftalarda hızlı (su ve glikojen kaybı), ilerleyen haftalarda ise daha yavaş (yağ dokusu kaybı) gerçekleşmiştir,.
- Fizyolojik olarak deneklerin bazal metabolizma hızları (BMR) ve fiziksel aktivite düzeyleri belirgin şekilde düşmüştür,.
- Deneklerde apati (duyarsızlık), asabiyet ve zihinsel olarak tamamen yemeğe odaklanma görülmüştür,.
- Kısıtlama dönemi bitip yiyeceğe serbest erişim sağlandığında, denekler aşırı yeme (hiperfaji) atakları sergilemiş ve yağ kütleleri başlangıç seviyelerinin üzerine çıkmıştır,. Bu çalışma, vücudun enerji açığını fizyolojik bir kriz olarak algılayıp hem biyolojik hem de davranışsal olarak eski kilosunu (veya yağ kütlesini) geri kazanmaya yönelik muazzam bir direnç gösterdiğini kanıtlamıştır.

## 2.3. Adaptif Termojenez: Vücudun Kilo Kaybına Metabolik Direnci (1995)
Minnesota deneyinin bulgularını modern obezite araştırmalarına entegre eden en önemli kırılma noktası, Rudolph Leibel ve arkadaşlarının 1995 yılında yayımladığı çalışmadır,,.

Normal şartlarda vücut ağırlığı (özellikle yağsız kütle/FFM) azaldığında, dinlenik enerji harcamasının (REE) da orantılı olarak düşmesi beklenir,. Ancak Leibel'in çalışması, vücut ağırlığında %10'luk bir azalma sağlandığında, vücudun enerji harcamasının, sadece kaybedilen kütle ile açıklanamayacak kadar _orantısız ve şiddetli_ bir şekilde düştüğünü göstermiştir,,. Bu kavrama literatürde **"Adaptif Termojenez"** (AT) adı verilir. Vücut, enerji kısıtlaması sırasında iskelet kaslarının kasılma verimliliğini artırır, sempatik sinir sistemi (SNS) aktivitesini düşürür, parasempatik tonusu (PNS) artırır ve biyoaktif tiroid hormon (T3) seviyelerini azaltır,,. Sonuç olarak vücut daha az kalori ile yaşamını sürdürmeye adapte olur; bu da diyet yapan bireylerde kilo vermenin durmasına (plateau) ve kaybedilen kilonun hızla geri alınmasına neden olan ana mekanizmadır,.

## 2.4. Leptin ve Ghrelin: Tokluk Hormonundan Kıtlık Sinyaline Geçiş (1994-2001)
Adipoz (yağ) dokusu ile beyin arasındaki iletişimin nöroendokrin doğası 1994 yılında Jeffrey Friedman ve ekibinin adipoz dokudan salgılanan **"Leptin"** (ob geni) hormonunu klonlamasıyla aydınlanmıştır,,.

- **İlk Hipotez:** Başlangıçta leptinin obeziteyi çözen bir "tokluk sinyali" olduğu düşünülmüştür. Yağ kütlesi arttıkça leptin artar ve beyne "yemeyi durdur, enerjiyi harca" sinyali gönderir. Ancak klinik çalışmalar, obez bireylerin çoğunda leptin seviyelerinin zaten çok yüksek olduğunu ve dışarıdan leptin verilmesinin kilo kaybı sağlamadığını göstermiştir,. Bu durum literatüre **"leptin direnci"** olarak geçmiştir,.
- **Paradigma Değişimi:** Leptin direncinin keşfiyle birlikte bilimsel bakış açısı değişmiştir. Güncel anlayışa göre leptinin evrimsel ve birincil rolü obeziteyi engellemek değil, yağ depoları azaldığında (açlık durumunda) düşerek beyne **"kıtlık (starvation) sinyali"** göndermektir,,. Kilo kaybı sırasında kan leptin seviyesi düştüğünde; hipotalamusta iştah açıcı (oreksijenik) AgRP/NPY nöronları uyarılır, iştah kapatıcı (anoreksijenik) POMC nöronları baskılanır. Aynı zamanda tiroid ve sempatik sinir sistemi baskılanarak adaptif termojenez tetiklenir,. Yani leptin düşüklüğü, vücudun enerji tasarruf moduna geçmesini ve şiddetli açlık hissini başlatan ana şalterdir,.

Bu dönemin bir diğer önemli keşfi, 2001 yılında Cummings ve ekibi tarafından fonksiyonları tanımlanan **"Ghrelin"** hormonudur. Mideden salgılanan ghrelin, leptinin aksine açlık durumunda artarak beyni uyarır ve doğrudan gıda arama ve yeme davranışını (oreksijenik tonusu) başlatır.

# 3.NEDEN TEORİ VE MODELLERE İHTİYACIMIZ OLDU?
Obezitenin karmaşık doğasını anlamak için gözlemleri organize edecek, test edilebilir hipotezler sunacak ve biyolojik nedensellik yönünü (sebep-sonuç ilişkisini) belirleyecek modellere ihtiyaç vardır. On yıllardır uygulanan "daha az ye, daha çok hareket et" müdahalelerinin popülasyon düzeyinde başarısız olması, obezitenin sadece bilinçli bir davranış veya irade sorunu olmadığını göstermiştir. 1959'da Albert Stunkard kalori kısıtlamasına dayalı diyet tedavilerinin uzun vadeli başarı oranlarının istatistiksel olarak son derece düşük olduğunu bildirmiştir. Vücudun kilo kaybına karşı geliştirdiği biyolojik savunma mekanizmaları (metabolizmanın yavaşlaması ve artan açlık), termodinamik denklemlerin tek başına hastalığın etiyolojisini açıklamakta yetersiz kaldığını kanıtlamış ve bilim insanlarını farklı etiyolojik modeller geliştirmeye zorlamıştır

Bu klinik başarısızlığın fizyolojik kanıtı, 1995 yılında Rudolph Leibel ve arkadaşları tarafından sunulmuştur. Leibel'in çalışmaları, vücut ağırlığında %10'luk bir azalmanın ardından vücudun dinlenik enerji harcamasını beklenen vücut kompozisyonu değişiminden çok daha fazla düşürdüğünü (adaptif termojenez) ve iştahı artırarak kaybedilen kiloyu geri almaya yönelik nöroendokrin bir direnç gösterdiğini kanıtlamıştır.

Vücut ağırlığının sadece bilinçli bir irade veya basit bir termodinamik denge sorunu olmadığı gerçeği, EBM (Enerji Dengesi Modeli), CIM (Karbonhidrat-İnsülin Modeli) ve çevresel/evrimsel adaptasyon hipotezleri gibi yapılandırılmış teorilerin geliştirilmesini zorunlu kılmıştır. Bu modeller; toplanan ampirik verileri organize etmek, obezite patogenezindeki nedensellik yönünü (sebep ve sonuç ilişkisini) test etmek ve gelecekte obezitenin önlenmesi ile klinik tedavisi için rasyonel ve yeni hedefler belirlemek amacıyla kullanılmaktadır.

## 3.1.Fizyolojiye Termodinamik Yaklaşım, Kilo Kaybını ve Müdahalelerini Neden Açıklayamıyor?
Fizyolojik enerji dengesi ve termodinamik yaklaşım, temellerini 18. yüzyılda Antoine Lavoisier'nin oksitlenme ve fizyolojik yanma (kalorimetri) keşiflerinden alır ve Termodinamiğin Birinci Yasasına (enerjinin korunumu) dayanır. Bu yaklaşıma göre, açık bir sistem olan insan vücudunda alınan enerji (kalori) ile harcanan enerji arasındaki fark, depolanan enerjiye eşittir (ΔU=Alınan Enerji−Harcanan Enerji).

Bu yasa fiziksel olarak kesinlikle doğru olsa da, kilo kaybını ve obeziteyi _nedensel_ olarak açıklamada şu sebeplerden ötürü yetersiz kalır:

- **Totoloji (Nedensellik Eksikliği):** Enerjinin korunumu yasası, aşırı yağ birikiminin "pozitif enerji dengesi" (harcanandan fazlasını almak) anlamına geldiğini söyler; ancak bu bir totolojidir (malumu ilamdır). Bir insanın ateşinin çıkmasını "vücudun atabildiğinden daha fazla ısı üretmesi" ile açıklamak ne kadar yetersizse, obeziteyi de sadece "pozitif enerji dengesi" ile açıklamak o kadar yetersizdir; çünkü bu durum aşırı kalori alımını neyin tetiklediğini veya vücudun bu kalorileri neden hücresel oksidasyon yerine yağ dokusunda depolamayı seçtiğini açıklamaz.
- **Açık Sistemlerde Kütle vs. Enerji Ayrımı:** Matematiksel ve biyofiziksel analizler, insan vücudu gibi "açık" termodinamik sistemlerde enerji dengesi ile kütle (mass) dengesinin aynı şey olmadığını göstermektedir. Vücut ağırlığındaki değişimler, sadece enerji akışıyla değil; atomların ve moleküllerin (karbonhidrat, yağ, protein) kütlesel akışıyla (mass flux) gerçekleşir. Obeziteyi saf bir enerji birikimi problemi olarak görmek, sistemin iç fizyolojik dinamiklerini göz ardı eder.
- **Müdahalelerin Başarısızlığı:** Termodinamik bakış açısı, müdahalelerin "alınan kaloriyi kısıtlamak" veya "harcananı artırmak" üzerine kurulmasına neden olmuştur. Ancak kilo kaybı sürecinde adaptif termojenez devreye girerek enerji harcamasını düşürür ve açlığı artırır. Bu nedenle, sadece dışarıdan bir kalori kısıtlaması dayatmak (CICO yaklaşımı), vücudun kendi iç homeostatik düzenlemeleri ve fizyolojik direnci (metabolik adaptasyon) nedeniyle uzun vadede başarısızlıkla sonuçlanır.
## 3.2.CICO Yaklaşımı ve "Bir Kalori Bir Kaloridir" Tartışması
CICO (Calories In, Calories Out) paradigması, 1890'larda W.O. Atwater'ın besinlerin kalori değerlerini hesaplamasıyla ve 1930'da Newburgh ile Johnston'ın "obezitenin her zaman aşırı yeme kaynaklı olduğu" beyanıyla şekillenmiştir. Klasik Enerji Dengesi Modeli (EBM), besinlerin makrobesin (yağ, karbonhidrat, protein) içeriğinden bağımsız olarak, vücut yağı üzerinde yalnızca kalori değerleri ölçüsünde etkili olduğunu ("bir kalori bir kaloridir") savunmuştur.

Buna karşılık, "bir kalori bir kalori _değildir_" (farklı kalorilerin farklı metabolik etkileri olduğu) argümanı ve kanıtları şu fizyolojik bulgulara dayanarak ortaya çıkmıştır:

- **Hormonal ve Metabolik Yanıtlar (Yakıt Bölüştürme):** Farklı makrobesinler (örneğin karbonhidratlar ve yağlar) insülin ve glukagon gibi hormonlar üzerinde tamamen farklı tepkilere neden olur. Karbonhidrat-İnsülin Modeli (CIM), yüksek glisemik yüklü karbonhidratların insülini artırarak (ve glukagonu baskılayarak) enerjiyi yağ dokusuna hapsettiğini, bunun da kan dolaşımındaki yakıtı azaltarak beyni sürekli açlığa ittiğini (adaptif termojenezi tetiklediğini) savunur.
- **Besinlerin Termik Etkisi ve Termojenez:** Proteinlerin, karbonhidratların ve yağların sindirilmesi ve metabolize edilmesi için harcanan enerji (DIT - Diet-induced thermogenesis) birbirinden farklıdır (örneğin proteinlerin termik etkisi %20-30 iken, yağlarınki %0-3'tür). Dolayısıyla, 100 kalorilik bir badem ile 100 kalorilik bir şekerlemenin vücuttaki enerji harcaması, hormon salgılanması ve yağ depolama sinyalleri üzerindeki hücresel etkileri aynı değildir
## 3.3.Neden Bu Kadar Çok Modele İhtiyaç Duyduk?
Basit termodinamik denklemlerin ve CICO yaklaşımının yetersizliğinin anlaşılması, araştırmacıları obezitenin altındaki gerçek biyolojik, çevresel ve evrimsel mekanizmaları aramaya itmiş ve çok sayıda modelin geliştirilmesini zorunlu kılmıştır. Bu gereksinimin temel nedenleri şunlardır:

1. **Epidemiyolojik ve Çevresel Çelişkiler:** Obezite epidemisi sadece artan kalori alımıyla açıklanamamaktadır. Örneğin, ABD ulusal verileri 2000 yılından itibaren enerji alımının plato çizdiğini veya düştüğünü, fiziksel aktivitenin ise bir miktar arttığını; ancak buna rağmen obezitenin hızla artmaya devam ettiğini göstermektedir. Bu durum, besinlerin işlenme derecesi, mikrobiyota, sirkadiyen ritim ve çevresel toksinler (ekspozom) gibi kalori-bağımsız faktörlerin metabolizmayı nasıl değiştirdiğini açıklayacak yeni teorilere (Çevresel ve Ekspozom Modelleri) ihtiyaç doğurmuştur.
2. **Bireysel ve Genetik Çeşitliliğin Açıklanması:** İkiz ve aile çalışmaları, beden kütle indeksi (BKİ) varyasyonunun %40 ila %75'inin genetik faktörlere atfedilebileceğini kanıtlamıştır. Aynı çevrede ve aynı kaloriyi alan iki insandan birinin neden obez olup diğerinin zayıf kaldığını (gen-çevre etkileşimi) açıklamak için kontrol teorilerine, genetik modellere (Thrifty, Drifty gen hipotezleri vb.) ve ayar noktası (set-point) modellerine ihtiyaç duyulmuştur.
3. **Kausalitenin (Nedenselliğin) Yönünü Belirleme İhtiyacı:** Obezitede "Çok yediğimiz için mi yağlanıyoruz (Enerji Dengesi Modeli), yoksa vücudumuz enerjiyi yağ olarak depolamaya programlandığı için mi açlık çekip çok yiyoruz (Karbonhidrat-İnsülin Modeli)?" sorusuna yanıt bulmak, obezitenin tıbbi tedavisi için hayati önem taşımaktadır
## 3.4.Enerji dengesi modeliyle açıklayamıyorsa, kalori kısıtlı diyetlerin başarısı tesadüfi mi?
Enerji kısıtlamasına dayalı diyetler tesadüfi bir başarı elde etmez; tam aksine, bu müdahalelerin sonuçları son derece öngörülebilir ve termodinamik/fizyolojik yasalara sıkı sıkıya bağlıdır.

- Vücut negatif enerji dengesine girdiğinde, hayatta kalmak ve enerji ihtiyacını karşılamak için zorunlu olarak kendi iç depolarını (önce glikojen ve su, ardından yağ ve yağsız kas kütlesi) kullanmak zorundadır. Bu, termodinamiğin doğrudan bir sonucudur.
- Geçmişte kullanılan "3500 kcal kuralı" (haftada 0.5 kg vermek için günde 500 kcal açık yaratmak) statik bir hesaplamaydı ve metabolizmanın yavaşlayacağını hesaba katmadığı için kilo kaybını abartılı tahmin ediyordu.
- Ancak günümüzde Kevin Hall ve diğer araştırmacılar tarafından geliştirilen **dinamik matematiksel modeller**, insanlardaki enerji kısıtlaması sonuçlarını olağanüstü bir doğrulukla (neredeyse %1'in altında bir hata payıyla) öngörebilmektedir. Bu modeller, kilo kaybı sırasında yaşanan yağsız kütle (kas) kaybını ve "adaptif termojenez" (metabolik yavaşlama) oranlarını diferansiyel denklemlerle hesaplayarak bireyin ne kadar kilo vereceğini, enerjinin veya kilonun girdi-çıktısını tam olarak ölçerek ortaya koyar. Dolayısıyla ortada tesadüfi bir başarı değil, çok hassas işleyen bir biyofiziksel sistem vardır.

**Başarı Sadece "Plato" Dönemine Kadar mı Sürüyor?:**
Klinik çalışmalarda, diyet veya farmakolojik müdahalelerle sağlanan kilo kaybının genellikle 6-9 ay civarında bir zirveye ulaştığı, ardından bir "plato" (duraklama) dönemine girildiği ve sonrasında kaybedilen kilonun yavaş yavaş geri alındığı (regain) görülmektedir.

Bu durumun iki temel nedeni vardır:
- **Fizyolojik Direnç (Adaptif Termojenez):** Kilo kaybedildikçe vücudun dinlenik enerji harcaması (REE) düşer, kasların çalışma verimliliği artar (daha az kalori yakarlar) ve iştah hormonları (ghrelin artarken, leptin düşer) yeme isteğini şiddetlendirir. Bu durum enerji açığını kapatarak plato evresini zorunlu kılar.
- **Davranışsal Uyumun (Adherence) Kaybolması:** Dinamik matematiksel modellerle yapılan hesaplamalar (örneğin Kevin Hall'un çalışmaları), plato evresinin sadece metabolik yavaşlamadan değil, aynı zamanda hastaların diyet programına olan **uyumlarının (adherence) zamanla azalmasından** kaynaklandığını net bir şekilde kanıtlamıştır. Hastalar altıncı haftadan itibaren gizli bir şekilde kalori alımlarını artırmaya başlarlar ve 10. aya gelindiğinde enerji alımları genellikle diyet öncesi seviyelere geri döner. Model hesaplamaları, hastalar diyete tam olarak uysaydı kilonun yıllarca (çok daha uzun süre) düşmeye devam edeceğini göstermektedir.

## 3.5.Enerji Dengesi Modelini Destekleyen Kanıtlar ve Modele Yönelik Eleştiriler
Modern EBM, basit bir "aldığın kaloriden fazlasını yak" mantığının ötesine geçerek fiziği biyoloji ile birleştirir. EBM'ye göre beyin (özellikle hipotalamus ve beyin sapı); ghrelin, leptin, GLP-1 gibi hormonlar ve vagal afferentlerden gelen sinyalleri entegre ederek vücut ağırlığını bilinçdışı bir seviyede düzenler. Obezite salgınının temel nedeni olarak da, modern çevredeki ucuz, ultra işlenmiş, yüksek enerjili ve lezzetli gıdaların beynin ödül ve iştah merkezlerini aşırı uyarması gösterilir.

Literatürde kırılma yaratan ve modern EBM'nin temelini oluşturan iki ana dalga çalışma vardır:

1. **Leibel, Rosenbaum ve Hirsch'in 1995 tarihli çalışması:** Vücut ağırlığındaki değişime karşı vücudun gösterdiği hücresel ve metabolik direnci (adaptif termojenez) ilk kez bu kadar net kanıtlamıştır. Kişiler başlangıç kilolarının %10 altına veya üstüne çıkarıldığında, dinlenik olmayan enerji harcamalarının (NREE) ve kas çalışma verimliliklerinin kaybettikleri/aldıkları kütleyle açıklanamayacak kadar radikal şekilde değiştiği gösterilmiştir.
2. **Kevin Hall ve ekibinin Dinamik Matematiksel Modelleri (2010 sonrası):** EBM'nin eksik kalan "bu sistem zamanla nasıl değişiyor?" sorusuna yanıt vermiştir. İnsanların karbonhidrat, yağ ve protein metabolizmasını; de novo lipojenez (yağ sentezi), glukoneojenez ve adaptif termojenez gibi mekanizmaları sıradan diferansiyel denklemlerle modelleyerek kilo kaybını eşi görülmemiş bir doğrulukla tahmin etmeyi başarmışlardır.

**Makrobesinlerden Bağımsız Olarak Yağ Depolanmasının Kanıtlanması**:
EBM'nin en güçlü kanıtları, insanların haftalarca kapalı metabolik koğuşlarda (metabolic ward) tutulduğu ve yedikleri her gramın, harcadıkları her kalorinin ölçüldüğü kontrollü deneylerden gelir. EBM, diyetin içeriği (yüksek karbonhidrat veya yüksek yağ) ne olursa olsun, **kaloriler eşitlendiğinde genel enerji dengesizliğinin doğrudan yağ dokusundaki değişimi belirleyeceğini** savunur. Karbonhidrat-İnsülin Modeli (CIM) gibi rakipler, yüksek karbonhidratın insülini artırarak daha fazla yağ depolatacağını iddia etse de, metabolik koğuş deneyleri **kalori kısıtlandığında yüksek karbonhidratlı diyetlerin isokalorik (eşit kalorili) düşük karbonhidratlı diyetlere kıyasla benzer veya daha fazla yağ kaybı sağladığını** net bir şekilde kanıtlamıştır. Bu durum, enerjinin yağ olarak depolanmasında belirleyici olanın spesifik hormonlardan (insülin) ziyade, toplam enerji açığı/fazlası (EBM) olduğunu destekler.

**Sadece Kiloyu Değil, "Hücresel Yakıt Seçimini" (Fuel Selection) Öngörebilmesi**:
Kevin Hall gibi araştırmacıların geliştirdiği EBM tabanlı dinamik matematiksel modeller, sadece tartıdaki ağırlığı tahmin etmekle kalmaz; vücudun iç metabolik mutfağını da simüle eder. Kanıtların gücü şuradadır: Bu modeller, diyet değiştirildiğinde vücudun **Solunum Katsayısı (RQ) değişimlerini, de novo lipojenez (karbonhidrattan yağ sentezi) oranlarını, ketojenezi ve yağ/karbonhidrat oksidasyon (yakılma) hızlarını** inanılmaz bir doğrulukla öngörür. Örneğin, diyetteki yağ oranı artırıldığında model, vücudun yakıt seçimini değiştirerek karbonhidrat yakmayı ne hızla bırakıp yağ yakmaya geçeceğini gün gün ve gram gram doğru tahmin etmiştir. Bu durum, modelin sadece fiziksel kalorileri değil, insan metabolizmasının endokrin ve biyokimyasal adaptasyonlarını da doğru kavradığının kanıtı kabul edilir.

**Obezitenin Nörolojik (Beyin Merkezli) ve Çevresel Temeline Dair Kanıtlar**:
Modern EBM, "insanlar bilinçli olarak çok yiyor" demez. EBM'ye göre **beyin, vücudun enerji ihtiyaçları ile çevresel uyaranları entegre ederek gıda alımını bilinçdışı bir seviyede yöneten ana organdır**. Modern kanıtlar, yüksek porsiyonlu, düşük lifli, enerji yoğun "ultra işlenmiş gıdaların" (obesojenik çevre) beyindeki ödül ve iştah merkezlerini aşırı uyararak tokluk sinyallerini (leptin vb.) baskıladığını göstermektedir. EBM, obezite salgınının suçlusu olarak tek bir makrobesini (örneğin sadece şekeri) değil, beynin gıda ödül sistemini (hedonik beslenme) manipüle eden bu modern gıda çevresini gösterir ve bu hipotez nörobiyolojik kanıtlarla güçlü şekilde desteklenmektedir.

**Bu Kanıtlar Neden Eleştiriliyor?:
Sizin de sezdiğiniz gibi, EBM'nin "başarısı" bazı bilim insanlarına göre bir illüzyondur. Francisco Arencibia-Albite gibi araştırmacılar, EBM'nin temel denklemlerinin açık termodinamik sistemlerde (insan vücudu) **matematiksel ve mantıksal olarak tutarsız** olduğunu kanıtlamıştır. EBM'nin "kilo sabitken ortalama alınan enerji, ortalama harcanan enerjiye eşittir" (3000 alındı, 3000 harcandı) şeklindeki temel varsayımı, klinik verilerle yapılan matematiksel testlerde çökmüş ve %300'lere varan hata payları vermiştir. Kütle dengesi (mass balance) teorisine göre vücut ağırlığı kaloriye değil, gıdaların fiziksel kütlesine bağlıdır; bu nedenle termodinamik EB denklemleri gerçek biyolojik nedenselliği açıklayamaz


**"3 Ayda 2 kg Kaybetmek İçin X Kalori Yakmalısın" Diyebiliyor muyuz?**

**Hayır, diyemiyoruz.** Bu tür hesaplamalar klinik pratikte uzun yıllar kullanılan ve Max Wishnofsky tarafından 1958'de ortaya atılan statik **"3500 kcal kuralına"** (1 libre/0.45 kg yağ kaybetmek için 3500 kcal açık yaratmak gerekir; veya 1 kg = ~7000-7700 kcal) dayanır.

Bu statik yaklaşımın iki devasa hatası vardır:

1. **Vücut kompozisyonunu sabit varsayar:** Kilo kaybının her zaman %75 yağ ve %25 yağsız kütleden (FFM) oluştuğunu varsayar. Oysa kilo kaybı süresince FFM kaybı %20 ile %40, yağ kaybı (FM) ise %60 ile %80 arasında sürekli değişkenlik gösterir.
2. **Enerji harcamasının sabit kaldığını varsayar:** Kalori kısıtlandığında enerji harcamasının (EE) da zorunlu (kaybedilen dokular nedeniyle) ve adaptif (adaptif termojenez nedeniyle) olarak düşeceğini göz ardı eder.

Bu nedenlerle 3500 kcal kuralı, zaman geçtikçe kişinin vereceği kiloyu devasa oranda **abartır (overestimate)**. Statik modelin aksine, bir kişi kalori açığı yarattığında sonsuza kadar kilo vermez; azalan enerji harcaması bir noktada yeni ve daha düşük enerji alımıyla eşitlenir ve kilo kaybı durur (plato).

## 3.6.Kilo Kaybını Oldukça Doğru Tahmin Edebilen Modeller ve Bileşenleri

Kilo kaybını yüksek doğrulukla öngören çalışmaların başında **Kevin Hall (2010)** ve **Diana Thomas ve arkadaşlarının (2011, 2014)** geliştirdiği dinamik matematiksel modeller (örneğin _NIH Body Weight Planner_ veya _Pennington Weight Loss Predictor_) gelir.

Bu modellerin denklemleri şu karmaşık bileşenleri aynı anda işler:

- **Vücut Kütlesi (BW) Dinamikleri:** Sadece yağ (FM) ve yağsız kütleyi (FFM) değil; aynı zamanda FFM'nin içindeki glikojen, protein, hücre içi ve hücre dışı suyu ayrı ayrı hesaplar.
- **Makrobesin Dengesi:** Karbonhidrat, yağ ve proteinin alım ile harcanma (oksidasyon) hızları arasındaki farkı sürekli günceller.
- **Toplam Enerji Harcaması (TEE) Bileşenleri:** Dinlenik Metabolizma Hızı (RMR) + Fiziksel Aktivite Harcaması (PAE) + Besinlerin Termik Etkisi (TEF) ve en önemlisi **Adaptif Termojenez (AT)**. Bu modeller, diyetin süresi uzadıkça enerji harcamasındaki yavaşlamayı diferansiyel denklemlerle (zamanın bir fonksiyonu olarak) hesaba katar.

**Herkes İçin Benzer Bir Çıktı mı Öngörülüyor?**

**Kesinlikle hayır.** Modeller, herkesin aynı kaloriyi yakarak aynı kiloyu vereceğini öngörmez. Sonuçların kişiden kişiye değişmesinin ana sebepleri şunlardır:

1. **Başlangıç Koşulları:** Başlangıç vücut ağırlığı, yağ yüzdesi, vücut suyu, yaş, cinsiyet ve fiziksel aktivite seviyesi her bireyin metabolik uyum kapasitesini değiştirir. Örneğin, başlangıçta çok daha ağır olan bireylerin (FFM'leri daha yüksek olduğu için) metabolik adaptasyonları ve dinlenik enerji harcamaları da farklılık gösterir.
2. **Metabolik Fenotipler:** İnsanlar kalori açığına verdikleri biyolojik tepki açısından genetik olarak farklıdırlar. Literatürde **"müsrif (spendthrift)"** ve **"tutumlu (thrifty)"** metabolik fenotiplerden bahsedilir. Tutumlu fenotipe sahip olanlar kalori kısıtlamasına girdiklerinde enerji harcamalarını çok daha şiddetli bir şekilde düşürürler (yüksek adaptif termojenez) ve kilo vermeye karşı daha dirençlidirler. Müsrif olanlar ise enerji harcamalarını daha az kısarak daha fazla kilo verirler.
3. **Diyete Uyum (Adherence):** Modeller, insanların reçete edilen diyete mükemmel uyduğu varsayımıyla çalıştırıldığında ile gerçek hayattaki serbest yaşam verileri arasında fark vardır. Hall'un çalışmaları, klinik dışı ortamlarda insanların 6. haftadan sonra yavaş yavaş gizli kalori alımlarını artırdığını ve 10. ay civarında diyet öncesi kalori alımlarına geri döndüklerini göstermiştir. Bu davranışsal uyum farklılıkları, aynı diyeti uygulayan iki kişinin tamamen farklı sonuçlar almasına neden olur.

# 4.TEMEL FİZYOLOJİK PARADİGMALAR VE TERMODİNAMİK MODELLER
## 4.1.Enerji Dengesi Modeli
Obezite patogenezini açıklayan modeller arasında en köklü ve literatürü en çok şekillendiren paradigma Enerji Dengesi Modeli'dir (EBM). Başlangıçta basit bir termodinamik denklik olarak ortaya çıkan bu model, günümüzde beynin enerji alımını nasıl yönettiğini açıklayan karmaşık bir nörobiyolojik çerçeveye dönüşmüştür.

**1. Fikrin Kökenleri ve Tarihsel Gelişim** Enerji dengesi kavramının temelleri, 18. yüzyılın sonlarında Antoine Lavoisier'nin kalorimetriyi icat etmesi ve oksijenin yanma ve solunumdaki rolünü keşfetmesiyle atılmıştır. W.O. Atwater'ın 1890'larda besinlerin kalori değerlerini hesaplamasının ardından, modelin klinik bir obezite teorisi olarak formüle edilmesi 1930 yılında L.H. Newburgh ve M.W. Johnston tarafından gerçekleştirilmiştir. Newburgh ve Johnston, obezitenin temelinde "her zaman harcanandan daha fazla enerji alınmasının" yattığını ve tüm obez bireylerin temel bir ortak noktası olarak "tam anlamıyla aşırı yediklerini" öne sürmüştür. On yıllar boyunca bu yaklaşım ("Kalori Girdisi = Kalori Çıktısı" veya CICO), diyet kısıtlamasına dayalı geleneksel obezite tedavisinin merkezini oluşturmuştur.

**2. Modern Hipotez ve Çalışma Mekanizmaları** Günümüzde Kevin Hall ve arkadaşları tarafından savunulan modern EBM, basit bir irade veya "bilinçli davranış" modeli değildir. Modelin temel hipotezi şudur: Beyin (özellikle hipotalamus ve beyin sapı), vücut ağırlığını düzenlemekten sorumlu birincil organdır ve bu düzenlemeyi bilinçdışı bir seviyede, karmaşık endokrin, metabolik ve sinirsel sinyaller aracılığıyla yapar.

- **Obezojenik Çevre ve Hedonik Beslenme:** EBM'ye göre, son on yıllarda obezite prevalansındaki artışın asıl nedeni değişen gıda çevresidir. Ucuz, kolay erişilebilir, yüksek porsiyonlu, yüksek yağ ve şeker içeren ancak düşük lif ve protein barındıran "ultra işlenmiş gıdalar", beynin ödül (hedonik) ve iştah merkezlerini aşırı uyarır.
- **Enerji Bölüştürme (Energy Partitioning):** EBM, vücuda alınan kalorilerin makrobesin kompozisyonundan bağımsız olarak, toplam enerji fazlasının doğrudan yağ dokusunda depolanacağını savunur ("bir kalori bir kaloridir" prensibi). İnsülin gibi hormonlar elbette aktiftir, ancak bu hormonlar enerji açığı veya fazlasına sekonder olarak organize olur ve makrobesin oranı ne olursa olsun fazla enerjinin yağ olarak depolanmasını garanti altına alırlar.

**3. Çalışma Tasarımları, Matematiksel Modeller ve Bulgular** EBM'nin gücü, kontrollü metabolik koğuş (metabolic ward) deneylerine ve dinamik matematiksel modellemelere dayanır.

- **Dinamik Diferansiyel Denklemler:** Kevin Hall, 2010 yılında karbonhidrat, yağ ve protein metabolizmasını; lipojenez, glukoneojenez ve adaptif termojenez gibi hücresel süreçleri içeren sekiz adi diferansiyel denklemden oluşan bir bilgisayar modeli geliştirmiştir.
- **Çalışma Tasarımı ve Doğrulama:** Bu modeller, Ancel Keys'in Minnesota Açlık Deneyi (yarı-açlık durumu) ve Diaz ve arkadaşlarının aşırı besleme (overfeeding) çalışmaları gibi klinik araştırmaların verileriyle test edilmiştir. Örneğin, vücut ağırlığında yaratılan %10'luk veya %25'lik enerji açığı senaryolarında, deneklerin zaman içindeki yağ ve yağsız kütle kayıpları ile metabolik yavaşlamaları (adaptif termojenez) model tarafından dışarıdan hiçbir parametre değiştirilmeden öngörülebilmiştir.
- **Makrobesin Testleri:** Hall ve ekibi, obez yetişkinleri metabolik koğuşlara kapatarak kalori eşlenmiş "düşük yağlı" ve "düşük karbonhidratlı" diyetleri karşılaştırmış ve kalori açığı aynı olduğunda diyetlerin yağ kaybı üzerinde belirgin (veya düşük yağlı diyet lehine) sonuçlar verdiğini saptamıştır.

**4. Gösterdiklerinin Bilim İçin Önemi**

- **Dinamik Kilo Kaybı Öngörüsü:** EBM, klinik pratikte onlarca yıldır kullanılan statik "3500 kcal kuralını" (haftada 0.5 kg vermek için 500 kcal açık yaratma) çürütmüştür. Statik model, metabolizmanın yavaşladığını hesaba katmadığı için kilo kaybını abartılı tahmin ediyordu. Dinamik EBM modelleri (örneğin NIH Body Weight Planner), enerji kısıtlaması sırasında değişen vücut kompozisyonu ve enerji harcamasını hesaplayarak plato evresini kesin bir doğrulukla açıklayabilmektedir.
- **Nörobiyolojik Odak:** Obeziteyi bir "karakter zayıflığı" olmaktan çıkarıp, modern gıda çevresinin beynin ödül sistemlerini (dopaminerjik döngüler) nasıl "hacklediğine" dair nörolojik bir zemine oturtmuştur.

**5. Çatışmalar ve Yöneltilen Eleştiriler** EBM, obezite araştırmalarındaki en baskın model olmasına rağmen Karbonhidrat-İnsülin Modeli (CIM) savunucuları ve Kütle Dengesi savunucuları (örneğin Arencibia-Albite) tarafından şiddetle eleştirilmektedir:

- **Totoloji (Nedensellik Eksikliği) Eleştirisi:** CIM savunucularına göre (örn. Ludwig ve Taubes), "pozitif enerji dengesi kilo aldırır" demek Termodinamiğin Birinci Yasası'nı tekrar etmekten ibarettir ve bir totolojidir. Bir kişinin ateşinin çıkmasını "vücudunun attığından daha fazla ısı üretmesiyle" açıklamak nasıl hastalığın biyolojik nedenini (enfeksiyonu) açıklamıyorsa, obeziteyi de "harcanandan fazla enerji alımıyla" açıklamak, aşırı yemeye neden olan hücresel veya hormonal itici güçleri (insülin aracılı yağ hapsolması) göz ardı eder.
- **Enerji ve Kütle Dengesinin Birbirine Karıştırılması (Matematiksel Çelişkiler):** Francisco Arencibia-Albite, insan vücudu gibi "açık" termodinamik sistemlerde enerji dengesi ile kütle (mass) dengesinin aynı şey olmadığını kanıtlamıştır. EBM denklemlerini Hall'un kendi açık metabolik koğuş verileriyle test eden Arencibia-Albite, modelde hesaplanan enerji dengesi ile gerçek enerji dengesi arasında %31 ile %399 arasında devasa göreceli hatalar bulmuştur.
- **Tip-2 Enerji Dengesi Paradoksu:** Arencibia-Albite'in matematiksel analizlerine göre, EBM'nin temel varsayımı olan "kilo sabitken enerji dengesi sıfırdır (Girdi = Çıktı)" kuralı fizyolojik bir imkansızlığa yol açar. Eğer alınan tüm enerji tam olarak harcanıyorsa, alınan tüm diyet proteini oksitlenmiş (yakılmış) demektir. Vücudun deri, saç, idrar yoluyla yaşadığı "zorunlu protein kaybını" yerine koyacak hammadde kalmayacağı için, sistem paradoksal olarak **aynı anda hem "sabit ağırlıkta" hem de "kilo kaybediyor"** konumuna düşer.
- **Pozitif Enerji Dengesinde Kilo Kaybı:** EBM her pozitif enerji dengesinin kilo alımıyla sonuçlanacağını öngörür. Ancak Arencibia-Albite'in Hall'un verilerinde yaptığı bağımsız analiz, pozitif enerji dengesinde olan bireylerin yarısının (%50) aynı anda kilo kaybettiğini ortaya koymuştur. Bu, obezite etiyolojisinin kalori hesaplarından ziyade hücresel düzeyde fiziksel madde/kütle giriş-çıkışıyla yönetildiğini (İştah Düzenlemeli Kütle Dengesi) savunanların en güçlü eleştirisidir.

## 4.2.Karbonhidrat- İnsülin Modeli
Enerji Dengesi Modeli'nin (EBM) "çok yediğimiz için yağlanıyoruz" şeklindeki nedensellik yönünü tamamen tersine çeviren Karbonhidrat-İnsülin Modeli (CIM), "yağlandığımız için çok yiyoruz" argümanını temel alır. Obeziteyi davranışsal bir enerji dengesizliğinden ziyade, hücresel düzeyde bir substrat (yakıt) bölüştürme bozukluğu olarak tanımlar.

**1. Fikrin Kökenleri ve Tarihsel Gelişim** CIM'in kökleri, 20. yüzyılın başlarına, Alman ve Avusturyalı araştırmacıların (örneğin Gustav von Bergmann) geliştirdiği "lipofili" (dokusunun yağa olan aşırı afinitesi/eğilimi) kavramına dayanır. Bu kavram, obeziteye yatkın bireylerin yağ dokusunun yağı hapsetmeye abartılı bir eğilimi olduğunu öne sürüyordu. 1950'lerde A.W. Pennington, obez bireylerin karbonhidrat oksidasyonunda hücresel bir defekt olduğunu ve diyet karbonhidratlarının insülin salgısını artırarak bu sorunu şiddetlendirdiğini savunmuştur. 1970'ler ve 1990'lar arasında Mark Friedman gibi araştırmacılar, karaciğerdeki enerji durumunun beyne giden sinyalleri belirlediğini öne sürmüştür.

Modern ve "yağ dokusu merkezli (adiposeantrik)" CIM'in ilk popüler formülasyonu 2007 yılında Gary Taubes tarafından yapılmıştır. Taubes, diyet karbonhidratlarının insülini artırarak yağı hücrelere hapsettiğini ve yağ dışı dokuları yakıtsız bırakarak açlığa ve metabolik yavaşlamaya neden olduğunu savunmuştur. 2018 ve 2021 yıllarında ise David S. Ludwig ve arkadaşları, modeli sadece yağ dokusuna ve insüline indirgenmekten çıkararak diğer hormonları (glukagon, inkretinler) ve otonom sinir sistemini de içeren daha kapsamlı, çoklu-organ sistemine dayalı güncel bir CIM formülasyonu sunmuşlardır.

**2. Modern Hipotez ve Çalışma Mekanizmaları** CIM'in temel hipotezi nedenselliğin yönünü tersine çevirmektir: Uzun vadede pozitif enerji dengesi (aşırı yeme) artan yağlanmanın nedeni değil; aksine, yağ depolamayı teşvik eden yakıt bölüştürme (fuel partitioning) değişimlerinin bir sonucudur.

- **Hormonal Yanıt ve Yakıtın Hapsedilmesi:** Yüksek glisemik yüklü (GL) gıdalar (rafine tahıllar, ilave şekerler) ve fruktoz tüketimi, insülin salgısını hızlıca artırırken glukagon salgısını baskılar. Bu durum insülin/glukagon oranını ve GIP/GLP-1 inkretin oranını yükseltir.
- **İçsel (Hücresel) Açlık Sinyali:** Yüksek insülin oranı oldukça anaboliktir; dolaşımdaki glukoz ve lipidleri hızla yağ dokusuna çeker (lipojenez) ve yağ yıkımını (lipoliz) güçlü bir şekilde baskılar. Öğünden yaklaşık 2.5-4 saat sonraki geç postprandiyal (tokluk) evresinde, kanda dolaşan toplam metabolik yakıt (glukoz, serbest yağ asitleri ve ketonlar) konsantrasyonu hızla düşer.
- **Beynin Yanıtı:** Beyin ve karaciğerdeki yakıt sensörleri bu düşüşü bir "hücresel açlık" ve enerji homeostazisine yönelik bir tehdit olarak algılar. Vücut, mevcut yakıtı korumak ve yenilemek için açlık hissini şiddetlendirir (enerji alımını artırır) ve kas çalışma verimliliğini artırıp yorgunluk hissi yaratarak enerji harcamasını (metabolik hızı) düşürür.

**3. Çalışma Tasarımları, Modeller ve Bulgular** CIM hipotezleri, nedenselliği test etmek için tasarlanmış hayvan deneyleri ve kontrollü insan beslenme çalışmalarıyla test edilmektedir.

- **Hayvan Çalışmaları (Kütle Sabitliği Tasarımı):** Sprague-Dawley sıçanlarında yapılan 18 haftalık bir çalışmada, sıçanlar makrobesinleri eşlenmiş yüksek glisemik indeksli (GI) veya düşük GI'li diyetlerle beslenmiştir. Yüksek GI grubunun daha fazla kilo almasını engellemek için kalorileri (porsiyonları) kısıtlanmıştır. 18 hafta sonunda her iki grubun vücut ağırlıkları tamamen aynı (yaklaşık 548 gr) olmasına rağmen, yüksek GI ile beslenen grupta vücut yağı %71 daha fazla çıkmış, yağsız kas kütlesi ise azalmıştır. Kalorileri kısıtlanmasına rağmen daha fazla yağ depolayan bu hayvan modeli, yağlanmanın termodinamik bir kalori fazlasından değil, hormon aracılı substrat bölüştürme defektinden kaynaklandığına dair güçlü kanıt sunmuştur.
- **İnsan Klinik Deneyleri:** Ludwig ve arkadaşları, 12 ergen üzerinde kalori eşlenmiş yüksek, orta ve düşük glisemik yüklü üç farklı kahvaltı ile çapraz geçişli (cross-over) bir çalışma yapmıştır. Yüksek GL'li öğünden sonra insülin hızla yükselmiş, glukagon baskılanmış ve yaklaşık 2.5 saat sonra kanda dolaşan yakıtlar diğer öğünlere kıyasla anlamlı derecede düşmüştür. Kontra-regülatör bir hormon olan epinefrin 4. saatte zirve yapmıştır (beynin kriz algısı). Serbest yeme (ad libitum) izni verildiğinde, denekler yüksek GL kahvaltısının ardından gelen öğünde 600-700 kcal daha fazla tüketmişlerdir.

**4. Gösterdiklerinin Bilim İçin Önemi**

- **"Bir Kalori Bir Kaloridir" (CICO) Yaklaşımının Reddi:** CIM, "bir kalori bir kaloridir" düşüncesini çürüterek, makrobesin kalitesinin (özellikle insülin yanıtını belirleyen glisemik yükün) vücudun kaloriyi nasıl kullanacağını ve depolayacağını (yakıt bölüştürmesini) değiştireceğini gösterir.
- **Diyet Müdahalelerinde Paradigma Değişimi:** CICO modeline dayalı klasik kalori kısıtlama tavsiyesi, hastanın zaten yaşamakta olduğu "hücresel açlığı" daha da derinleştirir ve sürdürülemez bir mücadeleye (metabolik yavaşlama ve şiddetli açlık) yol açar. CIM'e göre, sorunun temel çözümü kalorileri değil, insülin salgısını uyaran rafine karbonhidratları kısıtlamak ve hormonal ortamı yağ yakımına (lipolize) elverişli hale getirmektir.

**5. Çatışmalar ve Yöneltilen Eleştiriler** Kevin Hall önderliğindeki EBM savunucuları ile Ludwig ve Taubes gibi CIM savunucuları arasında literatürde keskin ve şiddetli bir bilimsel çatışma yaşanmaktadır. EBM'nin CIM'e yönelttiği temel eleştiriler ve CIM cephesinin yanıtları şunlardır:

- **Klinik Çalışmalardaki İştah Sonuçları:**
    - _EBM Eleştirisi:_ Kevin Hall'un kapalı metabolik koğuş deneyleri, bitki bazlı düşük yağlı (yüksek karbonhidratlı) bir diyetin, hayvansal bazlı ketojenik (düşük karbonhidratlı) bir diyete kıyasla insanlarda _daha az_ spontane kalori alımı sağladığını göstermiştir. Bu, yüksek karbonhidratın iştahı artıracağı yönündeki CIM tahminini doğrudan çürütür.
    - _CIM Yanıtı:_ Kısa süreli (örneğin 2 haftalık) çalışmalar kronik makrobesin etkilerini ölçmek için yetersizdir. Ketojenik diyete metabolik adaptasyonun (keton seviyelerinin stabil hale gelmesi) 3 hafta sürdüğü bilinmektedir; erken dönemdeki iştah değişiklikleri yanıltıcıdır.
- **İnsülinin Anoreksijenik (İştah Kapatıcı) Etkisi:**
    - _EBM Eleştirisi:_ CIM, hiperinsülineminin açlık yaratacağını savunur. Ancak beyne nazal yolla veya sistemik yolla uygulanan insülin, hayvanlarda ve insanlarda iştahı artırmaz, aksine iştahı baskılar.
    - _CIM Yanıtı:_ İnsülinin periferal (yağ dokusundaki) anabolik ve yağ hapsedici etkisi, santral (beyindeki) anoreksijenik etkisine baskın çıkar. Genetik veya kronik insülin infüzyonuyla hiperinsülinemi yaratılan hayvanlar, kalorileri kısıtlansa dahi obez hale gelirler. Periferal substrat bölüştürmesi merkezidir.
- **Genetik ve Beynin Rolü:**
    - _EBM Eleştirisi:_ İnsanlarda obeziteyle ilişkili genetik varyantların (örneğin FTO, MC4R) büyük çoğunluğu yağ dokusunda değil, merkezi sinir sisteminde ifade edilmektedir. Bu durum obezitenin yağ hücresi merkezli (adiposeantrik) değil, beyin ve iştah merkezli olduğunu kanıtlar.
    - _CIM Yanıtı:_ Beyin sadece iştahı değil, otonom sinir sistemi ve vagus siniri aracılığıyla tüm metabolizmayı, insülin salgısını, pankreas ve karaciğer fonksiyonlarını da kontrol eder. Genlerin beyinde ifade edilmesi, eylemin sadece gıda alımı (davranış) yönünde olduğunu kanıtlamaz; CIM'in otonom metabolik yollarıyla tamamen uyumludur.
- **Hayvan Modellerinde Yağ Diyetlerinin Etkisi:**
    - _EBM Eleştirisi:_ Farelerde karbonhidrat oranının %20'ye düşürülüp yağ oranının %60'a çıkarıldığı diyetler obeziteye yol açarken, %70 karbonhidrat içeren klasik laboratuvar yemleri obezite yapmaz. Karbonhidrat obezitenin zorunlu nedeni olamaz.
    - _CIM Yanıtı:_ Laboratuvar ortamında kullanılan yüksek yağlı kemirgen diyetleri sadece yağ açısından değil, aynı zamanda çok yüksek doymuş yağ ve şeker açısından da zengindir. Bu kombinasyon hipotalamik inflamasyona ve sistemik insülin direncine yol açarak CIM'in öngördüğü şekilde hücresel metabolik defektleri (yakıt hapsedilmesini) tetikler. Doğa ile uyumlu olmayan bu tür laboratuvar kurguları, glisemik yük hipotezini geçersiz kılmaz.
## 4.3. İştah Düzenlemeli Kütle Dengesi Modeli:
İştah Düzenlemeli Kütle Dengesi Modeli (Appetite-Regulated Mass Balance Model), Enerji Dengesi Modeli'nin (EBM) temelini oluşturan termodinamik denklemlerin insan vücuduna yanlış uygulandığını savunan ve obeziteyi "kalori/enerji" üzerinden değil, doğrudan "fiziksel madde/kütle" akışı üzerinden açıklayan bir fizik ve matematik modelidir.

**1. Fikrin Kökenleri ve Tarihsel Gelişim** Beslenme ve obezite bilimi on yıllardır Lavoisier'den miras kalan kalori ve enerji hesaplamaları üzerine kuruludur. Ancak 2020, 2022 ve 2026 yıllarında yayımlanan detaylı teorik ve matematiksel çalışmalarıyla Francisco Arencibia-Albite, bu yerleşik paradigmanın fiziksel temellerini sorgulamıştır.

Arencibia-Albite'in çıkış noktası, Termodinamiğin Birinci Yasası'nın (enerjinin korunumu) sistemin türüne göre farklı işlemesidir. İnsan vücudu; çevresiyle sadece enerji değil, aynı zamanda madde alışverişi de yapan ve nükleer reaksiyonların görülmediği "açık bir termodinamik sistemdir". Kapalı sistemlerde kütle sabit kalırken, açık sistemlerde kütle dengesi (mass balance) ile enerji dengesi (energy balance) birbirinden tamamen farklı ve bağımsız fiziksel ölçümlerdir. EBM'nin yaptığı en büyük "kategori hatası", açık bir sistemde enerji dengesizliğinin doğrudan kütle (kilo) değişimine yol açacağını varsayarak enerji dinamiği ile materyal dinamiğini birbirine karıştırmasıdır.

**2. Modern Hipotez ve Çalışma Mekanizmaları** ARMBM, vücut ağırlığı dinamiklerinin anlaşılabilmesi için enerjiden ziyade maddenin (atomların ve moleküllerin) izlenmesi gerektiğini savunur.

- **Kütle Akışı (Mass Flux) ve Fiziksel Gıda Tüketimi:** Vücut ağırlığındaki değişimler, enerji (kalori) girdisi ve çıktısı arasındaki farktan değil; vücuda giren fiziksel madde miktarı (su, makrobesinler, mineraller vb.) ile vücuttan atılan fiziksel madde miktarı (ter, idrar, dışkı, solunumla atılan karbondioksit ve su buharı) arasındaki farktan (net kütle akışından) kaynaklanır. Enerji alımı, tüketilen bu fiziksel kütlenin sadece bir özelliğidir, nedensel sürücüsü değildir.
- **İştah ve Metabolik Adaptasyonların Kütleye Etkisi:** Bu modele göre diyetin bileşimi (örneğin aşırı işlenmiş gıdalar veya makrobesin oranları), insülin gibi hormonları ve metabolik yolları etkileyerek açlık/tokluk sinyallerini değiştirir. İştah arttığında, doygunluk sağlanana kadar tüketilen "fiziksel gıda kütlesi" (mass intake) artar ve kütle dengesi kilo alımı yönünde bozulur. İştah azaldığında ise fiziksel kütle alımı düşer ve kütle dengesi kilo kaybı yönünde değişir.

**3. Çalışma Tasarımları, Modeller ve Bulgular** ARMBM'nin geçerliliğini test etmek için Arencibia-Albite, paradoksal bir şekilde, EBM'nin en büyük savunucusu olan Kevin Hall'un kusursuz kabul edilen, kapalı metabolik koğuşlarda (metabolic ward) yürüttüğü klinik araştırmaların (düşük yağlı vs. düşük karbonhidratlı diyet veya işlenmiş vs. işlenmemiş diyet çalışmaları) veri setlerini kütle dengesi formülleriyle yeniden analiz etmiştir.

- **Devasa Ölçüm Hataları:** Eğer EBM doğruysa, dolaylı kalorimetri ile ölçülen enerji dengesi ile vücut kompozisyonu değişiminden hesaplanan enerji dengesinin birbirini tutması gerekir. Ancak Arencibia-Albite'in analizleri, bu iki EBM hesaplaması arasında %31 ile %399 arasında değişen devasa bağıl (relative) hatalar olduğunu ortaya çıkarmıştır.
- **Pozitif Enerji Dengesinde Kilo Kaybı:** EBM'ye göre pozitif enerji dengesi daima kilo alımı yaratmalıdır. Ancak Hall'un açık verilerinde, metabolik koğuşta pozitif enerji dengesinde (harcadıklarından fazla kalori alan) olan bazı katılımcıların aynı anda kilo verdikleri gösterilmiştir.
- **Kütle ile İlişki:** Aynı veri setleri ARMBM'nin "kütle dengesi" çerçevesinde incelendiğinde; kalori harcamasından ziyade, su içermeyen fiziksel gıda kütlesi alımı (water-free food-mass intake) ile vücut ağırlığı değişimi arasında son derece güçlü ve sistematik bir ilişki bulunmuştur.

**4. Gösterdiklerinin Bilim İçin Önemi**

- **EBM'nin Salt Bir "Metafor" Olduğunun İddiası:** ARMBM, EBM'nin fizyolojik ve fiziksel olarak geçerli nedensel bir teori olmadığını; daha çok diyet ve kilo değişimi arasındaki ortalama korelasyonları tanımlamaya çalışan, kendi içinde tutarsız bir "muhasebe metaforu" (accounting metaphor) olduğunu öne sürer.
- **Karbonhidrat-İnsülin Modeline (CIM) Fiziksel Bir Zemin Sunması:** CIM'in hipotezleri, EBM'nin katı termodinamik kuralları içerisinde değerlendirildiğinde mantıksal çıkmazlara girmektedir. Ancak ARMBM; hormonların ve metabolizmanın iştahı değiştirerek "tüketilen kütleyi" (mass intake) nasıl kontrol ettiğini fiziksel yasalarla açıkladığı için, CIM'in iddialarının (insülinin yakıtı hapsedip hücresel açlık ve aşırı kütle alımı yaratması) EBM yerine ARMBM çerçevesinde çok daha tutarlı bir şekilde test edilebileceğini kanıtlamıştır.

**5. Çatışmalar ve Yöneltilen Eleştiriler** ARMBM, geleneksel termodinamik obezite paradigmasına açılmış tam cepheli bir savaştır ve özellikle EBM savunucuları ile sert çatışmalar içerir:

- **Tip-2 Enerji Dengesi Paradoksu:** ARMBM'nin EBM'ye yönelttiği en ölümcül matematiksel eleştiri budur. EBM'ye göre vücut ağırlığı sabit kalıyorsa, enerji dengesi mutlaka "sıfır" olmak zorundadır. Ancak Arencibia-Albite bunun imkansız olduğunu şöyle ispatlar: Eğer enerji dengesi sıfırsa ve alınan tüm enerji yakılıyorsa, diyetteki tüm protein de enerji için oksitlenmiş demektir. İnsan vücudu her gün deri, saç ve idrar yoluyla "zorunlu protein kaybı" (OPL) yaşar. Tüm protein yakıldığında bu kayıpları sentezleyecek yapıtaşı kalmaz. Sonuç olarak EBM; vücut kütlesinin hem "sabit kaldığını" hem de protein depoları tükendiği için "sürekli azaldığını" iddia eden ve çözülemeyen (unresolvable) bir mantıksal çelişki (paradoks) yaratır.
- **EBM'nin ARMBM'ye Yanıtı:** EBM savunucuları, ARMBM'nin bu eleştirilerini "fizyolojik esnekliği (dinamik dengeyi) anlamamakla" suçlar. EBM'ye göre vücut statik bir makine değildir; solunum katsayısını (RQ) ve yakıt seçimini anlık olarak değiştirir. ARMBM'nin formüllerinin, fizyolojik dengelemeleri göz ardı eden ve matematiği kasıtlı olarak imkansız sonuçlar verecek şekilde zorlayan kurgusal bir eleştiri olduğunu belirtirler. Ancak ARMBM, metabolik koğuşlardaki gerçek insan verilerini kullanarak bu eleştiriyi çürütür ve hatanın fizyolojide değil, EBM'nin "kütle ile enerjiyi birbirine eşitleyen" fizik denkleminde olduğunu yineler.

# 5.VÜCUT AĞIRLIĞI VE YAĞ DOKUSUNUN DÜZENLENMESİ İLE İLİŞKİLİ MODELLER


Enerji Dengesi (EBM) ve Karbonhidrat-İnsülin (CIM) gibi birinci bölümdeki etiyolojik modeller "neden obez oluyoruz?" sorusuna odaklanırken, Kontrol Teorisi modelleri "sistem vücut ağırlığındaki değişime nasıl direniyor?" sorusuna odaklanır. Bu modellerin kökeni, mühendislikte makine hızlarını sabitlemek için James Clerk Maxwell tarafından geliştirilen mekanik regülatörlere ve Norbert Wiener ile Arturo Rosenblueth'un "sibernetik" (negatif geri bildirim) çalışmalarına dayanır. Kontrol teorisi, vücut ağırlığının dinamik dalgalanmalara karşı matematiksel olarak nasıl savunulduğunu (adaptif termojenez ve iştah değişimleri aracılığıyla) açıklar.

James Clerk Maxwell, 1868 yılında buhar motorlarının hızını sınırlamak için icat edilen mekanik regülatörlerin (hız denetleyicilerin) işleyişini inceleyerek matematiksel kontrol teorisinin temellerini atmıştır. Bu mekanik sistemlerin özü, sistemin çıktısındaki bir değişikliğin, sisteme giren girdiyi azaltarak bir denge oluşturması, yani "negatif geri bildirim" (negative feedback) ile çalışmasıdır.

1940'lı yıllarda ise kontrol teorisinin öncüsü Norbert Wiener ve Walter B. Cannon ile çalışan fizyolog Arturo Rosenblueth, mühendislikteki bu kavramları alıp "sibernetik" adı altında biyolojiye ve fizyolojiye uyarlamışlardır. Vücut ağırlığının ve yağının düzenlenmesiyle olan doğrudan ilişkisi de burada başlar: Kontrol teorisi modelleri, insan vücudunun da tıpkı bu makineler gibi negatif geri bildirim sistemleriyle ağırlığını koruduğunu belirtir. Vücut ağırlığında veya yağ kütlesinde bir değişiklik olduğunda (örneğin kilo kaybı), bu değişim bir geri bildirim sinyali yaratır; bu sinyal de kilo kaybını durdurmak ve eski dengeye dönmek için "vücut ağırlığını düzenleyici iştahı" (açlığı) artırır ve enerji harcamasını (adaptif termojenez) düşürür. Yani mekanik mühendisliğindeki negatif geri bildirim ile vücudun diyetlere karşı gösterdiği fizyolojik direnç tamamen aynı matematiksel mantık ve denklemlerle modellenmektedir

## 5.1. Set-Point ve Settling-Point Modelleri
Obezite literatüründe homeostatik vücut ağırlığı savunmasını açıklayan en klasik ve ilk yapılandırılmış mühendislik temelli teorilerdir. İki model de negatif geri bildirime dayanmakla birlikte, referans hedefleri açısından birbirlerinden ayrılırlar.

**1. Fikrin Kökenleri ve Tarihsel Gelişim** Vücut parametrelerinin belirli sınırlar içinde düzenlenmesi (homeostazi) fikri 19. yüzyılda Claude Bernard ve Walter Cannon tarafından fizyolojiye kazandırılmıştır. Vücut ağırlığı bağlamında bu fikrin ilk yapılandırılmış hali, 1953 yılında G.C. Kennedy'nin ortaya attığı "lipostaz" teorisidir. Kennedy, hipotalamusun yağ depolarından (depot fat) gelen sinyallere göre gıda alımını düzenlediğini öne sürmüştür.

"Yerleşme Noktası" (Settling-Point) kavramı ise 1977'de Wirtshafter ve Davis tarafından, klasik Set-Point (Ayar Noktası) kavramına karşı daha basit bir alternatif olarak literatüre tanıtılmıştır.

**2. Hipotez ve Çalışma Mekanizmaları**

- **Set-Point (Ayar Noktası) Modeli:** Bu model, biyolojik sistemin genetik olarak belirlenmiş sabit bir "referans noktasına" (set-point) sahip olduğunu savunur. İdeal yağ kütlesi ile mevcut yağ kütlesi (feedback) karşılaştırılır. Eğer mevcut yağ düzeyi referans noktasından saparsa matematiksel bir "hata sinyali" (error signal) oluşur. Vücut bu hata sinyaliyle orantılı olarak denetlenen değişkenleri (kontrollü iştah ve enerji harcamasını) devreye sokarak kiloyu tekrar hedef noktaya çeker.
- **Settling-Point (Yerleşme Noktası) Modeli:** Bu modelde vücudun savunduğu sabit, değişmez bir hedefi (referans noktası) yoktur; model "basit negatif geri bildirim" üzerinden işler. Sistem; çevresel faktörler, diyet kısıtlamaları (açık döngü/open-loop girdiler) ve vücudun fizyolojik geri bildirimleri (kapalı döngü/closed-loop) nerede dengeye ulaşırsa (dinamik denge), ağırlığın oraya "oturduğunu/yerleştiğini" belirtir.

**3. Çalışma Tasarımları, Biyolojik Modeller ve Bulgular** Set-point mekanizmasının fizyolojik kanıtları ağırlıklı olarak genetik hayvan modellerinden ve açlık deneylerinden elde edilmiştir:

- **Dolaşımdaki Sinyalin Keşfi:** 1960'larda ve 1970'lerde Douglas Coleman'ın genetik olarak obez (ob/ob) ve diyabetik (db/db) farelerin dolaşım sistemlerini birleştirdiği parabiyoz deneyleri, beyin ile yağ dokusu arasında negatif geri bildirim sağlayan bir sinyalin varlığını göstermiştir. 1994 yılında Jeffrey Friedman ve ekibinin _ob_ genini (leptin hormonu) klonlaması, lipostaz teorisinin afferent geri bildirim sinyalinin (feedback) fiziksel kanıtı olmuştur.
- **Klinik Gözlemler (Reaktif Hiperfaji):** Minnesota Açlık Deneyi'ndeki (1950) veriler kullanılarak oluşturulan matematiksel modeller, bireylerin uzun süreli yarı açlık durumundan serbest beslenmeye (ad libitum) geçtiklerinde, vücut ağırlıkları ve yağ depoları başlangıç noktasına (ayar noktasına) dönene kadar iştahlarının kronik olarak açık kaldığını (reaktif hiperfaji) açıkça göstermiştir.

**4. Gösterdiklerinin Bilim İçin Önemi** Kontrol teorisi modelleri, obezite tedavisindeki en büyük sorunun klinik olarak açıklanmasını sağlamıştır: Diyetle verilen kiloların geri alınması bir "irade zayıflığı" değildir. Sistem, alt genetik sınırların altına düşüldüğünde enerji harcamasını azaltan (integral ve türevsel kontrol denklemlerine göre) adaptif termojenezi ve şiddetli bir "vücut ağırlığını düzenleyici iştahı" devreye sokarak mekanik ve amansız bir direnç göstermektedir.

**5. Çatışmalar ve Yöneltilen Eleştiriler**

- **Set-Point'e Yöneltilen Eleştiriler (Obezite Epidemisi Çelişkisi):** Eğer insan vücudunun sıkı sıkıya savunduğu bir set-point varsa, obezite salgını nasıl gerçekleşmektedir? Modern insanın yağ kütlesi neden yıllar içinde sürekli yukarı doğru kaymaktadır?. Set-point savunucuları bunu, yüksek yağlı/karbonhidratlı modern diyetlerin leptin direncine veya hipotalamik inflamasyona yol açarak beynin referans noktasını "yukarı doğru yeniden ayarlaması" ile açıklarlar.
- **Settling-Point'in Yanıtı ve Zayıf Yönleri:** Settling-point modeli bu artışı daha kolay açıklar: Çevre değiştiğinde (örneğin daha lezzetli ve enerjisi yoğun gıdalar geldiğinde), vücudun dengeye ulaştığı nokta pasif olarak yukarıya "yerleşir". Ancak J.R. Speakman'ın belirttiği üzere, settling-point modeli de vücudun açlık sonrası sergilediği şiddetli geri kazanım çabasını (reaktif hiperfaji veya enerji harcamasındaki asimetrik düşüşü) tatmin edici şekilde açıklayamaz; çünkü bu modelde kilonun pasif bir dinamik dengede kalması gerekirken, gerçekte sistem hedefine dönmek için "aktif" bir çaba sarf etmektedir.

Kontrol mekanizmalarının "sabit bir nokta mı" yoksa "pasif bir denge mi" olduğuna dair bu temel ayrım, literatürde bu sorunu çözmek için geliştirilen ve Set-point ile Settling-point'i birleştiren "Çift Müdahale Noktası (Dual-Intervention Point)" modeli gibi daha karmaşık teorilerin doğmasına zemin hazırlamıştır.

**Ortak Noktaları ve Benzerlikleri:**

- Her iki model de vücut ağırlığının ve yağ kütlesinin negatif geri bildirim mekanizmaları aracılığıyla kontrol edildiğini kabul eder.
- Her iki modele göre de çevresel veya açık döngü girdileri (örneğin kalori kısıtlaması) sabit bir seviyeye getirildiğinde, vücut ağırlığı dinamik bir eğri çizer ve en sonunda bir "dengeye" (steady-state) ulaşır.
- Her iki model de, zorunlu kilo kaybı durumlarında (açlık veya diyet), vücudun enerji harcamasını düşürüp iştahı artırarak eski kiloya dönmeye yönelik şiddetli dengeleyici (kompansatuar) yanıtlar vereceğini öngörür.

**Farklılıkları ve Savundukları Temel Fikirler:**

**1. Set-point (Ayar Noktası) Modeli:**

- **Ne Söyler:** Bu model, vücudun biyolojik ve genetik olarak önceden belirlenmiş sabit bir "referans değerine" (bir hedef kiloya veya yağ oranına) sahip olduğunu savunur.
- **Mekanizma:** Hipotalamus gibi bir beyin bölgesi, yağ dokusundan gelen mevcut geri bildirim sinyallerini (örneğin leptin seviyesini) bu "ayar noktası" ile karşılaştırır. Eğer mevcut kilonuz ayar noktasından saparsa, matematiksel bir "hata sinyali" oluşur. Vücut sadece bu hata sinyalini sıfırlamak (yani kişiyi tam olarak hedeflenen o kiloya geri getirmek) için aktif olarak iştah ve metabolizma değişiklikleri yaratır.
- **Zayıf Yönü:** Çevresel faktörlerle sürekli artan modern obezite salgınını açıklamakta zorlanır. Eğer vücudun sıkı sıkıya savunduğu genetik bir kilo hedefi varsa, popülasyonun kilosunun neden son on yıllarda sürekli ve istikrarlı olarak arttığı ("ayar noktasının" neden aniden değiştiği) net olarak açıklanamaz.

**2. Settling-point (Yerleşme Noktası) Modeli:**

- **Ne Söyler:** 1977'de Wirtshafter ve Davis tarafından önerilen bu modelde, vücudun ulaşmaya çalıştığı belirli bir genetik referans noktası (hedefi) veya hesaplanan bir "hata sinyali" yoktur.
- **Mekanizma:** Vücut ağırlığı, sadece dışarıdan gelen çevresel baskılar (besinlerin lezzeti, bolluğu, fiziksel aktivite düşüklüğü) ile vücudun bu değişimlere gösterdiği fizyolojik negatif geri bildirim direnci arasındaki matematiksel dengenin sağlandığı noktaya pasif olarak "yerleşir" veya "oturur".
- **Zayıf Yönü:** Diyet yapıldığında ulaşılan yeni kiloda, enerji dengesi sağlandığı an kişinin iştahının kapanması ve vücudun o noktaya uyum sağlaması gerektiğini öngörür. Ancak klinik deneyler, diyet yapan kişilerin yeni kilolarında kalmak için sürekli bir iştah artışı ve metabolik direnç ile mücadele ettiklerini, sistemi kendi haline bıraktıklarında eski kilolarına döndüklerini (reaktif hiperfaji) gösterir. Bu geri dönüş çabası, basit bir yerleşme noktası dengesinden ziyade bir hedefin savunulduğunu (Set-point) işaret eden veriler olarak yorumlanır.

Fizyoloji ve obezite literatüründe sıklıkla kullanılan "kontrol mekanizmaları" ve "negatif geri bildirim" kavramları, mühendislikteki kontrol teorisinden (sibernetik) biyolojiye uyarlanmış matematiksel ve mantıksal prensiplerdir. Vücudun diyetlere ve kilo değişimlerine karşı gösterdiği direnci anlamak için bu kavramların neyi ifade ettiğini şu şekilde açıklayabiliriz:

**1. Vücut Ağırlığında "Kontrol Mekanizmaları" Nelerdir?** Bir kontrol sisteminin, hedeflediği değeri savunabilmesi için sistem üzerinde fiziksel değişiklikler yapabilen mekanizmalara (efektörlere) ihtiyacı vardır. Vücut ağırlığı ve yağ kütlesi regülasyonunda sistemin kullandığı iki temel **"kontrol mekanizması" (veya kontrol edilen değişken)** şunlardır:

- **Vücut Ağırlığını Düzenleyici İştah (BW-Regulatory Appetite):** Sadece anlık kan şekeri veya mide boşluğuna yanıt veren açlık değil, vücuttaki toplam enerji depolarının (yağ kütlesinin) durumuna göre uzun vadeli enerji alımını (EI) yönlendiren iştah dürtüsüdür.
- **Adaptif Termojenez (AdEE):** Vücut ağırlığı değiştiğinde, iskelet kaslarının çalışma verimliliğini, tiroid hormonlarını ve sempatik sinir sistemi aktivitesini değiştirerek enerji harcamasını (EE) aktif olarak artıran veya azaltan metabolik hız ayarlamasıdır.

**2. "Negatif Geri Bildirim" (Negative Feedback) Ne Demektir?** Bir sistemin çıktısında (vücut ağırlığı) meydana gelen bir değişimin, sistemi, o **değişimi tersine çevirecek (muhalefet edecek) yönde** tepki vermeye zorlamasına negatif geri bildirim denir. Örneğin, kalori kısıtlaması yaparak vücut ağırlığınızı (çıktıyı) düşürdüğünüzde, bu düşüş beyne bir "geri bildirim sinyali" (örneğin azalan leptin) gönderir. Bu sinyalin **"negatif"** olmasının nedeni, beynin kilo kaybını desteklemek yerine ona _karşı çıkarak_ iştahı (kontrol mekanizmasını) artırması ve metabolizmayı (adaptif termojenezi) yavaşlatmasıdır. Amaç, değişimi durdurmak ve sistemi önceki durumuna getirmektir.

Bu mekanizmaların iki temel modelde (Set-point ve Settling-point) nasıl farklı kurgulandığı ise şu şekildedir:

**3. Set-Point (Ayar Noktası) Modelinde Negatif Geri Bildirim** Bu model, klasik bir negatif geri bildirim sistemine ek olarak **genetik olarak önceden belirlenmiş sabit bir "hedef değer" (referans noktası)** barındırır.

- **İşleyiş:** Yağ dokusundan gelen mevcut geri bildirim sinyali (örn. leptin), beyindeki bu sabit hedef (set-point) ile sürekli karşılaştırılır.
- **Hata Sinyali (Error Signal):** Eğer mevcut kilonuz bu hedef değerden saparsa (kilo alırsanız veya verirseniz), sistem matematiksel bir "hata sinyali" üretir.
- **Mekanizmanın Amacı:** Sistemdeki kontrol mekanizmaları (iştah ve termojenez), **sadece bu hata sinyalini sıfırlamak için** çalışır. Yani vücut, sizi ne pahasına olursa olsun o spesifik referans kilosuna (genetik hedefe) geri döndürmek için iştahınızı açar veya kapatır.

**4. Settling-Point (Yerleşme Noktası) Modelinde Negatif Geri Bildirim** Bu modelde ise vücudun genetik olarak savunduğu sabit bir hedefi (referans değeri) veya buna bağlı olarak hesaplanan bir "hata sinyali" **yoktur**.

- **İşleyiş:** Bu model, "basit negatif geri bildirim" (simple negative-feedback) veya dinamik denge (dynamic equilibrium) ile çalışır.
- **Mekanizmanın Amacı:** Vücudun ulaşmaya çalıştığı belirli bir kilo yoktur. Kilo aldıkça vücut kütlesinin artmasından dolayı zorunlu enerji harcaması doğal olarak artar. Aynı zamanda sistem, artan ağırlığa karşı basit bir orantısal geri bildirim (iştahı bir miktar baskılama veya harcamayı bir miktar artırma) uygulayabilir.
- **Sonuç:** Vücut ağırlığı; dışarıdan gelen itici güçler (örneğin lezzetli gıdalar nedeniyle artan kalori alımı) ile vücudun bu artan kütleyi taşımak için harcadığı enerji veya basit fizyolojik direncin **birbirini eşitlediği (dengelendiği) herhangi bir noktaya pasif olarak "yerleşir"**. Eğer çevresel koşullar değişirse (örneğin diyet bırakılırsa), kilo farklı bir noktaya doğru hareket edip orada yeni bir dengeye oturur.

Özetle; **negatif geri bildirim ve kontrol mekanizmaları**, vücudun kilo değişimine karşı gösterdiği iştah ve metabolizma direncidir. Bu direnç **Set-point modelinde** genetik bir hedefe ulaşmak için "hata sinyallerini" kullanarak çalışırken; **Settling-point modelinde** genetik bir hedef olmadan, sadece çevresel girdiler ile hücresel enerji harcamasının eşitlendiği dinamik bir denge bulmak için çalışır.

Özetle; Set-point modelinde vücut ağırlığı içerideki sabit bir biyolojik "hedefe" göre belirlenirken, Settling-point modelinde ağırlık, genetik bir hedef olmaksızın sadece çevresel girdiler ve vücudun harcama hızı arasındaki dengenin kurulduğu noktada var olur.

## 5.2. Çift Müdahale Noktası Modeli
**1. Fikrin Kökenleri ve Tarihsel Gelişim** Literatürdeki tartışmalarda, Set-point modeli diyet sonrası kaybedilen kiloların neden hızla ve şiddetle geri alındığını (reaktif hiperfaji) başarıyla açıklarken, obezite salgınında insanların nasıl olup da sürekli kilo aldığını açıklamakta zorlanıyordu. Settling-point (Yerleşme Noktası) modeli ise kilo alımını (dinamik dengeyi) açıklayabiliyor, ancak kilo kaybına karşı vücudun gösterdiği şiddetli geri dönüş çabasını açıklayamıyordu.

Bu iki zıt gözlemi matematiksel ve fizyolojik olarak uzlaştırmak amacıyla John R. Speakman ve diğer araştırmacılar tarafından Çift Müdahale Noktası Modeli (DIPM) formüle edilmiştir.

**2. Hipotez ve Çalışma Mekanizmaları** DIPM, vücudun genetik olarak savunduğu tek bir "ideal" referans noktası (set-point) olduğu fikrini reddeder. Bunun yerine, sistemin vücut ağırlığına müdahale etmediği bir **"Kayıtsızlık Bölgesi" (Zone of Indifference)** ve bu bölgeyi alttan ve üstten sınırlayan iki bağımsız eşik noktası bulunduğunu savunur:

- **Alt Müdahale Noktası (Lower Intervention Point - LIP):** Vücut ağırlığı bu sınırın altına düştüğünde, fizyolojik hayatta kalma mekanizmaları (şiddetli açlık ve adaptif termojenez) devreye girerek daha fazla kilo kaybını engeller ve ağırlığı tekrar kayıtsızlık bölgesine iter.
- **Üst Müdahale Noktası (Upper Intervention Point - UIP):** Vücut ağırlığı bu sınırın üzerine çıktığında ise aktif negatif geri bildirim mekanizmaları devreye girerek kilo alımını engellemeye çalışır ve ağırlığı aşağı doğru bastırır.
- **Kayıtsızlık Bölgesi:** LIP ve UIP arasında kalan bu bölgede vücut, enerji alımına ve harcamasına karşı hiçbir aktif fizyolojik direnç göstermez. Ağırlık, çevresel etkilere (alınan diyete ve aktiviteye) bağlı olarak bu aralıkta rastgele (dinamik bir denge halinde) serbestçe dalgalanır.

**3. Evrimsel Temeller: Hastalık ve Yırtıcı Riski Dengesi** Speakman, LIP ve UIP noktalarının birbirinden tamamen farklı evrimsel seçilim baskılarıyla oluştuğunu öne sürer.

- Geçmişte Alt Müdahale Noktasını (LIP) belirleyen şey, kıtlık (starvation) veya enfeksiyon hastalıklarına (disease) karşı hayatta kalmak için gereken minimum yağ deposu ihtiyacıydı.
- Üst Müdahale Noktasını (UIP) belirleyen evrimsel baskı ise "av olma (predation) riskiydi". Aşırı yağlanmak, eski insanı yırtıcı hayvanlardan kaçarken yavaşlatacağı için UIP bir üst sınır olarak evrimleşmişti.

**4. Gösterdiklerinin Bilim İçin Önemi (Obezite Salgınının Açıklanması)** DIP modeli, obezite salgınının modern çağda nasıl bu kadar hızlı yayıldığını rasyonel bir çerçeveye oturtur. Modelin açıklamasına göre; modern çevredeki lezzetli, enerji yoğun ve ucuz gıdalar (obesojenik çevre) bireyleri "kayıtsızlık bölgesi" içinde yukarı doğru iter. Vücut bu bölgede hiçbir direnç göstermediği için insanlar kolayca kilo alırlar. Ateşin ve silahların icadıyla insanların yırtıcı hayvanlara yem olma riski (predation risk) ortadan kalktığı için, üst sınırı (UIP) koruyan genetik baskı yok olmuş; genetik mutasyonların rastgele birikmesiyle (Drifty Gen/Sürüklenen Gen hipotezi) UIP seviyesi toplumda çok yüksek seviyelere kaymıştır. Bireylerin modern çevrede farklı seviyelerde obezite geliştirmesinin nedeni, genetik olarak UIP (üst sınır) eşiklerinin birbirlerinden farklı olmasıdır.

**5. Çatışmalar ve Yöneltilen Eleştiriler** DIP modeli, obezite fenomenlerini açıklamada başarılı olsa da matematiksel ve fizyolojik açılardan ciddi eleştiriler almıştır:

- **Nori Geary'nin Mühendislik Eleştirisi:** Geary, vücudun ağırlığı belirli bir tolerans zarfı (envelope of regulation/kayıtsızlık bölgesi) içinde tuttuğu fikrine katılır ancak bunun için sistemde iki ayrı müdahale noktasına (LIP ve UIP) gerek olmadığını matematiksel olarak kanıtlar. Kontrol teorisine göre; merkeze konacak tek bir set-point ve bu merkezden küçük sapmalarda tepki vermeyen, ancak sapma büyüdükçe şiddetlenen "doğrusal olmayan (non-linear) basit bir negatif geri bildirim sistemi" DIP modelinin ürettiği tüm sonuçları tek başına üretebilir. Geary'e göre DIP modeli, nöroendokrin kanıtı olmayan iki ayrı set-point uydurduğu için gereksiz yere karmaşıktır.
- **Speakman'ın Geary'e Yanıtı:** Speakman, mühendislikte alt ve üst sınırların genellikle aynı mekanizmayla kontrol edildiğini ancak biyolojinin bu mühendislik kurallarına uymak zorunda olmadığını belirtir. Literatürdeki mevcut veriler, LIP ve UIP'nin tek bir sistem değil, muhtemelen tamamen farklı nöroendokrin sistemler (örneğin LIP'nin leptin, UIP'nin başka bir sinyal) tarafından yönetildiğini işaret etmektedir; bu da iki bağımsız noktanın varlığını haklı çıkarır.
- **Alternatif Matematiksel Uzlaştırma Modelleri (Hall-Guo ve İşletim Noktası):** DIP modeline alternatif olarak, Kevin Hall ve J. Guo tarafından geliştirilen "Hall-Guo Modeli" ile Bar ve ekibinin "İşletim Noktası (Operating Point) Modeli" öne sürülmüştür. Bu modeller, set-point ve settling-point'i birleştirmek için iki ayrı sınır (LIP ve UIP) yaratmak yerine; "hareketli (kayabilen) bir set-point" fikrini kullanırlar. Bu yaklaşımlarda vücudun savunduğu tek bir hedef vardır, ancak bu hedef çevresel koşullar (diyet kalitesi) veya fizyolojik değişimlerle (leptin direnci) enerji harcaması ekseni üzerinde aşağı veya yukarı doğru kayabilmektedir.
**Peki Hall-Guo ve İşletim Noktası Modellerinin "Hareketli" (Sliding) Modelden Anladığı ve Farkı Nedir?** Bu modellerin literatüre kattığı devrimsel fark, ayar noktasının "neden ve nasıl kaydığını" sihirli bir genetik değişime bağlamak yerine, **iki farklı fizyolojik eğrinin kesişim noktası (matematiksel bir denge)** olarak tanımlamalarıdır:

- **Hall-Guo Modeli:** Bu modele göre ayar noktası, vücutta sabit duran bir hedef değil; **"Enerji Harcaması Eğrisi"** (kilo arttıkça harcamanın artması) ile **"Gıda Alım Yanıtı Eğrisi"nin** (kilodan saptıkça ne kadar yediğimiz) **kesiştiği noktadır**. Eğer diyetinizin kalitesi değişirse (örneğin ultra-işlenmiş gıdalar yemeye başlarsanız), "gıda alım yanıtı eğriniz" yukarı doğru kayar. Bu eğri yukarı kaydığında, harcama eğrisiyle kesiştiği nokta da (yani ayar noktanız) **harcama ekseni üzerinde dinamik olarak yukarı kaymış (sliding) olur**.
- **İşletim Noktası (Operating Point) Modeli:** Benzer şekilde Bar ve ekibi, ayar noktasını **"Diyet Eğrisi"** (belirli bir kalori verildiğinde vücudun tuttuğu yağ) ile **"İştah Eğrisi"nin** (serbest bırakıldığında ne kadar yediğimiz) kesişimi olarak tanımlar. Vücutta **leptin direnci** geliştiğinde, iştah eğrisi değişir ve bu "işletim noktası" diyet eğrisi üzerinde yukarıya doğru kayar.

## 5.3.İkili Düzenleme Hipotezi ve Gravitostat

Önceki bölümde incelediğimiz Çift Müdahale Noktası (Dual-Intervention Point - DIP) modelinin çözemediği çok büyük bir fizyolojik boşluk vardı: Vücut alt sınıra düştüğünde leptin hormonunun azalarak şiddetli bir açlık başlattığını biliyorduk, peki üst sınıra çıkıldığında vücut aşırı yağlanmayı algılayıp "dur" demek için hangi biyolojik sinyali kullanıyordu?

İşte literatürdeki en yenilikçi ve çarpıcı yaklaşımlardan biri olan **İkili Düzenleme ve Gravitostat (Dual Hypothesis and Gravitostat)** modeli, obezite araştırmalarında on yıllardır aranan bu "üst sınır sensörünün" mekanik bir temele dayandığını öne sürmektedir.

**1. Fikrin Kökenleri ve Tarihsel Gelişim** Vücut ağırlığının düzenlenmesinde yerçekimi kuvvetlerinin (gravitasyon) bir rol oynayabileceği fikri, ilk olarak 1950 yılında Royal Society Başkan Yardımcısı Charles Dodds tarafından ortaya atılmış, ancak herhangi bir deneysel kanıt sunulmamıştır. İlerleyen yıllarda hayvanların santrifüj cihazlarına konularak hiper-yerçekimine (hypergravity) maruz bırakıldığı bağımsız deneyler, artan yerçekimi yükünün kemirgenlerde vücut kütlesini azalttığını göstermiştir.

Yaklaşık 20 yıl önce araştırmacılar, hayvanların karın boşluğuna inert (etkisiz) ağırlık kapsülleri yerleştirdiklerinde hayvanların vücut ağırlıklarında düşüşler kaydetmişlerdir. Bu verileri toparlayan ve Speakman'ın Çift Müdahale Noktası modeliyle birleştirerek 2018 ve 2023 yıllarında sistematik bir teoriye dönüştüren kişiler ise John-Olov Jansson, Claes Ohlsson ve ekipleridir. Jansson ve ekibi, karada yaşayan hayvanların vücut kütlelerini algılamak için yerçekimini kullanan homeostatik bir sisteme sahip olduklarını öne sürmüş ve bu sisteme **"Gravitostat"** adını vermişlerdir.

**2. Hipotez ve Çalışma Mekanizmaları** Jansson ve ekibinin öne sürdüğü "İkili Düzenleme Hipotezi", vücut ağırlığının alt ve üst sınırlarının birbirinden tamamen farklı iki homeostatik sistem tarafından savunulduğunu belirtir:

- **Alt Sınır Regülatörü (Leptin):** Birey aşırı kilo kaybettiğinde veya aç kaldığında devreye girer. Azalan yağ dokusu kanda leptin hormonunu düşürür, bu da beyni uyararak iştahı açar ve enerji harcamasını azaltır.
- **Üst Sınır Regülatörü (Gravitostat):** Birey normal kilosunun çok üzerine çıktığında (aşırı beslenme ve yağlanma) devreye girer. Gravitostat iki ayrı mekanizmayla çalışır:
    1. **Mekanik/Enerjetik Komponent:** Klasik fizik kurallarına göre bir cismin kütlesi arttığında, yerçekimine karşı o kütleyi hareket ettirmek için harcanan kuvvet ve zorunlu enerji de artar (ΔKuvvet=Δku¨tle×g).
    2. **Sensör-Bağımlı (Osteosit) Komponent:** Asıl yenilikçi mekanizma budur. Artan yağ kütlesi, alt ekstremitelerdeki (bacaklardaki) yük taşıyan kemiklere mekanik bir eksenel basınç uygular. Kemiklerde bulunan **osteosit** hücreleri bu mekanik yük artışını hücresel bir sensör gibi algılar. Osteositler henüz tam tanımlanamayan endokrin veya sinirsel yollarla beyne sinyal göndererek iştahı baskılar ve/veya yağ yakımını tetikler.

**3. Çalışma Tasarımları, Biyolojik Modeller ve Bulgular** Hipotez, olağanüstü deneysel kurgularla test edilmiştir:

- **Ağırlık Kapsülü Deneyleri:** Farelerin deri altına veya karın boşluklarına kendi ağırlıklarının bir kısmı kadar ağır kapsüller (deney grubu) veya çok hafif kapsüller (kontrol grubu) yerleştirilmiştir. Ağır kapsül takılan farelerin, bu eklenen "yapay" ağırlığı telafi etmek için biyolojik vücut ağırlıklarını (özellikle yağ dokularını) tam da o kapsülün ağırlığı kadar erittikleri ve yeni bir dengeye oturdukları görülmüştür. Kapsüller cerrahi olarak çıkarıldığında ise fareler tekrar eski biyolojik ağırlıklarına geri dönmüşlerdir.
- **Obez vs. Zayıf Hayvan Modelleri:** Kapsül yüklemesiyle oluşan bu zayıflama (homeostatik vücut kütlesi azaltıcı) etkisi, normal diyetle beslenen zayıf farelerde zayıf kalırken; insan obezitesini taklit eden, **yüksek yağlı diyetle obezleştirilmiş farelerde çok daha şiddetli ve verimli** olmuştur. Bu bulgu, Gravitostat'ın özellikle üst sınırdaki obezite durumlarında aktive olduğunu kanıtlar niteliktedir.
- **Osteosit Deplesyonu (Hücre Yıkımı):** Eğer sensör kemiklerdeyse, kemik hücreleri yok edildiğinde sistem çökmelidir. Araştırmacılar, osteositleri genetik olarak azaltılmış farelere aynı ağırlık yüklemesini yaptıklarında, farelerin ağırlığa yanıt veremediklerini (zayıflayamadıklarını) göstermişlerdir.
- **Evrimsel Genellenebilirlik:** Posta güvercinlerinin sırtlarına vücut ağırlıklarının %5'i kadar küçük cihazlar yapıştırıldığında, kuşların da bu yüke yanıt olarak kendi biyolojik ağırlıklarını tam olarak %5 oranında düşürdükleri saptanmıştır. Bu durum, yerçekimi üzerinden kütle kontrolünün memeliler ve kuşlar gibi birbirinden çok uzak evrimsel dallarda korunduğunu işaret eder.

**4. Gösterdiklerinin Bilim İçin Önemi** Obezite araştırmalarında yıllardır yanıtlanamayan "Aşırı beslendiğimizde vücudumuz bunu neden durduramıyor veya bunu durduracak mekanizma nedir?" sorusuna somut, test edilebilir ve endokrin olmayan (mekanik) yeni bir hedef sunar. Bu model, leptin eksikliğinin obeziteye değil sadece "açlığa" yanıt verdiğini, dolayısıyla obez bireylere dışarıdan leptin vermenin (eğer birey halihazırda obez ise) neden işe yaramadığını açıklar. Zira obezlerde vücut kütlesini düşürmek leptinin değil, mekanik Gravitostat'ın işidir.

**5. Çatışmalar ve Yöneltilen Eleştiriler** Gravitostat hipotezi obezite camiasında halen yeni ve tartışmalı bir teoridir:

- **Stres Yanıtı Eleştirisi:** Diğer araştırmacılar, farelere cerrahi olarak ağır kapsül yerleştirmenin veya onları santrifüj cihazlarında döndürmenin kemikte spesifik bir homeostatik sinyal oluşturmaktan ziyade, hayvanda kronik bir "stres yanıtı" (stress response) yaratmış olabileceğini ve hayvanların sadece strese girdikleri için kilo kaybettiklerini öne sürmüşlerdir.
- **Leptin Odaklı Savunmalar:** Literatürün geleneksel çoğunluğu (özellikle EBM savunucuları), vücut ağırlığının üst sınırının korunmasında da leptinin başat bir rol oynamaya devam ettiğini, sadece bireylerin modern diyetler yüzünden "leptin direnci" geliştirdiği için bu korumanın aşıldığını savunurlar.
- Jansson ve ekibi ise, iki sistemin (Leptin ve Gravitostat) birbirinin zıttı olmadığını, farklı uçlarda çalışarak beynin entegre merkezlerine metabolik durum hakkında tamamlayıcı sinyaller gönderdiğini (İkili Hipotez) belirterek eleştirilere yanıt vermektedir.

# 6.OBEZİTE SALGININI AÇIKLAYAN EVRİMSEL GENETİK HİPOTEZLER

**Genlerimiz neden bizi bu kadar kolay obez olmaya ve orada kalmaya zorluyor?**

Evrimsel genetik hipotezler, insan genomunun yüz binlerce yıllık avcı-toplayıcı geçmişindeki seçilim baskılarıyla (kıtlık, yırtıcı hayvanlar, üreme zorlukları) şekillendiğini; ancak bu "eski genlerin" modern ve bolluk içindeki çevreyle karşılaştığında nasıl bir "evrimsel uyumsuzluk (mismatch)" yarattığını açıklamaya çalışır. Bu alanda en çok tartışılan dört temel hipotez şunlardır:

## 6.1.Tutumlu Gen (Thrifty Gene) Hipotezi

**Fikrin Kökenleri ve Hipotez:** Obezitenin evrimsel kökenlerine dair ilk ve en ünlü modeldir. 1962 yılında genetikçi James Neel tarafından ortaya atılmıştır. Neel, modern insanda diyabet ve obeziteye yatkınlığın, geçmişteki atalarımızın yaşadığı çevresel zorluklara karşı geliştirilmiş bir adaptasyon olduğunu öne sürmüştür.

- **Mekanizma:** Eski çağlarda insanlık, avın bol olduğu "ziyafet (feast)" dönemleri ile yiyecek bulunamayan "kıtlık (famine)" dönemleri arasında gidip geliyordu. Ziyafet dönemlerinde alınan fazla enerjiyi hızla yağa çevirip depolayabilen (insülin direnci ve hızlı lipojenez yeteneği olan) bireyler, kıtlık dönemlerinde hayatta kalma ve genlerini aktarma avantajına sahipti.
- **Günümüzdeki Sorun:** Bolluk ortamının sürekli hale geldiği modern çevrede, bizi eskiden hayatta tutan bu "tutumlu genler" sürekli çalışarak felaketimiz (obezite ve diyabet) haline gelmiştir.

**Eleştiriler ve Zayıf Yönleri:** John R. Speakman bu hipoteze en ciddi eleştirileri yönelten isimdir. Speakman'a göre, kıtlıklar insanlık tarihinde genetiğimizi bu kadar radikal şekillendirecek kadar sık veya ölümcül olmamıştır. Ayrıca, eğer "tutumlu gen" geçmişte herkes için hayati bir avantaj sağladıysa, bugün modern toplumdaki **herkesin** obez olması gerekirdi; oysa aynı çevrede yaşayan insanların sadece bir kısmı obezite geliştirmektedir.

## 6.2.Sürüklenen Gen (Drifty Gene) Hipotezi

**Fikrin Kökenleri ve Hipotez:** Tutumlu Gen hipotezinin açıklarını kapatmak için 2008 yılında John R. Speakman tarafından formüle edilmiştir. Speakman, obezitenin nedeninin alt sınırla (kıtlık) değil, üst sınırla (yırtıcılar) ilgili olduğunu savunur.

- **Mekanizma (Üst Sınırın Kaybolması):** Geçmişte insan vücut ağırlığının üst sınırını (UIP) belirleyen evrimsel baskı, **"yırtıcı hayvanlara av olma (predation)"** riskiydi. Aşırı yağlanmak, insanı yırtıcılardan kaçarken yavaşlatacağı için negatif bir seçilim baskısı yaratıyordu. Ancak yaklaşık 2 milyon yıl önce hominidlerin ateşi, silahları ve sosyal organizasyonu icat etmesiyle birlikte, yırtıcı hayvanlardan kaynaklanan bu ölüm riski ortadan kalktı.
- **Genetik Sürüklenme:** Üst sınırı tutan seçilim baskısı kalktığında, vücut ağırlığının üst sınırını (UIP) kontrol eden genlerde rastgele mutasyonlar birikmeye başladı. Bu genler evrimsel olarak bir avantaj sağladığı için (Tutumlu Gen) değil, sadece üzerlerindeki baskı kalktığı için rastgele **"sürüklendiler (drift)"**.

**Önemi:** Bu hipotez, toplumda neden herkesin obez olmadığını (mutasyonların rastgele dağılması nedeniyle genetik çeşitlilik oluşmasını) Tutumlu Gen modelinden çok daha iyi açıklar.

## 6.3. Mikroevrimsel Hipotez

**Fikrin Kökenleri ve Hipotez:** Joseph Fraiman ve Maciej Henneberg tarafından detaylandırılan bu yeni hipotez, obezite salgınının sadece diyet ve yaşam tarzındaki değişikliklerle değil, aynı zamanda modern tıbbın (özellikle obstetrik/doğum biliminin) insan evrimini yönlendirmesiyle de ilgili olduğunu savunur.

- **Mekanizma:** Tarih boyunca obez kadınlar için doğum yapmak son derece ölümcül bir süreçti (gebelik diyabeti, preeklampsi, iri bebek/makrozomi ve sefalopelvik disproporsiyon gibi nedenlerle). Bu durum, obeziteye yatkınlık genleri taşıyan annelerin ve bebeklerin doğum sırasında ölmesine, dolayısıyla bu genlerin popülasyondan sürekli olarak elenmesine (negatif seçilim) neden oluyordu.
- **Modern Tıbbın Etkisi:** Son 100 yılda Sezaryen doğumların, antibiyotiklerin ve modern gebelik takibinin yaygınlaşmasıyla, obez anneler ve iri bebekleri hayatta kalmaya başladı. Bu durum, obezite genleri üzerindeki amansız negatif seçilim baskısını aniden kaldırdı. Sadece birkaç nesil içinde (mikroevrimsel bir hızla), obeziteye yatkın genler popülasyonda hızla birikti ve bugünkü salgının temel itici güçlerinden biri oldu.

## 6.4.Tembel vs. Enerjik-Tutumlu (Lazy vs. Peppy-Thrifty) Hipotezi**

**Fikrin Kökenleri ve Hipotez:** Reddon ve arkadaşları (2018), obezitenin sadece "metabolik" bir tutumlulukla açıklanamayacağını; işin içine davranışsal enerji harcamasını (fiziksel aktiviteyi) da katan pleiotropik (bir genin birden fazla özelliği etkilemesi) bir yaklaşım getirdiler.

- **Mekanizma:** Bu modele göre genlerimiz bizi iki farklı "tutumlu" yola iterek yağ depolamamızı sağlayabilir:
    1. **Tembel-Tutumlu (Lazy-Thrifty) Fenotip:** Bu genetik varyantlar (örneğin Drd1, Nhlh2 gibi dopaminerjik gen mutasyonları) hem iştahı artırır hem de fiziksel aktiviteyi (hareketi) güçlü bir şekilde düşürerek enerji tasarrufu sağlar.
    2. **Enerjik-Tutumlu (Peppy-Thrifty) Fenotip:** Bu genetik varyantlar (örneğin Serotonin 5-ht(2c) mutasyonları) ise tam tersine, hayvanı veya insanı hiperaktif yapar (yiyecek arama davranışını artırır). Ancak bu yüksek enerji harcaması, devasa boyutta bir iştah artışıyla fazlasıyla kompanse edilir, böylece kişi çok hareket etse bile aşırı kalori alarak obeziteye ulaşır.

**Önemi:** Bu ayrım, klinik pratikte bazı insanların neden diyet yaparken hareket etmeyi tamamen bırakıp koltuğa çakıldığını (tembel-tutumlu direnç), bazılarının ise neden egzersiz yaptıkça doymak bilmez bir iştahla daha çok yediğini (enerjik-tutumlu direnç) evrimsel genetikle mükemmel bir şekilde açıklar.

# 7.MODERN ÇEVRE VE DAVRANIŞ OBEZİTE HİPOTEZLERİ
**1. Klasik Modellerin Modern Gıda Ortamını Açıklamadaki Yetersizliği:** Klasik makrobesin odaklı negatif geri bildirim modelleri (önceki bölümlerdeki termostat benzeri yapılar), modern gıda çevrelerinde bolca bulunan ucuz, aşırı lezzetli (hiperpalatable), kolay sindirilebilir ve enerji yoğun gıdaların obeziteye nasıl yol açtığını açıklamakta sınırlı bir kapasiteye sahiptir. Gıda alımı sadece kalori veya besin ihtiyacıyla değil; gıda ödülü (beğenme, isteme), otomatik alışkanlıklar, duygusal tepkiler ve stres gibi nöropsikolojik yapılarla da yönlendirilir. Modern "obezojenik" (obeziteye yol açan) çevrede, bu hedonik ve reaktif faktörler homeostatik sınırları kolayca aşabilmektedir.

**2. Evrimsel Uyumsuzluğun Eşitsizlikleri Açıklayamaması (Sosyal Belirleyiciler):** Evrimsel modeller (Bölüm 3) insan zihninin eski kıtlık koşullarına göre evrimleştiğini ve bugünkü modern bolluğa "uyum sağlayamadığını" (mismatch) öne sürer. Ancak eğer sorun sadece modern bolluk olsaydı, refah seviyesi yüksek ülkelerin kendi içindeki obezite oranlarında neden devasa farklar olduğunu açıklayamazdık. Obezite, genellikle ekonomik eşitsizliğin ve güvencesizliğin yüksek olduğu topluluklarda yoğunlaşmaktadır. Sosyoekonomik statü (SES), ırkçılık, damgalanma ve çocukluk çağı travmaları gibi kronik stres faktörlerinin alt sosyoekonomik gruplarda sağlıklı bir vücut ağırlığını korumayı zorlaştırdığını gösteren "Temel Neden Teorisi" (Fundamental Cause Theory) ve "Stres Süreci Modelleri" gibi sosyolojik yaklaşımlara ihtiyaç duyulmuştur.

**3. Aynı Çevrede Farklı Tepkiler (Gen-Çevre Etkileşimi):** Aynı kötü beslenme ortamına veya sosyoekonomik strese maruz kalan herkes obez olmamaktadır. Bu durum, "Diferansiyel Duyarlılık Hipotezi" (Differential Susceptibility Hypothesis) gibi modellerin gelişmesine yol açmıştır. Bu modele göre, taşıdığımız bazı genler (plastisite genleri), bizi çevresel etkilere karşı sadece "savunmasız" yapmakla kalmaz, aynı zamanda çevrenin kalitesine (örneğin; duyarsız ebeveynlik, düşük SES, obezojenik gıda çevresi veya tam tersi sağlıklı destekleyici bir çevre) ne kadar "duyarlı" olduğumuzu belirler. Yani obezite, genlerin ve çevrenin karmaşık yollarla etkileşime girmesinin bir sonucudur.

**4. Yaşam Boyu Maruziyetin (Ekspozom) Anlaşılması:** Bilim insanları, bir bireyin kilosunun sadece o gün yediği yemeğe bağlı olmadığını fark etmişlerdir. Obezitenin kökenleri; erken embriyo dönemindeki (intrauterin) anne beslenmesinden ve fetal çevreden başlar. Bireyin genetik yatkınlığı (genom), doğum öncesinden başlayarak ömür boyu maruz kaldığı fiziksel, kimyasal ve psikososyal çevrenin toplamıyla (ekspozom) etkileşime girerek nihai sağlık sonucunu (resposom) şekillendirir.

## 7.1. Protein Leverage (Protein Kaldıraç Hipotezi)

Protein Kaldıraç Hipotezi (PLH), obeziteyi kalori, yağ veya karbonhidrat fazlalığından ziyade, modern diyetlerdeki bir "eksiklik" (protein seyrelmesi) üzerinden açıklar.

**1. Fikrin Kökenleri ve Tarihsel Gelişim** PLH, kökenini insan fizyolojisinden değil, geniş çaplı evrimsel "beslenme ekolojisi" çalışmalarından alır. Hipotez, 2005 yılında David Raubenheimer ve Stephen J. Simpson tarafından, çekirgelerden farelere ve primatlara kadar birçok canlı türünün besin seçimlerini inceledikleri sırada formüle edilmiştir. Araştırmacılar, canlıların beslenirken rastgele kalori almadıklarını; spesifik makrobesin hedefleri olduğunu ve bunlar arasında en güçlü ve taviz verilmeyen hedefin "protein" olduğunu fark ettiler. Bu kavramı modern insan diyetlerine uyarladıklarında, obezite salgınının temelinde yatan yepyeni bir mekanizma keşfettiler.

**2. Hipotez ve Çalışma Mekanizmaları** Hipotezin kalbinde, tüm makrobesin iştahlarını (yağ ve karbonhidrat) domine eden güçlü bir **"protein iştahı" (protein appetite)** yatar.

- **Sabit Protein Hedefi:** İnsan vücudu, hayatta kalmak, nitrojen dengesini korumak ve doku onarımını sağlamak için günlük mutlak bir protein miktarına (örneğin günde 90 gram) ulaşmaya programlanmıştır.
- **Protein Seyrelmesi (Protein Dilution) ve Kaldıraç Etkisi:** Evrimsel geçmişimizde yediğimiz doğal gıdalarda protein, yağ ve karbonhidrat dengeli bir orandaydı. Ancak modern gıda endüstrisi, üretimi ucuzlatmak ve raf ömrünü uzatmak için gıdalara yüksek oranda rafine karbonhidrat ve yağ eklemekte, bu da gıdadaki proteinin oransal olarak düşmesine (seyrelmesine) neden olmaktadır.
- **Mekanizma (Aşırı Yeme):** Beslenmemizdeki protein yüzdesi düştüğünde, vücudumuz o genetik "mutlak protein hedefine" ulaşana kadar bizi yemeye zorlar. Hedefe ulaşmak için mecburen daha fazla yiyecek tüketiriz; ancak gıda protein açısından fakir olduğu için, ihtiyacımız olan proteini alana kadar devasa miktarda gereksiz yağ ve karbonhidrat (kalori) "kaldıracı" altında kalırız. Yani, proteini tamamlamak uğruna kaloride aşırıya kaçarız.

**3. Çalışma Tasarımları, Matematiksel Modeller ve Bulgular** Bu hipotez, hem kontrollü insan beslenme deneyleriyle hem de çok yakın zamanda nüfus verileri üzerindeki istatistiksel ve matematiksel modellemelerle test edilmiştir:

- **Klinik İnsan Deneyleri:** Gönüllüler kapalı kamplara alınarak onlara sadece %10, %15 ve %25 protein içeren (ancak lezzetleri aynı olan) diyetler sunulmuştur. Denekler serbestçe (ad libitum) yediklerinde, %10 proteinli diyeti tüketenlerin, %15 ve %25'lik diyetleri tüketenlere kıyasla günlük ortalama 300-400 kcal daha fazla enerji aldıkları görülmüştür. Vücutları, protein açığını kapatmak için toplam gıda alımını artırmıştır.
- **Nüfus Verileri ve Matematiksel Modellemeler (Senior et al., 2022):** Alistair M. Senior ve arkadaşları, PLH'nin varlığını nüfus düzeyindeki sürveyans verileriyle test etmek için matematiksel bir model geliştirmişlerdir. PLH'ye göre protein alımı, karbonhidrat ve yağ alımından çok daha katı bir şekilde düzenlendiği için; toplumdaki insanların protein alımlarındaki değişkenlik (varyans), protein dışı enerji alımlarındaki değişkenlikten çok daha düşük olmalıdır. Senior ve ekibi, log-normal dağılım ve Taylor serisi açılımlarını kullanarak geliştirdikleri formüllerle, protein alımının enerji alımından çok daha dar bir varyansa sahip olduğunu ve "protein alımının, protein dışı alıma kıyasla çok daha güçlü bir şekilde regüle edildiğini" matematiksel olarak kanıtlamışlardır. Model analizleri, diyetteki protein oranı azaldıkça toplam enerji alımının matematiksel bir zorunluluk olarak nasıl fırladığını göstermiştir.

**4. Gösterdiklerinin Bilim İçin Önemi (Kırılma Noktası)** PLH, obezite salgınına dair suçluyu tamamen değiştirerek bilimde bir kırılma yaratmıştır:

- Geleneksel Enerji Dengesi Modeli (EBM), "yağlar ve şekerler çok lezzetli olduğu için irademize yenilip onları çok yiyoruz" diyerek hedonik (haz odaklı) bir açıklama sunar.
- PLH ise "ultra-işlenmiş gıdaları (UPF) onları çok sevdiğimiz için değil, içlerinde yeterince protein bulamadığımız ve vücudumuz umutsuzca protein aradığı için fazla yiyoruz" der. Bu, obeziteyi bir "lezzet bağımlılığı" olmaktan çıkarıp, gıda endüstrisinin vücudumuzun homeostatik protein arayışını istismar etmesine (silahlaştırmasına) bağlar.

**5. Çatışmalar ve Yöneltilen Eleştiriler** Oldukça güçlü ve evrimsel temeli sağlam bir model olmasına rağmen literatürde bazı noktalarda eleştirilmektedir:

- **Hedonik Yeme Göz Ardı mı Ediliyor?** Eleştirmenler, insanların mükemmel ve yüksek proteinli bir akşam yemeği yediklerinde bile (protein hedefine fazlasıyla ulaşılmış olmasına rağmen) üzerine yüksek şekerli ve yağlı bir tatlıyı rahatlıkla yiyebildiklerini belirtirler. Yani PLH, protein hedefi dolsa bile lezzetin tek başına yaratabileceği "ödül odaklı aşırı yemeyi" tam olarak açıklayamaz.
- **EBM'nin Karşı Çıkışı:** Kevin Hall gibi Enerji Dengesi Modeli (EBM) savunucuları, protein kaldıracının geçerli bir mekanizma olduğunu kabul etseler de, bunun obezite salgınının "tek veya ana" nedeni olmadığını öne sürerler. EBM'ye göre PLH, obesojenik çevrenin (ultra işlenmiş gıdaların) bizi enerji fazlasına itmesinin (kalori artışının) alt yollarından sadece biridir; dolayısıyla EBM paradigmasıyla çelişmez, onun bir alt kümesi olarak çalışır.
- **Protein Hedefinin Esnekliği:** Bazı araştırmacılar, insan vücudunun böcekler veya kemirgenler kadar katı bir protein hedefine sahip olmadığını; protein ihtiyacının gebelik, yaşlılık veya fiziksel aktiviteye göre çok geniş bir yelpazede esneyebildiğini (adaptif olduğunu), bu yüzden "tek bir sabit hedefin" kaldıracı tetiklediği fikrinin insanda fazla basitleştirilmiş olabileceğini savunurlar.
## 7.2.Fructose Survival (Fruktoz Hayatta Kalma Hipotezi)
Fruktoz Hayatta Kalma Hipotezi, obeziteyi bir hastalık (veya irade zayıflığı) olarak değil; hayvanları kıtlık ve susuzluk gibi krizlere karşı hazırlamak için evrimleşmiş, ancak modern çevrede "aşırı uyarılmış" biyolojik bir **"hayatta kalma anahtarı" (survival switch)** olarak tanımlar. Richard J. Johnson ve ekibi tarafından 2023 yılında kapsamlı bir şekilde formüle edilen bu model, Enerji Dengesi Modeli (EBM) ile Karbonhidrat-İnsülin Modelini (CIM) hücresel düzeyde birbirine bağlamayı başarır.

**1. Fikrin Kökenleri ve Evrimsel Gelişim (Ürikaz Mutasyonu)** Modelin kökeni, kış uykusuna yatan (hibernasyon) memeliler ile uzun mesafe göç eden kuşların kıtlık öncesi dönemde nasıl hızla yağlandıklarının incelenmesine dayanır. Johnson ve ekibi, bu hayvanların yağlanma sürecinin insanlardaki "metabolik sendrom" ile (hiperfaji, insülin direnci, yağlanma, tansiyon yüksekliği) birebir aynı olduğunu fark ettiler ve buna "yağ depolama sendromu" adını verdiler.

Peki insanlar fruktoza neden bu kadar duyarlıdır? Yaklaşık 24 milyon yıl önce, Miyosen dönemindeki küresel soğuma ve kıtlıklar sırasında atalarımızda **ürikaz (uricase)** enzimi mutasyona uğrayarak yok oldu. Ürikaz, ürik asidi parçalayan enzimdir; bu enzimin kaybı, atalarımızın fruktoz yediğinde kan ürik asit seviyelerinin çok daha fazla yükselmesine neden oldu. Bu durum fruktozun yağ depolayıcı etkisini artırarak, o dönemki amansız kıtlıklarda atalarımızın hayatta kalmasını sağlayan gerçek bir "tutumlu gen" (thrifty gene) avantajı yarattı.

**2. Hipotez ve Hücresel Çalışma Mekanizmaları (ATP Çöküşü)** Bu hipotezin merkezinde fruktozun (diğer tüm besinlerden farklı olarak) hücre içindeki **aktif enerjiyi (ATP) tüketmesi** yatar.

- **ATP'nin Hızla Tüketilmesi:** Fruktoz hücreye girdiğinde _fruktokinaz C (KHK-C)_ enzimi tarafından hızla fosforile edilir. Ancak bu enzimin, glukoz metabolizmasından farklı olarak, ATP düşüşünü durduracak bir "negatif geri bildirim" freni yoktur. Sonuç olarak hücre içi ATP ve fosfat seviyeleri hızla dibe vurur.
- **Ürik Asit ve Mitokondriyal Kapatma:** Düşen fosfat, AMP deaminaz-2 (AMPD2) enzimini uyararak AMP'yi yıkar ve hücrede devasa miktarda **ürik asit** üretilmesine neden olur. Hücre içindeki bu ürik asit artışı, mitokondrilerde oksidatif stresi tetikleyerek yağ asidi oksidasyonunu (beta oksidasyon) durdurur ve enerji sensörü olan AMP-kinaz'ı (AMPK) baskılar.
- **Sahte Kıtlık (Low Power Mode):** Mitokondriler oksijenli enerji üretimini kestiğinde hücre "Warburg etkisi"ne (glikolize) geçer. Ortada bolca kalori (şeker/yağ) dolaşıyor olmasına rağmen, hücrenin içindeki aktif enerji (ATP) düştüğü için beyin bunu bir **"kriz ve kıtlık durumu"** olarak algılar. Hayatta kalmak için şiddetli bir iştah, su arama dürtüsü (foraging) başlatır ve metabolizmayı yavaşlatarak gelen tüm kalorileri yağa çevirip hapseder.

**Görünmez Tehlike: İçsel (Endojen) Fruktoz Üretimi** Hipotezin en sarsıcı yanı şudur: Sadece dışarıdan fruktoz (meyve veya mısır şurubu) yemenize gerek yoktur. Vücudumuz **"Poliol Yolağı"** (Aldoz redüktaz enzimi) aracılığıyla glukozu kendi kendine fruktoza çevirebilir. Yüksek glisemik indeksli karbonhidratlar (şeker dalgalanması), tuzlu gıdalar, alkol, susuzluk (hiperozmolarite) ve hatta umami/pürin içeren gıdalar (kırmızı et, işlenmiş etler) karaciğerde ve beyinde endojen fruktoz üretimini şiddetle tetikleyerek bu sahte kıtlık anahtarını açar.

**3. Çalışma Tasarımları, Biyolojik Modeller ve Bulgular**

- **KHK-Nokavt (Fruktokinazı Olmayan) Fareler:** Glukoz (şeker) verilen normal fareler ciddi şekilde obez olup yağlanırken, fruktozu metabolize edemeyen KHK-nokavt farelere aynı glukoz verildiğinde obezite, yağlı karaciğer veya insülin direnci geliştirmezler. Bu durum, şekerin asıl zararının insülinden ziyade, vücudun o şekeri _fruktoza çevirmesinden_ kaynaklandığını kanıtlar.
- **Eşit Kalorili (Pair-feeding) ve Hipokalorik Diyet Deneyleri:** Fruktozun etkisinin sadece "fazla kalori" almak olmadığını kanıtlamak için, farelere _hipokalorik (kalori açığı olan)_ fruktozlu diyetler verilmiştir. Fareler kilo almamalarına rağmen şiddetli yağlı karaciğer, insülin direnci, hipertrigliseridemi ve yüksek tansiyon (metabolik sendrom) geliştirmişlerdir. Bu da fruktozun kalori fazlasından bağımsız olarak doğrudan doku hasarı ve yakıt hapsi yaptığını gösterir.
- **Vazopressin ve Susuzluk (V1b Reseptörü):** Fruktoz, böbreklerden su tutmak için vazopressin hormonunu uyarır. Araştırmacılar, vazopressin V1b reseptörü genetik olarak silinmiş farelerin fruktoz kaynaklı metabolik sendromdan tamamen korunduğunu bulmuşlardır.

**4. Gösterdiklerinin Bilim İçin Önemi (Büyük Uzlaşma / Kırılma Noktası)** Fruktoz Hipotezi, birinci bölümde birbiriyle savaşan Enerji Dengesi Modeli (EBM) ile Karbonhidrat-İnsülin Modelini (CIM) mükemmel bir şekilde birbirine bağlayarak literatürde bir kırılma yaratmıştır:

- _CIM'e Açıklama Getirir:_ CIM, "yüksek glisemik indeksli karbonhidratlar insülini artırıp bizi yağlandırır" diyordu. Fruktoz hipotezi bunu bir adım ileri götürür: Yüksek glukoz (karbonhidrat), poliol yolağıyla karaciğerde fruktoza dönüşür; hücresel ATP'yi çökerten, yağlanmayı ve insülin direncini asıl başlatan şey bu fruktozdur.
- _EBM'ye Açıklama Getirir:_ EBM, "beynimiz çok yememizi emrettiği (pozitif enerji dengesi) için kilo alıyoruz" diyordu. Fruktoz hipotezi bu aşırı yemenin biyolojik nedenini gösterir: Fruktoz metabolizması haftalar içinde beyinde **merkezi leptin direncine** yol açar. Leptin direnci gelişen vücut, tokluk sinyallerini kaybeder ve tam da EBM'nin öngördüğü gibi kronik olarak fazla kalori (özellikle de yağ) almaya başlar.

**5. Çatışmalar ve Yöneltilen Eleştiriler** Bu hipotez her şeyi kusursuz açıklıyor gibi görünse de literatürde bazı sınırlılıkları ve çelişkileri nedeniyle eleştirilmektedir:

- **Ketojenik Diyet Paradoksu:** Fruktoz hipotezi, ürik asit yüksekliğinin ATP'yi çökertip yağlanmayı başlattığını söyler. Ancak çok düşük karbonhidratlı ketojenik diyet uygulayan kişilerde, ketonların böbrekten ürik asit atılımını engellemesi nedeniyle _kanda ciddi hiperürisemi (ürik asit yüksekliği) görülür_. Modele göre bu kişilerin yağ depolaması gerekirken, aksine hızla kilo verirler. Hipotez savunucuları bunu, karbonhidrat yokluğunda (açlık/keto durumunda) fruktozun yağa değil glukoza (enerjiye) dönüştürülmesiyle ve ketonların anti-inflamatuar etkisinin ürik asit hasarını engellemesiyle açıklarlar, ancak bu alan hala tam çözülememiştir.
- **Doymuş Yağların Bağımsız Etkisi:** Hipotez obezitenin ana motorunu fruktoza (ve glukozdan fruktoz üretimine) bağlasa da, fruktoz metabolize edemeyen (KHK-nokavt) farelere yüksek doymuş yağlı (tereyağı vb.) diyet verildiğinde fruktoz olmadan da hafif obezite ve karaciğer yağlanması geliştirebildikleri görülmüştür. Bu, yağların fruktoz yardımı olmadan da lipolizi baskılayıp karaciğere yüklenerek (ikincil bir mekanizmayla) obezite yapabileceğini gösterir.

**Özetle:** Fruktoz Hayatta Kalma Hipotezi; obeziteyi, şekerin, tuzun ve işlenmiş gıdaların hücredeki ATP'yi "kısa devre yaptırarak" vücuda sahte bir kış/kıtlık alarmı verdirmesi olarak açıklar. Kilo almamız, evrimin bize krizde hayatta kalalım diye verdiği bu eşsiz savunma sisteminin, modern süpermarketlerde üzerimize dönüp kendi biyolojimizi hacklemesinin bir sonucudur.

## 7.3.Insurance  (Sigorta Hipotezi)
Sigorta Hipotezi, ilk bakışta tamamen mantıksız görünen bir halk sağlığı gerçeğini açıklar: **Neden dünyanın en zengin ülkelerinde, gıdaya erişimi en kısıtlı ve en fakir olan insanlar en yüksek obezite oranlarına sahiptir?** (Açlık-Obezite Paradoksu),.

Bu model, obeziteyi aşırı bir gıda bolluğunun lüksü olarak değil, aksine **"gıdasız kalma korkusuna ve güvencesizliğine" karşı bedenin geliştirdiği çaresiz bir hayatta kalma (sigorta) stratejisi** olarak tanımlar.

**1. Fikrin Kökenleri ve Tarihsel Gelişim** Besin güvencesizliğinin (food insecurity) obeziteye yol açabileceği fikri klinik literatürde ilk olarak 1995 yılında W.H. Dietz tarafından "aralıklı gıda yetersizliğine karşı adaptif bir yanıt" olarak öne sürülmüştür,. Ancak hipotezin sağlam bir evrimsel ve matematiksel temele oturtulması, 2017 yılında Daniel Nettle, Clare Andrews ve Melissa Bateson tarafından gerçekleştirilmiştir,.

Nettle ve ekibi, bu teoriyi insanlardan ziyade 1980'lerden beri **davranışsal ekoloji** literatüründe bilinen kuş deneylerinden (örneğin sığırcıklar ve baştankaralar) kurgulamışlardır,. Doğada küçük kuşlar, kış aylarında besin bulma olasılıkları "öngörülemez" (unpredictable) hale geldiğinde, aniden hayatta kalmak için vücut yağlarını artırırlar. Bu adaptif ilke, modern insan toplumlarına uyarlandığında obezite sosyolojisini açıklayan güçlü bir modele dönüşmüştür.

**2. Hipotez ve Çalışma Mekanizmaları** Hipotezin kalbinde yatan mantık son derece nettir: Vücut yağı, gıdanın bulunamadığı dönemlerde enerji açığına karşı evrimsel bir **"sigorta poliçesi"dir**. Ancak yağ taşımanın metabolik maliyetleri, hareket kabiliyetini (yırtıcılardan kaçmayı) azaltması ve hastalık riski gibi ciddi bedelleri vardır.

- **Dinamik Optimizasyon:** Evrimsel olarak, bir canlının taşıması gereken "optimum yağ miktarı", gıdaya erişiminin ne kadar öngörülemez (güvencesiz) olduğuna bağlıdır. Gıda güvenliği yüksekse, sistem minimum yağ depolar,. Ancak besin arzı tehlikeye girdiğinde, beynin "Ayar Noktası" (set-point) veya hedef kilosu, açlıktan ölme riskine karşı sigorta yapmak için otomatik olarak daha yüksek bir yağ seviyesine kayar,.
- **Mekanizma (Metabolik Kaydırma ve Hiperfaji):** Gıda güvencesizliği (FI) algılandığında beyin, anlık bir hiperfaji (aşırı yeme) tetikler. Ancak tek mekanizma yemeği artırmak değildir. Vücut, elindeki kısıtlı enerjiyi "somatik bakımdan" (hücre onarımı vb.) çalarak acil bir şekilde "yağ depolarına" yönlendirir (enerji harcamasını kısar). Bu, gıda güvencesizliği yaşayan toplumlarda neden obezitenin yanı sıra erken yaşlanma ve hastalıklara yatkınlığın da arttığını açıklar,.

**3. Çalışma Tasarımları, Modeller ve Bulgular** Bu hipotez hem teorik matematikle, hem hayvan deneyleriyle hem de devasa insan meta-analizleriyle test edilmiştir:

- **Dinamik Matematiksel Modeller:** Nettle ve ekibi, bir bireyin her dönemde gıda bulma olasılığını (p) modelleyen bilgisayar simülasyonları yaratmışlardır. Model, gıda bulma güvencesi (p) düştükçe, sistemin hayatta kalma şansını maksimize etmek için otomatik olarak "hedef yağ rezervlerini" yukarı çektiğini (yani bireylerin daha ağır hale geldiğini) kusursuz bir matematikle ispatlamıştır,.
- **Hayvan Deneyleri:** Sığırcık kuşlarına laboratuvarda gıda bir gün verilip bir gün rastgele kesildiğinde (öngörülemezlik yaratıldığında), kuşların kontrol grubuna kıyasla hızla yağlandıkları ve vücut ağırlıklarını artırdıkları görülmüştür. Yakın tarihli bir başka çalışmada (Gil ve ark., 2025), farelere aralıklı oruç ve kalori kısıtlaması (gıda güvencesizliği simülasyonu) uygulandığında; fareler standart diyetle beslenirken bile yağ kütlelerini artırmış ve yağsız (kas) kütlelerini kaybetmişlerdir,. Bu, güvencesizliğin doğrudan yağ depolamaya yönelik metabolik bir adaptasyon (yakıt bölüştürme) başlattığını kanıtlar.
- **İnsan Psikolojisi ve Meta-Analizler:** İnsanlara küresel ısınma nedeniyle "gelecekte gıda kıtlığı yaşanacağını" anlatan haber videoları izletilen psikolojik deneylerde, özellikle kadın katılımcıların anında daha yüksek kalorili ve enerji yoğun gıdaları tercih etmeye başladığı (beklenen kıtlık sinyali) gösterilmiştir,. 125 çalışmayı içeren devasa bir meta-analizde ise, özellikle yüksek gelirli ülkelerde gıda güvencesizliği yaşayan kadınların obez olma ihtimalinin çok daha yüksek olduğu istatistiksel olarak kesinleşmiştir,,.

**4. Gösterdiklerinin Bilim İçin Önemi (Kırılma Noktası)** Sigorta Hipotezi, klinik obezite tedavisine yaklaşımda felsefi bir devrim yaratır:

- Obeziteyi "bireysel bir irade zayıflığı" veya "bilgisizlik" olmaktan çıkarıp, yoksulluğun ve güvencesizliğin yarattığı derin bir yapısal soruna bağlar.
- **Diyetlerin Çöküş Nedeni:** Eğer bir hastanın beyni "bir sonraki kaliteli öğünün nereden geleceğini" bilmiyorsa (ekonomik stres), bu beyin kıtlık modundadır. Siz bu hastaya "kalorilerini kısıtlamasını" (diyet yapmasını) söylediğinizde, hastanın beyni bunu _beklenen kıtlığın kanıtı_ olarak algılar ve sigorta mekanizmasını daha da şiddetlendirerek yağı daha sıkı hapseder. Hipoteze göre, bu popülasyonların ihtiyacı olan şey "daha az gıda" veya diyet listeleri değil, aksine hayatlarında **"daha fazla ve güvenilir gıda erişimidir (food security)"**,.

**5. Çatışmalar ve Yöneltilen Eleştiriler** Evrimsel ve mantıksal olarak çok güçlü olmasına rağmen, insan epidemiyolojisindeki bazı tutarsızlıklar nedeniyle tartışma konusudur:

- **Cinsiyet Uçurumu:** Yüksek gelirli ülkelerde gıda güvencesizliği ile obezite arasındaki ilişki kadınlarda son derece güçlü ve tutarlıyken, erkeklerde ve çocuklarda çok zayıftır veya yoktur,. Hipotez, kadınların üreme için asgari bir yağ rezervine ihtiyaç duymaları gibi nedenlerle bu duruma evrimsel kılıflar bulmaya çalışsa da, modelin erkekleri neden aynı şekilde etkilemediği halen tam bir muammadır ve eleştirmenlerin en güçlü silahıdır,.
- **Gelir Düzeyi Farkı:** Yüksek gelirli ülkelerde (ABD, Avrupa) gıda güvencesizliği obezite yaparken; düşük gelirli ülkelerde (örneğin Sahra Altı Afrika) gıda güvencesizliği beklendiği gibi "zayıflık" (underweight) yaratır. Çünkü düşük gelirli ülkelerde "güvencesizlik", doğrudan mutlak bir kalori yokluğu anlamına gelir ve sigorta mekanizmasını çalıştıracak kadar bile gıda yoktur.
- **Biyolojik Adaptasyon mu, Ucuz Gıda mı?** Birçok araştırmacı (EBM savunucuları), yoksul insanların "kıtlık evrimi" nedeniyle değil; sadece sağlıklı taze gıdalara (sebze, et) paraları yetmediği ve bütçeleriyle alabilecekleri tek şeyin ucuz, bol şekerli, ultra-işlenmiş (UPF) gıdalar olduğu için obez olduklarını savunur (Food Desert / Gıda Çölü teorisi). Nettle ise, UPF tüketiminin ve diyet kalitesizliğinin de aslında "gıda güvencesizliğine" karşı bedenin ucuz enerji arayışının bir parçası olduğunu söyleyerek yanıt verir,.

Özetle Sigorta Hipotezi; beynimizin çevresel stresi ve yoksulluğu nasıl bir "kıtlık tehdidi" olarak okuduğunu ve bizi hayatta tutmak için paradoksal bir şekilde nasıl obeziteye sürüklediğini gösteren, obezitenin sosyal belirleyicilerini (social determinants of health) evrimsel biyolojiyle birleştiren harika bir sentezdir.

## 7.4.Exposome (Ekspozom Hipotezi)
Ekspozom Hipotezi, obeziteyi basit bir "kalori" veya "makrobesin" sorunu olmaktan çıkarıp; modern insanın doğum öncesinden ölümüne kadar maruz kaldığı fiziksel, kimyasal, biyolojik ve psikososyal çevrenin toksikolojik bir birikimi olarak ele alır.

**1. Fikrin Kökenleri ve Tarihsel Gelişim** İnsan genomunun haritalanmasındaki büyük başarının ardından, bilim insanları genetiğin (SNPs - tek nükleotid polimorfizmleri) obezite gibi hastalıkları açıklamada tek başına yetersiz kaldığını fark ettiler. Genlerimiz son 100 yılda değişmemişti ancak obezite görülme sıklığı muazzam bir hızla artıyordu. Dahası, sadece insanlar değil; evcil hayvanlar, laboratuvar hayvanları ve insanla aynı ortamı paylaşan vahşi hayvanlarda da eşzamanlı bir "çoğul obezite salgını" (plurality of epidemics) yaşanıyordu. Bu hayvanlar ne diyet trendlerinden etkilenmiş ne de bilgisayar başında oturmuşlardı.

Bu durum, çevremizde biyolojimizi derinden değiştiren görünmez faktörler olduğu fikrini doğurdu. "Ekspozom" kavramı, bireyin anne karnına düştüğü andan (konsepsiyon) yaşlılığına kadar tüm yaşamı boyunca maruz kaldığı bütün çevresel faktörlerin (toksinler, diyet, stres, kirlilik) toplamını ve bunun hastalıklarla ilişkisini tanımlamak için literatüre kazandırılmıştır.

**2. Hipotez ve Çalışma Mekanizmaları** Ekspozom hipotezi, obeziteye yatkınlığın, genetik altyapımız (genom) ile yaşam boyu maruz kaldığımız bu kimyasal ve fiziksel çevrenin etkileşime girerek verdiğimiz fizyolojik yanıt (resposom) üzerinden şekillendiğini savunur. Hipotezin merkezinde şu mekanizmalar yatar:

- **Obezojenler ve Endokrin Bozucu Kimyasallar (EDC'ler):** Plastiklerdeki Bisfenol A (BPA), ftalatlar, tarım ilaçları, kozmetiklerdeki kimyasallar, alev geciktiriciler ve ağır metaller vücudumuza girdiğinde hormonlarımızı taklit eder veya bloke ederler. Bu kimyasallar doğrudan hücresel düzeyde _PPAR-_γ ve _RXR_ gibi nükleer reseptörleri aktive ederek, kök hücrelerin zorunlu olarak yağ hücresine (adiposite) dönüşmesine (adipogenez) ve yağ hücrelerinin çoğalmasına neden olurlar. Ayrıca yağ yakımını (lipolizi) sağlayan mekanizmaları baskılarlar.
- **Epigenetik Programlama ve DOHaD Paradigması:** Hastalıkların Gelişimsel Kökenleri (DOHaD) paradigmasına göre, fetüs anne karnındayken maruz kalınan obezojenler, annenin stresi veya kötü beslenmesi, DNA'nın dizilimini değiştirmeden onun "nasıl okunacağını" (DNA metilasyonu vb. yollarla) kalıcı olarak değiştirir (epigenetik). Bu durum çocuğu ömür boyu obeziteye yatkın hale getirir.
- **Kentsel Planlama ve İklim Değişikliği:** Ekspozom sadece kimyasallardan ibaret değildir. Yaşadığımız mahallenin hava kirliliği, trafik gürültüsü, yeşil alan eksikliği ve sağlıklı gıdaya erişim zorluğu fizyolojimizi doğrudan etkiler. Ayrıca küresel ısınma ve sürekli klima/kalorifer ile kontrol edilen termonötral evlerde yaşamak, vücudumuzun ısı üretmek (termojenez) için enerji harcamasını gereksiz kılarak kahverengi yağ dokusunu (BAT) köreltir ve kilo alımını kolaylaştırır.

**3. Çalışma Tasarımları, Biyolojik Modeller ve Bulgular** Ekspozom çok boyutlu olduğu için biyolojik kanıtları da hayvan deneylerinden insan "big data" (büyük veri) analizlerine kadar uzanır:

- **Transjenerasyonel (Nesiller Arası) Hayvan ve İnsan Çalışmaları:** Hayvanlarda yapılan deneyler, anne karnında obezojenlere (örneğin EDC'lere) maruz kalmanın etkilerinin, epigenetik yollarla 4. nesle (F4) kadar aktarılabildiğini göstermiştir. İnsanlarda ise, ABD'de 1972'de yasaklanan DDT böcek ilacına maruz kalan büyükannelerin torunlarında, obezite ve erken menarş (ilk adet) riskinin belirgin şekilde arttığı 2021 yılında devasa bir kohort çalışmasıyla kanıtlanmıştır.
- **Mikroplastikler ve Mikrobiyom Araştırmaları:** Hem çevredeki mikroplastiklere maruziyetin hem de ultra işlenmiş gıdaların, bağırsak mikrobiyomunun mimarisini değiştirerek enerji emilimini artırdığı ve obeziteye yol açtığı klinik olarak gösterilmiştir.
- **Makine Öğrenmesi (AI) Destekli Çevre Analizleri:** Çok yakın tarihli çalışmalar, bireylerin yaşadığı adreslerin coğrafi verilerini, trafik gürültüsünü, ev fiyatlarını ve havadaki partikül madde oksidasyon kapasitesini aynı anda analiz eden algoritmalar kullanarak; kötü kentsel "ekspozomun" sosyodemografik özelliklerden bağımsız olarak BMI artışıyla tutarlı bir şekilde ilişkili olduğunu saptamıştır.

**4. Gösterdiklerinin Bilim İçin Önemi (Kırılma Noktası)** Ekspozom hipotezi, obezite sorununu bireyin omuzlarına yüklenen "az ye, çok hareket et" (EBM) suçlamasından tamamen kurtarır. Obezitenin aslında kirlenmiş bir çevrenin, bozuk bir gıda sisteminin ve toksik kimyasalların insan biyolojisi (ve epigenetiği) üzerindeki acımasız bir istilası (syndemic/sindemi) olduğunu gösterir.

Bilimsel açıdan bu paradigma, tıp dünyasını politika yapıcılara (hükümetlere) yönlendirmiştir. Örneğin, Avrupa Birliği'nin REACH (kimyasalların kaydı ve kısıtlanması) regülasyonunun yetersiz kaldığını; obezojenik kimyasalların (EDC'lerin) en düşük dozlarda dahi, özellikle hamilelerde ve bebeklerde, kalıcı hasarlar ve nesiller boyu sürecek obezite yarattığını vurgulayarak uluslararası sağlık politikalarının acilen değiştirilmesini talep eden devasa bilimsel dilekçelerin ortaya çıkmasını sağlamıştır.

**5. Çatışmalar ve Yöneltilen Eleştiriler** Bu hipotezin zayıf noktası, savunduğu şeyin yanlış olmasından değil, **matematiksel ve analitik olarak ölçülmesinin neredeyse imkansız olmasından** kaynaklanır:

- **Korelasyon vs. Nedensellik Çıkmazı:** İnsanlar gerçek hayatta tek bir kimyasala değil, aynı anda binlerce kimyasala, strese ve kötü diyete (kokteyl etkisi) maruz kalırlar. Hangi obezojenin, tam olarak hangi "kritik pencerede" (örneğin hamileliğin 3. ayında mı yoksa ergenlikte mi?) obeziteyi tetiklediğini saptamak ve bir doz-yanıt ilişkisi kurmak epidemiyolojik olarak son derece zordur.
- **Ölçüm ve Veri Zorlukları:** Genomumuz hayatımız boyunca sabitken (ölçmesi tek sefere mahsustur), ekspozomumuz her saniye değişir. Araştırmacıların, bireyin anne karnından itibaren maruz kaldığı her şeyi ölçebilecekleri "ekspozom veritabanlarına" ve standart bir terminolojiye (tıpkı genom projelerindeki gibi) henüz sahip olmamaları en büyük engeldir.

# 8.VÜCUT AĞIRLIĞI MODELLERİ VE OBEZİTE HİPOTEZLERİNE GÖRE İDEAL BİR DİYET NASIL OLMALIYDI?

Vücut Ağırlığı Modelleri ve Obezite Hipotezlerine Dayanarak Geliştirilen İdeal Diyet Modeli

# 9.SOSYAL TEORİLER
## 9.1.Yaşam Boyu Teorisi (Life Course Theory) ve Birikimli Eşitsizlik
Bu teori, obezitenin temelinin genellikle çocuklukta atıldığını ve bireyin yaşamı boyunca maruz kaldığı sosyal ve ekonomik dezavantajların zamanla "birikerek" (cumulative disadvantage) obeziteye yol açtığını savunur.

- **Bağlantılı Hayatlar (Linked Lives):** Kişinin vücut ağırlığı yörüngesi sadece kendisine değil; ailesinin, arkadaşlarının ve içinde bulunduğu sosyal ağın yörüngesine de bağlıdır.
- Düşük sosyoekonomik statüye (SES) bağlı kronik stresörler, zaman içinde biyolojik işleyişi bozarak bedenin uzun vadeli bir dezavantaja "aşırı kilo" ile yanıt vermesine neden olur.

## 9.2.Temel Neden Teorisi (Fundamental Cause Theory)
Link ve Phelan tarafından geliştirilen bu teori; **sosyoekonomik statü (SES), ırkçılık ve sosyal damgalanmayı (stigma)** hastalıkların ve obezitenin "temel nedenleri" olarak tanımlar.

- **Mekanizma:** Yüksek sosyal sınıflara mensup bireyler, obezite risklerinden kaçınmak veya tedavi olmak için gerekli kaynaklara (para, bilgi, güvenli çevre, güç) sahiptir. Alt sosyoekonomik gruplar ise bu koruyucu kaynaklardan yoksundur; dolayısıyla genetikleri veya metabolizmaları ne olursa olsun, obezite geliştirmeleri yapısal olarak çok daha kolaydır.
## 9.3.Kültürel Sermaye Teorisi (Cultural Capital Theory) ve Sağlık Yaşam Tarzı
Pierre Bourdieu'nün sosyolojik çalışmalarına dayanan bu yaklaşım, yeme alışkanlıklarının ve gıda tercihlerinin (damak tadının) kişinin sosyal sınıfı ve kültürel geçmişi tarafından şekillendirildiğini savunur.

- Örneğin Brezilya'da yapılan bir çalışma, düşük gelirli obez annelerin beslenme tercihlerinin, çocukluklarından gelen geleneksel gıdalar ile modern fast-food kültürünün bir karışımı olduğunu göstermiştir. Artık ağır fiziksel iş gücü gerektirmeyen modern bir yaşam tarzında, geçmişin "kültürel mirası" olan bu yüksek kalorili yiyecek alışkanlıkları günümüzde obeziteye dönüşmektedir. Yani obezite, kişinin içine doğduğu sınıfın kültürel damak tadını sürdürmesinin bir sonucudur.

## 9.4.Diferansiyel Duyarlılık Hipotezi (Differential Susceptibility Hypothesis)
Bu model, genetik ile sosyal çevreyi birleştirir. Bireylerin sadece obeziteye yatkınlık genleri taşımadığını, bazı kişilerin taşıdıkları genler (örneğin DRD4 gibi dopamin sistemi genleri) nedeniyle **sosyal çevrelerine karşı çok daha "duyarlı/plastik" olduklarını** öne sürer.

- **"İyi ya da Kötü İçin" (For better and for worse):** Bu genlere sahip kişiler, olumsuz sosyal koşullarda (yoksulluk, ilgisiz ebeveynlik, mahalle dezavantajı) hızla obeziteye sürüklenirken; aynı kişiler şefkatli bir aile veya yüksek sosyal sermayeye (güçlü sosyal bağlara) sahip bir çevrede yetiştiklerinde obeziteye karşı dirençli hale gelirler. Yani genler kişiyi obez yapmaz, kişiyi sosyal çevresinin etkisine açık hale getirir.

## 9.5.Stres Süreci Modeli (Stress Process Model) ve Mahalle Dezavantajı
Toplumsal kaynaklı stresin (örneğin ekonomik zorluklar veya ırkçılık) obezitede çok büyük bir payı olduğunu belirten kavramsal bir çerçevedir.

- İnsanlar toplumsal olarak indüklenen kronik strese karşı bir başa çıkma (coping) mekanizması olarak kalori, yağ ve şeker oranı yüksek gıdaları tüketirler ("komfort" yeme davranışı).
- Aynı zamanda yaşanılan mahallenin fiziksel (built environment) ve algısal ortamı; örneğin suç oranlarının yüksekliği, yürüyecek yeşil alanların olmaması ve taze gıda bulunamayan "gıda çölleri" (food deserts), sağlıklı beslenmeyi kişisel bir irade sorunu olmaktan çıkarıp, çevresel/sosyal bir imkansızlığa dönüştürür.

Özetle bu teoriler; obezitenin bireysel "tembellik veya boğazına düşkünlük" (gluttony or sloth) olmadığını; aksine toplumdaki **sınıf eşitsizliklerinin, kültürel mirasların, yoksulluğun ve maruz kalınan kronik stresin beden üzerinde vücut bulmuş (somutlaşmış) hali** olduğunu savunur. Biyolojik modeller "beden nasıl yağ depolar?" sorusunu yanıtlarken, bu sosyal teoriler "neden toplumun belirli bir kesimi bunu yaşamak zorunda bırakılıyor?" sorusunu yanıtlar.

# 10. DİĞER MODEL VE HİPOTEZLER


Beynin veya yağ dokusunun vücut ağırlığını nasıl kontrol ettiğine dair (Set-point ve Settling-point dışında) ortaya atılmış farklı bakış açılarıdır:

## 10.1. Dinamik Denge Modeli (Dynamic Equilibrium Model):
Bu oldukça radikal bir yaklaşımdır çünkü vücut ağırlığının veya yağının _aslında hiçbir şekilde biyolojik olarak düzenlenmediğini_ savunur. Bu modele göre, kilolarını koruyan insanlarda gördüğümüz o "sabit referans noktası" tamamen bir illüzyondur. Kişi fazla kalori aldığında kütlesi büyür, kütlesi büyüdükçe bu kütleyi taşımak ve yaşatmak için gereken zorunlu enerji harcaması artar. Ağırlık, biyolojik bir hedef olduğu için değil, sırf artan bu kütlenin harcadığı enerji, alınan fazla kaloriyi sıfırladığı (eşitlediği) için matematiksel bir zorunluluk olarak durur. Yani ortada aktif bir savunma değil, saf bir fiziksel denge vardır.
## 1o.2.Adipozite Gücü Modeli (Adiposity Force Model):
Thorkild I. A. Sørensen tarafından ortaya atılan bu "düşünce deneyi" ve model, normal enerji dengesi sisteminden tamamen bağımsız çalışan, kendi başına bir "yağlanma gücü" (adiposity force) olduğunu öne sürer. Bu görüş, enerji alımı ve harcamasındaki değişimlerin yağlanmanın _nedeni_ değil, bu bilinmeyen içsel/dürtüsel "adipozite gücünün" bir _sonucu_ olduğunu savunur.
## 10.3. Genel Alım Düzenleme Modeli (General Model of Intake Regulation):
Klasik modeller iştahı "vücut ağırlığına veya yağ oranına" göre ayarlanmış bir mekanizma olarak görürken, de Castro'nun bu modeli iştahın yağ depolarından ziyade doğrudan **yemek yeme eyleminin kendisi** tarafından kontrol edildiğini savunur. Bu modele göre iştah, mide doluluğu ve öğün öncesi sübjektif açlık gibi geri bildirimlerle ve sosyal kolaylaştırma, hedonik faktörler ve gıda maliyeti gibi açık döngü faktörlerle anlık olarak yönetilir.

Tutumlu Gen (kıtlık) ve Sürüklenen Gen (yırtıcı hayvanlar) gibi klasik evrimsel hipotezlere karşı çıkan alternatif görüşlerdir:

## 10.4. İklime Uyumsuzluk / Maladaptasyon Görüşü (Maladaptation Viewpoint):
2014 yılında Sellayah tarafından ortaya atılmıştır. Bu hipotez, "tutumlu genlerimizin" aslında atalarımızın kıtlığa karşı değil, **soğuk iklime karşı** geliştirdiği bir hayatta kalma mekanizması (yan ürün) olduğunu savunur. Erken dönem insanları soğuktan donmamak için kahverengi yağ dokusu (BAT) ve titremesiz termojenez geliştirmiştir. Hipoteze göre, modern insanın merkezi ısıtmalı evleri ve klimaları sayesinde soğuk stresi ortadan kalktığı için bu termojenik (ısı üreten) mekanizma körelmiş, evrimsel bir "uyumsuzluk (maladaptasyon)" doğmuş ve alınan enerji ısıya dönüşemeyip yağ olarak depolanmaya başlamıştır.


Beyin, bağırsak veya makrobesinler dışındaki sistemlere odaklanan modellerdir:

## 10.5.İnfektobezite (Infectobesity / Viral Obezite):
 
 Obeziteyi metabolik veya davranışsal bir sorun olmaktan çıkarıp, doğrudan **bulaşıcı bir hastalık** olarak ele alan oldukça şaşırtıcı bir teoridir. Özellikle _Adenovirüs-36 (Ad-36)_ gibi spesifik virüs enfeksiyonlarının, kişinin kalori alımından bağımsız olarak kök hücreleri doğrudan yağ hücrelerine dönüşmeye zorladığı ve yağ hücresi çoğalmasını tetiklediği gösterilmiştir. Bu teori, obezite salgınının bir kısmının kelimenin tam anlamıyla "viral bir salgın" olabileceğini savunur.
 
## 10.6.Hepatostatik Teori (Hepatostatic Theory):
 Obezite patogenezinde beyni (hipotalamusu) ve yağ dokusunu (leptini) merkeze alan klasik görüşlere alternatif olarak M. Russek tarafından 1980'lerde geliştirilmiştir. Bu teori, yeme davranışının ve tokluğun ana şalterinin **karaciğer** olduğunu söyler. Karaciğerdeki enerji durumu (özellikle ATP seviyeleri ve glikojen depoları) azaldığında vagus siniri yoluyla beyne açlık sinyali gider; enerji dolduğunda ise tokluk sinyali başlar.
 

Bu "kıyıda köşede kalmış" veya daha spesifik olan modeller, aslında obezitenin tek bir basit denklemle çözülemeyecek kadar çok boyutlu bir sistemler biyolojisi problemi olduğunu (virüslerden karaciğer ATP'sine, evrimsel iklim adaptasyonundan saf fiziksel kütle dengesine kadar) bizlere bir kez daha kanıtlamaktadır.