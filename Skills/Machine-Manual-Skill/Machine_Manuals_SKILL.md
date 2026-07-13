---
name: machine-manuals
description: >
  Use this skill for ANY task related to creating, structuring, drafting, reviewing, or generating
  Operating & Safety Manuals for industrial machinery. Triggers include: starting a new manual project,
  scoping a tier (A/B/C), drafting any manual section (LOTO, E-Stop, Hazard ID, Operating Instructions,
  Maintenance, Schematics), performing a compliance audit, generating Word (.docx) or Excel (.xlsx)
  deliverables, building an Open Actions Register, writing quick reference documents, or reviewing
  content against ISO 12100, ISO 20607, IEC 82079-1, IS 4571, ISO 13849-1, ISO 13850, or ANSI B11.
  Also triggers when Ravi mentions: "new project", "new customer", "site visit data ready",
  "risk assessment uploaded", "P5", "P6" (or any new project code), "draft section", "generate manual",
  "Open Actions", "LOTO section", "maintenance schedule", or any machine name. Apply this skill even
  when Ravi just describes a machine or customer situation — recognise the pattern and engage immediately.
---

# Machine Manuals Skill
**Version:** 2.0 — May 2026
**Formatting Authority:** OSM_WORD_FORMAT_STANDARD_V1_2.md (supersedes all older formatting rules)
**Workflow Authority:** WORKFLOW_A.md (chat-based) | WORKFLOW_B.md (code-based)

> **Conflict rule:** If anything in this skill conflicts with OSM_WORD_FORMAT_STANDARD_V1_2.md,
> follow the format standard. It is the master authority.

Ravikumar is a Certified Safety Professional running an independent technical documentation
consultancy in Chennai, India. This skill encodes the complete workflow for creating
ISO/IEC/ANSI-compliant Operating & Safety Manuals for industrial machinery clients.

---

## QUICK ORIENTATION

Before doing anything, establish:
1. **New project or continuation?** New → Phase 1 intake. Continuation → confirm project code + current phase.
2. **Project code?** P1–P4 complete. New projects are P5+.
3. **Mode?** Standard OSM project → this skill. Indo-MIM/Apple/Tata Electronics → also load DFM.md.
4. **Which workflow?** New/complex/first draft → Workflow A. Repeat/template/speed → Workflow B.
5. **Documents uploaded?** RA report, drawings, checklist, photos.
6. **Task?** Scope tier / Draft section / Compliance audit / Generate Word file.

If any of these are unclear, **ask before proceeding. Never assume.**

---

## SECTION 1: WORKFLOW SELECTION

### Workflow A — Chat-Based (New / Complex Projects)
**Use when:** First draft of a new machine, complex machine, heavy iteration expected.

```
Step 1 — STRUCTURE (ChatGPT):     Machine data + RA → YAML outline → section_outline.yaml
Step 2 — AUTHOR (Claude chat):    One conversation. Section by section. Confirm before next.
Step 3 — GENERATE (Claude chat,   .docx via Node.js docx 9.6.1 + .xlsx via Python openpyxl
          new conversation):
```

Full prompt templates → WORKFLOW_A.md

### Workflow B — Code-Based (Repeat / Template Projects)
**Use when:** Same machine type repeated, template-based generation, speed is priority.

```
Step 1 — PREPARE:   Build machine_data.json + section_content.yaml (fully reviewed content)
Step 2 — GENERATE:  Claude Code or Codex — no LLM chat during generation
Step 3 — REVIEW:    Claude chat compliance audit. Fix in source files + regenerate.
                    Never patch Word manually.
```

Full code generation brief and input file templates → WORKFLOW_B.md

### Critical Rules (Both Workflows)
- All content drafted and approved before generation starts
- Draft in ONE conversation; generate in a NEW conversation
- Fixes go into source files and regenerate — never manually patch the .docx
- Do NOT upload RA reports or drawings to multiple LLMs unnecessarily

---

## SECTION 2: PROJECT REGISTRY

