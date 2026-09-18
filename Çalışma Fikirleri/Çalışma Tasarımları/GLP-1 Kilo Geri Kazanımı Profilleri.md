[[GLP-1]] #çalışmafikri 
1. Çalışmanın Arka Planı ve Gerekçesi (Background and Rationale)

Obezite tedavisinde Semaglutid (GLP-1 RA) ve Tirzepatid (GLP-1/GIP RA) klinik obezite yönetiminde devrim yaratmıştır. Ancak klinik çalışmalar, ilaç kesildiğinde hastaların hızla kilo geri alımı (weight regain) yaşadığını ve kardiyometabolik faydaların gerilediğini göstermektedir. Obezitede hassas tıp (precision medicine), bugüne kadar hastaların ilaca vereceği _kilo verme yanıtına_ odaklanmıştır; ancak ilacı bıraktıktan sonra kimin, ne hızda nüks yaşayacağını öngören fenotipler tanımlanmamıştır. Ayrıca "Ayar Noktası (Set-Point) Paradoksu" hipotezine göre, tedavi sırasında en başarılı sonucu elde edip "preklinik/sağlıklı" sınıfa geçen hastaların, biyolojik dengenin eski haline dönme çabası nedeniyle en agresif kilo geri alımını yaşaması olasıdır. Bu çalışma, gözetimsiz makine öğrenmesi (unsupervised machine learning) kullanarak geri alım profillerini fenotiplemeyi ve iki farklı molekül (Semaglutid ve Tirzepatid) arasındaki nüks farklarını ortaya koymayı amaçlamaktadır.

2. Çalışmanın Amaçları ve Hipotezleri (Objectives and Hypotheses)

- **Birincil Amaç (Primary Objective):** K-Means kümeleme analizi kullanarak, ilaç bırakma anındaki (discontinuation point) klinik özelliklere göre hastaları "kilo geri alım fenotiplerine" (Örn: Dirençli Koruyucular, Agresif Reboundcular) ayırmak.
- **İkincil Amaç (Secondary Objective):** "Ayar Noktası Paradoksunu" test etmek. Tedaviyle VKİ < 25 (veya < 30) seviyesine inenlerin, obezite sınıfında kalanlara kıyasla başlangıç kilolarına dönüş (relapse) hızlarını Kaplan-Meier sağkalım analizi ile karşılaştırmak.
- **Üçüncül Amaç (Tertiary Objective):** Tekli agonist (Semaglutid) ile çift agonist (Tirzepatid) kullanan hastaların ilaç bırakma sonrası rebound hızlarını ve kardiyometabolik risk geri dönüşlerini (Örn: bel çevresi ve HbA1c artışı) karşılaştırmak.

3. Çalışma Tasarımı ve Popülasyon (Study Design and Population)

Bu çalışma, tamamlanmış iki büyük Faz 3 çalışmasının bireysel katılımcı verilerini (IPD) kullanan retrospektif bir sekonder analizdir:

- **Kohort 1 (Semaglutid):** STEP 1 Extension trial (NCT03548935). Sadece 68 haftalık tedaviyi tamamlayıp ilacı bırakan ve 1 yıllık (52 hafta) uzatma periyodunda (off-treatment) izlenen hastalar.
- **Kohort 2 (Tirzepatid):** SURMOUNT-4 trial (NCT04660643). 36 haftalık lead-in periyodundan sonra plasebo koluna randomize edilip 52 hafta boyunca ilaçsız izlenen hastalar.

4. Talep Edilen Veri Değişkenleri (Requested Data Variables)

İnceleme kurulunun sizin ne istediğinizi net görmesi için şu değişkenleri talep ettiğinizi belirtin:

