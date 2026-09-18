#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📖 Düzenlenebilir Veri Sözlüğü Motoru (Editable Data Dictionary Engine)
Dr. Caner Özyıldırım Akademik Vault Altyapısı

Özellikler:
1. .sav, .xlsx, .xls, .csv, .tsv, .omv, .jasp dosyalarını tarar.
2. Belirtilen şemada 'data_dictionary.md' üretir.
3. KULLANICI DÜZENLEMELERİNİ KORUR (Preserve Edits): Kullanıcı Clean_Label, New_Name veya Role alanlarını değiştirdiyse bunları ezmez.
"""

import os
import sys
import re
import json
import glob
import zipfile
import tempfile
import subprocess
from pathlib import Path

def to_snake_case(s):
    """Sütun adını temiz R değişken adına (snake_case) çevirir"""
    s = s.strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s-]+", "_", s)
    # Türkçe karakter normalizasyonu
    tr_map = str.maketrans("ıİğĞüÜşŞöÖçÇ", "iIgGuUsSoOcC")
    s = s.translate(tr_map)
    s = s.lower().strip("_")
    return s if s else "var"

def guess_clean_label(col_name, spss_label=""):
    """Sütun adından veya SPSS etiketinden şık bir yayın etiketi önerir"""
    if spss_label and len(spss_label.strip()) > 0:
        return spss_label.strip()
    # Kelimeleri ayır ve baş harflerini büyüt
    words = re.split(r"[_\s\-]+", col_name)
    clean_words = [w.capitalize() for w in words if w]
    return " ".join(clean_words)

def guess_role(col_name):
    """Sütun adından muhtemel rol tahmin eder (id, outcome, predictor, covariate)"""
    name_l = col_name.lower()
    if any(k in name_l for k in ["id", "no", "hasta_no", "patient", "subject"]):
        return "id"
    elif any(k in name_l for k in ["outcome", "sonuc", "hba1c", "death", "mortality", "remission"]):
        return "outcome"
    elif any(k in name_l for k in ["grup", "group", "treatment", "tedavi", "diet", "diyet", "arm"]):
        return "predictor"
    else:
        return "covariate"

def parse_existing_dictionary(dict_path):
    """Mevcut data_dictionary.md dosyasını okuyup kullanıcının düzenlemelerini çeker"""
    if not os.path.exists(dict_path):
        return {}

    with open(dict_path, "r", encoding="utf-8") as f:
        content = f.read()

    edits = {}
    lines = content.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|") and not stripped.startswith("| :---"):
            parts = [p.strip() for p in stripped.split("|")[1:-1]]
            if len(parts) >= 7 and parts[0] != "Original_Column":
                orig_col = parts[0].replace("`", "").strip()
                new_name = parts[1].replace("`", "").strip()
                clean_label = parts[2].strip()
                role = parts[6].strip()
                edits[orig_col] = {
                    "New_Name": new_name,
                    "Clean_Label": clean_label,
                    "Role": role
                }
    return edits

R_INSPECTOR_CODE = """
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
  cat(jsonlite::toJSON(list(error = "Desteklenmeyen dosya")), "\\n")
  quit(status = 1)
}

n_rows <- nrow(df)
n_cols <- ncol(df)

columns_info <- list()

