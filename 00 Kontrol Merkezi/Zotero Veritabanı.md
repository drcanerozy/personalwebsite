---
tags: [dashboard, zotero, literature-matrix, kontrol-merkezi]
BAŞLIK: "Zotero Okumalar Literatür Veritabanı & Araştırma Matrisi"
TOPLAM_MAKALE: 1562
SON_GÜNCELLEME: "2026-09-05"
---

# 📚 Zotero Veritabanı & Dinamik Literatür Matrisi

> **Kapsam:** Zotero `Okumalar` hiyerarşisi (`1562` Makale)  
> **Sıralama:** Zotero'ya Eklenme Tarihi (En yeniden en eskiye ↓)  
> **Puanlama:** Tamamen sizin kontrolünüzdedir (`rating: 5` verdikleriniz kalıcı arşiv rozeti alır ve Zotero'dan silinse de korunur).  
> **Tüm Detaylar:** Çıkarımlar, bulgular ve çalışma fikri gerekçeleri doğrudan tabloda görüntülenir.

---

## 🔍 Kütüphane İstatistikleri

```dataviewjs
const pages = dv.pages('"00 Kontrol Merkezi/Zotero Literatür"');
const total = pages.length;
const star5 = pages.where(p => p.rating === 5).length;
const rated = pages.where(p => p.rating > 0).length;
const withIdeas = pages.where(p => p.related_idea_link && p.related_idea_link.length > 0).length;

dv.paragraph(`📊 **Toplam Makale:** \`${total}\` | ⭐ **5 Yıldızlı Kalıcı Arşiv:** \`${star5}\` | 📝 **Puanladığınız:** \`${rated}\` | 🔬 **Çalışma Fikrine Bağlı:** \`${withIdeas}\``);
```

---

## 🎛️ Ana Literatür Matrisi (Tüm Çıkarımlar & Gerekçeler Tabloda)

> [!tip] 💡 Tablo İpuçları
> * Sütun başlıklarına tıklayarak herhangi bir kritere göre anında sıralayabilirsiniz.
> * Tablo doğrudan **Zotero'ya Eklenme Tarihine (`date_added`)** göre en yeniden en eskiye sıralıdır.
> * Makale notuna `rating: 5` (veya 1-4) yazarak puanlayabilirsiniz; puanlarınız senkronizasyon sırasında asla kaybolmaz.

```dataview
TABLE WITHOUT ID
  date_added as "Eklenme 📅",
  file.link as "Makale & Künye 📄",
  zotero_collection as "Klasör 📁",
  dizin as "Ana Dizin (MOC) 🧭",
  micro_topics as "Mikro-Konu (Odak) 🧬",
  takeaways as "Ana Çıkarımlar & Bulgular 💡",
  choice(related_idea_link, related_idea_link + "<br><br>🎯 <i>" + related_idea_rationale + "</i>", "—") as "İlişkili Çalışma Fikri & Gerekçesi 🔬",
  choice(rating = 5, "⭐⭐⭐⭐⭐<br>(Kalıcı Arşiv)", choice(rating > 0, rating + " ⭐", "—")) as "Puanınız ⭐"
FROM "00 Kontrol Merkezi/Zotero Literatür"
SORT date_added DESC
```

---

## 🔬 Sadece Çalışma Fikirlerinizle Katı Eşleşen Makaleler

```dataview
TABLE WITHOUT ID
  date_added as "Eklenme",
  file.link as "Makale",
  micro_topics as "Mikro-Konu",
  takeaways as "Bulgular / Çıkarımlar",
  related_idea_link + "<br><br>🎯 <i>" + related_idea_rationale + "</i>" as "Çalışma Fikri & Teknik Gerekçe"
FROM "00 Kontrol Merkezi/Zotero Literatür"
WHERE related_idea_link AND length(related_idea_link) > 0
SORT date_added DESC
```

---

## 🧬 Mikro-Konu ve Tematik Küme Gezgini
Tüm alt araştırma alanlarını ve kümelenmiş makaleleri tematik olarak incelemek için:
👉 **[[Dizin/00_Makale_Mikro_Konulari_MOC|00 — Makale Mikro-Konuları & Tematik Kümeler MOC]]**
