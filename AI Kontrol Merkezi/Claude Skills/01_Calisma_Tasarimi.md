---
tags: [claude, skill, çalışma-tasarımı, RCT, randomizasyon]
created: 2026-09-04
skill: beslenme-calisma-tasarimi
---

# 📐 Skill 1 — Çalışma Tasarımı

**Komut:** `/beslenme-calisma-tasarimi`

Beslenme klinik denemelerinde ve gözlemsel çalışmalarda tasarım kararlarını yönetir.

---

## Ne Yapabilir

- Paralel / çapraz geçiş / küme randomizasyonu seçimi
- Bloklu randomizasyon kodu (Python, seed ile tekrarlanabilir)
- Örneklem büyüklüğü hesabı (%15 kayıp izlem dahil)
- Carry-over etkisi ve wash-out süresi hesabı
- Beslenmeye özgü kör uygulama stratejileri
- Diyet uyumluluk doğrulama yöntemleri
- CONSORT / STROBE öncesi kontrol listesi
- ClinicalTrials.gov kayıt rehberi

---

## Örnek İstekler

```
TRF termogenez RCT için paralel kollu tasarım öner, 
UCP1 adipoz biyopsi primer sonuç, %80 güç, %15 kayıp izlem ayarlı
```

```
16:8 vs 5:2 IF çapraz geçiş: uygun wash-out süresi ve 
carry-over testi için analitik plan
```

```
COST Action çok-ülkeli anket: küme randomizasyonu, 
ICC hesabı, design effect, kaç ülke/diyetisyen gerekir?
```

---

## Tasarım Karar Ağacı

| Araştırma sorusu | Tasarım | Neden |
|------------------|---------|-------|
| TRF vs. kontrol, adipoz biyopsi | Paralel RCT | Carry-over yok |
| 16:8 vs. 5:2 IF | Çapraz geçiş | Küçük örneklem |
| Okul beslenme müdahalesi | Küme RCT | Kontaminasyon riski |
| UPF → MetSend ilişkisi | Kesitsel | Müdahale yapılamaz |

---

## Temel Kod

```python
# Bloklu randomizasyon + örneklem büyüklüğü
from statsmodels.stats.power import TTestIndPower
import math, random, pandas as pd

analiz = TTestIndPower()
n_per_group = analiz.solve_power(effect_size=0.6, alpha=0.05, power=0.80)
n_kayit = math.ceil(n_per_group / (1 - 0.15))  # %15 dropout

def bloklu_randomizasyon(n, kollar, blok=4, seed=42):
    random.seed(seed)
    atamalar = []
    while len(atamalar) < n:
        b = kollar * (blok // len(kollar))
        random.shuffle(b)
        atamalar.extend(b)
    return pd.DataFrame({'no': range(1, n+1), 'kol': atamalar[:n]})

df = bloklu_randomizasyon(n_kayit*2, ['TRF_16_8', 'Kontrol'])
```

---

## İlgili Projeler

- [[../../../Çalışma Tasarımları|Çalışma Tasarımları klasörü]]
- TRF Termogenez RCT (planlama aşaması)
- COST Action CA24166 çok-ülkeli anket
