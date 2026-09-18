---
tags: [claude, skill, yayın, dergi, hakem, STROBE, CONSORT, PRISMA]
created: 2026-09-04
skill: beslenme-yayin-sureci
---

# 📝 Skill 4 — Yayın Süreci

**Komut:** `/beslenme-yayin-sureci`

Literatür taramasından hakem yanıtına — tüm yayın sürecini kapsar.

---

## Ne Yapabilir

- Sistematik literatür taraması (PRISMA akışı + PubMed şablonları)
- Dergi seçimi (IF, kapsam, süre karşılaştırması)
- Methods bölümü istatistik yazım şablonları
- STROBE / CONSORT / PRISMA checklist kontrolü
- Hakem yanıt mektubu yapısı + sık yanıt şablonları
- Cover letter yazımı
- Etik beyan, veri erişilebilirliği, çıkar çatışması metinleri
- İngilizce Methods/Results bölümü çeviri + düzeltme

---

## Aktif Projeler için Dergi Önerileri

| Makale | 1. Tercih | IF | 2. Tercih |
|--------|-----------|-----|-----------|
| FOP Etiketi (NOVA×NutriScore) | Food Quality & Preference | 5.1 | Appetite |
| TRF Termogenez RCT | J. of Nutrition | 6.1 | Obesity |
| COST Action Anketi | Public Health Nutrition | 4.2 | Nutrients |
| GLP-1/Kanser hipotezi | Nutrition & Cancer | 3.8 | Front. Oncology |
| Refeeding review | Nutrients | 5.0 | Br. J. Nutrition |
| Mikrobiyota farkındalık | J. Nutr. Educ. Behav. | 3.2 | Nutrients |

---

## Örnek İstekler

```
FOP makalesi için hakem yanıt mektubu: 
Hakem 1'in "enerji ayarlaması yok" yorumuna yanıt yaz
```

```
TRF RCT için CONSORT checklist doldur,
eksik bölümleri işaretle
```

```
"Ultra-processed food AND metabolic syndrome" için 
sistematik tarama protokolü hazırla (PRISMA)
```

```
Methods bölümündeki istatistik paragrafını 
J. Nutrition formatına uygun İngilizce'ye çevir
```

---

## Hakem Yanıtı — Sık Yorumlar

| Yorum | Strateji |
|-------|----------|
| "Örneklem küçük" | Kabul + güç analizi + pilot olarak çerçevele |
| "Enerji ayarlaması yok" | Residual yöntemi ile model ekle |
| "Nedensellik iddiası" | "associated with" kullan, Discussion'dan kaldır |
| "UPF tanımı tutarsız" | NOVA v4 Methods'a ekle, Monteiro 2019 alıntıla |
| "Multiple comparison yok" | FDR-BH ekle, ek tablo sun |
| "Confounding yetersiz" | Fiziksel aktivite, sigara modele ekle |

---

## PubMed Arama Şablonları

```
# UPF araştırmaları
("ultra-processed food*"[tw] OR "NOVA classification"[tw])
AND ("metabolic syndrome"[MeSH] OR "obesity"[MeSH])
AND ("2015"[dp]:"3000"[dp])

# TRF/IF
("time-restricted eating"[tw] OR "intermittent fasting"[MeSH])
AND ("adipose tissue"[MeSH] OR "thermogenesis"[tw])

# FOP etiketleme
("front-of-pack label*"[tw] OR "Nutri-Score"[tw])
AND ("consumer*"[tw] OR "food choice*"[tw])
```

---

## ⚠️ TRF RCT için Zorunlu

ClinicalTrials.gov kaydı çalışma başlamadan yapılmalı.
Kayıt olmadan büyük çoğunluk dergi kabul etmez.

---

## İlgili Notlar

- [[../Claude Komut Protokolü|Claude Komut Protokolü]]
- [[../../../Manuscripts|Manuscripts klasörü]]
- [[../../../Personalized Fasting|Personalized Fasting]]
