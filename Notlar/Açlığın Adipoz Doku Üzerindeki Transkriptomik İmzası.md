---
Tür:
  - Besleyici
ODAK:
  - "[[Adipoz Doku]]"
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: 10.1152/physiolgenomics.00083.2020
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Yağ Dokusu Transkriptopmik Reprogramlanması-Anabolik Yolakların Kapatılması]]"
  - "[[Adipoz Doku Endokrin Fonksiyonu ve Dinamikleri]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Besin Kısıtlaması (Fasting / FMD)"] --> B["İnsülin / IGF-1 Düşüşü & AMPK Artışı"]
>     B --> C["mTORC1 İnhibisyonu & ULK1 Aktivasyonu"]
>     C --> D["Hücresel Otofaji / Mitofaji (Organel Temizliği)"]
>     B --> E["Hepatik Glikojen Boşalması → Ketogenez (Beta-Hidroksibütirat)"]
> ```
>
> **Şekil Açıklaması:** Besin kısıtlaması ve açlık durumunda düşen insülin/IGF-1 ve yükselen AMPK, mTORC1'i inhibe edip ULK1'i aktive ederek hücresel otofaji ve mitofaji (hasarlı organel temizliği) süreçlerini başlatır; eş zamanlı olarak hepatik glikojenin boşalmasıyla ketogenez (Beta-hidroksibütirat üretimi) devreye girer.

**Çalışmanın Amacı ve Yapılma İhtiyacı**
İnsanlık tarihi boyunca açlık (kıtlık), metabolizmamızı şekillendiren en büyük evrimsel baskılardan biri olmuştur. Günümüzde fare, sıçan ve domuz gibi hayvan modellerinde açlığın yağ dokusundaki gen ifadelerini nasıl değiştirdiğine dair pek çok araştırma bulunmasına rağmen, **insan yağ dokusunda (adipoz doku) açlığın gen regülasyonunu nasıl etkilediği literatürde neredeyse hiç bilinmemektedir**. Bu büyük boşluğu doldurmak için çalışmanın **amacı**, insanlarda uzamış açlığın (fasting) deri altı yağ dokusu transkriptomu (tüm gen ifadeleri) üzerindeki etkilerini haritalandırmak ve bu insan verilerini standart laboratuvar farelerindeki (C57Bl/6J) açlık yanıtlarıyla doğrudan kıyaslamaktır.

**Çalışma Kısaca Nasıl Yapıldı? (Metodoloji)**

- **İnsan Çalışması (FASTING Kohortu):** 11 sağlıklı gönüllüye akşam 18:00'de standart bir yemek yedirilmiş, ardından saat 20:00'de (tokluk durumu / yemeğin üzerinden 2 saat geçtikten sonra) deri altı yağ dokusu biyopsisi ve kan örneği alınmıştır. Katılımcılar daha sonra sadece su içerek aç bırakılmış ve ertesi gün saat 20:00'de (açlık durumu / yemeğin üzerinden tam 26 saat geçtikten sonra) ikinci biyopsi ve kan örnekleri alınmıştır.
- **Fare Çalışması (Kıyaslama İçin):** 24 adet fare iki gruba ayrılmış; yarısı serbestçe beslenirken (ad libitum), diğer yarısı 16 saat boyunca aç bırakılmıştır.
- **Zamanlama Stratejisi:** İnsanlardaki 26 saatlik ve farelerdeki 16 saatlik açlık süreleri rastgele seçilmemiştir; bu süreler her iki türde de **karaciğerdeki glikojen depolarının neredeyse tamamen tükendiği (Açlığın 3. Evresi)**kritik metabolik faza denk gelmektedir. Alınan dokular, Affymetrix mikrodizi (microarray) teknolojisiyle tüm genom çapında analiz edilmiştir.

**Primer ve Sekonder Bulgular Nelerdir?**

- **Primer Bulgular (İnsanlarda Kapatılan Şalterler):** Açlık, insan yağ dokusunda devasa bir metabolik yavaşlamaya yol açmıştır. Trigliserit ve yağ asidi sentezi, glikoliz (şekerin parçalanması), glikojen sentezi, TCA döngüsü, oksidatif fosforilasyon, mitokondriyal translasyon ve insülin sinyal yolaklarını yöneten **çok sayıda anabolik gen şiddetli bir şekilde baskılanmıştır (downregulated)**.
- **Sekonder Bulgular (Şaşırtıcı Keşifler):**
    - _Proteazomların Kapatılması:_ Sadece enerji üretim yolları değil, hücrede protein yıkımını sağlayan **"proteazom" genleri de açlık sırasında beklenmedik şekilde kapatılmıştır**.
    - _Kollajen Yıkımı:_ İnsanlarda ve farelerde dokuya yapısal sertlik veren çok sayıda kollajen geni (COL11A1, COL15A1 vb.) açlıkla birlikte anlamlı şekilde baskılanmıştır.
    - _İnsan ve Fare Uyuşmazlığı (Discordance):_ Açlığın fare yağ dokusundaki etkisi, insanlara kıyasla çok daha şiddetlidir. Her iki türde TCA döngüsü ve lipid sentezinin durması gibi "ortak" yanıtlar görülse de (77 ortak artan, 173 ortak azalan gen); **insülin sinyali, PPAR sinyali, glikojen metabolizması ve lipid damlacığı genlerinde (PNPLA2, CIDEC gibi) iki tür arasında birbirine tamamen zıt genetik yanıtlar (farklılıklar) saptanmıştır**. Örneğin, farelerde PCK1 geni (gliseroneogenez için) artarken, insanlarda azalmıştır.

**Bu Bulgular Nasıl Açıklanıyor ve Yorumlanıyor?** Yazarlar, elde ettikleri bu benzersiz hücresel haritayı şu metabolik adaptasyonlarla açıklamaktadır:

- **İnsülinin Düşüşü ve Anabolizmanın Durması:** İnsanlarda açlık sırasında kanda insülinin dramatik şekilde düşmesi; yağ hücresinin yağ ve glukoz alımını, sentezini ve depolanmasını sağlayan genlerini (SREBF1 gibi) kapatmasının ana sebebidir. Hücre enerji tasarrufu moduna geçmiştir.
- **Proteazom Kapatılmasının Sebebi (Enzimleri Korumak):** Hücrenin açlık sırasında protein yıkım (proteazom) genlerini kapatması, lipoliz (yağ yakımı) ve diğer hayati süreçler için hücreye acil olarak gereken **değerli metabolik enzimlerin parçalanıp yok edilmesini önlemek** adına alınan bir güvenlik (tasarruf) önlemidir.
- **Kollajen Düşüşü (Dokunun Fiziksel Küçülmesi):** Açlık sırasında hücrenin içindeki trigliseritler yıkılıp kana karıştıkça (lipoliz), adipositler (yağ hücreleri) fiziksel olarak büzüşür ve küçülür. Kollajen genlerinin baskılanması, dokunun bu "küçülmeye" uyum sağlaması için **kendi iskeletinde (hücre dışı matris) yaptığı esneme ve yapısal yeniden modellenmeyi** yansıtmaktadır.
- **Farelerdeki PCK1 Artışı vs. İnsanlardaki Düşüşü:** Farelerde PCK1 geni, gliserol 3-fosfat üreterek kana salınan yağların yeniden depolanmasını (gliseroneogenez) desteklemek için artar. Ancak insanlarda bunun düşmesi, insan yağ dokusunun açlık sırasında bu alternatif yolağa fareler kadar şiddetli bir ihtiyaç duymadığını (GPD1 enziminin yeterli olduğunu) göstermektedir.

**Sonuçların Önemi ve Klinik/Pratik Çıkarımlar Nelerdir?**

1. **"Fareler İnsan Değildir" Uyarı Sinyali:** Bu çalışmanın bilim dünyası için en büyük ve sarsıcı klinik uyarısı şudur: Obezite ve açlık diyetleri (örneğin Aralıklı Açlık) konusunda **farelerden elde edilen bulguları doğrudan insanlara uyarlamak son derece tehlikelidir.** İki türün yağ dokusundaki insülin, glikojen ve lipoliz (yağ yakım) genleri açlığa karşı çok farklı refleksler göstermektedir.
2. **Gelecek Araştırmalar İçin Rehber Veritabanı:** Bu araştırma, "insan" yağ dokusunun gerçek açlık durumunda nasıl çalıştığını genetik düzeyde haritalandıran eşsiz bir kaynak (resource) sağlamıştır. Diyetisyenlerin ve klinik araştırmacıların gelecekte tasarlayacakları kalori kısıtlaması veya aralıklı açlık tedavilerinde, hücrenin enerjiyi nasıl yönettiğini anlamaları için bir "başvuru kılavuzu" niteliği taşır.