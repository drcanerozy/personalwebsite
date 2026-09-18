const {
  Plugin,
  Modal,
  Notice,
  PluginSettingTab,
  Setting,
  MarkdownView,
  normalizePath,
} = require("obsidian");

const DEFAULT_SETTINGS = {
  notebooks: [], // { id, name, folder, mode, paperShape, paperColor, fontFamily, autoTask, manualOrder: [] }
  lastNotebookId: null,
  taskRegistry: {}, // dtid -> { originPath, notebookId, createdAt, done, completedAt }
  dashboardPath: "Defter Dashboard.md",
  dashboardFilter: "both", // "both" | "pending" | "done"
};

const DTID_RE = /%%dtid:([a-z0-9]+)%%/;
const CHECKBOX_RE = /^(\s*-\s\[)([ xX])(\]\s.*)$/;

const FONT_OPTIONS = {
  default: null,
  caveat: "'Caveat', cursive",
  kalam: "'Kalam', cursive",
  patrick: "'Patrick Hand', cursive",
  shadows: "'Shadows Into Light', cursive",
  special_elite: "'Special Elite', monospace",
  georgia: "Georgia, serif",
  jetbrains: "'JetBrains Mono', monospace",
};

const FONTS_LINK_ID = "defter-fonts-link";
const FONTS_HREF =
  "https://fonts.googleapis.com/css2?family=Caveat&family=Kalam&family=Patrick+Hand&family=Shadows+Into+Light&family=Special+Elite&family=JetBrains+Mono&display=swap";

function genId(len) {
  const chars = "abcdefghijklmnopqrstuvwxyz0123456789";
  let s = "";
  for (let i = 0; i < len; i++) s += chars[Math.floor(Math.random() * chars.length)];
  return s;
}

