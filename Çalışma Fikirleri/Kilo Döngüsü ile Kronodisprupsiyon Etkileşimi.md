# Deneysel Tasarım Önerisi: Weight Cycling × Kronodisrupsiyon Etkileşimi

**Durum:** Fikir aşaması — mevcut narrative review'a dahil edilmeyecek, bağımsız araştırma hattı olarak değerlendirilecek.

---

## 1. Boşluk (Gap) Tanımı

İki ayrı literatür hattı bağımsız olarak aynı moleküler hedefi gösteriyor:

1. **Weight cycling → adipoz doku saat geni baskılanması.** Farelerde 4 ardışık kilo döngüsü, izokalorik sürekli hiperkalorik beslenmeye kıyasla anlamlı derecede daha fazla yağ kütlesi kazanımına yol açıyor; yağ dokusunda Dbp, Tef, Per1, Per2, Per3, Nr1d2/Rev-erbα ekspresyonu baskılanıyor (Guo ve ark., AJP-Endo 2013).
2. **Yanlış-faz beslenme / kronodisrupsiyon → aynı saat genleri üzerinden yağ birikimi.** Aktif faz dışında beslenme, DMH elektriksel ritmini bozuyor (Su ve ark. 2022), adipoz termogenezi baskılıyor (Hepler ve ark., Science 2022), ve bu etki zamanlamayı düzeltmekle (gece beslemesi) tamamen geri döndürülebiliyor.

**Test edilmemiş soru:** Bu iki tetikleyici (weight cycling + yanlış-faz beslenme) aynı anda uygulandığında **katlanmalı/sinerjistik bir clock-disrupsiyon ve adipozite fenotipi** ortaya çıkıyor mu, yoksa etkiler birbirinden bağımsız mı kalıyor? Literatür taramasında bu spesifik 2×2 kombinasyonu test eden bir çalışmaya rastlanmadı.

---

## 2. Hipotez

**H1:** Weight cycling, inaktif fazda (yanlış-faz) uygulandığında, aktif fazda uygulanan weight cycling'e kıyasla adipoz dokuda daha belirgin saat geni baskılanması (Per2, Nr1d2, Dbp) ve daha fazla yağ kütlesi rebound'u üretir.

