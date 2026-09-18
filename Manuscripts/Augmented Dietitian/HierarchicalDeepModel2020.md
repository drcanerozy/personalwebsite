---
Title: "A Hierarchical deep model for food classification from photographs"
Authors: ""
Year: 2020
DOI: "10.3837/tiis.2020.04.016"
Nitelik: 
Alan: 
Konu: 
AI_Methodology: 
Layer_Focus: 
Model_Asamasi: 
Proposed_Tool: 
Methods: "scale. We build a hierarchical structure composed of deep CNN to recognize and classify food from photographs We build a dataset for Korean food of 18 classes, which are further categorized in 4 major classes. Our hierarchical recognizer classifies foods into four major classes in the first step. Each food in the major classes is further classified into the exact class in the second step. We employ DenseNet structure for the baseline of our recognizerTo train our classifier, we collected the images of our target Korean foods from various internet sites. In total, we collect 6452 images, which means that the images for each food are about 358 in average. Among the collected images, we assign 70% of them for training, 15% for validation and 15% for test. The exact amounts of the collected images are suggested in Table. 1. We train our classifier for 100 epochs. We set dropout rate as 70% and learning rate as 0.0001."
Findings: "Our recognizer, whose baseline is constructed using DenseNet, classifies Korean food in two stages: the first stage classifies food into 4 major classes, which are rice, soup, main dish and side dish, and the second stage classifies the foods in the major class into the exact class. This hierarchical structure improves the accuracy of the recognition than the conventional single-layer structured recognizer."
Conclusions: "The hierarchical structure provides higher accuracy and F1 score than those from the single-structured recognizer."
Limitations: "The success of a hierarchical classifier depends on the accuracy of the first layer. The final accuracy is a multiplication of the accuracies of the first layer and the second layer. Therefore, the final accuracy may be lower than the single layer classifier even though the second layer shows better accuracy than the single layer classifier. Fortunately, the accuracy of the first layer that classifies Korean food into four major categories is close to 1.0. In other cases where the first layer does not show very high accuracy, a hierarchical structured classifier may show worse accuracy than a single layer classifier"
User_Notes: ""
---

# A Hierarchical deep model for food classification from photographs
**Yazarlar:**  | **Yıl:** 2020
**DOI:** 10.3837/tiis.2020.04.016 | **Zotero:** [Görüntüle](zotero://select/library/items/DRIEYAFP)

---

## 📝 Benim Notlarım


## 🟡 Genel Bilgiler (Sarı)
- "Finally, some other areas such as dietetics can incorporate with our recognizer to build various applications very effective on many users." ([Sayfa 14](zotero://open-pdf/library/items/UDW9R6Z4?page=14&annotation=2ZDXEW3S))

## 🟢 Yöntem & Örneklem (Yeşil)
- "scale. We build a hierarchical structure composed of deep CNN to recognize and classify food from photographs We build a dataset for Korean food of 18 classes, which are further categorized in 4 major classes. Our hierarchical recognizer classifies foods into four major classes in the first step. Each food in the major classes is further classified into the exact class in the second step. We employ DenseNet structure for the baseline of our recognizer" ([Sayfa 1](zotero://open-pdf/library/items/UDW9R6Z4?page=1&annotation=SBCKHMJJ))- "To train our classifier, we collected the images of our target Korean foods from various internet sites. In total, we collect 6452 images, which means that the images for each food are about 358 in average. Among the collected images, we assign 70% of them for training, 15% for validation and 15% for test. The exact amounts of the collected images are suggested in Table. 1. We train our classifier for 100 epochs. We set dropout rate as 70% and learning rate as 0.0001." ([Sayfa 8](zotero://open-pdf/library/items/UDW9R6Z4?page=8&annotation=F6D7D8GI))

## 🔴 Bulgular (Kırmızı)
- "Our recognizer, whose baseline is constructed using DenseNet, classifies Korean food in two stages: the first stage classifies food into 4 major classes, which are rice, soup, main dish and side dish, and the second stage classifies the foods in the major class into the exact class. This hierarchical structure improves the accuracy of the recognition than the conventional single-layer structured recognizer." ([Sayfa 14](zotero://open-pdf/library/items/UDW9R6Z4?page=14&annotation=NC9GS485))

## 🔵 Sonuç / Conclusions (Mavi)
- "The hierarchical structure provides higher accuracy and F1 score than those from the single-structured recognizer." ([Sayfa 1](zotero://open-pdf/library/items/UDW9R6Z4?page=1&annotation=DCXC2HAC))

## 🟠 Limitasyonlar (Turuncu)
- "The success of a hierarchical classifier depends on the accuracy of the first layer. The final accuracy is a multiplication of the accuracies of the first layer and the second layer. Therefore, the final accuracy may be lower than the single layer classifier even though the second layer shows better accuracy than the single layer classifier. Fortunately, the accuracy of the first layer that classifies Korean food into four major categories is close to 1.0. In other cases where the first layer does not show very high accuracy, a hierarchical structured classifier may show worse accuracy than a single layer classifier" ([Sayfa 11](zotero://open-pdf/library/items/UDW9R6Z4?page=11&annotation=B78NQAAU))