```dataview
TABLE 
    PDF_Adi as "Dosya Adı",
    Dosya_No as "Dosya No",
    Marka_Sahis as "Marka/Şahıs",
    Mecra as "Mecra",
    Konu as "Konu",
    Ihlal_Detayi as "İhlal Detayı",
    Ceza as "Verilen Ceza"
FROM "Reklam Kurulu Kararları"
WHERE file.name != this.file.name
SORT Dosya_No DESC
```