# Proje Fikri: Çok-Sınıflamalı, AI Destekli, Araştırmacı-Doğrulamalı UPF Takip Uygulaması

## 1. Özet

Kullanıcıların gün içi tükettikleri her şeyi (özellikle paketli besinleri) kaydettiği; paketli ürünleri AI ile **birden fazla işlenmişlik sınıflama sistemine göre paralel** sınıflandıran; araştırmacı ekibin fotoğraf üzerinden örneklem doğrulaması yaptığı; sonucunda boylamsal, bireysel düzeyde UPF tüketim verisi üreten bir mobil uygulama/araştırma altyapısı. Uzun vadede Sağlık Bakanlığı ve/veya Tarım ve Orman Bakanlığı ile veri/altyapı işbirliği hedefleniyor.

## 2. Mevcut Literatür ve Pazar Durumu

### 2.1 Ticari uygulamalar (doygun alan)
- **Processed, NOVAScanner, Is It Food, EXPOSR** gibi uygulamalar zaten fotoğraf/barkod ile tarama yapıp NOVA sistemine göre sınıflama sunuyor. "AI ile fotoğraftan NOVA sınıflaması" artık özgün bir konsept değil — bu haliyle sunulursa hakemlerden/değerlendiricilerden "zaten var" tepkisi alınır.
- Bu uygulamaların ortak zayıflığı: (a) tek sınıflama sistemi (neredeyse hepsi NOVA), (b) bilimsel doğrulama/validasyon şeffaflığı yok, (c) boylamsal araştırma çıktısı üretmiyorlar, tüketiciye yönelik ticari ürünler.

### 2.2 Akademik zemin
- 2025-2026 tarihli bir scoping review, AI destekli UPF değerlendirme araçlarını taramış; incelenen çalışmalarda F1 skorlarının 0.86-0.98 arasında değiştiğini, ancak gerçek-zamanlı/saha koşullarında validasyonun hâlâ eksik olduğunu bildirmiş. Bu, alanın "teknik olarak mümkün ama metodolojik olarak olgunlaşmamış" bir aşamada olduğunu gösteriyor.
- Görüntü tabanlı AI beslenme uygulamalarının akademik validasyonu için iyi emsaller var: **Keenoa** uygulaması CHILD Kohort Çalışması kapsamında ASA24 24-saatlik hatırlatma yöntemiyle çapraz geçişli (crossover) tasarımda karşılaştırılmış; yetişkinlerde 3 günlük besin günlüğüne karşı da ayrıca doğrulanmış. **Ghithaona** (Filistin) benzer bir görüntü tabanlı yaklaşımı üniversite öğrencilerinde 3-günlük besin kaydına karşı test etmiş. Bu iki çalışma, sizin uygulamanız için doğrudan kullanılabilecek bir validasyon şablonu sunuyor.

### 2.3 Çoklu sınıflama sistemi karşılaştırmaları — asıl boşluk burada
- Sistematik bir derleme NOVA, EPIC, IFPRI, UNC, UP3 ve Siga olmak üzere 6 farklı işlenmişlik/UPF sınıflama sistemi tespit etmiş; sistemler arasında işleme tekniklerinin tanımlanma düzeyi, katkı maddesi ele alınışı ve nicel besin kalitesi kriterleri açısından belirgin farklar var. Siga sistemi şeker/yağ/tuz için nicel eşik değerleri içeren tek sistem olarak öne çıkıyor.
- Karşılaştırmalı bir çalışma aynı veri setinde (küresel diyet) sistemler arası UPF payı tahminlerinin NOVA'da %10.2, UNC'de %15.2, IFPRI'de %16.7, IFIC'te %17.7, IARC'ta %47.4 gibi büyük farklılıklar gösterdiğini bulmuş. NHANES verisiyle yapılan başka bir karşılaştırmada NOVA diğer sistemlerle sadece %63.8-66.8 uyum göstermiş.
- **Kritik nokta:** Bu karşılaştırmaların tamamı kesitsel, popülasyon düzeyinde, var olan anket/FFQ verileri üzerinden yapılmış. Bireysel düzeyde, boylamsal, akıllı telefon tabanlı ve gerçek-zamanlı çoklu-sistem sınıflaması yapan bir çalışma/araç literatürde yok.

### 2.4 Türkiye bağlamı — kurumsal altyapı
- Sağlık Bakanlığı'nın hâlihazırda "Türkiye Beslenme Rehberi" adlı bir mobil uygulaması mevcut (bilinirlik/kullanım düşük olduğu bir çalışmada raporlanmış).
- Tarım ve Orman Bakanlığı'nın Türkomp besin bileşim veritabanı ve buna dayalı bir gıda karşılaştırma uygulaması bulunuyor; veritabanının genişletilmesi planlanıyor.
- Sonuç: Bakanlık işbirliği fikri sıfırdan bir teklif değil, **var olan altyapıya entegrasyon/tamamlayıcılık** pozisyonunda kurulabilir — bu hem daha inandırıcı hem de daha az bürokratik dirençle karşılaşabilecek bir çerçeve.

