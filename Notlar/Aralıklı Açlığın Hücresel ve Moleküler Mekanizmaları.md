---
Tür:
  - Çekirdek
ODAK:
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[AMPK]]"
  - "[[İnsülin Direnci]]"
  - "[[Sirkadiyen Ritim]]"
  - "[[Mikrobiyota]]"
  - "[[Adipoz Doku]]"
  - "[[Karaciğer Yağlanması]]"
  - "[[Yaşlanma]]"
  - "[[İnflamasyon]]"
  - "[[Mitokondriyal Disfonksiyon]]"
  - "[[Sirtüin]]"
  - "[[Nutrient Sensing]]"
  - "[[Cinsiyet Farklılıkları]]"
DİZİN:
  - "[[00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC]]"
  - "[[Metabolizma]]"
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "null"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "p > 0.05 (anlamsız)"
BESLEDİĞİ NOTLAR:
  - "[[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]"
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

> **Metodolojik Etiketler:** #finding/null
# Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları: Bütünleşik Bir Referans

## İçindekiler

- [[#Giriş: Açlığın Ortak Dili ve Ayrışan Lehçeleri]]
- [[#Yolak ve Mekanizma Başlıkları]]
    - [[#1. Lipogenez ve Lipid Sentez Yolağı]]
    - [[#2. AMPK - Katabolik Anahtar]]
    - [[#3. İnsülin Sinyali ve Beta Hücre Sekresyonu]]
    - [[#4. Endoplazmik Retikulum Stresi ve Unfolded Protein Response]]
    - [[#5. Sirkadiyen Saat]]
    - [[#6. Browning ve Termojenez]]
    - [[#7. Desatürasyon ve Elongasyon Enzimleri]]
    - [[#8. Adipoz Doku İnflamasyonu]]
    - [[#9. Mikrobiyota-Metabolit Ekseni]]
    - [[#10. Kas Protein Dengesi]]
    - [[#11. Karaciğer Glikojen ve Steatoz Dinamiği]]
    - [[#12. Substrat Oksidasyonu ve Metabolik Esneklik]]
    - [[#13. Hücresel Yaşlanma ve Kök Hücre Plastisitesi]]
    - [[#14. Oksidatif Stres ve Antioksidan Savunma]]
- [[#Çapraz-Tema Başlıkları]]
    - [[#A. İnflamasyon ↔ İnsülin Direnci: Zincir Her Zaman Aynı Halkalardan Geçmiyor]]
    - [[#B. Sirkadiyen Saat ↔ Lipid Metabolizması: Zamanlama Bir Değişken Değil, Bir Mekanizma]]
    - [[#C. Plazma ↔ Doku Ayrışması: Sistemik Sessizlik, Lokal Gürültü]]
    - [[#D. Genotip ↔ Diyet Stresi Etkileşimi]]
    - [[#E. Protokol Dozu ↔ Doku Yanıt Eşiği]]
    - [[#F. Yaşlanma ↔ Doku Yanıt Kapasitesi]]
    - [[#G. Depot-Spesifiklik: Yağ Dokusu Tek Bir Organ Değildir]]
- [[#Genel Değerlendirme]]
- [[#Bibliyografya]]

---

## Giriş: Açlığın Ortak Dili ve Ayrışan Lehçeleri

Açlık durumu, hücre düzeyinde tek bir sinyal setiyle başlar: dolaşımdaki glukoz ve insülin düşer, glukagon ve kortikosteron yükselir, hücre içi enerji yükü (ATP/AMP oranı) azalır. Bu ortak başlangıç sinyali, AMPK aktivasyonu, insülin sinyalinin geri çekilmesi ve sirkadiyen saat genlerinin yeniden hizalanması gibi bir dizi "aşağı akış" (downstream) yolağı tetikler. Ancak bu ortak başlangıç noktasından itibaren, doku tipine, protokolün süresine/sıklığına, eşlik eden diyetin bileşimine, hayvanın (veya insanın) yaşına, cinsiyetine ve altta yatan metabolik fenotipine (yalın vs obez, insülin duyarlı vs dirençli) bağlı olarak yollar keskin biçimde ayrışır. Bu not, tek tek çalışmaların bulgularını sıralamak yerine, bu ortak başlangıçtan itibaren ayrışan yolları — mekanizma mekanizma — takip etmeyi amaçlıyor.

---

## Yolak ve Mekanizma Başlıkları

### 1. Lipogenez ve Lipid Sentez Yolağı

**Normal Fizyoloji:** Tokluk durumunda, insülin sinyali karaciğer ve yağ dokusunda lipogenezi tetikleyen ana anahtardır. İnsülin, sterol düzenleyici element bağlayıcı protein olan **SREBP-1c**'nin (ve karaciğerde ayrıca **SREBP-2**'nin, kolesterol sentezi için) nükleer translokasyonunu ve transkripsiyonel aktivitesini artırır. SREBP-1c, sırasıyla **ACC (Asetil-CoA Karboksilaz)**, **FAS/FASN (Yağ Asidi Sentaz)** ve **DGAT (Diaçilgliserol Açiltransferaz)** gibi yağ asidi ve trigliserit sentez enzimlerinin ekspresyonunu artırır. Bu yolak, fazla glukozu/asetil-CoA'yı depolanabilir trigliseride dönüştürerek enerji fazlasını "paketler."

**Açlıkta Ne Değişir:** Açlık, bu anaboliğik yönü tersine çevirmesi beklenen klasik bir baskı sinyalidir — ve gerçekten de çoğu çalışmada bu baskı doğrulanıyor, ama derece ve tutarlılık protokole göre çarpıcı biçimde değişiyor. Kilic-Erkek (2025) çalışmasında, hem 8:16 TRF hem 5:2 IF, bazal (fruktozsuz) koşulda serum ACC'yi kontrolün altına düşürmüş; yüksek fruktoz (HF) diyetiyle kombine edildiğinde ise her iki protokol de HF'nin yükselttiği serum ve karaciğer SREBP-1c, SREBP-2, ACC, TG ve kolesterolü **tamamen tersine çevirmiştir** — ancak 8:16 TRF, SREBP-1c ve TAG baskılamasında 5:2'ye göre sistematik olarak daha üstün çıkmıştır; bu, aynı toplam kalori kısıtlaması altında bile **beslenme penceresinin genişliğinin** (16 saatlik açlık vs 24 saatlik açlık döngüsü) lipogenik baskı gücünü belirleyebileceğini gösteriyor. Bushman et al. (2026) çalışmasında ise tablo daha karmaşık: yaşlı dişi farelerde TRF, Gon-WAT'ta (visseral) HFD ile baskılanan Srebp-1c'yi ve Fasn'ı **beklenenin tersine** kontrol ve HFD-AL gruplarının da üzerine çıkararak up-regüle etmiştir — burada lipogenez baskısının değil, tam tersine bir "lipogenik-lipolitik döngü" (futile cycle) yeniden aktivasyonunun devrede olduğu görülüyor (bkz. [[#6. Browning ve Termojenez]]). Yang and Liu (2024) çalışmasında ise TRF, karaciğerde Pparγ-2 ve Srebp1c'yi klasik yönde baskılarken, aynı hayvanların **eWAT** dokusunda tam tersi bir eğilim (yükselme trendi, anlamlı değil) göstermiştir — yani lipogenez baskısı doku-spesifiktir, karaciğerde tutarlı ama yağ dokusunda depo-bağımlıdır.

Fruktozun burada özel bir rolü var: Kilic-Erkek (2025)'de yalnızca fruktoz mevcutken lipogenik genlerdeki değişim büyük ve anlamlı hale geliyor — açlığın "tersine çevirme" etkisi, aslında ortada tersine çevrilecek güçlü bir lipogenik uyarı olduğunda daha net görünür hale geliyor. Bu, açlığın lipogenez üzerindeki etkisinin mutlak değil, **diyetin lipogenik yük düzeyine göre şartlı** olduğuna işaret ediyor.

### 2. AMPK - Katabolik Anahtar

**Normal Fizyoloji:** AMPK (AMP-aktive protein kinaz), hücrenin enerji sensörüdür; AMP/ATP oranı yükseldiğinde aktive olur ve anabolik (enerji tüketen) yolakları baskılarken katabolik (enerji üreten) yolakları teşvik eder. Aktive AMPK, ACC'yi fosforile ederek (**pACC**) inhibe eder — bu, malonil-CoA üretimini durdurarak hem yağ asidi sentezini durdurur hem de karnitin palmitoiltransferaz-1 (CPT1) üzerinden mitokondriyal yağ asidi oksidasyonunu serbest bırakır (malonil-CoA normalde CPT1'i inhibe eder).

**Açlıkta Ne Değişir:** Tsameret et al. (2023) çalışması, bu yolağın açlığın **zamanlamasına** ne kadar duyarlı olduğunu gösteren en net örnektir: 5 haftalık TRF hem erken (E-TRF) hem geç (L-TRF) grupta karaciğer pAMPK/AMPK oranını artırmış, ama bu artışın aşağı akış etkileri (pACC/ACC oranı, UCP2 protein düzeyi) yalnızca **E-TRF** grubunda karaciğer, yağ dokusu ve iskelet kasının **üçünde birden** güçlü şekilde ortaya çıkmıştır. L-TRF de kas dokusunda pACC/ACC'yi artırmış ama genel iyileşme E-TRF seviyesine hiç ulaşamamıştır. Yani AMPK aktivasyonunun kendisi zamanlamadan bağımsız tetiklenebiliyor, ama bu aktivasyonun **fonksiyonel sonuca** (gerçek yağ asidi oksidasyonu artışı, FAS baskılanması) dönüşmesi büyük ölçüde beslenme penceresinin sirkadiyen fazla (aktif/karanlık faz başlangıcı) hizalanmasına bağlı görünüyor. Nitekim aynı çalışmada FAS seviyeleri AL-HF ve L-TRF-HF gruplarında yüksek kalırken, yalnızca E-TRF-HF grubunda kontrol seviyesine kadar baskılanabilmiştir — AMPK aktive olsa da, yanlış fazda aktive olduğunda lipogenezi tam olarak durduramıyor.

### 3. İnsülin Sinyali ve Beta Hücre Sekresyonu

**Normal Fizyoloji:** Tokluk sonrası yükselen glukoz, pankreas beta hücrelerinden insülin salgılanmasını tetikler; insülin karaciğer, kas ve yağ dokusunda glukoz alımını, glikojen sentezini ve lipogenezi teşvik ederken lipolizi güçlü şekilde baskılar (antilipolitik etki). Beta hücresi bu sekresyonu sürdürebilmek için yüksek bir proteostatik ve mitokondriyal (OXPHOS) kapasiteye ihtiyaç duyar.

**Açlıkta Ne Değişir:** Çoğu protokolde açlık insülini ve HOMA-IR'yi düşürür — Soares et al (2025)'de tüm IF grupları (TRF, ADF, ADMF) kontrole göre daha düşük HOMA-IR göstermiştir; Tsameret et al. (2023)'te hem E-TRF hem L-TRF insülin/C-peptid/HOMA-IR'yi AL-LF (düşük yağlı kontrol) seviyesine indirmiş, E-TRF bunu daha güçlü yapmıştır. Ancak bu iyileşme evrensel değildir: Conn et al. (2024) çalışmasında, genetik obezite/T2D modeli olan db/db farelerde 10 haftalık 5:2 IF, yüksek fed ve fasted serum insülin konsantrasyonlarını **hiç değiştirmemiştir** — bu, aşağıda tartışılacak "hiperinsülinemik fren" kavramının temelini oluşturuyor (bkz. Çapraz-Tema A). Mehl et al. (2024) ise bu resmi bir katman daha derinleştiriyor: standart 5 saatlik açlık sonrası, yükselen açlık glisemisi periferik insülin duyarlılığıyla negatif korele olurken, plazma insülinemi **sabit kalmıştır** — bu, artan glisemiye rağmen beta hücresinin telafi edici insülin artışı yapamadığını, yani göreceli bir **sekresyon kusuru** olduğunu düşündürür. Bu kusurun transkriptomik temeli adacık (islet) dokusunda görülebiliyor: yükselen glisemiyle birlikte ribozom, ER protein işleme, proteazom ve mitokondriyal OXPHOS yolakları baskılanırken, ubikitin-bağlı proteoliz yukarı regüle olmuştur — yani beta hücresinin protein üretim/kalite kontrol/enerji üretim kapasitesi, artan talebe yetişemeyecek şekilde geriliyor. Önemli bir nüans: bu yolakların çoğu **yalnızca standart diyet grubunda bile** anlamlı çıkmıştır — yani adacığın bazal fonksiyonel tavanı büyük ölçüde genetik arka plan (suş) tarafından belirleniyor, diyet bunun üzerine ek bir yük bindiriyor.

### 4. Endoplazmik Retikulum Stresi ve Unfolded Protein Response

**Normal Fizyoloji:** ER, sekretuvar ve membran proteinlerinin katlandığı organeldir. Aşırı lipid akışı veya sentez yükü ER'nin katlama kapasitesini aştığında, katlanmamış protein yanıtı (UPR) devreye girer: **PERK** (eIF2α fosforilasyonu üzerinden genel protein sentezini yavaşlatır), **GRP78/BiP** (bir şaperon, stres sensörlerini serbest bırakarak UPR'yi başlatır) ve **XBP1** (splicing sonrası şaperon/ERAD genlerini indükler) bu yanıtın üç ana kolu.

**Açlıkta Ne Değişir:** Kilic-Erkek (2025), bu yolağın açlıkla nasıl modüle edildiğini doğrudan gösteriyor: tek başına IF (fruktozsuz koşulda) ER stresi yaratmıyor, ama yüksek fruktoz diyetinin indüklediği ER stresini **tersine çeviriyor**. Burada da bir doz/protokol farkı var — 8:16 TRF, HF ile yükselen hem PERK hem GRP78'i baskılayabilirken, 5:2 IF yalnızca GRP78'i düşürebilmiştir; PERK üzerinde etkisiz kalmıştır. Bu, ER stresi düzeltmesinin de lipogenez baskısı gibi TRF lehine asimetrik olduğunu gösteriyor. Mehl et al. (2024)'te ise karaciğerde HFD'ye bağlı glisemi artışıyla birlikte, artan protein sentez yüküne (immün infiltrasyon kaynaklı) yanıt olarak unfolded protein yanıtı ve ERAD aktivitesi indüklenmiştir — burada ER stresi, doğrudan bir lipid yükünden değil, **immün infiltrasyonun** getirdiği sekonder bir proteostatik yükten kaynaklanıyor gibi görünüyor; bu da ER stresinin tek bir tetikleyicisi olmadığını, farklı üst akış sinyallerinden (lipid fazlası vs inflamasyon) beslenebileceğini gösteriyor.

### 5. Sirkadiyen Saat

**Normal Fizyoloji:** Periferik dokularda (karaciğer, yağ, kas) hücre-otonom bir moleküler saat işler: **BMAL1** ve **CLOCK** heterodimeri, **Per** ve **Cry** genlerinin transkripsiyonunu aktive eder; biriken PER/CRY proteinleri kendi transkripsiyonlarını baskılayarak negatif geri besleme döngüsü oluşturur. **RORα** ve **REV-ERBα** ise BMAL1 transkripsiyonunu sırasıyla aktive/baskılayarak ikinci bir döngü katmanı ekler. Bu saat, beslenme zamanlaması (özellikle karaciğerde) tarafından güçlü şekilde senkronize edilir — yani "ne zaman yediğiniz," merkezi (SCN) saatten bağımsız olarak periferik saati doğrudan resetleyebilir.

**Açlıkta Ne Değişir:** Tsameret et al. (2023), bu yolağın belki de en net kanıtını sunuyor: aynı 8 saatlik TRF penceresi, yalnızca aktif faza denk gelip gelmemesine (E-TRF: ZT8-16 vs L-TRF: ZT16-24) göre karaciğer, yağ ve kas dokusunda tamamen farklı saat geni amplitüd ve faz profilleri üretiyor — E-TRF grubu Bmal1, Clock, Per1, Cry1, Rorα, Rev-erbα için daha ileri faz kayması ve daha yüksek amplitüdlü ritimler sergilerken, L-TRF bu güçlü senkronizasyonu sağlayamıyor. Szekely et al. (2026), bu hayvan bulgusunu insanda tamamlıyor: erken (eTRE, 08:00-16:00) ve geç (lTRE, 13:00-21:00) beslenme pencereleri arasında subkutan yağ dokusunda sirkadiyen ritim gösteren desatüraz/elongaz genlerinin (**FADS1, SCD1, ELOVL6**) ekspresyonu anlamlı şekilde farklılaşıyor — lTRE sonrası bu genlerin mRNA seviyeleri eTRE'ye göre daha yüksek kalıyor. Bu iki bulgu birlikte okunduğunda: sirkadiyen saat yalnızca "ne zaman uyanık/aktif olduğunuzu" değil, **lipid metabolizma enzimlerinin bazal ekspresyon düzeyini** de doğrudan belirliyor — yani zamanlama, kalori/makrobesin içeriğinden bağımsız bir mekanistik değişken olarak işliyor (detaylı tartışma için bkz. Çapraz-Tema B).

### 6. Browning ve Termojenez

**Normal Fizyoloji:** Beyaz yağ dokusu (WAT), uygun uyaranlar altında (soğuk, β3-adrenerjik sinyal, bazı beslenme müdahaleleri) "bejleşerek" kahverengi yağ dokusuna (BAT) benzer, çok-odacıklı lipid damlacıklı, mitokondri-zengin bir fenotip kazanabilir. Bu süreç **UCP1** (mitokondriyal iç membranda proton sızıntısı yaratıp ısı üretimini artıran ayrıştırıcı protein), **PRDM16** (bej/kahverengi hücre kaderini belirleyen ana transkripsiyon faktörü) ve **PGC-1α** (mitokondriyal biyogenezin ana koordinatörü) üçlüsü tarafından yönetilir. Klasik BAT'ta ayrıca **Cidea**, **Tfam**, **Elovl3**, **Dio2** (tiroid hormonu aktivasyonu üzerinden termojenezi destekler) ve **Errα**/**Atp5b**/**Cpt1** gibi mitokondriyal oksidasyon genleri de rol oynar.

**Açlıkta Ne Değişir:** Yang et al. (2023), mikrobiyota aracılı bir browning mekanizması gösteriyor: gün-aşırı açlık, inguinal WAT'ta PRDM16, UCP1 ve PGC-1α'yı dramatik şekilde artırıyor, ve bu etki tamamen **Akkermansia muciniphila** bağımlı — antibiyotikle flora temizlendiğinde browning yanıtı duruyor, Akkermansia kolonizasyonuyla tam olarak geri kazanılıyor (bkz. [[#9. Mikrobiyota-Metabolit Ekseni]]). Tsameret et al. (2023)'te ise termojenez sinyali **UCP2** üzerinden (BAT'a özgü UCP1 değil, daha genel bir ayrıştırıcı protein) izleniyor ve yalnızca erken-fazlı TRF'de (E-TRF) hem karaciğer, hem yağ, hem kas dokusunda birlikte yükseliyor. Ancak bu resmin karşı ucunda **yaşlanmanın getirdiği bir tavan etkisi** var: Yang and Liu (2024)'te orta yaşlı obez farelerde TRF, BAT'ta Ucp1/Elovl3/Dio2'yi belirgin şekilde artırırken, **yaşlı** obez farelerde bu termojenik gen indüksiyonunun hiçbiri gerçekleşmiyor — yazarlar bunu doğrudan "yaşlanmayla körelen termojenik kapasite" olarak yorumluyor. Ealey et al. (2024)'te de benzer bir tavan görülüyor: yaşlı farelerde IF, BAT'ta klasik termojenik genler (Ucp1, Cidea, Tfam) üzerinde hiçbir etki yaratmıyor, buna karşın mitokondriyal oksidasyon genleri (Errα, Atp5b, Cpt1) ve lipogenez-lipoliz döngü genleri (Scd1, Elovl5, Atgl) IF ile tersine çevrilebiliyor. Bu, "termojenez" adı altında birbirinden ayrılabilir en az iki alt-mekanizma olduğunu gösteriyor: (a) klasik UCP1-bağımlı ısı üretimi, yaşlanmayla birlikte fasting'e dirençli hale geliyor; (b) mitokondriyal oksidasyon kapasitesi ve lipid döngüsü (futile cycle, bkz. [[#1. Lipogenez ve Lipid Sentez Yolağı]]) ise yaşlı dokuda bile kısmen fasting'e duyarlı kalabiliyor.

### 7. Desatürasyon ve Elongasyon Enzimleri

**Normal Fizyoloji:** Doymuş yağ asitleri, **SCD1** (stearoyl-CoA desatüraz, palmitik/stearik asidi tekli doymamışa çevirir), **FADS1/FADS2** (delta-5/delta-6 desatüraz, çoklu doymamış yağ asidi [PUFA] sentezinin hız-kısıtlayıcı enzimleri) ve **ELOVL5/ELOVL6** (yağ asidi zincir uzatma enzimleri) tarafından işlenerek membran fosfolipid kompozisyonunu ve depolanan trigliseritlerin akışkanlığını belirler. Bu enzimlerin aktivitesi doğrudan ölçülmek yerine genellikle substrat/ürün yağ asidi oranlarından (dolaylı "enzim aktivite indeksleri") tahmin edilir.

**Açlıkta Ne Değişir:** Szekely et al. (2026) bu yolağın insanda en ayrıntılı kanıtını sunuyor: 2 haftalık eTRE, yalnızca kendi içinde (başlangıca göre) **ELOVL6 indeksinde düşüş**, **D5D/FADS1 ve D9D/SCD1 indekslerinde artış**, **D6D/FADS2 indeksinde azalma** yaratırken; lTRE'de yalnızca D5D/FADS1 indeksinde bir artış görülüyor — yani aynı sürede, aynı (izokalorik hedeflenen) kısıtlamada, yalnızca beslenme penceresinin saat diliminin değişmesi enzim aktivite profilini kalitatif olarak farklılaştırıyor. Doku düzeyinde bu farkın izi de var: lTRE sonrası subkutan yağ dokusunda FADS1, SCD1 ve ELOVL6 mRNA seviyeleri eTRE'ye göre anlamlı derecede daha yüksek kalıyor — yani genç/orta yaşlı insan yağ dokusunda bu enzimlerin bazal transkripsiyonel tavanı, günün hangi saatinde beslenildiğine bağlı. Bushman et al. (2026)'da ise aynı enzim ailesinden Scd1 ve Elovl5, yaşlı fare BAT ve WAT depolarında HFD tarafından baskılanıyor ve TRF tarafından (kısmen veya tamamen) restore ediliyor — yani bu enzimler yalnızca zamanlamaya değil, aynı zamanda **diyet-kaynaklı baskılanmaya karşı bir "restorasyon" sinyaline** de yanıt veriyor.

### 8. Adipoz Doku İnflamasyonu

**Normal Fizyoloji:** Sağlıklı yağ dokusunda makrofajlar M2-benzeri, anti-inflamatuar bir fenotipte bulunur. Obezite, adiposit hipertrofisi ve hücre ölümüyle birlikte, makrofajlar ölü adipositleri çevreleyen "taç-benzeri yapılar" (crown-like structures) oluşturur ve M1-benzeri, pro-inflamatuar bir fenotipe kayar; bu, **F4/80, CD11b, CD11c** gibi makrofaj markörlerinin ve **Tnfα, Il6, Mcp1** gibi sitokin/kemokinlerin yükselmesiyle karakterizedir.

**Açlıkta Ne Değişir:** Yang and Liu (2024), burada özellikle önemli bir ayrışma sunuyor: TRF, hem orta yaşlı hem yaşlı obez farelerin eWAT'ında crown-like yapıları ve makrofaj/sitokin genlerini (F4/80, cd11b, cd11c, Mcp1, yaşlılarda Tnfα) güçlü şekilde baskılıyor — **ama bu baskılama, adipoz doku ağırlığında veya adiposit boyutunda hiçbir değişiklik olmadan** gerçekleşiyor. Yazarlar bunu açıkça "adipoz doku inflamasyonu, doku kütlesi/hipertrofi değişikliğinden **bağımsız** olarak azaltılabilir" şeklinde yorumluyor. Ealey et al. (2024)'te ise tam tersi bir örüntü var: pWAT'ta hücresel düzeyde (ASPC, eozinofil) belirgin bir yeniden yapılanma olmasına rağmen, **bulk doku** düzeyinde ölçülen inflamasyon genlerinde (fibro-inflamasyon markörleri) hiçbir grup farkı bulunamıyor — yazarlar bunu, farelerin obezojenik değil normal diyette olmasına bağlıyor (bkz. Çapraz-Tema D). Hurza et al. (2025) ise inflamasyonun cinsiyete göre tamamen zıt yönlere gidebileceğini gösteriyor: margarin+IF kombinasyonu, adipoz IL-1β'yı hem erkek hem dişide azaltıyor, ama erkekte bu azalma sistemik bir enflamatuar patlamayla (lökosit sayısında %87 artış) birlikte gidiyor — yani lokal adipoz doku ölçümü ile sistemik enflamasyon durumu birbirini yansıtmayabiliyor.

### 9. Mikrobiyota-Metabolit Ekseni

**Normal Fizyoloji:** Bağırsak mikrobiyotası, konakçının enerji hasadını, bağırsak bariyer bütünlüğünü (tight junction proteinleri: **ZO-1, Occludin, Claudin**) ve dolaşımdaki metabolit havuzunu (kısa zincirli yağ asitleri, amino asitler) doğrudan etkiler. **Akkermansia muciniphila**, müsin-yıkıcı bir tür olarak bağırsak mukus tabakası bütünlüğü ve metabolik sağlıkla ilişkilendirilir.

**Açlıkta Ne Değişir:** Yang et al. (2023), bu ekseni uçtan uca gösteren en mekanistik çalışma: gün-aşırı açlık, fekal mikrobiyotada Akkermansia bolluğunu dramatik artırıyor; bu artış, ileum tight junction proteinlerinin (ZO-1, Occludin, Claudin-5) yukarı regülasyonu, bağırsak lipid emilim genlerinin (**FATP, CD36, DGAT, FASN**) baskılanması ve iWAT browning'i (UCP1, PRDM16, PGC-1α, bkz. [[#6. Browning ve Termojenez]]) ile birlikte gidiyor. Bu zincirin nedensel olduğu, antibiyotik ile flora temizlenip ardından Akkermansia'nın tekrar kolonize edilmesiyle **gösterilmiş**: flora temizliği IF'nin faydalarını büyük ölçüde ortadan kaldırıyor, Akkermansia gavajı bu faydaları tam olarak geri kazandırıyor. Zincirin bir diğer halkası arjinin metabolizması: IF ile fekal arjinin azalırken plazma arjinin artıyor, ve bu ikisi Akkermansia bolluğuyla neredeyse mükemmel bir negatif korelasyon (R=-0.983) gösteriyor; artan plazma arjinin, bağırsak epitelinde **PI3K/AKT** yolağını inhibe ederek Occludin ekspresyonunu artırıyor — yani bariyer güçlenmesinin moleküler bir aracısı olarak arjinin/PI3K-AKT ekseni öne çıkıyor.

### 10. Kas Protein Dengesi

**Normal Fizyoloji:** İskelet kası protein kütlesi, protein sentezi (mTOR-aracılı, beslenme/amino asit-duyarlı) ile protein yıkımı (ubikitin-proteazom ve otofaji-lizozom yolakları, açlık/kortikosteron-duyarlı) arasındaki dengeyle belirlenir.

**Açlıkta Ne Değişir:** Bu, derlemede protokole göre en tutarsız (ve klinik olarak en dikkat gerektiren) yolaklardan biri. Yang and Liu (2024)'te 8 haftalık TRF, hem orta yaşlı hem yaşlı obez farelerde yağ kütlesini değiştirmeden **yağsız (lean) kütleyi anlamlı şekilde azaltıyor** — yazarlar bunu genç fare literatürüyle (TRF'nin tipik olarak yağdan kilo verdirdiği) doğrudan çelişen, yaşa özgü bir bulgu olarak sunuyor. Soares et al (2025) ise protokoller arası doğrudan bir karşılaştırma sunuyor: aynı 4 haftalık süre içinde CR grubu kas liflerinde yırtılma ve sarkomer düzensizliği gösterirken, TRF grubu homojen ama **hipotrofik** (küçülmüş) lifler sergiliyor; buna karşın ADF ve ADMF grupları homojen ve **hipertrofik** (büyümüş) kas lifleri gösteriyor — en büyük kas lifi boyutuna ADMF ulaşıyor. Bu, aynı genel "kalori kısıtlaması" şemsiyesi altında, kısıtlamanın **sürekliliği** (günlük hafif kısıtlama [CR/TRF] vs. döngüsel tam açlık + refeeding [ADF/ADMF]) kas dokusunda taban tabana zıt sonuçlar doğurabildiğini gösteriyor — muhtemelen refeeding günlerindeki güçlü anabolik/insülin sinyali darbesinin (bkz. [[#3. İnsülin Sinyali ve Beta Hücre Sekresyonu]]) kompanzatuar bir kas protein sentezi penceresi açması nedeniyle.

### 11. Karaciğer Glikojen ve Steatoz Dinamiği

**Normal Fizyoloji:** Karaciğer, kısa süreli açlık boyunca kan glukozunu glikojenoliz yoluyla, uzayan açlıkta ise glukoneogenez yoluyla korur. Aşırı lipid akışı (HFD, fruktoz) karaciğerde ektopik trigliserit birikimine (steatoz) yol açar; bu süreç lipogenez artışı, yağ asidi oksidasyon kapasitesinin (beta-oksidasyon, mitokondriyal OXPHOS) yetersiz kalması ve/veya periferik yağ dokusundan aşırı yağ asidi akışıyla ilerler.

**Açlıkta Ne Değişir:** Bu yolakta bulgular arasında en keskin karşıtlık **cinsiyete göre** ortaya çıkıyor. Hurza et al. (2025)'te margarin+IF kombinasyonu, erkek farelerde karaciğer glikojenini %37 azaltırken trigliseriti **3.5 kat artırıyor** (ağır karaciğer yağlanması); aynı kombinasyon dişi farelerde ise karaciğer TAG'ini serbest-margarin grubuna göre %44 **azaltıyor**. Tsameret et al. (2023) ve Yang and Liu (2024)'te ise TRF, tutarlı biçimde karaciğer steatozunu ve fibrozis skorunu geriletiyor, NF-κB'yi baskılıyor — ancak bu çalışmalarda yalnızca erkek hayvan kullanılmış olması, cinsiyet etkisinin bu iki çalışmada test edilemediği anlamına geliyor. Soares et al (2025)'te ilginç bir istisna var: ADMF grubu, kontrol ve TRF gruplarına kıyasla **daha yüksek** karaciğer TAG'i gösteriyor — yani en agresif refeeding-sonrası açlık döngüsü, karaciğerde beklenmedik bir lipid birikimine yol açabiliyor, muhtemelen refeeding günündeki ani ve büyük kalori yüklemesinin karaciğere yönlendirdiği akut lipogenik dalga nedeniyle.

### 12. Substrat Oksidasyonu ve Metabolik Esneklik

**Normal Fizyoloji:** Metabolik esneklik, bir organizmanın tokluk-açlık geçişlerinde baskın substrat kullanımını (karbonhidrat ↔ yağ) verimli şekilde değiştirebilme kapasitesidir; solunum değişim oranı (**RER = VCO2/VO2**) bunun dolaylı bir göstergesidir (RER≈1.0 karbonhidrat, RER≈0.7 yağ oksidasyonuna işaret eder).

**Açlıkta Ne Değişir:** Conn et al. (2024), bu kavramın en temiz deneysel gösterimini sunuyor: 10 haftalık 5:2 IF, zayıf db/+ farelerde hem tok hem aç durumda RER'i düşürüp yağ asidi oksidasyonunu artırarak klasik "metabolik esneklik" kazanımını gösterirken, aynı protokol obez/T2D db/db farelerde **tam tersi yönde** işliyor — tok durumda RER yükseliyor (karbonhidrat oksidasyonuna kayma), bu da "metabolik inflexibility"nin fasting ile düzelmek yerine **kötüleşebileceğini** gösteriyor. Tsameret et al. (2023)'te ise zamanlama bu esnekliği modüle ediyor: E-TRF grubu, aktif fazdaki açlık periyodunda L-TRF'ye göre anlamlı derecede daha yüksek RER sergiliyor (daha dinamik karbonhidrat/yağ geçişi), inaktif fazda ise daha düşük RER (yağ oksidasyonuna kayma) gösteriyor — yani yalnızca fasting'in varlığı değil, fasting'in hangi sirkadiyen fazda gerçekleştiği de esneklik kalitesini belirliyor.

### 13. Hücresel Yaşlanma ve Kök Hücre Plastisitesi

**Normal Fizyoloji:** Adipoz doku kök/öncül hücreleri (ASPC), iki işlevsel alt popülasyona ayrılabilir: **DPP4+** (kendini yenileme kapasitesi yüksek, "stem-benzeri" havuz) ve **DPP4-** (adipojenik farklılaşmaya taahhütlü, daha yüksek adipojenik kapasiteye sahip havuz). Yaşlanmayla birlikte ASPC'lerde hücresel yaşlanma (senesens) markörleri olan **p16^INK4a** ve **p21** birikir; bu senesent hücreler kendi farklılaşma kapasitelerini kaybetmekle kalmaz, komşu hücrelere de parakrin olarak (SASP — senesens-ilişkili sekretuvar fenotip) zarar verir.

**Açlıkta Ne Değişir:** Ealey et al. (2024), bu alanda en detaylı mekanistik veriyi sunuyor. IF sonrası pWAT'ta artan Pdgfrα+ progenitör kümesi (Cluster 8), makalenin discussion kısmında özellikle **DPP4-negatif** olarak tanımlanıyor — yani IF, genel olarak daha fazla progenitör üretmiyor, kendini-yenileme havuzundan adipojenik-taahhüt havuzuna doğru **yönlü bir kompozisyon kayması** yaratıyor. Bu kaymanın fonksiyonel karşılığı in vitro gösteriliyor: IF-türevi ASPC'ler farklılaştırıldığında Adipoq ve Pparγ2 ekspresyonu ve lipid damlacığı birikimi artıyor, aynı zamanda p16^INK4a ve p21 anlamlı şekilde azalıyor — yani senesens freni en azından progenitör düzeyinde kısmen kırılabiliyor. Ancak bu kırılma seçici: aynı protokol iWAT'ta (subkutan) hiçbir ASPC değişikliği yaratmıyor, yalnızca pWAT'a (visseral) özgü kalıyor; ayrıca bulk doku düzeyinde senesens genlerinde hiçbir değişim yok — yani fren kırılması yalnızca belirli bir hücre alt tipinde gerçekleşiyor, dokunun geneline yayılmıyor.

### 14. Oksidatif Stres ve Antioksidan Savunma

**Normal Fizyoloji:** Reaktif oksijen türleri (ROS), normal mitokondriyal solunumun bir yan ürünüdür ve **SOD (süperoksit dismutaz)**, **katalaz**, **GPx (glutatyon peroksidaz)**, **GST (glutatyon-S-transferaz)** ve **G6PDH (glukoz-6-fosfat dehidrogenaz, NADPH üretimi üzerinden antioksidan kapasiteyi besler)** gibi enzimatik savunma sistemleriyle nötralize edilir. Lipid peroksitleri (**LOOH**) bu dengenin bozulduğu durumlarda membran hasarının bir göstergesi olarak birikir.

**Açlıkta Ne Değişir:** Hurza et al. (2025), bu yolağın en zengin ve en cinsiyet-ayrışmış veri setini sunuyor. Erkek farelerde margarin+IF, yağ dokusu LOOH'unu yüksek tutarken (oksidatif hasar devam ediyor) karaciğerde SOD'u artırıyor ama katalazı ve GST'yi baskılıyor — parçalı, tutarsız bir antioksidan yanıt. Dişi farelerde ise aynı kombinasyon karaciğer LOOH'unu dramatik şekilde düşürüyor (kontrole göre %56, MarAD'a göre %74) ve bunu SOD, GST (bazal düzeyin %88 üzerinde) ve GPx'in (bazalin %86 üzerinde) güçlü, tutarlı bir up-regülasyonuyla destekliyor. Bu, aynı oksidatif yükün altında, fasting'in antioksidan savunmayı harekete geçirme kapasitesinin cinsiyete göre nitel olarak farklı çalıştığını gösteriyor — erkekte savunma parçalı ve yetersiz kalırken, dişide koordineli ve etkili.

---

## Çapraz-Tema Başlıkları

### A. İnflamasyon ↔ İnsülin Direnci: Zincir Her Zaman Aynı Halkalardan Geçmiyor

Klasik model, adipoz doku inflamasyonunun (makrofaj infiltrasyonu, TNFα/IL-6 artışı) doğrudan insülin direncine yol açtığını varsayar. Ancak bu derlemedeki kaynaklar bu zincirin evrensel olmadığını gösteriyor. Ealey et al. (2024), Bapat ve ark. (2015)'e atıfla, **obeziteye bağlı** ve **yaşlanmaya bağlı** insülin direncinin farklı hücresel aktörler üzerinden işleyebileceğini öne sürüyor — obeziteye bağlı direnç büyük ölçüde makrofaj-kaynaklı inflamasyonla ilişkiliyken, yaşa bağlı direnç (örn. yağ-rezidan Treg kaybı üzerinden) bu eksenden bağımsız çalışabiliyor. Bu, Ealey'nin kendi bulgusunu açıklıyor: IF glukoz toleransını ve insülin duyarlılığını anlamlı şekilde iyileştiriyor, ama bulk doku inflamasyon genlerinde hiçbir değişiklik yaratmıyor — çünkü bu yaşlı-zayıf modelde iyileşme muhtemelen inflamasyon ekseninden değil, [[#13. Hücresel Yaşlanma ve Kök Hücre Plastisitesi|ASPC/eozinofil remodeling]] üzerinden ilerliyor. Buna karşın Yang and Liu (2024)'te (yaşlı+obez model) inflamasyon baskılanması çok güçlü ve tutarlı — bu da inflamasyon-insülin direnci zincirinin özellikle **obezite** zemininde daha baskın bir rol oynadığını düşündürüyor. Pratik çıkarım: "IF glukoz toleransını düzeltti" bulgusu tek başına hangi mekanizmanın devrede olduğunu söylemez; altta yatan fenotip (yaşlı-zayıf vs yaşlı-obez vs genetik-obez) farklı bir zincir aracılığıyla aynı sonuca ulaşabilir.

### B. Sirkadiyen Saat ↔ Lipid Metabolizması: Zamanlama Bir Değişken Değil, Bir Mekanizma

Bu derlemedeki en tutarlı çapraz-tema, beslenme zamanlamasının (erken vs geç) yalnızca davranışsal bir detay değil, kendi başına bağımsız bir mekanistik eksen olduğudur. Tsameret et al. (2023) (fare) ve Szekely et al. (2026) (insan), tür sınırlarını aşarak aynı mesajı veriyor: erken zamanlı beslenme penceresi (aktif/uyanıklık fazının erken kısmına denk gelen), geç pencereye kıyasla sistematik olarak daha güçlü metabolik faydalar (daha güçlü AMPK/ACC aktivasyonu, daha düşük FAS, daha belirgin desatüraz/elongaz indeks değişimleri, daha yüksek amplitüdlü saat gen ritimleri) üretiyor. Bu, aynı kalori kısıtlaması ve aynı beslenme penceresi genişliği altında bile, **saat diliminin kendisinin** bağımsız bir tedavi değişkeni olarak ele alınması gerektiğini gösteriyor — "TRF" tek bir müdahale değil, en az iki farklı (erken/geç) alt-müdahaledir.

### C. Plazma ↔ Doku Ayrışması: Sistemik Sessizlik, Lokal Gürültü

Birden fazla çalışma, sistemik/plazma ölçümlerinin doku-düzeyi değişiklikleri gizleyebileceğini gösteriyor. Szekely et al. (2026)'de eTRE ve lTRE arasında **plazma** lipidom düzeyinde hiçbir doğrudan fark yokken, aynı karşılaştırma **subkutan yağ dokusu** transkriptominde (FADS1, SCD1, ELOVL6) anlamlı farklar ortaya çıkarıyor. Ealey et al. (2024)'te bulk doku inflamasyon/senesens genlerinde fark yokken, tek-hücre (CyTOF) düzeyinde belirgin bir ASPC/eozinofil remodeling'i var. Yang and Liu (2024)'te plazma TAG/kolesterol değişmezken karaciğer ve adipoz dokuda güçlü moleküler değişiklikler var. Bu örüntü, derlemenin metodolojik bir uyarısı olarak okunmalı: yalnızca plazma/serum ölçümlerine dayanan çalışmalar, gerçek doku-düzeyi remodeling'i (özellikle hücre alt-popülasyonu düzeyinde olanları) kaçırma riski taşıyor.

### D. Genotip ↔ Diyet Stresi Etkileşimi

Mehl et al. (2024), bu etkileşimin en sistematik kanıtını sunuyor: aynı standart açlık protokolü altında, üç fare suşundan yalnızca Balb/c, HFD ile glisemik bozulma gösteriyor; C57Bl/6 ve DBA/2 etkilenmiyor. Bu, "diyet stresi" tek başına bir değişken değil, **genotipin diyet stresine verdiği yanıtın** asıl belirleyici olduğunu gösteriyor. Conn et al. (2024) bu temayı genişletiyor: leptin reseptörü mutasyonu (db/db) tek başına, aynı fasting protokolüne verilen yanıtı taban tabana zıt yöne çeviriyor (bkz. [[#12. Substrat Oksidasyonu ve Metabolik Esneklik]]). Bu iki çalışma birlikte, kişiselleştirilmiş fasting yaklaşımlarının genotipik arka planı göz ardı edemeyeceğini gösteriyor.

### E. Protokol Dozu ↔ Doku Yanıt Eşiği

Soares et al (2025), tek bir çalışma içinde beş farklı "doz" (CON, CR, TRF, ADF, ADMF) karşılaştırarak bir doz-yanıt eğrisi sunuyor: TRF (16 saat açlık) en hafif uçta kalıp en düşük kilo kaybı/en yüksek adipozite indeksini gösterirken, ADF ve ADMF (24 saat tam/kısmi açlık) en güçlü kilo kaybı ve glisemik iyileşmeyi sağlıyor — ama kas dokusunda ADF/ADMF hipertrofi yaratırken TRF hipotrofi yaratıyor (bkz. [[#10. Kas Protein Dengesi]]). Kilic-Erkek (2025)'te ise 8:16 (TRF) ve 5:2 protokolleri karşılaştırıldığında, kilo kaybı 5:2'de daha erken başlarken, lipogenez/TG/kolesterol baskısında 8:16 sistematik olarak daha üstün çıkıyor. Bu iki çalışma birlikte, "daha uzun/daha sık açlık = her zaman daha iyi" varsayımının yanlış olduğunu, her doku ve her çıktının kendi doz-yanıt eğrisine sahip olabileceğini gösteriyor.

### F. Yaşlanma ↔ Doku Yanıt Kapasitesi

Yang and Liu (2024) ve Ealey et al. (2024), her ikisi de yaşlı hayvan modelleri kullanarak aynı temayı farklı açılardan doğruluyor: yaşlanma, fasting'e yanıt verme kapasitesini **azaltmıyor**, onu **seçici olarak** azaltıyor. Termojenik/BAT yanıtı yaşlılıkta büyük ölçüde köreliyor (bkz. [[#6. Browning ve Termojenez]]), ama inflamasyon baskılanması (Yang and Liu (2024)) veya ASPC senesens kırılması (Ealey et al. (2024)) gibi diğer yanıtlar yaşlı dokuda hâlâ mümkün. Bu, "yaşlı doku fasting'e yanıt vermiyor" gibi kaba bir genellemenin yanlış olduğunu, bunun yerine **hangi alt-mekanizmanın** yaşla birlikte kaybolduğunun, hangisinin korunduğunun haritalanması gerektiğini gösteriyor.

### G. Depot-Spesifiklik: Yağ Dokusu Tek Bir Organ Değildir

Neredeyse her preklinik kaynak bu temayı bir şekilde doğruluyor: Bushman et al. (2026)'da BAT, Gon-WAT ve Ing-WAT üçü de aynı TRF protokolüne birbirinden tamamen farklı transkriptomik imzalarla yanıt veriyor; Ealey et al. (2024)'te IF etkisi yalnızca pWAT'a özgü, iWAT tamamen duyarsız; Kilic-Erkek (2025)'te mezenterik yağ her iki protokolle de azalırken retroperitoneal/gonadal yağ yalnızca 5:2 ile azalıyor; Yang et al. (2023)'te browning etkisi özellikle inguinal (subkutan) depoda görülüyor. Bu tutarlılık, "adipoz doku" teriminin tek bir birim gibi ele alınmasının artık savunulamaz olduğunu gösteriyor — her analiz, hangi depodan bahsedildiğini açıkça belirtmek zorunda.

---

## Genel Değerlendirme

**Açlık türüne göre:** TRF (zaman kısıtlı, günlük döngü), ADF/5:2 (gün-aşırı veya haftalık tam açlık) ve ADMF (modifiye, kısmi kalori ile) birbirinden niteliksel olarak farklı mekanizma profilleri üretiyor. TRF'nin gücü **zamanlama** (sirkadiyen hizalama) üzerinden geliyor — bu yüzden erken/geç TRF ayrımı bu protokolde özellikle kritik (Tsameret et al. (2023), Szekely et al. (2026)). ADF/5:2'nin gücü ise daha çok **toplam kalori kısıtlaması ve döngüsel refeeding şoku** üzerinden geliyor — bu da kas dokusunda (hipertrofi, Soares et al (2025)) ve yağ dokusu boyut dağılımında TRF'den farklı, bazen ondan daha güçlü sonuçlar doğurabiliyor. CR (sürekli hafif kısıtlama) ise metabolik olarak faydalı olsa da kas dokusu bütünlüğü açısından en kırılgan protokol gibi görünüyor.

**Açlık süresine göre:** Derlemedeki süreler 2 hafta (Szekely et al. (2026)) ile 16 hafta (Hurza et al. (2025)) arasında değişiyor. Kısa süreli (2-5 hafta) çalışmalar genellikle erken transkripsiyonel/enzimatik değişiklikleri yakalıyor (Szekely et al. (2026), Tsameret et al. (2023) — 5 hafta), orta süreli (8-10 hafta) çalışmalar doku yeniden yapılanmasını ve immün profil değişikliklerini gösterebiliyor (Yang and Liu (2024), Ealey et al. (2024), Kilic-Erkek (2025), Conn et al. (2024)), uzun süreli (16 hafta, Hurza et al. (2025)) ise kronik/kümülatif hasarın (karaciğer fibrozis benzeri değişiklikler, kalıcı oksidatif dengesizlik) ortaya çıkabileceği bir pencere sağlıyor. Genel olarak süre arttıkça, protokoller arası ve cinsiyetler arası ayrışma azalmak yerine **derinleşiyor** gibi görünüyor.

**Diyet kompozisyonuna göre:** Fruktoz (Kilic-Erkek (2025)), yüksek yağ/lard (Bushman et al. (2026), Yang and Liu (2024), Tsameret et al. (2023), Yang et al. (2023)) ve margarin/trans yağ (Hurza et al. (2025)) gibi farklı "stresör" diyetler, açlığın koruyucu etkisinin görünürlüğünü büyük ölçüde belirliyor: tek başına standart chow diyetinde açlığın etkisi çoğu zaman ölçülemeyecek kadar küçük kalırken (Ealey et al. (2024)'te bulk doku genlerinde değişim yok), güçlü bir lipogenik/inflamatuar stresör (fruktoz, yüksek yağ) eklendiğinde açlığın "tersine çevirme" kapasitesi çok daha net ortaya çıkıyor (Kilic-Erkek (2025)). Bununla birlikte, benzer diyet kompozisyonlarının farklı çalışmalarda farklı sonuçlar doğurması (Bushman et al. (2026) vs Yang and Liu (2024), her ikisi de lard-bazlı HFD), diyet kompozisyonunun **tek başına** açıklayıcı olmadığını, cinsiyet ve tür-suşuyla etkileşime girdiğini gösteriyor.

**Bireysel faktörler (genotip, yaş, tür/insan-hayvan):** Genotip (Mehl et al. (2024), Conn et al. (2024)), yaş (Yang and Liu (2024), Ealey et al. (2024)) ve cinsiyet (Hurza et al. (2025)) her biri bağımsız olarak fasting yanıtının **yönünü** değiştirebiliyor — yalnızca büyüklüğünü değil. İnsan verisi (Szekely et al. (2026)) şimdilik yalnızca zamanlama ekseninde ve tek cinsiyette (kadın, çoğunlukla postmenopozal) mevcut; hayvan modellerindeki genotip/yaş/cinsiyet etkileşimlerinin insanda ne ölçüde geçerli olduğu büyük ölçüde açık bir soru olarak kalıyor.

---

## Bibliyografya

- Bushman, T., Su, H., & Chen, X. (2026). Impact of time-restricted feeding on metabolic health and adipose tissue metabolism in aged female mice with high-fat diet-induced obesity. _Journal of Physiology_, 604(3), 1137–1157.
- Conn, M. O., Marko, D. M., & Schertzer, J. D. (2024). Intermittent fasting increases fat oxidation and promotes metabolic flexibility in lean mice but not obese type 2 diabetic mice. _American Journal of Physiology-Endocrinology and Metabolism_, 327, E470–E477.
- Ealey, K. N., Togo, J., Lee, J. H., Patel, Y., Kim, J.-R., Park, S.-Y., & Sung, H.-K. (2024). Intermittent fasting promotes rejuvenation of immunosenescent phenotypes in aged adipose tissue. _GeroScience_, 46, 3457–3470.
- Hurza, V. V., Bayliak, M. M., Vatashchuk, M. V., Sorochynska, O. M., Lylyk, M. P., Abrat, O. B., Gospodaryov, D. V., Storey, K. B., & Lushchak, V. I. (2025). Intermittent fasting partially alleviates dietary margarine-induced morphometrical, hematological, and biochemical changes in female mice, but not in males. _Biochemistry Research International_, 2025, Article 2163104.
- Kilic-Erkek, Ö. (2025). 8:16 time restricted feeding and 5:2 intermittent fasting exert beneficial metabolic effects on lipid profile and endoplasmic reticulum stress in high fructose-consuming rats.
- Mehl, F., et al. (2024). A multiorgan map of metabolic, signaling, and inflammatory pathways that coordinately control fasting glycemia in mice.
- Soares, et al. (2025). Evaluation of the effect of different intermittent fasting regimens on metabolic parameters in healthy male Wistar rats.
- Szekely, et al. (2026). Impact of intended isocaloric early versus late time-restricted eating on plasma lipidome in women with overweight or obesity.
- Tsameret, S., et al. (2023). Effect of early vs. late time-restricted high-fat feeding on circadian metabolism and weight loss in obese mice.
- Yang, Y., & Liu, D. (2024). Impacts of time-restricted feeding on middle-aged and old mice with obesity. _Journal of Physiology_, 602(22), 6109–6123.
- Yang, et al. (2023). Gut microbiota mediates the anti-obesity effect of intermittent fasting by inhibiting intestinal lipid absorption.