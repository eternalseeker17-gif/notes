# Static GK — Build Notes (raw-extraction stage)

**Status (2026-09-24): RAW EXTRACTION COMPLETE for all Round 1 + Round 2 sub-topics (13 files under `claude/static-gk-raw/`). No test cross-referencing done (per instruction). Stopped here; user returns after the relevant Static GK tests.**

## 0. Scope and instruction recap
- Task: raw-extraction only for Static GK (59 tests total; largest subject). Sources: **Lucent's GK (2026)** + **Parmar SSC Fatman 2nd Ed. (2026)**. Both PDFs were found in the user's Downloads folder — Drive link not used.
- Round 1: Dances, Festivals, Music, Books & Authors, Sports (37 tests). Round 2: Architecture, Days & Events, Awards, Famous People/Places, Govt Policies, Sci-Tech (22 tests).
- Method follows the Ancient-History build notes (`claude/ancient-history-topic-build-notes.md`): dense list/table content kept, cross-book disagreements flagged, no silent trimming.

## 1. Method and disclosure (read this)
- **"Fact-complete", not word-for-word.** Every list entry, table row, name, number, date and mnemonic mapping was kept; explanatory prose was condensed. Where the book prints a slip, it is kept as printed with [sic]/bracketed correction and marked ⚠.
- Both books are **scanned PDFs with no text layer**. Every page was read from a page image (1400px JPEG); tesseract OCR was used only as a cross-check/locator, never as the source. Two small low-quality tables (Parmar Census religion tables) were re-rendered at 260 dpi and read separately.
- **Verification status (honest):** transcription was checked against the page image while writing each part. A separate full second-pass re-read of every raw file against every source page was **not** run for all 13 files; only spot checks (e.g. Parmar Awards p.505 vs. the awards file, Nobel/Grammy/Booker tables) plus stale-pointer/leftover greps. Treat the files as first-pass ground truth, and the ⚠ items and Part-C/Z "doubts" lists as the things to verify.
- ⚠ = printing slip / cross-book disagreement / doubt / recent-event item (2024–2026). Recent-event items (Secretary-General, WTO/ISA heads, G20 presidency, BRICS members, awardee lists for 2024–2025, Census status, Operation Sindoor, Paris 2024 etc.) are as printed in the 2026 editions and may be outdated at exam time — check current sources.
- Where I noted something from general knowledge that the book does not print, it is labelled as unverified in the file (I have no verified source for it).

## 2. Page-range map
- **Parmar:** PDF page = book page + 33. Static GK = book pp.429–509 (PDF 462–542). Chapters (from its printed Index): Music & Paintings 429–439 · Classical Dance 440–443 · Folk Dances 444–458 · Festivals 459–473 · Census 474–476 · Important Days 477–479 · Books & Authors 480–487 · Sports 488–497 · International Organisations 498–502 · National Organisations 503–504 · Awards & Honours 505–509.
- **Lucent:** PDF page = book page + 13. Ch.7 Art & Culture (Architecture, Sculpture, Painting, Festivals & Fairs) = book pp.306–329 (Static GK part read from PDF 319–342). Ch.11 Miscellany = book pp.430–487 (PDF 443–500), §1–§73. Ch.12 Computer = book pp.488–498 (PDF 501–511; PDF 512 blank).

## 3. Sub-topic → files (all in `claude/static-gk-raw/`)

| Sub-topic | File | Main sources |
|---|---|---|
| Dances | `dances_raw_extraction.md` | Parmar Classical + Folk Dances; Lucent §31–32 |
| Music | `music_raw_extraction.md` | Parmar Music & Paintings (incl. paintings of states); Lucent §30 |
| Festivals | `festivals_raw_extraction.md` | Parmar Festivals; Lucent Festivals & Fairs |
| Books & Authors | `books_authors_raw_extraction.md` | Parmar Books & Authors; Lucent §50 |
| Sports | `sports_raw_extraction.md` | Parmar Sports; Lucent §53 (sports part)–§73 |
| Architecture | `architecture_raw_extraction.md` | Lucent Architecture/Sculpture/Painting; §7 World Monuments |
| Days & Events | `days_events_raw_extraction.md` | Parmar Important Days; Lucent §17–§19, foundation days |
| Awards | `awards_raw_extraction.md` | Parmar Awards & Honours; Lucent §38–§53 (Padma, Nobel, Oscar, Grammy, Booker, Magsaysay, Gandhi Peace, Kalinga, Committees/Commissions) |
| Famous People / Places / Firsts | `famous_people_places_raw_extraction.md` | Lucent §1–§13, §20–§21, §34–§37 (Parmar has no such chapter) |
| Organisations, Defence, Research (extra) | `organisations_defence_research_raw_extraction.md` | Lucent §14–§16, §22–§29, §33; Parmar International Orgs + National Orgs (not in calendar list) |
| Govt Policies | `govt_policies_raw_extraction.md` | Lucent §53 Youth Affairs; Ch.12 "Important Initiatives of the Government" (Parmar has none) |
| Sci-Tech | `sci_tech_computer_raw_extraction.md` | Lucent Ch.12 Computer (Parmar has no Sci-Tech chapter) |
| Census (extra) | `census_raw_extraction.md` | Parmar Census pp.474–476 |

