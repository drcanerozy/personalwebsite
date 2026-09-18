# Aralıklı Açlık/TRF Crossover Çalışmalarında Asimetrik Carryover Etkisi: Metodolojik Audit + Yeniden Analiz Protokolü

## 1. Çalışmanın Çekirdek Hipotezi

RoB 2 crossover extension'ın "period and carryover" domain'i carryover etkisini **jenerik ve yön-körü** (symmetric) bir tehdit olarak modelliyor. Enerji kısıtlayıcı diyet müdahalelerinde (TRF/IF) bu varsayım fizyolojik olarak sorunlu: kilo kaybının tetiklediği adaptif termogenez, leptin düşüşü ve iştah hormon değişimleri, kilo alımından/toparlanmadan çok daha yavaş geri döner. Bu nedenle:

- **H1:** A→B ve B→A kollarında gözlenen etki büyüklüğü farkı, sadece "gürültü" değil, sistematik ve öngörülebilir yönde (kilo-kaybı-önce sırası ikinci fazın etkisini küçültür) olmalı.
- **H2:** Yayınlanmış TRF/IF crossover çalışmalarının büyük çoğunluğu washout sonrası **kilonun/metabolik parametrelerin gerçekten baseline'a döndüğünü ölçüp raporlamıyor** — süre geçmesini yeterli görüyor.
- **H3:** RoB 2'de "carryover riski düşük" olarak işaretlenen çalışmaların bir kısmı, bu asimetrik mekanizma açısından yeniden değerlendirildiğinde aslında risk taşıyor.

## 2. Kapsam Kararı: IF (genel) mi, sadece TRF mi?

Karar vermeden önce tartılması gereken noktalar:

- [ ] **Sadece TRF (time-restricted feeding/eating):** Mekanistik argüman en temiz burada kurulur (günlük pencere daraltma → tek değişken). Örneklem küçük kalabilir.
- [ ] **TRF + ADF (alternate-day fasting) + 5:2:** Örneklem büyür ama "kilo kaybı hızı/şiddeti" müdahaleler arası çok farklılaşır — asimetrik carryover büyüklüğü karşılaştırılabilir olmaktan çıkabilir, confound riski artar.
- [ ] **Sadece kilo kaybı/kilo yönetimi birincil sonuç olan çalışmalar** (glisemik kontrol veya performans birincil ise dışla) — mekanistik argüman kilo cyclingile ilgili olduğundan bu daraltma savunulabilir ve muhtemelen doğru seçim.
- **Öneri:** TRF ile başla, ADF'yi duyarlılık analizi (sensitivity subgroup) olarak ekle. Gerekçesini Giriş'te netleştir: "TRF seçildi çünkü en homojen ve en çok crossover-tasarımlı alt-literatür."

## 3. Literatür Tarama Stratejisi

### 3.1 İki Yol Var — Karar Gerekiyor

- **Yol A — Sıfırdan sistematik arama:** PubMed/Embase/Cochrane'de orijinal tarama yap, crossover TRF/IF RCT'lerini tek tek topla.
- **Yol B — "Meta-analizlerin meta-analizi" (umbrella/re-audit yaklaşımı):** Son 2-3 yılda yayınlanmış TRF/IF meta-analizlerinin (ör. Nutrition Reviews 2025, network meta-analiz 2024/2025, Nutrients 2024) dahil ettikleri crossover çalışmaları çıkar, bunları havuzla, tekilleştir.

**Öneri: Yol B ile başla, Yol A ile tamamla.** Gerekçe: (a) hız — dahil edilecek trial havuzunu hızlıca oluşturur, (b) mevcut RoB 2 değerlendirmelerini "referans" olarak kullanıp kendi yeniden-değerlendirmenle karşılaştırma imkanı verir (bu senin orijinal katkının kanıtı olur), (c) ama yeni yayınlanmış (son 6-12 ay) trialler mevcut meta-analizlerde olmayabilir, bu yüzden PubMed'de 2024-Temmuz 2026 aralığında tamamlayıcı bir arama şart.

### 3.2 Arama Terimleri (taslak)

```
("time-restricted feeding" OR "time-restricted eating" OR "intermittent fasting" 
OR "alternate day fasting" OR "5:2 diet")
AND ("crossover" OR "cross-over" OR "within-subject")
AND (weight OR "body composition" OR adiposity)
```

