---
date: 2025-11-28
Tür:
  - Besleyici
ODAK:
  - "[[İstatistik]]"
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Mendelian Randomizasyon Nedir?]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[Biyoistatistik]]"
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Metabolik ve Moleküler Yanıtlar"
p_value_summary: "p < 0.05"
BESLEDİĞİ NOTLAR:
  - "[[SEM_Mediation_Moderation_Rehberi]]"
  - "[[Olcek_Uyarlama_Istatistik_Rehberi]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Ultra İşlenmiş Besin (Parçalanmış Gıda Matrisi)"] --> B["Hızlı Gastrointestinal Geçiş & Emilim"]
>     B --> C["Akut Glisemik / İnsülinemik Pikler"]
>     B --> D["Distal İleal Frenin Bypass Edilmesi"]
>     C & D --> E["Erken Acıkma & Hiperfaji"]
> ```
>
> **Şekil Açıklaması:** Ultra işlenmiş besinlerde tahrip edilmiş gıda matrisi, gastrointestinal geçişi hızlandırarak distal ileal fren mekanizmasını bypass eder. Bu durum hem akut glisemik/insülinemik piklere hem de tokluk sinyallerinin gecikmesiyle erken acıkma ve hiperfajiye yol açar.

# RCT Analiz Yöntemleri: 2 Grup ve Zaman Etkisi (ANOVA vs T-Test)

Bu not, Randomized Controlled Trial (RCT) çalışmalarında, özellikle sadece 2 grup olsa dahi neden ve nasıl ANOVA/ANCOVA kullanılması gerektiğine dair metodolojik detayları içerir.

## 1. Temel Soru: 2 Grup İçin ANOVA Yapılır mı?
**Cevap:** Evet, kesinlikle yapılır.
Literatürde (özellikle beslenme ve diyetetik çalışmalarında) sadece "Müdahale" ve "Kontrol" grubu olsa bile t-testi yerine ANOVA tercih edilmesinin temel nedenleri şunlardır:

### A. Zaman Faktörü (Time Factor)
RCT'lerde genellikle sadece sonuca değil, değişime bakılır.
- **T-testi:** Sadece "Son Test" veya sadece "Fark Puanları" (Delta) üzerinden tek kareye bakar.
- **Repeated Measures ANOVA:** Hem **Grup** (Diyet A vs Diyet B) hem de **Zaman** (Başlangıç vs Bitiş) faktörlerini aynı modelde analiz eder.

### B. Matematiksel Eşdeğerlik
Eğer zaman faktörü yoksa (sadece son ölçümler karşılaştırılıyorsa), 2 grup için yapılan One-Way ANOVA ile Bağımsız Örneklem T-testi matematiksel olarak aynıdır.
$$F = t^2$$
Bu formül gereği her iki test de **birebir aynı p değerini** verir.

---

## 2. Analiz Türü: Two-Way Mixed ANOVA
Beslenme müdahalelerinde "Zamanın Etkisi"ni modele katmak için kullanılan standart yöntemdir. SPSS'te *General Linear Model > Repeated Measures* altından yapılır.

Bu analiz çıktısında yorumlanması gereken 3 temel P değeri vardır:

### A. Main Effect of Time (Zamanın Temel Etkisi)
> [!QUESTION] Soru
> Katılımcılar hangi grupta olursa olsun, zaman içinde değişim gösterdi mi?

- **Anlamı:** Grupları birleştirip (pooling) bakar.
- **Örnek:** Hem diyet hem kontrol grubu zayıfladıysa bu değer anlamlı ($p < 0.05$) çıkar.

### B. Main Effect of Group (Grubun Temel Etkisi)
> [!QUESTION] Soru
> Zamanı bir kenara bırakırsak, genel ortalamada bir grup diğerinden farklı mı?

- **Anlamı:** T0 ve T1 ortalamalarını alıp kıyaslar.
- **Kısıtlılık:** Başlangıçta (randomizasyonda) gruplar eşitse, bu değerin tek başına anlamı zayıftır.

### C. Interaction Effect: Time x Group (Etkileşim Etkisi) ⭐
> [!IMPORTANT] En Kritik Değer
> **"Zaman içindeki değişim çizgileri gruplar arasında farklılık gösteriyor mu?"** sorusunun cevabıdır. Müdahalenin başarısını bu değer gösterir.

- **Senaryo:** Diyet grubu 10 kg verdi, Kontrol grubu 1 kg verdi.
- **Sonuç:** Etkileşim **Anlamlıdır ($p < 0.05$)**. Çünkü değişim eğimleri paralel değildir.
- **Görselleştirme:** *Interaction Plot* (Etkileşim Grafiği) ile gösterilir.
    - **Paralel Çizgiler:** Etkileşim Yok (Fark yok).
    - **Kesişen/Açılan Çizgiler:** Etkileşim Var (Müdahale etkili).

---

## 3. Kontrol Grubu Olmayan Çalışmalar (Head-to-Head)
Eğer "Pasif Kontrol" grubu yoksa ve iki farklı diyet (Örn: Ketojenik vs Akdeniz) kıyaslanıyorsa analiz stratejisi şu şekildedir:

### Seçenek 1: ANCOVA (Altın Standart)
Başlangıç değerlerindeki (baseline) olası şans eseri farkları yok etmek için kullanılır.
- **Bağımlı Değişken:** Son Test (T1)
- **Sabit Faktör:** Grup (Diyet A, Diyet B)
- **Covariate (Kovaryat):** Ön Test (T0)
> [!TIP] İpucu
> "Regression to the mean" hatasını minimize ettiği için hakemler tarafından sıkça tercih edilir.

### Seçenek 2: Delta ($\Delta$) Üzerinden T-Testi
En pratik yöntemdir.
1. Her kişi için fark hesapla: $\Delta = \text{Son} - \text{İlk}$
2. Bu fark puanlarını *Independent Samples T-test* ile karşılaştır.
> **Not:** Bu yöntem, Two-way ANOVA'daki *Interaction Effect* ile aynı sonucu verir.

---

## 4. Karar Ağacı (Özet)

| Durum | Kullanılacak Test | Amaç |
| :--- | :--- | :--- |
| **Sadece Son Test (2 Grup)** | Independent T-Test / One-Way ANOVA | Grupların bitiş değerlerini kıyaslamak. |
| **Ön Test + Son Test (RCT)** | **Two-Way Mixed ANOVA** | Zaman ve Grup etkileşimini (Interaction) görmek. |
| **Başlangıç Değerleri Farklıysa** | **ANCOVA** | Başlangıç değerini sabitleyerek (adjust) sonuca bakmak. |
| **Hızlı Sonuç (Manuel)** | Delta T-Test | Değişim miktarlarını kıyaslamak. |

---

## 5. Raporlama İpuçları
Eğer kontrol grubu yoksa, makalenin **Limitations** kısmına şu not düşülmelidir:
> "Since there was no passive control group, the results represent the **relative effectiveness** of Diet A compared to Diet B, rather than the absolute effect of the intervention solely."