## 3. Özgünlük Değerlendirmesi

| Bileşen | Özgün mü? | Not |
|---|---|---|
| AI ile fotoğraf/barkoddan besin tanıma | Hayır | Ticari alan doymuş |
| Tek sistemle (NOVA) UPF sınıflama | Hayır | Çok sayıda ticari örnek var |
| **Çoklu sistemi paralel uygulayan, bireysel-boylamsal veri üreten bir araç** | **Evet** | Literatürde net boşluk |
| Araştırmacı doğrulamalı (human-in-the-loop) akademik-kalite veri seti | Kısmen | Var olan validasyon çalışmaları (Keenoa vb.) makro besin ögesi odaklı; işlenmişlik sınıflaması odaklı validasyon nadir |
| Paketli besine odaklanma (etiket/OCR tabanlı) | Kısmen özgün | Teknik olarak daha isabetli bir tercih; ticari uygulamalar genelde her besini (pişmiş yemek dahil) kapsamaya çalışıyor, bu da doğruluğu düşürüyor |
| Bakanlık ile boylamsal ulusal UPF izleme ortaklığı | Evet (Türkiye bağlamında) | Kurumsal altyapı var ama işbirliği süreci ayrı bir zorluk |

**Sonuç:** Projenin "teknoloji" kısmı özgün değil; "araştırma tasarımı" kısmı özgün. Başvuru/sunum bu şekilde çerçevelenmeli — "yeni bir uygulama yapıyoruz" değil, "sınıflama sistemleri arasındaki tutarsızlığı bireysel-boylamsal düzeyde ölçen bir araştırma altyapısı kuruyoruz, uygulama bunun aracı."

## 4. Alternatif Tasarım Yaklaşımları

### Alternatif A — Tam ölçekli boylamsal kohort (orijinal fikir)
Gönüllü havuzu, sürekli kayıt, AI çoklu sınıflama, örneklem doğrulaması, bakanlık ortaklığı.
- **Artı:** En yüksek bilimsel/etki potansiyeli, gerçek epidemiyolojik veri.
- **Eksi:** Yüksek maliyet, çok yıllı süreç, KVKK/etik kurul yükü, araştırmacı doğrulama iş yükü ölçeklenmez.

### Alternatif B — Metodolojik pilot çalışma (önerilen ilk adım)
Küçük bir gönüllü grubunda (n=50-150, örn. üniversite öğrencileri/klinik hasta popülasyonu), 2-4 haftalık kayıt, çoklu sistem sınıflaması + tam araştırmacı doğrulaması (küçük ölçek olduğu için mümkün). Amaç: sistemler arası uyumu bireysel/boylamsal düzeyde ilk kez göstermek.
- **Artı:** Hızlı, düşük maliyetli, yayınlanabilir, büyük projenin kanıt temelini oluşturur.
- **Eksi:** Ulusal temsiliyet yok, bakanlık ilgisini çekmek için tek başına yetersiz olabilir.

### Alternatif C — Sadece algoritma/metodoloji makalesi (uygulama olmadan)
Var olan açık veri setlerini (ör. Open Food Facts, Türkomp) kullanarak çoklu sınıflama sistemlerini otomatik olarak uygulayan bir algoritma geliştirip, ürün düzeyinde sistemler arası uyumu/tutarsızlığı raporlayan bir metodoloji makalesi.
- **Artı:** Çok düşük maliyet, hızlı yayın, mobil uygulama geliştirme riskini taşımaz.
- **Eksi:** Boylamsal/bireysel veri yok, "gerçek kullanıcı" bileşeni eksik, projenin en özgün kısmı olan bireysel düzey kayboluyor.

### Alternatif D — Mevcut bir uygulamaya "araştırma modülü" eklemek
Sıfırdan uygulama geliştirmek yerine, var olan bir açık kaynak/araştırma amaçlı uygulamaya (ör. Open Food Facts altyapısı) çoklu-sınıflama modülü eklemek.
- **Artı:** Geliştirme maliyeti ve zamanı büyük ölçüde azalır.
- **Eksi:** Kontrol ve özelleştirme kısıtlı, veri sahipliği/KVKK karmaşıklaşabilir.

**Öneri:** B ile başlayıp, sonuçlarına göre A'ya (bakanlık ortaklığıyla) veya C'ye (daha sınırlı akademik hedefle) evrilmek en gerçekçi yol.

## 5. Araştırma Soruları (derinlik)

