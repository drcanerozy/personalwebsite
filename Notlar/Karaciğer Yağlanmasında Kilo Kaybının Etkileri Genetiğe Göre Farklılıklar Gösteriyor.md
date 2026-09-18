---
Tür:
  - Besleyici
ODAK:
  - "[[Karaciğer Yağlanması]]"
MEKANİZMA: "[[Genetik, Epigenetik, Nutrigenetik]]"
DİZİN: "[[Kilo Verme]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[İkiz Döngü Hipotezi]]"
  - "[[Kalori Kısıtlaması, Kilo Kaybı Olmasa da İnsülin Direncini Kısa Sürede İyileştiriyor, Ancak Doku Bazında Etkileri Farklı.]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[MASLD'de Genetik Varyasyonlar ve Mikrobiyota Temelli Kişiselleştirilmiş Beslenme Yaklaşımları]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: https://doi.org/10.1016/j.clnu.2026.106672
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Diyet Modellerin Tanımları ve Etkileri (MASLD Bağlamında)]]"
  - "[[Farklı Obezite Fenotipleri]]"
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
### 1. Çalışmanın Amacı Nedir?

Bu çalışmanın temel amacı; genetik profilleri (riskleri) önceden belirlenmiş olan aşırı kilolu veya obez MASLD (Metabolik disfonksiyon ilişkili steatotik karaciğer hastalığı) hastalarında, **kilo kaybı odaklı kişiselleştirilmiş Akdeniz diyetinin klinik, laboratuvar ve en önemlisi "serum metabolomik profilleri" üzerindeki etkilerini** tanımlamaktır. Çalışma, hastaların verdiği kilo miktarına ve taşıdıkları spesifik genetik risk alellerine göre metabolik değişimlerin nasıl farklılaştığını (modüle edildiğini) haritalandırmayı hedeflemiştir.

### 2. Çalışmanın Hipotezleri Nelerdir?

Araştırmacıların kurduğu hipotezler, önceki tartıştığımız "Hassas Beslenme / Precision Nutrition" vizyonuyla birebir örtüşmektedir:

- **Genetik x Tedavi Etkileşimi:** Yaşam tarzı değişikliklerine (diyet ve kilo kaybına) verilen metabolik ve hücresel yanıtlar evrensel veya homojen değildir; bu yanıtlar hastanın **genetik yatkınlığından** yüksek oranda etkilenmektedir.
- **PNPLA3 Paradoksu:** Özellikle MASLD'nin en büyük genetik suçlusu olan _PNPLA3_ gen mutasyonunu taşıyan hastalar, karaciğer yağlanmasına ve iltihaba çok daha yatkın olsalar da; kilo verdiklerinde karaciğerlerindeki iyileşme potansiyeli genetik mutasyonu olmayanlara kıyasla çok daha yüksek (paradoksal bir gen-çevre etkileşimi) olmalıdır.
- **Dinamik Biyobelirteçler:** Klasik kan tahlilleri yerine kanın "metabolomik" (tüm metabolitleri gösteren) haritasını çıkarmak; kilo kaybının karaciğeri nasıl iyileştirdiğini gösteren yepyeni metabolik aracıları ve dinamik biyobelirteçleri bulmamızı sağlayabilir.

### 3. Çalışma Kısaca Nasıl Yapıldı? (Metodoloji)

Çalışma, oldukça sıkı tasarlanmış, teknolojik ve prospektif (ileriye dönük) bir klinik kohort araştırmasıdır.

