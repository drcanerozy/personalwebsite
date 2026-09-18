---
Tür:
  - Besleyici
ODAK:
  - "[[Obezite]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Benzer Risk Faktörlerinde Bile Obezite İlişkili Morbidite Riski Değişkenlik Gösteriyor]]"
  - "[[Obezite Tanısında EASO 2024 Yaklaşımı]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ: "[[Benzer Risk Faktörlerinde Bile Obezite İlişkili Morbidite Riski Değişkenlik Gösteriyor]]"
BAĞLANTILI DERSLER:
  - "[[Yetişkinlerde Beslenme Tedavisi Uygulaması]]"
YORUM:
KAYNAK: https://doi.org/10. 1016/j.ebiom.2026. 106272
study_type:
evidence_direction: "positive"
primary_outcome:
p_value_summary:
BESLEDİĞİ NOTLAR:
  - "[[Obezite Tanısında ABCD Yaklaşımı]]"
  - "[[BKİ Yerine Adipozite Bazlı Sınıflandırma Hastalık Riski ile Daha Fazla İlişkili]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

![[ABCDrisk2.png]]

![[ABCDrisk3.png]]

![[ABCDrisk1.png]]

### 1. Çalışma Nasıl Tasarlandı ve Sınıflandırma Nasıl Yapıldı?

- **Popülasyon ve Takip:** UK Biobank kohortundan **489.311 yetişkin** birey dahil edilmiş ve ortanca **13.1 yıl** (15 yıla kadar) boyunca prospektif olarak izlenmiştir.
- **3x3 Adipozite Matrisi (BF% – WC):** Araştırmacılar sadece tartıya ve boya dayalı VKİ yerine, vücut yağının **toplam miktarını** gösteren _Vücut Yağ Yüzdesi (BF%)_ ile **dağılımını/viseral birikimini** gösteren _Bel Çevresi (WC)_ parametrelerini cinsiyete özgü DSÖ eşik değerleriyle 3x3'lük bir matriste birleştirmiştir:
    - **Kadınlar:** BF% (<30%<30%, 30−35%30−35%, >35%>35%) ve Bel Çevresi (<80 cm<80 cm, 80−88 cm80−88 cm, >88 cm>88 cm)
    - **Erkekler:** BF% (<20%<20%, 20−25%20−25%, >25%>25%) ve Bel Çevresi (<94 cm<94 cm, 94−102 cm94−102 cm, >102 cm>102 cm)
- **5 Aşamalı Trafik Lambası Risk Gruplandırması:** Bu 9 kombinasyon, kardiyometabolik riske göre 5 gruba indirgenmiştir:
    - 🟢 **Grup 1 (Risk Yok - Referans, %15):** Hem BF% hem WC normal.
    - 🟢 **Grup 2 (Hafif Artmış Risk, %17):** Biri hafif yüksek, diğeri normal.
    - 🟡 **Grup 3 (Artmış Risk, %16):** Her ikisi hafif yüksek veya biri yüksek diğeri normal.
    - 🟠 **Grup 4 (Yüksek Risk, %19):** Biri yüksek, diğeri hafif yüksek.
    - 🔴 **Grup 5 (Çok Yüksek Risk, %32):** Hem BF% hem WC yüksek.

---

### 2. Temel Bulgular ve İstatistiksel Çıktılar

Takip süresi boyunca **24.778 kişide 3P-MACE** (ölümcül olmayan MI + inme + KV ölüm), **30.376 kişide Tip 2 Diyabet (T2D)** ve **14.906 kişide Kronik Böbrek Hastalığı (CKD)** gelişmiştir.

1. **T2D'de Devasa Risk Artışı:**
    - Grup 1'e kıyasla Grup 5'teki bireylerde Tip 2 Diyabet gelişme riski tam **9.23 kat (HR: 9.23, %95 GA 8.70–9.83)** artmıştır.
    - 15 yıllık kümülatif T2D insidansı Grup 5'te **%14.8** iken Grup 1'de yalnızca **%1.5**'tir.
2. **Kardiyovasküler ve Renal Hasar:**
    - Grup 5'te 3P-MACE riski **%63 daha yüksek (HR: 1.63)**, CKD riski ise **2.27 kat (HR: 2.27)** bulunmuştur.
3. **VKİ Düzeltmesinden Sonra Bile Korunan Risk:**
    - Modele VKİ eklendiğinde dahi (kolineriteye rağmen) BF%–WC sınıflamasının T2D, böbrek ve kalp üzerindeki bağımsız öngörü gücü istatistiksel olarak anlamlı kalmaya devam etmiştir.
