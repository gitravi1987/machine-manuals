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

Ravikumar is a Certified Safety Professional running an independent technical documentation
consultancy in Chennai, India. This skill encodes the complete, battle-tested workflow for
creating ISO/IEC/ANSI-compliant Operating & Safety Manuals for industrial machinery clients.

---

## QUICK ORIENTATION

Before doing anything, establish:
1. **Is this a new project or continuation?** (New → start at Phase 1. Continuation → check project code and current phase.)
2. **Which project code?** (P1–P4 complete/in progress; new projects are P5+.)
3. **What documents has Ravi uploaded?** (SICK/third-party RA report, drawings, Excel checklist, photos.)
4. **What is the task?** (Scope tier / Draft section / Compliance audit / Generate Word file.)

If any of these are unclear, **ask before proceeding.**

---

## SECTION 1: FOUR-PHASE DELIVERY MODEL

| Phase | Task | Output |
|-------|------|--------|
| **1 – Data Consolidation** | Review RA + drawings + checklist; identify data gaps; confirm tier | Structured data summary + gap list |
| **2 – Manual Writing** | Section-by-section drafting with review-and-confirm at each step | Drafted manual content (one conversation) |
| **3 – Review & Refinement** | Compliance audit, Open Actions audit, image placeholder check | Final content ready for generation |
| **4 – Word/Excel Generation** | Build .docx and .xlsx files using Node.js docx 9.6.1 / Python openpyxl | Downloadable deliverables |

**Critical workflow rule:** Draft ALL content in one conversation (section-by-section, confirm before next).
Open a NEW conversation within the same Claude project for Word/Excel generation.

---

## SECTION 2: PROJECT REGISTRY

| Code | Client | Machine | Status |
|------|--------|---------|--------|
| P1 | Accurate Machines | 48-Spindle Drilling Machine | ✅ Complete (no coolant — any coolant references are incorrect) |
| P2 | KEMC / Valeo | Tilting Machine (Clutch Plate) | ✅ Complete |
| P3 | Valeo | LE Test Bench | ✅ Complete |
| P4 | Indo-MIM Limited / Tata Electronics | BG Snap Assembly Machine (V67) | ✅ Complete |
| P5+ | TBD | TBD | New project — follow Phase 1 intake |

**Designation rule:** Always use "Certified Safety Professional" in documents. Never use "B11 LMSS Licensed Machinery Safety Specialist" in customer-facing content (retired).

**Third-party branding rule:** Never reference SICK or any RA firm by name in customer-facing documents. Use "Independent Safety Consultant" or "Machine Safety Assessment" instead.

---

## SECTION 3: TIER SCOPING (DO THIS FIRST FOR NEW PROJECTS)

### Tier Decision Matrix

| Question | Yes | No |
|----------|-----|----|
| Risk assessment (RA) report available? | Continue | Recommend commissioning RA first (adds ₹20k–40k, 2–3 weeks) |
| Full schematics (electrical/pneumatic/hydraulic) available? | → Tier A candidate | → Tier B/C candidate |
| Control system documentation (PLC/HMI backup) available? | → Tier A candidate | → Tier B/C candidate |
| Machine age < 10 years with active maintenance? | → Tier A/B | → Tier B/C |
| Operating procedures formally documented? | → Tier A/B | → Tier B/C |

### Tier Summary

**TIER A — Complete Data**
- All schematics, RA, control system docs, LOTO points labeled, maintenance history
- Output: 40–60 pages (lean; no padding)
- Price: ₹15,000–20,000 | Timeline: 14–21 days
- Deliverables: Full manual + Quick Reference (Word + PDF) + Open Actions Register

**TIER B — Partial Data**
- RA available; some schematics; informal procedures; partial maintenance history
- Output: 25–40 pages
- Price: ₹10,000–12,000 | Timeline: 10–14 days
- Deliverables: Standard manual (Word + PDF) + Open Actions Register

