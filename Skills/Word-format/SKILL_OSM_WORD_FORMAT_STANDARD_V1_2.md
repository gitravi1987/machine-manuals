# OSM_WORD_FORMAT_STANDARD_V1_2.md
# Operating & Safety Manual — Master Word Document Format Standard

**Author:** Certified Safety Professional
**Applies To:** All machine safety manual projects — P1 onwards
**Last Updated:** May 2026
**Changelog from V1.1:**
- TOC: H1 entries only — 50% shorter; appears once only
- Cover + front matter duplication: removed
- Sec 1.6: name removed — role only
- Revision table: "Prepared By" column removed
- Sec 1.9 (ISO 7010 reference table): removed entirely
- Placeholders: bold text (was italic grey)
- Sec 3: max 2 pages, narrative only, no WARNING/DANGER boxes
- Sec 4.2: Image column added (ISO energy pictogram)
- DANGER boxes: removed from entire template
- Sec 4.4, 4.5, 5.4, 5.5, 6.4, 6.5, 6.7, 6.8, 6.9, 11.4, 12.2: flowcharts
- Sec 12.5: bullets only
- Sec 13.3: role only, no name
- Liability disclaimer: Section 13 only (removed from Sec 1)
- Sign-off blocks: single instance only
- Appendix A (Residual Risk Summary): permanently removed
- Appendix A = Maintenance Log | Appendix B = LOTO Log
- Generation: Workflow A (ChatGPT YAML + Claude chat) or Workflow B (Claude Code / Codex)
- Google Antigravity: dropped

---

## PART 1: PAGE SETUP

| Parameter | Value |
|---|---|
| Paper size | A4 |
| Orientation | Portrait |
| Top margin | 25mm |
| Bottom margin | 25mm |
| Left margin | 25mm |
| Right margin | 25mm |
| Gutter | 0mm |
| Header distance from edge | 12mm |
| Footer distance from edge | 12mm |

---

## PART 2: TYPOGRAPHY

### Font Family
**Calibri throughout — no exceptions.**

### Font Size Hierarchy

| Element | Size | Weight | Colour |
|---|---|---|---|
| Document title (cover) | 22pt | Bold | #1F3864 |
| Machine name (cover) | 18pt | Bold | #1F3864 |
| Section heading H1 | 14pt | Bold | #1F3864 |
| Sub-section heading H2 | 13pt | Bold | #1F3864 |
| Sub-sub-section H3 | 12pt | Bold | #1F3864 |
| Body text | 11pt | Regular | #000000 |
| Table body | 10pt | Regular | #000000 |
| Table header | 10pt | Bold | #FFFFFF |
| Caption | 10pt | Italic | #555555 |
| Placeholder label | 11pt | **Bold** | #000000 |
| Footer | 9pt | Regular | #555555 |
| Header | 9pt | Regular | #1F3864 |

### Paragraph Spacing

| Element | Before | After | Line |
|---|---|---|---|
| H1 | 18pt | 6pt | Single |
| H2 | 12pt | 4pt | Single |
| H3 | 8pt | 4pt | Single |
| Body | 0pt | 6pt | 1.15 |
| Table cell | 0pt | 0pt | Single |
| List item | 0pt | 4pt | Single |

---

## PART 3: COLOUR PALETTE

### Primary Colours

| Name | Hex | Use |
|---|---|---|
| Dark Blue | #1F3864 | Headings, table headers, borders, flowchart borders |
| Light Blue | #D9E1F2 | Alternating table rows, flowchart sub-action boxes |
| White | #FFFFFF | Table header text, flowchart background |
| Black | #000000 | Body text, borders |

### Alert Box Colours

> **DANGER boxes are not used in this template.** Removed May 2026.

| Box Type | Background | Border | Colour | Width |
|---|---|---|---|---|
| WARNING | #FFF2CC | Full | #000000 | 1pt |
| CAUTION | #FCE4D6 | Left | #FF6600 | 3pt |
| NOTICE | #F2F2F2 | Left | #000000 | 2pt |
| OPEN ACTION | #FCE4D6 | Left | #FF0000 | 3pt |
| PLACEHOLDER | #F7F7F7 | Left | #AAAAAA | 2pt |

