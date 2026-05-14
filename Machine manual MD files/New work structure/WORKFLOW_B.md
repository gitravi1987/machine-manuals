# WORKFLOW_B.md — Code-Based Manual Creation
## Structured Input → Claude Code / Codex → .docx + .xlsx

**Owner:** Certified Safety Professional
**Use When:** Repeat projects, same machine type, template-based generation, speed priority
**Last Updated:** May 2026
**Formatting Spec:** `OSM_WORD_FORMAT_STANDARD_V1_2.md`

---

## STEP 1 — PREPARE INPUT FILES

Before running any code, prepare two structured input files. Use Claude chat or build manually.

### File 1: `machine_data.json`
```json
{
  "project_code": "P5",
  "end_user": "Company Name",
  "client": "Manufacturer Name",
  "machine_name": "Machine Name",
  "machine_ref": "V67",
  "site": "Facility, City, State",
  "tier": "A",
  "revision": "V1.0",
  "date": "May 2026",
  "loto_points": [
    {
      "id": "LP-01",
      "energy_type": "Electrical",
      "image_code": "IEC60417-5036",
      "isolation_method": "Main rotary disconnect",
      "location": "Right side panel"
    }
  ],
  "open_actions": [
    {
      "id": "OA-P5-001",
      "description": "",
      "category": "Documentation",
      "priority": "High",
      "responsibility": "Customer",
      "target_date": "TBD",
      "status": "Open"
    }
  ]
}
```

### File 2: `section_content.yaml`
```yaml
section_2:
  title: "Machine Overview"
  subsections:
    2_1:
      title: "Machine Identification"
      content: |
        [full approved content here]
    2_2:
      title: "Intended Use"
      content: |
        [full approved content here]

section_3:
  title: "Hazard Identification & Risk Assessment"
  content: |
    [narrative paragraphs — max 2 pages worth]
    [end with: Full hazard identification documented in Machine Safety Assessment Report [ref]]

# ... repeat for all sections
```

**Rule:** All content in these files must be fully reviewed and approved by Ravi before Step 2 runs. No LLM chat happens during generation.

---

## STEP 2 — GENERATE (Claude Code or Codex — No LLM Chat)

### Code Generation Brief
*(Paste at start of Claude Code / Codex session)*

```
CODE GENERATION BRIEF — [Project Code] [Machine Name]

Generate Operating & Safety Manual from structured input files.
Apply OSM_WORD_FORMAT_STANDARD_V1_2.md formatting throughout.

INPUT FILES:
- machine_data.json
- section_content.yaml

OUTPUT FILES (→ /mnt/user-data/outputs/):
- [EndUser]_[MachineName]_OSM_V1.0.docx
- [Client]_[MachineName]_OpenActions_V1.0.xlsx

TECHNICAL STACK:
- Word: Node.js docx library v9.6.1
- Excel: Python openpyxl
- Validation: python3 /mnt/skills/public/docx/scripts/office/validate.py

CODE RULES:
- Read /mnt/skills/public/docx/SKILL.md before writing any code
- Each section = standalone .js file
- Inject via Python content.replace() — NEVER str_replace for Unicode content
  (em-dashes and special symbols cause silent failures with str_replace)
- Validate after every section injection
- Extend bodyChildren array when adding sections beyond original stub count
- PageNumber.CURRENT inside TextRun — not new PageNumber()
- TOC requires manual refresh in Word after generation
  (right-click → Update Field → Update entire table)
- Working directory: /home/claude/
- Output directory: /mnt/user-data/outputs/

FORMATTING TO APPLY:

Page: A4, 25mm margins all sides

Typography:
- Calibri throughout — no exceptions
- H1: 14pt Bold #1F3864, page break before, bottom border 0.5pt
- H2: 13pt Bold #1F3864
- H3: 12pt Bold #1F3864
- Body: 11pt Regular #000000, space after 6pt, line spacing 1.15
- Table body: 10pt | Table header: 10pt Bold #FFFFFF

Colours:
- Heading: #1F3864
- Table header bg: #1F3864 | Alt rows: #D9E1F2 | Border: #1F3864 0.5pt

Alert boxes — NO DANGER BOXES:
- WARNING: bg #FFF2CC, full border 1pt #000000, padding 8pt
- CAUTION: bg #FCE4D6, left border 3pt #FF6600, padding 8pt
- NOTICE: bg #F2F2F2, left border 2pt #000000, padding 8pt
- OPEN ACTION: bg #FCE4D6, left border 3pt #FF0000, padding 8pt

Placeholders:
- bg #F7F7F7, left border 2pt #AAAAAA
- Text: Bold 11pt #000000
- Format: [PLACEHOLDER — description, source, status]

Flowcharts (sections 4.4, 4.5, 5.4, 5.5, 6.4, 6.5, 6.7, 6.8, 6.9, 11.4, 12.2):
- Pill terminals: fill #1F3864, text #FFFFFF
- Process steps: fill #FFFFFF, border #1F3864, text #1F3864
- Sub-actions: fill #D9E1F2, border #1F3864
- Decisions: fill #FFFFFF, border #1F3864
- Arrows: #1F3864, 1pt
- Max 10 steps | Action verb first | ≤10 words per step
- Must pass greyscale print test

Header (all pages except cover):
- Left: machine name | Centre: Operating & Safety Manual | Right: Page N of N
- Font: Calibri 9pt #1F3864 | Separator: #1F3864 0.5pt below

Footer: CONFIDENTIAL centre, Calibri 9pt bold #555555
Cover: no header/footer, logo top-centre, titles #1F3864

TOC:
- H1 entries only — no H2 sub-entries
- Single instance on pages 3–4 — never generate a second TOC
- Font: Calibri 11pt | Heading: 14pt bold #1F3864 centred

Revision table (page 2):
- 4 columns only: Revision | Date | Description | Reviewed By
- No "Prepared By" column

Section 4 Table 4.2 — 5 columns:
  Point ID | Energy Type | Image (ISO pictogram 20×20mm SVG) | Isolation Method | Location
  Column widths: 10% / 15% / 10% / 35% / 30%

Author field everywhere: "Certified Safety Professional" — no individual name

Appendices:
- Appendix A: Maintenance Log Template (blank table, 10 rows minimum)
- Appendix B: LOTO Log Template (blank table, 10 rows minimum)
- No other appendices
```

