// Notion Style Gallery for DataviewJS (Kitaplar, Diziler, Filmler)
const container = dv.container;
container.innerHTML = "";

// Month Map for Chronological Sorting
const monthMap = {
    "ocak": 1, "şubat": 2, "subat": 2, "mart": 3, "nisan": 4, "mayıs": 5, "mayis": 5,
    "haziran": 6, "temmuz": 7, "ağustos": 8, "agustos": 8, "eylül": 9, "eylul": 9,
    "ekim": 10, "kasım": 11, "kasim": 11, "aralık": 12, "aralik": 12
};

function getReadingDateScore(p) {
    const year = parseInt(p.Yıl) || 0;
    const monthStr = (p.Ay || "").toString().toLowerCase().trim();
    const month = monthMap[monthStr] || 0;
    if (year > 0) {
        return year * 100 + month;
    }
    return 0;
}

// Fetch all items in Kitaplar folder - Sort: Son okunan (en yeni Yıl & Ay) -> İlk okunan
const rawPages = dv.pages('"Kitaplar"').array();
const pages = rawPages.sort((a, b) => {
    const scoreA = getReadingDateScore(a);
    const scoreB = getReadingDateScore(b);
    if (scoreB !== scoreA) {
        return scoreB - scoreA;
    }
    const timeA = a.file?.mtime ? Number(a.file.mtime) || 0 : 0;
    const timeB = b.file?.mtime ? Number(b.file.mtime) || 0 : 0;
    if (timeB !== timeA) {
        return timeB - timeA;
    }
    return (a.file?.name || "").localeCompare(b.file?.name || "", "tr");
});

if (pages.length === 0) {
    dv.paragraph("*Kitaplar klasöründe henüz kayıt bulunamadı.*");
    return;
}

// Category & Type Colors
function getCategoryStyle(cat) {
    const c = (cat || "").toLowerCase();
    if (c.includes("roman")) return "background: rgba(74, 158, 107, 0.18); color: #2b8251;";
    if (c.includes("fikir")) return "background: rgba(217, 115, 13, 0.18); color: #b85e00;";
    if (c.includes("öykü") || c.includes("oyku")) return "background: rgba(209, 87, 150, 0.18); color: #ad3374;";
    if (c.includes("akademik")) return "background: rgba(180, 115, 60, 0.18); color: #8f5424;";
    if (c.includes("günlük") || c.includes("gunluk")) return "background: rgba(13, 148, 136, 0.18); color: #0f766e;";
    if (c.includes("şiir") || c.includes("siir")) return "background: rgba(168, 85, 247, 0.18); color: #7e22ce;";
    if (c.includes("oyun")) return "background: rgba(234, 88, 12, 0.18); color: #c2410c;";
    return "background: rgba(100, 116, 139, 0.18); color: #475569;";
}

function getTypeIcon(t) {
    const type = (t || "").toLowerCase();
    if (type === "dizi") return "📺";
    if (type === "film") return "🎬";
    return "📖";
}

function getTypeStyle(t) {
    const type = (t || "").toLowerCase();
    if (type === "dizi") return "background: rgba(239, 68, 68, 0.15); color: #dc2626;";
    if (type === "film") return "background: rgba(245, 158, 11, 0.15); color: #d97706;";
    return "background: rgba(59, 130, 246, 0.15); color: #2563eb;";
}

