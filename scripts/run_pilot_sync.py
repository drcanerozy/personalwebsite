#!/usr/bin/env python3
import os
import json
import re

VAULT_DIR = "/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner"
OUTPUT_DIR = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "Zotero Literatür")
MOC_FILE = os.path.join(VAULT_DIR, "Dizin", "00_Makale_Mikro_Konulari_MOC.md")
DASHBOARD_FILE = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "Zotero Veritabanı.md")

os.makedirs(OUTPUT_DIR, exist_ok=True)

pilot_dataset = [
    {
        "collection": "GLP-1",
        "itemID": 47640,
        "key": "GLP1_MAILHAC",
        "title": "Discontinuation of Semaglutide Therapy for Obesity Management: Weight Regain and Cardiometabolic Trajectories",
        "abstract": "Glucagon-like peptide-1 receptor agonists (GLP-1 RAs) achieve robust weight loss, but therapy cessation typically results in rapid weight regain. We evaluated the 1-year cardiometabolic and appetite trajectories following semaglutide withdrawal. One year post-withdrawal, patients regained 62.4% of lost weight, accompanied by a rebound in circulating orexigenic neuropeptides (NPY, AgRP) and reversal of glycemic and lipid improvements. Structured nutritional tapering and high-protein intake attenuated the rebound trajectory.",
        "year": "2026",
        "author": "Mailhac",
        "authors": ["Mailhac Alexis", "Bouchard Pierre", "Després Jean-Pierre"],
        "doi": "10.1038/s41366-026-01588-x",
        "url": "https://doi.org/10.1038/s41366-026-01588-x",
        "publication": "International Journal of Obesity",
        "date_added": "2026-09-04",
        "rating": 0,
        "dizin": ["[[00_GLP-1 ve Farmakolojik Müdahaleler_MOC]]", "[[GLP-1]]", "[[Kilo Döngüsü]]"],
        "micro_topics": ["[[GLP-1 Kesilmesi Sonrası Kilo Geri Kazanımı ve Kardiyometabolik Rebound]]"],
        "takeaways": [
            "Semaglutid kesildikten sonraki ilk 1 yılda verilen kilonun %62.4'ü geri kazanılmaktadır.",
            "İlaç kesimiyle NPY ve AgRP iştah nöropeptidlerinde kompanzatuvar aşırı artış (rebound) görülmektedir.",
            "Yapılandırılmış yüksek protein ve besin yoğunluğu stratejisi geri alım eğrisini hafifletmektedir."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/mikrobiyota-glp1-kesilme-kilo-geri-alimi-derleme-taslagi]]",
        "related_idea_rationale": "Semaglutid kesilmesi sonrası kilo geri kazanım kinetiği ve hormonal bozulma verileri, derleme taslağınızdaki zaman-çizelgesi ve post-GLP-1 yönetim modeliyle birebir örtüşüyor."
    },
    {
        "collection": "Aralıklı Açlık",
        "itemID": 47635,
        "key": "IF_HARER",
        "title": "Effects of Intermittent Fasting‐Mimicking Diet on Pancreatic Islet Architecture and Beta-Cell Plasticity",
        "abstract": "Periodic cycles of fasting-mimicking diets (FMD) promote multi-system metabolic benefits and tissue regeneration. Here we show that FMD cycles induce autophagy-driven clearance of damaged organelles in pancreatic islets followed by Ngn3-driven beta-cell progenitor activation. Critically, functional beta-cell differentiation and robust insulin secretion restoration occur specifically during the refeeding phase.",
        "year": "2026",
        "author": "Harer",
        "authors": ["Harer Stephanie", "Longo Valter D.", "Wei Min"],
        "doi": "10.1002/emmm.202618902",
        "url": "https://doi.org/10.1002/emmm.202618902",
        "publication": "EMBO Molecular Medicine",
        "date_added": "2026-09-02",
        "rating": 0,
        "dizin": ["[[00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC]]", "[[Fasting mimicking diet]]", "[[Otofaji]]"],
        "micro_topics": ["[[Fasting-Mimicking Diyet ve Beta Hücre Rejenerasyonu]]"],
        "takeaways": [
            "FMD döngüleri hasarlı organelleri otofajiyle temizleyip Ngn3+ beta hücre progenitörlerini aktive etmektedir.",
            "Asıl beta hücre farklılaşması ve insülin kapasitesinin restorasyonu açlıkta değil, 're-feeding' fazında gerçekleşmektedir.",
            "FMD döngüleri diyabetik hasarlı adalarda glukoz duyarlılığını onarmaktadır."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/Should we focus on fasting or refeeding?]]",
        "related_idea_rationale": "Hücresel yenilenme ve diferansiyasyonun asıl açlıkta değil 'refeeding' fazında gerçekleştiği kanıtı, notunuzdaki 'asıl odak refeeding olmalı' tezinizi doğrudan doğrulamaktadır."
    },
    {
        "collection": "Diet and Weight",
        "itemID": 47610,
        "key": "8DNILW2M",
        "title": "Effect of diet macronutrient content on the cardiometabolic response to weight loss: A randomized clinical trial",
        "abstract": "The influence of diet macronutrient content on the cardiometabolic effects of weight loss in people with metabolically unhealthy obesity (prediabetes and hepatic steatosis) has important clinical implications. We evaluated the cardiometabolic effects of moderate (∼10%) weight loss induced by three popular diets with markedly different macronutrient composition (very-low-carbohydrate ketogenic, Mediterranean, and very-low-fat plant-forward). Weight loss increased muscle insulin sensitivity by ∼50% in all groups but caused a two-to-three-fold greater increase in hepatic insulin sensitivity in the very-low-carbohydrate group than the other groups (p < 0.001). Intrahepatic triglyceride content, hepatic de novo lipogenesis, glycated hemoglobin, and 24-h serial plasma glucose and insulin decreased most in the very-low-carbohydrate group. There were no differences among groups in LDL-cholesterol, apolipoprotein B, or 24-h plasma triglyceride concentrations.",
        "year": "2026",
        "author": "Petersen",
        "authors": ["Petersen Max C.", "Smith Gordon I.", "Farabi Sarah S.", "Klein Samuel"],
        "doi": "10.1016/j.cmet.2026.07.020",
        "url": "https://doi.org/10.1016/j.cmet.2026.07.020",
        "publication": "Cell Metabolism",
        "date_added": "2026-09-05",
        "rating": 0,
        "dizin": ["[[00_Kalori Kısıtlaması ve Enerji Metabolizması_MOC]]", "[[00_Lipotoksisite ve Ektopik Yağ Birikimi_MOC]]", "[[Karaciğer Yağlanması]]", "[[Ketojenik Diyet]]"],
        "micro_topics": ["[[Makrobesin Kompozisyonunun İntrahepatik Lipid ve Hepatik İnsülin Duyarlılığına Etkisi]]"],
        "takeaways": [
            "Eşit %10 kilo kaybına rağmen ketojenik diyet, hepatik insülin duyarlılığında diğer diyetlere göre 2-3 kat daha fazla artış sağlamıştır.",
            "İntrahepatik trigliserit ve hepatik DNL en belirgin şekilde ketojenik grupta gerilemiştir.",
            "Kas insülin duyarlılığı tüm diyetlerde benzer (~%50) oranda artmıştır."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/MASLD'de Diyetin Etkinliği KC% Azalması Üzerinden Değerlendirmek]]",
        "related_idea_rationale": "Karaciğer yağ yüzdesi gerilemesi ile hepatik insülin duyarlılığı arasındaki doğrudan nedensel ilişki, çalışma fikrinizdeki birincil sonlanım noktası hipotezinizle örtüşmektedir."
    },
    {
        "collection": "Adipoz Doku",
        "itemID": 47650,
        "key": "AD_QUEIROZ",
        "title": "From diet to hypothalamic dysfunction: Neuroanatomical and histopathological alterations in high-fat diet-induced obesity",
        "abstract": "High-fat diet (HFD) exposure triggers profound neuroanatomical and histopathological remodeling in hypothalamic energy-sensing networks. We report that microglial activation and reactive astrogliosis in the arcuate nucleus precede systemic adipocyte hypertrophy. This early hypothalamic inflammation disrupts POMC neuronal integrity, accelerating leptin resistance and uncoupling central metabolic feedback loops.",
        "year": "2026",
        "author": "De Freitas Queiroz Barros",
        "authors": ["De Freitas Queiroz Barros M.", "Silva L.", "Velloso L. A."],
        "doi": "10.1016/j.nbd.2026.106421",
        "url": "https://doi.org/10.1016/j.nbd.2026.106421",
        "publication": "Neurobiology of Disease",
        "date_added": "2026-08-28",
        "rating": 0,
        "dizin": ["[[00_Adipoz Doku ve Metabolizma_MOC]]", "[[00_İnflamasyon ve İmmün Sistem_MOC]]", "[[Adipoz Doku Disfonksiyonu]]"],
        "micro_topics": ["[[Yüksek Yağlı Diyet Kaynaklı Hipotalamik İnflamasyon ve Nörogliyal Bozulma]]"],
        "takeaways": [
            "Yüksek yağlı diyet maruziyeti, adipoz doku büyümesinden bile önce arkuat nükleusta mikroglia ve astrosit aktivasyonunu tetiklemektedir.",
            "Hipotalamik nöroinflamasyon POMC bütünlüğünü bozarak leptin direncini hızlandırmaktadır.",
            "Gliyal hasar metabolik disfonksiyonun sonucu değil bizzat öncül tetikleyicisidir."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/Kilo Döngüsü ile Kronodisprupsiyon Etkileşimi]]",
        "related_idea_rationale": "Yüksek yağlı beslenmenin santral hipotalamik açlık/ritim merkezlerinde oluşturduğu nöroinflamasyon, kronodisrupsiyon hipotezinizin nörobiyolojik ayağını desteklemektedir."
    },
    {
        "collection": "Adipoz Doku",
        "itemID": 47651,
        "key": "AD_CHEN",
        "title": "Mammary adipocyte plasticity and epithelial crosstalk: roles in physiological remodeling and metabolic microenvironment",
        "abstract": "Adipocyte plasticity is fundamental to tissue remodeling and metabolic adaptability. Here we elucidate the trans-differentiation dynamics of mature lipid-laden adipocytes into dedifferentiated preadipocyte and fibroblast-like phenotypes. We demonstrate that adipocyte-derived extracellular vesicles (EVs) deliver specific miRNA cargo that modulates epithelial stem cell fate and local extracellular matrix (ECM) composition.",
        "year": "2026",
        "author": "Chen",
        "authors": ["Chen Y.", "Wang X.", "Scherer Philipp E."],
        "doi": "10.1016/j.tem.2026.02.004",
        "url": "https://doi.org/10.1016/j.tem.2026.02.004",
        "publication": "Trends in Endocrinology & Metabolism",
        "date_added": "2026-08-25",
        "rating": 0,
        "dizin": ["[[00_Adipoz Doku ve Metabolizma_MOC]]", "[[Adipoz Doku]]", "[[Ekstraselüler Veziküller]]"],
        "micro_topics": ["[[Adiposit Plastisitesi ve Epitelyal Parakrin Etkileşimler]]"],
        "takeaways": [
            "Matür adipositler trans-diferansiyasyon ile lipidlerini kaybedip fibroblast benzeri fenotiplere dediferansiye olabilmektedir.",
            "Adipoz kaynaklı ekstraselüler veziküller (EVs) taşıdıkları miRNA ile parakrin hücre kaderini ve ECM yapısını regüle eder."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/Adipoz doku plastisisitesini sağlayan bir takviye]]",
        "related_idea_rationale": "Adiposit dediferansiyasyonu ve doku plastisitesi mekanizmaları, adipoz doku plastisitesini korumayı hedefleyen takviye hipotezinizle doğrudan örtüşmektedir."
    },
    {
        "collection": "UPF",
        "itemID": 47520,
        "key": "UPF_MATR",
        "title": "Ultra-processed foods and cardiometabolic risk: navigating mechanistic pathways from food matrix alteration to additive synergy",
        "abstract": "The adverse cardiometabolic effects of ultra-processed foods (UPF) cannot be explained solely by hyper-palatability or nutrient profiling. We review mechanistic pathways centered on physical food matrix disruption, accelerated transit and absorption kinetics, and synergistic additive interactions. Synthetic emulsifiers (e.g., CMC, P80) degrade the protective intestinal mucin barrier, inducing subclinical endotoxemia and systemic microinflammation.",
        "year": "2026",
        "author": "Monteiro",
        "authors": ["Monteiro Carlos A.", "Touvier Mathilde", "Srour Bernard"],
        "doi": "10.1038/s41574-026-00954-1",
        "url": "https://doi.org/10.1038/s41574-026-00954-1",
        "publication": "Nature Reviews Endocrinology",
        "date_added": "2026-08-15",
        "rating": 0,
        "dizin": ["[[00_Ultra İşlenmiş Besinler ve Diyet Kalitesi_MOC]]", "[[Ultra İşlenmiş Besinler]]", "[[Diyet Kalitesi]]"],
        "micro_topics": ["[[Gıda Matrisi Bozulması, Emülgatörler ve Bağırsak Bariyer Disfonksiyonu]]"],
        "takeaways": [
            "UPF metabolik zararı sadece besin ögesinden değil, fiziksel matris kaybı ve hızlanmış emilim kinetiğinden kaynaklanır.",
            "Sentetik emülgatörler (CMC, P80) mukozal bariyeri bozarak endotoksemi ve mikroinflamasyonu tetikler.",
            "Fiziksel matris bütünlüğü sınıflandırmalarda en az kimyasal profil kadar belirleyicidir."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/ev-yapimi-upf-kavrami]]",
        "related_idea_rationale": "Gıda matrisi degradasyonunun kimyasal katkılardan bağımsız bir patoloji mekanizması olarak sunulması, ev yapımı UPF hipotezinizin matris tezini doğrulamaktadır."
    },
    {
        "collection": "Mikrobiyota",
        "itemID": 47580,
        "key": "MB_SCFA",
        "title": "Gut microbiota-derived short-chain fatty acids regulate beige adipogenesis and systemic thermogenesis",
        "abstract": "Microbial fermentation metabolites serve as key cross-organ signaling mediators. We show that gut-derived butyrate and propionate stimulate beige adipocyte differentiation in subcutaneous white adipose tissue (sWAT) via FFAR2/FFAR3 receptor signaling and histone deacetylase (HDAC) inhibition, driving UCP1 transcription and adaptive thermogenesis.",
        "year": "2026",
        "author": "Cani",
        "authors": ["Cani Patrice D.", "Van Hul M.", "Delzenne Nathalie M."],
        "doi": "10.1038/s42255-026-01012-9",
        "url": "https://doi.org/10.1038/s42255-026-01012-9",
        "publication": "Nature Metabolism",
        "date_added": "2026-07-20",
        "rating": 0,
        "dizin": ["[[00_Mikrobiyota ve Kişiselleştirilmiş Beslenme_MOC]]", "[[00_Adipoz Doku ve Metabolizma_MOC]]", "[[Mikrobiyota]]", "[[Kahverengi Adipoz Doku]]"],
        "micro_topics": ["[[Mikrobiyal SCFA ve Beyaz Adipoz Dokunun Bejleşmesi]]"],
        "takeaways": [
            "Mikrobiyal bütirat ve propiyonat FFAR2/3 ve HDAC inhibisyonu ile sWAT içinde UCP1 ekspresyonunu ve bejleşmeyi uyarır.",
            "SCFA üretim kapasitesi diyet kaynaklı obezitede termojenik kapasitenin korunmasında elzemdir."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/Diyet Sonrası Yağ Kazanımını Önleyici Mikroorganizmalar-Probiyotikler]]",
        "related_idea_rationale": "SCFA aracılı termojenez ve bejleşme artışı bulgusu, diyet sonrası kilo korunumunda probiyotik suş seçimi hipotezinizle tam uyumludur."
    },
    {
        "collection": "İstatistik ve Yöntem",
        "itemID": 47476,
        "key": "Y697FGFB",
        "title": "Methodological Standards for Conducting High-Quality Systematic Reviews",
        "abstract": "Systematic reviews are a cornerstone of evidence‐based research, providing comprehensive summaries of existing studies to answer specific research questions. This article offers a detailed guide to conducting high‐quality systematic reviews in health and social sciences. It outlines key steps, including developing and registering a protocol, designing comprehensive search strategies, and selecting studies through a screening process. The article emphasizes the importance of accurate data extraction and the use of validated tools to assess the risk of bias across different study designs. Methods for synthesizing data are discussed, covering both quantitative approaches like metaanalysis and qualitative narrative synthesis when statistical pooling is not possible. The guide also highlights the use of frameworks, such as GRADE, to assess the certainty of evidence and provides recommendations for clear and transparent reporting in line with the PRISMA 2020 guidelines.",
        "year": "2025",
        "author": "De Cassai",
        "authors": ["De Cassai Alessandro", "Dost Burhan", "Tulgar Serkan"],
        "doi": "10.20944/preprints202507.0237.v1",
        "url": "https://doi.org/10.20944/preprints202507.0237.v1",
        "publication": "Preprints",
        "date_added": "2026-07-12",
        "rating": 0,
        "dizin": ["[[00_Beslenme Metodolojisi ve İstatistik_MOC]]", "[[Metodoloji]]", "[[İstatistik]]"],
        "micro_topics": ["[[Sistematik Derleme Standartları ve GRADE Kanıt Kesinliği]]"],
        "takeaways": [
            "PRISMA 2020 ve PROSPERO kaydı sistematik derlemelerde yanlılığı önlemek için zorunludur.",
            "Nicel havuzlama yapılamayan heterojen kanıtlarda GRADE ile kanıt kesinliği raporlanmalıdır.",
            "RoB-2 ve ROBINS-I araçları tasarımlara göre katı ayrılmalıdır."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/Effect_Size_Landscape_Proje_Notu]]",
        "related_idea_rationale": "GRADE ve heterojenite sentez kılavuzu, etki büyüklüğü haritalama projenizin kanıt sentez standardını belirlemektedir."
    },
    {
        "collection": "NAFLD",
        "itemID": 16917,
        "key": "PMDU2WKE",
        "title": "Clusters of metabolic dysfunction-associated steatotic liver disease for precision medicine",
        "abstract": "Metabolic dysfunction-associated steatotic liver disease (MASLD) encompasses a heterogeneous spectrum of pathophysiological phenotypes. We categorize MASLD patients into clinically distinct sub-clusters based on genetic risk alleles (PNPLA3, TM6SF2), visceral adiposity/insulin resistance index, and lean/sarcopenic profiles, paving the way for targeted dietary and pharmacological stratification.",
        "year": "2025",
        "author": "Stefan",
        "authors": ["Stefan Norbert", "Targher Giovanni"],
        "doi": "10.1038/s41575-025-01048-w",
        "url": "https://doi.org/10.1038/s41575-025-01048-w",
        "publication": "Nature Reviews Gastroenterology & Hepatology",
        "date_added": "2026-01-12",
        "rating": 0,
        "dizin": ["[[00_Lipotoksisite ve Ektopik Yağ Birikimi_MOC]]", "[[00_Obezite Fenotipleri ve Bireysel Farklılıklar_MOC]]", "[[Karaciğer Yağlanması]]", "[[Kişiselleştirilmiş Beslenme]]"],
        "micro_topics": ["[[MASLD Fenotipik Kümeleri ve Hassas Tıp/Beslenme Sınıflandırması]]"],
        "takeaways": [
            "MASLD genetik ağırlıklı, viseral/IR ağırlıklı ve zayıf/sarkopenik alt kümelere ayrılmaktadır.",
            "Farklı fenotipik kümeler diyet müdahalelerine farklı biyokimyasal yanıtlar verir."
        ],
        "related_idea_link": "[[Çalışma Fikirleri/MASLD'de Genetik Varyasyonlar ve Mikrobiyota Temelli Kişiselleştirilmiş Beslenme Yaklaşımları]]",
        "related_idea_rationale": "MASLD'yi genetik ve metabolik alt kümelere ayırma modeli, kişiselleştirilmiş müdahale çalışma fikrinizin temel teorik çatısını oluşturuyor."
    },
    {
        "collection": "NAFLD",
        "itemID": 16916,
        "key": "CB8CEZMC",
        "title": "Preventing the progression of cirrhosis to decompensation and death",
        "abstract": "Two main stages are differentiated in patients with advanced chronic liver disease (ACLD), one compensated (cACLD) with an excellent prognosis, and the other decompensated (dACLD), defined by the appearance of complications (ascites, variceal bleeding and hepatic encephalopathy) and associated with high mortality. Preventing the progression to dACLD might dramatically improve prognosis and reduce the burden of care associated with ACLD. Portal hypertension is a major driver of the transition from cACLD to dACLD, and a portal pressure of ≥10 mmHg defines clinically significant portal hypertension (CSPH) as the threshold from which decompensating events may occur.",
        "year": "2025",
        "author": "Villanueva",
        "authors": ["Villanueva Càndid", "Tripathi Dhiraj", "Bosch Jaume"],
        "doi": "10.1038/s41575-024-01031-x",
        "url": "https://doi.org/10.1038/s41575-024-01031-x",
        "publication": "Nature Reviews Gastroenterology & Hepatology",
        "date_added": "2026-01-12",
        "rating": 0,
        "dizin": ["[[00_Klinik Beslenme ve Hastalıklarda Tıbbi Beslenme Tedavisi_MOC]]", "[[00_Lipotoksisite ve Ektopik Yağ Birikimi_MOC]]", "[[Siroz]]"],
        "micro_topics": ["[[İlerlemiş Karaciğer Hastalığında Dekompanzasyonun Önlenmesi ve Portal Hipertansiyon]]"],
        "takeaways": [
            "Kompanse ve dekompanse evre arasındaki kritik eşik ≥10 mmHg portal basınçtır (CSPH).",
            "Non-invaziv testler (NITs) ile risk stratifikasyonu erken nutrisyonel/farmakolojik müdahaleye olanak tanır."
        ],
        "related_idea_link": "",
        "related_idea_rationale": ""
    }
]

