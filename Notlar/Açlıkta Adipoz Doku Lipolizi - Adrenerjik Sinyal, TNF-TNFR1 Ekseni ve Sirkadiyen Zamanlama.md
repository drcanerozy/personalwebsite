---
Tür:
  - Çekirdek
ODAK:
  - "[[Aralıklı Açlık]]"
  - "[[Adipoz Doku]]"
MEKANİZMA:
  - "[[Adiposit Trigliserid Lipaz]]"
  - "[[İnflamasyon]]"
  - "[[Sirkadiyen Ritim]]"
DİZİN:
  - "[[00_Adipoz Doku ve Metabolizma_MOC]]"
  - "[[00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC]]"
  - "[[00_İnflamasyon ve İmmün Sistem_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Kişiselleştirilmiş Açlık]]"
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "p < 0.0001"
BESLEDİĞİ NOTLAR:
  - "[[Adipoz Doku Lipolizi]]"
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

- [[#1. Lipolitik Kaskad — β3-AR → PKA → HSL-ATGL-Plin1]]
- [[#2. TNF-TNFR1 Ekseni — Lipoliz İçin Zorunlu Bir Enflamatuar Ön Koşul]]
- [[#3. Sirkadiyen Beslenme Zamanlaması — eTRE vs dTRE Farkı]]
- [[#4. Kronik Obezitede Lipolitik Direnç — ADRB3 Kaybının Kalıcılığı]]
- [[#Kaynaklar]]

---

### 1. Lipolitik Kaskad — β3-AR → PKA → HSL-ATGL-Plin1

**Çıkarımım:** Bu üç kaynağı bir arada okuduğumda karşıma çıkan tablo, lipolizin tek bir "açık/kapalı" anahtar değil, en az üç ayrı kontrol noktasından geçen (adrenerjik reseptör yoğunluğu → PKA aktivasyonu → enzim fosforilasyonu) katmanlı bir kaskad olduğu. Kritik nokta şu: bu kaskadın her katmanı, farklı bir "açlık modülatörü" tarafından ayrı ayrı hedeflenebiliyor — de Oliveira et al. (2025) reseptör yoğunluğunun kendisini (ADRB3 ekspresyonu) TNF sinyaline bağlarken, Zambrano et al. (2024) aynı kaskadın çıktısının (gliserol salınımı) sirkadiyen saate göre farklılaştığını gösteriyor. Yani "lipoliz açlıkla artar" cümlesi doğru ama eksik; asıl soru "hangi seviyede, ne zaman ve kimde artıyor" sorusu.

#### Normal Fizyoloji

Beslenmiş durumda adipoz doku, enerjiyi trigliserit (TAG) formunda depolamaya programlıdır. Bu depolama durumunu koruyan temel fren insülindir: insülin sinyali, hücre içi siklik AMP (cAMP) düzeyini düşük tutarak Protein Kinaz A'nın (PKA) aktivasyonunu engeller. PKA aktive olmadığı sürece, lipolizin üç ana efektör proteini — Hormon Duyarlı Lipaz (HSL), Adiposit Trigliserid Lipaz'ı (bkz. Adiposit Trigliserid Lipaz) düzenleyen ko-aktivatör ABHD5/CGI-58 ve lipid damlacığının yüzeyini örten Perilipin-1 (Plin1) — fosforile olmaz ve trigliseritler adipositin içinde kilitli kalır. Sempatik sinir sisteminin salgıladığı noradrenalin ise bu dengenin karşı kutbunu oluşturur: adipositlerdeki β3-adrenerjik reseptörlere (ADRB3) bağlanarak cAMP-PKA yolunu aktive eder, PKA da hem HSL'yi hem Plin1'i fosforile ederek lipid damlacığının açığa çıkmasını ve trigliseritlerin serbest yağ asitleri (FFA) ile gliserole parçalanmasını sağlar.

#### Açlıkta Ne Değişir

Açlıkla birlikte insülin baskısı kalktığı ve sempatik tonus arttığı için bu kaskad tersine döner — ama üç kaynak da bu "dönüşün" beklenenden çok daha kırılgan ve çok katmanlı olduğunu gösteriyor. de Oliveira et al. (2025), sağlıklı (yalın) farelerde 24-48 saatlik açlığın hem eWAT hem iWAT'ta β3-AR içeriğini belirgin şekilde artırdığını, buna paralel olarak HSL ve Plin1 fosforilasyonunun yükseldiğini ve adiposit boyutunun küçüldüğünü göstermiştir. Ancak bu zincirin en üst noktasında beklenmedik bir gereklilik ortaya çıkmaktadır: TNFR1 reseptörü olmayan (TNFR1⁻/⁻) farelerde β3-AR artışı tamamen engellenmekte, dolayısıyla HSL/Plin1 fosforilasyonu da tetiklenememekte ve doku hiçbir küçülme göstermemektedir — bu ilişkiyi bir sonraki başlıkta detaylandıracağım. Duan et al. (2026) ise aynı kaskadın obezite bağlamında nasıl "donduğunu" gösteriyor: HFD-beslenen obez farelerde bazal (6 saatlik açlık) HSL ve Plin1 fosforilasyonu, yalın kontrol farelerine kıyasla zaten çok düşüktür; 3 günlük akut kalori kısıtlaması (diyet değişimi, DS) ile insülin düzeyleri tamamen normale dönmesine rağmen, bu bazal fosforilasyon defekti **hiç düzelmemiştir**. Bu, kaskadın "insülin baskısının kalkması yetmiyor, üst-akım reseptör havuzunun da (ADRB3) yeniden inşa edilmesi gerekiyor" şeklinde okunabilecek kritik bir bulgusudur — nitekim aynı çalışmada ADRB3 mRNA/protein düzeyi DS sonrasında da düşük kalmaya devam etmiştir. Zambrano et al. (2024) ise bu kaskadın nihai çıktısını (gliserol salınımı) insan yağ dokusu eksplantlarında ölçerek, açlık süresi arttıkça (8→12→16 saat) bu çıktının doğrusal olarak arttığını (p<0.0001) ve bunun zamanlama penceresinden (erken/geç) bağımsız olduğunu göstermiştir — yani kaskadın "ne kadar süre çalıştığı" ile "ne zaman çalıştığı" birbirinden ayrışan, farklı üst-sinyallerle kontrol edilen iki ayrı boyuttur.

---

### 2. TNF-TNFR1 Ekseni — Lipoliz İçin Zorunlu Bir Enflamatuar Ön Koşul

**Çıkarımım:** Bu, üç kaynak arasında bence en çarpıcı ve en çok "ezber bozan" bulgu. Kronik enflamasyonun (özellikle TNF-α'nın) insülin direnci ve metabolik hastalıkla ilişkisi klasik bir literatür — ama de Oliveira et al. (2025) TNF sinyalinin, en azından TNFR1 üzerinden, açlığa **fizyolojik ve zorunlu bir yanıt** olduğunu, yani "kötü" değil "gerekli" bir sinyal olabileceğini gösteriyor. Bu, enflamasyon-metabolizma ilişkisinin tek yönlü ("enflamasyon her zaman kötüdür") değil, bağlama göre (akut fizyolojik açlık vs. kronik metabolik hastalık) yön değiştirebilen bir ilişki olduğunu düşündürüyor — bu noktayı İnflamasyon notunuzla ve Kişiselleştirilmiş Açlık-Çapraz Tema Sentezi'ndeki "İnflamasyon ↔ İnsülin Direnci" başlığıyla mutlaka çapraz okumalısınız.

#### Normal Fizyoloji

Adipositlerde TNF, iki reseptör ailesi üzerinden sinyal iletir: TNFR1 ve TNFR2. Sağlıklı, beslenmiş durumda bazal TNF ekspresyonu düşüktür ve bu reseptörler adipositlerde asimetrik dağılım gösterir — de Oliveira et al. (2025)'in yayınlanmış tek-çekirdek RNA-sekanslama verisi üzerinden yaptığı analiz, farelerde adipositlerin %13'ünün TNFR1, yalnızca %8'inin TNFR2 eksprese ettiğini; insanda bu asimetrinin çok daha belirgin olduğunu (%24 vs %2.6) göstermiştir. Özellikle lipolitik bir adiposit alt kümesinde (mAd3) TNFR1 ekspresyonu TNFR2'nin neredeyse 5 katıdır — yani TNFR1 baştan itibaren lipoliz yapan hücrelerde zenginleşmiş bir reseptördür.

#### Açlıkta Ne Değişir

Açlıkla birlikte hem eWAT hem iWAT'ta TNF ekspresyonu anlamlı şekilde artar. Bu artışın işlevsel karşılığını test etmek için kullanılan TNFR1⁻/⁻ nakavt fare modeli, konunun ağırlığını ortaya koyuyor: bu fareler 24 saatlik açlığa **hiçbir** yağ dokusu kütle/adiposit boyutu küçülmesiyle yanıt vermemekte, bu direnç 48 saate uzatılan açlıkta bile kırılmamaktadır. Mekanizma zincirinin tamamı TNFR1'e bağımlıdır: reseptör yokluğunda β3-AR artışı gerçekleşmemekte, buna bağlı olarak iWAT'ta (eWAT'a kıyasla %70 daha fazla TNFR1 eksprese eden depoda) lipaz ekspresyon artışı da devreye girmemektedir. Bu bulgu yalnızca genetik nakavt ile sınırlı değil — TNF'yi farmakolojik olarak bloke eden infliximab uygulaması, WT (yabani tip) farelerde de aynı direnci taklit ederek 48 saatlik açlığın yağ dokusu küçültücü etkisini tamamen ortadan kaldırmıştır; bu da mekanizmanın gelişimsel bir kompanzasyon değil, gerçek zamanlı bir sinyal bağımlılığı olduğunu doğrulamaktadır. Sitokin özgüllüğü de önemli: aynı çalışmada IL-18⁻/⁻ fareler WT ile aynı derecede yağ kaybı göstermiş (IL-18 gereksiz), üstelik bu farelerde bazal TNF ekspresyonunun zaten yüksek olduğu saptanmıştır — yani IL-18 eksikliği, yüksek bazal TNF ile "telafi edilmiş" görünmektedir. Bulgunun insana taşınabilirliği, BARICAN bariatrik cerrahi kohortunda (n=53) test edilmiş: TNFR1 ekspresyonu **yalnızca subkutan (sWAT)** dokuda ATGL, HSL, leptin ve adiponektin ile güçlü korelasyon göstermiş, omental (oWAT) dokuda bu ilişki saptanmamıştır — yani depot-spesifiklik insanda da korunmaktadır (bkz. [[#4. Kronik Obezitede Lipolitik Direnç — ADRB3 Kaybının Kalıcılığı]]). Bununla birlikte, cerrahi öncesi TNFR1 düzeyi ile 1 yıl sonraki kilo/yağ kaybı arasında hiçbir korelasyon bulunamamıştır — bu, "lokal moleküler mekanizma" ile "sistemik klinik sonuç" arasındaki ayrışmanın (bkz. Kişiselleştirilmiş Açlık-Çapraz Tema Sentezi madde 3) bir başka insan kanıtıdır.

---

### 3. Sirkadiyen Beslenme Zamanlaması — eTRE vs dTRE Farkı

**Çıkarımım:** Zambrano et al. (2024) burada değerli bir ayrıştırma yapıyor: "ne kadar aç kaldığınız" ile "günün hangi saatinde aç kaldığınız" birbirinden bağımsız iki eksen. Bu, klinik pratikte hastalara sadece "16 saat aç kalın" demenin yeterli olmadığını, pencerenin sabaha mı akşama mı denk geldiğinin de ayrı bir değişken olduğunu gösteren güçlü bir mekanistik temel sağlıyor — bkz. Sirkadiyen Ritim.

#### Normal Fizyoloji

Adipoz dokunun lipolitik kapasitesi sabit değildir; periferik sirkadiyen saat (adipositlerin kendi iç saatleri), günün farklı saatlerinde farklı bir lipolitik "hazırlık düzeyi" oluşturur. Zambrano ve ark.'nın ex vivo insan yağ dokusu modelinde, dekzametazon ile senkronize edilen eksplantlar dört farklı koşulda (kontrol/4 öğün, erken TRE [08:00-12:00], geç TRE [16:00-20:00], 24 saat tam açlık) test edilmiş ve gliserol salınımı 4 saatte bir (CT0'dan CT24'e) izlenmiştir.

#### Açlıkta Ne Değişir

24 saatlik ortalamaya bakıldığında, hem eTRE hem dTRE kontrole kıyasla anlamlı derecede daha yüksek lipoliz üretmiş (p<0.0001), ancak **eTRE dTRE'den de anlamlı derecede yüksek** çıkmıştır (p=0.019). Bu farkın kaynağı özellikle önemli: gündüz/aktif fazda eTRE ile dTRE arasında hiçbir fark yokken (p=0.976), fark tamamen **gece/uyku fazında** ortaya çıkmaktadır (p=0.000007) — yani erken yeme penceresi, gece boyunca dokunun daha güçlü bir lipolitik durum sürdürmesini sağlıyor. Bu zamanlama etkisi, saf açlık süresinin etkisinden tamamen bağımsızdır: eTRE ve dTRE grupları açlık süresine göre eşleştirildiğinde, gliserol salınımı süreyle doğrusal olarak artmakta (8h: 0.08, 12h: 0.09, 16h: 0.12 μmol/h/g; p<0.0001), ancak süre ile zamanlama penceresi arasında hiçbir etkileşim bulunmamaktadır (p=0.988). Bu iki bulgu birlikte okunduğunda ortaya çıkan pratik çıkarım şu: bir TRE protokolünün toplam lipolitik "dozu" açlık süresiyle belirlenirken, bu dozun günün hangi saatine (özellikle gece periyoduna) denk geleceği ayrı bir değişken olarak protokolün erken mi geç mi olduğuna bağlıdır — iki eksen aynı anda optimize edilebilir, birbirini dışlamaz.

---

### 4. Kronik Obezitede Lipolitik Direnç — ADRB3 Kaybının Kalıcılığı

**Çıkarımım:** Bu son başlık, aslında ilk üç başlıkta anlatılanların "işe yaramadığı" senaryoyu gösteriyor ve klinik olarak belki en önemli mesajı taşıyor: yukarıda anlatılan tüm lipolitik kaskad (β3-AR artışı, HSL/Plin1 fosforilasyonu), obezite kronikleştikçe artık açlığa yanıt vermeyen, "kilitli" bir sisteme dönüşebiliyor.

#### Normal Fizyoloji

Sağlıklı/yalın bir bireyde, yukarıda anlatılan lipolitik kaskad açlığa hızlı ve orantılı şekilde yanıt verir; ADRB3 ekspresyonu bazal düzeyde korunur ve açlık sinyaliyle yukarı regüle olabilir.

#### Açlıkta Ne Değişir

Duan et al. (2026), 8 haftalık HFD ile obezleştirilen farelerde ADRB3 ekspresyonunun **gWAT'ta** (visseral depo) belirgin şekilde azaldığını, **iWAT'ta** (subkutan) ise bu azalmanın çok daha ılımlı ve istatistiksel olarak daha zayıf kaldığını göstermiştir — yazarlar bu farkı, iWAT'taki enflamasyonun gWAT'a kıyasla obezite sürecinde daha geç ortaya çıkmasıyla ilişkilendiriyor. Akut kalori kısıtlaması (DS, 3 gün) bu ADRB3 kaybını **hiçbir depoda tersine çevirememiştir** — tıpkı bir önceki başlıkta anlatılan HSL/Plin1 defekti gibi. Kronisite ekseni eklendiğinde tablo daha da netleşiyor: 18 haftalık (kronik) HFD sonrasında ADRB3 kaybı artık **her iki depoda da** belirgin ve derinleşmiş durumda, üstelik bu tabloya gWAT'ta biriken adiposit ölümü, makrofaj infiltrasyonu ("taç benzeri yapılar", CLS) ve TNF-α yüksekliği de eklenmiş durumdadır — bunların hiçbiri 18 saatlik akut kalori kısıtlamasıyla gerilememiştir. Burada ilginç bir kavramsal gerilim var: de Oliveira et al. (2025)'te TNF/TNFR1 sinyali açlığa **gerekli, fizyolojik** bir yanıt olarak resmedilirken, Duan et al. (2026)'da kronik obezitede biriken TNF-α, ADRB3'ü **baskılayan, patolojik** bir faktör olarak görünmektedir. Bu çelişki değil, bir doz-zaman eğrisi: akut/fizyolojik TNF sinyali lipolizi kolaylaştırırken, kronik/patolojik TNF birikimi (adipoz doku enflamasyonunun bir sonucu olarak) aynı reseptör sistemini (ADRB3) aşağı regüle ederek tam tersi bir sonuç üretebiliyor — "aynı molekül, bağlama göre zıt yön" örneği, Kişiselleştirilmiş Açlık-Çapraz Tema Sentezi'ndeki inflamasyon-IR ilişkisinin bu veri setindeki en somut karşılığı.

---

### Kaynaklar

- Zambrano, C., González-Alvarado, E., Salmerón, D., et al. (2024). Time-restricted eating affects human adipose tissue fat mobilization. _Obesity_, 32(9), 1680-1688. [https://doi.org/10.1002/oby.24057](https://doi.org/10.1002/oby.24057)
- de Oliveira, A. C. C., Babêtto, A. M., Silva, M. L., et al. (2026). TNF/TNFR1 is a Key Regulator of Prolonged Fasting-Induced Decrease in Adipose Tissue. _The FASEB Journal_, 40, e71404. [https://doi.org/10.1096/fj.202501928RR](https://doi.org/10.1096/fj.202501928RR)
- Duan, X., Davis, L. M., Patel, S., et al. (2026). Integrated analysis of insulin resistance reveals metabolic remodeling following diet switch–triggered calorie reduction. _Science Advances_, 12(19), eaed0535. [https://doi.org/10.1126/sciadv.aed0535](https://doi.org/10.1126/sciadv.aed0535)