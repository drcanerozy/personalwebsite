---
tags: [dashboard, kokpit]
cssclasses: [dashboard]
---

```dataviewjs
// ════════════════════════════════════════════════════════════════
// 🚀 DR. CANER ÖZYILDIRIM — AKADEMİK ANA KOKPİT (MASTER DASHBOARD)
// ════════════════════════════════════════════════════════════════

const RENKLER = ["#7C6AF7","#4FC8A0","#F7A76A","#F76A8A","#6AB5F7","#C46AF7","#F7D76A","#6AF7C4","#A0C4FF","#FFB3C6"];

function linkAdi(v) {
  if (!v) return [];
  let arr = Array.isArray(v) ? v : [v];
  return arr.map(x => {
    if (!x) return null;
    if (typeof x === "object" && x.path) return x.path.split("/").pop().replace(".md","");
    return String(x).replace(/\[\[|\]\]/g,"").split("|")[0].trim();
  }).filter(Boolean);
}

function rozet(renk, metin) {
  return `<span style="background:${renk}18;color:${renk};border:1px solid ${renk}40;border-radius:6px;padding:2px 8px;font-size:0.8em;font-weight:600;display:inline-block">${metin}</span>`;
}

function bar(yuzde, renk="#7C6AF7") {
  const p = Math.min(100, Math.max(0, Math.round(yuzde)));
  return `<div style="background:var(--background-modifier-border, rgba(255,255,255,0.1));border-radius:4px;height:7px;width:100%;overflow:hidden;margin-top:4px"><div style="background:${renk};height:100%;width:${p}%"></div></div>`;
}

// ── VERİLERİ ÇEK (Standart JS Array Formatında) ────────────────
const notlarArray      = dv.pages('"Notlar"').array();
const fikirlerArray    = dv.pages('"Çalışma Fikirleri"').array();
const substackArray    = dv.pages('"Sosyal Medya/Substack"').where(p => p.file.name !== "Substack").array();
const clipHamArray     = dv.pages('"00 Kontrol Merkezi/Clippings"').array();
const zotHamArray      = dv.pages('"AI Kontrol Merkezi/Veri Pipeline/Zotero Ham"').array();
const nbHamArray       = dv.pages('"AI Kontrol Merkezi/Veri Pipeline/NotebookLM Ham"').array();
const hamToplam = clipHamArray.length + zotHamArray.length + nbHamArray.length;
const substackTamamlanan = substackArray.filter(p => p.DURUM === "tamamlandı" || p.DURUM === "tamamlandi" || p.DURUM === "yayinlandi");
const substackDevamEden  = substackArray.filter(p => p.DURUM === "devam ediyor" || p.DURUM === "taslak" || p.DURUM === "yazılıyor");
const substackFikir      = substackArray.filter(p => p.DURUM === "fikir" || (!substackTamamlanan.includes(p) && !substackDevamEden.includes(p)));

// ── BAŞLIK KARTI ──────────────────────────────────────────────
{ const _headerCard = dv.el("div", "", { cls: "kokpit-header-card", attr: { style: "background:var(--background-secondary, rgba(124,106,247,0.08));border:1px solid var(--background-modifier-border, rgba(124,106,247,0.25));border-radius:12px;padding:16px 20px;margin-bottom:20px" } });
  _headerCard.innerHTML = `
  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
    <div>
      <h1 style="margin:0;font-size:1.7em;letter-spacing:-0.5px">🧭 Akademik Ana Kokpit</h1>
      <p style="opacity:0.75;margin:3px 0 0 0;font-size:0.85em">${new Date().toLocaleDateString('tr-TR', {weekday:'long', day:'numeric', month:'long', year:'numeric'})} · Dr. Caner Özyıldırım</p>
    </div>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      ${rozet("#7C6AF7", `📚 ${notlarArray.length} Not`)}
      ${rozet("#F7A76A", `💡 ${fikirlerArray.length} Araştırma Fikri`)}
      ${rozet("#4FC8A0", `📢 ${substackArray.length} Substack`)}
      ${substackDevamEden.length > 0 ? rozet("#6AB5F7", `✍️ ${substackDevamEden.length} Devam Eden`) : ""}
      ${substackTamamlanan.length > 0 ? rozet("#4FC8A0", `✅ ${substackTamamlanan.length} Tamamlandı`) : ""}
      ${substackFikir.length > 0 ? rozet("#F7A76A", `💡 ${substackFikir.length} Fikir`) : ""}
      ${rozet(hamToplam > 0 ? "#F76A8A" : "#6AF7C4", `📥 ${hamToplam} Ham Girdi`)}
    </div>
  </div>
  <div style="margin-top:10px;padding-top:8px;border-top:1px dashed var(--background-modifier-border, rgba(124,106,247,0.2));font-size:0.85em;display:flex;gap:15px;flex-wrap:wrap">
    <span>⚡ <b>Hızlı Kılavuzlar & Panolar:</b></span>
    <a class="internal-link" href="Sosyal Medya/BAŞLANGIÇ PLANI.md">🚀 16 Haftalık Master Başlangıç Planı</a>
    <a class="internal-link" href="AI Kontrol Merkezi/Talimatlar & Kurallar/02_Akademik_Super_Komutlar_ve_Uretim_Playbook.md">⚡ Akademik Süper Komutlar Playbook</a>
    <a class="internal-link" href="00 Kontrol Merkezi/Dashboard_Gaps_and_Contradictions.md">⚖️ Null & Çelişkiler</a>
    <a class="internal-link" href="00 Kontrol Merkezi/Kitaplar.md">📚 Kitaplar</a>
    <a class="internal-link" href="00 Kontrol Merkezi/Graph_View_ve_Gorsellestirme_Rehberi.md">🧭 Graph Rehberi</a>
    <a class="internal-link" href="AI Kontrol Merkezi/Talimatlar & Kurallar/Vault_Bakim_ve_Entegrasyon_Protokolu.md">🏛️ Vault Protokolü</a>
  </div>
