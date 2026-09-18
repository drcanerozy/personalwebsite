---
TÜR:
ODAK:
MEKANİZMA:
DİZİN:
ETİKET:
BAĞLANTILI NOTLAR:
BAĞLANTILI ÇALIŞMA FİKİRLERİ:
BAĞLANTILI DERSLER:
YORUM:
KAYNAK:
---
Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?
Obezite
Kevin Hall gibi araştırmacılar bu deneyleri "Enerji Dengesi Modeli'ni (EBM)" kanıtlamak için tasarladılar. Onların varsayımına göre dışkı ve idrarla atılan standart oranlar (kilo alımında %7, kilo kaybında %11 gibi sabit düzeltmeler) hesaba katıldıktan sonra, geriye kalan ve oksijenle yakılmayan her şeyin vücutta depolanması gerekir. Bu yüzden o "gizli kaçakları" özel olarak ölçme gereği duymadılar.

**Peki o zaman bu analizi siz nasıl yapacaksınız? (Adli Muhasebe Yöntemi)**

Cevap, Francisco Arencibia-Albite'nin 2026 yılındaki güncel çalışmasında yatmaktadır. Arencibia-Albite, Kevin Hall'un açık erişimli veri setini (OSF: `https://osf.io/zdwqb/`) kullanarak, **ölçülmemiş olanı, "matematiksel bir hata (açık)" üzerinden kanıtlamıştır**. Sizin fenotip fikrinizi bu veri setleriyle hayata geçirmek için tam olarak şu "adli muhasebe" (forensic accounting) adımlarını izleyebilirsiniz:

**1. Elinizdeki Veri Setinde Hangi Değişkenler Var?** Hall'un klinik deney (metabolic ward) veri setlerinde ihtiyacınız olan şu temel değişkenler halihazırda ölçülmüş olarak mevcuttur:

- **DXA Taraması Sonuçları:** Fiziksel Yağ Kütlesi (FM) ve Yağsız Kütle (FFM) değişimleri.
- **Alınan Enerji ve Madde:** Günlük alınan kalori (EI) ve makrobesinlerin (yağ, karb, protein) gram cinsinden miktarları (FI, CI, PI).
- **Harcama ve Oksidasyon:** Solunum odasında (metabolic chamber) ölçülen günlük Enerji Harcaması (EE) ve gaz değişiminden (O2 ve CO2) hesaplanan "Oksitlenmiş (Yakılmış) Yağ" miktarı (FOx).

**2. EBM'nin Kendi İçindeki Tutarsızlığını (Kaçağı) Hesaplamak** Veri setini indirdikten sonra, Arencibia-Albite'nin 3. Sayısal Tutarlılık Testini uygularsınız. EBM'nin kendi matematiksel kurallarına göre, bir kişinin vücudundaki fiziksel yağ değişim miktarı (ΔFM), yediği yağ (FI) eksi oksijenle yaktığı yağ (FOx) olmak zorundadır:ΔFM/Zaman=AlınanYag˘​(FI)−YakılanYag˘​(FOx)

İşte dananın kuyruğunun koptuğu yer burasıdır. Veri setindeki DXA ölçümlerini (gerçek fiziksel yağ değişimi) alıp, solunum odasındaki yakılan yağdan çıkardığınızda **matematiğin tutmadığını göreceksiniz**. Örneğin Hall'un verilerinde katılımcılar, EBM'nin öngördüğünden çok daha farklı ve oksijenle yakmadıkları halde açıklanamayan fiziksel kütle kayıpları/kazançları yaşamışlardır.

**3. Aradaki "Kayıp Kütle" Sizin "Atılan Enerjinizdir"** Kişi kalorimetre cihazında (solunum odasında) o yağı oksijen kullanarak **yakmamış**, diyetle de almamış ama DXA taramasında yağ kütlesi fiziksel olarak kaybolmuş. O kütle nereye gitti? EBM bu soruya cevap veremez (ölçüm hatası der geçer). Ancak Kütle Dengesi (Mass Balance) çerçevesinden bakıldığında, aradaki bu matematiksel fark (discrepancy), ketonlar veya mevalonik asit gibi yanmadan **idrar, ter ve solunum yoluyla sızan "atılan/oksitlenmemiş kütledir"**. Onların ölçmediği değeri, siz formüldeki "hata payı" üzerinden net bir şekilde hesaplamış olursunuz.

**4. Kendi Teorinizle (Fenotipleme) Sentezlemek** Sizin o harika fikrinizi uygulayacağınız aşama tam olarak burasıdır:

- Önce veri setindeki katılımcıları, diyetin ilk haftasındaki Enerji Harcaması (EE) düşüşlerine bakarak **"Tutumlu (Thrifty)"** (EE'si çok düşenler) ve **"Savurgan (Spendthrift)"** (EE'si düşmeyenler) olarak ayırın.
- Sonra 2. ve 3. adımlardaki "Kayıp Kütle / Atılan Enerji (Leakage)" hesabını bu iki gruba ayrı ayrı uygulayın.

Eğer analizinizin sonucunda, **"Savurgan (Spendthrift) fenotiplerde, DXA ile solunum odası arasındaki uyuşmazlığın (yani vücuttan yanmadan atılan kütle/enerjinin) Tutumlu fenotiplere kıyasla istatistiksel olarak çok daha büyük olduğunu"**bulursanız; EBM'yi tamamen çürütmüş ve obezite literatürüne yepyeni bir "Kişiselleştirilmiş Kütle Dengesi" modeli kazandırmış olursunuz.

Bu veri seti açık (Open Science Framework), bu denklemler biliniyor. Tek eksik, verileri EBM'yi doğrulamak için değil, bu kütle kaçağını (excretion) fenotiplere göre analiz etmek için kullanacak bir araştırmacı vizyonudur.

## Bağlantılı Notlar
- [[Vücut Ağırlığı, Adipozite ve Obezite Modelleri - Neden Yağlanıyoruz ve Sistem Nasıl Kontrol Ediliyor?]]
- [[Vücut Ağırlığının Matematiği]]
- [[Vücut Ağırlığı Modelleri ve Obezite Hipotezlerine Göre Kilo Kaybında Plato Dönemi]]
- [[Kalori Kısıtlaması, Kilo Kaybı Olmasa da İnsülin Direncini Kısa Sürede İyileştiriyor, Ancak Doku Bazında Etkileri Farklı.]]
- [[Adipoz Doku]]