- **Katılımcılar:** Ultrason ile MASLD (karaciğer yağlanması) teşhisi kesinleşmiş, Vücut Kitle İndeksi (BMI) 25'in üzerinde olan 148 yetişkin hasta dahil edilmiştir. (Diyet veya kilo kaybını etkileyecek GLP-1 gibi ilaçlar kullananlar çalışmadan çıkarılmıştır).
- **Genetik Profilleme:** Sürecin başında tüm hastalardan kan alınarak, karaciğer yağlanması ile ilişkili 4 kilit genetik mutasyon (_PNPLA3, TM6SF2, MBOAT7, GCKR_) taranmış ve hastaların "Poligenik Risk Skorları" (PRS) hesaplanmıştır.
- **Diyet Müdahalesi:** Hastalara 6 ay boyunca, kişiye özel planlanmış, günlük 1300-1800 kcal içeren **hipokalorik (düşük kalorili) Akdeniz Diyeti** uygulanmıştır. Makrobesin dağılımı %45-50 düşük glisemik indeksli karbonhidrat, %20-25 protein ve %30-35 sağlıklı yağlar (zeytinyağı vb.) olacak şekilde ayarlanmıştır. Hastalar her 4 haftada bir diyetisyen eşliğinde kontrolden geçirilmiştir.
- **Metabolomik Ölçüm:** Diyetin başında (0. ay) ve sonunda (6. ay) alınan açlık serum örnekleri, "Hedefsiz Gaz Kromatografisi-Kütle Spektrometrisi (GC-MS)" isimli son teknoloji bir cihazla analiz edilerek hastaların vücudundaki yüzlerce farklı küçük molekülün/metabolitin haritası çıkarılmıştır.
- **Klinik Takip ve Gruplandırma (Çalışmanın Eşsiz Yönü):** Hastaların vücut ağırlıkları ve FibroScan (VCTE/CAP) cihazıyla karaciğer yağlanma (steatoz) oranları düzenli ölçülmüştür. Analiz aşamasında hastalar "Verdikleri Kilo Yüzdesine" göre 3 gruba ayrılmış (Düşük Yanıt:  < %5, Orta Yanıt: %5-10, Yüksek Yanıt: >%10) ve "Taşıdıkları Genetiğe" (_PNPLA3_ genine sahip olanlar vs. olmayanlar) göre katmanlara (stratifikasyon) bölünerek; kimin diyetinin metabolizmayı nasıl değiştirdiği karşılaştırmalı olarak incelenmiştir.

Kişiselleştirilmiş Akdeniz diyeti ve kilo kaybının karaciğer yağlanması (MASLD) üzerindeki etkilerini metabolomik ve genetik katmanlarla inceleyen bu çalışmanın bulguları, mekanizmaları ve klinik çıkarımları şu şekildedir:

### Primer (Birincil) Bulgular

- **Hızlı Kilo Kaybı ve Steatoz (Yağlanma) İyileşmesi:** 6 aylık hipokalorik Akdeniz diyeti sonucunda hastalarda ortalama %8 vücut ağırlığı kaybı ve karaciğer yağlanmasını gösteren **CAP (Kontrollü Zayıflama Parametresi) değerinde yaklaşık %17 oranında belirgin bir azalma** saptanmıştır. Bu iyileşmenin en büyük kısmı diyetin **ilk 8 haftasında** gerçekleşmiştir.
- **Fibrozis (Karaciğer Sertliği) Sabit Kalmıştır:** Karaciğer yağlanması hızla azalsa da, karaciğer sertliğini (fibrozisi) yansıtan "Liver Stiffness (LS)" değerinde 6 ay sonunda anlamlı bir değişim olmamıştır.
- **Doza Bağımlı Yanıt:** Kilo kaybı yüzdesi arttıkça karaciğerdeki steatoz azalması da orantılı olarak büyümüştür (< %5 kilo kaybında CAP -%8.1, %5-10 kilo kaybında CAP -%14.4, >%10 kilo kaybında CAP -%22.9 düşmüştür).
- **Genetik Faktörün (PNPLA3) Üstünlüğü:** En belirgin karaciğer yağlanması (CAP) düşüşü, MASLD için en bilinen genetik risk faktörü olan **PNPLA3 geninin G-aleli mutasyonunu taşıyan hastalarda** görülmüştür.

### Sekonder (İkincil / Metabolomik) Bulgular

- **Güçlü Metabolomik Yeniden Modelleme:** Diyet öncesi ve sonrası hastaların serum metabolomik profilleri arasında devasa bir fark (PLS-DA modelinde %92 doğruluk) saptanmıştır.
- **Evrensel Biyobelirteç Üçlüsü:** Kilo kaybı oranından ve hastanın genetiğinden bağımsız olarak her modelde tutarlı bir şekilde serumda seviyesi artan üç kilit metabolit bulunmuştur: **Kaproik asit, gliserol ve hidroksipropanedioik asit**.
- **Azalan Toksik Metabolitler:** Diyet sonrasında karaciğere toksik etki yapan palmitik asit (doymuş yağ) ve D-galaktoz seviyeleri belirgin şekilde düşmüştür.
- **Yanıt Düzeyine Göre Değişim:** %10'dan fazla kilo veren "yüksek yanıtlı" hastalarda ekstra olarak dallı zincirli amino asitlerin (BCAA'lar) seviyelerinin arttığı gözlemlenmiştir. İlginç şekilde, %5'ten az kilo veren "düşük yanıtlı" grupta bile erken evre olumlu metabolik değişimler saptanmıştır.

