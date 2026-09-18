---
Tarih: <% tp.date.now("YYYY-MM-DD") %>
Hafta: <% tp.date.now("YYYY-[W]WW") %>
---

# Haftalık Review — <% tp.date.now("DD MMMM YYYY", 0, "tr") %>

```dataviewjs
// ============================================================
// DİNAMİK HAFTALIK REVIEW — otomatik vault özeti
// ============================================================

function formatTarih(dt) {
    if (!dt) return "—";
    try { return dt.toFormat("dd MMM · HH:mm"); } catch(e) { return String(dt).slice(0,16); }
}

function gunOncesi(n) { return dv.date("today").minus({ days: n }); }
function rozet(renk, metin) {
    return `<span style="background:${renk}22;color:${renk};border:1px solid ${renk}44;border-radius:4px;padding:1px 7px;font-size:0.8em">${metin}</span>`;
}

const YEDI   = gunOncesi(7);
const ON_DORT = gunOncesi(14);

// ── ÖZET SAYAÇLAR ─────────────────────────────────────────────
const buHaftaNotlar  = dv.pages('"Notlar"').where(p => p.file.ctime >= YEDI);
const buHaftaFikirler= dv.pages('"Çalışma Fikirleri"').where(p => p.file.ctime >= YEDI);
const degisilenNotlar= dv.pages("").where(p => p.file.mtime >= YEDI && p.file.ctime < YEDI);
const aktifProjeler  = dv.pages('"Projeler"').where(p => p.Durum === "aktif" || p.Durum === "yazılıyor");

dv.paragraph(`<div style="background:var(--background-secondary);border-radius:10px;padding:14px 20px;margin:12px 0 20px 0;border-left:4px solid #4A90D9">
<strong>Bu haftanın özeti</strong> · ${new Date().toLocaleDateString('tr-TR',{weekday:'long',day:'numeric',month:'long'})}
<div style="display:flex;gap:16px;margin-top:10px;flex-wrap:wrap">
  <div><span style="font-size:1.5em;font-weight:700;color:#4A90D9">${buHaftaNotlar.length}</span> <span style="opacity:0.6;font-size:0.85em">yeni not</span></div>
  <div><span style="font-size:1.5em;font-weight:700;color:#E8724A">${buHaftaFikirler.length}</span> <span style="opacity:0.6;font-size:0.85em">yeni fikir</span></div>
  <div><span style="font-size:1.5em;font-weight:700;color:#7BC67E">${aktifProjeler.length}</span> <span style="opacity:0.6;font-size:0.85em">aktif proje</span></div>
  <div><span style="font-size:1.5em;font-weight:700;color:#B57BCC">${degisilenNotlar.length}</span> <span style="opacity:0.6;font-size:0.85em">güncellenen not</span></div>
</div>
</div>`);

// ── BU HAFTA EKLENEN NOTLAR ────────────────────────────────────
if (buHaftaNotlar.length > 0) {
    dv.header(4, "📄 Bu Hafta Eklenen Notlar");
    dv.table(
        ["Not", "Eklenme", "Klasör"],
        buHaftaNotlar.sort(p => p.file.ctime, "desc").map(p => [
            p.file.link,
            formatTarih(p.file.ctime),
            p.file.folder.split("/").pop() || "kök"
        ])
    );
}

// ── BU HAFTA EKLENEN FİKİRLER ─────────────────────────────────
if (buHaftaFikirler.length > 0) {
    dv.header(4, "💡 Bu Hafta Eklenen Fikirler");
    dv.table(
        ["Fikir", "Konu", "Tür"],
        buHaftaFikirler.sort(p => p.file.ctime, "desc").map(p => [
            p.file.link,
            p.Konu ? (Array.isArray(p.Konu) ? p.Konu.slice(0,2).join(", ") : p.Konu) : "—",
            p.Tür ? (Array.isArray(p.Tür) ? p.Tür[0] : p.Tür) : "—"
        ])
    );
}

// ── GÜNCELLENEN NOTLAR ─────────────────────────────────────────
if (degisilenNotlar.length > 0) {
    dv.header(4, "✏️ Güncellenen Notlar");
    dv.table(
        ["Not", "Son Değişiklik"],
        degisilenNotlar.sort(p => p.file.mtime, "desc").limit(10).map(p => [
            p.file.link,
            formatTarih(p.file.mtime)
        ])
    );
}

// ── AKTİF PROJELER ────────────────────────────────────────────
if (aktifProjeler.length > 0) {
    dv.header(4, "🚀 Aktif Projeler Durumu");
    dv.table(
        ["Proje", "Durum", "Son Güncelleme"],
        aktifProjeler.sort(p => p.file.mtime, "desc").map(p => [
            p.file.link,
            rozet(p.Durum==="aktif"?"#7BC67E":"#4A90D9", p.Durum),
            formatTarih(p.file.mtime)
        ])
    );
}
```

---

## ⚡ Bu Hafta Ne İlerledi?

| Proje | Ne yapıldı |
|-------|-----------|
|  |  |

---

## 🚧 Takılı Kalanlar

- 

---

## 💡 Bu Hafta Aklıma Gelenler
*Aşağıdaki fikirler otomatik listelendi — bunları Çalışma Fikirleri klasörüne taşıyın*

- 

---

## 📬 Bekleyen Dış Yanıtlar

| Kişi / Platform | Konu | Gönderim Tarihi |
|----------------|------|-----------------|
|  |  |  |

---

## 📅 Önümüzdeki Hafta Öncelikler

1. 
2. 
3. 

---

## 🔄 Projeye Taşınacak Fikirler?

- [ ] 
