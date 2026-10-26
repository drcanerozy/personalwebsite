import os
import re

CONTENT_DIR = "/Users/canerozyildirim/Sites/personalwebsite/content"

# Enrichments for Turkish teaching files
TR_ENRICHMENTS = {
    "01-bilgisayar-ve-yapay-zeka.md": """
## 🎯 Dersin Amacı ve Kapsamı
Bu ders, beslenme ve diyetetik lisans öğrencilerinin güncel yapay zeka (AI), makine öğrenmesi (ML), büyük dil modelleri (LLM) ve veri analitiği araçlarını mesleki karar alma süreçlerine entegre etmelerini hedefler. Öğrenciler, besin tüketim kayıtlarının dijitalleştirilmesi, makro ve mikro besin ögesi analizi, kanıta dayalı literatür tarama (PubMed/BioRxiv filtreleme) ve kişiselleştirilmiş danışan iletişim materyalleri tasarlama süreçlerinde modern dijital teknolojileri etik ve güvenilir biçimde kullanma yetkinliği kazanır.

## 📚 Haftalık Konu Dağılımı ve Müfredat
- **Hafta 1:** Bilişim Teknolojileri ve Beslenme Biliminin Kesişimi: Temel Kavramlar ve Tarihsel Evrim.
- **Hafta 2:** Yapay Zeka, Makine Öğrenmesi ve Derin Öğrenme Mimarisi: Diyetisyenin Çalışma Masasındaki Dönüşüm.
- **Hafta 3:** Besin Veri Tabanları ve Bileşim Tabloları (TürKomp, USDA FoodData Central) ile API Kullanımı.
- **Hafta 4:** Doğal Dil İşleme (NLP) ve LLM Teknolojileri: Danışan Notları ve Görüşme Özetleme.
- **Hafta 5:** Bilgisayar Destekli Menü Planlama ve Diyet Değişim Listesi Optimizasyonu.
- **Hafta 6:** Akademik Literatür Tarama Stratejileri: Yapay Zeka Destekli Bilimsel Sentez ve Özetleme Araçları.
- **Hafta 7:** Dijital Sağlık Uygulamaları, Mobil Kalori Takip Sistemleri ve Giyilebilir Cihaz Verileri.
- **Hafta 8:** Sağlık İletişiminde Görselleştirme: Infografik Tasarımı ve Danışan Eğitim Materyalleri.
- **Hafta 9:** Beslenme Biyoinformatiğine Giriş: Omiks Verileri ve Kişiselleştirilmiş Beslenme Algoritmaları.
- **Hafta 10:** Yapay Zekanın Hata Payı (Halüsinasyon), Mahremiyet (KVKK/GDPR) ve Mesleki Etik Sınırlar.

## 🏆 Kazanımlar ve Mesleki Yetkinlikler
- Yapay zeka çıktılarını beslenme bilimi ve biyokimya süzgecinden geçirerek doğrulama yeteneği.
- Dijital besin veri tabanlarını ve analitik yazılımları klinik diyetisyenlik pratiğinde etkin kullanma.
- Danışanların mobil sağlık uygulamalarından getirdiği verileri doğru yorumlama ve klinik karara dönüştürme.
- Yapay zeka tabanlı araçların sınırlarını, gizlilik kurallarını ve tıbbi sorumluluk çerçevesini benimseme.

## 📖 Temel Başvuru Kaynakları
- Topol, E. (2019). *Deep Medicine: How Artificial Intelligence Can Make Healthcare Human Again*. Basic Books.
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach (4th ed.)*. Pearson.
- Türkiye Beslenme Rehberi (TÜBER 2022). T.C. Sağlık Bakanlığı Yayınları.
- Güncel ESPEN, AND (Academy of Nutrition and Dietetics) ve EFSA dijital sağlık bildirileri.
""",

    "02-beslenmenin-psikososyal-boyutlari.md": """
## 🎯 Dersin Amacı ve Biyopsikososyal Yaklaşım
Beslenme yalnızca biyokimyasal bir enerji alımı süreci değil; kültürel, ailesel, psikolojik ve sosyoekonomik faktörlerin karmaşık bir etkileşimidir. Bu dersin temel amacı; diyetisyen adaylarına bireylerin ve toplumların beslenme davranışlarını şekillendiren biyopsikososyal dinamikleri kavramsal ve klinik düzeyde aktarmaktır. Öğrenciler, diyet kısıtlamalarının psikolojik dinamiklerini, ödül mekanizmalarını, hedonik açlık fizyolojisini ve beden dismorfisi riskini bütüncül bir yaklaşımla ele almayı öğrenirler.

## 📚 Haftalık Konu Dağılımı ve Seminerler
- **Hafta 1:** Beslenme Davranışının Biyopsikososyal Modeli: Evrimsel Miras ve Modern Çevre.
- **Hafta 2:** Açlık, İştah ve Tokluk Algısının Nöropsikolojisi: Homeostatik ve Hedonik Açlık.
- **Hafta 3:** Sosyokültürel Normlar, Aile Dinamikleri ve Çocukluk Çağı Beslenme Alışkanlıkları.
- **Hafta 4:** Beden Algısı, Medya İdealizasyonu ve Sosyal Karşılaştırma Teorisi.
- **Hafta 5:** Bozulmuş Yeme Davranışları Spektrumu: Duygusal Yeme, Gece Yeme ve Kısıtlayıcı Diyetler.
- **Hafta 6:** Klinik Yeme Bozuklukları (Anoreksiya Nervoza, Bulimiya Nervoza, Tıkınırcasına Yeme Bozukluğu).
- **Hafta 7:** Ortoreksiya Nervoza: 'Sağlıklı Beslenme' Takıntısı ve Sosyal Medya Fanatizmi.
- **Hafta 8:** Ağırlık Stigması (Weight Stigma), Kilo Ayrımcılığı ve Sağlık Hizmetlerine Yansımaları.
- **Hafta 9:** GLP-1 Reseptör Agonistleri ve İştah Baskılayıcı İlaçların Psikososyal Etkileri.
- **Hafta 10:** Farkındalıklı Beslenme (Mindful Eating) ve Sezgisel Yeme (Intuitive Eating) İlkeleri.

## 🏆 Temel Öğrenme Çıktıları ve Klinik Kazanımlar
- Danışanın yeme davranışının ardındaki duygusal ve psikososyal tetikleyicileri analiz edebilme.
- Klinik yeme bozukluklarını erken aşamada tarayabilme ve multidisipliner ekibe (psikiyatri/psikoloji) doğru sevk edebilme.
- Ağırlık odaklı önyargılardan arındırılmış, kapsayıcı ve danışan merkezli klinik iletişim dili geliştirebilme.
- Yeme tutumu ve beden algısı psikometrik testlerini (EAT-26, ORTO-15, DEBQ) bilimsel olarak uygulayabilme.

## 📖 Temel Başvuru Kaynakları
- Fairburn, C. G. (2008). *Cognitive Behavior Therapy and Eating Disorders*. Guilford Press.
- Tribole, E., & Resch, E. (2020). *Intuitive Eating: A Revolutionary Anti-Diet Approach (4th ed.)*. St. Martin's Essentials.
- American Psychiatric Association (APA). (2013). *DSM-5: Diagnostic and Statistical Manual of Mental Disorders*.
- Tylka, T. L., et al. (2014). The weight-inclusive approach to health. *Journal of Obesity*, 2014.
""",

    "03-beslenme-ve-medya.md": """
## 🎯 Dersin Amacı ve Medya Okuryazarlığı
Bilgi çağında beslenme ve sağlık alanındaki en büyük tehditlerden biri, bilimsel temelden yoksun popüler iddialar ve infodemidir. Bu dersin temel amacı; beslenme ve diyetetik öğrencilerine dijital medyada, televizyonda ve sosyal ağlarda yayılan beslenme iddialarını eleştirel süzgeçten geçirme, yanıltıcı pazarlama stratejilerini tanıma ve kanıta dayalı bilimsel veriyi kamuoyuna anlaşılır ve doğru biçimde aktarma becerisi kazandırmaktır.

## 📚 Haftalık Konu Başlıkları ve İnceleme Modülleri
- **Hafta 1:** Sağlık İletişiminin Temel İlkeleri ve Medya Sosyolojisi: Diyetisyenin Kamusal Rolü.
- **Hafta 2:** Beslenme Gazeteciliği ve Sansasyonel Manşetler: 'Mucize Besin' ve 'Süper Gıda' Mitleri.
- **Hafta 3:** Bilimsel Literatürü Çarpıtma Yöntemleri: Korelasyondan Nedensellik Üretme Yanılgısı.
- **Hafta 4:** Sosyal Medya Algoritmaları, Yankı Odaları ve Beslenme Dezenformasyonu (Infodemi).
- **Hafta 5:** Takviye Edici Gıda Pazarlaması, Sağlık Beyanları ve Yasal Mevzuat (TİTCK / EFSA / FDA).
- **Hafta 6:** Influencer Kültürü, Ürün Yerleştirme ve Sponsorlu Sağlık İddialarının Analizi.
- **Hafta 7:** Besin Endüstrisi ve Lobicilik: Bilimsel Araştırmalarda Fon Sağlayıcı Etkisi ve Çıkar Çatışmaları.
- **Hafta 8:** Kanıta Dayalı Sağlık İçeriği Üretimi: Karmaşık Biyokimyasal Veriyi Sadeleştirme Sanatı.
- **Hafta 9:** Kriz İletişimi: Gıda Güvenliği Korkuları, Zehirlenme Haberleri ve Kamusal Panik Yönetimi.
- **Hafta 10:** Diyetisyenin Dijital Markası, Bilimsel Etik ve Doğruluk Kontrolü (Fact-Checking) Araçları.

## 🏆 Mesleki Kazanımlar ve İletişim Yetkinlikleri
- Medyadaki popüler beslenme iddialarını bilimsel hiyerarşi (meta-analiz, randomize kontrollü çalışma) düzeyinde test edebilme.
- Gıda takviyesi ve diyet reklamlarındaki örtük pazarlama taktiklerini ve yasal ihlalleri tespit edebilme.
- Sosyal medya ve geleneksel medya platformları için kanıta dayalı, etik ve ilgi çekici içerik üretebilme.
- Bilgi kirliliğiyle mücadelede bilimsel sözcülük ve toplum sağlığını koruma misyonunu üstlenebilme.

## 📖 Temel Başvuru Kaynakları
- Goldacre, B. (2009). *Bad Science: Quacks, Hacks, and Big Pharma Flacks*. Faber and Faber.
- Nestle, M. (2018). *Unsavory Truth: How Food Companies Skew the Science of What We Eat*. Basic Books.
- Nelson, D. E., et al. (2009). *Making Data Talk: Communicating Public Health Data to the Public, Policy Makers, and the Press*. Oxford University Press.
""",

    "04-diyet-ilkeleri-ve-populer-diyetler.md": """
## 🎯 Dersin Amacı ve Kanıta Dayalı Diyet Yaklaşımı
Bu ders, insan beslenmesinin evrimsel temellerinden başlayarak günümüzün en çok tartışılan popüler diyet modellerini (Ketojenik diyet, Aralıklı oruç/Intermittent Fasting, Akdeniz diyeti, Paleo, Karnivor, Düşük FODMAP, Vegan/Vejetaryen modeller) moleküler metabolizma, enerji balansı ve klinik kanıt düzeyinde incelemeyi hedefler. Öğrenciler, her bir diyet protokolünün endokrin yanıtlarını, mikrobiyota üzerindeki etkilerini ve uzun vadeli kardiyometabolik güvenlik profilini analiz ederler.

## 📚 Haftalık Konu Dağılımı ve Diyet Modelleri
- **Hafta 1:** İnsan Beslenmesinin Evrimsel Yolculuğu: Avcı-Toplayıcı Atalarımızdan Ultra-İşlenmiş Gıda Çağına.
- **Hafta 2:** Enerji Dengesi Modeli (CICO) ve Karbonhidrat-İnsülin Modeli (CIM): Büyük Tartışma.
- **Hafta 3:** Akdeniz Diyeti (Mediterranean Diet): Biyoaktif Bileşenler, Polifenoller ve Kardiyometabolik Koruma.
- **Hafta 4:** Aralıklı Oruç (Intermittent Fasting & TRE): Otofaji, İnsülin Duyarlılığı ve Sirkadiyen Ritim.
- **Hafta 5:** Ketojenik Diyetler ve Çok Düşük Karbonhidratlı Protokoller: Ketogenez Mekanizması ve Klinik Kullanım.
- **Hafta 6:** Bitki Temelli Beslenme: Vegan ve Vejetaryen Diyetlerin Mikrobiyota, Kardiyovasküler Sağlık ve Eksiklik Riskleri.
- **Hafta 7:** Paleolitik ve Karnivor Diyetler: Antropolojik Temeller, Lif Yetersizliği ve Lipid Parametreleri.
- **Hafta 8:** Eliminasyon Diyetleri: Düşük FODMAP, Otoimmün Protokol (AIP) ve Histamin İntoleransı.
- **Hafta 9:** Düşük Sodyumlu ve Hipertansiyon Diyetleri (DASH Modeli): Elektrolit Dengesi ve Vasküler Etkiler.
- **Hafta 10:** Diyet Sürdürülebilirliği, Yo-Yo Etkisi ve Bireye Özgü Diyet Modeli Belirleme İlkeleri.

## 🏆 Kazanımlar ve Klinik Yetkinlikler
- Popüler diyet modellerinin etki mekanizmalarını hücresel ve metabolik düzeyde açıklayabilme.
- Farklı diyetlerin klinik randomize kontrollü çalışma ve meta-analiz sonuçlarını eleştirel biçimde karşılaştırabilme.
- Danışanın klinik tablosuna, biyokimyasal parametrelerine ve yaşam tarzına en uygun kişiselleştirilmiş beslenme modelini kurgulayabilme.
- Moda diyetlerin olası besin ögesi yetersizliklerini ve metabolik risklerini önceden saptayıp önlem alabilme.

## 📖 Temel Başvuru Kaynakları
- Lieberman, D. E. (2014). *The Story of the Human Body: Evolution, Health, and Disease*. Vintage.
- Ross, A. C., et al. (2014). *Modern Nutrition in Health and Disease (11th ed.)*. Lippincott Williams & Wilkins.
- Willett, W. (2012). *Nutritional Epidemiology (3rd ed.)*. Oxford University Press.
- American Heart Association (AHA) & American Diabetes Association (ADA) Diyet Kılavuzları.
""",

    "05-immun-sistem-ve-immunonutrisyon.md": """
## 🎯 Dersin Amacı ve İmmünometabolizma
Bağışıklık sistemi, vücudun patojenlere ve metabolik stres faktörlerine karşı en dinamik savunma mekanizmasıdır. Bu dersin temel amacı; besin ögelerinin bağışıklık hücrelerinin gelişimi, proliferasyonu, sinyal iletimi ve enflamatuar yanıtları üzerindeki moleküler etkilerini incelemektir. Öğrenciler, akut enflamasyon ile düşük dereceli kronik sistemik enflamasyon arasındaki farkı kavrar ve kritik cerrahi, sepsis, kanser kakeksisi ve otoimmün hastalıklarda immünonütrisyon protokollerinin kanıta dayalı klinik yönetimini öğrenirler.

## 📚 Haftalık Konu Dağılımı ve İmmünomodülasyon Modülleri
- **Hafta 1:** Bağışıklık Sistemine Genel Bakış: Doğuştan (Doğal) ve Edinilmiş (Kazanılmış) Bağışıklık Mekanizmaları.
- **Hafta 2:** İmmünometabolizmaya Giriş: Lökosit Aktivasyonunda Glikoliz ve Oksidatif Fosforilasyon Değişimi.
- **Hafta 3:** Makro Besin Ögeleri ve Bağışıklık: Protein-Enerji Malnütrisyonunun İmmün Supresyona Etkisi.
- **Hafta 4:** İmmünonütrientler I: Glutamin, Arjinin ve Nükleotidlerin Mukozal Bariyer ve T Hücre Fonksiyonları.
- **Hafta 5:** İmmünonütrientler II: Omega-3 Yağ Asitleri (EPA/DHA), Eikozanoidler ve Rezolvin/Proktin Yolağı.
- **Hafta 6:** Mikro Besin Ögeleri ve İmmün Savunma: Çinko, Demir, Selenyum, A, C ve D Vitaminlerinin Rolü.
- **Hafta 7:** Bağırsak Mikrobiyotası ve Mukozal Bağışıklık (GALT): Kısa Zincirli Yağ Asitleri ve İmmün Tolerans.
- **Hafta 8:** Cerrahi, Travma ve Yanık Vakalarında Perioperatif İmmünonütrisyon Stratejileri.
- **Hafta 9:** Kronik Düşük Dereceli Enflamasyon ve Metabolik Sendrom (Metainflamasyon): Obezitede İmmün Cevap.
- **Hafta 10:** Otoimmün Hastalıklarda (Çölyak, Crohn, Romatoid Artrit) Beslenme Tedavisi ve İmmünomodülasyon.

## 🏆 Temel Öğrenme Çıktıları ve Klinik Kazanımlar
- Besin ögesi eksikliklerinin bağışıklık fonksiyonları üzerindeki patofizyolojik etkilerini değerlendirebilme.
- Kritik hastalarda ve majör cerrahi operasyon öncesinde/sonrasında immünonütrisyon ürünlerinin endikasyon ve kontrendikasyonlarını belirleyebilme.
- Mikrobiyota-bağırsak-immün eksenini regüle edecek kanıta dayalı prebiyotik, probiyotik ve diyet modelleri planlayabilme.
- ESPEN ve ASPEN immünonütrisyon klinik uygulama kılavuzlarını vaka analizlerine entegre edebilme.

## 📖 Temel Başvuru Kaynakları
- Calder, P. C., & Yaqoob, P. (Eds.). (2013). *Diet, Immunity and Inflammation*. Woodhead Publishing.
- Calder, P. C. (2021). Nutrition and immunity: lessons for COVID-19. *European Journal of Clinical Nutrition*, 75(9), 1309-1318.
- ESPEN Guidelines on Clinical Nutrition in Surgery & Critical Care.
- Abbas, A. K., Lichtman, A. H., & Pillai, S. (2021). *Cellular and Molecular Immunology (10th ed.)*. Elsevier.
""",

    "06-yetiskin-hastaliklarinda-diyet-tedavisi.md": """
## 🎯 Dersin Amacı ve Klinik Diyet Tedavisi
Bu ders, klinik diyetisyenlik eğitiminin omurgasını oluşturan en temel mesleki uzmanlık modülüdür. Amacı; yetişkinlerde sık görülen akut ve kronik hastalıklarda (obezite, tip 1 ve tip 2 diyabet, hipertansiyon, dislipidemi, metabolik sendrom, gastrointestinal sistem hastalıkları, karaciğer, safra kesesi, pankreas, böbrek hastalıkları ve onkoloji) kanıta dayalı Tıbbi Beslenme Tedavisi (TBT) ilkelerini öğretmektir. Öğrenciler, Uluslararası Beslenme Bakım Süreci (Nutrition Care Process - NCP) basamaklarını uygulayarak vaka simülasyonları üzerinden kapsamlı klinik diyet planlama yetkinliği kazanırlar.

## 📚 Haftalık Konu Dağılımı ve Klinik Alanlar
- **Hafta 1:** Beslenme Bakım Süreci (NCP) Basamakları: Değerlendirme, Tanı (PES), Müdahale, İzleme ve Değerlendirme.
- **Hafta 2:** Obezite Patofizyolojisi, Nöroendokrin Regülasyon (Leptin/Ghrelin) ve Enerji Dengesi.
- **Hafta 3:** Obezitede Kanıta Dayalı Tıbbi Beslenme Tedavisi, Davranış Değişikliği ve Farmakoterapi Entegrasyonu.
- **Hafta 4:** Bariatrik Cerrahi (Sleeve Gastrektomi, Gastrik Bypass) Öncesi ve Sonrası Kademeli Beslenme Protokolleri.
- **Hafta 5:** Diyabet Patofizyolojisi: İnsülin Direnci, Prediyabet, Tip 1 ve Tip 2 DM, Gestasyonel Diyabet.
- **Hafta 6:** Diyabette TBT ve İleri Karbonhidrat Sayımı: İnsülin/Karbonhidrat Oranı ve Düzeltme Faktörü Hesaplama.
- **Hafta 7:** Kardiyovasküler Hastalıklar ve Ateroskleroz: Lipid Profili, Endotelyal Disfonksiyon ve Diyet Yağları.
- **Hafta 8:** Hipertansiyon Patofizyolojisi ve DASH Diyeti İlkeleri: Sodyum, Potasyum ve Vasküler Yanıtlar.
- **Hafta 9:** Üst Gastrointestinal Sistem Hastalıkları: Reflü (GÖRH), Gastrit, Peptik Ülser ve Disfaji Yönetimi.
- **Hafta 10:** Alt GİS Hastalıkları: İBS, Çölyak, İnflamatuar Bağırsak Hastalıkları (Crohn, Ülseratif Kolit) ve Düşük FODMAP.
- **Hafta 11:** Hepatosteatoz (NAFLD/MASLD), Siroz ve Karaciğer Yetmezliğinde Nütrisyonel Yönetim.
- **Hafta 12:** Kronik Böbrek Hastalığı (KBH), Hemodiyaliz ve Periton Diyalizinde Elektrolit/Protein Kısıtlamaları.

## 🏆 Temel Öğrenme Çıktıları ve Klinik Yetkinlikler
- Hasta biyokimyasal lab sonuçlarını, antropometrik ölçümlerini ve klinik öyküsünü multidisipliner değerlendirebilme.
- Standart NCP terminolojisini (PES cümleleri) kullanarak uluslararası standartlarda beslenme tanısı koyabilme.
- Karmaşık komorbiditeleri (örn. Diyabet + KBH + Hipertansiyon) olan hastalara bireyselleştirilmiş TBT menüsü planlayabilme.
- ADA, EASD, ESC, KDIGO ve ESPEN klinik uygulama kılavuzlarını klinik karar verme mekanizmasına dahil edebilme.

## 📖 Temel Başvuru Kaynakları
- Raymond, J. L., & Morrow, K. (2020). *Krause and Mahan's Food & the Nutrition Care Process (15th ed.)*. Elsevier.
- American Diabetes Association (ADA). Standards of Care in Diabetes (Güncel Yıl Kılavuzu).
- European Society of Cardiology (ESC) & EASD Kardiyovasküler ve Metabolik Hastalık Kılavuzları.
- KDIGO Clinical Practice Guideline for Diabetes Management in Chronic Kidney Disease.
""",

    "07-enteral-ve-parenteral-beslenme.md": """
## 🎯 Dersin Amacı ve İleri Klinik Nütrisyon
Oral besin alımı anatomik, fonksiyonel veya nörolojik engeller nedeniyle yetersiz veya imkansız olan kritik ve kronik hastalarda, yaşam desteğinin en kritik bileşeni yapay beslenmedir. Bu dersin temel amacı; diyetisyen adaylarına enteral nütrisyon (tüple beslenme) ve parenteral nütrisyon (intravenöz beslenme) yollarının endikasyonlarını, ürün bileşimlerini, erişim yollarını, infüzyon protokollerini ve olası komplikasyonların klinik yönetimini öğretmektir. Öğrenciler yoğun bakım, cerrahi ve palyatif bakım kliniklerinde ESPEN ve ASPEN standartlarına uygun nütrisyonel destek ekibi (NST) üyesi olma yetkinliği kazanırlar.

## 📚 Haftalık Konu Dağılımı ve Klinik Protokoller
- **Hafta 1:** Klinik Nütrisyon Desteğine Giriş: Malnütrisyon Taraması (NRS-2002, MUST, GLIM Kriterleri).
- **Hafta 2:** Enteral Beslenme (EN) Endikasyonları, Kontrendikasyonları ve 'Bağırsağı Kullan' Prensibi.
- **Hafta 3:** Enteral Erişim Yolları: Nazogastrik, Nazojejunal, PEG (Perkütan Endoskopik Gastrostomi) ve PEJ.
- **Hafta 4:** Enteral Ürün Sınıflandırması: Polimerik, Oligomerik (Semielemental), Elementel ve Hastalığa Özel Formüller.
- **Hafta 5:** Enteral İnfüzyon Yöntemleri: Bolus, Aralıklı (İntermittan) ve Sürekli Pompa İnfüzyonu Protokolleri.
- **Hafta 6:** Enteral Beslenmenin Gastrointestinal, Mekanik ve Metabolik Komplikasyonları ve Çözüm Yolları.
- **Hafta 7:** Parenteral Beslenme (PN) Endikasyonları: Santral ve Periferik Venöz Erişim Yolları.
- **Hafta 8:** Parenteral Çözelti Bileşenleri: Dekstroz, Amino Asitler, Lipid Emülsiyonları, Elektrolitler ve Vitaminler.
- **Hafta 9:** Total Parenteral Beslenme (TPN) Hesaplama Atölyesi: Osmolarite, Enerji/Azot Oranı ve İnfüzyon Hızı.
- **Hafta 10:** Yeniden Besleme Sendromu (Refeeding Syndrome): Patofizyoloji, Hipofosfatemi Riski ve Profilaksi.
- **Hafta 11:** Kritik Yoğun Bakım Hastasında Nütrisyon: Hipermetabolizma, İndirekt Kalorimetri ve Protein Hedefleri.
- **Hafta 12:** Evde Enteral ve Parenteral Beslenme (HEN/HPN) Yönetimi ve Taburculuk Sonrası İzlem.

## 🏆 Temel Öğrenme Çıktıları ve Yetkinlikler
- Yatan ve yoğun bakım hastalarında malnütrisyon derecesini GLIM standartlarıyla teşhis edebilme.
- Hastanın gastrointestinal fonksiyonuna göre en uygun yapay beslenme yolunu (EN vs PN) ve tüp erişimini seçebilme.
- Hastanın klinik durumuna göre polimerik, lifli, immünomodülatör veya böbrek/karaciğer spesifik ürün reçete edebilme.
- TPN solüsyonlarının makro ve mikro besin ögelerini mililitre ve gram bazında hatasız formüle edebilme.

## 📖 Temel Başvuru Kaynakları
- Singer, P., et al. (2019). ESPEN guideline on clinical nutrition in the intensive care unit. *Clinical Nutrition*, 38(1), 38-79.
- Cederholm, T., et al. (2019). GLIM criteria for the diagnosis of malnutrition. *Clinical Nutrition*, 38(1), 1-9.
- Mueller, C. M. (Ed.). (2017). *The ASPEN Adult Nutrition Support Core Curriculum (3rd ed.)*. ASPEN.
- Sobotka, L. (Ed.). (2019). *Basics in Clinical Nutrition (5th ed.)*. Galen / ESPEN.
"""
}

