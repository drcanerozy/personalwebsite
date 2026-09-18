---
Tür:
  - Çekirdek
ODAK:
  - "[[İmmün Sistem]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[İmmün Sistem ve İmmünonutrisyon]]"
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Pankreas Beta Hücre Plastisitesi ve Rejenerasyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[İmmün Yanıt ve İnflamasyon Döngüsü]]"
  - "[[Adipoz Doku Endokrin Fonksiyonu ve Dinamikleri]]"
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

İmmün Sistem ve İmmünonutrisyon
İmmün Sistem
Adipoz Doku
GIS İmmün Hücreleri ve Metabolik Etkileri
Karaciğer İmmün Hücreleri ve Metabolik Etkileri
#star 

**Makale Başlığı:** Regulation of systemic metabolism by tissue-resident immune cell circuits
**DOI:** 10.1016/j.immuni.2023.05.001
**Amacı:** Karaciğer, yağ dokusu ve bağırsaktaki yerleşik bağışıklık hücrelerinin, yapısal hücrelerle oluşturduğu metabolik devreleri, bu devrelerin diyet ve mikrobiyota ile nasıl etkileştiğini ve hastalık durumlarında bu iletişimin nasıl bozulduğunu incelemektir [1], [2].

---

### 1) Öne Çıkan İmmün Hücreler ve Etki Mekanizmaları

Kaynağa göre, sistemik metabolizmayı yöneten "doku yerleşik" (tissue-resident) üç ana immün hücre grubu ve bunların dokulara özgü kritik mekanizmaları şunlardır:

#### A. ILC (Innate Lymphoid Cells) Ailesi: Metabolik Termostatlar
Bu hücreler, dokudaki metabolik sinyalleri (diyet, nöronal sinyaller) ilk algılayan ve hızla yanıt veren anahtarlardır.
*   **ILC1 (Karaciğer & Adipoz):** Genelde patolojiktir. Obezite veya karaciğer hasarında **IFN-$\gamma$** salgılayarak makrofajları inflamatuar tipe dönüştürür ve insülin direncini başlatır [3], [4]. Ancak karaciğer rejenerasyonunda hepatositleri koruyucu (Bcl-xL artışı ile) bir rolü de vardır [4].
*   **ILC2 (Adipoz & Karaciğer):** Metabolik koruyucudur.
    *   *Adipozda:* Nöronal sinyallere (Norepinefrin) yanıt vererek **IL-13 ve Metiyonin-Enkefalin (MENK)** üretir; bu da yağ yakımını (bejleşme) ve insülin duyarlılığını artırır [5], [6].
    *   *Karaciğerde:* **IL-13** salgılayarak glukoneogenezi (şeker üretimini) baskılar [7].
*   **ILC3 (Bağırsak):** Besin emilim bekçisidir. Salgıladığı **IL-22**, bağırsak epitelindeki lipit taşıyıcılarını baskılayarak yağın kana karışmasını sınırlar [8], [9].

#### B. Makrofajlar: Çöpçüler ve Sinyal İleticiler
*   **Kupffer Hücreleri (Karaciğer):** Periportal bölgede yerleşiktir. **IL-6 ve IL-1$\beta$** üreterek hepatositlerin glikojen depolamasını veya glikoz üretimini yönetir. Ayrıca "FGF21" hormonunu baskılayarak yağ dokusuyla konuşur [10], [11].
*   **PVM (Perivasküler Makrofajlar - Adipoz):** Damar çevresinde durur, **PDGFc** salgılayarak yağ hücrelerinin (adipositlerin) lipit depolama kapasitesini düzenler [12].
*   **LAM (Lipid-Associated Macrophages - Adipoz/Karaciğer):** **TREM2** reseptörü ile ölü yağ hücrelerini veya hepatositleri temizler (eferositoz). Bu temizlik yapılmazsa (TREM2 kesilirse), metabolik inflamasyon kronikleşir [13], [14].

#### C. T Hücreleri (MAIT ve $\gamma\delta$T): Lipit Sensörleri
*   **MAIT ve $\gamma\delta$ T Hücreleri:** Özellikle karaciğer ve bağırsakta lipit antijenlerini algılarlar. **IL-17A** üreterek karaciğerde yağ birikimini ve fibrozisi (HSC aktivasyonu ile) tetiklerken, bağırsakta bariyer geçirgenliğini artırabilirler [15], [16], [17].

