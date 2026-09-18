# Çalışma Fikri: UPF Metabolit İmzasının Tersten Ayrıştırılması — İşleme mi, Besin Kategorisi mi?

## 1. Arka Plan / Problem Tanımı

MTBLS12705 (IDATA çalışması, Abar ve ark. 2025, *PLoS Medicine*) UPF tüketimini öngören poli-metabolit skorları geliştirdi: 28 serum + 33 idrar metaboliti, LASSO regresyonla seçilmiş. Ancak MetaboLights'ta depolanan veri sadece iki kaba kategori içeriyor — **"food (unprocessed)"** vs **"processed food"** (araştırmacıların kendi çapraz-geçişli deneyindeki %0/%80 UPF fazları). Tek tek yenen besinlerin listesi veya bunların NOVA/başka bir sistemle etiketlenmiş hali **MetaboLights'ta yok**. IDATA kohortunun (n=718) 24-saatlik diyet hatırlatma (ASA-24) verisi ayrı bir sistemde (CDAS, NCI) ve Data Transfer Agreement gerektiriyor.

Bu, ilk bakışta bir sınırlama gibi görünüyor ama aslında **fırsatı netleştiriyor**: elimizde zaten besin listesi olmadığı için "önce besinleri yeniden sınıflandır, sonra metabolitlerle ilişkilendir" yaklaşımı mümkün değil. Bunun yerine **tersten** gitmek gerekiyor: metabolitlerden başlayıp, hangi metabolitin gerçekte neyi ölçtüğünü sorgulamak.

## 2. Boşluk (Gap)

Orijinal makale (Abar ve ark. 2025), 28+33 metaboliti **tek bir bileşik UPF skoru** olarak sunuyor — hepsi aynı doğrusal modelin parçası. Ancak bu metabolitlerin biyolojik kökeni son derece heterojen:
- **Isıl-işlem/AGE kaynaklı** (ör. N6-karboksimetillizin) — gerçekten "işlemeyi" ölçüyor
- **Ambalaj/kontakt-materyal kaynaklı** (ör. levoglukozan) — işlemeyi değil, *ambalajı* ölçüyor
- **Besin-öğesi-eksikliği kaynaklı** (ör. beta-kriptoksantin, lahanagil biyobelirteci) — işlemeyi değil, basitçe "az sebze/meyve yemeyi" ölçüyor

Makale bu üç kategoriyi ayrıştırmıyor; hepsini tek bir "UPF skoru" içinde eritiyor. **Kimse şu soruyu sormamış:** Bu skorun öngörü gücünün ne kadarı gerçek işleme-kaynaklı kimyasal değişimden (birinci grup), ne kadarı sadece besin çeşitliliği/kalitesi eksikliğinden (üçüncü grup) geliyor? Bu, UPF literatüründeki en temel eleştiriyle ("UPF etkisi aslında besin kalitesi eksikliğinin bir vekili mi?") doğrudan test edilebilir bir bağlantı kuruyor.

## 3. Önerilen Yaklaşım — Paralel İki Kol

