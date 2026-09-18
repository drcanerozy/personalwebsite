---
Tür:
  - Besleyici
ODAK:
  - "[[GLP-1]]"
MEKANİZMA:
DİZİN:
  - "[[Obezite]]"
  - "[[Kilo Geri Kazanımı]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Kilo Döngüsü ve İmmün Hafıza]]"
  - "[[GLP-1'e Yanıtsız Olmak]]"
  - "[[Semaglutid, Metabolik Adaptasyonu Kötüleştirmiyor]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[GLP-1lerin AD ve kas kaybı miktarları yanında kalitelerine etkisi]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: 10.1136/bmj-2025-085304
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "GLP-1 Reseptör Aktivasyonu, Kilo ve Kas Dinamikleri"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Kilo Döngüsü ve İmmün Hafıza]]"
  - "[[GLP-1 Sürecinde Hasta Yönetimi Delphi Yaklaşımı 2026]]"
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

**Makalenin Amacı:** Obezite veya fazla kilolu yetişkinlerde, kilo yönetimi ilaçlarının (WMM) kesilmesinden sonraki kilo geri kazanım oranını (regain rate) nicel olarak belirlemek, bu oranı davranışsal programlarla karşılaştırmak ve kardiyometabolik belirteçlerdeki değişimleri analiz etmektir [1].

---

### 1. Primer ve Sekonder Bulgular

**Primer Bulgu (Kilo Geri Kazanımı):**
Çalışmanın en çarpıcı sonucu, ilaç tedavisinin kesilmesini takiben **hızlı bir kilo alımının** gerçekleştiğidir.
*   Genel olarak tüm ilaçlar için ortalama aylık geri kazanım hızı **0.4 kg**'dır [2].
*   İlaç bırakıldıktan sonra, kaybedilen kilonun tamamen geri alınması ve başlangıç ağırlığına dönülmesi (return to baseline) ortalama **1.7 yıl** sürmektedir [3].

**Sekonder Bulgu (Kardiyometabolik Belirteçler):**
Kilo kaybıyla elde edilen sağlık kazanımları kalıcı değildir. HbA1c, açlık glukozu, kan basıncı (sistolik/diyastolik) ve lipid profili (kolesterol, trigliserit) gibi tüm iyileşen değerlerin, ilaç bırakıldıktan sonra **1.4 yıl içinde** tamamen başlangıç seviyelerine döneceği öngörülmüştür [2, 4]. Yani metabolik iyileşme, ilaç kullanımıyla sınırlıdır.

---

### 2. İlaç Gruplerine Göre Sonuçlar ve Farklılıklar

Çalışma, ilaçları etkinliklerine göre sınıflandırmış ve şaşırtıcı bir korelasyon bulmuştur: **İlaç ne kadar güçlüyse, bırakıldığında geri dönüş o kadar hızlıdır.**

*   **Tüm Kilo Yönetimi İlaçları (Genel):**
    *   Bıraktıktan sonra aylık geri kazanım: **0.4 kg** [5].
    *   Başlangıç ağırlığına dönüş süresi: **1.7 yıl** [6].
*   **İnkretin Mimetikleri (Liraglutide vb.):**
    *   Bıraktıktan sonra aylık geri kazanım: **0.5 kg** [5].
    *   Başlangıç ağırlığına dönüş süresi: **1.6 yıl** [6].
*   **Yeni ve Daha Etkili İnkretin Mimetikleri (Semaglutide, Tirzepatide):**
    *   *Kritik Veri:* Bu grupta tedavi sonu kilo kaybı çok daha yüksektir (ort. 14.7 kg). Ancak ilacı bıraktıktan sonraki geri kazanım hızı, diğerlerinden iki kat daha hızlıdır: **Aylık 0.8 kg** [5].
    *   Başlangıç ağırlığına dönüş süresi: Sadece **1.5 yıl** [6].

**Yorum:** Semaglutide (Ozempic/Wegovy) veya Tirzepatide (Mounjaro) kullanan hastalar çok hızlı kilo verirler, ancak ilacı bıraktıklarında "rebound" (geri tepme) etkisi çok daha sert ve hızlı gerçekleşir.

---

### 3. İlaçlar vs. Davranışsal Programlar (BWMP)

Makale, ilaç sonrası durumu, sadece diyet ve egzersiz içeren davranışsal programlarla (BWMP) karşılaştırmıştır.
*   **Bulgu:** İlaçla zayıflayanlar, davranışsal programla zayıflayanlara göre **daha hızlı** kilo geri almaktadır. İlaç grubunda geri alım hızı, davranışsal gruba göre ayda **0.3 kg daha fazladır** [2].
*   **Neden?** Davranışsal programlar kişiye kalıcı başa çıkma becerileri kazandırabilirken, ilaçlar biyolojik bir "doygunluk" sağlar. İlaç kesildiğinde biyolojik baskı kalkar ve açlık geri döner; ancak kişi gerekli davranışsal donanıma sahip değilse hızla eski kilosuna döner [7].

