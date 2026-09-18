// 00 Kontrol Merkezi/scripts/moc_panorama/view.js
// Çatı MOC Domain Panoraması & Bilgi Haritası (DataviewJS + Mermaid Subgraphs)

const currentFile = dv.current()?.file;
if (!currentFile) {
    dv.paragraph("⚠️ *Aktif MOC dosyası bilgisi alınamadı.*");
    return;
}

const mocTitle = currentFile.name;
const mocPath = currentFile.path;

// Yardımcı Fonksiyonlar
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

// 1. Bu MOC'a ait tüm notları tara
const allNotes = dv.pages('"Notlar"');
const allIdeas = dv.pages('"Çalışma Fikirleri"');

let domainCores = [];
let domainFeeders = [];
let domainMechs = new Map(); // Mech -> Set of Note Names

allNotes.forEach(p => {
    const pFm = p.file.frontmatter || {};
    const pDizin = toList(pFm["DİZİN"] || pFm["dizin"]);
    const pOdak = toList(pFm["ODAK"] || pFm["odak"]);
    const pTur = toList(pFm["Tür"] || pFm["tür"]);
    const pMechs = toList(pFm["MEKANİZMA"] || pFm["mekanizma"]);
    
    // MOC eşleşmesi kontrolü (Dizin, Odak veya dosya içi outlinks)
    const isDirectMember = pDizin.includes(mocTitle) || 
                           pDizin.some(d => mocTitle.includes(d) || d.includes(mocTitle.replace("00_", "").replace("_MOC", ""))) ||
                           (currentFile.outlinks && currentFile.outlinks.map(l => l.fileName).includes(p.file.name));
    
    if (isDirectMember) {
        const isCore = pTur.some(t => t.toLowerCase().includes("çekirdek") || t.toLowerCase().includes("cekirdek"));
        const noteObj = {
            name: p.file.name,
            path: p.file.path,
            mechs: pMechs,
            linkedNotes: toList(pFm["BAĞLANTILI NOTLAR"]),
            evidence: pFm["evidence_direction"] || pFm["study_type"] || "Not"
        };

        if (isCore) {
            domainCores.push(noteObj);
        } else {
            domainFeeders.push(noteObj);
        }

        // Mekanizma frekansı
        pMechs.forEach(m => {
            if (!domainMechs.has(m)) domainMechs.set(m, []);
            domainMechs.get(m).push(p.file.name);
        });
    }
});

// Eğer doğrudan eşleşme çok azsa, genel Notlar klasöründeki Odak köprülüleri de topla
if (domainCores.length === 0 && domainFeeders.length === 0) {
    allNotes.forEach(p => {
        const pFm = p.file.frontmatter || {};
        const pTur = toList(pFm["Tür"] || pFm["tür"]);
        const isCore = pTur.some(t => t.toLowerCase().includes("çekirdek") || t.toLowerCase().includes("cekirdek"));
        const noteObj = {
            name: p.file.name,
            path: p.file.path,
            mechs: toList(pFm["MEKANİZMA"]),
            linkedNotes: toList(pFm["BAĞLANTILI NOTLAR"]),
            evidence: pFm["evidence_direction"] || "Not"
        };
        if (isCore) domainCores.push(noteObj);
        else domainFeeders.push(noteObj);
    });
    domainCores = domainCores.slice(0, 3);
    domainFeeders = domainFeeders.slice(0, 6);
}

// 2. Bu Domain ile İlgili Çalışma Fikirleri
let domainIdeas = [];
allIdeas.forEach(idea => {
    const outlinks = idea.file.outlinks ? idea.file.outlinks.map(l => l.fileName) : [];
    const isLinkedToMoc = outlinks.includes(mocTitle) || (currentFile.outlinks && currentFile.outlinks.map(l => l.fileName).includes(idea.file.name));
    const isLinkedToDomainNotes = domainCores.some(c => outlinks.includes(c.name)) || domainFeeders.some(f => outlinks.includes(f.name));
    
    if (isLinkedToMoc || isLinkedToDomainNotes) {
        domainIdeas.push({
            name: idea.file.name,
            path: idea.file.path
        });
    }
});

// 3. MERMAID SUBGRAPH DİYAGRAMI
let nodeCount = 0;
const nodeMap = new Map();
const clickDirectives = [];

function getOrSetNode(name, path) {
    if (!nodeMap.has(name)) {
        nodeCount++;
        const id = `M${nodeCount}`;
        nodeMap.set(name, id);
        if (path) {
            clickDirectives.push(`    click ${id} "${getVaultUri(path)}" "Notu Aç"`);
        }
    }
    return nodeMap.get(name);
}

let mLines = [];
mLines.push("flowchart LR");

// Stiller
mLines.push("    classDef moc fill:#2e1065,stroke:#c084fc,stroke-width:3px,color:#faf5ff,font-weight:bold;");
mLines.push("    classDef core fill:#4c0519,stroke:#fb7185,stroke-width:2.5px,color:#fff1f2,font-weight:bold;");
mLines.push("    classDef feeder fill:#064e3b,stroke:#34d399,stroke-width:1.5px,color:#ecfdf5;");
mLines.push("    classDef hub fill:#172554,stroke:#60a5fa,stroke-width:2px,color:#dbeafe,font-weight:bold;");
mLines.push("    classDef idea fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#fefce8,font-weight:bold;");

const mocId = getOrSetNode(mocTitle, mocPath);
mLines.push('    subgraph SUB_DOMAIN ["🏛️ DOMAIN ÇATISI"]');
mLines.push(`        ${mocId}["🏛️ <b>${wrapText(mocTitle, 24)}</b>"]:::moc`);
mLines.push("    end");

