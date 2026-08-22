# Akademik Portföy & Araştırma Laboratuvarı Web Sitesi

Bu depo, **Doç. Dr. Alexandra Reed**'in akademik çalışmalarını, hakemli yayınlarını, araştırma projelerini, ders içeriklerini, Substack bültenini ve interaktif podcast çalarını sergileyen modern, tam fonksiyonel ve GitHub Pages uyumlu akademik web sitesini içerir.

---

## 🚀 Hızlı Başlangıç & GitHub Pages Yayını

Bu web sitesi herhangi bir derleme (build) adımı gerektirmeyen **saf ve optimize edilmiş HTML5 + Tailwind CSS + JavaScript** mimarisine sahiptir. Doğrudan GitHub Pages üzerinde yayınlanabilir.

### 1. Adım: GitHub Deposu Oluşturma ve Yükleme
```bash
git init
git add .
git commit -m "feat: ilk akademik portföy sürümü"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADINIZ/academic-portfolio.git
git push -u origin main
```

### 2. Adım: GitHub Pages'i Etkinleştirme
1. GitHub reponuzda **Settings** > **Pages** menüsüne gidin.
2. **Build and deployment** > **Source** kısmından **GitHub Actions** veya **Deploy from a branch** seçeneğini seçin.
3. Branch olarak `main` ve `/ (root)` seçin, **Save** butonuna tıklayın.
4. Birkaç saniye içinde siteniz `https://KULLANICI_ADINIZ.github.io/academic-portfolio` adresinde canlıya geçecektir.

---

## 📂 Proje Mimarisi

```
.
├── index.html                   # Ana web sayfası (GitHub Pages giriş noktası)
├── akademik_portf_y_ve_medya_merkezi.html # Orijinal tasarım taslağı
├── CV_Ozyildirim.pdf            # Akademik Özgeçmiş dosyası
├── .nojekyll                    # GitHub Pages Jekyll atlama dosyası
├── .github/
│   └── workflows/
│       └── deploy.yml           # Otomatik GitHub Pages dağıtım iş akışı
├── _templates/                  # Obsidian / Markdown içerik şablonları
│   ├── tpl-publication.md       # Yayın şablonu
│   ├── tpl-tool.md              # 3D / İnteraktif araç şablonu
│   ├── tpl-lecture-slide.md     # Sunum & ders şablonu
│   ├── tpl-reproducible-code.md # R & Analiz kod şablonu
│   ├── tpl-project.md           # Proje şablonu
│   └── tpl-post-podcast.md      # Bülten & Podcast şablonu
├── assets/                      # Medya ve statik dosyalar
│   ├── images/
│   ├── pdfs/
│   └── audio/
└── content/                     # Çok dilli içerik havuzu
    ├── tr/ (bio.md, yayinlar, projeler, vb.)
    └── en/ (bio.md, publications, projects, vb.)
```

---

## ✨ Öne Çıkan Özellikler & Fonksiyonlar

1. **Akademik Anlatı & Özgeçmiş (Narrative CV)**:
   - ORCID, Google Scholar, CV indirme bağlantıları ve metrik kartları (Yayın, Atıf, Fon, Takipçi).
2. **Dinamik Yayın Filtreleme**:
   - Makaleleri *Tümü*, *Klinik Araştırmalar*, *Biyoistatistik & Yapay Zeka*, *Derlemeler* kategorilerine göre anlık filtreleme.
3. **BibTeX & Halk İçin Özet (Lay Summary)**:
   - Tek tıkla BibTeX alıntısını panoya kopyalama ve modern bildirim (Toast) sistemi.
   - Bilimsel makaleler için genişleyebilir / daralabilir sade dille özet kutuları.
4. **İnteraktif Podcast & Medya Çalar**:
   - Oynat / Duraklat, bölüm seçimi (EP.14, EP.13, EP.12), canlı ilerleme çubuğu, tıklanabilir zaman sarma (seek bar).
5. **Substack Bülten Entegrasyonu**:
   - Anlık doğrulama ve bildirim sunan e-posta abonelik simülasyonu.
6. **Mobil & Tablet Tam Uyumluluğu**:
   - Akıcı mobil navigasyon menüsü, modern cam efekti (glassmorphism) üst çubuk.

---

## 🛠️ Yerel Önizleme

Projeyi yerel makinenizde test etmek için:

```bash
# Python ile:
python3 -m http.server 8000
# Ardından tarayıcınızda http://localhost:8000 adresini açın.
```
