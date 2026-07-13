# WORKFLOW_B.md — Code-Based Manual Creation
## Raw Inputs → Claude Code Drafts → You Approve → .docx + .xlsx

**Owner:** Certified Safety Professional
**Use When:** Claude Code / VS Code session — any new or repeat project
**Last Updated:** May 2026
**Formatting Spec:** `OSM_WORD_FORMAT_STANDARD_V1_2.md`

---

## OVERVIEW — How This Workflow Works

```
YOUR RAW INPUTS
(RA report, drawings, photos, questionnaire)
        ↓
STEP 1 — Claude Code reads inputs, asks gap questions,
         drafts section content, builds machine_data.json
         + section_content.yaml
        ↓
STEP 2 — You review and approve both files
        ↓
STEP 3 — Claude Code generates .docx + .xlsx
        ↓
STEP 4 — Compliance review. Fix in source, regenerate.
```

**Key rule:** No .docx is generated until you have approved the content in Step 2.
**No LLM chat happens during Step 3** — pure code execution only.

---

## STEP 1 — INGEST INPUTS & DRAFT CONTENT (Claude Code)

### What you bring to every project

**Mandatory:**
- Risk Assessment report (PDF) — from Independent Safety Consultant
- Drawing files — GA drawing, electrical schematic, pneumatic schematic
- Site photographs — see Photo Checklist below

**Standard questionnaire (fill what you have, leave rest blank):**
Four standard intake forms — provide answers to any/all that are available:

| Form | What it covers |
|------|---------------|
| Machine Data | Machine name, model, serial, year, power, voltage, air pressure, PLC/HMI, cycle time, stations, operator count |
| Documents & Drawings | What documents are available (RA ✅, schematics ✅/partial/❌, PLC backup, HMI alarm list, SOP, OEM manual) |
| Safety & Operation Inputs | LOTO points, safety devices, guarding, PPE, startup/shutdown procedures, maintenance details, operator interview notes |
| Site Photographs Checklist | Which photos were taken (full machine views, control panel, e-stop, LOTO isolators, hazard zones, nameplate) |

**Optional (if available):**
- Completed questionnaire answers in any format (typed notes, voice-to-text, WhatsApp messages — anything)
- OEM manual
- HMI alarm list
- Maintenance schedule
- Operator interview notes

> **If you have a `section_outline.yaml` from ChatGPT** (from a Workflow A session or generated separately), you can upload it as an optional input. Claude Code will use it as the structural skeleton and populate it from your raw inputs. This is optional — not required.

---

### What Claude Code does in Step 1

After receiving all available inputs, Claude Code will:

1. **Extract** all machine data from the RA report, drawings, questionnaire answers, and photos
2. **Identify gaps** — any data needed for the manual that is not in the inputs
3. **Ask you gap questions** — one pass, list all gaps together, not one at a time
4. **Confirm tier** (A / B / C) based on available data
5. **Draft all section content** — full text for every section, compliant with all structural rules
6. **Build two output files:**
   - `machine_data.json` — machine metadata, LOTO points, open actions
   - `section_content.yaml` — full drafted manual content, section by section

**Gap handling rule:** If data is missing and you cannot answer, Claude Code marks it as:
`**[PLACEHOLDER — description, source, status]**`
or logs it as an Open Action. **Never invented or assumed.**

---

### `machine_data.json` — structure

```json
{
  "project_code": "P5",
  "end_user": "Company Name",
  "client": "Manufacturer Name",
  "machine_name": "Machine Name",
  "machine_ref": "Internal ref if any",
  "site": "Facility Name, City, State",
  "tier": "A",
  "revision": "V1.0",
  "date": "Month Year",
  "loto_points": [
    {
      "id": "LP-01",
      "energy_type": "Electrical",
      "image_code": "IEC60417-5036",
      "isolation_method": "Main rotary isolator switch",
      "location": "Right side of control panel"
    },
    {
      "id": "LP-02",
      "energy_type": "Pneumatic",
      "image_code": "ISO7010-M004",
      "isolation_method": "Quarter-turn ball valve with lockout hasp",
      "location": "Rear of machine, air inlet"
    }
  ],
  "open_actions": [
    {
      "id": "OA-P5-001",
      "description": "Motor nameplate rating not confirmed on site — verify kW and RPM",
      "category": "Documentation",
      "priority": "High",
      "responsibility": "Customer",
      "target_date": "TBD",
      "status": "Open"
    }
  ]
}
```

---

### `section_content.yaml` — structure