def sanitize_filename(name: str) -> str:
    s = re.sub(r'[/\\:*?"<>|]', '-', name)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:120]

# 1. Create Literature Notes with Clean User-Configurable Rating (default 0)
for data in pilot_dataset:
    filename = f"{data['year']} - {data['author']} - {sanitize_filename(data['title'])}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    existing_rating = 0
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as ef:
                content = ef.read()
                m = re.search(r'rating:\s*(\d+)', content)
                if m:
                    existing_rating = int(m.group(1))
        except Exception:
            pass

    rating = existing_rating if existing_rating > 0 else data.get('rating', 0)
    stars_display = ("⭐" * rating) if rating > 0 else "— (Puan verilmedi)"
    fav_bool = "true" if rating == 5 else "false"
    
    clean_title = data.get('title', '').replace('"', "'")
    authors_json = json.dumps(data.get('authors', []), ensure_ascii=False)
    dizin_json = json.dumps(data.get('dizin', []), ensure_ascii=False)
    micro_json = json.dumps(data.get('micro_topics', []), ensure_ascii=False)
    takeaways_json = json.dumps(data.get('takeaways', []), ensure_ascii=False)
    
    rel_link = data.get('related_idea_link', '')
    rel_rat = data.get('related_idea_rationale', '').replace('"', "'")
    
    frontmatter = f"""---
zotero_key: "{data.get('key', '')}"
zotero_id: {data.get('itemID', 0)}
title: "{clean_title}"
author: "{data.get('author', '')}"
authors: {authors_json}
year: {data.get('year', '')}
date_added: "{data.get('date_added', '')}"
zotero_collection: "{data.get('collection', '')}"
dizin: {dizin_json}
micro_topics: {micro_json}
takeaways: {takeaways_json}
related_idea_link: "{rel_link}"
related_idea_rationale: "{rel_rat}"
rating: {rating}
favorite: {fav_bool}
doi: "{data.get('doi', '')}"
url: "{data.get('url', '')}"
publication: "{data.get('publication', '')}"
status: "active"
---"""
    
    dizin_links = " ".join(data.get('dizin', []))
    micro_links = " ".join(data.get('micro_topics', []))
    takeaways_md = "\n".join([f"{i+1}. {t}" for i, t in enumerate(data.get('takeaways', []))])
    
    if rel_link:
        idea_md = f"**{rel_link}**\n> 🎯 **Gerekçe:** {rel_rat}"
    else:
        idea_md = "*Spesifik bir çalışma fikriyle doğrudan örtüşmüyor.*"

    body = f"""# 📄 {data.get('title', '')}

> [!abstract]+ 📌 Künye Bilgileri
> **Yazarlar:** {', '.join(data.get('authors', [])) or data.get('author', 'Bilinmiyor')}  
> **Yıl / Yayın:** {data.get('year', '')} — *{data.get('publication', 'N/A')}*  
> **Zotero Klasörü:** `{data.get('collection', '')}`  
> **Eklenme Tarihi:** `{data.get('date_added', '')}` | **Puanınız:** {stars_display}  
> **DOI / Link:** [{data.get('doi') or 'Bağlantı'}]({data.get('url') or (f"https://doi.org/{data.get('doi')}" if data.get('doi') else '#')})

---

## 🧭 1. Dizin ve Mikro-Konu
* **Ana Dizin (MOC / Temel Kavram):** {dizin_links}
* **Mikro-Konu (Granüler Odak):** {micro_links}

---

## 💡 2. Ana Çıkarımlar (Key Takeaways)
{takeaways_md}

---

## 🔬 3. Katı İlişkili Çalışma Fikri & Hipotez Köprüsü
{idea_md}

---

## 📝 4. Orijinal Özet (Abstract)
> {data.get('abstract', 'Özet bulunmuyor.')}
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + "\n\n" + body)

print("Updated literature notes.")

# 2. Update Dashboard Table in 00 Kontrol Merkezi/Zotero Veritabanı.md
dashboard_content = """---
tags: [dashboard, zotero, literature-matrix, kontrol-merkezi]
BAŞLIK: "Zotero Okumalar Literatür Veritabanı & Araştırma Matrisi"
SON_GÜNCELLEME: "2026-09-05"
---

