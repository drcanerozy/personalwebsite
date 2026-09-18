---
Tür:
  - Besleyici
ODAK:
  - "[[Adipoz Doku]]"
MEKANİZMA:
  - "[[Tiroid]]"
DİZİN:
  - "[[Kilo Geri Kazanımı]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Kilo Döngüsü ve İmmün Hafıza]]"
  - "[[Mikrobiyotaya Giriş]]"
  - "[[Adipoz Doku Lipolizi]]"
  - "[[GLP-1 Kullanımından Sonra Ağırlık Kazanımı]]"
  - "[[İnsülin–IRF4 Ekseni Açlıkta Yağ mı Kas mı Kaybedilir?]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM: "Tiroid-D3 mekanizması kas korumayla çelişiyor. İnsülin-IRF4 ekseniyle ortak hat: kilo regain sırasında yağ öncelikli. Mikrobiyota bağlantısı henüz kurulmamış."
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Kas Proteolizi ve Substrat Partisyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Kilo Döngüsü ve İmmün Hafıza]]"
  - "[[Tutumlu ve Savurgan Fenotipler - Thrifty vs Spendthrifty]]"
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

Bu fenotip, ciddi kilo kaybı, açlık veya hastalık (kaşeksi) sonrasında gerçekleşen yeniden beslenme (weight regain) döneminde, vücut yağının yağsız dokuya (özellikle kas kütlesine) kıyasla orantısız derecede hızlı ve öncelikli olarak geri kazanılması durumudur. Vücut, yağ depolarını hızla doldurmak için metabolik verimliliğini artırır. Bu durum, kilo kaybı sırasında devreye giren "adaptif termojenezin" (metabolik yavaşlamanın), kilo alımı sürecinde de devam etmesiyle sağlanır.

Bu süreçte iskelet kası, enerji harcamasını baskılamak için nörohormonal sisteme karşı bir direnç geliştirir. Bu direncin merkezinde **Tip 3 Deiyodinaz (D3)** enzimi yer alır. D3, aktif tiroid hormonu olan T3'ü ve öncüsü T4'ü inaktif formlara (T2 ve Reverse T3/rT3) dönüştüren ana enzimdir. Kilo alımı sürecinde iskelet kaslarında D3 ekspresyonu ve aktivitesi artarken, T4'ü aktif T3'e çeviren Tip 2 Deiyodinaz (D2) azalır. Bu durum, kanda tiroid hormon seviyeleri normal olsa bile, kas dokusu içinde lokal bir **"hipotiroidizm"** (tiroid yetersizliği) durumu yaratır.

D3 aracılığıyla hücre içi T3'ün azalması, kas metabolizmasında şu değişikliklere yol açarak enerjinin korunmasını sağlar:
    ◦ Kas kasılma-gevşeme kinetiğinin yavaşlaması (daha az ATP harcanması).
    ◦ Hızlı kas liflerinden (tip II), daha ekonomik olan yavaş kas liflerine (tip I) geçiş olması.
    ◦Protein döngüsü hızının azalması

