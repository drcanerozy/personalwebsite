**Defour et al. (2020) - Transcriptomic signature of fasting in human adipose tissue**

> **Hızlı Künye:** Karma (İnsan + Fare) | İnsan: 26sa açlık, n=11 (transkriptom) / Fare: 16sa açlık, n=8/grup, erkek | Doku: İnsan subkutan sWAT vs fare epididimal (visseral) yağ - tür arası transkriptomik karşılaştırma.

### Metodolojik Künye

**Tür/Model:** Karma tasarım — (1) İnsan: 40-70 yaş arası, BMI 22-30 kg/m², sağlıklı gönüllüler (kohortun çoğunluğu kadın); (2) Hayvan: 3-4 aylık erkek yabani tip (WT) C57Bl/6J fare

**N / Grup:**

- İnsan (FASTING çalışması): 24 gönüllü dahil edildi (23'ü tamamladı); plazma metabolitleri n=11 için raporlandı; transkriptom analizi için 12 kişi rastgele seçildi, 1'i kalite kontrolden elendi → **final transkriptom n=11 (8 kadın, 3 erkek)**
- Fare: toplam 24 fare (12 AL, 12 aç bırakılan); transkriptom analizi için grup başına rastgele 8 fare seçildi (**n=8/grup**)

**Süre:**

- İnsan: 26 saat tam açlık (yalnızca su serbest), standardize öğünden sonra
- Fare: 16 saat açlık

**Karşılaştırma:** Tok (fed) vs. Aç (fasted) durumu — hem insan hem fare içinde eşleştirilmiş/eşleştirilmemiş karşılaştırma; ayrıca insan-fare arası transkriptomik yanıtın (SLR bazlı) karşılaştırılması (12.502 ortak homolog gen üzerinden)

**Doku/Ölçüm:**

- İnsan: periumbilikal iğne biyopsisi ile subkutan beyaz yağ dokusu (sWAT); 2 saat (tok) ve 26 saat (aç) sonra, günün aynı saatinde (sirkadiyen kontrol)
- Fare: epididimal yağ dokusunun üst kısmı; inaktif faz başlangıcında (09:00) sakrifiye
- Yöntem: Affymetrix mikroarray (Human/Mouse Gene 2.1 ST), IBMT istatistiği ile P<0.001 eşiği; GSEA ve EnrichR pathway analizi; Cibersort ile hücresel dekonvolüsyon; seçili genler qPCR ile doğrulandı
- Plazma metabolitleri: glukoz, TAG, kolesterol, NEFA, β-hidroksibütirat (her iki türde de ölçüldü)

**Çalışma tipi:** Karşılaştırmalı translasyonel çalışma — Klinik (insan, tek kollu açlık müdahalesi, kontrolsüz/tek-örnek öncesi-sonrası tasarım) + Preklinik (fare, AL vs. açlık, paralel grup tasarımı)

**Sınırlılık/Dikkat:**

- Yazarların belirttiği limitasyonlar:
    - İnsan ve fare açlık sürelerini birebir eşleştirmek mümkün değil; insan 10 saat daha uzun aç kalmasına rağmen yanıt farede daha güçlü — yazarlar insan açlığını 48 saate uzatsalar bile sonucun büyük ölçüde değişmeyeceğini öngörüyor (ama bu doğrulanmamış bir varsayım)
    - Dokular karşılaştırılabilir değil: insan **subkutan (periumbilikal)** vs. fare **epididimal (visseral)** — insan subkutan dokusuna tam karşılık gelen bir fare deposu yok; ayrıca bazı genlerin (_Pnpla2, Lipe, Srebf1, Ppara_) yanıtı fare içinde bile depoya göre değişebiliyor
    - İnsan verisinde bazal ve açlık-kaynaklı gen ifadesi farede çok daha değişken (interindividual varyasyon yüksek) — bu istatistiksel gücü azaltıyor ve insanda anlamlı gen sayısını kısıtlıyor
    - **Cinsiyet dengesizliği:** insan kohortu ağırlıklı kadın (8K/3E), fare çalışması yalnızca erkek — cinsiyete bağlı açlık yanıtı farkını analiz etmek için yetersiz
    - Çalışma yalnızca mRNA düzeyinde; protein düzeyinde doğrulama yapılmamış
- Benim eklediğim dikkat noktaları:
    - İnsan tarafında **tek zaman noktası karşılaştırması** (tok vs. 26 saat aç) var; farklı açlık sürelerinin (örn. 12h, 24h, 48h) doz-yanıt ilişkisi test edilmemiş — derlemede "personalized fasting/protokol süresi" tartışılırken bu çalışmanın yalnızca tek bir açlık süresi noktasını temsil ettiği vurgulanmalı
    - İnsan biyopsisi yalnızca **subkutan** depoyu örnekliyor; visseral insan yağ dokusuna dair bir veri yok — derlemenin "depot-specific remodeling" bölümünde bu tür karşılaştırma yaparken insan-fare doku eşleşmesi problemi mutlaka belirtilmeli
    - Sonuçlar sağlıklı, normal-kilolu/hafif kilolu gönüllülerden geliyor; obezite veya metabolik hastalık durumunda transkriptomik yanıtın farklı olabileceği test edilmemiş

Açlık esnasında insan subkutan (deri altı) ve fare epididimal yağ dokularındaki tüm genom transkriptomik (RNA/Microarray) ve metabolik yanıtların karşılaştırıldığı bu kapsamlı çalışma, akademik analizleriniz için parametre bazında kategorize edilerek Türkçeye çevrilmiş ve sistematik bir düzene kavuşturulmuştur.

## 1. METODOLOJİ VE ÇALIŞMA TASARIMI (METHODS)

### İnsan Çalışması (FASTING Study)

- **Kohort:** 40-70 yaş arası, BMI değeri 22–30 $\text{kg/m}^2$ olan 24 sağlıklı gönüllü (23'ü tamamladı).
    
- **Güç (Power) Analizi:** Birincil çıktı olan plazma ANGPTL4 konsantrasyonu baz alınarak; 14 ng/mL standart sapma, %90 güç ve iki yönlü 0.05 anlamlılık seviyesi ile gerekli örneklem $n=21$ (olası %10 drop-out hesabı ile $n=24$) olarak belirlenmiştir.
    
- **Protokol:** * Başlangıçta saat 18:00'de standardize bir yemek (%22 protein, %24 yağ, %51 karbonhidrat; 100 gramda 476 kJ) _ad libitum_ (doyana kadar) tüketilmiştir.
    
    - Ardından **26 saatlik tam açlık** (sadece su serbest) uygulanmıştır.
        
- **Örnekleme Zamanlaması (Sirkadiyen Kontrol):** * _Tokluk Etabı:_ Yemekten 2 saat sonra (20:00).
    
    - _Açlık Etabı:_ Yemekten 26 saat sonra (Ertesi gün 20:00).
        
    - Her iki örnekleme de günün aynı saatinde yapılarak **sirkadiyen ritim etkisi elimine edilmiştir** (İnaktif fazın başlangıcı).
        
- **Biyopsi Metodu:** Lokal anestezi altında, periumbilikal (göbek çevresi) bölgeden iğne biyopsisi ile subkutan beyaz yağ dokusu (sWAT) alınmıştır (Açlık etabında göbeğin tam karşı tarafından). Örnekler sıvı nitrojende şoklanıp -80°C'de saklanmıştır.
    
- **Klinik Kayıt:** NCT03757767 (Wageningen Üniversitesi onaylı).
    

### Hayvan Çalışması

- **Kohort:** 3-4 aylık, 24 adet erkek vahşi tip (WT) C57Bl/6J fare.
    
- **Protokol:** 12 fare **16 saat boyunca aç** bırakılmış (17:00 - 09:00), diğer 12 fareye serbest erişim (AL) sağlanmıştır. Saat 09:00'da (inaktif faz başlangıcı) sakrifiye edilerek sirkadiyen ritim etkisi dışlanmıştır.
    
- **Dokusal Analiz:** RNA izolasyonu ve transkriptom analizi için **epididimal yağ dokusunun** (erkek visseral yağ deposu) üst kısmı kullanılmıştır (Grup başına rastgele 8 fare seçilmiştir).
    

## 2. PLAZMA METABOLİTLERİ VE SİSTEMİK YANITLAR (METABOLITES)

Açlık süresi farelerde daha kısa (16 saat) olmasına rağmen, metabolik faz değişim hızı (metabolik hız farkından dolayı) farelerde insanlara kıyasla çok daha dramatik olmuştur. Bulgular, metabolik açlığın 5 fazlı modelinin **3. Evresinin sonuna (hepatik glikojenin tükenmek üzere olduğu evre)** denk gelmektedir.

- **Ortak Metabolik Trendler (İnsan ve Fare):**
    
    - Glikoz ve Trigliserid seviyeleri **anlamlı derecede düşmüştür**.
        
    - NEFA (Serbest Yağ Asitleri) ve $\beta$-hidroksibütirat (Keton cisciği) **anlamlı derecede yükselmiştir**.
        
- **Türler Arası Farklılık:** Plazma total kolesterol konsantrasyonu açlıkla birlikte **insanlarda anlamlı şekilde yükselirken, farelerde değişmemiştir**.
    

## 3. YAĞ DOKUSU TRANSKRİPTOMİK YANITLARI (TRANSCRIPTOMICS)

İnsan ve fare homolog genleri NCBI HomoloGene ile eşleştirilmiş ve **12.502 ortak homolog gen** analiz edilmiştir.

### A. Varyasyon, Kümeleme ve Yanıt Büyüklüğü (Volcano & PCA)

- **Yanıt Şiddeti:** Açlık, fare yağ dokusu gen ifadesini insanlara kıyasla **çok daha derin ve şiddetli** etkilemiştir (Kat kuralları ve istatistiksel anlamlılık farede çok daha yüksektir).
    
    - _İnsan sWAT ($P < 0.001$):_ 260 gen yukarı, 557 gen aşağı regüle (Toplam: 817 gen).
        
    - _Fare Yağ Dokusu ($P < 0.001$):_ 1.035 gen yukarı, 1.378 gen aşağı regüle (Toplam: 2.413 gen).
        
- **Kümeleme (Hierarchical Clustering & PCA):**
    
    - **Fare dokuları:** Beslenme durumuna göre (Tok vs. Aç) **mükemmel ve net bir şekilde** ikiye ayrılmıştır (Yüksek replikabilite).
        
    - **İnsan dokuları:** Açlık kayması net bir vektör gösterse de, örnekler esas olarak **donöre (bireysel genetik arka plana) göre** kümelenmiştir. İnsanlardaki interindividual (bireyler arası) varyasyon çok daha geniştir.
        
- **Bazal Cinsiyet Farkı (İnsan sWAT):** Açlık öncesi bazalde _SAA1_ (Serum Amiloid A1), _ECH1_ ve _ANXA1_ mRNA seviyeleri erkeklerde kadınlardan anlamlı derecede düşük, _RPS11_ ise yüksek bulunmuştur.
    
- **Hücresel Heterojenlik (Cibersort Analizi):** Transkriptomik dekonvolüsyon yöntemi, insan biyopsilerinde baskın hücrelerin adipositler ve yağ kök hücreleri olduğunu doğrulamış; **açlığın dokunun hücresel kompozisyonunu/heterojenliğini değiştirmediğini** göstermiştir.
    

### B. Açlık Sırasında Baskılanan / Azalan Ortak Yolaklar (Conserved Downregulation)

İki türde de ortak olarak **173 gen** anlamlı şekilde aşağı regüle edilmiştir. GSEA ve EnrichR analizlerine göre anabolik ve enerji tüketen yolaklar tamamen kapatılmıştır:

- **Trigliserid ve Yağ Asiti Sentezi / Depolanması:** Lipojenik yolaklar tamamen susturulmuştur. (Örn: _FASN_, _THRSP_, _PNPLA3_ genleri iki türde de baskılanmıştır ancak faredeki kat düşüşü çok daha keskindir).
    
- **Glikoliz ve Karbonhidrat Metabolizması:** Glikoz alımı, depolanması ve yıkım genleri baskılanmıştır.
    
- **Kolesterol Sentezi:** Hücresel kolesterol biyosentez yolakları susturulmuştur.
    
- **TCA Döngüsü ve Oksidatif Fosforilasyon:** Mitokondriyal enerji üretim yolakları anlamlı düzeyde baskılanmıştır.
    
- **İnsülin ve SREBP Sinyal Yolakları:** İnsan sWAT'ında _IRS1_ mRNA'sı açlıkla aşağı regüle olurken, _IRS2_ yukarı regüle olur — bu yön iki türde ortaktır. Ancak insülin sinyal yolağı **bir bütün olarak** farede insana kıyasla çok daha güçlü şekilde baskılanır; bu yolak, insan-fare arasında en belirgin diverjans gösteren yolaklardan biri olarak öne çıkar (ΔSLR analizinde insanda zayıf/hiç baskılanmayan, farede güçlü baskılanan genler arasında sınıflandırılmıştır). Dolayısıyla insülin sinyalinin baskılanması "iki türde konserve" değil, tür-spesifik şiddet farkı gösteren bir yanıttır.
    
- **Proteazom ve Kollajen Genleri:** Proteazomal gen setlerinin açlıkla baskılanması yalnızca **insan sWAT'ında** gösterilmiştir; bu bulgunun farede de konserve olduğuna dair doğrudan bir kanıt sunulmamıştır — dolayısıyla insana özgü bir bulgu olarak değerlendirilmelidir.  
**Kollajen:** İki türde ortak olarak baskılanan kollajen genleri _COL11A1, COL15A1, COL5A1, COL5A3_ ve _COL3A1_'dir (beş gen).

### C. Açlık Sırasında Uyarılan / Artan Ortak Yolaklar (Conserved Upregulation)

İki türde de ortak olarak **77 gen** anlamlı şekilde yukarı regüle edilmiştir. Fonksiyonel olarak çok çeşitlidirler ancak temel metabolik adaptasyonları yönetirler:

- **_PDK4_ (Piruvat Dehidrogenaz Kinaz 4):** Glikolizi inhibe ederek karbonhidratların korunmasını sağlar (En yüksek artış gösteren genlerden biri).
    
- **_ANGPTL4_ (Fasting-Induced Adipose Factor):** Kortizol ve FFA artışı, insülin düşüşü ile tetiklenir; kapiler düzeyde Lipoprotein Lipaz (LPL) aktivitesini inhibe ederek yağ dokusuna dışarıdan trigliserid girişini bloke eder.
    
- **_IRS2_ (İnsülin Reseptör Substratı 2):** _IRS1_ baskılanırken, _IRS2_'nin yukarı regüle olması açlık esnasındaki spesifik insülin duyarlılık modülasyonunu gösterir.
    
- **_ADRB2_ ($\beta_2$ Adrenerjik Reseptör):** Açlık lipid mobilizasyonu için adrenerjik sinyal duyarlılığını artırır.
    
- **_THBS1_ ve _THBS2_ (Trombospondin 1 ve 2):** İnsülin direnci ile ilişkili adipokinler iki türde de uyarılmıştır.
    
- **Otofaji:** Genel otofaji yolakları değişmezken, _GABARAPL1_ ve _DAPK2_ genleri spesifik olarak güçlü bir şekilde indüklenmiştir.
    

## 4. TÜRLER ARASI DİVERJANS VE FARKLI YANITLAR (DIVERGENT REGULATION)

İnsan ve fare yağ dokusunun açlığa transkriptomik yanıtlarında ciddi sapmalar (scatter) mevcuttur. Diferansiyel SLR (DSLR) analizine göre ana farklılıklar şunlardır:

### A. İnsan sWAT Lehine Olan Farklar (DSLR > 1 / İnsanda Güçlü, Farede Zayıf veya Ters)

- **Yolaklar:** **AMPK, İnsülin ve FOXO sinyal yolakları**.
    
- **İnsülin Sinyali:** İnsülin sinyal yolağı genleri fare yağ dokusunda açlıkla çok güçlü şekilde baskılanırken, insan sWAT'ında bu baskılanma ya hiç olmamış ya da çok hafif kalmıştır.
    
- **_CIDEA_:** İnsanda açlıkla uyarılırken, farede hafifçe azalmıştır.
    

### B. Fare Yağ Dokusu Lehine Olan Farklar (DSLR < -1 / Farede Güçlü, İnsanda Zayıf veya Ters)

- **Yolaklar:** **PPAR Sinyal Yolağı ve Yağ Asiti Biyosentezi**.
    
- **PPAR Hedef Genleri:** Çok sayıda PPAR hedef geni farede açlıkla güçlü şekilde indüklenirken, insanda bu yanıt alınamamıştır. Bu fark reseptör düzeyinden kaynaklanmamaktadır (PPAR ekspresyonları benzerdir). Ancak **_PPARG_ mRNA'sı insanda açlıkla aşağı regüle olurken, farede değişmemiştir.**
    
- **Glikoz ve Glikojen Metabolizması:** _GPD1_ (Gliserol-3-fosfat dehidrogenaz 1) ve _PYGB_ (Glikojen fosforilaz B) farede güçlü şekilde baskılanırken insanda değişmemiştir.
    
- **_PCK1_ (PEPCK):** Fare yağ dokusunda açlıkla **yukarı** regüle olurken, insan sWAT'ında **aşağı** regüle olmuştur (Önemli tür farkı).
    
- **_KLB_ (Beta-Klotho) ve _FGF2_:** _KLB_ insanda azalırken farede artmış; _FGF2_ ise insanda artarken farede azalmıştır.
    

## 5. LİPİD DAMLACIK DİNAMİĞİ VE EKSTRASELÜLER LİPOLİZ KARŞILAŞTIRMASI

Çalışma, yağ dokusunun iki ana lipolitik sürecini transkript düzeyinde karşılaştırmıştır:

### A. İntraselüler Lipoliz ve Lipid Damlacık Yıkımı (Diverjan/Farklı)

Lipid damlacıklarının hücresel düzeyde parçalanmasını yöneten genlerde türler arası ciddi uyumsuzluklar saptanmıştır:

- **_PNPLA2_ (ATGL):** Fare yağ dokusunda açlıkla anlamlı derecede indüklenirken (artarken), **insan sWAT'ında hiç etkilenmemiştir**.
    
- **_LIPE_ (HSL):** İnsanda açlıkla hafif ama anlamlı bir artış gösterirken, farede transkript düzeyinde değişmemiştir.
    
- **_CIDEC_ ve _PLIN1_:** _CIDEC_ insanda açlıkla azalırken farede artmıştır. _PLIN1_ (Perilipin 1) insanda değişmezken farede azalmıştır.
    
- **Ortak olanlar:** _ABHD5_ (ATGL aktivatörü), _ADRB2_ ve _IRF4_ iki türde de artmış; lipoliz inhibitörü _G0S2_ ise iki türde de konserve olarak baskılanmıştır.
    

### B. Ekstraselüler Lipoliz ve LPL Regülasyonu (Konserve/Benzer)

Hücre dışı trigliseridlerin hidrolizi ve dokuya alınmasını yöneten yolak, lipid damlacık genlerine kıyasla **insan ve fare arasında mükemmel bir tutarlılık (konservasyon)** göstermektedir:

- **_LPL_ (Lipoprotein Lipaz):** İnsanda hafifçe azalmış, farede değişmemiştir.
    
- **_GPIHBP1_:** LPL'i kapiler endoteline taşıyan ve çapalayan bu kritik taşıyıcı, **her iki türde de açlıkla indüklenmiştir**.
    
- **_ANGPTL4_ & _ANGPTL8_:** LPL inhibitörü _ANGPTL4_ iki türde de güçlü şekilde yukarı regüle olurken, onun antagonisti olan _ANGPTL8_ ve VLDL reseptörü (_VLDLR_) iki türde de anlamlı şekilde baskılanmıştır.
    

### Akademik Özet / Metodolojik Çıkarım (Academic Takeaway)

Bu çalışma; fare yağ dokusunun açlığa transkriptomik düzeyde (özellikle PPAR sinyalizasyonu, _PCK1_ yönelimi ve _PNPLA2/ATGL_ uyarımı açısından) insan subkutan yağ dokusuna göre **kat be kat daha dramatik ve bazen yönsel olarak tamamen farklı** yanıtlar verdiğini ortaya koymaktadır.

Buna karşın, **ekstraselüler lipolizin kapiler düzeydeki kontrol mekanizması (_ANGPTL4 - ANGPTL8 - GPIHBP1_ekseni)**, fare ve insan arasında evrimsel olarak tam anlamıyla konserve edilmiştir. Dolayısıyla, kemirgen açlık modellerinden elde edilen intrakrin/intraselüler lipid damlacık bulguları insana doğrudan genellenemezken, endotelyal lipid transport mekanizmaları yüksek translasyonel değere sahiptir.