#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 Evrensel Veri Okuyucu ve Veri Sözlüğü Motoru (Universal Data Inspector)
Dr. Caner Özyıldırım Akademik Vault Altyapısı

Desteklenen Formatlar:
- .sav (SPSS) via haven
- .xlsx / .xls (Excel) via readxl
- .csv / .tsv (Metin) via readr
- .omv (Jamovi) via ZIP extraction
- .jasp (JASP) via ZIP extraction
"""

import os
import sys
import json
import glob
import zipfile
import tempfile
import subprocess
from pathlib import Path

# R Script Şablonu (haven, readxl, readr ile derin analiz)
R_ANALYZER_TEMPLATE = """
suppressPackageStartupMessages({
  library(haven)
  library(readxl)
  library(readr)
})

args <- commandArgs(trailingOnly = TRUE)
file_path <- args[1]
ext <- tolower(tools::file_ext(file_path))

df <- NULL
if (ext == "sav") {
  df <- haven::read_sav(file_path)
} else if (ext %in% c("xlsx", "xls")) {
  df <- readxl::read_excel(file_path)
} else if (ext %in% c("csv", "tsv", "txt")) {
  df <- readr::read_delim(file_path, show_col_types = FALSE)
}

if (is.null(df)) {
  cat(jsonlite::toJSON(list(error = "Desteklenmeyen dosya formati")), "\\n")
  quit(status = 1)
}

n_rows <- nrow(df)
n_cols <- ncol(df)

columns_info <- list()

for (col_name in names(df)) {
  col_data <- df[[col_name]]
  col_label <- attr(col_data, "label")
  if (is.null(col_label)) col_label <- ""
  
  col_type <- class(col_data)[1]
  na_count <- sum(is.na(col_data))
  na_pct <- round((na_count / n_rows) * 100, 2)
  
  levels_str <- ""
  summary_str <- ""
  
  # SPSS Değer Etiketleri veya Faktörler
  val_labels <- attr(col_data, "labels")
  if (!is.null(val_labels)) {
    levels_str <- paste(paste(val_labels, names(val_labels), sep="="), collapse=", ")
    col_type <- "labelled / factor"
  } else if (is.factor(col_data) || is.character(col_data)) {
    uniq <- unique(na.omit(col_data))
    if (length(uniq) <= 10) {
      levels_str <- paste(uniq, collapse=", ")
    } else {
      levels_str <- paste0(length(uniq), " benzersiz kategori")
    }
  }
  
  # Sayısal Değişken İstatistikleri
  if (is.numeric(col_data)) {
    clean_num <- na.omit(col_data)
    if (length(clean_num) > 0) {
      m <- round(mean(clean_num), 2)
      s <- round(sd(clean_num), 2)
      med <- round(median(clean_num), 2)
      min_v <- round(min(clean_num), 2)
      max_v <- round(max(clean_num), 2)
      summary_str <- paste0("Ort: ", m, " ± ", s, " | Med: ", med, " [", min_v, "-", max_v, "]")
    }
  } else {
    # Kategorik frekans özeti
    tbl <- sort(table(col_data), decreasing = TRUE)
    top_tbl <- head(tbl, 3)
    summary_str <- paste(paste0(names(top_tbl), ": ", top_tbl), collapse=", ")
  }
  
  columns_info[[col_name]] <- list(
    name = col_name,
    label = col_label,
    type = col_type,
    na_count = na_count,
    na_pct = na_pct,
    levels = levels_str,
    summary = summary_str
  )
}

result <- list(
    file_name = basename(file_path),
    n_rows = n_rows,
    n_cols = n_cols,
    columns = columns_info
)

