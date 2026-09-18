---
Tür:
  - Besleyici
ODAK:
  - "[[Ultra İşlenmiş Besinler]]"
MEKANİZMA:
DİZİN:
  - "[[Kişiselleştirilmiş Beslenme]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[UPF Sınıflandırma Yöntemleri ve Aralarındaki Tutarsızlıklar]]"
  - "[[UPF Kanıtlarının Sınırlılıklarına Dair, Daha İyi UPF Çalışmaları Planlamak]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[UPF Sınıflandırmaların Dair Çalışma Fikirleri]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: https://doi.org/10.1371/ journal.pmed.1004560
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "p < 0.001"
BESLEDİĞİ NOTLAR:
  - "[[UPF Sınıflandırma Yöntemleri ve Aralarındaki Tutarsızlıklar]]"
  - "[[Mikrobiyota ve Kişiselleştirilmiş Beslenme]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Ultra İşlenmiş Besin (Parçalanmış Gıda Matrisi)"] --> B["Hızlı Gastrointestinal Geçiş & Emilim"]
>     B --> C["Akut Glisemik / İnsülinemik Pikler"]
>     B --> D["Distal İleal Frenin Bypass Edilmesi"]
>     C & D --> E["Erken Acıkma & Hiperfaji"]
> ```
>
> **Şekil Açıklaması:** Ultra işlenmiş besinlerde tahrip edilmiş gıda matrisi, gastrointestinal geçişi hızlandırarak distal ileal fren mekanizmasını bypass eder. Bu durum hem akut glisemik/insülinemik piklere hem de tokluk sinyallerinin gecikmesiyle erken acıkma ve hiperfajiye yol açar.

### **1. Araştırma Tasarımı ve Yöntemleri**

Çalışma, iki aşamalı güçlü bir metodolojik kurguya sahiptir:

- **Keşif Aşaması (Gözlemsel):** ABD'deki **IDATA Çalışmasına** katılan 50-74 yaş arası **718 sağlıklı yetişkinden** 6 ay arayla seri kan ve idrar örnekleri toplanmış, 12 ay boyunca 1 ila 6 kez 24 saatlik diyet hatırlatması (ASA-24) alınmıştır. Bu örneklerde **1000'den fazla serum ve idrar metaboliti** taranmıştır. LASSO regresyon analizleri kullanılarak UPF tüketimini en iyi öngören metabolit skorları oluşturulmuştur.
- **Doğrulama Aşaması (Klinik Deney):** Geliştirilen bu biyobelirteç skorları, NIH Klinik Merkezinde **20 sağlıklı bireyin** katıldığı ve 2 hafta boyunca **%80 UPF** ile 2 hafta boyunca **%0 UPF** içeren diyetlerin ad libitum (serbestçe) tüketildiği **çapraz geçişli (crossover) kontrollü bir besleme çalışmasında** test edilmiştir.

---

### **2. Öne Çıkan Bulgular ve Kritik Biyobelirteçler**

Yapılan analizlerde UPF alım oranlarıyla doğrudan ilişkili yüzlerce metabolit (191 serum ve 293 idrar metaboliti) saptanmıştır. LASSO modeli ile **28 serum, 33 24 saatlik idrar ve 23 ilk sabah idrarı metaboliti** en güçlü tahminciler olarak seçilmiştir.

Hem kan hem de idrarda en kararlı ve güçlü çalışan biyobelirteçler şunlardır:

- **N6-carboxymethyllysine (Pozitif İlişkili):** UPF tüketimi yüksek olanlarda belirgin şekilde artan bu bileşik, şekerlerin protein veya lipidlerle reaksiyona girmesiyle oluşan bir **ileri glikasyon son ürünüdür (AGE)**. Bu metabolit, diyabet ve kardiyometabolik hastalık riskleriyle doğrudan ilişkilidir.
- **(S)C(S)S-S-Methylcysteine sulfoxide (Negatif İlişkili):** Lahanagiller (cruciferous) tüketiminin bir biyobelirtecidir. UPF alımı arttıkça bu değerin düşmesi, yüksek UPF tüketenlerin sağlıklı sebzeleri beslenmelerinden çıkardığını doğrulamaktadır.
- **Levoglucosan (İdrarda Pozitif İlişkili):** Paketleme malzemelerinde kullanılan selülozun bir yıkım ürünüdür. İdrarda bu bileşiğin yüksek olması, yüksek UPF tüketen kişilerin **ambalaj malzemelerinden gıdaya geçen kimyasallara doğrudan maruz kaldığını** göstermektedir.
- **Beta-kriptoksantin ve Karoten Diol (Negatif İlişkili):** Narenciye, kırmızı biber ve taze meyve-sebze tüketiminin göstergeleri olan bu provitamin A karotenoidleri, UPF tüketimi arttıkça dramatik şekilde düşmektedir.

---

### **3. UPF Tüketiminin Genel Diyet Kalitesine Etkisi**

Çalışmada, UPF tüketimi en yüksek olan grup (Quintile 5) ile en düşük olan grup (Quintile 1) kıyaslandığında, UPF tüketiminin artmasıyla diyet kalitesinin nasıl çöktüğü net olarak gösterilmiştir:

- **Düşen Değerler:** Protein ve idrar azotu seviyeleri, lif yoğunluğu (7.9 g vs 10.7 g/1000 kcal), A, C, D, E vitaminleri ile demir, çinko, potasyum, magnezyum, fosfor ve kalsiyum alımları anlamlı şekilde azalmıştır.
- **Artan Değerler:** Karbonhidrat, ilave şeker ve doymuş yağ tüketimi anlamlı oranda artmıştır.

---

### **4. Çapraz Geçişli Klinik Deneyde Tam Doğrulama**

IDATA kohortunda (serbest yaşayan bireylerde) geliştirilen poli-metabolit skorları, klinikte yatırılarak %80 ve %0 UPF tükettirilen bağımsız katılımcıların kan ve idrar örneklerine uygulandığında, **bireylerin UPF diyet fazlarını kendi içlerinde (within-individual) kusursuz ve son derece anlamlı bir şekilde ayırt etmeyi başarmıştır (P < 0.001)**. Ayrıca, diyetin UPF oranındaki basamaklı artışı (0%, 30% ve 80%) idrar skorlarındaki adım adım artışın izlenebildiği doğrulanmıştır.

---

### **💡 Çalışmanın Akademik Çıkarımı**

Bu araştırma, gelecekteki epidemiyolojik çalışmalarda sadece katılımcıların anket beyanlarına güvenmek yerine, **kan veya idrardan alınacak basit bir biyobelirteç profiliyle kişilerin gerçek UPF maruziyet düzeylerinin objektif olarak ölçülebileceğini** kanıtlamıştır. Ayrıca, UPF ambalajlarından vücuda geçen levoglukozan gibi bileşiklerin ve diyabet riskiyle ilişkili N6-karboksimetillizin gibi moleküllerin tespiti, UPF tüketiminin sağlığı hangi patolojik yolaklarla bozduğunu anlamak için devasa bir kapı aralamaktadır.


**Araştırmacılar Pratikte Kullanmak İçin Bir Metabolit Kümesi Önerdi mi?**

**Evet, araştırmacılar tam olarak bunu yaptı ancak bu sistem ticari bir "basit hızlı test" değil, gelişmiş bir istatistiksel skorlama modelidir****.**

Araştırmacılar, serbest yaşayan bireylerden (IDATA Kohortu) elde edilen veriler üzerinde **LASSO regresyon analizi** kullanarak, UPF tüketim düzeyini en güçlü şekilde tahmin eden spesifik metabolit kümeleri seçmişlerdir. Bu metabolitlerin her birinin ağırlık katsayısı (korelasyon gücü) hesaplanmış ve **"Poli-Metabolit Skorları" (Poly-metabolite Scores)** adı verilen doğrusal formüller oluşturulmuştur.

**"Şu Seviye Çıkarsa Şu Kadar UPF Tüketiyordur" Denilebilir mi?**

Makalede sunulan katsayılar (S6 Table), metabolitlerin log-transforme edilmiş konsantrasyonlarının ağırlıklı toplamını alarak sürekli (continuous) bir UPF enerji yüzdesi tahmini yapmaktadır. Ancak yazarlar, bu skorlama sisteminin bireysel bir kesin tanı aracından ziyade, **tıpkı genetik çalışmalardaki "poligenik risk skorları" gibi** epidemiyolojik çalışmalarda popülasyon düzeyindeki maruziyeti objektif olarak sınıflandırmak için kullanılmasını önermektedir. Model, bireyleri UPF tüketim yüzdelerine göre (örneğin en yüksek %25'lik dilim ile geri kalanlar) ayırt etmede orta-yüksek düzeyde bir doğruluk (AUC: 0.66 - 0.78) sağlamaktadır.

**Doğrudan makale yazarlarının işaret ettiği ve verilerini depoladığı resmi platformlar bulunmaktadır**:

**1. MetaboLights (Açık ve Doğrudan Erişimli Klinik Deney Verisi)**

Makalede sunulan, 20 sağlıklı bireyin katıldığı ve %80 UPF ile %0 UPF diyetlerinin ad libitum (serbestçe) tüketildiği kontrollü çapraz geçişli klinik besleme çalışmasına ait metabolomik veriler tamamen kamuya açık bir şekilde **MetaboLights** veri tabanına yüklenmiştir.

- **Veri Tabanı Platformu:** [MetaboLights](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.ebi.ac.uk%2Fmetabolights%2F)
- **Çalışma Tanımlayıcı Kodu (Study Identifier):** **REQ20250409209843**
- **Kullanım Amacı:** Bu tanımlayıcıyı kullanarak plazma, 24 saatlik idrar ve anlık (spot) idrar metabolomik verilerini doğrudan indirebilir; levoglukozan, beta-kriptoksantin ve CML gibi spesifik moleküllerin diyet fazlarına göre değişimini kendi bilgisayarınızda test edebilirsiniz.

**2. Cancer Data Access System - CDAS (Gözlemsel Kohort Verisi)**

718 katılımcıdan oluşan geniş gözlemsel **IDATA Çalışmasına** ait seri kan, 24 saatlik idrar ve ilk sabah idrarı metabolomik verileri ile beslenme anketleri kayıtları, ABD Ulusal Kanser Enstitüsü'nün (NCI) CDAS portalı üzerinden araştırmacılara açılmıştır.

- **Erişim Sayfası:** [CDAS IDATA Instructions](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcdas.cancer.gov%2Flearn%2Fidata%2Finstructions%2F)
- **Erişim Şartı:** Bu verileri indirmek için web sitesi üzerinden bir proje önerisi (proposal) sunulması ve resmi bir Veri Transfer Anlaşması'nın (Data Transfer Agreement - DTA) imzalanması gerekmektedi