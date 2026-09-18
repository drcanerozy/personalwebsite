---
Tür:
  - Besleyici
ODAK:
  - "[[Aralıklı Açlık]]"
MEKANİZMA: "[[Cinsiyet Farklılıkları]]"
DİZİN: "[[İştahın Düzenlenmesi]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Aralıklı Açlığın Longevity Etkisi Cinsiyete ve Genetiğe Göre Farklılık Gösteriyor]]"
  - "[[Aralıklı Açlıktaki Kilo Kaybı İnsülin Düzeylerinden Etkileniyor]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: " 10.3389/fnut.2026.1735869"
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Kişiselleştirilmiş Açlık]]"
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
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
**Çalışmanın Amacı ve Hipotezleri** İnsanlarda kilo kaybı için oldukça popüler olan 5:2 aralıklı açlık diyetinin (haftada ardışık olmayan 2 gün tam veya kısmi açlık, 5 gün serbest beslenme) mekanizmaları ve geniş fizyolojik etkileri literatürde çok az bilinmektedir. Bu çalışmanın temel amacı; obez olmayan bireylerde 5:2 diyetinin vücut ağırlığı, iskelet büyümesi, yağ depoları ve metabolizma üzerindeki etkilerini hücresel boyutta haritalandırmaktır. Araştırmacılar, bu diyetin yarattığı açlık-tokluk döngülerinin "açlık hormonu" olarak bilinen ghrelin salgısını artıracağını ve bu hormonun kendi reseptörü olan **GHSR (Büyüme Hormonu Salgılatıcı Reseptör)** üzerinden metabolik etkileri (büyüme ve yağ depolanması) yöneteceğini hipotez etmişlerdir.

**Çalışma Kısaca Nasıl Yapıldı?** Çalışma, vahşi tip (WT) ve genetik olarak ghrelin reseptörü silinmiş (GHSR-null) fareler kullanılarak yapılmıştır. Büyüme çağının zirvesindeki ergen (7 haftalık) ve büyümesi durmuş yetişkin (7 aylık) fareler, cinsiyetlerine göre ayrılarak iki gruba bölünmüştür:

1. **Kontrol Grubu:** Sınırsız (Ad libitum - AL) beslenen grup.
2. **5:2 Diyet Grubu:** Pazartesi ve Perşembe günleri 24 saat boyunca yemleri tamamen alınan, diğer 5 gün serbest beslenen grup. 3 ila 6 haftalık takiplerin ardından farelerin kemik büyüme hızları (epifiz plağı), kemik iliği yağlanması, beyaz ve kahverengi yağ dokusu (BAT ve WAT) ağırlıkları, hücresel yağ depolama kapasiteleri (GC-FID analizi ile) ve kandaki serbest yağ asitleri (FFA) detaylıca ölçülmüştür.

**Primer Bulgular (Kilo Kaybı ve Beslenme Davranışı)**

- **Cinsiyete Özgü Kilo Kaybı:** 5:2 diyeti erkek ve dişi farelerde tamamen zıt etkiler yaratmıştır. Diyet, ergen WT erkek farelerde kilo alımını %31 oranında azaltmış ve yetişkin erkek farelerde belirgin bir kilo kaybına yol açmıştır. Ancak **dişi farelerde (hem ergen hem yetişkin) 5:2 diyetinin vücut ağırlığı üzerinde hiçbir etkisi olmamıştır**.
- **Aşırı Yeme (Hiperfaji) Yanıtı:** Hem erkek hem de dişi fareler, açlık günlerinin ardındaki serbest yeme günlerinde aşırı yeme (hiperfaji) davranışı sergilemişlerdir. Ancak bu aşırı yeme, açlık günlerinde alınamayan kalorileri tam olarak telafi etmiş; yani 5:2 diyeti farelerin toplam (kümülatif) kalori alımını değiştirmemiştir.

**Sekonder Bulgular (Adipozite, Kemik ve Metabolizma)**

- **İskelet Büyümesi Hızlanmıştır:** İlginç bir şekilde, diyet her iki cinsiyette de kemik büyüme oranını (tibial epifiz plak genişliğini) %9 ila %13 oranında artırmıştır.
- **Kemik İliği Yağlanmasında Cinsiyet Farkı:** Ergen erkek farelerde kemik iliği yağlanması (adipozitesi) üç katına çıkıp adiposit sayısı ve boyutu artarken; ergen dişi farelerde tam tersine kemik iliği yağlanması yarı yarıya azalmıştır.
- **Yağ Depolarında Paradoksal Artış:** Diyet, kandaki serbest yağ asidi (FFA) miktarını erkeklerde %57 oranında artırmış olmasına rağmen (ki bu normalde yağ yakımının bir göstergesidir), farelerin "inguinal" (deri altı) beyaz yağ dokusu (WAT) her iki cinsiyette de sırasıyla %39 ve %22 oranında büyümüş, adiposit hücre boyutları artmıştır.
- **Kahverengi Yağ Dokusunun (BAT) Tembelekleşmesi:** Normalde ısı üretip kalori harcaması beklenen kahverengi yağ dokusunun kütlesi her iki cinsiyette de %37 oranında artmıştır. Hücresel analizde, kahverengi yağ hücrelerinin ısı üretme kapasitesini gösteren _Ucp1_ gen ifadesinin düştüğü ve hücrelerin içini doymuş yağ asitleriyle doldurduğu (kristalleştiği) saptanmıştır.
- **Karaciğer Yağlanması:** Karaciğer kütlesi değişmese de, karaciğerdeki yağ asidi profilinde cinsiyete özgü ufak değişimler saptanmıştır.

