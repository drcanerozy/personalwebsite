---
Tür:
  - Besleyici
ODAK:
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[İnflamasyon]]"
  - "[[İmmün Sistem]]"
  - "[[Leptin]]"
DİZİN:
  - "[[00_İnflamasyon ve İmmün Sistem_MOC]]"
  - "[[00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
  - "[[Adipoz Doku Endokrin Fonksiyonu ve Adipokin Dinamikleri]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "p = 0.041"
BESLEDİĞİ NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
  - "[[İmmün Yanıt ve İnflamasyon Döngüsü]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Enerji Kısıtlaması / Açlık"] --> B["AMPK Aktivasyonu"]
>     B -->|Katabolik Sinyal| C["Lipoliz ve Yağ Oksidasyonu"]
>     B -->|Geri Bildirim| D["TBK1 İndüksiyonu"]
>     D -.->|İnhibisyon / Fren| B
>     E["Kronik Düşük Dereceli İnflamasyon"] -->|Sürekli Yüksek| D
> ```
>
> **Şekil Açıklaması:** Enerji kısıtlaması veya açlıkta aktive olan AMPK, lipoliz ve yağ oksidasyonunu uyarırken aynı zamanda TBK1 indüksiyonunu tetikleyerek negatif bir geri bildirim freni oluşturur; kronik düşük dereceli inflamasyon varlığında ise TBK1 sürekli yüksek kalarak AMPK'yi baskılar ve katabolik yağ yıkımını kilitler.

> **Metodolojik Etiketler:** #finding/contradictory
### İçindekiler

- [[#Giriş — Açlığın İki Yüzü- Enflamasyonu Artıran ve Azaltan]]
- [[#Normal Fizyoloji — İmmün Sistemin Enerji Durumuna Duyarlılığı]]
- [[#Leptin ve Akut Faz Yanıtının Paradoksal İlişkisi]]
- [[#İmmünoglobulin Baskılanması ve Th1-Th2 Kayması]]
- [[#Klinik İnsan Verisi — Protokol-Spesifik Sitokin Yanıtları]]
- [[#Sentez — Aynı Yönde mi, Zıt Yönde mi]]
- [[#Kişisel Notlarım]]

---

### Giriş — Açlığın İki Yüzü: Enflamasyonu Artıran ve Azaltan

Aralıklı açlığın "anti-enflamatuar" olduğu yönündeki popüler anlatı, Stefanakis et al. (2024)'ün leptin proteomik verisiyle karşılaştırıldığında beklenmedik bir gerilim ortaya çıkarıyor: leptin replasmanı (yani düşen leptin seviyesinin _tersine çevrilmesi_) aslında pro-enflamatuar akut faz yanıtını güçlü biçimde **artırıyor**. Buna karşılık Permataputri et al. (2025)'in insan TRE çalışması, günlük zaman-kısıtlı beslenmenin pro-enflamatuar IFN-γ'yı **azalttığını** gösteriyor. Bu iki bulgu çelişkili değil — farklı sinyalleri, farklı zaman ölçeklerinde ve farklı immün eksenlerde inceliyorlar; bu not bu ayrımı netleştirmeyi amaçlıyor.

---

### Normal Fizyoloji — İmmün Sistemin Enerji Durumuna Duyarlılığı

Leptin, yalnızca bir doygunluk hormonu değil, aynı zamanda İmmün Sistem için bir "enerji yeterliliği" sinyalidir — leptin reseptörleri T hücreleri, monositler ve NK hücreleri gibi birçok immün hücrede eksprese edilir. Yeterli enerji/leptin varlığında, immün sistem Th1-yönelimli, proliferatif bir profil sürdürebilir; enerji/leptin eksikliğinde ise bu kapasite kısıtlanır (klasik açlık-immünsüpresyon ilişkisi). Bu bağlamda leptin düşüşü, immün sistemin geçici olarak "tasarruf moduna" geçmesinin bir işaretidir.

---

### Leptin ve Akut Faz Yanıtının Paradoksal İlişkisi

Stefanakis et al. (2024), hem 72 saatlik kısa dönem açlık+leptin replasmanı hem de 36 haftalık uzun dönem metreleptin tedavisi (REDs'li hipoleptinemik kadınlarda) modellerinde tutarlı bir örüntü buluyor: **leptin seviyesinin yükseltilmesi, CRP ve CD14 gibi akut faz proteinlerini kitlesel olarak yukarı çekiyor.** Bu, sezgiye aykırı görünebilir — çünkü leptin genellikle "obezitede yüksek, açlıkta düşük" bir hormon olarak bilinir ve obezite kronik düşük dereceli enflamasyonla ilişkilendirilir. Ama bu çalışma, leptinin akut olarak _yükseltilmesinin_ (fizyolojik replasman dozlarında bile) doğrudan pro-enflamatuar bir tetikleyici olduğunu gösteriyor — leptin, sınıf I sitokin reseptörü üzerinden sinyalleşen gerçek bir proinflamatuar adipokindir, obezitedeki kronik hiperleptinemi de büyük olasılıkla bu akut mekanizmanın kronikleşmiş bir versiyonudur.

Uzun dönem çalışmada bu etki, 24. haftada (en yüksek leptin konsantrasyonlarının görüldüğü dönem) zirveye ulaşıyor: SAA1/SAA2, LBP, THBS4, DBH, NCAM1 gibi akut faz ve hücre-matriks proteinleri güçlü biçimde artıyor. Ayrıca leptin, kortizol bağlayıcı SERPINA6'yı belirgin, tiroksin bağlayıcı SERPINA7'yi hafif düzeyde baskılayarak HPA ve tiroid eksenlerini de moleküler düzeyde etkiliyor — bu, Adipoz Doku Endokrin Fonksiyonu ve Adipokin Dinamikleri notunda daha ayrıntılı ele alınıyor.

---

### İmmünoglobulin Baskılanması ve Th1-Th2 Kayması

Leptinin ikinci büyük immünolojik etkisi, B-lenfosit aracılı hümoral bağışıklığın baskılanması: immünoglobulin değişken zincirleri, hem kısa hem uzun dönem çalışmalarda tutarlı biçimde down-regüle oluyor. Bu, leptinin hayvan çalışmalarında gösterilen Th1-yönelimli T hücre proliferasyonunu artırıp Th2-aracılı immünoglobulin üretimini baskılama etkisiyle uyumlu. İlginç biçimde, uzun dönem çalışmada belirli bir immünoglobulin alt kümesi (örn. IGLV8-61) bu genel baskılanma örüntüsüne aykırı olarak _artıyor_ — yazarlar bunu, kronik leptin maruziyetine karşı gelişen bir B hücre adaptif/kompanzatuar yanıtı olarak yorumluyor.

---

### Klinik İnsan Verisi — Protokol-Spesifik Sitokin Yanıtları

Permataputri et al. (2025), obez genç kadınlarda 20 günlük TRE (18:6) ve ADMF (%25 enerji alımı) protokollerini karşılaştırdığında, pro-enflamatuar IFN-γ'da yalnızca **TRE** grubunda anlamlı bir azalma buluyor (kontrol grubuna göre de anlamlı, p=0.041); ADMF'de hiçbir sitokin değişikliği yok. Bu fark, antropometrik değişiklikten (BMI, yağ kütlesi, visseral yağ — hiçbiri değişmedi) bağımsız gerçekleşiyor; yani immünomodülasyon, yağ kaybına ihtiyaç duymadan, muhtemelen sirkadiyen hizalanma (Bmal1/Clock genleriyle günlük açlık-beslenme döngüsünün senkronizasyonu) ve AMPK aktivasyonu/mTOR baskılanması üzerinden gerçekleşiyor. IL-10 (anti-enflamatuar) ise hiçbir grupta değişmiyor — yazarlar bunu, enflamasyonun IL-10 aracılı kompanzasyona ihtiyaç duymadan da azaltılabileceği şeklinde yorumluyor.

---

### Sentez — Aynı Yönde mi, Zıt Yönde mi

Bu iki çalışma birbirini çürütmüyor, tamamlıyor: Stefanakis et al. (2024) leptinin _kendisinin_ akut faz yanıtını tetiklediğini gösterirken, Permataputri et al. (2025) günlük TRE'nin (ki bu protokolde leptin doğrudan ölçülmemiş, ama günlük açlık dönemlerinde leptin düşüşü beklenir) sistemik IFN-γ'yı azalttığını gösteriyor. Olası bir birleştirici hipotez: leptin _artışı_ akut faz proteinlerini (CRP, CD14, SAA gibi doğuştan/innate immünite bileşenleri) tetiklerken, düzenli günlük açlık döngüleri Th1-kaynaklı sitokinleri (IFN-γ, adaptif immünite) farklı bir yoldan (sirkadiyen + AMPK/mTOR) baskılıyor olabilir. Bu, "enflamasyon" tek bir eksen değil, en az iki farklı immünolojik kompartmanın (doğuştan/akut faz vs. adaptif/T hücre) fasting'e farklı yanıt verdiği anlamına geliyor — derlemenin genel "fasting tek bir şey değildir" temasının immünoloji alanındaki yansıması.