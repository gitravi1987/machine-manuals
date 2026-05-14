# CLAUDE.md — Machine-Manuals---Desktop

**Repo:** `Machine-Manuals---Desktop`
**Owner:** Ravikumar | Certified Safety Professional | Chennai, India
**Read this file at the start of every Claude Code session.**

---

## 1. What This Repo Is

AI-assisted Operating & Safety Manuals (OSMs) for industrial machinery clients in India.
Output: `.docx` manual + `.xlsx` Open Actions Register per project, ISO/IEC/ANSI-compliant.

**Active project status (P1–P4 complete, P5+ pending):**

| Code  | End User                      | Machine                              | Tier | Status      |
| ----- | ----------------------------- | ------------------------------------ | ---- | ----------- |
| P1    | Accurate Machines             | 48-Spindle Drilling (no coolant)     | A    | ✅ Complete |
| P2    | KEMC / Valeo                  | Tilting Machine (Clutch Plate)       | B    | ✅ Complete |
| P3    | Valeo                         | LE Test Bench                        | A    | ✅ Complete |
| P4    | Indo-MIM → Tata Electronics   | BG Snap Assembly Machine (V67)       | A    | ✅ Complete |
| P5+   | TBD                           | TBD                                  | TBD  | Pending     |

---

## 2. Mode Selection — Confirm at Session Start

| Mode             | When                                                  | Primary spec file                |
| ---------------- | ----------------------------------------------------- | -------------------------------- |
| **Workflow B**   | Default for Claude Code / VS Code (this is the norm)  | `WORKFLOW_B.md`                  |
| **Workflow A**   | Only if I say so — Claude chat + ChatGPT YAML path    | `WORKFLOW_A.md`                  |
| **DFM mode**     | Only if I explicitly say "DFM project" at start       | `DFM.md` + Indo-MIM/Apple rules  |

> If I haven't said which mode, **assume Workflow B**. If a DFM rule seems to apply but I haven't flagged it, **ask before applying it**.

---

## 3. Authoritative Source Files (Read These When Relevant)

All under `Machine manual MD files/New work structure/`:

| File                                  | Use it for                                              |
| ------------------------------------- | ------------------------------------------------------- |
| `WORKFLOW_B.md`                       | Code-based generation (Claude Code default)             |
| `WORKFLOW_A.md`                       | Chat-based generation (reference only here)             |
| `OSM_WORD_FORMAT_STANDARD_V1_2.md`    | All formatting rules — page, fonts, colours, flowcharts |
| `Machine_Manuals_skill.md`            | Full skill — phases, prompts, section-level guidance    |
| `DFM.md`                              | Indo-MIM / Apple projects only                          |
| `PROJECT-README-TEMPLATE.md`          | Copy into each new project folder                       |

**Superseded — do not rely on these for current rules:**
`README.md`, `PRD.md`, `INDEX.md`, `instructions.md`, `MACHINE_MANUAL_INTEGRATED_WORKFLOW.md`, `Machine_manual_creatin_master.md`. Older page counts, "B11 LMSS Auditor" designation, and 14-section structure live here. **Do not propagate these.**

---

## 4. Repo Layout (Actual)

```
Machine-Manuals---Desktop/
├── CLAUDE.md                              ← this file
├── .gitattributes
├── MachineManaul_NewProject_SOP_V1.2.docx ← new-project SOP reference
├── master_yaml_template.yaml              ← starter for section_content.yaml
├── Machine manual MD files/
│   └── New work structure/                ← authoritative .md docs live here
│       ├── WORKFLOW_A.md
│       ├── WORKFLOW_B.md
│       ├── OSM_WORD_FORMAT_STANDARD_V1_2.md
│       ├── Machine_Manuals_skill.md
│       ├── DFM.md
│       └── PROJECT-README-TEMPLATE.md
├── Master template/                       ← (local only, not in GitHub yet)
└── Projects/
    ├── P1-accurate-machines/
    ├── P2-kemc-valeo/
    ├── P3-valeo-le/
    ├── P4-indomim-tata/
    └── P[n]-[shortname]/                  ← pattern for new projects
```

**Per-project folder structure** (inside `Projects/Pxx-name/`):

