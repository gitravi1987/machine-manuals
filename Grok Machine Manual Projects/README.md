# Grok Machine Manual Projects

Isolated sandbox for **Grok 4.5** machine-manual capability pilots.

---

## ALWAYS USE THIS PATH

**Machine Manuals root:**

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals
```

**Grok sandbox (all Grok creates go here):**

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\
```

| Do | Do not |
|----|--------|
| Create pilots, skills, docs under the path above | Create under `.grok\worktrees\...` or other clones |
| Use absolute paths when session cwd is a worktree | Assume “repo root” of the worktree is the real Machine Manuals folder |

---

## Isolation rule

- **Write only** under `Grok Machine Manual Projects\` on the Machine Manuals path above.
- **Do not modify** any existing files under `Projects\`, root `Skills\`, `CLAUDE.md`, or other Claude-era content unless Ravi asks.
- May **read** RA reports, photos, and Indo-MIM format references from `Projects\` for drafting.

## Grok-owned skills

| File | Purpose |
|------|---------|
| `GROK.md` | Session entrypoint + **mandatory path** |
| `Skills\SKILL.md` | Main trigger skill |
| `Skills\GROK_WORKFLOW_B.md` | Ingest → draft → generate |
| `Skills\GROK_OSM_FORMAT.md` | **V2.0 full Word format** (cover/TOC/HF/styles/colours — next projects) |
| `Skills\GROK_MACHINE_MANUALS_SKILL.md` | Content drafting rules |
| `Skills\GROK_MASTER_TEMPLATE.yaml` | Skeleton |

## Tooling

- Word: **python-docx** via pilot `working\build_osm.py` (Node may not be available)
- Excel: Python **openpyxl** via `working\build_open_actions.py`

## Pilot projects

| Folder | Machine | Status |
|--------|---------|--------|
| `P2-kemc-tilting-sample\` | KEMC Tilting Machine | **V1.1** Grok sample for Claude comparison |

### Latest P2 deliverables

```
...\Grok Machine Manual Projects\P2-kemc-tilting-sample\outputs\
  KEMC_TiltingMachine_OSM_GrokSample_V1.1.docx
  KEMC_TiltingMachine_OpenActions_GrokSample_V1.1.xlsx
```

## Label

All outputs are **Grok Sample / Draft** unless upgraded after customer review.
