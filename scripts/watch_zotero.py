#!/usr/bin/env python3
"""
Zotero Auto-Sync Watcher Daemon
Monitors ~/Zotero/zotero.sqlite for changes and triggers incremental sync
Preserves all user ratings in Obsidian.
"""

import os
import time
import subprocess
import sys

ZOTERO_DB = os.path.expanduser("~/Zotero/zotero.sqlite")
SYNC_SCRIPT = "/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner/scripts/build_full_zotero_library.py"

def get_db_mtime():
    try:
        return os.path.getmtime(ZOTERO_DB)
    except Exception:
        return 0

def main():
    print(f"Zotero Watcher started. Monitoring: {ZOTERO_DB}")
    last_mtime = get_db_mtime()
    
    while True:
        try:
            time.sleep(5)
            current_mtime = get_db_mtime()
            if current_mtime > last_mtime:
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Zotero database change detected! Syncing...")
                # Wait 1 second for Zotero to finish writing
                time.sleep(1)
                subprocess.run(["python3", SYNC_SCRIPT], check=False)
                last_mtime = get_db_mtime()
                print("Sync completed successfully.")
        except KeyboardInterrupt:
            print("Watcher stopped.")
            break
        except Exception as e:
            print(f"Watcher loop error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