```
Pxx-name/
├── PROJECT-README.md          ← copy of PROJECT-README-TEMPLATE.md, filled in
├── inputs/
│   ├── machine_data.json      ← see WORKFLOW_B Step 1
│   ├── section_content.yaml   ← see WORKFLOW_B Step 1
│   ├── ra-report.pdf          ← Machine Safety Assessment (read-only)
│   └── drawings/              ← electrical/pneumatic/hydraulic schematics
├── photos/                    ← naming: Pxx_Photo_NN_Subject.jpg
├── working/                   ← scratch .js section files, intermediate builds
└── outputs/
    ├── [EndUser]_[Machine]_OSM_V1.0.docx
    ├── [EndUser]_[Machine]_OSM_V1.0.pdf
    └── [Client]_[Machine]_OpenActions_V1.0.xlsx
```

---

## 5. Before Writing Any Code — Read the Skills

Whenever a task involves generating `.docx`, `.xlsx`, or filling a PDF, **read the relevant SKILL.md first**:

- Word generation → `/mnt/skills/public/docx/SKILL.md`
- Excel generation (Open Actions Register) → `/mnt/skills/public/xlsx/SKILL.md`
- PDF export or PDF form work → `/mnt/skills/public/pdf/SKILL.md`

This is mandatory. The skills encode environment-specific constraints (libraries available, validation script paths, pitfalls) that aren't in training data.

---

## 6. Technical Stack & Conventions

- **Word generation:** Node.js `docx` library v9.6.1 — each section as a standalone `.js` file
- **Excel generation:** Python `openpyxl`
- **Validation (run after every section injection):**
  `python3 /mnt/skills/public/docx/scripts/office/validate.py`
- **Working directory:** `Projects/Pxx-name/working/`
- **Final outputs:** `Projects/Pxx-name/outputs/`

### Code Gotchas (Battle-Tested — Do Not Re-Learn These)

1. **Never use `str_replace` for Unicode content** (em-dashes, special symbols cause silent failures). Use Python `content.replace(placeholder, new_code)` injection instead.
2. **`PageNumber.CURRENT` goes inside a `TextRun` children array** — never `new PageNumber()`.
3. **Extend `bodyChildren` explicitly** when adding sections beyond the original stub count (Sections 11–13 and Appendices commonly break this).
4. **TOC generated by `TableOfContents`** is a Word field — user must manually refresh in Word (right-click → Update Field → Update entire table). Note this in delivery.
5. **Sections 8–10 can be combined** into one `.js` file and injected via the Section 10 placeholder.
6. **Fix in source, regenerate** — never patch the generated `.docx` manually.

---

## 7. Non-Negotiable Content Rules (Firm — Apply Always)

These come from hard-won project learnings. Violating them is a defect.

### Designation & Naming
- Author/role field everywhere: **"Certified Safety Professional"** — no individual name
- **Never** write "B11 LMSS Licensed Machinery Safety Specialist" or any B11 LMSS variant in customer-facing documents
- **Never** name SICK or any third-party RA firm — use **"Independent Safety Consultant"** / **"Machine Safety Assessment"**

### Structure & Content
- **13 sections + 2 appendices** — Appendix A = Maintenance Log Template, Appendix B = LOTO Log Template. Nothing else.
- **Appendix A (Residual Risk Summary) is permanently removed.** Do not regenerate it.
- **TOC: H1 entries only, single instance only** (pages 3–4). Never repeated.
- **Revision table: 4 columns only** — Revision / Date / Description / Reviewed By. No "Prepared By".
- **Liability disclaimer: Section 13 only.** Never duplicated, never in Section 1.
- **Sign-off blocks: single instance only**, at end of Section 13.
- **Sec 1.6 and Sec 13.3: role only, no individual name.**
- **Section 3: max 2 pages, narrative only.** No tables. No WARNING/DANGER boxes. End with reference to Machine Safety Assessment Report.
- **Hazard register tables are excluded from the manual body** — Section 3 is summary narrative only.

### Boxes & Flowcharts
- **No DANGER boxes anywhere.** Template uses WARNING / CAUTION / NOTICE / OPEN ACTION only.
- **Flowcharts only** for sections 4.4, 4.5, 5.4, 5.5, 6.4, 6.5, 6.7, 6.8, 6.9, 11.4, 12.2.
- Flowcharts: blue borders `#1F3864`, white fill, pill terminals, max 10 steps, ≤10 words per step, greyscale-readable.

### Open Actions Register
- **Always a standalone `.xlsx` file** — never embedded in the manual.
- 7 columns: `ID | Description | Category | Priority | Responsibility | Target Date | Status`
- Filename: `[Client]_[MachineName]_OpenActions_V1.0.xlsx`

