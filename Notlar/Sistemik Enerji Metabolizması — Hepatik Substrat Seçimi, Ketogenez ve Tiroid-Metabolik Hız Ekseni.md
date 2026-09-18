---
Tür:
  - Çekirdek
ODAK:
  - "[[Adipoz Doku]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Solunum Katsayısı ve Substrat Oksidasyonu]]"
  - "[[BCAA Dinamikleri ve FGF21 — Açlık-Beslenme Geçişinin Amino Asit Sensörü]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "p < 0.0001"
BESLEDİĞİ NOTLAR:
  - "[[Açlıkta Lipoliz, Ketogenez ve Substrat Partisyonu]]"
  - "[[Solunum Katsayısı ve Substrat Oksidasyonu]]"
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
### İçindekiler

- [[#Hepatik Asetil-CoA Akıbeti Cinsiyete Bağlı TCA-Glukoneogenez Ayrışması]]
- [[#PCK1 ve Glyceroneogenesis Tür Farkı]]
- [[#Sistemik Ketogenez ve BHB Dinamikleri]]
- [[#Enerji Harcaması Substrat Oksidasyonu ve Cinsiyet Farkı]]
- [[#Serbest T3 ve Bazal Metabolik Hızın Baskılanması]]
- [[#Genel Değerlendirme]]
- [[#Bibliyografya]]

---

### Hepatik Asetil-CoA Akıbeti: Cinsiyete Bağlı TCA-Glukoneogenez Ayrışması

Karaciğer, açlıkta organizma-çapında glikoz arzını sürdürmekten sorumlu ana organdır — ama Suchacki et al. (2023)'ün fare verisi, bu organın açlığa **tek bir strateji** ile değil, cinsiyete göre iki farklı biyokimyasal "seçim" ile yanıt verdiğini gösteriyor. Bu ayrım, aynı girdinin (β-oksidasyondan gelen asetil-CoA) iki farklı çıkışa (TCA/OXPHOS vs. glukoneogenez) yönlendirilebileceğinin güzel bir örneği.

**Normal Fizyoloji:** Beslenmiş durumda karaciğer glukoz üretmez, tersine glikojen ve yağ asidi sentezler; asetil-CoA öncelikle lipojenez için kullanılır. Açlıkta bu program tersine döner: β-oksidasyon ile üretilen asetil-CoA iki olası yola girebilir — TCA döngüsü/oksidatif fosforilasyon (enerji üretimi) ya da PC (piruvat karboksilaz) aktivasyonu üzerinden glukoneogenez/ketogenez desteği.

**Açlıkta Ne Değişir:** Suchacki'nin RNA-Seq verisi ve buna eşlik eden plazma keton ölçümleri, CR fareleri arasında net bir cinsiyet ayrışması ortaya koyuyor. **Erkeklerde** CR, karaciğerde TCA döngüsü ve oksidatif fosforilasyon genlerini artırıyor — yani asetil-CoA öncelikle enerji üretimine (ATP) yönlendiriliyor. **Dişilerde** ise TCA/OXPHOS artmıyor; bunun yerine β-oksidasyon kaynaklı asetil-CoA karaciğerde birikiyor. Bu birikim, piruvat karboksilazı aktive ederek glukoneogenezi uyarıyor — ilginç biçimde gluconeogenez-ilişkili genler aslında **her iki cinsiyette de** CR ile artıyor, hatta transkripsiyonel düzeyde erkeklerde biraz daha yüksek görünüyor. Ama yazarların modeline göre asıl belirleyici, mevcut asetil-CoA'nın **nereye harcandığı**: dişilerde biriken asetil-CoA doğrudan piruvat karboksilazı aktive ederken, erkeklerde bu havuz TCA döngüsüne akıtıldığı için glukoneogenik sinyal kadar güçlü bir "itki" oluşturmuyor. Bu modelin dolaylı ama güçlü bir kanıtı plazma keton seviyeleri: hepatik asetil-CoA'nın dolaylı bir biyobelirteci olan plazma ketonlar, CR sırasında dişilerde erkeklerden belirgin şekilde daha yüksek — biriken asetil-CoA'nın bir kısmının ketogeneze de yönlendiğini gösteriyor. Net sonuç: dişiler CR sırasında açlık kan glikozunu erkeklerden daha iyi koruyor, çünkü glukoneogenik sinyalleri (asetil-CoA birikimi üzerinden) daha güçlü.

---

### PCK1 ve Glyceroneogenesis: Tür Farkı

**Normal Fizyoloji:** PCK1 (fosfoenolpiruvat karboksikinaz, sitozolik izoform), glukoneogenezin klasik hız-kısıtlayıcı enzimi olmasının yanında, adipoz dokuda **glyceroneogenesis** için de kullanılır — glukoneogenik substratlardan gliserol-3-fosfat üretimi, lipolizle serbest kalan yağ asitlerinin yeniden esterifikasyonunu (re-esterifikasyon) destekler.

**Açlıkta Ne Değişir:** Defour et al. (2020), bu genin adipoz dokuda **tam ters yönde** düzenlendiğini gösteriyor: farede açlıkla _Pck1_ artarken, insan sWAT'ında **azalıyor**. Yazarlar bunu şöyle yorumluyor: farede glukoz alımı düşük olduğu için glyceroneogenesis (PCK1 üzerinden) devreye giriyor ve yeniden esterifikasyonu destekliyor; insanda ise _PCK1_'in düşmesi, glyceroneogenesis'in bu ölçüde aktive edilmesine gerek olmadığını düşündürüyor — çünkü gliserol-3-fosfat sentezi glukozdan, yani GPD1 üzerinden, zaten yeterli düzeyde sürdürülebiliyor (GPD1 insanda açlıkla değişmezken farede belirgin şekilde düşüyor). Bu iki gen (PCK1, GPD1) birlikte, insan ve fare adipoz dokusunun aynı işlevsel hedefe (re-esterifikasyon için gliserol-3-fosfat temini) **farklı biyokimyasal yollarla** ulaştığını gösteriyor — türler arası "aynı çıktı, farklı yol" örüntüsünün belki de en net örneği.

---

### Sistemik Ketogenez ve BHB Dinamikleri

**Normal Fizyoloji:** Açlıkta karaciğer, artan β-oksidasyon ürünü asetil-CoA'yı, TCA kapasitesinin yetersiz kaldığı noktada keton cisimciklerine (β-hidroksibütirat/BHB, asetoasetat) yönlendirir; bu ketonlar beyin dahil periferik dokular için alternatif yakıt kaynağıdır.

**Açlıkta Ne Değişir:** Üç kaynak da ketogenezi farklı zaman ölçeklerinde belgeliyor ve birlikte okunduğunda **doz-yanıt** benzeri bir eğri ortaya çıkıyor. Defour et al. (2020)'da 16-26 saatlik açlıkta BHB zaten anlamlı şekilde yükseliyor (insan ve farede). Suchacki et al. (2023)'te 6 haftalık %30 CR sırasında dişilerde belirgin şekilde daha yüksek keton seviyeleri gözleniyor (hepatik asetil-CoA birikiminin göstergesi). Cagigas et al. (2025)'te ise 9.8 günlük tam su orucunda BHB **0.6'dan 5±1 mmol/L'ye** sıçrıyor — bu, önceki iki çalışmadaki büyüklüklerden kat be kat daha derin bir ketozis. Bu üç veri noktası bir araya geldiğinde, ketogenezin açlık süresi ve derinliğiyle orantılı, kademeli bir süreç olduğu izlenimi güçleniyor; ancak üç farklı çalışma tasarımı (tür, protokol, ölçüm yöntemi) arasında doğrudan bir doz-yanıt eğrisi çizmek metodolojik olarak temkin gerektirir.

---

### Enerji Harcaması, Substrat Oksidasyonu ve Cinsiyet Farkı

**Normal Fizyoloji:** Toplam enerji harcaması (EE), bazal metabolik hız, termik etki ve fiziksel aktiviteyi kapsar; solunum katsayısı (RER) o anda hangi substratın (karbonhidrat mı yağ mı) tercihen oksitlendiğini yansıtır.

**Açlıkta Ne Değişir:** Suchacki et al. (2023)'ün indirekt kalorimetri verisi, CR'nin ilk haftasında dişilerin erkeklere kıyasla **daha düşük** gündüz, gece ve toplam enerji harcamasına sahip olduğunu gösteriyor — bu fark 3. haftada kayboluyor. Postprandiyal RER'de dişiler >1 değerine erkeklerden daha güçlü ulaşıyor (diyet karbonhidratlarının yağ asidi sentezine yönlendirilmesi, yani lipogenez, dişilerde daha belirgin), ve mutlak yağ oksidasyonu CR ile erkeklerde dişilere göre çok daha güçlü artıyor. Bu üçlü (düşük EE + yüksek postprandiyal lipogenez + düşük yağ oksidasyonu), dişilerin CR'nin ilk haftasında neden kilo/yağ kaybına dirençli olduğunu açıklayan, birbirini tamamlayan üç mekanizma olarak okunabilir.

---

### Serbest T3 ve Bazal Metabolik Hızın Baskılanması

**Normal Fizyoloji:** Tiroid hormonu triiyodotironin (T3), bazal metabolik hızın ana hormonal düzenleyicisidir; enerji arzı kısıtlandığında organizmanın enerji tüketimini azaltarak hayatta kalma süresini uzatan klasik bir adaptif mekanizmadır.

**Açlıkta Ne Değişir:** Cagigas et al. (2025), 9.8 günlük su orucunda serbest T3'ün 3.292'den 2.051 pg/mL'ye düştüğünü gösteriyor (p<0.0001) — ve bu düşüş, plazma BCAA değişimiyle güçlü negatif korelasyon taşıyor (r=-0.65) ve BHB değişimiyle de ilişkili (r=-0.513). Yazarların yorumu: metabolik hızın tiroid-aracılı baskılanması, BCAA salınımı ve ketozis derinliğiyle **senkronize** ilerliyor — yani bu üç eksen (tiroid, amino asit, keton) tek bir koordineli adaptasyonun farklı yüzleri gibi davranıyor. Burada dikkatli olunması gereken bir nokta: bu, Suchacki'nin fare verisindeki "dişilerde düşük EE" bulgusuyla yüzeysel olarak benzer bir tema taşısa da (ikisi de "metabolik hızın düşürülmesi" içeriyor), doğrudan bağlanamaz — biri insan/kronik-açlık/serbest T3 eksenli, diğeri fare/CR/indirekt kalorimetri eksenli; aralarında bir nedensel bağlantı kurmak spekülatif olur, en fazla paralel bir tema olarak not edilebilir.

---

### Genel Değerlendirme

Bu üç kaynak birlikte, süre ekseninde ilginç bir tabloyu ortaya koyuyor: Defour'un 16-26 saatlik akut açlığı ketogenezi başlatıyor ama henüz derinleştirmiyor; Suchacki'nin 6 haftalık kronik %30 CR'si cinsiyete göre ayrışan bir hepatik strateji (TCA vs. glukoneogenez) üretiyor; Cagigas'ın 9.8 günlük tam açlığı ise en derin ketozis ve en belirgin tiroid baskılanmasını gösteriyor. Bu, "açlık süresi arttıkça hepatik substrat seçiminin daha köklü biçimde yeniden programlandığı" şeklinde bir hipotez öne sürmeye izin veriyor — ama üç farklı protokol tipi (tek-seferlik açlık / kronik günlük CR / uzatılmış tam açlık) arasında kontrollü bir karşılaştırma olmadığından bu bir hipotez olarak kalmalı, kanıtlanmış bir doz-yanıt eğrisi değil. Diyet kompozisyonu ekseninde: Suchacki'de CR diyeti izonutrisyon için formüle edilmiş (malnütrisyon önlenmiş standart içerik), Cagigas'ta refeeding bitkisel-ağırlıklı; hiçbiri yüksek-yağ veya yüksek-fruktoz bir arka plan test etmiyor, dolayısıyla "diyet kompozisyonu açlığın hepatik etkisini nasıl güçlendirir/maskeler" sorusu bu kaynaklarla yanıtlanamaz. Cinsiyet ekseninde en somut bulgu Suchacki'den geliyor (TCA vs. glukoneogenez ayrışması) — Cagigas'ın insan kohortu karma cinsiyetli olsa da örneklem gücü (11K/9E) cinsiyet-spesifik tiroid/BCAA etkileşimini test etmeye yetmiyor; bu nedenle Suchacki'nin fare bulgusunun insana genellenip genellenemeyeceği açık bir soru olarak kalıyor.

---

### Bibliyografya

- Suchacki KJ, Thomas BJ, Ikushima YM, et al. (2023). The effects of caloric restriction on adipose tissue and metabolic health are sex- and age-dependent. _eLife_ 12:e88080.
- Defour M, Michielsen CCJR, O'Donovan SD, Afman LA, Kersten S. (2020). Transcriptomic signature of fasting in human adipose tissue. _Physiological Genomics_ 52:451–467.
- Cagigas ML, Santiappillai NT, Commissati S, et al. (2025). The Metabolic Transition Between Fasting and Feeding Alters Aging-Associated Metabolites, Lowers BCAAs, and Stimulates FGF21 Production in Humans. _Aging Cell_ 24:e70270.