4. **VKİ ile Uyuşmazlık (Discordance):**
    - En yüksek riskli grup olan **Grup 5'teki bireylerin neredeyse 1/3'ü (%32.6)** geleneksel VKİ sınıflamasına göre **"Obez Değil"** (Normal kilolu veya Fazla kilolu) çıkmaktadır!

---

### 3. Figür Bazında Hikayeleştirilmiş Analiz ve Klinik Yorumlar

#### 📊 Figür 1: Trafik Lambası Modeli ve Zaman İçinde Ayrışan Kaderler

_(3x3 Matris, Kümülatif İnsidans Eğrileri ve Tehlike Oranları)_

[Figür 1 Konsepti]

Grup 1 (Yeşil)  ───────> Düz seyreden düşük insidans çizgileri

Grup 2-4        ───────> Kademeli yükselen risk basamakları

Grup 5 (Kırmızı) ───────> Özellikle T2D'de dik açıyla fırlayan eğri (9 kat risk)

- **Hikayeleştirme:** Kliniğe aynı gün başvuran 5 farklı danışanı hayal edin. Yaş ve cinsiyetleri benzer olsa da vücut kompozisyonu matrisindeki yerleri farklı.
- **Klinik Yorum:** Figür 1'in kümülatif insidans eğrilerinde en dikkat çeken unsur **T2D eğrisinin Grup 5 için bir roket gibi dikleşmesidir.** Kalp damar ve böbrek hastalıkları kümülatif olarak zamanla birikirken, viseral yağlanma ve aşırı total yağ (Grup 5) glukoz metabolizmasını çok daha erken ve agresif bir şekilde çökertmektedir. Bu durum, kardiyometabolik-böbrek sendromunda (CKM) ilk domino taşının her zaman beta hücre disfonksiyonu ve glukotoksisite olduğunu doğrular.

---

#### 🌊 Figür 2: Alluvial (Akış / Sankey) Diyagramı — "Görünmez Hastalar"

_(BF%–WC Risk Grupları ile Standart VKİ Kategorileri Arasındaki Geçişler)_

[Figür 2 Akış Mantığı]

BF% - WC Grupları               VKİ Sınıfları

─────────────────               ─────────────

Grup 1 (Yeşil)   ═════════════> Normal Kilo (%89)

Grup 2-3         ═════════════> Fazla Kilolu (Overweight) - BÜYÜK KAOS

Grup 4 (Turuncu) ═════════════> Fazla Kilolu (%74.5)

Grup 5 (Kırmızı) ════╤════════> Obezite Evre I-III (%67.4)

                     └────────> 🔴 Fazla Kilo & Normal Kilo (%32.6 GİZLİ YÜKSEK RİSK)

- **Hikayeleştirme:** Figür 2, adeta sağlık sisteminin nasıl "kör" olabildiğini gösteren bir haritadır. Ortadaki "Fazla Kilolu" (Overweight, BMI 25–29.9) havuzu adeta devasa bir kavşaktır; içinde risksiz Grup 1 hastası da vardır, organları yağ içinde yüzen Grup 5 hastası da.
- **Klinik Yorum:** Klasik sistemde hekim bu hastaya _"Biraz kilonuz var ama obez değilsiniz, acil ilaca/tedaviye gerek yok"_ der. Oysa Alluvial akışı gösteriyor ki; **Grup 5'teki her 3 kişiden biri bu 'fazla kilolu' maskesinin arkasına saklanmaktadır.** Hatta bu yüksek riskli grubun %5'e yakını tamamen "Normal VKİ"ye sahiptir (Normal Weight Obesity / Sarkopenik Obezite).

---

#### ⚖️ Figür 3: Paradoksun Çözümü — "Kilolu Ama Kaslı" vs. "Normal Kilolu Ama Viseral Yağlı"

_(BMI Katmanlarına Göre Yüksek Riskli Grupların [Grup 4 ve 5] Karşılaştırmalı Riskleri)_

[Figür 3 Çarpıcı Karşılaştırması]

1. Senaryo: Grup 5 (Çok Yüksek Adipozite) + Fazla Kilolu (BMI 25-29.9) ──> 3P-MACE HR: 1.45

2. Senaryo: Grup 4 (Yüksek Adipozite)      + Obez (BMI ≥ 30)         ──> 3P-MACE HR: 1.41