# Enrichments for English teaching files
EN_ENRICHMENTS = {
    "01-computer-and-ai-applications.md": """
## 🎯 Course Aim & Pedagogical Scope
This course is designed to equip undergraduate nutrition and dietetics students with foundational and advanced competencies in artificial intelligence (AI), machine learning (ML), large language models (LLMs), and dietary data analytics. Students learn to critically evaluate and deploy modern computational tools for nutrient composition databases, personalized meal planning, automated dietary intake logging, clinical literature synthesis via scientific APIs, and evidence-based patient communication materials.

## 📚 Weekly Curriculum & Hands-on Modules
- **Week 1:** Digital Health and Nutritional Informatics: Historical Overview and Current Landscape.
- **Week 2:** AI, Machine Learning, and Deep Learning Architectures: Core Principles for Dietetic Practice.
- **Week 3:** Food Composition Databases (USDA FoodData Central, TürKomp) and RESTful API Integration.
- **Week 4:** Natural Language Processing (NLP) and LLMs: Summarizing Medical Records and Client Intake Forms.
- **Week 5:** Algorithmic Meal Planning and Linear Programming for Dietary Exchange Optimization.
- **Week 6:** Advanced Scientific Literature Retrieval: AI-Assisted Evidence Synthesis and Bibliometric Tools.
- **Week 7:** Digital Health Platforms, Mobile Food Logging Applications, and Wearable Sensor Telemetry.
- **Week 8:** Health Data Visualization: Infographic Creation, Dashboard Design, and Client Educational Media.
- **Week 9:** Introduction to Nutritional Bioinformatics: Omics Data and Precision Nutrition Algorithms.
- **Week 10:** Algorithmic Bias, AI Hallucinations, Data Privacy (GDPR/HIPAA), and Professional Dietetic Ethics.

## 🏆 Learning Outcomes & Professional Competencies
- Validate and critically audit AI-generated dietary recommendations against biochemical and clinical standards.
- Navigate and query digital nutrient databases and statistical packages in clinical dietetics.
- Synthesize patient-generated health data from mobile trackers into actionable clinical insights.
- Uphold stringent patient data confidentiality, intellectual property standards, and professional accountability.

## 📖 Key Reference Textbooks & Guidelines
- Topol, E. (2019). *Deep Medicine: How Artificial Intelligence Can Make Healthcare Human Again*. Basic Books.
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach (4th ed.)*. Pearson.
- Academy of Nutrition and Dietetics (AND) Position Papers on Health Informatics and Telehealth.
- WHO Guidance on Ethics and Governance of Artificial Intelligence for Health (2021).
""",

    "02-psychosocial-aspects-of-nutrition.md": """
## 🎯 Course Aim & Biopsychosocial Framework
Human eating behavior is profoundly shaped by an intricate interplay of emotional, cultural, neurobiological, and environmental influences. The primary goal of this course is to provide dietetics students with an evidence-based biopsychosocial understanding of eating behaviors. Students explore the psychology of food choice, homeostatic versus hedonic hunger pathways, the neural reward circuitry of ultra-processed foods, body image dissatisfaction, and compassionate client counseling models.

## 📚 Weekly Topics & Clinical Seminars
- **Week 1:** The Biopsychosocial Model of Eating Behavior: Evolutionary Drivers in Modern Food Environments.
- **Week 2:** Neurobiology of Appetite and Satiety: Homeostatic Signaling vs. Hedonic Reward Pathways.
- **Week 3:** Sociocultural Determinants of Dietary Habits: Family Systems, Social Class, and Cultural Traditions.
- **Week 4:** Body Image Development, Media Idealization, and Social Comparison Mechanisms.
- **Week 5:** Disordered Eating Spectrum: Emotional Eating, Night Eating Syndrome, and Restrictive Dieting.
- **Week 6:** Clinical Eating Disorders: DSM-5 Diagnostic Criteria for Anorexia Nervosa, Bulimia Nervosa, and BED.
- **Week 7:** Orthorexia Nervosa: When Clean Eating Becomes Obsessive and Detrimental.
- **Week 8:** Weight Stigma and Healthcare Bias: Clinical Impacts and Non-Stigmatizing Communication.
- **Week 9:** GLP-1 Receptor Agonists: Psychological and Behavioral Dimensions of Medical Appetite Suppression.
- **Week 10:** Mindful Eating and Intuitive Eating: Principles, Clinical Evidence, and Counseling Tools.

## 🏆 Core Competencies & Learning Outcomes
- Screen and assess emotional triggers, disordered eating attitudes, and dietary rigidity in clinical consultations.
- Differentiate between subclinical disordered eating patterns and DSM-5 eating disorders for prompt psychiatric referral.
- Adopt a compassionate, weight-inclusive, and evidence-informed counseling approach in dietetic practice.
- Administer and evaluate validated psychometric scales including EAT-26, ORTO-15, and DEBQ.

## 📖 Key References & Textbooks
- Fairburn, C. G. (2008). *Cognitive Behavior Therapy and Eating Disorders*. Guilford Press.
- Tribole, E., & Resch, E. (2020). *Intuitive Eating: A Revolutionary Anti-Diet Approach (4th ed.)*. St. Martin's Essentials.
- American Psychiatric Association (APA). (2013). *DSM-5: Diagnostic and Statistical Manual of Mental Disorders*.
- Tylka, T. L., et al. (2014). The weight-inclusive approach to health. *Journal of Obesity*, 2014.
""",

    "03-nutrition-and-media.md": """
## 🎯 Course Aim & Scientific Media Literacy
In an era dominated by rapid digital communication, nutritional misinformation and health fraud present substantial risks to public health. This course aims to equip future dietitians with critical media literacy skills, enabling them to deconstruct sensationalized dietary headlines, identify commercial conflicts of interest, and translate complex clinical literature into clear, engaging, and scientifically rigorous public communication.

## 📚 Weekly Syllabus & Analytical Modules
- **Week 1:** Principles of Public Health Communication: The Dietitian's Role as a Trusted Scientific Voice.
- **Week 2:** Nutrition Journalism and Media Sensationalism: Deconstructing 'Superfood' Myths and Miracle Cures.
- **Week 3:** Misinterpretation of Scientific Studies: Confounding Factors and the Correlation vs. Causation Fallacy.
- **Week 4:** Social Media Algorithms, Echo Chambers, and Health Infodemics: Combatting Digital Misinformation.
- **Week 5:** Dietary Supplement Marketing, Regulatory Oversight, and Health Claims (FDA, EFSA, National Guidelines).
- **Week 6:** Influencer Culture, Sponsored Content, and Hidden Commercial Endorsements.
- **Week 7:** The Food Industry and Research Funding: Corporate Sponsorship, Industry Bias, and Conflict of Interest.
- **Week 8:** Science Communication Craft: Translating Molecular Nutrition into Accessible Public Infographics.
- **Week 9:** Crisis Communication in Food Safety: Outbreaks, Food Recalls, and Public Anxiety Management.
- **Week 10:** Digital Personal Branding for Healthcare Professionals, Scientific Ethics, and Fact-Checking Toolkits.

## 🏆 Key Learning Outcomes & Professional Skills
- Evaluate media nutrition claims against the hierarchy of scientific evidence (meta-analyses vs. in vitro studies).
- Identify regulatory violations, unsubstantiated claims, and deceptive marketing in nutritional supplement advertising.
- Author compelling, evidence-based, and legally compliant public nutrition content across print and digital media.
- Serve as active public health advocates and science communicators against nutritional pseudoscience.

## 📖 Recommended References & Readings
- Goldacre, B. (2009). *Bad Science: Quacks, Hacks, and Big Pharma Flacks*. Faber and Faber.
- Nestle, M. (2018). *Unsavory Truth: How Food Companies Skew the Science of What We Eat*. Basic Books.
- Nelson, D. E., et al. (2009). *Making Data Talk: Communicating Public Health Data to the Public, Policy Makers, and the Press*. Oxford University Press.
""",

    "04-dietary-principles-and-popular-diets.md": """
## 🎯 Course Aim & Evidence-Based Diet Evaluation
This course explores human dietary patterns from evolutionary origins to modern commercial and clinical diet trends. Students systematically investigate popular dietary paradigms—including the Ketogenic diet, Intermittent Fasting / Time-Restricted Eating, Mediterranean Diet, Paleolithic diet, Carnivore diet, Low-FODMAP protocol, and plant-based models—evaluating their underlying metabolic mechanisms, endocrine impacts, microbiome alterations, and long-term cardiometabolic safety profiles.

## 📚 Weekly Curriculum & Dietary Paradigms
- **Week 1:** Human Dietary Evolution: From Ancestral Foraging to the Industrial Ultra-Processed Food Paradigm.
- **Week 2:** Energy Balance Models (CICO) vs. The Carbohydrate-Insulin Model (CIM): Biochemical Perspectives.
- **Week 3:** The Mediterranean Dietary Pattern: Polyphenols, Lipid Fractions, and Cardiovascular Longevity.
- **Week 4:** Intermittent Fasting and Time-Restricted Eating: Autophagy, Insulin Sensitivity, and Circadian Rhythms.
- **Week 5:** Ketogenic and Very-Low-Carbohydrate Diets: Hepatic Ketogenesis, Epilepsy, and Metabolic Flexibility.
- **Week 6:** Plant-Based and Vegan Diets: Gut Microbiome Diversity, Nutrient Deficiencies, and Cardiovascular Outcomes.
- **Week 7:** Paleolithic and Carnivore Diets: Anthropological Premises, Saturated Fat Intake, and Fiber Absence.
- **Week 8:** Therapeutic Elimination Diets: Low-FODMAP Protocol, Autoimmune Protocol (AIP), and Histamine Intolerance.
- **Week 9:** Dietary Approaches to Stop Hypertension (DASH Diet): Electrolyte Homeostasis and Vascular Dynamics.
- **Week 10:** Long-Term Diet Adherence, Weight Cycling (Yo-Yo Effect), and Precision Dietary Personalization.

## 🏆 Clinical Competencies & Learning Outcomes
- Explain the precise biochemical and hormonal adaptations triggered by distinct dietary macronutrient splits.
- Critically appraise clinical trial evidence and systematic reviews investigating popular dietary interventions.
- Formulate personalized, sustainable, and nutritionally complete dietary plans tailored to patient clinical profiles.
- Anticipate, monitor, and mitigate micronutrient deficiencies and metabolic risks associated with restrictive diets.

## 📖 Key Reference Textbooks & Guidelines
- Ross, A. C., et al. (2014). *Modern Nutrition in Health and Disease (11th ed.)*. Lippincott Williams & Wilkins.
- Willett, W. (2012). *Nutritional Epidemiology (3rd ed.)*. Oxford University Press.
- Lieberman, D. E. (2014). *The Story of the Human Body: Evolution, Health, and Disease*. Vintage.
- Dietary Guidelines for Americans & European Guidelines on Cardiovascular Disease Prevention.
""",

    "05-immune-system-and-immunonutrition.md": """
## 🎯 Course Aim & Immunometabolic Science
The immune system is an energetically demanding and biochemically sophisticated defense network. This course investigates how specific macro- and micronutrients modulate leukocyte development, cell signaling cascades, mucosal barrier integrity, and systemic inflammatory responses. Students examine the transition from acute protective inflammation to chronic low-grade metaflammation and master evidence-based immunonutrition strategies across critical illness, major surgery, oncological cachexia, and autoimmune disorders.

## 📚 Weekly Topics & Immunonutrition Modules
- **Week 1:** Overview of Immune Function: Innate and Adaptive Immunity Pathways and Cellular Effectors.
- **Week 2:** Introduction to Immunometabolism: Warburg Glycolysis, Oxidative Phosphorylation, and T Cell Activation.
- **Week 3:** Macronutrients and Immune Competence: Protein-Energy Malnutrition and Secondary Immune Deficiency.
- **Week 4:** Specialized Immunonutrients I: Glutamine, Arginine, and Nucleotides in Mucosal Defense and Wound Healing.
- **Week 5:** Specialized Immunonutrients II: Omega-3 Fatty Acids (EPA/DHA), Eicosanoids, Resolvins, and Protectins.
- **Week 6:** Micronutrients in Immune Regulation: Zinc, Iron, Selenium, Vitamin A, Vitamin C, and Vitamin D.
- **Week 7:** The Gut Microbiome and Mucosal Immunity (GALT): Short-Chain Fatty Acids and Regulatory T Cell Induction.
- **Week 8:** Perioperative Immunonutrition in Surgical and Trauma Patients: Reducing Postoperative Sepsis.
- **Week 9:** Metaflammation and Chronic Low-Grade Systemic Inflammation in Obesity and Type 2 Diabetes.
- **Week 10:** Nutritional Modulation in Autoimmune Diseases: Celiac Disease, Crohn's Disease, and Rheumatoid Arthritis.

## 🏆 Learning Outcomes & Clinical Competencies
- Evaluate the immunological repercussions of clinical malnutrition and specific micronutrient deficits.
- Formulate evidence-based immunonutrition interventions for surgical oncology and intensive care patients.
- Leverage dietary polyphenols, fibers, and fatty acids to target gut mucosal integrity and inflammatory cascades.
- Apply clinical practice guidelines from ESPEN and ASPEN on immunonutrition to complex clinical patient scenarios.

## 📖 Recommended References & Scientific Literature
- Calder, P. C., & Yaqoob, P. (Eds.). (2013). *Diet, Immunity and Inflammation*. Woodhead Publishing.
- Calder, P. C. (2021). Nutrition and immunity: lessons for COVID-19. *European Journal of Clinical Nutrition*, 75(9), 1309-1318.
- ESPEN Practical Guideline: Clinical Nutrition in Surgery & Intensive Care.
- Abbas, A. K., Lichtman, A. H., & Pillai, S. (2021). *Cellular and Molecular Immunology (10th ed.)*. Elsevier.
""",

    "06-medical-nutrition-therapy.md": """
## 🎯 Course Aim & Clinical MNT Competencies
Medical Nutrition Therapy (MNT) is the foundational clinical discipline of dietetics practice. This rigorous course prepares students to deliver comprehensive, evidence-based nutrition care to adult patients suffering from acute and chronic diseases, including obesity, metabolic syndrome, prediabetes, type 1 and type 2 diabetes, cardiovascular disease, renal failure, hepatic disorders, and gastrointestinal pathologies. Students utilize the standardized Nutrition Care Process (NCP) to conduct nutrition assessments, formulate PES diagnoses, design medical diet plans, and evaluate clinical outcomes.

## 📚 Comprehensive Weekly Clinical Modules
- **Week 1:** The Nutrition Care Process (NCP) and Model: Assessment, PES Diagnostic Statements, and Monitoring.
- **Week 2:** Obesity Pathophysiology: Neuroendocrine Dysregulation (Leptin, Ghrelin, GLP-1) and Energy Expenditure.
- **Week 3:** Evidence-Based Medical Nutrition Therapy for Weight Management, Behavioral Therapy, and Pharmacotherapy.
- **Week 4:** Bariatric and Metabolic Surgery: Pre- and Post-Operative Nutritional Protocols and Long-Term Supplementation.
- **Week 5:** Diabetes Mellitus Spectrum: Pathophysiology of Type 1, Type 2, and Gestational Diabetes.
- **Week 6:** Advanced Carbohydrate Counting in Diabetes: Insulin-to-Carbohydrate Ratios and Correction Factors.
- **Week 7:** Atherosclerotic Cardiovascular Disease: Dyslipidemia, Lipoprotein Subfractions, and Endothelial Health.
- **Week 8:** Hypertension Pathophysiology and Vascular Hemodynamics: The DASH Diet and Sodium Homeostasis.
- **Week 9:** Upper Gastrointestinal Disorders: GERD, Peptic Ulcer Disease, Gastric Dysmotility, and Dysphagia Management.
- **Week 10:** Lower Gastrointestinal Pathologies: Celiac Disease, IBD (Crohn's, Ulcerative Colitis), and IBS Low-FODMAP Protocols.
- **Week 11:** Hepatic, Biliary, and Pancreatic Diseases: MASLD/MASH, Cirrhosis, Hepatic Encephalopathy, and Pancreatitis.
- **Week 12:** Chronic Kidney Disease (CKD): Glomerular Filtration, Protein Modification, Potassium, and Phosphorus Control.

## 🏆 Key Clinical Learning Outcomes
- Interpret laboratory biomarkers, anthropometric parameters, and pharmacotherapy interactions in complex clinical cases.
- Draft standardized, internationally compliant PES diagnosis statements using the eNCPT terminology.
- Design precision medical nutrition therapy prescriptions for multimorbid clinical patients.
- Integrate the latest clinical guidelines from ADA, KDIGO, ESC, and ESPEN into patient-centered care plans.

## 📖 Required Clinical Textbooks & Guidelines
- Raymond, J. L., & Morrow, K. (2020). *Krause and Mahan's Food & the Nutrition Care Process (15th ed.)*. Elsevier.
- American Diabetes Association (ADA). Standards of Care in Diabetes.
- KDIGO Clinical Practice Guideline for Diabetes Management in Chronic Kidney Disease.
- ESC/EAS Guidelines for the Management of Dyslipidaemias.
""",

    "07-enteral-and-parenteral-nutrition.md": """
## 🎯 Course Aim & Specialized Nutrition Support
When disease, surgical intervention, or functional impairment prevents adequate voluntary oral nutrient intake, specialized nutrition support becomes a critical life-saving clinical therapy. This advanced clinical course covers the indications, contraindications, formulas, access techniques, infusion regimens, and complication management of Enteral Nutrition (EN) and Parenteral Nutrition (PN). Students are trained to function as vital members of multidisciplinary Nutrition Support Teams (NST) adhering strictly to ESPEN and ASPEN clinical standards.

## 📚 Detailed Syllabus & Clinical Formulations
- **Week 1:** Clinical Malnutrition Screening and Assessment: Utilizing NRS-2002, MUST, and Global GLIM Criteria.
- **Week 2:** Enteral Nutrition (EN) Principles: Indications, Contraindications, and Gut Mucosal Barrier Preservation.
- **Week 3:** Enteral Access Modalities: Nasogastric, Nasojejunal, PEG (Percutaneous Endoscopic Gastrostomy), and PEJ.
- **Week 4:** Commercial Formula Classification: Polymeric, Oligomeric (Semi-Elemental), Elemental, and Disease-Specific Blends.
- **Week 5:** Enteral Administration Protocols: Continuous Infusion, Intermittent Gravity, and Bolus Syringe Methods.
- **Week 6:** Enteral Complications: Prevention and Management of Aspiration, Diarrhea, Tube Occlusion, and Metabolic Shifts.
- **Week 7:** Parenteral Nutrition (PN) Indications: Peripheral vs. Central Venous Catheter Access (PICC, Hickman, Ports).
- **Week 8:** PN Substrate Compounding: Dextrose, Crystalline Amino Acids, Injectable Lipid Emulsions, and Micronutrients.
- **Week 9:** Total Parenteral Nutrition (TPN) Formulation Workshop: Osmolarity Calculations, Calorie-to-Nitrogen Ratios.
- **Week 10:** Refeeding Syndrome: Molecular Pathophysiology, Hypophosphatemia Prevention, and Electrolyte Replacement.
- **Week 11:** Critical Care Nutrition in the ICU: Hypermetabolism, Indirect Calorimetry, and Target Protein Delivery.
- **Week 12:** Home Enteral and Parenteral Nutrition (HEN/HPN) Transition, Patient Education, and Monitoring.

## 🏆 Learning Competencies & Clinical Outcomes
- Diagnose the phenotypic and etiologic criteria of disease-related malnutrition using the GLIM framework.
- Formulate personalized enteral feeding regimens specifying target volume, flow rate, and water flushes.
- Compound total parenteral nutrition prescriptions calculating dextrose delivery rates, nitrogen balance, and lipid limits.
- Anticipate, prevent, and treat mechanical, gastrointestinal, and metabolic complications of specialized nutrition support.

## 📖 Key Clinical References & Practice Guidelines
- Singer, P., et al. (2019). ESPEN guideline on clinical nutrition in the intensive care unit. *Clinical Nutrition*, 38(1), 38-79.
- Cederholm, T., et al. (2019). GLIM criteria for the diagnosis of malnutrition. *Clinical Nutrition*, 38(1), 1-9.
- Mueller, C. M. (Ed.). (2017). *The ASPEN Adult Nutrition Support Core Curriculum (3rd ed.)*. ASPEN.
- Sobotka, L. (Ed.). (2019). *Basics in Clinical Nutrition (5th ed.)*. Galen / ESPEN.
"""
}

