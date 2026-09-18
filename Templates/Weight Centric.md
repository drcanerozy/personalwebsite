---
Title: "{{title}}"
Authors: "{{authors}}"
Year: {{date | format("YYYY")}}
Journal: "{{publicationTitle}}"
DOI: "{{DOI}}"
Created: {{importDate | format("YYYY-MM-DD HH:mm")}}
Updated: {{importDate | format("YYYY-MM-DD HH:mm")}}
---

# {{title}}

> [!abstract] **Makale Künyesi**
> - **Yazarlar:** {{authors}} | **Yıl:** {{date | format("YYYY")}}
> - **Dergi:** {{publicationTitle}}
> - **DOI:** [{{DOI}}](https://doi.org/{{DOI}}) | **Zotero:** [Kütüphanede Aç]({{zoteroSelectURI}})

---

## 📝 Notlar (PDF'e Eklediğim Notlar)
{% for n in notes -%}
- {{n.note | replace('\n', ' ')}}
{% endfor %}

---

## 🟢 Atıf Yapılabilir (Yeşil)
{% for a in annotations -%}
{%- if a.color == "#5fb236" -%}
- "{{a.annotatedText}}" (Sayfa {{a.pageLabel}}) [PDF'de Gör](zotero://open-pdf/library/items/{{itemKey}}?page={{a.pageLabel}})
{%- endif -%}
{%- endfor %}

## 🔴 Makale Bulguları (Kırmızı)
{% for a in annotations -%}
{%- if a.color == "#ff6666" -%}
- "{{a.annotatedText}}" (Sayfa {{a.pageLabel}}) [PDF'de Gör](zotero://open-pdf/library/items/{{itemKey}}?page={{a.pageLabel}})
{%- endif -%}
{%- endfor %}

## 🔵 Conclusions / Sonuç (Mavi)
{% for a in annotations -%}
{%- if a.color == "#2ea8e5" -%}
- "{{a.annotatedText}}" (Sayfa {{a.pageLabel}}) [PDF'de Gör](zotero://open-pdf/library/items/{{itemKey}}?page={{a.pageLabel}})
{%- endif -%}
{%- endfor %}

## 🟠 Limitasyonlar (Turuncu)
{% for a in annotations -%}
{%- if a.color == "#f19837" -%}
- "{{a.annotatedText}}" (Sayfa {{a.pageLabel}}) [PDF'de Gör](zotero://open-pdf/library/items/{{itemKey}}?page={{a.pageLabel}})
{%- endif -%}
{%- endfor %}

## 🟡 Genel Bilgiler (Sarı)
{% for a in annotations -%}
{%- if a.color == "#ffd400" -%}
- "{{a.annotatedText}}" (Sayfa {{a.pageLabel}}) [PDF'de Gör](zotero://open-pdf/library/items/{{itemKey}}?page={{a.pageLabel}})
{%- endif -%}
{%- endfor %}