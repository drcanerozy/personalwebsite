---
Tür:
  - Besleyici
ODAK:
  - "[[Karaciğer Yağlanması]]"
MEKANİZMA:
DİZİN:
  - "[[Diyet Kalitesi]]"
  - "[[Popüler Diyetler]]"
  - "[[Sağlıklı Beslenme]]"
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[Diyet İlkeleri ve Popüler Diyetler]]"
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Karaciğer Yağlanmasında Kilo Kaybının Etkileri Genetiğe Göre Farklılıklar Gösteriyor]]"
  - "[[Düşük Kalorili Diyetlerde Hepatik ve Periferik İnsülin Direnci]]"
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
| Diyet Modeli                                               | Tanım ve Makro/Kalori Dağılımı                                                                                  | Öne Çıkan / Farklı Özellikleri                                                                                                            | MASLD Bağlamında Etki Mekanizmaları ve Sonuçlar                                                                                                                            |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Akdeniz Diyeti (MedDiet)**                               | Karbonhidrat (KH) %40-45, Yağ %30-35, Protein %15-20. Zeytinyağı, bitkisel gıdalar, balık odaklı.               | MASLD yönetiminde **altın standart** kabul edilir. Doymuş yağ ve kırmızı et kısıtlıdır.                                                   | _De novo_ lipogenezi (yeni yağ sentezi) azaltır, insülin duyarlılığını artırır, oksidatif stres ve inflamasyonu baskılar. Kilo kaybı olmasa bile karaciğer yağını düşürür. |
| **Düşük Karbonhidratlı Akdeniz Diyeti (LCMD)**             | Toplam kalori ihtiyacından 500 kcal açık. KH ≤ %35, Yağ > %45, Protein %15-20.                                  | Standart Akdeniz diyetine kıyasla karbonhidratı daha da kısıtlayıp zeytinyağı/balık yağını artırır.                                       | Trigliserit (TG) ve karaciğer yağlanmasını standart Akdeniz diyetine göre daha hızlı azaltabilir, insülin direncini kırar.                                                 |
| **Düşük Yağlı Akdeniz Diyeti (LFMD)**                      | Toplam kalori ihtiyacından 500 kcal açık. KH ≥ %55, Yağ %20-25, Protein %15-20.                                 | Akdeniz diyetinin yağ oranının standart düşük yağlı diyet seviyelerine çekilmiş halidir.                                                  | Kalori açığı ile vücut ağırlığını ve bel çevresini düşürür, LDL kolesterolde belirgin azalma sağlar.                                                                       |
| **Yeşil Akdeniz Diyeti (GreenMed)**                        | Toplam kalori ihtiyacından 500 kcal açık. KH ~%45, Yağ %35-40, Protein %15-20.                                  | Günlük 28g ceviz, 3-4 fincan yeşil çay ve su mercimeği (Mankai) ile polifenol oranı ekstra artırılmıştır. Kırmızı et çok daha kısıtlıdır. | Standart Akdeniz diyetine göre **karaciğer içi yağ oranını iki kat daha fazla (yaklaşık %39 oranında) azalttığı** kanıtlanmıştır.                                          |
| **Düşük Glisemik İndeksli Akdeniz Diyeti (LGIMD)**         | KH %40-45, Protein %15-20, Yağ %35-40.                                                                          | Kan şekerini hızlı yükselten rafine gıdalar tamamen çıkarılır, düşük glisemik indeksli tam tahıllar seçilir.                              | Glikozun yavaş salınmasını sağlar, tokluk insülinini ve karaciğerde yağ sentezini yavaşlatarak steatozu engeller.                                                          |
| **Çok Düşük Kalorili Ketojenik Diyet (VLCKD/VLEKT)**       | Günlük 600-800 kcal. KH < 50g/gün (sebzelerden), Yağ kısıtlı (sadece 10g zeytinyağı), Protein 0.8-1.2 g/kg/gün. | Hem çok düşük kalorilidir hem de ketozisi hedefler. Sürdürülebilirliği zordur.                                                            | Kısa sürede çok hızlı kilo kaybı ve karaciğer yağında dramatik azalma sağlar (Vücut ağırlığı, BMI ve bel çevresinde en etkili yöntemdir).                                  |
| **İyi Formüle Edilmiş Ketojenik Diyet (WFKD)**             | KH < 50g/gün, Protein 1.2-1.5 g/kg/gün. Yağ alımı doygunluğa göredir (kısıtlama yok).                           | Klasik keto'daki (CKD - %90 yağ) kas kaybı ve yağlanma riskini önlemek için protein ve kolin miktarı optimize edilmiştir.                 | Karaciğerde yağ yakımını (oksidasyon) doğrudan tetikler, keton cisimcikleri hücresel onarımı destekler. Doymuş yağ yüksekse uzun vadede LDL'yi artırabilir.                |
| **İspanyol Ketojenik Akdeniz Diyeti (SKMD)**               | Kalori kısıtlamasız, KH < 30g/gün.                                                                              | Kırmızı et ve doymuş yağlar yerine zeytinyağı, balık, yeşil sebzeler ve kırmızı şaraba dayalıdır.                                         | Ketozisin hızlı yağ yakma etkisi ile Akdeniz diyetinin anti-inflamatuar (Omega-3/polifenol) etkisini birleştirir. Transaminazları ve steatozu hızla düşürür.               |
| **DASH Diyeti (Hipertansiyonu Durdurma Yaklaşımı)**        | Sodyum çok kısıtlı (<2400mg/gün), potasyum, kalsiyum, magnezyumdan zengin. Doymuş yağ kısıtlı.                  | Yüksek tansiyonu önlemek için geliştirilmiş, meyve, sebze ve düşük yağlı süt ürünlerine odaklanan diyet.                                  | Kan basıncını düzenler, trigliseritleri, oksidatif stresi, VLDL üretimini ve LPS (endotoksin) düzeylerini düşürmede çok etkilidir.                                         |
| **Düşük Serbest Şekerli Diyet (LFSD)**                     | Günlük serbest şeker alımı toplam enerjinin ≤ %5'i (veya <10g/gün).                                             | Sadece karbonhidrat değil, özellikle früktoz ve ilave eklenti şekerler sıfırlanır.                                                        | Früktoz kaynaklı toksisiteyi ve yeni yağ üretimini durdurur. Glikoz ve HOMA-IR (insülin direnci) indekslerini iyileştirmede çok etkilidir.                                 |
| **Lakto-Ovo-Vejetaryen Diyet (LOV-D) / Bitki Bazlı Diyet** | Bitkisel gıdalar ağırlıklı, et yok; süt ürünleri ve yumurta serbest.                                            | Hayvansal proteinin getirdiği metabolik yükü kaldırıp bitkisel lif, antioksidan ve fitokimyasalları artırır.                              | Bağırsak mikrobiyotasındaki disbiyozisi onarır. HOMA-IR'yi düşürme ve total kolesterolü iyileştirmede standart zayıflama diyetlerinden üstündür.                           |
| **Portfolio Diyeti**                                       | Toplam kalori kısıtlı. Doymuş yağ ve kolesterol çok düşük.                                                      | Yulaf (beta glukan), bitki sterolleri, badem ve soya proteini içeren kolesterol düşürücü özel diyet.                                      | Karaciğer fonksiyonlarını (AST, ALT) iyileştirmede standart sağlıklı beslenme tavsiyelerine göre daha etkilidir.                                                           |
| **Zaman Kısıtlamalı Beslenme (TRF / TRE)**                 | Klasik 16:8 modeli (16 saat açlık, 8 saat beslenme penceresi). Kalori kısıtlaması şart değildir.                | _Ne_ yendiğinden ziyade _ne zaman_ yendiğine (sirkadiyen ritim) odaklanır. Erken (eTRE) veya geç (lTRE) olabilir.                         | Biyolojik saat ile senkronize olarak yağ oksidasyonunu (yakımını) artırır, otofajiyi (hücre temizliği) tetikler. Karaciğer sertliğini ve glukoz düzeylerini düzeltir.      |
| **Alternatif Gün Orucu (ADF)**                             | Oruç günlerinde sıfır veya %25 kalori (yaklaşık 500 kcal); beslenme günlerinde serbest alım.                    | Standart her gün diyet yapamayanlar için "bir gün diyet, bir gün serbest" mantığı.                                                        | Şiddetli kalori açığı yaratarak visseral yağı (iç organ yağlanması) ve karaciğer içi trigliseritleri hızlı şekilde eritir.                                                 |
| **5:2 Diyeti**                                             | Haftanın 5 günü normal beslenme, ardaşık olmayan 2 günü kadınlar için 500, erkekler için 600 kcal.              | Haftalık bazda aralıklı şiddetli kalori kısıtlaması sunar.                                                                                | Hepatik lipidleri azaltır, karaciğerde PPARα ve PCK1 yollarını uyararak MASH ve fibrozise karşı koruma sağlar.                                                             |
| **Açlığı Taklit Eden Diyet (FMD)**                         | Ayda ardışık 5 gün boyunca düşük kalori (%34-54), düşük protein (%9-11), bitki bazlı diyet.                     | Uzun süreli su orucunun tehlikelerinden kaçınarak hücrelere "açlık" sinyali gönderir.                                                     | Kök hücre yenilenmesini (rejenerasyon) teşvik eder, karaciğerde yağ damlacıklarını temizler ve inflamatuar hücre sızmasını önler.                                          |
| **Tam Diyet Değişimi (TDR)**                               | Günlük 800-850 kcal sağlayan formül mamalarla (çorba, shake vb.) beslenme.                                      | Normal yiyecekler yerine formüle edilmiş sıvı/katı diyet ürünleri kullanılır.                                                             | Özellikle T2DM eşlik eden MASLD hastalarında karaciğer yağında dramatik azalma sağlar.                                                                                     |

