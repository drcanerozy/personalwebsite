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

---

## ⚡ TEK KOMUTLA SUNUM EKLEME & YAYINLAMA PROTOKOLÜ

Yeni bir sunum HTML dosyası geldiğinde **asla sıfırdan manuel işlem yapma**.
Tüm akış aşağıdaki tek komutla otomatik olarak yürütülür:

```bash
cd /Users/canerozyildirim/Sites/personalwebsite
python3 scripts/publish_presentation.py <sunum_dosyasi.html> --course <DERS_KODU> [--deploy]
```

### Ders Kodları ve Şifre Matrisi:
| Ders Kodu | Ders Adı | Şifre |
|---|---|---|
| `BES339` | Diyet İlkeleri ve Popüler Diyetler | `COZYPOP2026_` |
| `BES200` | Bilgisayar ve Yapay Zeka Uygulamaları | `COZYBESAI2026_` |
| `BES317` | Yetişkin Hastalıklarında Diyet Tedavisi | `COZYYHTBT2026_` |

### Bu Otomasyon Ne Yapar?
1. **Şifreleme:** İlk 10 slaytı açık önizleme bırakır, 11+ slaytları AES-256 (CryptoJS) ile şifreler.
2. **Kilit Ekranı Enjeksiyonu:** Öğrenci kilit ekranı, 10. slayt uyarı banner'ı ve çözücü motoru HTML'e gömer.
3. **Markdown Entegrasyonu:**
   - `content/tr/presentations/` ve `content/en/presentations/` altına sunum kartlarını yazar.
   - `content/tr/teaching/` ve `content/en/teaching/` altındaki ilgili ders dosyasına sunum linkini ve frontmatter'ını ekler.
4. **Build:** `build.py`'yi tetikleyerek tüm Türkçe/İngilizce ana sayfa ve ders sayfalarını derler.
5. **Deploy (`--deploy` flag'i ile):** `git add`, `commit` ve `git push origin main` ile değişikliği doğrudan GitHub Pages'e yayına alır.

---

## Genel İçerik Ekleme / Düzenleme Kuralları

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
│   │   ├── teaching/       # 7 ders modülü (.md)
│   │   ├── presentations/  # İnteraktif sunum kartları (.md)
│   │   ├── tekrarlanabilir-kod/
│   │   └── bulten-podcast/
│   └── en/
│       ├── publications/
│       ├── projects/
│       ├── interactive-tools/
│       ├── open-teaching/
│       ├── presentations/
│       ├── reproducible-hub/
│       └── writing-podcast/
├── slides/                 # AES-256 şifreli interaktif sunumlar (.html)
├── scripts/
│   ├── publish_presentation.py  # ⚡ Tek komutla sunum yayınlama motoru
│   └── generate_encrypted_evrim.py
├── build.py                # Markdown → HTML derleme betiği
├── CV_Ozyildirim.pdf
└── GEMINI.md               # Bu dosya (proje kuralları)
```