---

### 4. Avantajlar, Dezavantajlar ve Yorumlar

**Avantajlar:**
*   **Hızlı ve Yüksek Etki:** Yeni nesil ilaçlar (Semaglutide/Tirzepatide) ile %15-20'lere varan devasa kilo kayıpları sağlanır [8].
*   **Aktif Dönemde Sağlık:** İlaç kullanıldığı sürece kardiyovasküler risk faktörlerinde belirgin iyileşme görülür [8].

**Dezavantajlar:**
*   **Sürdürülebilirlik Sorunu:** İlaç bırakıldığında kilo ve metabolik riskler <2 yıl içinde tamamen geri döner [3].
*   **Bağımlılık:** Sağlık faydalarının korunması için bu ilaçların kronik (belki de ömür boyu) kullanımı gerekebilir, ancak gerçek hayatta hastaların %50'si 1 yıl içinde ilacı bırakmaktadır [9].

**Nasıl Yorumlanmalı?**
Bu sonuçlar, GLP-1 ve benzeri ilaçların "kısa süreli bir çözüm" veya "kür" olarak görülmemesi gerektiğini kanıtlar. Bu ilaçlar obeziteyi tedavi etmez, sadece kullanıldığı sürece *yönetir*. İlaç, obezitenin kronik ve nükseden doğasını değiştirmez [10].

---

### 5. Diyetisyenler İçin Klinik Pratik Adımları

Bu çalışmanın verilerine dayanarak diyetisyenler için oluşturulabilecek eylem planı:

1.  **Gerçekçi Beklenti Yönetimi:** Hastaya, "İlacı bırakırsam ne olur?" sorusunun cevabı dürüstçe verilmelidir: "İstatistiklere göre, ilacı bırakanlar yaklaşık 1.5 yıl içinde verdikleri kilonun tamamını geri alıyor. Bu yüzden çıkış planımız ilaçtan daha önemli." [6, 11].
2.  **Agresif Koruma Programı:** İlaç kesildikten sonraki ilk aylar "riskli bölge"dir. Yeni nesil ilaçları bırakanlar ayda ortalama 0.8 kg almaktadır. Bu dönemde diyetisyen desteği sıklaştırılmalı (örneğin haftalık takip) ve protein/lif odaklı tokluk stratejileri uygulanmalıdır [5].
3.  **Davranışsal Temel:** İlaç kullanırken sadece iştah kapalılığına güvenilmemelidir. Hasta ilaçla zayıflarken, eş zamanlı olarak yoğun bir "davranışsal ağırlık yönetimi" (BWMP) eğitimi almalıdır. Çünkü ilaç gittiğinde hastayı koruyacak tek şey kazandığı alışkanlıklar olacaktır [7]. #vizyoner 

---

### 6. Makaleden Çıkarılacak 3 Ana Mesaj

1.  **"Hızlı Gelen, Hızlı Gider" (Bumerang Etkisi):**
    Özellikle yeni nesil güçlü ilaçlar (Semaglutide, Tirzepatide), daha fazla kilo verdirse de, ilaç kesildiğinde geri kilo alım hızı (ayda 0.8 kg), eski nesil ilaçlara veya diyet programlarına göre çok daha yüksektir. İlaç ne kadar etkiliyse, bırakıldığında "geri tepme" o kadar serttir [5, 12].

2.  **Kalıcı Metabolik İyileşme Yoktur:**
    İlaç kullanımı sırasında düzelen tansiyon, şeker ve kolesterol değerlerine güvenilmemelidir. İlaç bırakıldığında bu değerler, kilodan bağımsız olarak hızla bozulmakta ve ortalama 1.4 yılda tedavi öncesi seviyelere dönmektedir. Bu durum, ilacın kısa süreli kullanımının (örneğin düğün öncesi zayıflama gibi) uzun vadeli kalp sağlığına bir katkısı olmayacağını gösterir [2, 3].

3.  **İlaç Tek Başına Yeterli Bir Strateji Değildir:**
    Çalışma, ilaç sonrası geri kazanımın davranışsal yöntemlere göre daha hızlı olduğunu kanıtlamıştır. Bu, ilaçların "davranış değişikliğini kolaylaştıran bir araç" olarak kullanılması gerektiğini, ancak tek başına bir çözüm olmadığını; ilacın sağladığı biyolojik avantajın (tokluk), zihinsel ve davranışsal bir temelle (diyetisyen desteğiyle) birleştirilmediğinde geçici olduğunu vurgular [7, 13].