// Çekirdek Notlar Subgraph
if (domainCores.length > 0) {
    mLines.push('    subgraph SUB_CORES ["🔴 ÇEKİRDEK SENTEZ NOTLARI (' + domainCores.length + ')"]');
    domainCores.forEach(c => {
        const cId = getOrSetNode(c.name, c.path);
        mLines.push(`        ${cId}["🔴 ${wrapText(c.name, 22)}"]:::core`);
    });
    mLines.push("    end");
}

// Besleyici Notlar Subgraph
if (domainFeeders.length > 0) {
    mLines.push('    subgraph SUB_FEEDERS ["🟢 KANIT & BESLEYİCİ NOTLAR (' + domainFeeders.length + ')"]');
    domainFeeders.slice(0, 8).forEach(f => {
        const fId = getOrSetNode(f.name, f.path);
        mLines.push(`        ${fId}["🟢 ${wrapText(f.name, 20)}"]:::feeder`);
    });
    mLines.push("    end");
}

// Popüler Mekanizma Hub'ları
const topMechs = Array.from(domainMechs.entries())
    .filter(([m, notes]) => notes.length >= 2)
    .sort((a, b) => b[1].length - a[1].length)
    .slice(0, 4);

if (topMechs.length > 0) {
    mLines.push('    subgraph SUB_MECHS ["🧬 ANA MEKANİZMA KÖPRÜLERİ"]');
    topMechs.forEach(([m, notes]) => {
        const mechId = getOrSetNode(`MECH_${m}`);
        mLines.push(`        ${mechId}["🧬 ${wrapText(m, 18)}<br/><i>(${notes.length} Not)</i>"]:::hub`);
    });
    mLines.push("    end");
}

// Çalışma Fikirleri Subgraph
if (domainIdeas.length > 0) {
    mLines.push('    subgraph SUB_IDEAS ["💡 ÇALIŞMA FİKİRLERİ & HİPOTEZLER (' + domainIdeas.length + ')"]');
    domainIdeas.slice(0, 5).forEach(i => {
        const iId = getOrSetNode(i.name, i.path);
        mLines.push(`        ${iId}["💡 ${wrapText(i.name, 22)}"]:::idea`);
    });
    mLines.push("    end");
}

// Bağlantılar (Edges)
// MOC -> Cores
domainCores.forEach(c => {
    const cId = getOrSetNode(c.name);
    mLines.push(`    ${mocId} ==>|Kapsar| ${cId}`);
});

// Feeders -> Cores
domainFeeders.slice(0, 8).forEach(f => {
    const fId = getOrSetNode(f.name);
    // Bağlı olduğu çekirdeğe ok çiz
    const targetCore = domainCores.find(c => f.linkedNotes.includes(c.name)) || (domainCores.length > 0 ? domainCores[0] : null);
    if (targetCore) {
        const cId = getOrSetNode(targetCore.name);
        mLines.push(`    ${fId} -->|Besler| ${cId}`);
    } else {
        mLines.push(`    ${fId} -.-> ${mocId}`);
    }
});

// Top Mechs -> Cores & Feeders
topMechs.forEach(([m, notes]) => {
    const mechId = getOrSetNode(`MECH_${m}`);
    domainCores.filter(c => c.mechs.includes(m)).forEach(c => {
        const cId = getOrSetNode(c.name);
        mLines.push(`    ${cId} -.-|Yolak| ${mechId}`);
    });
});

// Cores -> Ideas
domainIdeas.slice(0, 5).forEach(i => {
    const iId = getOrSetNode(i.name);
    if (domainCores.length > 0) {
        const cId = getOrSetNode(domainCores[0].name);
        mLines.push(`    ${cId} ==>|Hipotez| ${iId}`);
    } else {
        mLines.push(`    ${mocId} ==>|Fikir| ${iId}`);
    }
});

// Tıklama direktifleri
if (clickDirectives.length > 0) {
    mLines.push("\n    %% Tıklanabilir Bağlantılar");
    clickDirectives.forEach(cd => mLines.push(cd));
}

// Çizim
const mermaidCode = "```mermaid\n" + mLines.join("\n") + "\n```";
dv.paragraph(mermaidCode);

// Domain Navigasyon Tablosu
const tableRows = [];
if (domainCores.length > 0) {
    tableRows.push(["🔴 **Çekirdek Sentez Notları**", domainCores.map(c => `[[${c.name}]]`).join("<br/>")]);
}
if (domainFeeders.length > 0) {
    tableRows.push(["🟢 **Besleyici Kanıt Notları** (" + domainFeeders.length + ")", domainFeeders.map(f => `[[${f.name}]] <small><i>(${f.evidence})</i></small>`).join("<br/>")]);
}
if (topMechs.length > 0) {
    tableRows.push(["🧬 **En Sık Kesişen Mekanizmalar**", topMechs.map(([m, notes]) => `\`${m}\` <i>(${notes.length} not)</i>`).join(", ")]);
}
if (domainIdeas.length > 0) {
    tableRows.push(["💡 **Çalışma Fikirleri & Hipotezler** (" + domainIdeas.length + ")", domainIdeas.map(i => `[[${i.name}]]`).join("<br/>")]);
}

if (tableRows.length > 0) {
    dv.table(["Domain Katmanı", "İlişkili Notlar & Sayfa Önizlemeleri (Hover / Tıkla)"], tableRows);
}
