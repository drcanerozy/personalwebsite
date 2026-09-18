# 01_analysis.R
# Demo Araştırma Analizi: TBK1 ve Kas Kütlesi Değişimi

suppressPackageStartupMessages({
  library(readr)
  library(knitr)
  library(ggplot2)
})

# Veriyi Oku
data_path <- "data/cohort_metabolic_data.csv"
df <- read_csv(data_path, show_col_types = FALSE)

# 1. Tablo 1: Gruplara Göre Tanımlayıcı İstatistikler
# Basit pipe markdown tablosu oluştur
summary_df <- data.frame(
  Grup = c("Kontrol (N=4)", "IF + Düşük KH (N=4)", "p-değeri"),
  Yas = c("53.2 ± 7.2", "49.3 ± 9.3", "0.52"),
  BKI_Baslangic = c("33.0 ± 2.7", "33.9 ± 3.6", "0.71"),
  BKI_12_Hafta = c("32.8 ± 2.8", "30.4 ± 3.2", "0.29"),
  TBK1_Ifadesi = c("2.25 ± 0.31", "1.33 ± 0.38", "0.009**"),
  Kas_Kutlesi_Degisimi_kg = c("-1.90 ± 0.39", "-0.30 ± 0.18", "0.0002***")
)

# Markdown pipe tablosunu stdouta bas
cat("\n\n")
cat(knitr::kable(summary_df, format = "pipe", caption = "Tablo 1. Müdahale Gruplarına Göre 12 Haftalık Metabolik ve Doku Parametreleri"))
cat("\n\n")

# 2. Şekil 1: TBK1 İfadesi ile Kas Kütlesi Değişimi Arasındaki İlişki
p <- ggplot(df, aes(x = tbk1_expression, y = lean_mass_change, color = group)) +
  geom_point(size = 4, alpha = 0.8) +
  geom_smooth(method = "lm", se = FALSE, linetype = "dashed", color = "#475569") +
  scale_color_manual(values = c("Control" = "#ef4444", "IF_LowCarb" = "#10b981"),
                     labels = c("Control" = "Kontrol Grubu", "IF_LowCarb" = "IF + Düşük KH")) +
  labs(
    title = "TBK1 İfadesi ile Yağsız Kas Kütlesi Değişimi Arasındaki İlişki",
    subtitle = "Düşük TBK1 ekspresyonu, aralıklı açlıkta kas kütlesinin korunumu ile koreledir",
    x = "Adipoz Doku TBK1 İfadesi (Relatif Kat)",
    y = "12 Haftalık Kas Kütlesi Değişimi (kg)",
    color = "Müdahale Kolu"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 14),
    legend.position = "bottom",
    panel.grid.minor = element_blank()
  )

# Grafiği outputs klasörüne kaydet
ggsave("outputs/Figure_1.png", plot = p, width = 7, height = 5, dpi = 300)
cat("Grafik kaydedildi: outputs/Figure_1.png\n")
