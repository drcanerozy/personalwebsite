---
citekey: {{citekey}}
status: #okunacak
tags: #zotero #literatür
---
# {{title}}

**Yazar:** {{authors}}
**Yıl:** {{date | format("YYYY")}}
**DOI:** {{doi}}
**Link:** {{url}}
**Zotero Kaydı:** [Zotero'da Aç]({{desktopURI}})

---

{% for annotation in annotations -%}
{%- if annotation.annotatedText -%}
- {{annotation.annotatedText}} (s. {{annotation.page}})
{% endif -%}
{%- endfor %}