### Table Colours

| Element | Colour |
|---|---|
| Header background | #1F3864 |
| Header text | #FFFFFF |
| Odd rows | #FFFFFF |
| Even rows | #D9E1F2 |
| Border | #1F3864, 0.5pt |

### Flowchart Colours (All Sections)

| Shape | Fill | Border | Text |
|---|---|---|---|
| Start/End pill (rx=19) | #1F3864 | #1F3864 | #FFFFFF |
| Process step rect (rx=6) | #FFFFFF | #1F3864 | #1F3864 |
| Sub-action rect | #D9E1F2 | #1F3864 | #1F3864 |
| Decision diamond | #FFFFFF | #1F3864 | #1F3864 |
| Arrow | #1F3864 | — | — |

---

## PART 4: HEADER & FOOTER

### Header (all pages except cover)

| Zone | Content | Style |
|---|---|---|
| Left | Machine name and model | Calibri 9pt #1F3864 |
| Centre | Operating & Safety Manual | Calibri 9pt #1F3864 |
| Right | Page N of N | Calibri 9pt #1F3864 |

Separator: single line below, #1F3864, 0.5pt.

### Footer
Centre: **CONFIDENTIAL** — Calibri 9pt bold #555555.
Separator: single line above, #CCCCCC, 0.5pt.

### Cover Page
No header or footer. Page numbering starts from page 2.

---

## PART 5: DOCUMENT FLOW

### Page Order

```
PAGE 1     — Cover Page
PAGE 2     — Revision History
PAGE 3–4   — Table of Contents (H1 only — SINGLE INSTANCE — never repeated)
PAGE 5     — Section 1: Front Matter
PAGE 6+    — Sections 2–13
FINAL      — Appendix A: Maintenance Log Template
           — Appendix B: LOTO Log Template
```

Each section starts on a new page (page break before every H1).

### Cover Page Layout

```
┌─────────────────────────────────────────────┐
│   [LOGO — centred, top third]               │
│   ─────────────────────────────────────     │
│   OPERATING & SAFETY MANUAL   [22pt Bold]   │
│   [Machine Name]              [18pt Bold]   │
│   ─────────────────────────────────────     │
│   Machine Reference: [ref]                  │
│   Manufacturer: [name]                      │
│   End User: [name]                          │
│   Installation: [facility, city, state]     │
│   ─────────────────────────────────────     │
│   Document Title  | [value]                 │
│   Document No.    | [value]                 │
│   Revision        | V1.0                    │
│   Date            | [Month Year]            │
│   Prepared By     | Certified Safety Prof.  │
│   Status          | Draft / Released        │
│   ─────────────────────────────────────     │
│   CONFIDENTIAL    [9pt centred #555555]     │
└─────────────────────────────────────────────┘
```

### Table of Contents
- H1 entries only — no H2 sub-entries
- Single instance on pages 3–4 — never repeated elsewhere
- Tab leader: dots | right-aligned page numbers
- Font: Calibri 11pt | Heading: 14pt bold #1F3864 centred
- Note: *Right-click → Update Field → Update entire table*

### Revision History (Page 2)
Four columns only — "Prepared By" removed:

| Revision | Date | Description | Reviewed By |
|---|---|---|---|
| V1.0 | [Month Year] | Initial issue | [Manufacturer] / [End User] |
| V1.1 | TBD | Post dry run | [Manufacturer] / [End User] |
| V2.0 | TBD | Full release | [Manufacturer] / [End User] |

---

## PART 6: SECTION 1 — FRONT MATTER

**Single instance, pages 5–6 maximum. No duplication with cover page.**

Sub-sections:
- 1.1 Scope of this Manual
- 1.2 Intended Audience
- 1.3 How to Use this Manual
- 1.4 Definitions & Abbreviations
- 1.5 Signal Words (table: WARNING / CAUTION / NOTICE with definitions)
- 1.6 Prepared by: Certified Safety Professional *(no individual name)*

**Removed permanently:**
- ❌ 1.3 Liability disclaimer → moved to Section 13 only
- ❌ 1.9 ISO 7010 sign reference table → removed entirely

---

## PART 7: SECTION 3 — HAZARD ID