| Code | Client | Machine | Tier | Status |
|------|--------|---------|------|--------|
| P1 | Accurate Machines | 48-Spindle Drilling Machine | A | ✅ Complete — **no coolant system** |
| P2 | KEMC / Valeo | Tilting Machine (Clutch Plate) | B | ✅ Complete |
| P3 | Valeo | LE Test Bench | A | ✅ Complete |
| P4 | Indo-MIM / Tata Electronics | BG Snap Assembly Machine (V67) | A | ✅ Complete |
| P5+ | TBD | TBD | TBD | Follow Phase 1 intake |

**P1 permanent note:** The Accurate Machines 48-spindle drilling machine has NO coolant system.
Any coolant reference in that manual is an error and must be removed if P1 is ever revised.

**Designation rule:** Always use "Certified Safety Professional" — never "B11 LMSS Licensed
Machinery Safety Specialist" or any variant in customer-facing documents.

**Author field rule:** Role only — "Certified Safety Professional". No individual name anywhere.

**Third-party branding rule:** Never reference SICK or any RA firm by name in customer-facing
documents. Use "Independent Safety Consultant" or "Machine Safety Assessment" instead.

---

## SECTION 3: TIER SCOPING

Run this before starting any project. Confirm tier with Ravi before writing a single word.

### Decision Matrix

| Question | Yes | No |
|----------|-----|----|
| Risk assessment (RA) available? | Continue | Recommend commissioning RA first (+₹20k–40k, 2–3 weeks) |
| Full schematics (electrical/pneumatic/hydraulic) available? | → Tier A candidate | → Tier B/C |
| Control system docs (PLC/HMI backup) available? | → Tier A candidate | → Tier B/C |
| Machine age < 10 years, active maintenance? | → Tier A/B | → Tier B/C |
| Operating procedures formally documented? | → Tier A/B | → Tier B/C |

### Tier Summary

| Tier | Situation | Pages | Hard Limit | Price | Timeline |
|------|-----------|-------|------------|-------|----------|
| A | Full RA + schematics + PLC docs + photos | 40–60 | 60 | ₹15k–20k | 14–21 days |
| B | RA + partial schematics + informal procedures | 25–40 | 40 | ₹10k–12k | 10–14 days |
| C | RA only, no schematics, legacy machine | 15–25 | 25 | ₹8k–10k | 7–10 days |

**Page count rule:** Manuals must be lean. Cut non-essential/repetitive content.
Never cut safety-critical content.

---

## SECTION 4: STANDARD MANUAL STRUCTURE

### Document Page Order
```
PAGE 1     — Cover Page (no header/footer)
PAGE 2     — Revision History
PAGE 3–4   — Table of Contents (H1 only — single instance — never repeated)
PAGE 5+    — Section 1: Front Matter
PAGE 6+    — Sections 2–13
FINAL      — Appendix A: Maintenance Log Template
           — Appendix B: LOTO Log Template
```

### Section Map by Tier

| Sec | Title | Tier A | Tier B | Tier C |
|-----|-------|--------|--------|--------|
| 1 | Front Matter (Scope, Audience, Definitions, Signal Words) | ✅ | ✅ | ✅ |
| 2 | Machine Overview | ✅ | ✅ | ✅ |
| 3 | Hazard ID — narrative, max 2 pages | ✅ | ✅ | ✅ Abbreviated |
| 4 | LOTO Procedures | ✅ | ✅ | ✅ |
| 5 | Emergency Stop | ✅ | ✅ | ✅ |
| 6 | Operating Instructions | ✅ | ✅ | ✅ |
| 7 | Maintenance & Care | ✅ | ✅ Partial | ✅ Abbreviated |
| 8 | Electrical Schematic | ✅ | ⚠️ Placeholder | ❌ Omit |
| 9 | Pneumatic Schematic | ✅ | ⚠️ Placeholder | ❌ Omit |
| 10 | Hydraulic Schematic | ✅ If applicable | ⚠️ Placeholder | ❌ Omit |
| 11 | HMI Alarms & Fault Codes | ✅ If applicable | ⚠️ If data available | ❌ N/A |
| 12 | Safety Features & Interlocks | ✅ | ✅ Streamlined | ✅ Abbreviated |
| 13 | Compliance & Certifications | ✅ | ✅ | ✅ |
| Appendix A | Maintenance Log Template | ✅ | ✅ | ✅ |
| Appendix B | LOTO Log Template | ✅ | ✅ | ✅ |
| Open Actions Register | Standalone .xlsx only — never in manual | ✅ | ✅ | ✅ |

