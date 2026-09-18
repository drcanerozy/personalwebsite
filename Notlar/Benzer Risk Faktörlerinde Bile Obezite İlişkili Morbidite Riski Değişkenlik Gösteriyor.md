---
Tür:
  - Besleyici
ODAK:
  - "[[Obezite]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Obezite İlişkili Riskte Bel Çevresi Kullanmak Oldukça Önemli]]"
  - "[[Metabolik olarak sağlıklı ve sağlıksız obeziteli bireylerin risk profilleri]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[Yetişkinlerde Beslenme Tedavisi Uygulaması]]"
YORUM:
KAYNAK: https://doi.org/10.1038/ s41591-026-04353-2 (2026)
study_type:
evidence_direction: "contradictory"
primary_outcome:
p_value_summary:
BESLEDİĞİ NOTLAR:
  - "[[Farklı Obezite Fenotipleri]]"
  - "[[BKİ Yerine Adipozite Bazlı Sınıflandırma Hastalık Riski ile Daha Fazla İlişkili]]"
---
> **Metodolojik Etiketler:** #finding/contradictory

![[Ekran Resmi 2026-08-31 10.49.25.png]]
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

### 1. Çalışma Nasıl Yapılmış? (Metodoloji)

- **Popülasyon ve Veri Havuzu:**
    - **UK Biobank** kohortundan başlangıç VKİ'si ≥27 kg/m2≥27 kg/m2 olan **200.000 yetişkin** birey dahil edilmiştir.
    - Bireylerin 2.000'den fazla genel klinik, biyokimyasal, antropometrik ve moleküler parametresi incelenmiştir.
- **Makine Öğrenimi ve Model Geliştirme (OBSCORE):**
    - Obeziteyle ilişkili **18 farklı komplikasyonun** (Tip 2 Diyabet, kardiyovasküler mortalite, MACE, MASLD, kronik böbrek hastalığı, inme, uyku apnesi, gut, artropati, GÖRH vb.) 10 yıllık gelişim riskini tahmin etmek üzere makine öğrenimi modelleri eğitilmiştir.
    - Binlerce parametre arasından, 18 sonucun tamamında en yüksek bilgi değerine sahip **ortak ve minimal 20 özellikten (20 shared minimal features)** oluşan sade ve klinik olarak uygulanabilir bir skorlama modeli (**OBSCORE**) türetilmiştir.
- **Dış Doğrulama (External Validation):**
    - Modelin genellenebilirliği iki bağımsız kohortta test edilmiştir:
        - **EPIC-Norfolk:** Avrupa kökenli bağımsız kohort.
        - **Genes & Health:** Doğu Londra merkezli, etnik açıdan çeşitlilik gösteren (özellikle Güney Asya kökenli) kohort.
- **Klinik İlaç Çalışmasına Uygulama:**
    - Model, bir obezite farmakoterapisi klinik çalışması olan **SURMOUNT-1 (Tirzepatid vs. Plasebo)** verilerine uygulanarak tedavi öncesi ve sonrası risk değişimleri değerlendirilmiştir.

---

### 2. Temel Bulgular Nelerdir?

1. **Yüksek Ayrım Gücü (Discrimination):**
    - OBSCORE, 18 komplikasyonun 10 yıllık insidansını tahmin etmede **0.62 – 0.86 arasında C-indeksi** (güçlü ayrım gücü) sergilemiştir.
2. **Uç Risk Grupları Arasındaki Devasa Fark:**
    - En yüksek riskli %20'lik grup ile en düşük riskli %20'lik grup karşılaştırıldığında:
        - **Tip 2 Diyabet (T2D) insidansı:** **42 kat daha yüksek**,
        - **Kardiyovasküler mortalite:** **47 kat daha yüksek** bulunmuştur.
3. **Aynı VKİ'de Yüksek Biyolojik/Klinik Heterojenite:**
    - Aynı yaş, cinsiyet ve VKİ değerine sahip bireylerin komplikasyon geliştirme risk profillerinin birbirinden tamamen farklı olduğu radar grafikleriyle gösterilmiştir.