cat(jsonlite::toJSON(result, auto_unbox = TRUE, pretty = TRUE), "\\n")
"""

def extract_jamovi_jasp(archive_path):
    """Jamovi (.omv) ve JASP (.jasp) arşivlerini açıp veri dosyasını bulur"""
    temp_dir = tempfile.mkdtemp(prefix="data_inspector_")
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    # Jamovi / JASP içindeki veri tablosunu ara
    candidates = glob.glob(f"{temp_dir}/**/*.csv", recursive=True) + \
                 glob.glob(f"{temp_dir}/**/*.tsv", recursive=True) + \
                 glob.glob(f"{temp_dir}/**/data.bin", recursive=True) + \
                 glob.glob(f"{temp_dir}/**/data", recursive=True)
                 
    if candidates:
        return candidates[0], temp_dir
    return None, temp_dir

def inspect_dataset(file_path):
    """Belirtilen veri setini analiz eder ve JSON metadata döndürür"""
    path = Path(file_path).resolve()
    if not path.exists():
        print(f"❌ Dosya bulunamadı: {path}")
        return None

    ext = path.suffix.lower()
    temp_dir_to_clean = None
    target_path = str(path)

    # Jamovi / JASP Açma
    if ext in ['.omv', '.jasp']:
        extracted_file, temp_dir_to_clean = extract_jamovi_jasp(target_path)
        if extracted_file:
            target_path = extracted_file
        else:
            print(f"⚠️ {ext} arşivinden veri tablosu çıkarılamadı.")
            return None

    # R Analyzer Scriptini çalıştır
    r_script_path = tempfile.mktemp(suffix=".R")
    with open(r_script_path, "w", encoding="utf-8") as f:
        f.write(R_ANALYZER_TEMPLATE)

    try:
        cmd = ["Rscript", r_script_path, target_path]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        out_json = proc.stdout.strip()
        data = json.loads(out_json)
        data["original_file_name"] = path.name
        return data
    except Exception as e:
        print(f"❌ R analizi sırasında hata oluştu: {e}")
        return None
    finally:
        if os.path.exists(r_script_path):
            os.remove(r_script_path)

def generate_data_dictionary(file_path, output_dir=None):
    """Veri setini okuyup data_dictionary.md oluşturur"""
    path = Path(file_path).resolve()
    data = inspect_dataset(path)
    if not data:
        return None

    out_folder = Path(output_dir).resolve() if output_dir else path.parent
    dict_path = out_folder / "data_dictionary.md"

    md_lines = []
    md_lines.append(f"# 📊 Veri Sözlüğü (Data Dictionary): `{data['original_file_name']}`")
    md_lines.append(f"> **Oluşturulma Tarihi:** {subprocess.getoutput('date')}")
    md_lines.append(f"> **Örneklem Boyutu (N):** `{data['n_rows']}` satır | **Değişken Sayısı (P):** `{data['n_cols']}` sütun")
    md_lines.append("")
    md_lines.append("## 📋 Değişkenler Tablosu")
    md_lines.append("| Değişken Adı | Etiket / Açıklama | Veri Tipi | Eksik Veri (NA) | Faktör Seviyeleri / Kategoriler | Özet İstatistikler |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")

    cols = data.get("columns", {})
    for col_name, col in cols.items():
        label = col.get("label") or "-"
        v_type = col.get("type") or "-"
        na_str = f"{col.get('na_count', 0)} (%{col.get('na_pct', 0)})"
        levels = col.get("levels") or "-"
        summary = col.get("summary") or "-"
        
        # Markdown tablosu için pipe karakterlerini temizle
        label = label.replace("|", "/")
        levels = levels.replace("|", "/")
        summary = summary.replace("|", "/")
        
        md_lines.append(f"| **`{col_name}`** | {label} | `{v_type}` | {na_str} | {levels} | {summary} |")

    md_lines.append("")
    md_lines.append("## 💡 İstatistiksel Modelleme Önerileri")
    
    # Basit otomatik modelleme içgörüsü
    numeric_count = sum(1 for c in cols.values() if "numeric" in str(c.get("type", "")).lower())
    factor_count = sum(1 for c in cols.values() if "factor" in str(c.get("type", "")).lower() or "character" in str(c.get("type", "")).lower())
    
    md_lines.append(f"- **Sayısal Değişkenler ({numeric_count} adet):** Normallik testleri (Shapiro-Wilk) sonrası `gtsummary::tbl_summary(type = all_continuous() ~ 'continuous2')` ile özetlenebilir.")
    md_lines.append(f"- **Kategorik Değişkenler ({factor_count} adet):** Ki-kare veya Fisher Exact testleri için uygundur.")
    md_lines.append("- **Çok Değişkenli Analizler:** GLM, LMM veya Cox Proportional Hazards modelleri kurulabilir.")
    md_lines.append("")

    with open(dict_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"✅ Veri sözlüğü başarıyla oluşturuldu: {dict_path}")
    return dict_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            generate_data_dictionary(target)
        elif os.path.isdir(target):
            for ext in ["*.sav", "*.xlsx", "*.xls", "*.csv", "*.omv", "*.jasp"]:
                for f in glob.glob(f"{target}/**/{ext}", recursive=True):
                    generate_data_dictionary(f)
    else:
        # Otomatik olarak Manuscripts/ altını tara
        for ext in ["*.sav", "*.xlsx", "*.xls", "*.csv", "*.omv", "*.jasp"]:
            for f in glob.glob(f"Manuscripts/**/{ext}", recursive=True):
                generate_data_dictionary(f)
