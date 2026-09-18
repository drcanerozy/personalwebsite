---
Tür:
ODAK:
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type:
evidence_direction:
primary_outcome:
p_value_summary:
---

> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

**İlk adım:** her halükarda seçilen bölgelerin haritalaması gibi olacak galiba. Türkiyenin haritalandırılması 10 numara olay olur. Hatta veri çekmek kolaysa ve dinamik bir hale getirilebilirse yaşayan bir sisteme dönüşebilir veya 2-3 yılda bir güncellenen bir çevre veriseti oluşturulabilir. (Amerikanınki acayip: https://gisportal.ers.usda.gov/portal/apps/experiencebuilder/experience/?id=2cbe6dd56a144568ad667128b7c388b0)
**İkinci adım:** Çevre mi bireysel faktörler mi? Etkiyi ölçebilir miyiz?
1)kötü çevrede yaşayan normal-zayıf bireyler
2)kötü çevrede yaşayan kilolu bireyler
3)iyi çevrede yaşayan zayıf-normal bireyler
4)iyi çevrede yaşayan kilolu bireyler
Bu bireylerin çevreye maruziyetini ve bireysel yeme fakrındalığı düzeyini ölçtükten sonra bunların sağlık-bel çevresi çıktılarına etkisini modellemek. Boylamsal olursa kıymetli. Çok benzerini yapmış makaleler var:

**Seattle Obesity Study (SOS I-III)**

