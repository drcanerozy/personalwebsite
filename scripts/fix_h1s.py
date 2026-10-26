import re

# 1. 01-beslenmenin-evrimi.html
p = '/Users/canerozyildirim/Sites/personalwebsite/slides/01-beslenmenin-evrimi.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<h1 class="text-xs sm:text-sm font-bold text-stone-900 tracking-wide font-serif">', '<p class="text-xs sm:text-sm font-bold text-stone-900 tracking-wide font-serif">')
c = re.sub(r'(<p class="text-xs sm:text-sm font-bold text-stone-900 tracking-wide font-serif">.*?BESLENME.*?)(</h1>)', r'\1</p>', c, flags=re.DOTALL)
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

# 2. beslenmenin_evrimi_sunum.html
p = '/Users/canerozyildirim/Sites/personalwebsite/slides/beslenmenin_evrimi_sunum.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<h1 class="text-xs sm:text-sm font-bold text-stone-900 tracking-wide font-serif">', '<p class="text-xs sm:text-sm font-bold text-stone-900 tracking-wide font-serif">')
c = re.sub(r'(<p class="text-xs sm:text-sm font-bold text-stone-900 tracking-wide font-serif">.*?BESLENME.*?)(</h1>)', r'\1</p>', c, flags=re.DOTALL)
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

# 3. 01-bilgisayar-ve-yapay-zeka.html: Keep first h1, change remaining 9 h1s to h2
p = '/Users/canerozyildirim/Sites/personalwebsite/slides/01-bilgisayar-ve-yapay-zeka.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

first_h1_match = re.search(r'<h1\b[^>]*>.*?</h1>', c, re.DOTALL)
if first_h1_match:
    idx = first_h1_match.end()
    head_part = c[:idx]
    rest_part = c[idx:]
    rest_part = re.sub(r'<h1(\b[^>]*)>', r'<h2\1>', rest_part)
    rest_part = rest_part.replace('</h1>', '</h2>')
    c = head_part + rest_part
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

# 4. 02-diyetler-ise-yaramiyor-mu.html
p = '/Users/canerozyildirim/Sites/personalwebsite/slides/02-diyetler-ise-yaramiyor-mu.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<div class="slide"><h1 style="font-size:clamp(30px,4vw,54px); margin-bottom:30px;">${s.title}</h1>', '<div class="slide"><h2 style="font-size:clamp(30px,4vw,54px); margin-bottom:30px;">${s.title}</h2>')
c = c.replace('<h1 class="slide-title" style="margin:0 auto 16px; max-width:24ch; text-align:center;">${s.title}</h1>', '<h2 class="slide-title" style="margin:0 auto 16px; max-width:24ch; text-align:center;">${s.title}</h2>')
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

# 5. 02-hafta-2-yapay-zeka-beslenme-bilimini-nasil-donusturuyor.html
p = '/Users/canerozyildirim/Sites/personalwebsite/slides/02-hafta-2-yapay-zeka-beslenme-bilimini-nasil-donusturuyor.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<h1 class="slide-title">4P Tıp Çağı: <em>Sağlık ve Beslenmenin Yeni Anayasası</em></h1>', '<h2 class="slide-title">4P Tıp Çağı: <em>Sağlık ve Beslenmenin Yeni Anayasası</em></h2>')
c = c.replace('<h1 class="slide-title" style="margin:0 auto 16px; max-width:24ch; text-align:center;">10 Slaytlık Açık Önizleme <em>Tamamlanmıştır</em></h1>', '<h2 class="slide-title" style="margin:0 auto 16px; max-width:24ch; text-align:center;">10 Slaytlık Açık Önizleme <em>Tamamlanmıştır</em></h2>')
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

# 6. 02-obezite-uygulama.html
p = '/Users/canerozyildirim/Sites/personalwebsite/slides/02-obezite-uygulama.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('class="eyebrow">${esc(s.eyebrow||s.section)}</div><h1>${esc(s.title)}</h1>', 'class="eyebrow">${esc(s.eyebrow||s.section)}</div><h2>${esc(s.title)}</h2>')
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

# 7. 03-diyabet-ve-tibbi-beslenme-tedavisi.html
p = '/Users/canerozyildirim/Sites/personalwebsite/slides/03-diyabet-ve-tibbi-beslenme-tedavisi.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<h1 class="slide-title" style="font-size:clamp(26px, 3.2vw, 42px); margin-bottom:14px; color:var(--ink);">10 Slaytlık Açık Önizleme Tamamlanmıştır</h1>', '<h2 class="slide-title" style="font-size:clamp(26px, 3.2vw, 42px); margin-bottom:14px; color:var(--ink);">10 Slaytlık Açık Önizleme Tamamlanmıştır</h2>')
c = c.replace('span class="eyebrow" style="justify-content:center;">BÖLÜM GEÇİŞİ</span>\n        <h1 class="slide-title"', 'span class="eyebrow" style="justify-content:center;">BÖLÜM GEÇİŞİ</span>\n        <h2 class="slide-title"')
c = c.replace('</span>\n        <h2 class="slide-title" style="font-size:clamp(28px, 3.8vw, 48px); margin-bottom:12px;">${esc(title)}</h1>', '</span>\n        <h2 class="slide-title" style="font-size:clamp(28px, 3.8vw, 48px); margin-bottom:12px;">${esc(title)}</h2>')
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('H1 fixes completed successfully!')
