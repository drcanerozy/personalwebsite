---
Tür:
  - Besleyici
ODAK:
  - "[[Adipoz Doku]]"
MEKANİZMA:
  - "[[AMPK]]"
DİZİN:
  - "[[Weight Cycling]]"
  - "[[Kilo Geri Kazanımı]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[AMPK–TBK1 Resiprokal Frenleme Devresi Adiposit Kataboliz Kontrolü]]"
  - "[[İnsülin–IRF4 Ekseni Açlıkta Yağ mı Kas mı Kaybedilir?]]"
  - "[[Otofaji]]"
  - "[[Kilo Döngüsü ve İmmün Hafıza]]"
  - "[[Hiperinsülinemi Açlık için Bir Fren Olabilir!]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM: "AMPK-TBK1 mekanizmasının popüler anlatımı. İkili ilaç kombinasyonu (Amlexanox+AICAR) bulguları klinik çalışma fikri için çıkış noktası."
KAYNAK: https://doi.org/10.1172/jci.insight.200168
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Adipoz Doku Lipolizi]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Enerji Kısıtlaması / Açlık"] --> B["AMPK Aktivasyonu"]
>     B -->|Katabolik Sinyal| C["Lipoliz ve Yağ Oksidasyonu"]
>     B -->|Geri Bildirim| D["TBK1 İndüksiyonu"]
>     D -.->|İnhibisyon / Fren| B
>     E["Kronik Düşük Dereceli İnflamasyon"] -->|Sürekli Yüksek| D
> ```
>
> **Şekil Açıklaması:** Enerji kısıtlaması veya açlıkta aktive olan AMPK, lipoliz ve yağ oksidasyonunu uyarırken aynı zamanda TBK1 indüksiyonunu tetikleyerek negatif bir geri bildirim freni oluşturur; kronik düşük dereceli inflamasyon varlığında ise TBK1 sürekli yüksek kalarak AMPK'yi baskılar ve katabolik yağ yıkımını kilitler.

Bu çalışma (Wisessaowapak ve ark., 2026), obezitede hücresel enerji harcamasının neden tıkandığını ve diyet yapıldığında vücudun "kilo vermemek için" nasıl direndiğini moleküler düzeyde inceleyen çok çarpıcı bir araştırmadır.

Önceki konuşmalarımızdaki AMPK (açlık/enerji sensörü) ve hücresel adaptasyon kavramlarını tam merkeze alan bu çalışmanın amacı, hipotezleri ve bulguları aşağıda detaylandırılmıştır:

### 1. Çalışmanın Amacı Ne?

Obezitede veya kalori kısıtlamasında vücudun enerji harcamasını kısarak kendini korumaya aldığı "metabolik adaptasyonun" arkasındaki moleküler fren mekanizmalarını çözmektir. Özellikle bağışıklık ve iltihapla ilişkili olduğu bilinen **TBK1 (TANK binding kinase 1)** enziminin, besin stresi (açlık) altında adipositlerde (yağ hücrelerinde) AMPK sinyalini nasıl baskıladığını (nasıl bir fren görevi gördüğünü) ve bu frenin kaldırılarak metabolik esnekliğin yeniden kazanılıp kazanılamayacağını araştırmayı amaçlamıştır.

### 2. Araştırmanın Hipotezleri

- **Açlık Freni Hipotezi:** Açlık sırasında yağ yakımını başlatan AMPK aktive olduğunda, enerji depolarının tamamen tükenmesini engellemek için kendi kendini sınırlayan bir geribildirim mekanizması olarak TBK1'i uyarır. TBK1 ise yükseldiğinde AMPK'yı baskılayarak "fren" yapar ve aşırı enerji harcamasını engeller.
- **Obezitede Kilitlenme Hipotezi:** Obezite durumunda, dokudaki kronik iltihaplanma nedeniyle TBK1 zaten sürekli (bazal olarak) yüksek seviyelerdedir. Bu yüksek TBK1, AMPK'yı sürekli baskılayarak "frenin takılı kalmasına" neden olur ve açlık/diyet durumunda yağ yakımını engeller.
- **Çift Yönlü Tedavi (Sinerji) Hipotezi:** Eğer farmakolojik olarak AMPK aktive edilirken aynı anda TBK1 freni de bir ilaçla kapatılırsa (çift yönlü müdahale), bu kilitlenme aşılabilir ve obez farelerde yağ yakımı, insülin duyarlılığı ve kilo kaybı çok daha güçlü bir şekilde sağlanabilir.

### 3. Çalışma Kısaca Nasıl Yapılmış?

- **Deney Modelleri:** Çalışmada standart diyetle beslenen zayıf fareler ve Yüksek Yağlı Diyet (HFD - %60 yağ) ile obez edilmiş fareler kullanılmıştır. Ayrıca yağ hücrelerinde TBK1, AMPK veya PGC1α genleri özel olarak silinmiş (Genetik Knockout - KO) fareler üretilmiştir.
- **Uygulamalar:** Farelere 24 ile 72 saat arası açlık (fasting) uygulanmış veya AMPK'yı uyaran ilaçlar (AICAR) verilmiştir.
- **İkili İlaç Kombinasyonu (Tedavi):** Obez farelere 21 gün boyunca sadece TBK1 inhibitörü (Amlexanox), sadece AMPK aktivatörü (AICAR) veya **ikisi birden (Amlexanox + AICAR)** verilerek kilo, glikoz toleransı ve doku değişimleri ölçülmüştür. Ayrıca laboratuvar ortamında 3T3-L1 hücreleriyle (insan ve fare hücreleri) moleküler doğrulamalar yapılmıştır.

### 4. Primer (Birincil) Bulguları

- **Frenin Keşfi (AMPK/PGC1α/NRF1 Ekseni):** Açlık durumunda AMPK aktive olduğunda, genetik bir kod (PGC1α/NRF1 ekseni) üzerinden doğrudan _Tbk1_ üretimini tetikler. Yani hücre yağ yakarken, enerjisi bitip ölmesin diye kendi frenini (TBK1) kendi üretir.
- **Obezitede Dengenin Bozulması:** Zayıf farelerde açlık AMPK'yı çok iyi uyarırken, obez farelerde (ve obez insanların biyopsi örneklerinde) hücrelerdeki TBK1 iltihap nedeniyle zaten çok yüksek olduğu için AMPK aktivasyonu başarısız olmuş, diyet (açlık) sırasında yağ dokusunda beklenen adaptasyon ve kilo kaybı körelmiştir.
- **İkili Tedavi (Kombinasyon) Başarısı:** TBK1 inhibitörü (Amlexanox) ve AMPK aktivatörü (AICAR) birlikte verildiğinde (kombinasyon tedavisi), fareler tek başlarına ilaç alanlara kıyasla devasa bir sinerji göstermiştir. Kilo kaybı artmış, glikoz toleransı düzelmiş, insülin seviyeleri düşmüş ve karaciğerdeki yağ birikimi mükemmel şekilde temizlenmiştir.

### 5. Sekonder (İkincil / Hücresel) Bulguları

- **Makrofaj (İltihap) İşgalinin Temizlenmesi:** Daha önceki konuşmalarımızda obez yağ dokusunun makrofajlarla (taç benzeri yapılar - CLS) işgal edildiğinden bahsetmiştik. İkili kombinasyon tedavisi (Amlexanox + AICAR), yağ dokusundaki bu makrofaj işgalini ve iltihaplı yapıları neredeyse tamamen ortadan kaldırmış, hücreleri küçülterek metabolik olarak sağlıklı adipositlere dönüştürmüştür.
- **Karaciğerdeki Çok Yönlü İyileşme (Katabolik Esneklik):** Kombinasyon tedavisi sadece yağları eritmekle kalmamış; karaciğerde doku sertleşmesine yol açan fibrozis genlerini (_Col1a1, Timp1_), Endoplazmik Retikulum (ER) stresini ve inflamatuar markörleri (_Tnfα, Ccl2_) ciddi oranda baskılamıştır. Karaciğer ve yağ dokusunda insülin duyarlılığı (Akt fosforilasyonu üzerinden) tam olarak onarılmıştır.
- **Genetik TBK1 Silinmesinin Etkisi (Mitochondrial OXPHOS):** Yağ hücrelerinden TBK1 geni tamamen silindiğinde (Tbk1AKO fareler), açlık sırasında AMPK üzerinde hiçbir fren kalmadığı için yağ hücreleri mitokondriyal kapasitelerini (OXPHOS kompleksleri) devasa oranda artırmış ve kandaki yağ yakım ürünlerini (NEFA ve gliserol) yükseltmiştir. Kas kütlesi (lean mass) korunurken, yağ kütlesi (fat mass) hızla erimiştir.
- **TBK1'in Benzersiz Karakteri:** Çoğu iltihap enzimi sadece enfeksiyon/bağışıklık sinyaliyle çalışırken, TBK1'in hem "besin fazlalığında (obezite)" hem de "besin azlığında (açlık)" katabolizmayı (yıkımı) durduran çift yönlü, nadir bir "enerji koruma sensörü" olduğu kanıtlanmıştır.

### **Gıda Alımından Bağımsız İyileşmenin İspatı 

Araştırmacılar yağ dokusundaki bu kilidi kırmak için TBK1 inhibitörü (Amlexanox) ve AMPK aktivatörünü (AICAR) birlikte uygulamışlardır. Buradaki en kritik bilimsel detay şudur: İlaç tedavisi alan farelerin iştahı azalıp daha az yemek yedikleri için, araştırmacılar ilaç verilmeyen HFD (Yüksek Yağlı Diyet) kontrol grubundaki fareleri "pair-fed" (eş beslemeli) olarak diyet kısıtlamasına sokmuşlar ve her iki grubun yediği gıda (kalori) miktarını eşitlemişlerdir.

**3. Kalori Aynı Olmasına Rağmen Görülen Devasa Fark** Her iki grup da aynı oranda kısıtlı kalori almasına rağmen:

- Sadece ilaç kombinasyonu (TBK1 baskılaması + AMPK uyarımı) alan grupta yağ hücreleri sağlıklı boyutlara küçülmüş ve esnekliğini geri kazanmıştır.
- Yağ dokusunu işgal eden iltihaplı makrofajlar (taç benzeri yapılar - CLS) neredeyse tamamen ortadan kalkmıştır.
- Dokunun insüline verdiği yanıt (Akt fosforilasyonu) tamamen onarılmıştır. Yazarlar, vücut ağırlığı kaybının, glikoz toleransındaki iyileşmenin ve yağ dokusundaki inflamasyonun azalmasının **gıda alımından (kaloriden) bağımsız olarak (independent of food intake)** gerçekleştiğini tartışma bölümlerinde açıkça vurgulamışlardır