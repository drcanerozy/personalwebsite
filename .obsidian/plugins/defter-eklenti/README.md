# Defter

## Kurulum
1. Bu klasörü (`defter-eklenti`) vault'unun şu yoluna kopyala:
   `<vault>/.obsidian/plugins/defter-eklenti/`
2. Obsidian'ı yeniden başlat, Ayarlar → Topluluk Eklentileri → "Defter"i aç (enable).
   Eskiden tek-defter sürümünü kullanıyorsan ayarların otomatik olarak yeni çoklu-defter
   formatına taşınır, hiçbir şey kaybolmaz.

## Kurulum sonrası
1. Ayarlar → Defter sekmesinden **"+ Defter"** ile en az bir defter tanımla: isim, klasör,
   navigasyon modu (sabit/canlı/manuel), kağıt teması.
2. Birden fazla defter tanımlayabilirsin — her biri ayrı bir klasörü izler.
3. Ayarlar → Kısayol Tuşları'ndan "Sonraki sayfa", "Önceki sayfa", "Hızlı not ekle"
   komutlarına kendi tuş kombinasyonunu ata.

## Kullanım

**Gezinme**: Bir defter klasöründeki herhangi bir notu aç, "Sonraki sayfa" / "Önceki sayfa"
komutlarıyla (ya da atadığın kısayollarla) o defterin sırasında ilerle/geri git. Status bar'da
"DefterAdı: 3/47" şeklinde konumun görünür.

**Hızlı not**: Kısayolla küçük bir pencere açılır. Birden fazla defterin varsa hangisine
yazacağını seçersin. Ctrl/Cmd+Enter ile kaydeder, otomatik olarak yeni bir not oluşturur ve
sıraya ekler.

**Devam eden işler (görev taşıma)**: Hızlı not ile yeni bir not oluşturduğunda, o defterde bir
önceki notta `- [ ]` ile işaretlenmiş ama tamamlanmamış satırlar varsa, otomatik olarak yeni
notun başına "## Devam eden işler" bölümü altında kopyalanır. Bu satırları silersen bir sonraki
nota taşınmaz — eski notlarda kayıt olarak kalır. Bir görevi nerede işaretlersen işaretle
(`- [x]`), ilk oluşturulduğu nota otomatik olarak "✅ [tarih] tarihinde tamamlandı" notu düşülür.

**Dashboard**: Ayarlar sekmesinden ya da "Dashboard notu oluştur / güncelle" komutuyla, tüm
tanımlı defterlerdeki bekleyen ve tamamlanan görevleri listeleyen bir "Defter Dashboard.md"
notu oluşturulur. **Dataview eklentisinin kurulu ve etkin olması gerekir.**

## Teknik notlar
- Notların sırası, dosya sisteminin `ctime`/`mtime` değeri yerine önce notun kendi
  frontmatter'ındaki `defter-created` / `defter-modified` alanlarına bakar (senkronizasyon
  ortamlarında dosya sistemi tarihleri güvenilmez olabildiği için). Eski notlar ilk açılışta
  otomatik olarak damgalanır.
- Görev taşıma sadece **Hızlı not** akışında tetiklenir; Obsidian'ın normal "Yeni not"
  komutuyla oluşturduğun notlarda otomatik çalışmaz.
- Kağıt teması sadece aktif düzenleyicide, o an açık olan not bir defter klasörüne aitse
  uygulanır.