**Maximum 2 pages. Narrative only.**

- No hazard register table in the body
- No WARNING or DANGER boxes
- 3–5 short paragraphs: hazard categories, risk levels, protective measures, residual risk statement
- Final sentence: *"Full hazard identification and risk assessment is documented in the Machine Safety Assessment Report [reference and date]."*

---

## PART 8: SECTION 4 — LOTO

### Table 4.2 — Energy Isolation Points (5 columns)

| Point ID | Energy Type | Image | Isolation Method | Location |
|---|---|---|---|---|
| LP-01 | Electrical | [ISO E001 icon 20×20mm] | Main rotary disconnect | Right panel |

- Image column: ISO 7010 / IEC 60417 energy type pictogram, 20×20mm inline
- Column widths: 10% / 15% / 10% / 35% / 30%

### Sections 4.4 & 4.5 — Tag-Out and Tag-In
**Flowcharts only.** No WARNING boxes. Max 8 steps each.

---

## PART 9: SECTION 5 — EMERGENCY STOP

### Sections 5.4 & 5.5
**Flowcharts only.** Max 6 steps each.
Functional safety performance table: **not included.**

---

## PART 10: SECTION 6 — OPERATING INSTRUCTIONS

### Flowchart Sub-Sections

| Sub-section | Content | Max Steps |
|---|---|---|
| 6.4 | Pre-start checks | 8 |
| 6.5 | Startup sequence | 8 |
| 6.7 | Normal operating cycle | 10 |
| 6.8 | Shutdown sequence | 6 |
| 6.9 | Emergency shutdown | 6 |

No WARNING boxes in or around these flowcharts.

---

## PART 11: SECTION 11 — HMI ALARMS

### Section 11.4
**Flowchart only.** Max 8 steps.
Flow: Alarm triggers → Identify code → Action decision → Resolve or escalate.

---

## PART 12: SECTION 12 — SAFETY FEATURES

### Section 12.2
Flowchart showing safety function hierarchy (input → logic → output) + max 5 bullet points below.

### Section 12.5
Bullet points only. Max 8 bullets.
Format: action verb + specific check + pass/fail criterion. No paragraph prose.

---

## PART 13: SECTION 13 — COMPLIANCE & CERTIFICATIONS

### Sec 13.3 — Prepared By
Role only:
```
Certified Safety Professional — Manual Author
Designation: Certified Safety Professional
Signature: _________________________
Date: _________________________
```

### Liability Disclaimer — Single Instance, Section 13 Only
```
LIABILITY DISCLAIMER

This Operating & Safety Manual has been prepared by a Certified Safety
Professional in accordance with ISO 12100:2010, ISO 20607:2019,
IEC 82079-1:2019, and IS 4571:2008, based on the Machine Safety
Assessment and technical documentation provided.

Where original technical data was unavailable, professional judgment
has been applied. All such areas are documented as Open Actions.

The customer is responsible for final review and verification before
the machine is placed into service. Items marked as Open Actions must
be verified and signed off by the customer's technical or safety
representative.

Neither the consulting practice nor the author assumes liability for
injuries or damages resulting from: non-compliance with this manual;
failure to maintain per the schedule; or operation by untrained personnel.
```

### Sign-Off Blocks — Once Only, End of Section 13
1. Manufacturer Authorization
2. End User Authorization
3. Certified Safety Professional — Manual Author

**Never repeated anywhere else in the document.**

---

## PART 14: ALERT BOX FORMAT

### WARNING
```
Background: #FFF2CC | Full border: 1pt #000000 | Padding: 8pt
Line 1: ⚠️ WARNING [ISO 7010 — Wxxx]  ← Bold 11pt #7F6000
Line 2+: Message text ← Regular 11pt #000000
```

### CAUTION
```
Background: #FCE4D6 | Left border: 3pt #FF6600 | Padding: 8pt
Line 1: ⚡ CAUTION [ISO 7010 — Wxxx]  ← Bold 11pt #FF6600
Line 2+: Message text ← Regular 11pt #000000
```

### NOTICE
```
Background: #F2F2F2 | Left border: 2pt #000000 | Padding: 8pt
Line 1: 📋 NOTICE  ← Bold 11pt #000000
Line 2+: Message text ← Regular 11pt #000000
```

