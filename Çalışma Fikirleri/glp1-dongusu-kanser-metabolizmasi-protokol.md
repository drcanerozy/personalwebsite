# GLP1 Döngüsü (Cycling) ve Kanser Metabolizması — Çalışma Tasarımı Taslağı

## 1. Arka Plan ve Boşluk

- GLP1RA kullanımı sırasında antikanser sinyal (AMPK aktivasyonu, glikolitik enzim baskılanması, adipokin profili düzelmesi) literatürde nispeten iyi karakterize edilmiş.
- GLP1RA **kesilmesi** sonrası hızlı ve orantısız kilo geri alımı (semaglutid/tirzepatid için ~9-14% bazal kiloya kadar) iyi belgelenmiş, ancak bunun tümör mikroçevresi/kanser metabolizmasına etkisi doğrudan çalışılmamış.
- Genel weight-cycling (yo-yo dieting) literatürü kanser riski açısından çelişkili/null sonuçlar veriyor (bazı çalışmalarda endometrial/renal/NHL riskinde ılımlı artış, büyük kohortlarda anlamlı ilişki yok).
- **Kilit boşluk:** GLP1 cycling'in weight cycling'in genel bir alt tipi mi, yoksa farmakolojik olarak ayrı bir mekanizma mı (ani GLP1R sinyal kaybı + oreksijenik rebound) olduğu bilinmiyor. Bu ayrım test edilmeden ikisi birbirine karıştırılıyor.

## 2. Ana Hipotez

Tekrarlayan GLP1RA başlatma-kesme döngüsü, sürekli tedaviye veya tedavisiz obeziteye kıyasla, tümör-permisif sistemik/adipoz sekretom (↑leptin, ↑IL-6, değişken insülin) ve tümör büyüme kinetiğinde farklı bir profil yaratır; bu etki salt kalori-kısıtlama kaynaklı kilo döngüsünden (GLP1'siz) mekanistik olarak ayrışır.

## 3. Kademeli (Staged) Yaklaşım — Önerilen Yol

### Faz 0 — Hücre kültürü / kondisyone medyum pilotu (en düşük maliyet, ilk adım)
- 3T3-L1 veya insan primer preadiposit → adiposite farklılaştırma
- Kollar: (1) kontrol, (2) besin kısıtlaması kontrolü, (3) GLP1RA yükle → kes (rebound fazı), (4) GLP1RA 3 döngü
- Her fazda kondisyone medyum topla → MCF7/MDA-MB-231/HCT116 gibi kanser hattına uygula
- Okuma: proliferasyon, migrasyon, Seahorse (glikoliz/OXPHOS), leptin/adiponektin/IL-6 ELISA
- **Amaç:** İn vivo çalışmaya geçmeden önce sinyal var mı yok mu görmek, doz/zaman parametrelerini optimize etmek

### Faz 1 — İn vivo metabolik fenotipleme (tümörsüz)
**Gruplar (4 kol, obez zeminde):**
1. HFD (tedavisiz) — obez referans
2. HFD + GLP1 sürekli — pozitif kontrol
3. HFD + GLP1 3 döngü
4. HFD + pair-fed kalori kısıtlaması (GLP1'siz, kolon 3 ile eşit kilo kaybı/geri alım paterni) — **kritik ayraç kolu**, GLP1'e özgü etkiyi davranışsal/kalorik etkiden ayırmak için

*Not: "Tek kesme" (1 döngü) kolu isteğe bağlı eklenebilir ama zorunlu değil — sürekli ve 3-döngü ekstremleri arasında doz-yanıt zaten örneklenmiş olur. Lean/chow kontrolü tam N ile değil, küçük referans kohort (n=5-6) olarak eklenebilir.*

**Toplanan veri:** vücut kompozisyonu (yağ/yağsız kütle, DEXA veya NMR), terminal serum (leptin, adiponektin, insülin, IL-6, TNF-α, ghrelin), yağ dokusu histolojisi ve gen ekspresyonu (inflamasyon markerları)

### Faz 2 — Daraltılmış tümör kohortu
- Faz 1'den en bilgilendirici 2-3 kolu seç (tipik olarak: sürekli GLP1 vs 3-döngü vs pair-fed kontrol)
- Tümör yaklaşımı için iki seçenek:
  - **A) Sentetik tümör (implantasyon):** Syngeneic immünkompetan model (örn. C57BL/6 + E0771 meme, MC38 kolon) — enjeksiyon altyapısı gerektirir
  - **B) Spontan tümöre yatkın genetik model:** MMTV-PyMT (meme), ApcMin/+ (kolorektal) — enjeksiyon gerektirmez, tümör kendiliğinden gelişir, altyapı basitleşir ama n artırımı ve zamanlama planlaması gerekir (döngü protokolü tümör insidansından önce mi progresyon fazında mı başlatılacak, net tanımlanmalı)
- Okuma: tümör hacim kinetiği, IHC (Ki67, GLUT1, HIF1α), eksize tümör dokusunda Seahorse

## 3.5. Alternatif Tasarımlar

### Alternatif A — Genetik yatkınlıklı model, baştan sona tek omurga (implantasyon yok)
Faz 1/Faz 2 ayrımı yerine, tümöre yatkın genetik hayvanı (MMTV-PyMT veya ApcMin/+) en baştan omurga olarak kullanıp tüm protokolü tek aşamada yürütme seçeneği:

- Doğuştan tümöre yatkın hayvanlara doğrudan HFD + GLP1 protokolü uygulanır, ayrı bir "tümörsüz fenotipleme fazı" ve sonra "tümör kohortu" ayrımı yapılmaz
- **Avantaj:** Tek kohort, tek zaman çizelgesi, enjeksiyon altyapısı hiç gerekmez, hayvan sayısı staged yaklaşıma göre daha öngörülebilir şekilde bütçelenir
- **Dezavantaj:** Faz 0/Faz 1 pilot verisiyle önce sinyali doğrulama fırsatı kalmaz — doğrudan en pahalı/en uzun deneye girilir, tümör penetransı ve zamanlaması genetik hat içinde bile değişken olabileceğinden (MMTV-PyMT'de tümör başlangıcı genellikle 8-10 hafta civarı ama hat/arka plan suşuna göre değişir) döngü protokolünün başlangıç zamanı önceden net tanımlanmalı: döngü tümör insidansından önce mi (önleme sorusu) yoksa tümör zaten varken mi (progresyon sorusu) başlıyor — bu iki farklı hipotez, aynı kohortta karıştırılmamalı
- **Kimin için uygun:** Enjeksiyon/implantasyon altyapısı hiç yoksa ve tek seferde tam ölçekli bir çalışma planlanıyorsa (staged pilot aşamasını atlamayı göze alarak) bu en pratik yol

### Alternatif B — 5 kollu tasarım (orijinal öneriye dönüş, genişletilmiş)
Pair-fed kontrolünü feda etmeden, "tek döngü" kolunu da ayrı tutmak isteniyorsa:

1. HFD (tedavisiz) — obez referans
2. HFD + GLP1 sürekli — pozitif kontrol
3. HFD + GLP1 tek kesme (1 döngü)
4. HFD + GLP1 3 döngü
5. HFD + pair-fed kalori kısıtlaması (GLP1'siz, ayraç kolu)

- **Avantaj:** 1 döngü ile 3 döngü arasında doz-yanıt (kaç döngünün eşiği geçtiği) net görülür — sadece iki ekstrem değil, ara nokta da örneklenmiş olur
- **Dezavantaj:** 4 kollu tasarıma göre ~%25 daha fazla hayvan/maliyet; ayrım gücü (1 vs 3 döngü) çalışmanın asıl sorusu (GLP1-spesifik mi genel mi) için kritik değilse bu ek maliyet gereksiz olabilir
- **Ne zaman tercih edilmeli:** Eğer nihai hedef sadece "cycling zararlı mı değil mi" değil, aynı zamanda "kaç döngüden sonra risk belirginleşiyor" sorusuna da cevap vermekse (doz-yanıt eğrisi klinik olarak daha aktarılabilir bir bulgu olur) bu 5. kol değerli; sadece var/yok sorusu yeterliyse 4 kollu tasarım daha verimli

### Karşılaştırma özeti

| Tasarım | Kol sayısı | Enjeksiyon gerekli mi | Ana kazanım | Ana bedel |
|---|---|---|---|---|
| Staged (Faz1→Faz2, önerilen) | 4 (+2-3 daraltılmış tümör) | Evet (implantasyon seçilirse) | Maliyet kontrolü, erken sinyal doğrulama | İki aşamalı zaman çizelgesi |
| Alternatif A (genetik, tek omurga) | 4 | Hayır | Tek kohort, basit altyapı | Zamanlama karmaşıklığı, pilot atlanır |
| Alternatif B (5 kollu) | 5 | Seçime bağlı | Doz-yanıt (1 vs 3 döngü) çözünürlüğü | En yüksek hayvan/maliyet |

## 4. Neden Bu Tasarım

- Tüm kollara baştan tümör vermek yerine staged yaklaşım hayvan sayısını ve maliyeti önemli ölçüde azaltır
- Pair-fed kolu olmadan "GLP1 cycling zararlı" ile "herhangi bir weight cycling zararlı" ayrıştırılamaz — bu kolun eklenmesi çalışmanın özgünlüğünü belirleyen en kritik unsur
- Genetik tümör modeli, enjeksiyon altyapısı yoksa gerçekçi bir alternatif; ana bedeli değişkenlik artışı ve zamanlama karmaşıklığı

## 5. Potansiyel Değerlendirmesi

**Güçlü yönler:**
- Klinik ihtiyaç güncel ve büyüyor (GLP1 kesme/döngü pratikte yaygınlaşıyor, maliyet/yan etki/arz kısıtları nedeniyle)
- Doğrudan dolduran yayın yok — "ilk" olma potansiyeli var
- Pair-fed kontrolü sayesinde mekanistik olarak özgün bir soruya (GLP1-spesifik mi, genel weight-cycling mi) cevap verebilir

**Riskler:**
- Null sonuç olasılığı yüksek (weight-cycling literatüründe emsal çok)
- Genetik tümör modelinde zamanlama ve değişkenlik kontrolü zor
- Fare→insan çeviri mesafesi büyük; bu bir pilot/ön veri çalışması olarak konumlandırılmalı, doğrudan klinik iddia için değil

## 6. Sıradaki Adımlar

- [ ] Kurumda hangi altyapının mevcut olduğunu netleştir (hücre kültürü / enjeksiyon / genetik model erişimi)
- [ ] Faz 0 pilot için bütçe ve zaman çizelgesi çıkar
- [ ] Pair-fed kontrol protokolünün metodolojik detaylarını literatürden netleştir
- [ ] Etik kurul başvurusu için gerekli hayvan sayısı hesaplaması (power analizi)

## Bağlantılı Notlar
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
- [[weight-cycling-glp1-cycling-perspektif-taslak]]
- [[IF-crossover-carryover-protokol]]
- [[Mendelian Randomizasyon Nedir?]]
- [[ev-yapimi-upf-kavrami]]
