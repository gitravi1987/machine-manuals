# GROK_OSM_FORMAT — Operating & Safety Manual Word Format Standard

**Version:** 2.0 — July 2026  
**Authority for:** All manuals generated under `Grok Machine Manual Projects\`  
**Source lineage:** Claude `SKILL_OSM_WORD_FORMAT_STANDARD_V1_2.md` + Indo-MIM OSM V5 visual style  
**Does not modify** root `Machine Manuals\Skills\Word-format\` (Claude skill remains untouched).

**Changelog V2.0 (from Grok V1.0 short card):**
- Expanded to full generation-ready standard (cover, TOC, headers, styles, alerts, flowcharts)
- Word **Heading 1 / Heading 2** styles mandatory (not Normal + paint)
- H2 size fixed at **13 pt** (not 12 pt)
- TOC: real Word TOC field, **H1 only**, tab leaders + page numbers
- Header: machine | OSM | **Page N of N** (not Page N alone)
- Footer: **CONFIDENTIAL** only (no draft/OEM brand string unless Ravi overrides)
- Cover layout aligned to V1.2 (meta fields; no dense ad-hoc tables that differ from standard)
- Revision table: **Reviewed By** only (no Prepared By column)
- Lessons from P7 vs Indo-MIM V5 format comparison baked into generator rules
- Grok tooling: **python-docx** (not Node) unless Ravi says otherwise

> **P7 Rani Enterprises V1.0 was not rebuilt.** This file applies from the **next** project (or next voluntary rebuild).

---

## 0. ALWAYS CREATE OUTPUTS HERE

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\<pilot>\outputs\
```

Never under `.grok\worktrees\...`.

**Optional read-only reference (do not edit unless Ravi asks):**
```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Skills\Word-format\SKILL_OSM_WORD_FORMAT_STANDARD_V1_2.md
```

---

## 1. PAGE SETUP

| Parameter | Value |
|-----------|-------|
| Paper | A4 (210 × 297 mm) |
| Orientation | Portrait |
| Margins | 25 mm all sides |
| Gutter | 0 mm |
| Header from edge | 12 mm |
| Footer from edge | 12 mm |
| Different first page | **Yes** (cover has no header/footer) |

---

## 2. TYPOGRAPHY

**Font family: Calibri throughout — no exceptions.**

### Size hierarchy

| Element | Size | Weight | Colour |
|---------|------|--------|--------|
| Document title (cover) | 22 pt | Bold | #1F3864 |
| Machine name (cover) | 18 pt | Bold | #1F3864 |
| Cover subtitle / org line | 12 pt | Regular | #555555 |
| Section heading **H1** | 14 pt | Bold | #1F3864 |
| Sub-section **H2** | **13 pt** | Bold | #1F3864 |
| Sub-sub-section **H3** | 12 pt | Bold | #1F3864 |
| Body text | 11 pt | Regular | #000000 |
| Table body | 10 pt | Regular | #000000 |
| Table header | 10 pt | Bold | #FFFFFF |
| Caption | 10 pt | Italic | #555555 |
| Placeholder label | 11 pt | **Bold** | #000000 |
| Header | 9 pt | Regular | #1F3864 |
| Footer | 9 pt | Bold | #555555 |

### Paragraph spacing

| Element | Before | After | Line |
|---------|--------|-------|------|
| H1 | 18 pt | 6 pt | Single |
| H2 | 12 pt | 4 pt | Single |
| H3 | 8 pt | 4 pt | Single |
| Body | 0 pt | 6 pt | 1.15 |
| Table cell | 2 pt | 2 pt | Single |
| List item | 0 pt | 4 pt | Single |

### Heading rules (mandatory for next projects)

1. Use real Word styles: **`Heading 1`**, **`Heading 2`**, **`Heading 3`** (or equivalent outline styles that map to TOC levels).
2. Apply **direct formatting** on those styles so final colour is **#1F3864** and sizes match the table above (override theme blues #365F91 / #4F81BD).
3. **Do not** implement section titles as `Normal` + bold only.
4. **H1 text style:** Title Case is preferred for new Grok manuals  
   (`1. Front Matter`, not `1.  FRONT MATTER`) unless Ravi requests ALL CAPS Indo-MIM look.
