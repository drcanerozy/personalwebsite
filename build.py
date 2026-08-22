#!/usr/bin/env python3
"""
Academic Website Builder for Dr. Caner ÖZYILDIRIM
Compiles Obsidian Markdown content (with YAML frontmatter) into bilingual HTML websites (TR & EN).
Zero external dependencies (pure Python 3 standard library).
"""

import os
import re
import glob
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
CONTENT_DIR = BASE_DIR / "content"
TEMPLATES_DIR = BASE_DIR / "_templates"

def parse_frontmatter(content):
    """Simple, robust YAML frontmatter parser without external dependencies."""
    if not content.startswith("---"):
        return {}, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    
    frontmatter_text = parts[1].strip()
    body = parts[2].strip()
    
    data = {}
    current_key = None
    in_list = False
    
    for line in frontmatter_text.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        
        # List item
        if line.strip().startswith("- ") and current_key:
            val = line.strip()[2:].strip().strip('"\'')
            if current_key not in data or not isinstance(data[current_key], list):
                data[current_key] = []
            data[current_key].append(val)
            continue
        
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            
            # Remove inline comments
            if "#" in val and not (val.startswith('"') or val.startswith("'")):
                val = val.split("#", 1)[0].strip()
            
            val = val.strip('"\'')
            
            if val.lower() == "true":
                data[key] = True
            elif val.lower() == "false":
                data[key] = False
            elif val.isdigit():
                data[key] = int(val)
            elif val == "" or val == "[]":
                data[key] = [] if val == "[]" else ""
                current_key = key
            else:
                data[key] = val
                current_key = key
                
    return data, body

def read_md_file(file_path):
    if not os.path.exists(file_path):
        return {}, ""
    with open(file_path, "r", encoding="utf-8") as f:
        return parse_frontmatter(f.read())

def load_section_items(lang_dir, section_name):
    folder = lang_dir / section_name
    if not folder.exists():
        return []
    
    items = []
    for md_file in sorted(folder.glob("*.md")):
        data, body = read_md_file(md_file)
        if not data.get("draft", False):
            data["body"] = body
            data["_filename"] = md_file.name
            items.append(data)
            
    # Sort items if order or date exists
    items.sort(key=lambda x: (x.get("order", 999), str(x.get("date", "")), str(x.get("year", ""))), reverse=False)
    return items

