---
PDF_Adi: "{{title}}"
Dosya_No: "{% for a in annotations %}{% if a.color == '#ffd400' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
Marka_Sahis: "{% for a in annotations %}{% if a.color == '#ff6666' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
Mecra: "{% for a in annotations %}{% if a.color == '#5fb236' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
Konu: "{% for a in annotations %}{% if a.color == '#2ea8e5' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
Ihlal_Detayi: "{% for a in annotations %}{% if a.color == '#a28ae5' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
Ceza: "{% for a in annotations %}{% if a.color == '#e56eee' %}{{a.annotatedText | replace('"', "'")}}{% endif %}{% endfor %}"
---

# {{title}}
**Orijinal Kaynak:** [Zotero'da Aç]({{desktopURI}}) | **PDF:** [Dosyayı Aç]({{pdfLink}})

---
### 🟡 Dosya No
{% for a in annotations %}{% if a.color == '#ffd400' %}- {{a.annotatedText}} ([Sayfa {{a.pageLabel}}]({{a.desktopURI}})){% endif %}{% endfor %}

### 🔴 Marka / Şahıs
{% for a in annotations %}{% if a.color == '#ff6666' %}- {{a.annotatedText}} ([Sayfa {{a.pageLabel}}]({{a.desktopURI}})){% endif %}{% endfor %}

### 🟢 Mecra
{% for a in annotations %}{% if a.color == '#5fb236' %}- {{a.annotatedText}} ([Sayfa {{a.pageLabel}}]({{a.desktopURI}})){% endif %}{% endfor %}

### 🔵 Konu Başlığı
{% for a in annotations %}{% if a.color == '#2ea8e5' %}- {{a.annotatedText}} ([Sayfa {{a.pageLabel}}]({{a.desktopURI}})){% endif %}{% endfor %}

### 🟣 İhlal Detayları
{% for a in annotations %}{% if a.color == '#a28ae5' %}- {{a.annotatedText}} ([Sayfa {{a.pageLabel}}]({{a.desktopURI}})){% endif %}{% endfor %}

### 🌸 Verilen Ceza
{% for a in annotations %}{% if a.color == '#e56eee' %}- {{a.annotatedText}} ([Sayfa {{a.pageLabel}}]({{a.desktopURI}})){% endif %}{% endfor %}