---
ODAK:
  - "[[İstatistik]]"
Tür:
  - Çekirdek
BAĞLANTILI NOTLAR:
  - "[[Olcek_Uyarlama_Istatistik_Rehberi]]"
study_type: Metodoloji Rehberi
evidence_direction: null
primary_outcome: SEM ve aracılık/düzenleyicilik analizleri
p_value_summary: N/A
BESLEDİĞİ NOTLAR:
  - "[[Olcek_Uyarlama_Istatistik_Rehberi]]"
MEKANİZMA:
  - "[[Metodoloji]]"
DİZİN:
  - "[[SEM]]"
ETİKET: dersten

---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> **Metodolojik Etiketler:** #finding/null
# Yapısal Eşitlik Modellemesi (SEM), Aracılık (Mediation) ve
# Düzenleyicilik (Moderation) Analizleri — Uygulamalı Rehber
### Beslenme ve Diyetetik Alanı İçin

> Bu rehber, CFA'nın (ölçüm modeli) ötesine geçip **değişkenler arasında yön/etki/nedensellik iddia eden** modelleri anlatır: tam Yapısal Eşitlik Modeli (SEM), aracılık (mediation) ve düzenleyicilik (moderation) analizleri. Bol örnekli, pratik/uygulamalı bir yaklaşımla, jamovi adımlarıyla birlikte.

---

## İÇİNDEKİLER

1. CFA'dan SEM'e: Temel Fark Nedir?
2. Path Analysis (Yol Analizi) — SEM'in En Basit Hali
3. Aracılık (Mediation) Analizi
4. Düzenleyicilik (Moderation) Analizi
5. Mediation vs. Moderation — Kafa Karışıklığını Bitirecek Karşılaştırma
6. İleri Konular: Moderated Mediation, Çoklu Aracı/Düzenleyici
7. Model Uyumu ve Raporlama
8. jamovi'de Baştan Sona Uygulama
9. Sözlük

---

## 1. CFA'DAN SEM'E: TEMEL FARK NEDİR?

Daha önceki rehberde CFA'yı işlemiştik — CFA sadece şunu sorar: **"Bu maddeler, bu gizil faktörün göstergeleri mi?"** Yön hep aynıdır: faktör → maddeler.

**Tam SEM**, buna ek olarak **gizil (ya da gözlemlenen) değişkenler arasında yönlü ilişkiler** (regresyon benzeri oklar) ekler. Yani SEM = **Ölçüm Modeli (CFA) + Yapısal Model (regresyon yolları)**.

**Basit bir benzetme:** CFA, "bu tuğlalar gerçekten bir duvar mı oluşturuyor?" sorusuna cevap verir. SEM ise "bu duvar, üstündeki çatıyı taşıyor mu?" sorusuna — yani parçaların birbirini nasıl **etkilediğine** bakar.

### Beslenme alanından somut örnek

Diyelim ki elinizde üç ölçülmüş (ya da gizil) kavram var:
- **Algılanan Stres** (Perceived Stress Scale ile ölçülmüş)
- **Duygusal Yeme** (Emotional Eating Scale ile ölçülmüş)
- **BMI**

Sadece korelasyona bakmak yerine, SEM ile şunu test edebilirsiniz:

```
Stres ──────────────► Duygusal Yeme ──────────────► BMI
  (β=0.42, p<.001)                    (β=0.31, p<.001)
```

Bu model, "stres, duygusal yeme **üzerinden**, BMI'yi etkiliyor" gibi bir **mekanizma** iddiası taşır — sadece "üçü de birbiriyle ilişkili" demekten çok daha güçlü, açıklayıcı bir bilgi verir.

---

## 2. PATH ANALYSIS (YOL ANALİZİ) — SEM'İN EN BASİT HALİ

**Path analysis**, SEM'in gizil değişken (faktör) içermeyen, sadece **gözlemlenen (doğrudan ölçülmüş) değişkenler arasındaki** regresyon yollarını test eden basit halidir. Genelde SEM öğrenmeye buradan başlanır.

