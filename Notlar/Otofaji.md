---
Tür:
  - Besleyici
ODAK:
  - "[[Aralıklı Açlık]]"
  - "[[Adipoz Doku]]"
  - "[[Obezite]]"
MEKANİZMA:
  - "[[Nutrient Sensing]]"
  - "[[Metabolic Flexibility]]"
DİZİN:
  - "[[mTOR]]"
  - "[[AMPK]]"
  - "[[Lizozom]]"
  - "[[Mitofaji]]"
  - "[[Sarkopeni]]"
  - "[[Urolithin A]]"
  - "[[Spermidin]]"
ETİKET:
  - makaleden
BAĞLANTILI NOTLAR:
  - "[[AMPK–TBK1 Resiprokal Frenleme Devresi Adiposit Kataboliz Kontrolü]]"
  - "[[Metiyonin Kısıtlı Diyetler Ömrü Nasıl Uzatıyor?]]"
  - "[[Ferroptozis ve İmmün Sistem]]"
  - "[[Hücresel Yaşlanma ve Kalori Kısıtlaması]]"
  - "[[mTORC1 Sinyalizasyonu ve Açlık-Tokluk Döngüsü]]"
  - "[[GLP-1'e Giriş]]"
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[Açlık ve Otofaji İlişkisi]]"
BAĞLANTILI DERSLER:
  - "[[Diyet İlkeleri ve Popüler Diyetler]]"
YORUM: "Erken evre koruyucu / ileri evre kilitlenme paradoksu kilit kavram. Metformin+IF kombinasyon riski klinik için kritik. Ferroptozis ile GPX4 üzerinden bağlantı var. AMPK-TBK1 devresiyle yukarı akım ilişkisi kurulmalı."
KAYNAK: "https://doi.org/10.1007/s13679-026-00716-5"
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
  - "[[mTORC1 Sinyalizasyonu ve Açlık-Tokluk Döngüsü]]"
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

> **Metodolojik Etiketler:** #finding/contradictory
https://doi.org/10.1007/s13679-026-00716-5

Aralıklı Açlık Adipoz Doku Obezite

---

## Otofaji Nedir?

Otofaji (Yunanca: "öz yeme"), hücrenin hasarlı organellerini, yanlış katlanmış proteinlerini ve gereksiz bileşenlerini lizozomlar aracılığıyla parçalayıp geri dönüştürdüğü evrimsel açıdan korunmuş bir kalite kontrol mekanizmasıdır. Açlık, enerji kısıtlaması ve çeşitli stres koşullarında aktive olur.

**Temel Düzenleyici Eksen:**
- **mTORC1 aktif** (beslenmiş durum) → otofajiyi baskılar
- **AMPK aktif / mTORC1 baskılı** (açlık durumu) → otofajiyi başlatır
- ULK1 → Beclin-1 → otofagozom oluşumu → lizozomal füzyon → içerik degradasyonu

---

## Erken Evre vs. İleri Evre Paradoksu

Otofajinin en kritik klinik kavramı: **doz-yanıt ilişkisi doğrusal değil, ters-U şeklinde.**

**Erken/Orta Evre Otofaji (Koruyucu):**
- Hasarlı mitokondrileri temizler (mitofaji)
- İnflamazom aktivasyonunu baskılar
- İnsülin duyarlılığını artırır
- Kanser öncesi hücreleri elimine eder
- Yaşlanmayı yavaşlatır

**İleri Evre / Kronik Otofaji (Kilitlenme Riski):**
- Lizozomal kapasite aşılır → otofagik akı durur
- Hasarlı materyaller birikmeye devam eder
- Parçalanmış organeller hücre içinde toksik birikim oluşturur
- p62/SQSTM1 birikimi → NF-κB aktivasyonu → proinflamatuvar dönüş

**Klinik önemi:** "Otofajiyi aktive et" söylemi tek başına yetersiz. **Ne kadar süreyle, hangi dokuda, hangi hastada** soruları kritik.

---

## Obezite ve Otofaji İlişkisi

