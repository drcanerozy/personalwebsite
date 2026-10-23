#!/usr/bin/env python3
"""
Internal Link Checker for canerozy.com
Scans all published HTML files and verifies that all relative and internal links resolve correctly.
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote

BASE_DIR = Path(__file__).parent.parent.resolve()

def check_all_links():
    html_files = []
    
    # Target published HTML files
    root_htmls = [BASE_DIR / "index.html", BASE_DIR / "404.html"]
    for rh in root_htmls:
        if rh.exists():
            html_files.append(rh)
            
    # Published sections
    if (BASE_DIR / "en").exists():
        html_files.extend((BASE_DIR / "en").rglob("*.html"))
    if (BASE_DIR / "yazilar").exists():
        html_files.extend((BASE_DIR / "yazilar").glob("*.html"))
    if (BASE_DIR / "dersler").exists():
        html_files.extend((BASE_DIR / "dersler").glob("*.html")) # only flat generated course pages
    if (BASE_DIR / "slides").exists():
        html_files.extend((BASE_DIR / "slides").glob("*.html")) # only flat slides
            
    broken_links = []
    total_links_checked = 0

    for file_path in sorted(html_files):
        # Skip raw obsidian / unbuilt folders if any
        if any(ignored in file_path.parts for ignored in [".git", "node_modules", "ders materyalleri"]):
            continue
            
        rel_src = file_path.relative_to(BASE_DIR)
        file_dir = file_path.parent
        
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception as e:
            broken_links.append((str(rel_src), "FILE_READ_ERROR", str(e)))
            continue

        # Extract href and src attributes
        links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
        
        for link in links:
            link = link.strip()
            if not link:
                continue
            if link.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                continue
            if "${" in link or "{{" in link: # skip template variables
                continue
                
            total_links_checked += 1
            parsed = urlparse(link)
            
            # Handle absolute URLs with our domain
            if parsed.scheme in ("http", "https"):
                if "canerozy.com" in parsed.netloc:
                    path = parsed.path.lstrip("/")
                    if not path:
                        target = BASE_DIR / "index.html"
                    elif path.endswith("/"):
                        target = BASE_DIR / path / "index.html"
                    else:
                        target = BASE_DIR / path
                    if not target.exists() and not (target.parent / f"{target.name}.html").exists():
                        broken_links.append((str(rel_src), link, f"Missing file: {target}"))
                continue
            elif parsed.scheme:
                # External link (http, https to external domain)
                continue
                
            # Relative or root-relative link
            clean_path = parsed.path
            if clean_path.startswith("/"):
                target = (BASE_DIR / clean_path.lstrip("/")).resolve()
            else:
                target = (file_dir / clean_path).resolve()
                
            # If path ends with slash, look for index.html
            if clean_path.endswith("/") or target.is_dir():
                idx_target = target / "index.html"
                if not idx_target.exists():
                    broken_links.append((str(rel_src), link, f"Missing directory index: {idx_target}"))
            elif not target.exists():
                # Try with .html extension
                html_target = target.parent / f"{target.name}.html"
                if not html_target.exists():
                    broken_links.append((str(rel_src), link, f"Target not found: {target}"))

    print(f"🔍 Checked {len(html_files)} HTML files ({total_links_checked} internal links checked).")
    if broken_links:
        print(f"❌ Found {len(broken_links)} broken internal link(s):")
        for src, link, reason in broken_links:
            print(f"  • In {src} -> '{link}' ({reason})")
        return False
    else:
        print("✅ All internal links resolved successfully! Zero 404 errors.")
        return True

if __name__ == "__main__":
    success = check_all_links()
    sys.exit(0 if success else 1)
