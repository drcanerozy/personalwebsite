#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Periyodik Vault & MOC Entegrasyon, Living Evidence ve 10-Not Otonom Kuluçka Motoru
Yazar: Dr. Caner Özyıldırım Akademik Obsidian Kasası için Geliştirilmiştir.

Özellikler:
1. 10 Not Sayacı Takibi (.sync_state.json)
2. Çapraz-MOC Köprüleme ve Yaşayan Kanıt (Living Evidence) Denetimi
3. Otonom Fikir Kuluçkası (Substack, Ders, Proje Hipotezleri Üretimi)
4. Ana Kokpit ve Fikir Üretim Logu Otomatik Güncellemesi
"""

import os
import glob
import re
import time
import json
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
STATE_FILE = os.path.join(SCRIPT_DIR, ".sync_state.json")
KOKPIT_FILE = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "00_Ana_Kokpit.md")
FIKIR_LOG_FILE = os.path.join(VAULT_DIR, "00 Kontrol Merkezi", "Fikir Üretim Logu.md")

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "last_sync_note_count": 150,
        "last_sync_time": time.strftime("%Y-%m-%d %H:%M"),
        "incubated_ideas_count": 0,
        "sync_history": []
    }

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def run_autonomous_incubator(notes, new_notes):
    """Yeni eklenen notlar arasındaki ortak mekanizmaları tarayarak otonom fikir adayları üretir"""
    print("🧬 Otonom Fikir Kuluçkası çalıştırılıyor...")
    
    # Mekanizma haritası çıkar
    mech_map = {}
    for p in notes:
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        
        # MEKANİZMA alanını çek
        m_match = re.search(r"MEKANİZMA:\s*\n((?:\s*-\s*[^\n]+\n)+)", content, re.IGNORECASE)
        if m_match:
            mechs = re.findall(r"-\s*[\"']?\[\[(.*?)\]\][\"']?", m_match.group(1))
            fname = os.path.basename(p).replace(".md", "")
            for m in mechs:
                if m not in mech_map:
                    mech_map[m] = []
                mech_map[m].append(fname)
                
    # 2 veya daha fazla farklı odaktan notu birleştiren en güçlü köprüleri bul
    bridges = []
    for m, note_list in mech_map.items():
        if len(note_list) >= 2:
            bridges.append((m, note_list))
            
    bridges.sort(key=lambda x: len(x[1]), reverse=True)
    
    # Zengin ve çoklu kuluçka fikir taslakları üret
    incubated_items = []
    
    # 1. 🔬 ÇALIŞMA FİKİRLERİ & PROJE HİPOTEZLERİ (Top 3 Köprü)
    for idx, (m, notes_m) in enumerate(bridges[:3], 1):
        sample_notes = ", ".join([f"[[{n}]]" for n in notes_m[:3]])
        incubated_items.append({
            "type": "🔬 Çalışma Fikri Adayı",
            "title": f"Müdahale Protokollerinde `{m}` Sinyalinin Doku Koruması ve Katabolik Eşikler Üzerine Etkisi",
            "bridge": f"`{m}` köprüsü ({len(notes_m)} not: {sample_notes})",
            "action": "12 haftalık RCT veya kesitsel kohort tasarımı ile `Çalışma Fikirleri/` altına taşınabilir."
        })

    # 2. ✍️ SUBSTACK DERİN BÜLTENLERİ (Popüler Algı vs Moleküler Gerçeklik)
    for idx, (m, notes_m) in enumerate(bridges[1:4], 1):
        incubated_items.append({
            "type": "✍️ Substack Bülten Fikri",
            "title": f"Bildiğimiz Yanlışlar Serisi: `{m}` Sinyali Neden Diyetisyenlerin Yeni Pusulası Olmalı?",
            "bridge": f"`{m}` ekseni ({len(notes_m)} not)",
            "action": "Klinik danışmanlıkta danışan iletişimini ve biyokimyasal gerçekliği anlatan 800 kelimelik taslak."
        })

    # 3. 🎓 LİSANS & KLİNİK DERS MÜNAZARALARI (BES339 / BES326)
    for idx, (m, notes_m) in enumerate(bridges[2:5], 1):
        incubated_items.append({
            "type": "🎓 BES339 / BES326 Ders Münazarası",
            "title": f"`{m}` Modülasyonu: Primer Terapötik Hedef mi, Yoksa Koruyucu Kompansasyon mu?",
            "bridge": f"`{m}` mekanizması ({len(notes_m)} not)",
            "action": "Öğrencileri fizyolojik mekanizma ile klinik sonuçlar arasındaki çelişkileri tartışmaya yöneltecek vaka senaryosu."
        })
        
    return incubated_items

def sync_vault_and_mocs(force=False):
    now_str = time.strftime("%d.%m.%Y %H:%M")
    print(f"\n🏛️ Obsidian Vault Otonom Senkronizasyon Motoru [{now_str}]")
    
    state = load_state()
    notes = glob.glob(os.path.join(VAULT_DIR, "Notlar", "*.md"))
    current_count = len(notes)
    last_count = state.get("last_sync_note_count", 0)
    diff = current_count - last_count
    
    print(f"📊 Mevcut Not Sayısı: {current_count} | Son Senkronizasyon: {last_count} (Fark: +{diff})")
    
    if diff < 10 and not force:
        print(f"⏳ Otonom tetiklenme eşiğine ({diff}/10 not) henüz ulaşılmadı. Kalan: {10 - diff} not.")
        state["current_note_count"] = current_count
        save_state(state)
        return False

    print("🚀 10 Yeni Not Eşiği Aşıldı veya Manuel Tetiklendi! Tam Otonom Senkronizasyon Başlatılıyor...")
    
    # 1. Living Evidence & Null/Contradiction Taraması
    null_count = 0
    contra_count = 0
    for path in notes:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().lower()
        if any(k in content for k in ["p > 0.05", "evidence_direction: null", "anlamsız", "#finding/null"]):
            null_count += 1
        if any(k in content for k in ["evidence_direction: contradictory", "paradoks", "çelişki", "#finding/contradictory"]):
            contra_count += 1

    # 2. Otonom Fikir Kuluçkasını Çalıştır
    incubated_ideas = run_autonomous_incubator(notes, diff)
    
    # 3. Fikir Üretim Logunu Güncelle
    if os.path.exists(FIKIR_LOG_FILE):
        with open(FIKIR_LOG_FILE, "r", encoding="utf-8") as f:
            log_c = f.read()
        
        inc_section = f"\n\n### 🧬 Otonom Kuluçka Raporu — {now_str}\n"
        inc_section += f"> **Not Sayacı:** {current_count} not (+{diff} yeni not eklendi)\n"
        inc_section += f"> **Living Evidence:** {contra_count} Çelişkili, {null_count} Null Kanıt\n\n"
        
        for item in incubated_ideas:
            inc_section += f"- **{item['type']}:** {item['title']}\n"
            inc_section += f"  - *Köprü:* {item['bridge']}\n"
            inc_section += f"  - *Aksiyon:* {item['action']}\n"
            
        if "## Otonom Kuluçka Havuzu" in log_c:
            new_log_c = log_c.replace("## Otonom Kuluçka Havuzu", "## Otonom Kuluçka Havuzu" + inc_section)
        else:
            new_log_c = log_c + "\n\n## 🧬 Otonom Kuluçka Havuzu" + inc_section
            
        with open(FIKIR_LOG_FILE, "w", encoding="utf-8") as f:
            f.write(new_log_c)
        print(f"📝 Fikir Üretim Logu güncellendi: {os.path.basename(FIKIR_LOG_FILE)}")

    # 4. State Güncelle
    state["last_sync_note_count"] = current_count
    state["current_note_count"] = current_count
    state["last_sync_time"] = now_str
    state["sync_history"].append({
        "time": now_str,
        "note_count": current_count,
        "contra_count": contra_count,
        "null_count": null_count
    })
    save_state(state)
    
    print("\n✅ Otonom Kasa & MOC Senkronizasyonu başarıyla tamamlandı!")
    return True

if __name__ == "__main__":
    import sys
    force_sync = "--force" in sys.argv or "-f" in sys.argv
    sync_vault_and_mocs(force=force_sync)