```yaml
section_2:
  title: "Machine Overview"
  subsections:
    2_1:
      title: "Machine Identification"
      content: |
        [Full drafted text here — extracted from RA + questionnaire + photos]
    2_2:
      title: "Intended Use"
      content: |
        [Full drafted text here]
    2_3:
      title: "Key Technical Specifications"
      content: |
        [Full drafted text here — or PLACEHOLDER if nameplate data missing]

section_3:
  title: "Hazard Identification & Risk Assessment"
  content: |
    [Narrative paragraphs — max 2 pages. No tables. No boxes.
     End with: Full hazard identification is documented in the
     Machine Safety Assessment Report [ref].]

section_4:
  title: "Lockout / Tagout (LOTO) Procedures"
  subsections:
    4_1:
      title: "Purpose and Scope"
      content: |
        [drafted text]
    4_2:
      title: "Energy Isolation Points"
      content: |
        [Table 4.2 populated from loto_points in machine_data.json]
        [5 columns: Point ID / Energy Type / Image / Isolation Method / Location]
    4_3:
      title: "Required LOTO Equipment"
      content: |
        [drafted text]
    4_4:
      title: "Tag-Out Procedure"
      content: FLOWCHART
    4_5:
      title: "Tag-In Procedure"
      content: FLOWCHART

# ... sections 5 through 13 follow same pattern
# Sections 5.4, 5.5, 6.4, 6.5, 6.7, 6.8, 6.9, 11.4, 12.2 = FLOWCHART
# Section 3 = narrative only, max 2 pages, no boxes or tables
# Section 13 = liability disclaimer here only
```

---

## STEP 2 — YOU REVIEW & APPROVE

Before any code runs, you must review both files:

**Review checklist:**
- [ ] All machine specs correct (nameplate data, power, pressure, dimensions)
- [ ] LOTO points match actual machine configuration
- [ ] Section 3 is narrative only, ≤2 pages worth of content, no tables
- [ ] All PLACEHOLDERs either filled in or confirmed as Open Actions
- [ ] Open Actions list is complete — nothing safety-critical is missing
- [ ] Tier confirmed (A / B / C) — sections included match tier map below
- [ ] No individual names anywhere — "Certified Safety Professional" only
- [ ] No SICK or RA firm names — "Independent Safety Consultant" only

**Only after your approval does Step 3 run.**

---

## STEP 3 — GENERATE (Claude Code — No LLM Chat)

### Before writing any code, Claude Code must read:
- `/mnt/skills/public/docx/SKILL.md` — mandatory before any Word generation
- `/mnt/skills/public/xlsx/SKILL.md` — mandatory before Open Actions Register

### Code Generation Brief
*(Claude Code uses this automatically — no need to paste manually if CLAUDE.md is loaded)*

```
CODE GENERATION BRIEF

INPUT FILES:
- Projects/Pxx-name/inputs/machine_data.json
- Projects/Pxx-name/inputs/section_content.yaml

OUTPUT FILES → Projects/Pxx-name/outputs/:
- [EndUser]_[MachineName]_OSM_V1.0.docx
- [Client]_[MachineName]_OpenActions_V1.0.xlsx

TECHNICAL STACK:
- Word: Node.js docx library v9.6.1
- Excel: Python openpyxl
- Validation: python3 /mnt/skills/public/docx/scripts/office/validate.py

CODE RULES:
- Each section = standalone .js file in working/ folder
- Inject via Python content.replace() — NEVER str_replace for Unicode content
  (em-dashes and special symbols cause silent failures)
- Validate after every section injection
- Extend bodyChildren array when adding sections beyond original stub count
- PageNumber.CURRENT inside TextRun children array — not new PageNumber()
- TOC requires manual refresh in Word (right-click → Update Field → Update entire table)
- Sections 8–10 can be combined into one .js file, injected at Section 10 placeholder
- Working directory: Projects/Pxx-name/working/
- Output directory: Projects/Pxx-name/outputs/
```

---

## STEP 4 — COMPLIANCE REVIEW (Claude Code or Claude Chat)

After generation, run the compliance checklist. **Fix issues in source files and regenerate — never patch the .docx manually.**

