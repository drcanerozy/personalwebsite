---
Tür:
  - Besleyici
ODAK:
  - "[[Obezite]]"
MEKANİZMA: "[[Adipoz Doku]]"
DİZİN: "[[Beden Kütle İndeksi]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Farklı Obezite Fenotipleri]]"
  - "[[Obezite Tanısında EASO 2024 Yaklaşımı]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[BMI- An Overvalued Treasure]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: https://doi.org/10.1016/j.ebiom.2026.106272
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Obezite Tanısında EASO 2024 Yaklaşımı]]"
  - "[[Obezite Tanısında ABCD Yaklaşımı]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["Adipoz Doku Kapasitesi Aşılması"] --> B["Viseral Yağ Birikimi (↑ Bel Çevresi)"]
>     A --> C["Artmış Vücut Yağ Yüzdesi (↑ BF%)"]
>     B --> D["Ektopik Yağ: Karaciğer / Pankreas / Kas"]
>     D --> E["Proinflamatuvar Adipokin: IL-6, TNF-α, Leptin ↑"]
>     E --> F["İnsülin Direnci & Kronik İnflamasyon"]
>     C --> F
>     F --> G["T2D Riski ↑ 9.23x | KBH ↑ 2.27x | 3P-MACE ↑ 1.63x"]
>     H["Normal BMI — gerçekte Grup 5 olanlar: %32.6"] -.->|"BMI Yanılsaması"| G
> ```
>
> **Şekil Açıklaması:** BF% ve bel çevresi kombinasyonu, viseral ve ektopik yağ birikiminin yol açtığı proinflamatuvar-insülin direnci döngüsünü BMI'a göre çok daha doğru yansıtır; normal BMI'a sahip bireylerin %32.6'sının en yüksek risk grubunda yer alması, ölçüm yanlılığının klinik sonuçlarını somutlaştırır.

Bu araştırma, obeziteyi sadece tartıdaki ağırlıkla değil, yağın vücuttaki miktarı ve dağılımıyla ölçen yepyeni bir sınıflandırma sistemini klinik olarak doğrulayan tarihi bir çalışmadır. Detayları şu şekildedir:

### 1. Çalışmanın Amacı ve Hipotezleri Nelerdir?

- **Çalışmanın Amacı:** Lancet Diyabet ve Endokrinoloji Komisyonu'nun "Obezite, sadece yüksek kilo değil, fazla yağlanma (adipozite) hastalığıdır" şeklindeki yeni yaklaşımını test etmektir. Bu doğrultuda; **Vücut Yağ Yüzdesi (BF%) ile Bel Çevresini (WC) birleştiren adipozite tabanlı yeni bir sınıflandırma sisteminin**, kardiyometabolik hastalıklar ve böbrek hastalıkları riskini ne kadar doğru tahmin edebildiğini kanıtlamak ve bu sistemi geleneksel BMI ile karşılaştırmaktır.
- **Çalışmanın Hipotezi:** Sadece boy ve kiloya dayanan BMI, kas kütlesi ile biyolojik olarak aktif ve riskli olan "yağ dokusunu" birbirinden ayıramaz ve yağın vücutta nereye dağıldığını gösteremez. Araştırmacılar, vücut yağ yüzdesi (toplam yağ) ve bel çevresi (yağ dağılımı/merkezi yağlanma) birleştirilerek yapılan bir teşhisin, obeziteye bağlı hastalık risklerini (kalp krizi, diyabet, böbrek yetmezliği) BMI'dan çok daha isabetli öngöreceğini hipotez etmişlerdir.

### 2. Çalışma Kısaca Nasıl Yapılmış? (Metodoloji)

- **Devasa Bir Kohort:** Çalışma, İngiltere Biobank (UKB) veritabanındaki 40-69 yaş arası tam **489.311 katılımcının**verileriyle yapılmış ve hastalar ortalama **13.1 yıl boyunca** (uzunlamasına/longitudinal) takip edilmiştir.
- **Yeni Sınıflandırma Matrisi:** Araştırmacılar hastaları BMI ile değil; Vücut Yağ Yüzdesi (BF%) ve Bel Çevresi (WC) ölçümlerini içeren 3x3'lük bir matris kullanarak sınıflandırmışlardır. Bu eşleştirmeyle hastalar 5 farklı risk grubuna ayrılmıştır (Grup 1: Risksiz, Grup 5: Çok Yüksek Riskli).
- Araştırmacılar, bu matrisi oluşturmak için cinsiyete özgü uluslararası (Dünya Sağlık Örgütü ve literatür fikir birliğine dayalı) belirli eşik değerleri (cut-off) kullanmışlardır. Matrisin altyapısını oluşturan değerler şunlardır:

- **Vücut Yağ Yüzdesi (BF%) Sınırları:** Kadınlarda %30 ve %35; erkeklerde ise %20 ve %25 eşik değer olarak alınmıştır. _(Bu ölçümler için çoğunlukla biyoelektrik empedans analizi (BIA) verileri kullanılmıştır__)._
- **Bel Çevresi (WC) Sınırları:** Kadınlarda 80 cm ve 88 cm; erkeklerde ise 94 cm ve 102 cm eşik değer olarak kabul edilmiştir.

Bu iki ölçümün düşük, orta ve yüksek değerlerinin birbiriyle kesiştirilmesi sonucunda toplamda **9 farklı adipozite (yağlanma) fenotipi** ortaya çıkmıştır.

Daha sonra araştırmacılar, elde edilen bu 9 fenotipi klinik olarak daha kullanışlı hale getirmek için bir **"trafik lambası şeması (traffic-light schema)" kullanarak 5 ana risk grubuna (Grup 1'den Grup 5'e) birleştirmişlerdir**:

- **Grup 1 (Risksiz / Yeşil):** Hem vücut yağ yüzdesi hem de bel çevresi belirlenen en alt eşiklerin altında olan sağlıklı bireyler.
- **Grup 2 (Hafif Artmış Risk):** Yağ yüzdesi veya bel çevresinden sadece birisi orta seviyede artmış olanlar.
- **Grup 3 (Artmış Risk):** Her iki ölçümde de orta seviyelere doğru ilerleyen risk profili.
- **Grup 4 (Yüksek Risk):** Ölçümlerden en az birinin tehlike sınırını aştığı grup.
- **Grup 5 (Çok Yüksek Risk / Kırmızı):** Hem vücut yağ yüzdesi (kadınlarda %35'in, erkeklerde %25'in üzerinde) hem de bel çevresi (kadınlarda 88 cm'in, erkeklerde 102 cm'in üzerinde) **en üst sınırları aşmış olan** en tehlikeli grup
- **Klinik Takip (Sonlanımlar):** Bu 5 grubun 13 yıl boyunca Tip 2 Diyabet (T2D), Kronik Böbrek Hastalığı (CKD) ve 3-Noktalı Majör Olumsuz Kardiyovasküler Olay (3P-MACE: ölümcül olmayan kalp krizi, inme ve kardiyovasküler ölüm) geçirip geçirmedikleri analiz edilmiştir.

### 3. Primer ve Sekonder Bulgular Nelerdir?

**Primer (Birincil) Bulgular: BMI'ın Çöküşü**

- **Kusursuz Risk Tahmini:** BF%-WC risk grupları arttıkça hastalık riskleri merdiven gibi kusursuz şekilde artmıştır. En sağlıklı olan Grup 1'e kıyasla, adipozitesi en kötü olan Grup 5'teki bireylerin **Tip 2 Diyabet riski 9.23 kat, kronik böbrek hastalığı riski 2.27 kat ve kalp-damar olayları riski 1.63 kat daha yüksek** bulunmuştur.
- **Şok Edici BMI Uyumsuzluğu (Discordance):** Çalışmanın en can alıcı bulgusu şudur: Yağ oranı ve bel çevresi açısından en tehlikeli grupta (Grup 5) yer alan bireylerin **%32.6'sının (neredeyse üçte birinin) BMI değerleri "Normal veya Fazla Kilolu" aralığında** çıkmıştır. Yani BMI'a göre obez olmayan yüz binlerce insan aslında çok yüksek riskli obez adipoziteye sahiptir. Öte yandan BMI'a göre "Fazla Kilolu" kategorisinde yer alan bireylerin, yağ-bel haritasındaki 5 risk grubunun hepsine dağıldığı görülmüştür (Yani her fazla kilolu aslında metabolik olarak riskli değildir).

**Sekonder (İkincil) Bulgular: Gizli Tehlikeler**

- **Normal Kilolu ama Yüksek Riskli Olanlar:** Sadece "Normal" bir BMI aralığında olmalarına rağmen, yeni matriksle yüksek adipozite riski (Grup 5) taşıdığı tespit edilen bireylerin; sağlıklı adipoziteye sahip olanlara kıyasla kalp hastalığı (3P-MACE) riskinin %45, böbrek yetmezliği (CKD) riskinin %58 ve **Diyabet (T2D) riskinin tam 4.24 kat daha yüksek** olduğu saptanmıştır.
- **Gençlerde Tehlike Daha Büyük:** Yaş stratifikasyonu yapıldığında, yüksek yağ oranı ve bel çevresinin Tip 2 Diyabet tetikleme gücü, genç bireylerde (<60 yaş) yaşlılara göre çok daha şiddetli bulunmuştur.

### 4. Bu Bulgular Nasıl Açıklanıyor ve Tartışılıyor?

Yazarlar bu tabloyu, önceki konuşmalarımızda sıkça değindiğimiz **"Yağ Dokusunun Disfonksiyonu"** üzerinden harika bir sistem mühendisliğiyle tartışmışlardır:

- **Sorun Tartıdaki Kilo Değil, Visseral Yağdır:** Bel çevresinin (WC) bu çalışmada bu kadar başarılı bir risk belirleyicisi olması, onun **"Visseral Yağ Doku" (İç organ yağlanması)** için bir ayna (proxy) olmasından kaynaklanmaktadır. Visseral yağ dokusu genişlediğinde (BMI normal bile olsa), ektopik yağ birikimi başlar, hücreler kana pro-inflamatuar (iltihaplı) ajanlar salgılar ve insülin duyarlılığı bozulur. Bu nedenle adipozite sınıflandırması, diyabeti BMI'dan çok daha iyi öngörmüştür.
- **Yağ ve Kas Ayrımı:** BMI'ın çökme nedeni, kas ile yağı ayıramamasıdır. Özellikle ilerleyen yaşlarda kas kütlesi azalırken yağ kütlesi arttığı için (sarkopenik obezite), kişinin kilosu (BMI) normal kalsa da hücresel ve metabolik olarak hastalık riski tavan yapmaktadır.

### 5. Sonuçların Önemi ve Klinik Çıkarımlar Nelerdir?

- **Obezitenin Tanımı Resmen Değişiyor:** Bu çalışma, obezite tanımında sadece boy ve kilo kullanmanın klinik bir hata olduğunu ve yüz binlerce yüksek riskli hastanın sırf "BMI'ları düşük diye" gözden kaçırıldığını net olarak kanıtlamaktadır. Obezite bir "kilo" hastalığı değil, bir "adipozite" (yağlanma) hastalığıdır.
- **Tedavide Önceliklendirme ve İlaç Kullanımı:** Zayıflama ilaçlarının (anti-obezite terapileri) veya bariatrik cerrahilerin kimlere uygulanacağı artık sadece BMI ile belirlenmemelidir. Bir hastanın BMI değeri 27 (sadece fazla kilolu) olabilir, ancak Vücut Yağ Yüzdesi ve Bel Çevresi Grup 5'teyse, bu kişi BMI'ı 35 olan ama Grup 3'te yer alan birinden çok daha acil tedaviye ihtiyaç duyuyor demektir.
- **Klinik Pratik İçin Diyetisyen Vizyonu:** Diyetisyenler ve hekimler için en büyük çıkarım şudur: Kliniğe giren hastanın BMI'ı "Normal veya Fazla Kilolu" çıktığında rehavete kapılınmamalıdır. **Bel çevresi ve biyoelektrik empedans (BIA) ile ölçülen yağ yüzdesi**, metabolik riski değerlendirmek için vazgeçilmez "tamamlayıcı tarama araçları" olarak kullanılmalıdır.