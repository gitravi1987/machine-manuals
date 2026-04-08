# Manual Creation Workflow

**Repo:** machine-manuals
**Owner:** Ravikumar | Fortress Safety (Halma)
**Updated:** April 2026

> This workflow governs how every machine manual is created in this repo.
> Full detail for each step is in `instructions.md`.
> Templates are in `/templates/`. Prompts are in `/prompts/`.

---

## Project Folder Structure

Before starting any project, create this folder structure:

```
/Pxx-customer-name/
  /inputs        ← Upload all raw data here first
  /outputs       ← Save all drafted sections here
  /final         ← Final approved .docx and .pdf only
  /risk-assessment
  /pictures
  /schematics
  /compliance
  PROJECT-README.md
```

For Indo MIM Apple projects only — also add:
```
  /dfm           ← DFM reviews (Apple / Tata only)
```

---

## STEP 1 — Upload All Inputs

Upload to `/inputs/`:
- Filled Excel checklist (14 tabs)
- Site photos (named: Pxx_Photo_01_Subject.jpg)
- Risk assessment document (SICK / TUV / third-party)
- Electrical / pneumatic / hydraulic schematics (if available)
- Any existing OEM manual or datasheet

Do NOT start writing until all available inputs are uploaded.

---

## STEP 2 — Determine Tier

Review inputs and confirm Tier with customer:

| Tier | Conditions | Sections |
|------|-----------|----------|
| A | Complete data — RA + all schematics + PLC + photos | 1–14 + Quick Ref |
| B | Partial — RA available, some schematics missing | 1–7 full + 8–10 placeholder |
| C | Legacy — RA only, no schematics, no PLC docs | 1–7 + functional diagrams |

Send Scope Agreement to customer (template in `instructions.md` Section 2.5).

---

## STEP 3 — Generate Each Section

For each section, use the matching prompt and template:

| Section | Prompt | Template |
|---------|--------|----------|
| 2 — Machine Overview | `prompts/section-2-machine-overview.md` | `templates/section-2-machine-overview.md` |
| 3 — Hazard & Risk | `prompts/hazard.md` | `templates/section-3-hazard-risk.md` |
| 4 — LOTO | `prompts/loto.md` | `templates/section-4-loto.md` |
| 5 — Emergency Stop | *(use loto.md guidance)* | `templates/section-5-emergency-stop.md` |
| 6 — Operating Instructions | `prompts/operating.md` | `templates/section-6-operating-instructions.md` |
| 7 — Maintenance | `prompts/maintenance.md` | `templates/section-7-maintenance.md` |
| 12 — Safety Features | *(use hazard.md guidance)* | `templates/section-12-safety-features.md` |
| 13 — Compliance | `prompts/compliance.md` | `templates/section-13-compliance.md` |

Save each output to `/outputs/section-X-[MACHINE_NAME].md`.

---

## STEP 4 — Generate Open Actions Register

Use: `prompts/open-actions.md` + `templates/open-actions-template.md`

- Consolidate all Open Actions from every section
- Save to `/outputs/open-actions-[MACHINE_NAME].md`
- Export to `.xlsx` for customer delivery

---

## STEP 5 — Review & Refinement

1. Perplexity → verify all standard citations are accurate
2. Claude → check consistency between sections
3. ChatGPT → review for clarity and readability
4. Ravikumar → final audit against source standard and real machine

Run compliance audit using: `prompts/compliance.md`

---

## STEP 6 — Combine All Sections

Combine all `/outputs/section-X` files into one master manual draft.
Order: Cover > TOC > 1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9 > 10 > 11 > 12 > 13 > 14 > Open Actions

---

## STEP 7 — Export to Word & PDF

Use Phase 4 Word Generation Brief from `instructions.md` Section 3.4.

Filename convention:
```
[Customer]_[Machine]_Tier[X]_Manual_v1.docx
[Customer]_[Machine]_Tier[X]_Manual_v1.pdf
[Customer]_[Machine]_Tier[X]_QuickRef_v1.docx  (Tier A only)
```

Save final files to `/final/`.

---

## Delivery Checklist

- [ ] Full Manual (.docx) — editable
- [ ] Full Manual (.pdf) — locked
- [ ] Quick Reference (.docx/.pdf) — Tier A only
- [ ] Open Actions Register (.xlsx)
- [ ] Compliance Audit Trail (.docx)
- [ ] Customer sign-off received
- [ ] All files committed to GitHub main branch

---

## Key Rules

- Never start Word generation until compliance audit is PASS
- Never mark Open Action as Closed without customer confirmation
- All final files go to `/final/` only — never to `/outputs/`
- DFM work for Indo MIM Apple → see `DFM.md` and `/dfm/` folder
- main branch = approved only | draft branch = work in progress
