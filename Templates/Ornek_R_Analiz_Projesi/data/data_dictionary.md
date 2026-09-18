# 📖 Veri Sözlüğü (Data Dictionary)

> [!tip] Düzenleme Kuralı
> `Clean_Label` alanını grafiklerde/tablolarda görünmesini istediğiniz şık isimle değiştirin. `New_Name` alanına temiz bir R değişken adı yazabilirsiniz. `Role` kısmına (predictor, outcome, covariate, id) belirtebilirsiniz.

| Original_Column | New_Name | Clean_Label | Type | Missing_N | Factor_Levels / Range | Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `patient_id` | `patient_id` | Patient Id | factor | 0 | P001, P002, P003, P004, P005, P006, P007, P008 | id |
| `group` | `group` | Group | factor | 0 | IF_LowCarb, Control | predictor |
| `age` | `age` | Age | integer | 0 | Min: 39, Max: 61 | covariate |
| `bmi_baseline` | `bmi_baseline` | **Baseline BMI (kg/m²)** | continuous | 0 | Min: 29.8, Max: 38.2 | covariate |
| `bmi_12week` | `bmi_12week` | **12-Week BMI (kg/m²)** | continuous | 0 | Min: 26.5, Max: 36.1 | covariate |
| `fasting_glucose` | `fasting_glucose` | **Fasting Glucose (mg/dL)** | integer | 0 | Min: 92, Max: 122 | covariate |
| `hba1c` | `hba1c` | **HbA1c (%)** | continuous | 0 | Min: 5.2, Max: 6.3 | outcome |
| `tbk1_expression` | `tbk1_expression` | **Adipose TBK1 Expression (Fold)** | continuous | 0 | Min: 0.9, Max: 2.6 | predictor |
| `lean_mass_change` | `lean_mass_change` | **12-Week Lean Mass Change (kg)** | continuous | 0 | Min: -2.3, Max: -0.1 | outcome |

