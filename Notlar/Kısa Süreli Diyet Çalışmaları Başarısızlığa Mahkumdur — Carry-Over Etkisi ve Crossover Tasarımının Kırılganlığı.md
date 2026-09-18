---
Tür:
  - Çekirdek
ODAK:
  - "[[Çalışma Tasarımı]]"
  - "[[Crossover Çalışmalar]]"
  - "[[Beslenme Bilimi Metodolojisi]]"
MEKANİZMA:
  - "[[Carry-Over Etkisi]]"
  - "[[Adaptif Termojenez]]"
DİZİN:
  - "[[00_Araştırma Metodolojisi_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Vücut Ağırlığı Modelleri ve Obezite Hipotezlerine Göre Kilo Kaybında Plato Dönemi]]"
  - "[[Kalori kısıtlamasında gözlenen bireysel farklılıklar]]"
  - "[[Semaglutid, Metabolik Adaptasyonu Kötüleştirmiyor]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
  - "[[TRF_Tutumlu-Savurgan_Fenotip_Calisma_Taslagi]]"
BAĞLANTILI DERSLER:
  - "[[Araştırma Yöntemleri]]"
YORUM: "Ludwig'in carry-over argümanı bizim IF crossover audit fikrimizin tam teorik zeminini sağlıyor. Hall et al. 2021'deki 2000 kcal/gün carry-over büyüklüğü alan için utanç verici bir rakam. Kendi crossover çalışmalarında wash-out yeterliliği standart haline gelmeli."
KAYNAK: https://davidludwigmd.medium.com/designed-to-fail-44d278e591a6
study_type: "Perspective/Opinion"
evidence_direction: "negative"
primary_outcome: "Crossover Tasarım Geçerliliği ve Carry-Over Etkisi"
p_value_summary: "Raporlanmamış (Perspektif Makalesi)"
BESLEDİĞİ NOTLAR:
  - "[[Beslenme Biliminde Paradigma Çatışması ve Duraksama]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["Crossover Çalışma Tasarımı\n(A → Wash-out → B)"] --> B{"Wash-out Yeterli mi?"}