### Temel kavramlar

| Terim | Anlamı |
|---|---|
| **Dışsal (Exogenous) değişken** | Modelde başka hiçbir değişken tarafından "yordanmayan", sadece etkileyen değişken (okun sadece çıktığı, hiç girmediği) |
| **İçsel (Endogenous) değişken** | Modelde en az bir değişken tarafından yordanan (okun girdiği) değişken |
| **Doğrudan etki (Direct effect)** | A'dan B'ye tek bir ok |
| **Dolaylı etki (Indirect effect)** | A'dan B'ye, bir ya da daha fazla ara değişken üzerinden giden yol |
| **Toplam etki (Total effect)** | Doğrudan + tüm dolaylı etkilerin toplamı |

---

## 3. ARACILIK (MEDIATION) ANALİZİ

### Ne işe yarar, hangi soruyu cevaplar?

Mediation, **"X, Y'yi NEDEN/NASIL etkiliyor?"** sorusuna cevap arar — aradaki **mekanizmayı** (M = aracı/mediator değişken) test eder.

**Mantık:** X → M → Y. X, önce M'yi etkiler, M de Y'yi etkiler; böylece X'in Y üzerindeki etkisinin bir kısmı (ya da tamamı) M **üzerinden** gerçekleşir.

### Beslenme alanından örnek

> **Araştırma sorusu:** "Beslenme okuryazarlığı (X), diyet kalitesini (Y) neden etkiliyor?"
> **Hipotez:** Çünkü beslenme okuryazarlığı yüksek olanlar, gıda etiketlerini daha iyi okuyor (M = etiket okuma davranışı), bu da diyet kalitesini artırıyor.

```
                    M (Etiket Okuma Davranışı)
                   ╱                          ╲
                  ╱ a (X→M)          b (M→Y)  ╲
                 ╱                              ╲
     X (Beslenme Okuryazarlığı) ────────────► Y (Diyet Kalitesi)
                        c' (doğrudan etki, "direct effect")
```

### Temel parametreler

| Sembol | Anlamı |
|---|---|
| **a** | X'in M üzerindeki etkisi (X→M yolu) |
| **b** | M'nin Y üzerindeki etkisi (X kontrol edilerek, M→Y yolu) |
| **c (toplam etki / total effect)** | X'in Y üzerindeki, M hiç modelde yokken ölçülen ham etkisi |
| **c' (doğrudan etki / direct effect)** | X'in Y üzerindeki, M modele girdikten SONRA kalan etkisi |
| **a×b (dolaylı etki / indirect effect)** | Aracılık etkisinin büyüklüğü — asıl ilgilendiğimiz sayı budur |

**Mantık kontrolü:** c = c' + (a×b) her zaman doğru olmalı (toplam etki = doğrudan + dolaylı).

### Tam mı, kısmi mi aracılık?

| Sonuç | Yorum |
|---|---|
| c' ≈ 0 (anlamsız), a×b anlamlı | **Tam aracılık (full mediation)** — X'in Y'ye etkisi tamamen M üzerinden |
| c' anlamlı ve a×b de anlamlı | **Kısmi aracılık (partial mediation)** — etkinin bir kısmı M üzerinden, bir kısmı doğrudan |
| a×b anlamsız | Aracılık yok |

### İstatistiksel anlamlılık nasıl test edilir?

**⚠️ Eski/yanlış yöntem:** Sobel testi — a×b'nin dağılımının normal olduğunu varsayar, ama gerçekte **çarpık (skewed)** bir dağılımdır, bu yüzden Sobel testi günümüzde önerilmez.

**✅ Güncel/doğru yöntem: Bootstrap Güven Aralığı**
- Veri setinden binlerce kez (genelde 5.000-10.000) **yerine koyarak (with replacement)** yeniden örneklem çekilir, her seferinde a×b hesaplanır, bu dağılımdan **%95 güven aralığı** elde edilir.
- **Karar kuralı: Güven aralığı sıfırı içermiyorsa** (örn. [0.08, 0.24] gibi, aralıkta 0 yoksa), dolaylı etki **anlamlıdır**.
- jamovi'de bu otomatik yapılır, elle hesaplama gerekmez.