Obez adipoz dokuda otofaji paradoksal şekilde **hem artmış hem bozulmuş** görünür:

- Bazal otofagozom sayısı artmış (kompansatuar yanıt)
- Ama lizozomal klirens bozulmuş → otofagik akı tıkalı
- Sonuç: işlevsiz otofagozom birikimi → inflamasyon amplifikasyonu

Bu durum, obezitede AMPK-TBK1 devresindeki kilitlenmeyle paralel: **sistem başlatmak istiyor ama tamamlayamıyor.**

---

## İlaç Etkileşimleri — Klinik Dikkat Noktaları

**Metformin + Aralıklı Açlık Kombinasyonu:**
Metformin AMPK'yı aktive ederek otofajiyi başlatır. IF de aynı yolağı kullanır. Teorik olarak sinerjik görünse de:
- Her ikisi birlikte uygulandığında mTORC1 baskısı çok derin olabilir
- Özellikle sarkopenik obez hastalarda kas yıkımı riski artabilir
- Klinik kanıt henüz sınırlı — bireysel değerlendirme şart

**Rapamisin (mTOR inhibitörü):**
Güçlü otofaji aktivatörü. Ama kronik kullanımda immünosüpresyon ve metabolik yan etkiler (insülin direnci paradoksu) — uzun vadeli kullanım sorunlu.

---

## Besin ve Nutrasötik Modulasyonu

**Otofajiyi Aktive Edenler:**
- Spermidin (buğday tohumu, soya, mantar) → mTOR'dan bağımsız yolak
- Urolithin A (nar, böğürtlen metaboliti — mikrobiyota dönüşümü gerekli) → mitofaji spesifik
- Resveratrol → SIRT1 üzerinden
- Curcumin → Beclin-1 aktivasyonu
- Kalori kısıtlaması / açlık → en güçlü fizyolojik uyaran

**Mikrobiyota Bağlantısı (Urolithin A):**
Urolithin A'nın mitofaji aktivasyonu için bağırsak mikrobiyotasının elagitanen → urolitin dönüşümünü yapabilmesi gerekir. Mikrobiyota kompozisyonu bu dönüşümü belirler → kişisel yanıt variabilitesinin kaynağı.

**Otofajiyi Baskılayanlar:**
- Yüksek insülin (rafine KH, sık öğün)
- Yüksek lösin / BCAA → mTORC1 aktivasyonu
- Klorokin (lizozomal asidifikasyonu bozar — araştırma aracı)

---

## Doku-Spesifik Farklılıklar

| Doku | Otofaji Rolü |
|------|-------------|
| Adipoz doku | Lipoliz ile koordineli; obezitede bozulmuş |
| Karaciğer | NAFLD'de koruyucu; aşırı aktivasyon hepatositlerde toksik |
| Kas | Mitofaji sarkopeniyi önler; kronik aktivasyon kas kaybı |
| Beyin | Nörodejenerasyona karşı koruyucu; alzheimer'da bozulmuş |
| β hücreleri | İnsülin granül homeostazı; T2DM'de kritik |

---

## Açlık Protokolleri ve Otofaji

- **12-16 saat açlık:** mTORC1 baskılanmaya başlar, otofaji hafifçe artar
- **24-48 saat:** Belirgin otofagik aktivasyon, mitofaji piki
- **72+ saat:** Lizozomal kapasite zorlanabilir — dikkatli izlem
- **Tekrarlayan kısa açlık (IF):** Kronik uzun açlıktan daha güvenli otofaji aktivasyonu — "pulse" etkisi

---

## Çekirdek Mesaj

> Otofaji, hücrenin en temel temizlik ve yenileme mekanizması. Aralıklı açlık bu mekanizmayı aktive etmenin en fizyolojik yolu. Ama "ne kadar çok, o kadar iyi" değil — erken evre koruyucu, ileri evre kilitlenme riski. Klinik pratikte protokol süresi, ilaç kombinasyonları ve doku bağlamı birlikte değerlendirilmeli.
