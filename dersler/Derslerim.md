---
tags: [dashboard]
cssclasses: [dashboard, dersler]
---

```dataviewjs
// ============================================================
// DERSLERİM DASHBOARD — Notion Gallery Görünümü
// ============================================================

function formatDonem(d) {
    if (d === "Güz") return `<span style="background:#E8C44A22;color:#A07830;border:1px solid #E8C44A44;border-radius:10px;padding:1px 8px;font-size:0.78em;font-weight:600">🍂 Güz</span>`;
    if (d === "Bahar") return `<span style="background:#7BC67E22;color:#3A7A4A;border:1px solid #7BC67E44;border-radius:10px;padding:1px 8px;font-size:0.78em;font-weight:600">🌸 Bahar</span>`;
    if (d === "Güz-Bahar") return `<span style="background:#4A90D922;color:#2F6EA8;border:1px solid #4A90D944;border-radius:10px;padding:1px 8px;font-size:0.78em;font-weight:600">📅 Yıllık</span>`;
    return `<span style="background:#88888822;color:#666;border-radius:10px;padding:1px 8px;font-size:0.78em">${d||"—"}</span>`;
}

function formatSinif(s) {
    const renkler = { 1: "#4A90D9", 2: "#7BC67E", 3: "#E8724A", 4: "#B57BCC" };
    const r = renkler[s] || "#888";
    return `<span style="background:${r}22;color:${r};border:1px solid ${r}44;border-radius:10px;padding:1px 8px;font-size:0.78em;font-weight:600">${s}. Sınıf</span>`;
}

const dersler = dv.pages('"Dersler"')
    .where(p => p.Ders_Adı)
    .sort(p => p.Sınıf || 99, "asc");

const KAPAKLARENK = {
    "🥗": ["#7BC67E", "#E8F5E9"],
    "🛡️": ["#E84A6F", "#FCE4EC"],
    "💉": ["#4A90D9", "#E3F2FD"],
    "🧬": ["#E8724A", "#FBE9E7"],
    "⚗️": ["#B57BCC", "#F3E5F5"],
    "🧠": ["#4A90D9", "#E1F5FE"],
    "📊": ["#5BAD7A", "#E8F5E9"],
    "🔍": ["#E8C44A", "#FFFDE7"],
    "📺": ["#E8724A", "#FFF3E0"],
    "🤖": ["#B57BCC", "#EDE7F6"],
    "🏥": ["#4A90D9", "#E3F2FD"],
    "🎓": ["#C5A059", "#FFFDE7"],
    "👶": ["#7BC67E", "#F1F8E9"],
};

// ── BAŞLIK ───────────────────────────────────────────────────
dv.paragraph(`<div style="padding:12px 0 24px 0">
<h1 style="margin:0;font-size:2em;letter-spacing:-0.5px">📚 Derslerim</h1>
<p style="opacity:0.5;margin:6px 0 0 0;font-size:0.9em">${dersler.length} ders · ${new Date().toLocaleDateString('tr-TR',{day:'numeric',month:'long',year:'numeric'})}</p>
</div>`);

// ── DÖNEM SAYAÇLARI ───────────────────────────────────────────
const guzDersler   = dersler.where(p => p.Dönem === "Güz").length;
const baharDersler = dersler.where(p => p.Dönem === "Bahar").length;

dv.paragraph(`<div style="display:flex;gap:8px;margin-bottom:28px;flex-wrap:wrap">
  <span style="background:var(--background-secondary);border-radius:8px;padding:6px 14px;font-size:0.85em">Tümü (${dersler.length})</span>
  <span style="background:#E8C44A22;color:#A07830;border:1px solid #E8C44A44;border-radius:8px;padding:6px 14px;font-size:0.85em">🍂 Güz (${guzDersler})</span>
  <span style="background:#7BC67E22;color:#3A7A4A;border:1px solid #7BC67E44;border-radius:8px;padding:6px 14px;font-size:0.85em">🌸 Bahar (${baharDersler})</span>
