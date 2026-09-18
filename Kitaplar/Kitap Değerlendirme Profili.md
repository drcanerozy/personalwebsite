---
tags: [claude, skill, kitap, profil, tercih-modeli]
created: 2026-09-06
---

# 📚 Kitap Değerlendirme Profili — Caner'in Okur Modeli

Bu dosya, Caner'in Kitaplar dashboard'undaki ~130 kitaplık puanlama geçmişinin
(dağılım analizi + Goodreads/1000kitap çapraz karşılaştırması) sonucunda çıkarılmış
bir tercih modelidir. Claude, "bu kitabı beğenir miyim / bana uyar mı" tarzı bir
soru geldiğinde ÖNCE bu dosyayı okumalı, sonra aşağıdaki çerçeveye göre tahmin
üretmelidir.

**Metodoloji notu:** Bu model kitapların "objektif kalitesi" üzerine değil,
Caner'in puanları ile genel okur konsensüsü (1000kitap/Goodreads ortalamaları,
tekrarlayan eleştiri temaları) arasındaki SAPMALARIN analizi üzerine kurulmuştur.
Genel görüşle uyumlu olduğu yerler (özellikle 5★'ler) güvenilir; asıl değerli
kısım, genel görüşten saptığı yerlerdeki tutarlı kalıplardır.

---

## 🎯 Ana Model: Kombinasyonel, Hiyerarşik Yapı

Kriterler birbirinden bağımsız kutular DEĞİL. Merkezde tek bir eksen var,
geri kalanlar onun etrafında telafi edilebilir risk faktörleri olarak işliyor:

```
                    ┌─────────────────────────────┐
                    │   CÜMLE / ÜSLUP ETKİSİ       │  ← ANA EKSEN
                    │  (sade ama vurucu; okuru     │
                    │   "içine işleyen" cümleler)  │
                    └──────────────┬───────────────┘
                                   │
              GÜÇLÜYSE:           │           ZAYIFSA:
              risk faktörlerini   │           risk faktörleri
              TELAFİ EDER         │           KATLANARAK BÜYÜR
                                   ▼
        ┌──────────────────────────────────────────────┐
        │             RİSK FAKTÖRLERİ                    │
        │  1. Zor giriş / dolambaçlı-parçalı anlatı      │
        │  2. Didaktik/sembolik kahraman (gerçek insan   │
        │     değil, "ders aracı")                       │
        │  3. Konu rahatsızlığı — ÖZELLİKLE başkasını    │
        │     nesneleştiren/romantize edilmiş etik ihlal │
        │  4. Okuma dönemi gürültüsü (bkz. not)          │
        └──────────────────────────────────────────────┘
```

### Kritik ayrım: "Zor/karanlık" tek başına düşük puan nedeni DEĞİL

- **Cümlesi güçlüyse** zor anlatı da, karanlık konu da taşınabilir/sevilir:
  - *Kesin İnançlılar* (Hoffer, 5★): yoğun bir tez kitabı ama "insanın
    derinlerine işliyor" türünde övgü alıyor — genel görüşle tam uyumlu.
  - *Tıkanma* (Palahniuk, 5★): çok rahatsız edici içerik (cinsel bağımlılık,
    sahtekarlık) ama grotesk/parodik üslupla + güçlü dille sunulmuş.
  - *İnsanlığımı Yitirirken* (Dazai, 5★): intihar, bağımlılık, kendinden
    nefret — ama "dili çok akıcı, lafı dolandırmadan anlatıyor" deniyor.
    Not: bu karanlık KENDİNE yönelik/itiraf niteliğinde, başkasını
    nesneleştirmiyor — bu da 3. risk faktörünü tetiklemiyor.

- **Cümlesi telafi etmiyorsa** zor anlatı düşük puana dönüşüyor:
  - *Kara Kitap* (Pamuk, 1★): genel görüş bile azınlıkta "sürükleyicilikten
    uzak, tekrarlayan" diyor — cümle düzeyinde tutmuyor.
  - *Beni Kör Kuyularda* (Toptaş, 2★): genel görüş dahi itiraf ediyor,
    "kolay okunan bir metin değil, sabır ister" — sabrı ödeyen cümle etkisi
    Caner'de oluşmamış.
  - *Gülün Adı* (Eco, 3★) / *Zaman Sığınağı* (Gospodinov, 3★): ikisi de
    yaygın övgü alıyor ama övgü KAVRAMSAL/yapısal ("düşündürücü kurgu"),
    cümle-düzeyinde duyusal değil → orta-düşük puan.

### Risk faktörü #2 örneği: Didaktik/sembolik kahraman
- *Simyacı* (Coelho, 3★): 8.3/10, 249bin okunma — devasa popülerlik ama
  kahraman "gerçek insan" değil, sembolik/ders aracı. Caner'in "karakter
  gerçekliği" kriterine takılıyor.

### Risk faktörü #3 örneği: Konu rahatsızlığı — nüans önemli
- *Benim Hüzünlü Orospularım* (Marquez, 2★): 1000kitap'ta kutuplaştırıcı —
  bir grup okur "kesinlikle pedofili var, etiğime ters geldi" diyor. Sorun
  konunun karanlık olması değil, **ciddiyetle "aşk" olarak romantize
  edilmesi** — yani başka (güçsüz) bir karakterin nesneleştirilmesi.
- Kontrast: Tıkanma ve İnsanlığımı Yitirirken de karanlık ama biri
  grotesk-parodik, diğeri kendine-yönelik-itiraf → risk tetiklenmiyor.

### Risk faktörü #4: Dönem etkisi (gürültü faktörü, kalite göstergesi değil)
- Düşük puanlı (1-2★) kitapların büyük çoğunluğu 2021-2022 döneminde
  okunmuş. Sonraki dönemde (2023-2026, 90+ kitap) neredeyse hiç 1-2★ yok.
  Bu, kitabın kalitesinden bağımsız bir zaman/okuma-hali etkisi olabilir —
  yeni bir kitaba dönem etkisi UYGULANAMAZ, sadece geçmiş puanları
  yorumlarken hatırlanmalı.

### YENİ EKSEN — Kişisel/biyografik rezonans (telafi edici, çarpan etkili)
- Karakterin yaşadığı belirli bir mücadele Caner'in kendi hayatındaki bir
  deneyimle örtüşüyorsa (örnek: yabancı dilde var olma çabası, dil öğrenme
  zorluğu), bu genel "karakter gerçekliği" kriterinin ötesinde ekstra bir
  bağ kuruyor ve puanı yukarı çekiyor. Shuggie Bain'deki "çocuk kahramanlara
  zaafım var" da bu eksenin bir örneği — burada tema "çocukluk", Tuzun
  Kitabı'nda tema "yabancı dilde var olma".
- Bu eksen dış kaynaklardan (Goodreads/1000kitap) TESPİT EDİLEMEZ — sadece
  Caner'in kendi hayatını bilen biri (yani bu profildeki bilgiler) fark
  edebilir. Yeni kitap önerirken, Caner'in profilindeki kişisel deneyimlerle
  (akademisyenlik, yurt dışı/göç ilgisi, dil öğrenme, beslenme/bilim alanı)
  örtüşen temalar ekstra ağırlık almalı.

### YENİ EKSEN — Tazelik / alışılmadık bakış açısı
- "Hiç bir denizci/şef gözünden bir şey okumamıştım" tarzı bir gözlem de
  puanı yukarı çekiyor — daha önce denenmemiş bir anlatıcı konumu/meslek/
  bakış açısı, tek başına bir artı puan kaynağı.

### Kalibrasyon vakası: Tuzun Kitabı (Monique Truong, okunuyor — henüz puanlanmadı)
- Caner okurken 4-5★ hissediyor; uygulamadaki AI modeli ilk denemede 3★
  tahmin etti. Sebep muhtemelen: (a) Paris/sömürge-dönemi Vietnam arasında
  kronolojik olmayan sıçramalı yapı risk faktörü #1'i tetikledi, (b) model
  bunu telafi eden çok güçlü cümle-düzeyi övgüyü (Goodreads: "stunning
  sentences", "lingers like an ocean voyage") yeterince ağırlıklandıramadı,
  (c) yukarıdaki yeni iki eksen (biyografik rezonans + tazelik) o sırada
  modelde yoktu. NOT: Türkçe çeviri kalitesiyle ilgili bir Goodreads yorumu
  var ("çeviri ile güme gitmiş") ama Caner kendisi dili çok beğendiğini
  söylediği için bu, ONUN OKUDUĞU baskı için doğrulanmış bir risk DEĞİL —
  çeviri kalitesi genel bir ihtiyat notu olarak kalsın, otomatik düşüş
  sebebi sayılmasın.

---

## 🧭 Yeni Bir Kitabı Değerlendirme Prosedürü

Claude, "bu kitabı okusam beğenir miyim" sorusu geldiğinde:

1. **Kitap hakkında hızlıca araştır** (1000kitap / Goodreads / genel eleştiri):
   - Genel puan ortalaması nedir?
   - Eleştirilerde üslup/dil hakkında ne deniyor? Cümle düzeyinde övgü
     var mı ("derinlerine işliyor", "akıcı", "vurucu") yoksa sadece
     kavramsal/yapısal övgü mü ("düşündürücü", "katmanlı", "orijinal kurgu")?
   - "Zor başlangıç ama sonra açılıyor" tarzı bir itiraf var mı?
2. **Kahramanı sınıfla**: gerçekçi/çelişkili bir insan mı, yoksa
   sembolik/didaktik bir araç mı?
3. **Varsa rahatsız edici temayı sınıfla**: kendine-yönelik/itiraf mı,
   yoksa başkasını nesneleştiren/romantize edilmiş bir ihlal mi?
4. **Sonucu birleştir**:
   - Cümle etkisi güçlü + risk faktörü yok/düşük → **muhtemelen 5★**
   - Cümle etkisi güçlü + risk faktörü var (zor yapı veya kendine-yönelik
     karanlık) → **muhtemelen 4-5★** (cümle telafi ediyor)
   - Cümle etkisi zayıf/belirsiz + zor yapı veya didaktik kahraman →
     **muhtemelen 2-3★**
   - Cümle etkisi zayıf + başkasını nesneleştiren romantize edilmiş ihlal
     → **muhtemelen 1-2★, dikkatli öner**
5. Tahmini gerekçesiyle birlikte sun — hangi eksende ne bulduğunu kısaca
   belirt, sadece "beğenirsin/beğenmezsin" deme.

---

## 📊 Ham Veri Özeti (referans için)

- Toplam ~130 kitap (Tür: Kitap), dizi/film hariç
- Dağılım: 1★:2, 2★:5, 3★:33, 4★:48, 5★:35
- En sevdiği yazar/tekrar: Vedat Türkali, Mario Vargas Llosa (2 kitap, ikisi
  de 5★), Annie Ernaux (Boş Dolaplar 5★, Babamın Yeri 4★), Hüseyin Rahmi
  Gürpınar (5 kitap, tümü 3-4★ — istikrarlı ama tavan yapmıyor)
- Dikkat: Bazı 5★'ler "Başlanacak/Okunuyor" durumundaki kitaplara verilmiş
  (Bilim Tarihi, Kardeşim Rüzgar, Kaygı Döngüsünü Kırmak, MeaningFULL,
  Multiple Regression and Beyond, Ultra Processed People, Çalışma, Ötekinin
  Rüyası) — bunlar gerçek okuma deneyimini değil yazar/konu itibarına dayalı
  "ön beklenti puanı"nı yansıtıyor, model eğitiminden hariç tutuldu.

---

## 🔄 Bu Dosyayı Güncelleme

Yeni bir kitap bitirip puanladığında, gerçek puan ile bu modelin tahmini
arasında fark varsa, bu dosyaya kısa bir "yeni gözlem" notu eklenmeli —
model zamanla daha da netleşecek.
