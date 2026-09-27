#!/usr/bin/env python3
"""Grep a list of key terms/facts against a raw-extraction source file to confirm
every fact cited in a built batch is actually backed by the raw extraction.

Usage:
  python3 factcheck.py terms.txt economy_combined_raw_extraction.md
  (terms.txt: one term/phrase per line; case-insensitive substring match)
"""
import sys
import re

def main():
    terms_file, source_file = sys.argv[1], sys.argv[2]
    terms = [l.strip() for l in open(terms_file, encoding="utf-8") if l.strip() and not l.strip().startswith("#")]
    source = open(source_file, encoding="utf-8", errors="replace").read().lower()
    missing = []
    for t in terms:
        if t.lower() not in source:
            missing.append(t)
    print(f"Checked {len(terms)} terms against {source_file}")
    if missing:
        print(f"MISSING ({len(missing)}):")
        for m in missing:
            print(" -", m)
    else:
        print("All terms found. Clean.")

if __name__ == "__main__":
    main()