### Bulgular Hangi Mekanizmalarla Açıklanmış?

1. **Artmış Lipoliz ve Hepatik Ketogenez:** Gliserol ve 3-hidroksibutirik asitteki (bir keton cisimciği) artışlar, vücudun enerji açığını (kalori kısıtlamasını) telafi etmek için yağları seferber ettiğini (lipoliz) ve yağ asidi beta-oksidasyonunu (FAO) hızlandırdığını göstermektedir.
2. **Glukoneogenez Adaptasyonu:** Karbonhidrat kısıtlaması nedeniyle hücrelerin kan şekerini koruma çabası, gliserol, alanin ve laktik asit gibi metabolitlerin artışıyla açıklanmıştır. Vücut bu maddeleri karaciğerde yeni şeker üretmek (glukoneogenez) için ana hammadde olarak kullanmıştır.
3. **Bağırsak Mikrobiyotası ve Yağ Asidi Profili:** Kaproik asit (kısa/orta zincirli bir yağ asidi) miktarındaki tutarlı artışın, Akdeniz diyetinin bağırsak mikrobiyotasını faydalı yönde yeniden modellemesinden veya farklı bir yağ metabolizması akışından kaynaklandığı belirtilmiştir.
4. **Antioksidan Savunmanın Yeniden Kurulması:** D-riboz ve glisin gibi metabolitlerdeki artışlar, hücresel "Pentoz Fosfat Yolağı (PPP)" aktivasyonunu ve glutatyon üretimini yansıtır. Yazarlar, diyetin sadece yağları yakmadığını, aynı zamanda MASLD'de bozulan **redoks dengesini (antioksidan kapasiteyi) onardığını** belirtmiştir.
5. **PNPLA3 Paradoksunun Çözümü:** MASLD riskini artıran PNPLA3 mutasyonuna sahip bireyler, karbonhidrat ağırlıklı beslendiklerinde bu mutant gen yağ parçalayıcı enzimleri (ATGL) bozarak şiddetli yağlanma yapar. Ancak kalori kısıtlaması ve açlık yapıldığında mutant genin ifadesi azalır; yağ parçalayıcı enzimlerin aktivitesi aniden iyileşerek **biriken yağların yıkımında wild-type (sağlıklı gen) bireylere göre daha üstün bir lipoliz** yanıtı verir.

### Bulguların Klinikteki Önemi (Çıkarımlar) Nedir?

- **"Hassas Beslenme" (Precision Nutrition) Vizyonuna Geçiş:** Bu çalışma, "herkese standart düşük kalorili diyet" ezberini yıkmaktadır. Diyetisyenlerin ve hekimlerin, hastanın PNPLA3 gibi genetik varyantlarını önceden bilerek, kişinin diyete vereceği metabolik yanıtı öngörebileceği ve MASLD yönetimini **kişiselleştirebileceği (precision nutrition)** kanıtlanmıştır.
- **Erken Teşhis ve Takip İçin Yeni Biyobelirteçler:** Geleneksel karaciğer enzimlerinin (ALT, AST) ötesinde; **kaproik asit, gliserol ve hidroksipropanedioik asit**, hastanın karaciğerindeki yağ hücrelerinin boşaldığını (tedavinin işe yaradığını) gösteren anlık ve yeni nesil klinik biyobelirteçler olarak kullanılabilecektir.
- **Diyetisyenler İçin Motivasyon Aracı:** Yağlanmadaki (CAP) büyük azalmanın daha **ilk 8 haftada** hızlıca gerçekleşmesi, diyet sürecinde hastanın motivasyonunu ve diyete uyumunu (adherence) artırmak için müthiş bir klinik geri bildirim aracı olarak kullanılabilir.
- **"Kilo Veremiyorum" Krizinin Çözümü:** < %5 gibi hedeflerin altında (çok az) kilo veren hastalarda bile kan metabolomik haritasının (lipotoksisitenin) olumlu yönde yeniden modellenmeye başladığı bulunmuştur. Bu durum klinisyene, "Tartıda fazla eksi görmesek de metabolizmanız hücresel bazda iyileşmeye başladı" güvencesini verme imkanı sunar.
- **Fibrozis Yönetiminde Uzun Vade Gerekliliği:** 6 ayda yağlanma tamamen çözülse de karaciğer sertliğinde (LS) bir değişim olmaması; fibrozis (kronik hasar) çözünmesinin 6 aydan çok daha uzun süreli ve kesintisiz bir metabolik baskı gerektirdiğini klinik olarak ispatlamaktadır.