---

## SECTION 5: NON-NEGOTIABLE CONTENT RULES

### Structure Rules
1. **TOC:** H1 entries only. Single instance pages 3–4. Never repeated.
2. **Revision table:** 4 columns only — Revision / Date / Description / Reviewed By. No "Prepared By".
3. **Section 1.6:** "Certified Safety Professional" — no individual name.
4. **Section 1.9:** Permanently removed. No ISO 7010 sign reference table in Section 1.
5. **Section 3:** Maximum 2 pages. Narrative only. No tables, no WARNING boxes, no DANGER boxes.
   End with: *"Full hazard identification and risk assessment is documented in the Machine Safety
   Assessment Report [reference and date]."*
6. **Section 4 Table 4.2:** 5 columns — Point ID / Energy Type / Image (ISO energy pictogram
   20×20mm) / Isolation Method / Location.
7. **Section 13:** Liability disclaimer appears here ONLY — never in Section 1 or cover page.
8. **Sign-off blocks:** Single instance only at the end of Section 13. Never repeated.
9. **Section 13.3:** Role only — no individual name.
10. **Appendices:** Two only — A = Maintenance Log Template, B = LOTO Log Template. Nothing else.

### Permanently Removed
- ❌ Appendix — Residual Risk Summary (permanently removed; customer has the RA report)
- ❌ DANGER boxes (removed from entire template, May 2026)
- ❌ Liability disclaimer on cover page or in Section 1
- ❌ "Prepared By" column in revision table
- ❌ Section 1.9 ISO 7010 sign reference table
- ❌ Functional safety performance table (Section 5)
- ❌ Individual name in any author field
- ❌ Full hazard register table in Section 3 body
- ❌ Open Actions Register inside the manual
- ❌ IEC 61508 and IEC 61800-5-2 references
- ❌ Google Antigravity

### Content Integrity
- **Never invent** machine features, specs, or systems not in the project data.
  Missing data → `**[PLACEHOLDER — description, source, status]**` or Open Action.
- **Placeholders:** Bold black text — `**[PLACEHOLDER — description, source, status]**`
  Not italic, not grey. Changed to bold in V1.2.
- **LOTO and E-stop procedures must be self-contained.** Operators must never need to
  cross-reference another section for a safety-critical step.
- **Quick reference documents must be fully self-contained.** Full sequences only.
  No "refer to Section X."

### Flowchart-Only Sub-Sections
These sub-sections use flowcharts only — no prose, no WARNING boxes:

| Section | Topic | Max Steps |
|---------|-------|-----------|
| 4.4 | LOTO Tag-Out | 8 |
| 4.5 | LOTO Tag-In | 8 |
| 5.4 | E-Stop activation | 6 |
| 5.5 | E-Stop reset | 6 |
| 6.4 | Pre-start checks | 8 |
| 6.5 | Startup sequence | 8 |
| 6.7 | Normal operating cycle | 10 |
| 6.8 | Shutdown sequence | 6 |
| 6.9 | Emergency shutdown | 6 |
| 11.4 | Alarm response | 10 |
| 12.2 | Safety function overview | 10 |

Section 12.5 = bullet points only, max 8. No flowchart.

---

## SECTION 6: FORMATTING SPECIFICATION

Full detail in OSM_WORD_FORMAT_STANDARD_V1_2.md. Summary below.

### Page Setup
A4 portrait. 25mm margins all sides. Header 12mm from edge. Footer 12mm from edge.
Each section starts on a new page (page break before every H1).

### Typography — Calibri throughout, no exceptions

| Element | Size | Weight | Colour |
|---------|------|--------|--------|
| Document title (cover) | 22pt | Bold | #1F3864 |
| Machine name (cover) | 18pt | Bold | #1F3864 |
| H1 | 14pt | Bold | #1F3864 |
| H2 | 13pt | Bold | #1F3864 |
| H3 | 12pt | Bold | #1F3864 |
| Body | 11pt | Regular | #000000 |
| Table body | 10pt | Regular | #000000 |
| Table header | 10pt | Bold | #FFFFFF |
| Caption | 10pt | Italic | #555555 |
| Placeholder | 11pt | **Bold** | #000000 |
| Header | 9pt | Regular | #1F3864 |
| Footer | 9pt | Regular | #555555 |

