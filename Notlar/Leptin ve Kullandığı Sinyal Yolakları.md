---
Tür:
  - Besleyici
ODAK:
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Besin Ögelerinin Leptin Sinyalizasyonundaki Etkileri]]"
  - "[[Obezitenin Beyinsel-Merkezi Olarak Düzenlenmesi]]"
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

Adipoz Doku Obezite Leptin Enerji Harcaması 
1) Leptin'in Etkilerini Göstermek İçin Kullandığı Sinyal Yolakları:

Leptin, biyolojik etkilerini temel olarak leptin reseptörüne (LepR veya ObRb) bağlanarak gösterir. Bu reseptör, sitokin reseptör süper ailesine aittir. Leptin'in etkilerini aracılık ettiği başlıca sinyal yolakları şunlardır:

JAK2/STAT3 Yolağı: Bu, leptin reseptörü aktivasyonundan sonraki birincil sinyal mekanizmasıdır. Hipotalamusta, leptin reseptörünün uzun izoformuna bağlanarak Janus kinaz 2'yi (JAK2) trans-fosforilasyon yoluyla aktive eder. Bu aktivasyon, leptin reseptörünün hücre içi alanındaki çeşitli tirozin kalıntılarının (özellikle Y985, Y1077 ve Y1138) fosforilasyonuna yol açar ve sinyal dönüştürücü ve transkripsiyon aktivatörü (STAT) proteinlerinin (özellikle STAT3 ve STAT5) toplanmasını sağlar. 

	STAT3 aktivasyonu, pro-opiomelanokortin (POMC) ekspresyonunu artırırken, neuropeptit Y (NPY) ekspresyonunu azaltır, bu da enerji homeostazının sürdürülmesi ve vücut ağırlığı düzenlemesi için kritik öneme sahiptir.

	STAT5 aktivasyonu, hipotalamik nöronlarda iştahı baskılar ve obezitenin önlenmesinde önemli bir rol oynar.

	Bu yolak aynı zamanda sitokin sinyalizasyonunu baskılayan protein 3 (SOCS3) gibi negatif düzenleyicilerin transkripsiyonel indüksiyonuna da yol açar

IRS/PI3K/Akt Yolağı: JAK2 aktivasyonu, insülin reseptör substratını (IRS) fosforilasyonunu teşvik eder. Bu da fosfatidilinozitol 3-kinazı (PI3K) ve ardından protein kinaz B'yi (PKB/Akt) aktive eder.

	Aktive edilmiş Akt, transkripsiyon faktörü FoxO1'i çekirdekten uzaklaştırarak NPY ve agouti-related peptide (AgRP) ile ilişkili FoxO1-aracılı uyarımı inhibe ederken, POMC ekspresyonunu destekler.


	Bu yolak ayrıca memeli rapamisin hedefini (mTOR) aktive eder, bu da enerji dengesi ve metabolik düzenlemede önemli bir rol oynar.


	Leptin, hipotalamusta PI3K yoluyla fosfodiesteraz 3B (PDE3B) ekspresyonunu da indükler.

Diğer Sinyal Yolakları: Leptin reseptörü, uyarım üzerine IRS'nin yanı sıra Src homoloji 2-içeren tirozin fosfataz 2 (SHP2) ve AMP-aktive protein kinazı (AMPK) gibi moleküler varlıkların aktivasyonunu da sağlar. Bu da sırasıyla SHP2/MAPK/ERK1/2 yolağını ve AMPK yolağını başlatır. Bu yolaklar, hipotalamik POMC popülasyonundaki nöronlar gibi leptine duyarlı nöronları hedefleyerek gıda alımını azaltır ve enerji harcamasını artırır. Periferik düzeyde ise IRS/PI3K/Akt yolağı, izole hepatositlerde glikoz metabolizmasını düzenler, hepatik yağ birikimini ve glikojen sentezini azaltır
