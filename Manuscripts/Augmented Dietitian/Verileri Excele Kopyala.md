```dataviewjs
const pages = dv.pages('"Augmented Dietitian"')
  .where(p => p.file.name !== dv.current().file.name)
  .sort(p => p.Year, 'desc');

let csv = [];

// 1. BAŞLIKLAR (Senin istediğin sıralama ve isimler)
csv.push([
"Başlık",
  "Yazarlar",
  "Yıl",
  "Nitelik",
  "Alan",
  "Algoritma/Teknik",
  "Odak Katman",
  "Augmented Aşama",
  "Özel Notlarım",
  "Yöntem",
  "Bulgular",
  "Sonuç",          // Conclusions
  "Sınırlılıklar",  // Limitations
  "DOI"
].join("\t")); // Excel için TAB ile ayırıyoruz

for (let p of pages) {
  // 2. VERİLER (Obsidian'daki Property isimlerin)
  const row = [
  p.Title,
    p.Authors,
    p.Year,
    p.Nitelik,
    p.Alan,
    p.AI_Methodology,
    p.Layer_Focus,
    p.Model_Asamasi,
    p.User_Notes,
    p.Methods,
    p.Findings,
    p.Conclusions, // Sonuçlar eklendi
    p.Limitations, // Sınırlılıklar eklendi
    p.DOI
  ].map(v => 
    // Temizlik: Boş verileri düzelt, Enter ve Tab karakterlerini sil (Hücre kaymasın)
    (v ?? "").toString().replace(/[\n\r\t]/g, " ")
  );

  csv.push(row.join("\t"));
}

const csvText = csv.join("\n");

// 3. KOPYALAMA İŞLEMİ
await navigator.clipboard.writeText(csvText);

dv.paragraph("📋 **Veriler kopyalandı!** Excel'i açıp direkt yapıştırabilirsin (Ctrl+V).");
```