### Compliance
- Standards in use: **ISO 12100:2010, ISO 20607:2019, IEC 82079-1:2019, IS 4571:2008, ISO 13849-1, ISO 13850, ANSI B11.19, Factories Act 1948**
- **Excluded — do not reference:** IEC 61508, IEC 61800-5-2

### Data Integrity
- **Never invent machine features, specs, or systems not in the project data.** Canonical example: P1 (Accurate Machines) does NOT have coolant — assuming it did was a defect.
- Missing data → mark as `**[PLACEHOLDER — description, source, status]**` (bold text) **or** log as Open Action. Never fabricate.
- **Never fabricate standard clause numbers.** If unsure, write `[INSUFFICIENT EVIDENCE — VERIFY WITH SOURCE STANDARD]`.

---

## 8. Tier Framework (Quick Reference)

| Tier | Data Available                                         | Pages | Price       | Timeline   |
| ---- | ------------------------------------------------------ | ----- | ----------- | ---------- |
| A    | Full RA + schematics + PLC + photos                    | 40–60 | ₹15k–20k    | 14–21 days |
| B    | RA + partial schematics + informal procedures          | 25–40 | ₹10k–12k    | 10–14 days |
| C    | RA only, no schematics, legacy machine                 | 15–25 | ₹8k–10k     | 7–10 days  |

**Page counts are firm.** Customers are price-sensitive — manuals must be lean while preserving all safety-critical content. Old `PRD.md` / `instructions.md` say 80–120 pages for Tier A — that is superseded.

Full section map by tier is in `WORKFLOW_B.md`.

---

## 9. What to Do When… (Decision Quick Reference)

| If I say…                                              | You should…                                                                                                                                  |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| "New project P5" / "new customer"                      | Ask tier-scoping questions (RA available? Schematics? PLC docs?). Create `Projects/P5-shortname/`, copy `PROJECT-README-TEMPLATE.md`, fill it. |
| "Generate the manual" + `machine_data.json` ready       | Read `WORKFLOW_B.md` Step 2. Read `/mnt/skills/public/docx/SKILL.md`. Then build section-by-section, validate after each.                       |
| "Generate Open Actions Register"                       | Read `/mnt/skills/public/xlsx/SKILL.md`. Build standalone `.xlsx` from `open_actions[]` in `machine_data.json`. Never put it in the manual.    |
| "Fix the format" / "the docx has X wrong"              | Fix in source `.js` / `.json` / `.yaml` — **regenerate**, never edit the `.docx` directly. Validate after.                                    |
| "DFM project"                                          | Switch to DFM mode. Read `DFM.md`. Apply DFM rules only for Indo-MIM → Tata / Apple projects. Safety rules from this file still apply.        |
| Asking to update workflow / standard rules             | Edit the source `.md` in `Machine manual MD files/New work structure/`. Update this CLAUDE.md only if a non-negotiable rule changes.          |

---

## 10. What Claude Code Must NOT Do

- ❌ Fabricate ISO/IEC/ANSI/IS clause numbers
- ❌ Invent machine features or specs not present in `machine_data.json` or RA report
- ❌ Use DANGER boxes anywhere
- ❌ Reference IEC 61508 or IEC 61800-5-2
- ❌ Name SICK (or any RA firm) in customer-facing docs
- ❌ Include any individual person's name in author/role fields
- ❌ Write "B11 LMSS" anywhere in a customer-facing document
- ❌ Put the Open Actions Register inside the manual
- ❌ Duplicate the liability disclaimer, sign-off blocks, or TOC
- ❌ Include the deprecated Appendix A (Residual Risk Summary)
- ❌ Include hazard register tables in Section 3 body
- ❌ Patch the generated `.docx` manually instead of fixing source + regenerating
- ❌ Apply DFM rules to non-Apple / non-Indo-MIM projects
- ❌ Use `str_replace` to inject Unicode content into `.js` files

---

## 11. When in Doubt

**Ask before assuming.** Specifically:

- Tier unclear → ask
- Machine feature not in source data → ask or mark `[PLACEHOLDER ...]`
- Workflow A vs B not stated → assume Workflow B, confirm if anything looks chat-driven
- Two source files conflict → newer files win (WORKFLOW_A/B, OSM_V1_2, skill file). Old files (`PRD.md`, `instructions.md`, `README.md`) are superseded.

---

*This file lives at the repo root. Update only when a non-negotiable rule changes. Detailed workflow updates go in `WORKFLOW_B.md` / `OSM_WORD_FORMAT_STANDARD_V1_2.md` / `Machine_Manuals_skill.md`.*