5. **Page break before every H1** (including appendices).
6. Outline level: H1 = 0, H2 = 1, H3 = 2 (required for TOC field).

---

## 3. COLOUR PALETTE

### Primary

| Name | Hex | Use |
|------|-----|-----|
| Dark Blue (navy) | #1F3864 | Headings, table headers, table borders, flowchart borders, header text |
| Light Blue | #D9E1F2 | Alternating table rows, flowchart sub-action |
| White | #FFFFFF | Table header text, flowchart step fill |
| Black | #000000 | Body text |
| Grey | #555555 | Footer, captions, cover CONFIDENTIAL |
| Light grey line | #CCCCCC | Footer separator, image border |

### Alert box fills

| Box | Background | Border | Notes |
|-----|------------|--------|-------|
| WARNING | #FFF2CC | Full 1 pt #000000 | No DANGER boxes ever |
| CAUTION | #FCE4D6 | Left 3 pt #FF6600 | |
| NOTICE | #F2F2F2 | Left 2 pt #000000 | |
| OPEN ACTION | #FCE4D6 | Left 3 pt #FF0000 / title #CC0000 | |
| PLACEHOLDER | #F7F7F7 | Left 2 pt #AAAAAA | Bold placeholder text |

### Tables

| Element | Spec |
|---------|------|
| Header background | #1F3864 |
| Header text | #FFFFFF bold 10 pt centred |
| Odd rows | #FFFFFF |
| Even rows | #D9E1F2 |
| Border | **#1F3864, 0.5 pt** all sides (not default black grid alone) |
| Cell padding | ~4 pt top/bottom, 6 pt left/right |
| Vertical align | Centre |

Column width guidance: 2-col 40/60; 3-col 25/40/35; 4-col 20/35/25/20; 5+ equal.

---

## 4. HEADER & FOOTER

### Header (all pages except cover)

| Zone | Content | Style |
|------|---------|-------|
| Left | Machine name (and model if short) | Calibri 9 pt #1F3864 |
| Centre | Operating & Safety Manual | Calibri 9 pt #1F3864 |
| Right | **Page N of N** | Calibri 9 pt #1F3864 |

- Implement with tab stops or a single-row layout that keeps three zones.
- Word fields: `PAGE` and `NUMPAGES` (not PAGE alone).
- Separator under header: single line #1F3864, 0.5 pt (if supported cleanly in generator).

### Footer

| Zone | Content | Style |
|------|---------|-------|
| Centre | **CONFIDENTIAL** | Calibri 9 pt bold #555555 |

- **Default footer is only the word CONFIDENTIAL.**  
- Do **not** append “Draft | OEM name” unless Ravi explicitly requests a pilot watermark.
- Separator above footer: single line #CCCCCC, 0.5 pt (if supported).

### Cover page

- **No header, no footer** (different first page).
- Page numbering effectively starts after cover (body pages show correct N of N).

---

## 5. DOCUMENT FLOW (PAGE ORDER)

```
PAGE 1       — Cover Page
PAGE 2       — Revision History
PAGE 3–4     — Table of Contents (H1 only — SINGLE INSTANCE — never repeated)
PAGE 5+      — Section 1 Front Matter, then remaining body sections
FINAL        — Appendix A: Maintenance Log Template
             — Appendix B: LOTO Log Template
```

Each major section (H1) starts on a new page.

### Default full section map (Indo-MIM / V1.2 spine)

Use this unless the project charter explicitly authorises a condensed map:

| Sec | Title |
|-----|-------|
| 1 | Front Matter |
| 2 | Machine Overview |
| 3 | Hazard Identification & Risk Assessment |
| 4 | Lockout / Tagout (LOTO) Procedures |
| 5 | Emergency Stop Function |
| 6 | Operating Instructions |
| 7 | Maintenance & Care |
| 8 | Electrical Schematic |
| 9 | Pneumatic Schematic |
| 10 | HMI / Alarms & Fault Codes |
| 11 | Safety Features & Interlocks |
| 12 | Compliance & Certifications *(or Sec 12–13 split if using full V1.2 liability/sign-off)* |

