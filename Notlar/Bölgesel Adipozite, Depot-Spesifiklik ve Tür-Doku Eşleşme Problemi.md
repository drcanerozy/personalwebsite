---
Tür:
  - Besleyici
ODAK:
  - "[[Adipoz Doku]]"
MEKANİZMA:
DİZİN:
  - "[[00_Adipoz Doku ve Metabolizma_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Adipoz Doku Lipolizi]]"
  - "[[Ektopik Yağ Birikiminin Doku-Organ ve Hastalık Bazlı Etkileri]]"
  - "[[BKİ Yerine Adipozite Bazlı Sınıflandırma Hastalık Riski ile Daha Fazla İlişkili]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[AD Alt Popülasyonlarının Önemi-Obezitedeki Etkisi]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Adipoz Doku Endokrin Fonksiyonu ve Dinamikleri]]"
  - "[[Ektopik Yağ Birikiminin Doku-Organ ve Hastalık Bazlı Etkileri]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Besin Kısıtlaması (Fasting / FMD)"] --> B["İnsülin / IGF-1 Düşüşü & AMPK Artışı"]
>     B --> C["mTORC1 İnhibisyonu & ULK1 Aktivasyonu"]
>     C --> D["Hücresel Otofaji / Mitofaji (Organel Temizliği)"]
>     B --> E["Hepatik Glikojen Boşalması → Ketogenez (Beta-Hidroksibütirat)"]
> ```
>
> **Şekil Açıklaması:** Besin kısıtlaması ve açlık durumunda düşen insülin/IGF-1 ve yükselen AMPK, mTORC1'i inhibe edip ULK1'i aktive ederek hücresel otofaji ve mitofaji (hasarlı organel temizliği) süreçlerini başlatır; eş zamanlı olarak hepatik glikojenin boşalmasıyla ketogenez (Beta-hidroksibütirat üretimi) devreye girer.

### İçindekiler

- [[#Fare Modellerinde Depot-Spesifik CR Yanıtı]]
- [[#İnsan-Fare Doku Eşleşmesi Problemi]]
- [[#Çapraz Tema Depot Seçiminin Tür Farkı Bulgularını Ne Kadar Etkilediği]]
- [[#Genel Değerlendirme]]
- [[#Bibliyografya]]

---

### Fare Modellerinde Depot-Spesifik CR Yanıtı

"Yağ dokusu" tekil bir organ gibi konuşulsa da, aslında farklı anatomik konumlarda farklı gelişimsel kökene ve metabolik davranışa sahip depoların toplamıdır. Suchacki et al. (2023), bu heterojenliğin CR yanıtını nasıl derinden şekillendirdiğini gösteriyor.

**Normal Fizyoloji:** Beyaz yağ dokusu depoları — gonadal (gWAT), inguinal (iWAT), mezenterik (mWAT), perirenal (pWAT) ve pericardial (pcWAT) — anatomik konum, gelişimsel köken ve metabolik/endokrin profil bakımından birbirinden ayrışır; kahverengi yağ dokusu (BAT) ise termojenik işleviyle beyaz depolardan tamamen farklı bir kategoridir.

**Açlıkta Ne Değişir:** Genç farelerde CR, erkeklerde gWAT, iWAT, mWAT ve pWAT'ın hem mutlak hem göreceli (vücut ağırlığına oranlı) kütlesini azaltıyor; dişilerde bu kayıp görülmüyor. BAT'ta ise yalnızca mutlak kütle erkeklerde azalıyor, göreceli kütle CR'den etkilenmiyor. Bu depo-bazlı ayrışma, kaybın en belirgin olduğu depoların **visseral ağırlıklı** (gonadal, mezenterik, perirenal) depolar olduğunu gösteriyor — bu, insan CALERIE verisiyle de örtüşen bir tema (kadınlar erkeklere kıyasla gövde/trunk yağ kaybına direnç gösteriyor). Yaşlı farelerde ise bu depo-bazlı cinsiyet ayrışması ortadan kalkıyor — CR her iki cinsiyette de WAT depolarını benzer oranda küçültüyor; bu, Bireysel ve Metodolojik Modülatörler notunda ele alınan yaşlanma-bağımlı dimorfizm kaybının depo düzeyindeki yansıması.

---

### İnsan-Fare Doku Eşleşmesi Problemi

**Normal Fizyoloji:** İnsan çalışmalarında "subkutan yağ dokusu" genellikle periumbilikal/abdominal bölgeden biyopsi ile örneklenir. Fare çalışmalarında ise "visseral" depo olarak epididimal yağ dokusu, "subkutan" depo olarak da genellikle inguinal yağ dokusu kullanılır.

**Açlıkta Ne Değişir (Metodolojik Uyarı):** Defour et al. (2020), kendi çalışmasının en önemli sınırlılığı olarak şunu vurguluyor: insan **subkutan (periumbilikal)** dokusuyla fare **epididimal (visseral)** dokusunu karşılaştırmışlar — ama insan subkutan dokusuna doğrudan karşılık gelen bir fare deposu **yok**. Fare çalışmalarında "subkutan" terimi genellikle inguinal depoyu ifade eder, ki bu depo hem epididimal hem de insan subkutan dokusundan farklı bir biyolojiye sahiptir — özellikle soğuğa-bağlı kahverengileşmeye (browning) çok daha duyarlıdır (van der Lans et al. 2013; Seale et al. 2011). Üstelik yazarlar, başka bir çalışmaya (Tang et al. 2017) atıfla, _Pnpla2, Lipe, Srebf1_ ve _Ppara_ gibi genlerin açlık yanıtının **fare içinde bile** farklı yağ depoları arasında değişebildiğini belirtiyor.

---

### Çapraz Tema: Depot Seçiminin Tür Farkı Bulgularını Ne Kadar Etkilediği

Bu iki bulgu bir araya geldiğinde önemli bir metodolojik soru doğuyor: Yağ Dokusu Transkriptomik Reprogramlanması notunda ele alınan insan-fare **tür farkları** (örn. PPAR sinyali, insülin sinyali, PCK1 yönü), gerçekten türe mi özgü, yoksa kısmen **karşılaştırılan depoların farklı olmasının** bir yapay ürünü mü? Defour'un kendisi bu ihtimali dışlayamadığını açıkça yazıyor. Bu, derlemenin "Fasting Is Not One Thing" temasına doğrudan bir metodolojik boyut ekliyor: depot-spesifiklik yalnızca _bir_ türün içinde farklı sonuçlar üretmekle kalmıyor, aynı zamanda türler-arası karşılaştırmaların güvenilirliğini de sorguluyor. Pratik sonucu şu: bir bulgunun "insan-fare arası farklı" olarak sunulduğu her yerde, karşılaştırılan depoların gerçekten homolog olup olmadığını kontrol etmek gerekiyor — Suchacki'nin genç-yaşlı karşılaştırması aynı depo içinde yapıldığı için bu sorundan bağımsız, ama Defour'un tür karşılaştırması bu sorunla doğrudan yüzleşiyor.

---

### Genel Değerlendirme

Depot-spesifiklik ekseninde bu iki kaynak tamamlayıcı ama farklı sorulara odaklanıyor: Suchacki **aynı tür içinde** (fare) depolar-arası ve cinsiyetler-arası ayrışmayı gösteriyor; Defour ise **türler-arası** karşılaştırmanın depo-eşleşmesi sorunuyla nasıl karıştığını gösteriyor. Protokol tipi ekseninde: Suchacki'nin 6 haftalık CR'si depot-bazlı kütle kaybını ölçebilecek kadar uzun; Defour'un 16-26 saatlik akut açlığı ise yalnızca transkriptomik düzeyde bir anlık görüntü sunuyor — depo kütlesi değişimi bu kısa süre içinde henüz ölçülebilir düzeyde olmayabilir, dolayısıyla bu iki çalışmayı "depot yanıtının zaman dinamiği" ekseninde karşılaştırmak için elimizde yeterli veri yok. Yaş ekseninde yalnızca Suchacki veri sunuyor (genç vs. yaşlı fare) ve depot-bazlı cinsiyet farkının yaşlanmayla kaybolduğunu gösteriyor. Tür ekseninde ise asıl mesaj metodolojik: gelecekte okunacak her insan-fare karşılaştırmalı çalışmada, karşılaştırılan depoların gerçek homoloğu olup olmadığı mutlaka kontrol edilmeli — aksi halde "tür farkı" olarak sunulan bir bulgu aslında "depo farkı" olabilir.

---

### Bibliyografya

- Suchacki KJ, Thomas BJ, Ikushima YM, et al. (2023). The effects of caloric restriction on adipose tissue and metabolic health are sex- and age-dependent. _eLife_ 12:e88080.
- Defour M, Michielsen CCJR, O'Donovan SD, Afman LA, Kersten S. (2020). Transcriptomic signature of fasting in human adipose tissue. _Physiological Genomics_ 52:451–467.