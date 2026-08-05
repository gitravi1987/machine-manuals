---
name: antigravity-machine-manuals
description: >
  Use this skill for ANY task in the Antigravity Machine Manual Projects sandbox:
  drafting Operating & Safety Manuals (OSMs), scoping tier A/B/C, LOTO/E-Stop/
  operating/maintenance sections, compliance review, generating Word (.docx) or
  Excel Open Actions (.xlsx), or creating Antigravity sample manuals.
  Triggers: "machine manual", "OSM", "new project", "Antigravity sample",
  "generate manual", "Open Actions", "LOTO", "section_content", "Antigravity".
  ALWAYS create files under:
  C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Antigravity Machine Manual Projects\
---

# Antigravity Machine Manuals Skill (Sandbox Entry)

**Version:** 1.0 — path lock to Machine Manuals Desktop folder  
**Authority chain:** `ANTIGRAVITY.md` → this file → supporting skills below  

## ALWAYS CREATE FILES HERE

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Antigravity Machine Manual Projects\
```

Parent Machine Manuals root:

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals
```

- If the agent session cwd is a worktree clone, **still write to the absolute path above**.
- Do **not** create a second `Antigravity Machine Manual Projects` under a worktree.

## Load order (every session)

1. `../ANTIGRAVITY.md` — isolation + **mandatory path** + non-negotiables  
2. `ANTIGRAVITY_WORKFLOW_B.md` — ingest → draft → generate  
3. `ANTIGRAVITY_OSM_FORMAT.md` — Indo-MIM-style format (colours, sections)  
4. `ANTIGRAVITY_MACHINE_MANUALS_SKILL.md` — section drafting detail  
5. `ANTIGRAVITY_MASTER_TEMPLATE.yaml` — skeleton  

## Environment tooling

- Word (this sandbox): **python-docx** via pilot `working\build_osm.py`  
- Excel: openpyxl via pilot `working\build_open_actions.py`  

## Isolation

| Allowed | Forbidden |
|---------|-----------|
| Create/edit under the absolute Antigravity sandbox path | Create under temp worktrees |
| Read from `...\Machine Manuals\Projects\...` | Modify root `Projects\`, `Grok Machine Manual Projects\`, root `Skills\`, `CLAUDE.md` without request |

## Non-negotiables (summary)

- Certified Safety Professional only (no personal names)  
- No RA firm names → Independent Safety Consultant / Machine Safety Assessment  
- Never invent specs — PLACEHOLDER or Open Action  
- No DANGER boxes  
- No DFM unless pilot marked DFM  
- Appendices: A = Maintenance Log, B = LOTO Log only  
- Open Actions = standalone `.xlsx` only  
