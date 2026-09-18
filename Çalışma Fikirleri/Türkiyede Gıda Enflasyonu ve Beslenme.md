---
Tür: Orijinal Araştırma — Ekolojik Zaman Serisi + Normatif Diyet Maliyet Modeli
ODAK: Hiperenflasyon → Diyet Kalitesi Uçurumu → Nutrisyonel Histerez Hipotezi
MEKANİZMA: NRF/TL endeksi çöküşü + besin güvencesizliği korelasyonu + dezenflasyonda asimetrik toparlanma
DİZİN: Beslenme Ekonomisi; Gıda Güvencesi; Diyet Maliyet Modeli; Halk Sağlığı Beslenmesi
ETİKET: food-inflation, dietary-quality, Turkey, nutritional-hysteresis, diet-cost-modeling, NRF, food-insecurity, FIES, GYKA, COICOP, HBSA
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM: Tam revizyon — diyet maliyet modeli (NRF9.3/TL), besin güvencesizliği korelasyonu (FIES+GYKA), nutrisyonel histerez hipotezi ve UPF/adipoz/elastikiyet mekanizmaları eklendi (2026-09-13)
KAYNAK:
study_type: ecological time-series + normative diet cost modeling
evidence_direction:
primary_outcome: nutritional purchasing power index + food insecurity correlation
p_value_summary:
---

> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

# Nutrisyonel Histerez: Türkiye Hiperenflasyon Sonrası Diyet Kalitesi Dezenflasyonla Toparlanıyor mu?

## Temel Hipotez

**Tanım:** Hiperenflasyon ortamları beslenme kalitesinde tersine dönmeyen hasar yaratır. Fiyatlar düşse bile diyet kalitesi eşzamanlı toparlanmaz — bu gecikme "nutrisyonel histerez" olarak adlandırılır.

**Merkezi Soru:**
> Türkiye'nin 2024 dezenflasyon sürecinde sağlıklı diyetin TL cinsinden maliyeti düşüyor mu? Besin güvencesizliği göstergeleri toparlanıyor mu? Ve bu iki toparlanma senkronize mi, yoksa asimetrik mi?

Bu soruyu bir ekonomist soramaz (mekanizmayı bilmez), davranış bilimcisi soramaz (biyolojik izi görmez). Beslenmeci olarak özgün katkı: fiyat-kalite ilişkisinin besin ögesi düzeyindeki yansıması + adipoz doku biyolojisindeki kalıcı iz.

---

## Özgünlük — Literatür Boşluğu

| Ne Yapıldı | Kim | Eksik |
|---|---|---|
| Türkiye gıda fiyat dinamikleri (ekonometrik) | Cambridge Working Paper 2023 | Beslenme kalitesi metriği yok |
| Türkiye tüketici davranışı enflasyon altında (Bayesian ağ) | Frontiers 2026 | NRF/TL hesabı yok, biyoloji yok |
| Diyet maliyet modeli (ABD, Fransa, Brezilya) | Drewnowski ve ark. | Hiperenflasyon dönemi yok, histerez sorusu yok |
| FIES korelasyonları (küresel) | FAO 2024 | Türkiye dezenflasyon penceresi yok |

**Boşluk:** Türkiye'de hiperenlasyon + dezenflasyon dönemini kapsayan, gerçek besin bileşimi verisi kullanan, besin güvencesizliğiyle korelasyonu kuran, ve diyet kalitesinin geri dönmeyebileceği hipotezini test eden çalışma yok.

---

## Metodoloji: Üç Entegre Bileşen

### Bileşen 1 — Normatif Diyet Maliyet Modeli (NRF9.3/TL Endeksi)

**Kavramsal Çerçeve**

Drewnowski'nin "nutrient density per monetary unit" modelini Türkiye hiperenflasyon dönemine uygula. Temel metrik:

```
NRF9.3 Skoru = (protein + lif + A vit + C vit + D vit + kalsiyum +
                 demir + potasyum + magnezyum) / (doymuş yağ + şeker + sodyum)
                 — 100 kcal başına standardize edilmiş

NRF/TL = NRF9.3 Skoru / o besinin TL fiyatı (100 kcal başına)
```

Yüksek NRF/TL → o TL'ye iyi beslenme satın alıyorsun.
Düşük NRF/TL → o TL'ye sadece kalori satın alıyorsun.