`; }

// ── 🔄 OTONOM FİKİR KULUÇKASI & SENKRONİZASYON SAYACI ───────────
const lastSyncCount = 180; // sync_vault.py tarafindan guncellenen taban
const currentNoteCount = notlarArray.length;
const diffCount = Math.max(0, currentNoteCount - lastSyncCount);
const cycleCount = diffCount % 10;
const remainingToTrigger = 10 - cycleCount;
const triggerPct = (cycleCount / 10) * 100;

{ const _syncCounter = dv.el("div", "", { attr: { style: "background:var(--background-primary, rgba(0,0,0,0.2));border:1px solid var(--background-modifier-border, rgba(79,200,160,0.3));border-radius:10px;padding:12px 16px;margin-bottom:20px" } });
  _syncCounter.innerHTML = `
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
    <span style="font-weight:600;font-size:0.9em">🔄 Otonom Kuluçka & Senkronizasyon Sayacı: <b>${cycleCount} / 10 Not</b></span>
    <span style="font-size:0.8em;opacity:0.8">${remainingToTrigger === 10 ? "🟢 Kasa Güncel & Kuluçka Tamamlandı" : `⚡ Yeni otonom sentez için <b>${remainingToTrigger} not</b> kaldı`}</span>
  </div>
  ${bar(triggerPct, "#4FC8A0")}
  <div style="margin-top:6px;font-size:0.8em;opacity:0.75;display:flex;justify-content:space-between">
    <span>💡 <i>Her 10 yeni notta MOC köprüleri ve yeni araştırma/Substack hipotezleri kendiliğinden kuluçkalanır.</i></span>
    <a class="internal-link" href="00 Kontrol Merkezi/Fikir Üretim Logu.md">🧬 Kuluçka Havuzunu Gör →</a>
  </div>
