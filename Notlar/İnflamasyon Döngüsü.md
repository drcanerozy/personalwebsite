---
Tür:
  - Besleyici
ODAK:
  - "[[inflamasyon]]"
MEKANİZMA:
DİZİN:
  - "[[İmmün Sistem]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[İnflamasyonun Tanınması-DAMP]]"
  - "[[İmmün Yanıt ve İnflamasyon Döngüsü]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[İmmün Sistem ve İmmünonutrisyon]]"
YORUM:
KAYNAK: https://www.nature.com/articles/s44385-025-00010-4
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Metabolik ve Moleküler Yanıtlar"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[İmmün Yanıt ve İnflamasyon Döngüsü]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph TD
>     A["Doku Hasarı / Patojen / DAMP
ATP, HMGB1, eCIRP, cfDNA"] --> B["Nötrofil Toplanması & Aktivasyonu
PRR: TLR, NLR"]
>     B --> C["M1 Makrofaj Polarizasyonu
TNF-α, IL-1β, IL-6, MMP ↑"]
>     C --> D["Ek Doku Hasarı
ROS, Proteaz, NET"]
>     D --> A
>     E["Apoptotik Hücre
Fosfatidilserin Açığa Çıkması — 'Eat-me' Sinyali"] -->|"Sağlıklı Çözüm"| F["Eferositozis → M2 Polarizasyonu
TGF-β, IL-10 ↑"]
>     F --> G["İnflamasyon Çözümü
Doku Rejenerasyonu"]
>     H["Obezite / Inflammaging
ROS → PS Reseptör Hasarı"] -->|"Eferositozis Bozulması"| I["Kronik Nötrofil / M1 Yükü ↑"]
>     I --> C
>     C -.->|"Kısır Döngü"| D
> ```
>
> **Şekil Açıklaması:** İnflamasyon döngüsü, doku hasarı → nötrofil/M1 makrofaj aktivasyonu → daha fazla hasar döngüsüyle sürer; sağlıklı çözüm için PS-eferositozis ekseninin M2 polarizasyonunu tetiklemesi gerekir. Obezite ve inflammaging, ROS aracılı PS reseptör hasarıyla bu çözüm kapısını kapatarak kronik inflamasyonu perpetüe eder.

- Macrophage response to apoptotic cell engulfment is mediated by several receptors on the macrophage that can bind to a variety of apoptotic surface markers to facilitate recognition, uptake, and signaling. Exposure of the phospholipid phosphatidylserine (PS) onto the outer surface of the cell membrane is the most well-characterized apoptotic cell signal16,17. In most living cells, PS is confined to the inside of the cell by a flippase, a lipid transporter protein that moves certain lipids from the outer leaflet to the inner leaflet, producing anisotropic layers18. When that cell undergoes apoptosis, it loses its cell membrane anisotropy, exposing PS on its outer membrane. The exposure of PS acts as an “eat-me” signal to phagocytes, including macrophages, to engulf the dying cell18. This engulfment initiates a shift in macrophage polarization toward a pro-resolving phenotype, which reduces inflammation, stops additional damage to the tissue, and begins tissue regeneration19 (s. )
- Macrophages display significant plasticity to promote both inflammation and resolution based on extracellular signals20. In a healthy healing response, these cues can lead to the production of immunosuppressive cytokines, including TGF-β and IL-10 to restore homeostasis following an initial inflammatory phase; however, without a signal to polarize, or with continued stimulation by antigen, inflammation continues indefinitely in chronic inflammatory diseases21. In chronic or dysregulated inflammatory conditions, elevated numbers of neutrophils, monocytes, and macrophages persist22–24. Neutrophils persist abnormally, releasing excessive proteases, reactive oxygen species (ROS), and neutrophil extracellular traps (NETs), which damage tissue and sustain inflammation, while macrophages are skewed toward a pro-inflammatory (M1) state, failing to transition to a reparative (M2) phenotype. This imbalance perpetuates inflammation, (s. )
- delays healing in chronic conditions like non-healing diabetic wounds.  Macrophage persistence at sites of inflammation can be associated with disease severity and progression, such as in rheumatoid arthritis25–28. Proinflammatory immune cells overproduce matrix metalloproteinases (MMPs), ROS, and inflammatory cytokines, leading to increased tissue damage. Additional pro-inflammatory macrophage polarization occurs with further upregulated secretion of inflammatory cytokines, including TNF-α, IL-1β, and IL-629. Similar outcomes from increased macrophage infiltration and activation can be seen across a variety of inflammatory diseases and organ systems29–32. In contrast, normal healing is associated with the programmed death and clearance of neutrophils, which initiates an anti-inflammatory cascade in the tissue33. (s. 2)
- 1). DAMPs released from dead and dying cells serve to signal downstream inflammatory mediators, including macrophages to recruit to sites of injury and enhance the inflammatory cascade40,41. Canonical DAMPs include ATP, high mobility group box 1 (HMGB1), extracellular cold-inducible RNA-binding protein (eCIRP), histones, heat shock proteins (HSPs), extracellular RNAs (exRNAs), and cell-free DNA (cfDNA).  DAMPs are also released passively via cell necrosis, that is exemplified by loss of cell membrane integrity. The packaging and identity of DAMPs released from programmed death mechanisms versus necrosis differ.  Apoptosing neutrophils can secrete DAMPs via lysosomes, via release exosomal and ectosomal vesicles, apoptotic bodies, and via extracellular traps42. (s. 2)
- As humans age, the accumulation of effects from repeated or low-grade infection, chronic inflammatory disease, obesity, and environmental factors leads to changes in the number and function of myeloid cells.  This set of changes is one component of “inflammaging” - the accumulation of defects in the immune system associated with aging that lead to a persistent, low grade inflammatory state56. Neutrophils in particular show a reduced ability to phagocytose infectious bacteria and a reduced microbiocidal ability in aged individuals. The cells’ ability to conduct immune surveillance is impaired due to a decreased sensitivity to antiapoptotic factors. Neutrophils in the elderly have a greater likelihood to undergo apoptosis without triggering inflammation. Advanced age can therefore predispose an individual to harmful infections and reduce the responsiveness to vaccines. Conversely, the low-grade inflammation that results during inflammaging is characterized by higher levels of proinflammatory cytokines such as IL-6, TNF-α, and C-reactive protein, and the accumulation of DAMPs57. Under these conditions, neutrophils can contribute to telomere shortening and the production of ROS, thus adding to oxidative stress and cellular aging. The clearance of dead and dying neutrophils is similarly perturbed. For example, ROS can cleave PS receptors on macrophages and reduce their efferocytosis ability58. The reduction in efficient clearance of apoptotic neutrophils and the limitation on anti-inflammatory and tolerizing effects on macrophages may exacerbate the cycle of aging and inflammation. (s. 3)