def enrich_files():
    # 1. TR teaching files
    for fname, addition in TR_ENRICHMENTS.items():
        fpath = os.path.join(CONTENT_DIR, "tr/teaching", fname)
        if not os.path.exists(fpath):
            print(f"Skipping missing {fpath}")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Don't add if already added
        if "Dersin Amacı" in content:
            print(f"Already enriched: {fname}")
            continue
            
        # Append before any existing slides/links or at end
        # We can append right after frontmatter
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = f"---{parts[1]}---"
            body = parts[2].strip()
            new_content = f"{fm}\n\n{addition.strip()}\n\n{body}\n"
        else:
            new_content = content + "\n\n" + addition.strip() + "\n"
            
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully enriched TR: {fname}")

    # 2. EN teaching files
    for fname, addition in EN_ENRICHMENTS.items():
        fpath = os.path.join(CONTENT_DIR, "en/teaching", fname)
        if not os.path.exists(fpath):
            print(f"Skipping missing {fpath}")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "Course Aim" in content:
            print(f"Already enriched: {fname}")
            continue
            
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = f"---{parts[1]}---"
            body = parts[2].strip()
            new_content = f"{fm}\n\n{addition.strip()}\n\n{body}\n"
        else:
            new_content = content + "\n\n" + addition.strip() + "\n"
            
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully enriched EN: {fname}")

if __name__ == "__main__":
    enrich_files()