**Referans Besin Sepeti (40–50 madde)**

| Grup | Temsil Besinler |
|---|---|
| Protein (yüksek NRF) | Tavuk (but), yumurta, mercimek, nohut, ton balığı |
| Süt grubu | Yoğurt (%2), beyaz peynir, süt |
| Tam tahıl | Tam buğday ekmeği, bulgur, yulaf |
| Sebze | Domates, ıspanak, brokoli, havuç, soğan |
| Meyve | Elma, portakal, muz, üzüm |
| Sağlıklı yağ | Zeytinyağı, ceviz |
| UPF karşılaştırma | Bisküvi, salam/sosis, hazır çorba, meyve nektarı, cips, ayçiçek yağı |

**Veri Kaynakları — Bileşen 1**

| Kaynak | İçerik | Erişim |
|---|---|---|
| TürKomp (turkomp.tarimorman.gov.tr) | Her besin için NRF bileşenleri (makro+mikro) | Ücretsiz web; ~40 besin için manuel derleme |
| EVDS COICOP alt serileri | Aylık fiyat endeksleri, 2018–2024 | Ücretsiz, Python API |
| Piyasa fiyatı baz yılı | 2023 market fiyatları (BİM/A101 katalogları, Tarım Bakanlığı girdi izleme) | Kısmen açık |

**Hesaplama mantığı:** 2023 market fiyatlarını baz al → EVDS endeksleriyle 2018'e geri ve 2024'e ileriye deflate et → her yıl için NRF/TL hesapla.

**Analitik Adımlar**
1. 40–50 besin için TürKomp'tan NRF9.3 bileşenlerini derle (Excel tablosu)
2. Her besin için 2023 baz fiyat → EVDS'le 2018–2024 aylık fiyat serisi oluştur
3. Her besin için yıllık ortalama NRF/TL hesapla
4. Besin gruplarını ortalamayla birleştir → grup bazında NRF/TL endeksi (2019=100 baz)
5. Sağlıklı sepet vs. UPF sepeti NRF/TL trendlerini karşılaştır
6. Histerez testi: 2024 endeksi 2019 seviyesine geri döndü mü?

---

### Bileşen 2 — Besin Güvencesizliği Korelasyonu

**Veri Kaynakları — Bileşen 2**

| Kaynak | Gösterge | Kapsam | Erişim |
|---|---|---|---|
| FAO FIES (FAOSTAT → Food Security Indicators) | Orta+şiddetli besin güvencesizliği prevalansı (%) | 2015–2023, yıllık, ulusal | Ücretsiz indirme / API |
| TÜİK GYKA | "Yeterli gıdaya erişimde güçlük yaşayan hane %" | 2018–2023, yıllık | Ücretsiz bülten |
| DİSK-AR yoksulluk sınırı raporları | Açlık sınırı / yoksulluk sınırı TL, gelir dilimi bazında gıda enflasyonu | 2020–2024, aylık | disk-ar.org, ücretsiz PDF |

**Analitik Çerçeve**

Temel korelasyon: Sağlıklı diyet maliyet priması artarken FIES/GYKA besin güvencesizliği artıyor mu?

```
r = korelasyon(Δ NRF/TL endeksi, Δ FIES prevalansı)
```

Zaman serisi: 2019–2024, yıllık. İstatistik: Pearson; güçlendirmek için Granger nedensellik testi.

**Histerez Testi:** 2024'te hem NRF/TL toparlanıyor mu hem FIES/GYKA düşüyor mu? Fiyat toparlanırken güvencesizlik göstergesi gecikmeli iyileşiyorsa → histerez kanıtı somutlaşır.

---

### Bileşen 3 — Mekanizmalar: Neden Histerez Oluşur?

**3a. UPF Substitüsyon Kalıcılığı**

Fiyat baskısı altında NOVA Grup 4 gıdalara geçiş gerçekleşir. Fiyat düşünce tüketici hemen sağlıklı gıdaya dönmez: tat habitüasyonu, alışveriş rutini, UPF pazarlamasının yapısal avantajı devam eder. Referans: Brezilya, Meksika, İngiltere UPF/gelir çalışmaları.

**3b. Adipoz Doku Biyolojisi — Biyolojik Bellek (Özgün Katkı)**

