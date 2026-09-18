---
Tür:
  - Besleyici
ODAK:
  - "[[GLP-1]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[GLP-1 İlaçlarının Formları]]"
  - "[[GLP-1'e Giriş]]"
  - "[[Gelecek GLP-1 İlaçları]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[Yetişkinlerde Beslenme Tedavisi Uygulaması]]"
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[GLP-1'e Giriş]]"
  - "[[Gelecek GLP-1 İlaçları]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["GLP-1 Reseptör Agonizmi"] --> B["Santral İştah Baskılanması (POMC/CART)"]
>     A --> C["Gastrik Boşalmada Yavaşlama"]
>     B & C --> D["Spontan Kalori Kısıtlaması & Hızlı Kilo Kaybı"]
>     D --> E{"Yetersiz Protein & Direnç Egzersizi Yokluğu"}
>     E -->|Miyosteatoz & Katabolizma| F["İskelet Kası Kaybı (Sarkopenik Obezite)"]
>     E -->|Yüksek Protein & Egzersiz| G["Yağsız Kas Kütlesinin Korunması"]
> ```
>
> **Şekil Açıklaması:** GLP-1 reseptör agonizminin sağladığı santral iştah baskılanması ve gecikmiş gastrik boşalma hızlı kilo kaybı yaratır. Bu süreçte yetersiz protein alımı ve direnç egzersizi yokluğu miyosteatoz ve iskelet kası kaybına (sarkopenik obezite) yol açarken; hedefe yönelik yüksek protein ve direnç antrenmanı yağsız dokuyu korur.

GLP-1
Gelin 1990'lara gidelim. Araştırmacılar, bağırsaklarımızdan salgılanan ve kan şekerini düzenleyen 'GLP-1' adında bir hormon keşfetmişlerdi. Ancak ortada devasa bir biyolojik engel vardı: Bu hormon insan vücuduna enjekte edildiğinde sadece 5 dakika hayatta kalabiliyor, DPP-4 adındaki bir enzim tarafından anında parçalanıp yok ediliyordu. Etkisi o kadar kısaydı ki, tıp dünyası bunun bir ilaç olabileceğine dair inancını tamamen yitirmişti.

İşte tam bu umutsuzluk anında, New York'taki bir hastanede çalışan biyokimyager John Eng, egzotik hayvanların zehirlerini incelerken inanılmaz bir şey buldu. 'Gila Canavarı' adı verilen zehirli bir dev kertenkelenin tükürüğünde, insan GLP-1'ine %50 benzeyen ama enzimler tarafından asla parçalanmayan bir molekül (Exendin-4) vardı. Eğer bu kertenkele sizi ısırırsa zehirlenip ölüyordunuz; ama bu zehir laboratuvarda işlendiğinde dünyanın ilk GLP-1 ilacının temelini oluşturdu.

Ancak bu keşif bile dev ilaç şirketlerini ikna etmeye yetmedi. Novo Nordisk şirketinde bu projenin başına Lotte Bjerre Knudsen adında, henüz doktorası (PhD) bile olmayan çok genç bir kadın araştırmacı atanmıştı. Şirket yönetimi bu projeyi o kadar tuhaf ve işe yaramaz görüyordu ki, 1996 yılında Lotte'yi karşılarına alıp şu tarihi ültimatomu verdiler: _'Eğer bu sorunu 1 yıl içinde çözemezsen, şirketteki tüm GLP-1 araştırmalarını tamamen kapatıyoruz!'_.

Lotte pes etmedi. Kendisini 'Yalnız Kadın Savaşçı' olarak tanımladığı bu süreçte, molekülün üzerine doğal bir yağ asidi ekleyerek onun kandaki albümine tutunmasını sağladı ve o 5 dakikalık ömrü tam 12 saate çıkarmayı başardı.

Peki gelelim asıl soruya: **Araştırmacılar ve şirket, bu ilacın günün birinde dünyayı kasıp kavuran bir 'obezite ve kalp ilacına' dönüşeceğini biliyor muydu? En baştan her şeyi planlamışlar mıydı?**

Kesinlikle hayır! Yönetim toplantılarında konuşulan tek şey *'modern insülinler, modern insülinler, modern insülinler'*di. GLP-1 sadece diyabet için tasarlanıyordu. Fakat Lotte ve ekibi laboratuvarda tuhaf bir şey fark etti; GLP-1'i fazla üreten fareler yemek yemeyi tamamen kesiyor, adeta kendilerini aç bırakıyorlardı. Lotte, bu ilacın obezite tedavisinde de kullanılabileceğini şirketin pazarlama departmanına ilk sunduğunda aldığı cevap şu oldu:

_'Bir molekülde iki farklı biyoloji barındıramazsınız. Bu ilaç ya diyabet içindir ya da kilo kaybı içindir!'_.

O dönemde obezite biyolojik bir hastalık olarak değil, 'irade zayıflığı' olarak görülüyordu ve yönetim bu işe girmeye hiç sıcak bakmıyordu. İlacın kardiyovasküler (kalp-damar) hastalıklara veya beyin sağlığına iyi geleceği ise akıllarının ucundan bile geçmemişti. Hatta yıllar sonra ilacın kalp krizlerini ve felçleri önlediği ilk kez bir kongrede açıklandığında, araştırmacılar salonda sevinç gözyaşları dökecek kadar şaşkındı.

GLP-1'in Gelişim Tarihçesi (Figür 1'lerin Adım Adım Analizi)

**1. Temel Kavramların Doğuşu (1902 - 1964)**

- **1902 - Sekretin'in Keşfi:** William Bayliss ve Ernest Starling'in ilk hormon olan sekretini keşfetmesi, bağırsakların uzak organları (pankreas gibi) etkileyen faktörler salgılayabileceği fikrini doğurdu.
- **1964 - "İnkretin Etkisi"nin Ölçülmesi:** Ağız yoluyla alınan glukozun, damar yoluna (IV) kıyasla çok daha yüksek bir insülin tepkisine yol açtığının kanıtlanmasıyla, bağırsak kaynaklı insülin uyarıcı faktörlerin gücü sayısal olarak ortaya kondu.

**2. GLP-1'in Keşfi ve Biyolojik Engeller (1985 - 1987)**

- **1985/1986 - GLP-1'in Güçlü Bir İnkretin Olarak Tanımlanması:** Jens Juul Holst, Joel Habener ve Svetlana Mojsov gibi araştırmacılar, GLP-1'in amino asit dizilimini tanımlayarak pankreastan güçlü bir şekilde insülin salgılattığını kanıtladılar.
- **1987 - DPP-4 Yıkımının Keşfi:** Carolyn Deacon ve Jens Juul Holst, doğal GLP-1'in kanda bulunan DPP-4 enzimi tarafından hızla parçalandığını ve yarı ömrünün sadece 5-10 dakika olduğunu buldu. Bu durum, o dönem için GLP-1'in bir ilaç olarak kullanılmasının önündeki en büyük engeldi.

**3. Zehirden İlaca ve Tokluk Etkisi (1992 - 1996)**

- **1992 - Gila Canavarı Zehrinde Exendin-4'ün Keşfi:** John Eng, tesadüfi bir şekilde Gila canavarı zehrinde, DPP-4 enzimine dirençli ancak GLP-1 benzeri etkiler gösteren "Exendin-4" peptidini keşfetti. Bu, ilaç geliştirme çalışmalarının önünü açtı.
- **1996 - Tokluk Hormonu (Satiety Hormone) Etkisi:** Arne Astrup, Jens Juul Holst, Anne Flint ve Anne Raben, GLP-1 infüzyonunun midede boşalmayı yavaşlattığını ve insanlarda kendiliğinden alınan enerji miktarını azaltarak tokluğu (satiety) artırdığını kanıtladı. Bu keşif, ilacın rotasını diyabetten obeziteye çeviren tarihi bir andı.

**4. Kliniğe İlk Girişler (2005 - 2014)**

- **2005 - Exenatide (Byetta) Onayı:** Gila canavarı zehrinden sentezlenen günde iki kez kullanılan bu ilaç, FDA'dan onay alan ilk GLP-1 reseptör agonisti oldu ve diyabet tedavisinde "inkretin" yaklaşımını doğruladı.
- **2010 - Liraglutide (Victoza) Onayı:** Rasyonel protein mühendisliği ile geliştirilen, albumin bağlama özelliği sayesinde yarı ömrü 13 saate çıkan ve günde bir kez kullanılabilen ilk insan GLP-1 analoğu diyabet için onaylandı. Lotte Bjerre Knudsen ve Mads Krogsgaard Thomsen bu sürece öncülük etti.
- **2014 - Dulaglutide (Trulicity) Onayı:** Haftada bir kullanılabilen formüller kliniğe girdi.
- **2014 - Obezitede İlk Onay (Liraglutide 3.0 mg - Saxenda):** SCALE çalışması sonucunda, liraglutide'in diyabet harici sadece obezite tedavisi (kilo kaybı) için onay alan ilk GLP-1 analoğu olması tescillendi.

**5. Devrim Yılları: Kalp Koruması ve Çoklu Agonistler (2016 - 2023)**

- **2016 - LEADER ve SUSTAIN-6 Çalışmaları:** Liraglutide ve Semaglutide'in, yüksek riskli hastalarda majör advers kardiyovasküler olayları (MACE) anlamlı ölçüde azalttığı kanıtlandı.
- **2017 - Semaglutide (Ozempic) Onayı:** Haftada bir kez kullanılan semaglutide diyabet için onaylandı.
- **2021 - Semaglutide 2.4 mg (Wegovy) Onayı:** STEP programında sağlanan ortalama %14.9'luk devasa kilo kaybı sonrası obezite tedavisi için onaylandı.
- **2022 / 2023 - İkili Agonist Tirzepatide (Mounjaro ve Zepbound):** Hem GLP-1 hem de GIP reseptörlerini uyaran Tirzepatide, önce diyabet (2022) ardından da obezite (2023) için onaylandı. Obezite tedavilerinde bugüne kadar görülmemiş şekilde %22.5'e varan kilo kayıpları kayda geçti