for (col_name in names(df)) {
  col_data <- df[[col_name]]
  col_label <- attr(col_data, "label")
  if (is.null(col_label)) col_label <- ""
  
  na_count <- sum(is.na(col_data))
  
  # Tip belirleme
  val_labels <- attr(col_data, "labels")
  is_lbl <- !is.null(val_labels)
  
  col_type <- "continuous"
  range_or_levels <- ""
  
  if (is_lbl) {
    col_type <- "factor"
    range_or_levels <- paste(paste(val_labels, names(val_labels), sep="="), collapse=", ")
  } else if (is.factor(col_data) || is.character(col_data)) {
    col_type <- "factor"
    uniq <- unique(na.omit(col_data))
    if (length(uniq) <= 10) {
      range_or_levels <- paste(uniq, collapse=", ")
    } else {
      range_or_levels <- paste0(length(uniq), " benzersiz kategori")
    }
  } else if (is.integer(col_data) || all(na.omit(col_data) == floor(na.omit(col_data)))) {
    clean_num <- na.omit(col_data)
    if (length(clean_num) > 0) {
      min_v <- min(clean_num)
      max_v <- max(clean_num)
      if (length(unique(clean_num)) <= 5 && min_v >= 0 && max_v <= 10) {
        col_type <- "factor"
        range_or_levels <- paste(sort(unique(clean_num)), collapse=", ")
      } else {
        col_type <- "integer"
        range_or_levels <- paste0("Min: ", min_v, ", Max: ", max_v)
      }
    }
  } else if (is.numeric(col_data)) {
    col_type <- "continuous"
    clean_num <- na.omit(col_data)
    if (length(clean_num) > 0) {
      range_or_levels <- paste0("Min: ", round(min(clean_num), 2), ", Max: ", round(max(clean_num), 2))
    }
  }
  
  columns_info[[col_name]] <- list(
    name = col_name,
    label = col_label,
    type = col_type,
    missing_n = na_count,
    range_or_levels = range_or_levels
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
    temp_dir = tempfile.mkdtemp(prefix="data_inspector_")
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    candidates = glob.glob(f"{temp_dir}/**/*.csv", recursive=True) + \
                 glob.glob(f"{temp_dir}/**/*.tsv", recursive=True)
    if candidates:
        return candidates[0], temp_dir
    return None, temp_dir

def build_data_dictionary(file_path, output_dir=None):
    """Veri dosyasını analiz eder ve kullanıcı düzenlemelerini koruyarak data_dictionary.md oluşturur"""
    path = Path(file_path).resolve()
    if not path.exists():
        print(f"❌ Dosya bulunamadı: {path}")
        return None

    out_folder = Path(output_dir).resolve() if output_dir else path.parent
    dict_path = out_folder / "data_dictionary.md"
    existing_edits = parse_existing_dictionary(dict_path)

    ext = path.suffix.lower()
    target_path = str(path)
    if ext in ['.omv', '.jasp']:
        extracted, temp_dir = extract_jamovi_jasp(target_path)
        if extracted:
            target_path = extracted
        else:
            print(f"⚠️ {ext} arşivinden veri tablosu açılamadı.")
            return None

    r_script = tempfile.mktemp(suffix=".R")
    with open(r_script, "w", encoding="utf-8") as f:
        f.write(R_INSPECTOR_CODE)

    try:
        proc = subprocess.run(["Rscript", r_script, target_path], capture_output=True, text=True, check=True)
        data = json.loads(proc.stdout.strip())
    except Exception as e:
        print(f"❌ Veri analizi hatası: {e}")
        return None
    finally:
        if os.path.exists(r_script):
            os.remove(r_script)

    # Markdown Tablosunu Oluştur
    md_lines = []
    md_lines.append("# 📖 Veri Sözlüğü (Data Dictionary)")
    md_lines.append("")
    md_lines.append("> [!tip] Düzenleme Kuralı")
    md_lines.append("> `Clean_Label` alanını grafiklerde/tablolarda görünmesini istediğiniz şık isimle değiştirin. `New_Name` alanına temiz bir R değişken adı yazabilirsiniz. `Role` kısmına (predictor, outcome, covariate, id) belirtebilirsiniz.")
    md_lines.append("")
    md_lines.append("| Original_Column | New_Name | Clean_Label | Type | Missing_N | Factor_Levels / Range | Role |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

    cols = data.get("columns", {})
    preserved_count = 0

    for col_name, col in cols.items():
        # Varsayılanlar
        default_new_name = to_snake_case(col_name)
        default_clean_label = guess_clean_label(col_name, col.get("label", ""))
        default_role = guess_role(col_name)

        # Kullanıcı düzenlemesi varsa koru
        if col_name in existing_edits:
            user_edit = existing_edits[col_name]
            new_name = user_edit.get("New_Name") or default_new_name
            clean_label = user_edit.get("Clean_Label") or default_clean_label
            role = user_edit.get("Role") or default_role
            preserved_count += 1
        else:
            new_name = default_new_name
            clean_label = default_clean_label
            role = default_role

        v_type = col.get("type", "continuous")
        missing_n = col.get("missing_n", 0)
        range_levels = col.get("range_or_levels", "-").replace("|", "/")

        md_lines.append(f"| `{col_name}` | `{new_name}` | {clean_label} | {v_type} | {missing_n} | {range_levels} | {role} |")

    md_lines.append("")
    
    with open(dict_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")

    if preserved_count > 0:
        print(f"✅ {dict_path.name} güncellendi ({preserved_count} kullanıcı düzenlemesi korundu) -> {dict_path}")
    else:
        print(f"✅ Yeni veri sözlüğü oluşturuldu: {dict_path}")
        
    return dict_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            build_data_dictionary(target)
        elif os.path.isdir(target):
            for ext in ["*.sav", "*.xlsx", "*.xls", "*.csv", "*.omv", "*.jasp"]:
                for f in glob.glob(f"{target}/**/{ext}", recursive=True):
                    build_data_dictionary(f)
    else:
        for ext in ["*.sav", "*.xlsx", "*.xls", "*.csv", "*.omv", "*.jasp"]:
            for f in glob.glob(f"Manuscripts/**/{ext}", recursive=True):
                build_data_dictionary(f)
