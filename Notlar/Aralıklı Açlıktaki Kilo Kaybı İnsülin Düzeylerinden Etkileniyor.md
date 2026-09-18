---
Tür:
  - Besleyici
ODAK:
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[İnsülin Direnci]]"
DİZİN:
  - "[[Kilo Verme]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Aralıklı Açlığın Etkisi Alt Gruplara Göre Değişkenlik Gösteriyor]]"
  - "[[Hiperinsülinemi Açlık için Bir Fren Olabilir!]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ: "[[Farklı aralıklı açlık türleri yağ dağılımını ve fonksiyonelliğini farklı etkiliyor olabilir mi?]]"
  - "[[EMA_Appetite_GLP1_IF_Calisma_Fikri]]"
BAĞLANTILI DERSLER:
YORUM:
KAYNAK: https://doi.org/10.1016/j.celrep.2026.117023
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Adipoz Doku Lipolizi ve Termogenez Kontrolü"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Kişiselleştirilmiş Açlık]]"
  - "[[Aralıklı Açlığın Etkisi Alt Gruplara Göre Değişkenlik Gösteriyor]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["Açlık Sinyali"] --> B{"Bazal İnsülin Düzeyi"}
>     B -->|Normoinsülinemi| C["FoxO1 Nükleer Translokasyonu → IRF4 Aktivasyonu"]
>     C --> D["ATGL & HSL Aktivasyonu → Yağ Asidi Mobilizasyonu (Lipoliz)"]
>     B -->|Kronik Hiperinsülinemi| E["FoxO1 Dışlanması → IRF4 Baskılanması"]
>     E --> F["Yağ Kilitlenmesi → Kas Proteolizi (Alanin Salınımı) → Glukoneojenez"]
> ```
>
> **Şekil Açıklaması:** Açlık sinyali karşısında bazal insülin düzeyi substrat partisyonunu belirler: Normoinsülinemide FoxO1/IRF4 ekseni üzerinden ATGL ve HSL aktive olarak lipoliz sağlanırken; kronik hiperinsülinemide IRF4 baskılanarak yağ dokusu kilitlenir ve glukoneojenez için iskelet kası proteolizi (kas kaybı) zorunlu hale gelir.

> **Metodolojik Etiketler:** #finding/contradictory
IRF4 Nedir?

_Irf4_ (Interferon Düzenleyici Faktör 4), adipositlerde (yağ hücrelerinde) lipolizi (yağ yıkımını) aktive eden **kritik bir transkripsiyon faktörüdür**.

IRF4'ün genel özellikleri şunlardır:

1. **Regülasyon:** İnsülinin, **yağ hücrelerindeki (adiposit) IRF4 ekspresyonunu düşürerek** lipolizi transkripsiyonel olarak düzenlediği bilinmektedir.

2. **Lipoliz Aktivasyonu:** IRF4, lipolizi, **adipoz trigliserit lipaz (ATGL)** ve **hormon duyarlı lipaz (HSL)** ekspresyonu aracılığıyla düzenleyebilir ve aktive edebilir.

3. **Açlık Durumu:** IRF4'ün, akut açlık sırasında adipositlerde daha yüksek seviyelerde bulunduğu bilinmektedir, bu da yağ yıkımını başlattığını gösterir.

4. **Diğer Rolleri:** IRF4, kahverengi yağ dokusundaki (BAT) termojenik programı düzenler; ayrıca iskelet kasında glikojen ve glikoz metabolizmasını düzenleyebilir.

Bu Çalışmayla İlişkisi ve Önemi Nedir?

Bu çalışmanın ana hipotezi, obezite ile ilişkili yüksek insülin seviyelerinin, aralıklı oruç (IF) sırasında yağ kaybı yerine kas kaybını desteklemesidir. Çalışma, bu dengesizliği düzenleyen ana faktör olarak **insülin tarafından kontrol edilen adiposit IRF4'ü** tanımlamıştır.

**Çalışmadaki Önemli İlişkiler:**

1. **Hiperinsülinemi ve IRF4 İlişkisi:** Kronik olarak insülini yüksek olan farelerde (INS fareler), 10 haftalık 5:2 IF sonrasında yağ dokusunda **Irf4 gen ekspresyonunun anlamlı ölçüde daha düşük olduğu** bulunmuştur.

2. **IRF4 ve Kötü Sonuçların Benzerliği:** _Irf4_'ün vücut çapında veya sadece adipositlere özgü olarak silinmesi, kronik hiperinsülinemi ile gözlemlenen etkileri **fenokopilemiştir**. Yani, Irf4'ü silinen fareler, IF sırasında **daha az yağ kaybı ve daha fazla kas kütlesi kaybı** yaşamıştır.

**Mekanistik Etkiler:**

1. **Lipolizin Engellenmesi:** Yüksek insülin, FoxO1'in sitozolik sekestrasyonu yoluyla _Irf4_ ekspresyonunu azaltır ve bu da ATGL ile HSL ekspresyonunu düşürerek **lipolizi baskılar**.

2. **Yakıt Değişiminin Bozulması:** _AdipoIrf4_ farelerinde daha yüksek RER bulunmuştur → oruç sonrası **daha düşük yağ oksidasyonu** ve **artan karbonhidrat oksidasyonu**.

3. **Kas Kaybının Artması:** Yağ yakımının yetersiz kalması, vücudu **glukoneojenik amino asitlere** yönlendiriyor → iskelet kası kaybı artıyor.
