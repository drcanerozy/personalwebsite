---
Tür:
  - Besleyici
ODAK:
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
  - "[[Sistemik Enerji Metabolizması — Hepatik Substrat Seçimi, Ketogenez ve Tiroid-Metabolik Hız Ekseni]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Kas Proteolizi ve Substrat Partisyonu"
p_value_summary: "p < 0.001"
BESLEDİĞİ NOTLAR:
  - "[[Açlıkta Lipoliz, Ketogenez ve Substrat Partisyonu]]"
  - "[[Sistemik Enerji Metabolizması — Hepatik Substrat Seçimi, Ketogenez ve Tiroid-Metabolik Hız Ekseni]]"
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

> **Metodolojik Etiketler:** #finding/contradictory
### İçindekiler

- [[#Açlıkta BCAA Salınımı ve Doku Kaynakları]]
- [[#Refeedingde BCAA Çöküşü ve İnsülin Aracılı Doku Alımı]]
- [[#FGF21 Tür Farkı Paradoksu]]
- [[#Genel Değerlendirme]]
- [[#Bibliyografya]]

> **Not:** Bu notun refeeding-ağırlıklı kısımları, ayrı yürüttüğün refeeding-odaklı derlemenle örtüşüyor olabilir — burada mekanizmanın bütünü (açlık + refeeding) tek parça olarak sunuluyor; senteze geçerken ilgili kısmı oradan çekebilirsin.

---

### Açlıkta BCAA Salınımı ve Doku Kaynakları

Dallı zincirli amino asitler (BCAA: Valin, Lösin, İzolösin), açlık fizyolojisinde uzun süredir "kas yıkımının belirteci" olarak basitleştirilen ama aslında çok daha katmanlı davranan bir amino asit grubudur. Cagigas et al. (2025)'in 10 günlük insan verisi, bu basitleştirmenin yanıltıcı olduğunu gösteriyor.

**Normal Fizyoloji:** Beslenmiş durumda BCAA'lar öncelikle iskelet kasında katabolize edilir (BCAA aminotransferaz ve dehidrogenaz kompleksi üzerinden); bu katabolizma insülin tarafından baskılanır, yani insülin varlığında BCAA'lar dokuda tutulur/kullanılır, dolaşıma net salınım olmaz.

**Açlıkta Ne Değişir:** Beklenenin aksine, ölçülebilen 18 amino asitin çoğu (12 tanesi) açlıkla homojen biçimde **azalırken**, BCAA'lar farklı davranıyor: metiyonin, prolin, lösin ve valin **değişmiyor**; izolösin ise **anlamlı şekilde artıyor**. Yazarlar bunu, kalp ve iskelet kasında BCAA katabolizmasının azaltılması ve karaciğer ile kas dokusundan dolaşıma **net BCAA salınımı** ile açıklıyor — yani açlık, BCAA'ları "yakıt olarak tüketmek" yerine, dolaşımda **tutmayı/serbest bırakmayı** tercih ediyor gibi görünüyor. Bu yorum, daha önceki hayvan (Holecek et al. 2001, sıçanlarda 3 günlük açlıkta korunan/artan BCAA, azalmış kalp/iskelet kası katabolizmasına ve karaciğerden net salınıma bağlanmış) ve insan (Fryburg et al. 1990, 60 saatlik açlıkta önkoldan net lösin salınımının 2-3 kat artması) çalışmalarıyla uyumlu. Bu stabil BCAA profili, Serbest T3 ve Bazal Metabolik Hızın Baskılanması başlığında ele alınan tiroid baskılanmasıyla güçlü negatif korelasyon taşıyor (r=-0.65) — metabolik hızın düşürülmesi ile BCAA'nın korunması senkronize bir adaptasyon gibi işliyor. Önemli bir negatif bulgu: açlık fazında BCAA dalgalanmaları **glikoz, insülin, FGF21, leptin, adiponektin veya kortizol ile ilişkili değil** — yani bu regülasyon, klasik metabolik hormonların dışında, öncelikle tiroid ekseniyle bağlantılı görünüyor.

---

### Refeeding'de BCAA Çöküşü ve İnsülin Aracılı Doku Alımı

**Normal Fizyoloji:** Beslenmenin başlamasıyla insülin yükselir; insülin, iskelet kasında amino asit taşıyıcılarını aktive ederek dolaşımdaki amino asitlerin (özellikle BCAA'ların) hızla kasa alınmasını sağlar (Saltiel & Kahn 2001; Huang & Czech 2007).

**Açlıkta Ne Değişir (Refeeding Fazı):** Açlıkta stabil kalan BCAA'lar, refeeding'de beklenmedik ve çarpıcı bir tersine dönüş gösteriyor — valin -%45, lösin -%52, izolösin -%48 (hepsi p<0.001), yani **bazal seviyenin de altına** düşüyor. Bu düşüş, yükselen insülin ile korele (r=-0.57); insülin değişimi ayrıca metiyonin (r=-0.63), lösin (r=-0.59), fenilalanin (r=-0.55) ve valin (r=-0.51) ile de güçlü negatif korelasyon gösteriyor — burada metiyonin ve fenilalaninin BCAA olmadığını, yalnızca insülin ile en güçlü korele olan amino asitler arasında yer aldıklarını not etmek gerekir. Yazarlar bu düşüşü insülin-aracılı doku alımı ile **tutarlı** buluyor, ama korelasyonun nedensellik ifade etmediğini özellikle vurguluyor.

---

### FGF21: Tür Farkı Paradoksu

**Normal Fizyoloji:** FGF21, karaciğer kaynaklı bir hepatokindir; lipid, glukoz ve enerji metabolizmasını düzenler, glukoz alımını artırır, insülin duyarlılığını iyileştirir ve lipid oksidasyonunu destekler.

**Açlıkta Ne Değişir:** Burada en net translasyonel kopukluk ortaya çıkıyor. Kemirgen modellerinde açlık FGF21'i hızla ve güçlü biçimde indükler. Cagigas et al. (2025)'in insan verisinde ise **9.8 günlük açlık FGF21'i anlamlı şekilde değiştirmiyor** (243.2→512.5 pg/mL, p=0.3285) — yazarlar bunun nedenini, insanda ketogenez/BHB yükselişinin FGF21 yükselişinden **önce geldiğine** (Fazeli et al. 2015) ve bu açlık süresinin FGF21'i tetiklemeye **yetersiz kalmış olabileceğine** bağlıyor; yani "insan FGF21'i açlıkta hiç kullanmaz" değil, "bu sürede henüz tetiklenmemiş olabilir" sonucu daha temkinli ve doğru. Asıl sürpriz refeeding'de geliyor: FGF21, yeniden beslenmeyle **1176 pg/mL'ye** fırlıyor (p=0.0007) — yaklaşık 5 kat artış. Bu artış, düşen BCAA'larla güçlü negatif korelasyon taşıyor (metiyonin r=-0.70, alanin r=-0.61, tirosin r=-0.59, valin r=-0.53, toplam BCAA r=-0.46), ama glikozla **hiç korelasyon göstermiyor** — bu, FGF21'in glukoz-alımı-uyarma rolüne (farede tanımlanmış) rağmen, burada glikozdan bağımsız bir tetikleyicinin (amino asit yetersizliği) öne çıktığını gösteriyor. Yazarların mixed-effects regresyon modeli, BCAA-FGF21 ilişkisinin **yalnızca refeeding fazında** anlamlı olduğunu, açlık fazında olmadığını doğruluyor — yani refeeding, mekanistik tetikleyici olarak öne çıkıyor. Bu model, literatürdeki başka bulgularla da uyumlu: BCAA repletion'ın mTORC1 sinyalini tersine çevirdiği (Maida et al. 2017) ve eksojen FGF21'in fare modellerinde BCAA birikimini azalttığı (Xu et al. 2022) gösterilmiş. Defour et al. (2020)'daki _IRS2_ artışı (insülin sinyalinin farklı bir kolu, hem açlıkta hem — dolaylı olarak — refeeding'e geçişte rol oynayabilecek bir düzenleyici) bu tabloyla tematik olarak bağlantılı, ama iki çalışma doğrudan aynı zaman noktalarını veya aynı türü incelemediği için bu bağlantı spekülatif bir paralellik olarak okunmalı.

---

### Genel Değerlendirme

Bu iki kaynak (Cagigas insan/9.8 gün su orucu + refeeding; Defour insan-fare/16-26 saat tek-seferlik açlık) BCAA-FGF21 ekseninde tür ve süre bakımından tamamlayıcı ama doğrudan karşılaştırılamaz iki veri noktası sunuyor. Protokol tipi ekseninde: ikisi de "sürekli su orucu / tek-seferlik açlık" paradigmasında, TRF/ADF/5:2 gibi tekrarlayan-döngüsel protokollerle bu eksenin nasıl davranacağı bu kaynaklarla bilinmiyor — özellikle FGF21'in "refeeding-tetiklenen" doğası düşünüldüğünde, günlük açlık-besleme döngüsü uygulayan protokollerde (TRF, ADF) bu ekseninin her döngüde yeniden aktive olup olmadığı önemli ve şu an açık bir soru. Süre ekseninde, Cagigas'ın 9.8 günlük açlığının FGF21'i tetiklemeye yetmediği gözlemi, "daha uzun açlık FGF21'i harekete geçirir mi" sorusunu açık bırakıyor — bu kaynaklarla yanıtlanamıyor. Diyet kompozisyonu: Cagigas'ın refeeding fazı özellikle bitkisel-ağırlıklı (düşük protein olası) bir diyetle yürütülmüş; FGF21'in düşük diyet-protein alımına karşı da duyarlı olduğu bilindiğinden (metinde dolaylı olarak değinilen bir literatür teması), bu refeeding diyetinin spesifik protein içeriğinin BCAA-FGF21 ilişkisini ne kadar güçlendirdiği ayrı bir değişken olarak ayrıştırılamıyor. Tür ekseninde tablo net: FGF21'in "açlık hormonu" kimliği kemirgene özgü bir basitleştirme; insanda bu hormon en azından bu protokolde bir "refeeding/nutrient-sensing" sinyali gibi davranıyor.

---

### Bibliyografya

- Cagigas ML, Santiappillai NT, Commissati S, et al. (2025). The Metabolic Transition Between Fasting and Feeding Alters Aging-Associated Metabolites, Lowers BCAAs, and Stimulates FGF21 Production in Humans. _Aging Cell_ 24:e70270.
- Defour M, Michielsen CCJR, O'Donovan SD, Afman LA, Kersten S. (2020). Transcriptomic signature of fasting in human adipose tissue. _Physiological Genomics_ 52:451–467.