import os
import re
from datetime import datetime

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
WORK_IDEAS_DIR = os.path.join(BASE_DIR, "Çalışma Fikirleri")
DIZIN_DIR = os.path.join(BASE_DIR, "Dizin")

def get_subjects():
    subjects = []
    if not os.path.exists(DIZIN_DIR):
        return []
    for f in os.listdir(DIZIN_DIR):
        if f.endswith(".md"):
            name = f.replace("_MOC.md", "").replace(".md", "")
            name = re.sub(r'^\d+_', '', name)
            subjects.append(name.strip())
    return sorted(list(set(subjects)))

def parse_yaml(content):
    yaml_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    match = yaml_pattern.match(content)
    if not match:
        return {}, content
    
    yaml_text = match.group(1)
    main_content = content[match.end():]
    
    data = {}
    for line in yaml_text.splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            # Basic parsing for lists and strings
            if val.startswith('[') and val.endswith(']'):
                items = [i.strip().strip('"').strip("'") for i in val[1:-1].split(',') if i.strip()]
                data[key] = items
            else:
                data[key] = val.strip('"').strip("'")
    return data, main_content

def dump_yaml(data):
    lines = ["---"]
    for k, v in data.items():
        if isinstance(v, list):
            items_str = ", ".join([f'"{i}"' for i in v])
            lines.append(f"{k}: [{items_str}]")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)

def process_note(filepath, subjects):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    meta_data, main_content = parse_yaml(content)
    
    # Initialize properties
    meta = {
        "Konu": meta_data.get("Konu", []),
        "Tür": meta_data.get("Tür", []),
        "Durum": meta_data.get("Durum", "fikir"),
        "Öncelik": meta_data.get("Öncelik", "Normal"),
        "Oluşturulma_Tarihi": meta_data.get("Oluşturulma_Tarihi", datetime.now().strftime("%Y-%m-%d")),
        "Modifiye_Edilme_Tarihi": datetime.now().strftime("%Y-%m-%d")
    }

    # Ensure lists
    if isinstance(meta["Konu"], str): meta["Konu"] = [meta["Konu"]] if meta["Konu"] else []
    if isinstance(meta["Tür"], str): meta["Tür"] = [meta["Tür"]] if meta["Tür"] else []

    # Auto-detection
    search_text = (os.path.basename(filepath) + " " + main_content).lower()
    for subject in subjects:
        if subject.lower() in search_text:
            if subject not in meta["Konu"]:
                meta["Konu"].append(subject)

    new_content = dump_yaml(meta) + "\n\n" + main_content.lstrip()
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    subjects = get_subjects()
    print(f"Extracted {len(subjects)} subjects.")
    
    if not os.path.exists(WORK_IDEAS_DIR):
        print("Work ideas directory not found.")
        return

    notes = [f for f in os.listdir(WORK_IDEAS_DIR) if f.endswith(".md")]
    for note in notes:
        process_note(os.path.join(WORK_IDEAS_DIR, note), subjects)
    print(f"Processed {len(notes)} notes.")

if __name__ == "__main__":
    main()
