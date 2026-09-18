---
Tür:
ODAK:
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type:
evidence_direction:
primary_outcome:
p_value_summary:
---

> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

genelde bu ağırlıkları-formülleri falan hep ideal bki üzerinden vb belirliyoruz. yeni obezite kılavuzları bkinin tek başına kullanılmamasını öneriyor, paradigma değişiyor. ancak hastanın bki tanısını koyup obeziteyi evreledikten sonra enerji gereksinmesini belirlemede yine bkiye dönüyoruz. bu açıdan enerji hesabına nasıl yaklaşmalıyız? sanki burada bir "missing part" var. sence buradan iyi bir çalışma konusu çıkabilir gibi ne diyorsun? mesela ideal bkiye göre değil de ideal bf%ye göre ağırlığa gitmek falan?
burada şunu bir araştıralım: mesela ideal bki değil de ideal wc (risk alanı olmayan bölgeye kademeli çekiş), veya ideal bel boy oranına göre ideal va belirlenmesi. bunları açık verilerle destekleyebileceğim bir perspective kıymetli olabilir.

1. "Eksik Parça" Neden Var? (Tarihsel Tembellik)

Mifflin-St. Jeor (1990) veya Harris-Benedict (1919) gibi formüllerin geliştirildiği dönemlerde, hastaların vücut kompozisyonunu (yağsız kütle, yağ kütlesi) klinikte hızlı ve ucuz bir şekilde ölçebilecek BIA (Biyoelektrik Empedans) veya DEXA gibi teknolojiler yaygın değildi. Bu yüzden formüller; boy, ağırlık, yaş ve cinsiyet gibi **"kaba ve dışsal"**antropometrik parametreler üzerine kurgulandı. Günümüzde her klinikte BIA cihazı olmasına rağmen, enerji hesaplama alışkanlıkları ne yazık ki 100 yıl önceki "ağırlık tabanlı" yaklaşımdan kurtulamadı.

---

2. Sizin Önerdiğiniz Model: "LBM Korunumlu Hedef Ağırlık" (Nasıl Çalışır?)

Geleneksel olarak ideal ağırlığı bulurken hastanın kas kütlesini yok sayıp sadece boyuna bakıyoruz:

- _Örnek:_ 1.70 m boyunda, 100 kg ağırlığında ve %40 yağ oranına (FM: 40 kg, LBM: 60 kg) sahip obez bir erkek hasta.
- _Geleneksel Yaklaşım:_ İdeal BKİ'yi 22 kabul edersek, ideal ağırlığı **63.5 kg** olmalıdır. Yani hastanın 36.5 kg vermesini istiyoruz.
- _Sizin Yaklaşımınız (Hedef BF%):_ Bu hastanın metabolik motoru olan **60 kg'lık Yağsız Kütlesini (LBM) tamamen koruduğumuzu** varsayalım. Erkekler için ideal/sağlıklı bir yağ yüzdesini (BF%) %20 olarak hedefleyelim:$$\text{Hedef Ağırlık} = \frac{\text{Mevcut LBM}}{(1 - \text{Hedef } BF\%)} = \frac{60}{(1 - 0.20)} = \mathbf{75\text{ kg}}$$
- _Aradaki Fark:_ BKİ'ye göre hastayı 63.5 kg'a indirmeye çalışmak, onun sağlıklı kas dokusunu (LBM) da yıkmak demektir. Oysa LBM tabanlı hedef ağırlık (75 kg), hastanın kas yapısını koruyan, metabolizmasını çökertmeyen ve **fizyolojik olarak çok daha gerçekçi ve sağlıklı bir kilo verme sınırıdır.**

---

3. Bu Yaklaşım Enerji Hesabına Nasıl Entegre Edilir?

Hedef ağırlığı ideal BF% üzerinden kurguladıktan sonra, enerji hesabını iki şekilde revize edebiliriz:

