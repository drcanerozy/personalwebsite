---
Tür:
  - Besleyici
ODAK:
  - "[[MCT]]"
MEKANİZMA:
DİZİN:
  - "[[Ketojenik Diyet]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Ketojenik Diyet ve Enerji Kısıtlaması İlişkisi]]"
  - "[[Sistemik Enerji Metabolizması — Hepatik Substrat Seçimi, Ketogenez ve Tiroid-Metabolik Hız Ekseni]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[Diyet İlkeleri ve Popüler Diyetler]]"
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Açlıkta Lipoliz, Ketogenez ve Substrat Partisyonu]]"
  - "[[Düşük KH Diyetlerin T2DM'deki Evrimi]]"
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

1. MCT'lerin Tanımı ve Temel Rolü

Orta zincirli trigliseritler (MCT'ler), geleneksel bir ketojenik diyete veya uzun süreli açlığa gerek kalmadan **ketozisi indükleyebilen**ticari olarak temin edilebilen, ucuz diyet takviyeleridir.

• **Potansiyel Fayda:** MCT'lerin, Alzheimer hastalığı gibi nörodejeneratif hastalıkların ilerlemesini marjinal düzeyde geciktirme potansiyeli bulunmaktadır. Bu, beyin fonksiyonlarında düşüşün bir nedeni olan **glikoz hipometabolizmasını** telafi etmek için ketonların (βHB ve asetoasetat) alternatif bir enerji kaynağı olarak kullanılabilmesiyle ilişkilidir.

• **BHB'nin Rolü:** Ketonlardan biri olan Beta-hidroksibütirat (βHB), kalori kısıtlamasında gözlemlenen yaşlanma karşıtı etkiler gibi sağlık faydalarına sahiptir.

2. Ketojenik Etkinin Kaynağı ve Tutarsızlıklar

MCT'lerin ketojenik etkisi üzerindeki çalışmalar, doz-yanıt ilişkisi ve bileşenlerin etkisi açısından tutarsızlıklar göstermiştir.

A. En Önemli Ketojenik Bileşen

MCT'lerin majör ketojenik bileşeni **Kaprilik Asit (C8)** olup, bunu Kaprik Asit (C10) veya Laurik Asit (C12) takip eder.

• **Zincir Uzunluğunun Etkisi:** C8'in ketojenik etkisi, C10'dan üç, C12'den ise altı kat daha yüksektir. Vandenberghe ve ark. tarafından yapılan bir çalışma, C8 tüketiminden sonra yaklaşık 4 saat boyunca toplam plazma keton konsantrasyonunun arttığını, ancak C10 tüketiminden sonra artmadığını göstermiştir.

• **Mekanizma:** Yalnızca 8 veya daha az karbon zincir uzunluğuna sahip yağ asitleri, mitokondrinin iç zarını **karnitin palmitoil transferaz I'den bağımsız** olarak geçebilir. C8'in C10 ve C12'den daha güçlü bir ketojenik etkiye sahip olmasının nedeni bu olabilir.

B. Dozaj Tutarsızlıkları

Bazı eski incelemeler, MCT dozları 70 g'a kadar çıktığında maksimum plazma βHB konsantrasyonu arasında neredeyse **doğrusal bir ilişki**olduğunu öne sürmüştür. Ancak makale, bu eski analizlerin, çalışmalara sağlıklı yetişkinlerin yanı sıra hafıza sorunları olan yetişkinleri ve diyabet hastalarını dahil etmesi, sadece C8 yerine tüm MCT'lerin (C6, C8, C10, C12) toplam dozunu kullanması ve yemek eşlik edip etmediği gibi faktörleri dikkate almaması nedeniyle sorunlu olduğunu belirtmektedir.

Daha yeni bulgular, MCT alımı ile plazma keton konsantrasyonu arasındaki doğrusal olmayan ilişkinin nispeten düşük dozlarda (10–20 g) başlayabileceğini göstermektedir.

3. Ketojenik Etkiyi Optimize Eden Faktörler

Mevcut literatüre dayanarak, MCT'lerin ketojenik etkisini optimize etmek ve istenmeyen yan etkileri (özellikle gastrointestinal rahatsızlık ve ishal) azaltmak için dört pratik tavsiye sunulmuştur:

|   |   |
|---|---|
|Etkileşen Faktör|Bulgular ve Optimizasyon|
|**Dozaj**|**Başlangıç dozu** olarak 5 g C8 veya 5 g C8 + C10 kombinasyonu ile başlanmalı. Bu doz, kademeli olarak **15–20 g C8'e** yükseltilmelidir. Norgren ve ark., potansiyel yan etkileri en aza indirmek için C8 dozunun alım başına 15-20 g ile sınırlandırılmasını önermiştir.|
|**Öğün Eşlik Etmesi**|MCT'lerin yanında **karbonhidrat içeren bir öğün olmadan** tüketilmesi daha güçlü bir ketojenik etki yaratır. Örneğin, 20 g C8'e 50 g glikoz eklenmesi ketojenik etkiyi %63 oranında azaltmıştır. Karbonhidrat tüketimini takiben MCT tüketiminin ketojenik etkiyi baskıladığı da gösterilmiştir.|
|**Açlık Süresi**|MCT'ler, **gece boyunca açlık sonrası**tüketilmelidir. Daha uzun açlık süreleri (16 veya 24 saat), MCT'lerin tek bir dozundan sonra daha büyük ketojenik yanıtlarla sonuçlanır.|
|**Kafein Tüketimi**|Kafeinin MCT'ler ile birleştirilmesi, ketojenik etkiyi **hafifçe artırabilir**.|
|**Emülsifikasyon**|MCT'lerin içeceklerle **emülsifiye edilmesi**, aynı dozda emülsifiye edilmemiş MCT'lere kıyasla ketojenik etkilerini artırabilir ve yan etkileri hafifletebilir.|

4. Yan Etkiler ve Direkt Nöral Fonksiyonlar

MCT'ler 1 g/kg'a kadar dozlarda güvenli olsa da, **gastrointestinal rahatsızlık** ve **ishal** gibi yaygın yan etkiler ortaya çıkabilir. Yan etkileri azaltmak için düşük dozla başlanması ve emülsifikasyon önerilmektedir.

Makale, ayrıca MCT'lerin (C8 ve C10) **keton metabolitlerinin etkilerinin ötesinde** doğrudan nöral fonksiyonları iyileştirdiğini belirtmektedir:

• **C8:** Pro-opiomelanokortin nöronlarının aktivitesini etkileyerek enerji dengesini düzenler.

• **C10:** SIRT1 enzimini aktive ederek nöronlarda mitokondriyal fonksiyonu iyileştirir ve mTOR'u inhibe ederek astrosit fonksiyonunu düzenler.

• **C8 ve C10 Ortak Etkisi:** Her ikisi de glutamin tedarikini artırarak nöronlarda GABA sentezini artırır.

Sonuç olarak, makale, önceki çalışmalardaki tutarsızlıkları açıkça belirlemiş ve MCT'lerin nörolojik faydalarını maksimize etmek için **dozajın, zamanlamanın (açlık sonrası) ve tüketim şeklinin (düşük karbonhidratlı öğün veya tek başına)** kritik olduğunu vurgulayan pratik öneriler sunmuştur.