module.exports = class DefterPlugin extends Plugin {
  async onload() {
    await this.loadSettings();
    this.injectFonts();

    this.statusBarItem = this.addStatusBarItem();
    this.statusBarItem.addClass("defter-status-bar");
    this.updateStatusBar();

    this.addSettingTab(new DefterSettingTab(this.app, this));

    this.addCommand({
      id: "defter-next-page",
      name: "Sonraki sayfa (not)",
      callback: () => this.navigate(1),
    });

    this.addCommand({
      id: "defter-prev-page",
      name: "Önceki sayfa (not)",
      callback: () => this.navigate(-1),
    });

    this.addCommand({
      id: "defter-quick-capture",
      name: "Hızlı not ekle",
      callback: () => new QuickCaptureModal(this.app, this).open(),
    });

    this.addCommand({
      id: "defter-create-dashboard",
      name: "Dashboard notu oluştur / güncelle",
      callback: () => this.createDashboardNote(),
    });

    this.registerEvent(
      this.app.workspace.on("file-open", () => {
        this.updateStatusBar();
        this.updatePaperClass();
      })
    );
    this.registerEvent(
      this.app.workspace.on("active-leaf-change", () => {
        this.updateStatusBar();
        this.updatePaperClass();
      })
    );
    this.registerEvent(this.app.workspace.on("css-change", () => this.updatePaperClass()));
    this.registerEvent(this.app.workspace.on("layout-change", () => this.updatePaperClass()));
    this.registerInterval(window.setInterval(() => this.updatePaperClass(), 1500));

    this.lastStamp = new Map();
    this.registerEvent(this.app.vault.on("create", (file) => this.handleFileCreate(file)));
    this.registerEvent(this.app.vault.on("modify", (file) => this.handleFileModify(file)));

    this.app.workspace.onLayoutReady(() => {
      this.updatePaperClass();
      this.ensureAllNotebookFolders();
      window.setTimeout(() => this.backfillExistingNotes(), 1500);
    });
  }

  async ensureFolder(folderPath) {
    const path = normalizePath(folderPath || "");
    if (!path) return;
    const existing = this.app.vault.getAbstractFileByPath(path);
    if (!existing) {
      try {
        await this.app.vault.createFolder(path);
      } catch (e) {
        // zaten var olabilir ya da geçersiz yol, yoksay
      }
    }
  }

  toTaskLines(text) {
    return text
      .split("\n")
      .map((line) => {
        if (line.trim() === "") return line;
        if (/^\s*-\s\[[ xX]\]/.test(line)) return line; // zaten checkbox
        if (/^\s*-\s/.test(line)) return line.replace(/^(\s*)-\s/, "$1- [ ] "); // liste maddesi -> checkbox
        if (/^\s*#{1,6}\s/.test(line)) return line; // başlık satırlarına dokunma
        return line.replace(/^(\s*)/, "$1- [ ] ");
      })
      .join("\n");
  }

  async ensureAllNotebookFolders() {
    for (const nb of this.settings.notebooks) {
      if (nb.folder) await this.ensureFolder(nb.folder);
    }
  }

  onunload() {
    this.clearPaperClass();
    const link = document.getElementById(FONTS_LINK_ID);
    if (link) link.remove();
  }

  injectFonts() {
    if (document.getElementById(FONTS_LINK_ID)) return;
    const link = document.createElement("link");
    link.id = FONTS_LINK_ID;
    link.rel = "stylesheet";
    link.href = FONTS_HREF;
    document.head.appendChild(link);
  }

  // ---- Ayarlar ----

  async loadSettings() {
    const raw = await this.loadData();
    if (raw && raw.folder !== undefined && !raw.notebooks) {
      // eski (tek defter) formattan göç
      const nb = {
        id: genId(6),
        name: "Defter",
        folder: raw.folder || "",
        mode: raw.mode || "created",
        paperShape: raw.paperShape || "none",
        paperColor: raw.paperColor || "#ffffff",
        fontFamily: "default",
        autoTask: false,
        manualOrder: raw.manualOrder || [],
      };
      this.settings = Object.assign({}, DEFAULT_SETTINGS, { notebooks: [nb] });
      await this.saveSettings();
    } else {
      this.settings = Object.assign({}, DEFAULT_SETTINGS, raw || {});
      if (!this.settings.notebooks) this.settings.notebooks = [];
      if (!this.settings.taskRegistry) this.settings.taskRegistry = {};
    }
  }

  async saveSettings() {
    await this.saveData(this.settings);
  }

  // ---- Defter / dosya yardımcıları ----

  getNotebookForFile(file) {
    if (!file) return null;
    for (const nb of this.settings.notebooks) {
      const folder = normalizePath(nb.folder || "");
      if (!folder) continue;
      if (file.path === folder || file.path.startsWith(folder + "/")) return nb;
    }
    return null;
  }

  getTrackedFiles(nb) {
    const folder = normalizePath(nb.folder || "");
    if (!folder) return [];
    return this.app.vault
      .getMarkdownFiles()
      .filter((f) => f.path === folder || f.path.startsWith(folder + "/"));
  }

  getDate(file, field, fallback) {
    const cache = this.app.metadataCache.getFileCache(file);
    const raw = cache && cache.frontmatter && cache.frontmatter[field];
    if (raw) {
      const t = Date.parse(raw);
      if (!isNaN(t)) return t;
    }
    return fallback;
  }

  sortFiles(nb, files) {
    const list = files.slice();

    if (nb.mode === "created") {
      list.sort(
        (a, b) =>
          this.getDate(a, "defter-created", a.stat.ctime) -
          this.getDate(b, "defter-created", b.stat.ctime)
      );
      return list;
    }

    if (nb.mode === "modified") {
      list.sort(
        (a, b) =>
          this.getDate(a, "defter-modified", a.stat.mtime) -
          this.getDate(b, "defter-modified", b.stat.mtime)
      );
      return list;
    }

    // manual
    if (!nb.manualOrder) nb.manualOrder = [];
    const order = nb.manualOrder.filter((p) => list.some((f) => f.path === p));
    const known = new Set(order);
    const rest = list
      .filter((f) => !known.has(f.path))
      .sort(
        (a, b) =>
          this.getDate(a, "defter-created", a.stat.ctime) -
          this.getDate(b, "defter-created", b.stat.ctime)
      );

    const orderedFiles = order.map((p) => list.find((f) => f.path === p)).filter(Boolean);
    const merged = orderedFiles.concat(rest);

    const newOrder = merged.map((f) => f.path);
    if (JSON.stringify(newOrder) !== JSON.stringify(nb.manualOrder)) {
      nb.manualOrder = newOrder;
      this.saveSettings();
    }

    return merged;
  }

  // ---- Navigasyon ----

  async navigate(direction) {
    const active = this.app.workspace.getActiveFile();
    const nb = this.getNotebookForFile(active);
    if (!nb) {
      new Notice("Aktif not tanımlı bir deftere ait değil.");
      return;
    }

    const files = this.getTrackedFiles(nb);
    if (files.length === 0) {
      new Notice(`"${nb.name}" defterinde not bulunamadı.`);
      return;
    }

    const sorted = this.sortFiles(nb, files);
    const idx = sorted.findIndex((f) => f.path === active.path);

    let newIndex;
    if (idx === -1) {
      newIndex = direction > 0 ? 0 : sorted.length - 1;
    } else {
      newIndex = idx + direction;
    }

    if (newIndex < 0) {
      new Notice("Defterin ilk sayfasındasın.");
      return;
    }
    if (newIndex >= sorted.length) {
      new Notice("Defterin son sayfasındasın.");
      return;
    }

    await this.app.workspace.getLeaf(false).openFile(sorted[newIndex]);
  }

  // ---- Status bar ----

  updateStatusBar() {
    const active = this.app.workspace.getActiveFile();
    const nb = this.getNotebookForFile(active);
    if (!nb) {
      this.statusBarItem.setText("Defter: -");
      return;
    }
    const files = this.getTrackedFiles(nb);
    const sorted = this.sortFiles(nb, files);
    const idx = sorted.findIndex((f) => f.path === active.path);
    if (idx === -1) {
      this.statusBarItem.setText(`${nb.name}: ${sorted.length} sayfa`);
    } else {
      this.statusBarItem.setText(`${nb.name}: ${idx + 1} / ${sorted.length}`);
    }
  }

  // ---- Kağıt teması ----

  clearPaperClass() {
    document.querySelectorAll(".defter-paper-active").forEach((el) => {
      el.removeClass("defter-paper-active");
      el.removeClass("defter-shape-none");
      el.removeClass("defter-shape-lines");
      el.removeClass("defter-shape-grid");
      el.removeClass("defter-shape-dots");
      el.style.removeProperty("--defter-paper-color");
      el.style.removeProperty("--defter-paper-font");
    });
  }

  updatePaperClass() {
    const view = this.app.workspace.getActiveViewOfType(MarkdownView);
    if (!view) {
      this.clearPaperClass();
      return;
    }

    const nb = this.getNotebookForFile(view.file);
    if (!nb) {
      this.clearPaperClass();
      return;
    }

    const el = view.contentEl.querySelector(".cm-editor") || view.contentEl;
    const fontFamily = FONT_OPTIONS[nb.fontFamily] || null;

    const alreadyCorrect =
      el.hasClass("defter-paper-active") &&
      el.hasClass(`defter-shape-${nb.paperShape}`) &&
      el.style.getPropertyValue("--defter-paper-color").trim() === nb.paperColor &&
      el.style.getPropertyValue("--defter-paper-font").trim() === (fontFamily || "");
    if (alreadyCorrect) return;

    this.clearPaperClass();
    el.addClass("defter-paper-active");
    el.addClass(`defter-shape-${nb.paperShape}`);
    el.style.setProperty("--defter-paper-color", nb.paperColor);
    if (fontFamily) {
      el.style.setProperty("--defter-paper-font", fontFamily);
    }
  }

  // ---- Tarih damgalama (defter-created / defter-modified) ----

  async handleFileCreate(file) {
    if (!file || file.extension !== "md") return;
    const nb = this.getNotebookForFile(file);
    if (!nb) return;
    const now = new Date().toISOString();
    this.lastStamp.set(file.path, Date.now());
    try {
      await this.app.fileManager.processFrontMatter(file, (fm) => {
        if (!fm["defter-created"]) fm["defter-created"] = now;
        if (!fm["defter-modified"]) fm["defter-modified"] = now;
      });
    } catch (e) {
      /* yoksay */
    }
  }

  async handleFileModify(file) {
    if (!file || file.extension !== "md") return;
    const nb = this.getNotebookForFile(file);
    if (!nb) return;

    const last = this.lastStamp.get(file.path) || 0;
    const now = Date.now();
    if (now - last >= 3000) {
      this.lastStamp.set(file.path, now);
      try {
        await this.app.fileManager.processFrontMatter(file, (fm) => {
          fm["defter-modified"] = new Date(now).toISOString();
        });
      } catch (e) {
        /* yoksay */
      }
    }

    await this.checkForCompletedTasks(file);
  }

  async backfillExistingNotes() {
    for (const nb of this.settings.notebooks) {
      const files = this.getTrackedFiles(nb);
      for (const file of files) {
        const cache = this.app.metadataCache.getFileCache(file);
        const fm = cache && cache.frontmatter;
        if (fm && fm["defter-created"]) continue;
        this.lastStamp.set(file.path, Date.now());
        try {
          await this.app.fileManager.processFrontMatter(file, (frontmatter) => {
            if (!frontmatter["defter-created"]) {
              frontmatter["defter-created"] = new Date(file.stat.ctime).toISOString();
            }
            if (!frontmatter["defter-modified"]) {
              frontmatter["defter-modified"] = new Date(file.stat.mtime).toISOString();
            }
          });
        } catch (e) {
          /* yoksay, sonraki başlatmada tekrar dener */
        }
      }
    }
    this.updateStatusBar();
  }

  // ---- Görev taşıma (carry-over) ve tamamlanma takibi ----

  extractDtid(line) {
    const m = line.match(DTID_RE);
    return m ? m[1] : null;
  }

  // Bir önceki nottaki bitmemiş görevleri bulur, kimliksizse kimlik verir
  // (kaynak nota geri yazar), yeni nota kopyalanacak metni döner.
  async buildCarryOverSection(nb) {
    const files = this.getTrackedFiles(nb);
    if (files.length === 0) return "";
    const sorted = this.sortFiles(nb, files);
    const prev = sorted[sorted.length - 1];
    if (!prev) return "";

    const content = await this.app.vault.read(prev);
    const lines = content.split("\n");
    const carried = [];
    let changed = false;

    for (let i = 0; i < lines.length; i++) {
      const m = lines[i].match(CHECKBOX_RE);
      if (!m) continue;
      if (m[2].toLowerCase() === "x") continue; // tamamlanmış, taşınmaz

      let line = lines[i];
      let dtid = this.extractDtid(line);
      if (!dtid) {
        dtid = genId(10);
        line = `${line} %%dtid:${dtid}%%`;
        lines[i] = line;
        changed = true;
        this.settings.taskRegistry[dtid] = {
          originPath: prev.path,
          notebookId: nb.id,
          createdAt: Date.now(),
          done: false,
        };
      }
      carried.push(line);
    }

    if (changed) {
      this.lastStamp.set(prev.path, Date.now());
      await this.app.vault.modify(prev, lines.join("\n"));
      await this.saveSettings();
    }

    if (carried.length === 0) return "";
    return "## Devam eden işler\n" + carried.join("\n") + "\n\n";
  }

  // Değiştirilen dosyada, daha önce kaydı olan ve şimdi işaretlenmiş
  // görev var mı diye bakar; varsa kaynak nota "tamamlandı" notu düşer.
  async checkForCompletedTasks(file) {
    let content;
    try {
      content = await this.app.vault.read(file);
    } catch (e) {
      return;
    }
    const lines = content.split("\n");
    let anyDone = false;

    for (const line of lines) {
      const dtid = this.extractDtid(line);
      if (!dtid) continue;
      const reg = this.settings.taskRegistry[dtid];
      if (!reg || reg.done) continue;
      const m = line.match(CHECKBOX_RE);
      if (!m) continue;
      if (m[2].toLowerCase() === "x") {
        reg.done = true;
        reg.completedAt = Date.now();
        anyDone = true;
        await this.annotateOrigin(dtid, reg, file.path);
      }
    }

    if (anyDone) await this.saveSettings();
  }

  async annotateOrigin(dtid, reg, completedInPath) {
    if (reg.originPath === completedInPath) return; // zaten kendi kutucuğu, ek not gereksiz
    const originFile = this.app.vault.getAbstractFileByPath(reg.originPath);
    if (!originFile) return;

    let content;
    try {
      content = await this.app.vault.read(originFile);
    } catch (e) {
      return;
    }
    const lines = content.split("\n");
    const dateStr = new Date(reg.completedAt).toLocaleDateString("tr-TR", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    let changed = false;

    for (let i = 0; i < lines.length; i++) {
      if (this.extractDtid(lines[i]) === dtid && !lines[i].includes("tamamlandı)")) {
        lines[i] = `${lines[i]}  *(✅ ${dateStr} tarihinde tamamlandı)*`;
        changed = true;
      }
    }

    if (changed) {
      this.lastStamp.set(originFile.path, Date.now());
      await this.app.vault.modify(originFile, lines.join("\n"));
    }
  }

  // ---- Dashboard ----

  async createDashboardNote() {
    if (this.settings.notebooks.length === 0) {
      new Notice("Önce ayarlardan en az bir defter tanımla.");
      return;
    }
    const folders = this.settings.notebooks
      .map((nb) => normalizePath(nb.folder || ""))
      .filter(Boolean);
    const names = {};
    this.settings.notebooks.forEach((nb) => {
      names[normalizePath(nb.folder || "")] = nb.name;
    });

    const script =
      `const folders = ${JSON.stringify(folders)};\n` +
      `const names = ${JSON.stringify(names)};\n` +
      `let filter = ${JSON.stringify(this.settings.dashboardFilter || "both")};\n` +
      "\n" +
      'const pages = dv.pages().where(p => folders.some(f => p.file.path === f || p.file.folder === f || p.file.folder.startsWith(f + "/")));\n' +
      "\n" +
      "function fmtDate(ts) {\n" +
      '  if (!ts) return "";\n' +
      "  const d = new Date(ts);\n" +
      '  const dd = String(d.getDate()).padStart(2, "0");\n' +
      '  const mm = String(d.getMonth() + 1).padStart(2, "0");\n' +
      "  return `${dd}.${mm}.${d.getFullYear()}`;\n" +
      "}\n" +
      "\n" +
      "function pageDate(p) {\n" +
      '  if (p["defter-created"]) {\n' +
      '    const t = Date.parse(p["defter-created"]);\n' +
      "    if (!isNaN(t)) return t;\n" +
      "  }\n" +
      "  return p.file.ctime.ts;\n" +
      "}\n" +
      "\n" +
      "function pagesUnder(folder) {\n" +
      '  return pages.where(p => p.file.folder === folder || p.file.folder.startsWith(folder + "/"));\n' +
      "}\n" +
      "\n" +
      "function projectOf(p, nbFolder) {\n" +
      "  const folder = p.file.folder;\n" +
      "  if (folder === nbFolder) return null;\n" +
      '  const rest = folder.slice(nbFolder.length + 1);\n' +
      '  return rest.split("/")[0];\n' +
      "}\n" +
      "\n" +
      "function filterTasks(tasks) {\n" +
      '  if (filter === "pending") return tasks.where(t => !t.completed);\n' +
      '  if (filter === "done") return tasks.where(t => t.completed);\n' +
      "  return tasks;\n" +
      "}\n" +
      "\n" +
      "function renderNoteBlock(p, container) {\n" +
      "  const tasks = filterTasks(p.file.tasks);\n" +
      "  if (tasks.length === 0) return;\n" +
      '  container.createEl("div", { text: fmtDate(pageDate(p)) + ":", attr: { style: "font-weight:600; margin-top:8px; opacity:0.8;" } });\n' +
      "  dv.taskList(tasks, false, container);\n" +
      "}\n" +
      "\n" +
      'let mode = "card";\n' +
      "const root = dv.container;\n" +
      "\n" +
      "function render() {\n" +
      '  root.innerHTML = "";\n' +
      "\n" +
      '  const toolbar = root.createEl("div", { attr: { style: "margin-bottom: 12px; display:flex; gap:6px; flex-wrap:wrap;" } });\n' +
      '  const listBtn = toolbar.createEl("button", { text: "Liste görünümü" });\n' +
      '  const cardBtn = toolbar.createEl("button", { text: "Kart görünümü" });\n' +
      '  const pendingBtn = toolbar.createEl("button", { text: "Sadece bekleyenler" });\n' +
      '  const doneBtn = toolbar.createEl("button", { text: "Sadece tamamlananlar" });\n' +
      '  const bothBtn = toolbar.createEl("button", { text: "İkisi de" });\n' +
      '  listBtn.onclick = () => { mode = "list"; render(); };\n' +
      '  cardBtn.onclick = () => { mode = "card"; render(); };\n' +
      '  pendingBtn.onclick = () => { filter = "pending"; render(); };\n' +
      '  doneBtn.onclick = () => { filter = "done"; render(); };\n' +
      '  bothBtn.onclick = () => { filter = "both"; render(); };\n' +
      "\n" +
      '  if (mode === "list") {\n' +
      "    const sorted = pages.array().sort((a, b) => pageDate(b) - pageDate(a));\n" +
      "    for (const p of sorted) renderNoteBlock(p, root);\n" +
      "    return;\n" +
      "  }\n" +
      "\n" +
      '  const grid = root.createEl("div", { attr: { style: "display:flex; flex-wrap:wrap; gap:12px; align-items:flex-start;" } });\n' +
      "\n" +
      "  for (const folder of folders) {\n" +
      "    const notebookPages = pagesUnder(folder);\n" +
      "    const groups = {};\n" +
      "    notebookPages.forEach((p) => {\n" +
      '      const proj = projectOf(p, folder) || "Genel";\n' +
      "      if (!groups[proj]) groups[proj] = [];\n" +
      "      groups[proj].push(p);\n" +
      "    });\n" +
      "\n" +
      "    for (const projName of Object.keys(groups)) {\n" +
      "      const notesSorted = groups[projName].sort((a, b) => pageDate(b) - pageDate(a));\n" +
      '      const card = grid.createEl("div", { attr: { style:\n' +
      '        "flex: 1 1 260px; min-width:220px; border:1px solid var(--background-modifier-border); border-radius:8px; padding:10px; background:var(--background-secondary);" } });\n' +
      '      card.createEl("h4", { text: `${names[folder] || folder} — ${projName}` });\n' +
      '      const body = card.createEl("div");\n' +
      "      for (const p of notesSorted) renderNoteBlock(p, body);\n" +
      "    }\n" +
      "  }\n" +
      "}\n" +
      "\n" +
      "render();\n";

    const content =
      `# Defter Dashboard\n\n` +
      `> Tanımlı defterlerdeki görevleri listeler. **Dataview** eklentisinin kurulu ve etkin olması gerekir.\n` +
      `> Checkbox'lara buradan tıklamak, ilgili notu da günceller — liste ve kart görünümü aynı canlı veriyi paylaşır.\n\n` +
      "```dataviewjs\n" +
      script +
      "```\n";

    const path = normalizePath(this.settings.dashboardPath || "Defter Dashboard.md");
    const parentFolder = path.includes("/") ? path.slice(0, path.lastIndexOf("/")) : "";
    if (parentFolder) await this.ensureFolder(parentFolder);
    let file = this.app.vault.getAbstractFileByPath(path);
    if (file) {
      await this.app.vault.modify(file, content);
    } else {
      file = await this.app.vault.create(path, content);
    }
    await this.app.workspace.getLeaf(false).openFile(file);
    new Notice("Dashboard notu güncellendi.");
  }
};

// ---- Hızlı Not Modal'ı ----

class QuickCaptureModal extends Modal {
  constructor(app, plugin) {
    super(app);
    this.plugin = plugin;
    this.selectedNb = null;
  }

  onOpen() {
    const { contentEl } = this;
    contentEl.empty();

    const notebooks = this.plugin.settings.notebooks;
    if (notebooks.length === 0) {
      new Notice("Önce ayarlardan en az bir defter tanımla.");
      this.close();
      return;
    }

    this.selectedNb =
      notebooks.find((n) => n.id === this.plugin.settings.lastNotebookId) || notebooks[0];

    contentEl.createEl("h3", { text: "Hızlı not" });

    if (notebooks.length > 1) {
      const selectWrap = contentEl.createEl("div", { attr: { style: "margin-bottom: 8px;" } });
      selectWrap.createEl("label", { text: "Defter: ", attr: { style: "margin-right: 6px;" } });
      const select = selectWrap.createEl("select");
      notebooks.forEach((nb) => {
        const opt = select.createEl("option", { text: nb.name, value: nb.id });
        if (nb.id === this.selectedNb.id) opt.selected = true;
      });
      select.addEventListener("change", (e) => {
        this.selectedNb = notebooks.find((n) => n.id === e.target.value) || notebooks[0];
      });
    }

    const titleInput = contentEl.createEl("input", {
      attr: {
        type: "text",
        placeholder: "Başlık (boş bırakırsan tarih-saat kullanılır)",
        style: "width: 100%; margin-bottom: 8px;",
      },
    });

    const textarea = contentEl.createEl("textarea", {
      attr: {
        rows: "8",
        placeholder: "Aklından ne geçiyorsa yaz...",
        style: "width: 100%; resize: vertical;",
      },
    });
    textarea.focus();

    contentEl.createEl("div", {
      text: "Kaydet: Ctrl/Cmd + Enter — İptal: Esc",
      attr: { style: "opacity: 0.6; font-size: 12px; margin-top: 6px;" },
    });

    const onKeydown = (evt) => {
      if ((evt.ctrlKey || evt.metaKey) && evt.key === "Enter") {
        evt.preventDefault();
        this.submit(textarea.value, titleInput.value);
      }
      if (evt.key === "Escape") this.close();
    };
    textarea.addEventListener("keydown", onKeydown);
    titleInput.addEventListener("keydown", onKeydown);

    const buttonRow = contentEl.createEl("div", {
      attr: { style: "margin-top: 10px; text-align: right;" },
    });
    const saveBtn = buttonRow.createEl("button", { text: "Kaydet" });
    saveBtn.addEventListener("click", () => this.submit(textarea.value, titleInput.value));
  }

  sanitizeTitle(raw) {
    return raw
      .trim()
      .replace(/[\\/:*?"<>|#^[\]]/g, "")
      .slice(0, 100);
  }

  async submit(rawContent, rawTitle) {
    const content = (rawContent || "").trim();
    if (!content) {
      new Notice("Boş not kaydedilmedi.");
      this.close();
      return;
    }

    const nb = this.selectedNb;
    const folder = normalizePath(nb.folder || "");
    if (!folder) {
      new Notice("Bu defterin klasörü tanımlı değil, ayarlardan kontrol et.");
      return;
    }

    const existingFolder = this.app.vault.getAbstractFileByPath(folder);
    if (!existingFolder) {
      await this.app.vault.createFolder(folder);
    }

    const carryOver = await this.plugin.buildCarryOverSection(nb);
    const body = nb.autoTask ? this.plugin.toTaskLines(content) : content;

    const now = new Date();
    const stamp = now.toISOString().slice(0, 19).replace("T", " ").replace(/:/g, "-");
    const cleanTitle = this.sanitizeTitle(rawTitle || "");
    const baseName = cleanTitle || stamp;

    let filename = baseName;
    let counter = 2;
    while (this.app.vault.getAbstractFileByPath(normalizePath(`${folder}/${filename}.md`))) {
      filename = `${baseName} (${counter})`;
      counter++;
    }
    const path = normalizePath(`${folder}/${filename}.md`);

    const file = await this.app.vault.create(path, carryOver + body);

    if (nb.mode === "manual") {
      if (!nb.manualOrder) nb.manualOrder = [];
      nb.manualOrder.push(file.path);
    }
    this.plugin.settings.lastNotebookId = nb.id;
    await this.plugin.saveSettings();

    await this.app.workspace.getLeaf(false).openFile(file);
    this.close();
  }

  onClose() {
    this.contentEl.empty();
  }
}

// ---- Ayarlar sekmesi ----

class DefterSettingTab extends PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }

  display() {
    const { containerEl } = this;
    containerEl.empty();

    containerEl.createEl("h2", { text: "Defter — Ayarlar" });

    new Setting(containerEl)
      .setName("Yeni defter ekle")
      .setDesc("Ayrı bir klasörü izleyen yeni bir defter tanımla")
      .addButton((btn) =>
        btn.setButtonText("+ Defter").onClick(async () => {
          const nb = {
            id: genId(6),
            name: `Defter ${this.plugin.settings.notebooks.length + 1}`,
            folder: "",
            mode: "created",
            paperShape: "none",
            paperColor: "#ffffff",
            fontFamily: "default",
            autoTask: false,
            manualOrder: [],
          };
          this.plugin.settings.notebooks.push(nb);
          await this.plugin.saveSettings();
          this.display();
        })
      );

    for (const nb of this.plugin.settings.notebooks) {
      containerEl.createEl("h3", { text: nb.name || "(isimsiz defter)" });

      new Setting(containerEl).setName("İsim").addText((text) =>
        text.setValue(nb.name).onChange(async (value) => {
          nb.name = value;
          await this.plugin.saveSettings();
        })
      );

      new Setting(containerEl).setName("Klasör").addText((text) => {
        text
          .setPlaceholder("Defterler/Gunluk")
          .setValue(nb.folder)
          .onChange(async (value) => {
            nb.folder = value.trim();
            await this.plugin.saveSettings();
            this.plugin.updateStatusBar();
          });
        text.inputEl.addEventListener("blur", async () => {
          await this.plugin.ensureFolder(nb.folder);
        });
      })
      .addButton((btn) =>
        btn
          .setButtonText("Oluştur")
          .setTooltip("Bu klasör vault'ta yoksa oluştur")
          .onClick(async () => {
            if (!nb.folder) {
              new Notice("Önce klasör yolunu yaz.");
              return;
            }
            await this.plugin.ensureFolder(nb.folder);
            new Notice(`"${nb.folder}" klasörü hazır.`);
          })
      );

      new Setting(containerEl)
        .setName("Navigasyon modu")
        .addDropdown((drop) =>
          drop
            .addOption("created", "Sabit (oluşturulma tarihi)")
            .addOption("modified", "Canlı (düzenleme tarihi)")
            .addOption("manual", "Manuel sıra")
            .setValue(nb.mode)
            .onChange(async (value) => {
              nb.mode = value;
              await this.plugin.saveSettings();
            })
        );

      new Setting(containerEl)
        .setName("Kağıt şekli")
        .addDropdown((drop) =>
          drop
            .addOption("none", "Düz")
            .addOption("lines", "Çizgili")
            .addOption("grid", "Kareli")
            .addOption("dots", "Noktalı")
            .setValue(nb.paperShape)
            .onChange(async (value) => {
              nb.paperShape = value;
              await this.plugin.saveSettings();
              this.plugin.updatePaperClass();
            })
        );

      new Setting(containerEl).setName("Kağıt rengi").addColorPicker((picker) =>
        picker.setValue(nb.paperColor).onChange(async (value) => {
          nb.paperColor = value;
          await this.plugin.saveSettings();
          this.plugin.updatePaperClass();
        })
      );

      new Setting(containerEl)
        .setName("Yazı tipi")
        .setDesc("Sadece bu defterdeki notların editöründe uygulanır")
        .addDropdown((drop) =>
          drop
            .addOption("default", "Varsayılan (tema)")
            .addOption("caveat", "El yazısı — Caveat")
            .addOption("kalam", "El yazısı — Kalam")
            .addOption("patrick", "El yazısı — Patrick Hand")
            .addOption("shadows", "El yazısı — Shadows Into Light")
            .addOption("special_elite", "Daktilo — Special Elite")
            .addOption("georgia", "Serif — Georgia")
            .addOption("jetbrains", "Monospace — JetBrains Mono")
            .setValue(nb.fontFamily || "default")
            .onChange(async (value) => {
              nb.fontFamily = value;
              await this.plugin.saveSettings();
              this.plugin.updatePaperClass();
            })
        );

      new Setting(containerEl)
        .setName("Hızlı notta her satırı görev yap")
        .setDesc("Açıksa, hızlı not penceresinde yazdığın her satır otomatik olarak checkbox'a (görev) çevrilir")
        .addToggle((toggle) =>
          toggle.setValue(!!nb.autoTask).onChange(async (value) => {
            nb.autoTask = value;
            await this.plugin.saveSettings();
          })
        );

      new Setting(containerEl)
        .setName("Manuel sırayı sıfırla")
        .addButton((btn) =>
          btn.setButtonText("Sıfırla").onClick(async () => {
            nb.manualOrder = [];
            await this.plugin.saveSettings();
            new Notice("Manuel sıra sıfırlandı.");
          })
        );

      new Setting(containerEl)
        .setName("Bu defteri sil")
        .setDesc("Sadece takipten kaldırır, notları silmez")
        .addButton((btn) =>
          btn
            .setButtonText("Sil")
            .setWarning()
            .onClick(async () => {
              this.plugin.settings.notebooks = this.plugin.settings.notebooks.filter(
                (n) => n.id !== nb.id
              );
              await this.plugin.saveSettings();
              this.display();
            })
        );

      containerEl.createEl("hr");
    }

    new Setting(containerEl)
      .setName("Dashboard konumu")
      .setDesc("Dashboard notunun vault içindeki yolu, örn. Defterler/Dashboard.md")
      .addText((text) =>
        text
          .setValue(this.plugin.settings.dashboardPath || "Defter Dashboard.md")
          .onChange(async (value) => {
            this.plugin.settings.dashboardPath = value.trim() || "Defter Dashboard.md";
            await this.plugin.saveSettings();
          })
      );

    new Setting(containerEl)
      .setName("Varsayılan görev filtresi")
      .setDesc("Dashboard ilk açıldığında hangi görevler gösterilsin (notun üzerinde de değiştirilebilir)")
      .addDropdown((drop) =>
        drop
          .addOption("both", "İkisi de")
          .addOption("pending", "Sadece bekleyenler")
          .addOption("done", "Sadece tamamlananlar")
          .setValue(this.plugin.settings.dashboardFilter || "both")
          .onChange(async (value) => {
            this.plugin.settings.dashboardFilter = value;
            await this.plugin.saveSettings();
          })
      );

    new Setting(containerEl)
      .setName("Dashboard notu oluştur / güncelle")
      .setDesc("Tüm defterlerdeki bekleyen/tamamlanan görevleri listeleyen bir not oluşturur (Dataview gerektirir)")
      .addButton((btn) =>
        btn.setButtonText("Oluştur").onClick(() => this.plugin.createDashboardNote())
      );

    containerEl.createEl("p", {
      text: "İpucu: 'Sonraki sayfa', 'Önceki sayfa' ve 'Hızlı not ekle' komutlarına Ayarlar → Kısayol Tuşları'ndan kendi tuş kombinasyonunu atayabilirsin.",
      attr: { style: "opacity: 0.7; font-size: 12px;" },
    });
  }
}