**TIER C — Legacy / Minimal Data**
- RA available; no schematics; operator-knowledge-only procedures; 30+ year old machine
- Output: 15–25 pages
- Price: ₹8,000–10,000 | Timeline: 7–10 days
- Deliverables: Streamlined manual (Word + PDF) + Open Actions Register (critical)

**Page count rule:** Manuals must be lean. Customers are price-sensitive. Cut non-essential or repetitive content. Never cut safety-critical content.

**Standard inputs:** SICK/third-party RA report + drawing files. Primary LLM workflow: Claude only (authoring + Word generation). Use ChatGPT only for data consolidation/structuring if needed. Perplexity only if citations/research required. Do NOT upload RA or drawings to multiple LLMs unnecessarily.

---

## SECTION 4: STANDARD MANUAL STRUCTURE

### Section Map by Tier

| Sec | Title | Tier A | Tier B | Tier C |
|-----|-------|--------|--------|--------|
| 1 | Cover, TOC, Disclaimer, Scope | ✅ Full | ✅ Full | ✅ Full |
| 2 | Machine Overview (nameplate, specs, intended use) | ✅ Full | ✅ Full | ✅ Full |
| 3 | Hazard ID & Risk Assessment (narrative summary) | ✅ Full | ✅ Full | ✅ Abbreviated |
| 4 | LOTO Procedures | ✅ Full | ✅ Full | ✅ Full |
| 5 | Emergency Stop (ISO 13850) | ✅ Full | ✅ Full | ✅ Full |
| 6 | Operating Instructions | ✅ Full | ✅ Full | ✅ Full |
| 7 | Maintenance & Care | ✅ Full | ✅ Partial | ✅ Abbreviated |
| 8 | Electrical Schematic | ✅ Full | ⚠️ Placeholder | ❌ Omit |
| 9 | Pneumatic Schematic | ✅ Full | ⚠️ Placeholder | ❌ Omit |
| 10 | Hydraulic Schematic | ✅ If applicable | ⚠️ Placeholder | ❌ Omit |
| 11 | HMI Alarms & Fault Codes | ✅ If applicable | ⚠️ If data available | ❌ Usually N/A |
| 12 | Safety Features & Interlocks | ✅ Full | ✅ Streamlined | ✅ Abbreviated |
| 13 | Compliance & Certifications | ✅ Full | ✅ Full | ✅ Full |
| Appendix A | Residual Risk Summary | ✅ | ✅ | ⚠️ |
| Appendix B | Maintenance Log Template | ✅ | ✅ | ✅ |
| Appendix C | LOTO Log Template | ✅ | ✅ | ✅ |
| Open Actions Register | Standalone .xlsx (never in manual body) | ✅ | ✅ | ✅ |

**Hazard register rule:** Never include a full hazard register table in the manual body. Section 3 contains narrative summary only. Full residual risk content goes in Appendix A.

---

## SECTION 5: DRAFTING RULES & CONTENT STANDARDS

### Non-Negotiable Rules

1. **Never invent machine features, specs, or systems** not explicitly provided in the project data. If information is missing, use a placeholder (e.g., `[TBC — pending customer confirmation]`) or flag as an Open Action.
2. **Completeness over condensation for safety-critical content.** LOTO tag-out/tag-in sequences, E-stop procedures, and emergency protocols must be fully self-contained in every location they appear. Operators must not need to cross-reference the full manual.
3. **Quick reference documents must be fully self-contained.** All LOTO, startup/shutdown, and emergency stop steps must appear in full — no "refer to Section X."
4. **Open Actions are a professional differentiator.** Every safety gap, unverified item, or missing data point must be formally logged in the Open Actions Register (.xlsx), not ignored or papered over.
5. **All Open Actions go in the standalone .xlsx register only.** The register is a working document and is never included in the customer-facing manual.

### Compliance Standards to Reference

