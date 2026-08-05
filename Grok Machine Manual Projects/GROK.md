# GROK.md — Machine Manual Sandbox (Grok 4.5)

**Owner:** Certified Safety Professional  
**Read this at the start of every Grok OSM session in this sandbox.**

---

## 0. ALWAYS CREATE FILES HERE (mandatory path)

**Machine Manuals root (only allowed base for Grok outputs):**

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals
```

**Grok sandbox (create/edit only under this folder):**

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\
```

### Hard rules

| Rule | Detail |
|------|--------|
| **Always** | Put every new Grok pilot, skill update, `.docx`, `.xlsx`, JSON/YAML under the path above |
| **Never** | Create `Grok Machine Manual Projects` (or pilot outputs) under `.grok\worktrees\...`, temp clones, or any other drive/path unless Ravi explicitly overrides |
| **If session cwd is a worktree** | Still write to the **absolute** Machine Manuals path above — do not use relative `./Grok Machine Manual Projects` from the worktree |

Shorthand name used in this file: **Machine Manuals root** = the OneDrive Desktop path above.

---

## 1. Isolation

| Allowed | Forbidden |
|---------|-----------|
| Create/edit under `...\Machine Manuals\Grok Machine Manual Projects\**` | Modify existing Claude content: `Projects\`, root `Skills\`, `CLAUDE.md`, Master template, checklists (unless Ravi asks) |
| **Read** RA/photos/templates from `...\Machine Manuals\Projects\...` | Write pilot deliverables outside Machine Manuals root |

Read-only inputs may live under `Projects\...` (RA, photos, Indo-MIM format samples).

---

## 2. Skills to load (this folder)

All under  
`...\Machine Manuals\Grok Machine Manual Projects\`:

1. `Skills\SKILL.md` — main entry / triggers  
2. `Skills\GROK_WORKFLOW_B.md`  
3. `Skills\GROK_OSM_FORMAT.md`  
4. `Skills\GROK_MACHINE_MANUALS_SKILL.md`  
5. `Skills\GROK_MASTER_TEMPLATE.yaml`  

Environment tooling:

- **Word (this sandbox):** python-docx via pilot `working\build_osm.py`  
- **Excel:** openpyxl via pilot `working\build_open_actions.py`  
- Optional: `~/.grok/skills/docx/SKILL.md` / `xlsx/SKILL.md`  

---

## 3. Non-negotiable content rules

- Author/role: **Certified Safety Professional** only — no individual name  
- Never name RA firms (e.g. SICK) — use **Independent Safety Consultant** / **Machine Safety Assessment**  
- Never invent specs, features, or standard clause numbers  
- Missing data → **`[PLACEHOLDER — description, source, status]`** or Open Action  
- **No DANGER boxes** in the manual  
- **No DFM rules** unless the pilot is explicitly marked DFM  
- Appendices: **A = Maintenance Log**, **B = LOTO Log** only  
- Open Actions = standalone `.xlsx`, never inside the manual  
- Standards in use: ISO 12100, ISO 20607, IEC 82079-1, IS 4571, ISO 13849-1, ISO 13850, ANSI B11.19, Factories Act 1948  
- Never reference IEC 61508 or IEC 61800-5-2  

---

## 4. Format authority

`Skills\GROK_OSM_FORMAT.md` **V2.0** — full Word format standard for Grok pilots  
(cover, TOC field H1-only, Heading 1/2 styles, header Page N of N, footer CONFIDENTIAL,  
navy/Calibri palette, tables, flowcharts, alert boxes).  

Derived from Claude OSM Word Format V1.2 + Indo-MIM V5 visuals.  
Does **not** edit root `Skills\Word-format\`. Apply V2.0 on the **next** project generation.

---

## 5. Default workflow

Workflow B: RA + photos → `machine_data.json` + `section_content.yaml` → `.docx` + `.xlsx`  
(all under the absolute Grok sandbox path in §0).

See `Skills\GROK_WORKFLOW_B.md`.