def generate_html(lang="tr"):
    lang_dir = CONTENT_DIR / lang
    is_tr = (lang == "tr")
    
    # Load Profile Bio & Education
    bio_data, bio_body = read_md_file(lang_dir / "bio.md")
    edu_data, edu_body = read_md_file(lang_dir / "education.md")
    
    # Load Collections
    publications = load_section_items(lang_dir, "publications")
    projects = load_section_items(lang_dir, "projects")
    teaching = load_section_items(lang_dir, "teaching")
    presentations = load_section_items(lang_dir, "presentations")
    tools = load_section_items(lang_dir, "tools")
    articles = load_section_items(lang_dir, "articles")
    podcasts = load_section_items(lang_dir, "podcasts")
    
    # UI Texts
    ui = {
        "title": "Dr. Caner ÖZYILDIRIM | Beslenme ve Diyetetik Akademisyeni" if is_tr else "Dr. Caner ÖZYILDIRIM | Nutrition & Dietetics Academic",
        "role_subtitle": "Beslenme ve Diyetetik Akademisyeni" if is_tr else "Nutrition & Dietetics Academic",
        "institution": "Akdeniz Üniversitesi Sağlık Bilimleri Fakültesi" if is_tr else "Akdeniz University Faculty of Health Sciences",
        "department": "Beslenme ve Diyetetik Bölümü • Antalya, Türkiye" if is_tr else "Department of Nutrition and Dietetics • Antalya, Turkey",
        "nav_about": "Hakkımda" if is_tr else "About",
        "nav_education": "Eğitim" if is_tr else "Education",
        "nav_publications": "Yayınlar" if is_tr else "Publications",
        "nav_projects": "Projeler" if is_tr else "Projects",
        "nav_teaching": "Dersler" if is_tr else "Teaching",
        "nav_presentations": "Sunumlar" if is_tr else "Presentations",
        "nav_tools": "Araçlar" if is_tr else "Tools",
        "nav_articles": "Yazılar" if is_tr else "Articles",
        "nav_podcasts": "Podcastler" if is_tr else "Podcasts",
        "contact_btn": "İletişim" if is_tr else "Contact",
        "cv_btn": "Özgeçmiş (CV PDF)" if is_tr else "Curriculum Vitae (PDF)",
        "switch_lang_url": "en/" if is_tr else "../",
        "switch_lang_label": "EN" if is_tr else "TR",
        "current_lang_badge": "TR" if is_tr else "EN",
        "all_filter": "Tümü" if is_tr else "All",
        "sci_filter": "Uluslararası SCI/SCI-E" if is_tr else "International SCI/SCI-E",
        "national_filter": "Ulusal Hakemli" if is_tr else "National Peer-Reviewed",
        "book_filter": "Kitap Bölümleri" if is_tr else "Book Chapters",
        "conf_filter": "Konferans Bildirileri" if is_tr else "Conference Proceedings",
        "lay_summary_btn": "Halk İçin Özet" if is_tr else "Lay Summary",
        "bibtex_btn": "BibTeX Al" if is_tr else "Get BibTeX",
        "toggle_pubs_more": f"Tüm Yayınları Gör ({len(publications)} Eser)" if is_tr else f"View All Publications ({len(publications)} Works)",
        "toggle_pubs_less": "Daha Az Göster" if is_tr else "Show Less",
        "footer_rights": "© 2026 Bütün Hakları Saklıdır. Beslenme ve Diyetetik Akademisyeni • Akdeniz Üniversitesi" if is_tr else "© 2026 All Rights Reserved. Nutrition & Dietetics Academic • Akdeniz University",
        "live_slide_btn": "Sunumu Canlı İzle (HTML)" if is_tr else "View Live Slides (HTML)",
        "download_slide_btn": "Slaytları İndir (PDF)" if is_tr else "Download Slides (PDF)",
        "launch_tool_btn": "Aracı Başlat" if is_tr else "Launch Tool",
        "read_more_btn": "Devamını Oku" if is_tr else "Read Article",
        "listen_podcast_btn": "Bölümü Dinle" if is_tr else "Listen Episode",
        "asset_prefix": "" if is_tr else "../"
    }

    # Helper for rendering publications HTML
    pubs_html = []
    bibtex_dict = {}
    for idx, pub in enumerate(publications, 1):
        pid = f"bib-{idx}"
        abs_id = f"abs-{idx}"
        cat_class = pub.get("category", "sci")
        badge = pub.get("badge", "SCI-E")
        title = pub.get("title", f"Publication {idx}")
        authors = pub.get("authors_formatted", pub.get("authors", ""))
        if isinstance(authors, list):
            authors = ", ".join(authors)
        journal_info = pub.get("journal_info", pub.get("journal", ""))
        doi = pub.get("doi", "")
        doi_url = pub.get("url", f"https://doi.org/{doi}" if doi and not doi.startswith("http") else doi)
        link_label = "Makale Linki" if is_tr else "View Article"
        if not doi and "dergipark" in doi_url:
            link_label = "Dergide Gör" if is_tr else "Journal Page"
        elif not doi and ("pdf" in doi_url.lower() or "cv" in doi_url.lower()):
            link_label = "Kitap Detayı (CV PDF)" if is_tr else "Book Details (CV PDF)"
            doi_url = f"{ui['asset_prefix']}CV_Ozyildirim.pdf"

        lay_summary = pub.get("lay_summary", "")
        bibtex = pub.get("bibtex", "")
        if bibtex:
            bibtex_dict[pid] = bibtex

        doi_btn = f"<a href='{doi_url}' target='_blank' rel='noopener noreferrer' class='inline-flex items-center space-x-1 text-academic-700 font-semibold hover:underline'><i class='fa-solid fa-arrow-up-right-from-square'></i><span>{link_label}</span></a>" if doi_url else ""
        lay_btn = f"<button onclick=\"toggleAbstract('{abs_id}')\" class='inline-flex items-center space-x-1 text-slate-600 hover:text-academic-700 transition'><i class='fa-solid fa-align-left'></i><span>{ui['lay_summary_btn']}</span></button>" if lay_summary else ""
        bib_btn = f"<button onclick=\"copyBibtex('{pid}')\" class='inline-flex items-center space-x-1 text-slate-600 hover:text-academic-700 transition'><i class='fa-solid fa-quote-right'></i><span>{ui['bibtex_btn']}</span></button>" if bibtex else ""
        
        lay_title = "Halk Diliyle Açıklama: " if is_tr else "Lay Summary: "
        lay_box = f"<div id='{abs_id}' class='hidden mt-4 p-4 bg-white border border-slate-200 rounded-lg text-xs text-slate-600 leading-relaxed shadow-sm'><strong class='text-slate-800'>{lay_title}</strong>{lay_summary}</div>" if lay_summary else ""

        card = f"""
                <!-- {idx}. {title} -->
                <div class="pub-item {cat_class} border border-slate-200 rounded-xl p-6 bg-warmBg hover:shadow-md transition">
                    <div class="flex flex-wrap items-start justify-between gap-2">
                        <span class="text-xs font-semibold bg-emerald-100 text-emerald-800 px-2.5 py-1 rounded-full">{badge}</span>
                    </div>
                    <h3 class="text-lg font-bold text-academic-900 mt-3 font-serif">
                        {idx}. {title}
                    </h3>
                    <p class="text-sm text-slate-600 mt-2">
                        {authors}
                    </p>
                    <p class="text-xs text-slate-500 mt-2">
                        <em>{journal_info}</em>
                    </p>
                    <div class="mt-4 flex flex-wrap gap-3 text-xs">
                        {doi_btn}
                        {lay_btn}
                        {bib_btn}
                    </div>
                    {lay_box}
                </div>"""
        pubs_html.append(card)

    # Helper for Presentations HTML
    pres_html = []
    for pres in presentations:
        p_badge = pres.get("badge", "[Kongre / Etkinlik]")
        p_date = pres.get("date", "[Tarih]")
        p_title = pres.get("title", "[Sunum Başlığı]")
        p_desc = pres.get("summary", pres.get("body", "[Sunum Açıklaması]"))
        p_slides = pres.get("slide_count", "[Slayt Sayısı]")
        p_live = pres.get("html_url", "")
        p_dl = pres.get("download_url", f"{ui['asset_prefix']}CV_Ozyildirim.pdf")
        
        live_btn = f"<a href='{p_live}' target='_blank' class='text-emerald-700 font-semibold hover:underline flex items-center space-x-1'><i class='fa-solid fa-play'></i><span>{ui['live_slide_btn']}</span></a>" if p_live else ""
        dl_btn = f"<a href='{p_dl}' target='_blank' class='text-academic-700 font-semibold hover:underline flex items-center space-x-1'><i class='fa-solid fa-download'></i><span>{ui['download_slide_btn']}</span></a>" if p_dl else ""

        card = f"""
                <div class="bg-warmBg rounded-xl border border-slate-200 p-6 flex flex-col justify-between hover:shadow-md hover:border-academic-700 transition">
                    <div>
                        <div class="flex justify-between items-center mb-3">
                            <span class="text-[11px] font-bold bg-amber-100 text-amber-900 px-2.5 py-0.5 rounded-full">{p_badge}</span>
                            <span class="text-xs text-slate-400 font-mono">{p_date}</span>
                        </div>
                        <h3 class="font-serif font-bold text-lg text-academic-900">
                            {p_title}
                        </h3>
                        <p class="text-xs text-slate-600 mt-2.5 leading-relaxed">
                            {p_desc}
                        </p>
                    </div>
                    <div class="mt-5 pt-4 border-t border-slate-200 flex flex-wrap justify-between items-center gap-2 text-xs">
                        <span class="text-slate-500 font-mono text-[11px]"><i class="fa-solid fa-file-powerpoint text-amber-600 mr-1"></i> {p_slides}</span>
                        <div class="flex items-center space-x-3">
                            {live_btn}
                            {dl_btn}
                        </div>
                    </div>
                </div>"""
        pres_html.append(card)

    # Template card for presentation
    pres_html.append(f"""
                <div class="border-2 border-dashed border-slate-200 rounded-xl p-6 flex flex-col justify-center items-center text-center bg-slate-50/50 hover:bg-slate-100/60 transition">
                    <div class="w-10 h-10 rounded-full bg-academic-100 text-academic-700 flex items-center justify-center mb-3">
                        <i class="fa-solid fa-file-circle-plus text-base"></i>
                    </div>
                    <h3 class="font-serif font-bold text-base text-slate-800">{"[Yeni Sunum Ekleyin]" if is_tr else "[Add New Presentation]"}</h3>
                    <p class="text-xs text-slate-500 mt-1 max-w-xs">
                        {"Obsidian'dan yeni bir sunum notu oluşturarak buraya anında slayt ekleyebilirsiniz." if is_tr else "Create a new presentation note in Obsidian to add slides here instantly."}
                    </p>
                    <span class="mt-4 text-xs font-semibold text-academic-700">Obsidian _templates &rarr;</span>
                </div>""")

    # Helper for Tools HTML
    tools_html = []
    for tool in tools:
        t_badge = tool.get("badge", "[Kategori]")
        t_tech = tool.get("tech", "[R / Shiny / Python]")
        t_title = tool.get("title", "[Araç Adı]")
        t_desc = tool.get("summary", tool.get("body", "[Araç Açıklaması]"))
        t_url = tool.get("url", "https://github.com/drcanerozy")
        t_status = tool.get("status", "Açık Kaynak" if is_tr else "Open Source")
        
        card = f"""
                <div class="bg-white rounded-xl border border-slate-200 p-6 flex flex-col justify-between hover:shadow-md hover:border-purple-600 transition group">
                    <div>
                        <div class="flex justify-between items-center mb-3">
                            <span class="text-[11px] font-bold bg-purple-100 text-purple-900 px-2.5 py-0.5 rounded-full">{t_badge}</span>
                            <span class="text-xs text-purple-600 font-mono font-bold">{t_tech}</span>
                        </div>
                        <h3 class="font-serif font-bold text-lg text-slate-900 group-hover:text-purple-700 transition">
                            {t_title}
                        </h3>
                        <p class="text-xs text-slate-600 mt-2.5 leading-relaxed">
                            {t_desc}
                        </p>
                    </div>
                    <div class="mt-5 pt-4 border-t border-slate-100 flex justify-between items-center text-xs">
                        <span class="text-slate-500 flex items-center"><i class="fa-solid fa-code mr-1.5 text-purple-600"></i> {t_status}</span>
                        <a href="{t_url}" target="_blank" rel="noopener noreferrer" class="text-purple-700 font-bold group-hover:underline flex items-center space-x-1">
                            <span>{ui['launch_tool_btn']} &rarr;</span>
                        </a>
                    </div>
                </div>"""
        tools_html.append(card)

    tools_html.append(f"""
                <div class="border-2 border-dashed border-purple-200 rounded-xl p-6 flex flex-col justify-center items-center text-center bg-white/50 hover:bg-white transition">
                    <div class="w-10 h-10 rounded-full bg-purple-100 text-purple-700 flex items-center justify-center mb-3">
                        <i class="fa-solid fa-plus text-base"></i>
                    </div>
                    <h3 class="font-serif font-bold text-base text-slate-800">{"[Yeni Araç Ekleyin]" if is_tr else "[Add New Tool]"}</h3>
                    <p class="text-xs text-slate-500 mt-1 max-w-xs">
                        {"R Shiny, Streamlit veya Web tabanlı hesaplayıcılarınızı Obsidian üzerinden ekleyebilirsiniz." if is_tr else "Add your R Shiny, Streamlit, or web calculators via Obsidian."}
                    </p>
                    <span class="mt-4 text-xs font-semibold text-purple-700">Obsidian _templates &rarr;</span>
                </div>""")

    # Helper for Articles HTML
    articles_html = []
    for art in articles:
        a_badge = art.get("badge", "[Kategori]")
        a_date = art.get("date", "[Tarih]")
        a_title = art.get("title", "[Yazı Başlığı]")
        a_desc = art.get("summary", art.get("body", "[Yazı Özeti]"))
        a_time = art.get("read_time", "5 dk" if is_tr else "5 min")
        a_url = art.get("url", "https://substack.com")
        
        card = f"""
                <article class="bg-warmBg rounded-xl border border-slate-200 p-6 flex flex-col justify-between hover:shadow-md hover:border-academic-700 transition group">
                    <div>
                        <div class="flex justify-between items-center mb-3">
                            <span class="text-[11px] font-bold bg-amber-100 text-amber-900 px-2.5 py-0.5 rounded-full">{a_badge}</span>
                            <span class="text-xs text-slate-400 font-mono">{a_date}</span>
                        </div>
                        <h3 class="font-serif font-bold text-lg text-academic-900 group-hover:text-academic-700 transition">
                            <a href="{a_url}" target="_blank" rel="noopener noreferrer">
                                {a_title}
                            </a>
                        </h3>
                        <p class="text-xs text-slate-600 mt-2.5 leading-relaxed">
                            {a_desc}
                        </p>
                    </div>
                    <div class="mt-5 pt-4 border-t border-slate-200 flex justify-between items-center text-xs text-slate-500">
                        <span class="flex items-center"><i class="fa-regular fa-clock mr-1"></i> {a_time}</span>
                        <a href="{a_url}" target="_blank" rel="noopener noreferrer" class="text-academic-700 font-semibold group-hover:underline flex items-center space-x-1">
                            <span>{ui['read_more_btn']}</span>
                            <span>&rarr;</span>
                        </a>
                    </div>
                </article>"""
        articles_html.append(card)

    articles_html.append(f"""
                <article class="border-2 border-dashed border-slate-200 rounded-xl p-6 flex flex-col justify-center items-center text-center bg-slate-50/50 hover:bg-slate-100/60 transition">
                    <div class="w-10 h-10 rounded-full bg-academic-100 text-academic-700 flex items-center justify-center mb-3">
                        <i class="fa-solid fa-plus text-base"></i>
                    </div>
                    <h3 class="font-serif font-bold text-base text-slate-800">{"[Yeni Yazı Ekleyin]" if is_tr else "[Add New Article]"}</h3>
                    <p class="text-xs text-slate-500 mt-1 max-w-xs">
                        {"Substack veya blog yazılarınızı Obsidian notları olarak yönetebilirsiniz." if is_tr else "Manage your Substack or blog posts as Obsidian notes."}
                    </p>
                    <span class="mt-4 text-xs font-semibold text-academic-700">Obsidian _templates &rarr;</span>
                </article>""")

    # Helper for Podcasts HTML
    podcasts_html = []
    for pod in podcasts:
        p_ep = pod.get("episode", "Bölüm #01" if is_tr else "Episode #01")
        p_dur = pod.get("duration", "30 dk" if is_tr else "30 min")
        p_date = pod.get("date", "[Tarih]")
        p_title = pod.get("title", "[Bölüm Başlığı]")
        p_desc = pod.get("summary", pod.get("body", "[Bölüm Özeti]"))
        p_url = pod.get("spotify_url", pod.get("url", "https://open.spotify.com"))
        
        card = f"""
                <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-6 flex flex-col justify-between hover:border-amber-400/60 transition group">
                    <div>
                        <div class="flex justify-between items-center mb-3">
                            <span class="text-xs font-bold bg-amber-500/20 text-amber-400 px-3 py-1 rounded-full border border-amber-500/30">{p_ep}</span>
                            <span class="text-xs text-slate-400 font-mono flex items-center"><i class="fa-regular fa-clock mr-1"></i> {p_dur}</span>
                        </div>
                        <h3 class="font-serif font-bold text-lg text-white group-hover:text-amber-400 transition">
                            {p_title}
                        </h3>
                        <p class="text-xs text-slate-300 mt-3 leading-relaxed">
                            {p_desc}
                        </p>
                    </div>

                    <div class="mt-6 pt-4 border-t border-slate-700/80 flex justify-between items-center text-xs">
                        <a href="{p_url}" target="_blank" rel="noopener noreferrer" class="text-emerald-400 hover:underline flex items-center space-x-1.5 font-semibold">
                            <i class="fa-brands fa-spotify text-sm"></i>
                            <span>{ui['listen_podcast_btn']}</span>
                        </a>
                        <span class="text-slate-400 text-[11px]">{p_date}</span>
                    </div>
                </div>"""
        podcasts_html.append(card)

    podcasts_html.append(f"""
                <div class="border-2 border-dashed border-slate-700 rounded-xl p-6 flex flex-col justify-center items-center text-center bg-slate-800/30 hover:bg-slate-800/60 transition">
                    <div class="w-10 h-10 rounded-full bg-slate-700 text-amber-400 flex items-center justify-center mb-3">
                        <i class="fa-solid fa-microphone text-base"></i>
                    </div>
                    <h3 class="font-serif font-bold text-base text-white">{"[Yeni Bölüm Ekleyin]" if is_tr else "[Add New Episode]"}</h3>
                    <p class="text-xs text-slate-400 mt-1 max-w-xs">
                        {"Yeni podcast bölümlerinizi Obsidian üzerinden ekleyebilirsiniz." if is_tr else "Add new podcast episodes directly via Obsidian."}
                    </p>
                    <span class="mt-4 text-xs font-semibold text-amber-400">Obsidian _templates &rarr;</span>
                </div>""")

    # Format BibTeX dictionary for JS
    bibtex_js_obj = "{\n"
    for k, v in bibtex_dict.items():
        escaped_v = v.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")
        bibtex_js_obj += f"            '{k}': `{escaped_v}`,\n"
    bibtex_js_obj += "        }"

    html = f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ui['title']}</title>
    <meta name="description" content="{bio_data.get('meta_description', 'Dr. Caner ÖZYILDIRIM - Akdeniz University Nutrition & Dietetics')}">
    <meta property="og:title" content="{ui['title']}">
    <meta property="og:description" content="{ui['role_subtitle']} | {ui['institution']}">
    <meta property="og:type" content="website">

    <!-- Favicon -->
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧬</text></svg>">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        academic: {{
                            50: '#f4f6f8',
                            100: '#e5e9ef',
                            200: '#cbd4e1',
                            700: '#2b4c6f',
                            800: '#1e3854',
                            900: '#0f1f31',
                        }},
                        warmBg: '#fbfaf8',
                        accent: '#c5a059',
                    }},
                    fontFamily: {{
                        serif: ['Playfair Display', 'serif'],
                        sans: ['Inter', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            background-color: #fbfaf8;
            color: #2d3748;
        }}
        .glass-header {{
            background: rgba(251, 250, 248, 0.94);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }}
        .academic-border {{
            border-color: rgba(43, 76, 111, 0.12);
        }}
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #f1f1f1;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #cbd4e1;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #2b4c6f;
        }}
        @keyframes fadeInOut {{
            0% {{ opacity: 0; transform: translateY(10px); }}
            15% {{ opacity: 1; transform: translateY(0); }}
            85% {{ opacity: 1; transform: translateY(0); }}
            100% {{ opacity: 0; transform: translateY(-10px); }}
        }}
        .toast-active {{
            animation: fadeInOut 3s ease forwards;
        }}
    </style>
