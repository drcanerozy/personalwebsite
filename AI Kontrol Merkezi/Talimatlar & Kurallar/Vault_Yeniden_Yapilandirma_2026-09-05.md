---
title: Vault Yeniden Yapılandırma Günlüğü
tarih: 2026-09-05
amac: Diğer AI araçlarına / gelecekteki Claude oturumlarına yeni klasör yapısını tanıtmak için referans
---

# Vault Yeniden Yapılandırması - 2026-09-05

Bu not, kasanın kök dizin yapısında yapılan tüm değişiklikleri eksiksiz listeler. Otomasyon/dashboard/skill dosyalarının **içeriği değiştirilmedi** — sadece klasör/dosya konumları taşındı.

## Yeni kök dizin yapısı (özet)
- `00 Kontrol Merkezi/` — dashboardlar, digestler, iş takibi + yeni: Clippings/, Bookmarks/
- `AI Kontrol Merkezi/` — (eski adıyla "AI Kontrol Merkezi") — AI'ın kuralları, skilleri, ham veri işleme hattı
- `Dizin/`, `Notlar/`, `Çalışma Fikirleri/`, `Dersler/`, `Sosyal Medya/` — çekirdek içerik sistemi (yapıları genişletildi)
- `Manuscripts/` — tüm makale/yazım projeleri
- `Akademik/` — COST Actions, Postdoc, Akreditasyon
- `Kitaplar/` — kitap/film günlüğü (tek sistem)
- `Templates/` — tüm şablonlar (tek sistem)

## Taşıma detayları

### Kitaplar / Kitaplık
- `Kitaplık/` klasörü tamamen kaldırıldı. İçindeki Notion export'u (Kağıt ve Perde/Okuduklarım, 34 kitap notu + ekran görüntüsü klasörleri + 2 CSV + 1 "kitaplık" veritabanı sayfası) incelendi: **35 kayıttan 34'ü zaten Kitaplar/'da mevcuttu** (aynı kitap, farklı sistem).
- Bu yüzden hepsi `Kitaplar/_Notion Arsivinden - Kontrol Bekliyor/` klasörüne taşındı (silinmedi) — senin properties/puanlama sistemine göre elle karşılaştırıp hangi versiyonu tutacağına karar vermen gerekiyor.
- Ana `Kitaplar/` klasörünün kendisi hiç değişmedi.