### Paragraph Spacing

| Element | Before | After | Line Spacing |
|---------|--------|-------|--------------|
| H1 | 18pt | 6pt | Single |
| H2 | 12pt | 4pt | Single |
| H3 | 8pt | 4pt | Single |
| Body | 0pt | 6pt | 1.15 |
| Table cell | 0pt | 0pt | Single |
| List item | 0pt | 4pt | Single |

### Alert Boxes

> **DANGER boxes are NOT used. Removed May 2026. Do not generate under any circumstance.**

| Box Type | Background | Border | Label Format |
|----------|-----------|--------|--------------|
| WARNING | #FFF2CC | Full 1pt #000000 | ⚠️ WARNING [ISO 7010 — Wxxx] |
| CAUTION | #FCE4D6 | Left 3pt #FF6600 | ⚡ CAUTION |
| NOTICE | #F2F2F2 | Left 2pt #000000 | 📋 NOTICE |
| OPEN ACTION | #FCE4D6 | Left 3pt #FF0000 | ⚠️ OPEN ACTION [OA-Pn-xxx] |
| PLACEHOLDER | #F7F7F7 | Left 2pt #AAAAAA | **Bold text** |

### Table Colours
Header: #1F3864 background, #FFFFFF text, 10pt Bold, centred.
Rows: alternating #FFFFFF / #D9E1F2. Border: 0.5pt #1F3864 all sides.
Cell padding: 4pt top/bottom, 6pt left/right.

### Flowchart Colours

| Shape | Fill | Border | Text |
|-------|------|--------|------|
| Start/End pill (rx=19) | #1F3864 | #1F3864 | #FFFFFF |
| Process step (rx=6) | #FFFFFF | #1F3864 | #1F3864 |
| Sub-action (rx=6) | #D9E1F2 | #1F3864 | #1F3864 |
| Decision diamond | #FFFFFF | #1F3864 | #1F3864 |
| Arrows | #1F3864 1pt | — | — |

Direction: top to bottom. Step text: action verb first, ≤10 words per step.
Must pass greyscale print test. Split into two if more than 10 steps needed.

### Header & Footer
- Header (all pages except cover): Machine name (L) | Operating & Safety Manual (C) | Page N of N (R)
  Separator: single line below, #1F3864 0.5pt.
- Footer: CONFIDENTIAL — centre, Calibri 9pt bold #555555.
  Separator: single line above, #CCCCCC 0.5pt.
- Cover page: no header, no footer. Page numbering starts from page 2.

### ISO 7010 Safety Signs
Inline only at the exact procedural step where hazard exists. Never at section headers. 20×20mm.

| Code | Hazard |
|------|--------|
| W001 | General warning |
| W003 | Crushing hazard |
| W017 | Electrical hazard |
| W019 | Automatic start-up |
| W028 | Entanglement |
| P002 | Do not touch |
| P010 | Do not switch on |
| M008 | Wear gloves |
| M009 | Wear safety footwear |

### Image & Placeholder
Actual image: max 160mm wide, centred, 0.5pt #CCCCCC border. Caption: Figure [N]: [Description].
Placeholder: #F7F7F7 background, left border 2pt #AAAAAA.
Caption: **[PLACEHOLDER — description, source, status]** — Bold 11pt #000000.

---

## SECTION 7: OPEN ACTIONS REGISTER

Standalone `.xlsx` only — **never inside the manual body**.

**3 sheets:**
- Sheet 1 — Full Register
- Sheet 2 — Summary by Category
- Sheet 3 — Revision History

**Sheet 1 columns:**

| ID | Description | Category | Priority | Responsibility | Target Date | Status | Notes |
|----|-------------|----------|----------|----------------|-------------|--------|-------|
| OA-P[n]-001 | | Safety Gap / Documentation / Schematic / Software / Maintenance | High/Med/Low | Customer/Engineer | TBD | Open/Closed | |

