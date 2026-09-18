---
tags: [claude, skill, araştırma, dizin]
created: 2026-09-04
---

# 🧠 Claude Skills — Ana Dizin

Claude Cowork'e kurulu 4 beslenme araştırması skill'inin tam referansı.
Skill'ler her yeni sohbette otomatik aktif — `/komut` ile çağrılır.

---

## Kurulu Skill'ler

| # | Komut | Ne yapar | Ne zaman çağır |
|---|-------|----------|----------------|
| 1 | [[01_Calisma_Tasarimi\|/beslenme-calisma-tasarimi]] | RCT tasarımı, randomizasyon, örneklem büyüklüğü | Yeni çalışma tasarlarken |
| 2 | [[02_Istatistik_Analizi\|/beslenme-istatistik-analizi]] | Test seçimi, enerji ayarlama, FDR, karma model | Analiz planı / kod yazarken |
| 3 | [[03_Veritabani_Erisimi\|/beslenme-veritabani-erisimi]] | ClinicalTrials, GWAS, GTEx, WHO GHO API sorguları | Literatür taraması / veri toplarken |
| 4 | [[04_Yayin_Sureci\|/beslenme-yayin-sureci]] | Dergi seçimi, Methods yazımı, hakem yanıtı | Makale yazarken / revizyonda |

---

## Aktif Proje → Skill Eşleştirmesi

| Proje | Skill |
|-------|-------|
| FOP Etiketi makalesi (n=719) | #2 + #4 |
| TRF Termogenez RCT planlaması | #1 + #3 |
| COST Action diyetisyen anketi | #1 + #2 |
| GLP-1/Kanser hipotezi | #3 + #4 |
| Refeeding review | #3 + #4 |
| Mikrobiyota farkındalık çalışması | #2 |

---

## Birden Fazla Skill Kullanımı

Tek komutta iki skill birleştirilebilir:

```
"TRF RCT için örneklem büyüklüğü hesapla, sonra 
ClinicalTrials.gov'daki tamamlanmış TRF çalışmalarını getir"
```

Claude her iki skill'i aynı yanıtta işler.

---

## Online Kılavuz

[Master Skill Kılavuzu (Artifact)](https://claude.ai/code/artifact/ad26e3d8-3a79-449f-9773-1e6112e2f2fd)
