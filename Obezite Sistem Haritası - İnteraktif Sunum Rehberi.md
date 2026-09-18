---
title: Obezite Sistem Haritası & Atlası - İnteraktif Sunum Modülü
tags:
  - obezite
  - sunum
  - foresight
  - sistem-dinamikleri
  - enerji-dengesi
date: 2026-09-05
---

# 🌐 Foresight Obezite Sistem Haritası & Atlası (İnteraktif Sunum)

> [!NOTE]
> Bu modül, **Obezite Sunumunda 10. Slayt (Enerji Dengesi: Kalori Girişi vs. Çıkışı)** hemen sonrasında açılmak üzere özel olarak tasarlanmıştır.

---

## 🚀 İnteraktif Sunumu Başlatma

Aşağıdaki bağlantıya tıklayarak veya tarayıcınızda açarak tam ekran interaktif sunumu başlatabilirsiniz:

- **Dosya Yolu:** [obezite_sistem_atlasi_interaktif_sunum.html](file:///Users/canerozyildirim/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/caner/obezite_sistem_atlasi_interaktif_sunum.html)
- **Yüksek Çözünürlüklü Harita:** [obesity_map_hires.png](file:///Users/canerozyildirim/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/caner/obesity_map_hires.png)
- **Orijinal Sistem Atlası Raporu:** [07-1177-obesity-system-atlas.pdf](file:///Users/canerozyildirim/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/caner/07-1177-obesity-system-atlas.pdf)

### 💡 Obsidian İçinde Doğrudan Görüntüleme (Canlı İframe)
```html
<iframe src="obezite_sistem_atlasi_interaktif_sunum.html" width="100%" height="750px" style="border:none; border-radius:12px;"></iframe>
```

---

## ⌨️ Klavye ve Sunucu Kısayolları

| Tuş | Eylem |
| :--- | :--- |
| `Sağ Ok` / `Boşluk` / `PageDown` | **Sonraki Adıma İlerle (Zoom & Focus)** |
| `Sol Ok` / `PageUp` | **Önceki Adıma Dön** |
| `F` | **Tam Ekran Aç / Kapat** |
| `N` | **Konuşmacı İpuçları Panelini Aç / Kapat** |
| `M` | **Serbest Keşif Modu (Free Roam Pan/Zoom)** |
| `1` - `9`, `0` | **Doğrudan İlgili Kümeye/Adıma Atla** |

---

## 🎙️ 10 Adımlı Sunum Akışı ve Konuşmacı Notları (Slide 10 Sonrası)

```mermaid
graph LR
    S1["01. Büyük Resim (Şok)"] --> S2["02. Biyoloji"]
    S2 --> S3["03. Bireysel Psikoloji"]
    S3 --> S4["04. Sosyal Psikoloji"]
    S4 --> S5["05. Gıda Tüketimi"]
    S5 --> S6["06. Gıda Üretimi"]
    S6 --> S7["07. Bireysel Aktivite"]
    S7 --> S8["08. Aktivite Çevresi"]
    S8 --> S9["09. Kritik Kısır Döngüler"]
    S9 --> S10["10. Kaldıraç Noktaları & Çözüm"]

    style S1 fill:#ef4444,stroke:#fff,color:#fff
    style S2 fill:#3b82f6,stroke:#fff,color:#fff
    style S3 fill:#06b6d4,stroke:#fff,color:#fff
    style S4 fill:#8b5cf6,stroke:#fff,color:#fff
    style S5 fill:#10b981,stroke:#fff,color:#fff
    style S6 fill:#f59e0b,stroke:#fff,color:#fff
    style S7 fill:#eab308,stroke:#fff,color:#fff
    style S8 fill:#ec4899,stroke:#fff,color:#fff
    style S9 fill:#ef4444,stroke:#fff,color:#fff
    style S10 fill:#14b8a6,stroke:#fff,color:#fff
```

### 1. Büyük Resim: 108 Değişken ve Enerji Dengesi Çekirdeği
* **Görsel:** Haritanın bütünü gösterilir, merkezdeki *Energy Balance* kutusu vurgulanır.
* **Konuşmacı Cümlesi:** *"10. slaytta enerji dengesini (Kalori Girişi vs. Kalori Çıkışı) konuştuk. Termodinamik olarak bu formül doğrudur. Ancak soru şudur: Milyonlarca insan neden aynı anda iradesini kaybetti? Cevap bu haritada: Çünkü biyolojimiz tek başına çalışmıyor; etrafını saran 108 faktörlük devasa bir ekosistemin içinde sıkışmış durumda."*

### 2. Biyoloji (Evrimsel Miras ve Hormonal Savunma)
* **Odak:** Sol-orta biyoloji kümesi.
* **Kritik Kavramlar:** Leptin direnci, ghrelin fırtınası, metabolik adaptasyon (kilo verildiğinde BMR'nin kısılması).
* **Vurgu:** Biyolojimiz kilo almaya açıktır ama kilo kaybına karşı ölüm kalım savaşı verir (asimetrik savunma).

### 3. Bireysel Psikoloji (Dopamin, Ödül ve Stres)
* **Odak:** Sol-üst psikoloji kümesi.
* **Kritik Kavramlar:** Duygusal yeme, dopaminerjik ödül arayışı, kronik stres-kortizol aksı.
* **Vurgu:** Gıda sadece yakıt değil; stres, yalnızlık ve tükenmişlik anlarında en ucuz ve en hızlı nörokimyasal rahatlatıcıdır.

### 4. Sosyal Psikoloji (Normlar ve Sosyalleşme)
* **Odak:** Üst-orta sosyal psikoloji kümesi.
* **Kritik Kavramlar:** Akran etkisi, aile mirası, büyük porsiyonların sosyal normalleşmesi, kilo damgalaması (weight stigma).
* **Atıf:** Nicholas Christakis'in çalışması: Yakın arkadaşı obez olan birinin obez olma riski %57 artar.

### 5. Gıda Tüketimi (Porsiyon Bozulması ve Enerji Yoğunluğu)
* **Odak:** Üst-orta-sağ tüketim kümesi.
* **Kritik Kavramlar:** *Portion distortion*, sıvı şekerler, lifi soyulmuş rafine gıdalar, gün boyu atıştırma (snacking).
* **Mekanizma:** Mide hacimle gerilir; enerji yoğun gıdalar mekanoreseptörleri uyarmadan aşırı kalori aldırır.

### 6. Gıda Üretimi ve Pazarı (Ultra-İşlenmiş Gıda Ekonomisi)
* **Odak:** Sağ-üst üretim kümesi.
* **Kritik Kavramlar:** *Bliss point* (şeker-yağ-tuz mühendisliği), ucuz kalori sübvansiyonları, çocuk odaklı reklamlar.
* **Atıf:** Kevin Hall (2019): Ultra-işlenmiş gıda tüketen bireyler, tamamen aynı besin değerine sahip doğal beslenenlere göre günde fazladan 500 kcal tüketir.

### 7. Bireysel Aktivite (Fiziksel Kapasite ve NEAT)
* **Odak:** Sol-alt aktivite kümesi.
* **Kritik Kavramlar:** NEAT (Egzersiz dışı hareket), kondisyonsuzluk eşiği, kompensatuar hareketsizlik.
* **Vurgu:** Spor salonundaki 45 dakika değerlidir; ancak gün boyu süren oturma süresini ve metabolik yavaşlamayı tek başına telafi edemez.

### 8. Aktivite Çevresi (Eforu Sıfırlayan Yapılı Çevre)
* **Odak:** Sağ-alt yapılı çevre kümesi.
* **Kritik Kavramlar:** Otomobil odaklı şehirler, yürünemez kaldırımlar, asansörler, kapıya teslimat sistemleri.
* **Vurgu:** İnsanlık tarihinde ilk kez hayatta kalmak için sıfır fiziksel efor harcanan bir çevre inşa ettik.

### 9. Kritik Sistemik Döngüler (Feedback Loops)
* **Görsel:** 4 döngü rotası harita üzerinde parlayan animasyonlarla gösterilir.
  1. *Stres $\rightarrow$ Kortizol $\rightarrow$ Yeme $\rightarrow$ Kilo $\rightarrow$ Stres*
  2. *Sedanter Yaşam $\rightarrow$ Kondisyon Kaybı $\rightarrow$ Efordan Kaçınma $\rightarrow$ Hareketsizlik*
  3. *Hızlı Kalori Talebi $\rightarrow$ UPF Arzı $\rightarrow$ Düşük Fiyat $\rightarrow$ Artan Pazar*
  4. *Toplumda Kilo Artışı $\rightarrow$ Algı Eşiğinin Yükselmesi $\rightarrow$ Normalleşme*

### 10. Çözüm ve Kaldıraç Noktaları (Whole-Systems Approach)
* **Görsel:** Harita genel görünüme döner, çözüm reçetesi listelenir.
* **Kaldıraç Noktaları:**
  * **Default Choice:** Sağlıklı tercihi en kolay, en ucuz ve varsayılan seçenek yapmak.
  * **Yapısal Regülasyonlar:** Şeker vergisi, reklam yasakları, gıda reformülasyonu.
  * **Aktif Şehirler:** Yürünebilir sokaklar, bisiklet ağları, yeşil alanlar.
  * **Damgalamanın Bitirilmesi:** Bireyi suçlamak yerine sistemi iyileştirmek.
