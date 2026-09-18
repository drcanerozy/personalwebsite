GLP-1 #çalışmafikri #nutrientdensity

1. Araştırma Sorusu ve Gerekçe

GLP-1 RA kullanıcılarında nutrient density (besin ögesi yoğunluğu) indekslerinin (NRF9.3, MAR, DQI gibi) vücut kompozisyonu, kilo kaybı ve besin ögesi yetersizliğiyle ilişkisini gösteren bir çalışma **literatürde yok**. Üç ayrı kol var ama hiçbiri birleşmemiş:

- **Diyet kalitesi (HEI bazlı):** GLP-1RA kullanıcılarında HEI skoru 54±12 (n=69), hedefin belirgin altında; kalori/protein akşam öğününe kayıyor (Johnson et al., Frontiers in Nutrition 2025 / ScienceDirect secondary analysis).
- **Mikrobesin yetersizliği:** NHANES/claims tabanlı retrospektif analizler ve narrative review'ler (demir, B12, folat, D vitamini, tiamin eksikliği vakaları dahil).
- **Vücut kompozisyonu:** BIA/DXA ile yağ-kas kütlesi takibi yapan çalışmalar, ama diyet verisiyle hiç bağlanmamış.

**Boşluk:** Nutrient density indeksini hesaplayıp hem vücut kompozisyonu değişimiyle hem kilo kaybı hızıyla ilişkilendiren çalışma yok. Sistematik derleme düzeyinde de doğrulanmış: RKÇ'lerin çoğu diyet kalitesini raporlamıyor (Jansson et al., Obesity Reviews 2026; Babazadeh/Wyatt/Steinberg, Advances in Nutrition 2025 — 129 RKÇ taranmış, sadece 10'u diyet sonucu raporlamış).

2. Alternatif 1 — NHANES Pooled Kesitsel Analiz (En Hızlı, Ücretsiz)

**Yöntem:** 2013-2014'ten 2017-March 2020 cycle'larına kadar `RXQ_RX` (jenerik ilaç ismiyle GLP-1RA kullanıcı tanımlama) + `DR1TOT`/`DR2TOT` (24-saat besin hatırlatma, NRF9.3 hesaplama) + `BMX` (antropometri) birleştirilir.

**Kritik kısıt — NHANES ilaç verisi:**
- 2013-March 2020 cycle'ları: `RXQ_RX` jenerik ilaç ismi içeriyor, GLP-1RA filtrelenebiliyor. Ama bu pencere Wegovy'nin obezite onayından (Haziran 2021) önce biter — yakalanan kullanıcılar neredeyse tamamen **T2DM endikasyonuyla** eski GLP-1RA (exenatid, liraglutid, dulaglutid, erken semaglutid) kullanan hastalar. Obezite-only, yüksek doz, kısa süreli kullanıcı profili (bugünkü gerçek popülasyon) bu veri setinde yok denecek kadar az.
- **2021-2023 cycle'ı (Ağustos 2021-Ağustos 2023) kullanılamaz:** Bu cycle'da detaylı reçete ilaç ismi, kullanım süresi ve nedeni toplanmadı — sadece "son 1 ayda reçeteli ilaç kullandın mı" kaba sorusu var. Jenerik isimle GLP-1 filtrelemek mümkün değil, proxy soru da yok (statin çalışmalarında olduğu gibi bir vekil soru GLP-1 için mevcut değil).
- **Antropometri sorunsuz:** `BMX` (ağırlık, boy, bel/kalça çevresi, BMI) her cycle'da tam, 2021-2023 dahil.
- **DXA vücut kompozisyonu 2018'de kesildi**, 2021-2023'te hiç yok. Bel çevresi/BMI/WHtR gibi antropometrik indekslerle idare etmek gerekiyor, doğrudan yağ/yağsız kütle verisi yeni cycle'larda yok.

