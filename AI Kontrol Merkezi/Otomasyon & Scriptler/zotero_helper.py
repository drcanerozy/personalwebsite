#!/usr/bin/env python3
"""
Zotero Local Integration Helper
Allows instant searching, collection listing, and PDF text extraction
directly from local Zotero storage without manual setup.
"""
import os
import shutil
import sqlite3
from typing import List, Dict, Any, Optional

ZOTERO_DIR = os.path.expanduser("~/Zotero")
SCRATCH_DIR = os.path.expanduser("~/.gemini/antigravity/brain/shared_zotero_cache")

def get_db_connection() -> sqlite3.Connection:
    os.makedirs(SCRATCH_DIR, exist_ok=True)
    for fname in ["zotero.sqlite", "zotero.sqlite-wal", "zotero.sqlite-shm"]:
        src = os.path.join(ZOTERO_DIR, fname)
        dst = os.path.join(SCRATCH_DIR, fname)
        if os.path.exists(src):
            shutil.copy2(src, dst)
    db_path = os.path.join(SCRATCH_DIR, "zotero.sqlite")
    return sqlite3.connect(db_path)

def list_collections() -> List[Dict[str, Any]]:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT collectionID, collectionName, parentCollectionID, key FROM collections ORDER BY collectionName")
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "parent_id": r[2], "key": r[3]} for r in rows]

def search_items(query: str = "", collection_name: Optional[str] = None, limit: int = 20) -> List[Dict[str, Any]]:
    conn = get_db_connection()
    c = conn.cursor()
    
    col_id = None
    if collection_name:
        c.execute("SELECT collectionID FROM collections WHERE collectionName LIKE ?", (f"%{collection_name}%",))
        res = c.fetchone()
        if res:
            col_id = res[0]
            
    sql = """
    SELECT DISTINCT i.itemID, i.key, idv.value as title
    FROM items i
    JOIN itemData id ON i.itemID = id.itemID
    JOIN itemDataValues idv ON id.valueID = idv.valueID
    JOIN fields f ON id.fieldID = f.fieldID
    """
    params = []
    
    where_clauses = ["f.fieldName = 'title'"]
    if query:
        where_clauses.append("idv.value LIKE ?")
        params.append(f"%{query}%")
        
    if col_id:
        sql += " JOIN collectionItems ci ON i.itemID = ci.itemID"
        where_clauses.append("ci.collectionID = ?")
        params.append(col_id)
        
    sql += " WHERE " + " AND ".join(where_clauses) + f" LIMIT {limit}"
    
    c.execute(sql, params)
    items = c.fetchall()
    
    results = []
    for item_id, item_key, title in items:
        c.execute("""
            SELECT ia.itemID, ia.path, ia.contentType, i_att.key 
            FROM itemAttachments ia 
            JOIN items i_att ON ia.itemID = i_att.itemID 
            WHERE ia.parentItemID = ?
        """, (item_id,))
        attachments = c.fetchall()
        pdf_paths = []
        for att in attachments:
            _, path, _, att_key = att
            if path:
                if path.startswith("storage:"):
                    rel = path.replace("storage:", "")
                    full = os.path.join(ZOTERO_DIR, "storage", att_key, rel)
                else:
                    full = path
                if os.path.exists(full):
                    pdf_paths.append(full)
                else:
                    dir_path = os.path.join(ZOTERO_DIR, "storage", att_key)
                    if os.path.exists(dir_path):
                        for f in os.listdir(dir_path):
                            if f.lower().endswith(".pdf"):
                                pdf_paths.append(os.path.join(dir_path, f))
        results.append({
            "id": item_id,
            "key": item_key,
            "title": title,
            "pdf_paths": pdf_paths
        })
    conn.close()
    return results

if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = search_items(q)
    for r in res:
        print(f"[{r['id']}] {r['title']} -> PDFs: {r['pdf_paths']}")