### Kol A — Bağımsız Reanaliz (hemen başlanabilir, işbirliğine bağlı değil)
1. Makalenin S6 Tablosundaki (veya MetaboLights'taki tam metabolit listesi) 28+33 metaboliti tek tek biyolojik kaynağına göre 3 kategoriye ayır: (i) ısıl-işlem/neoformed kontaminant, (ii) ambalaj/ksenobiyotik, (iii) besin-öğesi/mikro-besin eksikliği belirteci.
2. Her alt-küme için ayrı ayrı, orijinal LASSO ağırlıklarını kullanarak **alt-skor** hesapla (kod ve ham veri MetaboLights'ta açık, CC0).
3. Bu üç alt-skorun, orijinal çapraz-geçişli deneydeki %0 vs %80 UPF fazlarını ayırt etme gücünü (AUC, within-individual ayrışma) ayrı ayrı karşılaştır.
4. **Beklenen katkı:** Eğer "besin-öğesi-eksikliği" alt-kümesi tek başına ayrışmanın büyük kısmını açıklıyorsa, bu "UPF etkisi = besin kalitesi eksikliği" tezine güçlü bir kanıt olur. Eğer ısıl-işlem/ambalaj alt-kümesi bağımsız ve ek bir ayrışma sağlıyorsa, bu "işlemenin kendisi, kompozisyondan bağımsız bir etki bırakıyor" tezini destekler — [[nova-grup4-nutrient-adjustment-calisma-plani]] ile doğrudan örtüşür.
5. Bu kol, food-level veri olmadan, sadece MetaboLights'taki açık veriyle yapılabilir — hızlı bir "letter/short communication" veya metodolojik not olarak yayınlanabilir düzeyde.

### Kol B — Yazarlarla İşbirliği Teklifi (paralel, daha yavaş, daha güçlü)
1. Erikka Loftfield (NCI, ilgili yazar) ile kısa, somut bir e-posta: poli-metabolit skorlama modelini **çoklu-sınıflama-sistemi** (NOVA/Siga-proxy/IARC) ve **tersten-korelasyon** yaklaşımıyla genişletmek istediğinizi belirt.
2. Veri zaten CC0 lisanslı — izin istemene gerek yok; teklifin amacı **CDAS'taki food-level ASA-24 verisine ortak erişim/işbirliği**, tek taraflı izin talebi değil.
3. Gerçekçi beklenti: NCI/büyük-grup yazışma yoğunluğu nedeniyle hızlı yanıt garantisi yok, ama açık-veri kültürü güçlü bir grup olduğu için tamamen kapalı kapı da beklenmiyor. Yanıt gelirse, food-level veriyle Kol A'daki analiz çok daha güçlü hale gelir (gerçek NOVA kodlaması + metabolit alt-kümeleri çapraz tablosu mümkün olur).
4. Ortak yazarlık isteği makul bir karşılık olabilir — bu, analizin özgünlüğünü bozmaz, senin analitik sorunun (hangi metabolit alt-kümesi neyi ölçüyor) zaten kendi fikrin.

**Öneri:** İkisini paralel yürüt. Kol A'yı hemen başlat (bağımsız, hızlı, elinde kalır); Kol B'nin e-postasını aynı hafta gönder. Yanıt gelene kadar Kol A'daki bulgularla bir ön-taslak/poster hazırlanabilir; yanıt gelirse tam makaleye genişletilir.

## 4. Bağlantılı Projeler
- [[off-upf-cross-classification]] — bu fikir, çapraz-sınıflandırma projesinin ampirik doğrulama ayağı olabilir
- [[nova-grup4-nutrient-adjustment-calisma-plani]] — "kompozisyondan bağımsız işleme etkisi" tezine doğrudan test
- [[upf-taste-sensitivity-bap]] — ileride food-level veri elde edilirse, tat duyarlılığı bağlamına genişletilebilir

## 5. Sonraki Adımlar
1. MTBLS12705'in tam metabolit listesini (S6 Table, orijinal makale ekinden) çek ve 3 kategoriye ön-kodlama yap.
2. Erikka Loftfield'a işbirliği e-postası taslağı hazırla (istersen taslağı birlikte yazalım).
3. Kol A'nın istatistiksel planını (hangi alt-skor, hangi karşılaştırma, hangi yazılım/paket) netleştir.

## Bağlantılı Notlar
- [[UPF Sınıflandırmaların Dair Çalışma Fikirleri]]
- [[UPF Tüketimi Metabolitlerle Belirlenebilir Mi?]]
- [[ev-yapimi-upf-kavrami]]
- [[cok-siniflamali-upf-takip-uygulamasi]]
- [[nova-grup4-nutrient-adjustment-calisma-plani]]
