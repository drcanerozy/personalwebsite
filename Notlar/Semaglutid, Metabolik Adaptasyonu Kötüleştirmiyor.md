---
Tür:
  - Besleyici
ODAK:
  - "[[GLP-1]]"
MEKANİZMA:
DİZİN:
  - "[[Metabolizma]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[GLP-1 Tedavisinde Her Kas Kaybı Risk Değildir]]"
  - "[[GLP-1 Kullanımından Sonra Ağırlık Kazanımı]]"
  - "[[Tirzepatide, Kilo ve Yağ Kaybı Sağlasa da Adipoz Doku Disfonksiyonelliğini Düzeltmiyor]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[GLP-1 Nutrient Density ve Vücut Kompozisyonu]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: 10.1159/000553510
study_type:
evidence_direction:
primary_outcome:
p_value_summary:
---

> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["Semaglutid — GLP-1R Agonisti"] --> B["Merkezi İştah Baskılanması
Hipotalamik GLP-1R Aktivasyonu"]
>     B --> C["Sürdürülen Kalori Açığı → 11 kg Kilo Kaybı / 12 ay"]
>     C --> D["Yağ Kütlesi ↓
Mutlak FFM hafifçe ↓"]
>     D --> E["Adaptif Termojenez
ΔAT = -210 kcal/gün"]
>     F["Yaşam Tarzı Tek Başına"] --> G["Sürdürülemeyen Kalori Açığı"]
>     G --> H["ΔAT = -373 kcal/gün
p = 0.961 — Fark Anlamsız"]
>     E -.->|"İki grup arasında fark yok"| H
>     D --> I["SMI-SDS ↑ +0.52
Relatif Kas Gücü ↑"]
>     I --> J["Kas Kalitesi İyileşmesi
Fonksiyonel Sarkopeni Riski Yok"]
> ```
>
> **Şekil Açıklaması:** Semaglutid, vücudun oluşturduğu adaptif termojenezi yaşam tarzı müdahalesine göre kötüleştirmez (p=0.961); merkezi iştah baskılaması, metabolik freni aşarak sürdürülebilir kalori açığı yaratırken kas kalitesi (SMI-SDS) paradoksal olarak iyileşir.

Bu çalışma, İspanya’daki Vall d'Hebron Üniversite Hastanesi Obezite Birimi'nde (UTIO) yürütülen ve Semaglutid tedavisinin obezitesi olan (diyabeti olmayan) yetişkinlerde **vücut bileşimi, kas kütlesi/kalitesi, kas gücü, Dinlenme Enerji Harcaması (REE) ve Adaptif Termojenez (AT)** üzerindeki 12 aylık gerçek yaşam etkilerini inceleyen **Filippi-Arriaga ve arkadaşları (2026)** tarafından yayımlanmış ileri düzey bir araştırmadır.

Çalışmada, yalnızca yaşam tarzı eğitimi alan grup (n=39) ile yaşam tarzı eğitimi + Semaglutid alan grup (n=44) karşılaştırılmıştır.

---

### 1. Çalışmanın Primer (Birincil) Bulguları

- **Belirgin Kilo ve Adipozite Kaybı:** Semaglutid grubu 12 ayın sonunda ortalama **11.0 kg kilo kaybı** (BMI'da -4.0 kg/m² düşüş) sağlarken; yaşam tarzı grubunda kilo değişimi anlamlı bulunmamıştır (+1.1 kg, BMI +0.1 kg/m²). Bel çevresi (-7.0 cm) ve bel-boy oranı (-0.04) Semaglutid ile belirgin şekilde iyileşmiştir. BIA (biyoempedans) analizlerinde vücut yağ yüzdesi, yağ kütlesi ve visseral yağ alanı Semaglutid grubunda anlamlı düzeyde gerilemiştir.
- **Mutlak Kas Kaybına Karşın "Yapısal Kas İyileşmesi" (SMI-SDS):** Semaglutid grubunda mutlak İskelet Kas Kütlesi (SMM: 29.9 kg'dan 28.7 kg'a) ve Yağsız Kütle (FFM: 53.8 kg'dan 52.7 kg'a) düşmüştür. **Ancak**, yaş ve BMI'a göre düzeltilmiş MR-valideli standart sapma skorları (SMI-SDS) incelendiğinde; Semaglutid grubunda SMI-SDS skorunda **+0.52'lik son derece anlamlı bir artış (iyileşme)** saptanmıştır (yaşam tarzı grubunda +0.09). Bu durum, mutlak kas kütlesi azalsa bile kasın yeni ve hafiflemiş bedene göre **yapısal/nitelliksel olarak optimize olduğunu** göstermektedir.
- **Kas Gücünün Korunması ve Göreli Güç Artışı:** Mutlak el kavrama gücü (handgrip strength) her iki grupta da korunmuş (herhangi bir kayıp yaşanmamış); **vücut ağırlığına oranlanmış göreli kas gücü (relative handgrip strength)** ise Semaglutid grubunda anlamlı derecede yükselmiştir.

---

### 2. Adaptif Termojenez (AT) Bulguları ve Derinlemesine Yorumlar

Araştırmacıların dolaylı kalorimetre (indirect calorimetry) ve doku kütlelerine özel geliştirilmiş regresyon modelleriyle elde ettiği **adaptif termojenez** sonuçları son derece çarpıcıdır:

- **Tanım:** Adaptif termojenez (metabolik yavaşlama), kilo kaybı sırasında Dinlenme Enerji Harcamasında (REE) meydana gelen ve **sadece yağ ile kas kütlesindeki azalmayla açıklanamayan, beklentinin üzerindeki metabolik düşüştür**.
- **Sayısal Bulgular:**
    - 12 ay sonunda her iki grupta da ölçülen REE belirgin şekilde düşmüştür.
    - Çalışmaya özgü tahmin denklemi kullanılarak hesaplanan **Adaptif Termojenez değişimi (Delta AT)**; yaşam tarzı grubunda **-373.4 kcal/gün**, Semaglutid grubunda ise **-210.2 kcal/gün** olarak bulunmuştur.
    - Düzeltilmiş analizlerde (ANCOVA) iki grup arasındaki **Delta AT farkı istatistiksel olarak anlamsızdır (adjusted p=0.961)**. (Dış geçerlilik için kullanılan Ostendorf denklemiyle de fark anlamsız çıkmıştır, p=0.274).

#### 🧠 Yazarların Adaptif Termojenez Yorumları ve Klinik Anlamı:

1. **"Semaglutid Metabolik Yavaşlamayı Kışkırtmaz (Exacerbate Etmez)":** Obezite tedavisinde en büyük korkulardan biri, güçlü ilaçlarla sağlanan hızlı kilo kaybının vücutta şiddetli bir "metabolik savunma mekanizmasını" tetikleyerek adaptif termojenezi katlamasıdır. Bu çalışma, Semaglutid ile ~11 kg verilmesine rağmen, metabolik yavaşlamanın hiç kilo veremeyen yaşam tarzı grubuyla **aynı seviyede kaldığını (ve hatta sayısal olarak daha düşük gerçekleştiğini)** göstererek bu kaygıyı çürütmektedir.
2. **Metabolik Fren Karşısında İlacın Üstünlüğü:** Hem yaşam tarzı müdahalesi hem de ilaç tedavisi vücutta biyolojik bir "enerji koruma cezası" (metabolik fren) başlatmaktadır. Ancak yaşam tarzı grubu bu metabolik fren nedeniyle kilitlenip kilo veremezken; Semaglutid'in merkezi sinir sistemi üzerindeki iştah ve tokluk baskılama mekanizması, **bu metabolik engeli aşacak kadar güçlü bir kalori açığı yaratmaya devam etmekte** ve kilo kaybını sürdürebilmektedir.
3. **İlaç Bırakıldığında Geri Kilo Alma (Rebound) Riski:** Her iki grupta da gelişen ~200-370 kcal/günlük adaptif termojenez, ilacın bırakılması durumunda hastaların neden hızla geri kilo aldığını (yaklaşık ayda 0.8 kg) metabolik olarak açıklamaktadır. İlaç kesildiğinde iştah geri gelirken metabolik hızın hâlâ baskılanmış olması, kilo alımını kolaylaştırmaktadır.

---

### 3. Özet ve Klinik Çıkarım

Çalışma, GLP-1 (Semaglutid) tedavisi altındaki hastaların takibinde **sadece tartı kilosuna bakmanın yetersiz olduğunu**; BIA ile kas kalitesinin (SMI-SDS), dinamometre ile kas gücünün ve dolaylı kalorimetre ile metabolik adaptasyonun bütüncül olarak izlenmesi gerektiğini kanıtlamaktadır. Semaglutid, kas gücünü koruyarak ve metabolik hızı ekstra cezalandırmadan etkili bir yağ kaybı sağlamaktadır.