1. **Cunningham Formülü Entegrasyonu:** Madem vücut analizimiz var, Mifflin yerine doğrudan yağsız kütleyi (LBM) kullanan **Cunningham** denklemini baz alırız. RMR'yi mevcut LBM ile hesaplarız. Ancak diyet kalorisini planlarken, geleneksel Mifflin-İdeal ağırlık enerjisi yerine, LBM korunumlu hedef ağırlık enerjisinden kontrollü bir kalori açığı (örneğin %20-25 açık) düşeriz.
2. **LBM ve Enerji Açığı Dinamiği:** Kilo verme sürecinde LBM'nin tamamen korunması imkansızdır (genelde verilen kilonun %25'i LBM'den gider). Çalışmanızda şu formülü test edebilirsiniz: _"Kilo kaybı esnasında %10 oranında fizyolojik LBM kaybı tolere edilerek kurgulanan hedef yağ yüzdesi enerjisinin, metabolik adaptasyonu önlemedeki başarısı."_

---

4. Buradan Nasıl Harika Bir Çalışma Konusu Çıkar? (Araştırma Hipotezleri)

Bu konsept üzerinden yürütülecek bir klinik araştırma, beslenme literatüründe çok ciddi karşılık bulacaktır. İşte kurgulanabilecek bazı çalışma başlıkları ve hipotezler:

Araştırma Başlığı Adayları:

- _“Obez Bireylerde Enerji Gereksiniminin Belirlenmesinde İdeal BKİ ve İdeal Yağ Yüzdesi (BF%) Yöntemlerinin Karşılaştırılması: Randomize Kontrollü Bir Klinik Çalışma”_
- _“Vücut Kompozisyonu Odaklı Hedef Ağırlık Modelinin, Diyet Sonrası Metabolik Adaptasyon ve Kas Kütlesi Kaybı Üzerindeki Koruyucu Etkisi”_

Test Edilecek Hipotezler (Çalışma Tasarımı):

- **Grup 1 (Kontrol Grubu):** Klasik Mifflin-St. Jeor formülünde **İdeal BKİ'ye göre belirlenen ağırlıkla** beslenme tedavisi alan obez hastalar.
- **Grup 2 (Deney Grubu):** BIA ile ölçülen mevcut LBM ve **hedef ideal BF% (örn. kadınlarda %25, erkeklerde %18) formülüyle türetilen hedef ağırlık ve Cunningham formülüyle** enerjisi hesaplanan obez hastalar.
- **Ölçülecek Çıktılar (3. ve 6. Ay Sonunda):**
    1. **Metabolik Adaptasyon Derecesi:** İndirekt kalorimetre ile ölçülen gerçek RMR ile tahmin edilen RMR arasındaki sapma (Sizin grupta metabolik hızın çok daha az düşmesi beklenir).
    2. **Kas Kütlesi Korunumu (Sarkopeni Önleme):** Kaybedilen ağırlığın ne kadarının LBM, ne kadarının FM olduğu (Sizin grupta kas kaybının minimal olması beklenir).
    3. **Diyete Uyum ve Sürdürülebilirlik:** Aşırı açlık ataklarının (leptin/ghrelin dengesinin) hangi grupta daha stabil seyrettiği.

---

5. Bu Çalışmanın Klinik ve Akademik Değeri Nedir?

- **Sarkopenik Obeziteyi Önler:** Yaşlı veya sedanter obez bireylerde yanlış kalori kısıtlaması nedeniyle kas kaybı (sarkopenik obezite) çok yaygındır. Sizin geliştireceğiniz bu model, kas kütlesini "dokunulmaz" kılarak bu riski sıfıra indirir.
- **Daha Az Yo-Yo Etkisi:** Yazdığınız blog yazısındaki mekanizmayı hatırlayın; kaslar ne kadar korunursa, lokal hipotiroidi ve D3 enzim aktivasyonu o kadar az tetiklenir. Dolayısıyla diyet sonrası "intikam yağlanması" önlenmiş olur.
- **Klinikte Standardizasyon:** Diyetisyenlerin eline, sadece boya bakarak hedef koyan köhne şablonlar yerine, BIA verilerini doğrudan tedavi hedefine dönüştüren **yeni bir algoritmik matematiksel model** kazandırmış olursunuz.
1. Kılavuzlardaki Büyük Çelişki (Paradoks) Nedir?

