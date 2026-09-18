---
Tür:
  - Besleyici
ODAK:
  - "[[İmmün Sistem]]"
MEKANİZMA:
DİZİN:
  - "[[inflamasyon]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[İnflamasyonun Tanınması-DAMP]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[İmmün Sistem ve İmmünonutrisyon]]"
YORUM:
KAYNAK: 10.1016/j.immuni.2024.03.002
study_type: "Animal Study"
evidence_direction: "positive"
primary_outcome: "Kas Proteolizi ve Substrat Partisyonu"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[İnflamasyonun Tanınması-DAMP]]"
  - "[[İmmün Yanıt ve İnflamasyon Döngüsü]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

**Makale Başlığı:** DAMPs and DAMP-sensing receptors in inflammation and diseases

**Amacı:** Bu derleme, endojen moleküllerin nasıl DAMP'lara dönüştüğünü, bunların hangi reseptörler tarafından algılandığını sınıflandırmayı ve bu reseptörlerin inflamatuar hastalıklardaki klinik önemini özetlemeyi amaçlamaktadır.

Kaynağa göre, inflamasyonu tetikleyen tehlike sinyallerini (DAMP ve PAMP) algılayan reseptörler sadece klasik "Örüntü Tanıma Reseptörleri" (PRR) ile sınırlı değildir. Yazarlar bu reseptörleri genel olarak **"DAMP Algılayıcı Reseptörler" (DAMP-sensing receptors)** çatısı altında toplamış ve üç ana grupta incelemiştir.

İşte kaynakta tanımlanan reseptör aileleri ve spesifik örnekleri:

### 1. Klasik Örüntü Tanıma Reseptörleri (PRR'ler)
Bu grup, hem mikropları (PAMP) hem de vücudun kendi hasar moleküllerini (DAMP) tanıyan en bilinen ailedir.

*   **Toll-Benzeri Reseptörler (TLRs):**
    *   **TLR2 ve TLR4:** Hücre zarında bulunur. HMGB1, ısı şok proteinleri (HSPs), S100 proteinleri ve okside lipidler gibi protein ve lipid bazlı DAMP'ları tanır.
    *   **TLR3, TLR7, TLR8, TLR9:** Endozomlarda bulunur. Hasar görmüş hücrelerden çıkan nükleik asitleri (RNA ve DNA) tanırlar. Örneğin TLR9, mitokondriyal DNA'yı (mtDNA) ve histonları algılar.
*   **C-Tipi Lektin Reseptörleri (CLRs):**
    *   **Dectin-1:** Tümör hücrelerindeki N-glikanları tanır.
    *   **DNGR-1 (CLEC9A):** Nekrotik hücrelerden açığa çıkan F-aktin iskeletini tanır.
    *   **MINCLE:** Hasarlı böbrek hücrelerinden salınan SAP130 proteinini tanır.
    *   **CLEC2D:** Histonları tanıyarak DNA ile birlikte endozoma taşır.
*   **NOD-Benzeri Reseptörler (NLRs):**
    *   **NLRP3:** En kritik metabolik sensördür. ATP, ürik asit kristalleri, kolesterol kristalleri, potasyum düşüşü ve lizozomal hasarı algılar.
    *   **NLRP1:** Ribotoksik stresi (ZAK$\alpha$ aracılığıyla) algılar.
    *   **NLRP10:** Mitokondriyal hasarı ve sızan mtDNA'yı algılar.
*   **RIG-I-Benzeri Reseptörler (RLRs):**
    *   **RIG-I ve MDA5:** Normalde virüsleri tanır ancak koruyucu kılıfı (shielding) bozulmuş endojen RNA'ları (mRNA veya retroviral RNA) da algılayarak inflamasyonu başlatır.
*   **DNA Sensörleri (Sitozolik):**
    *   **cGAS (cyclic GMP-AMP synthase):** Sitozole sızan nükleer veya mitokondriyal DNA'yı algılar.
    *   **AIM2:** DNA'yı algılayarak inflamazom kompleksini kurar.
    *   **ZBP1:** Z-formundaki DNA ve RNA'yı tanır.

### 2. G-Protein Kenetli Reseptörler (GPCRs)
Makale, GPCR'ların DAMP algılamadaki rolünün yeni keşfedildiğini ve özellikle beslenme-metabolizma ilişkisinde çok önemli olduklarını vurgular.

*   **G$\alpha$i Alt Birimli GPCR'lar:**
    *   **GPR34:** Apoptotik nötrofillerden salınan LysoPS lipidini tanır.
    *   **P2Y14:** Glikojen metabolizması ara ürünü UDP-Glukoz'u tanır.
    *   **P2Y12:** ADP'yi tanır.
    *   **FPR1:** Mitokondriyal N-formil peptidleri tanır .
    *   **MC5R:** $\alpha$-MSH hormonunu tanır.
*   **G$\alpha$q Alt Birimli GPCR'lar (Kalsiyum sinyalini yönetirler):**
    *   **P2Y6:** UDP'yi tanır.
    *   **GPR40 (FFAR1):** Serbest yağ asitlerini (örneğin palmitat) tanır.
    *   **CaSR ve GPRC6a:** Hücre dışı kalsiyum seviyelerini algılar.

### 3. Diğer DAMP Algılayıcı Reseptörler
Bu grup, klasik PRR veya GPCR sınıfına girmeyen ancak steril inflamasyonda kritik olan reseptörlerdir.

*   **RAGE (Receptor for Advanced Glycation Endproducts):** İleri glikasyon son ürünlerini (AGEs), HMGB1'i, S100 proteinlerini ve DNA'yı tanır. Diyabet ve damar hasarında merkezdedir.
*   **TREM Ailesi (Triggering Receptor Expressed on Myeloid Cells):**
    *   **TREM1:** HMGB1, aktin ve HSP70'i tanır .
    *   **TREM2:** Hasarlı nöronlardan salınan fosfolipidleri (PA, PC, PS) ve APOE'yi tanır.
*   **CD Molekülleri ve İyon Kanalları:**
    *   **CD36:** Palmitat (doymuş yağ) ve okside lipidleri emer/tanır .
    *   **CD44:** Hiyalüronan parçalarını ve proteoglikanları (biglycan) tanır.
    *   **CD14:** Okside lipidleri (oxPAPC) endozoma taşıyarak algılatır .
    *   **P2X7:** Hücre dışı ATP'yi algılayan iyon kanalıdır (NLRP3 aktivasyonu için kritiktir) .
    *   **OLFR2 (Olfactory Receptor 2):** Damar makrofajlarında lipid peroksidasyon ürünü olan oktanalı (octanal) tanır.

**Özetle:** Kaynakta tanımlanan **10'dan fazla farklı aile** ve bunların altında **30'dan fazla spesifik reseptör** tipi bulunmaktadır. Bir beslenme akademisyeni için özellikle **NLRP3, TLR4, GPR40, CD36 ve RAGE** reseptörleri; besin ögelerinin (yağ asitleri, glikoz ürünleri, kolesterol) bağışıklık sistemini nasıl aktive ettiğini anlamak açısından en stratejik olanlarıdır.