**Filename:** `[Client]_[MachineName]_OpenActions_V[x.x].xlsx`

---

## SECTION 8: COMPLIANCE STANDARDS

| Standard | Where Applied |
|----------|--------------|
| ISO 12100:2010 | Section 3 — Hazard ID methodology |
| ISO 20607:2019 | Manual structure and content |
| IEC 82079-1:2019 | Instructions for use — quality and competence |
| IS 4571:2008 | Section 13 — Indian machinery safety |
| ISO 13849-1 | Section 12 — Safety control systems |
| ISO 13850 | Section 5 — Emergency stop |
| ANSI B11 | Referenced where applicable |
| Factories Act 1948 | Section 13 — Indian industrial law |

**Excluded — do not reference:** IEC 61508, IEC 61800-5-2

**Standards hierarchy (highest to lowest):**
Type C (machine-specific) → Type B (ISO 13857, 14120, 14119, 13855, 13849, IEC 62061) → Type A (ISO 12100) → Regional

---

## SECTION 9: WORD GENERATION — TECHNICAL STACK

- **Word (.docx):** Node.js `docx` library v9.6.1
- **Excel (.xlsx):** Python `openpyxl`
- **Validation:** `python3 /mnt/skills/public/docx/scripts/office/validate.py` after every section
- **Working directory:** `/home/claude/`
- **Output directory:** `/mnt/user-data/outputs/`

### Code Rules
1. Read `/mnt/skills/public/docx/SKILL.md` before writing any code — mandatory first step
2. Each section = standalone `.js` file
3. Inject via Python `content.replace(placeholder, new_code)` — **never `str_replace` for Unicode**
   (em-dashes and special symbols cause silent failures with str_replace)
4. Validate after every section injection
5. Sections 8+9+10 can share one file; inject at last section placeholder; stub earlier ones
6. `bodyChildren` array must be explicitly extended when adding sections beyond original stub count
7. `PageNumber.CURRENT` inside `TextRun` children — not `new PageNumber()`
8. TOC requires manual refresh in Word after generation
   (right-click → Update Field → Update entire table)

### Filenames & Versioning

| File | Convention |
|------|------------|
| Manual | `[EndUser]_[MachineName]_OSM_V[n.n].docx` |
| Manual PDF | `[EndUser]_[MachineName]_OSM_V[n.n].pdf` |
| Quick Reference (Tier A) | `[EndUser]_[MachineName]_QR_V[n.n].docx` |
| Open Actions | `[Client]_[MachineName]_OpenActions_V[n.n].xlsx` |

| Version | Trigger |
|---------|---------|
| V1.0 | Initial — placeholders in, all OAs open |
| V1.1 | Post dry run — site items updated |
| V2.0 | Full release — all OAs closed, sign-off complete |

---

## SECTION 10: COMPLIANCE AUDIT CHECKLIST

Run before generation (Workflow A) or after generation (Workflow B).
Fix in source files and regenerate — never patch manually in Word.

**Document Structure:**
- [ ] TOC: H1 only, single instance pages 3–4, never repeated
- [ ] Revision table: 4 columns only, no "Prepared By"
- [ ] Cover: no header/footer, no individual name
- [ ] No duplication between cover and Section 1

**Section-Level:**
- [ ] Sec 1.6: "Certified Safety Professional" — no individual name
- [ ] Sec 1.9: not present
- [ ] Sec 3: ≤2 pages, narrative only, no tables, no WARNING/DANGER boxes, ends with RA reference
- [ ] Sec 4 Table 4.2: 5 columns including Image column
- [ ] Sec 4.4 & 4.5: flowcharts only, no DANGER boxes
- [ ] Sec 5.4 & 5.5: flowcharts only, no functional safety table
- [ ] Sec 6.4, 6.5, 6.7, 6.8, 6.9: flowcharts only, no WARNING boxes
- [ ] Sec 11.4: flowchart only
- [ ] Sec 12.2: flowchart + ≤5 bullets
- [ ] Sec 12.5: ≤8 bullets only
- [ ] Sec 13: liability disclaimer single instance here only
- [ ] Sec 13.3: role only, no name
- [ ] Sign-off blocks: single instance at end of Section 13 only

