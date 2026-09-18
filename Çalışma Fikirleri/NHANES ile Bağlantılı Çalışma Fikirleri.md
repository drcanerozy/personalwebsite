---
Tür:
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

Tüm Çalışma Fikirleri klasörü taranarak NHANES'i (veya "Biobank/NHANES" ikilisini) veri kaynağı olarak öneren notlar aşağıda toplandı. Amaç: tek bir düzgün NHANES veri ayıklama/hazırlama işiyle birkaç çalışmanın temelini aynı anda atmak.

## Notlar

- [[Biobank veya NHANESte, farklı diyet türlerine sahip (başlangıçta ve devamında) kişilerin, veya farklı diyetleri takip edenlerin tüm süreçte kalori alımları nasıl değişmiş]]
  Farklı diyet türlerini takip eden bireylerin zaman içinde kalori alımlarının nasıl değiştiğini NHANES/Biobank'ta izleme fikri. Kilo kaybı/geri kazanımının kaloriden bağımsız olduğu bir durum var mı sorusu.

- [[Beslenme Geometrisi Temelli Çalışmşa Fikirleri]]
  En kapsamlı NHANES planı — Makale 2 (ampirik, NHANES tabanlı): CIM (karbonhidrat-insülin modeli) ve PLH (protein leverage hipotezi) öngörülerini aynı response-surface modelinde test etmek. 24 saatlik hatırlatma + FNDDS makro/mikro alt tipleri + HOMA-IR + DXA + bel çevresini birleştiriyor. Ek alt-analiz (B): NHANES III + mortalite bağlantı dosyalarıyla protein:enerji oranının yaşla nasıl kaydığını inceleyen bir uzantı da var.

- [[GLP-1 Nutrient Density ve Vücut Kompozisyonu]]
  Alternatif 1 olarak NHANES pooled kesitsel analiz planı: `RXQ_RX` (ilaç verisi) + `DR1TOT`/`DR2TOT` (24-saat besin hatırlatma, NRF9.3 hesaplama) + `BMX` (antropometri) birleştirilerek GLP-1RA kullanıcılarında nutrient density-vücut kompozisyonu ilişkisi. Notta önemli bir kısıt zaten işaretlenmiş: 2021-2023 cycle'ında detaylı ilaç ismi/kullanım süresi toplanmadığı için güncel (obezite-only, Wegovy sonrası) kullanıcı profili bu veride neredeyse yok — 2013-2020 cycle'ları T2DM ağırlıklı eski GLP-1RA kullanıcılarını yakalıyor.

- [[UPF Sınıflandırmaların Dair Çalışma Fikirleri]]
  Üç ayrı NHANES fikri aynı notta: (1) NOVA/NOURISH/Food Compass sınıflarını kodlayıp hangi gıdaların sistemler arasında ayrıştığını haritalama, (2) UPF'nin bir kısmını izokalorik olarak sebze/tam tahılla değiştirip HEI ve kardiyometabolik belirteçler üzerindeki teorik etkiyi hesaplama (substitution modeling), (3) UPF enerji yüzdesi ile diyet kalitesi arasındaki "güvenli eşik" kırılma noktasını spline analiziyle bulma. NotebookLM'in A/C fikirleri de (zenginleştirilmiş gıdaları çıkarınca mikrobesin riski) aynı NHANES altyapısını kullanıyor.

## Ortak Altyapı Notu

Yukarıdaki fikirlerin çoğu aynı temel NHANES bileşenlerini paylaşıyor:
- **Diyet verisi:** `DR1TOT`/`DR2TOT` (24 saatlik hatırlatma) + FNDDS besin kodları
- **Antropometri:** `BMX` (kilo, boy, bel çevresi) — her cycle'da tam
- **İlaç kullanımı:** `RXQ_RX` (jenerik isimle GLP-1RA filtrelenebilir, ama sadece 2013–Mart 2020 cycle'larında detaylı; 2021-2023'te kaba soru var, filtrelenemez)
- **Vücut kompozisyonu (DXA):** sadece 2017–Mart 2020 cycle'ına kadar mevcut, sonrasında yok
- **Kan biyobelirteçleri:** HOMA-IR, lipid paneli — belirli cycle'larda mevcut

Tek bir "NHANES temiz veri seti" (belirli cycle aralığı + diyet + antropometri + gerekirse ilaç/DXA birleştirilmiş) hazırlanırsa, hem UPF ikame/eşik analizi (Fikir 2+3), hem beslenme geometrisi Makale 2, hem de GLP-1/nutrient density analizi aynı temel üzerine inşa edilebilir — cycle seçimi bu üç kullanım arasında bir denge noktası gerektiriyor (DXA gerekiyorsa 2017-Mart 2020'ye sıkışılır, GLP-1 filtrelemesi gerekiyorsa 2020'den sonrasına geçilemez).

## Sonraki Adım

- [ ] Hangi çalışmanın önceliklendirileceğine karar ver (bkz. UPF Sınıflandırmaların Dair Çalışma Fikirleri içindeki öncelik sıralaması — Fikir 2+3 en hazır durumda)
- [ ] Seçilen cycle aralığı için değişken kapsam tablosunu çıkar (Beslenme Geometrisi notunda zaten "sıradaki somut adım" olarak işaretli)
- [ ] Tek bir R/Python pipeline'ı kur, birden fazla çalışma bu pipeline'dan beslenecek şekilde tasarla

## Bağlantılı Notlar
- [[GLP-1 Nutrient Density ve Vücut Kompozisyonu]]
- [[UPF Sınıflandırmaların Dair Çalışma Fikirleri]]
- [[Beslenme Geometrisi Temelli Çalışmşa Fikirleri]]
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
- [[GLP-1 Kullanan Hastalarda Nutrient Density Density Yaklaşımlı RCT]]