- **Demografik Veriler:** Yaş, Cinsiyet, Etnik Köken, Başlangıç Obezite Süresi.
- **Antropometrik Veriler (T0: Başlangıç, T1: İlaç Bırakma Anı, T2, T3..: Bırakma Sonrası Aylar):** Vücut Ağırlığı (kg), VKİ (kg/m²), Bel Çevresi (cm).
- **Klinik ve Biyobelirteçler (T0, T1 ve T2 noktalarında):** HbA1c, Sistolik/Diyastolik Kan Basıncı, Açlık Glikozu, Total Kolesterol, Trigliseritler.
- **Varsa Ek Veriler:** DEXA veya BIA ile ölçülmüş Vücut Kompozisyonu (Yağ ve Kas Kütlesi). _(Komiteye not: Varsa dâhil edilecektir, yoksa birincil modelleme antropometri üzerinden yapılacaktır)._

5. İstatistiksel Analiz Planı (Statistical Analysis Plan - SAP)

- **Aşama 1 (Kümeleme - K-Means Clustering):** Hastalar, _ilaç bırakma anındaki (T1)_ ulaşılan VKİ, kaybedilen toplam kilo yüzdesi, yaş, cinsiyet ve diyabetik/metabolik durum değişkenleri kullanılarak Gözetimsiz Makine Öğrenmesi (K-Means) ile kümelere ayrılacaktır. Optimal küme sayısı _Elbow metodu_ ve _Silhouette skoru_ ile belirlenecektir.
- **Aşama 2 (Sağkalım Analizi - Survival Analysis):** Hastaların %5 kilo geri alma veya başlangıç kilosuna nüks etme (event) süreleri Kaplan-Meier eğrileri kullanılarak hesaplanacaktır. "Preklinik" sınıfa düşenler ile "Klinik Obez" kalanlar arasındaki farklar Log-Rank testi ile kıyaslanacaktır.
- **Aşama 3 (İlaç Karşılaştırması):** Tirzepatid (SURMOUNT-4) ve Semaglutid (STEP 1) kohortları, propensity score matching (eğilim skoru eşleştirme) ile başlangıç özelliklerine göre dengelendikten sonra, ilaçların rebound katsayıları Cox Proportional Hazards (Cox Orantısal Risk) modelleriyle karşılaştırılacaktır.

6. Beklenen Etki ve Yayın Çıktısı (Expected Impact and Publication)

Bu çalışma, GLP-1/GIP reseptör agonistlerinin bırakılması sonrası süreci ilk kez makine öğrenmesiyle öngörebilen bir model sunacaktır. Sonuçlar, klinisyenlerin hangi hastaya "kademeli bırakma (tapering)" veya "agresif koruma" uygulaması gerektiğine dair ilk kişiselleştirilmiş tıp (precision medicine) kılavuzunu oluşturacak ve prestijli hakemli dergilerde (Örn. _Lancet Diabetes & Endocrinology_ veya _Obesity_) yayımlanacaktır.

--------------------------------------------------------------------------------

💡 Veri Erişimi İçin İletişim Stratejisi ve Sonraki Adımlar

1. **Eli Lilly (Tirzepatid) İçin:** `Vivli.org` portalında bir hesap oluşturun. "Search Trials" kısmına "SURMOUNT-4" veya "NCT04660643" yazarak çalışmayı bulun ve "Request Data" butonuna tıklayarak bu taslağı sisteme İngilizce olarak kopyalayın.
2. **Novo Nordisk (Semaglutid) İçin:** `novonordisk-trials.com` adresine gidin. STEP 1 Extension (NCT03548935) çalışması için "Submit a Research Proposal" seçeneğini kullanarak veri talebinde bulunun.


 GLP-1 "Biyolojik Nüks ve Klinik/Preklinik Sınıflandırma" Veri Seti Taslağı

Bu veri setini, her hasta için bir satır (ID) ve zaman serilerine bölünmüş sütunlar (Longitudinal Data) olarak düşünmelisiniz.

1. Demografik ve Sosyoekonomik Özellikler

