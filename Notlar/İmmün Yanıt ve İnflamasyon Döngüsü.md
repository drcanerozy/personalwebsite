---
Tür:
  - Çekirdek
ODAK:
  - "[[inflamasyon]]"
MEKANİZMA:
DİZİN:
  - "[[İmmün Sistem]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[İnflamasyon Döngüsü]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Metabolik ve Moleküler Yanıtlar"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[KC, AD ve GIS İmmün Hücrelerinde Öne Çıkanlar ve Metabolik Etkileri]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> **Metodolojik Etiketler:** #finding/contradictory
İnflamasyon ve yara iyileşmesi, vücudun hasara karşı verdiği dinamik ve hayati bir yanıttır. Beslenme ve diyetetik profesyonelleri için bu süreci anlamak, kronik hastalıkların beslenme ile yönetilmesinde (örneğin diyabetik yaralar veya obeziteye bağlı düşük dereceli inflamasyon) temel bir gerekliliktir [1], [2].

Kaynaklar doğrultusunda, bu süreci adım adım inceleyelim:

### 1) Sağlıklı Bir Döngü: Normal Yara İyileşmesi

Sağlıklı bir iyileşme süreci; **hemostaz, inflamasyon, proliferasyon (çoğalma) ve remodeling (yeniden şekillenme)** olmak üzere dört ana fazdan oluşur [3]. İnflamasyon fazı bu sürecin en kritik "yönetim" aşamasıdır.

**Adım Adım Hücresel Hareketler:**
1.  **Hasar ve Başlangıç Sinyalleri:** Bir doku hasarı oluştuğunda, trombositler bölgeye gelir ve büyüme faktörleri ile sitokinleri serbest bırakır (degranülasyon) [3].
2.  **Öncü Birliklerin (Nötrofiller) Gelişi:** Trombositlerden gelen sinyallerle bölgeye ilk olarak **nötrofiller** ulaşır [3]. Mast hücreleri de damar geçirgenliğini artırarak ve hücre dışı matrisi gevşeterek bu hücrelerin bölgeye sızmasına yardımcı olur [3].
3.  **Temizlik Başlıyor:** Nötrofiller, fagositoz yoluyla bakterileri ve yabancı cisimleri yutar; ayrıca daha fazla bağışıklık hücresini bölgeye çekmek için yoğun pro-inflamatuar sinyaller yayar [3].
4.  **Temizlik Timi (Makrofajlar) Devreye Giriyor:** Bölgeye göç eden monositler ve dokuda yerleşik makrofajlar, enkaz temizliğini devralır [3]. Bu aşamada makrofajlar **M1 (pro-inflamatuar)** yani "savaşçı" modundadır [4].
5.  **Programlı Ölüm (Apoptosis):** İşleri biten nötrofiller yaklaşık bir gün içinde "apoptosis" denilen programlı ölüme gider [3, 5]. Bu, sağlıklı bir döngü için şarttır çünkü hücrenin parçalanmadan, sessizce ölmesini sağlar [6].
6.  **"Beni Ye" Sinyali ve Dönüşüm:** Apoptotik hücrelerin yüzeyinde normalde içeride duran **fosfatidilserin (PS)** adlı bir molekül dışarı çıkar. Bu molekül makrofajlar için bir **"beni ye" (eat-me)** sinyalidir [7, 8].
7.  **Döngünün Tamamlanması (Eferositoz):** Makrofajlar bu ölü nötrofilleri yediğinde (eferositoz), kendi kimliklerini değiştirirler. M1 (savaşçı) modundan **M2 (tamirci/anti-inflamatuar)** moduna geçerler [3, 7]. Bu geçiş, TGF-β ve IL-10 gibi baskılayıcı sinyallerin salınmasını sağlar ve doku onarımı başlar [4, 7].

---

### 2) Kronik İnflamasyona Gidiş: Bozulmuş Döngü

Döngü bir noktada takılırsa, inflamasyon iyileşmeye hizmet etmek yerine dokuya zarar vermeye başlar [1].

