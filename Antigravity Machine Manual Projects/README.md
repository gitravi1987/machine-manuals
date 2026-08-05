# Antigravity Machine Manual Projects

Isolated sandbox for **Antigravity** machine-manual capability pilots.

---

## ALWAYS USE THIS PATH

**Machine Manuals root:**

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals
```

**Antigravity sandbox (all Antigravity creates go here):**

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Antigravity Machine Manual Projects\
```

| Do | Do not |
|----|--------|
| Create pilots, skills, docs under the path above | Create under worktrees or temporary clones |
| Use absolute paths when session cwd is a worktree | Assume "repo root" of a worktree is the real Machine Manuals folder |

---

## Isolation rule

- **Write only** under `Antigravity Machine Manual Projects\` on the Machine Manuals path above.
- **Do not modify** any existing files under `Projects\`, `Grok Machine Manual Projects\`, root `Skills\`, `CLAUDE.md`, or other existing content unless Ravi asks.
- May **read** RA reports, photos, and Indo-MIM format references from `Projects\` for drafting.

## Antigravity-owned skills

| File | Purpose |
|------|---------|
| `ANTIGRAVITY.md` | Session entrypoint + **mandatory path** |
| `Skills\SKILL.md` | Main trigger skill |
| `Skills\ANTIGRAVITY_WORKFLOW_B.md` | Ingest → draft → generate |
| `Skills\ANTIGRAVITY_OSM_FORMAT.md` | Word format (Indo-MIM V5 style colours/sections) |
| `Skills\ANTIGRAVITY_MACHINE_MANUALS_SKILL.md` | Content drafting rules |
| `Skills\ANTIGRAVITY_MASTER_TEMPLATE.yaml` | Skeleton |

## Tooling

- Word: **python-docx** via pilot `working\build_osm.py`
- Excel: Python **openpyxl** via `working\build_open_actions.py`

## Pilot projects

| Folder | Machine | Status |
|--------|---------|--------|
| *TBD* | *Pending new pilots* | Initialized |

## Label

All outputs are **Antigravity Sample / Draft** unless upgraded after customer review.
