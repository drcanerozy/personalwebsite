---
tags: [çalışma-fikri, precision-nutrition, food-sensitivity, FODMAP, DII, n-of-1]
durum: taslak / orijinallik-fizibilite değerlendirmesi
tarih: 2026-07-17
---

# Diyetsel Duyarlılık / Alerjenik Yük Modellemesi — 3 Aşamalı Araştırma Programı

## Ana Fikir

Besin duyarlılıkları ve alerjilerinin deneme-yanılma ile tespiti zahmetli ve düşük verimli. Amaç: bireyin dışlaması gereken en olası 3-5 besni öncelik sırasına koyan, hem **kompozisyon-bazlı (a priori)** hem **kişiye özel (a posteriori)** bir model geliştirmek. Gluteni doğrudan hedefleyen konvansiyonel yaklaşımın yerine, besin bazında olasılıksal bir öncelik listesi sunmak.

---

## Çalışma A — Literatür-Türetilmiş Diyetsel Duyarlılık Yükü İndeksi

**Şablon:** Dietary Inflammatory Index (Shivappa et al., 2014) metodolojisi.

- **Parametre seti (aday):** FODMAP alt tipleri (fruktan, GOS, laktoz, fazla fruktoz, polyoller), gluten, histamin, biyojenik aminler, salisilat, lektin, kapsaisin, sülfit.
- **Puanlama:** Her makale, ilgili parametrenin semptom şiddeti/insidansını artırıp azaltmadığına göre +1 / −1 / 0 olarak kodlanır → parametre-özel "overall score" elde edilir.
- **Standardizasyon:** Ham tüketim birimlerinin (mg, g) keyfiliğinden kaçınmak için z-skoru → merkezi yüzdelik dilim dönüşümü (DII'nin izlediği yol). Aşırı değer çarpıklığı için "scaling formula / SFOD" tipi düzeltme entegre edilebilir — bu metodolojik özgünlük katar.
- **Çıktı:** Bağımsız, tek başına yayınlanabilir bir metodoloji makalesi (TR Dizin veya orta-üst düzey dergi). DII gibi, sonraki tüm uygulama çalışmalarının (B ve C) omurgası olur.
- **Veri kaynakları:**
  - Monash / İsveç genişletilmiş FODMAP veritabanı (1060 besin kalemi, 1805 FODMAP değeri)
  - Kanada / Avusturya glutensiz ürün kompozisyon veritabanları
  - USDA / EuroFIR besin kompozisyon tabloları

**Fizibilite:** Yüksek. Kendi 3 adımlı doğrulama iş akışına (doğruluk kontrolü → bölüm bazlı yazım → metodolojik künye) doğrudan uyarlanabilir. Hızlı ilerletilebilir.

---

## Çalışma B — Kişiye Özel n-of-1 / Bayesian Duyarlılık Modeli

- Çalışma A'daki indeks **popülasyon-seviye prior** olarak kullanılır.
- Bireyin gerçek zamanlı besin+semptom günlüğü (FAST diary tipi enstrüman) ile **gecikmeli (lagged) regresyon** — LASSO/elastic net, çoklu korelasyonlu besin değişkenleri nedeniyle düzenlileştirme şart.
- Az gözlemli n-of-1 verisi için **Bayesian hiyerarşik model** özellikle uygun: popülasyon prior + bireysel posterior güncelleme. Metodolojik paralel: PREDICT (Zoe/Spector) — postprandiyal glisemik yanıt için kompozisyon + bireysel veriden kişiye özel tahmin üretimi.
- Alternatif/tamamlayıcı: önce besinleri A'daki skora göre kümele (yüksek FODMAP+gluten, yüksek histamin, yüksek salisilat vb.), sonra bireyin günlüğünü bu kümelere karşı test et → daha az veri gerektiren, mekanizma-temelli hibrit yaklaşım.

### Veri seti uygunluğu — kritik değerlendirme

**Mevcut haliyle uygun değil.** Üç sorun:
1. **FAST diary** — metodolojik olarak doğru örnek, ama halka açık ham veri yok; n=51 küçük validasyon kohortu.
2. **MyFitnessPal açık veri setleri** — milyonlarca kayıt var, ama semptom etiketi hiç yok.
3. **mySymptoms** (900K+ kullanıcı) — en zengin ham veri, ama kapalı/ticari, akademik erişim yok.

**Sonuç:** Besin-seviyesi + semptom-seviyesi + bireysel-seviyede eşleşen açık büyük veri seti mevcut değil. Bu, Çalışma B'yi ikincil veri analizinden **prospektif birincil veri toplama projesine** dönüştürüyor — orijinallik açısından güçlü, BAP başvurusu için uygun.

**Fizibilite:** Orta — pilot kohort + kendi veri toplama aracı gerektirir. Küçük n, tekrar ölçümlü tasarım.

---

## Çalışma C — Klinik Karar Destek Aracı (Prototip)

- A + B'nin çıktısını birleştiren, vaka bazlı öncelikli eleme sırası öneren bir arayüz/araç.
- "Augmented Dietitian" çerçevesine doğrudan oturuyor — AI-entegre pedagoji/klinik pratik hattıyla örtüşüyor.

**Fizibilite:** A ve B tamamlandıktan sonra anlamlı; şu an erken.

---

## Sıralama / Bağımlılık Zinciri

```
A (indeks, hızlı, bağımsız yayın)
   ↓ (prior olarak besler)
B (n-of-1/Bayesian model, BAP-uygun, birincil veri gerekli)
   ↓
C (klinik karar destek prototipi)
```

## Sonraki Somut Adım

Çalışma A için literatür tarama protokolü kurulması: dahil etme/dışlama kriterleri, taranacak veritabanları, hedef parametre listesinin netleştirilmesi.

## Dikkat Edilmesi Gerekenler

- **Confounding:** Aynı öğünde birden fazla şüpheli bileşen birlikte tüketiliyor (ör. domates soslu makarna = gluten + FODMAP + histamin). Association rule mining / çoklu doğrusal regresyon tek başına yetersiz kalabilir — challenge-tabanlı (körlemeli yeniden maruziyet) doğrulama gerekebilir.
- **Semptom raporlaması:** Sübjektif, gecikmeli, recall bias riski yüksek.
- **IgG-bazlı ticari testlerden ayrışma:** Zayıf kanıt tabanına sahip bu testlerin aksine, modelin kompozisyon+davranışsal veriye dayanması bilimsel ve yayın açısından avantaj.

## Bağlantılı Notlar
- [[cok-siniflamali-upf-takip-uygulamasi]]
- [[nova-grup4-nutrient-adjustment-calisma-plani]]
- [[ev-yapimi-upf-kavrami]]
- [[UPF Sınıflandırmaların Dair Çalışma Fikirleri]]
- [[upf-metabolit-tersten-ayristirma-calisma-fikri]]