| Standard | Application in Manual |
|----------|----------------------|
| ISO 12100:2010 | Hazard ID & Risk Assessment methodology (Section 3) |
| ISO 20607:2019 | Manual structure and information requirements |
| IEC 82079-1:2019 | Instructions for use — quality and competence |
| IS 4571:2008 | Indian machinery safety standard (compliance statement) |
| ISO 13849-1 | Safety-related control systems (Section 12) |
| ISO 13850 | Emergency stop function design (Section 5) |
| ANSI B11 | General machinery safety (referenced where applicable) |
| Factories Act 1948 | Indian industrial law (compliance statement) |

**Excluded standards (do not reference):** IEC 61508, IEC 61800-5-2 (removed per project decisions).

### Formatting Specification

- **Paper:** A4, 25mm margins
- **Font:** Calibri — Body: 11pt, Section headings: 13–14pt, Sub-headings: 12pt
- **Heading colour:** Dark blue `#1F3864`
- **Table rows:** Alternating `#D9E1F2`; header rows dark blue with white text
- **WARNING boxes:** `#FFF2CC` background, black border
- **DANGER boxes:** `#FCE4D6` background, red left border 3pt
- **CAUTION boxes:** Orange left border
- **NOTICE boxes:** Light grey background, black left border
- **Open Action boxes:** `#FCE4D6` background, red left border 3pt
- **Images:** Grey placeholder boxes with italic captions when photos unavailable
- **Header:** Machine name | Manual title | Page number
- **Footer:** CONFIDENTIAL

### Safety Signs (ISO 7010:2019)

Integrate inline at procedural steps where applicable:

| Sign | Code | Use When |
|------|------|----------|
| Warning: General | W001 | General caution steps |
| Warning: Crushing | W003 | Pinch/crush hazard steps |
| Warning: Electrical | W017 | Electrical isolation steps |
| Warning: Hand injury | W019 | Hand/finger hazard proximity |
| Warning: Suspended load | W028 | Overhead/lifting hazard |
| Mandatory: General | P002 | Mandatory action steps |
| Mandatory: Hearing protection | P010 | Noise hazard zones |
| Mandatory: Gloves | M008 | Hand protection required |
| Mandatory: Safety footwear | M009 | Foot protection required |

---

## SECTION 6: OPEN ACTIONS REGISTER

### Format (standalone .xlsx, 3 sheets)

**Sheet 1 — Full Register**

| ID | Description | Category | Priority | Responsibility | Target Date | Status | Notes |
|----|-------------|----------|----------|----------------|-------------|--------|-------|
| OA-P[n]-001 | [Item] | [Category] | [High/Med/Low] | [Customer/Engineer] | [Date] | Open/Closed | [Detail] |

**Categories:** Safety Gap | Documentation | Schematic | Software | Maintenance | Other

**Sheet 2 — Summary by Category**
**Sheet 3 — Revision History**

### Filename Convention

`[Client]_[MachineName]_OpenActions_V[x.x].xlsx`
Example: `IndoMIM_BGSnap_OpenActions_V1.0.xlsx`

---

## SECTION 7: WORD DOCUMENT GENERATION

### Technical Stack

- **Word (.docx):** Node.js `docx` library v9.6.1
- **Excel (.xlsx):** Python `openpyxl`
- **Validation:** `python3 /mnt/skills/public/docx/scripts/office/validate.py` after every section
- **Working directory:** `/home/claude/`
- **Output directory:** `/mnt/user-data/outputs/`

### Generation Workflow

1. Read `/mnt/skills/public/docx/SKILL.md` before writing any code
2. Write each section as a standalone `.js` file
3. Inject via Python script into `generate_osm.js` using `content.replace(placeholder, new_code)` — **never use `str_replace` for Unicode content** (em-dashes, special symbols cause silent failures)
4. Validate after every section injection
5. Sections with combined content (e.g., 8+9+10) can share one file; inject at last section's placeholder; replace earlier placeholders with comment stubs
6. The `bodyChildren` array must be explicitly extended when adding sections beyond original stub count
7. Use `PageNumber.CURRENT` (not `new PageNumber()`) inside `TextRun` children for page numbers
8. TOC fields require manual refresh in Word (right-click → Update Field → Update entire table)

### Filename Convention