**Note on the calendar's "Govt Policies" and "Sci-Tech":** neither book has a chapter with those names; the closest real content is Lucent's Youth Affairs + digital-governance initiatives, and the Computer chapter. Physics-side science content (instruments, inventions, SI units, atomic/nuclear) sits in `claude/physics-raw/*`. If the Testbook Sci-Tech tests turn out to be broader (space, defence tech, biotech, etc.), those topics will need to be pulled from the Physics/Chemistry/Biology raw files or a current-affairs source — decide when the tests are read.

**Extra chapters extracted although not in the calendar list:** Census, International Organisations, National Organisations (Parmar) and the Lucent Miscellany leftovers (Defence, Research Centres, National Parks after 1998, Cultural Organisations, Crematoria/Nicknames/Great Works).

## 4. Cross-reference list (pointers instead of re-extraction)
- Famous Places ↔ Geography raw (`claude/geography-raw/*`); Govt Policies ↔ Economy raw (`inflation_unemployment_schemes`, `poverty_bop_trade`, `agriculture_allied`, `banking_monetary_policy`) and the Polity PDF; Sci-Tech ↔ `claude/physics-raw/*`, `chemistry-raw/*`, biology; Awards ↔ Books/Sports files; UN/International institutions (IMF, WB, WTO) ↔ `claude/economy-raw/indices_reports_institutions_raw_extraction.md`; Census ↔ `geography-raw/human_geography_raw_extraction.md`.
- Inside Static GK: Days/UN weeks/International Years → days file; Music/Dances §30–32 → music/dances files; Awards §38–§53 → awards file; Sports §53–§73 → sports file; Books §50 → books file; Festivals §4 → festivals file; Committees §51–§52 → awards file.

## 5. Master doubts / verify list (one line each; details are in each file's Part C/Z)
1. Awards: Sharpless Nobel year printed 2021 (slip), blank Bardeen year, Grammy 2012/2013 mismatch, Magsaysay table gaps 2020–2022, Gandhi Peace Prize table gaps, Booker table lists International Booker as "Booker".
2. Architecture: Kandariya Mahadev year 1209, Connaught Place year 1774, Aurangzeb dates in painting section (printed).
3. Famous/Firsts: duplicated "firsts" with different answers (e.g. first woman Asiad gold); recent 2024–25 rows.
4. Organisations: National Parks after 1998 from a blurred scan — years marked (?); BRICS HQ/"5 new members" list; UN/WTO/ISA officeholders.
5. Census: religion table vs "declined by … pp" text; language table inconsistencies; "Census 2024/CMMS" status; second box headed "CENSUS 2011" carries 1951 data.
6. Sci-Tech: name/abbreviation slips (Kilbi, Fascimile, Telematrics…), Ted Nelson/"Soul of New Machine" attribution, PARAM-10000 credit name.
7. Govt Policies: RYSK "eight schemes" but six printed; RGNIYD Societies Registration Act year printed 1975; tele-density urban 133.82% "decreased".
8. Sports: Parmar vs Lucent cash amounts / awardee years (see sports Part C).

## 6. Housekeeping (for the user)
- Scratch folder `_claude_staticgk_work` (page images, OCR text, zoomed crops) was left in the Downloads folder — about 160 JPEGs plus text files. Deleting files on the computer needs the user's permission, so it was not removed; the folder can be deleted manually. Earlier `_claude_*` folders from previous subjects are also still there.
- Nothing in the original PDFs was edited.

## 7. Next steps (when the user returns)
- User completes the relevant Static GK tests → capture tests via the Chrome-extraction method in `claude/scripts/README.md` → classify questions by sub-topic → cross-reference against these raw files → build revision notes per sub-topic (per the Ancient-History leaner process).
- Before building, do the second-pass verification of any raw file that the tests lean on heavily (Awards, Sports, Days, Festivals are the densest).
