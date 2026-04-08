# INDEX.md — Project Index

## Machine Manuals Repository Index

**Owner:** Ravikumar | Fortress Safety
**Updated:** April 2026

---

## Root Files

| File | Purpose |
|------|---------|
| [README.md](./README.md) | Repository landing page and overview |
| [CLAUDE.md](./CLAUDE.md) | AI behavior instructions for Claude |
| [PRD.md](./PRD.md) | Product Requirements Document |
| [instructions.md](./instructions.md) | Workflow & usage guide |
| [DFM.md](./DFM.md) | Design for Manufacturability guide (Apple projects only) |
| [INDEX.md](./INDEX.md) | This file — project index |
| [PROJECT-README-TEMPLATE.md](./PROJECT-README-TEMPLATE.md) | Template for per-project READMEs |

---

## Projects

| ID | Folder | Customer | Machine | Tier | Status | DFM? |
|----|--------|----------|---------|------|--------|------|
| P1 | [P1-accurate-machines/](./P1-accurate-machines/) | Accurate Machines | 48-Spindle Drilling | A | Complete | No |
| P2 | [P2-karthik-engg/](./P2-karthik-engg/) | Karthik Engineering | Tilting Machine | B | In Progress | No |
| P3 | [P3-valeo/](./P3-valeo/) | Valeo | LE Test Bench | A | Content Complete | No |
| IndoMIM-Apple-P1 | [IndoMIM-Apple-P1/](./IndoMIM-Apple-P1/) | Indo MIM (Apple) | TBD | TBD | Planned | Yes |

---

## Standard Project Folder Structure

Each project folder contains:
```
[Project-Folder]/
├── README.md              <- Project overview (from template)
├── manual/                <- Operating manual files (.md, .docx, .pdf)
├── compliance/            <- Compliance checklists and audit trails
├── risk-assessment/       <- Customer RA documents
├── pictures/              <- Site photos (named per convention)
└── schematics/            <- Electrical/hydraulic schematics
```

Apple project (IndoMIM-Apple-P1) also contains:
```
IndoMIM-Apple-P1/
└── dfm/                   <- DFM review files
```

---

## Quick Start

1. New project? Copy `PROJECT-README-TEMPLATE.md` into your new project folder as `README.md`
2. Read `CLAUDE.md` before starting any AI session
3. Follow the workflow in `instructions.md`
4. DFM work? Only for Apple projects — see `DFM.md`