### OPEN ACTION
```
Background: #FCE4D6 | Left border: 3pt #FF0000 | Padding: 8pt
Line 1: ⚠️ OPEN ACTION [OA-Pn-xxx]  ← Bold 11pt #CC0000
Line 2: Description ← Regular 11pt #000000
Line 3: Responsibility: [name] | Target: [date] | Status: Open ← Italic 10pt #555555
```

### PLACEHOLDER
```
Background: #F7F7F7 | Left border: 2pt #AAAAAA | Padding: 8pt
Line 1: **[PLACEHOLDER — description, source, status]**  ← Bold 11pt #000000
```

---

## PART 15: TABLE FORMATTING

```
Width: full page (fits 25mm margins)
Header: #1F3864 background, #FFFFFF text, 10pt Bold, centred
Rows: alternating #FFFFFF / #D9E1F2
Cell padding: 4pt top/bottom, 6pt left/right
Border: 0.5pt #1F3864 all sides
Vertical align: centre
```

### Column Width Guidance
- 2 columns: 40% / 60%
- 3 columns: 25% / 40% / 35%
- 4 columns: 20% / 35% / 25% / 20%
- 5+ columns: equal distribution

---

## PART 16: IMAGE & PLACEHOLDER

### Actual Image
```
Width: full column (max 160mm) | Centred | Border: 0.5pt #CCCCCC
Caption below: Calibri 10pt Italic #555555
Format: Figure [N]: [Description]
```

### Placeholder
```
Box fill: #F7F7F7 | Left border: 2pt #AAAAAA
Caption: **[PLACEHOLDER — description, source, status]**
Font: Calibri 11pt Bold #000000
```

---

## PART 17: FLOWCHART STANDARD (ALL SECTIONS)

### Shapes

| Shape | Used For | Fill | Border | Text |
|---|---|---|---|---|
| Pill rx=19 | Start / End | #1F3864 | #1F3864 | #FFFFFF |
| Rect rx=6 | Process step | #FFFFFF | #1F3864 | #1F3864 |
| Rect rx=6 shaded | Sub-action | #D9E1F2 | #1F3864 | #1F3864 |
| Diamond | Decision | #FFFFFF | #1F3864 | #1F3864 |

### Text Rules
- Step text: ≤ 10 words, action verb first
- Decisions: Yes/No branches only
- Font: Calibri 11pt steps, 10pt labels

### Layout
- Direction: top to bottom
- Arrows: #1F3864, 1pt
- Max 10 steps — split into two if more needed
- Must pass greyscale print test

### Sections Using Flowcharts

| Section | Topic |
|---|---|
| 4.4 | LOTO Tag-Out |
| 4.5 | LOTO Tag-In |
| 5.4 | E-Stop activation |
| 5.5 | E-Stop reset |
| 6.4 | Pre-start checks |
| 6.5 | Startup sequence |
| 6.7 | Operating cycle |
| 6.8 | Shutdown |
| 6.9 | Emergency shutdown |
| 11.4 | Alarm response |
| 12.2 | Safety function overview |

---

## PART 18: ISO 7010 SAFETY SIGNS

| Code | Shape | Background | Use |
|---|---|---|---|
| W001 | Triangle | Yellow #FFCC00 | General warning |
| W003 | Triangle | Yellow #FFCC00 | Crushing hazard |
| W017 | Triangle | Yellow #FFCC00 | Electrical hazard |
| W019 | Triangle | Yellow #FFCC00 | Automatic start-up |
| W028 | Triangle | Yellow #FFCC00 | Entanglement |
| P002 | Circle | White + red diagonal | Do not touch |
| P010 | Circle | White + red diagonal | Do not switch on |
| M008 | Circle | Blue #0050A0 | Wear gloves |
| M009 | Circle | Blue #0050A0 | Wear safety footwear |

**Dimensions:** 20×20mm inline in alert boxes. **Section 1.9 removed** — no standalone sign table.

**Placement:** Inline at the exact procedural step where hazard exists. Never at section headers.

---

## PART 19: APPENDIX STANDARD

**Two appendices only:**