// Extract Image URL or Resource Path
function getCoverSrc(page) {
    let cover = page.Kapak || page.cover || "";
    if (typeof cover === "object" && cover?.path) {
        cover = cover.path;
    }
    if (typeof cover === "string") {
        cover = cover.replace(/[\[\]"']/g, "").trim();
    }
    
    if (!cover) return null;
    
    if (cover.startsWith("http://") || cover.startsWith("https://")) {
        return cover;
    }
    
    const file = app.metadataCache.getFirstLinkpathDest(cover, "") || 
                 app.vault.getAbstractFileByPath("Files/" + cover) || 
                 app.vault.getAbstractFileByPath(cover);
    if (file) {
        return app.vault.adapter.getResourcePath(file.path);
    }
    return null;
}

// State
let selectedTypeFilter = "all";
let searchQuery = "";

// Counts
const totalCount = pages.length;
const booksCount = pages.filter(p => (p.Tür || p.Type || "").toLowerCase() === "kitap").length;
const seriesCount = pages.filter(p => (p.Tür || p.Type || "").toLowerCase() === "dizi").length;
const movieCount = pages.filter(p => (p.Tür || p.Type || "").toLowerCase() === "film").length;

// Root Wrapper
const rootWrapper = document.createElement("div");
rootWrapper.className = "notion-library-wrapper";
rootWrapper.style.cssText = "display: flex; flex-direction: column; gap: 16px; margin: 12px 0;";

// Header / Controls Bar
const controlsBar = document.createElement("div");
controlsBar.style.cssText = "display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; padding: 14px 18px; background: var(--background-secondary); border-radius: 12px; border: 1px solid var(--background-modifier-border);";

// Filter Tabs Container
const tabsDiv = document.createElement("div");
tabsDiv.style.cssText = "display: flex; flex-wrap: wrap; gap: 6px; align-items: center;";

const tabs = [
    { id: "all", label: `🌟 Tümü (${totalCount})` },
    { id: "kitap", label: `📖 Kitaplar (${booksCount})` },
    { id: "dizi", label: `📺 Diziler (${seriesCount})` },
    { id: "film", label: `🎬 Filmler (${movieCount})` }
];

tabs.forEach(tab => {
    const btn = document.createElement("button");
    btn.textContent = tab.label;
    btn.dataset.type = tab.id;
    btn.style.cssText = `padding: 6px 12px; font-size: 12px; font-weight: 600; border-radius: 6px; border: 1px solid var(--background-modifier-border); cursor: pointer; transition: all 0.15s ease; ${tab.id === selectedTypeFilter ? "background: var(--interactive-accent); color: var(--text-on-accent);" : "background: var(--background-primary); color: var(--text-normal);"}`;
    
    btn.onclick = () => {
        selectedTypeFilter = tab.id;
        tabsDiv.querySelectorAll("button").forEach(b => {
            b.style.background = "var(--background-primary)";
            b.style.color = "var(--text-normal)";
        });
        btn.style.background = "var(--interactive-accent)";
        btn.style.color = "var(--text-on-accent)";
        renderGrid();
    };
    tabsDiv.appendChild(btn);
});

// Right Controls Container (Search + New Book Button)
const rightControlsDiv = document.createElement("div");
rightControlsDiv.style.cssText = "display: flex; gap: 8px; align-items: center;";

// Search Input
const searchInput = document.createElement("input");
searchInput.type = "text";
searchInput.placeholder = "🔍 Başlık, yazar, tür veya yıl ara...";
searchInput.style.cssText = "padding: 7px 14px; font-size: 12.5px; border-radius: 8px; border: 1px solid var(--background-modifier-border); background: var(--background-primary); color: var(--text-normal); width: 220px; outline: none;";

// New Book Button
const newBookBtn = document.createElement("button");
newBookBtn.innerHTML = "✨ <b>+ Yeni Eser Ekle</b>";
newBookBtn.style.cssText = "padding: 7px 14px; font-size: 12.5px; font-weight: 600; border-radius: 8px; border: none; background: var(--interactive-accent); color: var(--text-on-accent); cursor: pointer; display: flex; align-items: center; gap: 6px; transition: opacity 0.15s ease; box-shadow: 0 2px 6px rgba(0,0,0,0.15);";
newBookBtn.onmouseenter = () => { newBookBtn.style.opacity = "0.9"; };
newBookBtn.onmouseleave = () => { newBookBtn.style.opacity = "1"; };

// Interactive Modal Form Function
function openNewBookModal() {
    const existingModal = document.getElementById("notion-new-book-modal-overlay");
    if (existingModal) existingModal.remove();

    const overlay = document.createElement("div");
    overlay.id = "notion-new-book-modal-overlay";
    overlay.style.cssText = "position: fixed; inset: 0; background: rgba(0,0,0,0.65); z-index: 9999; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(4px); padding: 20px;";

    const modal = document.createElement("div");
    modal.style.cssText = "background: var(--background-primary); border: 1px solid var(--background-modifier-border); border-radius: 14px; width: 100%; max-width: 520px; box-shadow: 0 20px 40px rgba(0,0,0,0.3); display: flex; flex-direction: column; overflow: hidden; animation: modalPop 0.2s ease;";

    const aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"];
    const currentMonth = aylar[new Date().getMonth()];
    const currentYear = new Date().getFullYear();

    modal.innerHTML = `
        <div style="padding: 18px 24px; border-bottom: 1px solid var(--background-modifier-border); display: flex; justify-content: space-between; align-items: center; background: var(--background-secondary);">
            <div style="font-size: 16px; font-weight: 700; color: var(--text-normal); display: flex; align-items: center; gap: 8px;">
                <span>📚</span> Yeni Kitap / Eser Ekle
            </div>
            <button id="modal-close-btn" style="background: none; border: none; font-size: 18px; cursor: pointer; color: var(--text-muted); padding: 4px 8px; border-radius: 4px;">✕</button>
        </div>
        <div style="padding: 22px 24px; display: flex; flex-direction: column; gap: 14px; max-height: 75vh; overflow-y: auto;">
            <div>
                <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Eser Adı / Başlık <span style="color:#ef4444">*</span></label>
                <input id="nb-title" type="text" placeholder="örn. Sapiens: Hayvanlardan Tanrılara" style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;" required />
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div>
                    <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Tür</label>
                    <select id="nb-tur" style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;">
                        <option value="Kitap" selected>📖 Kitap</option>
                        <option value="Dizi">📺 Dizi</option>
                        <option value="Film">🎬 Film</option>
                    </select>
                </div>
                <div>
                    <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Yazar / Yönetmen</label>
                    <input id="nb-yazar" type="text" placeholder="örn. Yuval Noah Harari" style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;" />
                </div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div>
                    <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Kategori / Konu</label>
                    <input id="nb-kategori" type="text" placeholder="örn. Fikir, Roman, Tarih..." style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;" />
                </div>
                <div>
                    <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Puan</label>
                    <select id="nb-puan" style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;">
                        <option value="5" selected>⭐️⭐️⭐️⭐️⭐️ (5 / 5)</option>
                        <option value="4">⭐️⭐️⭐️⭐️ (4 / 5)</option>
                        <option value="3">⭐️⭐️⭐️ (3 / 5)</option>
                        <option value="2">⭐️⭐️ (2 / 5)</option>
                        <option value="1">⭐️ (1 / 5)</option>
                    </select>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: 1.2fr 1fr 1fr; gap: 12px;">
                <div>
                    <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Okuma/İzleme Durumu</label>
                    <select id="nb-durum" style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;">
                        <option value="Bitti" selected>✅ Bitti</option>
                        <option value="Okunuyor">📖 Okunuyor / İzleniyor</option>
                        <option value="Sırada">⏳ Sırada / Okunacak</option>
                        <option value="Bırakıldı">❌ Bırakıldı</option>
                    </select>
                </div>
                <div>
                    <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Ay</label>
                    <select id="nb-ay" style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;">
                        ${aylar.map(a => `<option value="${a}" ${a === currentMonth ? "selected" : ""}>${a}</option>`).join("")}
                    </select>
                </div>
                <div>
                    <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Yıl</label>
                    <input id="nb-yil" type="number" value="${currentYear}" style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;" />
                </div>
            </div>
            <div>
                <label style="font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; display: block;">Kapak Görseli (İsteğe Bağlı)</label>
                <input id="nb-kapak" type="text" placeholder="Görsel URL'si (https://...) veya Files/kapak.png" style="width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-secondary); color: var(--text-normal); font-size: 13px;" />
            </div>
        </div>
        <div style="padding: 16px 24px; border-top: 1px solid var(--background-modifier-border); display: flex; justify-content: flex-end; gap: 10px; background: var(--background-secondary);">
            <button id="modal-cancel-btn" style="padding: 8px 16px; font-size: 12.5px; font-weight: 600; border-radius: 6px; border: 1px solid var(--background-modifier-border); background: var(--background-primary); color: var(--text-normal); cursor: pointer;">İptal</button>
            <button id="modal-save-btn" style="padding: 8px 18px; font-size: 12.5px; font-weight: 600; border-radius: 6px; border: none; background: var(--interactive-accent); color: var(--text-on-accent); cursor: pointer;">💾 Kaydet ve Notu Aç</button>
        </div>
    `;

    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    // Focus Title
    setTimeout(() => {
        const titleInput = document.getElementById("nb-title");
        if (titleInput) titleInput.focus();
    }, 50);

    // Close handlers
    const closeModal = () => overlay.remove();
    document.getElementById("modal-close-btn").onclick = closeModal;
    document.getElementById("modal-cancel-btn").onclick = closeModal;
    overlay.onclick = (e) => { if (e.target === overlay) closeModal(); };

    // Save handler
    document.getElementById("modal-save-btn").onclick = async () => {
        const title = (document.getElementById("nb-title").value || "").trim();
        if (!title) {
            alert("Lütfen eser adını giriniz.");
            return;
        }

        const tur = document.getElementById("nb-tur").value || "Kitap";
        const yazar = (document.getElementById("nb-yazar").value || "").trim();
        const kategori = (document.getElementById("nb-kategori").value || "").trim();
        const puanNum = parseInt(document.getElementById("nb-puan").value) || 5;
        const puanStars = "⭐️".repeat(puanNum);
        const durum = document.getElementById("nb-durum").value || "Bitti";
        const ay = document.getElementById("nb-ay").value || currentMonth;
        const yil = document.getElementById("nb-yil").value || currentYear.toString();
        const kapak = (document.getElementById("nb-kapak").value || "").trim();

        const cleanTitle = title.replace(/[\\/:*?"<>|]/g, "").trim();
        const filePath = `Kitaplar/${cleanTitle}.md`;

        // Check if exists
        const existing = app.vault.getAbstractFileByPath(filePath);
        if (existing) {
            alert(`"${cleanTitle}" adında bir not zaten mevcut!`);
            return;
        }

        const turTag = tur.toLowerCase();
        const turCatTag = (kategori || tur).toLowerCase().replace(/\s+/g, "-");
        const durumTag = durum.toLowerCase().replace(/\s+/g, "-");

        const noteContent = `---
Tür: "${tur}"
Type: "${tur}"
ODAK:
  - "[[${kategori || tur}]]"
MEKANİZMA: []
DİZİN: []
ETİKET: []
Yazar: "${yazar}"
Puan: "${puanStars}"
Puan_Sayi: ${puanNum}
Durum: "${durum}"
Kategori: "${kategori}"
Ay: "${ay}"
Yıl: "${yil}"
Kapak: "${kapak}"
tags:
  - type/${turTag}
  - tur/${turCatTag}
  - durum/${durumTag}
---

# ${cleanTitle}

> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> \`\`\`dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> \`\`\`

## 📖 Notlar & Detaylar

*Henüz özel bir inceleme veya alıntı notu eklenmedi.*
`;

        try {
            await app.vault.create(filePath, noteContent);
            closeModal();
            if (window.Notice) new Notice(`✅ "${cleanTitle}" kütüphaneye eklendi!`);
            app.workspace.openLinkText(filePath, "");
        } catch (err) {
            alert("Dosya oluşturulurken hata oluştu: " + err.message);
        }
    };
}

newBookBtn.onclick = openNewBookModal;

rightControlsDiv.appendChild(searchInput);
rightControlsDiv.appendChild(newBookBtn);

controlsBar.appendChild(tabsDiv);
controlsBar.appendChild(rightControlsDiv);
rootWrapper.appendChild(controlsBar);

// Cards Grid
const gridDiv = document.createElement("div");
gridDiv.className = "notion-cards-grid";
gridDiv.style.cssText = "display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px;";

function renderGrid() {
    gridDiv.innerHTML = "";
    const q = searchQuery.toLowerCase().trim();

    const filtered = pages.filter(p => {
        const itemType = (p.Tür || p.Type || "").toLowerCase();
        if (selectedTypeFilter !== "all" && itemType !== selectedTypeFilter) {
            return false;
        }
        if (!q) return true;
        const name = (p.file.name || "").toLowerCase();
        const author = (p.Yazar || "").toLowerCase();
        const cat = (p.Kategori || "").toLowerCase();
        const year = (p.Yıl || "").toString();
        const month = (p.Ay || "").toLowerCase();
        return name.includes(q) || author.includes(q) || cat.includes(q) || year.includes(q) || month.includes(q);
    });

    if (filtered.length === 0) {
        gridDiv.innerHTML = `<div style="grid-column: 1/-1; padding: 40px; text-align: center; color: var(--text-muted); font-size: 14px;">Bu filtrede gösterilecek kayıt bulunamadı.</div>`;
        return;
    }

    filtered.forEach(p => {
        const card = document.createElement("div");
        card.className = "notion-card";
        card.style.cssText = "display: flex; flex-direction: column; background: var(--background-secondary); border: 1px solid var(--background-modifier-border); border-radius: 12px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.04); transition: transform 0.15s ease, box-shadow 0.15s ease; cursor: pointer; height: 100%;";

        card.onmouseenter = () => {
            card.style.transform = "translateY(-3px)";
            card.style.boxShadow = "0 8px 18px rgba(0,0,0,0.12)";
        };
        card.onmouseleave = () => {
            card.style.transform = "translateY(0)";
            card.style.boxShadow = "0 2px 6px rgba(0,0,0,0.04)";
        };
        card.onclick = (e) => {
            app.workspace.openLinkText(p.file.path, "", e.metaKey || e.ctrlKey);
        };

        // Cover Section
        const coverSrc = getCoverSrc(p);
        const coverBox = document.createElement("div");
        coverBox.style.cssText = "width: 100%; height: 180px; background: rgba(0,0,0,0.03); display: flex; align-items: center; justify-content: center; overflow: hidden; border-bottom: 1px solid var(--background-modifier-border); position: relative;";

        if (coverSrc) {
            const img = document.createElement("img");
            img.src = coverSrc;
            img.style.cssText = "width: 100%; height: 100%; object-fit: contain; background: rgba(0,0,0,0.03);";
            coverBox.appendChild(img);
        } else {
            // Elegant Notion-like Empty Cover / Title Preview
            const icon = getTypeIcon(p.Tür || p.Type);
            const emptyCover = document.createElement("div");
            emptyCover.style.cssText = "padding: 16px; font-size: 11.5px; color: var(--text-muted); line-height: 1.45; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; width: 100%; background: linear-gradient(135deg, rgba(0,0,0,0.02) 0%, rgba(0,0,0,0.06) 100%);";
            emptyCover.innerHTML = `<span style="font-size: 26px; margin-bottom: 6px;">${icon}</span><span style="font-weight: 500; color: var(--text-faint); font-size: 11px;">${p.Kategori || p.Tür || "Kayıt"}</span>`;
            coverBox.appendChild(emptyCover);
        }
        card.appendChild(coverBox);

        // Body Content
        const bodyBox = document.createElement("div");
        bodyBox.style.cssText = "padding: 12px 14px; display: flex; flex-direction: column; gap: 8px; flex-grow: 1;";

        // Title
        const titleEl = document.createElement("div");
        titleEl.style.cssText = "font-weight: 700; font-size: 13.5px; line-height: 1.35; color: var(--text-normal); min-height: 36px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;";
        titleEl.textContent = p.file.name;
        bodyBox.appendChild(titleEl);

        // Badges Container
        const badgesContainer = document.createElement("div");
        badgesContainer.style.cssText = "display: flex; flex-wrap: wrap; gap: 4px; align-items: center;";

        // Type Badge (if not Kitap or to make explicit)
        const itemType = p.Tür || p.Type;
        if (itemType && itemType !== "Kitap") {
            const typeBadge = document.createElement("span");
            typeBadge.style.cssText = `${getTypeStyle(itemType)} font-size: 10.5px; font-weight: 600; padding: 2px 6px; border-radius: 4px;`;
            typeBadge.textContent = itemType;
            badgesContainer.appendChild(typeBadge);
        }

        // Durum Badge
        if (p.Durum) {
            const durumBadge = document.createElement("span");
            durumBadge.style.cssText = "background: rgba(82, 156, 202, 0.2); color: #2b78a8; font-size: 11px; font-weight: 600; padding: 2px 7px; border-radius: 4px;";
            durumBadge.textContent = p.Durum;
            badgesContainer.appendChild(durumBadge);
        }

        // Yazar Badge
        if (p.Yazar) {
            const yazarBadge = document.createElement("span");
            yazarBadge.style.cssText = "background: rgba(147, 114, 224, 0.15); color: #7852c7; font-size: 11px; font-weight: 500; padding: 2px 7px; border-radius: 4px; max-width: 100%; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;";
            yazarBadge.textContent = p.Yazar;
            yazarBadge.title = p.Yazar;
            badgesContainer.appendChild(yazarBadge);
        }

        // Kategori / Tür Badge
        if (p.Kategori) {
            const catBadge = document.createElement("span");
            catBadge.style.cssText = `${getCategoryStyle(p.Kategori)} font-size: 11px; font-weight: 500; padding: 2px 7px; border-radius: 4px;`;
            catBadge.textContent = p.Kategori;
            badgesContainer.appendChild(catBadge);
        }

        // Rating Stars
        if (p.Puan) {
            const ratingEl = document.createElement("div");
            ratingEl.style.cssText = "font-size: 11px; letter-spacing: 0.5px; width: 100%; margin: 1px 0;";
            ratingEl.textContent = p.Puan;
            badgesContainer.appendChild(ratingEl);
        }

        // Ay Badge
        if (p.Ay) {
            const ayBadge = document.createElement("span");
            ayBadge.style.cssText = "background: rgba(224, 114, 180, 0.18); color: #b83281; font-size: 11px; padding: 2px 7px; border-radius: 4px;";
            ayBadge.textContent = p.Ay;
            badgesContainer.appendChild(ayBadge);
        }

        // Yıl Badge
        if (p.Yıl) {
            const yilBadge = document.createElement("span");
            yilBadge.style.cssText = "background: rgba(235, 87, 87, 0.18); color: #c43838; font-size: 11px; padding: 2px 7px; border-radius: 4px;";
            yilBadge.textContent = p.Yıl;
            badgesContainer.appendChild(yilBadge);
        }

        bodyBox.appendChild(badgesContainer);
        card.appendChild(bodyBox);
        gridDiv.appendChild(card);
    });
}

searchInput.addEventListener("input", (e) => {
    searchQuery = e.target.value;
    renderGrid();
});

renderGrid();
rootWrapper.appendChild(gridDiv);
container.appendChild(rootWrapper);