</head>
<body class="font-sans antialiased selection:bg-academic-700 selection:text-white">

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 hidden bg-academic-900 text-white px-5 py-3 rounded-xl shadow-2xl border border-academic-700 flex items-center space-x-3 text-sm">
        <i class="fa-solid fa-circle-check text-emerald-400 text-base"></i>
        <span id="toast-message">BibTeX alıntısı panoya kopyalandı!</span>
    </div>

    <!-- NAVIGATION BAR -->
    <header class="sticky top-0 z-50 glass-header border-b academic-border transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-full bg-academic-700 text-white flex items-center justify-center font-serif font-bold text-xl shadow-sm">
                        CÖ
                    </div>
                    <div>
                        <a href="#" class="font-serif font-bold text-xl text-academic-900 tracking-tight hover:text-academic-700 transition">Dr. Caner ÖZYILDIRIM</a>
                        <p class="text-xs text-slate-500 font-medium">{ui['role_subtitle']}</p>
                    </div>
                </div>

                <!-- Desktop Navigation -->
                <nav class="hidden xl:flex items-center space-x-5 text-sm font-medium text-slate-700">
                    <a href="#about" class="hover:text-academic-700 transition">{ui['nav_about']}</a>
                    <a href="#education" class="hover:text-academic-700 transition">{ui['nav_education']}</a>
                    <a href="#publications" class="hover:text-academic-700 transition">{ui['nav_publications']}</a>
                    <a href="#projects" class="hover:text-academic-700 transition">{ui['nav_projects']}</a>
                    <a href="#teaching" class="hover:text-academic-700 transition">{ui['nav_teaching']}</a>
                    <a href="#presentations" class="hover:text-academic-700 transition font-semibold text-academic-700">{ui['nav_presentations']}</a>
                    <a href="#tools" class="hover:text-academic-700 transition font-semibold text-purple-700">{ui['nav_tools']}</a>
                    <a href="#articles" class="hover:text-academic-700 transition">{ui['nav_articles']}</a>
                    <a href="#podcasts" class="hover:text-academic-700 transition">{ui['nav_podcasts']}</a>
                </nav>

                <!-- Language Switcher & Contact CTA -->
                <div class="hidden sm:flex items-center space-x-3">
                    <!-- Language Toggle Button -->
                    <a href="{ui['switch_lang_url']}" class="inline-flex items-center space-x-1.5 bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold px-3 py-2 rounded-lg border border-slate-300 transition shadow-sm" title="{'Switch to English' if is_tr else 'Türkçe Sayfaya Geç'}">
                        <i class="fa-solid fa-globe text-slate-600"></i>
                        <span>{ui['switch_lang_label']}</span>
                    </a>

                    <a href="mailto:canerozyildirim@akdeniz.edu.tr" class="inline-flex items-center space-x-2 bg-academic-700 hover:bg-academic-800 text-white text-xs font-semibold px-4 py-2.5 rounded-lg shadow-sm transition transform hover:-translate-y-0.5">
                        <i class="fa-solid fa-envelope"></i>
                        <span>{ui['contact_btn']}</span>
                    </a>
                </div>

                <!-- Mobile Menu Button -->
                <div class="flex items-center space-x-2 xl:hidden">
                    <a href="{ui['switch_lang_url']}" class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold px-2.5 py-1.5 rounded-md border border-slate-300">
                        {ui['switch_lang_label']}
                    </a>
                    <button id="mobile-menu-btn" aria-label="Menüyü Aç" class="text-slate-700 text-xl focus:outline-none p-2">
                        <i id="menu-icon" class="fa-solid fa-bars"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Nav Menu -->
        <div id="mobile-menu" class="hidden xl:hidden border-b academic-border bg-white px-4 pt-2 pb-6 space-y-3 text-sm shadow-lg">
            <a href="#about" class="mobile-nav-link block py-2 text-slate-700 hover:text-academic-700 font-medium">{ui['nav_about']}</a>
            <a href="#education" class="mobile-nav-link block py-2 text-slate-700 hover:text-academic-700 font-medium">{ui['nav_education']}</a>
            <a href="#publications" class="mobile-nav-link block py-2 text-slate-700 hover:text-academic-700 font-medium">{ui['nav_publications']}</a>
            <a href="#projects" class="mobile-nav-link block py-2 text-slate-700 hover:text-academic-700 font-medium">{ui['nav_projects']}</a>
            <a href="#teaching" class="mobile-nav-link block py-2 text-slate-700 hover:text-academic-700 font-medium">{ui['nav_teaching']}</a>
            <a href="#presentations" class="mobile-nav-link block py-2 text-academic-700 font-semibold">{ui['nav_presentations']}</a>
            <a href="#tools" class="mobile-nav-link block py-2 text-purple-700 font-semibold">{ui['nav_tools']}</a>
            <a href="#articles" class="mobile-nav-link block py-2 text-slate-700 hover:text-academic-700 font-medium">{ui['nav_articles']}</a>
            <a href="#podcasts" class="mobile-nav-link block py-2 text-slate-700 hover:text-academic-700 font-medium">{ui['nav_podcasts']}</a>
            <a href="mailto:canerozyildirim@akdeniz.edu.tr" class="mobile-nav-link block text-center bg-academic-700 text-white py-2.5 rounded-md font-semibold">{ui['contact_btn']}</a>
        </div>
    </header>

    <!-- 1. HERO / NARRATIVE CV SECTION -->
    <section id="about" class="py-16 md:py-24 border-b academic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                
                <!-- Profile Image & Badges Column -->
                <div class="lg:col-span-4 flex flex-col items-center text-center">
                    <div class="relative mb-6">
                        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=600" 
                             alt="Dr. Caner ÖZYILDIRIM" 
                             class="w-56 h-56 md:w-64 md:h-64 object-cover rounded-2xl shadow-xl border-4 border-white ring-1 ring-slate-200">
                        <span class="absolute bottom-3 right-3 bg-emerald-500 text-white p-2 rounded-full text-xs shadow-md" title="Aktif Araştırmacı">
                            <i class="fa-solid fa-check"></i>
                        </span>
                    </div>

                    <h2 class="text-2xl font-serif font-bold text-academic-900">Dr. Caner ÖZYILDIRIM</h2>
                    <p class="text-sm font-semibold text-academic-700 mt-1">{ui['role_subtitle']}</p>
                    <p class="text-xs text-slate-600 mt-1">{ui['institution']}</p>
                    <p class="text-xs text-slate-500">{ui['department']}</p>
                    
                    <!-- ORCID / AVESİS / Scholar / CV -->
                    <div class="flex flex-wrap justify-center gap-2 mt-4 text-xs font-medium">
                        <a href="https://orcid.org/0000-0001-8227-9575" target="_blank" rel="noopener noreferrer" class="bg-slate-100 hover:bg-slate-200 text-slate-700 px-3 py-1.5 rounded-md border border-slate-200 flex items-center space-x-1.5 transition shadow-sm" title="ORCID Profile">
                            <i class="fa-brands fa-orcid text-emerald-600 text-sm"></i>
                            <span>0000-0001-8227-9575</span>
                        </a>
                        <a href="https://avesis.akdeniz.edu.tr" target="_blank" rel="noopener noreferrer" class="bg-slate-100 hover:bg-slate-200 text-slate-700 px-3 py-1.5 rounded-md border border-slate-200 flex items-center space-x-1.5 transition shadow-sm" title="Akdeniz AVESİS">
                            <i class="fa-solid fa-building-columns text-academic-700 text-sm"></i>
                            <span>Akdeniz AVESİS</span>
                        </a>
                        <a href="https://scholar.google.com" target="_blank" rel="noopener noreferrer" class="bg-slate-100 hover:bg-slate-200 text-slate-700 px-3 py-1.5 rounded-md border border-slate-200 flex items-center space-x-1.5 transition shadow-sm" title="Google Scholar">
                            <i class="fa-solid fa-graduation-cap text-blue-600 text-sm"></i>
                            <span>Google Scholar</span>
                        </a>
                        <a href="{ui['asset_prefix']}CV_Ozyildirim.pdf" target="_blank" class="bg-academic-50 hover:bg-academic-100 text-academic-700 px-3 py-1.5 rounded-md border border-academic-200 flex items-center space-x-1.5 transition shadow-sm">
                            <i class="fa-solid fa-file-arrow-down"></i>
                            <span>{ui['cv_btn']}</span>
                        </a>
                    </div>

                    <!-- Social Icons -->
                    <div class="flex flex-wrap justify-center items-center gap-3 mt-6 text-slate-600 text-lg">
                        <a href="mailto:canerozyildirim@akdeniz.edu.tr" class="hover:text-academic-700 transition p-1" title="E-posta"><i class="fa-solid fa-envelope"></i></a>
                        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="hover:text-pink-600 transition p-1" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
                        <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" class="hover:text-red-600 transition p-1" title="YouTube"><i class="fa-brands fa-youtube"></i></a>
                        <a href="https://x.com" target="_blank" rel="noopener noreferrer" class="hover:text-slate-900 transition p-1" title="X (Twitter)"><i class="fa-brands fa-x-twitter"></i></a>
                        <a href="#articles" class="hover:text-amber-600 transition p-1" title="Yazılar & Blog"><i class="fa-solid fa-newspaper"></i></a>
                        <a href="#podcasts" class="hover:text-emerald-500 transition p-1" title="Spotify Podcast"><i class="fa-brands fa-spotify"></i></a>
                        <a href="#podcasts" class="hover:text-purple-500 transition p-1" title="Apple Podcasts"><i class="fa-solid fa-podcast"></i></a>
                        <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="hover:text-blue-600 transition p-1" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="https://github.com/drcanerozy" target="_blank" rel="noopener noreferrer" class="hover:text-slate-900 transition p-1" title="GitHub"><i class="fa-brands fa-github"></i></a>
                    </div>
                </div>

                <!-- Academic Narrative Bio -->
                <div class="lg:col-span-8 space-y-6">
                    <div class="inline-flex items-center space-x-2 bg-academic-50 text-academic-700 px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider">
                        <i class="fa-solid fa-feather-pointed"></i>
                        <span>{bio_data.get('tagline', 'Akademik Profil & Araştırma Vizyonu' if is_tr else 'Academic Profile & Research Vision')}</span>
                    </div>

                    <h1 class="text-3xl md:text-4xl font-serif font-bold text-academic-900 leading-tight">
                        {bio_data.get('heading', 'Metabolik Esneklik, Yağ Dokusu Disfonksiyonu ve Kardiyometabolik Bozukluklarda Biyoistatistiksel Modelleme' if is_tr else 'Metabolic Flexibility, Adipose Dysfunction, and Biostatistical Modeling in Cardiometabolic Disorders')}
                    </h1>

                    <div class="text-slate-700 leading-relaxed text-base space-y-4">
                        {bio_body}
                    </div>

                    <!-- Key Metrics Grid -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t academic-border">
                        <div class="p-3 bg-white rounded-lg border border-slate-100 shadow-sm hover:border-academic-200 transition">
                            <div class="text-2xl font-serif font-bold text-academic-700">13</div>
                            <div class="text-xs text-slate-500 font-medium">{'Hakemli Makale (10 SCI/SCI-E)' if is_tr else 'Peer-Reviewed Articles (10 SCI/SCI-E)'}</div>
                        </div>
                        <div class="p-3 bg-white rounded-lg border border-slate-100 shadow-sm hover:border-academic-200 transition">
                            <div class="text-2xl font-serif font-bold text-academic-700">4</div>
                            <div class="text-xs text-slate-500 font-medium">{'Akademik Kitap Bölümü' if is_tr else 'Academic Book Chapters'}</div>
                        </div>
                        <div class="p-3 bg-white rounded-lg border border-slate-100 shadow-sm hover:border-academic-200 transition">
                            <div class="text-2xl font-serif font-bold text-academic-700">3</div>
                            <div class="text-xs text-slate-500 font-medium">{'Uluslararası / Ulusal Proje' if is_tr else 'International / National Projects'}</div>
                        </div>
                        <div class="p-3 bg-white rounded-lg border border-slate-100 shadow-sm hover:border-academic-200 transition">
                            <div class="text-2xl font-serif font-bold text-academic-700">CA23110</div>
                            <div class="text-xs text-slate-500 font-medium">{'COST INFLAMomx Üyesi' if is_tr else 'COST INFLAMomx Member'}</div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 2. EDUCATION SECTION -->
    <section id="education" class="py-16 bg-white border-b academic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="max-w-3xl mb-10">
                <span class="text-xs font-semibold text-accent uppercase tracking-widest">{'Akademik Geçmiş & Dereceler' if is_tr else 'Academic Background & Degrees'}</span>
                <h2 class="text-3xl font-serif font-bold text-academic-900 mt-1">{ui['nav_education']} & {'Akademik Görevler' if is_tr else 'Academic Positions'}</h2>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Education Column -->
                <div class="space-y-6">
                    <h3 class="text-xl font-serif font-bold text-academic-900 flex items-center space-x-2">
                        <i class="fa-solid fa-graduation-cap text-academic-700"></i>
                        <span>{'Eğitim Bilgileri' if is_tr else 'Education'}</span>
                    </h3>

                    <!-- PhD -->
                    <div class="p-5 rounded-xl border border-slate-200 bg-warmBg">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="text-xs font-bold text-academic-700 bg-academic-100 px-2.5 py-0.5 rounded">{'Doktora (PhD)' if is_tr else 'Doctor of Philosophy (PhD)'}</span>
                                <h4 class="font-bold text-slate-900 text-base mt-2">{'Ankara Üniversitesi Sağlık Bilimleri Enstitüsü' if is_tr else 'Ankara University Graduate School of Health Sciences'}</h4>
                                <p class="text-xs text-slate-600 font-medium">{'Beslenme ve Diyetetik Anabilim Dalı • 2019 – 2024' if is_tr else 'Department of Nutrition and Dietetics • 2019 – 2024'}</p>
                            </div>
                            <span class="text-xs font-mono text-slate-400">12 {'Kasım' if is_tr else 'November'} 2024</span>
                        </div>
                        <p class="text-xs text-slate-700 mt-3">
                            <strong>{'Tez:' if is_tr else 'Dissertation:'}</strong> <em>{'Non-Alkolik Yağlı Karaciğer Hastalığı (NAFLD) Şiddetine Göre Diyetle İlişkili Risk Faktörlerinin Değerlendirilmesi' if is_tr else 'Evaluation of Diet-Related Risk Factors According to the Severity of Non-Alcoholic Fatty Liver Disease (NAFLD)'}</em>
                        </p>
                        <p class="text-xs text-slate-500 mt-1">{'Danışman:' if is_tr else 'Advisor:'} Prof. Dr. Nurcan Yabancı Ayhan</p>
                    </div>

                    <!-- MSc -->
                    <div class="p-5 rounded-xl border border-slate-200 bg-warmBg">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="text-xs font-bold text-academic-700 bg-academic-100 px-2.5 py-0.5 rounded">{'Yüksek Lisans (MSc)' if is_tr else 'Master of Science (MSc)'}</span>
                                <h4 class="font-bold text-slate-900 text-base mt-2">{'Ondokuz Mayıs Üniversitesi Sağlık Bilimleri Enstitüsü' if is_tr else 'Ondokuz Mayis University Graduate School of Health Sciences'}</h4>
                                <p class="text-xs text-slate-600 font-medium">{'Beslenme Bilimleri (Tezli) • 2016 – 2019' if is_tr else 'Nutritional Sciences (With Thesis) • 2016 – 2019'}</p>
                            </div>
                            <span class="text-xs font-mono text-slate-400">{'Ocak' if is_tr else 'January'} 2019</span>
                        </div>
                        <p class="text-xs text-slate-700 mt-3">
                            <strong>{'Tez:' if is_tr else 'Thesis:'}</strong> <em>{'İlk Kez Koroner Arter Hastalığı Tanısı Alan Bireylerde Zonulin, Total Antioksidan Kapasite, Total Oksidatif Seviye ve Beslenme İlişkisinin Değerlendirilmesi' if is_tr else 'Evaluation of the Relationship Between Zonulin, Total Antioxidant Capacity, Total Oxidant Status and Nutrition in Newly Diagnosed Coronary Artery Disease Patients'}</em>
                        </p>
                        <p class="text-xs text-slate-500 mt-1">{'Danışman:' if is_tr else 'Advisor:'} Dr. Öğr. Üyesi Alper Tokay</p>
                    </div>

                    <!-- BSc -->
                    <div class="p-5 rounded-xl border border-slate-200 bg-warmBg">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="text-xs font-bold text-academic-700 bg-academic-100 px-2.5 py-0.5 rounded">{'Lisans (BSc)' if is_tr else 'Bachelor of Science (BSc)'}</span>
                                <h4 class="font-bold text-slate-900 text-base mt-2">{'Ondokuz Mayıs Üniversitesi Sağlık Bilimleri Fakültesi' if is_tr else 'Ondokuz Mayis University Faculty of Health Sciences'}</h4>
                                <p class="text-xs text-slate-600 font-medium">{'Beslenme ve Diyetetik Bölümü • 2012 – 2016' if is_tr else 'Department of Nutrition and Dietetics • 2012 – 2016'}</p>
                            </div>
                            <span class="text-xs font-mono text-slate-400">{'Haziran' if is_tr else 'June'} 2016</span>
                        </div>
                    </div>
                </div>

                <!-- Academic Appointments & Credentials -->
                <div class="space-y-6">
                    <h3 class="text-xl font-serif font-bold text-academic-900 flex items-center space-x-2">
                        <i class="fa-solid fa-briefcase text-academic-700"></i>
                        <span>{'Akademik Görevler & Yetkinlikler' if is_tr else 'Positions & Competencies'}</span>
                    </h3>

                    <!-- Appointment -->
                    <div class="p-5 rounded-xl border border-slate-200 bg-warmBg">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="text-xs font-bold text-emerald-800 bg-emerald-100 px-2.5 py-0.5 rounded">{'Aktif Görev' if is_tr else 'Current Position'}</span>
                                <h4 class="font-bold text-slate-900 text-base mt-2">{'Araştırma Görevlisi Dr.' if is_tr else 'Research Assistant, PhD'}</h4>
                                <p class="text-xs text-slate-600 font-medium">{'Akdeniz Üniversitesi Sağlık Bilimleri Fakültesi' if is_tr else 'Akdeniz University Faculty of Health Sciences'}</p>
                                <p class="text-xs text-slate-500">{'Beslenme ve Diyetetik Bölümü • 2017 – Günümüz' if is_tr else 'Department of Nutrition and Dietetics • 2017 – Present'}</p>
                            </div>
                        </div>
                        <p class="text-xs text-slate-700 mt-3 leading-relaxed">
                            {'Klinik ve epidemiyolojik araştırmalar yürütme, biyoistatistiksel modelleme, lisans dersleri anlatımı ve lisans bitirme tezleri danışmanlığı.' if is_tr else 'Conducting clinical and epidemiological research, biostatistical modeling, undergraduate teaching, and mentoring bachelor theses.'}
                        </p>
                    </div>

                    <!-- Certifications & AI -->
                    <div class="p-5 rounded-xl border border-slate-200 bg-warmBg space-y-3">
                        <h4 class="font-bold text-slate-900 text-sm flex items-center space-x-2">
                            <i class="fa-solid fa-award text-amber-500"></i>
                            <span>{'Ağlar, Akreditasyonlar & Yetkinlikler' if is_tr else 'Networks, Accreditations & Skills'}</span>
                        </h4>
                        
                        <div class="pt-2 border-t border-slate-200 space-y-3 text-xs text-slate-700">
                            <div>
                                <strong class="text-academic-700 flex items-center space-x-1.5">
                                    <i class="fa-solid fa-robot text-purple-600"></i>
                                    <span>{'Yapay Zeka (AI) & LLM Yetkinliği:' if is_tr else 'Artificial Intelligence (AI) & LLMs:'}</span>
                                </strong>
                                <p class="text-slate-600 mt-0.5">{'Büyük Dil Modelleri (LLM), hesaplamalı beslenme, literatür sentezi ve veri madenciliği.' if is_tr else 'Large Language Models (LLMs), computational nutrition, literature synthesis, and data mining.'}</p>
                            </div>
                            <div>
                                <strong class="text-academic-700 flex items-center space-x-1.5">
                                    <i class="fa-solid fa-chart-line text-blue-600"></i>
                                    <span>{'Biyoistatistik & R Programlama:' if is_tr else 'Biostatistics & R Programming:'}</span>
                                </strong>
                                <p class="text-slate-600 mt-0.5">{'Çok değişkenli modelleme, sağkalım analizleri, ggplot2 veri görselleştirme.' if is_tr else 'Multivariable modeling, survival analysis, publication-grade ggplot2 visualization.'}</p>
                            </div>
                            <div>
                                <strong class="text-academic-700 flex items-center space-x-1.5">
                                    <i class="fa-solid fa-network-wired text-emerald-600"></i>
                                    <span>COST Action CA23110 (INFLAMomx):</span>
                                </strong>
                                <p class="text-slate-600 mt-0.5">{'Metabolik enflamasyon ve multi-omics veri entegrasyonu çalışma grubu üyeliği.' if is_tr else 'Working group member on multi-omics data integration in metabolic inflammation.'}</p>
                            </div>
                            <div>
                                <strong class="text-academic-700 flex items-center space-x-1.5">
                                    <i class="fa-solid fa-certificate text-amber-600"></i>
                                    <span>{'Deney Hayvanları Kullanım Sertifikası:' if is_tr else 'Laboratory Animal Care Certificate:'}</span>
                                </strong>
                                <p class="text-slate-600 mt-0.5">{'Kemirgen modellerinde deneysel prosedürler ve biyo-etik akreditasyonu.' if is_tr else 'Experimental procedures in rodent models and bio-ethical research accreditation.'}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. PUBLICATIONS SECTION -->
    <section id="publications" class="py-16 bg-white border-b academic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-10">
                <div>
                    <span class="text-xs font-semibold text-accent uppercase tracking-widest">{'Bibliyografya & Bilimsel Çıktılar' if is_tr else 'Bibliography & Scientific Outputs'}</span>
                    <h2 class="text-3xl font-serif font-bold text-academic-900 mt-1">{ui['nav_publications']}</h2>
                </div>

                <!-- Filter Tabs -->
                <div class="mt-4 md:mt-0 flex flex-wrap gap-2 text-xs font-medium" id="pub-filters">
                    <button data-filter="all" class="pub-filter-btn active bg-academic-700 text-white px-3.5 py-2 rounded-lg transition shadow-sm">{ui['all_filter']} ({len(publications)})</button>
                    <button data-filter="sci" class="pub-filter-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-3.5 py-2 rounded-lg transition">{ui['sci_filter']}</button>
                    <button data-filter="national" class="pub-filter-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-3.5 py-2 rounded-lg transition">{ui['national_filter']}</button>
                    <button data-filter="book" class="pub-filter-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-3.5 py-2 rounded-lg transition">{ui['book_filter']}</button>
                    <button data-filter="conference" class="pub-filter-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-3.5 py-2 rounded-lg transition">{ui['conf_filter']}</button>
                </div>
            </div>

            <!-- Publications Container -->
            <div class="space-y-6" id="publications-container">
                {"".join(pubs_html)}
            </div>

            <!-- Expand/Collapse Toggle -->
            <div id="toggle-pubs-container" class="mt-8 flex justify-center">
                <button onclick="toggleShowAllPubs()" class="inline-flex items-center space-x-2 bg-white hover:bg-academic-50 text-academic-700 font-semibold px-6 py-3 rounded-xl border border-academic-200 shadow-sm transition transform hover:-translate-y-0.5">
                    <span id="toggle-pubs-text">{ui['toggle_pubs_more']}</span>
                    <i id="toggle-pubs-icon" class="fa-solid fa-chevron-down text-xs ml-1"></i>
                </button>
            </div>
        </div>
    </section>

    <!-- 4. PROJECTS SECTION -->
    <section id="projects" class="py-16 bg-white border-b academic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <span class="text-xs font-semibold text-accent uppercase tracking-widest">{'Bilimsel Araştırma & İşbirlikleri' if is_tr else 'Scientific Research & Collaborations'}</span>
            <h2 class="text-3xl font-serif font-bold text-academic-900 mt-1 mb-8">{ui['nav_projects']}</h2>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- World Bank -->
                <div class="bg-warmBg rounded-xl border border-slate-200 p-6 shadow-sm flex flex-col justify-between hover:shadow-md transition">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <span class="text-xs font-bold bg-blue-100 text-blue-800 px-3 py-1 rounded-full flex items-center">
                                <i class="fa-solid fa-globe mr-1.5 text-[11px]"></i> {'Dünya Bankası Destekli Proje' if is_tr else 'World Bank Supported Project'}
                            </span>
                        </div>
                        <h3 class="text-xl font-serif font-bold text-academic-900">
                            {'Otizm Spektrum Bozukluğu ve Zihinsel Özel Gereksinimli Bireylerde Bireysel Beslenme Danışmanlığı Modeli' if is_tr else 'Individual Nutrition Counseling Model in Children with Autism Spectrum Disorder and Intellectual Disabilities'}
                        </h3>
                        <p class="text-sm text-slate-600 mt-3 leading-relaxed">
                            {'Özel gereksinimli bireylerde hizmet kapasitesinin güçlendirilmesi, aile temelli beslenme danışmanlığı modelinin geliştirilmesi ve beslenme kalitesinin artırılması.' if is_tr else 'Strengthening service capacity, developing family-based nutrition counseling protocols, and enhancing dietary quality for individuals with special needs.'}
                        </p>
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-200 flex justify-between items-center text-xs">
                        <span class="text-slate-600 font-medium">{'Fon: Dünya Bankası' if is_tr else 'Funding: World Bank'}</span>
                        <a href="{ui['asset_prefix']}CV_Ozyildirim.pdf" target="_blank" class="text-academic-700 font-semibold hover:underline flex items-center space-x-1">
                            <span>{'Detaylar' if is_tr else 'Details'} &rarr;</span>
                        </a>
                    </div>
                </div>

                <!-- Ministry of Health -->
                <div class="bg-warmBg rounded-xl border border-slate-200 p-6 shadow-sm flex flex-col justify-between hover:shadow-md transition">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <span class="text-xs font-bold bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full">
                                <i class="fa-solid fa-hand-holding-medical mr-1.5 text-[11px]"></i> {'T.C. Sağlık Bakanlığı Projesi' if is_tr else 'Republic of Turkey Ministry of Health Project'}
                            </span>
                        </div>
                        <h3 class="text-xl font-serif font-bold text-academic-900">
                            {'Otizm ve Zihinsel Özel Gereksinimli Bireylerde Ulusal Beslenme Araştırması' if is_tr else 'National Nutritional Survey in Individuals with Autism and Special Healthcare Needs'}
                        </h3>
                        <p class="text-sm text-slate-600 mt-3 leading-relaxed">
                            {'Sağlık Bakanlığı koordinasyonunda özel gereksinimli çocukların beslenme durumunun, büyüme parametrelerinin ve diyet ihtiyaçlarının haritalanması.' if is_tr else 'Mapping nutritional status, anthropometric growth indicators, and dietary needs of children with special needs across national centers.'}
                        </p>
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-200 flex justify-between items-center text-xs">
                        <span class="text-slate-600 font-medium">{'Kapsam: Ulusal Proje' if is_tr else 'Scope: National Project'}</span>
                        <a href="{ui['asset_prefix']}CV_Ozyildirim.pdf" target="_blank" class="text-academic-700 font-semibold hover:underline flex items-center space-x-1">
                            <span>{'Detaylar' if is_tr else 'Details'} &rarr;</span>
                        </a>
                    </div>
                </div>

                <!-- BAP -->
                <div class="bg-warmBg rounded-xl border border-slate-200 p-6 shadow-sm flex flex-col justify-between hover:shadow-md transition">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <span class="text-xs font-bold bg-purple-100 text-purple-800 px-3 py-1 rounded-full">
                                <i class="fa-solid fa-flask mr-1.5 text-[11px]"></i> {'Üniversite Bilimsel Araştırma Projesi (BAP)' if is_tr else 'University Scientific Research Project (BAP)'}
                            </span>
                        </div>
                        <h3 class="text-xl font-serif font-bold text-academic-900">
                            {'Koroner Arter Hastalarında Zonulin, Oksidatif Stres ve Beslenme İlişkisi' if is_tr else 'Relationship Between Zonulin, Oxidative Stress and Diet in Coronary Artery Disease'}
                        </h3>
                        <p class="text-sm text-slate-600 mt-3 leading-relaxed">
                            {'İlk kez koroner arter hastalığı tanısı alan bireylerde bağırsak geçirgenliği belirteci zonulin, total antioksidan kapasite (TAC), total oksidatif stres seviyesi (TOS) ve diyet örüntülerinin incelenmesi.' if is_tr else 'Evaluating intestinal permeability marker zonulin, total antioxidant capacity (TAC), total oxidant status (TOS) and dietary patterns in CAD patients.'}
                        </p>
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-200 flex justify-between items-center text-xs">
                        <span class="text-slate-600 font-medium">{'Alan: Biyobelirteç Analitiği' if is_tr else 'Field: Biomarker Analytics'}</span>
                        <a href="{ui['asset_prefix']}CV_Ozyildirim.pdf" target="_blank" class="text-academic-700 font-semibold hover:underline flex items-center space-x-1">
                            <span>{'Detaylar' if is_tr else 'Details'} &rarr;</span>
                        </a>
                    </div>
                </div>

                <!-- COST Action CA23110 -->
                <div class="bg-warmBg rounded-xl border border-slate-200 p-6 shadow-sm flex flex-col justify-between hover:shadow-md transition">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <span class="text-xs font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
                                <i class="fa-solid fa-diagram-project mr-1.5 text-[11px]"></i> COST Action CA23110 (European Union)
                            </span>
                        </div>
                        <h3 class="text-xl font-serif font-bold text-academic-900">
                            INFLAMomx: Multi-Omics Data Integration in Metabolic Inflammation
                        </h3>
                        <p class="text-sm text-slate-600 mt-3 leading-relaxed">
                            {'Metabolik enflamasyon ve klinik fenotiplerde multi-omiks verilerin entegrasyonu, biyobelirteç keşfi ve biyoinformatik modelleme üzerine Avrupa konsorsiyumu çalışma grubu üyeliği.' if is_tr else 'European consortium working group member on integrating multi-omics datasets, biomarker discovery, and bioinformatics modeling in metabolic inflammation.'}
                        </p>
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-200 flex justify-between items-center text-xs">
                        <span class="text-slate-600 font-medium">Network: COST CA23110</span>
                        <a href="https://www.cost.eu" target="_blank" rel="noopener noreferrer" class="text-academic-700 font-semibold hover:underline flex items-center space-x-1">
                            <span>{'COST Portalı' if is_tr else 'COST Portal'} &rarr;</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. TEACHING SECTION -->
    <section id="teaching" class="py-16 border-b academic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="max-w-3xl mb-10">
                <span class="text-xs font-semibold text-accent uppercase tracking-widest">{'Pedagoji & Eğitim Faaliyetleri' if is_tr else 'Pedagogy & Teaching'}</span>
                <h2 class="text-3xl font-serif font-bold text-academic-900 mt-1">{'Verdiğim Lisans Dersleri' if is_tr else 'Undergraduate Courses'}</h2>
                <p class="text-sm text-slate-600 mt-1">{'Akdeniz Üniversitesi Sağlık Bilimleri Fakültesi Beslenme ve Diyetetik Bölümü bünyesinde yürütülen dersler:' if is_tr else 'Courses taught at Akdeniz University Faculty of Health Sciences, Department of Nutrition and Dietetics:'}</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Course 1 -->
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm hover:border-academic-700 transition flex flex-col justify-between overflow-hidden">
                    <div class="p-5">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold text-academic-700 bg-academic-50 px-2.5 py-1 rounded">{'Lisans Modülü' if is_tr else 'Undergraduate'}</span>
                            <i class="fa-solid fa-laptop-code text-academic-700 text-lg"></i>
                        </div>
                        <h3 class="font-bold text-slate-900 text-base mt-3">{'Beslenme ve Diyetetikte Bilgisayar ve Yapay Zeka Uygulamaları' if is_tr else 'Computer and AI Applications in Nutrition & Dietetics'}</h3>
                        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                            {'R programlama dili ile biyoistatistiksel veri analizi, veri görselleştirme, yapay zeka ve hesaplamalı yöntemler.' if is_tr else 'Biostatistical data analysis with R programming, ggplot2 visualization, AI, and computational nutrition methodology.'}
                        </p>
                    </div>
                    <div class="border-t border-slate-100 bg-warmBg p-5">
                        <button onclick="toggleCourseDetails('course-det-1', 'course-icon-1')" class="w-full flex items-center justify-between text-xs font-bold text-academic-700 hover:text-academic-900 transition">
                            <span>{'Ders İçeriği & Laboratuvar Uygulamaları' if is_tr else 'Course Details & Lab Practice'}</span>
                            <i id="course-icon-1" class="fa-solid fa-chevron-down text-[11px] transition-transform duration-200"></i>
                        </button>
                        <div id="course-det-1" class="hidden mt-3 text-xs text-slate-600 space-y-2 border-t border-slate-200 pt-3">
                            <p><strong>🎯 {'Ana Konular:' if is_tr else 'Core Topics:'}</strong> {'R ve RStudio ortamı, tidyverse ile veri manipülasyonu, ggplot2 bilimsel grafik üretimi.' if is_tr else 'R/RStudio environment, tidyverse data wrangling, scientific publication figures with ggplot2.'}</p>
                            <p><strong>💻 {'AI & Uygulamalar:' if is_tr else 'AI & Applications:'}</strong> {'Besin tüketim verileri, regresyon modelleri, literatür sentezinde Büyük Dil Modelleri (LLM).' if is_tr else 'Dietary records analysis, multivariable models, Large Language Models (LLM) for literature synthesis.'}</p>
                        </div>
                    </div>
                </div>

                <!-- Course 2 -->
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm hover:border-academic-700 transition flex flex-col justify-between overflow-hidden">
                    <div class="p-5">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold text-academic-700 bg-academic-50 px-2.5 py-1 rounded">{'Lisans Modülü' if is_tr else 'Undergraduate'}</span>
                            <i class="fa-solid fa-shield-virus text-academic-700 text-lg"></i>
                        </div>
                        <h3 class="font-bold text-slate-900 text-base mt-3">{'İmmün Sistem ve İmmünonütrisyon' if is_tr else 'Immune System and Immunonutrition'}</h3>
                        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                            {'Bağışıklık mekanizmaları, besin ögesi-immün sistem etkileşimleri ve enflamatuar hastalıklarda immünonütrisyon.' if is_tr else 'Immunological pathways, nutrient-immune interactions, microbiota modulation, and therapeutic immunonutrition protocols.'}
                        </p>
                    </div>
                    <div class="border-t border-slate-100 bg-warmBg p-5">
                        <button onclick="toggleCourseDetails('course-det-2', 'course-icon-2')" class="w-full flex items-center justify-between text-xs font-bold text-academic-700 hover:text-academic-900 transition">
                            <span>{'Ders İçeriği & Klinik Yaklaşımlar' if is_tr else 'Course Details & Clinical Approaches'}</span>
                            <i id="course-icon-2" class="fa-solid fa-chevron-down text-[11px] transition-transform duration-200"></i>
                        </button>
                        <div id="course-det-2" class="hidden mt-3 text-xs text-slate-600 space-y-2 border-t border-slate-200 pt-3">
                            <p><strong>🎯 {'Ana Konular:' if is_tr else 'Core Topics:'}</strong> {'Doğuştan ve edinsel bağışıklık, sitokin salınımı, bağırsak epitel bariyeri ve mukoza bağışıklığı.' if is_tr else 'Innate/adaptive immunity, cytokine responses, gut barrier integrity, and mucosal immunology.'}</p>
                            <p><strong>💊 {'Bileşenler:' if is_tr else 'Components:'}</strong> {'Glutamin, arjinin, omega-3, nükleotidler, çinko, D vitamini ve probiyotikler.' if is_tr else 'Glutamine, arginine, omega-3 fatty acids, nucleotides, zinc, vitamin D, and probiotics.'}</p>
                        </div>
                    </div>
                </div>

                <!-- Course 3 -->
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm hover:border-academic-700 transition flex flex-col justify-between overflow-hidden">
                    <div class="p-5">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold text-academic-700 bg-academic-50 px-2.5 py-1 rounded">{'Lisans Modülü' if is_tr else 'Undergraduate'}</span>
                            <i class="fa-solid fa-notes-medical text-academic-700 text-lg"></i>
                        </div>
                        <h3 class="font-bold text-slate-900 text-base mt-3">{'Yetişkin Hastalıklarında Tıbbi Beslenme Tedavisi' if is_tr else 'Medical Nutrition Therapy in Adult Diseases'}</h3>
                        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                            {'Kardiyometabolik hastalıklar, diyabet, obezite ve karaciğer yağlanmasında patofizyoloji ve klinik diyet tedavisi.' if is_tr else 'Pathophysiology and evidence-based clinical diet therapy in diabetes, obesity, CVD, and liver diseases.'}
                        </p>
                    </div>
                    <div class="border-t border-slate-100 bg-warmBg p-5">
                        <button onclick="toggleCourseDetails('course-det-3', 'course-icon-3')" class="w-full flex items-center justify-between text-xs font-bold text-academic-700 hover:text-academic-900 transition">
                            <span>{'Ders İçeriği & Vaka Yönetimi' if is_tr else 'Course Details & Case Studies'}</span>
                            <i id="course-icon-3" class="fa-solid fa-chevron-down text-[11px] transition-transform duration-200"></i>
                        </button>
                        <div id="course-det-3" class="hidden mt-3 text-xs text-slate-600 space-y-2 border-t border-slate-200 pt-3">
                            <p><strong>🎯 {'Ana Konular:' if is_tr else 'Core Topics:'}</strong> {'Tip 2 Diyabet, karbonhidrat sayımı, koroner arter hastalıkları, NAFLD/MASLD ve böbrek hastalıkları.' if is_tr else 'Type 2 Diabetes, carbohydrate counting, dyslipidemia, NAFLD/MASLD, and renal nutrition therapy.'}</p>
                        </div>
                    </div>
                </div>

                <!-- Course 4 -->
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm hover:border-academic-700 transition flex flex-col justify-between overflow-hidden">
                    <div class="p-5">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold text-academic-700 bg-academic-50 px-2.5 py-1 rounded">{'Lisans Modülü' if is_tr else 'Undergraduate'}</span>
                            <i class="fa-solid fa-utensils text-academic-700 text-lg"></i>
                        </div>
                        <h3 class="font-bold text-slate-900 text-base mt-3">{'Beslenme İlkeleri ve Popüler Diyetler' if is_tr else 'Principles of Nutrition and Popular Diets'}</h3>
                        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                            {'Enerji dengesi, ketojenik diyet, aralıklı oruç (IF/TRE) ve popüler akımların fizyolojik analizi.' if is_tr else 'Energy expenditure calculations, ketogenic diets, Intermittent Fasting (IF/TRE), and popular dietary regimens.'}
                        </p>
                    </div>
                    <div class="border-t border-slate-100 bg-warmBg p-5">
                        <button onclick="toggleCourseDetails('course-det-4', 'course-icon-4')" class="w-full flex items-center justify-between text-xs font-bold text-academic-700 hover:text-academic-900 transition">
                            <span>{'Ders İçeriği & Bilimsel Değerlendirme' if is_tr else 'Course Details & Scientific Evidence'}</span>
                            <i id="course-icon-4" class="fa-solid fa-chevron-down text-[11px] transition-transform duration-200"></i>
                        </button>
                        <div id="course-det-4" class="hidden mt-3 text-xs text-slate-600 space-y-2 border-t border-slate-200 pt-3">
                            <p><strong>🎯 {'Ana Konular:' if is_tr else 'Core Topics:'}</strong> {'Intermittent Fasting (16:8, TRE), Ketojenik Diyet, Akdeniz Diyeti ve randomize kontrollü çalışma analizleri.' if is_tr else 'Intermittent fasting protocols, ketogenic diet models, Mediterranean diet, and RCT meta-analysis.'}</p>
                        </div>
                    </div>
                </div>

                <!-- Course 5 -->
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm hover:border-academic-700 transition flex flex-col justify-between overflow-hidden">
                    <div class="p-5">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold text-academic-700 bg-academic-50 px-2.5 py-1 rounded">{'Lisans Modülü' if is_tr else 'Undergraduate'}</span>
                            <i class="fa-solid fa-brain text-academic-700 text-lg"></i>
                        </div>
                        <h3 class="font-bold text-slate-900 text-base mt-3">{'Beslenmenin Psikososyal Yönleri' if is_tr else 'Psychosocial Aspects of Nutrition'}</h3>
                        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                            {'Yeme tutumları, ortoreksiya nevroza, duygusal yeme ve beslenme psikolojisi dinamikleri.' if is_tr else 'Eating attitudes, orthorexia nervosa, emotional eating, body image, and behavioral nutrition.'}
                        </p>
                    </div>
                    <div class="border-t border-slate-100 bg-warmBg p-5">
                        <button onclick="toggleCourseDetails('course-det-5', 'course-icon-5')" class="w-full flex items-center justify-between text-xs font-bold text-academic-700 hover:text-academic-900 transition">
                            <span>{'Ders İçeriği & Psikometrik Ölçümler' if is_tr else 'Course Details & Psychometrics'}</span>
                            <i id="course-icon-5" class="fa-solid fa-chevron-down text-[11px] transition-transform duration-200"></i>
                        </button>
                        <div id="course-det-5" class="hidden mt-3 text-xs text-slate-600 space-y-2 border-t border-slate-200 pt-3">
                            <p><strong>🎯 {'Ana Konular:' if is_tr else 'Core Topics:'}</strong> {'EAT-26, ORTO-15 ölçekleri, duygusal yeme skorlamaları ve psikometrik analizler.' if is_tr else 'EAT-26, ORTO-15 inventories, DEBQ emotional eating scales, and psychometric screening.'}</p>
                        </div>
                    </div>
                </div>

                <!-- Course 6 -->
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm hover:border-academic-700 transition flex flex-col justify-between overflow-hidden">
                    <div class="p-5">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold text-academic-700 bg-academic-50 px-2.5 py-1 rounded">{'Lisans Modülü' if is_tr else 'Undergraduate'}</span>
                            <i class="fa-solid fa-bullhorn text-academic-700 text-lg"></i>
                        </div>
                        <h3 class="font-bold text-slate-900 text-base mt-3">{'Beslenme ve Medya & Danışmanlık' if is_tr else 'Nutrition, Media & Counseling'}</h3>
                        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                            {'Medya okuryazarlığı, beslenme iletişimi, bilimsel bilginin topluma aktarımı ve klinik süpervizyon.' if is_tr else 'Media literacy, nutrition communication, translating evidence to public, and clinical supervision.'}
                        </p>
                    </div>
                    <div class="border-t border-slate-100 bg-warmBg p-5">
                        <button onclick="toggleCourseDetails('course-det-6', 'course-icon-6')" class="w-full flex items-center justify-between text-xs font-bold text-academic-700 hover:text-academic-900 transition">
                            <span>{'Ders İçeriği & İletişim Stratejileri' if is_tr else 'Course Details & Communication'}</span>
                            <i id="course-icon-6" class="fa-solid fa-chevron-down text-[11px] transition-transform duration-200"></i>
                        </button>
                        <div id="course-det-6" class="hidden mt-3 text-xs text-slate-600 space-y-2 border-t border-slate-200 pt-3">
                            <p><strong>🎯 {'Ana Konular:' if is_tr else 'Core Topics:'}</strong> {'Dezenformasyon analizi, bilimsel podcast kurgusu, kanıta dayalı blog yazımı.' if is_tr else 'Combating nutritional disinformation, scientific podcast design, and evidence-based blogging.'}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. PRESENTATIONS SECTION -->
    <section id="presentations" class="py-16 bg-white border-b academic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-10">
                <div>
                    <span class="text-xs font-semibold text-accent uppercase tracking-widest">{'Akademik Sunumlar & Eğitim Materyalleri' if is_tr else 'Academic Slides & Teaching Materials'}</span>
                    <h2 class="text-3xl font-serif font-bold text-academic-900 mt-1">{ui['nav_presentations']}</h2>
                    <p class="text-sm text-slate-600 mt-1">{'Konferans, sempozyum, çalıştay ve derslerimde sunduğum sunum slaytları:' if is_tr else 'Selected slides presented at conferences, symposia, workshops, and lectures:'}</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {"".join(pres_html)}
            </div>
        </div>
    </section>

    <!-- 7. TOOLS SECTION -->
    <section id="tools" class="py-16 bg-warmBg border-b academic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-10">
                <div>
                    <span class="text-xs font-semibold text-purple-700 uppercase tracking-widest">{'Hesaplamalı Çözümler & Yazılımlar' if is_tr else 'Computational Solutions & Software'}</span>
                    <h2 class="text-3xl font-serif font-bold text-academic-900 mt-1">{ui['nav_tools']}</h2>
                    <p class="text-sm text-slate-600 mt-1">{'Geliştirdiğim hesaplayıcılar, veri analiz araçları ve simülasyonlar:' if is_tr else 'Interactive calculators, data analysis tools, and computational simulations:'}</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {"".join(tools_html)}
            </div>
        </div>
    </section>

    <!-- 8. ARTICLES SECTION -->
    <section id="articles" class="py-16 bg-white border-b academic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-10">
                <div>
                    <span class="text-xs font-semibold text-accent uppercase tracking-widest">{'Düşünceler, Denemeler & Analizler' if is_tr else 'Thoughts, Essays & Analysis'}</span>
                    <h2 class="text-3xl font-serif font-bold text-academic-900 mt-1">{ui['nav_articles']}</h2>
                    <p class="text-sm text-slate-600 mt-1">{'Sondan eskiye doğru yayımlanan bilimsel değerlendirmeler ve yazılar:' if is_tr else 'Chronologically ordered scientific articles, op-eds, and reviews:'}</p>
                </div>

                <div class="mt-4 md:mt-0">
                    <a href="https://substack.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center space-x-2 text-xs font-semibold text-academic-700 hover:text-academic-900 bg-academic-50 hover:bg-academic-100 px-4 py-2 rounded-lg border border-academic-200 transition">
                        <i class="fa-solid fa-rss"></i>
                        <span>{'Tüm Yazılar (Substack)' if is_tr else 'All Articles (Substack)'} &rarr;</span>
                    </a>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {"".join(articles_html)}
            </div>
        </div>
    </section>

    <!-- 9. PODCASTS SECTION -->
    <section id="podcasts" class="py-16 bg-academic-900 text-white border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
                <div>
                    <span class="text-xs font-semibold text-accent uppercase tracking-widest">{'Sesli Yayınlar & Söyleşiler' if is_tr else 'Audio Episodes & Podcasts'}</span>
                    <h2 class="text-3xl font-serif font-bold text-white mt-1">{ui['nav_podcasts']}</h2>
                    <p class="text-sm text-slate-300 mt-1">{'Beslenme bilimi ve klinik kanıtlar üzerine sesli tartışmalar:' if is_tr else 'Audio discussions on nutritional biochemistry and clinical evidence:'}</p>
                </div>

                <div class="mt-6 md:mt-0 flex flex-wrap gap-2.5 text-xs font-medium">
                    <a href="https://open.spotify.com" target="_blank" rel="noopener noreferrer" class="bg-emerald-950/90 hover:bg-emerald-900 text-emerald-400 border border-emerald-700/60 px-4 py-2.5 rounded-xl flex items-center space-x-2 transition shadow-sm" title="Spotify">
                        <i class="fa-brands fa-spotify text-base"></i>
                        <span>Spotify</span>
                    </a>
                    <a href="https://podcasts.apple.com" target="_blank" rel="noopener noreferrer" class="bg-purple-950/90 hover:bg-purple-900 text-purple-300 border border-purple-700/60 px-4 py-2.5 rounded-xl flex items-center space-x-2 transition shadow-sm" title="Apple Podcasts">
                        <i class="fa-solid fa-podcast text-base"></i>
                        <span>Apple Podcasts</span>
                    </a>
                    <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" class="bg-red-950/90 hover:bg-red-900 text-red-300 border border-red-700/60 px-4 py-2.5 rounded-xl flex items-center space-x-2 transition shadow-sm" title="YouTube">
                        <i class="fa-brands fa-youtube text-base"></i>
                        <span>YouTube</span>
                    </a>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {"".join(podcasts_html)}
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-academic-900 text-slate-400 py-12 border-t border-slate-800 text-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center gap-6">
            <div>
                <p class="font-serif text-white font-bold text-base">Dr. Caner ÖZYILDIRIM</p>
                <p class="text-slate-400 mt-1">{ui['footer_rights']}</p>
            </div>
            
            <div class="flex flex-wrap justify-center gap-5">
                <a href="#about" class="hover:text-white transition">{ui['nav_about']}</a>
                <a href="#education" class="hover:text-white transition">{ui['nav_education']}</a>
                <a href="#publications" class="hover:text-white transition">{ui['nav_publications']}</a>
                <a href="#projects" class="hover:text-white transition">{ui['nav_projects']}</a>
                <a href="#teaching" class="hover:text-white transition">{ui['nav_teaching']}</a>
                <a href="#presentations" class="hover:text-white transition">{ui['nav_presentations']}</a>
                <a href="#tools" class="hover:text-white transition text-purple-400">{ui['nav_tools']}</a>
                <a href="#articles" class="hover:text-white transition text-amber-400">{ui['nav_articles']}</a>
                <a href="#podcasts" class="hover:text-white transition text-emerald-400">{ui['nav_podcasts']}</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE JAVASCRIPT LOGIC -->
    <script>
        // --- 1. Mobile Menu Toggle ---
        const mobileBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        const menuIcon = document.getElementById('menu-icon');
        const mobileLinks = document.querySelectorAll('.mobile-nav-link');
        
        if (mobileBtn && mobileMenu) {{
            mobileBtn.addEventListener('click', () => {{
                const isHidden = mobileMenu.classList.toggle('hidden');
                if (isHidden) {{
                    menuIcon.classList.remove('fa-xmark');
                    menuIcon.classList.add('fa-bars');
                }} else {{
                    menuIcon.classList.remove('fa-bars');
                    menuIcon.classList.add('fa-xmark');
                }}
            }});

            mobileLinks.forEach(link => {{
                link.addEventListener('click', () => {{
                    mobileMenu.classList.add('hidden');
                    menuIcon.classList.remove('fa-xmark');
                    menuIcon.classList.add('fa-bars');
                }});
            }});
        }}

        // --- 2. Publication Filtering & Top 5 Collapse/Expand Logic ---
        let showAllPubs = false;
        let activeFilter = 'all';

        const filterBtns = document.querySelectorAll('.pub-filter-btn');
        const pubItems = document.querySelectorAll('.pub-item');
        const toggleContainer = document.getElementById('toggle-pubs-container');

        function applyPubFilters() {{
            if (activeFilter === 'all') {{
                if (toggleContainer) toggleContainer.style.display = 'flex';
                pubItems.forEach((item, index) => {{
                    if (showAllPubs || index < 5) {{
                        item.style.display = 'block';
                    }} else {{
                        item.style.display = 'none';
                    }}
                }});
            }} else {{
                if (toggleContainer) toggleContainer.style.display = 'none';
                pubItems.forEach(item => {{
                    if (item.classList.contains(activeFilter)) {{
                        item.style.display = 'block';
                    }} else {{
                        item.style.display = 'none';
                    }}
                }});
            }}
        }}

        function toggleShowAllPubs() {{
            showAllPubs = !showAllPubs;
            const btnText = document.getElementById('toggle-pubs-text');
            const btnIcon = document.getElementById('toggle-pubs-icon');
            
            if (showAllPubs) {{
                btnText.innerText = "{ui['toggle_pubs_less']}";
                btnIcon.classList.remove('fa-chevron-down');
                btnIcon.classList.add('fa-chevron-up');
            }} else {{
                btnText.innerText = "{ui['toggle_pubs_more']}";
                btnIcon.classList.remove('fa-chevron-up');
                btnIcon.classList.add('fa-chevron-down');
                document.getElementById('publications').scrollIntoView({{ behavior: 'smooth' }});
            }}
            applyPubFilters();
        }}

        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                filterBtns.forEach(b => {{
                    b.classList.remove('active', 'bg-academic-700', 'text-white', 'shadow-sm');
                    b.classList.add('bg-slate-100', 'text-slate-700');
                }});
                
                btn.classList.add('active', 'bg-academic-700', 'text-white', 'shadow-sm');
                btn.classList.remove('bg-slate-100', 'text-slate-700');

                activeFilter = btn.getAttribute('data-filter');
                applyPubFilters();
            }});
        }});

        applyPubFilters();

        // --- 3. Toggle Abstract / Lay Summary ---
        function toggleAbstract(id) {{
            const element = document.getElementById(id);
            if (element) {{
                element.classList.toggle('hidden');
            }}
        }}

        // --- 4. Toggle Course Details Accordion ---
        function toggleCourseDetails(detailsId, iconId) {{
            const details = document.getElementById(detailsId);
            const icon = document.getElementById(iconId);
            if (details) {{
                const isHidden = details.classList.toggle('hidden');
                if (icon) {{
                    if (isHidden) {{
                        icon.classList.remove('rotate-180');
                    }} else {{
                        icon.classList.add('rotate-180');
                    }}
                }}
            }}
        }}

        // --- 5. Complete BibTeX Database ---
        const bibtexEntries = {bibtex_js_obj};

        function showToast(message) {{
            const toast = document.getElementById('toast');
            const msgEl = document.getElementById('toast-message');
            msgEl.innerText = message;
            toast.classList.remove('hidden');
            toast.classList.add('toast-active');
            
            setTimeout(() => {{
                toast.classList.remove('toast-active');
                toast.classList.add('hidden');
            }}, 3000);
        }}

        function copyBibtex(id) {{
            const text = bibtexEntries[id] || '';
            if (!text) return;
            
            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(text).then(() => {{
                    showToast("{'BibTeX alıntısı panoya kopyalandı!' if is_tr else 'BibTeX citation copied to clipboard!'}");
                }}).catch(() => {{
                    fallbackCopy(text);
                }});
            }} else {{
                fallbackCopy(text);
            }}
        }}

        function fallbackCopy(text) {{
            const tempInput = document.createElement("textarea");
            tempInput.value = text;
            tempInput.style.position = "fixed";
            tempInput.style.left = "-9999px";
            document.body.appendChild(tempInput);
            tempInput.select();
            try {{
                document.execCommand("copy");
                showToast("{'BibTeX alıntısı panoya kopyalandı!' if is_tr else 'BibTeX citation copied to clipboard!'}");
            }} catch (err) {{
                alert("BibTeX:\n\n" + text);
            }}
            document.body.removeChild(tempInput);
        }}
    </script>
</body>
</html>"""
    return html

def main():
    print("🚀 Building Academic Website...")
    
    # 1. Build TR site -> index.html
    tr_html = generate_html("tr")
    with open(BASE_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(tr_html)
    print("  ✅ Turkish site compiled: index.html")
    
    # 2. Build EN site -> en/index.html
    en_dir = BASE_DIR / "en"
    en_dir.mkdir(exist_ok=True)
    en_html = generate_html("en")
    with open(en_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(en_html)
    print("  ✅ English site compiled: en/index.html")
    
    print("🎉 All bilingual sites compiled successfully from Obsidian markdown!")

if __name__ == "__main__":
    main()
