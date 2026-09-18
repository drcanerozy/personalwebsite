---
Konu:
  - Yapay Zeka
Tür:
  - deneysel
Durum: fikir
Öncelik: Yüksek
Oluşturulma_Tarihi: 2026-03-15
Modifiye_Edilme_Tarihi: 2026-03-15
TÜR:
ODAK:
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
---

Beslenme alanında AI kullanımını sınıflandıran bir "Nutrition Prompting Taxonomy" geliştirme çalışması. Çalışmalardaki promptları Persona, Context, Task, Constraints ve Output Format bileşenlerine göre analiz et.

# 📋 Nutrition Prompting Taxonomy (NPT) — Araştırma Yöntem Planı

> **Amaç:** Beslenme alanında AI kullanımını sistematik biçimde sınıflandıran, Persona / Context / Task / Constraints / Output Format bileşenlerine dayalı bir taksonomi geliştirmek.

Var olan çalışmaların bir prompt analizini yapmak.
---

## AŞAMA 1 — Hazırlık ve Kapsam Belirleme

### 1.1 Araştırma Sorusunu Netleştir

- [ ] Ana araştırma sorusunu yaz: _"Beslenme alanında AI'ya yöneltilen promptlar hangi bileşenlerden oluşuyor ve bu bileşenler arasındaki dağılım nasıl?"_
- [ ] İkincil soruları listele (kalite, güvenlik, alan bazlı farklılıklar vb.)
- [ ] Çalışmanın türüne karar ver: yalnızca metodolojik mi, yoksa karma yöntemli mi?

### 1.2 Kapsam Sınırlarını Belirle

- [ ] Hangi AI araçları dahil edilecek? (ChatGPT, Claude, Gemini, Copilot…)
- [ ] Hangi beslenme alt alanları kapsama alınacak?
    - [ ] Klinik beslenme / diyetetik
    - [ ] Spor beslenmesi
    - [ ] Halk sağlığı / toplum beslenmesi
    - [ ] Beslenme eğitimi
    - [ ] Araştırma amaçlı kullanım
- [ ] Dil kısıtı: sadece İngilizce mi, çok dilli mi?
- [ ] Tarih aralığı: hangi yıldan itibaren? (öneri: 2022–2025)

### 1.3 Ekip ve Roller

- [ ] Araştırmacı sayısına karar ver (inter-rater için en az 2 kişi şart)
- [ ] Rolleri ata: veri toplayıcı, kodlayıcı, istatistikçi
- [ ] Takvim oluştur (aşama bazlı Gantt şeması)

---

## AŞAMA 2 — Literatür Taraması

### 2.1 Veritabanı Araması

- [ ] PubMed'de arama yap → anahtar kelimeler: `"artificial intelligence" AND "nutrition" AND "prompt"`
- [ ] Google Scholar'da arama yap
- [ ] Scopus / Web of Science'da arama yap
- [ ] JMIR (Journal of Medical Internet Research) özel taraması
- [ ] Preprint sunucularını tara: medRxiv, bioRxiv

### 2.2 Dahil / Dışlama Kriterleri

- [ ] Dahil etme kriterlerini yaz (örn: AI araç kullanımı + beslenme içeriği + prompt içeren)
- [ ] Dışlama kriterlerini yaz (örn: yalnızca öneri sistemi algoritmaları, insan müdahalesi içermeyen)
- [ ] PRISMA akış diyagramı hazırla

### 2.3 Mevcut Prompt Çerçevelerini İncele

- [ ] PECOT, PICO, SPOR gibi mevcut prompt çerçevelerini karşılaştır
- [ ] Beslenme dışı sağlık alanlarındaki taksonomi çalışmalarını incele
- [ ] Boşluk analizi yap: NPT'nin özgün katkısını netleştir

---

## AŞAMA 3 — Veri Seti Oluşturma

### 3.1 Prompt Toplama Stratejisi

- [ ] **Kaynak 1 — Yayımlanmış çalışmalar:** Makalelerdeki örnek promptları ayıkla
- [ ] **Kaynak 2 — Anket:** Diyetisyen ve beslenme uzmanlarına yönelik anket tasarla
- [ ] **Kaynak 3 — Odak grup (isteğe bağlı):** 6–8 kişilik grupla sesli düşünme oturumu
- [ ] **Kaynak 4 — Senaryo bazlı üretim:** Kontrollü koşullarda standart senaryolar için prompt üret