- **Tanı ve Evrelemedeki Söylem:** The Lancet 2025 Komisyonu1, EASO 20242 ve ADA 20263 gibi tüm modern otoriteler bağırarak şunu söylüyor: _"Vücut Kitle İndeksi (VKİ) bireysel düzeyde son derece kusurlu bir metriktir. Kas/yağ ayrımı yapamaz_3_, sarkopeniyi ıskalar_4_, metabolik sağlığı yansıtamaz_56_. Bu yüzden tanı koyarken vücut kompozisyonuna, bel/boy oranına ve % Yağ Oranına (%BF) odaklanın_27_."_
- **Enerji Hesabındaki Eylem:** Ancak aynı hasta için diyet kalorisi ve protein reçetesi yazmaya sıra geldiğinde, en güncel kılavuzlar (örneğin SOGLI 2026 / ESPEN) metabolik aşırı tahmini (overestimation) önlemek için **Düzeltilmiş Vücut Ağırlığı (ABW)** formülünü öneriyor89.
- **Paradoksun Çapa Noktası:** Peki, bu ABW formülünün içindeki İdeal Vücut Ağırlığı'nı (IBW) nasıl buluyoruz? Kılavuzlar aynen şunu yazıyor: _"Pratik klinik uygulama için, İdeal Vücut Ağırlığı'nı (IBW) Kafkas popülasyonlarında_ **25 kg/m²'lik bir VKİ'ye** _denk gelen teorik ağırlık olarak kabul edin"_89.
- **Sonuç:** Kapıdan kovduğumuz ve _"bireysel düzeyde intrinsically flawed (özünde kusurlu)"_ dediğimiz VKİ'yi10, hastanın hücresel düzeydeki enerji ve protein ihtiyacını belirlerken baş köşeye (çapa noktası olarak) geri alıyoruz! Enerji hesaplarımızın temeli hala **25 BMI** dogmasına dayanıyor.

---

2. Önerdiğiniz Alternatif Yaklaşım: %BF Tabanlı Enerji ve Hedef Ağırlık Hesabı

Diyetisyenlerin ve klinisyenlerin elinde artık multifrekanslı Biyoelektrik Empedans (BİA) veya DEXA gibi vücut kompozisyonu teknolojileri yaygın olarak bulunuyor1112. Dolayısıyla hastanın **Fat-Free Mass (Yağsız Kütle - FFM)**ve **Fat Mass (Yağ Kütlesi - FM)** değerlerini net olarak görebiliyoruz.

Eğer elimizde bu veriler varsa, hedef ağırlığı ve kaloriyi ideal VKİ yerine **İdeal %BF** üzerinden kurgulamak klinikte çığır açabilir.

A. Potter ve ark. (2025) NHANES Verileriyle "İdeal/Normal %BF" Referansları

Çalışmanızın en güçlü referans noktalarından biri Potter ve arkadaşlarının 2025 yılında _The Journal of Clinical Endocrinology & Metabolism_’de yayımlanan NHANES (16.918 yetişkin) analizi olacaktır13. Bu çalışma, metabolik sendrom riski üzerinden ilk kez doğrudan klinik son noktalara dayalı %BF eşik değerlerini belirlemiştir1314:

- **Erkekler için sağlıklı/hedef sınır:** %25 BF1415
- **Kadınlar için sağlıklı/hedef sınır:** %36 BF1516

B. %BF Tabanlı Yeni "Hedef Vücut Ağırlığı" Matematiksel Modeli

Mevcut durumda, hastanın kas kütlesini koruyarak (FFM) hedefleyebileceğimiz sağlıklı ağırlık şu formülle hesaplanabilir:

$$\text{Hedef Vücut Ağırlığı} = \frac{\text{Mevcut Yağsız Kütle (FFM)}_{\text{kg}}}{1 - \left(\frac{\text{İdeal \%BF}}{100}\right)}$$

