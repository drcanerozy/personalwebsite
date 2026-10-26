/**
 * Akademik Sunum Şifreleme, Güvenlik ve PDF İndirme Motoru
 * Dr. Caner ÖZYILDIRIM — Kişisel Web Sitesi Altyapısı
 * 
 * Özellikler:
 * 1. Şifre Kilit Ekranı Yönetimi: Kapakta, üst barda ve 10. slaytta şifre sorma garantisi.
 * 2. Buton Disabled Hatası Çözümü: 10. slaytta ileri butonlarının kilitlenmesini engeller.
 * 3. Saf Metin Odaklı PDF İndirme: Tüm slaytların metinlerini temiz, okunabilir A4 ders notu olarak PDF'e çevirip indirir.
 * 4. Mobil Swipe / Dokunmatik Navigasyon: Mobilde slayt atlama ve 10. slayt kilit tetikleyicisi.
 */

(function () {
  'use strict';

  // Global Değişkenler
  window.pendingDownloadPdf = false;

  // 1. html2pdf Kütüphanesinin Yüklenmesini Sağla
  function ensureHtml2Pdf(callback) {
    if (typeof html2pdf !== 'undefined') {
      if (callback) callback();
      return;
    }
    const script = document.createElement('script');
    script.src = 'assets/html2pdf.bundle.min.js';
    script.onload = () => { if (callback) callback(); };
    script.onerror = () => {
      // CDN Fallback
      const cdnScript = document.createElement('script');
      cdnScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
      cdnScript.onload = () => { if (callback) callback(); };
      document.head.appendChild(cdnScript);
    };
    document.head.appendChild(script);
  }

  // 2. Metin İçeriğini Çıkarıcı (Hem JSON SLIDES hem DOM elementleri için)
  function extractAllSlidesText() {
    const slideItems = [];

    // Durum A: window.SLIDES dizisi varsa
    if (window.SLIDES && Array.isArray(window.SLIDES) && window.SLIDES.length > 0) {
      window.SLIDES.forEach((s, idx) => {
        const num = s.orderNum || (idx + 1);
        let title = s.title || s.eyebrow || s.tag || `Slayt ${num}`;
        title = title.replace(/<[^>]+>/g, '').trim();

        let category = s.category || s.section || '';
        if (!category && s.sec !== undefined && window.SECTIONS && window.SECTIONS[s.sec]) {
          category = window.SECTIONS[s.sec];
        }

        let subtitle = s.subtitle || s.sub || s.kicker || s.lede || '';
        subtitle = subtitle.replace(/<[^>]+>/g, '').trim();

        const bullets = [];
        if (s.bullets && Array.isArray(s.bullets)) {
          s.bullets.forEach(b => {
            const clean = String(b).replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
            if (clean) bullets.push(clean);
          });
        }

        if (s.takeaway) {
          bullets.push("Önemli Not: " + String(s.takeaway).replace(/<[^>]+>/g, ' ').trim());
        }
        if (s.note) {
          bullets.push("Akademik Not: " + String(s.note).replace(/<[^>]+>/g, ' ').trim());
        }

        // Tablo varsa
        let tableData = null;
        if (s.table && s.table.headers) {
          tableData = {
            headers: s.table.headers,
            rows: s.table.rows || []
          };
        }

        slideItems.push({
          num,
          title,
          category,
          subtitle,
          bullets,
          tableData
        });
      });
      return slideItems;
    }

    // Durum B: DOM .slide elementleri taranır
    const domSlides = document.querySelectorAll('.slide');
    if (domSlides.length > 0) {
      domSlides.forEach((slideEl, idx) => {
        if (slideEl.id === 'slide_preview_lock') return; // Kilit ekranını notlara ekleme

        const titleEl = slideEl.querySelector('.slide-title, h1, .slide-header-title, .title, h2');
        const eyeEl = slideEl.querySelector('.eyebrow, .pill, .tag, .kicker');
        const subEl = slideEl.querySelector('.lede, .sub, .slide-sub, .subtitle');

        const num = idx + 1;
        const title = titleEl ? titleEl.textContent.trim().replace(/\s+/g, ' ') : `Slayt ${num}`;
        const category = eyeEl ? eyeEl.textContent.trim().replace(/\s+/g, ' ') : '';
        const subtitle = subEl ? subEl.textContent.trim().replace(/\s+/g, ' ') : '';

        const bullets = [];
        slideEl.querySelectorAll('p, li, .card, .taxo-card, .flip-back, .box').forEach(el => {
          // Başlık elementlerini tekrar ekleme
          if (el === titleEl || el === eyeEl || el === subEl) return;
          if (el.closest('.slide-title') || el.closest('.eyebrow')) return;
          const txt = el.textContent.trim().replace(/\s+/g, ' ');
          if (txt && txt.length > 3 && !bullets.includes(txt)) {
            bullets.push(txt);
          }
        });

        slideItems.push({
          num,
          title,
          category,
          subtitle,
          bullets,
          tableData: null
        });
      });
    }

    return slideItems;
  }

  // 3. Yazıcı ve PDF Dostu HTML Şablonu Oluşturucu
  function buildCleanPdfHtml() {
    const slides = extractAllSlidesText();
    const docTitle = (document.title || 'Ders Sunumu').replace(/\|.*/, '').trim();
    const totalCount = slides.length;

    let html = `
    <div style="font-family:'Segoe UI', -apple-system, Roboto, Helvetica, Arial, sans-serif; color:#1e293b; padding:24px; max-width:800px; margin:0 auto; line-height:1.5;">
      <!-- Kapak & Başlık Bilgisi -->
      <div style="border-bottom:2px solid #0f172a; padding-bottom:18px; margin-bottom:24px; text-align:center;">
        <div style="font-size:11px; font-weight:800; color:#b45309; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:6px;">
          Akademik Ders Notları &amp; Sunum Metinleri
        </div>
        <h1 style="font-size:24px; font-weight:800; color:#0f172a; margin:0 0 10px; line-height:1.3;">
          ${docTitle}
        </h1>
        <div style="font-size:13px; color:#475569; display:flex; justify-content:center; align-items:center; gap:12px; flex-wrap:wrap;">
          <span style="font-weight:600;">Dr. Caner ÖZYILDIRIM</span>
          <span>•</span>
          <span>Toplam ${totalCount} Slayt</span>
          <span>•</span>
          <span style="color:#059669; font-weight:600;">🔒 Ders Şifresiyle Doğrulandı</span>
        </div>
        <p style="font-size:11px; color:#64748b; margin:10px 0 0; font-style:italic;">
          Bu doküman sunumun tüm slaytlarındaki akademik başlıkları, metinleri, maddeleri ve veri tablolarını içermektedir.
        </p>
      </div>
    `;

    // Her Slayt İçin Temiz Metin Kartı
    slides.forEach((s) => {
      html += `
      <div style="border:1px solid #cbd5e1; border-radius:10px; padding:14px 18px; margin-bottom:14px; background:#f8fafc; page-break-inside:avoid;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #e2e8f0; padding-bottom:6px; margin-bottom:8px;">
          <span style="font-size:11px; font-weight:800; color:#b45309; font-family:monospace;">#Slayt ${s.num}</span>
          ${s.category ? `<span style="font-size:10px; font-weight:700; color:#64748b; text-transform:uppercase; letter-spacing:0.5px;">${s.category}</span>` : ''}
        </div>
        <h3 style="font-size:15px; font-weight:700; color:#0f172a; margin:0 0 4px; line-height:1.35;">${s.title}</h3>
        ${s.subtitle ? `<div style="font-size:12px; color:#475569; font-style:italic; margin-bottom:8px; line-height:1.4;">${s.subtitle}</div>` : ''}
      `;

      if (s.bullets && s.bullets.length > 0) {
        html += `<ul style="margin:4px 0 0; padding-left:18px; font-size:12px; color:#334155; line-height:1.6;">`;
        s.bullets.forEach((b) => {
          html += `<li style="margin-bottom:4px;">${b}</li>`;
        });
        html += `</ul>`;
      }

      if (s.tableData && s.tableData.headers) {
        html += `
        <table style="width:100%; border-collapse:collapse; margin-top:10px; font-size:11px;">
          <thead>
            <tr>
              ${s.tableData.headers.map(h => `<th style="border:1px solid #cbd5e1; padding:6px; background:#e2e8f0; text-align:left; color:#1e293b;">${h}</th>`).join('')}
            </tr>
          </thead>
          <tbody>
            ${s.tableData.rows.map(row => `
              <tr>
                ${row.map(cell => `<td style="border:1px solid #cbd5e1; padding:5px 6px; color:#334155;">${cell}</td>`).join('')}
              </tr>
            `).join('')}
          </tbody>
        </table>`;
      }

      html += `</div>`;
    });

    html += `
      <div style="margin-top:28px; padding-top:14px; border-top:1px solid #cbd5e1; font-size:10px; color:#94a3b8; text-align:center;">
        Dr. Caner ÖZYILDIRIM • Kişisel Web Sitesi Altyapısı • Tüm Hakları Saklıdır
      </div>
    </div>`;

    return html;
  }

  // Modal: 4'lü ve 6'lı Slayt PDF Seçim Ekranı
  function ensurePdfModal() {
    if (document.getElementById('pdf-options-modal')) return;
    const modal = document.createElement('div');
    modal.id = 'pdf-options-modal';
    modal.style.cssText = 'display:none; position:fixed; inset:0; background:rgba(15,23,42,0.85); backdrop-filter:blur(8px); z-index:999999; align-items:center; justify-content:center; padding:16px; font-family:"Inter",system-ui,sans-serif;';
    modal.innerHTML = `
    <div style="background:#1e293b; border:1px solid #334155; border-radius:20px; max-width:440px; width:100%; padding:26px 24px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.5); text-align:center; position:relative; color:#f8fafc;">
      <button type="button" onclick="window.closePdfOptionsModal()" style="position:absolute; top:14px; right:14px; background:none; border:none; color:#94a3b8; font-size:18px; cursor:pointer; padding:4px 8px; border-radius:6px;">✕</button>
      <div style="width:48px; height:48px; border-radius:14px; background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); color:#ef4444; display:flex; align-items:center; justify-content:center; font-size:22px; margin:0 auto 12px;">📄</div>
      <h3 style="font-size:18px; font-weight:700; margin:0 0 6px; color:#ffffff;">Ders Notlarını İndir (PDF)</h3>
      <p style="font-size:12px; color:#94a3b8; line-height:1.5; margin:0 0 20px;">Lütfen çalışma ve yazdırma tercihinize uygun slayt düzenini seçiniz:</p>
      
      <div style="display:flex; flex-direction:column; gap:12px;">
        <button type="button" onclick="window.triggerPresentationPdfDownload('4lu')" style="background:#0f172a; border:1px solid rgba(56,189,248,0.4); border-radius:12px; padding:14px; text-align:left; cursor:pointer; display:flex; align-items:center; justify-content:space-between; transition:all .15s; color:#fff;" onmouseover="this.style.borderColor='#38bdf8'; this.style.background='#132238';" onmouseout="this.style.borderColor='rgba(56,189,248,0.4)'; this.style.background='#0f172a';">
          <div style="display:flex; align-items:center; gap:12px;">
            <span style="font-size:24px;">📑</span>
            <div>
              <div style="font-size:14px; font-weight:700; color:#38bdf8;">4'lü Slayt Düzeni (A4)</div>
              <div style="font-size:11px; color:#94a3b8;">Sayfa başına 4 slayt • Not almak ve rahat okumak için ideal</div>
            </div>
          </div>
          <span style="font-size:12px; font-weight:700; color:#38bdf8; padding:5px 10px; background:rgba(56,189,248,0.15); border-radius:8px;">İndir ↓</span>
        </button>

        <button type="button" onclick="window.triggerPresentationPdfDownload('6li')" style="background:#0f172a; border:1px solid rgba(52,211,153,0.4); border-radius:12px; padding:14px; text-align:left; cursor:pointer; display:flex; align-items:center; justify-content:space-between; transition:all .15s; color:#fff;" onmouseover="this.style.borderColor='#34d399'; this.style.background='#0e2e25';" onmouseout="this.style.borderColor='rgba(52,211,153,0.4)'; this.style.background='#0f172a';">
          <div style="display:flex; align-items:center; gap:12px;">
            <span style="font-size:24px;">📚</span>
            <div>
              <div style="font-size:14px; font-weight:700; color:#34d399;">6'lı Slayt Düzeni (A4)</div>
              <div style="font-size:11px; color:#94a3b8;">Sayfa başına 6 slayt • Kompakt ve ekonomik yazdırma</div>
            </div>
          </div>
          <span style="font-size:12px; font-weight:700; color:#34d399; padding:5px 10px; background:rgba(52,211,153,0.15); border-radius:8px;">İndir ↓</span>
        </button>
      </div>

      <div style="margin-top:16px; font-size:11px; color:#64748b;">
        🔒 Notlar ders şifresi ile korunan resmi sunum içeriğidir.
      </div>
    </div>`;
    document.body.appendChild(modal);
  }

  window.openPdfOptionsModal = function() {
    ensurePdfModal();
    const m = document.getElementById('pdf-options-modal');
    if (m) m.style.display = 'flex';
  };

  window.closePdfOptionsModal = function() {
    const m = document.getElementById('pdf-options-modal');
    if (m) m.style.display = 'none';
  };

  // 4. Doğrudan PDF İndirme Motoru (4'lü ve 6'lı seçenek desteği ile)
  window.triggerPresentationPdfDownload = function (layout) {
    // Mevcut sayfanın dosya adı / slug'ını belirle
    const pathParts = window.location.pathname.split('/');
    const currentFileName = pathParts[pathParts.length - 1] || '';
    const slugBase = currentFileName.replace(/\.html$/, '');

    // Çoklu düzen (4'lü / 6'lı) destekleyen sunum haritası
    const multiPdfMap = {
      '01-obezite-ve-tibbi-beslenme-tedavisi': {
        '4lu': '01-obezite-ve-tibbi-beslenme-tedavisi-4lu.pdf',
        '6li': '01-obezite-ve-tibbi-beslenme-tedavisi-6li.pdf'
      },
      'Konu1_Obezite_Sunum': {
        '4lu': '01-obezite-ve-tibbi-beslenme-tedavisi-4lu.pdf',
        '6li': '01-obezite-ve-tibbi-beslenme-tedavisi-6li.pdf'
      },
      '03-diyabet-ve-tibbi-beslenme-tedavisi': {
        '4lu': '03-diyabet-ve-tibbi-beslenme-tedavisi-4lu.pdf',
        '6li': '03-diyabet-ve-tibbi-beslenme-tedavisi-6li.pdf'
      },
      'Konu2_Diyabet_Sunum': {
        '4lu': '03-diyabet-ve-tibbi-beslenme-tedavisi-4lu.pdf',
        '6li': '03-diyabet-ve-tibbi-beslenme-tedavisi-6li.pdf'
      },
      '04-kardiyovaskuler-hastaliklar-ve-hipertansiyon': {
        '4lu': '04-kardiyovaskuler-hastaliklar-ve-hipertansiyon-4lu.pdf',
        '6li': '04-kardiyovaskuler-hastaliklar-ve-hipertansiyon-6li.pdf'
      },
      'Konu3_KVH_HT_Sunum': {
        '4lu': '04-kardiyovaskuler-hastaliklar-ve-hipertansiyon-4lu.pdf',
        '6li': '04-kardiyovaskuler-hastaliklar-ve-hipertansiyon-6li.pdf'
      }
    };

    // Eğer sunum 4'lü/6'lı destekliyorsa ve layout belirtilmemişse seçim modalını aç
    if (!layout && multiPdfMap[slugBase]) {
      window.openPdfOptionsModal();
      return;
    }

    // Kilit çözülmemişse önce şifre sor
    if (!window.isUnlocked) {
      window.pendingDownloadPdf = true;
      window.pendingPdfLayout = layout;
      window.closePdfOptionsModal();
      if (typeof window.openLockModal === 'function') {
        window.openLockModal(null, true);
      }
      return;
    }

    // Seçim yapıldıysa modalı kapat
    window.closePdfOptionsModal();

    // GitHub Repo & Doğrudan İndirme Base Yolları
    const rawGithubBase = 'https://raw.githubusercontent.com/drcanerozy/personalwebsite/main/slides/pdf';

    // Standart tekli eşleştirmeler
    const pdfMap = {
      '01-beslenmenin-evrimi': '01-beslenmenin-evrimi.pdf',
      'beslenmenin_evrimi_sunum': '01-beslenmenin-evrimi.pdf',
      '01-bilgisayar-ve-yapay-zeka': '01-bilgisayar-ve-yapay-zeka.pdf',
      '01-obezite-ve-tibbi-beslenme-tedavisi': '01-obezite-ve-tibbi-beslenme-tedavisi.pdf',
      '02-obezite-uygulama': '02-obezite-uygulama.pdf',
      '02-hafta-2-yapay-zeka-beslenme-bilimini-nasil-donusturuyor': '02-hafta-2-yapay-zeka-beslenme-bilimini-nasil-donusturuyor.pdf',
      '02-diyetler-ise-yaramiyor-mu': '02-diyetler-ise-yaramiyor-mu.pdf',
      '03-diyabet-ve-tibbi-beslenme-tedavisi': '03-diyabet-ve-tibbi-beslenme-tedavisi.pdf',
      'Konu2_Diyabet_Sunum': '03-diyabet-ve-tibbi-beslenme-tedavisi.pdf',
      'diyabet-ve-tibbi-beslenme-tedavisi': '03-diyabet-ve-tibbi-beslenme-tedavisi.pdf',
      '04-kardiyovaskuler-hastaliklar-ve-hipertansiyon': '04-kardiyovaskuler-hastaliklar-ve-hipertansiyon.pdf',
      'Konu3_KVH_HT_Sunum': '04-kardiyovaskuler-hastaliklar-ve-hipertansiyon.pdf',
      'diyetler-ise-yaramiyor-mu': '02-diyetler-ise-yaramiyor-mu.pdf'
    };

    let targetPdfName = '';
    if (layout && multiPdfMap[slugBase] && multiPdfMap[slugBase][layout]) {
      targetPdfName = multiPdfMap[slugBase][layout];
    } else {
      targetPdfName = pdfMap[slugBase] || (slugBase ? `${slugBase}.pdf` : 'ders_notlari.pdf');
    }

    const downloadUrl = `pdf/${targetPdfName}`;

    // PDF indirme durumunu butonlarda göster
    const pdfBtns = document.querySelectorAll('#header-pdf-btn, .pdf-download-btn');
    pdfBtns.forEach(btn => {
      btn.dataset.origHtml = btn.innerHTML;
      btn.innerHTML = '⚡ PDF İndiriliyor...';
    });

    function resetPdfBtns() {
      pdfBtns.forEach(btn => {
        if (btn.dataset.origHtml) btn.innerHTML = btn.dataset.origHtml;
      });
    }

    // Doğrudan indirmeyi tetikle
    const a = document.createElement('a');
    a.href = downloadUrl;
    a.download = targetPdfName;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      if (a.parentNode) document.body.removeChild(a);
      resetPdfBtns();
    }, 1500);
  };

  function renderDynamicTextPdf() {
    ensureHtml2Pdf(() => {
      const pdfBtns = document.querySelectorAll('#header-pdf-btn, .pdf-download-btn');
      pdfBtns.forEach(btn => {
        btn.disabled = true;
        btn.dataset.origHtml = btn.innerHTML;
        btn.innerHTML = '⏳ PDF Hazırlanıyor...';
      });

      // Görünmez A4 render konteyneri
      const container = document.createElement('div');
      container.style.position = 'fixed';
      container.style.left = '-9999px';
      container.style.top = '0';
      container.style.width = '794px';
      container.style.background = '#ffffff';
      container.innerHTML = buildCleanPdfHtml();
      document.body.appendChild(container);

      const rawTitle = (document.title || 'Ders_Notu').replace(/\|.*/, '').trim();
      const cleanTitle = rawTitle.replace(/[^a-zA-Z0-9çğıöşüÇĞİÖŞÜ]+/g, '_').replace(/^_+|_+$/g, '');
      const filename = `${cleanTitle}_Ders_Notlari.pdf`;

      if (typeof html2pdf !== 'undefined') {
        const opt = {
          margin: [10, 10, 10, 10],
          filename: filename,
          image: { type: 'jpeg', quality: 0.98 },
          html2canvas: { scale: 1.5, useCORS: true, logging: false },
          jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };

        html2pdf().set(opt).from(container).save().then(() => {
          if (container.parentNode) container.parentNode.removeChild(container);
          pdfBtns.forEach(btn => {
            btn.disabled = false;
            if (btn.dataset.origHtml) btn.innerHTML = btn.dataset.origHtml;
          });
        }).catch(err => {
          console.error("PDF oluşturma hatası, fallback yazıcı açılıyor:", err);
          fallbackPrint(container, pdfBtns);
        });
      } else {
        fallbackPrint(container, pdfBtns);
      }
    });
  };

  function fallbackPrint(container, pdfBtns) {
    const printWin = window.open('', '_blank');
    if (printWin) {
      printWin.document.write('<!DOCTYPE html><html><head><title>' + document.title + ' - Ders Notları</title><style>@page{size:A4;margin:10mm;}body{margin:0;font-family:sans-serif;}</style></head><body>' + container.innerHTML + '<script>window.onload=function(){window.print();};<\/script></body></html>');
      printWin.document.close();
    }
    if (container.parentNode) container.parentNode.removeChild(container);
    pdfBtns.forEach(btn => {
      btn.disabled = false;
      if (btn.dataset.origHtml) btn.innerHTML = btn.dataset.origHtml;
    });
  }

  // 5. Kilit Butonu ve UI Senkronizasyonu
  window.updateGlobalLockUI = function () {
    const lockBtns = document.querySelectorAll('#header-lock-btn, .header-lock-btn');
    lockBtns.forEach(btn => {
      if (window.isUnlocked) {
        btn.className = btn.className.replace(/bg-amber-[^\s]+/g, 'bg-emerald-50').replace(/text-amber-[^\s]+/g, 'text-emerald-800').replace(/border-amber-[^\s]+/g, 'border-emerald-300');
        btn.innerHTML = '<span>🔓</span><span class="hidden sm:inline">Kilit Açık</span>';
        btn.title = "Sunum kilidi açıldı";
      } else {
        btn.innerHTML = '<span>🔒</span><span class="hidden sm:inline">Ders Şifresi</span>';
        btn.title = "Ders şifresini gir ve tüm sunumu aç";
      }
    });

    const coverLockBtns = document.querySelectorAll('.cover-lock-btn');
    coverLockBtns.forEach(btn => {
      if (window.isUnlocked) {
        btn.innerHTML = '<span>🔓</span><span>Sunum Kilidi Açıldı</span>';
        btn.style.opacity = '0.7';
      }
    });
  };

  // 6. 10. Slaytta Buton Disabled Kalmasını Önleyen Gardiyan
  function protectNavButtons() {
    // Sıkı denetim periyodu
    setInterval(() => {
      if (!window.isUnlocked) {
        const nextBtns = document.querySelectorAll('#nextBtn, #topNextBtn, #btn-next');
        nextBtns.forEach(b => {
          // Eğer 10. slayt (veya son açık önizleme) civarındaysa asla disabled kalmasın!
          if (b.disabled) {
            b.disabled = false;
            // Tıklandığında kilit aç
            if (!b.dataset.lockHooked) {
              b.dataset.lockHooked = "1";
              b.addEventListener('click', (e) => {
                if (!window.isUnlocked) {
                  e.stopImmediatePropagation();
                  e.preventDefault();
                  if (typeof window.openLockModal === 'function') window.openLockModal(10);
                }
              }, true);
            }
          }
        });
      }
    }, 250);
  }

  // 7. Mobil Swipe (Kaydırma) Desteği
  function setupMobileSwipe() {
    let startX = null;
    let startY = null;

    window.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches[0]) {
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
      }
    }, { passive: true });

    window.addEventListener('touchend', (e) => {
      if (startX === null || startY === null) return;
      const touch = e.changedTouches && e.changedTouches[0] ? e.changedTouches[0] : null;
      if (!touch) return;

      const dx = touch.clientX - startX;
      const dy = touch.clientY - startY;

      // Yatay kaydırma tespiti
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) {
        if (dx < 0) {
          // İleri
          if (typeof window.nextSlide === 'function') {
            window.nextSlide();
          } else if (typeof window.next === 'function') {
            window.next();
          } else if (typeof window.go === 'function') {
            if (typeof window.current !== 'undefined') window.go(window.current + 1);
            else window.go(1);
          } else if (typeof window.goTo === 'function') {
            if (window.state && typeof window.state.idx !== 'undefined') window.goTo(window.state.idx + 1);
          }
        } else {
          // Geri
          if (typeof window.prevSlide === 'function') {
            window.prevSlide();
          } else if (typeof window.prev === 'function') {
            window.prev();
          } else if (typeof window.go === 'function') {
            if (typeof window.current !== 'undefined') window.go(window.current - 1);
            else window.go(-1);
          } else if (typeof window.goTo === 'function') {
            if (window.state && typeof window.state.idx !== 'undefined') window.goTo(window.state.idx - 1);
          }
        }
      }

      startX = null;
      startY = null;
    }, { passive: true });
  }

  // Başlatıcı
  document.addEventListener('DOMContentLoaded', () => {
    protectNavButtons();
    setupMobileSwipe();
    ensureHtml2Pdf();
    ensurePdfModal();
    setTimeout(window.updateGlobalLockUI, 300);
  });

})();
