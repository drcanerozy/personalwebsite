import os
import glob
import re
import math
from collections import Counter

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
WORK_IDEAS_DIR = os.path.join(BASE_DIR, "Çalışma Fikirleri")
NOTLAR_DIR = os.path.join(BASE_DIR, "Notlar")

# SIMILARITY THRESHOLD (increased for "katı" constraint)
THRESHOLD = 0.25 

def get_tokens(text):
    # Lowercase and split into words
    words = re.findall(r'\w+', text.lower())
    # Filter very short words
    return [w for w in words if len(w) > 2]

def cosine_similarity_simple(tokens1, tokens2):
    if not tokens1 or not tokens2: return 0.0
    vec1 = Counter(tokens1)
    vec2 = Counter(tokens2)
    
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator: return 0.0
    return float(numerator) / denominator

def extract_clean_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove YAML
    clean = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    # Remove suggested links section
    clean = re.sub(r'\n## (Bağlantılı Notlar|Önerilen Bağlantılar).*', '', clean, flags=re.DOTALL)
    # Remove wiki links brackets
    clean = re.sub(r'\[\[(.*?)\]\]', r'\1', clean)
    return content, clean

def main():
    print("Loading notes...")
    work_idea_paths = glob.glob(os.path.join(WORK_IDEAS_DIR, "*.md"))
    notlar_paths = glob.glob(os.path.join(NOTLAR_DIR, "**", "*.md"), recursive=True)
    
    all_notes = [] # list of {'path', 'title', 'tokens', 'original'}
    
    for p in work_idea_paths + notlar_paths:
        title = os.path.splitext(os.path.basename(p))[0]
        original, clean = extract_clean_content(p)
        tokens = get_tokens(title + " " + clean) # Include title in tokens
        if len(tokens) < 5: continue
        all_notes.append({
            'path': p,
            'title': title,
            'tokens': tokens,
            'original': original,
            'is_work_idea': p.startswith(WORK_IDEAS_DIR)
        })

    print(f"Comparing {len(all_notes)} notes...")
    
    for i, note in enumerate(all_notes):
        if not note['is_work_idea']: continue
        
        suggestions = []
        for j, other in enumerate(all_notes):
            if i == j: continue
            
            score = cosine_similarity_simple(note['tokens'], other['tokens'])
            if score > THRESHOLD:
                suggestions.append((other['title'], score))
        
        # Sort and take top 5
        suggestions.sort(key=lambda x: x[1], reverse=True)
        top_suggestions = [f"- [[{s[0]}]]" for s in suggestions[:5]]
        
        if top_suggestions:
            # Reload to get current content (after metadata update)
            with open(note['path'], 'r', encoding='utf-8') as f:
                current_content = f.read()
            
            section_header = "\n\n## Bağlantılı Notlar\n"
            
            if "## Bağlantılı Notlar" in current_content:
                # Extract existing links
                parts = re.split(r'\n## Bağlantılı Notlar\n', current_content)
                header_content = parts[0]
                remaining = parts[1]
                
                # Split next section
                next_section_match = re.search(r'\n#+ ', remaining)
                if next_section_match:
                    section_content = remaining[:next_section_match.start()]
                    footer_content = remaining[next_section_match.start():]
                else:
                    section_content = remaining
                    footer_content = ""
                
                existing_links = re.findall(r'- \[\[.*?\]\]', section_content)
                # Filter out ones we are suggesting (avoid duplicates)
                unique_new = [s for s in top_suggestions if s not in existing_links]
                
                new_section = section_header + "\n".join(existing_links + unique_new) + "\n"
                final_content = header_content + new_section + footer_content
            else:
                final_content = current_content.rstrip() + section_header + "\n".join(top_suggestions) + "\n"
            
            with open(note['path'], 'w', encoding='utf-8') as f:
                f.write(final_content)

    print("Done linking.")

if __name__ == "__main__":
    main()
