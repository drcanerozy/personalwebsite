---
Tür:
  - Besleyici
ODAK:
  - "[[Ultra İşlenmiş Besinler]]"
MEKANİZMA:
  - "[[Disbiyozis]]"
BAĞLANTILI NOTLAR:
  - "[[Obesojenler]]"
  - "[[UPF Üretimi, Pazarlaması ve Tüketimine Yönelik Politikalar]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[nova-grup4-nutrient-adjustment-calisma-plani]]"
BAĞLANTILI DERSLER:
  - "[[BES339 Diyet İlkeleri ve Popüler Diyetler]]"
YORUM: MetaboLights taramasında bulundu (2026-08). NOVA Grup 4 içindeki bir katkı maddesinin, besin matriksinden tamamen bağımsız ve tek başına (in vitro mini-biyoreaktör + in vivo fare + çocuk feçes verisi) metabolik bozukluk yarattığını gösteren nadir çok-katmanlı bir çalışma.
KAYNAK: https://www.ebi.ac.uk/metabolights/MTBLS14529
study_type: "Multi-katmanlı (in vitro insan mikrobiyota reaktörü + in vivo fare + insan gözlemsel feçes)"
evidence_direction: "positive"
primary_outcome: "Cinsiyete bağımlı glukoz intoleransı ve mikrobiyota disbiyozu"
p_value_summary: "belirtilmedi (özet düzeyinde)"
BESLEDİĞİ NOTLAR:
  - "[[UPF Sınıflandırma Yöntemleri ve Aralarındaki Tutarsızlıklar]]"
  - "[[UPF Tüketimi Metabolitlerle Belirlenebilir Mi?]]"
DİZİN:
  - "[[Gıda Katkı Maddeleri]]"
ETİKET: makaleden

---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Gıda-sınıfı TiO2 (fg-TiO2), Katkı Maddesi"] --> B["Bağırsak Mikrobiyota Yapısının Yeniden Şekillenmesi"]
>     B --> C["İmmün Sinyalizasyonla İlişkili Taksonların Etkilenmesi"]
>     C --> D["Erkek Farelerde Cinsiyete-Özgü Glukoz İntoleransı, Artmış Açlık İnsülini ve HOMA-IR"]
>     D --> E["Yüksek Yağlı Diyet (HFD) Altında Hepatik/Metabolik/Bağırsak Bariyeri Bozulmasının Şiddetlenmesi"]
>     F["Fekal Mikrobiyota Transferi (FMT) → Germ-Free Fare"] --> D
> ```
>
> **Şekil Açıklaması:** Gıda-sınıfı TiO2, besin matriksinden ve toplam kalori/makro besin içeriğinden bağımsız olarak, doğrudan bağırsak mikrobiyotasını yeniden şekillendiriyor; bu değişim FMT ile germ-free farelere aktarıldığında glukoz intoleransını da birlikte taşıyor — yani etkinin mikrobiyota-aracılı ve nedensel olduğu gösterilmiş.

### 1. Araştırma Tasarımı

Üç katmanlı bir tasarım kullanılmış:
- **In vitro:** Sağlıklı donörlerden alınan feçes mikrobiyotasıyla aşılanmış MiniBioReactor Array sistemleri, gıda-sınıfı (food-grade, fg) TiO2'ye maruz bırakılmış.
- **İnsan gözlemsel:** Normal kilolu ve obez çocuklardan alınan feçes örneklerinde titanyum düzeyi ve mikrobiyota-kaynaklı belirteçler ölçülmüş.
- **In vivo (fare):** Gebelikten yetişkinliğe kadar, insan diyetindeki dozlara eşdeğer fg-TiO2 maruziyeti, standart veya yüksek yağlı diyet (HFD) ile birlikte uygulanmış; ardından fekal mikrobiyota transferi (FMT) ile germ-free farelere aktarım yapılarak nedensellik test edilmiş.

### 2. Öne Çıkan Bulgular

- fg-TiO2, in vitro insan mikrobiyota yapısını yeniden şekillendirmiş; immün sinyalizasyonla ilişkili taksonlar tutarlı şekilde etkilenmiş.
- Obez çocuklarda normal kilolulara kıyasla feçeste daha yüksek titanyum seviyesi saptanmış; bu düzey feçes flagellin (mikrobiyota-kaynaklı bir disbiyoz belirteci) ile korelasyon göstermiş.
- Yaşam boyu fg-TiO2 maruziyeti, erkek farelerde cinsiyete-özgü disbiyoz ve glukoz metabolizması bozulmasına (artmış açlık insülini, HOMA-IR, pro-inflamatuar feçes belirteçleri) yol açmış.
- FMT deneyi, TiO2 ile değişmiş mikrobiyotanın tek başına glukoz intoleransını germ-free farelere aktarmaya yettiğini göstererek **nedenselliği** kanıtlamış.
- HFD altında fg-TiO2, hepatik/metabolik/bağırsak bariyeri bozulmalarını şiddetlendirmiş.

### 3. Neden Not Aldık / Nasıl Kullanılabilir

Bu çalışma, [[nova-grup4-nutrient-adjustment-calisma-plani]] fikrinin merkezindeki soruya ("NOVA Grup 4 içindeki bir katkı maddesi kozmetik mi yoksa kritik mi") **doğrudan ve nedensel düzeyde kanıt** sağlıyor: besin kompozisyonu (kalori, makro besin, lif vb.) tamamen sabit tutulmasa bile, tek bir katkı maddesi (burada beyazlatıcı/opaklaştırıcı ajan TiO2), matriksten bağımsız olarak, mikrobiyota üzerinden metabolik bozukluk yaratabiliyor — ve bu FMT ile ispatlanmış.

Pratik kullanım alanları:
- **Atıf/vaka örneği** olarak: "kozmetik katkı = zararsız" varsayımının literatürde çürütüldüğü somut bir örnek olarak nutrient-adjustment çalışma planının giriş/gerekçe bölümünde kullanılabilir.
- **Metodolojik şablon** olarak: senin planladığın ayrıştırma çalışmasında "matriksten bağımsız katkı etkisi"ni test etmek için benzer bir FMT/germ-free doğrulama adımı örnek alınabilir.
- Bu çalışma MetaboLights'a sadece **feçes NMR metabolomiği** (fare) yüklemiş; katkı maddesinin kendisinin veya insan örneklerinin ham metabolomik verisi mevcut değil — yani doğrudan reanaliz konusu değil, kavramsal/atıf kaynağı olarak değerli.