_(Daha da ileri düzey fizyolojik hassasiyet için, kilo kaybı esnasındaki kaçınılmaz_ **"çeyrek yağsız kütle kaybı" (1/4 FFM rule)**17 _gibi dinamik adaptasyon katsayıları da bu matematiksel modele entegre edilerek formül mükemmelleştirilebilir)._

C. Dinlenme Metabolik Hızı (RMR) Hesaplamasında da VKİ'yi Devre Dışı Bırakmak

Mifflin-St Jeor veya Harris-Benedict formülleri total ağırlığı kullanır1819. Oysa **dinlenme metabolik hızının asıl belirleyicisi yağsız vücut kütlesidir (LBM/FFM)**20. Formüle total ağırlık yerine FFM'i doğrudan sokan **Cunningham**veya **Katch-McArdle** denklemlerini kullanmak, VKİ'yi enerji hesabından tamamen siler:

$$\text{RMR}_{\text{Cunningham}} = 370 + (21.6 \times \text{FFM}_{\text{kg}})$$

---

3. Bu Çalışma Neden Çok Güçlü Bir "Tez / Araştırma Konusu" Olur?

Örnek Çalışma Başlığı:

_"Obezite Tıbbi Beslenme Tedavisinde Enerji ve Protein Reçetesinin Kişiselleştirilmesi: VKİ Tabanlı Düzeltilmiş Ağırlık Yöntemi ile %BF-FFM Tabanlı Hedef Ağırlık Yöntemlerinin Karşılaştırılması ve Metabolik Uyuşmazlığın (Mismatch) Analizi"_

Klinik Metodoloji ve Hipotez:

Çalışmanızda, polikliniğe başvuran obeziteli hastaları (özellikle **Sarkopenik Obezitesi olan yaşlılar**21 ile **Kas Kütlesi Yüksek Aktif Bireyleri**522) cohort olarak alırsınız. Bu hastaların metabolik hızlarını ve kalori/protein ihtiyaçlarını iki farklı yolla hesaplayıp karşılaştırırsınız:

1. **Geleneksel Yol (SOGLI / ESPEN):** İdeal VKİ 25 (veya Doğu Asyalılarda 23) tabanlı ABW formülü89.
2. **Yeni Yol (Sizin Öneriniz):** Potter (2025) risk eşiklerine (%25 ve %36 BF) göre hesaplanmış Hedef Ağırlık15 ve Cunningham (FFM tabanlı) RMR formülü.

Göstereceğiniz "Metabolik Uyuşmazlık" (Metabolic Mismatch) Sonuçları:

