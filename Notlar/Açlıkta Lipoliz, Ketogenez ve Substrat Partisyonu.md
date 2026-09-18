---
Tür:
  - Çekirdek
ODAK:
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[Adiposit Trigliserid Lipaz]]"
  - "[[Yağ Metabolizması]]"
  - "[[Glukoz Dengesi]]"
DİZİN:
  - "[[00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC]]"
  - "[[00_Adipoz Doku ve Metabolizma_MOC]]"
  - "[[00_Kalori Kısıtlaması ve Enerji Metabolizması_MOC]]"
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

- [[#Giriş — Neden Lipoliz Tek Bir Yolak Değil]]
- [[#Normal Fizyoloji — Tokluk Durumunda Lipid Depolama]]
- [[#Açlıkta Ne Değişir — Sistemik Lipoliz ve Ketogenez]]
- [[#Adipoziteye Bağlı Ayrışma — Zayıf ve Obez Doku Farklı Konuşuyor]]
- [[#Refeeding'in Ayna Görüntüsü — BAT'ta Ters Yönlü Lipid Akışı]]
- [[#Gliseroneojenez — Yağ Depolamanın Şaşırtıcı Karbonhidrat Kaynağı]]
- [[#Kişisel Notlarım]]

---

### Giriş — Neden Lipoliz Tek Bir Yolak Değil

Lipoliz, "açlıkta yağ yakılır" cümlesinin arkasındaki tek bir anahtar reaksiyon gibi göründüğü sürece basit bir yolaktır. Ama Rossmeislova et al. (2024) ve Zhang et al. (2026)'yı yan yana okuduğunda, bu basitliğin yanıltıcı olduğu ortaya çıkıyor: lipolizin hızı, hangi dokuda gerçekleştiği, insülin tarafından ne kadar sıkı frenlendiği ve tokluk anında hangi yöne evrildiği — hepsi bireyin adipozite durumuna ve dokunun tipine (beyaz vs. kahverengi) göre kökten farklılaşıyor. Bu not, Adiposit Trigliserid Lipaz aracılı klasik lipoliz-ketogenez eksenini, iki farklı kaynaktan gelen insan ve fare verisiyle katmanlandırıyor.

---

### Normal Fizyoloji — Tokluk Durumunda Lipid Depolama

Beslenmiş (postprandiyal) durumda insülin, hem Adiposit Trigliserid Lipaz aktivitesini baskılayarak lipolizi durdurur hem de trigliserit sentezini (lipogenez) teşvik eder. Bu, adipositin normal "depolama modu"dur: dolaşımdaki glukoz ve yağ asitleri triaçilgliserol (TAG) olarak depolanır, serbest yağ asidi (FFA) akışı düşük tutulur, karaciğer ketogenez yapmaz çünkü insülin hepatik karnitin palmitoiltransferaz-1 aktivitesini baskılar. İnsülin Hassasiyeti normal olduğunda bu fren mekanizması hızlı ve etkilidir — az miktarda insülin bile lipolizi neredeyse tamamen durdurabilir.

---

### Açlıkta Ne Değişir — Sistemik Lipoliz ve Ketogenez

60 saatlik tam açlık modelinde (Rossmeislova et al. (2024)), insülin düzeyi düştükçe bu fren gevşer ve Adiposit Trigliserid Lipaz aracılı lipoliz devreye girer: dolaşımdaki gliserol ve FFA seviyeleri yükselir, karaciğerde ketogenez başlar ve β-hidroksibütirat (3HB) dramatik biçimde artar. Bu artış rastgele değildir — dokudaki FFA içeriğiyle güçlü pozitif, kan glukozuyla negatif korelasyon gösterir; yani ketogenez, doğrudan adipoz dokudan gelen yağ asidi akışının bir "aynası" gibi davranır. Aynı açlık, proteoliz göstergesi olan dallı zincirli amino asitleri (lösin, valin) de yükseltir ve laktat üretimini artırır — laktat ve gliserol, glikojen tükendikten sonra karaciğerin glukoneogenez için kullandığı iki temel substrattır.

Bu resim, Solunum Katsayısı üzerinden de doğrulanır: açlıkla RQ düşer (yağ oksidasyonuna kayış), tokluğa dönüldüğünde yükselir. Ama bu genel örüntünün altında, kimin ne kadar lipoliz yaptığı ve ne kadar keton ürettiği bireyin adipoz doku kütlesine göre keskin biçimde ayrışır.

---

### Adipositeye Bağlı Ayrışma — Zayıf ve Obez Doku Farklı Konuşuyor

Burada işin ilginç kısmı başlıyor. Rossmeislova et al. (2024)'te zayıf (LE) ve obez (OB) premenopozal kadınlar aynı 60 saatlik açlığa maruz bırakıldığında, obez kadınların yağ dokusu belirgin şekilde daha "sessiz" kalıyor: doku eksplantlarında izoproterenol-uyarılı gliserol artışı zayıflarda daha yüksek, 1 nM insülinin lipolizi baskılama gücü ise zayıflarda daha _düşük_ — yani zayıf doku hem daha kolay uyarılabiliyor hem insüline karşı daha az duyarlı. Kütleye normalize edildiğinde (FFA/yağ kütlesi, gliserol/yağ kütlesi) fark daha da çarpıcı hale geliyor: açlık sonunda zayıf kadınların kilogram yağ dokusu başına salgıladığı gliserol, obez kadınlardan yaklaşık üç kat fazla. Bu fark ketogenezde de yankılanıyor — obez kadınlarda açlık-indüklü 3HB artışı çok daha sönük kalıyor, çünkü karaciğere giden ham madde (FFA akışı) zaten kısıtlı.

Bu gözlem, obezitenin yağ dokusunu "tembelleştirdiği" şeklindeki basit anlatıyı tersine çeviriyor: yazarlar bunu, dokunun kendi genişlemiş boyutuna karşı geliştirdiği _koruyucu_ bir adaptasyon olarak yorumluyor — dolaşımdaki FFA'yı toksik düzeylere çıkarmamak için lipolitik akış kütleye göre kısıtlanıyor. Ama bu korumanın bedeli var: trigliserit turnover'ı düşük kaldığından, obez bireylerin kısa süreli enerji açığına (fasting'e) yanıt olarak yağ kaybetme kapasitesi de zayıflıyor. Bu ikili doğa (koruma + direnç), derlemenin "hücresel frenler" temasıyla doğrudan örtüşüyor (bkz. 4.Cellular Brakes).

Yeni geliştirilen **AdipoSLIP** indeksi (FFA'nın yağ kütlesine, insülinin vücut ağırlığına normalize edilmiş hali) bu farkı klasik AdipoIR indeksinden çok daha iyi yakalıyor — çünkü AdipoIR, vücut kompozisyonunu hesaba katmadan FFA×insülin çarpımına dayanıyor ve bu da adipoziteyle otomatik olarak şişiyor.

---

### Refeeding'in Ayna Görüntüsü — BAT'ta Ters Yönlü Lipid Akışı

Zhang et al. (2026), aynı açlık-tokluk çerçevesini bambaşka bir dokuda — kahverengi yağ dokusunda (Kahverengi Adipoz Doku) — test ettiğinde, beyaz yağ dokusunun (gWAT) alıştığımız davranışının tam tersini buluyor. gWAT, klasik senaryoyu izliyor: açlıkta büzülüyor (lipoliz), toklukta genişliyor (yeniden depolama). BAT ise açlığa neredeyse kayıtsız kalıyor — çünkü fasting sırasında kendi TAG depolarını değil, muhtemelen gWAT'tan salınan dolaşımdaki FFA'yı kullanarak termojenezi sürdürüyor. Asıl patolojik-benzeri yanıt, _tokluk_ evresinde ortaya çıkıyor: BAT bu evrede kütlesel bir "beyazlaşma" (whitening) yaşıyor, devasa lipid damlacıkları biriktiriyor ve doku lipid profili keskin biçimde doymamıştan doymuşa kayıyor (LPC 20:4/PC 38:5 azalırken, LPC 16:0/PC 30:1 artıyor).

Bu, "refeeding sadece depoları dolduran pasif bir evre" varsayımını çürütüyor — BAT için refeeding, aktif bir yeniden programlanma sinyalidir ve bu sinyalin yürütücüsü mTORC1'dir (bkz. mTORC1 Sinyalizasyonu ve Açlık-Tokluk Döngüsü).

---

### Gliseroneojenez — Yağ Depolamanın Şaşırtıcı Karbonhidrat Kaynağı

Hem Rossmeislova et al. (2024) hem Zhang et al. (2026), gliserol-3-fosfat (G3P) üretiminin trigliserit sentezindeki kilit rolüne işaret ediyor — ama iki farklı bağlamda. Rossmeislova'da, obez kadınların gliserol seviyeleri açlıkla değişmiyor (zayıflarda arttığı halde), bu da obez dokunun glikojen tükendikten sonra gliserolü glukoneogenez için tuttuğu/geri kullandığı şeklinde yorumlanıyor. Zhang'de ise refeeding sırasında BAT'ta üst glikoliz ara ürünü DHAP'ın gliseroneojeneze saptırıldığı, GPD1/TPI enzimlerinin indüklendiği ve bu G3P havuzunun Agpat2/Dgat2 üzerinden doğrudan yeni TAG sentezini beslediği gösteriliyor. Yani aynı biyokimyasal düğüm (G3P üretimi) bir dokuda "enerji açığını yönetme" stratejisi, diğerinde "tokluk-kaynaklı yağ depolama" motoru olarak iş görüyor — bağlam (doku tipi + beslenme fazı) aynı molekülün fizyolojik anlamını tersine çevirebiliyor.