**Adım Adım Kronikleşme Süreci:**
1.  **Sinyal Hatası veya Sürekli Uyarı:** Eğer antijen (hasar verici etken) bölgeden temizlenemezse veya makrofajlara "tamir moduna geç" diyen sinyaller gelmezse inflamasyon süresiz devam eder [4].
2.  **Hücresel Birikim:** Bölgede nötrofil, monosit ve makrofaj sayıları anormal derecede yüksek kalmaya devam eder [4].
3.  **Doku Tahribatı:** Nötrofiller bölgeden ayrılamadıkları için aşırı miktarda proteaz (protein yıkan enzim), reaktif oksijen türleri (ROS) ve "nötrofil ekstraselüler tuzakları" (NETs) salarak çevre dokuya zarar verirler [2, 4].
4.  **M1 Tuzağı:** Makrofajlar **M1 (pro-inflamatuar)** modunda takılı kalır ve M2 (tamirci) fazına geçemezler [4]. Bu durum TNF-α, IL-1β ve IL-6 gibi iltihabı körükleyen sitokinlerin sürekli salınmasına neden olur [2].
5.  **"Beni Yeme" Sinyali:** Özellikle yaşlanma veya kronik hastalıklarda, hücreler yüzeylerinde **CD47 ("beni yeme")** sinyalini artırarak bağışıklık sisteminden kaçabilirler. Bu da temizlenmesi gereken hücrelerin bölgede birikmesine yol açar [5, 9].
6.  **Sonuç:** İyileşmeyen diyabetik yaralar veya romatoid artrit gibi kronik hastalık tabloları oluşur [2].

---

### Bağışıklık Yanıt Döngüsü (Şematik Özet)

Aşağıdaki akış, sağlıklı bir döngünün nasıl bir "loop" oluşturduğunu özetler:

**HASAR/YARALANMA**
      ↓
**Trombosit Aktivasyonu** (Sinyal salınımı) [3]
      ↓
**Nötrofil ve Mast Hücresi Göçü** (Akut İnflamasyon Başlangıcı) [3]
      ↓
**Monosit/Makrofaj Göçü** (M1 Fazı: Enkaz temizliği ve sitokin salınımı) [3, 4]
      ↓
**Nötrofil Apoptosisi** (Fosfatidilserin - "Beni Ye" Sinyali) [6, 7]
      ↓
**Eferositoz** (Makrofajların ölü hücreleri yemesi) [3]
      ↓
**Fenotip Değişimi** (M1'den M2'ye geçiş: Anti-inflamatuar sitokin salınımı) [4, 7]
      ↓
**DOKU ONARIMI VE HOMEOTAZ** (Döngü başarıyla kapanır) [3, 10]

### Beslenme Profesyonelleri İçin Önemli Notlar
*   **DAMP'ler (Tehlike Sinyalleri):** Hücreler nekrozla (travmatik ölüm) öldüğünde dışarıya ATP veya HMGB1 gibi DAMP molekülleri salarlar [11, 12]. Bu moleküller inflamasyonu şiddetlendiren "alarm" zilleridir.
*   **İnflammaging:** Yaşlanma, obezite ve çevresel faktörler bağışıklık sisteminde kusurlara yol açarak sürekli bir "düşük dereceli inflamasyon" (inflammaging) yaratır [13]. Bu durumda makrofajların temizleme yeteneği azalır [13].
*   **Senolytics:** Quercetin ve Fisetin gibi bazı bileşiklerin (senolitikler), senesent (yaşlı) hücreleri azaltarak makrofajların tamir moduna (M2) geçmesine yardımcı olabileceği araştırılmaktadır [14, 15].

**Metafor:** Sağlıklı inflamasyonu, bir evdeki yangını söndürmeye gelen itfaiye ekibine benzetebiliriz. İtfaiyeciler (nötrofiller) yangını söndürür, sonra temizlik ekibi (makrofajlar) gelir. Temizlik bitince ekip gider ve inşaat başlar. Kronik inflamasyonda ise itfaiye ve temizlik ekibi evden hiç çıkmaz; sürekli balta ve su kullanarak evin sağlam kalan kısımlarına da zarar verirler [4, 16].
