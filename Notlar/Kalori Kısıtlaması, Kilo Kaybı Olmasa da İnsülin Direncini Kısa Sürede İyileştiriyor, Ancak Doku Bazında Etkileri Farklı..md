---
Tür:
  - Besleyici
ODAK:
  - "[[Kalori Kısıtlaması]]"
MEKANİZMA:
DİZİN:
  - "[[Adipoz Doku]]"
  - "[[İnsülin Direnci]]"
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ: "[[Farklı aralıklı açlık türleri yağ dağılımını ve fonksiyonelliğini farklı etkiliyor olabilir mi?]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: https://www.science.org/doi/10.1126/sciadv.aed0535
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Düşük Kalorili Diyetlerde Hepatik ve Periferik İnsülin Direnci]]"
  - "[[Sistemik Enerji Metabolizması — Hepatik Substrat Seçimi, Ketogenez ve Tiroid-Metabolik Hız Ekseni]]"
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
### **Çalışmanın Amacı ve Hipotezi** 
Bu çalışmanın temel amacı, obeziteyle ilişkili insülin direncinin (IR) belirgin bir kilo kaybı yaşanmadan ne kadar hızlı bir şekilde tersine çevrilebileceğini araştırmak ve bu süreçte insülinin hedef aldığı dokularda (karaciğer, kas ve yağ dokusu) meydana gelen entegre fizyolojik/metabolik değişimleri haritalandırmaktır.

Araştırmacıların hipotezi, kalori kısıtlamasının (CR) insülin direncini kilo kaybından çok daha önce düzeltebileceği, ancak dokuların basitçe eski sağlıklı (standart diyet) hallerine dönmek yerine yepyeni bir metabolik adaptasyonla (katabolik yeniden modelleme ile) bu sorunu çözeceğidir.

## **Çalışma Nasıl Yapıldı?**

- **Hayvan Modeli ve Diyet:** Çalışmada C57BL/6 tipi fareler kullanıldı. Fareler önce 8 hafta (veya hastalığın ileri evresini simüle etmek için 18 hafta) boyunca yüksek yağlı diyetle (HFD) beslenerek obez ve insülin dirençli hale getirildi.
- **Müdahale:** Daha sonra fareler "Diyet Değişimi (DS)" protokolüne alınarak standart diyete (CD) geçirildi veya yüksek yağlı diyet almaya devam etseler de yiyecekleri %70 oranında kısıtlandı (CR). Bu kısıtlama süresi sadece **1 ila 3 gün** gibi çok kısa bir süreydi.
- **Ölçümler:** Bu kısa kısıtlama sonrasında farelerde insülin tolerans testleri (ITT) ve HOMA-IR ölçümleri yapıldı; ayrıca glikozun kas ve yağ dokularına girişini izlemek için radyoaktif izotop işaretli glikoz (2-DOG) kullanıldı. Ek olarak, dokuların moleküler haritasını çıkarmak için lipidomik ve proteomik (protein ve yağ profili) analizler uygulandı.

## **Primer (Birincil) Bulgular**

- **Kilo Kaybı Olmadan İnsülin Direncinin Kırılması:** Sadece 1 ila 3 günlük kalori kısıtlaması, farelerde henüz anlamlı bir vücut ağırlığı veya yağ kütlesi kaybı yaşanmamasına rağmen (fareler hala obezken), insülin direncini tamamen geri çevirmiş ve HOMA-IR/QUICKI değerlerini sağlıklı fareler seviyesine getirmiştir.
- **Basit Bir "Geri Dönüş" Değil, Metabolik Yeniden Modelleme:** En çarpıcı primer bulgu, vücut insülin duyarlılığını geri kazansa da, bireysel organların hastalık öncesindeki orijinal durumlarına geri _dönmemesidir_. Vücut bunun yerine yağları yakmaya odaklanan, karaciğer ve kasta katabolik süreçlerin (yıkım yollarının) aktive olduğu tamamen yeni ve farklı bir metabolik duruma geçiş yapmıştır.