**Appendices & Register:**
- [ ] Appendix A = Maintenance Log Template (blank, 10 rows min)
- [ ] Appendix B = LOTO Log Template (blank, 10 rows min)
- [ ] No other appendices present
- [ ] Open Actions Register = standalone .xlsx only, not in manual

**Formatting:**
- [ ] Calibri throughout
- [ ] #1F3864 headings and table headers, #D9E1F2 alternating rows
- [ ] No DANGER boxes anywhere in the document
- [ ] All flowcharts: blue #1F3864 borders, white bg, pill terminals, greyscale-readable
- [ ] Placeholders: bold black text in #F7F7F7 box with grey left border
- [ ] ISO 7010 signs: inline at procedural steps, 20×20mm, not at section headers
- [ ] Header/footer consistent on all pages except cover

**Compliance & Branding:**
- [ ] Standards cited: ISO 12100, ISO 20607, IEC 82079-1, IS 4571, ISO 13849-1, ISO 13850, ANSI B11, Factories Act 1948
- [ ] IEC 61508 and IEC 61800-5-2 NOT referenced
- [ ] "Certified Safety Professional" used — no individual name anywhere
- [ ] SICK or any RA firm name absent — "Independent Safety Consultant" used
- [ ] No invented machine features or specs

---

## SECTION 11: NEW PROJECT INTAKE — QUICK STEPS

When Ravi says "new project" or "site visit data ready":

1. Ask: Project code (P5, P6…)?
2. Ask: What documents uploaded (RA / drawings / checklist / photos)?
3. Ask: Standard OSM or Indo-MIM/Apple DFM project? (Load DFM.md if DFM)
4. Run tier decision matrix (Section 3) — confirm tier before proceeding
5. Choose workflow: new/complex → Workflow A | repeat/template → Workflow B
6. List all data gaps → these become Open Actions
7. Optionally draft scope agreement for customer sign-off
8. Begin drafting section by section — confirm each before next

---

## SECTION 12: DFM MODE (INDO-MIM / APPLE / TATA ELECTRONICS ONLY)

**Applies only when:** Project is explicitly Indo-MIM / Apple supply chain.

Load `DFM.md` in addition to this skill. All safety rules in this skill remain fully non-negotiable.

DFM-specific AI toolchain:
- Perplexity → standards research, clause verification, citations
- Claude → drafting, structuring, compliance checking
- ChatGPT → review, rephrasing, clarity check

Every safety statement must cite a standard + clause number.
Never fabricate standard clause numbers.

**Do not apply DFM rules to any non-Apple / non-Indo-MIM project.**

---

## SECTION 13: WHAT NEVER TO DO

- ❌ Invent machine features, specs, or systems not in project data
- ❌ Use DANGER boxes anywhere — permanently removed May 2026
- ❌ Put liability disclaimer anywhere except Section 13
- ❌ Repeat sign-off blocks
- ❌ Repeat the TOC
- ❌ Use individual name in any author field
- ❌ Include Appendix — Residual Risk Summary
- ❌ Include Open Actions Register inside the manual
- ❌ Include full hazard register table in Section 3 body
- ❌ Reference IEC 61508 or IEC 61800-5-2
- ❌ Name SICK or any RA firm in customer-facing documents
- ❌ Apply DFM rules to non-Apple / non-Indo-MIM projects
- ❌ Fabricate standard clause numbers
- ❌ Patch the generated Word file manually — fix source and regenerate
- ❌ Use str_replace for Unicode content injection (causes silent failures)
- ❌ Proceed with ambiguous scope without confirming with Ravi

---

## REFERENCE FILES (Priority Order)

| Priority | File | Role |
|----------|------|------|
| 1 | `OSM_WORD_FORMAT_STANDARD_V1_2.md` | Master formatting authority — supersedes all |
| 2 | `WORKFLOW_A.md` | Full prompt templates for chat-based generation |
| 3 | `WORKFLOW_B.md` | Code brief + input file templates for code-based generation |
| 4 | This file | Operating context, rules, project registry |
| 5 | `DFM.md` | Indo-MIM / Apple projects only |