**Bu Bulgular Nasıl Açıklanıyor ve Tartışılıyor? (Etki Mekanizması)** Yazarlar, bu çarpıcı ve paradoksal tabloyu, hücrelerdeki iki farklı hormon aksının (Büyüme Hormonu ve Ghrelin) çatışmasıyla açıklamışlardır:

1. **Kemik Büyümesi ve Lipoliz (GH-IGF-1 Aksı):** 5:2 diyeti, büyüme hormonu (GH) ritmini tetikleyerek iskelet büyümesini hızlandırmakta ve yağ hücrelerinin içindeki yağın kana salınmasını (lipolizi) uyararak kandaki FFA'ları artırmaktadır.
2. **Ghrelin'in Yağı Savunması:** Haftada iki kez uygulanan 24 saatlik açlık, şiddetli bir ghrelin hormonu dalgasına yol açar. Bu ghrelin dalgası, vücudun inguinal (deri altı) ve kemik iliği bölgelerinde yoğun olarak bulunan GHSR reseptörlerine bağlanarak bu bölgelerdeki "yağların yakılmasını engeller" (yağı savunur) ve tam tersine dışarıdaki yağı buraya çekerek yağlanmayı artırır.
3. **Mekanizmanın İspatı (GHSR-null Fareler):** Araştırmacılar bunu ispatlamak için genetik olarak ghrelin reseptörü olmayan (GHSR-null) farelere aynı diyeti uygulamıştır. Reseptör olmadığında ergen erkeklerdeki kilo kaybı, kemik iliği yağlanması ve iskelet büyümesindeki hızlanma etkileri **tamamen ortadan kalkmıştır**. Ancak yetişkin erkeklerdeki kilo kaybı ghrelin reseptörü olmasa da devam etmiştir; bu durum yaşlanmayla birlikte ghrelin duyarlılığının düşmesiyle ilişkilendirilmiştir.

**Sonuçların Önemi ve Klinik Çıkarımlar**

- **Cinsiyete Göre Beslenme Vizyonu:** Obez olmayan bireylerde 5:2 diyeti "herkese uyan sihirli bir formül" değildir. Bu çalışma, 5:2 diyetinin kadınlarda vücut ağırlığına hiçbir fayda sağlamadığını doğrudan kanıtlamaktadır.
- **Gizli Zararlar ve Kötü Yağ Dağılımı:** Diyet, erkeklerde kilo kaybı sağlasa da, bunu arzu edilen "yağ yakımı" üzerinden yapmamaktadır. Ghrelin dalgalanmaları nedeniyle yağlar yakılmak yerine kemik iliğine ve deri altına (inguinal bölgeye) çekilerek yeniden dağıtılmaktadır. Kahverengi yağ dokusunun ısı üretim (termojenez) kapasitesinin düşmesi ve buralarda doymuş yağ depolanması metabolik açıdan son derece istenmeyen (undesirable) bir sonuçtur.
- **Kas (Yağsız Kütle) Kaybı Riski:** Kilo kaybı yaşanmasına rağmen belirli yağ depolarının büyümesi, bu zayıflamanın yağdan değil, **yağsız kütleden (kas kütlesinden veya organlardan)** gerçekleştiğini ima etmektedir. Bu durum, daha önceki klinik çalışmalarla uyumludur ve özellikle obez olmayan bireyler için 5:2 diyetinin sağlıklı bir strateji olmayabileceğine dair güçlü bir uyarıdır.

5:2 diyeti uygulanan farelerde açlık günlerinin ardından gelen serbest yeme günlerinde aşırı yeme (hiperfaji) davranışı görülmüş ve bu durum toplam kalori alımının değişmemesiyle sonuçlanmıştır. Ancak kalori alımı değişmese de erkeklerde kilo kaybı görülmesi ve dişilerde vücut ağırlığının korunması, hücresel düzeyde cinsiyete özgü endokrin (hormonal) savunma mekanizmalarından ve **ghrelin ile büyüme hormonu arasındaki metabolik çatışmadan**kaynaklanmaktadır.

