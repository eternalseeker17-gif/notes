# Economy — topic build notes (raw-extraction stage)

Status: raw extraction ONLY. No test cross-referencing, no ★-marking, no PDF build. To be resumed after the user's Economy tests are done.

## Sources and page-range map
| Source | Section | Book pages | PDF pages | Offset |
|---|---|---|---|---|
| Parmar SSC Fatman 2nd Ed. 2026 | Economics (11 chapters) | 248–294 | 269–315 | PDF = book + 21 |
| Lucent's GK 2026 | Ch.06 Indian Economy (§1–§18) | 250–305 | 262–318 | PDF = book + 12 for pp.250–272; an unnumbered ad page sits at PDF 285, so PDF = book + 13 from p.273 (book 305 = PDF 318). PDF 319 starts "Art and Culture". |

Parmar chapter-end marker is a red ■■■; Lucent Economy ends with ★★★ (p.305). Both PDFs are scans with no text layer; pages were rendered at 120 dpi and read visually.

Parmar chapters: 1 Basics (248–250), 2 Microeconomics (251–256), 3 National Income (257–260), 4 Budget and Taxation (261–265), 5 Inflation and Unemployment (266–269), 6 Banking Part-1 (270–273), 7 Monetary Policy (274–275), 8 Banking Part-2 (276–279), 9 Poverty and BoP (280–285), 10 Five Year Plan and IPR (286–291), 11 Indices, Reports, Institutions (292–294).

Lucent sections: §1 Highlights (250–252), §2 Economy and Economics (252–254), §3 Characteristics and Poverty (254–256), §4 Agriculture and Allied (256–258), §5 National Income (258–260), §6 Planning and Development (260–262), §7 Unemployment and Schemes (262–266), §8 NEP and Reforms (266–267), §9 Financial System (267–270), §10 Fiscal System (270–274), §11 Money, Banking and Insurance (274–280), §12 Tax System and GST (280–282), §13 Industry (282–285), §14 Industrial Performance (285–287), §15 Trade and Commerce (288–295), §16 Noteworthy Facts (295–296), §17 Economic and Financial Terms glossary + FAQs (296–303), §18 Miscellaneous (303–305).

## Output files (`claude/economy-raw/`)
Each = Part A (Parmar) + Part B (Lucent) + Part C (cross-book comparison).
1. basics_microeconomics — Parmar Ch.1–2; Lucent §2
2. national_income — Parmar Ch.3; Lucent §1, §5
3. budget_taxation_fiscal — Parmar Ch.4; Lucent §10, §12
4. inflation_unemployment_schemes — Parmar Ch.5; Lucent §7
5. banking_monetary_policy — Parmar Ch.6–8; Lucent §9, §11
6. poverty_bop_trade — Parmar Ch.9; Lucent §3, §15
7. planning_industry_reforms — Parmar Ch.10; Lucent §6, §8, §13, §14
8. agriculture_allied — Lucent §4 only (Parmar has no agriculture chapter)
9. indices_reports_institutions — Parmar Ch.11; Lucent §16

## KNOWN GAP — NOT YET TRANSCRIBED
Lucent §17 (glossary + FAQs, book pp.296–303, PDF 309–316) and §18 (Miscellaneous, book pp.303–305, PDF 316–318). These pages were read but deliberately NOT written up at this stage (the user asked to skip them for now and continue). They still need a verbatim transcription from the page images before the Economy build. Suggested file: `glossary_misc_raw_extraction.md`.

## Overlap check (done at start)
The project had no Static GK and no Economy raw files. Topical overlaps to cross-reference (not re-extract) later: Lucent's schemes catalogue (§7; "launched after 2016" tables in §10) with the future Static GK "Govt Policies"; Lucent's agriculture (§4) and transport (§14) content with `claude/geography-raw/agriculture_raw_extraction.md` and `transport_raw_extraction.md`.

## Method and judgment calls
- Verbatim, page by page and column by column; typos preserved; ⚠ marks doubts, contradictions and time-sensitive data.
- Lucent's numbered sections were kept as its own headings; Parmar's per-chapter files were merged with the matching Lucent sections by sub-topic.
- Unreadable scan spots were flagged with ⚠ rather than guessed: Lucent Navratna entry #3 on p.283; Parmar/Lucent p.291 top-left creased lines; a few words clipped at page edges; MSME table column merging.

## Cross-book disagreements (details in each file's Part C)
FYP targets/achievements and plan models; Green Revolution timing; People's/Gandhian Plan dates and authors; CPI and national-income base years; India's GDP rank; Maharatna/Navratna/Miniratna counts; IPR 1980 character; SIDBI year; primary deficit formula; reverse repo/MSF "always 1%" claim vs Lucent's own rate table; poverty committee lists; SCB counts (137 vs 136); GST slabs missing in Lucent.

## Caution: time-sensitive data
Most Lucent figures are dated 2023 to mid-2025 in a book presented as the 2026 edition, and Parmar has 2026-dated claims. Today is 24 Sept 2026; verify rankings, rates, counts, budget numbers and scheme details against primary sources before teaching them as current.

## Scratch folders
Rendered page images remain in the user's Downloads: `_claude_econ_pages` (and older `_claude_geo_scratch`, `_claude_modern_pages`, `_claude_pdf_pages`). Deleting them needs the user's permission.
