---
Tür:
  - Besleyici
ODAK:
  - "[[Anksiyete]]"
MEKANİZMA:
  - "[[Enerji Dengesinin Bileşenleri]]"
  - "[[Ghrelin]]"
DİZİN:
  - "[[İştahın Düzenlenmesi]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[GDF15, Anksiyete ve Adipoz Doku]]"
  - "[[Aralıklı Açlığın Etkileri Cinsiyete Göre Ghrelin Etkisiyle Farklılık Gösteriyor, Zararlı da Olabiliyor]]"
  - "[[Kişiselleştirilmiş Açlık-Çapraz Tema Sentezi]]"
  - "[[Stres, enerji dengesi ve adipoz doku modellenmesini etkiliyor]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
  - "[[Beslenmenin Psikososyal Yönleri]]"
YORUM:
KAYNAK: 10.1111/jne.70106
study_type: "Animal Study"
evidence_direction: "null"
primary_outcome: "Metabolik ve Moleküler Yanıtlar"
p_value_summary: "p > 0.05 (anlamsız)"
BESLEDİĞİ NOTLAR:
  - "[[Obezitenin Beyinsel-Merkezi Olarak Düzenlenmesi]]"
  - "[[Enerji Dengesinin Bileşenleri]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Besin Kısıtlaması (Fasting / FMD)"] --> B["İnsülin / IGF-1 Düşüşü & AMPK Artışı"]
