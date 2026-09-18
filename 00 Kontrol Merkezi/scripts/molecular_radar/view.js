// 00 Kontrol Merkezi/scripts/molecular_radar/view.js
// Akademik Ontoloji, Mekanizma & Fikir Radarı (DataviewJS + Mermaid Subgraphs + Genişletilmiş Matris)

const currentFile = dv.current()?.file;
if (!currentFile) {
    dv.paragraph("⚠️ *Aktif dosya bilgisi alınamadı.*");
    return;
}

// ==========================================
// 1. YARDIMCI FONKSİYONLAR
// ==========================================
function cleanLink(val) {
    if (!val) return "";
    if (typeof val === "object" && val.path) {
        return val.fileName || val.path.split("/").pop().replace(/\.md$/, "");
    }
    const str = String(val);
    return str.replace(/\[\[(.*?)\]\]/g, "$1").split("|")[0].replace(/\.md$/, "").trim();
}

function toList(val) {
    if (!val) return [];
    if (Array.isArray(val)) return val.map(cleanLink).filter(Boolean);
    return [cleanLink(val)].filter(Boolean);
}

// Başlıkları kelime kelime 2-3 satıra bölen Word-Wrap fonksiyonu (Kutudan taşmayı önler)
function wrapText(str, maxCharsPerLine = 22) {
    if (!str) return "";
    const clean = String(str).replace(/["#;:{}\[\]\(\)<>\/\\|]/g, " ").replace(/\s+/g, " ").trim();
    const words = clean.split(" ");
    let lines = [];
    let currentLine = "";

    for (let word of words) {
        if ((currentLine + " " + word).trim().length <= maxCharsPerLine) {
            currentLine = (currentLine + " " + word).trim();
        } else {
            if (currentLine) lines.push(currentLine);
            currentLine = word;
        }
    }
    if (currentLine) lines.push(currentLine);
    return lines.join("<br/>");
}

function getVaultUri(filePath) {
    const cleanPath = filePath.replace(/\.md$/, "");
    return `obsidian://open?vault=caner&file=${encodeURIComponent(cleanPath)}`;
}

// ==========================================
// 2. AKTİF NOT VERİLERİNİ ÇÖZÜMLEME
// ==========================================
const fm = currentFile.frontmatter || {};
const currentTitle = currentFile.name;
const currentPath = currentFile.path;

const turRaw = fm["Tür"] || fm["tür"] || fm["Tur"] || fm["tur"] || [];
const turList = toList(turRaw);
const isCore = turList.some(t => t.toLowerCase().includes("çekirdek") || t.toLowerCase().includes("cekirdek"));
const isFeeder = turList.some(t => t.toLowerCase().includes("besleyici"));

const odakList = toList(fm["ODAK"] || fm["odak"]);
let mechList = toList(fm["MEKANİZMA"] || fm["mekanizma"] || fm["Mekanizma"]);
let dizinList = toList(fm["DİZİN"] || fm["dizin"] || fm["Dizin"]);
const directLinkedNotes = toList(fm["BAĞLANTILI NOTLAR"] || fm["bağlantılı notlar"]);
let calismaFikirleri = toList(fm["BAĞLANTILI ÇALIŞMA FİKİRLERİ"] || fm["bağlantılı çalışma fikirleri"]);
let baglantiDersler = toList(fm["BAĞLANTILI DERSLER"] || fm["bağlantılı dersler"]);

// ==========================================
// 3. KASA GENELİ İLİŞKİ VE TERS-BAĞLANTI TARAMASI
// ==========================================
const allVaultNotes = dv.pages('"Notlar"').where(p => p.file.name !== currentTitle);
const allIdeas = dv.pages('"Çalışma Fikirleri"');

// A. Besleyicileri ve Çekirdekleri Belirle
let connectedFeeders = [];
let connectedCores = [];
let peerFeeders = [];

if (isCore) {
    // Aktif not ÇEKİRDEK ise: Onu besleyen tüm Besleyici notları bul
    allVaultNotes.forEach(p => {
        const pFm = p.file.frontmatter || {};
        const pTur = toList(pFm["Tür"] || pFm["tür"]);
        const pBaglanti = toList(pFm["BAĞLANTILI NOTLAR"]);
        const pIsFeeder = pTur.some(t => t.toLowerCase().includes("besleyici"));
        
        if (pIsFeeder && (pBaglanti.includes(currentTitle) || directLinkedNotes.includes(p.file.name))) {
            connectedFeeders.push({
                name: p.file.name,
                path: p.file.path,
                evidence: pFm["evidence_direction"] || pFm["study_type"] || "Besleyici Not",
                mechs: toList(pFm["MEKANİZMA"] || pFm["mekanizma"])
            });
        }
    });
} else if (isFeeder) {
    // Aktif not BESLEYİCİ ise: Bağlı olduğu Çekirdek notları bul
    allVaultNotes.forEach(p => {
        const pFm = p.file.frontmatter || {};
        const pTur = toList(pFm["Tür"] || pFm["tür"]);
        const pIsCore = pTur.some(t => t.toLowerCase().includes("çekirdek") || t.toLowerCase().includes("cekirdek"));
        const pBaglanti = toList(pFm["BAĞLANTILI NOTLAR"]);
        
        if (pIsCore && (directLinkedNotes.includes(p.file.name) || pBaglanti.includes(currentTitle))) {
            connectedCores.push({
                name: p.file.name,
                path: p.file.path,
                dizin: toList(pFm["DİZİN"])
            });
            // Eğer Besleyici notun DİZİN'i boşsa, beslediği Çekirdekten miras al
            if (dizinList.length === 0 && toList(pFm["DİZİN"]).length > 0) {
                dizinList = toList(pFm["DİZİN"]);
            }
        }
    });

    // Aynı Çekirdeği besleyen Kardeş Besleyicileri (Peer Feeders) bul
    if (connectedCores.length > 0) {
        const primaryCoreName = connectedCores[0].name;
        allVaultNotes.forEach(p => {
            const pFm = p.file.frontmatter || {};
            const pTur = toList(pFm["Tür"] || pFm["tür"]);
            const pBaglanti = toList(pFm["BAĞLANTILI NOTLAR"]);
            const pIsFeeder = pTur.some(t => t.toLowerCase().includes("besleyici"));
            
            if (pIsFeeder && pBaglanti.includes(primaryCoreName) && p.file.name !== currentTitle) {
                peerFeeders.push({
                    name: p.file.name,
                    path: p.file.path,
                    mechs: toList(pFm["MEKANİZMA"] || pFm["mekanizma"])
                });
            }
        });
    }
}

// B. Ortak Mekanizma Kardeşleri (Molecular Siblings)
let allMechSiblings = [];
if (mechList.length > 0) {
    allVaultNotes.forEach(p => {
        const pFm = p.file.frontmatter || {};
        const pMechs = toList(pFm["MEKANİZMA"] || pFm["mekanizma"]);
        const common = pMechs.filter(m => mechList.includes(m));
        const isAlreadyListed = connectedFeeders.some(f => f.name === p.file.name) || 
                                connectedCores.some(c => c.name === p.file.name) ||
                                peerFeeders.some(pf => pf.name === p.file.name);
        
        if (common.length > 0 && !isAlreadyListed) {
            allMechSiblings.push({
                name: p.file.name,
                path: p.file.path,
                commonCount: common.length,
                commonMechs: common,
                tur: toList(pFm["Tür"] || pFm["tür"])[0] || "Not"
            });
        }
    });
    // En çok ortak mekanizma paylaşandan en aza doğru sırala
    allMechSiblings.sort((a, b) => b.commonCount - a.commonCount);
}

// Grafikte gösterilecek en güçlü ilk 6 mekanizma kardeşi
const graphMechSiblings = allMechSiblings.slice(0, 6);

// C. Çalışma Fikirleri Ters-Bağlantı Taraması (Backlinks)
allIdeas.forEach(idea => {
    const outlinks = idea.file.outlinks ? idea.file.outlinks.map(l => l.fileName) : [];
    if (outlinks.includes(currentTitle) && !calismaFikirleri.includes(idea.file.name)) {
        calismaFikirleri.push(idea.file.name);
    }
});

// ==========================================
// 4. MERMAID SUBGRAPH DİYAGRAMI ÜRETİMİ
// ==========================================
let nodeCount = 0;
const nodeMap = new Map();
const clickDirectives = [];

function getOrSetNode(name, path) {
    if (!nodeMap.has(name)) {
        nodeCount++;
        const id = `N${nodeCount}`;
        nodeMap.set(name, id);
        if (path) {
            clickDirectives.push(`    click ${id} "${getVaultUri(path)}" "Notu Aç"`);
        }
    }
    return nodeMap.get(name);
}

let mLines = [];
mLines.push("flowchart LR");

// Stil Sınıfları
mLines.push("    classDef current fill:#0f172a,stroke:#38bdf8,stroke-width:3px,color:#ffffff,font-weight:bold;");
mLines.push("    classDef moc fill:#3b0764,stroke:#c084fc,stroke-width:2px,color:#faf5ff,font-weight:bold;");
mLines.push("    classDef core fill:#4c0519,stroke:#fb7185,stroke-width:2px,color:#fff1f2,font-weight:bold;");
mLines.push("    classDef feeder fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5;");
mLines.push("    classDef sibling fill:#1e293b,stroke:#94a3b8,stroke-width:1.5px,color:#f8fafc;");
mLines.push("    classDef idea fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#fefce8,font-weight:bold;");
mLines.push("    classDef lecture fill:#334155,stroke:#cbd5e1,stroke-width:1.5px,color:#ffffff;");

// 1. ÇATI DİZİN / MOC SUBGRAPH
if (dizinList.length > 0) {
    mLines.push('    subgraph SUB_MOC ["🏛️ ÇATI DİZİN / MOC"]');
    dizinList.forEach(moc => {
        const mocId = getOrSetNode(moc, `Dizin/${moc}.md`);
        mLines.push(`        ${mocId}["🏛️ ${wrapText(moc, 22)}"]:::moc`);
    });
    mLines.push("    end");
}

// 2. AKTİF NOT & ÇEKİRDEK / BESLEYİCİ SUBGRAPH
const currId = getOrSetNode(currentTitle, currentPath);
const currBadge = isCore ? "🔴 ÇEKİRDEK SENTEZ" : isFeeder ? "🟢 BESLEYİCİ KANIT" : "📄 AKADEMİK NOT";

if (isCore) {
    mLines.push('    subgraph SUB_CORE ["🔴 ÇEKİRDEK NOT"]');
    mLines.push(`        ${currId}["${currBadge}<br/><b>${wrapText(currentTitle, 24)}</b>"]:::current`);
    mLines.push("    end");

    if (connectedFeeders.length > 0) {
        mLines.push('    subgraph SUB_FEEDERS ["🟢 KANIT & BESLEYİCİ NOTLAR (' + connectedFeeders.length + ' Adet)"]');
        connectedFeeders.forEach(f => {
            const fId = getOrSetNode(f.name, f.path);
            mLines.push(`        ${fId}["🟢 ${wrapText(f.name, 22)}"]:::feeder`);
        });
        mLines.push("    end");
    }
} else if (isFeeder) {
    mLines.push('    subgraph SUB_FEEDER ["🟢 AKTİF BESLEYİCİ NOT"]');
    mLines.push(`        ${currId}["${currBadge}<br/><b>${wrapText(currentTitle, 24)}</b>"]:::current`);
    mLines.push("    end");

    if (connectedCores.length > 0) {
        mLines.push('    subgraph SUB_CORES ["🔴 BESLEDİĞİ ÇEKİRDEK SENTEZ"]');
        connectedCores.forEach(c => {
            const cId = getOrSetNode(c.name, c.path);
            mLines.push(`        ${cId}["🔴 ${wrapText(c.name, 24)}"]:::core`);
        });
        mLines.push("    end");
    }

    if (peerFeeders.length > 0) {
        mLines.push('    subgraph SUB_PEERS ["🤝 AYNI ÇEKİRDEĞİ BESLEYEN KARDEŞ NOTLAR"]');
        peerFeeders.slice(0, 4).forEach(pf => {
            const pfId = getOrSetNode(pf.name, pf.path);
            mLines.push(`        ${pfId}["📄 ${wrapText(pf.name, 22)}"]:::sibling`);
        });
        mLines.push("    end");
    }
} else {
    mLines.push(`    ${currId}["${currBadge}<br/><b>${wrapText(currentTitle, 24)}</b>"]:::current`);
}

// 3. ORTAK MEKANİZMA KARDEŞLERİ SUBGRAPH (İlk 6 En Güçlü Kesişim)
if (graphMechSiblings.length > 0) {
    mLines.push('    subgraph SUB_SIBLINGS ["🧬 EN YAKIN ORTAK MEKANİZMA KARDEŞLERİ"]');
    graphMechSiblings.forEach(sib => {
        const sId = getOrSetNode(sib.name, sib.path);
        const mechsLabel = wrapText(sib.commonMechs.join(", "), 18);
        mLines.push(`        ${sId}["🧬 ${wrapText(sib.name, 22)}<br/><i>(${mechsLabel})</i>"]:::sibling`);
    });
    mLines.push("    end");
}

// 4. ÇIKTILAR & ÇALIŞMA FİKİRLERİ SUBGRAPH
if (calismaFikirleri.length > 0 || baglantiDersler.length > 0) {
    mLines.push('    subgraph SUB_OUTPUTS ["💡 ÇALIŞMA FİKİRLERİ & DERSLER"]');
    calismaFikirleri.forEach(idea => {
        const iId = getOrSetNode(idea, `Çalışma Fikirleri/${idea}.md`);
        mLines.push(`        ${iId}["💡 ${wrapText(idea, 22)}"]:::idea`);
    });
    baglantiDersler.forEach(lec => {
        const lId = getOrSetNode(lec, `00 Kontrol Merkezi/Derslerim.md`);
        mLines.push(`        ${lId}["🎓 ${wrapText(lec, 20)}"]:::lecture`);
    });
    mLines.push("    end");
}

// ==========================================
// 5. BAĞLANTILARI ÇİZME (EDGES)
// ==========================================
// MOC -> Aktif Not
dizinList.forEach(moc => {
    const mocId = getOrSetNode(moc);
    mLines.push(`    ${mocId} ==>|Çatı Dizin| ${currId}`);
});

// Besleyiciler -> Çekirdek
if (isCore && connectedFeeders.length > 0) {
    connectedFeeders.forEach(f => {
        const fId = getOrSetNode(f.name);
        mLines.push(`    ${fId} -->|Besler & Kanıt| ${currId}`);
    });
} else if (isFeeder && connectedCores.length > 0) {
    connectedCores.forEach(c => {
        const cId = getOrSetNode(c.name);
        mLines.push(`    ${currId} -->|Besler| ${cId}`);
    });
    if (peerFeeders.length > 0 && connectedCores.length > 0) {
        const primaryCoreId = getOrSetNode(connectedCores[0].name);
        peerFeeders.slice(0, 4).forEach(pf => {
            const pfId = getOrSetNode(pf.name);
            mLines.push(`    ${pfId} -.->|Ayrıca Besler| ${primaryCoreId}`);
        });
    }
}

// Ortak Mekanizma Bağlantıları (Grafikteki Kardeşler)
if (graphMechSiblings.length > 0) {
    graphMechSiblings.forEach(sib => {
        const sId = getOrSetNode(sib.name);
        const mechsLabel = sib.commonMechs.slice(0, 2).join("+");
        mLines.push(`    ${currId} -.-|Ortak: ${mechsLabel}| ${sId}`);
    });
}

// Çıktılar (Çalışma Fikirleri ve Dersler)
calismaFikirleri.forEach(idea => {
    const iId = getOrSetNode(idea);
    mLines.push(`    ${currId} ==>|Hipotez / Fikir| ${iId}`);
});
baglantiDersler.forEach(lec => {
    const lId = getOrSetNode(lec);
    mLines.push(`    ${currId} -->|Ders Köprüsü| ${lId}`);
});

// Tıklanabilirlik Direktiflerini Ekle
if (clickDirectives.length > 0) {
    mLines.push("\n    %% Tıklanabilir Bağlantılar");
    clickDirectives.forEach(cd => mLines.push(cd));
}

// ==========================================
// 6. RENDER (GÖRSEL GRAFİK + İNTERAKTİF NAVİGASYON MATRİSİ)
// ==========================================
const mermaidCode = "```mermaid\n" + mLines.join("\n") + "\n```";
dv.paragraph(mermaidCode);

// İnteraktif Tıklanabilir Gezinme Tablosu
const rows = [];
if (dizinList.length > 0) {
    rows.push(["🏛️ **Çatı Dizin (MOC)**", dizinList.map(d => `[[${d}]]`).join("<br/>")]);
}
if (isCore && connectedFeeders.length > 0) {
    rows.push(["🟢 **Besleyen Kanıt Notları** (" + connectedFeeders.length + ")", connectedFeeders.map(f => `[[${f.name}]] <small><i>(${f.evidence})</i></small>`).join("<br/>")]);
}
if (isFeeder && connectedCores.length > 0) {
    rows.push(["🔴 **Beslediği Çekirdek Not**", connectedCores.map(c => `[[${c.name}]]`).join("<br/>")]);
    if (peerFeeders.length > 0) {
        rows.push(["🤝 **Kardeş Kanıt Notları** (" + peerFeeders.length + ")", peerFeeders.map(pf => `[[${pf.name}]]`).join("<br/>")]);
    }
}
if (mechList.length > 0) {
    rows.push(["🧬 **Temel Mekanizmalar**", mechList.map(m => `\`${m}\``).join(", ")]);
}

// TÜM Ortak Mekanizma Kardeşleri (Seçenek A Gereği Kapsamlı Liste)
if (allMechSiblings.length > 0) {
    const siblingListStr = allMechSiblings.map(s => {
        const mechStr = s.commonMechs.map(m => `\`${m}\``).join(", ");
        return `• [[${s.name}]] <small>(${s.commonCount} Ortak Mekanizma: ${mechStr})</small>`;
    }).join("<br/>");
    rows.push([`🔗 **Ortak Mekanizmalı Notlar (${allMechSiblings.length} Adet)**`, siblingListStr]);
}

if (calismaFikirleri.length > 0) {
    rows.push(["💡 **Çalışma Fikirleri & Hipotezler** (" + calismaFikirleri.length + ")", calismaFikirleri.map(i => `[[${i}]]`).join("<br/>")]);
}
if (baglantiDersler.length > 0) {
    rows.push(["🎓 **Ders Köprüleri**", baglantiDersler.map(d => `[[${d}]]`).join("<br/>")]);
}

if (rows.length > 0) {
    dv.table(["Katman / Ontoloji Boyutu", "İlişkili Notlar & Sayfa Önizlemeleri (Hover / Tıkla)"], rows);
}
