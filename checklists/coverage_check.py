#!/usr/bin/env python3
"""Coverage check: for each checklist line, extract candidate keywords/numbers
and verify at least a reasonable subset appear in the target HTML's text content.
This is a blunt recall aid, not proof of correctness -- flagged items still need
manual eyeballing."""
import sys, re, html

def load_checklist(path):
    items = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line.startswith("- [ ]"):
            items.append(line[5:].strip())
    return items

def text_of(html_path):
    raw = open(html_path, encoding="utf-8").read()
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    return re.sub(r"\s+", " ", raw).lower()

def keywords(item):
    # strip trailing [A]/[B] tag and bracketed asides for keyword extraction
    core = re.sub(r"\[[AB][^\]]*\]", "", item)
    core = re.sub(r"\[B:.*?\]", "", core)
    # pull out quoted/bold-ish tokens: numbers, capitalized multi-word terms, %
    nums = re.findall(r"\d+[\d.,%]*", core)
    words = re.findall(r"[A-Za-z][A-Za-z\-]{3,}", core)
    # drop common stopwords
    stop = {"with","that","this","from","into","also","then","when","eg","the","and","for","are","was","were","its","each","over","under","than","not","per","based","upon","such","like","have","has","been","def","formula","table","example","examples"}
    words = [w for w in words if w.lower() not in stop]
    return nums, words

def check(checklist_path, html_path):
    items = load_checklist(checklist_path)
    text = text_of(html_path)
    misses = []
    for item in items:
        nums, words = keywords(item)
        # require: at least half of unique significant words present, AND all numbers present
        uniq_words = list(dict.fromkeys(w.lower() for w in words))
        found_words = sum(1 for w in uniq_words if w in text)
        word_ratio = found_words / max(1, len(uniq_words))
        missing_nums = [n for n in nums if n not in text]
        if word_ratio < 0.5 or missing_nums:
            misses.append((item, word_ratio, missing_nums))
    print(f"Checklist items: {len(items)}")
    print(f"Flagged as possibly missing: {len(misses)}\n")
    for item, ratio, mnums in misses:
        print(f"- ratio={ratio:.2f} missing_nums={mnums}\n  {item}\n")

if __name__ == "__main__":
    check(sys.argv[1], sys.argv[2])