`; }

// ════════════════════════════════════════════════════════════════
// 1. AKTİF PROJELER & HEDEFLER (İş Takibi.md Tasks API)
// ════════════════════════════════════════════════════════════════
try {
  dv.header(2, "🎯 Aktif Projeler & Hedefler");
  const isTakibiSayfa = dv.page("00 Kontrol Merkezi/İş Takibi.md") || dv.page("İş Takibi");
  if (isTakibiSayfa && isTakibiSayfa.file && isTakibiSayfa.file.tasks) {
    const tasks = isTakibiSayfa.file.tasks.array();
    const grupMap = {};

    tasks.forEach(t => {
      let h = (t.header && t.header.subpath) ? t.header.subpath : "Genel Görevler";
      if (h.includes("Archive") || h === "İdari İşler") return;
      if (!grupMap[h]) grupMap[h] = { baslik: h, acik: 0, tamamlanan: 0 };
      if (t.completed) grupMap[h].tamamlanan++;
      else grupMap[h].acik++;
    });

    const projeListesi = Object.values(grupMap);
    projeListesi.forEach(p => {
      p.toplam = p.acik + p.tamamlanan;
      p.yuzde  = p.toplam > 0 ? Math.round((p.tamamlanan / p.toplam) * 100) : 0;
      p.skor   = (p.acik * 3) + p.yuzde;
    });

    // Açık görevi olanlar üstte (çoktan aza), %100 bitenler en altta
    const aktifler = projeListesi.filter(p => p.acik > 0).sort((a,b) => b.skor - a.skor);
    const bitenler = projeListesi.filter(p => p.acik === 0 && p.toplam > 0).sort((a,b) => b.toplam - a.toplam);
    const siraliProjeler = [...aktifler, ...bitenler];

    if (siraliProjeler.length > 0) {
      dv.table(
        ["Proje / Alan", "Açık Görev", "Tamamlanan", "İlerleme", "Durum"],
        siraliProjeler.map(p => {
          const renk = p.yuzde === 100 ? "#4FC8A0" : p.yuzde >= 50 ? "#7C6AF7" : "#F7A76A";
          const rozetRenk = p.yuzde === 100 ? "#4FC8A0" : p.acik > 0 ? "#F76A8A" : "#6AB5F7";
          const durumMetin = p.yuzde === 100 ? "✅ Tamamlandı" : `%${p.yuzde}`;
          return [
            p.yuzde === 100 ? `<span style="opacity:0.6">${p.baslik}</span>` : `**${p.baslik}**`,
            p.acik > 0 ? `<span style="color:#F76A8A;font-weight:700">${p.acik}</span>` : `<span style="opacity:0.3">0</span>`,
            p.tamamlanan,
            bar(p.yuzde, renk),
            rozet(rozetRenk, durumMetin)
          ];
        })
      );
    }
  }
} catch(e) {
  dv.paragraph("<span style='opacity:0.5'>Projeler yüklenirken bir sorun oluştu.</span>");
}

// ════════════════════════════════════════════════════════════════
// 📢 SUBSTACK YAYIN & İÇERİK YÖNETİM MASASI
// ════════════════════════════════════════════════════════════════
try {
  dv.header(2, `📢 Substack İçerik & Yayın Masası (${substackArray.length} Yazı/Fikir)`);

  { const _substackStats = dv.el("div", "");
    _substackStats.innerHTML = `
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px;padding:12px;background:var(--background-secondary, rgba(0,0,0,0.15));border-radius:8px;border:1px solid var(--background-modifier-border, rgba(255,255,255,0.1))">
      ${rozet("#6AB5F7", `✍️ Devam Eden: <b>${substackDevamEden.length}</b>`)}
      ${rozet("#F7A76A", `💡 Fikir Havuzu: <b>${substackFikir.length}</b>`)}
      ${rozet("#4FC8A0", `✅ Tamamlandı: <b>${substackTamamlanan.length}</b>`)}
      <span style="margin-left:auto;font-size:0.85em;opacity:0.8">
        <a class="internal-link" href="Sosyal Medya/Substack/Substack.md">📖 Substack MOC İndeksi →</a>
      </span>
    </div>
  `; }

  if (substackDevamEden.length > 0) {
    dv.header(3, `✍️ Devam Eden Yazılar (${substackDevamEden.length})`);
    dv.table(
      ["Yazı Başlığı", "No / Bölüm", "Odak Alanı", "Çatı MOC", "Durum"],
      substackDevamEden.map(p => [
        p.file.link,
        p.BOLUM_NO ? `#${p.BOLUM_NO}` : "—",
        p.ODAK || "—",
        p.DIZIN || "—",
        rozet("#6AB5F7", "⚡ Devam Ediyor")
      ])
    );
  }

  if (substackFikir.length > 0) {
    dv.header(3, `💡 Fikir Havuzu (${substackFikir.length})`);
    dv.table(
      ["Yazı Başlığı", "No / Bölüm", "Odak Alanı", "Çatı MOC", "Durum"],
      substackFikir.slice(0, 15).map(p => [
        p.file.link,
        p.BOLUM_NO ? `#${p.BOLUM_NO}` : "—",
        p.ODAK || "—",
        p.DIZIN || "—",
        rozet("#F7A76A", "💡 Fikir")
      ])
    );
    if (substackFikir.length > 15) {
      dv.paragraph(`<small style="opacity:0.75"><i>...ve ${substackFikir.length - 15} fikir daha mevcut. Tümünü görmek için <a class="internal-link" href="Sosyal Medya/Substack/Substack.md">Substack İndeksini</a> açabilirsiniz.</i></small>`);
    }
  }

  if (substackTamamlanan.length > 0) {
    dv.header(3, `✅ Tamamlanan / Yayınlananlar (${substackTamamlanan.length})`);
    dv.table(
      ["Yazı Başlığı", "No / Bölüm", "Odak Alanı", "Yayın Tarihi", "Durum"],
      substackTamamlanan.map(p => [
        p.file.link,
        p.BOLUM_NO ? `#${p.BOLUM_NO}` : "—",
        p.ODAK || "—",
        p.YAYIN_TARIHI || "—",
        rozet("#4FC8A0", "✅ Tamamlandı")
      ])
    );
  }
} catch(e) {
  dv.paragraph("<span style='opacity:0.5'>Substack panosu yüklenirken bir sorun oluştu.</span>");
}