---

### 2) Dokular Arası İletişim (Crosstalk) ve Döngüler

Dokular birbirleriyle hormonlar (adipokin/hepatokin), sitokinler ve sinirler aracılığıyla konuşur. Kaynakta belirtilen en çarpıcı iletişim döngüleri şunlardır:

#### Döngü 1: Bağırsak-Karaciğer-Adipoz Ekseni (FGF21 Kontrolü)
Bağırsaktaki mikrobiyal durum, karaciğer üzerinden yağ dokusunun yakıt yakma hızını belirler.

> **Flowchart:**
> Bağırsak Mikrobiyotası (Bakteriyel Ürünler) $\rightarrow$ Karaciğer Kupffer Hücrelerini Uyarır (IL-1$\beta$ salınımı) $\rightarrow$ Hepatositlerde **FGF21** Üretimini **BASKILAR** $\rightarrow$ Kanda FGF21 Azalır $\rightarrow$ Adipoz Dokuda Lipoliz (Yağ Yakımı) ve Adiponektin Üretimi **DURUR** $\rightarrow$ **Sonuç:** Enerji Harcamasının Azalması ve Yağlanma [11], [18].

#### Döngü 2: Adipoz-Karaciğer-Bağırsak Ekseni (Demir Kontrolü)
Yağ dokusundaki makrofajlar, demir seviyesini manipüle ederek bağırsağın ne kadar yağ emeceği konusunda emir verir.

> **Flowchart:**
> Adipoz Doku (CSF1R+ Miyeloid Hücreler) $\rightarrow$ Adipoz Doku Demir Seviyesini Düşürür $\rightarrow$ Karaciğer Demir Alımını Artırır (Transferrin reseptörü ile) $\rightarrow$ Bağırsak Epitel Hücrelerine Sinyal Gider $\rightarrow$ Bağırsaktan **Lipid Emilimi AZALIR** $\rightarrow$ **Sonuç:** Obeziteye Karşı Koruma [19], [20].

#### Döngü 3: Bağırsak-Sirkadiyen Ritim Ekseni
Bağırsak bakterileri ve bağışıklık hücreleri, karaciğerin ve vücudun biyolojik saatini ayarlar.

> **Flowchart:**
> Bağırsak Mikrobiyotası (Diyetle Değişen) $\rightarrow$ Epitel Hücreleri ve ILC3'ler $\rightarrow$ **Sirkadiyen Saat Genlerini (Bmal1, Nfil3)** Düzenler $\rightarrow$ Karaciğerdeki Metabolik Genlerin (PPAR$\gamma$) Ritmik Çalışmasını Sağlar $\rightarrow$ **Sonuç:** Kan Şekeri ve Yağ metabolizmasının günün saatine göre ayarlanması [21], [22].

---

### 3) Besinler ve Diyet Açısından İnceleme (Trigger Flowcharts)

Besinler sadece kalori değildir; immün devreleri başlatan "moleküler anahtarlar"dır. İşte diyete özgü mekanizmalar:

#### Senaryo A: Yüksek Karbonhidratlı Diyet ve "Şeker Modu"
Karbonhidrat yükü, bağışıklık sistemini "yağ emilimini serbest bırak, şekere odaklan" moduna sokar.

> **Flowchart:**
> **Yüksek Karbonhidrat Alımı** $\rightarrow$ Bağırsak Epiteli ve $\gamma\delta$ T Hücreleri Arasında **Jag2-Notch** Sinyali Başlar $\rightarrow$ ILC3 Hücreleri Baskılanır $\rightarrow$ **IL-22 Üretimi DURUR** $\rightarrow$ Epitel Hücreleri Karbonhidrat Metabolizması Genlerini Açar $\rightarrow$ **Sonuç:** Şeker Emilimine Adaptasyon [8], [3].

#### Senaryo B: Yüksek Yağlı Diyet (HFD) ve "Bariyer Çöküşü"
Aşırı yağ, koruyucu hücreleri öldürerek sistemik bir kaosa yol açar.