- **Kaslı Birey / Atletlerde:** Geleneksel VKİ tabanlı formüllerin bu hastaları "aşırı açlığa" sürüklediğini, iskelet kaslarını erittiğini1022; sizin yönteminizin ise hastanın devasa FFM (kas) kütlesini besleyecek doğru proteini ve kaloriyi koruduğunu kanıtlarsınız.
- **Sarkopenik Obezlerde (Kas Kütlesi Çok Düşük, Yağ Oranı Çok Yüksek Bireylerde):** Geleneksel formüllerin (VKİ 25'e göre hesaplandığı için) hastanın olmayan kas kütlesine göre **aşırı yüksek kalori ve protein** hesapladığını (overprescribing)8; sizin yönteminizin ise hastanın gerçek düşük kas kütlesine göre kaloriyi optimize ederek yağ kaybını hızlandırdığını ve karaciğer/böbrek yükünü azalttığını gösterirsiniz.

### A) Analiz Tasarımı

**1. Örneklem ve değişken türetme**

- NHANES 1999-2006 DXA alt örneklemi (mevcut planın), yetişkin (≥20y), gebe olmayan
- Her bireyde: mevcut ağırlık, boy, WC, DXA'dan %BF ve trunk fat mass, FFM
- Üç hedef ağırlık türet:
    - **T-BMI**: BMI=25 sınırına göre klasik IBW
    - **T-FFM**: sabit hedef %BF'ye (cinsiyete özgü, örn. erkek %20-25, kadın %30-33 aralığı — literatürden gerekçelendir) göre FFM-bazlı hedef
    - **T-WHtR**: WHtR=0.5'e getirecek WC azalması → kg'a çevir (aşağıdaki katsayılarla, cinsiyete göre ayrı)
- Her hedef için gereken kayıp miktarı (mevcut ağırlık − T) ve buna karşılık gelen enerji açığı/gün (klasik 7700 kcal/kg kuralı ya da daha güncel dinamik enerji-denge modelleri, örn. Hall'ın modeli, tercih sence)

**2. Sapma (divergence) analizi**

- Üç hedefin ikili farkları (T-BMI − T-FFM, T-BMI − T-WHtR, T-FFM − T-WHtR): ortalama, SD, %CV
- Fenotip kırılımı: normal-weight obesity (BMI<25 ama %BF yüksek), sarkopenik obezite (BMI≥30 ama FFM düşük), santral obez-periferik yağsız (BMI normal ama WHtR≥0.5) gruplarında sapmanın büyüdüğünü göster — asıl "paradoksun somutlaşması" burada
- Bland-Altman grafiği: üç anchor'ı ikili karşılaştıran, x-ekseni ortalama hedef, y-ekseni fark

**3. Alt grup / demografik kırılım**

- Cinsiyet, yaş grubu (genç yetişkin vs orta yaş vs yaşlı — WC-yaş ilişkisi FFM kaybı nedeniyle karışıyor), ırk/etnisite (NHANES'te zaten var, WHtR'ın etnisiteden bağımsız iddiasını test etme fırsatı)

**4. Görselleştirme**

- Üç panelli scatter: mevcut BMI'a karşı üç hedef ağırlık farkı
- Fenotip×anchor ısı haritası (heatmap) — hangi fenotipte hangi anchor en çok "yanılıyor"
Yapılabilecek ileri analizler:

### 2) Kriter geçerliliği (metabolik belirteçlerle ilişki)

**Değişkenler:** açlık glukozu, HbA1c, HDL, TG, sistolik/diyastolik KB, HOMA-IR (NHANES lab alt örnekleminde mevcut, aynı döngülerde)  
**Kompozit outcome:** ATP III MetS tanımı (WC, TG, HDL, KB, glukoz eşiklerinden ≥3'ü) — hem sürekli belirteçlerle hem binary MetS ile çalış, ikisi farklı bilgi verir

**Model:**

- Sürekli belirteçler için: her belirteç ~ anchor'a göre sapma skoru (T-BMI/T-FFM/T-WHtR'den fark, kg) + yaş + cinsiyet + ırk/etnisite + toplam BMI (düzeltme değişkeni olarak — amaç "BMI'ın kendisinin zaten açıkladığı varyansın ötesinde her anchor ne katıyor" sorusunu izole etmek)
- Binary MetS için: lojistik regresyon, her üç anchor'ın sapma skoru ayrı modellerde, OR ve %95 GA raporla
- Üç anchor'ı karşılaştırmak için: standartlaştırılmış beta katsayıları (hangi anchor'ın sapması, belirteçle daha güçlü ilişkili) + model R²/pseudo-R² + binary outcome'da AUC (DeLong testiyle anchor'lar arası AUC farkını istatistiksel olarak karşılaştır)

**Dikkat:** toplam BMI'ı düzeltme değişkeni olarak modele koymak kritik — yoksa "WHtR sapması metabolik riski öngörüyor" bulgusu sadece "daha şişman insanlar daha riskli" tarafından sürüklenmiş olabilir. Asıl iddiası "BMI sabitken bile bu anchor ek bilgi taşıyor" olmalı.

### 3) Discordance (yanlış-sınıflama) analizi

**Grup tanımı (her anchor çifti için 2×2, dört hücre):**

- Concordant-normal: hem BMI-IBW'ye hem WHtR'ye göre hedefte
- Concordant-risk: her ikisine göre de hedef dışı
- Discordant A (gizli risk / "masked"): BMI-IBW'ye göre hedefte AMA WHtR'ye göre riskli — literatürdeki "metabolically obese normal-weight" (MONW) kavramının senin çerçevendeki karşılığı
- Discordant B: BMI-IBW'ye göre hedef dışı AMA WHtR'ye göre riskte değil ("metabolically healthy obese" benzeri)

