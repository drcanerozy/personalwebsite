```dataview
TABLE 
Title as "Başlık",
Authors as "Yazarlar", 
Year as "Yıl", 
Nitelik as "Nitelik", 
Alan as "Alan", 
AI_Methodology as "Algoritma/Teknik", 
Layer_Focus as "Odak Katman", 
Model_Asamasi as "Augmented Aşama", 
User_Notes as "Özel Notlarım", 
Methods as "Yöntem", 
Findings as "Bulgular", 
Conclusions as "Sonuç", 
Limitations as "Sınırlılıklar", 
DOI 
FROM "Augmented Dietitian" 
WHERE file.name != this.file.name 
SORT Year DESC
```