- SOS I (2008-9 kesitsel, n=2001, konut değeri-obezite): Rehm CD, Moudon AV, Hurvitz PM, Drewnowski A. "Residential property values are associated with obesity among women in King County, WA, USA." — [https://pubmed.ncbi.nlm.nih.gov/22591823/](https://pubmed.ncbi.nlm.nih.gov/22591823/)
- SOS ile ilişkili census tract analizi (n=59.767): "The geographic distribution of obesity by census tract among 59,767 insured adults in King County, WA" — [https://pmc.ncbi.nlm.nih.gov/articles/PMC3955743/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955743/)
- ZIP code düzeyinde eşitsizlik analizi: "Disparities in obesity rates: Analysis by ZIP code area" — [https://pmc.ncbi.nlm.nih.gov/articles/PMC2709073/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2709073/)
- Census block görselleştirme yöntemi: "A new method to visualize obesity prevalence in Seattle-King County at the census block level" — [https://pubmed.ncbi.nlm.nih.gov/29479460/](https://pubmed.ncbi.nlm.nih.gov/29479460/)
- SOS II (boylamsal kohort, n=440, davranışsal yol analizi): "Obesity, diet quality, physical activity, and the built environment: the need for behavioral pathways" — [https://pmc.ncbi.nlm.nih.gov/articles/PMC5105275/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5105275/)
- SOS III (2 yıllık BMI değişimi, built environment + konut değeri): Buszkiewicz JH et al. — [https://pubmed.ncbi.nlm.nih.gov/35813186/](https://pubmed.ncbi.nlm.nih.gov/35813186/) (tam metin: [https://www.sciencedirect.com/science/article/pii/S2352827322001379](https://www.sciencedirect.com/science/article/pii/S2352827322001379))

**Seattle-Paris karşılaştırması**

- Drewnowski A et al. "Food Environment and Socioeconomic Status Influence Obesity Rates in Seattle and in Paris." Int J Obes 2014. — [https://www.researchgate.net/publication/237056433_Food_Environment_and_Socioeconomic_Status_Influence_Obesity_Rates_in_Seattle_and_in_Paris](https://www.researchgate.net/publication/237056433_Food_Environment_and_Socioeconomic_Status_Influence_Obesity_Rates_in_Seattle_and_in_Paris)

**Minneapolis-St Paul NFE-HFI**

- Agarwal S, Fertig AR, Trofholz AC, Tate AD, Robinson J, Berge JM. "Exploring the associations between neighbourhood food environment, household food insecurity and child weight-related outcomes..." Public Health Nutr 2022. — [https://pmc.ncbi.nlm.nih.gov/articles/PMC9991713/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9991713/) (PubMed: [https://pubmed.ncbi.nlm.nih.gov/36210770/](https://pubmed.ncbi.nlm.nih.gov/36210770/))
- İlişkili/arka plan çalışma (aynı bölge, GIS buffer + adolesan): "Neighbourhood food environments: are they associated with adolescent dietary intake, food purchases and weight status?" — [https://pmc.ncbi.nlm.nih.gov/articles/PMC3119051/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3119051/)

Daha sonra bu kişilere yönelik bazı politikalar-sunumlar geliştirilebilir: Mesela bireysel faktörlerin baskın olduğu kişilerde buna yöneilk beslenme eğitimleri, çevrenin baskın olduğu saptanan kişilerde bunu by pass etmelerini sağlayacak öneriler, yemek pişirme becerileri eğitimi falan..

**Üçüncü adım**: Sadece yaşanılan yere göre değil, vaktin çoğunun geçirildiği yere göre: kişi obezojenik bir yere _pasif maruz mu kalıyor_ yoksa zaten _o tercihleri yaptığı için mi_ oraya gidiyor, bunu ayırt etmek zor. Mesela burada bir iş paketi de hem orada olup hem yaşayan pek dışarı çıkmayan, başka bir bölgeye geçiş yapan birilerinin karşılaştırması olabilir gibi.

**Dördüncü adım:** Dijital besin çevresi?? Kentin kenti özelliklerini birincil parametre yapmadan, online yemek, market, eve teslim hizmetlerinin oluşturduğu "dijital çevreyi" tespit etmek? Veya dijital besin çevresinin ölçülebilirğini, ne olduğunu daha detaylıca araştırmak. Mesela yemek uygulamaları değil de instagramda çok popüler olan bir bank, bir mısır satısıcı mesela kendi çevresini oluşturuyordur??

Dijital çevreyle ilgili çalışmalar:
- Bennett R et al. "The potential influence of the digital food retail environment on health: a systematic scoping review." Obes Rev 2024. — [https://onlinelibrary.wiley.com/doi/10.1111/obr.13671](https://onlinelibrary.wiley.com/doi/10.1111/obr.13671)
- Morrison C et al. "Combo Deals, Junk Meals: A Systematic Review Examining the Healthiness of Foods Promoted on Meal Delivery Apps." Obes Rev 2026. — [https://pmc.ncbi.nlm.nih.gov/articles/PMC13243348/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13243348/)
- Sacks G et al. "The emergence of meal delivery applications: a research agenda to advance the next decade of progress in nutrition." Eur J Clin Nutr 2025. — [https://www.nature.com/articles/s41430-025-01597-y](https://www.nature.com/articles/s41430-025-01597-y)
- "Digital Food Environments and Hidden Obesity Risk Among Urban Youth: a Mixed-Methods Study" 2026. — [https://www.researchgate.net/publication/400407153_Digital_Food_Environments_and_Hidden_Obesity_Risk_Among_Urban_Youth_a_Mixed-Methods_Study](https://www.researchgate.net/publication/400407153_Digital_Food_Environments_and_Hidden_Obesity_Risk_Among_Urban_Youth_a_Mixed-Methods_Study)
- "Consumption of Food Offered by Delivery Applications (Apps)" (Brezilya, snowball örneklem). — [https://pmc.ncbi.nlm.nih.gov/articles/PMC11121648/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11121648/)

**Ek adım**: Besin çevrenin etkisi değiştiren düzenleyici faktörler var mı? Mesela yeşillik artınca nitelik nasıl değişiyor, walkability artınca nasıl, plazalar yoğunlaşınca nasıl...?

**Ek adım:** çevreyi tek bir "iyi/kötü" ekseninde değil, çok boyutlu tipolojiler (örn. "objektif iyi ama algısı kötü" gibi uyumsuz profiller) olarak ele alan çalışmalar var. mahalleler için farklı obesojenik profilleri oluşturulmuş (Sun Y, Lu W, Gu J, Yao Y, Wan T. "Unveiling the obesogenic neighborhood food environment factors and typologies in Tianjin, China." Front Public Health 2025)

**Ek adım:** Elimizde sokak sokak ciddi veriler olacaksa, AI yardımıyla birkaç bulgu girilip o sokağın-mahallenin-bölgenin anlık food environment skorunu tahmin eden modeller oluşturulabilir.

**Bunlardan hariç:** farklı platformların satış bölgelerini, yemek türlerini, 24 saatlik dağılımı haritalayıp fiziksel obezojenik çevre bölgeleriyle üst üste oturtmak. Veriye ulaşmak sıkıntı tabi.