| Appendix | Title | Content |
|---|---|---|
| A | Maintenance Log Template | Blank log, 10 rows minimum |
| B | LOTO Log Template | Blank LOTO log, 10 rows minimum |

Appendix A (Residual Risk Summary) permanently removed. Customer has the RA report.
Open Actions Register = standalone `.xlsx` only. Never in the manual.

---

## PART 20: GENERATION METHODS

### Workflow A — Chat-Based (ChatGPT YAML + Claude Chat)

```
1. ChatGPT → YAML structure outline
2. Claude chat → section-by-section authoring (one conversation)
3. Claude chat → .docx generation via Node.js docx 9.6.1 (new conversation)
   + .xlsx generation via Python openpyxl
```

Word generation instruction block (paste at start of generation conversation):
```
WORD GENERATION BRIEF — [Project Code] [Machine Name]

Apply OSM_WORD_FORMAT_STANDARD_V1_2.md formatting.

PAGE: A4, 25mm margins
FONT: Calibri | H1: 14pt Bold #1F3864 | H2: 13pt | Body: 11pt
COLOURS: Heading #1F3864 | Alt row #D9E1F2 | Border #1F3864 0.5pt
ALERT: WARNING #FFF2CC full border | CAUTION #FCE4D6 orange left
       NOTICE #F2F2F2 black left | OPEN ACTION #FCE4D6 red left
PLACEHOLDER: Bold 11pt #000000 in #F7F7F7 box, grey left border
HEADER: Machine name (L) | OSM title (C) | Page N of N (R)
FOOTER: CONFIDENTIAL (C)
COVER: No header/footer. Logo top-centre. Titles #1F3864.
FLOWCHARTS: Blue borders #1F3864, white background, pill terminals
TOC: H1 only, single instance, pages 3–4
AUTHOR: Certified Safety Professional (no individual name)
OUTPUT: [EndUser]_[MachineName]_OSM_V1.0.docx
        [Client]_[MachineName]_OpenActions_V1.0.xlsx

Send sections one at a time. Confirm receipt before next.
```

### Workflow B — Code-Based (Claude Code / Codex)

```
1. Prepare structured JSON/YAML input (manually or with Claude chat)
2. Claude Code or Codex generates .docx and .xlsx programmatically
   — No LLM chat during generation
3. Claude chat reviews output against compliance checklist
```

**Dropped:** Google Antigravity — not used.

Technical rules:
- Read `/mnt/skills/public/docx/SKILL.md` before any code
- Each section = standalone `.js` file
- Inject via Python `content.replace()` — never `str_replace` for Unicode
- Validate: `python3 /mnt/skills/public/docx/scripts/office/validate.py`
- `PageNumber.CURRENT` inside `TextRun` for page numbers

---

## PART 21: VERSIONING & FILENAMES

| Version | Trigger |
|---|---|
| V1.0 | Initial — placeholders in, all OAs open |
| V1.1 | Post dry run — site items updated |
| V2.0 | Full release — OAs closed, sign-off done |

| File | Convention |
|---|---|
| Manual | `[EndUser]_[MachineName]_OSM_V[n.n].docx` |
| Open Actions | `[Client]_[MachineName]_OpenActions_V[n.n].xlsx` |

---

## PART 22: PAGE COUNT TARGETS

| Tier | Target | Hard Limit |
|---|---|---|
| A | 40–60 pages | 60 |
| B | 25–40 pages | 40 |
| C | 15–25 pages | 25 |

### Page Budget (Tier A estimate)

| Section | Pages |
|---|---|
| Cover + Front Matter | 3–4 |
| Machine Overview | 2–3 |
| Hazard ID | 2 (hard max) |
| LOTO | 3–4 |
| E-Stop | 2 |
| Operating Instructions | 4–5 |
| Maintenance | 3–4 |
| Schematics (8–10) | 2–3 |
| HMI Alarms | 1–2 |
| Safety Features | 2–3 |
| Compliance | 2–3 |
| Appendix A + B | 1–2 |
| **TOTAL** | **~27–41 pages** |

---

*End of OSM_WORD_FORMAT_STANDARD_V1_2.md*
*Author: Certified Safety Professional | Version: 1.2 — May 2026*
