---
name: grok-machine-manuals
description: >
  Use this skill for ANY task in the Grok Machine Manual Projects sandbox:
  drafting Operating & Safety Manuals (OSMs), scoping tier A/B/C, LOTO/E-Stop/
  operating/maintenance sections, compliance review, generating Word (.docx) or
  Excel Open Actions (.xlsx), or comparing Grok vs Claude sample manuals.
  Triggers: "machine manual", "OSM", "new project", "P2 sample", "tilting machine",
  "generate manual", "Open Actions", "LOTO", "section_content", "Grok sample".
  ALWAYS create files under:
  C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\
  Never under .grok worktrees unless Ravi overrides.
---

# Grok Machine Manuals Skill (Sandbox Entry)

**Version:** 1.2 — path lock + full Word format skill  
**Authority chain:** `GROK.md` → this file → supporting skills below  

## ALWAYS CREATE FILES HERE

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\
```

Parent Machine Manuals root:

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals
```

- If the agent session cwd is a `.grok\worktrees\...` clone, **still write to the absolute path above**.
- Do **not** create a second `Grok Machine Manual Projects` under the worktree.

## Load order (every session)

1. `../GROK.md` — isolation + **mandatory path** + non-negotiables  
2. `GROK_WORKFLOW_B.md` — ingest → draft → generate  
3. **`GROK_OSM_FORMAT.md` (V2.0)** — **full Word format standard** (cover, TOC, headings, colours, HF, tables, flowcharts). Use this before any `.docx` generation.  
4. `GROK_MACHINE_MANUALS_SKILL.md` — section drafting detail  
5. `GROK_MASTER_TEMPLATE.yaml` — skeleton  

Optional read-only reference (do not edit unless Ravi asks):  
`...\Machine Manuals\Skills\Word-format\SKILL_OSM_WORD_FORMAT_STANDARD_V1_2.md`

## Environment tooling

- Word (this sandbox): **python-docx** via pilot `working\build_osm.py`  
- Excel: openpyxl via pilot `working\build_open_actions.py`  
- Optional: `~/.grok/skills/docx/SKILL.md` / `xlsx/SKILL.md`  

## Isolation

| Allowed | Forbidden |
|---------|-----------|
| Create/edit under the absolute Grok sandbox path | Create under `.grok\worktrees\...` |
| Read from `...\Machine Manuals\Projects\...` | Modify root `Projects\`, root `Skills\`, `CLAUDE.md` without request |

## Non-negotiables (summary)

- Certified Safety Professional only (no personal names)  
- No RA firm names → Independent Safety Consultant / Machine Safety Assessment  
- Never invent specs — PLACEHOLDER or Open Action  
- No DANGER boxes  
- No DFM unless pilot marked DFM  
- Appendices: A = Maintenance Log, B = LOTO Log only  
- Open Actions = standalone `.xlsx` only  

## Generation (P2 pilot)

```powershell
cd "C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\P2-kemc-tilting-sample"
python working\build_osm.py
python working\build_open_actions.py
```

## Pilot registry

| Code | Machine | Folder |
|------|---------|--------|
| P2-Grok-Sample | KEMC Tilting Machine | `P2-kemc-tilting-sample\` |
| P7-Rani-Sealant | Robotic Sealant Dispenser | `P7 - Rani Enterprises\` |

**Format note:** P2/P7 V1.0 used older short format. **Next projects** must follow `GROK_OSM_FORMAT.md` V2.0 (do not rebuild P7 unless Ravi asks).
