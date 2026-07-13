# WORKFLOW_A.md — Chat-Based Manual Creation
## ChatGPT YAML → Claude Chat (Author) → Claude Chat (Generate)

**Owner:** Certified Safety Professional
**Use When:** New projects, complex machines, first drafts, heavy iteration needed
**Last Updated:** May 2026
**Formatting Spec:** `OSM_WORD_FORMAT_STANDARD_V1_2.md`

---

## STEP 1 — STRUCTURE (ChatGPT)

Brief ChatGPT with machine specs + RA data. Ask it to generate a YAML outline.

**ChatGPT prompt template:**
```
Generate a YAML outline for an Operating & Safety Manual.
Machine: [name, make, model, year]
Client: [company] | End User: [company] | Site: [location]
Tier: [A/B/C]
Sections required: [list from tier — see Section Map below]
RA hazards identified: [list from RA report]
LOTO points: [list]
Control system: [PLC/HMI/hardwired]
Key specs: [power, pressure, dimensions]

Output YAML with: section number, section title, sub-sections,
key data points to populate per sub-section.
```

**Output from ChatGPT:** `section_outline.yaml`

---

## STEP 2 — AUTHOR (Claude Chat — One Conversation)

Open a new conversation in this Claude project. Upload:
- `section_outline.yaml` (from Step 1)
- RA report / Machine Safety Assessment
- Drawing files
- Site photos (if available)

**Authoring brief (paste at conversation start):**
```
AUTHORING BRIEF — [Project Code] [Machine Name]

I am drafting an Operating & Safety Manual.
Tier: [A/B/C] | Client: [name] | End User: [name]

Rules:
- Draft section by section. Wait for my confirmation before next section.
- Never invent machine features not in the uploaded data
- Missing data → [TBC — pending confirmation] or flag as Open Action
- No DANGER boxes anywhere
- Section 3: max 2 pages, narrative only, no WARNING boxes
- Sections 4.4, 4.5, 5.4, 5.5, 6.4, 6.5, 6.7, 6.8, 6.9, 11.4, 12.2: flowcharts only
- Placeholders: bold text [PLACEHOLDER — description, source, status]
- Liability disclaimer: Section 13 only
- Designation: "Certified Safety Professional" — no individual name
- No reference to SICK or any RA firm — use "Independent Safety Consultant"

Start with Section 2 (Machine Overview). I will confirm before you proceed.
```

**Draft order:** Section 2 → 3 → 4 → 5 → 6 → 7 → 8/9/10 → 11 → 12 → 13 → Appendices

**Rule:** All drafting in ONE conversation. Confirm each section before next.

**Output:** Complete manual content in Markdown, section by section.

---

## STEP 3 — GENERATE (Claude Chat — New Conversation)

Open a **new conversation** in this Claude project. Paste the generation brief below, then feed approved content section by section.

**Word generation brief (paste at conversation start):**
```
WORD GENERATION BRIEF — [Project Code] [Machine Name]

Generate Operating & Safety Manual .docx from content I will paste section by section.
Apply OSM_WORD_FORMAT_STANDARD_V1_2.md formatting throughout.

PAGE SETUP: A4, 25mm margins all sides

TYPOGRAPHY:
- Calibri throughout
- H1: 14pt Bold #1F3864 | H2: 13pt Bold #1F3864 | H3: 12pt Bold #1F3864
- Body: 11pt Regular #000000 | Table body: 10pt | Table header: 10pt Bold #FFFFFF

COLOURS:
- Headings: #1F3864 | Table header bg: #1F3864 | Alt rows: #D9E1F2
- Table border: #1F3864 0.5pt

ALERT BOXES (no DANGER boxes — do not generate any):
- WARNING: #FFF2CC background, black full border 1pt
- CAUTION: #FCE4D6 background, orange left border 3pt #FF6600
- NOTICE: #F2F2F2 background, black left border 2pt
- OPEN ACTION: #FCE4D6 background, red left border 3pt #FF0000

PLACEHOLDERS: Bold 11pt #000000 in #F7F7F7 box, grey left border 2pt #AAAAAA

FLOWCHARTS (sections 4.4, 4.5, 5.4, 5.5, 6.4, 6.5, 6.7, 6.8, 6.9, 11.4, 12.2):
- Blue borders #1F3864, white fill, pill start/end terminals (#1F3864 fill, white text)
- Max 10 steps | Action verb first | ≤10 words per step | Greyscale-readable

TOC: H1 entries only. Single instance pages 3–4. Never repeat.

SECTION 4 TABLE 4.2: 5 columns:
  Point ID | Energy Type | Image (ISO pictogram 20×20mm) | Isolation Method | Location

HEADER: Machine name (left) | Operating & Safety Manual (centre) | Page N of N (right)
FOOTER: CONFIDENTIAL (centre)
COVER: No header/footer. Logo top-centre. Titles #1F3864. No individual name.

AUTHOR FIELD: Certified Safety Professional (no individual name)
REVISION TABLE: 4 columns only — Revision | Date | Description | Reviewed By

APPENDICES: A = Maintenance Log Template | B = LOTO Log Template (nothing else)

TECHNICAL:
- Node.js docx library v9.6.1
- Each section as standalone .js file
- Inject via Python content.replace() — never str_replace for Unicode
- Validate: python3 /mnt/skills/public/docx/scripts/office/validate.py after each section
- PageNumber.CURRENT inside TextRun (not new PageNumber())
- Extend bodyChildren when adding sections beyond original stub

OUTPUT:
- [EndUser]_[MachineName]_OSM_V1.0.docx → /mnt/user-data/outputs/
- [Client]_[MachineName]_OpenActions_V1.0.xlsx → /mnt/user-data/outputs/

Confirm receipt of each section before I send the next.
```

