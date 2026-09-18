---
Ders_Adı: Bilgisayar Uygulamaları ve Yapay Zeka
Kod: BES
Dönem: Bahar
Sınıf: 1
Durum: aktif
Kapak: "🤖"
Açıklama: "AI araçları, R Shiny, beslenme bülteni otomasyonu, dijital portfolyo, sergi projesi"
---

## 📋 Ders İçeriği

**Ders Akışı:**
## Hafta 1: Yapay Zekaya Giriş (Kavramlar, Çalışma Mantığı ve Etik)
### 1. Temel Kavramlar Kutusu: Hangisi Ne Anlama Geliyor?

Teknoloji dünyasında sürekli duyduğunuz kısaltmaları (AI, ML, DL, LLM) iç içe geçmiş **matruşka bebeklerine**benzetebiliriz. En dıştaki en büyük bebek Yapay Zeka iken, en içerideki en küçük ve en uzman bebek Büyük Dil Modelleridir.

```
+---------------------------------------------------+
| YAPAY ZEKA (AI)                                   |
|   +-----------------------------------------------+
|   | MAKİNE ÖĞRENMESİ (ML)                         |
|   |   +-------------------------------------------+
|   |   | DERİN ÖĞRENME (DL)                        |
|   |   |   +---------------------------------------+
|   |   |   | ÜRETKEN YAPAY ZEKA (GenAI) & LLM'ler  |
|   |   |   +---------------------------------------+
|   |   +-------------------------------------------+
|   +-----------------------------------------------+
+---------------------------------------------------+
```

- **Yapay Zeka (AI - Artificial Intelligence):** İnsan zekasını (öğrenme, karar verme, görsel algı) taklit eden tüm bilgisayar sistemleridir.
    - _Beslenme Metaforu:_ AI, **bütün bir hastane mutfağıdır**. Yemek pişirme kurallarından hijyen standartlarına kadar her şeyi organize eden genel sistemdir.
- **Makine Öğrenmesi (ML - Machine Learning):** Bilgisayarların, insanlar tarafından açıkça programlanmadan, verilerden kalıplar çıkararak öğrenmesini sağlayan bir AI alt dalıdır.
    - _Beslenme Metaforu:_ ML, mutfakta **deneme-yanılma yoluyla öğrenen stajyer şeftir**. Şef, binlerce kilo boy/kilo ve kan tahlili verisine bakar ve "Hangi tahlil sonucu hangi hastalıkla ilişkili olabilir?" kalıbını kendi kendine çözer.
- **Derin Öğrenme (DL - Deep Learning):** İnsan beynindeki sinir hücrelerinden (nöronlardan) esinlenen yapay sinir ağlarını kullanarak çok daha karmaşık verileri (görüntüler, sesler) işleyen ML alt dalıdır.
    - _Beslenme Metaforu:_ DL, mutfağın **"Gözü Kapalı Gurme"sidir**. Bir tabağın fotoğrafına bakarak içindeki malzemeleri, porsiyon boyutunu ve hatta sosun içindeki gizli baharatları (piksel pikselleri analiz ederek) tanıyabilir.
- **Üretken Yapay Zeka (GenAI - Generative AI):** Mevcut verileri analiz ederek tamamen **yeni içerikler (metin, yemek tarifi, haftalık diyet planı, görsel)** üretebilen yapay zeka sistemleridir.
    - _Beslenme Metaforu:_ GenAI, elindeki malzemelerle **yepyeni bir füzyon tarifi uyduran yaratıcı bir şeftir**.
- **Büyük Dil Modelleri (LLM - Large Language Models):** ChatGPT, Gemini, Claude gibi devasa metin verileriyle eğitilmiş ve insan benzeri dille iletişim kurabilen GenAI sistemleridir.
    - _Beslenme Metaforu:_ LLM, dünyadaki **bütün beslenme kitaplarını, diyet bloglarını ve yemek tariflerini ezberlemiş ama hayatında hiç yemek yememiş** bir kütüphanecidir.
Öncelikle en temel üç kavramın (AI, ML, DL) arasındaki ilişkiyi, meşhur **"Matruşka Bebekleri"**analojisiyle zihnimize oturtalım:

- **Yapay Zeka (AI - Artificial Intelligence):** En dıştaki en büyük bebek. İnsanın yaptığı mantıklı her şeyi (hesap makinesinin bölme yapması, fırının dereceye göre kapanması dahil) taklit eden genel teknolojinin adıdır.
- **Makine Öğrenimi (ML - Machine Learning):** Onun içindeki orta boy bebek. Bilgisayara kuralları bizim söylemediğimiz, verileri verip _"Örüntüyü sen bul"_ dediğimiz yöntemdir.
- **Derin Öğrenme (DL - Deep Learning):** En içteki en küçük ve en dahi bebek. Beynimizdeki sinir hücrelerini taklit eden, Excel tablolarıyla değil; doğrudan ham fotoğraflar ve karmaşık seslerle kendi kendine öğrenen sistemdir.

Şimdi bu teknolojilerin beslenme bilimini nasıl dönüştürdüğünü, her birinin ardındaki çalışma mantığını ve **neden o göreve başka hiçbir tekniğin yakışmadığını** eğlenceli metaforlarla inceleyelim:

---

📊 1. Makine Öğrenimi (Machine Learning - ML)

🍳 Süper Benzetme: "Süper Hafızalı Muhasebeci Necdet Efendi"

Necdet Efendi’nin elinde devasa bir Excel tablosu var. Bu tablonun satırlarında binlerce insanın kan tahlilleri, bağırsak bakterilerinin (mikrobiyom) sayıları ve genetik kodları yazıyor. Sütunlarda ise bu insanların ne yediği ve yedikten sonra kan şekerlerinin kaça fırladığı kayıtlı. Necdet Efendi günlerce bu sayıları inceliyor, matematiksel korelasyonlar kuruyor ve formülü çözüyor: _"Eğer hastanın A bakterisi yüksek, B geni aktifse, muz yediğinde şekeri fırlar!"_.

🛠️ Nasıl Çalışıyor? (Tekniğin Özeti)

ML, yapılandırılmış (yani satırı sütunu belli olan düzgün sayısal veriler) üzerinde uzmanlaşmış bir istatistik canavarıdır. En meşhur modellerinden olan **XGBoost (Karar Ağaçları Grubu)**, elindeki verileri süzgeçten geçirerek adım adım sorular sorar: _"Yaşı 50'den büyük mü? Evet. Albümini düşük mü? Evet. O zaman malnütrisyon riski %80'dir"_.

🥦 Beslenmede Bu Teknikle Ne Yapıyoruz?