**Condensed maps** (e.g. lean Tier C / low-fee) are allowed only when Ravi specifies for that project. Format rules (type, colours, TOC, header/footer, styles) still apply fully.

### Appendices (always)

| Appendix | Title |
|----------|-------|
| A | Maintenance Log Template |
| B | LOTO Log Template |

- Residual Risk Summary appendix: **permanently removed**
- Open Actions: **standalone `.xlsx` only** — never inside the `.docx`

---

## 6. COVER PAGE LAYOUT

```
┌─────────────────────────────────────────────┐
│   [Optional logo — centred, top third]      │
│   ─────────────────────────────────────     │
│   OPERATING & SAFETY MANUAL   [22pt Bold]   │
│   [Machine Name]              [18pt Bold]   │
│   [Manufacturer | End User]   [12pt #555]   │
│   ─────────────────────────────────────     │
│   Machine Reference: [ref]                  │
│   Manufacturer: [name]                      │
│   End User: [name]                          │
│   Installation: [facility / city / state]   │
│   ─────────────────────────────────────     │
│   Document Title  | Operating & Safety Manual│
│   Document No.    | [CODE-OSM-001]          │
│   Revision        | V1.0                    │
│   Date            | [Month Year]            │
│   Prepared By     | Certified Safety Prof.  │
│   Status          | Draft / Released        │
│   ─────────────────────────────────────     │
│   CONFIDENTIAL    [9pt centred #555555]     │
└─────────────────────────────────────────────┘
```

**Cover rules:**
- Meta block may be a clean 2-column table (label | value) with navy label column `#D9E1F2` or white + navy text — keep sparse, same fields as above.
- Do **not** invent extra commercial fields (tier, price, page targets) on the cover.
- Prepared By = role only: **Certified Safety Professional**.

---

## 7. REVISION HISTORY (PAGE 2)

Four columns only — **Prepared By column removed**:

| Revision | Date | Description | Reviewed By |
|----------|------|-------------|-------------|
| V1.0 | [Month Year] | Initial issue | Manufacturer / End User |
| V1.1 | TBD | Post dry run / site update | Manufacturer / End User |
| V2.0 | TBD | Full release | Manufacturer / End User |

- Title: **Revision History** as H1 (or cover-adjacent title 14 pt navy).
- Table uses standard navy header styling.

---

## 8. TABLE OF CONTENTS (PAGES 3–4)

### Requirements

| Rule | Detail |
|------|--------|
| Entries | **H1 only** — no H2 sub-entries in TOC |
| Instance | **Single** TOC — never repeated later |
| Implementation | Prefer real Word **TOC field** (`TOC \o "1-1" \h \z \u` or H1-only equivalent) |
| Leaders | Dot leaders |
| Page numbers | Right-aligned |
| Heading line | `TABLE OF CONTENTS` or `Table of Contents` — 14 pt bold #1F3864 |
| Body of TOC | Calibri 11 pt |
| User note | *Right-click → Update Field → Update entire table* (or Ctrl+A then F9) |

### Forbidden TOC patterns

- Static bullet list of section titles with no page numbers (P7 V1.0 shortfall — do not repeat)
- TOC that includes H2/H3 entries
- Second TOC inside body sections

If the generator cannot emit a true TOC field, document the limitation and insert a field-ready stub the user can update in Word — still H1-only with leaders/page number placeholders.

---

## 9. SECTION-LEVEL FORMAT RULES (CONTENT STRUCTURE)

### Section 1 — Front Matter

Single instance after TOC. No duplication of full cover data.

Typical subs:
- 1.1 Scope  
- 1.2 Intended Audience  
- 1.3 How to Use / General Safety Rules  
- 1.4 Definitions (if needed)  
- 1.5 Signal Words (table: WARNING / CAUTION / NOTICE)  
- 1.6 Prepared by: Certified Safety Professional *(role only)*  

**Removed permanently from Sec 1:** liability disclaimer (→ compliance section only); ISO 7010 full sign catalogue table.

### Section 3 — Hazard ID