4. **VKİ 27−30 kg/m227−30 kg/m2 Aralığındaki "Gizli Yüksek Riskli" Bireyler:**
    - En yüksek risk dilimindeki bireylerin önemli bir kısmının BMI>30BMI>30 değil, aslında hafif kilolu / aşırı kilolu kabul edilen **BMI 27–30 kg/m2BMI 27–30 kg/m2 aralığında** olduğu tespit edilmiştir (örneğin T2D için en yüksek risk grubundakilerin %30'u bu aralıktadır).
5. **SURMOUNT-1 (Tirzepatid) Sonuçları:**
    - Tirzepatid ile elde edilen kilo kaybı en yüksek riskli grupta da diğer gruplarla benzer düzeyde gerçekleşmiştir.
    - İlaç tedavisi sonrasında katılımcıların OBSCORE ile hesaplanan tahmini risk skorlarında belirgin düşüş kaydedilmiştir.

---

### 3. Bulguların Önemi ve Klinik Doğuruları

- **VKİ Paradigmasının Aşılması:** Yalnızca boy ve kiloya dayalı VKİ sınırları, adipoz dokunun dağılımını ve metabolik yükü yansıtmaz. Bu çalışma, obezitenin "adipozite temelli kronik bir hastalık" olarak risk odaklı ele alınması gerektiğini kanıtlamaktadır.
- **Yeni Nesil İlaçlarda Hakkaniyetli ve Hedefe Yönelik Önceliklendirme:** GLP-1/GIP reseptör agonistleri gibi etkili ancak maliyetli tedavilerin, sadece BMI≥30BMI≥30 sınırına takılmadan, **komplikasyon geliştirme riski en yüksek olan bireylere (VKİ 27–30 olsa dahi)** öncelikli olarak ulaştırılmasına bilimsel zemin hazırlamaktadır.
- **Klinik Olarak Uygulanabilir Sade Mimari:** Binlerce moleküler ölçüm yerine 20 temel parametre ile 18 morbiditeyi aynı anda risk dilimlerine (desillere) ayırabilmesi, birinci basamak ve uzmanlık kliniklerinde kişiselleştirilmiş tedavi planlamasına olanak tanımaktadır.
Bu çalışmanın (_Nature Medicine, 2026_) en çarpıcı ve devrimsel çıktısı, makaledeki **Figür 1 (Radar Grafikleri)** üzerinden somutlaştırılan **"Aynı VKİ, Farklı Biyolojik Kader"** olgusudur.

Araştırmacılar; **tamamen aynı yaşta, aynı biyolojik cinsiyette ve aynı VKİ değerine sahip** (örneğin hepsi 52 yaşında, kadın ve BMI=32 kg/m2BMI=32 kg/m2) bireylerin 10 yıllık 18 farklı komplikasyon riskini OBSCORE ile modellediklerinde ortaya çıkan tablo şudur:

---

#### A. Hangi Açılardan Benzerler?

1. **Konvansiyonel Sınıflandırma ve Fenotip:**
    - Boy, kilo, yaş ve cinsiyet gibi geleneksel antropometrik ölçümleri tamamen özdeştir. Klasik DSÖ kılavuzlarına göre bu bireylerin hepsi aynı "Evre 1 / Evre 2 Obezite" tanısını alır ve rutin pratikte birbirinin kopyası kabul edilir.
2. **Kilo Verme İlacına (Tirzepatid) Yanıt Kapasitesi:**
    - SURMOUNT-1 klinik çalışma verilerinin analizinde; ister Tip 2 Diyabet riski tepe noktada olsun, ister kardiyovasküler riski, bireylerin farmakoterapi (Tirzepatid) ile **yüzdesel ağırlık kaybı başarıları benzer** bulunmuştur. Yani metabolik riskin yüksek olması kilo vermeye direnç oluşturmamaktadır.
3. **Mekanik / Kütle Temelli Taban Riskler:**
    - Vücut kütlesinin yarattığı fiziksel yük (örneğin eklem içi baskı veya abdominal basınç artışı), benzer kilodaki bireylerde artropati veya hafif diyafram zorlanması için benzer bir taban zemin oluşturmaktadır.

---

#### B. Hangi Açılardan Farklılar? (Morbidite Ayrışması)

Çalışmada incelenen 18 komplikasyon, aynı VKİ'ye sahip bireylerde birbiriyle taban tabana zıt 4 ana eksende ayrışmaktadır:

|Morbidite Ekseni|İncelenen Komplikasyonlar|Bireyler Arasındaki Çarpıcı Fark|
|---|---|---|
|**1. Glukotoksik / Hepatik Eksen**|• Tip 2 Diyabet (T2D)  <br>• MASLD (Yağlı Karaciğer)|**Birey A:** T2D ve MASLD açısından toplumun en üst %10'luk risk diliminde (10. desil) yer alırken; aynı kilodaki **Birey B** 2. desildedir (neredeyse sıfır diyabet riski).|
|**2. Aterosklerotik / Vasküler Eksen**|• Miyokard Enfarktüsü (Kalp Krizi)  <br>• İskemik Kalp Hastalığı  <br>• İnme (Stroke)  <br>• Koroner Ateroskleroz  <br>• KV Mortalite|**Birey B:** Kan şekeri normal olmasına rağmen koroner plak ve kardiyovasküler ölüm riski açısından tepe desildedir. En yüksek riskli %20'lik dilim, en düşüklere göre **47 kat daha fazla kardiyovasküler ölüm riski** taşır.|
|**3. Renal / Pürin / İnflamatuar Eksen**|• Kronik Böbrek Hastalığı (KBH)  <br>• Gut (Ürik Asit Metabolizması)  <br>• Artropati (Eklem Hasarı)|**Birey C:** Kardiyovasküler olay riski düşükken; mikrovasküler renal hasar, hiperürisemi ve gut krizleri açısından izole yüksek risk taşır.|
|**4. Mekanik / Anatomik Eksen**|• Obstrüktif Uyku Apnesi (OSAS)  <br>• GÖRH (Reflü)  <br>• Diyafram Hernisi  <br>• Safra Kesesi Taşı|Yağın anatomik dağılımına (boyun çevresi, üst gövde, intraabdominal) bağlı olarak solunumsal ve üst GİS komplikasyonları kişiden kişiye dramatik biçimde değişmektedir.|

---

### Bu Farklılıkların Patofizyolojik Sebepleri Nelerdir?

1. **Adipoz Doku Fonksiyon Bozukluğu (Adiposopati):**
    - Yağ dokusunu deri altında (subkutan) güvenle depolayabilen bireylerde VKİ 32 olsa dahi organ disfonksiyonu gelişmezken; depo kapasitesi dolup yağ viseral organlara, karaciğere ve kas içine sızan (ektopik yağlanma) bireylerde şiddetli insülin direnci ve MASLD gelişir.
2. **Genetik ve Proteomik Zemin:**
    - 20 parametrelik minimal OBSCORE modelinde yer alan inflamatuar belirteçler, lipid alt fraksiyonları ve hepatorenal biyomarkerlar, organ bazlı yatkınlığı (örneğin endotel hasarı vs. beta-hücre yetmezliği) net şekilde ayırt etmektedir.
3. **BMI 27–30 kg/m2BMI 27–30 kg/m2 Aralığındaki "Gizli Tehlike":**
    - Çalışma, T2D riski en yüksek olan bireylerin **%30'unun aslında obez bile sayılmayan (VKİ 27–30)** kişiler olduğunu göstermiştir. Bu kişiler klasik sistemde "ilaç/tedavi endikasyonu yok" denilerek dışlanırken, aslında en yüksek komplikasyon riskine sahip gruptur.

### Klinik ve Beslenme Bilimi Açısından Özeti

> **Klinik Mesaj:** Klasik VKİ odaklı yaklaşım, hekimi ve diyetisyeni yanıltmaktadır. Aynı kilodaki bir hastanın öncelikli ihtiyacı **agresif kardiyoproteksiyon ve ateroskleroz yönetimi** iken, diğerinin ihtiyacı **hepatik yağlanma ve insülin duyarlılaştırıcı stratejiler**, bir diğerininki ise **renal koruma ve pürin/ürik asit kontrolü**dür. OBSCORE gibi çok boyutlu risk tabakalama modelleri, tedavilerin ve klinik beslenme müdahalelerinin bireyin baskın morbidite riskine göre hedeflenmesini (Precision Nutrition & Medicine) zorunlu kılmaktadır.