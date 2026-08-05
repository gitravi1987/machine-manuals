# P7 — Rani Enterprises | Robotic Sealant Dispenser Machine

| Field | Value |
|-------|-------|
| Project code | P7-Rani-Sealant |
| Machine | Robotic Sealant Dispenser Machine |
| Manufacturer (OEM) | Rani Enterprises |
| End user | **[PLACEHOLDER — end-user facility]** |
| Status | **V1.0 generated — Draft for review** |
| Revision | V1.0 |
| Label | Draft |

## ALWAYS CREATE / KEEP FILES HERE

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\P7 - Rani Enterprises\
```

Do **not** create copies under `.grok\worktrees\...`.

## Isolation

Write only under `Grok Machine Manual Projects\` on the Machine Manuals path.  
Do not modify Claude-era `Projects\`, root `Skills\`, or `CLAUDE.md` unless Ravi asks.

## Inputs available

| Source | Status |
|--------|--------|
| Site photos (`Images\`) | ✅ 31 photos (28 July 2026) |
| Project README notes | ✅ process + energy notes |
| Machine Safety Assessment (RA) | ❌ **Not available** |
| Electrical schematic | ❌ Customer will insert later |
| Pneumatic schematic | ❌ Customer will insert later |
| PLC backup / full alarm list | ❌ Partial HMI screenshots only |
| Nameplate power / serial | ❌ Label only (machine title) |

## Section map

| Sec | Title |
|-----|-------|
| 1 | Front Matter |
| 2 | Machine Overview |
| 3 | Hazard Identification |
| 4 | Lockout / Tagout (LOTO) |
| 5 | Emergency Stop |
| 6 | Operating Instructions |
| 7 | Maintenance & Care |
| 8 | HMI, Alarms & Controls |
| 9 | Safety Features, Schematics & Compliance |
| App A | Maintenance Log Template |
| App B | LOTO Log Template |

## Key photo-backed facts

| Observation | Source image(s) |
|-------------|-----------------|
| Machine title label | Nameplate.jpg, Full view Front.jpg |
| Fisnar F4303N ADVANCE robot | Component on tray.jpg, two hand button full view.jpg |
| Fisnar blue dispenser cartridge | Dispenser.jpg |
| Dual two-hand + RESET + machine E-Stop | left/right push button photos, two hand button full view.jpg |
| Robot controller E-Stop | component tray button.jpg |
| Mitsubishi HMI “GLUE DISPENSER” | HMI Modes / Process / Settings / Alarms |
| Models JPTP / MGTP / APTDPT | HMI Modes 2.jpg |
| Dispenser inlet 2–3 bar; idle parking 3.0 min | HMI Settings.jpg |
| Live alarms Air Pressure Low, Robot Emergency [X12], Front Auto Door open Error [X6] | HMI Alarms.jpg |
| Machine Emergency Pressed [X0] | HMI Process.jpg |
| Rotary POWER ON/OFF isolator (LK OFF-salzer) | Isolato switch.jpg |
| SMC FRL + ~6 bar gauge | Pneumatic FRL.jpg |
| Omron GLS-M1 non-contact side-door switch | Omron safety switch.jpg |
| Mitsubishi PLC + Mean Well NDR-240-24 | PLC panel open.jpg |
| Parking / purging cups | dispenser parking.jpg, dispenser purging.jpg |
| Front auto door (no light curtain per intake) | README + HMI Settings “Front Automatic Safety Door ON” |

## Deliverables

| File | Location |
|------|----------|
| Machine data | `inputs\machine_data.json` |
| Section draft | `inputs\section_content.yaml` |
| OSM Word | `outputs\RaniEnterprises_RoboticSealantDispenser_OSM_V1.0.docx` |
| Open Actions Excel | `outputs\RaniEnterprises_RoboticSealantDispenser_OpenActions_V1.0.xlsx` |
| Generators | `working\build_osm.py`, `working\build_open_actions.py` |
| This tracker | `PROJECT-README.md` |

## Regenerate

```powershell
cd "C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Grok Machine Manual Projects\P7 - Rani Enterprises"
python working\build_osm.py
python working\build_open_actions.py
```

## Grok skills used

- `../GROK.md`
- `../Skills/SKILL.md`
- `../Skills/GROK_WORKFLOW_B.md`
- `../Skills/GROK_OSM_FORMAT.md`
- `../Skills/GROK_MACHINE_MANUALS_SKILL.md`

## Self-QA

- [x] Writes only under Grok Machine Manual Projects
- [x] Manufacturer = Rani Enterprises; end user placeholder
- [x] No RA firm names; role = Certified Safety Professional
- [x] No DANGER boxes
- [x] Specs from photos/README or PLACEHOLDER / Open Action
- [x] Appendices A/B = log templates only
- [x] Open Actions standalone xlsx (7 columns)
- [x] Customer-facing text does not mention internal commercial tier / page targets
- [x] V1.0 docx + xlsx generated
