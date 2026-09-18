---
tags: [claude, skill, veritabanı, API, veri-toplama]
created: 2026-09-04
skill: beslenme-veritabani-erisimi
---

# 🗄️ Skill 3 — Veritabanı Erişimi

**Komut:** `/beslenme-veritabani-erisimi`

10 ücretsiz açık-erişim veritabanına hazır Python sorguları.

---

## Ne Yapabilir

- ClinicalTrials.gov — TRF/IF/UPF RCT'leri listele, filtrelere göre sırala
- GWAS Catalog (EBI) — diyet, obezite, T2DM SNP asosiyasyonları
- Open Targets — GLP-1R, FTO, MC4R hastalık-hedef skorları (GraphQL)
- Metabolomics Workbench — IF/TRF metabolomik çalışma verileri
- GTEx v10 — UCP1, PPARGC1A adipoz doku ekspresyon değerleri
- WHO GHO — Türkiye/dünya obezite prevalansı (2000-2023)
- KEGG — keton cisimcikleri, yağ asidi metabolizması yolakları
- Reactome — UCP1/termogenez, GLP-1 sinyal yolağı haritası
- PubChem — besin bileşeni özellikleri, polifenoller
- PubMed E-utilities — literatür taraması, son yayınlar

---

## API Başvuru Tablosu

| Veritabanı | Erişim | Endpoint |
|-----------|--------|----------|
| ClinicalTrials.gov | Ücretsiz | `api/v2/studies` |
| GWAS Catalog | Ücretsiz | `gwas/rest/api` |
| Open Targets | Ücretsiz | GraphQL POST |
| Metabolomics Workbench | Ücretsiz | `rest/study` |
| GTEx v10 | Ücretsiz | `api/v2/expression` |
| WHO GHO | Ücretsiz | OData REST |
| KEGG | Ücretsiz | `rest.kegg.jp` |
| Reactome | Ücretsiz | ContentService REST |
| PubChem | Ücretsiz | PUG REST |
| USDA FoodData | API Key | api.nal.usda.gov |

---

## Örnek İstekler

```
GLP-1R'nin (ENSG00000112164) kanser hastalıklarıyla 
Open Targets asosiyasyon skorlarını getir
```

```
Adipoz doku ve termogenez sonuçlu tamamlanmış 
TRF klinik denemelerini ClinicalTrials.gov'dan listele
```

```
GTEx'ten UCP1 ve PPARGC1A'nın subkutan ve visseral 
adipoz doku median TPM değerlerini getir
```

```
WHO GHO'dan Türkiye obezite prevalansı 2000-2023 verisini 
çek, yıllar içindeki trendi göster
```

---

## Temel Kodlar

```python
import requests

# ClinicalTrials.gov — TRF çalışmaları
r = requests.get('https://clinicaltrials.gov/api/v2/studies', params={
    'query.term': 'time-restricted eating OR time-restricted feeding',
    'filter.overallStatus': 'COMPLETED',
    'query.outc': 'adipose OR thermogenesis OR UCP1',
    'pageSize': 30, 'format': 'json'
})

# Open Targets — GLP-1R hastalık ilişkileri
query = '{ target(ensemblId: "ENSG00000112164") { associatedDiseases { rows { disease { name } score } } } }'
r = requests.post('https://api.platform.opentargets.org/api/v4/graphql',
                  json={'query': query})

# GTEx — UCP1 adipoz doku ekspresyonu
r = requests.get('https://gtexportal.org/api/v2/expression/geneExpression', params={
    'datasetId': 'gtex_v10', 'gencodeId': 'ENSG00000109424.8',
    'tissueSiteDetailId': 'Adipose_Subcutaneous'
})

# PubMed — son FOP çalışmaları
r = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi', params={
    'db': 'pubmed', 'retmode': 'json',
    'term': '("front-of-pack label" OR "Nutri-Score") AND ("2024"[dp]:"3000"[dp])',
    'retmax': 20, 'sort': 'relevance'
})
```

---

## İlgili Projeler

- TRF Termogenez RCT (GTEx referans değerleri)
- GLP-1/Kanser hipotezi (Open Targets)
- Personalized Fasting review (Metabolomics Workbench)