### 3.2 Örneklem Yeterliliği

- [ ] Hedef prompt sayısını belirle (öneri: en az 150–200 benzersiz prompt)
- [ ] Alan bazında dengeli dağılım sağla (her alt alan için min. 30 prompt)
- [ ] Yinelenen / çok benzer promptları temizle

### 3.3 Etik Onay

- [ ] İnsan katılımcı içeriyorsa etik kurul başvurusu yap
- [ ] Gizlilik/anonimleştirme protokolü oluştur
- [ ] Anket onay formu hazırla

---

## AŞAMA 4 — Kodlama Şeması Geliştirme

### 4.1 Bileşen Tanımlarını Yaz

> Her bileşen için operasyonel tanım + pozitif örnek + negatif örnek hazırlanmalı.

- [ ] **PERSONA** tanımını yaz
    - [ ] Alt tipler: uzman, hasta, öğrenci, genel kullanıcı, anonim
    - [ ] Varlık/yokluk kodu + netlik puanı (1–3) tanımla
- [ ] **CONTEXT** tanımını yaz
    - [ ] Alt tipler: tıbbi durum, demografik bilgi, kültürel bağlam, ortam
    - [ ] Varlık/yokluk kodu + ayrıntı derinliği puanı (1–3) tanımla
- [ ] **TASK** tanımını yaz
    - [ ] Alt tipler: bilgi alma, hesaplama, planlama, yorumlama, içerik üretme
    - [ ] Görev karmaşıklık düzeyi puanı (1–3) tanımla
- [ ] **CONSTRAINTS** tanımını yaz
    - [ ] Alt tipler: allerji/intolerans, dini/kültürel, hastalık, bütçe, zaman, pişirme altyapısı
    - [ ] Varlık/yokluk kodu + kısıtlama sayısı tanımla
- [ ] **OUTPUT FORMAT** tanımını yaz
    - [ ] Alt tipler: tablo, liste, tarif, plan, metin açıklaması, görsel yönerge
    - [ ] Varlık/yokluk kodu + format özgüllük puanı (1–3) tanımla

### 4.2 Kodlama Kılavuzu

- [ ] Tüm tanımları tek belgede topla
- [ ] Her bileşen için 3'er örnek prompt ekle (iyi / orta / zayıf)
- [ ] Sınır vakaları (borderline) için karar ağacı hazırla
- [ ] Kılavuzu pilot kodlama öncesi gözden geçir

---

## AŞAMA 5 — Pilot Kodlama ve Güvenirlik Testi

### 5.1 Pilot Çalışma

- [ ] Toplam veri setinin %10'unu pilot için ayır (~20 prompt)
- [ ] Her kodlayıcı bağımsız olarak kodlasın
- [ ] Sonuçları karşılaştır, uyuşmazlıkları belgele

### 5.2 Güvenirlik Analizi

- [ ] **Cohen's Kappa** hesapla (kategorik değişkenler için)
- [ ] **ICC (Intraclass Correlation Coefficient)** hesapla (puanlama için)
- [ ] Hedef: κ ≥ 0.80 (yüksek uyum)
- [ ] κ < 0.80 ise → kılavuzu revize et → yeni pilot

### 5.3 Kılavuz Revizyonu

- [ ] Uyuşmazlık yaratan maddeleri yeniden tanımla
- [ ] Gerekirse bileşen alt tiplerini birleştir veya böl
- [ ] Revize kılavuzu belgele (versiyon numarası ver)

---

## AŞAMA 6 — Ana Kodlama

- [ ] Tüm prompt veri setini kodla (her kodlayıcı bağımsız)
- [ ] Çift kodlamada uyuşmazlık varsa üçüncü hakem kullan
- [ ] Veriyi Excel/SPSS/R formatına aktar
- [ ] Kodlama tamamlandığında ham veriyi yedekle

---

## AŞAMA 7 — Veri Analizi

### 7.1 Tanımlayıcı İstatistikler

- [ ] Her bileşenin varlık oranını hesapla (%)
- [ ] Alan bazında bileşen dağılımını hesapla
- [ ] En yaygın task tipini, en sık eksik bileşeni belirle

### 7.2 İleri Analizler

