---
tags: [dashboard, kitaplar, library]
cssclasses: [dashboard]
---

# 📚 Kitaplar

> Notion'daki kapaklı galeri veritabanınız birebir Obsidian'a aktarılmıştır. Kartlara tıklayarak kitap notunuza, alıntılarınıza ve detaylara ulaşabilirsiniz.

```dataviewjs
// ════════════════════════════════════════════════════════════════
// 📊 DR. CANER ÖZYILDIRIM — KİTAPLIK MİNİ DASHBOARD & İSTATİSTİKLER
// ════════════════════════════════════════════════════════════════

const allPages = dv.pages('"Kitaplar"').array();
const bookPages = allPages.filter(p => (p.Tür || p.Type || "").toLowerCase() === "kitap");
const diziPages = allPages.filter(p => (p.Tür || p.Type || "").toLowerCase() === "dizi");
const filmPages = allPages.filter(p => (p.Tür || p.Type || "").toLowerCase() === "film");

// Yazarlar
const yazarSet = new Set();
bookPages.forEach(p => {
  const y = (p.Yazar || "").trim();
  if (y && y.toLowerCase() !== "kolektif") yazarSet.add(y);
});

// Kategoriler
const katMap = {};
bookPages.forEach(p => {
  const k = (p.Kategori || "Diğer").trim();
  if (k) katMap[k] = (katMap[k] || 0) + 1;
});
const sortedKat = Object.entries(katMap).sort((a,b) => b[1] - a[1]);

// Yıldız Dağılımı
const starMap = { 5: 0, 4: 0, 3: 0, 2: 0, 1: 0 };
let toplamPuan = 0, puanliKitap = 0;
bookPages.forEach(p => {
  let s = parseInt(p.Puan_Sayi) || 0;
  if (!s && p.Puan) {
    s = (String(p.Puan).match(/⭐|⭐️/g) || []).length;
  }
  if (s >= 1 && s <= 5) {
    starMap[s]++;
    toplamPuan += s;
    puanliKitap++;
  }
});
const ortalamaPuan = puanliKitap > 0 ? (toplamPuan / puanliKitap).toFixed(1) : "—";

// Yıllara Göre Dağılım (Yıl, Toplam Kitap, Roman Sayısı)
const yilMap = {};
bookPages.forEach(p => {
  const y = parseInt(p.Yıl);
  if (y && y > 2000) {
    if (!yilMap[y]) yilMap[y] = { toplam: 0, roman: 0, fikir: 0, diger: 0 };
    yilMap[y].toplam++;
    const k = (p.Kategori || "").toLowerCase();
    if (k.includes("roman")) yilMap[y].roman++;
    else if (k.includes("fikir")) yilMap[y].fikir++;
    else yilMap[y].diger++;
  }
});
const sortedYillar = Object.entries(yilMap).sort((a,b) => Number(b[0]) - Number(a[0]));

// Rozet ve Bar yardımcıları
function rozet(renk, metin) {
  return `<span style="background:${renk}18;color:${renk};border:1px solid ${renk}40;border-radius:6px;padding:3px 8px;font-size:0.85em;font-weight:600;display:inline-block">${metin}</span>`;
}
function bar(yuzde, renk="#7C6AF7") {
  const p = Math.min(100, Math.max(0, Math.round(yuzde)));
  return `<div style="background:var(--background-modifier-border, rgba(255,255,255,0.1));border-radius:4px;height:7px;width:100%;overflow:hidden;margin-top:3px"><div style="background:${renk};height:100%;width:${p}%"></div></div>`;
}

// 1. KPI KARTLARI
dv.el("div", `
<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:10px;margin-bottom:16px">
  <div style="background:var(--background-secondary, rgba(124,106,247,0.08));border:1px solid var(--background-modifier-border);border-radius:10px;padding:12px;text-align:center">
    <div style="font-size:1.6em;font-weight:700;color:#7C6AF7">📚 ${bookPages.length}</div>
    <div style="font-size:0.8em;opacity:0.8;font-weight:600">Okunan Kitap</div>
  </div>
  <div style="background:var(--background-secondary, rgba(79,200,160,0.08));border:1px solid var(--background-modifier-border);border-radius:10px;padding:12px;text-align:center">
    <div style="font-size:1.6em;font-weight:700;color:#4FC8A0">✍️ ${yazarSet.size}</div>
    <div style="font-size:0.8em;opacity:0.8;font-weight:600">Farklı Yazar</div>
  </div>
  <div style="background:var(--background-secondary, rgba(247,167,106,0.08));border:1px solid var(--background-modifier-border);border-radius:10px;padding:12px;text-align:center">
    <div style="font-size:1.6em;font-weight:700;color:#F7A76A">📖 ${katMap["Roman"] || 0}</div>
    <div style="font-size:0.8em;opacity:0.8;font-weight:600">Roman</div>
  </div>
  <div style="background:var(--background-secondary, rgba(247,215,106,0.08));border:1px solid var(--background-modifier-border);border-radius:10px;padding:12px;text-align:center">
    <div style="font-size:1.6em;font-weight:700;color:#eab308">⭐️ ${ortalamaPuan}</div>
    <div style="font-size:0.8em;opacity:0.8;font-weight:600">Ortalama Puan</div>
  </div>
  <div style="background:var(--background-secondary, rgba(106,181,247,0.08));border:1px solid var(--background-modifier-border);border-radius:10px;padding:12px;text-align:center">
    <div style="font-size:1.6em;font-weight:700;color:#6AB5F7">📺 ${diziPages.length + filmPages.length}</div>
    <div style="font-size:0.8em;opacity:0.8;font-weight:600">Dizi / Film</div>
  </div>