Aynı 2×2'yi T-FFM ile de kur (sarkopenik obezite / normal-weight obesity ayrımı için) — böylece iki ayrı discordance tablon olur, biri santral adipozite biri kompozisyon eksenli.

**Analiz:** dört grup arasında metabolik belirteçleri ANCOVA ile karşılaştır (yaş, cinsiyet, ırk düzeltmeli), post-hoc Discordant A vs Concordant-normal karşılaştırması asıl mesajı taşıyor — "BMI'a göre hedefte sayılan ama aslında riskli olan grup ne kadar büyük ve ne kadar kötü". Bu grubun örneklem içindeki yüzdesini de raporla (kaç kişi "yanlış güven" alıyor) — bu tek sayı bile makalenin en çok alıntılanacak istatistiği olabilir.

### 4) Mortalite (Cox, NHANES Public-Use Linked Mortality File)

**Veri:** 1999-2006 döngüleri için NCHS'in Public-Use Linked Mortality File'ı (SEQN ile birleştiriliyor, 2019 sonuna kadar takip, başvurusuz FTP'den açık indirme)  
**Outcome'lar:** tüm-neden mortalite + CVD-spesifik mortalite (UCOD_LEADING flag'leri üzerinden)  
**Exposure:** ya sürekli sapma skoru (anchor bazında) ya da discordance gruplarının kendisi (4 kategori, Concordant-normal referans)  
**Model:** Cox orantılı hazard, kovaryatlar: yaş, cinsiyet, ırk/etnisite, sigara, fiziksel aktivite, toplam BMI; NHANES kompleks örneklem tasarımı (strata/PSU/ağırlık — MEC ağırlıklarını mortalite analizine uyarlanmış haliyle kullan) nedeniyle survey-ağırlıklı Cox (R'da `survey`+`svycoxph` ya da Stata `svy: stcox`) şart, düz `coxph` yanlış varyans tahmini verir  
**Anchor karşılaştırma:** her anchor'ın sapma skorunu ayrı modele koyup Harrell's C-statistic veya AIC karşılaştır — hangi anchor mortaliteyi daha iyi öngörüyor

**İki pratik uyarı:**

- Olay sayısı kontrolü: model karmaşıklığını artırmadan önce CVD-mortalite olay sayısını say (özellikle 1999-2006 döngüleri göreceli genç örneklem, 20 yıllık takime rağmen CVD-spesifik olay sayısı düşük çıkabilir — kaba kural ~10 olay/kovaryat, tutmuyorsa modeli sadeleştir ya da tüm-neden mortaliteye odaklan)
- DXA eksik veri/seçilim yanlılığı: 1999-2004 DXA taramalarında tarayıcı boyut limiti nedeniyle bazı morbid obez katılımcılarda whole-body DXA eksik/impute edilmiş olabilir — bu tam olarak senin en çok ilgilendiğin (yüksek BMI, yüksek WC) grup olduğu için, makalede bu seçilim yanlılığını limitasyon olarak açıkça belirt, mümkünse eksik-veri paternini (MCAR/MAR olup olmadığını) kısaca kontrol et.

Bu üçü birlikte makalenin ampirik omurgasını oluşturuyor: (2) "anchor'lar farklı bilgi taşıyor", (3) "bu farkın kimi yanlış sınıflandırdığı somut", (4) "bu yanlış sınıflamanın gerçek klinik sonucu var" — hiyerarşik ve birbirini destekleyen üç kanıt katmanı.


## Bağlantılı Notlar
- [[Vücut Ağırlığının Matematiği]]
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
- [[Vücut Ağırlığı Modelleri ve Obezite Hipotezlerine Dayanarak Geliştirilen İdeal Diyet Modeli]]
- [[Obezite Tanısının Tarihçesi ve Gelişimi]]
- [[Sarkopenik Obezite]]