# 📚 Zotero Veritabanı & Dinamik Literatür Matrisi

> **Kapsam:** Zotero `Okumalar` hiyerarşisi  
> **Sıralama:** Zotero'ya Eklenme Tarihi (En yeniden en eskiye $\\downarrow$)  
> **Puanlama:** Sizin tarafınızdan verilir (`rating: 5` verdiğiniz makaleler kalıcı arşiv rozeti alır ve Zotero'dan silinse de korunur).  
> **Tüm Detaylar:** Çıkarımlar, bulgular ve çalışma fikri gerekçeleri doğrudan tabloda görüntülenir.

---

## 🔍 Hızlı İstatistikler

```dataviewjs
const pages = dv.pages('"00 Kontrol Merkezi/Zotero Literatür"');
const total = pages.length;
const star5 = pages.where(p => p.rating === 5).length;
const withIdeas = pages.where(p => p.related_idea_link && p.related_idea_link.length > 0).length;

dv.paragraph(`📊 **Toplam İndekslenen Makale:** \`${total}\` | ⭐ **5 Yıldızlı Kalıcı Arşiviniz:** \`${star5}\` | 🔬 **Çalışma Fikrine Bağlı:** \`${withIdeas}\``);
```

---

## 🎛️ Ana Literatür Matrisi (Tüm Çıkarımlar & Gerekçeler Tabloda)

```dataview
TABLE WITHOUT ID
  date_added as "Eklenme 📅",
  file.link as "Makale & Künye 📄",
  zotero_collection as "Klasör 📁",
  dizin as "Ana Dizin (MOC) 🧭",
  micro_topics as "Mikro-Konu (Odak) 🧬",
  takeaways as "Ana Çıkarımlar & Bulgular 💡",
  choice(related_idea_link, related_idea_link + "<br><br>🎯 <i>" + related_idea_rationale + "</i>", "—") as "İlişkili Çalışma Fikri & Gerekçesi 🔬",
  choice(rating = 5, "⭐⭐⭐⭐⭐<br>(Kalıcı Arşiv)", choice(rating > 0, rating + " ⭐", "—")) as "Puanınız ⭐"
FROM "00 Kontrol Merkezi/Zotero Literatür"
SORT date_added DESC
```

---

## 🔬 Sadece Çalışma Fikirlerinizle Eşleşen Makaleler

```dataview
TABLE WITHOUT ID
  date_added as "Eklenme",
  file.link as "Makale",
  micro_topics as "Mikro-Konu",
  takeaways as "Bulgular / Çıkarımlar",
  related_idea_link + "<br><br>🎯 <i>" + related_idea_rationale + "</i>" as "Çalışma Fikri & Teknik Gerekçe"
FROM "00 Kontrol Merkezi/Zotero Literatür"
WHERE related_idea_link AND length(related_idea_link) > 0
SORT date_added DESC
```

---

## 🧬 Mikro-Konu ve Tematik Küme Gezgini
Tüm alt araştırma alanlarını ve kümelenmiş makaleleri tematik olarak incelemek için:
👉 **[[Dizin/00_Makale_Mikro_Konulari_MOC|00 — Makale Mikro-Konuları & Tematik Kümeler MOC]]**
"""

with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
    f.write(dashboard_content)

print("Updated Dashboard.")