**Ghrelin Üzerinden İlerleyen Derin ve Zararlı Mekanizmalar** Araştırmacılar 5:2 diyetinin yarattığı bu paradoksal durumu (kilo kaybı varken yağ depolarının büyümesini), hormonların birbirine zıt çalışmalarıyla açıklamaktadır:

- **Yağ Yakımı (Büyüme Hormonu - GH) ile Yağ Savunmasının (Ghrelin) Çatışması:** 5:2 diyetindeki 24 saatlik açlık periyotları, Büyüme Hormonu (GH) ve IGF-1 aksını uyararak iskelet büyümesini hızlandırır ve normalde yağların parçalanıp (lipoliz) kana serbest yağ asidi (FFA) olarak salınmasını sağlar. Ancak haftada iki kez uygulanan açlık, aynı zamanda devasa **ghrelin hormonu dalgalanmalarına** (bi-weekly surges) yol açar.
- **Yağın Yanlış Yerlere Depolanması:** Ghrelin, doğası gereği şiddetli bir "yağ savunucusudur". Vücudun kemik iliği ve deri altı (inguinal) bölgelerinde ghrelin reseptörleri (GHSR) çok yoğundur. Bu nedenle kana salınan yağlar enerji olarak yakılamaz; ghrelin bu yağları zorla kemik iliğine ve deri altı depolarına çekerek yağlanmayı artırır (yağın tehlikeli şekilde yeniden dağıtımı).
- **Kahverengi Yağ Dokusunun (BAT) Tembelleşmesi:** 5:2 diyetinin en zararlı metabolik etkilerinden biri, normalde ısı üretip kalori harcaması beklenen BAT hücrelerini bozmasıdır. Diyet sonucunda her iki cinsiyette de BAT kütlesi %37 artmış, ancak ısı üretimini sağlayan _Ucp1_ geninin ifadesi düşmüştür. Hücreler enerji harcamak yerine içlerini doymuş yağ asitleriyle doldurarak termojenez (kalori harcama) kapasitelerini baskılamıştır.
- **Kas (Yağsız Kütle) Kaybı İması:** Erkeklerde tartıda kilo kaybı görülmesine rağmen, kemik iliği, deri altı (inguinal) ve kahverengi yağ (BAT) depolarının boyutunun büyümesi çok ciddi bir gizli tehlikeye işaret etmektedir. Yazarlar, obez olmayan bireylerde yağ kütlesi artarken vücut ağırlığının düşmesinin, **bu kilo kaybının yağdan değil, kas (yağsız kütle) veya organ kütlesinden gerçekleştiği** anlamına geldiğini vurgulamaktadır.

**Kadınlarda Kilo Kaybı Olmamasının Sebepleri** Erkeklerde kilo kaybı görülürken dişi farelerde vücut ağırlığının tamamen aynı kalması, kalori alımından ziyade dişilerin farklı "anatomik ve metabolik yanıtlar" sergilemesiyle ilişkilendirilmiştir:

- **Kusursuz Kalori Telafisi:** Dişiler serbest yeme günlerinde, açlık günlerinde kaybettikleri kalorilerin milimetrik olarak %101.3'ünü tüketerek kusursuz bir aşırı yeme (hiperfaji) telafisi yapmışlardır.
- **Stres Yanıtı (Kortikosteron) Farklılığı:** 5:2 diyeti, erkeklerde bir stres hormonu olan kortikosteron seviyesini %50 artırırken, dişi farelerde **%35 oranında düşürmüştür**. Erkeklerde yüksek stres hormonu ghrelin ile birleştiğinde kemik iliği yağlanmasını üç katına çıkarırken, dişilerde kortikosteronun düşmesi kemik iliği yağlanmasını tam aksine yarı yarıya azaltmıştır. Kısacası dişi metabolizması, ghrelin dalgalanmalarına karşı farklı bir endokrin adaptasyon (kortikosteron düşüşü vb.) geliştirerek vücut ağırlığını dış etkilere karşı savunmuştur.
- Buna rağmen dişi fareler de, bölgesel yağ depolama (inguinal WAT ve BAT artışı) zararlarından ve termojenik kapasitenin (ısı üretiminin) düşmesinden kaçamamışlardır.

**Ghrelin'in (GHSR) Etkisinin Kesin İspatı** Araştırmacılar bu zıt mekanizmaların ghrelin yüzünden olduğunu kesinleştirmek için ghrelin reseptörü silinmiş (GHSR-null) fareleri kullanmışlardır. Reseptör ortadan kaldırıldığında, ergen erkeklerdeki kemik büyümesi, kemik iliği yağlanmasındaki artış ve **kilo kaybı tamamen yok olmuştur**. Bu bulgu, diyetteki kilo kaybının ve yağ dağılımı anormalliklerinin doğrudan ghrelin reseptörünün aktivasyonuna (GHSR) bağlı olduğunu net bir şekilde kanıtlamaktadır.