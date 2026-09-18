---
Tür:
  - Besleyici
ODAK:
  - "[[Solunum Katsayısı]]"
MEKANİZMA:
DİZİN:
  - "[[Metabolizma]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Sistemik Enerji Metabolizması — Hepatik Substrat Seçimi, Ketogenez ve Tiroid-Metabolik Hız Ekseni]]"
  - "[[Enerji Harcamasının Bileşenleri]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Kas Proteolizi ve Substrat Partisyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Enerji Dengesinin Bileşenleri]]"
  - "[[Enerji Harcamasının Bileşenleri]]"
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

Bir kişinin hangi enerji kaynağını (yağ, protein veya depolanmış karbonhidrat) kullandığını gösteren bir ölçümdür. RQ, metabolik ihtiyaçlar değiştiğinde (örneğin açlık, diyet veya egzersiz sırasında) yakıt oksidasyonundaki değişiklikleri ifade eden **metabolik esneklik** ile ilişkilidir.

Kullanım: Yüksek karbonhidratlı diyetler daha yüksek RQ'ya yol açabilirken, ketojenik diyetler yağ oksidasyonunu maksimize eden RQs değerleri gösterebilir. Gıda güvensizliği ve düzensiz yemek yeme alışkanlıkları da daha yüksek RQ ile ilişkilendirilmiştir, bu da karbonhidrat kullanımının daha fazla olduğunu gösterir. Araştırmalar, daha yüksek RQ'nun zamanla daha fazla kilo alımıyla ilişkili olduğunu göstermektedir, çünkü bu kişiler yağı yakıt kaynağı olarak mümkün olduğunca kullanmazlar. Amaç, yağ oksidasyonunu optimize etmek ve kas kütlesini korumaktır, bu da daha düşük RQ değerleriyle ilişkilendirilen bir diyet gerektirir. El cihazlarıyla karbondioksit üretimini ölçerek RQ geri bildirimi sağlamanın kilo kaybı ve glisemik kontrolü iyileştirdiği gösterilmiştir.
