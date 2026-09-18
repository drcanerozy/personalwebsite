#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
⚡ Yerel R & Quarto Yürütücüsü (R / Quarto Executor Engine)
Dr. Caner Özyıldırım Akademik Vault Altyapısı

Özellikler:
1. R kodlarını arka planda subprocess ile çalıştırır.
2. knitr::kable markdown tablolarını ayrıştırıp outputs/Table_X.md olarak kaydeder.
3. ggplot2 grafiklerini outputs/Figure_X.png olarak yakalar.
4. İlgili Obsidian makale notuna ![[Figure_X.png]] ve ![[Table_X.md]] ekler.
"""

import os
import sys
import re
import argparse
import subprocess
from pathlib import Path

def run_r_script(script_path, project_dir=None, manuscript_path=None):
    """Belirtilen R dosyasını çalıştırır ve çıktıları yönetir"""
    script_p = Path(script_path).resolve()
    if not script_p.exists():
        print(f"❌ R dosyası bulunamadı: {script_p}")
        return False

    working_dir = Path(project_dir).resolve() if project_dir else script_p.parent.parent
    outputs_dir = working_dir / "outputs"
    outputs_dir.mkdir(parents=True, exist_ok=True)

    print(f"🚀 R Scripti Yürütülüyor: {script_p.name}")
    print(f"📂 Çalışma Dizini: {working_dir}")

    cmd = ["Rscript", str(script_p)]
    try:
        proc = subprocess.run(cmd, cwd=str(working_dir), capture_output=True, text=True, check=True)
        stdout = proc.stdout
        stderr = proc.stderr
    except subprocess.CalledProcessError as e:
        print(f"❌ R yürütme hatası (Exit Code {e.returncode}):")
        print(e.stderr)
        return False

    # 1. Stdout içindeki Markdown Tablolarını Yakala
    # Format: | ... | ... |
    # Satır bazlı tablo tespiti
    lines = stdout.split("\n")
    table_blocks = []
    current_table = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            current_table.append(line)
        elif "Table:" in line and ("|" in line or "---" in line):
            current_table.append(line)
        else:
            if len(current_table) >= 2: # Başlık + Ayraç en az 2 satır
                table_blocks.append("\n".join(current_table))
            current_table = []
            
    if len(current_table) >= 2:
        table_blocks.append("\n".join(current_table))

    saved_tables = []
    for idx, tbl_str in enumerate(table_blocks, 1):
        tbl_file = outputs_dir / f"Table_{idx}.md"
        with open(tbl_file, "w", encoding="utf-8") as f:
            f.write(f"<!-- Table {idx} Generated Automatically by R Executor -->\n")
            f.write(tbl_str.strip() + "\n")
        saved_tables.append(tbl_file.name)
        print(f"  📄 Tablo kaydedildi: {tbl_file.name}")

    # Ayrıca outputs/ altında önceden kaydedilmiş diğer .md tablolarını da topla
    existing_tables = [f.name for f in outputs_dir.glob("Table_*.md")]
    for t in existing_tables:
        if t not in saved_tables:
            saved_tables.append(t)

    # 2. Üretilen Grafikleri Kontrol Et
    png_files = list(outputs_dir.glob("*.png")) + list(outputs_dir.glob("*.svg"))
    saved_figures = [f.name for f in png_files]
    for fig in saved_figures:
        print(f"  🖼️ Grafik hazır: {fig}")

    # 3. Eğer Manuscript Notu Belirtilmişse Notu Güncelle
    if manuscript_path:
        update_manuscript_with_outputs(manuscript_path, saved_tables, saved_figures)

    print(f"✅ R analizi başarıyla tamamlandı!")
    return True

def update_manuscript_with_outputs(manuscript_path, tables, figures):
    """Makale taslağındaki 'Bulgular ve Tablolar' bölümüne çıktıları iliştirir"""
    manu_p = Path(manuscript_path).resolve()
    if not manu_p.exists():
        return

    with open(manu_p, "r", encoding="utf-8") as f:
        content = f.read()

    embeds = []
    if tables:
        embeds.append("### 📊 İstatistiksel Tablolar")
        for t in tables:
            embeds.append(f"![[{t}]]")
    if figures:
        embeds.append("### 📈 Grafikler & Görselleştirmeler")
        for fig in figures:
            embeds.append(f"![[{fig}]]")

    embed_block = "\n" + "\n".join(embeds) + "\n"

    # '## 3. Bulgular ve Tablolar' altına yerleştir
    if "## 3. Bulgular ve Tablolar" in content:
        # Eğer zaten eklenmemişse ekle
        if any(f"![[{t}]]" in content for t in tables) or any(f"![[{fig}]]" in content for fig in figures):
            print("  ℹ️ Not zaten güncel çıktı bağlantılarını içeriyor.")
            return
            
        new_content = re.sub(
            r"(## 3\. Bulgular ve Tablolar.*?\n)",
            r"\1" + embed_block + "\n",
            content
        )
        with open(manu_p, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  📝 Makale taslağı güncellendi: {manu_p.name}")

def execute_r_code(code_string, project_dir, manuscript_path=None, script_name="analysis.R"):
    """Doğrudan metin olarak verilen R kodunu kaydedip yürütür"""
    p_dir = Path(project_dir).resolve()
    scripts_dir = p_dir / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    
    script_file = scripts_dir / script_name
    with open(script_file, "w", encoding="utf-8") as f:
        f.write(code_string)
        
    return run_r_script(script_file, project_dir=p_dir, manuscript_path=manuscript_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Yerel R & Quarto Yürütücüsü")
    parser.add_argument("--script", "-s", help="Çalıştırılacak .R veya .qmd dosya yolu")
    parser.add_argument("--project", "-p", help="Proje klasörü yolu")
    parser.add_argument("--manuscript", "-m", help="Güncellenecek Obsidian makale notu (.md)")
    parser.add_argument("--code", "-c", help="Doğrudan R kodu metni")
    
    args = parser.parse_args()
    
    if args.script:
        run_r_script(args.script, project_dir=args.project, manuscript_path=args.manuscript)
    elif args.code and args.project:
        execute_r_code(args.code, project_dir=args.project, manuscript_path=args.manuscript)
    else:
        print("Kullanım: python3 scripts/r_executor.py --script Manuscripts/Proje1/scripts/analysis.R --manuscript Manuscripts/Proje1/manuscript.md")
