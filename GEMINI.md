# Kişisel Web Sitesi — Proje Kuralları

Bu dizin, Dr. Caner ÖZYILDIRIM'ın akademik web sitesinin **tek ve yetkili kaynak dizinidir**.

## Temel Bilgiler

- **Proje Dizini:** `/Users/canerozyildirim/Sites/personalwebsite`
- **Canlı Site (TR):** https://drcanerozy.github.io/personalwebsite/
- **Canlı Site (EN):** https://drcanerozy.github.io/personalwebsite/en/
- **Platform:** GitHub Pages (`main` branch → otomatik deploy)
- **Teknoloji:** Saf HTML + Tailwind CSS, Python build scripti, çift dilli (TR/EN)

## Neden Bu Dizin?

Eski konum (`Desktop/Antigravity/academic_website`) Obsidian vault'u ve iCloud senkronizasyonu ile iç içeydi.
Bu yeni konum (`/Users/canerozyildirim/Sites/personalwebsite`) tamamen bağımsız ve temizdir.

## İçerik Ekleme / Düzenleme Kuralları

1. İçerikler `content/tr/` veya `content/en/` altındaki `.md` dosyalarından yönetilir.
2. Değişiklikten sonra **mutlaka** `python3 build.py` çalıştırılmalıdır.
3. Build sonrası `git push origin main` ile GitHub Pages'e yayınlanır.

## Dizin Yapısı

```
.
├── index.html              # TR Ana Sayfa (GitHub Pages root)
├── en/index.html           # EN Ana Sayfa
├── content/
│   ├── tr/
│   │   ├── publications/   # 19 yayın kaydı (.md)
│   │   ├── projeler/       # 5 proje kaydı (.md)
│   │   ├── lab-araclari/   # İnteraktif araçlar
│   │   ├── acik-dersler/   # Ders materyalleri
│   │   ├── tekrarlanabilir-kod/
│   │   └── bulten-podcast/
│   └── en/
│       ├── publications/
│       ├── projects/
│       ├── interactive-tools/
│       ├── open-teaching/
│       ├── reproducible-hub/
│       └── writing-podcast/
├── assets/
│   ├── images/             # profil.jpg, profil_thumb.jpg
│   ├── pdfs/
│   └── audio/
├── build.py                # Markdown → HTML derleme betiği
├── CV_Ozyildirim.pdf
└── GEMINI.md               # Bu dosya (proje kuralları)
```