`[Client]_[MachineName]_OSM_V[x.x].docx`
Example: `IndoMIM_BGSnap_OSM_V1.0.docx`

---

## SECTION 8: COMPLIANCE AUDIT CHECKLIST

Run this before Phase 4 (Word generation). Every item must pass.

**Content Completeness:**
- [ ] Section 2: Nameplate data complete (make, model, year, serial, power rating)
- [ ] Section 3: Narrative hazard summary covers all risks from RA; no full hazard table in body
- [ ] Section 4: All LOTO points documented; tag-out/tag-in sequences complete and self-contained
- [ ] Section 5: E-stop locations identified; ISO 13850 compliance noted; functional safety performance table NOT included (removed per project standard)
- [ ] Section 6: Operating cycle clear; startup/normal/shutdown and pre-shift checks defined
- [ ] Section 7: Maintenance schedule realistic (Weekly/Monthly/Six-Monthly only; no daily tasks unless confirmed); pre-shift checks in Section 6.3
- [ ] Appendix A: Residual Risk Summary present (not in Section 3 body)
- [ ] Appendix B: Maintenance Log Template present
- [ ] Appendix C: LOTO Log Template present
- [ ] Open Actions Register: All unverified items logged; register is standalone .xlsx only

**Safety & Risk:**
- [ ] All hazards from RA addressed in manual
- [ ] LOTO procedures match machine configuration
- [ ] E-stop locations marked; reset procedure clear
- [ ] Residual risk disclosure present
- [ ] No contradictions between sections
- [ ] No invented machine features or specs

**Formatting:**
- [ ] Formatting spec applied consistently (fonts, colours, box styles)
- [ ] Image placeholders in place for all pending photos
- [ ] ISO 7010 safety signs integrated at correct procedural steps
- [ ] Header/footer consistent throughout
- [ ] TOC present (requires manual refresh in Word)

**Compliance Statements:**
- [ ] Standards cited: ISO 12100:2010, ISO 20607:2019, IEC 82079-1:2019, IS 4571:2008
- [ ] Designation used: "Certified Safety Professional" (not B11 LMSS)
- [ ] Third-party RA firm branding removed; replaced with "Independent Safety Consultant" / "Machine Safety Assessment"
- [ ] Liability disclaimer present on cover page

---

## SECTION 9: IMAGE MANAGEMENT

When customer photos are unavailable:

**Option A — Grey placeholder box** (standard approach)
Insert grey shaded box with italic caption: `[IMAGE: Description — pending customer photo]`

**Option B — Text description**
For LOTO diagrams and control panels: detailed text description of what should be shown.

**Option C — SVG functional diagram**
For Tier C legacy machines: energy isolation diagram, machine layout with hazard zones.

### Photo Naming Convention (for customer brief)

`[ProjectCode]_Photo_[Seq]_[Subject]_[Detail].jpg`
Example: `P4_Photo_12_LOTO_Isolator_Front.jpg`

---

## SECTION 10: QUICK REFERENCE FOR NEW PROJECT INTAKE

When Ravi says "new project data ready" or similar:

1. **Ask:** What is the project code? (P5, P6, etc.)
2. **Ask:** What documents are uploaded? (RA report / drawings / checklist / photos)
3. **Determine tier** using Section 3 decision matrix — confirm with Ravi before proceeding
4. **Confirm machine details:** Client name, machine name, end user, site location, machine age
5. **List data gaps** — anything missing that will become Open Actions
6. **Draft scope agreement** (optional — for customer sign-off before writing begins)
7. **Begin Phase 2** section by section; confirm each section before starting next

---

## REFERENCE POINTER

For detailed prompt templates, compliance framework cross-reference tables, pricing/timeline breakdowns, and scope agreement templates, refer to:

`/mnt/project/MACHINE_MANUAL_INTEGRATED_WORKFLOW.md`

Sections to reference:
- Section 3 — Prompt templates for each phase
- Section 4 — Standards cross-reference table
- Section 6 — Pricing, timeline, deliverables checklist
- Section 2.3 — Scope Agreement template (send to customer before writing)
