---
Tür:
  - Çekirdek
ODAK:
  - "[[Adipoz Doku]]"
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[Adipokinler]]"
  - "[[Leptin]]"
DİZİN:
  - "[[00_Adipoz Doku ve Metabolizma_MOC]]"
  - "[[00_Obezite Fenotipleri ve Bireysel Farklılıklar_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Açlıkta Akut Faz Yanıtı ve İmmün Modülasyon]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Review / Mechanistic"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "p < 0.0001"
BESLEDİĞİ NOTLAR:
  - "[[Adipoz Doku]]"
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

> **Metodolojik Etiketler:** #finding/contradictory
### İçindekiler

- [[#Giriş — Yağ Dokusu Bir Salgı Bezi Olarak]]
- [[#Normal Fizyoloji — Adipokinlerin Enerji Durumunu Sinyalize Etmesi]]
- [[#Açlıkta Ne Değişir — Leptin Düşüşü ve Serpin Dinamikleri]]
- [[#Serpin F1- Adipoz-Karaciğer Ekseninde Şaşırtıcı Bir Aracı]]
- [[#Adipoziteye Göre Ayrışan Adipokin Yanıtları]]
- [[#Kişisel Notlarım]]

---

### Giriş — Yağ Dokusu Bir Salgı Bezi Olarak

Adipoz Doku, yalnızca bir enerji deposu değil, dinamik bir endokrin organdır. Bu not, Rossmeislova et al. (2024)'ün insan adipoz doku eksplant verisini ve Stefanakis et al. (2024)'ün leptin-replasman proteomik verisini birleştirerek, açlık-tokluk döngüsünde adipokin salgılanmasının nasıl yeniden şekillendiğini ele alıyor.

---

### Normal Fizyoloji — Adipokinlerin Enerji Durumunu Sinyalize Etmesi

Leptin, adiposit kütlesiyle orantılı salgılanan ve hipotalamusa "enerji yeterli" sinyali gönderen ana adipokindir. Adiponektin, CTRP3 ve kompleman faktör D (CFD) gibi diğer moleküller, lipid opsonizasyonu ve alternatif kompleman aktivasyonunda rol oynayarak Adipoz Doku metabolizması ile doğuştan bağışıklık arasında bir köprü kurar. ANGPTL4, lipoprotein lipazı inhibe ederek diyetsel yağın adipoz dokuya alımını düzenler; serpinler (SERPINA6, SERPINA7, Serpin F1/PEDF) ise hem hormon taşıyıcı hem de lipoliz/anjiyogenez düzenleyici işlevler görür.

---

### Açlıkta Ne Değişir — Leptin Düşüşü ve Serpin Dinamikleri

Açlıkla leptin düşer — bu, Açlıkta Akut Faz Yanıtı ve İmmün Modülasyon notunda ele alındığı gibi, leptinin akut faz yanıtını tetikleyici etkisinin tersine işleyen bir süreçtir. Rossmeislova et al. (2024)'te, kan leptin düzeyleri açlıkla düşerken, ANGPTL4 (fasting-sinyaline duyarlı bir gen) her iki adiposite grubunda da artıyor ve toklukla normalleşiyor — ama bu yanıtın _büyüklüğü_ obez kadınlarda daha sönük, muhtemelen daha düşük açlık-FFA seviyelerinin ANGPTL4 ekspresyonunu daha az tetiklemesinden kaynaklanıyor. Adiponektin ve CTRP3 ise beklenmedik biçimde açlıktan toklukla birlikte istikrarlı biçimde _azalıyor_ — bu, klasik "açlıkta adiponektin artar" varsayımını doğrulamıyor.

---

### Serpin F1: Adipoz-Karaciğer Ekseninde Şaşırtıcı Bir Aracı

Bu iki çalışmadan çıkan en dikkat çekici ortak tema serpinler. Rossmeislova et al. (2024)'te, Serpin F1 (PEDF, aynı zamanda bir ATGL ko-aktivatörü), açlık-tokluk döngüsüne zayıf ve obez kadınlar arasında **istatistiksel olarak taban tabana zıt** yanıt veren tek adipokin olarak öne çıkıyor; hem kan seviyesi hem doku salınımı, sistemik trigliserit (TAG) seviyeleriyle çok güçlü pozitif korelasyon gösteriyor (R=0.630, p<0.0001). Stefanakis et al. (2024)'te ise farklı bir serpin çifti — SERPINA6 (kortizol bağlayıcı globulin) ve SERPINA7 (tiroksin bağlayıcı globulin) — leptin replasmanıyla düzenleniyor: SERPINA6 güçlü biçimde baskılanırken SERPINA7 hafifçe baskılanıyor, ve bu, leptinin HPA ve tiroid eksenlerini nasıl moleküler düzeyde manipüle ettiğini gösteriyor. İki çalışma farklı serpinlere odaklansa da, ortak sonuç şu: serpin ailesi, adipoz dokunun enerji durumunu hem lipid metabolizmasına (Serpin F1-ATGL bağlantısı) hem nöroendokrin eksenlere (SERPINA6/7-HPA/tiroid bağlantısı) çeviren, azımsanan ama merkezi bir aracı sınıfı.

---

### Adipoziteye Göre Ayrışan Adipokin Yanıtları

Rossmeislova et al. (2024)'te kan leptin, serpin F1 ve CFD seviyeleri doğrudan adiposite durumundan etkileniyor (obez kadınlarda genel olarak daha yüksek bazal düzeyler), oysa adiponektin, CTRP3 ve ANGPTL4'ün bazal düzeyleri adiposite ile ilişkili değil. Bu, tüm adipokinlerin obeziteye aynı şekilde "duyarlı" olmadığını gösteriyor — bazıları (leptin, serpin F1, CFD) doku kütlesiyle orantılı skalalanırken, bazıları (adiponektin, CTRP3, ANGPTL4) daha çok akut beslenme durumuna (fasting/refeeding) duyarlı, adiposite-bağımsız bir düzenleme gösteriyor. Bu ayrım, "kişiselleştirilmiş fasting" bağlamında önemli: bir bireyin adipokin profilini yorumlarken, hangi molekülün "kronik adiposite göstergesi" hangisinin "akut beslenme durumu göstergesi" olduğunu ayırt etmek gerekiyor.