## **Sekonder (Dokulara Özgü) Bulgular** Çalışma, insülin direncinin kırılmasının her dokuda farklı bir mekanizmayla gerçekleştiğini göstermiştir:

- **Karaciğerde Yağ Yakımına Geçiş:** Karaciğerdeki insülin duyarlılığının düzelmesi; toksik yağların (TAG ve DAG) ve hücresel stresi artıran PKCε enzim aktivitesinin azalmasıyla paralellik göstermiştir. Ayrıca karaciğer baştan yağ üretimini (De Novo Lipogenesis - DNL) çok ciddi şekilde düşürmüş ve bunun yerine keton cisimciklerini (BHB/AcAc) artırarak karaciğerin enerji için yağ oksidasyonuna odaklandığı görülmüştür.
- **İskelet Kasında Glikoz Alımının Düzelmesi:** Kasta, insüline bağlı glikoz alımı tamamen normale dönmüş, hücre içi yağ birikimi azalmış ve yağ asidi oksidasyon yolları artmıştır.
- **Yağ Dokusunda (Adipoz Doku) Hasarın Kalıcı Olması:** İlginç bir şekilde, kısıtlama sonrası yağ dokusu eski haline dönmemiştir. Açlık durumunda yağ yıkımı (lipoliz) faaliyeti baskılanmış halde kalmıştır. Bu durum, yağ dokusundaki temel uyarıcılardan olan $\beta$-adrenerjik reseptör 3'ün (ADRB3) seviyesinin kalıcı olarak düşmesiyle açıklanmıştır. Ayrıca kasta glikoz alımı düzelirken, yağ dokusunda insülinle uyarılan glikoz alımı düşük kalmaya devam etmiştir.
- **Sistemik Çözüm:** Yağ dokusunun kana yağ asidi pompalamayı (lipolizi) durdurması ve karaciğer ile kasın yağı hızla yakmaya başlaması sayesinde kandaki serbest yağ asidi (NEFA) seviyeleri düşmüş; bu da kas ve karaciğerin üzerindeki "yağ zehirlenmesi" yükünü kaldırarak insülinin tekrar çalışmasını sağlamıştır.

**Maruziyet Süresine Dair Ek Bulgu **

Önceki konuşmamızda bahsettiğimiz "hastalığa maruz kalma süresinin müdahaleye yanıtı değiştirmesi" hipotezini mükemmel bir şekilde doğrulayan bir sekonder bulgu daha elde edilmiştir: Fareler 8 hafta değil de 18 hafta boyunca yüksek yağlı diyete maruz bırakılıp kronik hasta edildiklerinde, 18 saatlik kısa süreli kalori kısıtlaması insülin direncini ancak kısmen düzeltebilmiştir. Bunun sebebi, uzun süreli obezitede yağ dokusunda hücre ölümlerinin artması, makrofajların dokuyu işgal etmesi (crown-like structures) ve dokudaki iltihabın (TNF-α gibi) kalori kısıtlamasıyla aniden geri çevrilemeyecek kadar kronikleşmiş olmasıdır.

Çalışmanın bulgularına derinlemesine baktığımızda, insan metabolizmasının bir makine gibi "ayarları sıfırlanıp eski haline dönen" basit bir yapı değil; kriz anlarında yepyeni stratejiler üreten dinamik bir **"sistem mühendisliği"** olduğunu görüyoruz.

Öncelikle sorunuzdaki çok önemli bir yanlış anlamayı düzeltelim: **1-3 günlük kalori kısıtlaması (veya diyet değişimi) kasta ve karaciğerde İŞE YARAMIŞTIR!** Hatta hastalığı çözen, insülin direncini (IR) tamamen kıran şey kasın ve karaciğerin iyileşmesidir. **Asıl işe yaramayan (eski sağlıklı haline dönmeyen) doku, Adipoz Dokudur (Yağ Dokusu - AD)**.

Araştırmacıların bulduğu bu muazzam paradoksu, etki mekanizmalarını ve "Yağ dokusunun düzelmemesi ne işe yaradı?" sorusunun cevabını adım adım, çıkarımlarıyla birlikte açıklayayım:

## 1. Doku Bazında Etki Mekanizmaları 

Bulgular, vücudun sadece "kilo vererek" iyileşmediğini; bunun yerine **"katabolik yeniden modelleme"** adını verdikleri yepyeni bir yağ yakım (hayatta kalma) moduna geçtiğini gösteriyor.

- **Karaciğer (Tam İyileşme ve Şalter Değişimi):** Karaciğerde insülin direnci tamamen kırılmıştır. Bunun mekanizması şudur: Karaciğerdeki toksik yağlar (DAG ve TAG) azalmış, hücredeki "kötü şalter" olan PKCε enziminin aktivitesi düşmüştür. En önemlisi, karaciğer sıfırdan yağ üretimini (De Novo Lipogenesis - DNL) durdurmuş ve bunun yerine yağı yakarak **keton cisimcikleri (BHB ve AcAc)** üretmeye (ketogenez) başlamıştır.
- **İskelet Kası (Şeker Kapılarının Açılması):** Kasta insülin sinyali normale dönmüş ve kandan şekeri (glikozu) hücre içine alma yeteneği (2-DOG klirensi) tamamen onarılmıştır. Kas hücresi, tıpkı karaciğer gibi enerji için yağ asidi oksidasyonunu (yağ yakımını) artırmış ve içindeki zehirli yağ birikimini temizlemiştir.
- **Yağ Dokusu (AD) - (Düzelmeyen ve Kilitli Kalan Doku):** Çalışmanın en şaşırtıcı sekonder bulgusu burasıdır. Kas ve karaciğer iyileşirken, **yağ dokusu insülin direncini kırmamış ve sağlıklı haline dönmemiştir**. Şeker alımı düşük kalmaya devam etmiş, yeni yağ üretimi (DNL) baskılanmış ve en önemlisi **lipoliz (yağ hücrelerinin içindeki yağı parçalayıp kana salma işlemi) kilitli kalmıştır**. Bunun sebebi, yağ dokusunu uyaran β-adrenerjik reseptör 3'ün (ADRB3) kalıcı olarak düşük kalmasıdır.

## 2. Yağ Dokusunda IR'nin Düzelmemesi Neyle Sonuçlandı? 

_"Yağ dokusu düzelmediyse vücut nasıl iyileşti?"_ diye sorabilirsiniz. Aslında **vücudu diyabetten kurtaran şey tam olarak yağ dokusunun bu "bozuk" (kilitli) kalma halidir.**

