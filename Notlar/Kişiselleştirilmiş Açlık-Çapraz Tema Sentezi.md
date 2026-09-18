---
Tür:
  - Çekirdek
ODAK:
  - "[[Aralıklı Açlık]]"
MEKANİZMA:
  - "[[Sirkadiyen Ritim]]"
DİZİN:
  - "[[00_Aralıklı Açlık ve Açlık Mekanizmaları_MOC]]"
  - "[[00_İnsülin Direnci ve Tip 2 Diyabet_MOC]]"
  - "[[00_Obezite Fenotipleri ve Bireysel Farklılıklar_MOC]]"
ETİKET:
BAĞLANTILI NOTLAR:
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
  - "[[Açlıkta Lipoliz, Ketogenez ve Substrat Partisyonu]]"
  - "[[mTORC1 Sinyalizasyonu ve Açlık-Tokluk Döngüsü]]"
  - "[[Açlıkta Akut Faz Yanıtı ve İmmün Modülasyon]]"
  - "[[Adipoz Doku Endokrin Fonksiyonu ve Adipokin Dinamikleri]]"
  - "[[Epigenetik Programlama ve Gelişimsel Fasting Maruziyeti]]"
  - "[[AMPK–TBK1 Resiprokal Frenleme Devresi Adiposit Kataboliz Kontrolü]]"
  - "[[İnsülin–IRF4 Ekseni Açlıkta Yağ mı Kas mı Kaybedilir?]]"
  - "[[Anksiyete Enerji Akımını Azaltıyor ve Ghrelin Yanıtını Bozuyor]]"
  - "[[Diyet Lipidleri Deride Depolanıyor]]"
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
study_type: "Animal Study"
evidence_direction: "contradictory"
primary_outcome: "Metabolik ve Moleküler Yanıtlar"
p_value_summary: "Raporlanmış"
BESLEDİĞİ NOTLAR:
  - "[[Kişiselleştirilmiş Açlık]]"
  - "[[Aralıklı Açlığın Hücresel ve Moleküler Mekanizmaları]]"
---
> [!abstract]- 🧭 Ontolojik Not & Çevre Radarı
> ```dataviewjs
> await dv.view("00 Kontrol Merkezi/scripts/molecular_radar")
> ```

> [!example]- 🧬 Moleküler & Fizyolojik Yolak Akışı
> ```mermaid
> graph LR
>     A["Enerji Kısıtlaması / Açlık"] --> B["AMPK Aktivasyonu"]
>     B -->|Katabolik Sinyal| C["Lipoliz ve Yağ Oksidasyonu"]
>     B -->|Geri Bildirim| D["TBK1 İndüksiyonu"]
>     D -.->|İnhibisyon / Fren| B
>     E["Kronik Düşük Dereceli İnflamasyon"] -->|Sürekli Yüksek| D
> ```
>
> **Şekil Açıklaması:** Enerji kısıtlaması veya açlıkta aktive olan AMPK, lipoliz ve yağ oksidasyonunu uyarırken aynı zamanda TBK1 indüksiyonunu tetikleyerek negatif bir geri bildirim freni oluşturur; kronik düşük dereceli inflamasyon varlığında ise TBK1 sürekli yüksek kalarak AMPK'yi baskılar ve katabolik yağ yıkımını kilitler.

> **Metodolojik Etiketler:** #finding/contradictory
### İçindekiler

