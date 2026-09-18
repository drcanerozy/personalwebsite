---
title: Obsidian Kurulum Envanteri
amac: "Kurulu eklentileri, temayı, kısayolları ve snippet'leri tek bakışta hatırlamak için referans. Yeni bir şey kurduğunda/değiştirdiğinde buraya ekle."
son_guncelleme: 2026-09-05
---

# Obsidian Kurulum Envanteri

## Tema ve Görünüm
- **Tema**: Minimal
- **Yazı tipi**: Inter (metin), 16px taban boyut
- **CSS Snippet'ler** (Ayarlar > Görünüm > CSS Snippet'ler altından açık/kapalı):
  - `akademik_estetik.css`
  - `mermaid-scroll.css`
  - `tablo-genisletici.css`

## Kurulu Topluluk Eklentileri (24 adet)
| Eklenti | Muhtemel amacı |
|---|---|
| Dataview | Notlardan sorgu/tablo üretme (dashboard'ların çoğu buna dayanıyor) |
| Templater | Şablon otomasyonu (Templates/ klasöründeki şablonlar) |
| obsidian-kanban | Pano/görev takibi |
| obsidian-mind-map | Zihin haritası görünümü |
| obsidian-style-settings | Tema/snippet ayarlarını tek panelden yönetme |
| advanced-canvas | Canvas dosyaları için ek özellikler (.canvas dosyaların) |
| obsidian-admonition | Not içinde renkli kutular (info/warning vb.) |
| obsidian-image-toolkit | Görsel önizleme/zoom |
| obsidian-excalidraw-plugin | Excalidraw çizimleri (.excalidraw dosyaların) |
| obsidian-zotero-desktop-connector | Zotero entegrasyonu |
| smart-connections | AI destekli not bağlantı önerisi (.smart-env klasörü buradan) |
| obsidian-pandoc / obsidian-pandoc-reference-list | Pandoc ile dışa aktarım + kaynakça |
| obsidian-table-to-csv-exporter | Tabloyu CSV'ye çevirme |
| obsidian-icon-folder | Klasörlere özel ikon |
| obsidian-advanced-slides | Not içinden sunum/slayt üretme |
| pdf-plus | PDF okuma/annotasyon geliştirmeleri |
| highlightr-plugin | Renkli vurgulama |
| notebooklm-bridge | NotebookLM entegrasyonu |
| zotero-lib-view | Zotero kütüphanesi görünümü |
| multi-properties | Birden fazla nota toplu property ekleme |
| excalibrain | Excalidraw tabanlı beyin haritası |
| notebook-navigator | Dosya gezgini alternatifi |
| table-editor-obsidian | Tablo düzenleme kolaylığı |
| copilot | AI sohbet eklentisi (plugin klasöründe var, community-plugins.json listesinde değil — kapalı olabilir, kontrol et) |

Not: `.obsidian/plugins/` klasöründe ayrıca şunlar da duruyor ama `community-plugins.json` listesinde değil (yani şu an **kapalı/etkin değil** ya da manuel silinmemiş eski kalıntılar): `obsidian-git`, `obsidian-tasks-plugin`, `obsidian42-brat`, `breadcrumbs`, `obsidian-importer`, `defter-eklenti`, `adsız klasör`, `adsız klasör 2`. Bunlardan hangilerinin bilerek kapatıldığını, hangilerinin denenip vazgeçildiğini kontrol etmek isteyebilirsin.

## Kendi Yazdığın Eklenti
- **defter-eklenti**: senin kendi geliştirdiğin, bir klasördeki notlar arasında oluşturulma/düzenlenme tarihine göre "defter sayfası çevirir gibi" gezinme eklentisi (bkz. `/areas/obsidian-defter-eklenti.md` hafıza notu). Şu an community-plugins.json listesinde görünmüyor — kapalı olabilir.

## Özel Kısayollar (Hotkeys)
Sadece defter-eklenti için tanımlı 3 özel kısayol var, gerisi Obsidian varsayılanları:
- `Alt+B` → Hızlı not yakalama (quick capture)
- `Alt+←` → Önceki sayfa
- `Alt+→` → Sonraki sayfa

## Bunu nasıl güncel tutarım?
- Yeni bir eklenti/snippet/kısayol kurduğunda bu dosyaya bir satır ekle (Claude'a "kurulum envanterini güncelle" diyebilirsin).
- Ayarlar penceresinin sol üstündeki arama kutusu, unuttuğun bir ayarı isimle aramanın en hızlı yolu.
- "Style Settings" eklentisi zaten kurulu — tema/snippet ayarlarının çoğunu tek panelden (Ayarlar > Style Settings) görebilirsin, dosya dosya aramana gerek kalmaz.
- `obsidian-git` eklentisi (şu an kapalı görünüyor) kasanı otomatik commit'lerse, `.obsidian/` klasöründeki değişiklikler de versiyonlanır — "ne zaman ne kurdum" sorusuna geçmiş git commit'lerinden cevap bulabilirsin.
