### 1. Klasör Ağacı ve Dosya Mimarisi

  
  
  

Plaintext

Academic-Vault/  
├── .obsidian/                      # Obsidian sistem ve eklenti ayarları  
├── _templates/                     # Otomasyon için YAML şablonları (.md)  
│   ├── tpl-publication.md          # Makale, bildiri ve derleme şablonu  
│   ├── tpl-tool.md                 # 3D simülasyon ve hesaplayıcı şablonu  
│   ├── tpl-lecture-slide.md        # Canlı Reveal.js / HTML sunum şablonu  
│   ├── tpl-reproducible-code.md    # R betikleri, SEM ve analiz şablonu  
│   ├── tpl-project.md              # Fonlanan araştırma ve COST projeleri  
│   └── tpl-post-podcast.md         # Substack bülteni ve ses kayıtları  
│  
├── assets/                         # Statik medya ve dosya deposu  
│   ├── images/                     # Vaka fotoğrafları, portre, grafikler  
│   ├── pdfs/                       # Açık erişim makaleler, ders izlenceleri  
│   └── audio/                      # Podcast kayıtları ve ses dosyaları  
│  
└── content/                        # Çok Dilli İçerik Havuzu  
    ├── tr/                         # TÜRKÇE İÇERİKLER  
    │   ├── bio.md                  # Akademik hikaye ve özgeçmiş  
    │   ├── yayinlar/               # Yayınlanan bilimsel makaleler  
    │   ├── lab-araclari/           # 3D hücre modelleri & WebR hesaplayıcılar  
    │   ├── acik-dersler/           # HTML sunumlar & vaka simülasyonları  
    │   ├── tekrarlanabilir-kod/    # R kodları, lavaan modelleri, veri setleri  
    │   ├── projeler/               # TÜBİTAK, COST ve hibeler  
    │   └── bulten-podcast/         # Substack yazıları ve ses kayıtları  
    │  
    └── en/                         # İNGİLİZCE İÇERİKLER  
        ├── bio.md  
        ├── publications/  
        ├── interactive-tools/  
        ├── open-teaching/  
        ├── reproducible-hub/  
        ├── projects/  
        └── writing-podcast/  
  

### 2. Properties (YAML Frontmatter) Standartları

Tüm şablonlar statik site derleyicileri (Astro, Hugo, Quarto) ve Obsidian Dataview eklentisiyle tam uyumlu anahtar-değer çiftlerine sahiptir:

- Yayın Şablonu (_templates/tpl-publication.md):
    

  
  
  

YAML

---  
title: ""  
type: "publication"  
category: "clinical" # clinical | nutrition | multiomics | methodology | review  
journal: ""  
year: 2026  
date: 2026-01-01  
doi: ""  
authors:  
  - "Yazar 1"  
featured: true  
pdf_url: "/assets/pdfs/dosya.pdf"  
code_repo: ""  
lay_summary: ""  
draft: false  
lang: "tr"  
---  
  

- İnteraktif Araç Şablonu (_templates/tpl-tool.md):
    

  
  
  

YAML

---  
title: ""  
type: "interactive-tool"  
tech_stack:  
  - "Three.js"  
  - "WebR"  
embed_url: "/tools/ornek-arac/index.html"  
github_repo: ""  
category: "cellular-simulation" # cellular-simulation | clinical-calculator | data-viz  
featured: true  
draft: false  
lang: "tr"  
---  
  

- Ders & Sunum Şablonu (_templates/tpl-lecture-slide.md):
    

  
  
  

YAML

---  
title: ""  
type: "lecture-slide"  
course_code: ""  
level: "Undergraduate" # Undergraduate | Graduate | Workshop  
slide_format: "RevealJS-HTML" # RevealJS | Quarto-Slide | Marp  
live_slide_url: "/slides/ders-hafta-1/index.html"  
repo_url: ""  
license: "CC-BY-4.0"  
draft: false  
lang: "tr"  
---  
  

- Tekrarlanabilir Kod Şablonu (_templates/tpl-reproducible-code.md):
    

  
  
  

YAML

---  
title: ""  
type: "code-hub"  
tags:  
  - "R"  
  - "lavaan"  
  - "ggplot2"  
related_publication_doi: ""  
repo_url: ""  
reproducibility_badge: "Data & Code Available"  
draft: false  
lang: "tr"  
---  
  

- Proje Şablonu (_templates/tpl-project.md):
    

  
  
  

YAML

---  
title: ""  
type: "project"  
status: "ongoing" # ongoing | planned | completed  
funding_body: ""  
role: "Principal Investigator / Researcher / WG Member"  
start_date: 2026-01  
end_date: 2028-12  
featured: true  
external_link: ""  
draft: false  
lang: "tr"  
---  
  

- Bülten & Podcast Şablonu (_templates/tpl-post-podcast.md):
    

  
  
  

YAML

---  
title: ""  
type: "post" # post | podcast  
date: 2026-01-01  
tags:  
  - "Beslenme Biyokimyası"  
substack_url: ""  
spotify_embed_id: ""  
audio_file: "/assets/audio/bolum.mp3"  
read_time: "5 dk"  
draft: false  
lang: "tr"  
---  
  

### 3. Önerilen Eklentiler (Community Plugins) ve Temalar

Otomasyon ve veri akışını yönetmek için kurulması gereken Obsidian paketleri:

- Obsidian Git: Notları tek tuşla veya belirli aralıklarla GitHub reposuna git push ile senkronize eder.
    
- Dataview: Kasa içerisindeki makaleleri, dersleri ve projeleri Properties verilerine göre tablolar ve listeler halinde anlık sorgular (SQL benzeri filtreleme).
    
- Linter: Her dosya kaydedildiğinde YAML frontmatter başlıklarını standartlaştırır, boşluk ve formatlama hatalarını engeller.
    
- Templater: Şablon eklerken tarih, dil ve dosya adı değişkenlerini otomatik doldurur.
    
- Tema Önerisi: Minimal (Minimal Theme Settings eklentisiyle birlikte) veya AnuPpuccin. Açık renk modunda beyaz/kırık beyaz fon, arduvaz mavisi ve temiz serif tipografi ile bilimsel editoryal görünüm sunar.
    

### 4. Antigravity İçin Otomasyon İstemi (Prompt)

Aşağıdaki istemi Antigravity terminaline/arayüzüne yapıştırarak tüm ortamı tek seferde inşa ettirebilirsiniz:

  
  
  

Plaintext

Lütfen mevcut çalışma dizininde 'Academic-Vault' adında eksiksiz bir Obsidian kasası oluştur.  
  
1. Klasör Yapısı:  
- _templates  
- assets/images, assets/pdfs, assets/audio  
- content/tr/{yayinlar,lab-araclari,acik-dersler,tekrarlanabilir-kod,projeler,bulten-podcast}  
- content/en/{publications,interactive-tools,open-teaching,reproducible-hub,projects,writing-podcast}  
  
2. Şablon Dosyaları:  
- `_templates/` altına şu dosyaları oluştur ve içlerine ilgili YAML frontmatter yapılarını eksiksiz yaz:  
  * tpl-publication.md  
  * tpl-tool.md  
  * tpl-lecture-slide.md  
  * tpl-reproducible-code.md  
  * tpl-project.md  
  * tpl-post-podcast.md  
  
3. Başlangıç Dosyaları:  
- content/tr/bio.md ve content/en/bio.md dosyalarını oluştur.  
  
Tüm dosya formatlarının UTF-8 ve standart YAML syntax kurallarına uygun olduğundan emin ol.  
  


**