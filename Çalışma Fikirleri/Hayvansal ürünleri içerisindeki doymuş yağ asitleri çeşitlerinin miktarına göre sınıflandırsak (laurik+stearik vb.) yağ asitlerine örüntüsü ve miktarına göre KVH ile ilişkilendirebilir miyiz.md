---
Konu:
  - Diyet Kalitesi
Tür:
  - meta-analiz / derleme
Durum: planlama
Öncelik: Normal
Oluşturulma_Tarihi: 2026-03-14
Modifiye_Edilme_Tarihi: 2026-03-14
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
Buradan bir şey çıkacak gibi:

_"Fatty Acid Profile Clustering of Animal-Source Foods: A Food Composition Database Analysis with Matrix Context"_

### Temel Mantık

```
USDA verisi → hayvansal besinleri filtrele
→ yağ asidi profili vektörü oluştur (C12, C14, C16, C18:0, C18:1, vb.)
→ kümeleme analizi (hierarchical + k-means)
→ "beklenmedik komşular" ve "beklenmedik ayrışmalar" tespit et
→ ikinci değişkenle bağlamsal yorum katmanı ekle
→ KVH literatürüyle teorik tartışma
```

## SOMUT ANALİZ ADIMLARI

**1. Veri çekimi** USDA API veya bulk download → hayvansal besin filtresi (et, süt ürünleri, yumurta, deniz ürünleri) → eksik yağ asidi verisi olan besinleri çıkar → temiz matris.
EUROFIRden falan da veri çekilebilirse çok iyi olur.

**2. Yağ asidi profili vektörü** Her besin için: toplam SFA içindeki C12, C14, C16, C18:0 oranları + tekli doymamış (C18:1) ve çoklu doymamış yağ oranları. Ham gram değil, **oran vektörü** kullanmak besinleri karşılaştırılabilir kılar.

**3. Kümeleme** Hierarchical clustering (Ward metodu) → dendrogram → kaç küme anlamlı? Ardından k-means ile doğrulama. R'da `factoextra`, Python'da `scipy` + `sklearn` yeterli.

**4. Küme yorumu** Her kümenin yağ asidi "imzası" nedir? Hangi besinler beklenmedik biçimde aynı kümede? (örn. dana karaciğeri ile koyun sütü aynı kümede mi?) Bunlar makalenin en ilgi çekici kısmı olur. Farklı k değerleri ve mesafe ölçütleri için duyarlılık analizi yapın ve raporlamak gerek. Tek bir kümeleme sonucunu gerçekmiş gibi sunulmamalı.

**5. İkinci değişken katmanı** Kümelere ikinci değişkeni (makro oran veya kolesterol) renk/boyut olarak ekle → scatter/bubble plot → "aynı yağ asidi kümesinde matrix farklılığı ne kadar büyük?" sorusunu görselleştir.

**6. KVH literatürü bağlantısı** Kümeleri mevcut epidemiyolojik bulgularla karşılaştır — "yüksek riskli" olarak etiketlenen besinler gerçekten ayrı bir kümede mi, yoksa literatürdeki kategorizasyon veri tarafından desteklenmiyor mu?



## Bağlantılı Notlar
- [[Metabolik esnekliği AD türüne göre inceleyebilir miyiz belirleyen nedir bunu yağ yüzdesiyle ilişkili olarak]]
- [[Kalori Kısıtlaması, Kilo Kaybı Olmasa da İnsülin Direncini Kısa Sürede İyileştiriyor, Ancak Doku Bazında Etkileri Farklı.]]
- [[Adipoz Doku]]
- [[MASLD'de Diyet Müdahalelerinin Beslenme Geometri Bağlamında Etkinliğinin İncelenmesi]]
- [[Tirzepatide, Kilo ve Yağ Kaybı Sağlasa da Adipoz Doku Disfonksiyonelliğini Düzeltmiyor]]
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
