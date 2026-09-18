---
Title: "{{title}}"
Authors: "{{authors}}"
Year: {{date | format("YYYY")}}
DOI: "{{DOI}}"
Nitelik: 
Alan: 
Konu: 
AI_Methodology: 
Layer_Focus: 
Model_Asamasi: 
Proposed_Tool: 
Methods: "{% for a in annotations %}{% if a.color == '#5fb236' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
Findings: "{% for a in annotations %}{% if a.color == '#ff6666' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
Conclusions: "{% for a in annotations %}{% if a.color == '#2ea8e5' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
Limitations: "{% for a in annotations %}{% if a.color == '#f19837' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
User_Notes: "{% for n in notes %}{{n.note | replace('\n', ' ') | replace('"', "'")}}{% endfor %}"
---

# {{title}}
**Yazarlar:** {{authors}} | **Yıl:** {{date | format("YYYY")}}
**DOI:** {{DOI}} | **Zotero:** [Görüntüle]({{desktopURI}})

---

## 📝 Benim Notlarım
{% for n in notes -%}
- {{n.note}}
{%- endfor %}

## 🟡 Genel Bilgiler (Sarı)
{% for a in annotations -%}
{%- if a.color == "#ffd400" -%}
- "{{a.annotatedText}}" ([Sayfa {{a.pageLabel}}]({{a.desktopURI}}))
{%- endif -%}
{%- endfor %}

## 🟢 Yöntem & Örneklem (Yeşil)
{% for a in annotations -%}
{%- if a.color == "#5fb236" -%}
- "{{a.annotatedText}}" ([Sayfa {{a.pageLabel}}]({{a.desktopURI}}))
{%- endif -%}
{%- endfor %}

## 🔴 Bulgular (Kırmızı)
{% for a in annotations -%}
{%- if a.color == "#ff6666" -%}
- "{{a.annotatedText}}" ([Sayfa {{a.pageLabel}}]({{a.desktopURI}}))
{%- endif -%}
{%- endfor %}

## 🔵 Sonuç / Conclusions (Mavi)
{% for a in annotations -%}
{%- if a.color == "#2ea8e5" -%}
- "{{a.annotatedText}}" ([Sayfa {{a.pageLabel}}]({{a.desktopURI}}))
{%- endif -%}
{%- endfor %}

## 🟠 Limitasyonlar (Turuncu)
{% for a in annotations -%}
{%- if a.color == "#f19837" -%}
- "{{a.annotatedText}}" ([Sayfa {{a.pageLabel}}]({{a.desktopURI}}))
{%- endif -%}
{%- endfor %}