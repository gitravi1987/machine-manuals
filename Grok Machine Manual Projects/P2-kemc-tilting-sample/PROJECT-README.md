# P2 Grok Sample — KEMC Tilting Machine OSM

| Field | Value |
|-------|-------|
| Project code | P2-Grok-Sample |
| Machine | Tilting Machine (clutch plate assembly support) |
| Manufacturer | Karthick Engineering & Maintenance Consultants (KEMC) |
| Tier | B |
| Status | **Grok Sample / Draft** |
| Revision | **V1.1** (photo-backed control layout enrichment) |
| Purpose | Capability comparison: Grok 4.5 vs Claude P2 manuals |

## ALWAYS CREATE / KEEP FILES HERE

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\P2-kemc-tilting-sample\
```

Machine Manuals root:

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals
```

Do **not** create or keep a copy under `.grok\worktrees\...`.

## Isolation

All Grok pilot writes under `Grok Machine Manual Projects\` on the Machine Manuals path above only.

**No modifications** to root `Projects/`, root `Skills/`, `CLAUDE.md`, or Claude manuals.

## Read-only sources used

| Source | Path |
|--------|------|
| Machine Safety Assessment (primary) | `Projects/P2 - Karthik engineering/RA report/CD8AE7C8-9468-4C34-AE54-7B72CE6C1194Tilting_Machine_Report_V1.pdf` |
| Site photos | `Projects/P2 - Karthik engineering/Images/` |
| Format reference (sections/colours) | `Projects/P5 - Indo MIM/IndoMIM_BGSnap_OSM_V5.0.docx` + Grok `Skills/GROK_OSM_FORMAT.md` |

DFM rules: **not applied**.

## Deliverables (absolute base)

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\P2-kemc-tilting-sample\
```

| File | Location |
|------|----------|
| OSM Word | `outputs\KEMC_TiltingMachine_OSM_GrokSample_V1.1.docx` |
| Open Actions Excel | `outputs\KEMC_TiltingMachine_OpenActions_GrokSample_V1.1.xlsx` |
| Machine data | `inputs\machine_data.json` |
| Section draft | `inputs\section_content.yaml` |
| Photo refs (copies) | `inputs\photo-refs\` |
| Generators | `working\build_osm.py`, `working\build_open_actions.py` |

## Grok skills used

- `../Skills/SKILL.md` (entry)
- `../Skills/GROK_WORKFLOW_B.md`
- `../Skills/GROK_OSM_FORMAT.md`
- `../Skills/GROK_MACHINE_MANUALS_SKILL.md`
- `../GROK.md`

## Key facts extracted from RA

- Electrical: **230 V, single phase, 50 Hz**
- Pneumatic: **5 bar**
- Hydraulic: **NA**
- Modes: Manual / Automatic
- Capacity: one clutch plate per cycle
- Process: crane load → clamp → tilt → nut install → return → unload
- Safety: fixed mesh guard, Type 4 light curtain, two-hand cycle start, front E-Stop, power isolator, air isolation, SRPCS
- Risks: R001–R008

## Photo-backed additions (V1.1)

| Observation | Source photo |
|-------------|--------------|
| Dual left/right two-hand stations | full front |
| HMI on right control column | full front |
| E-Stop below HMI (ES-01) | full front |
| Rotary isolator lower right | full front + isolator close-up |
| Pneumatic FRL bank | full front |
| Hinged mesh guard door + crush warning | full front + guard sign |
| Clamp/tilt fixture with clutch plate | fixture photo |

## Self-QA checklist

- [x] Writes only under Grok Machine Manual Projects
- [x] No SICK / RA firm names in customer-facing text
- [x] Author role: Certified Safety Professional only
- [x] No DANGER boxes
- [x] No DFM content
- [x] Appendices A/B = Maintenance Log + LOTO Log only
- [x] Open Actions standalone xlsx (7 columns)
- [x] Specs match RA or marked PLACEHOLDER / Open Action
- [x] Indo-MIM-style navy `#1F3864` / Calibri formatting in generator

## Regenerate

```powershell
cd "C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\P2-kemc-tilting-sample"
python working\build_osm.py
python working\build_open_actions.py
```

## Compare with Claude

Claude P2 manuals (read-only for your comparison):

- `Projects/P2 - Karthik engineering/Tilting_Machine_OSM_v1.0.docx`
- `Projects/P2 - Karthik engineering/Tilting_Machine_Manual_FINAL.docx`
- Versioned `Karthik_engg_v_*.docx`

Suggested comparison axes: structure/colours vs Indo-MIM V5, RA fidelity, placeholder honesty, LOTO/E-stop completeness, forbidden-content slips.
