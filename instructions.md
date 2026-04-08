# instructions.md — Workflow & Usage Guide

## Machine Manuals GitHub Repo — How to Use This

**Owner:** Ravikumar | Fortress Safety
**Updated:** April 2026

---

## Repo Purpose
This repo stores AI-assisted machine operating manuals for industrial customers. It is structured so that each customer project is an isolated sub-folder. Claude (and other AI tools) use `CLAUDE.md` as behavioral context when working on files in this repo.

---

## Getting Started

### Step 1: Clone the Repo
```bash
git clone https://github.com/gitravi1987/machine-manuals.git
cd machine-manuals
```

### Step 2: Navigate to Your Project
```bash
cd P1-accurate-machines/
```

### Step 3: Start a Claude Session
- Load `CLAUDE.md` as system context
- Paste the relevant machine spec or existing manual section
- State which standard applies (or ask Claude to identify it)

---

## Folder Conventions

| Folder | Contents |
|--------|----------|
| `/P1-accurate-machines/` | All documents for Accurate Machines project |
| `/P2-karthik-engg/` | All documents for Karthik Engineering |
| `/P3-valeo/` | All documents for Valeo |
| `/IndoMIM-Apple-P1/` | All documents for Indo MIM Apple project |
| `/IndoMIM-Apple-P1/dfm/` | DFM reviews (Apple only) |
| `/templates/` | Reusable section templates (hazard log, risk matrix, etc.) |

---

## File Naming Convention

```
[ProjectID]-[DocumentType]-[Version]-[Date].md

Examples:
P1-operating-manual-v1-2026-04.md
P2-risk-assessment-v2-2026-03.md
P3-guard-specification-v1-2026-05.md
```

---

## AI Session Workflow (Multi-LLM Council)

1. **RESEARCH (Perplexity)**
   - Search for relevant ISO/ANSI clauses and cite sources
   - Output: Evidence block with cited sources

2. **DRAFT (Claude)**
   - Input: Perplexity evidence + machine specs + relevant standard list
   - Output: Draft manual section in Markdown

3. **REVIEW (ChatGPT)**
   - Input: Claude draft
   - Tasks: Check clarity, flag vague statements, suggest alternate wording

4. **AUDIT (Human – Ravikumar)**
   - Final check against source standards and real machine configuration
   - Approve, adjust, and commit to GitHub

---

## Safety Writing Rules (Non-Negotiable)
1. Every safety statement must cite a standard + clause number
2. Use signal words per ISO 11428 / IEC 82079-1:
   - DANGER — Imminent risk of death or serious injury
   - WARNING — Possible risk of death or serious injury
   - CAUTION — Risk of minor injury
   - NOTICE — Risk of property damage only
3. Never use passive voice for safety instructions
   - Wrong: "Guards should be checked"
   - Correct: "Inspect all guards before every shift"
4. Maintenance tasks must include energy isolation steps (LOTO)

---

## Version Control Rules
- `main` branch → approved, customer-ready documents only
- `draft` branch → work-in-progress drafts
- Commit message format: `[P1] Add hazard identification section v1`
- Tag releases: `P1-v1.0`, `P2-v1.0` etc.

---

## Manual Tier Quick Reference

| Tier | Description | Pages | Price |
|------|-------------|-------|-------|
| A | Full data, all 14 sections | 80-120 | ₹15,000-20,000 |
| B | Partial data, placeholders | 50-80 | ₹10,000-12,000 |
| C | Legacy machine, minimal data | 30-50 | ₹8,000-10,000 |

---

## Next Project Checklist (P4 and Beyond)

Before starting any new project, confirm all of the following:
- [ ] Risk assessment (machine safety portion) obtained from customer
- [ ] 2-3 hour on-site visit completed
- [ ] 15-25 photos taken per naming convention
- [ ] Operator interviewed
- [ ] Tier determined (A/B/C) and agreed with customer
- [ ] Scope Agreement drafted and signed by customer
- [ ] Excel checklist (14 tabs) filled out
- [ ] All documents organised and ready to upload

---

## Contact & Escalation
**Technical Queries:** Ravikumar (B11 LMSS Auditor)
**Standards Clarification:** Refer to ISO Online Browsing Platform (OBP) or ANSI Webstore

---

## Appendix: Standards Reference

| Standard | Title | Key Use |
|----------|-------|---------|
| ISO 12100:2010 | Risk Assessment Methodology | Hazard ID, risk matrix |
| ISO 13849-1:2015 | Safety Control Systems | PLd/PLe verification |
| ISO 13850:2015 | Emergency Stop | E-stop design & testing |
| ISO 14120:2015 | Guards | Guard design & construction |
| ISO 14119:2013 | Interlocking Devices | Interlock selection & testing |
| ISO 13857:2019 | Safety Distances | Safe reach distance calculations |
| IEC 82079-1:2019 | Instructions for Use | Manual structure & content |
| ANSI B11.19:2010 | General Machine Safety | US market reference |
| IS 4571:2008 | Indian Machinery Safety | Indian compliance |
| Factories Act 1948 | Indian Industrial Law | LOTO legal basis |