### jamovi'de Mediation Analizi

jamovi'nin araç çubuğunda **"medmod"** modülü tam bu iş için var (sizin ekran görüntünüzde de görmüştük):

1. Analyses > **medmod** > **Mediation**.
2. **Dependent Variable (Y):** Diyet kalitesi.
3. **Mediators (M):** Etiket okuma davranışı.
4. **Predictors (X):** Beslenme okuryazarlığı puanı.
5. Çıktıda: Direct Effect (c'), Indirect Effect (a×b) + bootstrap %95 GA, Total Effect (c) tabloları otomatik gelir.
6. **Bootstrap sayısını** (varsayılan genelde 1000-5000) artırabilirsiniz — 5000+ önerilir, daha kararlı sonuç verir.

---

## 4. DÜZENLEYİCİLİK (MODERATION) ANALİZİ

### Ne işe yarar, hangi soruyu cevaplar?

Moderation, **"X'in Y üzerindeki etkisi, KİMDE/NE ZAMAN/HANGİ KOŞULDA daha güçlü ya da daha zayıf?"** sorusuna cevap arar.

**Mantık:** X → Y ilişkisinin **gücü/yönü**, üçüncü bir değişkene (W = düzenleyici/moderator) göre değişir. Mediation'daki gibi bir "aradaki mekanizma" değil, **"ilişkinin kimde daha güçlü olduğu"** sorusu.

### Beslenme alanından örnek

> **Araştırma sorusu:** "Beslenme okuryazarlığının diyet kalitesi üzerindeki etkisi, gelir düzeyine göre değişir mi?"
> **Hipotez:** Beslenme okuryazarlığı yüksek olsa bile, düşük gelirli bireyler sağlıklı gıdaya erişemediği için bu bilgiyi diyetlerine yansıtamayabilir — yani etki, **yüksek gelirlilerde daha güçlü** olabilir.

```
X (Beslenme Okuryazarlığı) ──────────────► Y (Diyet Kalitesi)
                                  ▲
                                  │
                    W (Gelir Düzeyi) — düzenleyici
```

İstatistiksel olarak bu, bir **etkileşim terimi (interaction term, X×W)** ile test edilir:

```
Y = b0 + b1(X) + b2(W) + b3(X×W) + hata
```

**b3 (etkileşim katsayısı) anlamlıysa**, X'in Y üzerindeki etkisi gerçekten W'ye göre değişiyor demektir.

### Basit Eğim (Simple Slope) Analizi

Etkileşim anlamlı çıktıktan sonra, **"tam olarak nasıl değişiyor"** sorusunu cevaplamak için, düzenleyici değişkenin üç düzeyinde (genelde **ortalama, ortalama-1SS, ortalama+1SS**) X→Y eğimi ayrı ayrı hesaplanır ve genelde bir grafikle gösterilir:

```
Diyet         │                              ╱ Yüksek Gelir (dik eğim)
Kalitesi      │                         ╱
              │                    ╱
              │               ╱  ─ ─ ─ Düşük Gelir (yatay eğim)
              │          ╱ ─ ─
              └──────────────────────────────► Beslenme Okuryazarlığı
```

### Kategorik düzenleyiciler

Düzenleyici değişken **kategorik** de olabilir (örn. cinsiyet, tedavi grubu vs. kontrol grubu) — bu durumda "simple slope" yerine **her grup için ayrı regresyon eğimi** karşılaştırılır, mantık aynıdır.

### jamovi'de Moderation Analizi

1. Analyses > **medmod** > **Moderation**.
2. **Dependent Variable (Y):** Diyet kalitesi.
3. **Predictor (X):** Beslenme okuryazarlığı.
4. **Moderator (W):** Gelir düzeyi.
5. jamovi otomatik olarak X, W ve X×W etkileşim terimini modele girer.
6. **"Simple Slope Estimates"** ve **"Simple Slope Plot"** kutucuklarını işaretleyin — hem sayısal hem görsel çıktı alırsınız.

**⚠️ Önemli teknik detay — merkezileme (centering):** Etkileşim terimi hesaplanmadan önce X ve W değişkenlerinin **ortalamadan merkezi hale getirilmesi (mean-centering)** önerilir — bu, çoklu doğrusal bağlantı (multicollinearity) sorununu azaltır ve katsayıların yorumunu kolaylaştırır. jamovi'nin medmod modülü bunu genelde otomatik yapar, ama çıktıda kontrol edin.

---

## 5. MEDIATION vs. MODERATION — KAFA KARIŞIKLIĞINI BİTİRECEK KARŞILAŞTIRMA

| | **Mediation (Aracılık)** | **Moderation (Düzenleyicilik)** |
|---|---|---|
| **Soru** | X, Y'yi **NEDEN/NASIL** etkiler? | X→Y ilişkisi **KİMDE/NE ZAMAN** daha güçlü? |
| **Üçüncü değişkenin rolü** | Ara halka, **mekanizma** | Etkinin gücünü değiştiren **koşul** |
| **Diyagram** | X → M → Y (zincir) | X → Y, W bu okun **üzerine** etki eder |
| **İstatistiksel test** | Dolaylı etki (a×b), bootstrap GA | Etkileşim terimi (X×W), b3 katsayısı |
| **Beslenme örneği** | Stres → Duygusal Yeme → Kilo Alımı | Diyet Programı Etkisi × Sosyal Destek Düzeyi |
| **Sonucun ifadesi** | "...üzerinden etkiliyor" | "...bağlı olarak değişiyor" / "...için daha geçerli" |

### Basit hafıza tekniği
- **Mediation = "Neden" sorusuna cevap, bir ZİNCİR.**
- **Moderation = "Kimde/Ne zaman" sorusuna cevap, bir ÇARPAN/KOŞUL.**

Bir başka pratik ayrım testi: Üçüncü değişkeniniz (M ya da W), **X'ten sonra, zaman içinde X tarafından etkilenerek mi oluşuyor** (→ muhtemelen mediator, örn. stres önce olur, duygusal yeme sonra gelişir) yoksa **X ile aynı anda var olan, X'ten etkilenmeyen sabit bir özellik mi** (→ muhtemelen moderator, örn. cinsiyet, gelir düzeyi zaten oradaydı)?

---

## 6. İLERİ KONULAR

### 6.1 Moderated Mediation (Düzenlenmiş Aracılık / Conditional Process Analysis)

Bazen aracılık etkisinin **kendisi** bir düzenleyiciye göre değişir — yani "X, M üzerinden Y'yi etkiliyor, ama bu dolaylı etki W'ye göre değişiyor." Bu, mediation ve moderation'ın **birleşimidir** (Hayes'in "Model 7", "Model 14" gibi adlandırdığı kalıplar buraya girer).