---

## STEP 3 — REVIEW (Claude Chat)

After generation, open Claude chat and upload the generated `.docx`. Run the compliance checklist below. Fix issues in source files and regenerate — do not patch the Word file manually.

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

Run this before preparing input files. Confirm tier before writing content.

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

**Section 1:** TOC H1 only, single instance pages 3–4, never repeated. Revision table 4 columns. Sec 1.6 role only. Sec 1.9 removed. Liability NOT here.

**Section 3:** Max 2 pages. Narrative only. No tables. No WARNING/DANGER boxes. End with RA report reference.

**Section 4:** Table 4.2 = 5 columns with Image column. No DANGER. Sections 4.4 & 4.5 = flowcharts.

**Section 5:** Sections 5.4 & 5.5 = flowcharts. No functional safety performance table.

**Section 6:** Sections 6.4, 6.5, 6.7, 6.8, 6.9 = flowcharts. No WARNING boxes.

**Section 11:** Section 11.4 = flowchart.

**Section 12:** Section 12.2 = flowchart + ≤5 bullets. Section 12.5 = ≤8 bullets only.

**Section 13:** Liability single instance here only. Sign-offs once only at end. Sec 13.3 role only.

**Appendices:** A = Maintenance Log. B = LOTO Log. Nothing else.

**DANGER boxes:** Never used. **Placeholders:** Bold text only.

---

## COMPLIANCE STANDARDS

| Standard | Where Applied |
|----------|--------------|
| ISO 12100:2010 | Section 3 |
| ISO 20607:2019 | Manual structure |
| IEC 82079-1:2019 | Instructions for use |
| IS 4571:2008 | Section 13 |
| ISO 13849-1 | Section 12 |
| ISO 13850 | Section 5 |
| ANSI B11 | Referenced where applicable |
| Factories Act 1948 | Section 13 |

**Excluded:** IEC 61508, IEC 61800-5-2

---

## OPEN ACTIONS REGISTER

Standalone `.xlsx` only. 3 sheets. Never inside the manual.

| ID | Description | Category | Priority | Responsibility | Target Date | Status |
|----|-------------|----------|----------|----------------|-------------|--------|
| OA-P[n]-001 | | Safety Gap / Documentation / Schematic / Software / Maintenance | High/Med/Low | | | Open/Closed |

**Filename:** `[Client]_[MachineName]_OpenActions_V[x.x].xlsx`

---

## COMPLIANCE AUDIT CHECKLIST

Run in Step 3 after generation. Fix in source files and regenerate if anything fails.

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
- ❌ Patch the Word file manually — fix source files and regenerate
- ❌ Apply DFM rules to non-Apple/non-Indo MIM projects
