---
Tür:
  - Besleyici
ODAK:
  - "[[Aralıklı Açlık]]"
  - "[[Kalori Kısıtlaması]]"
  - "[[Karaciğer Yağlanması]]"
MEKANİZMA:
  - "[[İnsülin Direnci]]"
  - "[[Lipotoksisite]]"
  - "[[Yağ Metabolizması]]"
DİZİN:
  - "[[00_İnsülin Direnci ve Tip 2 Diyabet_MOC]]"
  - "[[00_Lipotoksisite ve Ektopik Yağ Birikimi_MOC]]"
  - "[[00_Kalori Kısıtlaması ve Enerji Metabolizması_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
  - "[[Açlıkta Adipoz Doku Lipolizi - Adrenerjik Sinyal, TNF-TNFR1 Ekseni ve Sirkadiyen Zamanlama]]"
  - "[[Açlıkta Lipoliz, Ketogenez ve Substrat Partisyonu]]"
  - "[[Ektopik Yağ Birikiminin Doku-Organ ve Hastalık Bazlı Etkileri]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Açlıkta Lipoliz, Ketogenez ve Substrat Partisyonu]]"
  - "[[Düşük Kalorili Diyetlerde Hepatik ve Periferik İnsülin Direnci]]"
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
### İçindekiler