1. Aynı bireyin gerçek zamanlı, boylamsal tüketim verisinde farklı UPF sınıflama sistemleri ne ölçüde uyuşuyor/uyuşmuyor?
2. Sistemler arası uyumsuzluk hangi ürün kategorilerinde en yüksek (ör. fonksiyonel/"sağlıklı" pazarlanan paketli ürünler mi, klasik atıştırmalıklar mı)?
3. AI'nin insan doğrulamasıyla uyumu (model güveni ile hata oranı ilişkisi) — aktif öğrenme döngüsü için hangi eşik değerleri kullanılmalı?
4. Bireysel UPF tüketim örüntüsü zaman içinde (mevsimsel, haftaiçi/haftasonu) nasıl değişiyor — sınıflama sistemine göre bu örüntü tespiti değişiyor mu?
5. (Bakanlık ortaklığı gerçekleşirse) Ulusal düzeyde hangi sınıflama sistemi politika hedefleri (ör. cephe etiketleme, vergi) için en uygun performans/pratiklik dengesini sunuyor?

## 6. Potansiyel Etki ve Çıktılar

- **Yayın potansiyeli:** Metodoloji makalesi (sistemler arası uyum, bireysel-boylamsal düzeyde — yüksek özgünlük); validasyon makalesi (AI-insan doğrulama uyumu); tanımlayıcı epidemiyoloji makalesi (kohort büyükse).
- **Fonlama potansiyeli:** TÜBİTAK 1001/3001, ya da COST Action ağları (CA24166/CA25129) üzerinden çok-ülkeli pilot/karşılaştırma — üye olduğunuz WG'lerle (WG1/WG3/WG4) doğal bir bağlantı kurulabilir.
- **Politika etkisi:** Türkiye'de cephe etiketleme veya UPF'e yönelik düzenleme tartışmaları gündeme gelirse, "hangi sınıflama sistemi kullanılmalı" sorusuna ampirik veri sunan nadir kaynaklardan biri olabilir.
- **Uzun vadeli ölçeklenebilirlik:** Pilot başarılı olursa, bakanlık ortaklığıyla ulusal UPF izleme sistemi öncüsü olabilir (bu, projenin en yüksek riskli ama en yüksek etkili senaryosu).

## 7. Riskler ve Pratik Engeller

- **Araştırmacı doğrulama iş yükü** ölçekle birlikte sürdürülemez hale gelir; çözüm: tabakalı örneklem doğrulaması + AI güven skoruna dayalı aktif öğrenme.
- **KVKK / etik kurul:** Beslenme verisi dolaylı olarak sağlık verisi sayılabilir, özel kategori veri işleme rejimine tabi olabilir; süreç baştan hukuki danışmanlıkla planlanmalı.
- **Kullanıcı bağlılığı (engagement):** Uzun süreli, sürekli kayıt gerektiren uygulamalarda düşüş oranı (attrition) yüksektir; gamification veya klinik popülasyon (ör. endokrinoloji kliniğindeki hastalar) üzerinden başlamak tutunmayı artırabilir.
- **Bakanlık işbirliği zaman ölçeği:** Yıllar sürebilir; projenin ana zaman çizelgesi buna bağımlı kılınmamalı, pilot veri kendi başına yayınlanabilir olmalı.
- **AI doğruluğu paketli üründe bile mükemmel değil:** Etiket OCR hataları, güncel olmayan ürün veritabanları, yeni/az bilinen markalar için düşük performans beklenmeli.

## 8. Önerilen Yol Haritası (özet)

1. **Faz 0 (0-3 ay):** Var olan sınıflama sistemlerinin (NOVA, Siga, UNC, IFPRI) kurallarını kodlanabilir algoritmalara dönüştürme; küçük bir ürün örnekleminde (ör. 200-300 paketli ürün) manuel çapraz test.
2. **Faz 1 (3-9 ay):** Pilot uygulama prototipi + küçük gönüllü grubunda (n=50-150) 2-4 haftalık boylamsal veri toplama, tam araştırmacı doğrulaması.
3. **Faz 2 (9-15 ay):** Pilot verinin analizi ve yayını; AI-insan uyum modelinin iyileştirilmesi.
4. **Faz 3 (15+ ay):** Sonuçlara göre ya bakanlık/kurumsal ortaklık girişimi ya da daha büyük çok-merkezli (COST Action ağı üzerinden) çalışmaya geçiş.

## Bağlantılı Notlar
- [[ev-yapimi-upf-kavrami]]
- [[UPF Sınıflandırmaların Dair Çalışma Fikirleri]]
- [[upf-siniflandirma-tutarsizligi-calisma-fikri]]
- [[upf-metabolit-tersten-ayristirma-calisma-fikri]]
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