**Pratik tasarım:** Küçük ama temiz örneklem (muhtemelen birkaç yüz kişi, T2DM ağırlıklı). GLP-1 kullanıcı alt-grubunda NRF9.3'ü düşük/orta/yüksek tertillere ayırıp BMI, bel çevresi, (varsa) kilo kaybı yüzdesi arasında fark var mı diye bakmak — kesitsel dizaynla uyumlu, "doz-yanıt benzeri" ilişki kurma imkanı, nedensellik iddia etmeden. Referans/karşılaştırma noktası: genel popülasyonda NRF9.3-antropometri ilişkisi zaten çalışılmış (Rotterdam kohortu, düzeltilmiş modellerde NRF9.3 skorunun BMI/bel çevresi/WHtR ile pozitif ilişkili çıktığı, oysa ham veride yüksek NRF9.3'lü kişilerin enerji alımının daha düşük olduğu bulunmuş) — GLP-1 popülasyonunda bu ilişki korunuyor mu, tersine mi dönüyor, kayboluyor mu sorusu özgün bir açı olur.

3. Alternatif 2 — UK Biobank (Boylamsal, Ücretsiz Değil/Hızlı Değil, Ama Özgün)

**Diyet verisi güçlü:** Oxford WebQ (tekrarlı 24-saat hatırlatma) — 4 davet turunda 176.012 kişi en az bir kez, %66'sı birden fazla kez, %16'sı 4 turun tamamını tamamlamış. Boylamsal diyet kalitesi hesaplamak metodolojik olarak mümkün, örneklem çok büyük.

