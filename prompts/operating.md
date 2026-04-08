# Prompt: Section 6 — Operating Instructions

> Reference: `instructions.md` Section 3.2 | Template: `templates/section-6-operating-instructions.md`

---

## INPUT

- Filled Excel checklist Tab 8 (Controls & Ops)
- Filled Excel checklist Tab 9 (Operator Interview)
- Site photos of control panel, startup sequence, HMI
- Risk assessment (operating cycle section)

---

## TASK

Draft Section 6 — Operating Instructions for [MACHINE_NAME]:
- 6.1 Pre-Start Checks (every shift checklist)
- 6.2 Startup Procedure (step by step)
- 6.3 Normal Operating Cycle (step by step)
- 6.4 Shutdown Procedure (step by step)
- 6.5 Open Actions for this section

---

## RULES

- Reference standards: IEC 82079-1:2019, ISO 12100:2010
- All procedures must be numbered, step-by-step, imperative voice
- Pre-start checks must be in checkbox format
- Never use passive voice
- Cycle time and production rate: use actual values from checklist or operator interview
- If operating mode selector positions are unclear — log as Open Action
- If cycle description is incomplete — log as Open Action and insert placeholder
- WARNING signal word required before operating cycle description
- NOTICE required before any step that could cause product damage
- Do not assume missing data

---

## OUTPUT FORMAT

- Markdown only
- Match template structure exactly
- Save output to: `/outputs/section-6-[MACHINE_NAME].md`
