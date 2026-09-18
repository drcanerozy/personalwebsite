**Wisessaowapak et al. (2026)-A nutrient-responsive AMPK/TBK1 circuit restricts adipocyte catabolism**

> **Hızlı Künye:** Karma (Fare + hücre kültürü + insan doku) | Akut açlık 24-72sa + kronik amlexanox/AICAR tedavisi (2-3 hafta) | Doku: iWAT/eWAT/karaciğer - AMPK/TBK1 ekseni, adiposit katabolizma freni.

### Metodolojik Künye

**Kaynak:** Wisessaowapak et al. 2026, _JCI Insight_ 11(9):e200168 — "A nutrient-responsive AMPK/TBK1 circuit restricts adipocyte catabolism"

**Tür/Model:** Hayvan (erkek C57BL/6J fare) + hücre kültürü (3T3-L1 adipositler, HEK293T, mouse iWAT'tan izole primer SVF-preadiposit) + insan doku verisi (biyopsi/scRNA-seq, retrospektif — insan RCT değil)

**N / Grup:**

- Hayvan çalışmaları: WT, Prkaa1/2AKOPrkaa1/2^{\text{AKO}} Prkaa1/2AKO (AMPK-KO), Tbk1AKOTbk1^{\text{AKO}} Tbk1AKO (TBK1-KO), Ppargc1aAKOPpargc1a^{\text{AKO}} Ppargc1aAKO (PGC1α-KO); fasting süresi/doz gruplarına göre n=2–10 arası (şekil bazlı değişken)
- Dual tedavi kohortu: HFD kontrol, amlexanox (AMX), AICAR (AI), AMX+AI; n=8–12 (glukoz tolerans/AUC), n=3–6 (karaciğer TG)
- İnsan verisi: farklı BMI aralıklarındaki (20-30, 30-40, 40-50) bireylerden subkutan ve viseral adipoz doku scRNA-seq (halka açık GEO verisi, GSE176171 kaynaklı)

**Süre:** Akut fasting 24-48 saat (çoğu deney) veya 72 saat (uzatılmış, Tbk1AKOTbk1^{\text{AKO}} Tbk1AKO); kronik tedavi: amlexanox 2 hafta (tek başına) veya 21 gün (dual AMX+AICAR kombinasyonu)

**Karşılaştırma:** ND vs HFD; WT vs KO (AMPK/TBK1/PGC1α-AKO); vehicle vs AICAR vs amlexanox vs AMX+AICAR kombinasyonu; tüm karşılaştırmalarda pair-feeding kontrolü ile amlexanoxun anorektik etkisi dışlanmış

**Doku/Ölçüm:** iWAT, eWAT, karaciğer (qPCR, immunoblot, histoloji/H&E, F4/80 IHC ile CLS kantifikasyonu); plazma NEFA/gliserol/insülin; ChIP-qPCR ve luciferase reporter (promotor mekanizması); ex vivo insülin stimülasyonu (eWAT explant); scRNA-seq (fare ve insan adiposit)

**Çalışma tipi:** Preklinik (hayvan + hücre kültürü), insan verisi yalnızca tanımlayıcı/korelatif doku ekspresyon analizi — klinik girişim/RCT değil

**Sınırlılık/Dikkat:**

- Yalnızca erkek fareler kullanılmış (yazarlar gerekçe olarak fenotipik varyasyonun azaltılmasını belirtmiş) → cinsiyet-spesifik yanıt bu çalışmadan çıkarılamaz
- Amlexanox, TBK1 dışında IKKε'yi de inhibe ediyor; yazarlar bunu açıkça belirtmiş — gözlenen etkilerin bir kısmı IKKε üzerinden olabilir
- Sistemik β-hidroksibütirat düzeyi TBK1 kaybından etkilenmemiş (veri gösterilmemiş) → bulgular lokal adipoz enerji sensingi ile sınırlı, sistemik ketojenik akışa genellenemez
- İnsan verisi korelatif/kesitsel (BMI ile TBK1 ekspresyonu ilişkisi) — nedensellik kurulamaz
- Baş yazar (ARS) amlexanox ile ilgili patent sahibi ve bir biyoteknoloji şirketinin kurucusu — potansiyel çıkar çatışması bildirilmiş

Açlık ve obezite (besin bolluğu) stress spektrumunun iki farklı ucunda yer alsa da, adiposit düzeyinde ortak bir "fren" mekanizması olan **TBK1 (TANK-binding kinase 1)** ve **AMPK** arasındaki resiprokal (karşılıklı) geribildirim döngüsünü ele alan bu moleküler biyoloji veri seti, akademik analizleriniz için parametre bazında kategorize edilerek Türkçeye çevrilmiş ve sistematik bir yapıya kavuşturulmuştur.

## 1. METODOLOJİ VE DENEYSEL MODEL (METHODS)

### Hayvan Modelleri (UCSD Laboratuvarı)

- **Arka Plan:** Fenotipik varyasyonu minimize etmek amacıyla **erkek C57BL/6J** fareler kullanılmıştır.
    
- **Genetik Nakavt (KO) Modelleri:** Laboratuvarda üretilen adiposit-spesifik 3 ana KO modeli:
    
    1. **$Prkaa1/2^{\text{AKO}}$:** Adiposit-spesifik AMPK $\alpha1/\alpha2$ Nakavt.
        
    2. **$Tbk1^{\text{AKO}}$:** Adiposit-spesifik TBK1 Nakavt.
        
    3. **$Ppargc1a^{\text{AKO}}$:** Adiposit-spesifik PGC1$\alpha$ Nakavt.
        
- **Diyet ve Müdahale:** Standart laboratuvar yemi (chow) veya **%60 yağ içerikli Yüksek Yağlı Diyet (HFD)**. Açlık çalışmaları 24-72 saat tekli barındırmada su serbest şekilde yapılmıştır.
    

### Hücre Kültürü ve Farmakolojik Ajanlar

- **Modeller:** 3T3-L1 adipositleri, HEK293T hücreleri ve fare iWAT dokusundan izole edilen Stromal Vasküler Fraksiyon (SVF) kaynaklı primer preadipositler.
    
- **Kullanılan Ajanlar:**
    
    - _AMPK Agonistleri:_ AICAR (İn vivo: 100-500 mg/kg i.p. / İn vitro: 500 $\mu\text{M}$) ve PF-739 (10 $\mu\text{M}$).
        
    - _AMPK İnhibitörü:_ Compound C (10 $\mu\text{M}$).
        
    - _TBK1 İnhibitörü:_ Amlexanox (İn vivo: sub-optimal 25 mg/kg gavage / İn vitro: 50 $\mu\text{M}$).
        
- **Çift Besleme (Pair-feeding) Kontrolü:** Amlexanox'un anorektik (iştah kesici) etkisini dışlamak için, kontrol grupları amlexanox grubunun bir gün önce tükettiği yem miktarı kadar beslenmiştir.
    

## 2. AÇLIK ENERJİ STRESİNDE AMPK/TBK1 AKTİVASYON MEKANİZMASI

Obezitede inflamasyonla tetiklendiği bilinen TBK1'in, açlık esnasında da iWAT ve eWAT depolarında paradoksal olarak indüklendiği saptanmıştır.

```
[Açlık / Enerji Stresi] ➔ ⬆ AMP/ATP Oranı ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ⬇
       │                                                                                │
       ▼                                                                                │
  p-Thr172 AMPK Aktivasyonu                                                             │
       │                                                                                │
       ▼                                                                                │
  Ppargc1a (PGC1α) Ekspresyonu ──► PGC1α/NRF1 Transkripsiyonel Kompleksi                │
                                                │                                       │
                                                ▼                                       │
                                   Tbk1 Gen Promotörüne Bağlanma                        │
                                                │                                       │
                                                ▼                                       │
                                        Tbk1 mRNA ve Protein ⬆                          │
                                                │                                       │
                                                ▼                                       │
                                     p-Ser172 TBK1 Aktivasyonu                          │
                                                │                                       │
                                                └─► (Negatif Geribildirim Freni) ───────┘
```

### A. Transkripsiyonel Yolak: AMPK $\rightarrow$ PGC1$\alpha$ $\rightarrow$ NRF1 $\rightarrow$ TBK1

- **Açlık Yanıtı:** 24-48 saatlik açlık; iWAT ve eWAT'ta _Tbk1_ mRNA, total TBK1 protein ve **p-Ser172 TBK1 (aktif)**seviyelerini, p-Thr172 AMPK aktivasyonu ve lipoliz geni _Pnpla2_ (ATGL) ile eş zamanlı olarak artırır.
    
- **AMPK Bağımlılık:** AICAR veya PF-739 ile farmakolojik aktivasyon _Tbk1_ ve _Ppargc1a_ mRNA'sını uyarır. Compound C veya siRNA ile AMPK knocking-down yapıldığında ya da **$Prkaa1/2^{\text{AKO}}$ farelerde açlık uygulandığında _Tbk1_ ve _Pnpla2_ indüksiyonu tamamen bloke olur.** (AMPK, TBK1 uyarımı için şarttır).
    
- **Transkripsiyonel Kontrol (Stabilite Değil):** Aktinomisin D/mRNA yarı ömür testleri, AMPK'nın _Tbk1_ mRNA stabilitesini değiştirmediğini, doğrudan transkripsiyonu uyardığını; sikloheksimid testi ise _de novo_ (yeni) protein sentezinin zorunlu olduğunu göstermiştir.
    
- **PGC1$\alpha$ ve NRF1 Zorunluluğu:** * Promotör analizleri, _Tbk1_ lokusunda bir **NRF1 bağlama motifi**saptamıştır (ChIP-seq ile doğrulanmıştır).
    
    - **$Ppargc1a^{\text{AKO}}$** modellerinde açlık veya AICAR, _Tbk1_ ekspresyonunu artıramamıştır.
        
    - 3T3-L1 hücrelerinde _Nrf1_ siRNA ile susturulduğunda, PF-739 kaynaklı _Tbk1_ artışı baskılanmıştır.
        
    - _Luciferase Reporter_ testi; WT AMPK ve PGC1$\alpha$ ko-ekspresyonunun promotör aktivitesini artırdığını, Kinase-Dead (enaktif) AMPK mutantının ise bu indüksiyonu yok ettiğini kanıtlamıştır.
        

### B. Resiprokal Ultra-Kısa Geribildirim Döngüsü (Feedback Loop)

TBK1, nutrient stresi altında kontrolden çıkan bir katabolizmayı engellemek için **AMPK üzerine basılan bir fren (brake)** görevi görür:

- **Tbk1AKOTbk1^{\text{AKO}} Tbk1AKO** adipositlerinde, AMPK sinyal yolağı (p-Thr172 AMPK) ve doğrudan downstream hedefleri (p-Ser79 ACC, p-S792 Raptor) WT kontrol grubuna göre **çok daha yüksek ve sürdürülebilir (sustained)** seviyede kalır.
- Ayrı bir deneyde, PF-739 ile zaman-bağımlı tedavi edilen WT 3T3-L1 hücrelerinde AMPK aktivasyonuna eşlik eden downstream hedefler arasında **p-S79 ACC, p-S555 ULK1 ve p-S792 Raptor** fosforilasyonu ile birlikte TBK1 fosforilasyonu ve protein düzeyinde artış gözlenmiştir.
- TBK1 baskılandığında AMPK üzerindeki tonik inhibitör etki kalkar.
    

## 3. OBEZİTENİN AÇLIK SİNYALİ ÜZERİNDEKİ YIKICI ETKİSİ

Obezite, bu hassas nutrient-sensing (besin-algılama) mekanizmasını tamamen işlevsiz hale getirir.

- **Fenotipik Direnç:** Açlık esnasında yağsız fareler hızla ağırlık, iWAT, eWAT ve karaciğer kütlesi kaybederken; obez fareler (HFD) bu kütle kayıplarına direnç gösterir (Açlık katabolizması baskılanmıştır).
    
- **Sinyal Yolağı Bozulması:** Yağsız farelerde açlık AMPK'yı (p-T172 AMPK, p-S79 ACC) ve eş zamanlı olarak TBK1 eksenini (_Tbk1, Ppargc1a, Pnpla2_) güçlü şekilde aktive eder. **Obez farelerde ise açlık AMPK'yı tam olarak aktive edemez; bazal TBK1 (p-S172) ve total protein seviyeleri kronik inflamasyona bağlı olarak zaten yüksek seyretmekte ve açlıkla daha da artmamaktadır**, bu da AMPK-TBK1 dengesinde obezite lehine bir kayma olduğunu göstermektedir.
    
- **İnflamatuar Kilitlenme:** İnflamatuar kemokin _Ccl2_ açlıkla yağsız farelerde baskılanırken obez farelerde yüksek kalır. Tek hücre RNA-seq (scRNA-seq) verileri obez eWAT adipositlerinde yüksek bazal _Tbk1_ doğrulamıştır.
    
- **İnsan Translasyonu:** Farklı BMI değerlerine sahip bireylerden alınan biyopsilerde, **yüksek BMI'lı (obez/kilolu) insanların hem subkutan hem viseral yağ dokusu adipositlerinde TBK1 ekspresyonunun kronik olarak yüksek olduğu** gösterilmiştir (HFD fare modeliyle tam uyum).
    
- **AICAR Direnci:** Obez farelere 500 mg/kg AICAR verilmesi bile AMPK'yı tam aktive edemez; kronik TBK1 yüksekliği, AMPK aktivasyonunu antagonize eder.
    

## 4. IN VIVO TBK1 İNHİBİSYONU VE NAKAVTININ AÇLIK ADAPTASYONUNA ETKİLERİ

TBK1 freninin farmakolojik (Amlexanox) veya genetik ($Tbk1^{\text{AKO}}$) olarak kaldırılması, açlık derinliğini ve lipid mobilizasyonunu dramatik olarak artırır.

### A. Sub-optimal Amlexanox Tedavisi (Yağsız Fareler)

- **Kütle Dağılımı:** 24 saatlik açlıkta, amlexanox uygulanan fareler (çift besleme kontrolüne rağmen) daha fazla vücut ağırlığı, iWAT ve eWAT kütlesi kaybetmiştir.
    
- **Lipoliz Patlaması:** Toklukta bazal lipolizi baskılayan amlexanox, **açlık esnasında dolaşımdaki NEFA ve gliserol seviyelerinde en yüksek zirve değerleri** açığa çıkarmıştır (Baskılanmamış güçlü lipoliz). iWAT'ta _Pnpla2_ ve _Lipe_(HSL) aşırı indüklenmiştir.
    
- **Gen Ekspresyonu:** Lipojenik genler (_Acaca, Fasn_) ve inflamatuar markerlar (_Tnf$\alpha$, Ccl2_) tamamen baskılanırken; _Ppargc1a_ ve _Ppar$\alpha$_ tavan yapmıştır. Protein düzeyinde p-T172 AMPK ve p-S79 ACC artmış, inhibitör p-S485 AMPK baskılanmıştır.
    

### B. $Tbk1^{\text{AKO}}$ Farelerde 72 Saatlik Uzatılmış Açlık

- **Doku Seçiciliği:** $Tbk1^{\text{AKO}}$ fareleri açlıkta **lean (kas/yağsız) kütleyi mükemmel korurken, tamamen fat (yağ) kütlesinden kaybetmiştir** (Azalmış iWAT/eWAT, fırlayan plazma NEFA ve gliserol).
    
- **Karaciğer Koruması:** Yağ dokusundan kaçan lipidlere rağmen, $Tbk1^{\text{AKO}}$ farelerinin karaciğer ağırlığı ve **hepatik trigliserid (steatoz) birikimi anlamlı derecede düşük kalmıştır** (Gelişmiş lipid kullanımı).
    
- **Mitokondriyal Yeniden Modelleme:** Aç bırakılan $Tbk1^{\text{AKO}}$ farelerinin iWAT dokusunda mitokondriyal Oksidatif Fosforilasyon (OXPHOS) kompleks proteinleri, özellikle **Kompleks IV ve Kompleks V**belirgin şekilde artmıştır (Artmış oksidatif kapasite).
    

## 5. DUAL TERAPİ: TBK1 İNHİBİSYONU (AMLEXANOX) + AMPK AKTİVASYONU (AICAR) COOPERATIVITY

Tek başına AMPK aktivasyonu kompansatuar (dengeleyici) frenleri (TBK1 gibi) devreye soktuğundan, **Amlexanox (25 mg/kg/gün) ve AICAR (100 mg/kg/2 günde bir)** sub-optimal kombine tedavisi obez (HFD) farelerde sinerjik bir metabolik devrim yaratmıştır.

### A. Sistemik ve Histolojik İyileşmeler

|**Parametre**|**HFD Kontrol**|**Tek Başına Ajanlar (Amlexanox / AICAR)**|**Dual Terapi (Amlexanox + AICAR)**|
|---|---|---|---|
|**Vücut Ağırlığı**|Sürekli Artış / Obezite|Minimal veya Geç Kilo Kaybı (18. Gün)|**14. Günde Başlayan Erken ve En Belirgin Kilo Kaybı**|
|**Doku Kütleleri**|İleri Derecede Adipozite & Karaciğer Büyümesi|Ilımlı Azalma|**iWAT, eWAT ve Karaciğer Kütlesinde Maksimum Düşüş**|
|**Glikoz Toleransı & İnsülin**|İnsülin Direnci / Yüksek Eğri (AUC)|Hafif İyileşme|**Mükemmel Glikoz Toleransı, Minimum AUC ve İnsülin Seviyeleri**|
|**Lipid Mobilizasyonu**|Bozuk / Adiposit Hipertrofisi|Orta Düzey Gliserol Artışı|**En Yüksek Plazma Gliserolü ve Maksimum Karaciğer TG Düşüşü**|
|**Adiposit Morfolojisi**|Dev Adipositler (Hipertrofi)|Ilımlı Küçülme|**Tamamen Sol Sağa Kaymış, Küçük ve Metabolik Sağlıklı Adipositler**|
|**Hepatik Histoloji**|Ağır Steatoz, Balonlaşma, İnfiltrasyon|Parsiyel Düzelme|**Tamamen Restore Edilmiş Karaciğer Mimarisi, Sıfıra Yakın Yağ**|
|**Makrofaj Yükü (F4/80)**|eWAT/iWAT'ta Yoğun Kronsu Yapılar (CLS)|Ilımlı Azalma|** Crown-Like Structures (CLS) Dokulardan Tamamen Temizlendi**|

### B. Moleküler Yolak Restorasyonu (Doku ve Karaciğer Düzeyi)

- **Yağ Dokusu (iWAT/eWAT):** Baskılanmış olan _Ppargc1a_ ve _Glut4_ en güçlü seviyede dual terapi ile restore edilmiştir. Lipojenik gen (_Me1, Acaca, Fasn_) ekspresyonları tamamen kapatılmıştır. Protein düzeyinde, kombinasyon grubu eWAT'ta **p-T172 AMPK ve p-S79 ACC'yi tam olarak restore ederken, inhibitör p-S485 AMPK ve p-S172 TBK1'i tamamen söndürmüştür**.
    
- **İnsülin Sinyalizasyonu Aktivasyonu:** HFD ile tamamen körelen insülin uyarımlı **p-Y1150/1151 $IR\beta$(İnsülin Reseptörü)** ve downstream **p-S473 Akt** sinyal iletimi, dual kombinasyon tedavisiyle en üst düzeyde (neredeyse normal sağlıklı seviyeye) geri döndürülmüştür. Yağ dokusu insüline yeniden duyarlı hale gelmiştir.
    
- **Karaciğer Sağlığı:** Karaciğerde _Tbk1_, lipid çeper proteini _Plin1_ ve lipojenik master regülatör _Srebf1_ (SREBP1c) ekspresyonları en güçlü şekilde dual grupta düşürülmüştür. Hepatik fibrozis markerları (_Col1a1, Timp1_) ve ER (Endoplazmik Retikulum) stres transkripti (_Ddit3 / CHOP_) tamamen atenüe edilerek (azaltılarak) karaciğer sağlığı kombine tedaviyle tam korumaya alınmıştır.
    

### Akademik Çıkarım ve Model Özeti (Academic Takeaway)

Bu çalışma, adiposit enerji metabolizmasının yönetiminde hayati bir **"AMPK-TBK1 Kontrol Ekseni"**tanımlamaktadır. Akut açlıkta AMPK, PGC1$\alpha$/NRF1 transkripsiyonel modülü üzerinden _Tbk1_'i aktive ederek katabolizmanın derinliğini sınırlayan evrimsel bir fren mekanizması (TBK1) kurar.

Ancak obezitede, kronik düşük dereceli inflamasyon bu freni (TBK1) kalıcı olarak kilitler; bu durum AMPK'yı tonik olarak inhibe ederek yağ dokusunu metabolik esneklikten yoksun, insüline dirençli, hipertrofik ve fonksiyonel olarak işlevsiz bir kısırdöngüye sokar. Farmakolojik olarak TBK1 freninin kaldırılması (Amlexanox) ile AMPK aktivasyonunun (AICAR) kombine edilmesi, obezitenin yarattığı bu sinyal blokajını kırarak adipoz dokunun sağlıklı yeniden modellenmesini (remodeling), ektopotik lipidlerin temizlenmesini ve sistemik glikoz homeostazının tam restorasyonunu sağlayan oldukça güçlü bir terapötik sinerji doğurmaktadır.

_Not: İncelediğimiz bu son makale ile ilettiğiniz serinin bu etabını tamamlamış bulunuyoruz. Yeni bir veri seti veya analiz talebiniz olduğunda sıradakiyle devam edebiliriz._