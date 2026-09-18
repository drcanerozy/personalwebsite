---
tags: [çalışma-fikri, GFN, nutritional-geometry, NHANES, protein-leverage, CIM]
oluşturulma: 2026-07-17
durum: değerlendirme aşamasında
---

# Geometric Framework for Nutrition (GFN) Temelli Çalışma Hattı

## Arka plan / temel tez

İnsan beslenme epidemiyolojisinde Geometric Framework for Nutrition (GFN, Raubenheimer & Simpson) büyük ölçüde **toplam makro düzeyinde** kalmış:
- 2003 pilot çalışma: protein alımının karbonhidrat+yağdan daha sıkı regüle edildiğini gösterdi (protein leverage'ın temeli).
- 2016: 116 diyetin meta-analitik geometrik haritalaması (yine sadece makro üçgeni).
- Cohen & Raubenheimer 2020: 1560 yaşlı yetişkinde GFN'yi biyolojik yaşlanma biyobelirteçleriyle birleştirdi — büyük ölçekli insan epidemiyolojisinde nadir örnek.
- Simpson ve ark. 2017 (precision medicine makalesi): GFN'nin makro-kalitesi (SFA/MUFA/PUFA, karbonhidrat alt tipleri, amino asit dengesi) boyutuna **henüz genişletilmediğini açıkça belirtiyor** — bu, literatürün kendi işaret ettiği ama doldurulmamış bir boşluk.

Hedonik iştah + GFN kombinasyonuna dair spesifik bir insan çalışmasına rastlanmadı; bu da potansiyel özgün bir açık.

## Genel kısıt

NHANES gibi kesitsel veri setleriyle **nedensellik iddia edilemez**. Hem CIM hem PLH temelde nedensel/dinamik mekanizmalar öne sürüyor; kesitsel response-surface ile sadece "hangi model gözlenen örüntüyle daha uyumlu" denebilir. Ters nedensellik (adipozitenin diyet alımını/iştahı etkilemesi) her makalede açık sınırlama olarak yazılmalı.

---

## Makale 1 — Kavramsal / Perspective (öncelikli)

**Format:** Perspective / Opinion / Narrative Review (orijinal veri yok, literatür sentezi + yeni kavramsal model).

**Tez:** GFN, CIM (karbonhidrat-insülin modeli) ve PLH (protein leverage hipotezi) gibi rakip obezite teorilerini birleştirici/test edici bir üst-çerçeve olarak kullanılabilir; ayrıca makro-alt-tip boyutuna genişletilmesi gerekiyor.

**Taslak yapı:**
1. Giriş — tek-besin-öğesi paradigmasının sınırları
2. GFN'nin temel mantığı (teknik olmayan okuyucu için)
3. CIM ve PLH'nin GFN diliyle yeniden ifadesi — **orijinal şematik response-surface diyagramı** (kendi çizeceğim, kavramsal illüstrasyon, veri değil)
4. Mevcut insan çalışmalarının kapsam taraması (tablo: hangi çalışma hangi boyutu kullanmış)
5. Boşluk analizi + önerilen araştırma gündemi (Makale 2'nin gerekçesi)
6. Metodolojik uyarılar (harmonizasyon, ölçüm hatası, RSM varsayımları, kesitsel sınırlama)

**Hedef dergiler:** Obesity Reviews, Advances in Nutrition, Nutrition Research Reviews (Nutrition Reviews'a da aşinalığım var, oraya da bakılabilir).

---

## Makale 2 — Ampirik, NHANES tabanlı (ana hat)

**Neden NHANES:** 24 saatlik hatırlatmadan üç makro + FNDDS alt tipleri (SFA/MUFA/PUFA, şeker/lif), açlık insülini/glukoz/HOMA-IR (belirli döngülerde), bel çevresi ve bazı döngülerde DXA ile adipozite, trigliserid/HDL — hepsi tek veri setinde, ücretsiz.

**Ana analiz:** CIM ve PLH öngörülerini aynı response-surface modelinde (mixture triangle / RSM) insülin ve adipozite çıktılarıyla yan yana test etmek.
- CIM öngörüsü: karbonhidrat/glisemik yük → insülin yanıtı → adipozite (insülin merkezli, karbonhidrat-spesifik)
- PLH öngörüsü: düşük protein oranı → toplam enerji alımı artışı → adipozite (protein merkezli, genel makro-oranı)

**Kademeli genişletme (tek modelde her şeyi birden koymamak için):**
1. Temel: protein:karbonhidrat:yağ üç boyutlu mixture triangle
2. Duyarlılık analizi: yağ alt tipleri (SFA:MUFA:PUFA)
3. Duyarlılık analizi: karbonhidrat alt tipleri (şeker/lif) — NHANES'te doğrudan mevcut
4. İsteğe bağlı ek katman: glisemik indeks/yük — FNDDS kodlarının harici GI veritabanına (Sydney Üniversitesi GI tablosu) eşlenmesi gerekir, iş yükü yüksek; ayrı bir alt-analiz veya üçüncü makale olarak düşünülebilir.

**Zamansal uzantı (opsiyonel, güçlü ek):** NHANES'in tekrarlı kesitleri (1999'dan beri ~2 yıllık döngüler) kullanılarak makro-oranı-adipozite response-surface yüzeyinin zaman içinde kayıp kaymadığı incelenebilir (örn. UPF payının arttığı dönemlerde protein leverage etkisinin güçlenip güçlenmediği) — UPF ilgi alanımla organik olarak örtüşüyor.

**Hedef dergiler:** British Journal of Nutrition, Nutrients, (daha yüksek çıtayla) American Journal of Clinical Nutrition.

---

## Ek/alternatif fikirler (değerlendirildi)

### A. Diyet fenotip kümeleme (Akdeniz, HPD, LPD, IF, düşük KH vb.) + kesitsel trend
**Durum: kalabalık alan, düşük öncelik.** NHANES üzerinde makro-küme + mortalite ilişkisini "3D cube" yöntemiyle inceleyen (2024-2025) ve Akdeniz/DASH/MIND skorlarıyla çeşitli çıktıları inceleyen çok sayıda güncel yayın mevcut. Yöntem (kümeleme + çıktı ilişkisi) özgün değil.
**Olası fark yaratma noktası:** Ad hoc kümeleme yerine GFN'nin mixture-triangle'ını kullanmak ve zaman içindeki geometrik kaymayı izlemek. Ana hikaye olarak değil, Makale 2'ye küçük bir ek analiz veya üçüncü öncelikli iş olarak düşünülmeli.

### B. Düşük protein-uzun ömür vs yüksek protein-sağlık paradoksu
**Durum: paradoks zaten belgelenmiş, GFN reframing özgün olabilir.**
- Levine ve ark. (Cell Metabolism, 2014): NHANES III + ulusal ölüm kaydı bağlantısı kullanarak 50-65 yaş grubunda yüksek proteinin artmış mortalite, 65+ grubunda ise koruyucu etki ile ilişkili olduğunu gösterdi (IGF-1 aracılı, yaşa bağlı ters etki).
- Solon-Biet ve ark. (Cell Metabolism, 2014): fare çalışmasında GFN'yi doğrudan kullanarak düşük protein/yüksek karbonhidratın yaşam süresini uzattığını gösterdi.
- **Veri seti hazır:** NHANES III + mortalite bağlantı dosyaları (ücretsiz, halka açık).
- **Özgün katkı fırsatı:** Klasik Cox regresyonu/tertil karşılaştırması yerine, **GFN response-surface ile yaşı üçüncü boyut/etkileşim ekseni olarak modelleyip**, "optimal protein:nonprotein enerji oranı yaşla nasıl kayıyor" sorusunu geometrik yüzey üzerinde göstermek. Bu soru literatürde geometrik olarak sorulmamış.
- Makale 2'ye üçüncü alt-analiz olarak ya da ayrı kısa bir makale (research letter / brief report) olarak eklenebilir.

#### B'nin görselleştirme/analiz tasarımı (Solon-Biet 2014 tarzı sliced response surface)

GFN'nin klasik "nutrient rails" yöntemi: protein sabit bir dilimde tutulup karbonhidrat:yağ ekseni gezdiriliyor. İnsan verisine uyarlanmış panel yapısı:

- **Panel A (düşük protein):** protein enerji yüzdesi sabit/dar aralıkta tutulur, x ekseni karbonhidrat:yağ oranı, y ekseni çıktı (mortalite riski / IGF-1 / metabolik biyobelirteç).
- **Panel B (yüksek protein):** aynı yapı, yüksek protein diliminde.
- İki panel yan yana konarak protein seviyesinin karbonhidrat:yağ ekseninin çıktı üzerindeki etkisini nasıl **moderatörlediği** görsel olarak karşılaştırılır.

**Aşama 1 — Temel model (öncelik):**
- Protein dilimleme: hem NHANES-içi tertil/persentil kesimi hem literatür temelli sabit eşikler (<%10 / >%20 enerji gibi) paralel çalıştırılıp duyarlılık analizi olarak raporlanacak.
- Yaş ayrımı yapılmadan genel modelle başlanacak; yaş × protein × KH:yağ etkileşimi ikinci adımda eklenecek (gerekirse Levine 2014'teki ≤65/66+ kesimiyle karşılaştırmalı).
- Çıktılar: mortalite (NHANES III + ulusal ölüm kaydı bağlantısı varsa), yoksa/ek olarak HOMA-IR, IGF-1 (mevcutsa), adipozite göstergeleri.

**Aşama 2 — Kalite katmanı (ayrı takip makalesi):**
- Aşama 1 miktar/oran modeli net bir bulgu ortaya koyduktan sonra, protein kaynağı (hayvansal/bitkisel), karbonhidrat kalitesi (şeker/lif), yağ kalitesi (SFA/MUFA/PUFA) aynı panel mantığıyla ikinci bir makalede test edilecek.
- Bu ayrım hem kapsam şişmesini önler hem de Aşama 1'in temiz bir "miktar meselesi mi kalite meselesi mi" sorusuna cevap vermesini sağlar.

---

## Genel değerlendirme

Üç ayaklı hat (Makale 1 kavramsal + Makale 2 NHANES ampirik + B: yaş-protein-longevity uzantısı) birlikte, kesitsel sınırlama açıkça belirtilerek ilerlenirse **yeterli ve sağlam bir temel**. A fikri (diyet fenotip kümeleme) düşük öncelikli, en fazla küçük bir ek analiz olarak değerlendirilmeli.

## Sıradaki somut adımlar
- [ ] NHANES döngülerinden hangi yıllarda hangi değişkenlerin (insülin, DXA, leptin, mortalite bağlantısı) birlikte mevcut olduğuna dair kapsam tablosu çıkar
- [ ] Makale 1 için mevcut insan GFN çalışmalarının sistematik tarama tablosunu oluştur
- [ ] Kavramsal response-surface şemasının ilk taslağını çiz (CIM vs PLH karşılaştırması)
- [ ] GI/GL eşleme iş yükünü değerlendir (Sydney GI tablosu ↔ FNDDS kodları)

## Bağlantılı Notlar
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
- [[FAOSTAT- Besin Alımının Uzun Vadeli İzlemi ve Değişen Beslenme Paradigmaları]]
- [[NHANES ile Bağlantılı Çalışma Fikirleri]]
- [[Vücut Ağırlığı Modelleri ve Obezite Hipotezlerine Dayanarak Geliştirilen İdeal Diyet Modeli]]
- [[Adipoz Doku]]