// ════════════════════════════════════════════════════════════════
// 2. 10 ÇATI ALANI (Yoğunluğa Göre Çoktan Aza Sıralı)
// ════════════════════════════════════════════════════════════════
try {
  dv.header(2, "🗺️ 10 Çatı Araştırma Alanı (Yoğunluk Sıralı)");

  const CATILAR_RAW = [
    { id: "IF", ad: "Aralıklı Açlık (IF / TRF)", moc: "00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC", renk: "#4A90D9", keys: ["Aralıklı Açlık", "TRF", "Fasting", "Açlık"] },
    { id: "AD", ad: "Adipoz Doku & Obezite Biyolojisi", moc: "00_Adipoz Doku ve Metabolizma_MOC", renk: "#E8724A", keys: ["Adipoz Doku", "Obezite", "Adiposit", "Lipoliz"] },
    { id: "GLP1", ad: "GLP-1 & Farmakoterapi", moc: "00_GLP-1 ve Farmakolojik Müdahaleler_MOC", renk: "#7BC67E", keys: ["GLP-1", "Semaglutid", "Tirzepatid"] },
    { id: "UPF", ad: "Ultra İşlenmiş Besinler (UPF)", moc: "00_Ultra İşlenmiş Besinler ve Diyet Kalitesi_MOC", renk: "#E8C44A", keys: ["Ultra İşlenmiş", "UPF", "NOVA"] },
    { id: "ENERJI", ad: "Enerji Metabolizması & Dengesi", moc: "00_Kalori Kısıtlaması ve Enerji Metabolizması_MOC", renk: "#F7A76A", keys: ["Enerji Metabolizması", "Enerji Harcaması", "Kalori Kısıtlaması"] },
    { id: "METOD", ad: "Beslenme Metodolojisi & İstatistik", moc: "00_Beslenme Metodolojisi ve İstatistik_MOC", renk: "#6AB5F7", keys: ["İstatistik", "Metodoloji", "SEM", "Ölçek"] },
    { id: "AI", ad: "Yapay Zeka & Dijital Beslenme", moc: "00_Yapay Zeka ve Dijital Beslenme_MOC", renk: "#B57BCC", keys: ["Yapay Zeka", "Augmented Dietitian", "AI"] },
    { id: "IMMUN", ad: "Metabolik İmmünoloji & İnflamasyon", moc: "00_İnflamasyon ve İmmün Sistem_MOC", renk: "#E84A6F", keys: ["İmmün", "İnflamasyon", "Ferroptozis", "Tek Karbon"] },
    { id: "KLINIK", ad: "Klinik Beslenme & MNT", moc: "00_Klinik Beslenme ve Hastalıklarda Tıbbi Beslenme Tedavisi_MOC", renk: "#4FC8A0", keys: ["Klinik Nütrisyon", "Tıbbi Beslenme", "Enteral", "Parenteral"] },
    { id: "SOSYAL", ad: "Beslenmenin Sosyal & Politik Boyutları", moc: "00_Beslenme Tarihi ve Sosyal Boyutlar_MOC", renk: "#C46AF7", keys: ["Beslenme ve Sosyal", "Stigma", "Medya", "Politika"] }
  ];

  const catilarHesapli = CATILAR_RAW.map(c => {
    const notSayisi = notlarArray.filter(p => {
      const outlinks = (p.file.outlinks && p.file.outlinks.array) ? p.file.outlinks.array().map(l=>l.path) : [];
      const tags = (p.file.tags && p.file.tags.array) ? p.file.tags.array() : [];
      const text = [...outlinks, ...tags, p.file.name].join(" ").toLowerCase();
      return c.keys.some(k => text.includes(k.toLowerCase()));
    }).length;

    const fikirSayisi = fikirlerArray.filter(p => {
      const outlinks = (p.file.outlinks && p.file.outlinks.array) ? p.file.outlinks.array().map(l=>l.path) : [];
      const text = [...outlinks, p.file.name].join(" ").toLowerCase();
      return c.keys.some(k => text.includes(k.toLowerCase()));
    }).length;

    const alanSubstackSayisi = substackArray.filter(p => {
      const text = [p.DIZIN, p.ODAK, p.file.name].join(" ").toLowerCase();
      return c.keys.some(k => text.includes(k.toLowerCase())) || text.includes(c.id.toLowerCase());
    }).length;

    return { ...c, notSayisi, fikirSayisi, alanSubstackSayisi };
  }).sort((a,b) => b.notSayisi - a.notSayisi);

  const maxNot = Math.max(...catilarHesapli.map(c => c.notSayisi), 1);

  dv.table(
    ["Sıra", "Çatı Alan", "MOC Linki", "Not Sayısı", "Fikir Sayısı", "Substack", "Kütüphane Payı"],
    catilarHesapli.map((c, idx) => {
      const oran = Math.round((c.notSayisi / maxNot) * 100);
      return [
        `#${idx + 1}`,
        `**${c.ad}**`,
        `[[${c.moc}|🗺️ MOC'u Aç]]`,
        rozet(c.renk, `${c.notSayisi} not`),
        c.fikirSayisi > 0 ? rozet("#F7A76A", `${c.fikirSayisi} fikir`) : `<span style="opacity:0.3">—</span>`,
        c.alanSubstackSayisi > 0 ? rozet("#F76A8A", `📢 ${c.alanSubstackSayisi} içerik`) : `<span style="opacity:0.3">—</span>`,
        bar(oran, c.renk)
      ];
    })
  );
} catch(e) {
  dv.paragraph("<span style='opacity:0.5'>Çatı alanları yüklenirken bir sorun oluştu.</span>");
}

