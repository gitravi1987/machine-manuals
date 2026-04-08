# Prompt: Section 7 — Maintenance & Care

> Reference: `instructions.md` Section 3.2 | Template: `templates/section-7-maintenance.md`

---

## INPUT

- Filled Excel checklist Tab 9 (Maintenance)
- Operator interview notes (Tab 9 of checklist)
- OEM datasheet or maintenance manual (if available)
- Site photos of lubrication points, filters, inspection zones

---

## TASK

Draft Section 7 — Maintenance & Care for [MACHINE_NAME]:
- 7.1 Maintenance Schedule (frequency, task, who does it)
- 7.2 Lubrication Schedule
- 7.3 Spare Parts List
- 7.4 Troubleshooting Guide
- 7.5 Open Actions for this section

---

## RULES

- DANGER signal word required at top of section (LOTO before all maintenance)
- Maintenance schedule must include: Every shift, Weekly, Monthly, 6-Monthly, Annual tasks
- Lubrication specs must come from OEM datasheet or site practice — not fabricated
- Spare parts list: include only what can be confirmed from site observation or customer input
- Troubleshooting: common symptoms only — do not fabricate fault codes
- If lubrication spec not confirmed — log as Open Action
- If spare parts list is incomplete — log as Open Action
- Do not assume missing data

---

## OUTPUT FORMAT

- Markdown only
- Match template structure exactly
- Save output to: `/outputs/section-7-[MACHINE_NAME].md`