Eğer yağ dokusu eski haline dönseydi ve içindeki o devasa obezite yağlarını lipoliz ile kana pompalasaydı, kan dolaşımı serbest yağ asidi (NEFA) ile dolup taşardı. Ancak yağ dokusundaki o bozukluk (ADRB3'ün düşüklüğü), yağ dokusunu "kilitli bir kasaya" dönüştürdü ve kana yağ sızdırmasını (lipolizi) engelledi.

**Sistemik Sonuç:**

1. Yağ dokusu kana yağ (NEFA) salmayı durdurdu.
2. Karaciğer ve kas ise enerji için kanda kalan yağları hızla yakmaya başladı.
3. Sonuç olarak kandaki serbest yağ asidi (NEFA) seviyeleri aniden düştü. Kasta ve karaciğerde "yağ zehirlenmesi (lipotoksisite)" ortadan kalktı. Yağ stresi biten kas ve karaciğer, insüline tekrar duyarlı hale gelerek şekeri kandan çekmeye başladı ve **bütün vücudun diyabetik tablosu (HOMA-IR) sadece 3 günde normale döndü**.

## 3. Bu Bulguların Klinik Çıkarımları ve Olası Etkileri Nelerdir?

Bu bulgular, obezite ve diyabet (T2DM) tedavisinde bildiğimiz bazı ezberleri yıkıyor:

- **Çıkarım 1: İnsülin Direncini Kırmak İçin "Kilo Vermek" Şart Değildir:** Bugüne kadar IR'nin düzelmesi hep tartıdaki kilonun azalmasına bağlanırdı. Ancak bu çalışma, **gözle görülür hiçbir kilo kaybı (veya yağ kütlesi kaybı) olmasa bile**, sadece 1 ila 3 gün kalori kısıtlamanın (açlığın/diyet değişiminin), vücuttaki enerji akışını (NEFA'yı) keserek insülin direncini tamamen çözebileceğini kanıtlamıştır. _Klinik Etkisi:_ Diyetin ilk haftasında kilo veremeyen hastanın metabolizmasının iyileşmediğini düşünmek büyük bir hatadır. Biyokimyasal iyileşme, tartıdaki değişimden çok daha önce başlar.
- **Çıkarım 2: Maruziyet Süresi (Hastalık Yaşı) Her Şeyi Değiştirir:** Önceki konuşmamızda "obeziteye maruz kalma süresi otofajiyi ve hücresel yanıtı etkiler" demiştik. Bu makale bunu kusursuzca ispatlıyor. Fareler 8 hafta değil de **18 hafta boyunca obez bırakıldığında (kronikleştiğinde)**, aynı kalori kısıtlaması (açlık) insülin direncini tam olarak çözememiştir.
    - _Neden?_ Çünkü obezite uzadıkça yağ dokusunda hücre ölümleri başlamış, makrofajlar dokuyu işgal etmiş (Crown-like structures) ve TNF-α gibi iltihap maddeleri kalıcı hale gelmiştir. _Klinik Etkisi:_ Yeni obez olmuş bir hastayı 3 günlük diyetle metabolik olarak toparlayabilirsiniz, ancak 10 yıllık kronik obez/diyabetik bir hastada yağ dokusu iltihaptan (makrofaj istilasından) dolayı hasar gördüğü için kısa süreli açlıklar tek başına mucize yaratamaz.
- **Çıkarım 3: Sağlık, Geçmişe Dönmek Değil "Katabolik Esnekliktir":** Tedavideki amaç hastanın dokularını "hiç obez olmamış" bir insanın dokularına çevirmek değildir. Vücut, kalori kısıtlamasıyla karşılaştığında eski anabolic (depolayıcı) haline dönmez; keton üreten, yağı yakan ve yağ depolarını kilitleyen yepyeni bir **"katabolik (yıkım) profiline"** geçer.

**Özetle;** Bu çalışma, kalori kısıtlamasının (veya aralıklı açlığın) bir "zayıflama aracı" olmaktan ziyade, yağ dokusunun kana yağ sızdırmasını anında durduran ve karaciğer ile kası "yağ yakım / keton üretimi" moduna geçirerek lipotoksisiteyi (yağ zehirlenmesini) şok etkisiyle temizleyen hücresel bir acil durum freni olduğunu göstermektedir.


## Adipoz Doku Hiç Mi Normale Dönmüyor?
Durumu adım adım, hem kısa vadeli hem de uzun vadeli projeksiyonlarla açıklayayım:

### 1. Duan Çalışmasının Zaman Kısıtlaması (1-3 Günlük Şok)

Öncelikle şunu belirtmek gerekir: Duan ve ekibinin çalışması, kilo vermenin aylar süren uzun vadeli sürecini değil, **sadece diyetin değiştirildiği ilk 1 ila 3 günlük "akut" süreci** incelemiştir. Bu ilk 3 günde vücut henüz yağ kaybetmemiştir; sadece sistemi zehirleyen "yağ sızıntısını (NEFA)" acil bir frenle durdurarak karaciğer ve kası kurtarmış ve insülin direncini (IR) sistemik olarak çözmüştür.

### 2. NEFA Paradoksu: Uzun Vadede Yağlar Nasıl Eriyip Kana Karışıyor?

Kişi diyet yapmaya devam ettikçe ve aylar içinde 10-20 kg yağ kütlesi kaybettikçe, elbette adipoz dokudaki lipoliz (yağ yıkımı) yeniden aktive olmak ve NEFA (serbest yağ asitleri) kana salınmak _zorundadır_. Ancak bu uzun vadeli süreçte kana salınan NEFA, artık vücudu zehirlemez ve insülin direnci yaratmaz. Neden mi?

