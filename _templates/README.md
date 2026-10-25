# 📝 Obsidian Şablonları & Web Sitesi İçerik Yönetim Rehberi

Bu klasör (`_templates/`), web sitenizin tüm içeriklerini **Obsidian** üzerinden kolayca yönetmeniz için hazırlanmış hazır YAML şablonlarını içerir.

---

## 🚀 Nasıl Çalışır?

1. **Obsidian'da Not Açın:** 
   İstediğiniz şablonu (örneğin `tpl-publication.md` veya `tpl-tool.md`) kopyalayın ve ilgili içerik klasörüne yeni bir not olarak yapıştırın:
   - 📄 **Yayınlar:** `content/tr/publications/` ve `content/en/publications/`
   - 📂 **Sunumlar:** `content/tr/presentations/` ve `content/en/presentations/`
   - ⚙️ **Araçlar & AI:** `content/tr/tools/` ve `content/en/tools/`
   - ✍️ **Yazılar & Blog:** `content/tr/articles/` ve `content/en/articles/`
   - 🎙️ **Podcastler:** `content/tr/podcasts/` ve `content/en/podcasts/`
   - 🔬 **Projeler:** `content/tr/projects/` ve `content/en/projects/`
   - 🎓 **Dersler:** `content/tr/teaching/` ve `content/en/teaching/`
   - 👤 **Biyografi & Profil:** `content/tr/bio.md` ve `content/en/bio.md`

2. **Properties (YAML) Alanlarını Doldurun:**
   Başlık, linkler, tarihler ve özetleri doldurun.

3. **Web Sitesini Otomatik Derleyin:**
   Terminalde tek bir komut çalıştırın:
   ```bash
   python3 build.py
   ```
   *Bu komut hem Türkçe (`index.html`) hem İngilizce (`en/index.html`) sayfalarınızı 0.1 saniyede otomatik üretir!*

4. **GitHub'a Gönderin:**
   ```bash
   git add .
   git commit -m "update: içerikler güncellendi"
   git push
   ```

---

## 📋 Şablon Listesi

| Şablon Dosyası | Açıklama |
|---|---|
| `tpl-publication.md` | Makale, Kitap Bölümü ve Kongre Bildirisi (DOI, BibTeX, Halk Diliyle Özet) |
| `tpl-presentation.md` | Kongre & Ders Slaytları (Canlı HTML ve PDF indirme linkleri) |
| `tpl-tool.md` | R/Shiny, Python, Streamlit ve Web Hesaplayıcıları/Simülasyonları |
| `tpl-article.md` | Substack, Blog ve Popüler Bilim Yazıları |
| `tpl-podcast.md` | Spotify, Apple Podcasts ve YouTube Sesli Bölümleri |
| `tpl-project.md` | Fonlanan ve Yürütülen Bilimsel Projeler |
| `tpl-teaching.md` | Lisans/Lisansüstü Dersleri ve Laboratuvar Uygulamaları |
| `tpl-bio.md` | Akademik Özgeçmiş, Unvan, Metrikler ve Sosyal Bağlantılar |

---

## 💡 Obsidian İpuçları:
- **Obsidian Git Eklentisi:** Obsidian içinden otomatik `git backup / push` yapabilirsiniz.
- **Obsidian Shell Commands Eklentisi:** Notu kaydettiğinizde otomatik olarak `python3 build.py` çalıştıracak bir kısayol tuşu atayabilirsiniz.