(Sonuç: Düşük kilolu olanın kalp krizi/inme riski, daha kilolu olandan daha yüksek!)

- **Hikayeleştirme (İki Hasta Karşılaştırması):**
    - **Hasta A (BMI 28, Bel Çevresi 104 cm, Yağ %40 - Grup 5):** Tartıda hafif kilolu görünür.
    - **Hasta B (BMI 31, Bel Çevresi 96 cm, Yağ %26 - Grup 4):** İri yapılı, kas kütlesi daha iyi, tartıda "obez" görünür.
- **Klinik Yorum:** Figür 3b'deki Cox analizleri kanıtlamaktadır ki; **Hasta A'nın kalp krizi, inme ve diyabet riski, Hasta B'den daha yüksektir.** Hatta normal kilolu olup Grup 5 fenotipinde olan bir bireyin T2D riski, sağlıklı bireye göre **4.24 kat** daha fazladır.

---

### 4. Patofizyolojik Nedenler: Neden Bu Kadar Farklılar?

1. **Ektopik Yağlanma ve Viseral Adipozite (VAT) Toksisitesi:**
    - Bel çevresi (WC), doğrudan visseral yağın ve karaciğer yağlanmasının (MASLD) yansımasıdır. Visseral yağ dokusu portal dolaşıma serbest yağ asitleri ve pro-inflamatuar sitokinler (IL-6, TNF-αα) pompalayarak hepatik insülin direncini tetikler.
2. **Sarkopeni ve İskelet Kası Kalitesi:**
    - VKİ normal veya hafif yüksek olan ancak BF% yüksek olan bireylerde iskelet kası kütlesi yetersizdir. Glukozun %80'inin iskelet kası tarafından klerens edildiği düşünüldüğünde, kası az-yağı çok bireyler (Sarkopenik obezite) diyabete karşı tamamen savunmasız kalmaktadır.
3. **Kardiyovasküler-Böbrek-Metabolik (CKM) Sendromu Hattı:**
    - Visseral yağ kaynaklı sistemik inflamasyon ve hiperinsülinemi; endotel disfonksiyonuna (MACE riski) ve glomerüler hiperfiltrasyon/podosit hasarına (CKD riski) neden olarak organ hasarını başlatmaktadır.

---

### 5. Klinik ve Diyetetik Mesaj

> **Özet Sonuç:** Bu çalışma, **"Boy ve kiloyu oranlayıp hastayı taburcu etme"** devrinin kapandığını göstermektedir. Rutin klinik pratikte **Bel Çevresi ve BIA/Vücut Yağ Yüzdesi ölçümü**, en az tansiyon ölçümü kadar hayati bir tarama aracı olmak zorundadır. Yalnızca bu iki basit ölçüm birleştirildiğinde bile, hiçbir pahalı genetik/proteomik teste gerek kalmadan diyabet riski 9 kat, böbrek riski 2 kat yüksek olan "gizli" hastalar erkenden yakalanabilmektedir.

### 1. Aynı Obezite Sınıfındaki (BMI≥30BMI≥30) Bireylerin Risk Ayrışması

Geleneksel tıpta BMI≥30 kg/m2BMI≥30 kg/m2 olan herkese homojen bir risk grubu gibi bakılır. Oysa çalışma, **obez bireylerin kendi içinde de tek tip olmadığını** gösteriyor:

- **Obez + Grup 4 Birey:** Vücut yağ oranı yüksek ancak bel çevresi/viseral yağ birikimi nispeten sınırlı olan obez bir hastada 15 yıllık Tip 2 Diyabet (T2D) riski belirgin şekilde daha ılımlı seyreder.
- **Obez + Grup 5 Birey:** Hem aşırı vücut yağı hem de geniş bel çevresi (şiddetli viseral adipozite) taşıyan obez bir hastada 15 yıllık T2D insidansı **%17.5**'e, 3P-MACE (kalp krizi/inme/ölüm) riski ise tepe noktaya fırlar.
- **Klinik Anlamı:** İki kişi de tartıda "obez"dir; ancak birinin organları viseral yağ ve lipotoksisite ile kuşatılmışken, diğeri yağı daha çok deri altında (subkutan) depolayabildiği için kardiyometabolik hasarı çok daha azdır.

---

### 2. "Fazla Kilolu" (Overweight, BMI 25–29.9) Havuzundaki Kaotik Ayrışma

