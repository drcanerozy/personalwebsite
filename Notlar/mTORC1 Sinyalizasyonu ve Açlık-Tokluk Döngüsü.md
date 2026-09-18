---
Tür:
  - Besleyici
ODAK:
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[Nutrient Sensing]]"
  - "[[Notlar/Otofaji|Otofaji]]"
  - "[[mTOR]]"
DİZİN:
  - "[[00_Adipoz Doku ve Metabolizma_MOC]]"
  - "[[00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC]]"
  - "[[00_Lipotoksisite ve Ektopik Yağ Birikimi_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
  - "[[Otofaji]]"
  - "[[BCAA Dinamikleri ve FGF21 — Açlık-Beslenme Geçişinin Amino Asit Sensörü]]"
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

- [[#Giriş — İki Farklı Deneyde Aynı Molekül]]
- [[#Normal Fizyoloji — mTORC1'in Besin Sensörü Olarak Rolü]]
- [[#Açlıkta Ne Değişir — Baskılanma mı, Sıçrama mı]]
- [[#Vaka 1 — Yin ve ark.-Kronik Maternal Baskılanma ve Epigenetik Kilit]]
- [[#Vaka 2 — Zhang ve ark.-Akut Tokluk-Kaynaklı Aktivasyon]]
- [[#Ortak Payda — mTORC1 Yönü Ne Zaman Zararlı, Ne Zaman Uyum Sağlayıcı]]
- [[#Kişisel Notlarım]]

---

### Giriş — İki Farklı Deneyde Aynı Molekül

mTORC1, "besin var, büyü/depola" sinyalinin moleküler yürütücüsüdür. Bu derlemede okuduğumuz iki fare çalışması — Yin et al. (2023) ve Zhang et al. (2026) — mTORC1'i tamamen farklı bağlamlarda, tamamen farklı yönlerde manipüle ediyor, ama ikisi de aynı temel gerçeği doğruluyor: **mTORC1'in aktivitesi, açlık-tokluk döngüsünün metabolik çıktısını belirleyen zorunlu bir anahtar noktadır** — ne var ki bu anahtarın hangi yöne çevrilmesinin "iyi" ya da "kötü" olduğu tamamen bağlama bağlıdır.

---

### Normal Fizyoloji — mTORC1'in Besin Sensörü Olarak Rolü

mTORC1 (mechanistic target of rapamycin complex 1), amino asit, glukoz ve büyüme faktörü bolluğunu algılayan bir Nutrient Sensing kompleksidir. Aktive olduğunda protein sentezini, lipogenezi ve hücre büyümesini teşvik eder; baskılandığında ise Otofaji ve katabolik süreçler devreye girer. Raptor, mTORC1'in kompleksin işlevi için zorunlu olan regülatör alt birimidir — Raptor yokluğunda mTORC1 aktivitesi besin durumundan bağımsız olarak tamamen ortadan kalkar. Downstream efektörü S6K1, ribozomal S6 proteinini fosforile ederek (p-S6) protein sentezini ve hücresel büyümeyi tetikler.

---

### Açlıkta Ne Değişir — Baskılanma mı, Sıçrama mı

Klasik beklenti şudur: açlıkta besin sinyali azalır, mTORC1 baskılanır, otofaji ve katabolizma artar; toklukta ise tam tersi olur. Ama bu iki çalışma, bu basit modelin üstüne iki katman daha ekliyor — biri _kalıcı/epigenetik_ bir baskılanma, diğeri _akut/protokole-özgü_ bir aktivasyon.

---

### Vaka 1 — Yin ve ark.: Kronik Maternal Baskılanma ve Epigenetik Kilit

Yin et al. (2023)'te mTORC1 baskılanması, açlığın kendisinden değil, **anne farenin gebelik öncesi 12 haftalık gün aşırı açlık öyküsünün yavruda bıraktığı epigenetik izden** kaynaklanıyor. Maternal IF, yavrunun karaciğerinde DNA metiltransferaz (DNMT1, DNMT3b) düzeylerini kalıcı olarak düşürüyor; tüm-genom bisülfit sekanslaması, mTOR yolağı bileşenlerinden Pik3ca, Pten, Prkca, Rps6ka6 ve Mtor'un hipometile, buna karşılık Eif4b ve Raptor'un hipermetile hale geldiğini gösteriyor. Sonuç: yetişkin yavruların karaciğerinde mTORC1 sinyali, hem normal hem yüksek yağlı diyet altında **kronik olarak baskılı** kalıyor — ve bu baskılanma hepatik steatoz, adipozite ve glukoz intoleransıyla doğrudan ilişkili.

Bu bulgunun en çarpıcı yanı, nedenselliği doğrulayan kurtarma deneyi: karaciğere S6K1 aşırı ekspresyonu (Ad-S6K1) verilerek mTORC1 yapay olarak yeniden aktive edildiğinde, glukoz intoleransı tamamen düzeliyor, karaciğer TAG birikimi normalleşiyor, yağ dokusu hipertrofisi geriliyor. Yani burada mTORC1'in **düşük olması** patolojiktir — kalıcı, epigenetik olarak "kilitlenmiş" bir baskılanma söz konusu, ve bu kilidi açmak (S6K1 ile) fenotipi düzeltiyor. Önemli bir nüans: bu kurtarma etkisi hem kontrol hem IF-öyküsü yavrularında görülüyor (IF'e özgü bir "panzehir" değil), bu da mTORC1'in genel bir metabolik düzenleyici olarak rolünü, epigenetik programlamadan bağımsız olarak da vurguluyor.

---

### Vaka 2 — Zhang ve ark.: Akut Tokluk-Kaynaklı Aktivasyon

Zhang et al. (2026)'de tablo tam tersi: mTORC1, kronik olarak baskılı değil, **her tokluk evresinde akut olarak aktive oluyor** — ve bu aktivasyon, sağlıklı bir adaptasyon değil, kahverengi yağ dokusunun (BAT) "beyazlaşmasını" tetikleyen patolojik-benzeri bir sinyal. Refeeding anında BAT'ta insülin/Akt fosforilasyonu değişmezken, S6K fosforilasyonu keskin biçimde artıyor — yani bu, insülinden bağımsız, tokluğa özgü bir mTORC1 sıçraması. BAT-spesifik genetik Raptor nakavtı (AAV-Cre ile), bu sıçramayı ortadan kaldırdığında, tokluk-kaynaklı BAT beyazlaşması, lipid damlacığı birikimi ve doymuş lipid sınıflarının (TG, MG, LPC, PC, HexCer) artışı da neredeyse tamamen engelleniyor. Burada mTORC1'in **yüksek olması** istenmeyen sonuca (BAT'ın termojenik kimliğini kaybedip depolayıcı bir dokuya dönüşmesi) yol açıyor.

---

### Ortak Payda — mTORC1 Yönü Ne Zaman Zararlı, Ne Zaman Uyum Sağlayıcı

İki çalışmayı yan yana koyduğunda ortaya çıkan sentez şu: mTORC1'in "iyi" ya da "kötü" olması, mutlak aktivite düzeyinden çok, **doku bağlamı ve zamanlamasıyla** ilgili. Karaciğerde kronik baskılanma (Yin) hepatik lipojenez genlerinin (Pparγ, Cd36, Scd1) paradoksal biçimde artmasına ve β-oksidasyonun (Acadvl, Atgl, Pparδ) baskılanmasına yol açarak steatoza neden oluyor — yani mTORC1 eksikliği burada lipid sentezini durdurmuyor, tam tersi yönde bir dengesizlik yaratıyor. BAT'ta ise akut aktivasyon, doğrudan Agpat2/Dgat2 aracılı TAG sentezini tetikleyerek benzer bir lipid-biriktirme sonucuna varıyor. İki farklı yönden (biri eksiklik, biri fazlalık) aynı fenotipik sonuca (ektopik/anormal lipid birikimi) ulaşılması, mTORC1 yolağının doku-spesifik "set noktasının" bozulmasının — yönden bağımsız olarak — metabolik disfonksiyona yol açabileceğini düşündürüyor. Bu, 4.Cellular Brakes başlığındaki "hücresel frenler" kavramına somut bir moleküler karşılık sunuyor.