> **Flowchart:**
> **Yüksek Yağlı Diyet (HFD)** $\rightarrow$ Bağırsak Mikrobiyota Bileşimi Bozulur (Disbiyozis) $\rightarrow$ Kolondaki **ILC3 Hücreleri AZALIR/Kaybolur** $\rightarrow$ IL-22 Seviyesi Düşer $\rightarrow$ Bağırsak Bariyeri Bozulur (Geçirgenlik Artar) $\rightarrow$ Bakteriyel Ürünler Kana Karışır $\rightarrow$ **Sonuç:** Sistemik Enflamasyon ve İnsülin Direnci [23], [24].

#### Senaryo C: Vitamin A Eksikliği ve "Tolerans Kaybı"
Besin eksikliği, immün sistemin "dostu düşmandan ayırma" yeteneğini bozar.

> **Flowchart:**
> **Diyette Vitamin A Yetersizliği** $\rightarrow$ Bağırsak Miyeloid Hücreleri **Retinoic Acid (RA)** Üretemez $\rightarrow$ **ILC3 Hücre Popülasyonu ÇÖKER** $\rightarrow$ IL-22 ve GM-CSF Üretilemez $\rightarrow$ Treg (Düzenleyici T) Hücreleri Oluşmaz $\rightarrow$ **Sonuç:** Gıdalara ve Mikroplara Karşı Tolerans Kaybı & Enflamasyon [25], [26].

#### Senaryo D: Soğuk Stresi veya Açlık (Nöro-İmmün Etki)
Vücut ısınmak veya enerji harcamak istediğinde yağ dokusunu "yakıt" olarak kullanır.

> **Flowchart:**
> **Soğuk Maruziyeti / Metabolik Stres** $\rightarrow$ Sempatik Sinirler **Norepinefrin** Salgılar $\rightarrow$ Adipoz Öncü Hücreleri GDNF ve **IL-33** Üretir $\rightarrow$ **ILC2 Hücreleri Aktive Olur** $\rightarrow$ IL-13 ve Enkefalin (MENK) Salgılar $\rightarrow$ Beyaz Yağ Hücreleri **UCP-1** Üreterek Bejleşir $\rightarrow$ **Sonuç:** Isı Üretimi ve Enerji Harcaması [27], [6].



**Makale Başlığı:** Regulation of systemic metabolism by tissue-resident immune cell circuits
**DOI:** 10.1016/j.immuni.2023.05.001
**Amacı:** Bu derleme; karaciğer, gastrointestinal sistem (GIS) ve yağ dokusunda yerleşik (tissue-resident) bağışıklık hücrelerinin, yapısal hücrelerle (hepatosit, enterosit, adiposit) kurduğu iletişim ağlarını; bu ağların sistemik metabolizmayı nasıl yönettiğini, diyet ve mikrobiyota ile nasıl etkileştiğini ve obezite/hastalık durumlarında bu devrelerin nasıl bozulduğunu incelemektedir [1], [2].

---

### BÖLÜM 1: Beslenme Akademisyeni İçin En Önemli 10 Çıkarım

Bu makale, beslenme bilimini klasik "kalori/enerji dengesi" modelinden, "hücreler arası iletişim ve immüno-metabolik sinyalizasyon" modeline taşımaktadır. İşte akademik vizyonunuzu derinleştirecek 10 kritik bulgu:

1.  **Emilim Pasif Değil, İmmünolojik Bir Karardır (IL-22 Freni):** Besin emilimi sadece sindirim enzimlerine bağlı pasif bir süreç değildir. ILC3 hücrelerinden salınan **IL-22**, bağırsak epitelindeki lipit taşıyıcı genleri baskılayan bir "fren" mekanizmasıdır. Bağışıklık sistemi bu freni çektiğinde lipit emilimi azalır. Obezitede ILC3 kaybı bu freni kaldırır ve metabolik bariyer çöker [3], [4].
2.  **Karaciğerde "Gayrimenkul" Önemlidir (Metabolik Zonasyon):** Karaciğer homojen bir depo değildir. Periportal bölge (giriş) glukoneogenez yaparken, perisentral bölge (çıkış) yağ sentezler. İmmün hücreler (Kupffer vs. MAIT) bu bölgelere göre dağılır. Diyet içeriği (şeker vs. yağ), karaciğerin hangi bölgesindeki immün devreyi tetikleyeceğini belirler [5], [6], [7].
3.  **Yağ Yakımı Nöro-İmmün Bir İşbirliğidir:** Termogenez (ısı üretimi/yağ yakımı) sadece kalori açığı veya egzersizle değil, sinir sistemi ile bağışıklık sisteminin el sıkışmasıyla olur. Sempatik sinirlerden gelen norepinefrin $\rightarrow$ ILC2 hücrelerini uyarır $\rightarrow$ ILC2'ler **Metiyonin-Enkefalin (MENK)** salgılar $\rightarrow$ Yağ hücresi bejleşir (UCP-1 artar) [8], [9].
4.  **"Eferositoz" (Hücresel Çöpçülük) Metabolizmanın Merkezidir:** Sağlıklı bir doku için ölü hücrelerin temizlenmesi şarttır. Karaciğer ve yağ dokusunda **TREM2+ makrofajlar** bu temizliği yapar. Obezitede artan TNF-$\alpha$, TREM2 reseptörünü kesip atar (ADAM17 enzimi ile). Temizlenemeyen ölü hücreler ("nekro-inflamasyon"), insülin direncinin ana kaynağıdır [10], [11], [12].
5.  **Demir, Yağ Emiliminin Uzaktan Kumandasıdır:** Yağ dokusundaki makrofajlar, demir seviyesini manipüle ederek bağırsağa sinyal gönderir. Yağ dokusunda demir azalırsa $\rightarrow$ Karaciğer demir alımını artırırken $\rightarrow$ Bağırsak yağ emilimini azaltır. Bu, demir metabolizması ile obezite arasında doğrudan bir köprüdür [13], [14].
6.  **Diyetin Türü İmmün Kaderi Belirler (Jag2-Notch):** Yüksek karbonhidratlı beslenme, bağırsak epitelini şeker emilimine programlarken, bağışıklık sistemine (ILC3'lere) "sus" emri verir (Jag2-Notch yolağı ile). Yani makro besinler, immün sistemin çalışma modunu değiştiren sinyallerdir [3], [15].
7.  **Sirkadiyen Beslenme İmmün Saatler Tarafından Yönetilir:** ILC3 hücrelerinin kendi biyolojik saatleri (Bmal1 genleri) vardır. Işık ve yemek zamanlaması (enterik nöronlardan VIP salınımı ile), bu hücrelerin IL-22 salgılamasını ve dolayısıyla besin emilim ritmini ayarlar. Gece yemeği, bu immün saati bozar [16], [17], [18].
8.  **Vitamin A: Toleransın Bekçisi:** Diyetle alınan Vitamin A, sadece göz sağlığı için değil, bağırsak toleransı için kritiktir. Miyeloid hücreler Vitamin A'yı retinoic aside çevirmezse, ILC3 hücreleri yok olur ve gıdalara karşı tolerans kaybolur [19].
9.  **Organlar Arası "WhatsApp" Grupları:** Organlar birbirleriyle sadece kan şekeri üzerinden değil, sitokinler ve lipid antijenleri üzerinden konuşur. Bağırsaktaki bir mikrop, karaciğerdeki $\gamma\delta$ T hücresini uyarabilir; karaciğerdeki bir sorun (FGF21 düşüşü), yağ dokusunun yakımını durdurabilir [20], [21].
10. **Yaşlanma ve Obezite: İmmünolojik İkizler:** Yaşlanmış yağ dokusu ile obez yağ dokusu şaşırtıcı derecede benzerdir (ILC2 kaybı, inflamasyon artışı). Yaşlılarda kilo kontrolü stratejisi, "zayıflatmak" değil, kaybolan ILC2 popülasyonunu geri kazanmak (immün gençleşme) üzerine olmalıdır [22], [23]. #vizyoner İmmün Sistem ve İmmünonutrisyon

---

### BÖLÜM 2: Akademik Kullanım ve Eğitim Entegrasyonu

Bu bulguları derslerinize ve akademik vizyonunuza şu şekilde entegre edebilirsiniz:

*   **Ders Anlatımında "Metafor" Kullanımı:**
    *   **Trafik Polisi:** ILC3 hücrelerini, bağırsak sınırında duran ve "Yağ kamyonları geçsin mi geçmesin mi?" kararını veren trafik polisleri olarak anlatın (IL-22 sinyali) [3], [4].
    *   **Çöpçüler Grevi:** NASH ve Obeziteyi, şehirdeki çöpçülerin (TREM2+ makrofajlar) greve gitmesi (reseptörlerinin kesilmesi) ve sokaklarda (dokularda) çöplerin (ölü hücrelerin) birikmesi olarak betimleyin [11], [24].
*   **Müfredat Güncellemesi:**
    *   **"İmmüno-metabolizma" Ünitesi:** Beslenme Biyokimyası dersine, makro besinlerin (yağ, karbonhidrat) sadece ATP üretmediğini, aynı zamanda sitokinleri (IL-17, IL-22) yönettiğini gösteren bu makaledeki yolakları ekleyin [25], [15].
    *   **Obezite Tedavisinde Yeni Vizyon:** Obezite tedavisini sadece "kalori kısıtlaması" olarak değil, **"Adipoz doku inflamasyonunu çözme (resolution)"** stratejisi olarak yeniden çerçeveleyin. Hedef sadece yağ hücresini küçültmek değil, makrofaj fenotipini değiştirmektir [26].
*   **Klinik Pratik Vizyonu:**
    *   Öğrencilere, danışanın sadece ne yediğine değil, **ne zaman yediğine** (Sirkadiyen-ILC3-VIP ilişkisi) odaklanmaları gerektiğini, çünkü metabolik emilim anahtarının orada olduğunu aşılayın [18].


Beslenme Biyokimyası dersinde "makro besinlerin sadece enerji (ATP) kaynağı olmadığı, aynı zamanda bağışıklık sistemini yöneten sinyaller olduğu" tezini işlemek için makalede (Li et al., 2023) yer alan şu üç temel moleküler yolağı kullanabilirsiniz.

Bu yolaklar, diyet içeriğinin (Karbonhidrat vs. Yağ) **IL-22** ve **IL-17** sitokinlerini nasıl açıp kapattığını ve bunun metabolizmayı nasıl değiştirdiğini kanıtlar:

### 1. Karbonhidratlar ve "Jag2-Notch" Yolağı (IL-22'nin Baskılanması)
Bu yolak, yüksek karbonhidratlı beslenmenin bağışıklık hücresi fonksiyonunu değiştirerek bağırsak metabolizmasını nasıl yeniden programladığını gösterir.

*   **Mekanizma:** Diyette karbonhidrat oranı yükseldiğinde, bağırsak epitel hücreleri (IEC) ile dokuda yerleşik **$\gamma\delta$ T hücreleri** arasında özel bir sinyalizasyon başlar. IEC'ler yüzeylerinde **Jag2** ligandını ifade eder ve bu ligand T hücrelerindeki **Notch** reseptörüne bağlanır [1], [2].
*   **Sonuç:** Bu etkileşim, ortamdaki **ILC3** hücrelerinin (bağışıklık bekçileri) **IL-22** üretmesini baskılar.
*   **Biyokimyasal Etki:** IL-22 seviyesinin düşmesi, epitel hücrelerinde bir "metabolik şalteri" indirir. Hücreler lipid metabolizması genlerini kapatır ve glikoz/karbonhidrat metabolizması enzimlerini (sükraz-izomaltaz vb.) artırır [2], [3].
*   **Ders Notu:** "Yediğiniz şeker, sadece glikolize girmez; bağışıklık hücrelerine 'IL-22 üretimini durdur, şekeri işleyeceğiz' emrini verir."

### 2. Yağlar ve "Lipid Freni" Yolağı (IL-22 ile Emilim Kontrolü)
Bu mekanizma, bağışıklık sisteminin yağ emilimini aktif olarak nasıl sınırladığını (frenlediğini) anlatır.

*   **Mekanizma (Normal Durum):** Sağlıklı koşullarda veya mikrobiyota sinyalleriyle **ILC3** hücreleri **IL-22** salgılar. IL-22, epitel hücrelerindeki **STAT3** yolağını aktive eder [4], [5].
*   **Biyokimyasal Etki:** STAT3 aktivasyonu, bağırsak epitelindeki **lipid taşıyıcı genlerin (CD36 gibi) ekspresyonunu baskılar**. Yani IL-22, vücuda aşırı yağ girmesini engelleyen bir "fren" mekanizmasıdır [2], [6].
*   **Diyetteki Karşılığı:**
    *   **Yüksek Yağlı Diyet (HFD):** Aşırı yağlı beslenme, kolondaki ILC3 hücrelerinin kaybına neden olur. ILC3 gidince IL-22 üretimi durur. "Fren" ortadan kalktığı için bağırsak kontrolsüzce daha fazla yağ emmeye başlar ve obezite/insülin direnci şiddetlenir [6].
    *   **Sütten Kesilme (Örnek):** Bebeklikte anne sütünden (yağlı) katı gıdaya geçerken, CD4+ T hücreleri IL-22'yi baskılayarak yağ emiliminin artmasına izin verir [4].
*   **Ders Notu:** "Yağ emilimi pasif bir difüzyon değildir; IL-22 sitokini tarafından kontrol edilen immünolojik bir karardır."

### 3. Lipid Antijenleri ve "IL-17 Tetikleyicisi" (MAIT ve $\gamma\delta$ T Hücreleri)
Bu yolak, diyet yağlarının ve mikrobiyota ürünlerinin karaciğer ve yağ dokusunda inflamasyonu (IL-17) nasıl başlattığını gösterir.

*   **Mekanizma:** Bağırsak mikrobiyotası veya diyetle gelen lipidler, antijen sunan hücreler üzerindeki **CD1d** molekülü aracılığıyla **$\gamma\delta$ T hücrelerine** veya **MAIT** hücrelerine sunulur [7], [8].
*   **Sitokin Yanıtı:** Bu sunum, söz konusu hücrelerin yoğun miktarda **IL-17A** üretmesine neden olur.
*   **Biyokimyasal Etki:**
    *   **Karaciğerde:** Artan IL-17A, hepatositlerde yağ birikimini (steatoz) ve fibrozisi teşvik eder [9], [7].
    *   **Bağırsakta:** Yüksek yağlı diyetle artan MAIT kaynaklı IL-17A, bağırsak bariyerini bozarak geçirgenliği (leaky gut) artırır [10].
*   **Ders Notu:** "Diyet yağları, CD1d molekülü üzerinden bağışıklık sistemine 'saldırı var' mesajı vererek IL-17 üretimini tetikler ve bu da dokuyu yağlandırır."

**Özet Tablo (Ders İçin):**

| Makro Besin / Durum | İlgili İmmün Hücre | Hedef Sitokin | Metabolik Sonuç (Yolak) |
| :--- | :--- | :--- | :--- |
| **Yüksek Karbonhidrat** | $\gamma\delta$ T ve ILC3 | **IL-22 Azalır** ($\downarrow$) | Jag2-Notch ile IL-22 baskılanır $\rightarrow$ Şeker metabolizması artar [1, 2]. |
| **Diyet Yağları (Kontrol)** | ILC3 | **IL-22 Artar** ($\uparrow$) | STAT3 ile lipid taşıyıcıları baskılanır $\rightarrow$ Yağ emilimi sınırlanır [4, 5]. |
| **Aşırı Yağ / Obezite** | MAIT / $\gamma\delta$ T | **IL-17A Artar** ($\uparrow$) | CD1d sunumu $\rightarrow$ Karaciğer yağlanması ve bağırsak geçirgenliği artar [7, 10]. |
![[Pasted image 20260118144921.png]]

#figure İmmün Sistem ve İmmünonutrisyon
**Makale Başlığı:** Regulation of systemic metabolism by tissue-resident immune cell circuits
**DOI:** 10.1016/j.immuni.2023.05.001
**Amacı:** Bu derleme; karaciğer, gastrointestinal sistem ve yağ dokusundaki yerleşik bağışıklık hücrelerinin sistemik metabolizmayı düzenleyen devrelerini ve bu devrelerin organlar arası iletişimdeki rollerini incelemektedir.

---

Makaledeki **Figür 4**, bağışıklık hücrelerinin sadece bulundukları dokuyu değil, **organlar arası iletişimi (inter-organ crosstalk)** sağlayarak sistemik metabolizmayı, sirkadiyen ritmi ve insülin duyarlılığını nasıl yönettiklerini özetleyen kapsamlı bir şemadır [1].

Figür, Bağırsak (Gut), Karaciğer (Liver) ve Yağ Dokusu (Adipose) arasındaki karmaşık sinyal trafiğini iki ana panelde (A ve B) açıklamaktadır:

### A Paneli: Genel İletişim Ağı
Bu panel, organların birbirleriyle izole çalışmadığını, aksine şu moleküller aracılığıyla sürekli bir diyalog halinde olduğunu gösterir [1]:
*   **Sitokinler:** Bağışıklık hücrelerinin iletişim dili.
*   **Lipid Antijenleri:** Bağırsaktan gelip karaciğeri etkileyen mikrobiyal yağ parçaları.
*   **[[Adipokinler]] ve Hepatokinler:** Yağ ve karaciğerden salınan metabolik hormonlar (örn. FGF21, Adiponektin).

### B Paneli: Detaylı Mekanizmalar ve Yolaklar
Beslenme akademisyeni için figürün en kritik kısmı burasıdır. Diyet, mikrobiyota ve bağışıklık hücrelerinin organları birbirine bağlayan 5 ana mekanizmasını gösterir [1, 2]:

**1. Mikrobiyota-Bağırsak-Yağ Ekseni (IL-22 Freni):**
*   **Mekanizma:** Sağlıklı bağırsak mikropları, ILC3 hücrelerini uyararak **IL-22** üretimini sağlar. IL-22, epitelden yağ emilimini kısıtlayan (frenleyen) bir sinyaldir.
*   **Diyetin Etkisi:** Yüksek Yağlı Diyet (HFD), mikrobiyotayı değiştirir ve ILC3 kaynaklı IL-22 üretimini azaltır. "Fren" ortadan kalktığı için hem bağırsak hem de yağ dokusu kontrolsüzce daha fazla lipid emmeye başlar [1].

**2. Karaciğer-Yağ Ekseni (FGF21 Sinyali):**
*   **Bağlantı:** Bağırsak mikropları ve diyet, karaciğerdeki Kupffer hücrelerini (IL-1$\beta$ salgılar) ve monositleri (IL-12 salgılar) etkileyerek hepatositlerden **FGF21** (Fibroblast Growth Factor 21) üretimini modüle eder.
*   **Sonuç:** Karaciğerden salınan FGF21, yağ dokusuna giderek burada lipolizi (yağ yakımı), termogenezi ve **Adiponektin** üretimini artırır. Adiponektin ise dönüp karaciğerde insülin duyarlılığını iyileştirir [1].

**3. "Zehirli İletişim": Lipid Antijenleri (Karaciğer Hasarı):**
*   **Yolak:** Bağırsaktan sızan mikrobiyal lipid antijenleri, karaciğerdeki **CD1d+ Dendritik Hücreler** tarafından yakalanır ve **$\gamma\delta$ T hücrelerine** sunulur.
*   **Sonuç:** Bu etkileşim, karaciğerde inflamatuar **IL-17A** üretimini tetikler. IL-17A, karaciğerde yağ birikimine (steatoz) ve insülin direncine yol açar [1].

**4. Demir (Iron) Metabolizması ile Uzaktan Kontrol:**
*   **Mekanizma:** Yağ dokusundaki CSF1R+ miyeloid hücreler, yağ dokusunun demir alımını (transferrin-bağımlı) artırırsa; karaciğere giden demir azalır.
*   **Kritik Etki:** Yağ dokusundaki bu demir manipülasyonu, şaşırtıcı bir şekilde bağırsaklara sinyal göndererek **intestinal lipid emilimini azaltır**. Yani yağ dokusu, demiri kullanarak bağırsağın emilim vanasını kapatabilir [1, 2].

**5. Ekstrasellüler Veziküller (EVs) ve Sirkadiyen Senkronizasyon:**
*   **EVs:** Yağ dokusu, içinde miRNA ve metabolitler taşıyan veziküller (EVs) salgılayarak karaciğer ve bağırsağın gen ekspresyonunu değiştirebilir.
*   **Sirkadiyen:** Bağırsak mikroplarının gün içindeki döngüsel hareketleri (diurnal cycling), bağırsak epitelinin ve karaciğerin biyolojik saat genlerini (clock genes) senkronize eder. HFD bu ritmi bozar [1, 2].