- [ ] Bileşen kombinasyonları: hangi bileşenler birlikte görülüyor? (ko-okürrans analizi)
- [ ] Kalite skoru: 5 bileşenin varlığına göre prompt kalite indeksi oluştur (0–10)
- [ ] Alan × bileşen çapraz tablosu (chi-square testi)
- [ ] Güvenlik analizi: klinik sınır aşımı olan promptların oranı

### 7.3 Görselleştirme

- [ ] Bileşen dağılım grafiği
- [ ] Alan bazında ısı haritası (heatmap)
- [ ] Prompt kalite skoru dağılım histogramı

---

## AŞAMA 8 — Taksonomi Çerçevesini Finalize Et

- [ ] NPT şemasını ver: her bileşen + alt tipler + kodlar
- [ ] Örnek "iyi yapılandırılmış prompt" şablonu oluştur
- [ ] Örnek "kötü yapılandırılmış prompt" + düzeltilmiş versiyonu ekle
- [ ] Taksonominin pratikte nasıl kullanılacağına dair rehber yaz

---

## AŞAMA 9 — Yazım ve Yayın

### 9.1 Makale Yapısı

- [ ] Abstract yaz (yapılandırılmış: amaç, yöntem, bulgular, sonuç)
- [ ] Giriş: kapsam, boşluk, NPT'nin özgünlüğü
- [ ] Yöntem: kodlama şeması, güvenirlik
- [ ] Bulgular: tanımlayıcı istatistikler + tablolar
- [ ] Tartışma: klinik önemi, sınırlılıklar
- [ ] Sonuç + pratik öneriler

### 9.2 Hedef Dergiler

- [ ] Journal of the Academy of Nutrition and Dietetics
- [ ] Nutrients (MDPI)
- [ ] JMIR mHealth and uHealth
- [ ] Clinical Nutrition
- [ ] Hedef dergi seç ve yazar kılavuzunu incele

### 9.3 Sunum ve Paylaşım

- [ ] Kodlama kılavuzunu ek dosya olarak hazırla (supplementary)
- [ ] Anonim veri setini açık erişimde paylaş (Zenodo / OSF)
- [ ] Konferans özeti hazırla (FENS, ESPEN veya IUNS)

---

## ⚠️ Dikkat Edilmesi Gereken Kritik Noktalar

### Güvenlik ve Etik

- [ ] Klinik sınır aşımı olan promptları (tıbbi tanı, ilaç dozu önericisi gibi) ayrı kategoriye al
- [ ] Araştırma bulgularını "AI klinik karar destek sistemi yerine geçemez" uyarısıyla dengele
- [ ] Hasta verisi içeren promptlarda anonimleştirme kontrolü yap

### Metodolojik Güçlükler

- [ ] Aynı metnin birden fazla bileşen içerebileceğini kodlama kılavuzuna ekle
- [ ] Örtük (implicit) bileşenler için karar kuralı yaz (örn: persona yazılmamış ama bağlamdan çıkarılabiliyorsa?)
- [ ] Çok aşamalı (multi-turn) konuşmaları nasıl kodlayacağını belirle

### Geçerlilik (Validity)

- [ ] İçerik geçerliliği: kodlama kılavuzu için uzman panel görüşü al (en az 3 uzman)
- [ ] Yapı geçerliliği: NPT puanı ile bağımsız kalite ölçütü arasında korelasyona bak
- [ ] Farklı AI sistemlerinde aynı promptun farklı yanıtlar üretip üretmediğini not et

### Sınırlılıklar (Önceden Belgele)

- [ ] Veri setinin temsil gücü (hangi kullanıcı profillerinden derlendiği)
- [ ] Zaman bağımlılığı: AI sistemlerinin hızlı değişmesi nedeniyle bulgular eskiyebilir
- [ ] Gözlemci etkisi: anket ile toplanan promptlar gerçek kullanımı tam yansıtmayabilir

---

## 📎 Kaynaklar ve Referanslar

- [ ] Temel taksonomi referanslarını ekle
- [ ] PRISMA 2020 kılavuzunu kaydet
- [ ] İlgili prompt mühendisliği makalelerini ekle
- [ ] Beslenme-AI alanındaki derleme makaleleri listele

---

## 📝 Notlar

> Bu alana serbest notlarını ekleyebilirsin.

---

_Son güncelleme: —_