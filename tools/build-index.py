#!/usr/bin/env python3
"""
Topic Index Builder
Scans markdown memory files and generates a keyword → location index.

Usage:
    python build-index.py [memory_directory] [output_file]
    
Defaults:
    memory_directory = memory/
    output_file = memory/topic-index.md

Customize the keyword patterns for your domain by editing the
DOMAIN_TERMS list below.
"""

import os
import re
import sys
from collections import defaultdict

# === CONFIGURATION ===

# Directory containing your memory files
MEMORY_DIR = sys.argv[1] if len(sys.argv) > 1 else "memory"

# Output file for the index
OUTPUT_FILE = sys.argv[2] if len(sys.argv) > 2 else os.path.join(MEMORY_DIR, "topic-index.md")

# Additional top-level files to index (relative to workspace root)
EXTRA_FILES = ["MEMORY.md"]

# Maximum locations to store per keyword (keeps index readable)
MAX_LOCATIONS = 5

# Minimum keyword length
MIN_KEYWORD_LENGTH = 3

# Common words to skip (add your own noise words here)
SKIP_WORDS = {
    'the', 'this', 'that', 'these', 'those', 'when', 'what', 'where',
    'how', 'why', 'from', 'with', 'into', 'also', 'about', 'been',
    'have', 'has', 'had', 'was', 'were', 'are', 'but', 'and', 'for',
    'not', 'all', 'can', 'will', 'new', 'key', 'see', 'may', 'got',
    'did', 'let', 'now', 'our', 'one', 'two', 'three', 'first', 'last',
    'next', 'each', 'every', 'some', 'most', 'both', 'done', 'sent',
    'read', 'made', 'same', 'still', 'just', 'added', 'updated',
    'fixed', 'checked', 'wrote', 'built', 'here', 'there', 'then',
    'than', 'very', 'only', 'more', 'much', 'such', 'like', 'over',
    'also', 'back', 'after', 'before', 'between', 'through', 'during',
    'under', 'above', 'below', 'should', 'would', 'could', 'might',
    'need', 'want', 'know', 'think', 'said', 'says', 'told', 'asked',
    'used', 'using', 'work', 'working', 'looks', 'looking', 'keep',
    'take', 'make', 'give', 'find', 'show', 'tried', 'trying',
    'session', 'today', 'yesterday', 'tomorrow', 'morning', 'night',
    'photo', 'photos', 'file', 'files', 'note', 'notes',
}

# Domain-specific terms to always capture (case-insensitive regex)
# CUSTOMIZE THIS for your agent's domain.
# Example below is for a mineral collection agent.
# Replace with terms relevant to your work.
DOMAIN_TERMS = r"""
    # Add your domain terms here, one per line, separated by |
    # These are matched case-insensitively
    # Example (geology):
    # calcite|quartz|fluorite|hematite|
    # Example (music):
    # chord|melody|tempo|rhythm|
    # Example (code):
    # refactor|deploy|merge|pipeline|
"""

# Clean up the domain terms into a usable pattern
domain_list = [t.strip() for t in DOMAIN_TERMS.replace('\n', '|').split('|') 
               if t.strip() and not t.strip().startswith('#')]
DOMAIN_PATTERN = re.compile(r'\b(' + '|'.join(domain_list) + r')\b', re.IGNORECASE) if domain_list else None


# === INDEX BUILDER ===

index = defaultdict(set)  # keyword → set of locations

def extract_keywords(text, filepath, section=""):
    """Extract meaningful keywords from a line of text and map to location."""
    loc = filepath
    if section:
        loc += f" § {section}"
    
    # Capitalized words (proper nouns, names, places)
    words = text.split()
    for word in words:
        clean = re.sub(r'[.,;:!?()\[\]"\'—–\-*/`#>]', '', word)
        if (len(clean) >= MIN_KEYWORD_LENGTH and 
            clean[0].isupper() and 
            not clean.isupper() and
            clean.lower() not in SKIP_WORDS):
            index[clean].add(loc)
    
    # Domain-specific terms
    if DOMAIN_PATTERN:
        for match in DOMAIN_PATTERN.findall(text):
            index[match.lower()].add(loc)
    
    # Identifiers (patterns like TN123, #456, ID-789, etc.)
    for identifier in re.findall(r'\b[A-Z]{1,4}\d{2,6}\b', text):
        index[identifier].add(loc)


def scan_file(filepath):
    """Scan a markdown file and extract keywords by section."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (IOError, UnicodeDecodeError):
        return
    
    current_section = ""
    for line in content.split('\n'):
        # Track section headers
        if line.startswith('## '):
            current_section = line[3:].strip()[:60]
        elif line.startswith('### '):
            current_section = line[4:].strip()[:60]
        
        extract_keywords(line, filepath, current_section)


def build_index():
    """Scan all memory files and build the topic index."""
    # Scan memory directory
    if os.path.isdir(MEMORY_DIR):
        for root, dirs, files in os.walk(MEMORY_DIR):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for fname in sorted(files):
                if fname.endswith('.md') and fname != 'topic-index.md':
                    scan_file(os.path.join(root, fname))
    
    # Scan extra files
    for filepath in EXTRA_FILES:
        if os.path.isfile(filepath):
            scan_file(filepath)


def write_index():
    """Write the topic index to a markdown file."""
    os.makedirs(os.path.dirname(OUTPUT_FILE) or '.', exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Topic Index\n")
        f.write(f"# Auto-generated by build-index.py\n")
        f.write(f"# {len(index)} keywords indexed\n")
        f.write(f"# Rebuild: python tools/build-index.py\n\n")
        
        sorted_keys = sorted(index.keys(), key=lambda k: k.lower())
        current_letter = ""
        
        for key in sorted_keys:
            letter = key[0].upper()
            if letter != current_letter:
                current_letter = letter
                f.write(f"\n## {letter}\n")
            
            locs = sorted(index[key])[:MAX_LOCATIONS]
            loc_str = " | ".join(locs)
            f.write(f"- **{key}**: {loc_str}\n")


if __name__ == "__main__":
    print(f"Scanning {MEMORY_DIR}/ ...")
    build_index()
    write_index()
    
    # Stats
    identifier_count = len([k for k in index if re.match(r'^[A-Z]{1,4}\d+$', k)])
    print(f"Done: {len(index)} keywords, {identifier_count} identifiers")
    print(f"Index written to {OUTPUT_FILE}")
    
    # Show sample entries
    if index:
        samples = sorted(index.keys(), key=lambda k: len(index[k]), reverse=True)[:5]
        print(f"\nMost-referenced keywords:")
        for s in samples:
            print(f"  {s}: {len(index[s])} locations")
