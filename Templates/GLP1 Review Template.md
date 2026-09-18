# {{title}}
**Yazarlar:** {{authors}}
**Yıl:** {{date | format("YYYY")}}
**Yayın:** {{publicationTitle}}
**Zotero Linki:** [Görüntüle]({{desktopURI}})
**PDF:** [Dosyayı Aç]({{pdfLink}})

---
## 🟡 Genel: GLP-1 ve Obezite

{% for annotation in annotations -%}
{%- if annotation.color == "#ffd400" or annotation.color == "#f19837" -%}
- "{{annotation.annotatedText}}" ([Sayfa {{annotation.pageLabel}}]({{annotation.desktopURI}}))
{%- if annotation.comment %}
    - **Notum:** {{annotation.comment}}
{%- endif %}
{%- endif -%}
{%- endfor %}

## 🟢 Mekanizma: GLP-1 ve Beyin

{% for annotation in annotations -%}
{%- if annotation.color == "#5fb236" -%}
- "{{annotation.annotatedText}}" ([Sayfa {{annotation.pageLabel}}]({{annotation.desktopURI}}))
{%- if annotation.comment %}
    - **Notum:** {{annotation.comment}}
{%- endif %}
{%- endif -%}
{%- endfor %}

## 🔵 Mekanizma: Enerji Harcaması (EBM Girdisi)

{% for annotation in annotations -%}
{%- if annotation.color == "#2ea8e5" -%}
- "{{annotation.annotatedText}}" ([Sayfa {{annotation.pageLabel}}]({{annotation.desktopURI}}))
{%- if annotation.comment %}
    - **Notum:** {{annotation.comment}}
{%- endif %}
{%- endif -%}
{%- endfor %}

## 🔴 Tartışma: GLP-1 vs CIM & İnsülin

{% for annotation in annotations -%}
{%- if annotation.color == "#ff6666" or annotation.color == "#e56eee" -%}
- "{{annotation.annotatedText}}" ([Sayfa {{annotation.pageLabel}}]({{annotation.desktopURI}}))
{%- if annotation.comment %}
    - **Notum:** {{annotation.comment}}
{%- endif %}
{%- endif -%}
{%- endfor %}

## 🟣 Tartışma: GLP-1 vs EBM

{% for annotation in annotations -%}
{%- if annotation.color == "#a28ae5" -%}
- "{{annotation.annotatedText}}" ([Sayfa {{annotation.pageLabel}}]({{annotation.desktopURI}}))
{%- if annotation.comment %}
    - **Notum:** {{annotation.comment}}
{%- endif %}
{%- endif -%}
{%- endfor %}