- Max ~2 pages; **narrative only**
- No hazard register table in body
- No DANGER boxes; avoid WARNING walls in Sec 3
- If MSA exists: end with reference to Machine Safety Assessment Report
- If no MSA: OPEN ACTION + Independent Safety Consultant language — do not invent scores/PLr

### Section 4 — LOTO

- Energy isolation table: Point ID | Energy Type | Image (optional) | Isolation Method | Location  
- Tag-Out / Tag-In: **flowcharts only** (≤8–10 steps)

### Section 5 — E-Stop

- Activation / reset: **flowcharts**
- No invented PL tables without assessment

### Section 6 — Operating

Flowchart-preferred for: pre-start, startup, cycle, shutdown, emergency shutdown (≤10 words/step).

### Schematics (8–9 or merged)

Missing drawings → PLACEHOLDER box for customer insert; do not invent schematics.

### Compliance / liability / sign-off

- Liability disclaimer: **once**
- Sign-off blocks: **once** at end of compliance section  
- Author fields: role only  

---

## 10. ALERT BOX FORMAT

**Never use DANGER.**

### WARNING
- Fill #FFF2CC | Full border 1 pt #000000 | Padding ~8 pt  
- Title line bold; body regular 11 pt  

### CAUTION
- Fill #FCE4D6 | Left border 3 pt #FF6600  

### NOTICE
- Fill #F2F2F2 | Left border 2 pt #000000  

### OPEN ACTION
- Fill #FCE4D6 | Left border 3 pt red  
- Include OA-ID when known; responsibility / target / status if available  
- Full register remains in Excel  

### PLACEHOLDER
- Fill #F7F7F7 | Left border 2 pt #AAAAAA  
- Text: **`[PLACEHOLDER — description, source, status]`** bold 11 pt  

In python-docx, approximate left borders with full thin borders if left-only borders are awkward; keep fill colours exact.

---

## 11. FLOWCHART STANDARD

Table-based vertical flow (greyscale-readable):

| Shape | Fill | Border | Text |
|-------|------|--------|------|
| Start / End | #1F3864 | #1F3864 | White bold |
| Process step | #FFFFFF | #1F3864 | #1F3864 |
| Sub-action | #D9E1F2 | #1F3864 | #1F3864 |

Rules:
- ≤10 steps; ≤10 words per step; action verb first  
- Top-to-bottom  
- Use for LOTO tag-out/in, E-Stop activate/reset, startup/cycle/shutdown, alarm response, safety overview as applicable  

---

## 12. IMAGES & FIGURES

| Item | Spec |
|------|------|
| Width | Max ~160 mm, centred |
| Border | 0.5 pt #CCCCCC |
| Caption | Calibri 10 pt italic #555555 — `Figure N: Description` |
| Missing photo | PLACEHOLDER box + caption, not fake image |

---

## 13. ISO 7010 (OPTIONAL INLINE)

Small pictograms (e.g. 20×20 mm) may appear **inline** at procedural steps.  
No standalone ISO 7010 catalogue section in Front Matter.

---

## 14. GENERATION RULES (GROK SANDBOX)

### Tooling

| Deliverable | Tool |
|-------------|------|
| `.docx` | **python-docx** via pilot `working\build_osm.py` |
| Open Actions `.xlsx` | **openpyxl** via `working\build_open_actions.py` |
| Optional skill read | `~/.grok/skills/docx/SKILL.md`, `xlsx/SKILL.md` |

### Generator checklist (next project)

- [ ] A4 + 25 mm margins + 12 mm header/footer distance  
- [ ] Different first page; cover blank HF  
- [ ] Header: machine · Operating & Safety Manual · Page N of N  
- [ ] Footer: CONFIDENTIAL only  
- [ ] Real Heading 1/2 (outline levels); H1 page break; H2 = 13 pt  
- [ ] Cover matches §6 fields  
- [ ] Revision 4-col Reviewed By  
- [ ] TOC field H1-only + update note  
- [ ] Table navy headers, alt rows #D9E1F2, borders #1F3864 0.5 pt  
- [ ] No DANGER boxes  
- [ ] Appendices A/B only; Open Actions xlsx separate  
- [ ] Author role only  
- [ ] No commercial tier/page-target text in customer-facing fields  

