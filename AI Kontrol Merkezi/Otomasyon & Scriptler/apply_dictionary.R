# scripts/apply_dictionary.R
# ════════════════════════════════════════════════════════════════════════════════
# 🌉 R Veri Hazırlama ve Sözlük Etiketleme Köprüsü (R Dictionary Labeling Bridge)
# Dr. Caner Özyıldırım Akademik Vault Altyapısı
# ════════════════════════════════════════════════════════════════════════════════

suppressPackageStartupMessages({
  library(haven)
  library(readxl)
  library(readr)
  library(labelled)
  library(dplyr)
})

#' Markdown Tablosunu R Data Frame'e Dönüştürür
parse_markdown_dictionary <- function(dict_path) {
  if (!file.exists(dict_path)) {
    stop(paste("❌ Sözlük dosyası bulunamadı:", dict_path))
  }
  
  lines <- readLines(dict_path, warn = FALSE, encoding = "UTF-8")
  table_lines <- lines[grepl("^\\|", lines)]
  
  # Başlık ve ayraç satırını ayıkla
  if (length(table_lines) < 3) {
    stop("❌ data_dictionary.md içinde geçerli bir Markdown tablosu bulunamadı.")
  }
  
  # Ayraç satırını filtrele (| :--- |)
  data_lines <- table_lines[!grepl("^\\|\\s*:?-+", table_lines)]
  
  # Header
  header <- strsplit(gsub("^\\||\\|$", "", data_lines[1]), "\\|")[[1]]
  header <- trimws(header)
  
  rows <- list()
  for (i in 2:length(data_lines)) {
    parts <- strsplit(gsub("^\\||\\|$", "", data_lines[i]), "\\|")[[1]]
    parts <- trimws(parts)
    if (length(parts) >= length(header)) {
      row_data <- parts[1:length(header)]
      # Kod formatlarını temizle (` `)
      row_data <- gsub("`", "", row_data)
      row_data <- gsub("\\*\\*", "", row_data)
      rows[[length(rows) + 1]] <- row_data
    }
  }
  
  df_dict <- as.data.frame(do.call(rbind, rows), stringsAsFactors = FALSE)
  colnames(df_dict) <- header
  return(df_dict)
}

#' Ham Veriyi Okur, Sözlükteki Yeni İsimleri ve Clean_Label'ları Uygular
#' @param data_path Ham veri dosyası yolu (.sav, .xlsx, .csv vb.)
#' @param dict_path data_dictionary.md dosya yolu (Varsayılan: aynı klasördeki data_dictionary.md)
#' @return Temizlenmiş, etiketlenmiş tibble / data.frame
load_clean_data <- function(data_path, dict_path = NULL) {
  if (is.null(dict_path)) {
    dict_path <- file.path(dirname(data_path), "data_dictionary.md")
  }
  
  # 1. Sözlüğü Oku
  dict <- parse_markdown_dictionary(dict_path)
  
  # 2. Ham Veriyi Oku
  ext <- tolower(tools::file_ext(data_path))
  raw_df <- NULL
  
  if (ext == "sav") {
    raw_df <- haven::read_sav(data_path)
  } else if (ext %in% c("xlsx", "xls")) {
    raw_df <- readxl::read_excel(data_path)
  } else if (ext %in% c("csv", "tsv", "txt")) {
    raw_df <- readr::read_delim(data_path, show_col_types = FALSE)
  } else {
    stop(paste("Desteklenmeyen dosya formatı:", ext))
  }
  
  df <- raw_df
  
  # 3. İsimleri ve Etiketleri Uygula
  for (i in 1:nrow(dict)) {
    orig_col <- trimws(dict$Original_Column[i])
    new_name <- trimws(dict$New_Name[i])
    clean_lbl <- trimws(dict$Clean_Label[i])
    col_type  <- tolower(trimws(dict$Type[i]))
    col_role  <- trimws(dict$Role[i])
    
    if (orig_col %in% colnames(df)) {
      # İsim değiştir
      if (orig_col != new_name && nchar(new_name) > 0) {
        colnames(df)[colnames(df) == orig_col] <- new_name
      }
      
      target_col <- if (nchar(new_name) > 0) new_name else orig_col
      
      # Etiket uygula (gtsummary ve ggplot2 için)
      if (nchar(clean_lbl) > 0) {
        attr(df[[target_col]], "label") <- clean_lbl
        labelled::var_label(df[[target_col]]) <- clean_lbl
      }
      
      # Rol uygula
      if (nchar(col_role) > 0) {
        attr(df[[target_col]], "role") <- col_role
      }
      
      # Tip dönüşümü (isteğe bağlı)
      if (col_type == "factor" && !is.factor(df[[target_col]])) {
        df[[target_col]] <- as.factor(df[[target_col]])
      }
    }
  }
  
  cat(paste0("✅ Veri sözlüğü başarıyla uygulandı: ", ncol(df), " sütun etiketlendi.\n"))
  return(df)
}