- [ ] TOC: H1 entries only, single instance on pages 3–4, never repeated
- [ ] Revision table: 4 columns only — Revision / Date / Description / Reviewed By. No "Prepared By"
- [ ] Sec 1.6: role only, no individual name | Sec 1.9: not present
- [ ] Cover and Section 1 not duplicated
- [ ] Sec 3: ≤2 pages, narrative only, no WARNING/DANGER boxes, no tables
- [ ] Sec 4: Table 4.2 has Image column | No DANGER boxes | 4.4 & 4.5 = flowcharts
- [ ] Sec 5: 5.4 & 5.5 = flowcharts | No functional safety performance table
- [ ] Sec 6: 6.4, 6.5, 6.7, 6.8, 6.9 = flowcharts | No WARNING boxes in these
- [ ] Sec 11: 11.4 = flowchart
- [ ] Sec 12: 12.2 = flowchart + ≤5 bullets | 12.5 = ≤8 bullets only
- [ ] Sec 13: Liability disclaimer once only | Sign-off blocks once only | 13.3 role only
- [ ] Appendix A = Maintenance Log Template | Appendix B = LOTO Log Template | Nothing else
- [ ] Open Actions Register = standalone .xlsx — NOT inside the manual
- [ ] All flowcharts: blue borders #1F3864, white bg, greyscale-readable, ≤10 steps
- [ ] All placeholders: bold text format
- [ ] No DANGER boxes anywhere in the document
- [ ] "Certified Safety Professional" — no individual name anywhere
- [ ] No SICK or any RA firm name anywhere

---

## TIER SCOPING (Confirm Before Step 1)

| Question | Yes | No |
|----------|-----|----|
| Risk assessment available? | Continue | Recommend RA first (+₹20k–40k, 2–3 weeks) |
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

**Section 1:** TOC = H1 only, single instance pages 3–4, never repeated. Revision table = 4 columns only. Sec 1.6 = role only, no name. Sec 1.9 = removed permanently. Liability NOT in Section 1.

**Section 3:** Max 2 pages. Narrative paragraphs only. No tables. No WARNING or DANGER boxes. End with reference to Machine Safety Assessment Report.

**Section 4:** Table 4.2 = 5 columns (Point ID / Energy Type / Image / Isolation Method / Location). No DANGER boxes. Sections 4.4 & 4.5 = flowcharts only.

**Section 5:** Sections 5.4 & 5.5 = flowcharts only. No functional safety performance table.

**Section 6:** Sections 6.4, 6.5, 6.7, 6.8, 6.9 = flowcharts only. No WARNING boxes in these subsections.

**Section 11:** Section 11.4 = flowchart only.

**Section 12:** Section 12.2 = flowchart + max 5 bullet points. Section 12.5 = max 8 bullets only.

**Section 13:** Liability disclaimer — single instance here only. Sign-off blocks — once only, at end. Sec 13.3 = role only, no name.

**Appendices:** A = Maintenance Log Template. B = LOTO Log Template. Nothing else. Residual Risk appendix permanently removed.

**DANGER boxes:** Never used anywhere. **Placeholders:** Bold text only — `**[PLACEHOLDER — description, source, status]**`

---

## OPEN ACTIONS REGISTER

Standalone `.xlsx` only — never inside the manual. 3 sheets.

| ID | Description | Category | Priority | Responsibility | Target Date | Status |
|----|-------------|----------|----------|----------------|-------------|--------|
| OA-P[n]-001 | | Safety Gap / Documentation / Schematic / Software / Maintenance | High/Med/Low | | | Open/Closed |

**Filename:** `[Client]_[MachineName]_OpenActions_V1.0.xlsx`

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

**Excluded — do not reference:** IEC 61508, IEC 61800-5-2

---

## DELIVERABLES & FILENAMES

| File | Naming Convention |
|------|-------------------|
| Full Manual | `[EndUser]_[MachineName]_OSM_V1.0.docx` |
| Full Manual PDF | `[EndUser]_[MachineName]_OSM_V1.0.pdf` |
| Quick Reference (Tier A only) | `[EndUser]_[MachineName]_QR_V1.0.docx` |
| Open Actions Register | `[Client]_[MachineName]_OpenActions_V1.0.xlsx` |

**Versioning:** V1.0 = initial delivery | V1.1 = post dry-run fixes | V2.0 = full release, all OAs closed

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

## WHAT NEVER TO DO

- ❌ Generate .docx before Ravi approves section_content.yaml
- ❌ Fabricate standard clause numbers
- ❌ Invent machine features or specs not present in input files or RA report
- ❌ Use DANGER boxes anywhere
- ❌ Put liability disclaimer in Section 1
- ❌ Repeat sign-off blocks or TOC
- ❌ Include any individual person's name in author or role fields
- ❌ Include Appendix A Residual Risk — permanently removed
- ❌ Put Open Actions Register inside the manual
- ❌ Include full hazard register table in Section 3
- ❌ Reference IEC 61508 or IEC 61800-5-2
- ❌ Name SICK or any RA firm in customer-facing documents
- ❌ Patch the generated .docx manually — fix source files and regenerate
- ❌ Apply DFM rules to non-Apple / non-Indo-MIM projects
- ❌ Use str_replace to inject Unicode content into .js files
