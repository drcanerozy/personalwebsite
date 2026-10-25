# Dr. Caner ÖZYILDIRIM — Akademik Portföy & Kişisel Web Sitesi

Bu depo, **Dr. Caner ÖZYILDIRIM**'ın akademik çalışmalarını, hakemli yayınlarını, araştırma projelerini, ders içeriklerini, bülten ve podcast yayınlarını sergileyen çok dilli (TR/EN), Obsidian uyumlu ve GitHub Pages üzerinde yayınlanan modern akademik web sitesinin kaynak kodlarını içerir.

🌐 **Canlı Web Sitesi (Türkçe):** [drcanerozy.github.io/personalwebsite](https://drcanerozy.github.io/personalwebsite/)  
🇬🇧 **Live Website (English):** [drcanerozy.github.io/personalwebsite/en/](https://drcanerozy.github.io/personalwebsite/en/)

---

## 🔬 Araştırma Alanları & Akademik Profil

- **Kurum:** Akdeniz Üniversitesi Sağlık Bilimleri Fakültesi, Beslenme ve Diyetetik Bölümü
- **Odak Alanları:** Metabolik Esneklik, Yağ Dokusu Disfonksiyonu, NAFLD / MASLD, Biyoistatistiksel Modelleme (R), Zaman Kısıtlı Beslenme (TRE), Çoklu Omiks (COST Action CA24166 - INFLAMomx) ve İn Vitro Bağırsak Modelleri (COST Action CA23110 - INFOGUT).
- **ORCID:** [0000-0001-8227-9575](https://orcid.org/0000-0001-8227-9575)

---

## 📂 Proje Mimarisi

```
.
├── index.html                   # Türkçe Ana Sayfa (GitHub Pages root)
├── en/                          # İngilizce Sayfa
│   └── index.html               # İngilizce Ana Sayfa
├── content/                     # Markdown İçerik Havuzu (Obsidian ile düzenlenir)
│   ├── tr/                      # Türkçe İçerikler
│   │   ├── bio.md               # Akademik Biyografi ve Profil
│   │   ├── yayinlar/            # Bilimsel Makaleler & Bildiriler
│   │   ├── projeler/            # Araştırma Projeleri & COST Aksiyonları
│   │   ├── lab-araclari/        # İnteraktif Araçlar & Hesaplayıcılar
│   │   ├── acik-dersler/        # Ders Notları & Sunumlar
│   │   ├── tekrarlanabilir-kod/ # R Kodları & Analiz Modelleri
│   │   └── bulten-podcast/      # Bülten Yazıları & Podcast Bölümleri
│   └── en/                      # İngilizce İçerikler
│       ├── bio.md
│       ├── publications/
│       ├── projects/
│       ├── interactive-tools/
│       ├── open-teaching/
│       ├── reproducible-hub/
│       └── writing-podcast/
├── _templates/                  # Obsidian YAML İçerik Şablonları
├── assets/                      # Medya Dosyaları
│   ├── pdfs/                    # Açık erişim PDF'ler, ders materyalleri
│   ├── images/                  # Görseller ve grafikler
│   └── audio/                   # Podcast ses dosyaları
├── build.py                     # Markdown -> HTML Derleme Betiği
└── CV_Ozyildirim.pdf            # Akademik Özgeçmiş Dosyası
```

---

## ✨ Öne Çıkan Özellikler

1. **Çift Dilli Mimari (TR / EN):**
   - Tek tıkla Türkçe ve İngilizce dilleri arasında geçiş.
2. **Obsidian Entegrasyonu:**
   - Tüm içerikler `content/` klasörü altındaki standart Markdown (`.md`) dosyalarından yönetilir. Obsidian veya herhangi bir metin editörüyle içerik eklendiğinde `python3 build.py` çalıştırılarak siteler anında güncellenir.
3. **Akademik Anlatı & Özgeçmiş:**
   - ORCID, Google Scholar, AVESİS ve güncel metrikler.
4. **Dinamik Yayın & Proje Filtreleme:**
   - Makaleleri ve projeleri araştırma kategorilerine göre anlık filtreleme.
   - Tek tıkla BibTeX kopyalama ve halka yönelik sade dil özeti (Lay Summary) kutuları.
5. **İnteraktif Medya & Podcast:**
   - Dahili ses çalar ve bülten entegrasyonu.
6. **Modern Tasarım:**
   - Tailwind CSS ile optimize edilmiş, mobil uyumlu ve yüksek performanslı saf HTML mimarisi.

---

## 🛠️ Yerel Geliştirme ve Güncelleme

### 1. İçerikleri Güncelleme ve Derleme
Markdown içeriklerini değiştirdikten sonra web sayfalarını derlemek için:

```bash
python3 build.py
```

### 2. Yerel Önizleme
```bash
python3 -m http.server 8000
# Tarayıcınızda http://localhost:8000 adresini açın.
```

### 3. Değişiklikleri Yayına Alma
```bash
git add .
git commit -m "feat: yeni icerik guncellemesi"
git push origin main
```
GitHub Pages birkaç saniye içinde sitenizi otomatik olarak güncelleyecektir.