Uzun süreli besin yetersizliği ve UPF ağırlıklı beslenme adipoz dokuda kalıcı değişiklikler bırakır: adipokin profili bozulması (adiponektin ↓, leptin direnci ↑), kronik düşük dereceli inflamasyon, insülin direnci ve metabolik reprogramlama. Bu biyolojik iz fiyatlar normale döndüğünde otomatik geri dönmez. 2025–2030'da Türkiye'de obezite ve metabolik sendromda gecikmiş dalga beklenmeli. Klinisyenler şimdiden hasta beslenme geçmişini (hiperenflasyon dönemi) sorgulamalı.

**3c. Gelir Elastikiyeti Asimetrisi**

Sağlıklı gıda talebinin gelir elastikiyeti pozitif ve yüksek; işlenmiş gıdanınki daha düşük. Fiyatlar düşse bile reel ücretler gecikmeli toparlanır, tasarruf açığı ve borç yükü alt dilimlerde sağlıklı gıda harcamasını baskılar. DİSK-AR ve GYKA verileriyle gösterilebilir: alt %20'nin sağlıklı ürün harcama payı 2019 seviyesine döndü mü?

---

## Şekil ve Tablo Planı

**Şekil 1 — Besin Güvencesizliği & NRF/TL Korelasyonu (2019–2024)**
İki eksenli çizgi grafik. Sol: NRF/TL endeksi (2019=100). Sağ: FIES orta+şiddetli % (FAO). Görsel örtüşme + 2024 asimetrik toparlanma. Ana figür.

**Şekil 2 — Sağlıklı Sepet vs. UPF Sepeti NRF/TL Trendi ("Beslenme Makası")**
Çift çizgi: sağlıklı sepet NRF/TL vs. UPF sepeti NRF/TL, 2019–2024. Aradaki makas 2022'de maksimum, 2024'te daralıyor mu? Histerez testi.

**Şekil 3 — COICOP Diferansiyel Enflasyon**
Besin yoğun grup (et/balık/süt/sebze-meyve) vs. kalori yoğun grup (ekmek/tahıl/yağ/şeker) kümülatif enflasyon endeksleri, 2018=100. Protein-karbonhidrat makası.

**Şekil 4 — Gelir Dilimlerine Göre Gıda Harcama Payı (2018–2024)**
Beş gelir dilimi, yıllık çizgi grafik. HBSA verisi.

**Şekil 5 — Normatif Sepet Satın Alma Gücü**
"Asgari ücretle normatif TBR sepeti kaç günlük?" — 2019–2024 yıllık bar grafik.

**Tablo 1 — Referans Sepet NRF Profili ve Maliyet Karşılaştırması**
Her besin: NRF9.3 skoru, TL/100 kcal (2019, 2022, 2024), NRF/TL (2019, 2022, 2024). Sağlıklı vs. UPF sepeti karşılaştırması.

---

## Veri Toplama Sırası

**Hafta 1: İndirme**
1. EVDS → Fiyat İstatistikleri → Tüketici Fiyatları → Alt Gruplar → COICOP 01.1.x serileri, 2018 Ocak–2024 son ay, aylık, Excel
2. FAO FAOSTAT → Food Security → Suite of Food Security Indicators → Turkey → FIES moderate+severe, CSV
3. TÜİK GYKA bültenleri 2019–2023 → "gıdaya erişim güçlüğü" tablosu
4. DİSK-AR → disk-ar.org → yoksulluk sınırı raporları 2021–2024

**Hafta 2: TürKomp + NRF Hesabı**
1. turkomp.tarimorman.gov.tr → 40–50 besin için protein, lif, A/C/D vitamini, Ca, Fe, K, Mg, doymuş yağ, şeker, Na → Excel
2. NRF9.3 formülünü uygula
3. 2023 baz fiyatları + EVDS deflasyonu → 2019–2024 fiyat serisi
4. NRF/TL hesapla, grup ortalamalarını al

**Hafta 3: Analiz ve Figürler**
1. FIES vs. NRF/TL korelasyonu → Pearson r + figürler
2. COICOP enflasyon endeksleri → sağlıklı vs. UPF farkı
3. HBSA harcama payı → gelir dilimi trendi
4. Asgari ücret / normatif sepet maliyeti hesabı

**Hafta 4–5: Yazım**

---

## Makale Bölüm Yapısı

**Başlık (Uluslararası):**
Nutritional Hysteresis After Hyperinflation: Does Dietary Quality Recover When Prices Stabilize? Evidence from Turkey's Disinflation Period, 2024