- [ ] MeSH terimleri netleştirilecek (Intermittent Fasting MeSH'i ne zaman eklendi, kapsamı kontrol et)
- [ ] "washout" terimini ayrı bir filtre olarak mı ekleyeceğiz yoksa tarama sonrası full-text'te mi arayacağız? (Öneri: tarama sonrası, çünkü "washout" raporlanmayan çalışmalar da tam olarak ilgi alanımız — arama terimine koyarsan onları kaçırırsın.)
- [ ] Dil filtresi: sadece İngilizce mi, yoksa Türkçe/diğer dillerdeki crossover TRF çalışmaları da (muhtemelen az sayıda) dahil mi?

### 3.3 Kayıt / Ön-kayıt

- [ ] PROSPERO'da bu spesifik sorunun (asimetrik carryover re-audit) daha önce kayıtlı olup olmadığını kontrol et — bulduğum genel IF/TRE meta-analizlerinden ayrışan bir protokol olduğunu göstermek için PROSPERO taraması şart.
- [ ] Kendi protokolünü PROSPERO'ya kaydetmek, "yenilik" iddiasını hakemler nezdinde güçlendirir (tarih damgası).

## 4. Dahil Etme / Dışlama Kriterleri

**Dahil:**
- Randomize, crossover (AB/BA) tasarımlı TRF (± ADF duyarlılık analizinde) çalışmaları
- Yetişkin katılımcılar (sağlıklı veya metabolik hastalıklı, alt-grup olarak ayrıştırılabilir)
- Birincil veya ikincil sonuç olarak kilo/vücut kompozisyonu raporlanmış
- Tam metin erişilebilir

**Dışla:**
- Paralel grup tasarımları
- Randomize olmayan sıralı (sequential, AB-only, randomizasyon yok) tasarımlar → **ayrı bir kategori olarak işaretle, dışlama, çünkü bunlar H2/H3'ün en net örnekleri olabilir** (bkz. §6)
- İnpatient sıkı kontrollü feeding çalışmaları (Hall grubu tarzı) — bunlar ayrı bir alt-grup olarak analiz edilmeli çünkü kasıtlı olarak washout'suz + sıra-randomize tasarım kullanıyorlar, kendi içlerinde farklı bir metodolojik kategori

## 5. Veri Çıkarma Parametreleri (kod defteri — madde madde)

Her çalışma için çıkarılacak alanlar:

1. **Tasarım detayları**
   - [ ] Sıra randomize mi (evet/hayır/belirtilmemiş)
   - [ ] Randomizasyon yöntemi raporlanmış mı (blok, minimizasyon, basit)
   - [ ] Washout süresi (gün/hafta)
   - [ ] Washout süresinin gerekçesi verilmiş mi (fizyolojik dayanak var mı, yoksa keyfi mi)
2. **Baseline dönüş doğrulaması** ⭐ (H2'nin çekirdeği)
   - [ ] İkinci faz öncesi kilo yeniden ölçülmüş mü
   - [ ] İkinci faz baseline'ı, çalışma başlangıcı baseline'ı ile istatistiksel olarak karşılaştırılmış mı (fark testi var mı)
   - [ ] Metabolik parametreler (açlık glukozu, leptin, HOMA-IR vb.) ikinci faz öncesi yeniden ölçülmüş mü
3. **Sonuç verileri (faz ve sıra kırılımında)**
   - [ ] Faz 1 ve Faz 2 için ayrı ayrı etki büyüklüğü (mümkünse sıra alt-gruplarına göre: A→B'de A'nın etkisi vs. B→A'da A'nın etkisi)
   - [ ] Bu kırılım makalede zaten var mı, yoksa yazarlarla iletişime geçip ham veri istemek mi gerekecek (bu noktada gerçekçi ol — çoğu makale bunu raporlamaz, IPD talebi zaman alır ve düşük yanıt oranı olur)
4. **Risk of bias**
   - [ ] Mevcut RoB 2 crossover extension puanı (eğer bir meta-analizde zaten değerlendirilmişse, kaynağını not al)
   - [ ] Senin yeniden-değerlendirmen (asimetrik carryover mercekli, ayrı bir checklist — bkz. §7)
5. **Müdahale özellikleri**
   - [ ] Pencere uzunluğu, erken/geç TRF, faz süresi (kaç hafta), kalori kısıtlaması eşlik ediyor mu (isokalorik mi, ad libitum mu)
   - [ ] Beklenen kilo kaybı büyüklüğü (faz başına) — büyük kayıplı çalışmalarda asimetrik carryover teorik olarak daha belirgin olmalı, bu bir doz-yanıt analizi imkanı verir

## 6. Ayrı Bir Alt-Bulgu: Randomize Olmayan "Sözde-Crossover" Taraması

- [ ] Dışlanan ama "sequential/non-randomized AB" olarak işaretlenen çalışmaları ayrı bir tabloda tut — bunların sayısı/oranı tek başına raporlanabilir bir bulgu ("TRF crossover literatüründe X çalışmadan Y'si aslında randomize değil, crossover olarak etiketleniyor" gibi bir gözlem, kısa bir paragraf/tablo olarak makaleye eklenebilir, ayrı bir yayın gerektirmez).

## 7. Yeniden Değerlendirme Checklist'i (RoB 2'den farkı burada)

Standart RoB 2 crossover carryover sorularına ek olarak:

- [ ] Washout süresi, o spesifik müdahalenin bilinen adaptif fizyolojik geri-dönüş kinetiğine (leptin yarı ömrü, adaptif termogenezin bilinen toparlanma süresi vb.) göre gerekçelendirilmiş mi, yoksa jenerik/keyfi mi
- [ ] Sıra (A→B vs B→A) alt-gruplarında etki büyüklüğü ayrı raporlanmış mı — raporlanmışsa, fark yönü H1 ile tutarlı mı (kilo-kaybı-önce sıradaki ikinci faz etkisi küçülüyor mu)
- [ ] Yazarlar carryover'ı limitation olarak tartışmış mı, tartışmışsa hangi mekanizmaya atıfla (varsa)

## 8. İstatistiksel Yeniden Analiz Planı

- [ ] Ham veri/yayınlanmış ortalama+SD'ler yeterliyse, sıra × dönem etkileşim testi (interaction term) her çalışma için yeniden hesaplanabilir mi
- [ ] Meta-regresyon: bağımlı değişken = sıra etkisi büyüklüğü, açıklayıcı değişken = washout süresi, faz süresi, beklenen kilo kaybı büyüklüğü → "hangi tasarım parametreleri asimetrik carryover riskini öngörüyor" sorusuna cevap
- [ ] Güç analizi gerçekçiliği: kaç çalışmanın sıra-kırılımlı verisi olacak, bu sayı meta-regresyon için yeterli mi (muhtemelen az olacak — bu bir limitation olarak baştan kabul edilmeli, abartılı istatistiksel iddiada bulunma)

## 9. Kılavuz/Standart Referansları (Giriş ve Yöntem'de kullanılacak)

- [ ] CONSORT 2010 crossover trial extension
- [ ] Cochrane RoB 2 (crossover trials) rehberi
- [ ] Senn S. — Cross-over Trials in Clinical Research (klasik metodoloji kaynağı, carryover kavramının kökeni)
- [ ] PRISMA 2020 (eğer sistematik review/audit formatında gidilirse)
- [ ] Meta-Research Reporting Guidelines (MR-CRES veya benzeri, eğer "audit/meta-research" olarak çerçevelenirse — bu format PRISMA'dan farklı, kontrol edilmeli)

## 10. Hedef Dergi ve Format Kararı

- [ ] **Kısa format (Letter/Commentary + küçük re-analiz tablosu):** Obesity Reviews, Nutrition Reviews, International Journal of Obesity — hızlı, ama ampirik ağırlık az olursa reddedilme riski yüksek
- [ ] **Tam metodolojik audit/scoping review formatı:** Obesity Reviews, Advances in Nutrition, veya bir meta-research dergisi (ör. BMC Medical Research Methodology) — daha uzun sürer ama H2/H3 iddialarını sistematik veriyle destekleyince çok daha savunulabilir
- **Öneri:** §3.1'deki Yol B taraması bittikten sonra, kaç çalışma toplandığına bakıp karar ver. 15-20 üstü crossover TRF çalışması varsa tam audit formatı; altındaysa commentary + tablo formatı daha gerçekçi.

## 11. Riskler / Dürüst Sınırlamalar (baştan not edilmesi gereken)

- [ ] Sıra-kırılımlı veri çoğu makalede raporlanmıyor olabilir → H1'in istatistiksel testi zayıf kalabilir, o zaman argüman büyük ölçüde kavramsal/tanımlayıcı kalır (bu da hâlâ yayınlanabilir ama iddia seviyesini buna göre ayarlamak gerekir)
- [ ] "Asimetrik carryover" mekanizması (leptin/adaptif termogenez toparlanma kinetiği) için kesin zaman aralıkları literatürde net değil — bu belirsizliği gizlemeden, bir sınırlama olarak yazılmalı
- [ ] Yazar iletişimi (IPD talebi) planlanıyorsa düşük yanıt oranı gerçekçi beklenti olmalı, zaman çizelgesine dahil edilmeli

## 12. Sonraki Adım (bir sonraki oturumda)

- [ ] §3.1 kararını ver (Yol A/B/karma)
- [ ] §2 kapsam kararını ver (sadece TRF mi)
- [ ] PROSPERO ön-taramasını yap (bu spesifik audit'in kayıtlı olup olmadığı)
- [ ] İlk 5 çalışmayla pilot veri çıkarma denemesi yap, kod defterinin (§5) pratikte çalışıp çalışmadığını test et

## Bağlantılı Notlar
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
- [[Effect_Size_Landscape_Proje_Notu]]
- [[TRF_Tutumlu-Savurgan_Fenotip_Calisma_Taslagi]]
- [[ev-yapimi-upf-kavrami]]
- [[Diyet Müdahalelerinde Kas Kaybının Yeniden Yorumlanması]]
