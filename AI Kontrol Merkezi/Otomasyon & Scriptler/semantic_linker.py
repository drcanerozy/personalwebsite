import os
import glob
import re
import math
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
NOTLAR_DIR = os.path.join(BASE_DIR, "Notlar")
DIZIN_DIR = os.path.join(BASE_DIR, "Dizin")
DERSLER_DIR = os.path.join(BASE_DIR, "Dersler")

def get_markdown_files(directory):
    return glob.glob(os.path.join(directory, "**", "*.md"), recursive=True)

def extract_content(filepath):
    """ Reads the file and removes existing wiki links """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip out existing [[...]] to not bias the TF-IDF
    clean_content = re.sub(r'\[\[(.*?)\]\]', r'\1', content)
    # Strip out the "## Önerilen Bağlantılar" section if it exists
    clean_content = re.sub(r'## Önerilen Bağlantılar.*', '', clean_content, flags=re.DOTALL)
    
    return content, clean_content

def extract_title(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def main(dry_run=True):
    print("Gathering files...")
    notlar_files = get_markdown_files(NOTLAR_DIR)
    dizin_files = get_markdown_files(DIZIN_DIR)
    dersler_files = get_markdown_files(DERSLER_DIR)
    
    # All files that can be linked to
    all_target_titles = []
    filepath_map = {} # title -> filepath
    
    for f in notlar_files + dizin_files + dersler_files:
        title = extract_title(f)
        all_target_titles.append(title)
        filepath_map[title] = f
        
    print(f"Total potential link targets: {len(all_target_titles)}")
    print(f"Reading {len(notlar_files)} Notlar files for semantic matching...")
    
    # 1. Read Contents
    notlar_data = [] # list of dicts: {'filepath':, 'title':, 'original':, 'clean':}
    corpus = []      # strictly the clean text for TF-IDF
    titles = []      # corresponding titles
    
    for f in notlar_files:
        title = extract_title(f)
        original, clean = extract_content(f)
        if len(clean.strip()) < 10:
             continue # Skip empty/very short notes
             
        notlar_data.append({
            'filepath': f,
            'title': title,
            'original': original,
            'clean': clean
        })
        corpus.append(clean)
        titles.append(title)
        
    print(f"Valid notes for TF-IDF: {len(corpus)}")
    
    # 2. Compute TF-IDF and Cosine Similarity
    # Expand turkish stop words to reduce noise from common verbs and connectors
    turkish_stops = [
        "ve", "ile", "veya", "için", "bir", "bu", "da", "de", "ise", "olarak", 
        "gibi", "daha", "en", "çok", "kadar", "kendi", "olan", "olanlar", "olup",
        "olduğunu", "olduğu", "göre", "tarafından", "ile", "sonra", "önce", "diğer",
        "ancak", "çünkü", "veya", "ya", "da", "hem", "sadece", "dolayı", "nedeniyle",
        "neden", "sonuç", "arasında", "arasındaki", "halde", "ise", "karşı", "rağmen"
    ]
    
    # Increase min_df to ensure word appears in at least 3 documents to be a "concept"
    # Decrease max_df to 0.60 to ignore words that appear in >60% of all documents (likely generic)
    vectorizer = TfidfVectorizer(stop_words=turkish_stops, min_df=3, max_df=0.60)
    
    try:
        tfidf_matrix = vectorizer.fit_transform(corpus)
    except ValueError as e:
        print("Error in fitting TF-IDF (maybe corpus is too small/empty):", e)
        return
        
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    # 3. Analyze and Output
    print("\n--- DRY RUN RESULTS: STRICTER SEMANTIC MATCHES ---")
    
    for idx, data in enumerate(notlar_data):
        title = data['title']
        scores = similarity_matrix[idx]
        
        # Get top matches (excluding self)
        related_indices = scores.argsort()[::-1]
        
        suggested_links = []
        for i in related_indices:
            # INCREASED THRESHOLD: from 0.15 to 0.25 for a stricter thematic overlap
            if i != idx and scores[i] > 0.25: 
                suggested_links.append((titles[i], scores[i]))
            if len(suggested_links) >= 4: # reduce suggestions to max 4 very strong ones
                break
                
        # Also let's try to find if any Dizin or Dersler title is mentioned in the clean content directly.
        # This is for "in-text" Wiki linking for empty Dizin files.
        direct_mentions = []
        content_lower = data['clean'].lower()
        for t in all_target_titles:
            if t != title and t.lower() in content_lower:
                direct_mentions.append(t)
                
        if dry_run:
            if idx < 5:
                print(f"\n📝 Note: {title}")
                print("  Semantic Connections (Concept Depth):")
                for link, score in suggested_links:
                    print(f"    -> [[{link}]] (Score: {score:.2f})")
                if direct_mentions:
                    print(f"  Direct Title Mentions (Potential Inline Links):")
                    for dm in list(set(direct_mentions))[:3]:
                        print(f"    -> [[{dm}]]")
        else:
            # APPLY MODE
            modified_content = data['original']
            
            # 1. Strip existing "Önerilen Bağlantılar" safely if we ran it before
            modified_content = re.sub(r'\n## Önerilen Bağlantılar.*', '', modified_content, flags=re.DOTALL)
            
            # 2. Add Inline Links strictly for Titles
            # We must be careful not to replace text inside existing links [[...]] or headers
            # A simple approach: for every direct mention, replace word with [[word]]
            # This is complex in regex but let's do a basic replacement for exact matches in text (not inside brackets)
            # To avoid messing up markdown, we only replace independent words
            for dm in set(direct_mentions):
                # Pattern: word boundaries, not preceded by [ or followed by ]
                pattern = re.compile(rf'(?<!\[)\b({re.escape(dm)})\b(?!\])', re.IGNORECASE)
                # Only replace the first occurrence to avoid spamming the text
                modified_content = pattern.sub(rf'[[\1]]', modified_content, count=1)
                
            # 3. Append Semantic Links
            if suggested_links:
                modified_content += "\n\n## Önerilen Bağlantılar\n"
                for link, _ in suggested_links:
                    modified_content += f"- [[{link}]]\n"
                    
            # 4. Write back to file
            with open(data['filepath'], 'w', encoding='utf-8') as f:
                f.write(modified_content)
                
    if dry_run:
        print("\n... and so on for the rest of the files.")
        print("If this looks good, we can apply the script to write the links back to the files.")
    else:
        print("\n✅ APPLY COMPLETE: Successfully injected semantic Wiki-links and inline link titles into 96 Notes.")

if __name__ == "__main__":
    # If run with --apply, we write to files
    is_dryrun = "--apply" not in sys.argv
    main(dry_run=is_dryrun)