- [[#1. Hepatik DAG-PKCε Ekseni ve Proksimal İnsülin Sinyali]]
- [[#2. De Novo Lipogenez'in Kapanması ve Ketogenik Geçiş]]
- [[#3. İskelet Kasında Ektopik Lipid ve Yağ Asidi Oksidasyonu]]
- [[#4. Sistemik NEFA Havuzu — Dokular Arası Koordinasyonun Anahtarı]]
- [[#Kaynaklar]]

---

### 1. Hepatik DAG-PKCε Ekseni ve Proksimal İnsülin Sinyali

**Çıkarımım:** Duan et al. (2026)'nın bu bölümü, karaciğerin diğer dokulara (özellikle yağ dokusuna) kıyasla akut kalori kısıtlamasına şaşırtıcı derecede hızlı ve tam yanıt verdiğini gösteriyor. Bu beni, "insülin direnci" kavramının tek bir hastalık değil, her organın kendi eşiği ve kendi kurtarılma hızı olan, birbirinden bağımsız süreçlerin toplamı olduğu fikrine götürüyor — bkz. İnsülin Direnci.

#### Normal Fizyoloji

Karaciğerde insülin, reseptörü (InsR) üzerinden Akt fosforilasyonunu (Ser473/Thr308) tetikleyerek glikojen sentazı aktive eder (GSK3β fosforilasyonu üzerinden) ve glukoz/lipid metabolizmasını anabolik yöne çevirir. Diaçilgliserol (DAG), sağlıklı düşük düzeylerde bu sinyali bozmaz; ancak aşırı biriktiğinde yeni nesil Protein Kinaz C izoformlarını (karaciğerde PKCε) aktive ederek insülin reseptörünün kendisini fosforile edip sinyali doğrudan bloke edebilir.

#### Açlıkta Ne Değişir

8 haftalık yüksek yağlı diyet (HFD) ile obezleştirilen farelerde, insülin uyarılı Akt fosforilasyonu (hem Ser473 hem Thr308) belirgin şekilde baskılanmış, GSK3 fosforilasyonu ise daha hafif etkilenmiştir; bazal InsR Tyr1162 fosforilasyonu paradoksal şekilde yükselmiş ama insülin uyarısına yanıt kaybolmuştur. Bu tablo, hepatik TAG ve DAG birikimiyle ve PKCε'nin membran/sitozol oranındaki yaklaşık 2 kat artışla (aktivasyon göstergesi) paralel seyretmektedir. Yalnızca 3 günlük diyet değişimi (DS, HFD'den standart diyete geçiş, spontan %70 kalori azalması) bu tabloyu büyük ölçüde tersine çevirmiştir: Akt/GSK3 fosforilasyonu restore olmuş, PKCε membran translokasyonu geri dönmüş, bazal InsR fosforilasyonu kontrol düzeyine inmiş — ancak insüline yanıt olarak artışı yalnızca **kısmen** restore edilebilmiştir. Lipidomik düzeyde de ilginç bir ayrışma var: DAG türlerine göre kümeleme analizi DS grubunu CD (kontrol) grubuna yakın konumlandırırken, aynı analiz TAG ve seramid türleri için DS'i HFD grubuna daha yakın göstermektedir — yani "karaciğer CD'ye döndü" ifadesi lipid sınıfına göre doğru ya da yanlış olabilir; DAG-PKCε ekseni gerçekten normalize olurken, toplam TAG havuzu hâlâ yüksek kalmaktadır. Beklenmedik bir bulgu da eIF2α fosforilasyonunun (bütünleşik stres yanıtı göstergesi) DS ile **artmış** olmasıdır — yazarlar bunun, bu bağlamda ER stresinin tek başına insülin direnci yaratmaya yetmediğini gösterdiğini öne sürmektedir.

---

### 2. De Novo Lipogenez'in Kapanması ve Ketogenik Geçiş

**Çıkarımım:** Bu bölüm bana, "karaciğer eski (CD) haline dönüyor" varsayımının yanlış olduğunu gösteren en net kanıt gibi görünüyor — karaciğer DS sonrasında CD'nin bile _ötesine_ geçen, tamamen yeni bir katabolik profile kayıyor.

#### Normal Fizyoloji

De novo lipogenez (DNL), karbonhidrat fazlasının yeni yağ asitlerine (palmitat gibi) dönüştürülmesi sürecidir; FAS ve ACLY gibi enzimler bu süreci katalizler ve insülin sinyaliyle pozitif yönde ilişkilidir.

#### Açlıkta Ne Değişir

İlginç bir şekilde, HFD-beslenen insülin dirençli farelerde hepatik DNL hızı CD kontrolüyle **benzer** kalmıştır (lipojenik enzim ekspresyonu, özellikle FAS ve ACLY, sürdürülmüştür) — yani DNL, insülin direncinin klasik tablosuna uymayan, "seçici olarak korunmuş" bir yolaktır. Asıl dramatik değişim DS sonrasında ortaya çıkmıştır: DNL hızı hem erkek hem dişi farelerde neredeyse tamamen kapanmış, FAS/ACLY/SCD1 protein düzeyleri düşmüştür — yani DNL, HFD'nin kendisiyle değil, akut kalori kısıtlamasıyla baskılanmaktadır. Bununla eş zamanlı olarak plazma keton cisimleri (β-hidroksibutirat ve asetoasetat) belirgin şekilde artmış, _Fgf21_ mRNA ekspresyonu (metabolik bir "açlık sinyali" hormonu) çok anlamlı şekilde yükselmiştir. Proteomik analiz (5003 protein), mitokondriyal OXPHOS yolaklarının DS grubunda aslında **down-regüle** olduğunu göstermiştir — yani artan ketogenez, artan mitokondriyal solunum kapasitesinden değil, muhtemelen TCA döngüsü akışının azalıp karbonun ketogenez yönüne yönlendirilmesinden kaynaklanmaktadır. Bu üçlü tablo (DNL kapanması + keton artışı + azalan OXPHOS), karaciğerin "hasarlı bir anabolik durumdan sağlıklı bir eski duruma dönmek" yerine, "anabolik durumdan tamamen farklı, katabolik/ketojenik yeni bir duruma geçiş" yaptığını gösteriyor.

---

### 3. İskelet Kasında Ektopik Lipid ve Yağ Asidi Oksidasyonu

**Çıkarımım:** Kas dokusu bu üç doku (karaciğer, kas, yağ dokusu) arasında en "sorunsuz" olanı — HFD ile hiçbir zaman gerçek bir proksimal sinyal bozukluğu geliştirmiyor, yalnızca daha fazla insüline ihtiyaç duyar hale geliyor. Bu, İnsülin Direnci kavramının kas için karaciğerden farklı bir mekanizmayla (konsantrasyon-bağımlı, reseptör-bağımsız) tanımlanması gerektiğini gösteriyor.

#### Normal Fizyoloji

İskelet kası, insülin uyarılı toplam glukoz atılımının büyük çoğunluğundan (bu çalışmada yağ kütlesinin ~20 katı) sorumludur; InsR-Akt-AS160-GLUT4 ekseni glukozun hücre içine taşınmasını sağlar.

#### Açlıkta Ne Değişir

HFD-beslenen farelerde kasta proksimal insülin sinyal elemanlarında (InsR, Akt-Ser473/Thr308, AS160, GSK3β) anlamlı bir bozulma **gözlenmemiştir** — radyolabel 2-DOG ile ölçülen glukoz atılımı da HFD grubunda düşük çıkmış olsa da, ortam kan şekerine göre düzeltildiğinde ("adjusted glukoz alımı") üç grup arasında fark kalmamıştır. Yani kas dokusu obezitede gerçek bir moleküler direnç geliştirmemiş, yalnızca aynı glukoz atılımını sağlamak için daha yüksek dolaşımdaki insülin konsantrasyonuna ihtiyaç duyar hale gelmiştir. DS sonrasında bu ihtiyaç normalleşmiş, 2-DOG klirensi CD düzeyine dönmüştür. Kas dokusundaki tek kalıcı iz lipidomiktir: HFD ile biriken TAG ve DAG havuzları DS ile anlamlı ölçüde azalmış, ancak CD grubuna kıyasla hâlâ yüksek kalmıştır. Bu kısmi lipid temizliği, yağ asidi oksidasyonundaki (FAO) belirgin artışla örtüşmektedir — proteomik yolak analizleri, FAO'nun HFD ile zaten arttığını ve 3 günlük DS ile katlanarak daha da yükseldiğini göstermiştir; yani kas, tıpkı karaciğer gibi, DS sonrasında enerji kaynağını yağ asidi oksidasyonuna kaydırarak kendi ektopik lipid yükünü aktif olarak temizlemektedir.

---

### 4. Sistemik NEFA Havuzu — Dokular Arası Koordinasyonun Anahtarı

**Çıkarımım:** Bu son bölüm, yukarıdaki üç ayrı doku hikâyesini birbirine bağlayan "sistem mühendisliği" perspektifini sunuyor — her dokunun kendi başına yaptığı değişikliğin toplamı, dolaşımdaki tek bir ortak para birimi (NEFA) üzerinden vücut çapında bir insülin duyarlılığı restorasyonuna dönüşüyor.

#### Normal Fizyoloji

Serbest yağ asitleri (NEFA/FFA), yağ dokusundan lipoliz yoluyla salınıp karaciğer ve kasa taşınan, hem enerji substratı hem de (fazla olduğunda) lipotoksik bir sinyal molekülüdür. Kronik olarak yüksek NEFA, karaciğer ve kasta DAG/seramid birikimine ve dolayısıyla insülin direncine katkıda bulunur.

#### Açlıkta Ne Değişir

DS sonrasında ortaya çıkan tablo, [[#1. Lipolitik Kaskad — β3-AR → PKA → HSL-ATGL-Plin1|adipoz doku lipolizinin]] (bkz. ilgili not) **baskılanmış kalmasının** aslında sistemik iyileşmeye hizmet ettiğini gösteriyor: yağ dokusu kana yağ asidi pompalamayı durdurduğu (ADRB3/HSL/Plin1 defekti nedeniyle), karaciğer ve kas ise mevcut yağı hızla oksitlemeye başladığı için, plazma NEFA düzeyleri hızla düşmüştür. Bu, karaciğer ve kastaki "yağ zehirlenmesi" yükünü kaldırarak, DAG-PKCε ekseninin (karaciğerde) ve ektopik lipid birikiminin (kasta) hızla gerilemesini sağlamıştır. Bu perspektiften bakıldığında, yağ dokusunun "düzelmemesi" bir başarısızlık değil, aksine sistemin bir bütün olarak hızla yeniden dengeye gelmesini sağlayan işlevsel bir uyum olarak okunabilir. Ancak bu denge kronik obezitede (18 hafta HFD) bozulmaktadır: aynı büyüklükte bir akut kalori kısıtlaması (18 saat), HOMA-IR'yi yalnızca ~%50 düzeltebilmiş, sistemik insülin direnci tam olarak çözülememiştir — bu farkın altında, gWAT'ta biriken adiposit ölümü, makrofaj infiltrasyonu (crown-like structures) ve TNF-α yüksekliğinin akut kalori kısıtlamasına dirençli kalması yatmaktadır (bkz. Açlıkta Adipoz Doku Lipolizi - Adrenerjik Sinyal, TNF-TNFR1 Ekseni ve Sirkadiyen Zamanlama). Yani sistemin bu "acil durum freni" mekanizması, yalnızca obezitenin henüz kronik enflamatuar hasara dönüşmediği erken/orta evrede tam kapasiteyle çalışabiliyor gibi görünmektedir.

---

### Kaynaklar

- Duan, X., Davis, L. M., Patel, S., et al. (2026). Integrated analysis of insulin resistance reveals metabolic remodeling following diet switch–triggered calorie reduction. _Science Advances_, 12(19), eaed0535. [https://doi.org/10.1126/sciadv.aed0535](https://doi.org/10.1126/sciadv.aed0535)