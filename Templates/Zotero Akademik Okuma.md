---
citekey: {{citekey}}
etiketler: [{% for t in tags %}{{t.tag}}{% if not loop.last %}, {% endif %}{% endfor %}]
yazarlar: {{authors}}
yil: {{date | format("YYYY")}}
dergi: {{publicationTitle}}
url: {{url}}
doi: {{DOI}}
zotero_link: {{select}}
---

# {{title}}

> [!abstract] Özet
> {{abstractNote}}

## 📝 Kişisel Notlarım & Analizim
*(Buraya analizini yaz)*

---

## 🖍️ Renkli Alıntılar

{% for color, annotations in annotations | groupby("color") %}
{# --- SARI GRUBU --- #}
{%- if color == "#ffd400" -%}
> [!example] 📒 Genel Bilgiler / Kavramlar
{% for annotation in annotations -%}
> * {{annotation.annotatedText}} [Sayfa {{annotation.pageLabel}}](zotero://open-pdf/library/items/{{annotation.attachment.itemKey}}?page={{annotation.pageLabel}}&annotation={{annotation.id}})
{% if annotation.comment %}> **Notum:** {{annotation.comment}}{% endif %}
>
{% endfor %}

{# --- KIRMIZI GRUBU --- #}
{%- elif color == "#ff6666" -%}
> [!failure] 🚨 Çok Önemli / Kritik
{% for annotation in annotations -%}
> * {{annotation.annotatedText}} [Sayfa {{annotation.pageLabel}}](zotero://open-pdf/library/items/{{annotation.attachment.itemKey}}?page={{annotation.pageLabel}}&annotation={{annotation.id}})
{% if annotation.comment %}> **Notum:** {{annotation.comment}}{% endif %}
>
{% endfor %}

{# --- YEŞİL GRUBU --- #}
{%- elif color == "#5fb236" -%}
> [!success] 🧪 Metodoloji
{% for annotation in annotations -%}
> * {{annotation.annotatedText}} [Sayfa {{annotation.pageLabel}}](zotero://open-pdf/library/items/{{annotation.attachment.itemKey}}?page={{annotation.pageLabel}}&annotation={{annotation.id}})
{% if annotation.comment %}> **Notum:** {{annotation.comment}}{% endif %}
>
{% endfor %}

{# --- MAVİ GRUBU --- #}
{%- elif color == "#2ea8e5" -%}
> [!info] 🧠 Çıkarımlar / Sonuçlar
{% for annotation in annotations -%}
> * {{annotation.annotatedText}} [Sayfa {{annotation.pageLabel}}](zotero://open-pdf/library/items/{{annotation.attachment.itemKey}}?page={{annotation.pageLabel}}&annotation={{annotation.id}})
{% if annotation.comment %}> **Notum:** {{annotation.comment}}{% endif %}
>
{% endfor %}

{# --- DİĞER RENKLER --- #}
{%- else -%}
> [!quote] 📌 Diğer Notlar ({{color}})
{% for annotation in annotations -%}
> * {{annotation.annotatedText}} [Sayfa {{annotation.pageLabel}}](zotero://open-pdf/library/items/{{annotation.attachment.itemKey}}?page={{annotation.pageLabel}}&annotation={{annotation.id}})
{% if annotation.comment %}> **Notum:** {{annotation.comment}}{% endif %}
>
{% endfor %}
{%- endif -%}
{% endfor %}

{# --- GÖRSELLER --- #}
{%- for annotation in annotations -%}
{%- if annotation.imageRelativePath %}
![[ {{annotation.imageRelativePath}} ]]
**Şekil:** {{annotation.comment}}
{%- endif -%}
{%- endfor -%}