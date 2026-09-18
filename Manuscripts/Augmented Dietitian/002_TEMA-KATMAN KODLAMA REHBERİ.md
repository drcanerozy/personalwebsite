# 📋 Kodlama Rehberi — Tema, Fonksiyon, Katman & Aşama (v2)

Bu not, "Artırılmış Diyetisyen" makalesi için literatür kodlama sürecini yönetir. **001_BİRLEŞTİRİLMİŞ VERİLER** notuna dokunulmadı — bu, aynı klasörü farklı alanlarla okuyan ayrı bir dataview.

Her makaleyi okuduktan sonra, o makalenin kendi notundaki frontmatter'da aşağıdaki alanları doldur. Tablo otomatik besleniyor.

**v2 notu:** Claude ve Antigravity'nin bağımsız kodlamalarını karşılaştırınca hem tutarsızlıklar hem de gerçek uydurma (yazar/DOI/bulgu) örnekleri bulundu. Bu sürüm o deneyden çıkan güvenlik kurallarını ve iki modelin çapraz doğrulamasından süzülen düzeltmeleri içeriyor.

---

## 🛡️ GÜVENLİK ADIMLARI — Kodlamaya (kendi yapsan da, bir AI'a yaptırsan da) başlamadan önce

Bu kurallar, hangi araç kodluyor olursa olsun (sen, Claude, Antigravity, başka bir model) geçerli.

**1. Başlık/Yazar/Yıl/DOI'yi ASLA hafızadan tamamlama.** Bu dört alan sadece iki yerden gelebilir: (a) o makalenin kendi Obsidian notunun frontmatter'ı, ya da (b) PDF'in kendisi. Bir modelin "mantıklı görünen ama kontrol edilmemiş" yazar ismi (örn. gerçek yazar "Ga Young Kim, Jung-Sook Seo" iken uydurulan "H. Lee, K. Kim" gibi) veya DOI üretmesi — kaynağa hiç bakılmadığının kanıtıdır. Kural: yazar/DOI alanı doldurulmadan önce mutlaka ilgili notun frontmatter'ı açılıp karşılaştırılır.

**2. Notta veri yoksa, o alanı UYDURMA — "veri yok" yaz.** Methods/Findings/Conclusions alanları boşsa (örn. sadece "Cited By: 5, full text yok" notu varsa), bu makale hakkında akıcı ve özgüvenli bir özet üretmek yasak. Böyle durumlarda `Konu` alanına sadece başlıktan çıkarılabilecek en temkinli tahmin yazılır ve `User_Notes`'a **"veri yetersiz, PDF'e bakılmalı"** eklenir — asla bulgu icat edilmez.

**3. Her `User_Notes` cümlesi, notta gerçekten alıntılanmış bir ifadeye kadar geri izlenebilmeli.** Bir makalenin dar kapsamlı bir cümlesini ("dietitian control is still crucial regarding taste/consumability") geniş bir güvenlik iddiasına ("klinik kullanım denetimsiz risklidir") genişletmek — kaynağı olsa bile — çarpıtmadır. Kendi kendine sor: *"Bu cümleyi makalenin kendi ifadesinden daha geniş bir iddiaya mı çevirdim?"* Cevap evetse, iddiayı makalenin gerçek kapsamına geri çek.

**4. Hiçbir dış modelin (Antigravity dahil) çıktısını doğrulamadan tabloya taşıma.** Bir aracın kodlaması "makul görünüyor" diye doğru değildir. Kısayol: (a) o makalenin gerçek notunu aç, (b) modelin verdiği Sentez Notu'ndaki iddiayı notta geçen alıntılarla karşılaştır, (c) örtüşmüyorsa ya kendi okumanla düzelt ya da PDF'e bak. İki farklı aracın çıktısı çelişiyorsa, "hangisi daha iddialı/kesin konuşuyor" diye seçme — ikisini de kaynakla karşılaştır.

