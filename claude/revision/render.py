#!/usr/bin/env python3
import sys
from playwright.sync_api import sync_playwright

def render(html_path, pdf_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        page = browser.new_page()
        page.goto(f"file://{html_path}")
        page.pdf(path=pdf_path, format="A4", print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
        browser.close()

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