Makalenin en çarpıcı bulgusu, **BMI 25−29.9 kg/m2BMI 25−29.9 kg/m2 aralığındaki bireylerin risk yelpazesinin Grup 1'den Grup 5'e kadar bütün kademeleri içermesidir:**

- **Senaryo A (Fazla Kilolu ama Metabolik Olarak Sağlıklı):** VKİ'si 28 olan, iyi kas kütlesine sahip, bel çevresi dar bir birey **Grup 1 veya 2**'de yer alır. Kalp krizi veya diyabet riski, normal kilolu bir insandan farksızdır.
- **Senaryo B (Fazla Kilolu ama Gizli Yüksek Riskli):** Yine VKİ'si 28 olan ancak kası az, bel çevresi geniş (viseral yağlı) bir birey **Grup 5**'e girer.
- **Çarpıcı Karşılaştırma (Figür 3b):** Grup 5 + Fazla Kilolu (BMI 25-29.9) Kalp Olayı Riski (HR: 1.45)≥Grup 4 + Obez (BMI ≥30) Riski (HR: 1.41)Grup 5 + Fazla Kilolu (BMI 25-29.9) Kalp Olayı Riski (HR: 1.45)≥Grup 4 + Obez (BMI ≥30) Riski (HR: 1.41) Yani tartıda **"daha zayıf / sadece hafif kilolu"** olan kişi, tartıda **"obez"** olandan daha yüksek kalp krizi ve inme riski taşımaktadır!

---

### 3. Normal Kilolu Obezite (Normal Weight Obesity - NWO) Riski

Aynı şekilde, BMI 18.5–24.9 kg/m2BMI 18.5–24.9 kg/m2 (tamamen normal kilo) olup vücut kompozisyonu bozuk (yüksek yağ %, geniş bel) olan **Grup 5** bireylerde:

- **Tip 2 Diyabet riski:** Normal akranlarına göre **4.24 kat (HR: 4.24)** artmaktadır.
- **Kardiyovasküler olay (3P-MACE) riski:** **%45 daha yüksek (HR: 1.45)**.
- **Kronik böbrek hastalığı (CKD) riski:** **%58 daha yüksek (HR: 1.58)**.

---

### 4. Yaş ve Cinsiyete Göre Risk Farklılaşması (Subgroup Heterojenitesi)

Makaledeki alt grup etkileşim analizleri (_Interaction tests_), aynı risk fenotipine sahip olsalar bile demografik faktörlerin risk şiddetini nasıl değiştirdiğini ortaya koymuştur:

1. **Genç Yaşta (<60 yaş) Obezitenin Yıkıcı Etkisi:**
    - Aynı Grup 5 fenotipine sahip **60 yaş altı genç bireylerde T2D riski 4.52 kat (HR: 4.52)** artarken;
    - **60 yaş üstü bireylerde bu artış 2.89 kat (HR: 2.89)** düzeyinde kalmaktadır (p<0.001p<0.001).
    - _Nedeni:_ Genç yaşta ortaya çıkan viseral yağlanma çok daha agresif bir metabolik tahribat yaratmakta; yaşlılarda ise diyabete yaşlanmanın doğal beta-hücre kaybı gibi başka faktörler de eşlik ettiği için obezitenin göreceli etkisi gençlerdeki kadar dik olmamaktadır.
2. **Cinsiyet Bazlı Ayrışma:**
    - Düşük ve orta risk gruplarında (Grup 2-4) erkeklerin diyabet riski kadınlardan daha yüksek seyrederken;
    - En uç grup olan **Grup 5'te kadınların T2D tehlike oranı (HR: 3.86), erkekleri (HR: 3.28) geride bırakmaktadır.**

---

### Özetle

Her iki makale de tek bir büyük gerçeğin altını çizmektedir:

> **"VKİ hastanın kilosunu söyler, ancak hastalığını ve gelecekteki komplikasyon riskini söyleyemez."** Aynı VKİ'ye, aynı yaşa veya cinsiyete sahip iki hastadan biri sadece basit bir yaşam tarzı takibi gerektirirken; diğeri sessizce ilerleyen bir karaciğer yağlanması, yaklaşan bir Tip 2 diyabet ve koroner olay riskiyle karşı karşıyadır. Bu nedenle **Bel Çevresi (viseral yağ) + Vücut Yağ Yüzdesi (adipozite)** ikilisi, klasik VKİ'nin yarattığı bu kör noktayı tamamen ortadan kaldırmaktadır.