Kilo geri alımında sosyoekonomik faktörler ve biyolojik altyapı çok kritiktir.

- **Temel:** Yaş (Başlangıç), Cinsiyet, Irk/Etnik Köken.
- **Özgünlük İçin Gerekli:** Eğitim durumu, Gelir düzeyi veya "Bölgesel Yoksunluk İndeksi" (Area Deprivation Index) [Xie 2024]. _(Not: İlaç bırakıldıktan sonra sağlıklı beslenmeye erişim gücünü gösterir)._
- **Obezite Geçmişi:** Fazla kilonun başlama yaşı, daha önceki başarısız diyet/ilaç/cerrahi deneme sayısı.

2. Klinik ve Preklinik Obezite Tanısı İçin Değişkenler (Mozaffarian 2025 Kriterleri)

Hastanın sadece VKİ'sine değil, "organ disfonksiyonu" olup olmadığına bakmalıyız.

- **Başlangıç (T0) ve İlaç Bırakma Anı (T1) Komorbidite Durumu (Var/Yok/Remisyonda):**
    - Tip 2 Diyabet veya Prediyabet (HbA1c > %5.7).
    - Hipertansiyon (Sistolik >130 / Diastolik >80).
    - Dislipidemi (Yüksek LDL, Düşük HDL, Yüksek Trigliserit).
    - Karaciğer Yağlanması (MASLD/MASH) veya yüksek ALT/AST.
    - Obstrüktif Uyku Apnesi (OSA) veya Osteoartrit.
- _Sınıflandırma Algoritması:_ Hasta VKİ > 30 ama bu komorbiditelerin hiçbiri yoksa **"Preklinik Obezite"**; VKİ > 27 ama en az 1 komorbidite varsa **"Klinik Obezite"** olarak kodlanacak.

3. Başlangıç, Müdahale ve Nüks Dönemi Antropometrik / Vücut Komp. Verileri

- **Rutin Ölçümler (T0, T-Müdahale Ayları, T1-Bırakma, T1 Sonrası 3-6-9-12. Aylar):**
    - Vücut Ağırlığı (kg), Vücut Kitle İndeksi (VKİ).
    - Bel Çevresi (cm) ve Bel/Boy Oranı (WHtR) _(Kardiyometabolik riskin en iyi göstergesi)_.
- **Vücut Kompozisyonu (DEXA, MRI veya BIA - Varsa):**
    - Toplam Yağ Kütlesi (Fat Mass - kg ve %).
    - Yağsız Vücut Kütlesi / İskelet Kası (Lean Body Mass - kg).
    - Viseral (İç Organ) Yağ Alanı (VAT).

4. İlaç, Farmakodinamik ve Takip Verileri

- **Müdahale:** İlaç Tipi (Semaglutid, Tirzepatid, Liraglutid), Ulaşılan Maksimum Doz (Örn: 2.4 mg veya 15 mg).
- **Zaman Çizelgesi:** İlaç kullanım süresi (Hafta/Ay), İlacı bırakma nedeni (Maliyet, Yan etki, Hedefe ulaşma, Gebelik planı vb.).
- **Takip (Follow-up):** İlacı bıraktıktan sonraki takipsiz/ilaçsız kalınan süre (Ay).

3. Beslenme ve Yaşam Tarzı Kayıtları

GLP-1 bırakıldıktan sonra hastanın neden geri kilo aldığını açıklayacak olan "Kara Kutu" burasıdır [Sievenpiper 2026].

- **Müdahale Sırası ve Sonrası Diyet:** Günlük ortalama kalori alımı (kcal), **Günlük Protein Alımı (g/kg)** _(Kas koruması için >1.2 g/kg olup olmadığı kritik)_.
- **Egzersiz:** Haftalık orta-şiddetli aerobik aktivite (dk/hafta) ve Direnç/Ağırlık antrenmanı (Evet/Hayır veya gün/hafta).

--------------------------------------------------------------------------------

