---
tags: [dashboard, kitaplar, library]
cssclasses: [dashboard]
---

# 📚 Kitaplar

> Notion'daki kapaklı galeri veritabanınız birebir Obsidian'a aktarılmıştır. Kartlara tıklayarak kitap notunuza, alıntılarınıza ve detaylara ulaşabilirsiniz.

```dataviewjs
await dv.view("00 Kontrol Merkezi/scripts/notion_book_gallery")
```

---

## 📋 Tablo Görünümü

```dataview
TABLE WITHOUT ID
  ("![](" + replace(replace(string(Kapak), "[[", ""), "]]", "") + ")") AS "Kapak",
  file.link AS "Kitap Adı",
  Yazar AS "Yazar",
  Kategori AS "Tür",
  Puan AS "Puan",
  Ay + " " + Yıl AS "Okunma Tarihi",
  Durum AS "Durum"
FROM "Kitaplar"
WHERE Tür = "Kitap"
SORT Yıl DESC, file.name ASC
```