>     B -->|Evet ≥2 ay| C["Temiz Karşılaştırma\nA ve B etkileri izole"]
>     B -->|Hayır <2 hafta| D["A Diyetinin Metabolik\nArkalığı Devam Ediyor"]
>     D --> E["B Dönemi Verisine Sızma\n(Carry-Over Etkisi)"]
>     E --> F["Sistematik Yanlılık\nİyileşen grup daha kötü,\nKötüleşen grup daha iyi görünür"]
>     F --> G["İstatistiksel Analiz Geçersiz\n'Sadece 1. dönem verisi kullanılabilir'\n— Varma 1974'ten bu yana konsensüs"]
>     G --> H["Sonuç: Milyonlarca $\nve Yanlış Çıkarım"]
> ```
>
> **Şekil Açıklaması:** Wash-out süresi yetersiz olduğunda önceki diyetin metabolik, hormonal ve mikrobiyota izi bir sonraki döneme sızar; bu carry-over etkisi sistematik yanlılık yaratarak crossover tasarımını geçersiz kılar. 1974'ten bu yana istatistik literatüründeki konsensüs: carry-over varsa ikinci dönem verisi kullanılamaz.

> **Metodolojik Etiketler:** #finding/negative #design/crossover #bias/carryover

### İçindekiler

- [[#Temel Argüman]]
- [[#Problem 1 — Adaptasyon Süresi]]
- [[#Problem 2 — Carry-Over Etkisi]]
- [[#Somut Örnek Hall et al. 2021]]
- [[#Çözüm Önerisi]]
- [[#Carry-Over Nedir — İstatistik 101]]

---

### Temel Argüman

Ludwig (2025), ABD federal hükümetinin 170 milyon dolarlık "Nutrition for Precision Health" programını örnek göstererek kısa süreli diyet çalışmalarının iki yapısal nedenden ötürü kronik hastalık sorusuna yanıt veremeyeceğini savunuyor: vücudun diyet değişikliğine tam adaptasyonu haftalar-aylar gerektiriyor; crossover tasarımı bu kısa süreli çalışmalarda carry-over etkisine kaçınılmaz olarak maruz kalıyor.

Temel analoji: Yoğun egzersiz vs. sedanter karşılaştırması, 2 haftalık crossover'da test edilirse — egzersiz yapanlar yorgun ve ağrılı, ölçüm "egzersiz kötü" çıkar. Bunun yerine uzun vadeli bir çalışma yapmak gerekir.

---

### Problem 1 — Adaptasyon Süresi

Büyük bir diyet değişikliğine vücudun tam adaptasyonu **haftalar ila aylar** alır. 2 haftalık bir pencere yalnızca geçiş semptomlarını ölçer, kronik etkiyi değil.

Somut örnek: Hall et al.'ın UPF vs. işlenmemiş diyet çalışmasında (2 haftalık inpatient), UPF grubunun aşırı enerji alımı **günde ~25 kcal** azalarak sürdü — bu trendle ilerlenirse iki diyet iki hafta sonra farksızlaşırdı. Replication çalışmasında etki yalnızca 1 haftada zayıflamıştı.

Keto gribi de aynı mekanizma: Habitual yüksek KH alanlarda low-carb'a geçişin ilk haftaları yorgunluk ve performans düşüşü yaratır. Bu adaptasyon sancısını diyetin uzun vadeli etkisiyle karıştırmak sistematik bir hata.

---

### Problem 2 — Carry-Over Etkisi

Crossover tasarımda katılımcı sırayla birden fazla diyeti alır. Önceki diyetin metabolik, hormonal veya mikrobiyota etkisi **tam olarak temizlenmeden** bir sonraki döneme geçilirse bu etki yeni döneme sızar.

**Egzersiz analojisiyle:**
- A grubu: Önce yoğun egzersiz → ardından sedanter. Sedanter dönemde geç adaptasyon faydası (toparlanma, gecikmiş kas gelişimi) yaşanır → sedanter *iyi görünür.*
- B grubu: Önce sedanter → ardından egzersiz. Kondisyon iyice düşmüş, egzersiz daha zor → egzersiz *kötü görünür.*

Carry-over etkisi: egzersizi olduğundan kötü, sedantarliği olduğundan iyi gösterir. Sonuç gerçekliğin tam tersi.

**Diyete uygulandığında:** Habitual yüksek KH alanlarda low-carb dönemi her zaman adaptasyon semptomlarıyla başlar → low-carb sistematik olarak dezavantajlı pozisyona düşer.

---

### Somut Örnek: Hall et al. 2021

Hall et al. (2021, *Nature Medicine*): 2 haftalık crossover, low-carb vs. low-fat. Sonuç: low-carb kolunda gönüllü enerji alımı daha yüksek → CIM ile çelişiyor şeklinde yorumlandı.

Ludwig grubu bu çalışmada **carry-over etkisinin 2000 kcal/gün büyüklüğünde** olduğunu gösterdi. Yani ölçülen etki gerçek diyet farkından değil, önceki dönemin artıklarından kaynaklanıyordu.

Hall cephesinin yanıtı: "Analizler pre-specified'dı, post-hoc analiz bias getirir, sonuçlar hâlâ geçerli." — İki taraf hâlâ tartışıyor. Milyonlarca dolar harcanmış, tekrarlama olası değil.

---

### Çözüm Önerisi

Ludwig'in önerileri:

1. **Diyet kolları en az 2 ay** olmalı (adaptasyona izin vermek için).
2. **Wash-out en az 2 ay** olmalı (carry-over temizlemek için).
3. Crossover yerine mümkünse **paralel grup tasarımı** tercih edilmeli.
4. Federal fonlamanın 170 milyon $'ı birkaç büyük kısa çalışmaya değil, **2+ yıllık uzun vadeli paralel çalışmalara** yönlendirilmeli.
5. İlaç için 2 haftalık veri asla onay alamazken, beslenme önerileri 2 haftalık verilerle şekillendiriliyor — bu standart çifte tutumlu.

---

### Carry-Over Nedir — İstatistik 101

Carry-over etkisi, A→B crossover'da A'nın etkisinin B dönemine taşınmasıdır. İstatistik kitapları 1974'ten bu yana şunu söylüyor:

> "Carry-over varsa ikinci dönem verisi kullanılamaz; yalnızca birinci dönem verisiyle analiz yapılır — bu da ikinci dönem çalışmayı anlamsız kılar."
> — Varma (1974), Hill (1979), Armitage (1982), FDA (2001) ve diğerleri

Wash-out süresi bu sızmanın önüne geçmek içindir. Wash-out yeterince uzun değilse, carry-over varlığı test edilse bile differential carry-over'ı period × treatment interaction'dan ayırt etmek istatistiksel olarak güçsüzdür (Freeman, 1989).

**Pratik kural:** Diyetin fizyolojik izi ne kadar sürüyorsa wash-out en az o kadar olmalı. Metabolomik, mikrobiyota, hormon ve epigenetik değişiklikler için bu süre çoğu zaman haftaları değil, ayları kapsıyor.

---

### Bibliyografya

- Ludwig DS (2025). Designed to Fail: Why Short-term Diet Trials Cannot Solve the Epidemics of Chronic Disease. *STAT News First Opinion* / Medium. https://davidludwigmd.medium.com/designed-to-fail-44d278e591a6
- Hall KD et al. (2021). Ultra-processed diets cause excess calorie intake and weight gain. *Nature Medicine*. DOI: 10.1038/s41591-020-01209-1
- Ebbeling CB et al. (2018). Effects of a low carbohydrate diet on energy expenditure during weight loss maintenance. *BMJ* 363:k4583.