**5. Fonksiyon ayrımı: İletişim ≠ Yaratım.** `İletişim` = diyalog/soru-cevap/koçluk akışı test ediliyor (chatbot bir soruya cevap veriyor). `Yaratım` = somut bir çıktı (menü, tarif, öğün planı, reçete) üretiliyor — bu çıktı sohbet arayüzünden gelse bile fonksiyon Yaratım'dır. Ayrım testi: *"Ölçülen şey diyalog kalitesi mi, yoksa üretilen planın/menünün doğruluğu mu?"*

**6. Derleme/Sistematik-Derleme makalelerinde Konu ayrımı.** Tüm derlemeleri otomatik olarak `performans-değerlendirme`'ye atama — ikisi arasında ayrım yap:
   - Derleme sadece algoritmik metrikleri (doğruluk, AUC, F1) topluyorsa → `performans-değerlendirme`
   - Derleme, klinik karar destek sistemlerinin hastane/pratik iş akışına entegrasyonunu haritalıyorsa → `klinik-işakışı`

**7. "Altın standart" kuralını harfiyen uygula.** Diyetisyen çalışmada sadece **karşılaştırma referansı/hakem** ise (YZ çıktısını puanlıyor, kendisi karar sürecine dahil değil) → `AI-Layer` + `Competency`. Diyetisyen **denetleyici/karar verici** ise (YZ çıktısını değerlendirip kendi kararını ona göre şekillendiriyor) → `Hybrid`. "Diyetisyenler değerlendirdi" ifadesi tek başına Hybrid'e yeterli sebep değildir — değerlendirme bir puanlama mı, yoksa bir karar mı, ona bak.

**8. Kararsız kaldığın her satırı işaretle, atlama.** `User_Notes`'un sonuna `[KARARSIZ]` etiketi eklersen, ikinci bir geçişte (kendi gözünle ya da başka bir modelle) o satırları hızlıca tarayabilirsin — sessizce en "makul" seçeneği seçip geçmek, hatanın fark edilmeden kalmasına yol açar.

---

## ⚡ ÇEKİRDEK — her makalede doldur (hızlı karar, 1-2 dakika)

**1. `Konu` (Tema).** Makale hangi ana eksende?
- `performans-değerlendirme` — YZ aracının doğruluk/güvenilirlik testi (örn. "ChatGPT ne kadar doğru öneriyor"); saf metrik odaklı derlemeler de burada (bkz. Güvenlik Adımı 6)
- `benimseme-kimlik` — diyetisyenlerin tutumu, direnç, meslek kimliği tehdidi, TAM/UTAUT, benimseme engelleri (hasta/klinisyen/sistem düzeyinde)
- `eğitim-müfredat` — diyetisyenlik eğitiminde YZ entegrasyonu, müfredat/eğitim programı çağrısı
- `klinik-işakışı` — somut pratik kullanım (tarama, izleme, hasta değerlendirmesi); klinik entegrasyonu haritalayan derlemeler de burada (bkz. Güvenlik Adımı 6)
- `alakasız` — hiçbirine girmiyor (saf teknik/moleküler AI-gıda makaleleri, ya da beslenimle bağı yüzeysel/zorlama). Listede kalır, sentezde kullanılmaz.