>     B --> C["mTORC1 İnhibisyonu & ULK1 Aktivasyonu"]
>     C --> D["Hücresel Otofaji / Mitofaji (Organel Temizliği)"]
>     B --> E["Hepatik Glikojen Boşalması → Ketogenez (Beta-Hidroksibütirat)"]
> ```
>
> **Şekil Açıklaması:** Besin kısıtlaması ve açlık durumunda düşen insülin/IGF-1 ve yükselen AMPK, mTORC1'i inhibe edip ULK1'i aktive ederek hücresel otofaji ve mitofaji (hasarlı organel temizliği) süreçlerini başlatır; eş zamanlı olarak hepatik glikojenin boşalmasıyla ketogenez (Beta-hidroksibütirat üretimi) devreye girer.

> **Metodolojik Etiketler:** #finding/null
**Makale Başlığı:** Stress-induced hyperphagia? Characterising the activity of the ghrelin axis in male rats with high anxiety behaviour

**Amacı:** Çalışma, doğuştan gelen yüksek anksiyete davranışının kendiliğinden yeme davranışı, ghrelin salgılanması ve yetişkin hipokampal nörogenezi (AHN) üzerindeki etkilerini, düşük (LAB) ve yüksek (HAB) anksiyeteli sıçan modelleri üzerinden incelemeyi amaçlamaktadır [1, 2].

---

### 1) Yüksek ve Düşük Anksiyeteli Ratlarda Yeme Davranışı
Çalışma, yüksek anksiyetenin yeme miktarını ve zamanlamasını belirgin şekilde etkilediğini ortaya koymuştur:

*   **Yeme Davranışındaki Değişim:** Yüksek anksiyeteli (HAB) sıçanların toplam günlük besin alımında, düşük anksiyeteli (LAB) sıçanlara kıyasla **%16'lık bir azalma (hipofaji)** gözlemlenmiştir [1, 3]. Ancak bu azalmaya rağmen, yeme olaylarının sayısı veya süresi gibi genel 24 saatlik yeme örüntülerinde radikal bir değişiklik saptanmamıştır [1, 4, 5].
*   **Işık (Light) ve Karanlık (Dark) Faz Etkisi:** Toplam besin alımındaki bu azalmanın temel nedeni, **ışık fazındaki (dinlenme dönemi) besin tüketiminin %35 oranında azalmasıdır** [1, 3]. Karanlık fazdaki tüketim ise anlamlı bir değişim göstermemiştir [3].
*   **Gösterge ve Açıklama:** Bu durum, HAB sıçanlarının günlük besin alımlarının daha büyük bir kısmını karanlık fazda tükettikleri "abartılı bir diurnal profil" sergilediklerini gösterir [3, 5]. Araştırmacılar bu durumu, HAB sıçanlarındaki **kronik stres seviyelerinin yüksekliğine** ve ışık fazında beslenmeye karşı duyulan potansiyel bir **kaçınma/aversiyon** duygusuna bağlamaktadır [6, 7].

### 2) Ghrelin ve Kalorik Kısıtlama (CR) İlişkisi
Çalışmada ghrelin hormonu ve açlık (açlık/kısıtlama durumu) arasındaki ilişki anksiyete düzeyi bağlamında test edilmiştir:

*   **Ghrelin ve Açlık Yanıtı:** Normal şartlarda açlık (24 saatlik fast), LAB sıçanlarında dolaşımdaki ghrelin seviyelerini %57 oranında artırmıştır [4, 8]. Ancak **yüksek anksiyeteli HAB sıçanlarında, açlığın tetiklediği bu ghrelin artışı tamamen ortadan kalkmıştır (abolished)** [4, 9, 10].
*   **Yeme Davranışıyla İlişki:** Ghrelin normalde vücut ağırlığını koruyan ve açlık durumunda besin aramayı tetikleyen bir hormondur [11, 12]. HAB sıçanlarında bu yanıtın körelmiş olması, bu hayvanların açlık sonrası yemeğe başlama sürelerinin (latans) neden daha uzun olduğunu açıklar [12, 13].
*   **Beklenmedik Nörogenez Yanıtı:** Ghrelin normalde yetişkin hipokampal nörogenezini (AHN) artıran bir faktördür; bu nedenle ghrelin yanıtı körelen HAB sıçanlarında nörogenezin düşük olması beklenirdi [13]. Ancak şaşırtıcı bir şekilde, **HAB sıçanlarında AHN'nin %68 ila %103 oranında daha yüksek olduğu** bulunmuştur [4, 14]. Araştırmacılar bunu, yüksek anksiyeteye karşı vücudun geliştirdiği ancak anksiyeteyi dindirmeye yetmeyen "başarısız bir homeostatik yanıt" olarak yorumlamaktadır [15, 16].

### 3) 5 Temel Mesaj ve Akademik Vizyon Değerlendirmesi

**Temel Mesajlar:**
1.  Doğuştan gelen yüksek anksiyete, yeme sıklığını bozmasa da toplam enerji alımını (özellikle aktif olunmayan dönemde) azaltan **hafif bir hipofajiye** yol açar [1, 7].
2.  Yüksek anksiyete, vücudun enerji eksikliğine karşı verdiği **en temel hormonal savunma olan ghrelin artışını felç eder** [4, 10].
3.  Anksiyete düzeyi, bireyin **sirkadiyen beslenme ritmini** (gece/gündüz dengesi) değiştirerek metabolik stresi derinleştirebilir [6].
4.  Düşük ghrelin yanıtına rağmen görülen yüksek nörogenez, beynin kronik strese karşı biyolojik bir **telafi mekanizması** çalıştırmaya çalıştığını ancak bunun anksiyeteyi çözmede yetersiz kaldığını gösterir [15, 16].
5.  Ghrelin sistemi, sadece iştahı değil, anksiyete ile ilişkili **duygusal ve bilişsel süreçleri de** (HPA aksı üzerinden) koordine eden merkezi bir düğüm noktasıdır [17].

**Beslenme Akademisyeni İçin Vizyoner Çıkarımlar:**
Bir beslenme akademisyeni için bu bulgular, "stres yemeği" (hyperphagia) kavramının her birey veya fenotip için geçerli olmadığını, bazı anksiyete türlerinin **iştah baskılanması ve hormonal körelme** ile seyrettiğini anlamak açısından kritiktir [17]. 
*   **Metabolik Esneklik:** Akademisyen, danışanlarında veya çalışmalarında sadece "ne kadar" yendiğine değil, "ne zaman" yendiğine odaklanarak (diurnal değişimler), kişinin içsel stres düzeyine dair biyomarker takibi yapabilir [7]. 
*   **Bireyselleştirilmiş Müdahale:** Ghrelin yanıtı körelmiş yüksek anksiyeteli bireylerde, klasik açlık/oruç (intermittent fasting) protokollerinin beklenen metabolik veya nörolojik faydayı (nörogenez artışı gibi) sağlamayabileceği gerçeğini vizyonuna eklemelidir [15, 16]. #çalışmafikri/deneysel
*   **Gelecek Perspektifi:** Beslenme-psikiyatri ilişkisinde ghrelin aksını, sadece bir iştah mekanizması değil, **duygusal direnç (resilience)** için bir hedef olarak konumlandırabilir [2, 18]. #vizyoner 


Kaynaklara göre, anksiyetenin yeme davranışı ve hormonal yanıtlar üzerindeki etkilerine dair bulgular ve bu bulguların diğer çalışmalarla karşılaştırılması şu şekildedir:

### 1) IF’in Etkisizliği: Bulgu mu, Çıkarım mı?
Çalışmada, Aralıklı Oruç (IF) bir tedavi yöntemi olarak doğrudan test edilmemiştir; ancak **24 saatlik açlığa (fasting) verilen hormonal yanıtlar** doğrudan ölçülmüştür. Bu bağlamda:
*   **Doğrudan Bulgu:** Düşük anksiyeteli (LAB) sıçanlarda 24 saatlik açlık, dolaşımdaki ghrelin seviyelerini %57 artırırken; **yüksek anksiyeteli (HAB) sıçanlarda bu ghrelin artışı tamamen ortadan kalkmıştır (abolished)** [1, 2]. 
*   **Yazarların Çıkarımı:** Yazarlar, ghrelin aktivitesindeki bu azalmanın normalde vücut ağırlığını savunma ve ghrelin bağımlı eylemleri (yetişkin hipokampal nörogenezi - AHN gibi) tetikleme işlevini bozacağını belirtmektedir [3]. 
*   **IF ile İlişkisi:** Önceki bilgilerimiz ve kaynaklardaki "kalorik kısıtlamanın (CR) anksiyolitik etkisinin ghrelin reseptörü (GHSR) aktivasyonuna bağlı olduğu" bulgusu birleştirildiğinde; **ghrelin yanıtı felç olmuş bir organizmada, IF veya CR gibi uygulamaların beklenen nörolojik ve metabolik faydaları sağlamayacağı** bilimsel bir çıkarım olarak öne çıkmaktadır [4-6]. Yazarlar, HAB sıçanlarındaki homeostatik yanıtların (hafif hipofaji ve AHN artışı gibi), bu "güçlü anksiyojenik koşulları" iyileştirmede **yetersiz kaldığını** ifade etmektedir [7].

### 2) Anksiyete ve Yeme Davranışındaki Çelişkili Sonuçlar
Kaynaklar, anksiyete ve beslenme arasındaki ilişkinin "belirsiz" (equivocal) olduğunu ve literatürde çelişkili sonuçlar bulunduğunu açıkça belirtmektedir [8].

*   **Yemeyi Artıran (Hiperphagia) Durumlar:**
    *   Kadınlarda yüksek anksiyete, artan kalori alımı ile ilişkilendirilmiştir [8].
    *   Yenidoğan döneminde anneden ayrılma (maternal separation), ergenlik döneminde başlayan aşırı yeme davranışına yol açabilmektedir [5, 9].
    *   Erken yaş stresörleri genel olarak obezite gelişimiyle bağlantılı bulunmuştur [8].

*   **Yemeyi Azaltan (Hypophagia) veya Değiştirmeyen Durumlar:**
    *   Birçok kemirgen çalışması, **kısıtlama stresinin (restraint stress) besin alımını azalttığını** göstermektedir [5, 8].
    *   Erkeklerde ameliyat öncesi stres ve anksiyetenin besin alımını veya diyet seçimini değiştirmediği gözlemlenmiştir [8, 10].
    *   Bu çalışmanın ana bulgusu olarak, kronik yüksek anksiyeteli erkek sıçanlarda **hafif bir hipofaji** (yeme azalması) saptanmıştır [11-13].

**Yazarlara Göre Çelişkilerin Sebepleri:**
Yazarlar, bu farklı sonuçların birkaç temel nedenden kaynaklandığını savunmaktadır:
1.  **Stresörün Doğası:** Akut stresörlerin iştahı bastırma eğiliminde olduğu, ancak kronik stresin (özellikle bu çalışmadaki gibi genetik bir özellik olarak varsa) farklı diurnal (günlük) profil değişimlerine yol açtığı belirtilmektedir [13].
2.  **Cinsiyet Farklılıkları:** Besin alımı ve anksiyete ilişkisinde cinsiyetin (kadın vs. erkek) kritik bir değişken olduğu vurgulanmıştır [7, 8].
3.  **Zamanlama:** Stresörün yaşamın hangi evresinde (yenidoğan, ergenlik veya yetişkinlik) meydana geldiği, yeme davranışının yönünü (hiper- vs. hipofaji) belirleyebilmektedir [5, 8].
4.  **Diyet İçeriği:** Yüksek anksiyeteli sıçanların, lezzetli (palatable) yüksek yağlı diyetlere karşı daha düşük tercih gösterdiği, bunun da hipotalamik ürokortin-2 seviyeleriyle ilişkili olabileceği not edilmiştir [14, 15].
