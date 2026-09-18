---
Tür:
  - Besleyici
ODAK:
  - "[[Adipoz Doku]]"
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[Cinsiyet Farklılıkları]]"
DİZİN:
  - "[[00_Adipoz Doku ve Metabolizma_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Adipoz Doku Lipolizi]]"
  - "[[Bölgesel Adipozite, Depot-Spesifiklik ve Tür-Doku Eşleşme Problemi]]"
  - "[[Adipozite Gücü]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
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
> graph TD
>     A["Açlık Sinyali"] --> B{"Bazal İnsülin Düzeyi"}
>     B -->|Normoinsülinemi| C["FoxO1 Nükleer Translokasyonu → IRF4 Aktivasyonu"]
>     C --> D["ATGL & HSL Aktivasyonu → Yağ Asidi Mobilizasyonu (Lipoliz)"]
>     B -->|Kronik Hiperinsülinemi| E["FoxO1 Dışlanması → IRF4 Baskılanması"]
>     E --> F["Yağ Kilitlenmesi → Kas Proteolizi (Alanin Salınımı) → Glukoneojenez"]
> ```
>
> **Şekil Açıklaması:** Açlık sinyali karşısında bazal insülin düzeyi substrat partisyonunu belirler: Normoinsülinemide FoxO1/IRF4 ekseni üzerinden ATGL ve HSL aktive olarak lipoliz sağlanırken; kronik hiperinsülinemide IRF4 baskılanarak yağ dokusu kilitlenir ve glukoneojenez için iskelet kası proteolizi (kas kaybı) zorunlu hale gelir.

### İçindekiler

- [[#İntraselüler Lipoliz Yağ Damlacığının Enzimatik Yıkımı]]
- [[#Ekstraselüler Lipoliz ve LPL Ekseni]]
- [[#Çapraz Tema Lipoliz Genlerinde Tür Farkının Kaynağı]]
- [[#Genel Değerlendirme]]
- [[#Bibliyografya]]

---

### İntraselüler Lipoliz: Yağ Damlacığının Enzimatik Yıkımı

Lipoliz, adipoz dokunun açlığa verdiği yanıtın en görünür katmanıdır, ama tam da bu görünürlük yüzünden tek bir "açlık yanıtı" olarak genellenmeye en yatkın mekanizmalardan biridir. Oysa hem tür hem cinsiyet düzeyinde, bu enzimatik zincirin hangi basamağının harekete geçtiği belirgin şekilde değişkendir — bu da lipoliz direncinin (örn. genç dişilerde) tek bir "kapalı anahtar" değil, birden fazla noktada ayarlanabilen bir kontrol sistemi olduğunu düşündürüyor.

**Normal Fizyoloji:** Beslenmiş durumda insülin, hormon-duyarlı lipaz (LIPE (HSL)) ve adipoz trigliserid lipaz (PNPLA2 (ATGL)) aktivitesini baskılar; trigliseridler perilipin (PLIN1) kaplı lipid damlacıklarında depolanır. G0S2 lipolizin bazal inhibitörü olarak işlev görür; ABHD5 (CGI-58) ise ATGL'nin ko-aktivatörüdür ve perilipinle etkileşimi bloke edildiğinde serbest kalıp lipolizi tetikler.

**Açlıkta Ne Değişir:** Sistemik düzeyde beklenen yön nettir — insülin düşer, katekolaminler ve ADRB2 (β2-adrenerjik reseptör) sinyali artar, lipoliz uyarılır. Ancak Defour et al. (2020)'un insan-fare karşılaştırması, bu basamağın transkript düzeyinde hiç de konserve olmadığını gösteriyor: fare epididimal yağ dokusunda _Pnpla2_ açlıkla belirgin şekilde artarken, insan subkutan yağ dokusunda **hiç değişmiyor**. Yazarlar bunun nedenini kısmen IRF4 ekseninde arıyor — IRF4, farede _Pnpla2_ ve _Adrb3_ indüksiyonuna aracılık eden bir transkripsiyon faktörü olarak tanımlanmış (Eguchi et al. 2011), ve insan yağ dokusunda çok daha zayıf indükleniyor. Yani insanda ATGL'nin transkriptomik düzeyde harekete geçmemesi, yukarı akıştaki bir düzenleyicinin (IRF4) zayıf kalmasıyla açıklanabilir. Buna karşılık _LIPE_ (HSL) insanda hafif ama anlamlı biçimde **artarken**, farede hiç değişmiyor — yani hangi lipazın öne çıktığı türe göre yer değiştiriyor. Suchacki et al. (2023)'ün fare CR modelinde ise mesele mRNA değil protein-aktivasyon düzeyinde: CR, iWAT'ta HSL fosforilasyonunu (P-HSL:HSL) **erkeklerde** uyarırken **dişilerde uyarmıyor**; toplam HSL miktarı ise CR ile yalnızca dişilerde artıyor. Bu, dişilerde enzimin miktarca arttığı ama aktivasyonunun (fosforilasyon) baskılı kaldığı bir tabloyu işaret ediyor — genç dişilerin adiposit boyutunu koruması (CR gWAT/mWAT'ta hipotrofi yaratmıyor) ve plazma NEFA'yı yükseltmemesi bu tabloyla uyumlu. Lipid damlacığı düzenleyicilerinden CIDEC ve CIDEA de tür-arası zıt yönlü davranıyor: CIDEC insanda açlıkla azalırken farede artıyor; CIDEA ise tam tersi — insanda artıyor, farede hafifçe azalıyor. Buna karşın **ABHD5, ADRB2 ve IRF4 iki türde de artıyor**, **G0S2 iki türde de baskılanıyor** — yani lipolizin "hazırlık" katmanı (aktivatörün serbest kalması, inhibitörün susturulması) konserve, ama "icra" katmanı (hangi lipaz, ne kadar, hangi lipid damlacığı proteini eşliğinde) türe ve muhtemelen cinsiyete göre yeniden düzenleniyor.

---

### Ekstraselüler Lipoliz ve LPL Ekseni

**Normal Fizyoloji:** Dolaşımdaki trigliseridden zengin lipoproteinlerin (şilomikron, VLDL) yağ asitlerine hidrolizi, kapiler endotelde çapalanmış LPL (lipoprotein lipaz) tarafından yürütülür. LPL'nin endotele taşınması ve sabitlenmesi GPIHBP1 üzerinden olur. ANGPTL4 (fasting-induced adipose factor, FIAF) LPL'nin güçlü bir inhibitörüdür; onun fonksiyonel antagonisti ANGPTL8 ise beslenmiş durumda LPL aktivitesini destekler. VLDLR doku düzeyinde VLDL-türevi yağ asidi alımına aracılık eder.

**Açlıkta Ne Değişir:** Bu eksen, Defour et al. (2020)'un bulduğu en çarpıcı **konservasyon** örneğidir — intraselüler lipoliz genlerindeki tür-arası uyumsuzlukla doğrudan tezat oluşturur. GPIHBP1 iki türde de indükleniyor; ANGPTL4 iki türde de güçlü şekilde artıyor; ANGPTL8 ve VLDLR iki türde de tutarlı biçimde baskılanıyor. LPL'nin kendisi insanda hafifçe azalırken farede değişmiyor, ama bu küçük fark ekseni bozmuyor. Sonuç olarak "kapiler seviyede trigliserid girişinin kapatılması" sinyali — ANGPTL4 artışı, ANGPTL8/VLDLR baskılanması, GPIHBP1 artışı — evrimsel olarak yüksek oranda korunmuş bir modül gibi davranıyor. Suchacki et al. (2023) bu ekseni doğrudan transkriptomik düzeyde incelemese de, dolaylı bir doğrulama sunuyor: NEFA yükselişi ve HSL aktivasyonu erkeklerde belirginken, LPL-ANGPTL4 ekseninin (ekstraselüler kapı) davranışının cinsiyetler arası bu kadar keskin ayrışıp ayrışmadığı bu çalışmada test edilmemiş — bu, ileride doldurulması gereken bir boşluk olarak not edilebilir.

---

### Çapraz Tema: Lipoliz Genlerinde Tür Farkının Kaynağı

Defour ve arkadaşlarının verisi, "hücre-içi lipoliz diverjan, hücre-dışı lipoliz konserve" ayrımının rastgele olmadığını düşündürüyor: ekstraselüler eksen (LPL-ANGPTL4-ANGPTL8-GPIHBP1) dolaşımdaki lipid akışını kapiler düzeyde, yani organizma-çapında bir "trafik kontrolü" olarak yönetiyor — bu tür bir sistemik sinyalin evrimsel baskı altında korunması beklenir. Buna karşın intraselüler lipoliz (PNPLA2, LIPE, CIDEC/CIDEA) adipositin kendi iç metabolik "karar" mekanizması; burada türe özgü beslenme geçmişi, depo dağılımı ve hormonal ortam (örn. IRF4 ekspresyon düzeyi) devreye girip farklı çözümler üretebiliyor. Bu ayrım, kemirgen lipoliz çalışmalarının insana **ne zaman** güvenle genellenebileceğine dair pratik bir kural sunuyor: kapiler/dolaşım-düzeyi bulgular (LPL, ANGPTL4) daha güvenle taşınabilir; adiposit-içi enzimatik ayrıntılar (hangi lipazın ne kadar aktive olduğu) türler arası doğrudan aktarılmamalı.

---

### Genel Değerlendirme

Bu üç kaynak (30 gün üstü hiçbir protokolü kapsamıyor — en uzunu Suchacki'nin 6 haftalık %30 CR'si) lipoliz mekanizmasını yalnızca iki paradigma üzerinden aydınlatıyor: kısa-orta süreli günlük açlık (Defour, 16-26 saat) ve orta-vadeli kronik kalori kısıtlaması (Suchacki, 6 hafta). Protokol tipi ekseninde (TRF/ADF/5:2/CR ayrımı) şu an elimizdeki veriyle güvenilir bir karşılaştırma yapılamaz — Defour'un 16-26 saatlik tek-seferlik açlığı ile Suchacki'nin günlük tekrarlanan %30 CR'si arasında "doz" bakımından da (kısıtlamanın derinliği) "tekrar" bakımından da (tek olay vs. kronik) temel farklar var; ikisini aynı eksende sıralamak yanıltıcı olur. Süre ekseninde söylenebilecek tek şey: Suchacki'nin 6 haftalık kronik CR modeli, akut lipoliz yanıtının (Defour'daki 16-26 saatlik pencere) ötesinde, protein-aktivasyon düzeyinde kalıcı bir cinsiyet ayrışması (HSL fosforilasyonu) üretiyor — bu, kısa süreli transkriptomik çalışmalarda görünmeyen bir katman olabilir. Diyet kompozisyonu bu üç kaynakta sabit tutulmuş (standart chow/insonutrisyon formülasyonu) — yüksek yağ veya fruktoz içeriğinin lipoliz genlerini nasıl güçlendirip maskeleyebileceğine dair burada veri yok. Tür ekseninde ise tablo net: hücre-dışı eksen konserve, hücre-içi eksen türe (ve muhtemelen cinsiyete) özgü ayrışıyor — ancak Defour'un fare kohortu yalnızca erkek olduğundan, "tür farkı" ile "cinsiyet farkı"nın birbirine karışmış olabileceği ihtimalini dışlayamıyoruz (bkz. Bireysel ve Metodolojik Modülatörler).

---

### Bibliyografya

- Suchacki KJ, Thomas BJ, Ikushima YM, et al. (2023). The effects of caloric restriction on adipose tissue and metabolic health are sex- and age-dependent. _eLife_ 12:e88080.
- Defour M, Michielsen CCJR, O'Donovan SD, Afman LA, Kersten S. (2020). Transcriptomic signature of fasting in human adipose tissue. _Physiological Genomics_ 52:451–467.