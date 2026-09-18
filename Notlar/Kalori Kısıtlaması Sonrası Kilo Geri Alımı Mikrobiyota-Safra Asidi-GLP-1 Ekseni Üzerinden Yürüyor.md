---
Tür:
  - Besleyici
ODAK:
  - "[[Kilo Döngüsü ve İmmün Hafıza]]"
MEKANİZMA:
  - "[[Disbiyozis]]"
BAĞLANTILI NOTLAR:
  - "[[Mikrobiyota ve Kişiselleştirilmiş Beslenme]]"
  - "[[Adipose Specific Control of Thermogenesis]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[weight-cycling-glp1-cycling-perspektif-taslak]]"
BAĞLANTILI DERSLER:
  - "[[BES339 Diyet İlkeleri ve Popüler Diyetler]]"
  - "[[BES326 İmmün Sistem ve İmmünonutrisyon]]"
YORUM: MetaboLights taramasında bulundu (2026-08). CR sonrası hızlı kilo geri alımının mikrobiyota-safra asidi-GLP-1 ekseni üzerinden yürüdüğünü ve bunun bir probiyotik/safra asidi müdahalesiyle yavaşlatılabildiğini gösteren, weight-cycling/GLP-1-cycling perspektifi için doğrudan mekanistik destek.
KAYNAK: https://doi.org/10.1038/s41467-022-29589-7 (Li et al., Nature Communications, 2022) — MetaboLights: https://www.ebi.ac.uk/metabolights/MTBLS4431
study_type: "Fare çalışması (metabolomik + metagenomik)"
evidence_direction: "positive"
primary_outcome: "Kalori kısıtlaması sonrası kilo geri alım hızı/büyüklüğü, safra asidi profili, BAT UCP1, serum GLP-1"
p_value_summary: "belirtilmedi (özet düzeyinde; makalede ayrıntılı istatistik mevcut)"
BESLEDİĞİ NOTLAR:
  - "[[Kilo Döngüsü ve İmmün Hafıza]]"
  - "[[GLP-1 Kullanımından Sonra Ağırlık Kazanımı]]"
  - "[[Catch-up Fat- Yağ Yakalama Fenotipi]]"
DİZİN:
  - "[[Kilo Döngüsü]]"
ETİKET: makaleden

