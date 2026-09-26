#!/usr/bin/env python3
"""Render a revision-notes HTML file to PDF via headless Chromium (Playwright),
then scan the rendered DOM for elements that overflow the A4 page box (clipcheck).

Usage:
  python3 render.py economy1.html                 # render to economy1.pdf + clipcheck
  python3 render.py economy1.html --no-clipcheck   # render only
  python3 render.py --combine out.pdf a.html b.html ...  # concat pages of multiple sources into one PDF
"""
import sys
import os
import glob
import subprocess

CHROME = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
CHROME = CHROME[0] if CHROME else None

from playwright.sync_api import sync_playwright

PAGE_W_MM = 210
PAGE_H_MM = 297
MARGIN_MM = 11  # matches @page margin in style.css (top/bottom slightly larger, ignored for overflow check)


def render_pdf(html_path, pdf_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME)
        page = browser.new_page()
        page.goto("file://" + os.path.abspath(html_path))
        page.pdf(path=pdf_path, format="A4",
                 margin={"top": "11mm", "bottom": "13mm", "left": "11mm", "right": "11mm"},
                 print_background=True)
        browser.close()
    print(f"Rendered {pdf_path}")


def clipcheck(html_path):
    """Flag DOM elements whose right edge exceeds the printable content width,
    or whose own scrollWidth > clientWidth (text/table overflow)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME)
        page = browser.new_page(viewport={"width": 794, "height": 1123})  # A4 @ 96dpi
        page.goto("file://" + os.path.abspath(html_path))
        problems = page.evaluate("""
        () => {
          const results = [];
          const contentWidth = document.body.clientWidth;
          document.querySelectorAll('body *').forEach(el => {
            const style = getComputedStyle(el);
            if (style.display === 'none') return;
            const rect = el.getBoundingClientRect();
            if (rect.width === 0 && rect.height === 0) return;
            // horizontal overflow: element wider than its own scrollable box
            if (el.scrollWidth - el.clientWidth > 2 && el.clientWidth > 0) {
              results.push({
                tag: el.tagName, cls: el.className || '',
                text: (el.textContent || '').trim().slice(0, 80),
                scrollWidth: el.scrollWidth, clientWidth: el.clientWidth
              });
            }
            // element right edge beyond page content box
            if (rect.right > contentWidth + 2) {
              results.push({
                tag: el.tagName, cls: el.className || '',
                text: (el.textContent || '').trim().slice(0, 80),
                right: rect.right, contentWidth: contentWidth
              });
            }
          });
          return results;
        }
        """)
        browser.close()
    if problems:
        print(f"CLIPCHECK: {len(problems)} problem(s) in {html_path}")
        for pr in problems[:50]:
            print(" ", pr)
    else:
        print(f"CLIPCHECK: clean, 0 problems in {html_path}")
    return problems


def combine(out_pdf, html_files):
    """Render each HTML to a temp PDF, then merge with pikepdf/pypdf if available, else qpdf."""
    tmp_pdfs = []
    for hf in html_files:
        tmp = hf.rsplit(".", 1)[0] + "_tmp_combine.pdf"
        render_pdf(hf, tmp)
        tmp_pdfs.append(tmp)
    try:
        from pypdf import PdfWriter
        writer = PdfWriter()
        for tp in tmp_pdfs:
            writer.append(tp)
        with open(out_pdf, "wb") as f:
            writer.write(f)
    except ImportError:
        subprocess.run(["pdfunite"] + tmp_pdfs + [out_pdf], check=True)
    for tp in tmp_pdfs:
        os.remove(tp)
    print(f"Combined {len(html_files)} files -> {out_pdf}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    if args[0] == "--combine":
        out = args[1]
        combine(out, args[2:])
        sys.exit(0)
    html = args[0]
    do_clip = "--no-clipcheck" not in args
    pdf = html.rsplit(".", 1)[0] + ".pdf"
    render_pdf(html, pdf)
    if do_clip:
        clipcheck(html)