### Templates
- `_Templates/Template_Manuscript.md` silindi (Templates/'deki ile birebir aynıydı).
- `_Templates/Template_Clinical_Case_Simulation.md` → `Templates/` içine taşındı.
- `_Templates/` klasörü kaldırıldı.

### Fikirler → Çalışma Fikirleri
- 4 not (Beslenme ve Diyetetik Metodolojisi, Neden Kilo Veremiyoruz?, Taş Devri Bilimi, Diyet Tarihi) `Çalışma Fikirleri/`'ne taşındı, her birinin frontmatter'ına `Kategori: Kitap-Egitim` eklendi (araştırma fikirlerinden ayırt etmek için).
- `Fikirler/` klasörü kaldırıldı.
- `Çalışma Tasarımları/` → `Çalışma Fikirleri/Çalışma Tasarımları/` (alt klasör oldu).

### Dersler (tamamen yeniden yapılandırıldı)
Her ders artık: `Dersler/[Ders Adı]/[Ders Adı].md` (F tablosu/fikirler) + `Ders Notları/`, `Sunumlar/`, `Araçlar/`, `Kaynaklar/` alt klasörleri.
- 7 ders (1. Sınıf Danışmanlıkları, Beslenme ve Medya, Beslenmenin Psikososyal Yönleri, Biyoistatistik, Enteral Parenteral Beslenme, Kanıta Dayalı Bilgelik, Çocuk Hastalıkları Stajı): sadece index notu taşındı, alt klasörler boş açıldı.
- **Bilgisayar Uygulamaları ve Yapay Zeka**: eski `Ders Notları/.../00_MOC.md` → yeni `Ders Notları/`; eski `02_Sunumlar/*` → yeni `Sunumlar/`.
- **Diyet İlkeleri ve Popüler Diyetler**: aynı mantık + CICO/Kişiselleştirilmiş Beslenme sunum iskeletleri → `Sunumlar/`.
- **Yetişkinlerde Beslenme Tedavisi Uygulaması** (eski adıyla "Yetişkin Hastalıkları Uygulaması" — isim birleştirildi): tüm Konu/Hafta ders içerikleri → `Ders Notları/`; Prompt.md → `Araçlar/`; tüm sunum HTML'leri/assets → `Sunumlar/`; **Vaka Raporları/** klasörü (16 dosya) → bu dersin `Kaynaklar/Vaka Raporları/` alt klasörüne taşındı.
- **İmmün Sistem ve İmmünonutrisyon**: eski karşılığı zaten boştu, boş alt klasörler açıldı.
- `Vault_Analizi_BES339_Ders_Notu_Kullanimi.md` (bir ders değil, analiz notuydu) → `00 Kontrol Merkezi/`'ne taşındı.
- Eski `Ders Notları/` klasörü tamamen kaldırıldı.
- `Dersler/Derslerim.md` (genel index) yerinde kaldı, dokunulmadı.

✅ **DÜZELTİLDİ (2026-09-05)**: `list_versions.py` içindeki sabit yol, kullanıcı onayıyla güncellendi (sadece dosya yolu string'i değiştirildi, script'in başka hiçbir satırına dokunulmadı):
```
path = ".../Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/Sunumlar/Konu1_Obezite_Sunum.html"
```
Ayrıca `semantic_linker.py`, `metadata_processor.py` ve `semantic_connection_engine.py` kontrol edildi: bunlar Dersler/Çalışma Fikirleri'ni recursive/kapsam-değişmeyen şekilde taradığı için yeni klasör yapısından etkilenmiyor, düzeltme gerekmedi.

### Kontrol Merkezi eklemeleri
- `Clippings/` → `00 Kontrol Merkezi/Clippings/`
- `Bookmarks/` → `00 Kontrol Merkezi/Bookmarks/`

### Manuscripts
- `NotebookLM Etkinliği/` → `Manuscripts/NotebookLM Etkinliği/`
- `Augmented Dietitian/` → `Manuscripts/Augmented Dietitian/`
- `Augmented Dietitian Okunmuşlar/` → `Manuscripts/Augmented Dietitian/Okunmuşlar/` (alt klasör)
- `Personalized Fasting/` → `Manuscripts/Personalized Fasting/`
- `Reklam Kurulu Kararları/` → `Manuscripts/Reklam Kurulu Kararları/`
- `Manuscripts/demo_project/` (sentetik test verisiydi, gerçek çalışman değildi) → `Templates/Ornek_R_Analiz_Projesi/` olarak taşındı

### Akademik (yeni klasör)
- `COST Actions/` → `Akademik/COST Actions/`
- `Postdoc/` → `Akademik/Postdoc/`
- `Yeni Akreditasyon Yapılanması.md` → `Akademik/`

### AI Kontrol Merkezi (yeni klasör, eski "AI Kontrol Merkezi" yerine geçti)
- `AI Kontrol Merkezi/` klasörünün tamamı (Clippings İşlenmiş, MOC, NotebookLM Ham/İşlenmiş, Zotero Ham/İşlenmiş) → `AI Kontrol Merkezi/` olarak yeniden adlandırıldı.
- `00 Kontrol Merkezi/Claude Skills/` → `AI Kontrol Merkezi/Claude Skills/`
- `00 Kontrol Merkezi/Claude Komut Protokolü.md` → `AI Kontrol Merkezi/`
- `00 Kontrol Merkezi/Vault_Bakim_ve_Entegrasyon_Protokolu.md` → `AI Kontrol Merkezi/`
- `00 Kontrol Merkezi/02_Akademik_Super_Komutlar_ve_Uretim_Playbook.md` → `AI Kontrol Merkezi/`
- `copilot/` (kök) → `AI Kontrol Merkezi/copilot/`

### Silinenler
- `GLP-1 CIM EBM Derlemesi/` (boştu) — silindi.

## BİLEREK DOKUNULMADI (otomasyonu bozmamak için)
- `00 Kontrol Merkezi/scripts/` (moc_panorama, molecular_radar, notion_book_gallery, run_nutrition_scout.sh) — dashboard'lardan sabit yolla çağrılıyor olabilir, doğrulanamadı.
- Kök dizindeki `scripts/`, `nutrition_scout.py`, `.scout_cache.json`, `sync_vault.py`, `semantic_linker.py`, `semantic_connection_engine.py`, `metadata_processor.py`, `citation_resolver.py`, `extract_stats.py`, `list_versions.py/.swift` — hiçbiri taşınmadı; bazıları (`nutrition_scout.py`, `metadata_processor.py`, `semantic_connection_engine.py`, `semantic_linker.py`) klasör adlarını (`Çalışma Fikirleri`, `Dersler`, `00 Kontrol Merkezi`) koduna gömülü olarak kullanıyor, bu yüzden bu klasörlerin **isimleri** hiç değiştirilmedi.
- `00 Kontrol Merkezi/Digests/` (digest çıktıları + scout logları) — `nutrition_scout.py` ve `run_nutrition_scout.sh` bu tam yola sabit yazıyor, taşınmadı.
- `00 Kontrol Merkezi` klasörünün adı ("00 " öneki dahil) değiştirilmedi — `sync_vault.py` bu ismi kodunda kullanıyor.

## HENÜZ KARAR VERİLMEMİŞ / GÖZDEN GEÇİRİLMESİ GEREKEN
- `Kitaplar/_Notion Arsivinden - Kontrol Bekliyor/` (69 dosya) — manuel karşılaştırma bekliyor.
- Kök dizinde hâlâ dağınık duran, bu oturumda karar verilmeyen dosyalar: ekran görüntüleri, `.canvas` dosyaları, `Kitaplar.md`, `Notlar.md`, `İstatistik Karar Ağacı.md`, `Personalized Fasting_first_draft.md` (muhtemelen `Manuscripts/Personalized Fasting/` içine taşınmalı), `Atama İlanı.md` (muhtemelen Akademik'e), `table-export-00X.csv`, `literature_export.csv`, `TEST_OBSIDIAN_WRITE.txt`.
- `00 Kontrol Merkezi/Kitaplar.md` ve `00 Kontrol Merkezi/Derslerim.md` gibi dashboard notları ile kök dizindeki `Kitaplar.md` arasında muhtemel bir çakışma var, incelenmedi (bu reorg'un kapsamı dışındaydı).


## Ek değişiklikler (2026-09-05, ikinci tur)

### Digest klasörü taşındı
- `00 Kontrol Merkezi/Digests/` (5 Digest_*.md + 3 log dosyası) → `00 Kontrol Merkezi/Digests/` olarak taşındı.
- `_Inbox/` klasörü boşaldığı için silindi.
- **Path düzeltmeleri yapıldı (kullanıcı onayıyla, sadece yol string'leri değişti):**
  - `nutrition_scout.py`: `OUTPUT_DIR` artık `00 Kontrol Merkezi/Digests`'i gösteriyor; "son taranan dosyaları" filtreleyen satır (`_Inbox` kontrolü) `OUTPUT_DIR`'a göre çalışacak şekilde güncellendi (aksi halde script kendi ürettiği digest'leri "yeni içerik" sanabilirdi); iki adet kozmetik print/docstring string'i de yeni yolu gösterecek şekilde güncellendi.
  - `00 Kontrol Merkezi/scripts/run_nutrition_scout.sh`: log dosyası yolundaki 3 satır `00 Kontrol Merkezi/Digests/scout_runner.log`'u gösterecek şekilde güncellendi.
- Script'lerin başka hiçbir satırına dokunulmadı.

### _Data/ klasörü silindi
- `_Data/meta_analysis_matrix.csv` (32 KB, ne işe yaradığı bilinmiyordu) kullanıcı talebiyle kalıcı olarak silindi.
- Hiçbir script bu klasöre referans vermiyordu (kontrol edildi), silinmesi başka bir şeyi etkilemedi.


## Ek değişiklikler (2026-09-05, üçüncü tur)

### Kök dizindeki başıboş ekran görüntüleri -> Files/
17 resim dosyası ("Ekran Resmi ...png" x14, "ABCDrisk1-3.png") kök dizinden `Files/` klasörüne taşındı.

**Not içeriklerine dokunulmadı**: Bu resimleri gösteren notlar (`Notlar/*.md` içinde `![[ABCDrisk1.png]]` gibi) Obsidian'ın çıplak-dosya-adı wikilink formatını kullanıyor — Obsidian bu tür linkleri klasör fark etmeksizin dosya adına göre tüm kasada arayıp buluyor, bu yüzden taşıma bu embedleri bozmadı, hiçbir not düzenlenmesi gerekmedi.

`Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/Sunumlar/Konu1_Obezite_Sunum.html` ve `Konu1_Slayt_Haritasi.md` de bu isimlerden bahsediyor ama kendi yanındaki `Sunumlar/assets/` klasöründe bu resimlerin BAĞIMSIZ birer kopyasını zaten barındırıyor — o yüzden kök dizindeki taşımadan hiç etkilenmediler.

(Not: `ABCDrisk1-3.png` zaten hem kökte hem `Sunumlar/assets/` içinde iki ayrı kopya olarak duruyordu — bu, taşımadan önce de var olan bir durumdu, taşıma bunu değiştirmedi.)
