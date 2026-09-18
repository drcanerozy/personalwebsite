---
tags: [dashboard, evidence, gaps]
cssclasses: [dashboard]
---

# ⚖️ Bilimsel Boşluklar, Çelişkiler ve "Null Result" Panosu

> Bu pano, kasanızda taranan veya eklenen makaleler arasında **istatistiksel olarak anlamsız ($p > 0.05$)**, **mevcut konsensüsle çelişen** veya **sonucu belirsiz (inconclusive)** olan çalışmaları listeler.

---

## 🚫 İstatistiksel Olarak Anlamsız / Nötr Sonuçlar (`#finding/null`)

```dataview
TABLE
  file.folder AS "Klasör",
  study_type AS "Çalışma Türü",
  sample_size AS "Örneklem (N)",
  primary_outcome AS "Primer Sonuç",
  p_value_summary AS "P Değeri"
FROM #finding/null OR #null_result
SORT file.mtime DESC
```

---

## ⚡ Literatür Çelişkileri ve Paradokslar (`#finding/contradictory`)

```dataview
TABLE
  file.folder AS "Klasör",
  study_type AS "Çalışma Türü",
  evidence_direction AS "Kanıt Yönü",
  key_mechanisms AS "Mekanizmalar",
  primary_outcome AS "Tartışmalı Çıktı"
FROM #finding/contradictory OR #contradiction
SORT file.mtime DESC
```

---

## 📊 Yaşayan Kanıt (Living Evidence) Matrisi

```dataviewjs
const pages = dv.pages().where(p => p.evidence_direction);

const positive = pages.where(p => p.evidence_direction === "positive").length;
const negative = pages.where(p => p.evidence_direction === "negative").length;
const nullCount = pages.where(p => p.evidence_direction === "null").length;
const inconclusive = pages.where(p => p.evidence_direction === "inconclusive").length;

dv.paragraph(`
<div style="display:flex;gap:12px;flex-wrap:wrap;margin:16px 0">
  <div style="background:rgba(79,200,160,0.15);border:1px solid #4FC8A0;border-radius:8px;padding:10px 16px">
    <b>🟢 Pozitif / Anlamlı:</b> ${positive}
  </div>
  <div style="background:rgba(247,106,138,0.15);border:1px solid #F76A8A;border-radius:8px;padding:10px 16px">
    <b>🔴 Negatif / Ters Yönlü:</b> ${negative}
  </div>
  <div style="background:rgba(247,167,106,0.15);border:1px solid #F7A76A;border-radius:8px;padding:10px 16px">
    <b>⚪ Null / Anlamsız:</b> ${nullCount}
  </div>
  <div style="background:rgba(124,106,247,0.15);border:1px solid #7C6AF7;border-radius:8px;padding:10px 16px">
    <b>🟣 Belirsiz / Inconclusive:</b> ${inconclusive}
  </div>
</div>
`);
```