// ════════════════════════════════════════════════════════════════
// 3. EN ÇOK BAĞLANTI ALAN MERKEZ NOTLAR (Hub Notes Top 10)
// ════════════════════════════════════════════════════════════════
try {
  dv.header(2, "🔗 En Güçlü Merkez Notlar (Hub Notes)");

  const notLinkSkorlari = notlarArray.map(p => {
    const inlinks  = (p.file.inlinks && p.file.inlinks.array) ? p.file.inlinks.array().length : (p.file.inlinks ? p.file.inlinks.length : 0);
    const outlinks = (p.file.outlinks && p.file.outlinks.array) ? p.file.outlinks.array().length : (p.file.outlinks ? p.file.outlinks.length : 0);
    const toplam   = inlinks + outlinks;
    const tur      = linkAdi(p.TÜR)[0] || "Belirtilmemiş";
    return { page: p, inlinks, outlinks, toplam, tur };
  }).sort((a,b) => b.toplam - a.toplam).slice(0, 10);

  dv.table(
    ["Sıra", "Not Başlığı", "Tür", "Gelen (In)", "Giden (Out)", "Toplam Bağlantı"],
    notLinkSkorlari.map((n, idx) => [
      `#${idx + 1}`,
      n.page.file.link,
      rozet(n.tur === "Çekirdek" ? "#7C6AF7" : "#4FC8A0", n.tur),
      n.inlinks,
      n.outlinks,
      `<span style="font-weight:700;color:#6AB5F7;font-size:1.05em">${n.toplam}</span>`
    ])
  );
} catch(e) {
  dv.paragraph("<span style='opacity:0.5'>Hub notları yüklenirken bir sorun oluştu.</span>");
}