---

## PROJECT REGISTRY

| Code | Client | Machine | Tier | Status |
|------|--------|---------|------|--------|
| P1 | Accurate Machines | 48-Spindle Drilling | A | ✅ Complete — no coolant system |
| P2 | KEMC / Valeo | Tilting Machine (Clutch Plate) | B | ✅ Complete |
| P3 | Valeo | LE Test Bench | A | ✅ Complete |
| P4 | Indo-MIM / Tata Electronics | BG Snap Assembly Machine (V67) | A | ✅ Complete |
| P5+ | TBD | TBD | TBD | Follow this workflow |

---

## TIER SCOPING

Run this before starting any project. Confirm tier before writing anything.

| Question | Yes | No |
|----------|-----|----|
| Risk assessment (RA) available? | Continue | Recommend RA first (+₹20k–40k, 2–3 weeks) |
| Full schematics available? | → Tier A | → Tier B/C |
| Control system docs (PLC/HMI) available? | → Tier A | → Tier B/C |
| Machine < 10 years, active maintenance? | → Tier A/B | → Tier B/C |
| Procedures formally documented? | → Tier A/B | → Tier B/C |

| Tier | Situation | Pages | Price | Timeline |
|------|-----------|-------|-------|----------|
| A | Full RA + schematics + PLC + photos | 40–60 | ₹15k–20k | 14–21 days |
| B | RA + partial schematics + informal procedures | 25–40 | ₹10k–12k | 10–14 days |
| C | RA only, no schematics, legacy machine | 15–25 | ₹8k–10k | 7–10 days |

---

## SECTION MAP BY TIER

| Sec | Title | Tier A | Tier B | Tier C |
|-----|-------|--------|--------|--------|
| 1 | Cover, TOC, Front Matter | ✅ | ✅ | ✅ |
| 2 | Machine Overview | ✅ | ✅ | ✅ |
| 3 | Hazard ID (narrative, 2 pages max) | ✅ | ✅ | ✅ Abbreviated |
| 4 | LOTO Procedures | ✅ | ✅ | ✅ |
| 5 | Emergency Stop | ✅ | ✅ | ✅ |
| 6 | Operating Instructions | ✅ | ✅ | ✅ |
| 7 | Maintenance & Care | ✅ | ✅ Partial | ✅ Abbreviated |
| 8 | Electrical Schematic | ✅ | ⚠️ Placeholder | ❌ Omit |
| 9 | Pneumatic Schematic | ✅ | ⚠️ Placeholder | ❌ Omit |
| 10 | Hydraulic Schematic | ✅ If applicable | ⚠️ Placeholder | ❌ Omit |
| 11 | HMI Alarms & Fault Codes | ✅ If applicable | ⚠️ If available | ❌ N/A |
| 12 | Safety Features & Interlocks | ✅ | ✅ Streamlined | ✅ Abbreviated |
| 13 | Compliance & Certifications | ✅ | ✅ | ✅ |
| Appendix A | Maintenance Log Template | ✅ | ✅ | ✅ |
| Appendix B | LOTO Log Template | ✅ | ✅ | ✅ |

---

## STRUCTURAL RULES (ALL PROJECTS)

**Section 1:**
- TOC: H1 only. Single instance pages 3–4. Never repeated.
- Revision table: Revision / Date / Description / Reviewed By. No "Prepared By".
- Sec 1.6: "Certified Safety Professional" — no individual name
- Sec 1.9: Removed. Do not include ISO 7010 sign reference table.
- Liability disclaimer: NOT in Section 1 — lives in Section 13 only

**Section 3:** Max 2 pages. Narrative only. No tables. No WARNING or DANGER boxes. End with reference to Machine Safety Assessment Report.

**Section 4:** Table 4.2 has 5 columns: Point ID / Energy Type / Image / Isolation Method / Location. No DANGER boxes. Sections 4.4 & 4.5 = flowcharts only.