🚀 Nasıl Özgün Bir Çalışma (Research Article / Commentary) Planlayabiliriz?

Literatür, "İlacı bırakınca herkes kilo alıyor" (West 2026, Berg 2025) gerçeğini artık kabul etti. Sizin bu verisetiyle yapacağınız çalışma, **"Kimin daha hızlı, kimin daha tehlikeli kilo aldığını"** ve **"İdeal kiloya inmenin aslında bir tuzak olup olmadığını"**kanıtlayacak.

İşte size dünyada ses getirecek 2 adet orijinal çalışma kurgusu (Pitch):

Hipotez 1: "Preklinik Tuzak: Biyolojik Ayar Noktası (Set-Point) Paradoksu"

- **Kurgu:** İlaç tedavisi sonucunda (T1 anında) büyük bir başarı gösterip VKİ'si 25'in altına düşen ve komorbiditeleri sıfırlanan **"Preklinik / Sağlıklı"** gruptaki hastalar ile; kilo vermesine rağmen hala VKİ > 30 olan **"Klinik Obezite"** grubunda kalan hastaları ayırın.
- **Analiz:** İlacı bıraktıktan sonraki kilo geri alım hızlarını (Survival/Kaplan-Meier analizi ile "Başlangıç kilosuna nüks etme süresi" olarak) karşılaştırın.
- **Özgün Mesaj:** _"Tedaviyle tamamen 'sağlıklı/preklinik' sınıfa geçen hastalar, biyolojik 'Set-Point' (ayar noktası) ile aralarındaki fark çok açıldığı için, ilacı bıraktıkları an klinik obezlere kıyasla çok daha şiddetli ve agresif bir geri tepme (rebound) yaşarlar."_ (Bu, obezite tedavisinde hedef kilonun yeniden tanımlanmasını sağlar).

Hipotez 2: "Sarkopenik Rebound: Yağsız Kütle Kaybının Nüks Hızına Etkisi"

- **Kurgu:** Elinizdeki DEXA (vücut kompozisyonu) verilerini ve Diyet/Protein kayıtlarını kullanın. Müdahale sırasında verdiği kilonun %30'undan fazlasını kas (Lean Mass) olarak kaybedenler ile kasını koruyanları gruplayın.
- **Analiz:** İlacı bıraktıktan sonraki 1. yılda, kas kaybedenlerin ağırlık ve özellikle "Bel Çevresi (Viseral Yağ)" geri alım hızlarını karşılaştırın.
- **Özgün Mesaj:** _"Müdahale sırasında yetersiz protein alan ve iskelet kasını kaybeden hastalar, GLP-1'i bıraktıklarında sadece daha hızlı kilo almakla kalmazlar; aynı zamanda yağlar kaslardan daha hızlı geri döndüğü için başlangıçtakinden daha yüksek bir kardiyometabolik risk profiline (Sarkopenik Obezite) sahip olurlar."_


