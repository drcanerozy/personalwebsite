# SEO & İçerik Yayınlama Kuralları

Bu kurallar `personalwebsite` reposunda yeni içerik üretirken, düzenlerken veya derlerken daima geçerlidir:

1. **Yayın Öncesi Derleme ve Link Kontrolü:**
   Her içerik ekleme/düzenleme sonrasında mutlaka `python3 build.py` ve `python3 scripts/check-links.py` çalıştırılmalı; 0 kırık link teyit edilmelidir.

2. **Slug Transliterasyonu:**
   Türkçe başlıklardan slug üretirken Türkçe karakterler doğrudan İngilizce ASCII eşdeğerlerine dönüştürülmeli (`ı→i, ş→s, ğ→g, ü→u, ö→o, ç→c, İ→i`). İngilizce yazılar için mutlaka başlıktan türetilmiş anlamlı İngilizce slug kullanılmalıdır.

3. **İki Dilli Eşleştirme (Bilingual Pairing):**
   - TR yazılarda `en_slug: "<ingilizce-slug>"`
   - EN yazılarda `tr_slug: "<turkce-slug>"`
   bulunmalıdır. Bu sayede hreflang ve sitemap `xhtml:link` çapraz eşleşmesi otomatik yapılır.

4. **Karakter Sınırları:**
   - `<title>`: En fazla 65 karakter (otomasyon ` | Caner Özyıldırım` ekler).
   - `meta description` (`summary`): 140–160 karakter aralığında, anahtar kelime ilk 120 karakterde.

5. **Tek H1 & E-E-A-T Bütünlüğü:**
   Her sayfada yalnızca 1 adet H1 etiketi yer almalıdır. Makale gövdesi ara başlıkları `##` ve `###` olmalıdır. E-E-A-T timestamps, Tıbbi Sorumluluk Reddi ve 3 İlgili Yazı kümelemesi `build.py` tarafından otomatik enjekte edilir.