### Word generation brief (paste into generator session)

```
WORD GENERATION BRIEF — GROK OSM FORMAT V2.0

Apply GROK_OSM_FORMAT.md (this file) fully.

PAGE: A4, 25mm margins, header/footer 12mm, different first page
FONT: Calibri | H1: 14pt Bold #1F3864 | H2: 13pt Bold #1F3864 | Body: 11pt
STYLES: Use Word Heading 1 / Heading 2 (not Normal-only titles)
COLOURS: Navy #1F3864 | Alt row #D9E1F2 | Borders #1F3864 0.5pt
ALERTS: WARNING / CAUTION / NOTICE / OPEN ACTION / PLACEHOLDER only — no DANGER
HEADER: Machine (L) | Operating & Safety Manual (C) | Page N of N (R)
FOOTER: CONFIDENTIAL only (C)
COVER: No HF; 22pt title; 18pt machine; meta fields; CONFIDENTIAL 9pt grey
ORDER: Cover → Revision (4-col Reviewed By) → TOC H1-only field → Sections → App A/B
TOC: Single instance; H1 only; Update Field note
FLOWCHARTS: Navy terminals, white steps, ≤10 steps / ≤10 words
AUTHOR: Certified Safety Professional (no personal name)
OUTPUT under: Grok Machine Manual Projects\<pilot>\outputs\
  [EndUser]_[MachineName]_OSM_V[n.n].docx
  [Client]_[MachineName]_OpenActions_V[n.n].xlsx

Fix in source JSON/YAML/build scripts and regenerate — never patch .docx by hand.
```

---

## 15. VERSIONING & FILENAMES

| Version | Trigger |
|---------|---------|
| V1.0 | Initial draft — placeholders / OAs open |
| V1.1 | Post dry run / photo enrichment |
| V2.0 | Release candidate — OAs closed, sign-off |

| File | Convention |
|------|------------|
| Manual | `[EndUser]_[MachineName]_OSM_V[n.n].docx` |
| Open Actions | `[Client]_[MachineName]_OpenActions_V[n.n].xlsx` |

---

## 16. PAGE COUNT TARGETS (INTERNAL PLANNING ONLY)

Use for scoping **outside** customer-facing text. **Never print tier labels or page budgets on the cover or in body prose.**

| Tier | Target | Hard limit |
|------|--------|------------|
| A | 40–60 | 60 |
| B | 25–40 | 40 |
| C | 15–25 | 25 |

---

## 17. KNOWN FAILURES TO AVOID (from P7 vs Indo-MIM V5)

| Failure | Correct behaviour |
|---------|-------------------|
| Headings as Normal + bold | Real Heading 1/2 styles + navy |
| H2 at 12 pt | H2 at **13 pt** |
| Static TOC without pages | TOC field, H1 only, page numbers |
| Header Page N only | Page **N of N** |
| Footer “CONFIDENTIAL — Draft \| OEM” | Footer **CONFIDENTIAL** only |
| Cover cluttered with non-standard fields | Cover fields per §6 |
| Revision “Prepared By” column | **Reviewed By** only |
| Black default table borders only | Explicit navy 0.5 pt borders |
| Open Actions inside Word | Standalone xlsx |
| DANGER boxes | Never |
| Patching final .docx | Fix sources → regenerate |

---

## 18. AUTHORITY CHAIN (GROK)

1. `GROK.md` — path isolation + non-negotiables  
2. **This file (`GROK_OSM_FORMAT.md`)** — Word visual/layout standard  
3. `GROK_WORKFLOW_B.md` — process  
4. `GROK_MACHINE_MANUALS_SKILL.md` — content drafting  
5. `GROK_MASTER_TEMPLATE.yaml` — content skeleton  

If this file and a pilot `build_osm.py` conflict: **update the builder** to match this file; do not silently weaken format.

---

*End of GROK_OSM_FORMAT.md V2.0*  
*Grok Machine Manual Projects sandbox — Certified Safety Professional*
