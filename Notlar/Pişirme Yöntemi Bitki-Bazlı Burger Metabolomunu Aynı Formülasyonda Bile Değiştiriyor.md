---
Tür:
  - Besleyici
ODAK:
  - "[[Ultra İşlenmiş Besinler]]"
MEKANİZMA:
  - "[[Biyokimya/Metabolizma]]"
BAĞLANTILI NOTLAR:
  - "[[UPF Tüketimi Metabolitlerle Belirlenebilir Mi?]]"
  - "[[Fenolik Bileşiklerin Posayla Etkileşimi]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[ev-yapimi-upf-kavrami]]"
  - "[[upf-siniflandirma-tutarsizligi-calisma-fikri]]"
BAĞLANTILI DERSLER:
  - "[[BES339 Diyet İlkeleri ve Popüler Diyetler]]"
YORUM: MetaboLights taramasında bulundu (2026-08). Aynı formülasyon/hammaddenin farklı pişirme/işleme yöntemleriyle metabolomik imzasının nasıl değiştiğini gösteren, "ev yapımı UPF" fikri için metodolojik şablon niteliğinde bir çalışma.
KAYNAK: https://www.sciencedirect.com/science/article/abs/pii/S0308814625044292 (de Vargas et al., Food Chemistry, Vol 502, 2026, Art. 147755) — MetaboLights: https://www.ebi.ac.uk/metabolights/MTBLS12849
study_type: "Kontrollü laboratuvar deneyi (untargeted metabolomik)"
evidence_direction: "positive"
primary_outcome: "Pişirme yöntemi (termal işlem) kaynaklı metabolit profili değişimi"
p_value_summary: "belirtilmedi (özet düzeyinde; PCA ile ayrışma raporlanmış)"
BESLEDİĞİ NOTLAR:
  - "[[UPF Sınıflandırma Yöntemleri ve Aralarındaki Tutarsızlıklar]]"
  - "[[UPF sınıflandırmasına bilimsel yaklaşım önerileri, IAFNS 2026 Önerileri]]"
DİZİN:
  - "[[Ultra İşlenmiş Besinler]]"
ETİKET: makaleden

---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Aynı Nohut-Bazlı Burger Formülasyonu (Ham)"] --> B["4 Farklı Pişirme Yöntemi: Air-Fryer / Izgara / Fırın / Mikrodalga"]
>     B --> C["Termal İşlem Yoğunluğu ve Süresi Farklılaşıyor"]
>     C --> D["Isıya-Duyarlı Lipid ve Flavonoidlerin Farklı Derecede Degradasyonu"]
>     D --> E["Untargeted Metabolomik Profilde Ölçülebilir Ayrışma (PCA: Çiğ vs Pişmiş, Yönteme Göre)"]
> ```
>
> **Şekil Açıklaması:** Formülasyon (hammadde, oran, katkı) tamamen sabit tutulsa bile, sadece pişirme/işleme yöntemi değiştirildiğinde metabolomik profil ölçülebilir şekilde ayrışıyor — yani "işleme" değişkeni besin kompozisyonundan bağımsız bir eksen olarak izole edilebiliyor.

### 1. Araştırma Tasarımı

Nohut-bazlı (chickpea-based) bitkisel burgerler tek bir formülasyonla üretilmiş; ardından dört farklı yaygın ev/ticari pişirme yöntemine (air frying, ızgara, fırında pişirme, mikrodalga) tabi tutulmuş. Untargeted metabolomik yöntemle çiğ ve pişmiş örnekler karşılaştırılmış.

### 2. Öne Çıkan Bulgular

- Varyansın birincil kaynağı termal işlem olmuş: çiğ örnekler PCA'da pişmiş örneklerden net şekilde ayrışıyor.
- Isıya duyarlı bileşikler (lipidler, çeşitli flavonoidler) **tüm pişirme yöntemlerinde** degrade olmuş — yani etki yönteme özgü değil, ısıl işlemin kendisine bağlı.
- Pişirme yöntemleri arasında da (air-fryer vs ızgara vs fırın vs mikrodalga) metabolit profili farklılaşıyor, yani ısı iletim biçimi/süresi de ayrı bir değişken.

### 3. Neden Not Aldık / Nasıl Kullanılabilir

Bu çalışma, [[ev-yapimi-upf-kavrami]] fikrindeki temel hipotezin ("aynı hammadde/tarif, farklı işleme tekniğiyle farklı bir metabolomik/matriks imzasına dönüşebilir") **doğrudan metodolojik kanıtı ve prototipi**: burada değişken pişirme yöntemi, senin fikrinde ise blenderleme/izolasyon/homojenizasyon gibi ev-mutfağı teknikleri — ama mantık aynı: **formülasyonu sabit tutup sadece işleme tekniğini değiştirerek metabolomik ayrışmayı izole etme tasarımı**.

Pratik kullanım alanları:
- **Deney tasarımı şablonu:** Kendi pilot çalışman için (ev yapımı tarif vs "UPF'leştirilmiş" aynı tarif) doğrudan uyarlanabilir bir kontrollü-formülasyon + çoklu-işleme-yöntemi tasarımı sunuyor.
- **Kavramsal destek:** "İşleme derecesi, kompozisyondan bağımsız ölçülebilir bir metabolomik imza bırakır" tezini destekleyen ampirik bir örnek olarak [[upf-siniflandirma-tutarsizligi-calisma-fikri]] ve [[nova-grup4-nutrient-adjustment-calisma-plani]] için atıf kaynağı.
- MetaboLights'taki ham LC-HRMS verisi (MTBLS12849, 106 örnek) teorik olarak reanaliz edilebilir durumda — istersen bu veriyi kendi işleme-derecesi metriklerinle (ör. bir "işleme yoğunluğu skoru") yeniden etiketleyip metabolomik ayrışmayla ne kadar örtüştüğünü test edebiliriz.
