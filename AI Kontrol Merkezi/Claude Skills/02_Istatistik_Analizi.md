---
tags: [claude, skill, istatistik, analiz, python]
created: 2026-09-04
skill: beslenme-istatistik-analizi
---

# 📊 Skill 2 — İstatistik Analizi

**Komut:** `/beslenme-istatistik-analizi`

Beslenme verilerinin istatistiksel analizi — test seçiminden raporlamaya.

---

## Ne Yapabilir

- Doğru test seçimi (12 senaryo tablosu)
- Varsayım kontrolü (normallik, varyans homojenliği)
- Enerji ayarlama — residual yöntemi (tercih) veya besin yoğunluğu
- Sıfır şişirilmiş veri modelleri (alkol, balık tüketimi)
- Tekrarlı ölçüm karma modelleri (LME)
- FDR-BH çoklu karşılaştırma düzeltmesi
- Cohen's kappa + Cramér's V (FOP uyum analizi)
- Lojistik regresyon + OR tablosu
- APA formatında sonuç raporlama
- pingouin 0.6+ uyumlu kod

---

## Örnek İstekler

```
n=719'da NOVA × NutriScore-DE uyum analizi:
kappa, Cramér's V, FDR düzeltmeli ki-kare, diskordans tablosu
```

```
UPF yüzdesi → metabolik sendrom lojistik regresyon,
3 model: ham / enerji+yaş+cinsiyet / +fiziksel aktivite
```

```
TRF adipoz biyopsi tekrarlı ölçüm: karma model,
zaman×grup etkileşimi, group SE ve %95 GA
```

```
20 biyobelirteç aynı anda — FDR uygula, q-değerleri tablo yap
```

---

## Test Seçim Tablosu

| Durum | Test | Dikkat |
|-------|------|--------|
| 2 grup, normal | t-testi | Levene ile varyans kontrolü |
| 2 grup, normal değil | Mann-Whitney U | Ortanca ± IQR raporla |
| ≥3 grup | ANOVA → Tukey | Homojenlik yoksa Welch |
| Tekrarlı ölçüm | Karma model | Pseudoreplication hatası! |
| İkili sonuç | Lojistik regresyon | Enerji ayarlı model zorunlu |
| Kategorik × kategorik | Ki-kare + κ + V | Beklenen frekans ≥5 |
| Sıfır şişik veri | Hurdle/iki-parçalı | Önce lojistik, sonra OLS |
| Çoklu belirteç (≥10) | Her test + FDR-BH | p yerine q raporla |

---

## Temel Kodlar

```python
import statsmodels.api as sm
import numpy as np
from sklearn.metrics import cohen_kappa_score
from scipy.stats import chi2_contingency
from statsmodels.stats.multitest import multipletests

# Enerji ayarlama — residual yöntemi
X = sm.add_constant(df['enerji_kcal'])
model = sm.OLS(df['lif_g'], X).fit()
df['lif_enerji_ayarli'] = model.resid

# Kappa + Cramér's V (FOP makalesi, n=719)
kappa = cohen_kappa_score(df['NOVA_UPF'], df['NutriScore_DE'])
ct = pd.crosstab(df['NOVA_UPF'], df['NutriScore_DE'])
chi2, p, dof, _ = chi2_contingency(ct)
cramers_v = np.sqrt(chi2 / (ct.values.sum() * (min(ct.shape)-1)))
# → κ=0.20 (zayıf), V=0.34 (orta-güçlü)

# FDR düzeltmesi
_, q_values, _, _ = multipletests(p_values, method='fdr_bh')
```

---

## İlgili Projeler

- [[../../../İstatistik Karar Ağacı|İstatistik Karar Ağacı]]
- FOP Etiketi makalesi (kappa revizyonu)
- Mikrobiyota farkındalık çalışması (n=1400)
- Sezgisel yeme makalesi (hedonik yeme)