- [[#1. İnflamasyon ↔ İnsülin Direnci — Tek Yön mü, Çok Yollu mu]]
- [[#2. Sirkadiyen Ritim ↔ Lipid-İmmün Metabolizma]]
- [[#3. Plazma ↔ Doku Ayrışması — Kan Testi Yeterli mi]]
- [[#4. Genotip-Epigenotip ↔ Diyet Stresi Etkileşimi]]
- [[#5. Protokol Dozu ↔ Doku Yanıt Eşiği]]
- [[#6. Depot-Spesifiklik — Aynı Vücut, Farklı Kararlar]]
- [[#Kişisel Notlarım]]

---

### 1. İnflamasyon ↔ İnsülin Direnci — Tek Yön mü, Çok Yollu mu

Klasik model, kronik enflamasyonun insülin direncini tetiklediğini varsayar (TNF-α/IL-6 → NF-κB → insülin sinyal bozulması). Bu beş çalışma bu modeli doğrulamakla birlikte, ilişkinin çift yönlü ve doku-spesifik olduğunu gösteriyor. Rossmeislova et al. (2024)'te obez kadınların bazal HOMA-IR'ı yüksek, Matsuda indeksi düşük — klasik kronik IR tablosu. Ama açlık eklendiğinde tablo tersine dönüyor: zayıf kadınlarda _akut_ insülin direnci (AdipoIR/AdipoSLIP artışı, glukoz toleransı bozulması) obez kadınlardan daha şiddetli gelişiyor — yani kronik IR ile akut/fasting-indüklü IR farklı, hatta ters yönlü davranan iki ayrı fenomen. Stefanakis et al. (2024)'te ise leptin artışının doğrudan CRP/CD14 gibi akut faz-insülin direnci ilişkili proteinleri tetiklediği gösteriliyor — leptin burada hem enflamasyonun hem (dolaylı olarak) insülin direncinin ortak bir yukarı-akım tetikleyicisi olarak konumlanıyor. Permataputri et al. (2025)'te ise IFN-γ'nın (insülin direncini NF-κB ve SOCS3 üzerinden kötüleştirdiği bilinen bir sitokin) TRE ile azalması, antropometrik değişiklik olmadan gerçekleşiyor — yani enflamasyon-IR bağlantısı, yağ kaybı gerçekleşmeden de kesilebilir bir döngü olabilir.

---

### 2. Sirkadiyen Ritim ↔ Lipid-İmmün Metabolizma

Sirkadiyen Ritim bu beş çalışmada iki farklı sistemde karşımıza çıkıyor. Permataputri et al. (2025)'te, günlük ve tutarlı TRE protokolünün (18:6) IFN-γ'yı düşürürken, düzensiz/gün-aşırı ADMF protokolünün aynı etkiyi göstermemesi, yazarlar tarafından Bmal1/Clock genlerinin günlük hizalanmasına bağlanıyor. Zhang et al. (2026)'de ise BAT'ın tokluk-spesifik "beyazlaşma" yanıtı, günlük değil 3-döngülük ADF protokolünde gözleniyor ve termonötral koşullarda (30°C) zayıflıyor — yani burada sirkadiyen hizalanmadan çok, sıcaklık/soğuk-stres bağlamı mekanizmayı belirliyor. Bu iki bulgu birlikte okunduğunda önemli bir soru ortaya çıkıyor: fasting protokolünün "düzenliliği" (günlük vs. gün aşırı) immün sistemde sirkadiyen genler üzerinden etkiliyken, aynı düzenliliğin BAT lipid metabolizmasındaki etkisi termal bağlamla iç içe geçmiş olabilir. Bu, kişiselleştirilmiş fasting tasarımında hem protokol frekansının hem ortam sıcaklığının birlikte değerlendirilmesi gerektiğine işaret ediyor.

---

### 3. Plazma ↔ Doku Ayrışması — Kan Testi Yeterli mi

Bu beş çalışmanın belki de en tutarlı ortak mesajı: **dolaşımdaki (plazma) ölçümler, dokudaki gerçek durumu her zaman yansıtmıyor.** Rossmeislova et al. (2024)'te, bazal kan FFA seviyeleri iki grup arasında farksızken, kütleye normalize edilmiş doku-düzeyi FFA akışı (FFA/FM) belirgin şekilde ayrışıyor — salt kan FFA'sına bakan bir klinisyen, obez ve zayıf dokunun aslında ne kadar farklı davrandığını kaçırabilir. Zhang et al. (2026)'de vücut ağırlığı toplamda değişmezken BAT'ın kütlesel beyazlaşması gizli kalıyor — sistemik ölçüt (kilo) doku-düzeyi patolojiyi maskeliyor. Permataputri et al. (2025)'te de antropometrik parametreler (BMI, yağ kütlesi) sıfır değişim gösterirken immün sistemde (IFN-γ) anlamlı bir değişim yaşanıyor — burada "doku" değil ama yine sistemik/görünür ölçüt ile altta yatan fizyolojik değişim arasında bir ayrışma var. Bu üçlü örüntü, 3.1.Sistemik ve Lokal Yanıtın Ayrışması temasının bu derlemedeki en güçlü kanıtlarından biri.

---

### 4. Genotip-Epigenotip ↔ Diyet Stresi Etkileşimi

Klasik "genotip×tedavi etkileşimi" kavramı bu derlemede iki farklı biçimde temsil ediliyor. Yin et al. (2023)'te, hiçbir genotipik varyasyon olmadan, saf epigenetik programlama (DNA metilasyonu) tedaviye (S6K1 kurtarma) verilen yanıtı belirliyor — yani bireyin "genetik profili" değil, gelişimsel dönemde edinilmiş epigenetik ayar noktası, fasting-benzeri bir müdahalenin etkinliğini şekillendiriyor. Zhang et al. (2026)'de ise gerçek bir genetik manipülasyon (Raptor floxed + AAV-Cre) kullanılarak, mTORC1 genotipinin (fonksiyonel vs. nakavt) aynı ADF protokolüne tamamen farklı doku yanıtları ürettiği doğrudan gösteriliyor. Bu iki yaklaşım birlikte, "bireysel modülatör" kavramının yalnızca doğuştan genetik varyantlarla sınırlı olmadığını, edinilmiş epigenetik durumun ve doku-spesifik genetik bağlamın da eşit derecede belirleyici olabileceğini gösteriyor.

---

### 5. Protokol Dozu ↔ Doku Yanıt Eşiği

Aynı genel kategori altındaki ("aralıklı açlık") protokoller, dokuların tepki eşiğini aşıp aşmamasına göre kökten farklı sonuçlar üretebiliyor. Permataputri et al. (2025)'te TRE (günlük 18 saat açlık) IFN-γ'yı düşürürken ADMF (gün aşırı, %25 enerji) hiçbir sitokin değişikliği yaratmıyor — aynı toplam kalori kısıtlaması yaklaşık olarak sağlanmış olsa da, günlük tekrarın frekansı sonucu belirliyor. Zhang et al. (2026)'de 3 döngülük ADF, BAT'ta belirgin bir mTORC1-aracılı beyazlaşma tetikliyor — daha kısa veya daha uzun döngü sayılarının eşiği nasıl etkileyeceği bu çalışmada test edilmemiş, ama sonuçların "kümülatif döngü sayısına" duyarlı olabileceğini düşündürüyor. Yin et al. (2023)'te ise 12 haftalık kronik maternal IF, tek seferlik veya kısa süreli bir müdahalenin yaratamayacağı kalıcı bir epigenetik iz bırakıyor — süre burada yalnızca "doz" değil, geri döndürülebilirlik eşiğini de belirleyen bir faktör.

---

### 6. Depot-Spesifiklik — Aynı Vücut, Farklı Kararlar

Bu beş çalışma toplu olarak, "yağ dokusu" kavramının tekilleştirilemeyeceğini gösteriyor. Zhang et al. (2026)'de BAT ve gWAT aynı ADF protokolüne taban tabana zıt yanıt veriyor. Yin et al. (2023)'te sWAT, rWAT ve eWAT'ın hepsi erkek yavrularda hipertrofi gösterirken, dişi yavrularda yalnızca rWAT etkileniyor — hem depo hem cinsiyet birlikte belirleyici. Rossmeislova et al. (2024) yalnızca abdominal subkutan dokuyu incelemiş olsa da (yazarların kendi belirttiği bir sınırlılık), femoral ve visseral depoların farklı davranabileceğini öngörüyor. Bu üçlü kanıt, "yağ dokusu fasting'e nasıl yanıt verir" sorusunun aslında "_hangi_ yağ dokusu, _hangi_ bireyde" sorusuna dönüştürülmesi gerektiğini gösteriyor — derlemenin 3.2.Depot-specific modeling başlığının merkezi tezini doğrudan destekliyor.