text
# INDEX.md — Master File Map
**Repo:** machine-manuals
**Owner:** Ravikumar | Fortress Safety (Halma)
**Updated:** April 2026

---

## What Is This Repo?
This repo stores all AI-assisted machine operating manuals and DFM reviews.
- Machine Manuals → All projects (Accurate, KEMC, Valeo, future)
- DFM → Indo MIM → Tata Electronics (Apple) projects ONLY

---

## Root Folder Files — What Each Does

| File | Purpose | Use When |
|------|---------|----------|
| `INDEX.md` | This file — master map | Always refer here first |
| `README.md` | GitHub landing page | Public repo overview |
| `CLAUDE.md` | AI behavior rules | Start every Claude session |
| `PRD.md` | Project requirements | Scoping, pricing, standards |
| `instructions.md` | Full manual workflow | Writing any machine manual |
| `DFM.md` | DFM rules | Indo MIM / Apple ONLY |
| `PROJECT-README-TEMPLATE.md` | Project folder template | Copy into each new project |

---

## Project Register

| ID | Folder | Customer | Machine | Tier | Status | DFM? |
|----|--------|----------|---------|------|--------|------|
| P1 | `/P1-accurate-machines/` | Accurate Machines | 48-Spindle Drilling | A | Complete | No |
| P2 | `/P2-kemc-valeo/` | KEMC / Karthik Engg | Tilting Machine | B | In Progress | No |
| P3 | `/P3-valeo-le/` | Valeo | LE Test Bench | A | Content Complete | No |
| P4 | `/P4-pending/` | TBD | Legacy machines | B/C | Pending | No |
| DFM-P1 | `/IndoMIM-Apple-P1/` | Indo MIM | Tata / Apple | — | TBD | ✅ Yes |

---

## Folder Structure Per Project
Pxx-customer-name/
├── PROJECT-README.md ← Filled from template; project summary
├── manual/ ← All manual drafts → final .docx + .pdf
├── risk-assessment/ ← SICK/TÜV RA documents (read-only reference)
├── pictures/ ← Site photos (naming: P1_Photo_01_Subject.jpg)
├── schematics/ ← Electrical / Pneumatic / Hydraulic
└── compliance/ ← ComplianceAudit.docx + OpenActions.xlsx