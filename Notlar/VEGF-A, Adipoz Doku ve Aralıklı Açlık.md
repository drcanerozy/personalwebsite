---
Tür:
  - Besleyici
ODAK:
  - "[[Adipoz Doku]]"
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[VEGF-A]]"
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Review / Mechanistic"
evidence_direction: "positive"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Aralıklı Açlık, Adipoz Dokudaki Nöral ve Vasküler Ağları Yeniden Modelliyor]]"
  - "[[Adipoz Doku Endokrin Fonksiyonu ve Dinamikleri]]"
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

**1. Yağ Dokusunun Kahverengileşmesi (Browning) ve Termojenez** IF, viseral beyaz yağ dokusunda VEGF-A ekspresyonunu uyarır ve bu artış, yağ dokusunun "kahverengileşmesine" (beiging/browning) yol açar. Bu süreçte _Adrb3, Ppargc1a, Cidea_ ve _Ucp1_ gibi termojenik genlerin yukarı regülasyonu (upregulation) gerçekleşir. Bu kahverengileşme etkisi, enerji harcamasının artmasına, glikoz toleransının iyileşmesine ve insülin duyarlılığının artmasına katkıda bulunur.

**2. M2 Tipi Makrofaj Polarizasyonu** VEGF-A aracılı kahverengileşme mekanizması, bağışıklık hücrelerinin modülasyonuna bağlıdır. IF ile artan VEGF-A, yağ dokusundaki makrofajların anti-enflamatuar özellik gösteren **M2-benzeri fenotipe** polarize olmasını sağlar (_Clec10a, Il10_ ve _Ym1_ artışı ile karakterizedir). Bu immün hücre değişimi, yağ dokusunun metabolik homeostazı ve yeniden şekillenmesi için gereklidir.

**3. Anjiyogenez ve Endotelyal Crosstalk (Hücreler Arası İletişim)** VEGF-A, yağ dokusunda anjiyogenezi (yeni kan damarı oluşumu) teşvik eder. Bu süreçte adipositler ve endotel hücreleri arasında kritik bir etkileşim gerçekleşir:

• VEGF-A, endotel hücrelerini uyararak **Trombosit Kaynaklı Büyüme Faktörü CC'nin (PDGF-CC)** salınmasını sağlar.

• Endotel kaynaklı bu PDGF-CC, adiposit progenitör hücrelerinin "bej" (beige) fenotipe farklılaşmasını teşvik eder.

• Bu mekanizma, IF'nin damarlanmayı artırarak yağ dokusunun besin ve oksijen ihtiyacını karşılamasına ve metabolik atıkların uzaklaştırılmasına yardımcı olduğunu gösterir.

**4. Sempatik Sinir Büyümesi ve Lipoliz** VEGF-A'nın yağ dokusundaki sempatik sinir büyümesini (innervasyon) teşvik ettiği ve bu yolla lipolizi (yağ yıkımı) artırdığı öne sürülmektedir. VEGF-A aşırı ekspresyonunun, sempatik sinirleri büyüterek beta-3 adrenerjik reseptör (ADRB3) aktivasyonuna ve hormona duyarlı lipazın (HSL) fosforilasyonuna yol açtığı, bunun da termojenezi ve enerji harcamasını artırdığı belirtilmektedir.

**Moleküler Düzenleyiciler** Bu sürecin, karaciğerden salgılanan FGF21 ve yağ dokusundaki AMPK-SIRT1-PGC1α sinyal ekseni tarafından yukarı akışta (upstream) düzenlendiği ve VEGF-A üretimini tetiklediği düşünülmektedir