</div>
`);

// 2. YILDIZ PUAN DAĞILIMI & YILLARA GÖRE OKUMA (2 SÜTUNLU YAN YANA PANO)
dv.el("div", `
<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:16px;margin-bottom:20px">
  
  <!-- Yıldız Dağılımı Kutusu -->
  <div style="background:var(--background-secondary);border:1px solid var(--background-modifier-border);border-radius:12px;padding:16px">
    <div style="font-weight:700;font-size:0.95em;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center">
      <span>⭐️ Puan Dağılımı</span>
      <span style="font-size:0.8em;opacity:0.75">${puanliKitap} Değerlendirme</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:8px">
      ${[5, 4, 3, 2, 1].map(stars => {
        const count = starMap[stars];
        const pct = puanliKitap > 0 ? ((count / puanliKitap) * 100).toFixed(0) : 0;
        const starColor = stars >= 4 ? "#eab308" : stars === 3 ? "#F7A76A" : "#F76A8A";
        return `
          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.8em;margin-bottom:2px">
              <span>${"★".repeat(stars)}${"☆".repeat(5 - stars)} <small style="opacity:0.7">(${stars} Yıldız)</small></span>
              <span><b>${count}</b> <small style="opacity:0.65">(%${pct})</small></span>
            </div>
            ${bar(pct, starColor)}
          </div>
        `;
      }).join("")}
    </div>
  </div>

  <!-- Yıllara Göre Okuma Kutusu -->
  <div style="background:var(--background-secondary);border:1px solid var(--background-modifier-border);border-radius:12px;padding:16px">
    <div style="font-weight:700;font-size:0.95em;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center">
      <span>📅 Yıllara Göre Okuma Dağılımı</span>
      <span style="font-size:0.8em;opacity:0.75">Yıl / Kitap / Roman</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:8px">
      ${sortedYillar.map(([yil, data]) => {
        const maxKitap = Math.max(...sortedYillar.map(y => y[1].toplam), 1);
        const pct = (data.toplam / maxKitap) * 100;
        return `
          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.8em;margin-bottom:2px">
              <span><b>${yil}</b></span>
              <span>📚 <b>${data.toplam}</b> kitap <small style="opacity:0.75">(${data.roman} roman, ${data.fikir || 0} fikir)</small></span>
            </div>
            ${bar(pct, "#4FC8A0")}
          </div>
        `;
      }).join("")}
    </div>
  </div>

</div>
`);

// 3. TÜR VE KATEGORİ ROZETLERİ (Pills)
dv.el("div", `
<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px 14px;background:var(--background-secondary);border-radius:10px;border:1px solid var(--background-modifier-border);margin-bottom:20px;font-size:0.85em">
  <span style="font-weight:700;opacity:0.85;margin-right:4px">🏷️ Tür Dağılımı:</span>
  ${sortedKat.map(([k, count]) => {
    return rozet("#7C6AF7", `${k}: ${count}`);
  }).join(" ")}
</div>
`);
```

```dataviewjs
await dv.view("00 Kontrol Merkezi/scripts/notion_book_gallery")
```

---

## 📋 Tablo Görünümü

```dataviewjs
const monthMap = {
    "ocak": 1, "şubat": 2, "subat": 2, "mart": 3, "nisan": 4, "mayıs": 5, "mayis": 5,
    "haziran": 6, "temmuz": 7, "ağustos": 8, "agustos": 8, "eylül": 9, "eylul": 9,
    "ekim": 10, "kasım": 11, "kasim": 11, "aralık": 12, "aralik": 12
};

function getScore(p) {
    const y = parseInt(p.Yıl) || 0;
    const m = monthMap[(p.Ay || "").toString().toLowerCase().trim()] || 0;
    return y * 100 + m;
}

const kitaplar = dv.pages('"Kitaplar"')
    .where(p => (p.Tür || p.Type || "").toLowerCase() === "kitap")
    .array()
    .sort((a, b) => {
        const sA = getScore(a);
        const sB = getScore(b);
        if (sB !== sA) return sB - sA;
        return (Number(b.file?.mtime) || 0) - (Number(a.file?.mtime) || 0);
    });

dv.table(
    ["Kitap Adı", "Yazar", "Kategori", "Puan", "Okunma Tarihi", "Durum"],
    kitaplar.map(p => [
        p.file.link,
        p.Yazar || "—",
        p.Kategori || "—",
        p.Puan || "—",
        (p.Ay ? p.Ay + " " : "") + (p.Yıl || "—"),
        p.Durum || "—"
    ])
);
```