Çünkü diyetin ilk günlerinde karaciğer ve iskelet kası, **"katabolik yeniden modelleme"** geçirmiş; yani devasa birer yağ yakım ve keton üretim fabrikasına dönüşmüşlerdir. Aylar süren diyet boyunca yağ dokusundan kana yavaş yavaş salınan NEFA'lar, karaciğerde ve kasta zehirli lipitler (DAG, seramid vb.) olarak birikmeye fırsat bulamadan **anında yakıt (enerji) olarak tüketilir**. Yani sistemik NEFA dolaşımı olsa bile, bu bir "birikim" değil, "akış" halindedir.

### 3. Adipoz Doku Ne Zaman Normale Dönüyor? (Dönmüyor!)

Sorunuzun en can alıcı kısmı burası: _Adipoz doku tamamen eski, sağlıklı (hiç obez olmamış) haline dönüyor mu?_Literatürdeki en güncel çalışmalara (özellikle eklediğiniz **Zhu ve ark., 2026** ve **Li ve ark., 2023** kaynaklarına) göre cevap çarpıcıdır: **Hayır, adipoz doku ciddi bir kilo kaybından sonra bile tam anlamıyla "normale" dönmez; kalıcı bir hasar ve direnç izi taşır.**

Vücut normale dönse bile adipoz dokuda kalan kalıcı hasarlar şunlardır:

- **Mekanik Hafıza ve Kalıcı Fibrozis (Zhu ve ark., 2026):** Obezite sırasında aşırı büyüyen yağ hücrelerinin etrafındaki iskelet (Hücre Dışı Matriks - ECM) fibrozisle kalınlaşır ve sertleşir. Kişi kilo verdiğinde yağ hücreleri (adipositler) sönüp küçülür, ancak **o sert fibrotik kafes ve doku sertliği kalıcıdır (geri dönmez)**. Küçülmüş yağ hücresi, bu sert boşluğun içinde mekanik bir gerilime (strese) maruz kalır.
- **İmmünolojik Hafıza (Li ve ark., 2023):** Obezite sırasında yağ dokusunu işgal eden iltihaplı makrofajlar ve bağışıklık hücreleri, kişi kilo verip zayıflasa bile o iltihaplı "obezite fenotiplerini" (davranışlarını) korumaya devam ederler.
- **Epigenetik Hafıza:** Kilo verildikten sonra bile adipositlerin genetik kodlarındaki (DNA metilasyonlarındaki) "obeziteye ait epigenetik hafıza" silinmez.

### 4. AD Hep IR-Resistant mı Kalıyor Yani? 

Adipoz doku sistemik olarak vücudu zehirlemeyi bıraksa da, kendi içinde kısmen dirençli, metabolik olarak esnekliğini kaybetmiş ve "kilitli" kalmaya eğilimlidir.

**İşte insanların diyetle verdikleri kiloları aylar/yıllar sonra hızla geri almalarının (Weight Rebound / Yo-yo etkisi) asıl sebebi, adipoz dokunun bu "normale dönememe" halidir.**

Zhu ve arkadaşlarının belirttiği gibi; küçücük kalmış ama etrafı sert bir kafesle (fibrozisle) sarılı olan o yağ hücresi, bu fiziksel ve mekanik stresten kurtulmak zorundadır. Hücre, mekanik dengeyi yeniden kurabilmek için (mekanik hafıza) **en ufak bir kalori fazlasında adeta bir sünger gibi hızla yeniden yağ çekip şişmeye programlanmıştır**. Yani bağışıklık ve epigenetik sistemi önceden tetikte bekleyen (pre-activated) yağ dokusu, kaloriyi gördüğü an "kaldığı yerden" obeziteye devam eder.