// ════════════════════════════════════════════════════════════════
// 3.1 🧬 ÇEKİRDEK NOTLARIN BESLENME GÜCÜ VE FEEDER MATRİSİ
// ════════════════════════════════════════════════════════════════
try {
  dv.header(2, "🧬 Çekirdek Notların Beslenme Gücü (Feeder Matrix)");

  // 1. Besleme Haritasını Çıkar
  const feederMap = {}; // { coreName: [feederPage, ...] }
  notlarArray.forEach(p => {
    const rawFeeders = p["BESLEDİĞİ NOTLAR"] || p["BESLEDİĞİ_NOTLAR"] || (p.file.frontmatter && p.file.frontmatter["BESLEDİĞİ NOTLAR"]);
    const targets = linkAdi(rawFeeders);
    targets.forEach(target => {
      if (!feederMap[target]) feederMap[target] = [];
      feederMap[target].push(p);
    });
  });

  // 2. Çekirdek Notları Filtrele ve Sırala
  const cekirdekNotlar = notlarArray.filter(p => {
    const tur = (linkAdi(p.TÜR)[0] || linkAdi(p.Tür)[0] || "").toLowerCase();
    return tur === "çekirdek" || tur === "cekirdek";
  });

  const cekirdekSkorlari = cekirdekNotlar.map(p => {
    const name = p.file.name.replace(".md", "");
    const feeders = feederMap[name] || [];
    return {
      page: p,
      name: name,
      feederCount: feeders.length,
      feeders: feeders
    };
  }).sort((a,b) => b.feederCount - a.feederCount);

  const maxFeeder = Math.max(...cekirdekSkorlari.map(c => c.feederCount), 1);

  // En Çok Beslenen Top 10 Çekirdek Not
  dv.table(
    ["Sıra", "Çekirdek Sentez Notu", "Besleyen Not Sayısı", "Olgunluk Düzeyi", "Örnek Besleyici Kanıtlar"],
    cekirdekSkorlari.slice(0, 10).map((c, idx) => {
      let durum = rozet("#F76A8A", "🔴 Kanıt Açlığı (0-1)");
      if (c.feederCount >= 5) durum = rozet("#4FC8A0", "🟢 Zengin Sentez (5+)");
      else if (c.feederCount >= 2) durum = rozet("#F7A76A", "🟡 Gelişiyor (2-4)");

      const sampleLinks = c.feeders.slice(0, 2).map(fp => fp.file.link).join(", ") || "<span style='opacity:0.4'>Henüz besleyici not yok</span>";

      return [
        `#${idx + 1}`,
        c.page.file.link,
        rozet("#7C6AF7", `🌱 ${c.feederCount} besleyici not`),
        durum,
        sampleLinks
      ];
    })
  );

  // Kanıt Açlığı Çeken (Under-Fed) Çekirdek Notlar Radarı
  const underFed = cekirdekSkorlari.filter(c => c.feederCount <= 1);
  if (underFed.length > 0) {
    { const _underFedBox = dv.el("div", "");
      _underFedBox.innerHTML = `
      <div style="background:rgba(247,106,138,0.08);border:1px dashed #F76A8A80;border-radius:8px;padding:10px 14px;margin-top:10px;font-size:0.85em">
        <b>🎯 Kanıt Açlığı Çeken Çekirdek Notlar (${underFed.length} Not):</b>
        <span style="opacity:0.8"> Literatür taramalarında (Zotero / PubMed) öncelikle bu başlıkları besleyecek atomik çalışmalar aranmalıdır:</span><br>
        <div style="margin-top:6px;display:flex;gap:8px;flex-wrap:wrap">
          ${underFed.slice(0, 8).map(u => `<span style="background:var(--background-primary);border:1px solid #F76A8A40;border-radius:4px;padding:2px 6px">${u.page.file.name} (${u.feederCount} besleyici)</span>`).join(" ")}
        </div>
      </div>
    `; }
  }

} catch(e) {
  dv.paragraph("<span style='opacity:0.5'>Feeder matrisi yüklenirken bir sorun oluştu.</span>");
}