**Reçete verisi:** GP-linked primary care records üzerinden mevcut (subset'te).

**Boşluk burada da var:** UK Biobank'te GLP-1 üzerine çalışan iki grup var, hiçbiri diyete girmiyor:
- GLP1R genetik çalışmaları (GWAS, yan etki/etkinlik tahmini) — 27.885 kişide self-report kilo kaybı ve yan etkilerin genom-çapında ilişkisi, GLP1R'de etkinlikle ilişkili missense varyant bulunmuş. Bu ekip GLP-1 kullanıcı fenotipleme konusunda deneyimli ama diyet değişkeni kullanmamış.
- Nadir GLP1R varyant/obezite çalışmaları — T2D riskiyle ilişkilendirme, yine genetik odaklı.

**Erişim gerçeği:** UK Biobank başvurusu ücretli ve aylar sürebilir — "ücretsiz hızlı" kategorisine girmiyor. Bu yüzden öncelik: erişim almadan önce yazışma/işbirliği yoluyla fikir/metodoloji netleştirmek.

4. İletişim Stratejisi — Kimlere Mail Atılabilir

**NHANES/ABD tarafı (nutrient density + GLP-1 gap'i işaret edenler):**
- **Johnson B, Milstead M, Thomas O, McGlasson T, Green L, Kreider R, Jones R** — "Investigating nutrient intake during use of glucagon-like peptide-1 receptor agonist: a cross-sectional study", *Frontiers in Nutrition*, 2025 (n=69, 3 günlük besin kaydı + DRI karşılaştırması). Ellerinde ham besin kaydı verisi var, NRF9.3 hesaplaması için ek analiz/işbirliği teklif edilebilir. Not: GNC Holdings (endüstri) finansmanlı — bağımsızlık açısından dikkate alınmalı.
- **Dashti HS, Szczerbinski L** — "The Silent Weight of Nutrition Data in Glucagon-Like Peptide-1 Receptor Agonists Clinical Trials", *Advances in Nutrition*, 2025 (MGH/Harvard Medical School + Medical University of Bialystok). Boşluğu kavramsal olarak yazıyla işaret etmişler, orijinal fikir teklifine açık olabilirler.
- **Babazadeh D, Wyatt S, Steinberg FM** (UC Davis Nutrition) — "Examining the Omission of Dietary Quality Data in Glucagon-Like Peptide 1 Clinical Trials: A Scoping Review", *Advances in Nutrition*, 2025. 129 RKÇ'yi taramışlar, hangi trial'ların diyet verisi topladığını (ama raporlamadığını) biliyorlar — IPD talebi için hangi trial'lara yönelmek gerektiği konusunda rehberlik verebilirler.
- **Jansson AK ve ark.** — "A systematic review identifying critical evidence gaps in reporting dietary change in randomized controlled trials prescribing liraglutide, semaglutide, or tirzepatide", *Obesity Reviews*, 2026. En güncel/geniş kapsamlı gap-analizi, iyi bir ilk temas noktası.

**UK Biobank/İngiltere tarafı (öncelik sırasıyla):**
1. **Basso M, Zhang L, Savva GM, Cohen Kadosh K, Traka MH** (Quadram Institute Bioscience / University of Surrey, Guy's & St Thomas' NHS Trust) — GLP-1 tedavisine başlayan obez hastalarda en uygun dijital diyet değerlendirme aracını belirlemeye yönelik fizibilite çalışması (NCT07194317, henüz recruit etmemiş — NOT_YET_RECRUITING). En sıcak temas: kurulum aşamasındalar, nutrient density indeksi entegrasyonu önerilebilir.
2. **Oxford WebQ geliştiricileri** (Oxford Population Health / Cancer Epidemiology Unit — Bette Liu, Heather Young, Francesca Crowe, Naomi Allen ekibi) — aracın metodolojisini kendileri yayınlamışlar. GLP-1 alt-grup analizi için metodolojik danışmanlık istenebilir, UK Biobank başvurusu öncesi görüş almak mantıklı.
3. **Jackson SE, Brown J, Llewellyn C, Mytton O, Shahab L** (UCL) — "Prevalence of use and interest in using glucagon-like peptide-1 receptor agonists for weight loss: a population study in Great Britain", 2026 (Smoking Toolkit Study, n=5893). UK Biobank değil ama İngiltere'de GLP-1 kullanıcı fenotipleme/anket metodolojisinde taze deneyim — ortak başvuru tasarımı için iyi aday.
4. **UK Biobank GLP1R genetik grubu** (GWAS/yan etki analizi ekibi) — GLP-1 kullanıcı fenotipleme boru hattı (self-report + reçete linkage) kurulu, ama ana ilgi alanları farmakogenomik. İkincil öncelik.

5. Önerilen Yol Haritası

1. Paralel iki mail: (a) Quadram/Guy's ekibine somut katkı teklifiyle ("fizibilite çalışmanıza NRF9.3 eklemek ister misiniz"), (b) Oxford WebQ grubuna danışma talebiyle ("UK Biobank'te GLP-1 alt-grubunda diyet kalitesi değişimini incelemek istiyorum, metodolojik yol haritası konusunda görüşünüzü alabilir miyim").
2. Paralelde NHANES 2013-2020 pooled analizle hızlı, düşük maliyetli bir pilot/hipotez-üretici makale çıkarmak — literatürde konumlanmayı sağlar, yukarıdaki gruplarla temasa geçerken elinde somut iş (sadece fikir değil) olur.
3. IPD talebi (Vivli/YODA) için başvuru sürecini şimdiden başlatmak — zaman aldığından paralel yürütülebilir; Babazadeh/Wyatt/Steinberg'in hangi trial'ların diyet verisi topladığını bilmesi bu başvuruyu hedefli hale getirir.

## Bağlantılı Notlar
- [[NHANES ile Bağlantılı Çalışma Fikirleri]]
- [[GLP-1 Kullanan Hastalarda Nutrient Density Density Yaklaşımlı RCT]]
- [[GLP-1 Kullanan Hastalar için Mikrobiyota Temelli Müdahaleler]]
- [[GLP-1 İlaçlarının Ortaya Çıkışı ve Kliniğe Girişi]]
- [[Gelecek GLP-1 İlaçları]]
