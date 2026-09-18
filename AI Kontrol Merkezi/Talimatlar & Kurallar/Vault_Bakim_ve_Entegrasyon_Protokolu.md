# 🏛️ Akademik Obsidian Vault Bakım, Senkronizasyon ve Living Evidence Protokolü

Bu belge, Dr. Caner Özyıldırım akademik Obsidian kasasının zaman içinde büyümesini, yeni yayınların entegrasyonunu, MOC güncellemelerini ve Living Evidence standartlarını yönetmek üzere hazırlanmış operasyonel talimat kılavuzudur.

---

## 🎯 1. Sistemin Temel Prensipleri ve Çatı Mimarisi

Kasa 4 ana katmandan oluşur:
1. **Çatı Dizinler (10 Domain MOC):** `Dizin/` altında yer alan 10 ana metabolik ve klinik MOC.
2. **Klinik & Mekanizma Notları:** `Notlar/` altındaki 150+ yapılandırılmış atomik not.
3. **Çalışma & Fikir Logu:** `Çalışma Fikirleri/` altındaki 290+ araştırma hipotezi ve soru.
4. **Girdi ve Takip Motoru:** `00 Kontrol Merkezi/Digests/` ve `nutrition_scout.py` üzerinden haftada 2 kez (4 günlük tarama penceresi ile) akan canlı literatür bülteni.

---

## 🔬 2. Living Evidence ve Çelişki / Null Standartları

Eklenen her yeni klinik/akademik not veya taranan yayın şu kurallara uymalıdır:

### A) Frontmatter Standartları:
```yaml
---
study_type: "RCT" # RCT, Cohort, Meta-Analysis, Cross-Sectional, Animal Study, Review
evidence_direction: "positive" # positive | negative | null | contradictory | inconclusive
primary_outcome: "Pankreas Beta Hücre Plastisitesi"
p_value_summary: "p < 0.05"
BESLEDİĞİ NOTLAR:
  - "[[Doğrudan derinleştirdiği veya taze kanıt eklediği Çekirdek Not]]"
---
```

### B) Besleyici (Feeder) Not Kuralı:
* Bir not, başka bir notla sadece kavramsal/bağlamsal olarak ilişkili olmanın ötesinde **doğrudan onun üzerine inşa ediyor, mekanizmasını derinleştiriyor veya ampirik yeni kanıt ekliyorsa**, o notu **besliyor** demektir.
* Bu durum `BESLEDİĞİ NOTLAR:` YAML alanına eklenmeli ve ilgili ana notun içindeki sentezi güçlendirmelidir.

### C) Çelişki ve Null Etiketleri:
* Sonuç istatistiksel olarak anlamsızsa (p > 0.05): `#finding/null` eklenir.
* Sonuç yerleşik konsensüsle çelişiyorsa, paradoks içeriyorsa veya kas kaybı/ters etki bildiriyorsa: `#finding/contradictory` eklenir.
* Tüm bu maddeler otomatik olarak `00 Kontrol Merkezi/Dashboard_Gaps_and_Contradictions.md` panosunda toplanır.

---

## 💡 3. Fikir Logu Çapraz Bağlantılama (Cross-Referencing)

Yeni bir makale veya bülten işlenirken:
* Sadece "bu iyi bir fikir" denilmemeli;
* `Çalışma Fikirleri/` altındaki mevcut bir notla (Örn: `[[GLP-1 Kullanan Hastalarda Nutrient Density Yaklaşımlı RCT]]` veya `[[upf-siniflandirma-tutarsizligi-calisma-fikri]]`) bağlantı kurulmalı; yeni bulgunun mevcut hipotezi destekleyip desteklemediği veya çürütüp çürütmediği belirtilmelidir.

---

## 🎓 4. Çok Boyutlu Akademik Üretim Matrisi (Dersler, Substack, Podcast, Proje)

Her yeni bulgu veya bülten analizinde şu 4 boyut zorunlu olarak somutlaştırılır:
1. **🎓 Lisans / Klinik Ders Köprüsü (BES339 / BES326 / YHD):** İlgili haftanın ders planına eklenecek somut vaka sorusu veya öğrenci münazara konusu.
2. **✍️ Substack & Sosyal Medya Açısı:** Popüler algı vs. Moleküler gerçeklik ikilemi üzerinden kurgulanan derin bülten taslağı.
3. **🎙️ Konsantre Podcast / Sesli Not Başlığı:** 5-7 dakikalık klinik odak tartışma başlığı ve hasta/danışan yansıması.
4. **🔬 İleri Araştırma & Proje Tohumu:** Makaledeki metodolojik boşluğu (örn. örneklem, süre, cinsiyet yanıtı) kapatacak yerel bir RCT veya anket hipotezi.

---

## 🔄 5. Periyodik Vault & MOC Güncelleme Protokolü

Birkaç haftada bir veya kasaya toplu not/makale eklendiğinde şu adımlar işletilir:

1. **Senkronizasyon Motorunu Çalıştır:**
   `python3 sync_vault.py`
2. **MOC Köprülerini Doğrula:**
   Yeni eklenen kavramların 10 ana MOC altındaki ilgili mekanizma ve ders köprülerine `[[Not Adı]]` olarak eklendiğinden emin ol.
3. **Living Evidence Panosunu Gözden Geçir:**
   `00 Kontrol Merkezi/Dashboard_Gaps_and_Contradictions.md` panosunu açıp son haftalarda ortaya çıkan null ve çelişkili bulguları incele; ders veya Substack yazısı konusu çıkar.