// ════════════════════════════════════════════════════════════════
// 4. ODAK VE MEKANİZMA KÖPRÜLERİ (Tablo Formatında Kusursuz Render)
// ════════════════════════════════════════════════════════════════
try {
  dv.header(2, "🎯 En Çok Çalışılan Odaklar");

  let odakMap = {}, mekMap = {};
  notlarArray.forEach(p => {
    linkAdi(p.ODAK).forEach(o => { odakMap[o] = (odakMap[o] || 0) + 1; });
    linkAdi(p["MEKANİZMA"]).forEach(m => { mekMap[m] = (mekMap[m] || 0) + 1; });
  });

  const topOdaklar = Object.entries(odakMap).sort((a,b)=>b[1]-a[1]).slice(0, 8);
  const topMek     = Object.entries(mekMap).sort((a,b)=>b[1]-a[1]).slice(0, 8);

  const maxOdakSayi = topOdaklar.length > 0 ? topOdaklar[0][1] : 1;
  const maxMekSayi  = topMek.length > 0 ? topMek[0][1] : 1;

  dv.table(
    ["Sıra", "Odak Alanı", "Not Sayısı", "Yoğunluk Dağılımı"],
    topOdaklar.map(([o, s], idx) => {
      const yuzde = Math.round((s / maxOdakSayi) * 100);
      return [
        `#${idx + 1}`,
        `[[${o}]]`,
        rozet(RENKLER[idx % RENKLER.length], `${s} not`),
        bar(yuzde, RENKLER[idx % RENKLER.length])
      ];
    })
  );

  dv.header(2, "⚙️ En Sık Bağlanan Mekanizma Yolakları");

  dv.table(
    ["Sıra", "Mekanizma Yolağı", "Not Sayısı", "Köprü Ağırlığı"],
    topMek.map(([m, s], idx) => {
      const yuzde = Math.round((s / maxMekSayi) * 100);
      return [
        `#${idx + 1}`,
        `[[${m}]]`,
        rozet(RENKLER[(idx+3) % RENKLER.length], `${s} not`),
        bar(yuzde, RENKLER[(idx+3) % RENKLER.length])
      ];
    })
  );
} catch(e) {
  dv.paragraph("<span style='opacity:0.5'>Odak ve mekanizma tabloları yüklenirken bir sorun oluştu.</span>");
}

// ════════════════════════════════════════════════════════════════
// 5. ⚠️ YETİM / İZOLE NOT RADARI (Son 10 İzole Not)
// ════════════════════════════════════════════════════════════════
try {
  dv.header(2, "⚠️ Yetim / İzole Not Radarı (Hiçbir Yerden Bağlantı Almayanlar)");

  const yetimNotlar = notlarArray.filter(p => {
    const inlinks = (p.file.inlinks && p.file.inlinks.array) ? p.file.inlinks.array() : (p.file.inlinks || []);
    return inlinks.length === 0;
  }).sort((a,b) => {
    const at = a.file.mtime ? Number(a.file.mtime) || 0 : 0;
    const bt = b.file.mtime ? Number(b.file.mtime) || 0 : 0;
    return bt - at;
  }).slice(0, 10);

  if (yetimNotlar.length > 0) {
    dv.paragraph(`<p style="opacity:0.8;font-size:0.88em;margin-bottom:10px">Aşağıdaki notlar kasanızda henüz hiçbir not tarafından linklenmemiştir. Bir MOC'a veya ilgili nota bağladığınızda bu listeden otomatik olarak çıkarlar:</p>`);
    dv.table(
      ["İzole Not", "Giden Bağlantı", "Odak Durumu"],
      yetimNotlar.map(p => {
        const outlinks = (p.file.outlinks && p.file.outlinks.array) ? p.file.outlinks.array() : (p.file.outlinks || []);
        const odaklar = linkAdi(p.ODAK);
        return [
          p.file.link,
          outlinks.length > 0 ? rozet("#6AB5F7", `${outlinks.length} outlink`) : rozet("#F76A8A", "0 bağlantı"),
          odaklar.length > 0 ? odaklar.map(o => rozet("#7C6AF7", o)).join(" ") : `<span style="opacity:0.4;font-style:italic">Odak atanmamış</span>`
        ];
      })
    );
  } else {
    dv.paragraph("<span style='color:#4FC8A0;font-weight:600'>🎉 Harika! Kasanızda izole/yetim kalmış hiçbir not bulunmuyor.</span>");
  }
} catch(e) {
  dv.paragraph("<span style='opacity:0.5'>Yetim notlar yüklenirken bir sorun oluştu.</span>");
}
```