</div>`);

// ── GALLERY GRID ──────────────────────────────────────────────
let kartlar = dersler.map(p => {
    const kapak = p.Kapak || "📄";
    const [renkAna, renkAck] = KAPAKLARENK[kapak] || ["#888", "#F5F5F5"];
    const aciklama = p.Açıklama || "";
    const kisa = aciklama.length > 80 ? aciklama.slice(0, 80) + "…" : aciklama;

    return `<a class="internal-link" href="${p.file.path}" style="text-decoration:none;color:inherit">
  <div style="
    background:var(--background-secondary);
    border-radius:12px;
    overflow:hidden;
    border:1px solid rgba(0,0,0,0.06);
    transition:all 0.2s ease;
    cursor:pointer;
    display:flex;
    flex-direction:column;
  "
  onmouseover="this.style.boxShadow='0 6px 20px rgba(0,0,0,0.12)';this.style.transform='translateY(-2px)'"
  onmouseout="this.style.boxShadow='none';this.style.transform='translateY(0)'"
  >
    <div style="height:110px;background:${renkAck};display:flex;align-items:center;justify-content:center;font-size:3.2em;border-bottom:1px solid rgba(0,0,0,0.04)">${kapak}</div>
    <div style="padding:12px 14px 14px;flex:1;display:flex;flex-direction:column;gap:6px">
      <div style="font-weight:700;font-size:0.9em;line-height:1.3;color:var(--text-normal)">${p.Ders_Adı}</div>
      <div style="font-size:0.75em;opacity:0.55;line-height:1.4">${kisa}</div>
      <div style="display:flex;gap:5px;flex-wrap:wrap;margin-top:auto;padding-top:6px">
        ${formatDonem(p.Dönem)}
        ${p.Sınıf ? formatSinif(p.Sınıf) : ""}
      </div>
    </div>
  </div>
</a>`;
}).join("");

dv.paragraph(`<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;margin-bottom:40px">${kartlar}</div>`);

// ── İYİ UYGULAMALAR / FİKİRLER ───────────────────────────────
dv.header(2, "💡 İyi Uygulamalar & Fikirler");
dv.paragraph(`<div style="font-size:0.82em;opacity:0.5;margin:-10px 0 14px 0">Derslerde uygulamak istediğin teknikler, aktiviteler ve yenilikçi yaklaşımlar — <a class="internal-link" href="Dersler/İyi Uygulamalar.md">notun tamamını aç →</a></div>`);

// İyi Uygulamalar notunu oku ve önizle
const fikirNotu = dv.pages('"Dersler"').where(p => p.file.name === "İyi Uygulamalar").first();

if (fikirNotu) {
    dv.paragraph(`<div style="background:var(--background-secondary);border-radius:10px;padding:16px 20px;border-left:4px solid #C5A059;margin-bottom:8px">
      <a class="internal-link" href="${fikirNotu.file.path}" style="font-weight:600;color:#C5A059;text-decoration:none;font-size:0.95em">📝 İyi Uygulamalar & Fikirler →</a>
      <div style="font-size:0.82em;opacity:0.55;margin-top:6px">Son güncelleme: ${fikirNotu.file.mtime ? fikirNotu.file.mtime.toFormat("dd MMM yyyy") : "—"}</div>
    </div>`);
} else {
    dv.paragraph(`<div style="background:var(--background-secondary);border-radius:10px;padding:18px 22px;border:1px dashed rgba(197,160,89,0.5);text-align:center">
      <div style="opacity:0.45;font-style:italic;font-size:0.88em">
        "İyi Uygulamalar.md" notu henüz oluşturulmadı.<br>
        <span style="font-size:0.9em">Dersler klasörüne ekle, otomatik görünecek.</span>
      </div>
    </div>`);
}

// ── BİLİM KULÜBÜ ETKİNLİKLERİ ────────────────────────────────
dv.header(2, "🔬 Bilim Kulübü Etkinlikleri");

dv.paragraph(`<div style="background:var(--background-secondary);border-radius:10px;padding:16px 20px;border-left:4px solid #4A90D9">
  <div style="display:flex;flex-direction:column;gap:10px">
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-size:1.1em">📖</span>
      <span>Kitap okuma-eleştiri-kritik <em style="opacity:0.6">(Tahıl beyin ile başlıyoruz)</em></span>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-size:1.1em">🧪</span>
      <span>GLP-1 hakkında makale okuma etkinliği</span>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-size:1.1em">🎮</span>
      <span>Passaparola etkinliği</span>
    </div>
  </div>
</div>`);

// ── SINIF DAĞILIMI ────────────────────────────────────────────
dv.header(2, "📅 Sınıf Dağılımı");

const siniflar = [1,2,3,4];
let satirlar = siniflar.map(s => {
    let sinifDersler = dersler.where(p => p.Sınıf === s);
    if (sinifDersler.length === 0) return null;
    let isimler = sinifDersler.map(p => p.file.link).join("  ·  ");
    return [
        `${s}. Sınıf`,
        sinifDersler.where(p => p.Dönem === "Güz").length || "—",
        sinifDersler.where(p => p.Dönem === "Bahar").length || "—",
        isimler
    ];
}).filter(Boolean);

dv.table(["Sınıf","Güz","Bahar","Dersler"], satirlar);
```