**Section 5:** Sections 5.4 & 5.5 = flowcharts only. No functional safety performance table.

**Section 6:** Sections 6.4, 6.5, 6.7, 6.8, 6.9 = flowcharts only. No WARNING boxes in these.

**Section 11:** Section 11.4 = flowchart only.

**Section 12:** Section 12.2 = flowchart + max 5 bullet points. Section 12.5 = max 8 bullets only.

**Section 13:** Liability disclaimer — single instance here only. Sign-off blocks — once only at end. Sec 13.3 = role only, no name.

**Appendices:** A = Maintenance Log. B = LOTO Log. Nothing else. Residual Risk appendix permanently removed.

**DANGER boxes:** Never used anywhere.

**Placeholders:** `**[PLACEHOLDER — description, source, status]**` — bold, not italic.

---

## COMPLIANCE STANDARDS

| Standard | Where Applied |
|----------|--------------|
| ISO 12100:2010 | Section 3 — Hazard ID methodology |
| ISO 20607:2019 | Manual structure and content |
| IEC 82079-1:2019 | Instructions for use |
| IS 4571:2008 | Section 13 — Indian compliance |
| ISO 13849-1 | Section 12 — Safety control systems |
| ISO 13850 | Section 5 — Emergency stop |
| ANSI B11 | Referenced where applicable |
| Factories Act 1948 | Section 13 — Indian law |

**Excluded (do not reference):** IEC 61508, IEC 61800-5-2

**Standards hierarchy:** Type C → Type B (ISO 13857, 14120, 14119, 13855, 13849) → Type A (ISO 12100) → Regional

---

## OPEN ACTIONS REGISTER

Standalone `.xlsx` only — never inside the manual. 3 sheets.

| ID | Description | Category | Priority | Responsibility | Target Date | Status |
|----|-------------|----------|----------|----------------|-------------|--------|
| OA-P[n]-001 | | Safety Gap / Documentation / Schematic / Software / Maintenance | High/Med/Low | | | Open/Closed |

**Filename:** `[Client]_[MachineName]_OpenActions_V[x.x].xlsx`

---

## COMPLIANCE AUDIT CHECKLIST

Run after Step 2 (authoring), before Step 3 (generation).

- [ ] TOC: H1 only, single instance
- [ ] Revision table: 4 columns, no "Prepared By"
- [ ] Sec 1.6: role only, no name | Sec 1.9: not present
- [ ] No cover / Section 1 duplication
- [ ] Sec 3: ≤2 pages, narrative, no boxes, no tables
- [ ] Sec 4: Image column in Table 4.2 | No DANGER | 4.4 & 4.5 flowcharts
- [ ] Sec 5: 5.4 & 5.5 flowcharts | No functional safety table
- [ ] Sec 6: 6.4, 6.5, 6.7, 6.8, 6.9 flowcharts | No WARNING boxes
- [ ] Sec 11: 11.4 flowchart
- [ ] Sec 12: 12.2 flowchart + ≤5 bullets | 12.5 ≤8 bullets only
- [ ] Sec 13: Liability once | Sign-offs once | 13.3 role only
- [ ] Appendix A = Maintenance Log | Appendix B = LOTO Log | Nothing else
- [ ] Open Actions Register = standalone .xlsx only
- [ ] All flowcharts: blue borders, white bg, greyscale-readable
- [ ] Placeholders: bold text
- [ ] No DANGER boxes anywhere
- [ ] "Certified Safety Professional" — no individual name anywhere
- [ ] No SICK or RA firm names in document

---

## DELIVERABLES & FILENAMES

| File | Naming Convention |
|------|-------------------|
| Full Manual | `[EndUser]_[MachineName]_OSM_V1.0.docx` |
| Full Manual PDF | `[EndUser]_[MachineName]_OSM_V1.0.pdf` |
| Quick Reference (Tier A only) | `[EndUser]_[MachineName]_QR_V1.0.docx` |
| Open Actions Register | `[Client]_[MachineName]_OpenActions_V1.0.xlsx` |

**Versioning:** V1.0 = initial | V1.1 = post dry run | V2.0 = full release, all OAs closed

---

## WHAT NEVER TO DO

- ❌ Fabricate standard clause numbers
- ❌ Invent machine features or specs not in project data
- ❌ Use DANGER boxes anywhere
- ❌ Put liability disclaimer in Section 1
- ❌ Repeat sign-off blocks
- ❌ Repeat TOC
- ❌ Include individual name in author fields
- ❌ Include Appendix A Residual Risk — permanently removed
- ❌ Put Open Actions Register inside the manual
- ❌ Include full hazard table in Section 3
- ❌ Reference IEC 61508 or IEC 61800-5-2
- ❌ Name SICK or any RA firm in customer documents
- ❌ Apply DFM rules to non-Apple/non-Indo MIM projects