**Özetle:** Vücut (karaciğer ve kas) diyetle şok bir şekilde iyileşir ve insülin direncini çözer. Ancak adipoz doku (yağ dokusu) savaştan çıkmış ve yara izi (fibrozis) kalmış bir asker gibidir. Tamamen naif (eski) haline dönmez; sistemik bir diyabet yaratmasa da, obezite hafızasını içinde saklayarak her an kiloları geri almaya (weight rebound) hazır, kısmen disfonksiyonel bir doku olarak kalır.

## Diyetisyenler İçin OMAD ve Maruziyet Bağlamında Çıkarımlar

Bu çalışmayı ve sizin vizyonunuzu birleştirdiğimizde, klinik diyetisyenlik pratiği için çok net çıkarımlar doğuyor:

**A. İleri Evre Diyabetikte/Obezitede OMAD Bir "Mucize" Değildir:** Diyetisyenler genellikle Aralıklı Açlık veya OMAD'ı herkese aynı şiddetle önerirler. Ancak çalışma, 18 haftalık (kronik) obez farelerde 18 saatlik açlığın (OMAD muadili) sistemi tam tamir edemediğini gösteriyor. Kronik hastalarda yağ dokusu zaten iltihaplı (makrofaj istilasında) olduğu için, bu hastaları bir anda 23 saat aç bırakmak (OMAD), otofajiyi sağlıklı bir şekilde başlatmak yerine hücre içi stresi ve hasarı daha da derinleştirebilir. Kronik hastalarda OMAD yerine daha ılımlı (örneğin 12:12 veya 14:10) kısıtlamalarla yavaş bir adaptasyon süreci başlatılmalıdır.

**B. Şok Diyetlerin (VLCD/Açlık) İlk Günlerindeki Başarı "Yağ Yakımı" Değildir:** Hastalar OMAD'a veya çok düşük kalorili diyetlere başladıklarında ilk günlerde kan şekerleri aniden düzelir. Diyetisyen ve hasta bunun "yağların erimesinden" kaynaklandığını sanır. Oysa çalışma bunun tam tersini ispatlıyor: İnsülin direncinin aniden düzelmesinin sebebi yağların erimesi değil, yağ dokusunun "kendini kilitleyerek" (lipolizi, yani kana yağ asidi sızdırmasını durdurarak) karaciğer ve kası zehirlenmekten (lipotoksisiteden) kurtarmasıdır. Diyetisyenin buradaki vizyonu, hastaya "Harika yağ yakıyoruz" demek yerine, "Vücudundaki zehirli yağ sızıntısını durdurduk, şimdi karaciğerini iyileştiriyoruz" demek olmalıdır.

**C. Yağ Dokusu "Dirençli" (Resistant) Kalmaya Devam Eder:** OMAD veya açlık ile sistemik insülin direnci çözülse de, yağ dokusunun lipolitik (yağ yıkım) kapasitesi ve glikoz alımı uzun süre bozuk kalmaya devam eder (ADRB3 reseptörü düşük kalır). Diyetisyen, hastanın kan tablosu (HbA1c, HOMA-IR) düzelse bile, hastanın yağ dokusunun hücresel ve mekanik olarak hala "obezite hafızası" taşıdığını bilmelidir. Hasta tek öğünü (veya diyeti) bırakıp aşırı kalori aldığında, bu kilitli ve hasarlı doku hızla yeniden şişerek (Weight Rebound) kiloları geri alacaktır.

**Özetle;** OMAD (Tek Öğün) gibi agresif kısıtlamalar, sistemik zehirlenmeyi (NEFA akışını) bir "acil durum freni" gibi anında keserek karaciğeri ve kası kurtaran müthiş bir araçtır. Ancak hastanın "obezite yaşı (maruziyet süresi)" ilerledikçe bu frenin tutma ihtimali azalır. Sizin planladığınız çalışma, tam da bu "frenin" (otofaji ve lipit metabolizması üzerinden) hastanın hastalığının hangi evresinde çalışıp, hangi evresinde kilitlendiğini ortaya çıkaracak bir başyapıt potansiyeli taşımaktadır.