**2. `AI_Function` (AI hangi yeteneği taklit ediyor).** Soru: "Bu YZ, diyetisyenin hangi organını/yeteneğini taklit ediyor?" (İletişim/Yaratım ayrımı için Güvenlik Adımı 5'e bak)
- `Görme` — yemek fotoğrafından kalori/besin/tür tanıma (image recognition, CNN, food classification)
- `Hesaplama` — kan değeri/ölçüm/anketten hastalık-risk tahmini (prediction, risk assessment, screening)
- `İletişim` — hastayla sohbet eden chatbot/sanal asistan, soru-cevap/koçluk akışı (chatbot, NLP, conversational agent, coaching)
- `Yaratım` — kişiye özel menü/tarif/öğün planı üretimi (menu planning, recipe generation, diet plan generation)
- `Sistematik-Derleme` — literatürün tarandığı/sentezlendiği çalışmalar
- `Perspektif-Editöryal` — teknik veri sunmayan, meslek geleceği/etik üzerine uzman görüşü

**3. `Layer_Focus` (Katman).** Çalışmanın İÇİNDE kimin işi güçleniyor?
- `AI-Layer` — odak otomasyon/hız/veri toplama (örn. fotoğraftan porsiyon tahmini)
- `Human-Layer` — odak etik, empati, diyetisyen-danışan ilişkisi, stratejik liderlik
- `Hybrid` — YZ çıktısını diyetisyenin nasıl yorumlaması/kullanması gerektiği tartışılıyor
- *Kural (Güvenlik Adımı 7'ye bak):* Diyetisyen "altın standart/karşılaştırma referansı" ise → AI-Layer. Diyetisyen "denetleyici/karar verici" ise → Hybrid.

**4. `Model_Asamasi` (Roadmap Aşaması).** Makale, yol haritasının hangi aşamasına kanıt sağlıyor?
- `Awareness` — YZ'nin ne olduğu, tutumlar, farkındalık düzeyi (çoğunlukla kesitsel çalışmalar)
- `Competency` — belirli bir aracın kullanımı/doğruluğu test ediliyor (çoğunlukla validasyon çalışmaları)
- `Leadership` — karar destek, etik standart, disiplinlerarası yönetim, diyetisyenin "üst akıl" rolü
- *Kural:* Çalışmanın *amacına* bak, *sonucuna* değil — bir şey kanıtlamak mı istiyor (Competency) yoksa vizyon mu çiziyor (Leadership)? Makalenin kendi sonuç cümlesi "yeni içgörü sunmadı, mevcut akıl yürütmeyi doğruladı" gibi bir şey diyorsa, ne kadar iddialı bir başlığı olursa olsun bu Competency'dir, Leadership değil.

**5. `User_Notes`.** Tek cümle: bu çalışma "alan nereye evriliyor" sorusuna ne katkı sağlıyor? Alıntı değil, kendi yorumun — ama Güvenlik Adımı 3'teki genişletme tuzağına düşme. Bu cümle doğrudan sentez bölümünün taslağı olacak.

---

## 🔧 OPSİYONEL — elindeyse doldur, zorlama

- `Validation_Source` — Teknik / Uzman-Onaylı / Klinik (kanıt seviyesi — en düşükten en yükseğe)
- `Key_Barrier` — Bağlam Körlüğü / Teknik Yetersizlik / Güven-Etik / Klinik Kanıt Yok (limitasyonda en büyük şikayet)
- `Future_Direction` — Hibrit-İnsan Döngüde / Tam Otomasyon / Entegrasyon (sonuçta önerilen çözüm)
- `Proposed_Tool` — çalışmada kullanılan/geliştirilen somut araç adı
- `Dyt_karsilastirmasi` —çalışmadaki sonuçlar bir diyetisyenle karşılaştırılıyor mu?karşılaştırıyorsa evet. diyetisyen sonuçları sadece kontrol eden durumdayrsa kontrol olarak doldur. hiçbiyse hayır de.
- `prompt_var_mi` —eğer çalışmada kullanılan promptlar-istemler makalede veya supplementaryde paylaşılmışsa evet de. yoksa hayır de.

Bunlar Tartışma/Sınırlılıklar/Gelecek Yönelimleri paragraflarını zenginleştirir ama sentez + roadmap omurgası bunlarsız da tamamlanır. İlk turda atlanabilir, ikinci geçişte eklenebilir.

---

## 🧭 Zor Vakalar İçin Karar Rehberi (sadece kararsız kaldığında bak)

| Senaryo | Layer_Focus | Model_Asamasi |
|---|---|---|
| Görüntü işleme ile besin tanıma algoritması geliştirme | AI-Layer | Competency |
| YZ'nin diyetisyenlikte kullanımına dair etik rehber | Human-Layer | Leadership |
| Diyetisyenlerin ChatGPT kullanımı sonrası iş yükü analizi | Hybrid | Awareness/Competency |
| Kanser hastalarında YZ ile malnütrisyon riski saptama | AI-Layer | Competency |
| YZ risk skoru çıkarıyor, diyetisyen buna göre müdahale planlıyor | Hybrid | Leadership |
| AI bir kalori hesaplıyor, diyetisyen de hesaplıyor, fark karşılaştırılıyor (revize yok, hakem rolü) | AI-Layer | Competency |
| Diyetisyenler YZ çıktısını puanlıyor/eksik-halüsinasyon test ediyor (hakem, karar sürecine dahil değil) | AI-Layer | Competency |
| Kesitsel: diyetisyenlerin YZ'ye bakışını ölçen anket | Human-Layer | Awareness |
| RCT: YZ destekli uygulama vs standart takip, klinik çıktı ölçülüyor | Hybrid | Competency |
| Hastane sistemine canlıya alınmış (deployed) model, kalibrasyon/adalet inceleniyor | Hybrid | Competency veya Leadership — makalenin ağırlık merkezine bak: teknik düzeltme mi, sistem yönetimi vizyonu mu? |

**Dışlama kriteri:** Makale sadece mühendislik odaklıysa ve diyetetikle bağ kurmuyorsa (örn. genel nesne tanıma algoritması) → `Konu: alakasız`.

---
## 🤖 Bu İşi Bir AI'a Yaptırırken Kullanılacak Prompt

Bu görevi Claude, Antigravity veya başka bir modele devredeceksen, aşağıdaki metni olduğu gibi kopyala-yapıştır yap:

```
Görev: Aşağıdaki Obsidian notlarını (Augmented Dietitian klasörü) bu rehberdeki
(002_TEMA-KATMAN KODLAMA REHBERİ.md) çekirdek şemaya göre kodla: Konu, AI_Function,
Layer_Focus, Model_Asamasi, User_Notes.

Kesin kurallar (ihlal edilirse çıktı reddedilir):
1. Title, Authors, Year, DOI alanlarını SADECE o notun kendi frontmatter'ından al.
   Hafızandan tamamlama, "muhtemelen böyledir" diye yazma. Emin değilsen alanı boş
   bırak ve "doğrulanamadı" yaz — asla uydurma.
2. Methods/Findings/Conclusions alanı boşsa veya "full text yok" notu varsa, o
   makale için özgüvenli bir bulgu cümlesi YAZMA. User_Notes'a "veri yetersiz"
   yaz ve Konu'yu sadece başlıktan en temkinli tahminle doldur.
3. User_Notes'taki her cümle, nottaki alıntılanmış Methods/Findings/Conclusions/
   Limitations metnine kadar geri izlenebilmeli. Dar kapsamlı bir cümleyi geniş bir
   iddiaya genişletme (örn. "lezzet uygunluğu için denetim gerekir" cümlesini
   "denetimsiz kullanım risklidir" gibi bir güvenlik iddiasına çevirme).
4. Kararsız kaldığın her satırı User_Notes sonuna [KARARSIZ] etiketiyle işaretle,
   sessizce en makul seçeneği seçip geçme.
5. Fonksiyon ayrımı: İletişim = diyalog/soru-cevap kalitesi test ediliyor.
   Yaratım = somut çıktı (menü/tarif/plan) üretimi test ediliyor — arayüz chatbot
   olsa bile ölçülen şey plan/menünün doğruluğuysa Yaratım'dır.
6. Derlemelerde: sadece algoritmik metrik topluyorsa performans-değerlendirme;
   klinik iş akışına entegrasyonu haritalıyorsa klinik-işakışı.
7. Katman kuralı: diyetisyen sadece karşılaştırma referansı/hakem ise AI-Layer;
   diyetisyenin kendi kararını YZ çıktısına göre şekillendirdiği gösteriliyorsa
   Hybrid.
8. Aşama kuralı: makalenin KENDİ sonuç cümlesine bak, başlığın iddialılığına değil.
   "Yeni içgörü sunmadı, mevcut akıl yürütmeyi doğruladı" gibi bir sonuç varsa,
   ne kadar geniş kapsamlı görünürse görünsün bu Competency'dir, Leadership değil.

Çıktı formatı: [tablo formatı burada belirtilir]

İşin bitince, hangi satırları [KARARSIZ] işaretlediğini ayrıca listele.
```
