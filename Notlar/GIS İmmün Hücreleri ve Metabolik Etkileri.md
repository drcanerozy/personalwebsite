---
Tür:
  - Besleyici
ODAK:
  - "[[İmmün Sistem]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[KC, AD ve GIS İmmün Hücrelerinde Öne Çıkanlar ve Metabolik Etkileri]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[İmmün Sistem ve İmmünonutrisyon]]"
YORUM:
KAYNAK: 10.1016/j.immuni.2023.05.001
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[KC, AD ve GIS İmmün Hücrelerinde Öne Çıkanlar ve Metabolik Etkileri]]"
  - "[[İmmün Yanıt ve İnflamasyon Döngüsü]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["Diyet Lifleri & Prebiyotikler"] --> B["Kommensal Bakteriyel Fermentasyon"]
>     B --> C["Kısa Zincirli Yağ Asitleri (Asetat, Propiyonat, Bütirat)"]
>     C --> D["Sıkı Bağlantı Proteinleri (Claudin/Occludin) → Sağlam Mukozal Bariyer"]
>     C --> E["GLP-1/PYY Sekresyonu & İmmün Tolerans (Treg İndüksiyonu)"]
> ```
>
> **Şekil Açıklaması:** Diyet lifleri ve prebiyotiklerin kommensal bakteriler tarafından fermentasyonu sonucu üretilen kısa zincirli yağ asitleri (asetat, propiyonat, bütirat); sıkı bağlantı proteinlerini (claudin/occludin) uyararak mukozal bariyeri güçlendirir ve enteroendokrin GLP-1/PYY salınımı ile Treg indüksiyonu üzerinden immün toleransı destekler.

**Amacı:** Bu derleme; karaciğer, gastrointestinal sistem (GIS) ve yağ dokusundaki yerleşik (resident) bağışıklık hücrelerinin, yapısal hücrelerle (epitel, adiposit vb.) kurduğu iletişim ağlarını, bu ağların besin emilimi ve sistemik metabolizmayı nasıl yönettiğini ve obezite gibi hastalıklarda bu devrelerin nasıl bozulduğunu incelemeyi amaçlamaktadır [1], [2].

---

### 1) GIS'teki Yerleşik İmmün Hücrelerin Fonksiyonel Etkileri

Bağırsaktaki immün hücreler sadece patojen savunması yapmaz; bariyer bütünlüğünü koruyan, mikrobiyal toleransı sağlayan ve metabolik ritmi yöneten aktif düzenleyicilerdir.

*   **Bariyer ve Mikrobiyal Tolerans:** ILC3 (Innate Lymphoid Cells Type 3), $\gamma\delta$ T hücreleri ve Th17 hücreleri bağırsak homeostazının merkezindedir [3].
    *   **Tolerans Döngüsü:** Mikrobiyal sinyaller, miyeloid hücrelerden IL-1$\beta$ salınımını tetikler. Bu sitokin ILC3'leri uyararak GM-CSF üretmelerini sağlar. GM-CSF ise miyeloid hücrelerin **Retinoic Acid (RA)** ve **IL-10** üretmesini sağlayarak düzenleyici T hücrelerini (Tregs) aktive eder ve besinlere/kommensal bakterilere karşı tolerans oluşur [4], [5].
*   **[[Sirkadiyen Ritim]] Yönetimi:** ILC3 hücreleri, bağırsak epitel hücrelerinin (IEC) "metabolik tonunu" ve sirkadiyen ritmini yönetir. ILC3 kaynaklı **IL-22**, epitel hücrelerinde *Nfil3* gibi sirkadiyen saat genlerinin ekspresyonunu düzenler [6], [7]. Bu ritim, beyinden gelen ışık sinyalleri (suprakiyazmatik çekirdek) ve yemek yeme ile tetiklenen enterik nöronlardan salınan **VIP (Vazoaktif İntestinal Peptid)** ile koordine edilir [8], [9].

### 2) Besin Ögesi Emilimi ve Fonksiyonları Üzerine Etkiler

Beslenme akademisyeni için en kritik nokta, immün hücrelerin bağırsak epitelindeki "besin taşıyıcılarını" (transporter) açıp kapayan bir anahtar gibi çalışmasıdır. Burada **IL-22** sitokini merkezi bir rol oynar.

*   **Lipid vs. Karbonhidrat Emilimi "Anahtarı":**
    *   **Lipid Emiliminin Baskılanması:** Yüksek seviyedeki IL-22, bağırsak epitelindeki lipid taşıyıcı genlerin ekspresyonunu baskılar. Yani bağışıklık sistemi aktifken (yüksek IL-22), vücut yağ emilimini sınırlar [10], [11].
    *   **Lipid Emiliminin Artırılması:** Beslenme ile yağ alımının artması gerektiğinde (örneğin sütten kesilme döneminde), CD4+ T hücreleri devreye girerek ILC3'leri baskılar ve IL-22 üretimini azaltır. Bu sayede lipid taşıyıcıları artar ve yağ emilimi gerçekleşir [10]. Ayrıca cDC2 hücreleri, **IL-22BP (Binding Protein)** salgılayarak ortamdaki IL-22'yi "hroplar" (sequester) ve lipid emilimini serbest bırakır [11].
    *   **Karbonhidrat Moduna Geçiş:** Yüksek karbonhidratlı diyet, epitel hücreleri ile $\gamma\delta$ T hücreleri arasında **Jag2-Notch** sinyalini tetikler. Bu sinyal ILC3'lerden IL-22 salınımını durdurur. IL-22 azaldığında epitel hücreleri metabolik programlarını değiştirerek karbonhidrat metabolizmasına ve emilimine odaklanır [12], [6].

### 3) Farklı Diyetlerin GIS Yerleşik İmmün Hücrelerine Etkisi

Diyetin içeriği, bağırsaktaki immün popülasyonu ve dolayısıyla metabolik sağlığı doğrudan şekillendirir.

*   **Yüksek Yağlı Diyet (HFD) ve Obezite:**
    *   **ILC3 Kaybı:** HFD, kolondaki IL-22 üreten koruyucu ILC3 hücrelerinin kaybına neden olur. Bu durum bağırsak geçirgenliğini (leaky gut) artırır ve sistemik glikoz intoleransına yol açar [11].
    *   **MAIT Hücrelerinin Agresifleşmesi:** Obezitede, ileumdaki MAIT (Mucosal-associated invariant T) hücreleri artar ve aşırı miktarda inflamatuar **IL-17A** üretmeye başlar. Bu durum bağırsak bariyerini bozar ve mikrobiyotayı (disbiyozis) olumsuz değiştirir [13], [14].
*   **Yüksek Karbonhidratlı Diyet:**
    *   Yukarıda belirtildiği gibi, $\gamma\delta$ T hücreleri üzerinden IL-22 üretimini baskılayarak bağırsağı şeker emilimine programlar [12].
*   **Vitamin A Eksikliği:**
    *   ILC3 hücreleri Vitamin A'ya son derece duyarlıdır. Vitamin A eksikliği olan diyetlerde ILC3 popülasyonu dramatik şekilde azalır. Ayrıca miyeloid hücrelerin tolerans oluşturmak (Treg aktivasyonu) için Vitamin A'dan retinoic acid üretmesi gerekir; bu eksiklik immün toleransı bozar [4].
*   **Yeme Zamanlaması (Sirkadiyen Etki):**
    *   Yemek yeme eylemi, enterik nöronlardan VIP salgılatır. VIP, ILC3'leri uyararak IL-22 salgılatır ve bu da besin emilim ritmini ayarlar. Düzensiz yeme saatleri bu nöro-immün devreyi bozarak metabolik disregülasyona neden olabilir [9].

**Özet Çıkarım:**
Besin emilimi pasif bir süreç değil, immün hücrelerin (özellikle ILC3, T hücreleri) denetiminde gerçekleşen aktif bir karardır. **IL-22**, lipid emilimini frenleyen bir "metabolik fren" mekanizmasıdır. Yüksek karbonhidrat diyeti veya bağışıklık baskılayıcı sinyaller bu freni kaldırarak besin emilim paternini değiştirir.

karaciğerdeki immün hücrelerin yağ metabolizmasına olan etkilerini özetle