**H2:** Bu etkinin büyüklüğü depot-spesifiktir — viseral depo (epididimal/mezenterik) subkutan depoya (inguinal) göre daha duyarlıdır (mevcut review'daki depot-spesifik remodeling çerçevesiyle uyumlu).

**H3:** Zaman-kısıtlı beslemeyle (aktif faza hizalanmış) yürütülen weight cycling, klasik ad libitum weight cycling'e kıyasla rebound yağ kazanımını azaltır — yani zamanlama, weight cycling'in metabolik "cezasını" modüle eden bağımsız bir değişkendir.

---

## 3. Deneysel Tasarım (2×2 Faktöriyel)

| | **Aktif faz beslenme (uygun faz)** | **İnaktif faz beslenme (yanlış faz)** |
|---|---|---|
| **Sürekli enerji kısıtlaması → tek döngü (kontrol)** | Grup A | Grup B |
| **Tekrarlayan weight cycling (4 döngü: kısıtlama → yeniden besleme)** | Grup C | Grup D |

- **Tür/suş:** Wistar veya Sprague-Dawley sıçan (mevcut RCT/BAP deneyimine paralel); erkek + dişi kolu önerilir (cinsiyet dimorfizmi Bölüm 5'te zaten işlenmiş bir eksen).
- **Işık koşulu:** Standart 12:12 LD, tüm gruplarda sabit tutulur (sıcaklık/ışık değişkeni bu tasarımda kontrol dışı bırakılıyor — sadece beslenme fazı manipüle ediliyor, karışıklığı önlemek için).
- **Diyet içeriği:** Tüm gruplarda izokalorik/izomakro — sadece erişim penceresi (ZT saatleri) ve döngü sayısı değişken.
- **Döngü protokolü (C ve D grupları):** ~%40 enerji kısıtlaması × 1 hafta → ad libitum yeniden besleme × 1 hafta, 4 kez tekrar (Guo ve ark. 2013 protokolüne benzer, faz kısıtlaması eklenmiş).
- **Süre:** Toplam 10-12 hafta (4 döngü + son gözlem penceresi).

---

## 4. Ölçülecek Uç Noktalar

**Birincil:**
- Adipoz doku saat geni ekspresyonu (qPCR): *Bmal1, Clock, Per1/2/3, Nr1d1/2 (Rev-erbα/β), Dbp, Tef* — inguinal, epididimal/perigonadal, mezenterik depolarda ayrı ayrı.
- Depot ağırlığı ve adiposit boyut dağılımı (histoloji).

**İkincil:**
- Serum leptin, adiponektin, insülin, NEFA (24 saatlik profil — en az 4 zaman noktası, ZT ile eşleştirilmiş).
- Karaciğer lipid içeriği (HPTLC veya benzeri).
- Lipoliz/lipogenez genleri (Atgl, Hsl, Srebf1c, Lpl) — depot bazında.
- Vücut kompozisyonu (DEXA veya NMR, her döngü sonunda).

**Keşifsel:**
- Adipoz doku RNA-seq (WC × faz etkileşimini yönlendiren ortak/farklı transkripsiyon imzası; Guo ve ark. 2013'teki rank-product meta-analiz yaklaşımına benzer).

---

## 5. Faz 2 Eklentisi: Önceki Döngü/Faz Geçmişi Sonraki Kilo Kaybı Müdahalesine Yanıtı Etkiliyor mu?

Bu, tasarıma eklenmesi güçlü gerekçeli bir üçüncü boyut. Gerekçe literatürde zaten var — "obesogenic memory" (obezojenik bellek) kavramı:

- Tek bir 4 haftalık HFD döngüsü bile, sonraki HFD döngülerinde kilo alımını hızlandıran kalıcı bağırsak mikrobiyota değişiklikleri bırakıyor (Thaiss ve ark. 2016).
- Kilo kaybı sonrası adipoz doku ve karaciğerde kalıcı bir enflamatuar imza kalıyor — bu, "obezojenik bellek" olarak adlandırılıyor ve kilo geri alımını kolaylaştırdığı düşünülüyor.
- Yo-yo (weight cycling) geçmişi olan farelerde, kilo kaybı sonrası adipoz doku enflamasyonu devam ediyor, pro-enflamatuar belirteçler ve bozulmuş Glut4 ekspresyonu kalıcı — üstelik zayıflamış olsalar bile.
- Pankreatik insülin sekresyonu weight cycling geçmişi olan farelerde bozuluyor, bu da sonraki metabolik müdahalelere yanıtı etkileyebilir.
- Guo ve ark. (2013) çalışmasında, son enerji kısıtlama döngüsünden 24 gün sonra bile adipoz dokuda saat geni bozulmasının hâlâ tespit edilebilir olması, bunun kalıcı/epigenetik bir "iz" olabileceğine işaret ediyor (Dbp, Per2, Bmal1 promoter bölgelerinde H3K9 asetilasyon değişiklikleri öne sürülüyor).

**Tasarıma eklenecek Faz 2:** Yukarıdaki 2×2 faktöriyel indüksiyon fazının (Faz 1) ardından, **tüm dört gruba (A, B, C, D) standart, tek tip bir kilo kaybı müdahalesi** uygulanır — örneğin 4 haftalık %20 enerji kısıtlaması, aktif faza hizalanmış olarak (TRF benzeri, tüm gruplarda aynı saat). Böylece Faz 1'deki geçmiş (WC var/yok × faz uygun/uygunsuz) sabit tutulan bir kilo kaybı protokolüne verilen yanıtı nasıl etkiliyor, izole edilebilir.

**Faz 2'de ölçülecek yanıt uç noktaları:**
- Kilo kaybı hızı ve platoya ulaşma süresi (haftalık vücut ağırlığı eğrisi).
- Adipoz doku saat geni ekspresyonunun kilo kaybıyla normale dönüp dönmediği (Per2, Dbp, Nr1d2 — Faz 1 sonu ile Faz 2 sonu karşılaştırması).
- Glukoz toleransı ve insülin sekresyon kapasitesi (IPGTT + ex vivo adacık sekresyon testi, Winn ve ark. 2022 protokolüne benzer).
- Adipoz doku makrofaj infiltrasyonu / enflamatuar belirteçler (F4/80, TNF-α, IL-6) — kalıcı enflamatuar "bellek" var mı.
- Kilo kaybı sonrası regain hızı (Faz 2 sonrasında ad libitum'a dönüldüğünde ne kadar hızlı geri alınıyor) — bu, "obezojenik bellek"in en doğrudan davranışsal göstergesi.

**Genişletilmiş hipotez (H4):** Faz 1'de yanlış-faz weight cycling geçmişi olan grup (D), Faz 2'deki standart kilo kaybı müdahalesine en yavaş yanıt verir (en yavaş kilo kaybı, en az saat geni normalizasyonu, en kalıcı enflamasyon) ve Faz 2 sonrası en hızlı regain'i gösterir — yani **geçmişteki hem döngüsel hem yanlış-fazlı beslenme, gelecekteki kilo kaybı müdahalesinin etkinliğini önceden azaltan bir "çifte bellek" oluşturur.**

Bu, çalışmayı sadece tanımlayıcı bir mekanizma çalışmasından çıkarıp **klinik olarak doğrudan uygulanabilir bir soruya bağlıyor**: "Hastanın geçmiş diyet öyküsü (kaç kere denedi, ne zaman yedi) gelecekteki müdahalenin başarı olasılığını öngörebilir mi?" — bu senin BAP/klinik pratiğin ile doğrudan konuşan bir çerçeve.

**Tasarım maliyeti notu:** Faz 2 eklenmesi toplam süreyi ~4-6 hafta uzatır ama ek hayvan grubu gerektirmez (aynı 4 grup takip ediliyor) — sadece longitudinal takip ve son ötanazi noktası ileri kayıyor. Güç analizinde tekrarlı ölçüm (repeated measures) tasarımı kullanılmalı.

---

## 6. Beklenen Katkı / Yayın Açısı

- Eğer H1 doğrulanırsa: "weight cycling'in metabolik zararı, beslenme fazına bağlıdır" — klinik olarak IF/TRF protokollerinin yo-yo diyet riskini azaltabileceğine dair mekanistik gerekçe sağlar. Bu doğrudan senin fasting review'ındaki argümana (kişiselleştirilmiş IF'nin koruyucu potansiyeli) tamamlayıcı, ayrı bir makale olarak konumlanabilir.
- Negatif sonuç (etkiler additif, sinerjistik değil) bile yayınlanabilir — mevcut weight cycling literatüründe faz değişkeninin hiç kontrol edilmediğini gösteren ilk çalışma olur.
- Hedef dergi: Sunulan bulgulara göre *International Journal of Obesity*, *Obesity (Silver Spring)*, veya mekanistik derinliğe göre *American Journal of Physiology-Endocrinology and Metabolism* (Guo ve ark. 2013'ün yayınlandığı dergi — doğal bir devam niteliğinde konumlanabilir).

---

## 7. Kısıtlılıklar / Riskler

- 2×2 × 2 cinsiyet tasarımı hayvan sayısını hızla artırır (n≥8/grup önerilirse toplam ~64-128 hayvan) — BAP bütçesi için güç analizi şart.
- Faz kısıtlamalı weight cycling protokolünün sıçanlarda strese bağlı confound yaratma riski var (kortikosteron ölçümü eklenmesi önerilir — bkz. Herrera-Márquez ve ark. anksiyete/TRH çalışması, aynı stres eksenini farklı bir bağlamda işliyor).
- Tek başına ışık/sıcaklık ekseni bu tasarıma dahil edilmedi; ikinci aşama olarak eklenebilir ama faktör sayısı artışı örneklem büyüklüğünü ciddi şekilde büyütür.


# Bibliyografya — Kronodisrupsiyon, Çevresel Tetikleyiciler ve Weight Cycling

Bu liste, sohbet boyunca web araması ile bulunan ve tartışılan tüm kaynakları içerir. APA benzeri kısa format kullanılmıştır; tam bibliyografik detay (cilt/sayfa) için DOI/URL üzerinden orijinal kaynağa bakılması önerilir.

---

## A. Barınma Sıcaklığı ve Adipozite

1. Albustanji, L., Perez, G. S., AlHarethi, E., Aldiss, P., Bloor, I., Barreto-Medeiros, J. M., Budge, H., Symonds, M. E., & Dellschaft, N. (2019). Housing Temperature Modulates the Impact of Diet-Induced Rise in Fat Mass on Adipose Tissue Before and During Pregnancy in Rats. *Frontiers in Physiology*. https://doi.org/10.3389/fphys.2019.00209 (tam metin: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6414463/)

2. Impact of short-term housing temperature alteration on metabolic parameters and adipose tissue in female mice. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12234322/

3. Cold Exposure Drives Weight Gain and Adiposity following Chronic Suppression of Brown Adipose Tissue. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8836787/

## B. Fotoperiyot ve Adipozite

4. Photoperiod influences visceral adiposity and the adipose molecular clock independent of temperature in wild-derived *Peromyscus leucopus*. *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12050962/

## C. Gece Işığı (Light at Night, LAN) ve Obezite

5. A large prospective investigation of outdoor light at night and obesity in the NIH-AARP Diet and Health Study. *Environmental Health*. https://ehjournal.biomedcentral.com/articles/10.1186/s12940-020-00628-4

6. Impact of artificial light at night on obesity and overweight: a systematic review and meta-analysis. *BMC Public Health*. https://link.springer.com/article/10.1186/s12889-025-25883-3

7. Sex- and age-specific association between outdoor light at night and obesity in Chinese adults: A national cross-sectional study of 98,658 participants. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9987422/

8. Fonken, L. K. et al. Light at night increases body mass by shifting the time of food intake. *PNAS* (2010). https://www.pnas.org/doi/10.1073/pnas.1008734107

9. Exposure to light at night (LAN) and risk of obesity: A systematic review and meta-analysis of observational studies. *ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0013935120305302

10. Opperhuizen, A. L., Stenvers, D. J., Jansen, R. D., Foppen, E., Fliers, E., & Kalsbeek, A. (2017). Light at night acutely impairs glucose tolerance in a time-, intensity- and wavelength-dependent manner in rats. *Diabetologia*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5487588/

11. Artificial Light at Night and Type 2 Diabetes Mellitus. *e-dmj.org*. https://www.e-dmj.org/journal/view.php?number=2879

12. Exposure to dim light at night alters daily rhythms of glucose and lipid metabolism in rats. *Frontiers in Physiology* (2022). https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2022.973461/full

13. Chronic constant light exposure aggravates high fat diet-induced renal injury in rats. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9372432/

## D. Beslenme Zamanlaması / Zaman-Kısıtlı Beslenme (TRF) ve Kronodisrupsiyon

14. Combining Time-Restricted Wheel Running and Feeding During the Light Phase Increases Running Intensity Under High-Fat Diet Conditions. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12347854/

15. Time-restricted feeding provides limited microglial immunometabolic improvements in diet-induced obese rats. *ScienceDirect* (2025). https://www.sciencedirect.com/science/article/pii/S2211124725011519

16. Su, Y. et al. High-Fat-Diet-Evoked Disruption of the Rat Dorsomedial Hypothalamic Clock Can Be Prevented by Restricted Nighttime Feeding. https://pmc.ncbi.nlm.nih.gov/articles/PMC9735604/ (PubMed: https://pubmed.ncbi.nlm.nih.gov/36501063/)

17. Hepler, C. et al. (2022). Time-restricted feeding mitigates obesity through adipocyte thermogenesis. *Science*, 378(6617). https://www.science.org/doi/10.1126/science.abl8007

18. Synergy between time-restricted feeding and time-restricted running is necessary to shift the muscle clock in male Wistar rats. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11462373/

19. Circadian Disruption and the Risk of Developing Obesity. *Current Obesity Reports* (2025). https://link.springer.com/article/10.1007/s13679-025-00610-6

20. Diet-Induced Obesity and Circadian Disruption of Feeding Behavior. *Frontiers in Neuroscience* (2017). https://www.frontiersin.org/articles/10.3389/fnins.2017.00023/full

21. Circadian Synchronization of Feeding Attenuates Rats' Food Restriction-Induced Anxiety and Amygdalar Thyrotropin-Releasing Hormone Downregulation. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11172148/

22. Early Time-Restricted Feeding Amends Circadian Clock Function and Improves Metabolic Health in Male and Female Nile Grass Rats. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8877212/

23. Delayed Meal Timing, a Breakfast Skipping Model, Increased Hepatic Lipid Accumulation and Adipose Tissue Weight by Disintegrating Circadian Oscillation in Rats Fed a High-Cholesterol Diet. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8280346/

24. Delayed first active-phase meal, a breakfast-skipping model, led to increased body weight and shifted the circadian oscillation of the hepatic clock and lipid metabolism-related genes in rats fed a high-fat diet. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6209334/

25. An Ultradian Feeding Schedule in Rats Affects Metabolic Gene Expression in Liver, Brown Adipose Tissue and Skeletal Muscle with Only Mild Effects on Circadian Clocks. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6214081/

## E. Weight Cycling ve Adipoz Doku Saat Genleri

26. Guo, F. et al. (2013). Weight cycling promotes fat gain and altered clock gene expression in adipose tissue in C57BL/6J mice. *American Journal of Physiology-Endocrinology and Metabolism*. https://journals.physiology.org/doi/full/10.1152/ajpendo.00188.2013 (PubMed: https://pubmed.ncbi.nlm.nih.gov/24302006/)

## F. Weight Cycling Sonrası Kilo Kaybı Müdahalesine Yanıt / "Obezojenik Bellek"

29. Winn, N. C., Cottam, M. A., Bhanot, M., Caslin, H. L., Garcia, J. N., Arrojo e Drigo, R., & Hasty, A. H. (2022). Weight Cycling Impairs Pancreatic Insulin Secretion but Does Not Perturb Whole-Body Insulin Action in Mice With Diet-Induced Obesity. *Diabetes*, 71(11), 2313–2330. https://doi.org/10.2337/db22-0161

30. Repeated weight cycling in obese mice causes increased appetite and glucose intolerance. *ScienceDirect*. https://www.sciencedirect.com/science/article/abs/pii/S0031938418302531

31. Weight cycling exacerbates glucose intolerance and hepatic triglyceride storage in mice with a history of chronic high fat diet exposure. *Journal of Translational Medicine* (2025). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11699648/ (yayıncı sürümü: https://link.springer.com/article/10.1186/s12967-024-06039-0)

32. Weight cycling-induced hypothalamic and metabolic tissue immune remodeling is uncoupled from metabolic dysfunctions. *bioRxiv* (preprint, 2025). https://www.biorxiv.org/content/10.1101/2025.06.27.661006.full.pdf

33. Effects of multiple cycles of weight loss and regain on the body weight regulatory system in rats. *American Journal of Physiology-Endocrinology and Metabolism*. https://journals.physiology.org/doi/prev/20191024-aop/abs/10.1152/ajpendo.00110.2019

34. Weight Cycling Enhances Adipose Tissue Inflammatory Responses in Male Mice. *PLOS One* (2012). https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0039837

*(İlgili tarihsel/karşılaştırmalı referanslar — Winn ve ark. 2022 ve Effects of multiple cycles çalışmalarının kaynakçasında geçen, insan verisi içeren klasik çalışmalar: Fothergill ve ark. 2016, "Biggest Loser" sonrası kalıcı metabolik adaptasyon, *Obesity* 24:1612–1619; Sumithran ve ark. 2011, kilo kaybı sonrası hormonal adaptasyonların uzun süreli kalıcılığı, *NEJM* 365:1597–1604; Smith ve ark. 2018, farelerde weight cycling'in sürekli obeziteye kıyasla yaşam süresini uzattığı bulgusu, *Obesity* 26:1733–1739 — bu makalelerin tam metnine bu oturumda doğrudan erişilmedi, atıf ikincil kaynak üzerinden yapılmıştır.)*

## G. Adipoz Doku Sirkadiyen Fizyolojisi — Genel Referans

27. Daily Gene Expression Rhythms in Rat White Adipose Tissue Do Not Differ Between Subcutaneous and Intra-Abdominal Depots. *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC5936761/

28. Daily Lipolysis Gene Expression in Male Rat Mesenteric Adipose Tissue: Obesity and Melatonin Effects. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11765279/

---

**Not:** Bazı kaynaklar (örn. DMH çalışması, weight cycling çalışması) sohbette birden fazla kez farklı arama sonuçlarıyla eşleşmiştir; burada tekilleştirilmiştir. Kaynakların büyük kısmı PMC/PubMed üzerinden serbest erişimlidir; Science ve bazı Springer Nature makaleleri abonelik gerektirebilir.

## Bağlantılı Notlar
- [[kilo-kaybi-refeeding-kaynaklar-ve-protokol]]
- [[Should we focus on fasting or refeeding?]]
- [[weight-cycling-glp1-cycling-perspektif-taslak]]
- [[Farklı aralıklı açlık türleri yağ dağılımını ve fonksiyonelliğini farklı etkiliyor olabilir mi?]]
- [[Uzun Dönem Başarılı Kilo Kaybıyla İlişkili Genler]]