**Beslenme örneği:** "Stres, duygusal yeme üzerinden kilo alımını etkiliyor — ama bu dolaylı etki, sosyal destek düzeyi yüksek olanlarda daha zayıf."

### 6.2 Çoklu Aracı (Multiple Mediators)

Birden fazla aracı değişken **aynı modelde, paralel ya da seri** olarak test edilebilir:
- **Paralel:** X → M1 → Y ve X → M2 → Y aynı anda (iki ayrı mekanizma).
- **Seri:** X → M1 → M2 → Y (bir mekanizma diğerini tetikliyor).

### 6.3 Çoklu Düzenleyici (Multiple Moderators)

Birden fazla düzenleyici aynı modelde test edilebilir, ama **3'lü etkileşimler (X×W1×W2)** yorumlanması çok zorlaşan, dikkatli kullanılması gereken bir alandır — çok gerekli olmadıkça önerilmez.

---

## 7. MODEL UYUMU VE RAPORLAMA

Tam SEM modelleri için de **CFA rehberinde anlattığımız fit indeksleri** (χ²/df, CFI, TLI, RMSEA, SRMR) aynen geçerlidir — çünkü tam SEM, ölçüm modeli (CFA) + yapısal model (path'ler) birleşimidir, uyum yine bütün model için değerlendirilir.

**Ek olarak raporlanması gerekenler:**
- Her yol için: standartlaştırılmış katsayı (β), standart hata (SE), p-değeri
- Mediation'da: dolaylı etki + bootstrap %95 GA (mutlaka)
- Moderation'da: etkileşim terimi katsayısı + basit eğim grafiği
- **R² (açıklanan varyans):** Y değişkenindeki varyansın modelin tamamı tarafından ne kadarının açıklandığı (0-1 arası, % olarak da ifade edilir)

---

## 8. jamovi'DE BAŞTAN SONA UYGULAMA — ÖZET AKIŞ

**Basit path analysis / mediation / moderation için:**
1. Veriyi yükleyin, değişken tiplerini (Continuous/Nominal) kontrol edin.
2. Analyses > **medmod** modülü (mediation ya da moderation seçin).
3. Değişkenleri X (predictor), Y (dependent), M (mediator) ya da W (moderator) kutularına atayın.
4. Bootstrap sayısını artırın (mediation için, 5000 önerilir).
5. Çıktıyı yorumlayın: doğrudan/dolaylı/toplam etkiler (mediation) ya da etkileşim terimi + basit eğim (moderation).

**Tam/karmaşık SEM modelleri için (gizil değişkenli, çoklu yol):**
1. Analyses > **SEM** modülü.
2. Ölçüm modelini (varsa gizil değişkenler) `=~` ile, yapısal yolları `~` ile tanımlayın (lavaan sözdizimi, jamovi SEM panelinde de aynı mantık arayüzle sunulur).
3. Estimator'ı veri normalliğine göre seçin (bkz. ilk rehberdeki CFA bölümü — ML/MLR/WLSMV).
4. Fit indekslerini ve tüm yol katsayılarını inceleyin.

---

## 9. SÖZLÜK

| Terim | Anlamı |
|---|---|
| **Exogenous (dışsal)** | Modelde hiçbir okun girmediği, sadece çıktığı değişken |
| **Endogenous (içsel)** | Modelde en az bir okun girdiği değişken |
| **Path coefficient (yol katsayısı)** | İki değişken arasındaki okun üzerindeki standartlaştırılmış etki büyüklüğü (β) |
| **Direct effect (doğrudan etki)** | X'ten Y'ye tek bir ok üzerinden giden etki |
| **Indirect effect (dolaylı etki)** | X'ten Y'ye bir ara değişken (M) üzerinden giden etki (a×b) |
| **Total effect (toplam etki)** | Doğrudan + tüm dolaylı etkilerin toplamı |
| **Bootstrap** | Veriden tekrar tekrar örneklem çekerek bir istatistiğin güven aralığını ampirik olarak tahmin etme yöntemi |
| **Interaction term (etkileşim terimi)** | X×W çarpımı; moderation'ın istatistiksel testi |
| **Simple slope (basit eğim)** | Düzenleyicinin belirli bir düzeyinde X→Y ilişkisinin eğimi |
| **Centering (merkezileme)** | Bir değişkenden kendi ortalamasını çıkarma işlemi; etkileşim terimlerinde çoklu doğrusal bağlantıyı azaltır |
| **R²** | Bağımlı değişkendeki varyansın model tarafından açıklanan oranı |

---

*Bu rehber, ilk rehberdeki (Ölçek Uyarlama ve Psikometrik Değerlendirme Rehberi) CFA/güvenirlik/geçerlik temelinin üzerine inşa edilecek şekilde tasarlanmıştır. Mind-Eat Scale-TR gibi doğrulanmış bir ölçeğiniz olduğunda, bu ölçeği kullanarak buradaki yöntemlerle (örn. "mindful eating, BMI'yi duygusal yeme üzerinden mi etkiliyor?") yeni, içerik-odaklı bir araştırma sorusu test edebilirsiniz.*