---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Kalori Kısıtlaması (CR)"] --> B["Bağırsak Mikrobiyota Kompozisyonunun Değişimi (↑Firmicutes/Bacteroidetes, ↓P. distasonis)"]
>     B --> C["↓Non-12α-OH Safra Asitleri (UDCA, LCA)"]
>     C --> D["↓BAT UCP1 Ekspresyonu ve ↓Serum GLP-1"]
>     D --> E["Serbest Beslenmeye Dönüşte (Refeeding) Hızlı Kilo Geri Alımı"]
>     F["Müdahale: P. distasonis Takviyesi VEYA Non-12α-OH Safra Asidi Takviyesi"] --> G["↑Termogenez"]
>     G -.->|"Geri Alımı Yavaşlatır"| E
> ```
>
> **Şekil Açıklaması:** CR, mikrobiyotayı HFD'ye benzer şekilde yeniden şekillendiriyor ve P. distasonis'i azaltıyor; bu da safra asidi profilini (özellikle termojenik sinyal veren non-12α-OH safra asitlerini) düşürüyor. Refeeding fazında bu eksik sinyal, BAT termogenezini ve GLP-1'i düşük tutarak hızlı kilo geri alımına zemin hazırlıyor — ama dışarıdan P. distasonis veya eksik safra asidi verilirse bu döngü kırılabiliyor.

### 1. Araştırma Tasarımı

- **Gruplar:** Kontrol (chow), Yüksek Yağlı Diyet (HFD), Kalori Kısıtlaması (CR).
- CR sonrası hayvanlar serbest beslenmeye (**refeeding/rebound fazı**) geçiriliyor ve bu fazda **boylamsal örnekleme** yapılıyor (MetaboLights Factors: diet, timepoint).
- Rebound fazında iki ayrı **müdahale kolu** test ediliyor: (i) *Parabacteroides distasonis* takviyesi, (ii) non-12α-hidroksile safra asidi (UDCA/LCA tipi) takviyesi — bunlar tedavisiz rebound grubuyla karşılaştırılıyor.
- Örneklem: n=252 (serum, feçes, karaciğer dokusu), LC-MS hedefli metabolomik + metagenomik.

### 2. Öne Çıkan Bulgular

- CR ve HFD, mikrobiyotayı **benzer yönde** yeniden şekillendiriyor (artmış Firmicutes/Bacteroidetes oranı) — yani "az yemek" ile "kötü yemek" mikrobiyota düzeyinde benzer bir imza bırakıyor.
- *Parabacteroides distasonis*, hem CR hem HFD sonrası en belirgin şekilde azalan tür; bu bakteri sekonder safra asidi üretiminde (özellikle non-12α-OH tipte) kritik.
- CR sırasında non-12OH safra asitleri (UDCA, LCA) belirgin azalıyor. Serbest beslenmeye dönüşte ise **12α-OH safra asitleri** (yağ emilimini kolaylaştıran tip) ve enerji-hasadı-verimli bakteriler artıyor — yani mikrobiyota refeeding'de "yağ depolamaya" optimize bir profile kayıyor.
- Kilo-geri-alan (rebound) farelerde BAT'ta UCP1 ekspresyonu düşük, serum GLP-1 düşük.
- **Kilo geri alım hızı/büyüklüğü doğrudan ölçülmüş ve gruplar arası karşılaştırılmış:** P. distasonis veya non-12α-OH safra asidi takviyesi alan gruplarda, artmış termogenez yoluyla kilo geri alımı **iyileşmiş** (yavaşlamış/azalmış) — tedavisiz rebound grubuna kıyasla.

### 3. Neden Not Aldık / Nasıl Kullanılabilir

Bu çalışma [[weight-cycling-glp1-cycling-perspektif-taslak]] fikrine iki açıdan doğrudan malzeme sağlıyor:

1. **Mekanistik köprü:** Klasik weight cycling (CR-kaynaklı) ile GLP-1 cycling (ilaç kesilmesi kaynaklı) arasında iddia ettiğin paralelliğin somut bir moleküler ortak paydası burada gösteriliyor — **her iki senaryoda da düşen endojen/sistemik GLP-1 ve mikrobiyota-safra asidi ekseni bozulması, kilo geri alımının merkezinde**. Bu, "iki farklı tetikleyici (diyet kısıtlaması vs ilaç kesilmesi), ortak bir mikrobiyota-aracılı mekanizmaya çıkıyor" tezini destekleyen doğrudan bir kaynak.
2. **Güncel paralel literatür (2026):** Bu çalışmanın CR bağlamındaki bulgusuyla neredeyse birebir örtüşen, ama GLP-1RA kesilmesi bağlamında yapılmış çok yeni çalışmalar var — *Limosilactobacillus fermentum* GB102 probiyotiğinin dulaglutid kesilmesi sonrası geri alımı azalttığı (2026, PubMed 41978101) ve semaglutid-kaynaklı disbiyozun kesim-sonrası geri alımı yönettiği, lif takviyesinin bunu hafiflettiği (medRxiv, 2026) çalışmaları. **MTBLS4431, bu güncel GLP-1-kesilmesi literatürünün "atası" niteliğinde** — aynı mekanizmanın (mikrobiyota→safra asidi/SCFA→termogenez/GLP-1 ekseni) daha önce CR bağlamında gösterilmiş hali.

Pratik kullanım: Weight-cycling makalende "kas kaybı ve mikrobesin yetersizliği" eksenine ek olarak, **"mikrobiyota-aracılı termogenik/insretin sinyal kaybı"** başlığı altında ayrı bir alt-bölüm açılabilir; bu bölümde MTBLS4431 (CR modeli) ile GB102/medRxiv çalışmaları (GLP-1RA modeli) yan yana konularak iki cycling türünün ortak mekanizması somut olarak gösterilebilir.