**Başlık (Yerel / Türkçe):**
Gıda Hiperenflasyonu Sonrası Nutrisyonel Histerez: Sağlıklı Diyet Erişimi Dezenflasyonla Toparlanıyor mu? Türkiye 2019–2024 Verileri

**1. Giriş (400–500 kelime)**
Türkiye 2021–2023 gıda enflasyonu zirvesi → 2024 dezenflasyon → ekonomi literatürü fiyatı inceledi, beslenme kalitesi sorulmadı → nutrisyonel histerez hipotezi.

**2. Yöntem (600–700 kelime)**
NRF9.3 metodolojisi (Drewnowski referanslı) → referans sepet → fiyat serisi türetme → besin güvencesizliği kaynakları → korelasyon analizi → ekolojik tasarım kısıtları.

**3. Bulgular (500–600 kelime + 5 figür)**
NRF/TL endeksi 2019–2022 düşüşü → 2024 kısmi toparlanma → FIES korelasyonu → gelir dilimi asimetrisi → asgari ücret/sepet oranı.

**4. Mekanizmalar (600–700 kelime)**
UPF substitüsyon kalıcılığı → adipoz doku biyolojik belleği (özgün) → gelir elastikiyeti asimetrisi.

**5. Klinik ve Politik İmlikasyonlar (300–400 kelime)**
Dezenflasyon tek başına yeterli değil → aktif beslenme müdahalesi → klinisyen rolü → adipoz doku izleme.

**6. Kısıtlamalar (150 kelime)**
Ekolojik tasarım → vekil fiyat serisi → FIES lag → TBSA 2023–24 bekleniyor.

**7. Sonuç (150–200 kelime)**
Nutrisyonel histerez Türkiye için acil araştırma gündem. Dezenflasyon ekonomistlerin ilgisini çekerken, beslenme bilimcilerin hanelerin tabağına bakması gerekiyor.

---

## Hedef Dergiler

| Dergi | IF | Makale Tipi | Not |
|---|---|---|---|
| Public Health Nutrition | 4.2 | Orijinal araştırma | Birincil tercih — politika odaklı |
| European Journal of Clinical Nutrition | 4.5 | Orijinal araştırma | Diyet maliyet modeli iyi oturur |
| Nutrients (MDPI) | 5.9 | Orijinal araştırma | Açık erişim, hızlı süreç |
| Frontiers in Nutrition | 4.0 | Perspective/Original | Açık erişim |
| Beslenme ve Diyetetik Dergisi | yerel | Araştırma makalesi | Türkçe, yerel politika etkisi |

---

## Metodolojik Uyarılar

1. **Ekolojik tasarım:** Ulusal düzey korelasyonlar bireysel nedensellik iddia etmez; ecological fallacy tartışmada açıkça ele alınır.
2. **Fiyat serisi yöntemi:** Baz yıl market fiyatı + EVDS endeksleri = vekil yaklaşımı; doğrudan ürün fiyatı verisi olmayan dönemler için makul ama sınırlı.
3. **FIES veri gecikmesi:** FAO FIES verileri 1–2 yıl gecikmeli yayımlanabilir; 2024 verisi yoksa 2023 son veri olur — kısıtlamaya yaz.
4. **TÜİK metodoloji tartışması:** 2022–2023 TÜFE hesaplama yöntemine yönelik akademik eleştiriler bülten notunda belirtilmeli.
5. **TürKomp manuel derleme:** Toplu API yok; 40–50 besin için manuel giriş. Seçilen besinler şeffaf raporlanmalı.
6. **TBSA 2023–24:** Yeni ulusal beslenme araştırması yayımlandığında gerçek diyet verisiyle doğrulama önerilmeli.

---

## Önceki Sürümden Farklılıklar (v2 → v3)

v2 ekolojik analiz taslağıydı. v3'te:
- Merkezi çerçeve "nutrisyonel histerez" hipotezi oldu
- NRF9.3/TL endeksi eklendi (besin bileşimi düzeyinde analiz)
- Besin güvencesizliği bileşeni eklendi (FIES, GYKA, DİSK-AR)
- Üç mekanizma bölümü eklendi (UPF, adipoz, elastikiyet)
- Makale tipi: perspektif → orijinal araştırma
- Hedef dergi güncellemesi