- **Hassas Beslenme ve Kan Şekeri Tahmini:** ZOE ve DayTwo gibi dev girişimler bu tekniği kullanır. 800 kişinin 46.898 öğünlük verisini inceleyen bir XGBoost modeli, bir insanın hiç yemediği bir gıdaya vereceği şeker tepkisini %70 doğrulukla (Necdet Efendi'nin hesap hassasiyetiyle) tahmin eder.
- **Kilo Verme Başarısını Öngörme:** **Random Forest (Rastgele Orman)** algoritması, bir kişinin uygulayacağı diyetle kilo verip veremeyeceğini (diyet uyumunu) daha diyetin 1. gününde %80 güvenle tahmin edebilir.

❌ Neden Diğer Teknikler (Örn: Derin Öğrenme - DL) Burada Tercih Edilmez?

- **"Bana Hesap Ver!" Kuralı (Explainability):** Klinik beslenmede bir hastaya _"Sana domatesi yasakladım"_ diyorsanız, tıbbi olarak nedenini (hangi gen veya bakteri yüzünden olduğunu) açıklamak zorundasınız. ML modelleri (XGBoost, Random Forest), bize kararı verirken hangi parametreye ne kadar güvendiğini **SHAP veya LIME** denilen yöntemlerle satır satır açıklar.
- Ancak en içteki bebek olan **Derin Öğrenme (DL)** tam bir **"Kara Kutudur" (Black Box)**. DL size sadece _"Bu hastaya domates yasak"_ der ama nedenini asla söylemez; tıp dünyası ise gerekçesiz kararlara güvenemez.

---

📸 2. Derin Öğrenme ve Bilgisayarlı Görü (Deep Learning & Computer Vision)

🍳 Süper Benzetme: "Piksel Süzgeçli Gurme Şef"

Önünüze bir tabak İskender kebap koyduk. Klasik Makine Öğrenimi (Necdet Efendi) bu tabağa bakıp orada ne olduğunu anlayamaz; çünkü Necdet Efendi'nin gözü yoktur, o sadece sayılardan anlar. İşte burada devreye **Derin Öğrenme (Ressam Çocuk)** girer. Tabağın fotoğrafını alır, onu milyonlarca küçük kareye (piksele) böler. Üzerinden **CNN (Evrişimli Sinir Ağları)** denilen süzgeçleri geçirerek dönerin dikey çizgilerini, yoğurdun beyaz dokusunu, tereyağının parlaklığını yakalar. Pikselleri üst üste yığarak kendi kendine İskender kebabı teşhis eder.

🛠️ Nasıl Çalışıyor? (Tekniğin Özeti)

**CNN (Convolutional Neural Networks)**, görsellerin üzerindeki geometrik desenleri (kenarları, köşeleri, renk geçişlerini) katman katman süzerek nesneleri tanır. Biz bilgisayara _"Bak döner böyle bir şeydir"_ diye kural yazmayız; o binlerce döner fotoğrafına bakarak dönerin görsel "imzasını" kendi kendine keşfeder.

🥦 Beslenmede Bu Teknikle Ne Yapıyoruz?

- **Tabaktan Kalori ve Makro Sayımı (goFOOD™ & YOLOv8):** Telefonunuzla yemeğin fotoğrafını çektiğiniz an, sistem (Örn: YOLOv8 tabanlı Diet Engine veya goFOOD™) tabaktaki besini segmentlere ayırır, hacmini hesaplar ve içindeki proteini, yağı saniyeler içinde ekranınıza düşürür.

❌ Neden Klasik Makine Öğrenimi (ML) Burada Tercih Edilmez?

- **"Özellik Mühendisliği" (Manual Feature Engineering) Ameleliği:** Eğer fotoğrafı klasik ML ile tanımaya çalışsaydık, bizim oturup bilgisayara elle: _"Eğer sarı renkli piksellerin uzunluğu 5 cm ise bu patatestir"_ gibi milyarlarca kural yazmamız gerekirdi (Buna özellik mühendisliği denir). İnsan dışı bir yemek kombinasyonunda bu sistem anında çökerdi. DL (Görsel Ağlar) ise bu ameleliği ortadan kaldırarak fotoğraftan uçtan uca (end-to-end) doğrudan kalori ve besin değeri çıkarabilen tek kraldır.

---

💬 3. Doğal Dil İşleme ve Dil Modelleri (NLP, LLM & SLM)

🍳 Süper Benzetme: "Diyetisyen Kürsüsündeki Dahi Papağan"

Karşınızda dünyadaki bütün beslenme kitaplarını, tıp makalelerini ve internetteki sağlıklı yaşam forumlarını yutmuş dev bir papağan var. Bu papağan aslında biyoloji, metabolizma veya insan psikolojisi hakkında hiçbir şey "hissedip anlamıyor". Sadece siz ona bir şey sorduğunuzda, okuduğu milyarlarca metne bakarak _"Bu kelimeden sonra hangi kelime gelirse kulağa en mantıklı ve bilimsel gelir?"_ olasılık hesabı yapıyor ve konuşmaya başlıyor.

🛠️ Nasıl Çalışıyor? (Tekniğin Özeti)

Doğal Dil İşleme (NLP) ve **Büyük Dil Modelleri (LLM - ChatGPT/Gemini)**, insan dilindeki kelimeleri "token" (sayısal jetonlar) haline getirerek aralarındaki anlamsal mesafeleri ve istatistiksel olasılıkları hesaplar.

🥦 Beslenmede Bu Teknikle Ne Yapıyoruz?

- **Sanal Diyet Koçluğu:** ChatGPT veya Claude gibi sistemler, hastayla 7/24 konuşarak ona motivasyon sağlar, buzdolabındaki malzemelere göre anlık sağlıklı tarifler üretir.
- **Sanal Hasta Simülasyonu (Monash ATLAS):** Öğrencilerin hasta iletişim becerilerini geliştirmek amacıyla, yapay zekaya "savunmacı ve kaygılı hasta Carol" kimliği yüklenerek diyetisyenlerin empati eğitimi yapması sağlanır.
- **FoodSky (Küçük Dil Modeli - SLM):** Genel dil modellerinin aksine, sadece gastronomi ve klinik beslenme verileriyle eğitilen (fine-tuned) **FoodSky** gibi küçük ve kompakt dahi modeller, şeflik ve diyetisyenlik sınavlarını %91 gibi rekor başarılarla geçmektedir.

❌ Neden ML veya DL Burada Tercih Edilmez?

- **Sayılar Konuşamaz!** Necdet Efendi (ML) veya Şef (DL) çok iyi tahminler yapabilir: _"Şekerin 120 çıkacak"_ veya _"Bu tabakta elma var"_ diyebilirler. Ama bir hastaya _"Tuzsuz yemek yemekte zorlandığını biliyorum, gel seninle damak tadını zorlamayacak harika bir baharat karışımı hazırlayalım"_ diyemezler. İnsan dilinin o muazzam anlamsal ve duygusal zenginliğini işleyebilecek tek yapı NLP ve Transformer tabanlı dil modelleridir.

---

🔒 4. Federe Öğrenme (Federated Learning - FL)

🍳 Süper Benzetme: "Sır Tutma ve Ortak Akıl Kulübü"

Diyelim ki Türkiye'nin, Amerika'nın ve Hindistan'ın en büyük kanser hastaneleri ortak bir yapay zeka eğitmek istiyor. Ancak hastaların genetik, kanser ve beslenme verileri o kadar gizli ki, yasal olarak hastane dışına çıkarılması veya tek bir ortak bilgisayarda toplanması kesinlikle yasak (KVKK/GDPR duvarı). Kulüp şöyle bir kural koyuyor: _"Hiçbir hastane verisini dışarı göndermeyecek (Veri lokalde kalacak)__. Yapay zeka modeli her hastanenin kendi bilgisayarına misafir gidecek, orada hastaların dosyalarını okuyup öğrenecek, edindiği matematiksel 'ders notunu' şifreleyerek merkeze gönderecek__. Merkez, üç hastaneden gelen ders notlarını birleştirip süper akıllı ortak bir model yapacak; ama hiçbir hastanın özel kimliğini görmemiş olacak"__._

🛠️ Nasıl Çalışıyor? (Tekniğin Özeti)

Federe Öğrenme (FL), merkezi olmayan (decentralized) bir yapay zeka eğitim modelidir. Veriler cihazlarda (örneğin kullanıcıların cep telefonlarında veya hastane sunucularında) kalır; sadece modelin güncellenen ağırlık parametreleri (gradients) şifrelenmiş olarak paylaşılır.

🥦 Beslenmede Bu Teknikle Ne Yapıyoruz?

- **Mahrem Verilerle Sağlık Modellemesi (FAITH Projesi):** Kanser hastalarının uykusunu, terindeki biyobelirteçlerini, genetik risklerini ve diyet günlüklerini takip eden sistemlerde, hastanın özel hayatını %100 koruyarak yapay zekanın kendini geliştirmesini sağlıyoruz.

❌ Neden Klasik Merkezi Yapay Zeka Burada Tercih Edilmez?

- **NHS-Google Skandalı ve Veri İhlalleri:** Klasik sistemlerde tüm hastaların verilerini tek bir devasa sunucuya kopyalamanız gerekir. Bu durum siber korsanlar için dev bir hedef tahtası yaratır. Tarihteki NHS-Google işbirliğinde yaşanan yasal krizler gibi, hasta mahremiyetini ihlal ederek milyonlarca dolarlık davalara yol açar. FL, hastanın mahremiyetini kilit altında tutarak bu yasal ve etik felaketleri tamamen bloke eden tek güvenli kapıdır.

. Nüans: CNN'de "Bak Bu Dönerdir" Demiyorsak, Makine Onun Döner Olduğunu Nereden Biliyor?

**Eksik olan nüans şu:** Biz makineye dönerin ismini (yani etiketini) elbette söylüyoruz; söylemediğimiz şey döneri döner yapan **görsel kurallar**.

- **Eski Dünyanın Yöntemi (Kural Tabanlı):** Mühendisler oturup bilgisayara kod yazardı: _"Eğer fotoğrafta yan yana dikey kahverengi şeritler varsa, altında yeşil biber ve yanında beyaz yoğurt pikselleri varsa bu dönerdir."_ Bu sistem ilk farklı tabakta (örneğin sosu dökülmemiş veya biberi olmayan bir dönerde) anında çökerdi.
- **CNN'in Yöntemi (Denetimli Öğrenme - Supervised Learning):** Biz bilgisayara bir çocuk atlası gibi binlerce resimli kart veriyoruz [120]. 10.000 tane döner fotoğrafı yüklüyoruz ve her birinin altına elle **"Döner"** yazıyoruz (buna etiketleme denir) [120, 123].
- **Peki CNN ne yapıyor?** Biz ona "dikey şeritleri ara" demiyoruz. CNN, o 10.000 döner fotoğrafını süzgeçten geçirirken kendi kendine matematiksel bir örüntü keşfediyor [121, 123]. Bakıyor ki, altında "Döner" yazan tüm kartlarda ortak bir desen var: _Dikey lifli dokular, etin üzerindeki yağlı parıltılar, pide gözenekleri..._
- Önüne hiç görmediği yeni bir tabak fotoğrafı koyduğumuzda, o tabağın piksellerini süzüyor ve kendi hafızasındaki şablonla karşılaştırıyor: _"Aha! Bu tabağın dokusu ve desenleri, %96 oranında o üzerinde 'Döner' yazan kartlardaki desene benziyor. O halde bu dönerdir!"_diyor.
- **Özetle:** Kelimeyi (etiketi) biz öğretiyoruz [120, 121]. Ama o kelimeye giden **"görsel ipuçlarını ve kuralları"** bilgisayar milyonlarca fotoğrafa bakarak kendi kendine keşfediyor [121, 123].

---

2. Nüans: Dil Modelleri Kelime Tahmin Ederek Nasıl Bu Kadar Uzun Cevaplar Yazıyor? Bizim Yazdığımız Promptu Gerçekten "Anlıyor" mu?

"Bir sonraki kelimeyi tahmin etmek" denince insanın aklına telefon klavyelerindeki otomatik tamamlama geliyor. Peki telefon klavyemiz neden 3 sayfalık diyet yazamıyor da ChatGPT yazıyor?

- **Telefon Klavyenizin Sınırı (Kör Tahmin):** Telefonunuz sadece yazdığınız son 1-2 kelimeye bakar. "Su" yazarsanız arkasından en yüksek ihtimalli "iç" kelimesini getirir. "İç" yazınca "tim" getirir. Süreç tamamen kopuktur, paragrafın başını çoktan unutmuştur.
- **LLM'lerin Sırrı: "Attention" (Dikkat) Mekanizması ve "Dinamik Yerçekimi":** Dil modellerindeki devrim, **Transformer** adı verilen bir mimaridir [120, 121]. Bu sistemde, yazdığınız tüm prompt (örneğin: _"Bana diyabet hastası için glütensiz menü yaz"_) devasa bir **manyetik alan/yerçekimi** oluşturur [120].
- Yapay zeka ilk kelimeyi tahmin etmek için tüm bu manyetik alanı tartar [121]. İlk kelimeyi üretir: _"Sabah"_.
- Şimdi, ikinci kelimeyi üretirken girdi kutusuna bu kelimeyi de ekler: _"Bana diyabet hastası için glütensiz menü yaz. Sabah..."_
- Burada "glütensiz" ve "diyabet" kelimelerinin yarattığı manyetik çekim, "Sabah" kelimesinin yanına "ekmek" gelmesini engeller; çünkü "glütensiz" kelimesi ekmek kelimesini iter, yerine "yulaf" kelimesini çeker. İkinci kelimeyi üretir: _"Yulaf"_.
- Üçüncü kelimeye geçerken girdi şudur: _"Bana diyabet hastası için glütensiz menü yaz. Sabah yulaf..."_
- Bu süreç (otoregresif döngü) tren vagonları gibi birbirini çekerek, her adımda paragrafın başındaki o "glütensiz" ve "diyabet" manyetik alanına sadık kalarak satırlarca, sayfalarca akar [121].
- **Promptu Anlıyor mu?** Hayır, insan gibi "anlamıyor" [121]. Bizim yazdığımız prompt, onun milyarlarca kelimeden oluşan matematiksel haritasında (vektör uzayında) bir **"istikamet"**belirliyor. O da o istikamete en uygun kelimeleri istatistiksel olasılıklarla yan yana diziyor [121]. Ortada gerçek bir bilinç veya anlama yok; kusursuz bir matematiksel hizalama var [121].

---

3. Nüans: Dil Modeli Hastanın "Savunmacı ve Kaygılı" Olduğunu Nereden Biliyor? Özel Bir Veriseti mi Yüklüyoruz?

Hayır Hocam, "Kaygılı insan kelimeleri sözlüğü" diye özel bir veritabanı yüklemiyoruz.

- **Büyük Kütüphane ve Gizli Tiyatro Odası Analojisi:** Yapay zeka (LLM), eğitilirken internetteki milyarlarca film senaryosunu, romanı, psikiyatri seans dökümlerini, forum tartışmalarını ve Reddit dertleşmelerini okudu [120, 121]. Dolayısıyla, kaygılı veya savunmacı insanların konuşurken nasıl cümleler kurduğunu, hangi kelimeleri hangi sırayla seçtiğini istatistiksel olarak zaten çok iyi biliyor [121].
- Biz yapay zekaya (Carol personasına) şu sistem talimatını (system prompt) verdiğimizde: _"Sen diyaliz hastası Carol'sın. Kaygılı ve savunmacı bir karakterin var."_
- Onun devasa beynindeki milyarlarca bağlantı arasından **"Kaygılı ve Savunmacı İnsan Diyalogları" tiyatro odasının kapısını** kilitleyip diğer odaları kapatıyoruz.
- Yapay zeka artık o odanın içindedir. Öğrenci ona _"Haftada kaç kadeh alkol alıyorsunuz?"_diye sorduğunda, yapay zeka normalde verebileceği _"Haftada iki kadeh"_ cevabını vermez. Çünkü o "kaygılı tiyatro odasında" bu soruya verilecek en yüksek olasılıklı kelime kalıbı şudur: _"Bunu neden soruyorsunuz? Doktorum zaten her şeyi biliyor, beni yargılamayın!"_.
- Yani yapay zeka kaygıyı **hissederek** reaksiyon vermiyor; sadece bizim çizdiğimiz sınırlar (tiyatro odası) dahilinde, o karaktere en uygun kelime olasılıklarını yukarı çekip konuşuyor [121].
- 1. Yapay Zeka Ne Zaman Duracağına Nasıl Karar Veriyor?

Yapay zeka yazarken kelimeleri birer birer üretir. Peki, sayfalarca yazdıktan sonra bir noktada noktayı koyup durmasını sağlayan şey nedir?

- **Süper Benzetme: "Hesap Fişinin Sonundaki Makas" (Durma Jetonu / EOS)**
    - Yapay zekanın okuduğu milyarlarca kitaptaki her cümlenin, her paragrafın ve her makalenin sonunda bizim göremediğimiz görünmez bir işaret vardır. Bilgisayar biliminde buna **EOS (End of Sequence - Dizilim Sonu)** jetonu denir. Bunu bir otobanın sonundaki **"DUR" tabelası** veya kasiyerin hesap fişini kestiği **görünmez makas** gibi düşünebilirsiniz.
    - Yapay zeka her yeni kelimeyi tahmin ederken, olasılık listesinde bu "Durma İşareti"ni de bulundurur.
    - Örneğin bir menü yazarken: _"Akşam yemeğinde ızgara balık yiyebilirsiniz."_ cümlesini kurdu. Bu cümleden sonra gelebilecek kelimelerin olasılıklarını hesaplar. Eğer kafasındaki o "manyetik alan" (diyabet hastası için 1 günlük menü planı) görevini tamamlamışsa, olasılık tablosunda bir sonraki kelime olarak "veya", "ayrıca", "domates" gelme ihtimali %1'e düşerken, **"Durma İşareti" (EOS) gelme ihtimali %99'a fırlatılır**.
    - Yapay zeka o durma işaretini seçtiği an, yazılımsal olarak elektrik devresi kesilir ve robot yazmayı anında bırakır.

---

2. Hangi Konuda Ne Kadar Yazacağına (Paragraf Boyutuna) Nasıl Karar Veriyor?

Biz robota "bana uzun bir makale yaz" demesek bile o sabah kahvaltısına 3 satır, akşam yemeğine 5 satır yazıp konuyu dengeler. Bu porsiyon kontrolünü nasıl yapıyor?

- **Süper Benzetme: "Göz Kararı Yemek Dağıtan Aşçı Yardımcısı"**
    - Yapay zeka, internetteki milyonlarca yemek tarifini ve diyet planını okurken buralardaki **"porsiyon ve metin dengesini" istatistiksel bir göz kararıyla**öğrenmiştir.
    - Bilir ki, bir diyet yazısında "sabah kahvaltısı" konusu genellikle 50-100 kelime sürer. Eğer kahvaltı üzerine 2000 kelime yazmaya başlarsa, o "Attention" (dikkat) mekanizmasındaki denge bozulur; çünkü kelimelerin arasındaki mesafe uzadıkça "öğle yemeği" ve "akşam yemeği" kelimelerinin manyetik çekim gücü robotu kendine doğru çekmeye başlar.
    - Eğer biz prompta **"bunu sadece 20 kelimeyle açıkla"** gibi katı bir kısıtlama koyarsak, robotun kafasındaki manyetik alana devasa bir engel koymuş oluruz. Robot her kelimeyi üretirken kalan kelime sayısını geriye doğru sayar ve sınıra yaklaştıkça "Durma İşareti"nin (EOS) seçilme olasılığını yapay olarak yukarı pompalar. Böylece konuyu hızlıca bağlayıp durur.

---

3. Yapay Zekaya "Yaratıcı Ol" Dediğimizde İlerleyiş Nasıl Değişiyor?

Yapay zeka sadece geçmişte yazılanları tekrar ediyorsa, nasıl oluyor da bize daha önce hiç duyulmamış yaratıcı bir fikir veya tarif sunabiliyor?

- **Süper Benzetme: "Olasılık Kumarı" ve "Sıcaklık (Temperature) Ayarı"**
    - Normal şartlarda yapay zeka uslu bir çocuktur. Sorduğumuz sorunun arkasından gelecek **en yüksek olasılıklı (%90 ihtimalli)** kelimeyi seçer. Buna "güvenli sürüş" denir.
    - Örneğin: _"Sabah kahvaltısında sıcak bir..."_ dedik. Arkasından gelebilecek en yüksek ihtimalli kelime %90 olasılıkla **"çay"** veya **"kahve"**dir. Yapay zeka hep bu en yüksek olasılığı seçerse sıfır yaratıcı olur, herkesle aynı şeyi söyler.
    - Ancak yapay zekanın arkasında bilgisayar mühendislerinin **"Temperature" (Sıcaklık)**adını verdiği matematiksel bir **"delilik/kumar" parametresi** vardır.
    - Biz robota _"Bana yaratıcı, çılgın bir fikir bul!"_ dediğimizde, arka planda bu sıcaklık ayarını sonuna kadar açarız. Bu ayar açıldığında yapay zekaya şu emri vermiş oluruz: **"En yüksek olasılıklı birinci kelimeyi seçme! Git o listenin altındaki %2'lik, %1'lik sürpriz kelimeleri seç!"**
    - Şimdi aynı cümleyi kurduruyoruz: _"Sabah kahvaltısında sıcak bir..."_ Sıcaklık açık olduğu için robot en üstteki "çay" kelimesini eler. Listenin altındaki %1 ihtimalli **"avokado çorbası"** veya **"bilişsel iksir"** kelimesini seçer. Kumar oynayarak sıra dışı yollara sapar.

---

4. Fikir Bulmak ve Yaratıcılık Yapay Zekaya Nasıl "Öğretiliyor"?

Yapay zekanın yeni bir fikir bulması, aslında **iki uzak galaksiyi çarpıştırmasından** ibarettir.

- **Süper Benzetme: "Moleküler Gastronomi Çarpıştırıcısı"**
    - İnsan beyni yaratıcı bir fikir bulurken ne yapar? Dünyada daha önce hiç yan yana gelmemiş iki konuyu birleştirir. Örneğin: _"Cep telefonu"_ ile *"Kamera"*yı birleştirip kameralı telefonu buluruz.
    - Yapay zeka da kelimelerin birbiriyle olan anlamsal mesafelerini bir harita (vektör uzayı) üzerinde tutar. Bu haritada **"Uzay Gemisi"** kelimesi ile **"Brokoli Çorbası"**kelimesi birbirinden kilometrelerce uzaktadır.
    - Biz robota _"Çocukların seveceği yaratıcı bir çorba fikri bul"_ dediğimizde; yapay zeka "Çocuk", "Brokoli" ve "Uzay" kelimelerinin yarattığı üç farklı manyetik alanı aynı anda çalıştırır.
    - Bu üç alanın tam ortasında, kelimelerin yerçekimi birbirini çeker ve ortaya daha önce internette hiç yazılmamış olan: **"Gezegen halkaları şeklinde doğranmış havuçların yüzdüğü, astronot kaskı kâsesinde sunulan Kozmik Brokoli Çorbası"** fikri çıkar.
    - **Peki bunun iyi bir fikir olduğunu nereden biliyor?** Burada devreye **RLHF (Reinforcement Learning from Human Feedback - İnsan Geri Bildirimiyle Takviyeli Öğrenme)** girer. İnsan öğretmenler, yapay zekanın ürettiği milyonlarca fikir arasından saçma sapan olanları (Örn: _"Brokolili uzay gemisi motoru yiyin"_) elerken; mantıklı ve yaratıcı olanlara (Örn: _"Astronot kaskında çorba"_) yıldızlı pekiyi verirler. Yapay zeka da zamanla bu iki uzak konuyu "insan estetiğine uygun" şekilde çarpıştırmayı öğrenir.

---

### 2. Yapay Zekanın Kısa Tarihçesi: Kurallardan Yaratıcılığa

Yapay zeka gökten zembille inmedi; onun da bir gelişim hikayesi var:

1. **Doğuş (1956):** "Yapay Zeka" terimi ilk kez **John McCarthy** tarafından 1956 yılında Dartmouth Konferansı'nda ortaya atıldı (Alan Turing'in erken dönem teorik tartışmalarının ardından).
2. **Kural Tabanlı Sistemler Dönemi (İlk Klinik Dönem):** 1970'lerde ve 80'lerde YZ, sadece insanların yazdığı "EĞER... İSE..." kurallarına dayanıyordu. Örneğin: "EĞER hastanın kan şekeri 200'den yüksekse, O ZAMAN karbonhidratı kısıtla." Bu sistemler (MYCIN gibi) çok katıydı ve esnek değildi.
3. **Makine ve Derin Öğrenme Devrimi (2010'lar):** İnternetin yaygınlaşması ve bilgisayar güçlerinin artmasıyla YZ, kurallarla değil **büyük veriyle** öğrenmeye başladı. Fotoğraflardan yemek tanıma (Computer Vision) bu dönemde hızlandı.
4. **Üretken YZ Çağı (2022-Günümüz):** ChatGPT'nin 2022 sonlarında çıkmasıyla YZ, sadece sınıflandıran bir araç olmaktan çıkıp, diyetisyen gibi konuşabilen üretken bir asistana dönüştü.

---

### 3. Yapay Zeka Nasıl Çalışır? (Kelime Tahmin Etme Yaklaşımı ve Token)

Öğrencilerimizin en çok şaşırdığı gerçek şudur: **Yapay zeka aslında bizim anladığımız anlamda "düşünmez" veya klinik muhakeme yapmaz.**

#### Telefonunuzdaki "Klavye Tahmini" Oyunu

Yapay zeka (özellikle LLM'ler), telefonunuzda mesaj yazarken bir sonraki kelimeyi tahmin eden "otomatik tamamlama" (predictive text) özelliğinin çok gelişmiş bir versiyonudur. Kendisine verilen milyarlarca internet sayfasındaki istatistiksel kalıplara bakarak, **"Bu kelimeden sonra hangi kelimenin gelme olasılığı en yüksektir?"** sorusunun cevabını verir.

- **Token Nedir?**
    - Bilgisayarlar kelimeleri doğrudan okuyamaz. Bu yüzden metinleri **"token" (jeton)** adı verilen küçük anlamlı parçalara (bazen bir kelime, bazen bir hece veya birkaç harf) bölerler ve bunları sayılara (vektörlere) dönüştürürler.
    - _Metafor:_ Token'ları bir **yapboz parçası** gibi düşünebilirsiniz. YZ, tabağınızdaki yemeği analiz ederken veya "Diyet" kelimesini işlerken onu harf harf değil, bu yapboz parçalarıyla okur ve bir sonraki parçayı yerleştirir.

---

### 4. Prompt Nedir ve Nasıl Hazırlanır? (Diyetisyenin Sihirli Değneği)

Yapay zekaya verdiğimiz talimatlara **Prompt (Sutre/İstem)** denir. YZ girdiğiniz dile, promptun netliğine ve detayına aşırı duyarlıdır. Kötü bir prompt kötü bir diyet planına, iyi bir prompt ise profesyonel bir sonuca yol açar.

#### Prompt Teknikleri (Beslenme Örnekleriyle):

1. **Zero-Shot (Sıfır Örnekli) Prompting:** Modüle hiçbir örnek vermeden doğrudan ne istediğinizi söylemektir.
    - _Örnek:_ _"Tip 2 diyabet hastası için 1 günlük menü yaz."_ (YZ burada tamamen kendi hafızasına güvenir).
2. **Few-Shot (Birkaç Örnekli) Prompting:** Modüle neyi nasıl yapması gerektiğini gösteren birkaç örnek eklemektir.
    - _Örnek:_ _"Danışan: 'Çok tatlı krizim geliyor.' -> Çözüm: Tarçınlı ılık süt içebilirsiniz. Danışan: 'Akşam çok acıkıyorum.' -> Çözüm: Akşam yemeğine salatayla başlayabilirsiniz. Danışan: 'Sürekli su içmeyi unutuyorum.' -> Çözüm: [YZ burayı doldurur]"_.
3. **Chain of Thought (CoT - Düşünce Zinciri):** YZ'ye adım adım akıl yürütmesini söylemektir.
    - _Örnek:_ _"Bir porsiyon mercimek çorbasının kalorisini hesapla. Önce malzemelerin kalorilerini tek tek listele, ardından toplam porsiyon kalorisine nasıl ulaştığını adım adım açıkla."_ Bu yöntem hata oranını ciddi şekilde düşürür.
4. **RAG (Retrieval-Augmented Generation - Veri Kurtarma Destekli Üretim):** YZ'nin kendi kafasından uydurmasını engellemek için, ona güvenilir bir kütüphane (örneğin ulusal diyet kılavuzları) sunup, soruları sadece oradaki verilere bakarak cevaplamasını istemektir.
    - _Metafor:_ Sınavda kopya çekmek serbesttir ama sadece önünüzdeki açık kitaptan (kılavuzdan) bakarak yazabilirsiniz. Bu sayede YZ'nin uydurma şansı kalmaz.

---

### 5. Karanlık Taraf: Etik, Gizlilik, Halüsinasyon ve Kara Kutu

Yapay zeka harika bir asistan olsa da, beslenme gibi insan sağlığını doğrudan etkileyen bir alanda çok tehlikeli olabilir.

- **Halüsinasyon (Uydurma):** YZ'nin tamamen ikna edici bir üslupla, tamamen **yanlış veya uydurma bilgiler/kaynaklar üretmesidir**.
    - _Gerçek Hayat Riski:_ ChatGPT'nin besin alerjisi olan bir hasta için hazırladığı diyete alerjen besini (örneğin fındık alerjisi olan birine badem sütü) eklemesi veya vitamin eksikliklerini göz ardı etmesi klinik olarak kanıtlanmıştır.
- **Kara Kutu (Black Box) Problemi:** Yapay zekanın (özellikle derin öğrenme modellerinin) milyonlarca matematiksel işlem sonucunda bir karara nasıl ulaştığını insanların tam olarak anlayamamasıdır.
    - _Çözüm:_ **XAI (Explainable AI - Açıklanabilir Yapay Zeka)**. YZ'nin karar verme mantığını şeffaf bir şekilde açıklamasıdır.
- **Gizlilik ve KVKK (GDPR):** Danışanlarınızın kişisel sağlık verilerini (kan tahlilleri, kilo bilgileri vb.) genel yapay zeka araçlarına yüklediğinizde, bu veriler modelin eğitimi için kullanılabilir ve veri sızıntılarına yol açabilir. Bu yüzden veriler lokal (internet bağlantısı olmayan yerel bilgisayarlarda) veya şifrelenmiş güvenli sistemlerde işlenmelidir.
- **Dehumanization (Bakımın Robotlaşması/İnsansızlaşma):** Diyetisyenlik sadece kalori hesabı yapmak değildir; **empati**, motivasyonel görüşme ve insan dokunuşu gerektirir. Yapay zeka empati yapamaz, danışanın o günkü moral bozukluğunu anlayıp ona göre sarılamaz.

---

### 6. Popüler Sorular ve İlginç Gerçekler

#### Soru: Neden sürekli yeni modeller çıkıyor (GPT-4o, Claude 3.5, Gemini 1.5 vb.)?

Teknoloji şirketleri modellerin "bilgi kesilme tarihini" (knowledge cutoff) güncellemek, kelime kapasitesini (bağlam penceresini) artırmak ve daha akıllı, hızlı ve az hata yapan modellerle pazar payı kazanmak için yarışıyorlar.

#### Soru: Şirketlerin modellerinin birbirinden farkı ne?

Her model farklı algoritma ve veri setleriyle eğitilmiştir. Örneğin, **GPT-4o** klinik sınavlarda yüksek doğruluk ve tutarlılık gösterirken, **Grok-3** matematiksel ve bilimsel akıl yürütmede güçlüdür ancak şeffaflığı azdır; **DeepSeek** ise bütçe dostu, açık kaynak kodlu ve yapılandırılmış yanıtlar sunan bir modeldir.

#### Soru: Yapay zekanın "Su Tüketimi" neden olay oldu?

Yapay zeka modellerini eğitmek ve çalıştırmak için binlerce güçlü bilgisayarın (HPC sunucuları) bulunduğu **devasa veri merkezleri** gerekir. Bu bilgisayarlar çalışırken muazzam miktarda elektrik harcar ve aşırı ısınır. Sunucuları soğutmak için kullanılan soğutma kulelerinde milyonlarca litre **temiz su buharlaştırılarak tüketilir**. Birkaç soru sormak bile dolaylı olarak doğadan su eksilmesine yol açtığı için YZ'nin çevresel ayak izi (planetary health) büyük bir tartışma konusudur.

---

### 7. Beslenme Dünyasından İlginç Araştırma Örnekleri

Sınıfta arkadaşlarınızla paylaşabileceğiniz vizyon açıcı gerçek bilimsel çalışmalar:

1. **Diyetisyen Sınavını Geçen YZ:** 2025 yılındaki bir çalışmada, GPT-4o, Claude 3.5 ve Gemini 1.5 Pro modelleri Resmi Kayıtlı Diyetisyenlik (RD) sınavına sokulmuş ve tüm modeller **%88'in üzerinde başarı göstererek** sınavı geçmiştir!.
2. **Karbonhidrat Sayan Yapay Zeka:** Tip 1 diyabet hastalarının en büyük derdi karbonhidrat saymaktır. ChatGPT, Gemini ve Claude tabağın fotoğrafına bakarak karbonhidrat miktarını tahmin etmede denenmiş; diyetisyenler kadar olmasa da klinik tedaviye destek olabilecek seviyede tahminler yapabilmişlerdir.
3. **Yemek Fotoğrafından Kalori Hesaplama:** ChatGPT-5 ile yapılan güncel bir çalışmada, sadece yemek fotoğrafı verildiğinde kalori tahmin hatası yüksek çıkarken, tabağa dair malzemeler metin olarak prompta eklendiğinde YZ'nin hata payının neredeyse profesyonel cihazlar seviyesine indiği görülmüştür.



### 1. The Hook (Giriş ve Çelişki) - 10 Dakika

- **Süre:** 00:00 - 00:10
- **Amaç:** Öğrencilerin ilgisini çekmek ve zihinlerinde bir merak uyandırmak.
- **Şaşırtıcı Bilimsel Çelişki (The Hook):**
    - **Veri Noktası 1:** 2023 yılında yapılan bir çalışmada, ChatGPT'nin yaygın beslenme sorularına verdiği yanıtlar bilimsel doğruluk, anlaşılırlık ve uygulanabilirlik açısından insan diyetisyenlerin yanıtlarıyla karşılaştırılmıştır. Sonuçta ChatGPT, insan diyetisyenlerden birçok soruda **daha yüksek veya benzer puanlar almış**, hiçbir soruda insan diyetisyenler yapay zekadan anlamlı derecede daha yüksek puan alamamıştır!.
    - **Veri Noktası 2 (Çelişki):** Ancak aynı yapay zeka, besin alerjileri olan hayali bir hasta için hazırladığı 56 diyet planının 4 tanesine **hastanın ölümcül alerjisi olan malzemeleri (örneğin fındık alerjisi olan kişiye badem sütü) doğrudan yerleştirmiş** ve hiçbir uyarı yapmamıştır!. Ayrıca vegan diyet planlarında hayati öneme sahip **B12 vitaminini tamamen eksik bırakmıştır**.
    - **Sınıfa Soru:** _"Bir yapay zeka nasıl olur da diyetisyenlik sınavlarını ve teorik soruları bizden daha iyi cevaplayabilirken, gerçek bir hastanın tabağına onu zehirleyecek malzemeleri bu kadar kolay koyabiliyor? Bu derste bu gizemi çözeceğiz!"_.

### 2. Concept Deconstruction (Kavram Analizi ve Çalışma Mekanizması) - 20 Dakika

- **Süre:** 00:10 - 00:30
- **Amaç:** LLM'lerin çalışma mantığını matematiksel değil, pratik bir beslenme benzetmesiyle anlatmak.
- **"Ezberci Kör Şef" Metaforu:**
    - Yapay zekayı (LLM'ler), dünyadaki tüm yemek kitaplarını, beslenme bloglarını ve internetteki forum yazılarını kelimesi kelimesine ezberlemiş ama hayatında hiç yemek yememiş, diline tek bir lokma sürmemiş bir **"Kör Şefe"** benzetelim.
    - Bu şef, domatesin tadını bilmez; sadece internetteki tariflerde "domates" kelimesinden sonra %85 ihtimalle "zeytinyağı", %10 ihtimalle "tuz" ve %5 ihtimalle "fesleğen" kelimesinin geldiğini istatistiksel olarak bilir.
    - Siz ona bir prompt verdiğinizde, klinik bir akıl yürütme yapmaz. Sadece elindeki devasa "kelime olasılıkları tablosunu" açar ve telefonunuzun klavyesindeki kelime tahmini gibi **sıradaki en mantıklı jetonu (token) yan yana koyarak** bir cümle veya tarif oluşturur.
    - İşte bu yüzden, teoride "Mercimek çorbasında ne kadar protein vardır?" sorusunu ezberden mükemmel yanıtlar. Ancak pratikte ona "Alerjisi olan birine menü yaz" dediğinizde, internette sağlıklı smoothie tariflerinde sürekli gördüğü "badem sütü" kelimesini, hastanın alerjisi olduğunu unutarak (çünkü sadece sonraki kelime olasılığına odaklanır) tabağa koyuverir.

### 3. Friction Points (Bilişsel Engeller ve Çözümleri) - 10 Dakika

- **Süre:** 00:30 - 00:40
    
- **Öngörülen 2 Bilişsel Engel ve Çözüm Yolları:**
    
    1. **Friction Point 1: "Yapay zekanın kendi bilinci, klinik mantığı ve empati yeteneği var sanmak."**
        
        - _Sorun:_ Öğrenciler YZ'nin tıp kitaplarını "anlayarak" hastaya özel empati kurduğunu ve tıpkı bir insan hekim gibi düşündüğünü varsayarlar.
        - _Çözüm (Oyunlaştırma):_ Sınıftan bir öğrenciye telefonunu açtırın. Klavyede sadece orta tahmin tuşuna basarak bir beslenme cümlesi kurmasını isteyin (Örn: "Diyet yaparken her gün su içmek çok..."). Çıkan anlamsız ama gramer olarak doğru cümleyi gösterip: _"İşte ChatGPT de tam olarak bunu yapıyor, sadece milyarlarca kat daha büyük bir olasılık tablosuyla!"_ deyin.
    2. **Friction Point 2: "Yapay zekanın kararlarına tamamen güvenmek ve denetlemeyi unutmak."**
        
        - _Sorun:_ RD sınavında %88 alan bir sisteme öğrencilerin teslim olması ve "Diyet planını o yazsın, ben sadece imzalayayım" kolaycılığına kaçması.
        - _Çözüm:_ **"Human-in-the-Loop" (İnsan Denetimi)** kavramını öğretmek. Yapay zekanın sadece bir asistan (karar destek sistemi) olduğunu, imza ve sorumluluğun (ve uydurma/halüsinasyon riskinin) her zaman insana ait olduğunu, YZ çıktılarının mutlaka profesyonel bir diyetisyen tarafından onaylanması gerektiğini anlatmak.

### 4. Application Exercise: "Alerjen Mayın Tarlası" (Grup Çalışması) - 20 Dakika

- **Süre:** 00:40 - 01:00
- **Amaç:** Öğrencilerin öğrendikleri prompt tekniklerini ve insan denetimi (HITL) rolünü bizzat deneyimlemesi.

#### Öğrencilere Yönelik Talimatlar (Sınıfa Dağıtılacak Metin):

> **Senaryo:** Önünüzde yapay zeka (ChatGPT) tarafından hazırlanmış ve fıstık (peanut) ile sert kabuklu yemiş (tree nut) alerjisi olan bir danışan için yazılmış 1 günlük menü taslağı duruyor. Ancak yapay zeka, "kelime tahmini" mantığıyla çalıştığı için menünün içine tehlikeli malzemeler gizlemiş olabilir!
> 
> **Grup Görevi (4'er Kişilik Gruplar):**
> 
> 1. **Aşama 1 (Mayın Arama):** Aşağıdaki menüyü inceleyin ve bir diyetisyen gözüyle (HITL) potansiyel alerjen mayınlarını bulun.
>     - _Sabah:_ Yulaf ezmesi, muz ve **badem sütü** ile hazırlanmış kase.
>     - _Öğle:_ Izgara tavuklu yeşil salata (sosunda sızma zeytinyağı ve limon).
>     - _Ara Öğün:_ Elma dilimleri ve üzerine sürülmüş **fıstık ezmesi**.
>     - _Akşam:_ Fırında çipura ve haşlanmış sebzeler.
> 2. **Aşama 2 (Prompt Mühendisliği ile Mayın Temizleme):** Bu hataları yapay zekaya bir daha yaptırmamak için **"Rol Tanımlama"** (Act as a Dietitian) ve **"Adım Adım Düşünme"** (Chain of Thought) tekniklerini kullanarak yapay zekaya yazacağınız yeni, güvenli ve hatasız bir prompt (talimat) tasarlayın.
> 
> **Örnek Güvenli Prompt Taslağı:** _"Sen klinik beslenme alanında uzman, dikkatli bir diyetisyensin. Fıstık ve sert kabuklu yemiş alerjisi olan bir hasta için 1 günlük menü planla. Planı hazırlarken şu adımları takip et: 1. Alerjen listesini belirle. 2. Menüdeki her yemeğin malzemelerini tek tek kontrol et ve alerjen içermediğinden emin ol. 3. Menüyü yaz."_

Harika katkılar! Bir yapay zeka uzmanı ve diyetisyen gözüyle baktığımızda, ders içeriğini %100 mükemmel hale getirmek için tam olarak bu eksik parçaları tamamlamamız gerekiyor.

Beslenme ve diyetetik öğrencilerinin zihninde bu kavramların ömür boyu yer etmesini sağlayacak, **Yapay Sinir Ağları**, **Büyük Veri krizleri**, **ChatGPT'nin tarihsel soyağacı** ve **bir diyetisyenin bilmesi gereken ileri düzey popüler konuları** içeren genişletilmiş yeni ders notu ekini, etkileşimli mini anketi ve güncellenmiş 60 dakikalık ders planını aşağıda bulabilirsin.
### 1. Yapay Sinir Ağları (Artificial Neural Networks - ANN) Nedir?

Derin öğrenmenin kalbinde yer alan **Yapay Sinir Ağları (ANN)**, insan beynindeki nöronların (sinir hücrelerinin) birbirleriyle kurduğu biyolojik bağları taklit eden matematiksel sistemlerdir. Bir yapay sinir ağı; **Girdi Katmanı (Input Layer)**, bilgiyi işleyen **Gizli Katmanlar (Hidden Layers)** ve son kararı veren **Çıktı Katmanı (Output Layer)** olmak üzere üç ana bölümden oluşur.

#### 🍳 "Mutfak Yamakları ve Baş Şef" Metaforu

Yapay Sinir Ağını, büyük bir restoranın mutfak ekibine benzetelim:

- **Girdi Katmanı (Yamaklar):** Mutfağın kapısında duran ve malzemeleri içeri alan yamaklardır. Yapay zekaya bir yemek fotoğrafı verdiğimizde, bu yamaklar fotoğrafı piksellerine ayırıp içeri taşır. Örneğin; biri kırmızı rengi, diğeri dairesel şekli içeriye rapor eder.
- **Gizli Katmanlar (Uzman Aşçılar):** Mutfağın arkasında, her biri kendi işinde aşırı uzmanlaşmış aşçılar zinciridir. Birinci aşçı sadece "bıçak kesim şekillerine" bakar, ikinci aşçı "malzemenin dokusunu" analiz eder, üçüncü aşçı ise "buhar ve pişme derecesini" inceler. Bu aşçılar birbirlerine sürekli sinyal gönderir ("Hey, bu kırmızı nesne domatese çok benziyor, sen ne dersin?"). Derin Öğrenme (Deep Learning) dediğimiz şey, mutfaktaki bu uzman aşçı katmanlarının çok fazla (derin) olmasıdır.
- **Çıktı Katmanı (Baş Şef):** Tüm aşçılardan gelen raporları toplar ve tabağa son noktayı koyar: "Bu %94 ihtimalle sızma zeytinyağlı bir Akdeniz salatasıdır!".

---

### 2. Büyük Veri (Big Data) ve Yapay Zekanın "Veri Savaşları"

Yapay zeka modellerinin milyarlarca veya trilyonlarca parametreye sahip olduğunu duymuşsunuzdur. Bu kadar devasa bir beyni eğitmek için akılalmaz büyüklükte bir veriye, yani **Büyük Veri'ye (Big Data)** ihtiyaç vardır.

#### Neden Büyük Veriye İhtiyaç Var?

Yapay zeka, dünyadaki tüm beslenme kalıplarını anlayabilmek için milyonlarca insanın tahlil sonuçlarına, diyet günlüklerine ve yemek fotoğraflarına bakmak zorundadır. Model ne kadar çok veri görürse, o kadar hassas tahminlerde bulunur.

#### ⚠️ Büyük Tehlike: Yapay Zekanın "Veri Duvarı" (Eğitim Verisi Sıkıntısı)

Günümüzde yapay zeka şirketleri çok ciddi bir krizle karşı karşıya: **İnternetteki kaliteli insan verisi tükeniyor.** Yapay zekalar artık internetteki tüm kaliteli kitapları, bilimsel makaleleri ve makul forum yazılarını okuyup bitirdi.

- **Sonuç Ne Olabilir?** Şirketler artık modelleri eğitmek için yapay zekaların ürettiği "sentetik verileri" (yapay zekanın kendi yazdığı metinleri) kullanmaya başlıyor. Bu durum, **"Model Çökmesi" (Model Collapse)** adı verilen, yapay zekanın kendi uydurduğu yalanları tekrar okuyarak zamanla aptallaşması riskini doğuruyor.
- **Küçük Dillerin Diyet Dışı Kalması:** Eğitim verilerinin ezici çoğunluğu İngilizcedir. Örneğin; Kazakistan'da yapılan bir çalışmada, ChatGPT-4'ün İngilizce ve Rusça klinik beslenme tavsiyeleri başarılı bulunurken, Kazakça çıktılarının yetersiz eğitim verisi nedeniyle klinik olarak değerlendirilemeyecek düzeyde zayıf olduğu görülmüştür. Bu, beslenme biliminde **kültürel biyolojik eşitsizliğe** yol açabilir.

#### Şirketlerin Neden Bizim Verilerimize İhtiyacı Var?

Siz ChatGPT'ye her "Bugün ne yemeliyim?" diye sorduğunuzda veya bir kan tahlili yüklediğinizde, şirketler bu verileri modellerini **hizalamak (alignment)** ve **insan geri bildirimiyle pekiştirmeli öğrenme (RLHF)** ile eğitmek için kullanırlar. Ancak hastalarınızın hassas sağlık verilerini genel sistemlere yüklemek, uluslararası veri gizliliği yasalarını (GDPR/KVKK) ihlal eder. Bu yüzden beslenme dünyasında verilerin METROFOOD-IT projesindeki gibi güvenli ve anonimleştirilmiş sistemlerde işlenmesi kritik önem taşır.

---

### 3. ChatGPT Bir Günde mi Doğdu? (Transformers ve Dikkat Mekanizması)

2022'de ChatGPT hayatımıza girdiğinde bir büyü gibi hissettirdi. Ancak arkasında 70 yıllık bir birikim var.

- **Geçmişin Hantal Sistemleri (RNN ve LSTM):** Eski yapay zekalar kelimeleri sırayla okurdu. "Diyetisyen danışanına çok sağlıklı bir taze sıkılmış portakal..." cümlesini okurken, cümlenin sonuna geldiğinde başındaki "Diyetisyen" kelimesini unuturdu. Hafızaları çok dardı.
- **2017 Devrimi - Transformer Mimarisi:** Google araştırmacıları 2017'de **Transformer** adını verdikleri yeni bir yapay zeka mimarisi geliştirdiler. Bu mimarinin sihirli gücü **"Dikkat Mekanizması" (Attention Mechanism)** idi.
- **Dikkat Mekanizması Nedir?** Yapay zekanın bir metindeki tüm kelimelere aynı anda bakabilmesini ve aralarındaki mesafeye bakılmaksızın hangi kelimelerin birbiriyle ilişkili olduğunu "tartmasını" sağlar.
    - _Örnek:_ "Diyetisyen, yoğun geçen klinik gününün ardından masasındaki **elmayı** yedi, çünkü **o** çok acıkmıştı." Yapay zeka bu cümledeki "o" kelimesinin diyetisyene, "elma" kelimesinin ise yenilen nesneye ait olduğunu dikkat mekanizması sayesinde milisaniyeler içinde çözer.
- İşte bu Transformer mimarisinin üzerine milyarlarca internet verisi yüklenip, insan gibi konuşması için diyalog odaklı eğitilmesiyle (GPT modelleri) ChatGPT ve türevleri doğdu.

### 4. Diyetisyen ve AI Uzmanı Gözüyle Olmazsa Olmaz Popüler Kavramlar

İlk hafta dersine eklemeniz gereken, sizi öğrencilerinizin gözünde gerçek bir "Gelecek Vizyoneri" yapacak 3 kritik başlık:

#### A) SLM (Small Language Model - Küçük Dil Modeli) vs. LLM (Büyük Dil Modeli)

- **LLM (ChatGPT, Claude, Gemini):** Her şeyi bilen ama hiçbirinde uzman olmayan devasa genel kütüphanecilerdir. Bazen çok basit bir besin değerini uydurabilirler.
- **SLM (Küçük Dil Modeli):** Sadece beslenme bilimleri, gıda bileşenleri ve alerjen ontolojileri üzerine eğitilmiş minik, kompakt ama **aşırı keskin** yapay zekalardır.
    - _Trend:_ Beslenme dünyasında geleceğin teknolojisi, LLM'lerin konuşma yeteneğiyle gıda sektörüne özel eğitilmiş SLM'lerin (Spoon Guru'nun gıda kategorizasyon modelleri gibi) bir arada kullanılmasıdır.

#### B) Multimodal (Çok Modlu) AI ve Görsel Zayıflık: "Çorba Kasesi Çıkmazı"

Yapay zeka artık sadece yazmıyor; yemek fotoğraflarını da görüp kalori tahmini yapabiliyor. Buna **Multimodal (Çok Modlu) AI** diyoruz. Ancak klinik çalışmalarda ortaya çıkan harika bir zayıflık var:

- Yapay zekalar (en gelişmiş ChatGPT-5 bile), yemek **düz bir tabakta** sunulduğunda kalori ve karbonhidrat miktarını harika tahmin ederken, yemek **derin bir kasede veya çorba formunda** sunulduğunda derinliği ve hacmi çözemez ve aşırı derecede hata yapar. Çünkü tek bir fotoğraftan derinlik algılamak (monocular depth) yapay zeka için hala çok zordur.

#### C) RAG (Retrieval-Augmented Generation) Nedir?

Yapay zekanın halüsinasyon görüp uydurma kaynak yazmasını engellemenin en modern yolu **RAG** sistemidir.

- _Öğrencilere Örnek:_ Sınava giriyorsunuz. Sorular tamamen hafızanızdan çıkarsa uydurabilirsiniz (Normal LLM). Ama öğretmen size sınavda "TÜBER (Türkiye Beslenme Rehberi)" kitabını veriyor ve "Soruları sadece bu kitaba bakarak cevapla" diyor (RAG). Bu sayede uydurma sıfıra iner.
- C) Sorulan soruyu çok yavaş yanıtlaması.
- _Aha! Açıklaması:_ Halüsinasyon, yapay zekanın tamamen uydurma ama son derece bilimsel tınlayan kaynaklar ve iddialar üretmesidir. Klinik beslenmede bu durum ölümcül olabilir!


### 1. The Hook (Giriş ve Çelişki) - 10 Dakika

- **Süre:** 00:00 - 00:10
- **Öğretim Metodu:** Şaşırtıcı Veri Karşılaştırması ve Soru-Cevap
- **Akış ve Veriler:**
    - Dersi şu çelişkiyle açın: _"Sevgili arkadaşlar, 2023 yılında Wageningen Üniversitesi'nde yapılan bilimsel bir araştırmada, ChatGPT'nin yaygın beslenme sorularına verdiği yanıtlar, gerçek uzman diyetisyenlerin yanıtlarıyla karşılaştırıldı ve jüriye kör değerlendirme yaptırıldı. Sonuçta, ChatGPT bilimsel doğruluk, uygulanabilirlik ve anlaşılırlıkta diyetisyenleri geride bıraktı veya benzer puanlar aldı. Hiçbir soruda insanlar yapay zekayı geçemedi!"_
    - **Giriş Çelişkisi:** _"Ancak, aynı ChatGPT ile yapılan güncel araştırmalarda; fıstık alerjisi olan hayali hastalar için hazırladığı reçetelerin %7'sine ölümcül fıstık ezmesi koydu, vegan hastalar için yazdığı listelerde ise hayati önemdeki B12 vitaminini tamamen unuttu. Nasıl oluyor da diyetisyenlik sınavlarını %88 başarıyla geçen bir sistem, gerçek bir insanı zehirleyecek hataları bu kadar kolay yapabiliyor? Bugün yapay zekanın kafasının içine bakacağız."_

### 2. Concept Deconstruction (Kavram Analizi ve Analojiler) - 20 Dakika

- **Süre:** 00:10 - 00:30
- **Öğretim Metodu:** Görsel Analoji ve İnteraktif Modelleme
- **Akış ve Analojiler:**
    - **Yapay Sinir Ağları (ANN) -> "Mutfak Yamakları ve Aşçılar":** AI, ML, DL ve ANN kavramlarını mutfak hiyerarşisiyle tahtaya çizin. Yamakların bilgiyi alıp (Girdi), gizli bölmedeki uzman aşçılara (Gizli katmanlar) paslamasını ve en son baş şefin (Çıktı) tabağı isimlendirmesini anlatın.
    - **Transformer ve Dikkat Mekanizması -> "Tabaktaki Malzemeleri Aynı Anda Gören Gurme":** Eski yapay zekaların (RNN) malzemeleri tek tek ve sırayla koklayıp son kokuyu aldığında ilk kokuyu unuttuğunu, 2017'de doğan Transformers'ın ise tabaktaki tüm malzemeleri aynı anda görüp hangisinin diğeriyle uyumlu olduğuna (Dikkat Mekanizması) karar verdiğini örnekleyin.
    - **Token Jetonu:** Kelimelerin bilgisayar dilindeki yapboz parçaları (Token) olduğunu gösterin.

### 3. Friction Points (Bilişsel Engeller ve Çözümleri) - 10 Dakika

- **Süre:** 00:30 - 00:40
- **Öğretim Metodu:** Canlı Uygulama ve Kavramsal Düzeltme
- **Engeller ve Çözüm Yolları:**
    - **Friction Point 1: "Yapay zekanın interneti bir ansiklopedi gibi okuyup doğru bildiğini sanmak."**
        - _Sorun:_ Öğrenciler ChatGPT'yi akademik bir kütüphane sanırlar.
        - _Çözüm:_ Öğrencilere yapay zekanın aslında sadece forumlardaki diyet mitlerini, magazin haberlerini ve kirli internet bilgilerini ezberlediğini açıklayın. _"O bir bilim insanı değil, internetteki dedikoduları çok iyi sentezleyen bir taklitçidir"_ deyin.
    - **Friction Point 2: "Çok Modlu (Multimodal) AI her şeyi kusursuz görüyor sanmak."**
        - _Sorun:_ Yemek fotoğrafı atıldığında yapay zekanın kaloriyi tam bildiğine inanmak.
        - _Çözüm:_ Canlı ders örneği olarak tahtaya bir çorba kasesi çizip: _"Yapay zeka bu çorbanın sadece yüzeyini görür, kasenin ne kadar derin olduğunu algılayamaz. Bu yüzden derinlik (monoküler derinlik) krizini çözemez"_ diyerek öğrencilere klinik denetimin (HITL) neden şart olduğunu gösterin.

### 4. Application Exercise: "Çorba Kasesi ve Alerjen Avı" - 20 Dakika

- **Süre:** 00:40 - 01:00
- **Öğretim Metodu:** Durum Tabanlı Grup Senaryosu ve Prompt Tasarımı

#### Öğrencilere Yönelik Dağıtılacak Çalışma Yönergesi:

> **GÖREV TANIMI:** Sizler bir hastanede klinik diyetisyen olarak çalışıyorsunuz. Altınızda çalışan stajyer yapay zekanız (ChatGPT-5), çölyak hastası (glutensiz beslenmesi gereken) ve ciddi badem alerjisi olan bir danışan için bir akşam yemeği menüsü ve görseli analiz etmiş. Ancak yapay sinir ağları "kase derinliğini" algılayamadığı ve uydurma kelime eğiliminde olduğu için menüde hatalar yapmış olabilir.
> 
> **Aşama 1 (Hata Analizi - HITL / İnsan Denetimi Rolü) - 8 Dakika:** Aşağıdaki yapay zeka çıktısını inceleyin ve klinik olarak tehlikeli "mayını" ve "tahmin hatasını" bulun:
> 
> - _Yemek:_ Glutensiz yulaf unlu, kıvam artırmak için içine gizlice **arpa şerbeti** eklenmiş kremalı domates çorbası.
> - _Sunum:_ Çorba derin bir porselen kasede sunuluyor. Yapay zeka tahmini: _"Bu çorba düz tabakta duruyor gibi görünüyor, porsiyonu yaklaşık 150 ml'dir ve 80 kaloridir."_ (Gerçekte kase 450 ml çorba alıyor!).
> - _Üzerindeki Süsleme:_ İnce kıyılmış **badem parçacıkları** (Yapay zeka bunu görsel olarak algılayamamış!).
> 
> **Aşama 2 (RAG ve Gelişmiş Prompt Tasarımı) - 12 Dakika:** Grubunuzla birlikte, yapay zekanın bu monoküler derinlik hatasını ve alerjen uydurmalarını bir daha yapmasını engelleyecek bir **"Düşünce Zinciri (CoT)"** ve **"Rol Tanımlı"** prompt tasarlayın. Yapay zekaya, tahmin yaparken tabağın yanına koyulmuş bir cetveli referans almasını ve malzemeleri tek tek doğrulamasını emredin.

---

### 1. "Human-in-the-Loop" (HITL) Tam Olarak Nedir?

Yapay zekada üç temel çalışma modeli vardır. Kavramı netleştirmek için bunları bir **hastane mutfağı** üzerinden örneklendirelim:

1. **Human-Out-of-the-Loop (İnsansız Sistem):** Yapay zeka kararları tamamen kendi başına alır ve uygular.
    - _Örnek:_ Bir mobil uygulamanın, hastanın tahlillerine bakıp hiçbir diyetisyen kontrolü olmadan doğrudan hastanın telefonuna menü göndermesi. Klinik beslenmede bu model **kabul edilemez ve ölümcül** riskler taşır.
2. **Human-on-the-Loop (İnsanın Gözlemci Olduğu Sistem):** Yapay zeka sistemi çalıştırır, insan sadece uzaktan izler ve büyük bir hata gördüğünde acil durum frenine basar.
3. **Human-in-the-Loop (İnsanın Sistemin Kalbinde Olduğu Sistem):** Yapay zeka ve insan uzman sürekli etkileşim halindedir. Yapay zeka karmaşık verileri işler, taslaklar hazırlar; ancak **klinik muhakeme, dozu belirleme, hastaya özgü adaptasyon ve nihai klinik sorumluluk** tamamen insandadır. Yapay zeka, insan uzmanı devre dışı bırakamaz; aksine insan uzmanın yeteneklerini büyütmek (augmentation) için çalışır.

---

### 2. Neden Yapay Zekayı Kendi Başına Bırakamayız? (Bilimsel Kanıtlar)

Literatürdeki en güncel klinik çalışmalar, yapay zekanın tek başına diyet yazacak veya klinik karar alacak zekaya sahip olmadığını net şekilde ortaya koymaktadır:

- **Aşırı Karbonhidrat Tahmini ve İnsülin Riski:** Tip 1 Diyabet hastalarında karbonhidrat sayımı hayati önem taşır. 2026 yılında yapılan bir araştırmada; Claude, Gemini ve ChatGPT'nin tabak fotoğrafları üzerinden karbonhidrat miktarı tahminleri incelenmiştir. Gemini'nin **%38**, Claude'un **%17** oranında **20 gramın üzerinde aşırı karbonhidrat tahmini (overestimation)** yaptığı saptanmıştır. Eğer bir hasta yapay zekaya güvenip bu tahmine göre yüksek dozda insülin vurulursa, **ölümcül hipoglisemi komasına** girebilir.
- **Alerjen Mayınları:** ChatGPT ile yapılan ünlü "alerji" simülasyonunda, 56 diyet listesinin 4 tanesine hastanın **ölümcül alerjisi olan besinlerin** (badem sütü gibi) yerleştirildiği saptanmıştır.
- **Mikronutrient ve Kalori Açıkları:** Yapay zeka tarafından hazırlanan vegan listelerinde **B12 vitamini**, demir, kalsiyum ve D vitamini gibi kritik mikro besinlerin sıklıkla unutulduğu veya yetersiz bırakıldığı saptanmıştır.

İşte bu yüzden, yapay zekanın ürettiği çıktılarda **aktif bir diyetisyen denetimi (HITL)** klinik güvenliğin tek teminatıdır.

---

### 3. Diyetisyen ve Beslenme Uzmanı Olarak "HITL"da Nasıl Kalabiliriz? (Pratik Yöntemler)

Bir diyetisyen olarak yapay zekayla çalışırken "döngünün içinde kalmanın" ve sistemi kontrol etmenin **4 somut yolu**vardır:

#### 🗺️ Yöntem 1: Sistem Tasarımcısı ve "Kural Koyucu" Rolü (Spoon Guru Örneği)

HITL sadece klinikte hasta bakarken değil, yapay zeka sistemleri henüz yazılım aşamasındayken başlar. Global bir yapay zeka ve beslenme şirketi olan **Spoon Guru**, milyonlarca gıda ürününü algoritmalarla analiz ederken tam olarak bu yöntemi kullanır.

- **Süreç:** Veri bilimciler kod yazar; ancak gıda maddelerinin alerjen, glisemik indeks veya kültürel uygunluk kurallarını (ontoloji) **beslenme uzmanları** belirler.
- **Nasıl Uygulanır?** Bir yapay zeka modeline "Diyabetik smoothie hazırla" kodu yazılmadan önce, beslenme uzmanı sisteme şu kuralı gömer: _"Eğer smoothie tarifi üretiyorsan, kaloriyi ≤350 kcal, karbonhidratı ≤50 g, lifi ise ≥8 g sınırında tutmalısın"_. Algoritma bu kuralların dışına çıkamaz. İnsan, sistemin anayasasını yazan kişidir.

#### 🩺 Yöntem 2: Klinik Karar Destekli Denetim (Copilot Kullanımı)

Hastalarınız için yapay zekadan faydalanırken, onu bir "hazır liste makinesi" olarak değil, bir **idari asistan** olarak konumlandırırsınız.

- **Süreç (Üç Adımlı Doğrulama Protokolü):**
    1. **Veri Analizi:** Hastanın kan tahlilini ve beslenme günlüğünü yapay zekaya analiz ettirip kalıpları (örneğin hastanın hafta sonları protein alımının çok düştüğünü) saptamasını istersiniz.
    2. **Taslak Üretimi:** Yapay zekaya bu kalıplara uygun bir menü taslağı hazırlatırsınız. (Bu işlem diyetisyenin saatler süren menü yazım yükünü hafifletir ve tükenmişliği önler).
    3. **Klinik Filtre (HITL):** Çıkan taslağı hastaya vermeden önce şu 3 soruyu sorarak **klinik süzgecinizden**geçirirsiniz:
        - _Bu menüde hastanın kronik hastalıklarına (örneğin hipertansiyonuna) aykırı gizli sodyum var mı?_
        - _Yapay zeka popüler diyet mitlerine kapılıp uydurma bir besin önermiş mi?_
        - _Menü hastanın sosyo-ekonomik durumuna ve pişirme becerisine pratik olarak uygun mu?_

#### 🔍 Yöntem 3: Açıklanabilir Yapay Zeka (XAI) ve "İzlenebilir Mantık" Denetimi

Bir yapay zeka size bir öneri sunduğunda, ona körü körüne inanmak yerine **mantığını sorgulamak** HITL'ın en güçlü adımlarından biridir.

- **Nasıl Uygulanır?** Prompt hazırlarken modele şu talimatı eklersiniz: _"Bu diyabetik menüde karbonhidrat dağılımını nasıl yaptığını, hangi bilimsel kılavuzu (örneğin ADA kılavuzunu) referans aldığını adım adım açıkla ve kaynaklarını göster"_.
- **Faydası:** Yapay zekanın arkadaki "Kara Kutu" (Black Box) işlemlerini şeffaflaştırarak, mantık yürütme yolundaki hataları (hallucination) çok daha kolay yakalamanızı sağlar.

#### 🤝 Yöntem 4: İletişim ve Davranışsal Liderlik (Empati Köprüsü)

Diyetisyenlik sadece bir kalori hesaplama veya kimya bilimi değildir; aynı zamanda bir **psikoloji ve iletişim** sanatıdır. Yapay zeka ne kadar gelişirse gelişsin, hastanın gözlerinin içine bakıp onun motivasyonunu yükseltemez, tabağıyla kurduğu duygusal bağı (örneğin tıkınırcasına yeme atağı arkasındaki stresi) anlayamaz.

- **Nasıl Uygulanır?** Hesaplamaları, veri grafiklerini ve rutin şablon taslaklarını yapay zekaya bırakıp; kazandığınız vakti hastanızla **motivasyonel görüşme (motivational interviewing)** yapmaya, empati kurmaya ve davranış değişikliği terapileri uygulamaya harcarsınız. Böylece yapay zeka arka planda veri motoru olarak çalışırken, siz tedavinin **insani ön planında** lider kalırsınız.

---

### 🎓 Sınıf İçi Tartışma / Akıl Defteri Egzersizi

**Senaryo:** Böbrek yetmezliği ve gut hastalığı olan karmaşık bir danışanınız var. Yapay zeka asistanınız, bu hasta için mükemmel kalori dengesine sahip, protein sınırlarını tutturmuş harika bir menü hazırladı. Ancak menünün içine **pürin içeriği çok yüksek olan ıspanak ve sakatat türevlerini** yerleştirmiş.

1. Diyetisyen olarak bu vakanın neresinde **"Human-in-the-Loop"** rolünüzü oynamalısınız?
2. Yapay zekanın bu hatasını hastaya zarar vermeden önce nasıl bloke edersiniz?
3. Sistemin bu hatayı gelecekte yapmaması için sistem promptuna hangi kısıtlama kurallarını eklemelisiniz?


# 2.Hafta
TIBBIN VE SAĞLIĞIN BÜYÜK DÖNÜŞÜMÜ

Beslenme bilimindeki yapay zeka devrimini anlamak için, önce içinde bulunduğumuz **sağlık ve tıp paradigmasının** nasıl küresel bir tektonik kayma yaşadığını kavramamız gerekir. Yapay zeka beslenmeyi dönüştürüyor; çünkü tıp zaten baştan aşağı yeniden yazılıyor.

1. Eski Tıp Paradigması: Reaktif ve İndirgemeci Dönem (Reductionist & Reactive Era)

Eski dünya tıbbı ve beslenme bilimleri iki temel direğe dayanırdı:

1. **Reaktif Yaklaşım (Hastalık Odaklı):** Sistem, hasta olmanızı bekler. Sağlıklı bir birey doktora gitmez. Ne zaman ki tahliller bozulur, semptomlar başlar; tıp o zaman devreye girer ve hasarı onarmaya (tedavi etmeye) çalışır.
2. **İndirgemeci (Reductionist) ve Tek Tipçilik (One-Size-Fits-All):** İnsan vücudu çok karmaşık bir makinedir. Eski tıp, bu makineyi parçalarına ayırarak incelerdi. Beslenmede de durum aynıydı: _"Günlük 2000 kalori al, yağ oranını %30'da tut, herkes için ideal olan Akdeniz diyetidir"_ denilirdi. Ancak bu yaklaşım, iki farklı insanın aynı tabağı yediğinde neden tamamen farklı metabolik tepkiler (biri zayıflarken diğerinin şekerinin fırlaması) verdiğini açıklayamazdı.

3. Yeni Tıp Paradigması: 4P Tıp Çağı (Preventive, Predictive, Personalized, Participatory)

**Sistem Biyolojisi**, **Büyük Veri (Big Data)** ve **Yapay Zeka** teknolojilerinin birleşmesiyle, sağlık sektörü reaktif modelden **4P Tıp** paradigmına evrilmiştir:

```
+---------------------------------------------------------------------------------+
|                                 4P TIP ÇAĞI                                     |
+-------------------+-------------------------------------------------------------+
| 1. PREVENTIVE     | Hastalık ortaya çıkmadan, hücresel düzeyde önleme odaklıdır. |
| (Önleyici)        |                                                             |
+-------------------+-------------------------------------------------------------+
| 2. PREDICTIVE     | Genomik ve yapay zeka analizleriyle, bireyin 10 yıl sonra    |
| (Öngörücü)        | hangi hastalıklara yakalanacağını tahmin eder.              |
+-------------------+-------------------------------------------------------------+
| 3. PERSONALIZED   | Tek tip tedavi yerine, kişinin genetiğine, mikrobiyomuna ve |
| (Kişiselleşmiş)   | metabolizmasına özel "nokta atışı" tedavi sunar.            |
+-------------------+-------------------------------------------------------------+
| 4. PARTICIPATORY  | Hasta pasif bir izleyici değil, giyilebilir cihazlarla kendi |
| (Katılımcı)       | sağlığını 7/24 takip eden aktif bir katılımcıdır.           |
+-------------------+-------------------------------------------------------------+
```

İşte **Hassas Beslenme (Precision Nutrition)**, bu küresel tıp dönüşümünün en güçlü ve en dinamik çocuğudur. Beslenme artık sadece kilo verdiren bir diyet listesi değil; 4P tıbbın en önemli önleyici ve kişiselleştirilmiş tedavi aracıdır.

BESLENME BİLİMİNDE DÖNÜŞÜMÜN 5 TEMEL İLKESİ

Tıptaki bu devasa paradigma kaymasını beslenme bilimlerine uyguladığımızda, mesleğimizin anayasasını yeniden yazan **5 Temel Dönüşüm İlkesi** ortaya çıkar:

```
+-----------------------------------------------------------------------------------------+
|                        BESLENMEDE DÖNÜŞÜMÜN 5 TEMEL İLKESİ                              |
+-------------------+---------------------------------------------------------------------+
| 1. İLKE           | Bireyselleştirilmiş Hassas Beslenme ve Omik Veri Entegrasyonu       |
+-------------------+---------------------------------------------------------------------+
| 2. İLKE           | Reaktif Teşhisten Gerçek Zamanlı Proaktif Karar Desteğine Geçiş     |
+-------------------+---------------------------------------------------------------------+
| 3. İLKE           | Aktif Kullanıcı Beyanından Pasif ve Kesintisiz Gözleme Geçiş        |
+-------------------+---------------------------------------------------------------------+
| 4. İLKE           | Bilgi Bekçiliğinden "İnsan-Merkezli" (HITL) Sistem Tasarımcılığına  |
+-------------------+---------------------------------------------------------------------+
| 5. İLKE           | Bireysel Sağlıktan Gezegensel Sürdürülebilirlik Uyumuna Evrilme     |
+-------------------+---------------------------------------------------------------------+
```

---

🧬 1. İLKE: Bireyselleştirilmiş Hassas Beslenme ve Omik Veri Entegrasyonu

- **Dönüşüm Dinamiği (Eskiden Nasıl/Şimdi Nasıl?):**
    - _Eskiden:_ Diyetisyenler, hastanın sadece yaş, boy ve kilosuna bakarak statik formüllerle (Harris-Benedict vb.) enerji ihtiyacı hesaplar ve genel popülasyon kılavuzlarına göre diyet yazarlardı.
    - _Şimdi ve Gelecekte:_ Yapay zeka; bireyin **genetik haritasını (nutrigenomik)**, bağırsaklarındaki trilyonlarca bakterinin profilini **(mikrobiyom)** ve kan/idrarındaki biyolojik parmak izlerini **(metabolomik)** entegre eder. Bu devasa veri havuzundan (Büyük Veri), o kişinin hangi gıdaya nasıl bir postprandiyal glisemik (yemek sonrası şeker) tepki vereceğini milimetrik tahmin eden sistemler (Dijital İkiz) kurulmaktadır.
- **Bilimsel Kanıt ve Bulgular:**
    - Santhuja ve ark. tarafından yapılan IoT ve makine öğrenimi entegrasyonu çalışmasında, gerçek zamanlı biyosensör verileriyle beslenen yapay zekanın, bireylere özel beslenme planları üretmede **%86 doğruluk oranına** ulaştığı saptanmıştır.
    - Iwendi ve ark. tarafından IoMT (Tıbbi Şeylerin İnterneti) verileri kullanılarak geliştirilen LSTM (Uzun Kısa Süreli Hafıza) yapay sinir ağı modelinin, kronik hastaların sağlık parametrelerine göre tüketebileceği "izin verilen" güvenli besinleri sınıflandırmada **%97.74 doğruluk, %98 hassasiyet (precision) ve %99 F1-skoruna** ulaştığı kanıtlanmıştır.
- **Diyetisyen Nasıl Adapte Olmalı?**
    - Diyetisyenler sadece kalori hesaplamayı değil; genetik test raporlarını, mikrobiyom tahlil sonuçlarını ve biyobelirteç grafiklerini okumayı öğrenmelidir. Geleceğin diyetisyeni, biyoloji ile veri biliminin kesişiminde duran bir **"Beslenme Biyo-Enformatisyeni"** olacaktır.

---

📊 2. İLKE: Reaktif Teşhisten Gerçek Zamanlı Proaktif Karar Desteğine Geçiş

- **Dönüşüm Dinamiği (Eskiden Nasıl/Şimdi Nasıl?):**
    - _Eskiden:_ Hastanelerde malnütrisyon (yetersiz beslenme) teşhisi, hasta yatağında belirgin kas kaybı ve ödem oluştuktan (hasar oluştuktan) sonra konulurdu. Taramalar hantal ve gecikmeliydi.
    - _Şimdi ve Gelecekte:_ Yapay zeka, hastanın hastaneye adım attığı andan itibaren tüm laboratuvar ve klinik verilerini arka planda proaktif olarak tarar. Klinik beslenme ekiplerine, hangi hastanın daha yüksek malnütrisyon riski taşıdığını henüz semptomlar fiziksel olarak gözle görülür hale gelmeden önce gerçek zamanlı olarak raporlar.
- **Bilimsel Kanıt ve Bulgular:**
    - Mount Sinai Sağlık Sistemi'nde 6 farklı hastanede 3 yıl boyunca geriye dönük olarak doğrulanan **MUST-Plus** klinik uygulaması, yatak başı manuel taramaların hantallığını tamamen ortadan kaldırmıştır. EHR verilerini otomatik tarayan bu yapay zeka modeli, diyetisyen ekibinin günlük klinik vizit turlarını optimize etmesini ve en yüksek riskli hastaları saniyeler içinde önceliklendirmesini (prioritize) sağlamıştır.
    - Peking Union Hospital’ın **FANS** doğal dil işleme çerçevesi, doktorların serbest metin olarak girdiği klinik notları tarayarak, gözden kaçabilecek "istemsiz kilo kaybı" ve "yutma güçlüğü" gibi riskleri **0.9142 F1-skoru** gibi olağanüstü bir doğrulukla saptamış ve erken tanı sürelerini dramatik şekilde kısaltmıştır.
- **Diyetisyen Nasıl Adapte Olmalı?**
    - Diyetisyenler, hastane otomasyon sistemlerine entegre edilen karar destek algoritmalarını yönetmeyi öğrenmelidir. Yapay zekanın ürettiği risk skorlarını (0 ile 1 arasındaki olasılıkları) klinik deneyimleriyle birleştirerek, yatak başında **hızlı ve proaktif klinik eylem** alabilme yeteneğini geliştirmelidir.

---

⏱️ 3. İLKE: Aktif Kullanıcı Beyanından Pasif ve Kesintisiz Gözleme Geçiş

- **Dönüşüm Dinamiği (Eskiden Nasıl/Şimdi Nasıl?):**
    - _Eskiden:_ Diyet izleme süreci tamamen hastanın dürüstlüğüne ve hafızasına bağlıydı. Hasta gün boyu yediklerini kağıda yazar (aktif beyan) veya diyetisyenin karşısında "dün ne yediğini" hatırlamaya çalışırdı (24HR recalls). Bu durum, hastaların yediklerini saklaması veya unutması nedeniyle devasa veri sapmalarına (underreporting) yol açardı.
    - _Şimdi ve Gelecekte:_ Giyilebilir sensörler, akıllı gözlükler ve pasif kameralar sayesinde diyet izleme süreci **kesintisiz, zahmetsiz ve tamamen objektif** bir pasif gözleme dönüşmektedir.
- **Bilimsel Kanıt ve Bulgular:**
    - Afrika popülasyonlarında bizzat denenen **EgoDiet** gibi giyilebilir yapay zeka destekli kamera sistemleri, kullanıcının göğsüne takılan pasif bir lens aracılığıyla gün boyu yenen besinleri, porsiyonları ve yeme hızını diyetisyenin ekranına otomatik aktarabilmektedir.
    - goFOOD™ sistemi, tek kameralı veya çift kameralı akıllı telefonlardan alınan iki fotoğrafla tabak segmentasyonu yaparak, porsiyon hacmini tahmin etmede ve kaloriyi saptamada **%94.4 gibi yüksek bir doğruluk düzeyi** elde etmiş ve deneyimli diyetisyenlerden daha düşük bir hata payıyla çalışmıştır.
- **Diyetisyen Nasıl Adapte Olmalı?**
    - Yeni nesil diyetisyenler, hastaların manuel besin günlüklerini okumak yerine; giyilebilir cihazlardan, sürekli glikoz monitörlerinden (CGM) ve akıllı terazilerden gelen **anlık veri akış grafiklerini (sensör analitiği)** yorumlayabilmeli ve uzaktan hasta izleme (Remote Patient Monitoring) yetkinliklerini artırmalıdır.

---

🤝 4. İLKE: Bilgi Bekçiliğinden "İnsan-Merkezli" (HITL) Sistem Tasarımcılığına

- **Dönüşüm Dinamiği (Eskiden Nasıl/Şimdi Nasıl?):**
    - _Eskiden:_ Diyetisyen, beslenme bilgisinin tek sahibi ve bekçisiydi (gatekeeper). Hasta bilgiye ulaşmak için diyetisyenin ofisine gelmek zorundaydı.
    - _Şimdi ve Gelecekte:_ Bilgi artık her yerdedir; internette ve yapay zeka sohbet robotlarında sınırsız beslenme tavsiyesi bulunmaktadır. Ancak bu kontrolsüz bilgi okyanusu, ölümcül alerjen hatalarını, bilimsel dezenformasyon salgınını (infodemic) ve halüsinasyonları beraberinde getirmektedir. Diyetisyenin rolü bilgi sunmaktan, yapay zekayı denetleyen ve yöneten bir **"Sistem Tasarımcısı ve Güvenlik Denetçisi (HITL)"** rolüne evrilmektedir.
- **Bilimsel Kanıt ve Bulgular:**
    - Azimi ve ark. tarafından yapılan ve yapay zekaların diyetisyenlik sınavlarındaki başarısını ölçen çalışmada, gelişmiş prompt teknikleri (CoT-SC) kullanıldığında modellerin **%94.48 gibi olağanüstü bir teorik başarı** gösterdiği kanıtlanmıştır. Ancak aynı çalışmada, harici bilgi kurtarma (RAG) sistemlerine alakasız veriler beslendiğinde, modellerin kendi içsel tıbbi doğrularını da unutarak "bilgi zehirlenmesi" yaşadığı ve sınav performanslarının düştüğü keşfedilmiştir.
    - Daha da önemlisi, Bayram ve Arslan (2025) çalışmasında görüldüğü üzere, genel yapay zekaların (ChatGPT-4.1) hazırladığı diyabet menülerindeki **doymuş yağ oranını klinik güvenlik sınırının %172 üzerine çıkarması**, yapay zekanın "insan süzgeci" (HITL) olmadan tek başına serbest bırakılamayacağının en büyük kanıtıdır.
- **Diyetisyen Nasıl Adapte Olmalı?**
    - Diyetisyenler, yapay zekayı sadece kullanmakla kalmamalı; güvenli ve kanıta dayalı RAG beslenme yazılımlarının geliştirilmesinde, klinik kuralların (guardrails) algoritmaya gömülmesinde ve yapay zeka çıktılarının son onay makamı (HITL) olarak doğrulanmasında **aktif sistem mimarı** rolünü üstlenmelidir.

---

🌍 5. İLKE: Bireysel Sağlıktan Gezegensel Sürdürülebilirlik Uyumuna Evrilme

- **Dönüşüm Dinamiği (Eskiden Nasıl/Şimdi Nasıl?):**
    - _Eskiden:_ Diyet planlaması sadece mikro ve makro besin dengesine göre, bireysel sağlık hedefleri (zayıflama, kas kazanımı) odağında yapılırdı. Tabağın çevreye, su kaynaklarına ve karbon ayak izine olan dolaylı etkileri klinik hesaplamaların tamamen dışındaydı.
    - _Şimdi ve Gelecekte:_ Geleceğin beslenmesi, Birleşmiş Milletler Sürdürülebilir Kalkınma Amaçları (SDGs) doğrultusunda hem insan sağlığını hem de gezegenin sağlığını (Planetary Health) aynı anda optimize etmek zorundadır. Yapay zeka, bu çok boyutlu optimizasyon problemini saniyeler içinde çözen tek araçtır.
- **Bilimsel Kanıt ve Bulgular:**
    - University of Twente'den Gavai ve van Hillegersberg (2025) tarafından geliştirilen RAG tabanlı "Sanal Diyetisyen" sistemi, sadece Tip 2 Diyabet ve obezite hedeflerini (kalori, lif, şeker kısıtı) tutturmakla kalmamış; aynı zamanda gıdaların Hollanda Ulusal Halk Sağlığı Enstitüsü (RIVM) veritabanındaki **karbon ayak izi, su tüketimi, mevsimsellik ve yerel üretim** parametrelerini de aynı algoritmanın içine yerleştirmiştir.
    - Yapay zeka sistemi, hazırladığı 1,000 farklı reçetede **%80.1 oranında klinik beslenme kılavuzlarına** tam uyum sağlarken, aynı anda **%92 oranında çevresel sürdürülebilirlik kriterlerine (karbon ayak izi kısıtına)** de kusursuz uyum göstermeyi başarmıştır.
- **Diyetisyen Nasıl Adapte Olmalı?**
    - Diyetisyenler artık sadece kalori cetvellerini değil, besinlerin ekolojik ayak izlerini ve sürdürülebilirlik parametrelerini de diyet planlama süreçlerine entegre etmelidir. Geleceğin diyetisyeni, hastasını iyileştirirken gezegeni de koruyan bir **"Sürdürülebilir Klinik Nütrisyon Lideri"** olacaktır

- **ABCD Yöntemi (NCP Değerlendirme Temeli):** Beslenme durumunu saptamak için kullanılan geleneksel yöntemdir. **A**ntropometrik (Boy, kilo, bel çevresi), **B**iyokimyasal (Kan tahlilleri), **K**linik (Fiziksel belirtiler, ödem) ve **D**iyet (Besin tüketim kayıtları) verilerinden oluşur.
- **MUST-Plus (Olasılıksal Risk Tahmin Sistemi):** Mount Sinai Sağlık Sistemi'nde geliştirilen ve hastanın Elektronik Sağlık Kayıtlarındaki (EHR) laboratuvar, antropometrik ve klinik verileri analiz ederek malnütrisyon (yetersiz beslenme) riskini otomatik hesaplayan olasılıksal bir makine öğrenimi modelidir.
- **FANS (Framework for automatic Assessment of Nutritional Status):** Peking Union Medical College Hospital tarafından geliştirilen, doktor ve hemşirelerin serbest metin olarak yazdığı klinik notları **Doğal Dil İşleme (NLP)** ile tarayarak hastadaki gizli malnütrisyon risk faktörlerini saptayan yapay zeka çerçevesidir.
- **IADA (Image-Assisted Dietary Assessment - Görüntü Destekli Diyet Değerlendirmesi):** goFOOD™ gibi sistemlerin kullandığı, yemek fotoğraflarından yapay sinir ağları ve 3D rekonstrüksiyon ile porsiyon hacmini ve besin değerlerini saptayan teknolojidir.
- **PES İfadesi (Problem, Etioloji, Belirti):** Beslenme tanısını standartlaştırmak için kullanılan katı klinik dildir. Örn: _"Yutma güçlüğüne bağlı (Etioloji) yetersiz oral enerji alımı (Problem); son 3 ayda %10 istemsiz kilo kaybıyla (Semptom) kanıtlanmıştır."_
- **RAG (Retrieval-Augmented Generation - Bilgi Kurtarma Destekli Üretim):** Yapay zekaya bir soru sorulduğunda, kafasından uydurmasını (halüsinasyon) engellemek için, soruyu sadece arkada bağlı olan güvenilir tıp kitaplarını ve klinik kılavuzları (Örn: TÜBER, ADA) aratarak yanıtlamasını sağlayan güvenlik mimarisidir.
- **SLM (Small Language Model - Küçük Dil Modeli):** Milyarlarca parametrelik devasa genel modeller (LLM) yerine, sadece belirli bir uzmanlık alanına (örneğin gıda bileşen kimyası ve alerjenler) yönelik eğitilmiş, daha küçük, kompakt ve hata yapma ihtimali sıfıra yakın olan yapay zekalardır.
- **XAI (Explainable AI - Açıklanabilir Yapay Zeka) ve SHAP Analizi:** Yapay zekanın bir hastaya neden "yüksek riskli" teşhisi koyduğunu, hangi laboratuvar bulgusuna ne kadar ağırlık verdiğini klinisyene grafiklerle (SHAP şemalarıyla) şeffaf bir şekilde kanıtlamasıdır.
- BÖLÜM 2: BESLENME BAKIM SÜRECİNDE (NCP) BÜYÜK DÖNÜŞÜM

```
+------------------------------------------------------------------------------------------+
|                        BESLENME BAKIM SÜRECİNİN (NCP) AI DÖNÜŞÜMÜ                        |
+--------------------------+----------------------------------+----------------------------+
| ADIM                     | ESKİDEN                          | ŞİMDİ (AI ÇAĞI)            |
+--------------------------+----------------------------------+----------------------------+
| 1. Değerlendirme (Ass.)  | Yatak başı statik anket (MUST)   | MUST-Plus & FANS NLP       |
|                          | Kağıt-kalem 3 günlük tüketim     | goFOOD™ 3D Tabak Analizi   |
+--------------------------+----------------------------------+----------------------------+
| 2. Tanı (Diagnosis)      | Öznel, manuel PES cümleleri      | İnsan denetimli (HITL)     |
|                          |                                  | XAI Teşhis Desteği         |
+--------------------------+----------------------------------+----------------------------+
| 3. Girişim (Intervent.)  | Değişim listesiyle manuel kalori | RAG tabanlı kişiselleşmiş  |
|                          | hesaplama (Saatler sürer)        | otomatik menüler (Saniyeler) |
+--------------------------+----------------------------------+----------------------------+
| 4. İzleme (Monitoring)   | Göz kararı tabak artığı takibi   | Tüketim öncesi/sonrası     |
|                          |                                  | visual yapay zeka analizi  |
+--------------------------+----------------------------------+----------------------------+
```

📋 1. Adım: Beslenme Değerlendirmesi (Nutrition Assessment)

- **Eskiden:** Hastaneye yatan hastaların malnütrisyon taraması, hemşireler tarafından yatış anında statik MUST formları doldurularak yapılırdı. Yoğun klinik temposu nedeniyle bu formlar genellikle üstünkörü doldurulur, hastaların %20-%50’sinde malnütrisyon gözden kaçardı. Evdeki hastaların besin tüketim takibi ise kağıt-kalem günlüğüne dayanır, "eksik beyan" (underreporting) nedeniyle güven vermezdi.
- **Şimdi:** Mount Sinai Hastanesi'nde aktif olarak kullanılan **MUST-Plus** modeli, hastanın laboratuvar tahlillerini (albümin, lenfosit, sodyum vb.) ve antropometrik verilerini arka planda tarayarak **%73 sensitivity (hassasiyet)** ile malnütrisyonu henüz yatak başına gidilmeden saptıyor. Peking Union Hospital'ın **FANS** sistemi ise, doktorların serbest metin olarak yazdığı klinik notları NLP ile tarayarak istemsiz kilo kaybı ve disfaji (yutma güçlüğü) gibi risk faktörlerini **0.9142 F1-skoru** ile otomatik olarak ayıklıyor. Evde ise hastalar tabağın fotoğrafını çekerek **goFOOD™** sistemiyle porsiyon hacmini saniyeler içinde hesaplatabiliyor.
- **Gelecekte:** Giyilebilir pasif kameralar (EgoDiet/eButton) ve çene hareketini takip eden akustik sensörler, hastanın yeme hızını ve yutkunmasını zahmetsizce kaydedecektir. Bu veriler, sürekli glikoz monitörleri (CGM) ile birleşerek hastanın canlı bir **"Dijital İkiz" (Digital Twin)** metabolik modelini oluşturacaktır.

🔬 2. Adım: Beslenme Tanısı (Nutrition Diagnosis)

- **Eskiden:** Diyetisyenler hastanın tablosunu inceleyip subjektif olarak PES (Problem-Etioloji-Belirti) cümleleri kurarlardı. Bu durum diyetisyenler arasında standart dışı tanı farklılıklarına yol açardı.
- **Şimdi:** Klinik araştırmalar (Örn: Naja ve ark., 2024), genel amaçlı yapay zekaların (ChatGPT-4) diyet yazmada başarılı olsalar da **Beslenme Tanısı ve standart PES ifadeleri üretme adımında tamamen yetersiz kaldığını ve bu cümleleri oluşturmayı unuttuğunu** ortaya koymuştur. Bu durum, yapay zekanın tıbbi bir "muhakeme" gücü olmadığını gösteren en net kanıttır.
- **Gelecekte:** **Açıklanabilir Yapay Zeka (XAI)** modelleri, SHAP analizleri kullanarak, diyetisyene tahlil sonuçları ile beslenme tanısı arasındaki moleküler korelasyonları şeffaf bir şekilde sunarak klinisyenin karar alma sürecini destekleyecektir.

🍳 3. Adım: Beslenme Girişimi (Nutrition Intervention)

- **Eskiden:** Diyetisyenler Harris-Benedict formülüyle bazal metabolizma hızı hesaplar, besin değişim tablolarıyla saatlerce uğraşarak hastaya özel menüler hazırlarlardı.
- **Şimdi:** İstanbul Gelişim ve Bandırma Onyedi Eylül Üniversitelerinden Bayram ve Arslan (2025) tarafından yapılan çığır açıcı çalışmada; **ChatGPT-4.1, Grok-3 ve DeepSeek** modellerinin Tip 2 Diyabet hastaları için hazırladığı menüler karşılaştırılmıştır. Grok-3 kalori doğruluğunda %83.1 ile en başarılısı olurken, DeepSeek hastanın kilosuna göre protein miktarını dinamik ayarlayan tek model olmuştur. Ancak ChatGPT-4.1'in hazırladığı listelerdeki **doymuş yağ oranının, güvenli klinik sınırın %172'sine (neredeyse iki katına) çıkarak** hastanın kardiyovasküler sağlığını tehlikeye attığı saptanmıştır. Modellerin tek başına diyet yazması hala büyük klinik riskler barındırmaktadır.
- **Gelecekte:** Yapay zeka destekli hassas enteral/parenteral nütrisyon (TPN) sistemleri, yoğun bakımdaki hastanın anlık kan tahlillerine göre tamamen kişiselleştirilmiş beslenme solüsyonu reçetelerini milisaniyeler içinde hazırlayıp eczane robotlarına gönderecektir.

📈 4. Adım: Beslenme İzleme ve Değerlendirmesi (Nutrition Monitoring & Evaluation)

- **Eskiden:** Hastanelerde hastanın ne kadar yediği (tabak artığı / plate waste), hemşirelerin göz kararı "Yemeğin yarısını yedi" şeklindeki öznel notlarıyla veya tabakları tek tek hassas terazide tartarak (weighed food record) hantalca takip edilirdi.
- **Şimdi:** Klinik izleme sistemleri, servis edilen tabak ile tüketim sonrası tabağın fotoğraflarını yapay zekayla karşılaştırır. Derin öğrenme algoritmaları, iki görüntü arasındaki farktan hastanın gerçekte kaç kalori ve ne kadar protein aldığını %15'in altında bir hata payıyla saptayarak diyetisyenin paneline otomatik raporlar düşürür.
- **Gelecekte:** Evde parenteral beslenme alan hastaların kateter enfeksiyon riski ve hidrasyon durumları giyilebilir biyosensörlerle 7/24 izlenecek; yapay zeka anormal bir metabolik dalgalanma saptadığında diyetisyeni anlık olarak uyaracaktır.
Hikaye 1: "20 Gramlık Rus Ruleti" (Tabağın Arkasındaki Ölümcül Risk)

*"Sevgili arkadaşlar, aranızda Tip 1 diyabetli bir yakını olan var mı? Her lokmayı tartmak, karbonhidrat saymak zorunda olan bir hasta hayal edin. 2026 yılında, Fransa'da klinik diyetisyenler bir deney yapıyor. Hastaların karbonhidrat sayımı için kullandığı yapay zekaları (Gemini, Claude ve ChatGPT) 30 farklı gerçek akşam yemeği tabağıyla test ediyorlar.

Sonuç ne çıkıyor biliyor musunuz? Google'ın en gelişmiş yapay zekası Gemini, tabaklardaki karbonhidrat miktarını **%38 oranında, en az 20 gramdan fazla** tahmin ediyor! Klinik beslenmede 20 gramlık bir hata sadece bir sayı değildir. Yapay zekaya güvenen bir hasta, tabakta fazladan karbonhidrat olduğunu sanıp kendine **aşırı dozda insülin enjekte ediyor** ve yolda yürürken aniden **ölümcül hipoglisemi komasına** girme riskiyle yüzleşiyor! Yapay zeka kelimeleri harika diziyor olabilir ama o aslında tabağın arkasındaki insan hayatından habersiz, gözü kör bir olasılık motorudur."*

Hikaye 4: "Sanal Hasta Carol ve Empati Yoksunu Robot" (ATLAS Deneyimi)

*"Yapay zekanın sadece kalori hesaplayan soğuk bir program olduğunu mu düşünüyorsunuz? Monash Üniversitesi'ndeki akademisyenler, yeni başlayan diyetetik öğrencileri için **ATLAS** adını verdikleri yapay zeka tabanlı sanal bir klinik tasarladılar. Bu klinikte yapay zekaya **'Carol'** adında, diyaliz tedavisi gören sanal bir hasta kimliği (persona) yüklediler. Carol'ın bir kişiliği var: Kaygılı, savunmacı ve doktorlardan bıkmış durumda.

Öğrenciler Carol ile sesli olarak konuşarak onun beslenme öyküsünü almaya çalışıyorlar. Carol, alkol tüketimi gibi bazı hassas bilgileri **gizli tutacak** şekilde programlandı. Eğer öğrenci, Carol'a bir robot gibi yaklaşıp empati kurmadan, doğrudan 'Haftada kaç kadeh alkol alıyorsunuz?' diye sorarsa, yapay zeka Carol anında **savunmaya geçiyor, iletişimi kesiyor ve kısa, soğuk yanıtlar vererek 'kilitleniyor'**. Öğrencinin bu gizli bilgileri alabilmesi için önce yapay zekaya 'Geçmiş olsun Carol hanım, diyaliz sürecinizin zor olduğunu tahmin edebiliyorum' gibi empatik ve açık uçlu cümleler kurması gerekiyor.
BÖLÜM 4: DİYETİSYENİN YENİ ROLÜ VE ADAPTASYON REHBERİ

Yapay zeka çağında işsiz kalmamak ve kendinizi geleceğe hazırlamak için şu 3 kritik alanda uzmanlaşmalısınız:

1. "Süper Kütüphaneci" (LLM) ile "Cerrahi Terazi"yi (SLM) Evlendirmek

ChatGPT gibi Büyük Dil Modelleri (LLM) her şeyi bilir ama hiçbirinde uzman değildir. Geleceğin diyetisyeni, bu genel modelleri, sadece gıda kimyası ve klinik beslenme üzerine eğitilmiş Küçük Dil Modelleri (SLM) ve güvenilir bilgi bankalarıyla (RAG) entegre etmeyi öğrenmelidir. Siz sistemin anayasasını yazan **"Kural Koyucu"** olacaksınız.

2. "Tıp Kibrini" Hastanın Mutfağına Tercüme Etmek

Hacettepe Üniversitesi'ndeki hocalarımız (Elif Ulug ve ark., 2025) tarafından yapılan araştırmada, ChatGPT'nin Polikistik Over Sendromu (PCOS) hastalarına verdiği beslenme önerilerinin kalitesi çok yüksek çıkmıştır. Ancak okunabilirlik analizleri yapıldığında; ChatGPT'nin Türkçe yanıtlarının **"Akademik/Üniversite Mezunu Seviyesinde" ve okunması "Zor"** olduğu saptanmıştır.

- **Diyetisyenin Rolü:** Yapay zeka, hastaya bir profesör kibriyle, ağır biyokimyasal terimlerle konuşur. Diyetisyenin yeni rolü; yapay zekanın bu kuru, akademik ve anlaşılmaz tıbbi dilini, hastanın evindeki buzdolabının diline, sıcak ve uygulanabilir bir yaşam tarzına tercüme etmektir.

3. "Örtük Bilgi" (Tacit Knowledge) ve Klinik Sezgi Liderliği

Yunanistan'da yapılan bir çalışmada (Fappa ve ark., 2025), internetteki 177 zayıflama web sitesinin kalitesi hem diyetisyenlere hem de ChatGPT-4.5'e inceletilmiştir. ChatGPT, sitelerdeki "Bol bol su için, sebze yiyin" gibi aşırı genel ve hiçbir kişiselleştirme içermeyen yüzeysel tavsiyeleri görünce kandırılmış ve sitelerin %22'sine "Mükemmel" notu vermiştir. Gerçek diyetisyenler ise sitelerin sadece %3'üne bu notu vermiştir.

- **Diyetisyenin Rolü:** Yapay zekada klinik tecrübeden gelen **"Örtük Bilgi" (Tacit Knowledge)** ve şüphecilik yoktur. Diyetisyen, satır aralarındaki ticari tuzakları, eksik mikro besinleri saniyeler içinde sezer. Bu sezgisel klinik liderlik, asla bir algoritmayla taklit edilemez.

1. ADIM: Beslenme Değerlendirmesi (Nutrition Assessment) – Tanılamanın Otomasyonu

Beslenme değerlendirmesi (ABCD yöntemi: Antropometrik, Biyokimyasal, Klinik, Diyet verileri), NCP sürecinin ilk ve en kritik adımıdır.

- **Eskiden (Klasik Dönem):**
    - Hastaneye yatan hastaların malnütrisyon (yetersiz beslenme) taramaları, hemşireler veya diyetisyenler tarafından yatak başında, kısıtlı ve statik sorulara dayanan klasik MUST veya NRS-2002 formları ile sadece "yatış anında bir kez" doldurulurdu. Bu süreç hem çok zaman alırdı hem de hastaların %20-%50’sinde malnütrisyonun gözden kaçmasına neden olurdu.
    - Danışanların evdeki besin tüketim kayıtları ise kağıt kalemle yazılan 3 günlük besin günlüğü veya 24 saatlik hatırlatma (24HR) yöntemlerine dayanırdı ve ciddi bir "yanlış/eksik hatırlama" (underreporting) sapması barındırırdı.
- **Şimdi (Yapay Zeka Destekli Dönem):**
    - **Probabilistik (Olasılıksal) Tarama Modelleri (MUST-Plus):** Mount Sinai Sağlık Sistemi'nde geliştirilen ve uygulanan **MUST-Plus** makine öğrenimi modeli, hastanın yatışından önceki son 5 günlük Elektronik Sağlık Kayıtlarını (EHR) (laboratuvar tahlilleri, antropometrik veriler, vital bulgular, demografik bilgiler) Random Forest algoritmasıyla saniyeler içinde tarar. MUST-Plus, klasik hemşire MUST taramasına göre **%30 daha yüksek hassasiyet (sensitivity)** göstermiş ve malnütrisyonlu hastaları yatak başında saptama başarısını rekor düzeyde artırmıştır.
    - **Klinik Not NLP Taramaları (FANS):** Peking Union Medical College Hospital’da bizzat klinik notlardan malnütrisyon risk faktörlerini (istemsiz kilo kaybı, iştahsızlık vb.) otomatik olarak yakalamak amacıyla geliştirilen **FANS (Framework for automatic Assessment of Nutritional Status)** sistemi, serbest metin olarak yazılmış doktor ve hemşire notlarını Doğal Dil İşleme (NLP) ile tarayarak **0.9142 F1-skoru** ile risk faktörlerini saptamakta ve diyetisyenin önüne getirmektedir.
    - **Fotoğraf Tabanlı Analiz (IADA):** goFOODTM ve eTRIP gibi akıllı telefon tabanlı IADA sistemleri, tabağın iki farklı açıdan fotoğrafını çekerek veya video kaydı alarak 3D rekonstrüksiyon yapar ve gıdanın porsiyon hacmini ölçerek USDA gıda veritabanından kaloriyi otomatik hesaplar.
- **Gelecekte (Dijital İkiz Dönemi):**
    - Hastaların giydiği göğse takılı pasif kameralar (eButton, EgoDiet) ve kulak arkası/çene sensörleri yeme eylemini, çiğneme/yutkunma hızını akustik sinyallerle takip edecektir. Sürekli Glikoz Monitörleri (CGM), nefes analizörleri ve akıllı teraziler entegre bir bulut sisteminde birleşerek hastanın sürekli güncellenen dinamik bir **"Dijital İkiz" (Digital Twin)** modelini oluşturacak ve diyetisyenin paneline anlık metabolik analizleri raporlayacaktır.

🎬 Hikaye: Yatak Başındaki Görünmez Düşman (Mount Sinai Deneyimi)

*"Mount Sinai Hastanesi’nde çalışan klinik diyetisyenler, her sabah hangi hastanın başına gideceklerini seçerken ciddi bir zaman baskısı yaşıyorlardı. Hemşireler tarafından yatışta doldurulan klasik MUST skorları genellikle '0' (risk yok) olarak giriliyordu çünkü yoğun klinik ortamda yatak başı manuel ölçümler çok hantaldı. Ancak hastaların malnütrisyonu hastanede yattıkları sürece ilerlemeye devam ediyordu.

Bilgi işlem birimi **MUST-Plus** yapay zekasını devreye aldığında her şey değişti. Sistem, hastaların geçmiş laboratuvar tahlillerini (albümin, lenfosit, sodyum vb.) ve doktorların klinik notlarını arka planda sürekli tarayarak her hastaya 0 ile 1 arasında değişen dinamik bir 'malnütrisyon risk skoru' atadı. Diyetisyenler sabah bilgisayarlarını açtıklarında, panellerinde kırmızı renkle yanan 'En Yüksek Öncelikli Hastalar' listesini gördüler. Yapay zeka sayesinde hastanın kabulünden kesin teşhisine kadar geçen **'gecikme süresi' (lag time) dramatik şekilde düştü** ve diyetisyenlerin klinik performans memnuniyeti %90’ı aştı! Yapay zeka, hastanedeki görünmez açlığı yakalayan bir göz haline gelmişti."*

---

🔬 2. ADIM: Beslenme Tanısı (Nutrition Diagnosis) – "Kara Kutunun" Standardizasyon Sınavı

Beslenme değerlendirmesinden sonra diyetisyen, problemi, nedenini ve belirtilerini içeren standart **PES (Problem, Etioloji, Belirti/Semptom) ifadelerini** formüle eder.

- **Eskiden (Klasik Dönem):**
    - Diyetisyenler, hastanın klinik tablosunu önlerine alıp saatlerce düşünerek "Gıda-sağlık bilgisi eksikliğine bağlı aşırı enerji alımı; yüksek HbA1c ve beslenme günlüğü kayıtlarıyla kanıtlanmıştır" gibi standart PES ifadelerini manuel ve öznel olarak yazarlardı. Bu süreç, kurumlar ve diyetisyenler arasında büyük farklılıklar (subjektif sapmalar) yaratırdı.
- **Şimdi (Yapay Zeka Destekli Dönem):**
    - Yapay zekanın en büyük kısıtlamalarından biri bu adımda ortaya çıkmaktadır. Yapılan klinik araştırmalarda (örneğin Naja ve ark. 2024), ChatGPT ve benzeri dil modellerine Tip 2 Diyabet veya Metabolik Sendrom hastalarının vakaları sunulmuştur. Yapay zekanın beslenme girişimlerinde (diyet yazmada) başarılı olmasına rağmen, **Beslenme Tanısı (NCP Diagnosis) adımında tamamen sınıfta kaldığı** saptanmıştır.
    - Chatbotlar çoğunlukla **standart PES ifadelerini üretmeyi tamamen unutmuş, yanlış teşhis terimleri kullanmış** veya klinik etiolojiyi (nedeni) yanlış analiz etmişlerdir. Bu durum, yapay zekanın klinik bir muhakeme (reasoning) yeteneği olmadığını, sadece kelimeleri yan yana dizdiğini kanıtlayan en büyük klinik kanıttır.
- **Gelecekte (XAI ve Ontoloji Entegrasyonu Dönemi):**
    - Sadece konuşkan LLM’ler değil, arkada tıbbi tıp kütüphanelerine (RAG) ve tıbbi endüstri verilerine bağlı **Açıklanabilir Yapay Zeka (XAI)** modelleri kullanılacaktır. Bu sistemler, hastanın biyokimyasal grafiğindeki anormalliğin neden bu beslenme tanısına yol açtığını diyetisyene matematiksel bir karar ağacıyla (SHAP analizleriyle) kanıtlayarak gösterecek ve diyetisyenin hata yapma riskini sıfıra indirecektir.

🎬 Hikaye: Mayo Klinik'te Robotların "Teşhis" Sınavı

*"2025 yılında Mayo Klinik’teki Beslenme Destek Servisi'nde çalışan uzman hekimler ve diyetisyenler, yoğun bakımdaki refeeding sendromu (yeniden besleme sendromu) ve kısa bağırsak sendromu gibi son derece karmaşık 5 gerçek klinik vakayı topladılar. Bu vakaları kör bir şekilde dört yapay zekaya (ChatGPT, OpenEvidence, Gemini ve Copilot) sordular.

Sonuçta Gemini en yüksek netlik ve klinik doğruluk puanını aldı. Ancak uzmanların raporundaki can alıcı cümle şuydu: **'Yapay zeka modelleri, bizim klinik olarak zaten bildiğimiz şeyleri çok güzel özetledi ve taklit etti. Ancak hiçbir vaka için yeni, çığır açıcı bir tanısal içgörü sunamadı veya gözümüzden kaçan bir klinik riski bize bildiremedi'**. Yani, karmaşık klinik vakalarda yapay zeka sadece diyetisyenin arkasından gelen ve onun adımlarını onaylayan bir 'taklitçidir'; asla klinik liderliği eline alamaz."*

---

🍳 3. ADIM: Beslenme Girişimi (Nutrition Intervention) – "Otopilottan" RAG-Sistemli "Yardımcı Pilota"

Tanı konulduktan sonra diyetisyen, hastanın ihtiyaçlarına uygun beslenme tedavisini, kaloriyi ve makro/mikro dağılımını planlar.

- **Eskiden (Klasik Dönem):**
    - Diyetisyenler, hastanın yaşına, cinsiyetine ve fiziksel aktivitesine göre kağıt üzerinde Harris-Benedict formülüyle kalori hesabı yapar, ardından besin değişim listelerini (karbonhidrat, protein, yağ) tek tek hesaplayarak menü oluştururlardı. Bu işlem saatler sürerdi. Hastanede TPN (Damardan beslenme) torbası hazırlarken, hastanın kan tahlillerine göre mevcut multichamber (çok odacıklı) hazır torbaların içeriklerini manuel olarak karşılaştırmak büyük bir zaman ve dikkat yükü yaratırdı.
- **Şimdi (Yapay Zeka Destekli Dönem):**
    - **Matematiksel Menü Planlayıcılar:** Simplex algoritmaları ve Durum Tabanlı Muhakeme (C CBR) sistemleri, diyetisyenin girdiği sınırlamalara (Örn: "Kalori <1500 kcal olsun, protein >80 g olsun") göre milisaniyeler içinde hatasız menüler tasarlamaktadır.
    - **RAG Tabanlı "Sanal Diyetisyenler":** Obezite ve Tip 2 Diyabet hastaları için geliştirilen gelişmiş RAG (Retrieval-Augmented Generation) sistemleri (Twente Üniversitesi'ndeki smoothie projesi gibi), LLaMA3 veya GPT-4 modelini Amerikan Diyabet Derneği (ADA) ve ulusal diyet kılavuzlarıyla eşleştirerek, hastanın sağlık profiline ve yerel/mevsimsel gıdalara göre %80.1 oranında klinik kılavuzlara uyumlu özel tarifler üretmektedir.
    - **Önemli Hata Uyarısı:** Ancak standart, harici bilgi bankası olmayan (non-RAG) genel yapay zekalar diyet girişimlerinde büyük hatalar yapabilir. ChatGPT-4o ile yapılan bir çalışmada, diyabet hastası için yazılan menülerin karbonhidrat dengesi tutsa da, **doymuş yağ miktarlarının güvenli klinik sınırın tam %172’sine (neredeyse iki katına) çıktığı** saptanmıştır. Yani yapay zeka diyabeti çözerken, hastanın damarlarını tıkayacak bir girişim yapabilir!
- **Gelecekte (Hassas Tıp ve Yapay Zeka Destekli Reçeteleme):**
    - Klinik diyetisyenler, TPN ve enteral beslenme formüllerini yazarken yapay zeka asistanlarını kullanacaktır. Yenidoğan yoğun bakım ünitelerinde bizzat denenen sistemlerdeki gibi, yapay zeka hastanın o günkü EHR ve kan sonuçlarına bakarak tamamen kişiye özel, en güvenli ve en ucuz TPN torbası formülasyonunu saniyeler içinde eczaneye sipariş edecektir.

🎬 Hikaye: Yapay Zekalı Şeflerin Çocuk Bahçesindeki "Yemek Savaşı"

*"Çocuk bakım merkezlerinde yüzlerce çocuk için besleyici, ucuz ve çocukların seveceği menüler planlamak tam bir kabustur. 2022 yılında araştırmacılar, çocuk menüsü planlaması için iki yapay zekayı (bir takviyeli öğrenme - RL modeli ve bir üretken GAN modeli) yarıştırıyorlar. Yapay zekalara tüm beslenme kılavuzları yükleniyor ve çocukların seveceği menüler yazmaları isteniyor.

Menüler hazırlandığında, diyetisyen jüri üyelerine menüleri 'çift kör' olarak değerlendiriyorlar. İlk aşamada, jüriye yemek isimleri gizlenip sadece 'besin değerleri ve kalori dengesi' veriliyor. Sonuçta, Takviyeli Öğrenme (RL) yapay zekasının hazırladığı menüler, insan diyetisyenlerin ve GAN'ın menülerini açık ara geride bırakarak tam puan alıyor!

Ancak ikinci aşamada jüriye yemeklerin isimleri ve kompozisyonları (Örn: 'Ispanaklı ve portakallı brokoli püresi yanına süt') gösterildiğinde jüri yüzünü ekşitiyor. Yapay zeka besin değerini tutturmak için öyle absürt yemek kombinasyonları ve pratik olmayan pişirme yöntemleri sunmuştur ki, bir çocuğun o yemeği yemesi imkansızdır! Sonuçta insan diyetisyenler, pratiklik ve yemek uyumu (culinary pragmatism) konusunda robotları ezici bir şekilde geçiyor. Yapay zeka bir matematik dehasıdır ama tabağın lezzet uyumunu ve çocuk ruhunu anlayamaz."*

---

📈 4. ADIM: Beslenme İzleme ve Değerlendirmesi (Nutrition Monitoring & Evaluation) – Pasif Gözün Gücü

Girişim uygulandıktan sonra diyetisyen, hastanın hedeflere ulaşıp ulaşmadığını takip eder ve diyeti revize eder.

- **Eskiden (Klasik Dönem):**
    - Hastanelerde hastanın ne kadar yediğini takip etmek (plate waste / tabak artığı takibi) için hemşirelerin göz kararı doldurduğu hantal formlar kullanılırdı veya en doğru yöntem olan yemek öncesi ve sonrası tabakları tek tek hassas terazide tartma (weighed food record) yöntemi uygulanırdı. Tartım işlemi o kadar zor ve zaman alıcıydı ki klinik pratiklerde neredeyse hiç uygulanamazdı.
- **Şimdi (Yapay Zeka Destekli Dönem):**
    - **Dijital Tabak Artığı Takibi:** Hastanelerde yatan yaşlı hastalar üzerinde yapılan çalışmalarda, hastanın tabağının yemek servis edilmeden önce (servis anı) ve hasta yedikten sonra (artık anı) çekilen fotoğrafları yapay zekaya yüklenmektedir. Derin öğrenme algoritmaları, iki fotoğraf arasındaki hacimsel farkı otomatik analiz ederek hastanın gerçekte kaç kalori ve ne kadar protein tükettiğini %15'in altında bir hata payıyla (teraziyle tartım yöntemine son derece yakın bir doğrulukla) hesaplayarak diyetisyenin ekranına düşürür. Hemşirelerin saatler süren iş yükü sıfırlanmış olur.
- **Gelecekte (Uzaktan Hasta İzleme ve Akıllı Bildirimler):**
    - Evdeki hastalar için YZ tabanlı sistemler PROMs (Hasta Tarafından Bildirilen Çıktılar) ve PREMs (Hasta Deneyimi Ölçümleri) verilerini uzaktan izleyecektir. Örneğin, evde parenteral beslenme (HPN) alan bir hastanın kateter enfeksiyonu riski, vücut ısısı ve hidrasyon durumu akıllı giyilebilir sensörlerle takip edilecek; yapay zeka anormal bir biyokimyasal dalgalanma saptadığında diyetisyene anlık olarak 'Bu hastanın diyet planını revize etmelisin' uyarısı gönderecektir



# 3.Hafta
4.Hafta
5.Hafta
6.Hafta
7.Hafta
8.Hafta
9.Hafta
10.Hafta
11.Hafta
12.Hafta
13.Hafta
14Hafta

sen zamana haftaya takılma. ilk hafta anlattıklarımızı tekrar anlatmamıza gerek yok. ben akış şöyle olsun istiyorum:

AI'nin sağlık alanına girişi, tıp nasıl dönüşüyor AI ile (kişiselleitirlmiş tıp, 4P.. bunların getirdikleri, etkisi, nasıl çalışacağız ilerde falan)

sonra bu yaklaşımlar beslenmeye nasıl sıçradı (diyetisyenin her pratiği etkilendi. ne şekilde etkilendiğini açıklayan çalışmalar, NCP sürecindeki değişimler, geçmişte nasıldı şimdi nasıl, gelecekte nasıl olabilir vizyon projeksiyonları falan... burada diyetisyenlikle ilgili her şeyden bahsetmek gerekiyor ki öğrenciler her bakış açısından anlasınlar nasıl bir dönüşümün içinde olduğumuzu. çünkü öğrenciler çok farkında değil olanın bitenin.)

sonra diyetisyenin yeni rolü, bu dönüşüme nasıl adapte olabiliriz, neler yapmalıyız, kendimizi nasıl dönüştürmeliyiz tarzında son bölüm.

sen bu not hariinde kendi literatür taramanı ve eklemelerini de yapabilirsin.



**Münazara konusu**: AI diyetisyenin yerini alacak mı? 

**Öğrenci sunumları:** 
besin kompozisyonu tanıyan ai uygulamaları
klinik nutrisyonda ai uygulamaları
danışmanlık-hasta takibinde AI kullanımı ipuçları
AI çağında digital health-twin kişiselleştirilmiş beslenme
AI'yı etkili kullanma rehberi... vb tematik konular ver. 

**NotebookLM Dijital Defteri Oluşturma**: herkese bir ödev konusu ver, öğrenciler birbirlerinin defterlerinin yaratıcılığını puanlasın. ilginç şeyler çıkacak mı bakalım.

**Mutfakta yapılan bir yemeğin AI ile kompozisyon tahmini yarışması**: nasıl tahmin düzeyini artırabiliriz AI'in?

**İhtiyaca Yönelik Custom GPT-Gem Oluşturma**

**Herkes githubla websitesi kurabilir**


**Heygen ve Elevenlabs ile Otomatize İçerikler Oluşturma**
Podcast yaparlar, otomatize youtube kanalı açarlar..
**Otomasyon: AI Otomasyonu ile Beslenme Bülteni Geliştirme**
**MVP:** Make.com + PubMed RSS + Google Gemini
> - UPF, IF, Obezite sorguları + Meta-analiz/RCT filtresi
> - Türkçe özet + PICO analizi + sosyal medya kancası
> - Google Sheets'te onay bekleyen taslak
>
> **Genişletilmiş Kapsam:** TDD, Onkolojik Diyetisyenler, Tarım Bakanlığı tağşiş listesi
>
> **Vizyon:** "Nutri-Doğrulama Bülteni" (Substack) → Diyetisyenler için SaaS platform

**Vibe Coding Süreci:**
R Tabanlı Diyet Analizi Yazılımı Geliştirmek
**Amaç:** USDA veritabanından beslenen, vaka analizini otomatize eden interaktif R Shiny uygulaması
>
> **Teknik Altyapı:**
> - Platform: R + R Shiny
> - Veri: USDA FoodData Central API
>
> **Çalışma Akışı:**
> 1. Türkçe besin girişi → İngilizce mapping → USDA sorgusu
> 2. RDA/DRI karşılaştırması
> 3. Kısıtlama kontrolü (düşük sodyum, oksalat vb.)
> 4. Çıktı: "Demir alımı %60, şunları eklemeyi düşün: mercimek, kırmızı et..."

Danışan ilk Görüşme Robotu
Duygusal yeme, aşermeler, UPF tüketimi, antropometrik ölçümler
> **Slogan:** "ChatGPT sana ne yemen gerektiğini söyler, biz ise neden yediğini söyleriz"
>
> Öne çıkan modüller:
> - Dedektif Modu (trigger bulma)
> - Sanal Buzdolabı Testi (duygusal durum analizi)
> - UPF Dedektörü (görsel analiz)
> - Risk Skoru → PDF Gap Analiz Raporu

Sistem Biyolojisine Uygun Uygulama-Diyagram Geliştirme
Kendi Bilgi Yarışmalarını-Etkinliklerini Geliştirme
Mesela bir besinin aa ve protein kalitesini biyorarlanımı da göz önünde bulundurarak hesaplayan bir uygulama güzel olur.
Farklı hesaplara göre enerji alımı-kilo kaybı tahmini yapan uygulama, kilo kaybı tahmini simülasyonları??
Diyetleri sadece besinlerdeki miktara değil, biyorararlanım baz alındığında ortaya çıkaran gerçek tabloyu görselleştiren uygulama. cool olur. şuradaki biyorararlanım oranlarına bir bak: https://doi.org/10.1016/j.ajcnut.2026.101253

Etkinlikler:
Dönem sonunda geliştirilen fikirleri sergileme işi yapılabilir ürünler iyi olursa.
Sergi de olmalı içerisinde: Derste geçen önemli kavramlar bir esere/ürüne dönüştürülür
> Resimlerin, müziklerin, romanların, dizilerin yeniden uyarlanması
> Her ürünün etiketi: "Neden bunu yaptım? Ne anlatıyor? Hangi araçları kullandım?"
> **Herkese açık Notion page veya online sergi**

Fikirler:
Bunların hepsini yapabilirsek öğrencilere dönem sonu bir temsili sertifika hazırlanabilir..
kendi besin kompozisyonu robotumu yaparım. TURKOMP verilerini atarım. yemek tariflerini buradan seçerim bana fenotipi verir. akdeniz diyetine uyum, ketojenik, protein....




