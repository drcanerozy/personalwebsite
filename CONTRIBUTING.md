# Dr. Caner Özyıldırım Kişisel Web Sitesi — Katkı ve Yayın Rehberi

Bu belge, kişisel web sitesine (`canerozy.com`) yeni bilimsel yazı, ders notu veya sunum eklerken uyulması gereken SEO, URL ve şablon standartlarını içerir.

---

## 1. Mimari & Derleme İş Akışı

Web sitesi saf Python (`build.py`) ile Obsidian Markdown kaynaklarını statik HTML'e derler.

- **TR Makaleler:** `content/tr/articles/*.md`
- **EN Makaleler:** `content/en/articles/*.md`
- **Ders Notları & Kurslar:** `content/tr/teaching/*.md`, `content/en/teaching/*.md`
- **Ham Sunumlar (Obsidian):** `/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner/Dersler/`
- **Şifreli Canlı Sunumlar:** `slides/*.html`

### Siteyi Derleme & Test Etme

```bash
# 1. Siteyi derle
python3 build.py

# 2. Tüm iç linkleri doğrula (0 kırık link kuralı)
python3 scripts/check-links.py

# 3. Yerel önizleme
python3 -m http.server 8000
```

---

## 2. Yeni Makale Ekleme Kuralları (SEO & Transliterasyon)

Yeni bir makale yazıldığında TR ve EN sürümleri çift olarak eklenmeli ve aşağıdaki kurallara kesinlikle uyulmalıdır:

### 2.1. Slug & Transliterasyon Standardı
- **Türkçe Slug:** Türkçe karakterler (`ı, ş, ğ, ü, ö, ç, İ`) doğrudan ASCII eşdeğerlerine (`i, s, g, u, o, c, i`) çevrilmeli; asla karakter düşürülmemelidir.
  - *Doğru:* `aralikli-aclik-yapiyorsunuz-ama-ise-yaramiyor`
  - *Yanlış:* `aralkl-aclk-yapyorsunuz-ama-ise-yaramyor`
- **İngilizce Slug:** Başlıktan türetilmiş anlamlı İngilizce URL olmalıdır.
  - *Doğru:* `intermittent-fasting-gut-microbiome`

### 2.2. Eşleştirme (Bilingual Pairing)
İki dildeki sayfaların `xhtml:link` hreflang, canonical ve `workTranslation` / `translationOfWork` bağlantılarının doğru kurulması için frontmatter'da eşleştirme tanımlanmalıdır:
- TR dosyasında: `en_slug: "intermittent-fasting-gut-microbiome"`
- EN dosyasında: `tr_slug: "aralikli-aclik-yapiyorsunuz-ama-ise-yaramiyor"`

### 2.3. Meta Başlık & Açıklama (Limits)
- **Başlık (`title`):** Maksimum 50–55 karakter olmalıdır. Otomasyon sonuna ` | Caner Özyıldırım` eklediğinde toplam uzunluk **≤ 65 karakter** kalmalıdır.
- **Özet (`summary`):** Kesinlikle **140–160 karakter** aralığında olmalıdır. Ana anahtar kelime ilk 120 karakter içerisinde geçmelidir.
- **H1 Kuralı:** Makale içinde yalnızca 1 adet H1 (sayfa başlığı) olmalıdır. Gövde içindeki ara başlıklar `##` (H2) veya `###` (H3) olarak açılmalıdır.

### 2.4. Frontmatter Örneği

```yaml
---
title: "Aralıklı Açlık Yapıyorsunuz Ama İşe Yaramıyor: Mikrobiyota Faktörü"
date: "2026-10-08"
summary: "Aralıklı açlık yapmanıza rağmen kilo veremiyor musunuz? Bağırsak mikrobiyotası, SCFA üretimi ve GLP-1 salınımının metabolik etkilerini inceleyin."
badge: "Bilimsel Analiz"
read_time: "8 dk"
cover_image: "assets/images/articles/aralikli-aclik.jpg"
tags: ["Aralıklı Açlık", "Mikrobiyota", "Metabolizma"]
substack_url: "https://drcaner.substack.com/p/..."
is_local: true
en_slug: "intermittent-fasting-gut-microbiome"
---
```

---

## 3. Otomatik Yapılanlar (`build.py`)

Bir makale eklenip `python3 build.py` çalıştırıldığında sistem otomatik olarak:

1. **Blog Liste Sayfalarını Günceller:** `/yazilar/index.html` ve `/en/articles/index.html` (kategori filtreleri, `CollectionPage` + `ItemList` şeması).
2. **RSS 2.0 Beslemelerini Üretir:** `/yazilar/feed.xml` ve `/en/articles/feed.xml` (RFC-822 yayın tarihleri, autodiscovery).
3. **XML Sitemap & robots.txt:** `sitemap.xml` dosyasını `git log` üzerinden gerçek `lastmod` tarihleriyle ve çift dilli `xhtml:link` hreflang etiketleriyle üretir.
4. **E-E-A-T & Konu Kümeleri:**
   - Başlık altına "Yayın: {tarih} · Son Güncelleme: {tarih}" ekler.
   - Yazı sonuna Tıbbi Sorumluluk Reddi kutusu ekler.
   - Dr. Caner Özyıldırım Akdeniz Üniversitesi E-E-A-T yazar kutusunu ekler.
   - Ortak etiket ve anahtar kelime skorlaması ile 3 adet "İlgili Bilimsel Yazılar" kartını bağlar.
5. **Görsel Optimizasyonu:** Gövdedeki tüm görsellere `loading="lazy"` ve kartlara explicit boyutlar ekler.

---

## 4. Canlıya Alma (Commit & Deploy)

Her yeni içerik veya SEO güncellemesi sonrasında:

```bash
python3 build.py
python3 scripts/check-links.py
git add .
git commit -m "feat(content): add new scientific article on..."
git push origin main
```