1. Hastaların VKİ'si 30'un (veya 25'in) Altına İnebiliyor mu? (Obezite Remisyonu)

Evet, ilaçlarla ulaşılan kilo kaybı, hastaların önemli bir kısmının obezite kategorisinden tamamen çıkmasını (remisyon) sağlamaktadır. SELECT çalışmasında (semaglutid 2.4 mg kullanan 17.604 hasta) 2. yılın (104. hafta) sonunda şu sonuçlar elde edilmiştir:

- **Obezite Sınıfından Çıkış:** Başlangıçta ilaç grubundaki hastaların %71.0'i obez (VKİ ≥ 30 kg/m²) kategorisindeyken, tedaviyle birlikte bu oran **%43.3'e düşmüştür**. Yani hastaların çok büyük bir kısmı obezite kategorisinden kurtulmuştur.
- **"Sağlıklı" Kategoriye Ulaşanlar (VKİ < 25):** Ekrana yansıtılabilecek en çarpıcı verilerden biri budur: Başlangıçta hiçbir hastanın VKİ'si 25'in altında değilken, tedavi sonunda semaglutid kullanan hastaların **%12.0'si "sağlıklı" (VKİ < 25 kg/m²) kategorisine** inerek tam bir kilo remisyonu sağlamıştır (bu oran plasebo grubunda sadece %1.2'dir).
- Genel olarak bakıldığında, hastaların yarısından fazlası (**%52.4'ü**) bir alt VKİ kategorisine geçiş yapmayı başarmıştır. Gerçek dünya verilerinde de hastalar VKİ 25 hedefine ulaştıklarında tedavinin koruma dozlarına veya bırakma (tapering) şemalarına geçirilebilmektedir.

2. Bel Çevresi Risk Sınırlarının Altına (80/92/102 cm) İnebiliyor mu?

Kardiyometabolik riski yansıtan bel çevresi (iç organ yağlanması) açısından da çok ciddi geri dönüşler rapor edilmiştir.

- Çalışmada cinsiyete ve ırka özgü risk sınırları (örneğin Asyalı olmayan kadınlarda <88 cm, erkeklerde <102 cm; Asyalı kadınlarda <80 cm, erkeklerde <88 cm) baz alınmıştır.
- Başlangıçta VKİ'si 35'in altında olan grupta, semaglutid kullanan hastaların **%41.2'si cinsiyete ve ırka özgü bu tehlikeli bel çevresi sınırlarının tamamen altına inmeyi başarmıştır** (plasebo grubunda bu oran sadece %18.0'de kalmıştır). Bel-boy oranında (WHtR) da plaseboya kıyasla %6.9'luk net bir küçülme kaydedilmiştir.

3. Başlangıç VKİ'sine Göre "Preklinik vs. Klinik" Farklılıkları (Ayar Noktası Paradoksu)

Sorunuzun en can alıcı kısmı burasıdır; çünkü literatür, başlangıç kilosu daha düşük olan (VKİ < 30, yani fazla kilolu/preklinik obezite) hastalar ile ileri derece obezitesi olanlar (VKİ ≥ 35 veya 40) arasında çok ilginç bir biyolojik farklılık (paradoks) saptamıştır:

- **Düşük VKİ'liler Daha Az Kilo Kaybediyor:** Beklenenin aksine, VKİ'si 30'un altında olan kişiler, aynı ilacı (hatta vücut kütlesine oranla daha yüksek doz maruziyetiyle) kullanmalarına rağmen, ileri derece obezitesi olanlara kıyasla **yüzdesel olarak daha az kilo kaybetmektedirler**. Örneğin SELECT verilerinde, VKİ < 30 olanlar ortalama %7.52 oranında kilo kaybederken, bu kayıp VKİ ≥ 40 olanlarda %9.23'e çıkmaktadır.
- **"Ayar Noktası" (Set-Point) Teorisi:** Araştırmacılar bu durumu, vücudun genetik ve çevresel "ayar noktası" (settling point) ile açıklıyor. VKİ'si 30'un altında olan kişiler, zaten biyolojik olarak korumaları gereken sağlıklı vücut ağırlığına daha yakındırlar; bu nedenle sistem o noktaya ulaşmak için devasa bir kilo kaybına ihtiyaç duymaz (direnç gösterir).
- **Kardiyometabolik İyileşme İçin Devasa Kilo Kaybı Şart Değil:** Çalışmalar, düşük VKİ'li ancak metabolik olarak hasta olan bireylerde (preklinik obezite/kardiyometabolik hastalık fenotipi), sağlığın düzelmesi için çok büyük bir genel "vücut kütlesi" kaybına ihtiyaç olmadığını vurguluyor. Sadece hastalık yaratan anormal ektopik ve viseral (iç organ) yağ depolarının temizlenmesi, bu hastaların hastalık remisyonuna girmesi için yeterli olmaktadır.