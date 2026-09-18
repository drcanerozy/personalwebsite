---
tags: [protokol, claude]
---

# 🤖 Claude Komut Protokolü — Faz 2

Bu dosya, Claude'un AI Kontrol Merkezi klasöründe nasıl çalışacağını tanımlar.
Her oturumda bu dosyayı okuyarak başla.

---

## 📁 Klasör Yapısı

```
vault/
├── 00 Kontrol Merkezi/
│   ├── 00_Ana_Kokpit.md               ← Master kontrol paneli
│   ├── Dashboard_Gaps_and_Contradictions.md ← Null bulgular ve çelişki panosu
│   ├── Kitaplar.md                    ← Kitap galerisi & tablosu
│   ├── Fikir Üretim Logu.md
│   ├── Katman Analizi Geçmişi.md
│   └── 02_Akademik_Super_Komutlar_ve_Uretim_Playbook.md
│
├── AI Kontrol Merkezi/                          ← Claude'un çalışma alanı
│   ├── Clippings İşlenmiş/            ← Web içerikleri
│   ├── Zotero İşlenmiş/               ← Akademik notlar
│   ├── NotebookLM İşlenmiş/           ← Literatür özeti notları
│   └── MOC/                           ← Tematik haritalar
│
├── 00 Kontrol Merkezi/Digests/                    ← Canlı literatür bültenleri (Haftada 2x / 4 gün)
├── Clippings/                         ← Ham web içerikleri (dokunma)
├── Notlar/                            ← Senin olgunlaştırdıkların
└── Çalışma Fikirleri/                 ← Araştırma fikirleri
```

---

## ⌨️ KOMUT 1 — Clipping İşle

**Kullanım:** `"[dosya adı] clipping'ini işle"`
veya: `"Clippings klasöründeki yeni içerikleri işle"`

**Claude ne yapar:**
1. Clippings klasöründeki belirtilen (veya işlenmemiş) dosyayı okur
2. AI Kontrol Merkezi şablonunu doldurur:
   - Türkçe özet (3-5 cümle)
   - Anahtar bulgular (madde madde)
   - ODAK, MEKANİZMA, DİZİN alanlarını doldurur
   - ÖNEMLİ derecesi atar (🔴/🟡/🟢)
   - Mevcut notlarla bağlantı önerir
3. `AI Kontrol Merkezi/Clippings İşlenmiş/` klasörüne kaydeder
4. MOC'u günceller

**Önem derecesi kriterleri:**
- 🔴 Kesinlikle oku: Birden fazla odak alanına dokunan, klinik/metodolojik önemi yüksek içerik
- 🟡 Okumaya değer: Tek odak alanına güçlü katkı sağlayan içerik
- 🟢 Özet yeterli: Genel bağlam, arka plan bilgisi

---

## ⌨️ KOMUT 2 — Zotero Notu İşle

**Kullanım:** `"Zotero notlarını işle"` veya `"[makale adı] Zotero notunu işle"`

**Claude ne yapar:**
1. Obsidian'daki Zotero import'unu okur (highlight'lar + notlar)
2. Türkçeye çevirir
3. AI Kontrol Merkezi şablonunu doldurur:
   - Metodoloji özeti
   - Ana bulgular (Türkçe)
   - Klinik/araştırma önemi
   - DOI/kaynak bilgisi KAYNAK_URL'ye
4. `AI Kontrol Merkezi/Zotero İşlenmiş/` klasörüne kaydeder
5. Çalışma fikri adaylarını işaretler

---

## ⌨️ KOMUT 3 — NotebookLM Notu İşle

**Kullanım:** `"[defter adı] NotebookLM notunu işle"`

**Akış:**
1. Sen NotebookLM'de ilgili defterle konuşursun
2. Cevabı buraya yapıştırırsın (veya eklenti üzerinden)
3. Claude işler:
   - Yapılandırır (başlıklar, maddeler)
   - Katmanlar (ODAK, MEKANİZMA, DİZİN)
   - Mevcut notlarla bağlantı kurar
   - Çekirdek not adayı olabilecekleri işaretler
4. `AI Kontrol Merkezi/NotebookLM İşlenmiş/` klasörüne kaydeder

**Standart NotebookLM prompt şablonu:**
```
Bu PDF'lerdeki şu konuyu analiz et: [KONU]
Şu soruları yanıtla:
1. Ana mekanizma nedir?
2. Klinik önemi nedir?
3. Mevcut literatürle çelişen bulgular var mı?
4. Metodolojik güçlü/zayıf yanlar neler?
5. Araştırma boşlukları neler?
Yanıtlarını maddeler halinde ver.
```

---

## ⌨️ KOMUT 4 — AI Kontrol Merkezi Dashboard Güncelle

**Kullanım:** `"AI Kontrol Merkezi'i analiz et"`

**Claude ne yapar:**
1. Tüm AI Kontrol Merkezi alt klasörlerini okur
2. Şunları raporlar:
   - İşlenmemiş içerik sayısı (klasör başına)
   - 🔴 önem dereceli içerikler listesi
   - Bu dönem işlenen içeriklerin odak/mekanizma dağılımı
   - Notlar klasörüne taşıma önerileri
   - Yeni çalışma fikri adayları
3. Fikir Üretim Logu'na ekler

---

## ⌨️ KOMUT 5 — MOC Oluştur / Güncelle

**Kullanım:** `"[KONU] için MOC oluştur"`

**Claude ne yapar:**
1. AI Kontrol Merkezi + Notlar + Çalışma Fikirleri'nden ilgili içerikleri toplar
2. Tematik bir harita oluşturur:
   - Temel kavramlar
   - Mekanizma bağlantıları
   - Açık sorular / boşluklar
   - Okuma sırası önerisi
3. `AI Kontrol Merkezi/MOC/` klasörüne kaydeder

---

## 🚦 Karar Protokolü — Ne Notlar'a Taşınır?

| Kriter | Karar |
|--------|-------|
| Orijinal analiz/yorum içeriyor | ✅ Notlar'a taşı |
| Birden fazla odakla bağlantılı ve derin | ✅ Notlar'a taşı |
| Sadece özet/referans niteliğinde | 🔄 AI Kontrol Merkezi'de kalır |
| Tek bir çalışmanın bulgusu | 🔄 AI Kontrol Merkezi'de kalır |
| Güncel ama hızla eski olacak | ❌ Sil / arşivle |
| Tekrar eden içerik | ❌ Sil |

---

## 📌 Önemli Kurallar

1. **AI Kontrol Merkezi ≠ Notlar** — AI Kontrol Merkezi ham hammadde deposu. Notlar senin olgunlaştırdıkların.
2. **Çekirdek not kararı sende** — Claude işaretler, sen taşırsın.
3. **Her oturumda bu dosyayı oku** — Sonraki Claude bağlamı bilmez.
4. **Kalabalık = kirlilik** — Ayda bir AI Kontrol Merkezi'i temizle.
