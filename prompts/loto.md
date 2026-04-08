# Prompt: Section 4 — LOTO Procedures

> Reference: `instructions.md` Section 3.2 | Template: `templates/section-4-loto.md`

---

## INPUT

- Filled Excel checklist Tab 5 (LOTO)
- Site photos of isolation points (LP-1 to LP-4)
- Risk assessment (LOTO section)
- Any existing LOTO procedure documents from customer

---

## TASK

Draft Section 4 — LOTO Procedures for [MACHINE_NAME]:
- 4.1 Energy Isolation Points table
- 4.2 De-energisation sequence (step by step)
- 4.3 Re-energisation sequence (step by step)
- 4.4 LOTO diagram placeholder
- 4.5 Open Actions for this section

---

## RULES

- Reference standards: ISO 12100:2010, ISO 13849-1:2015, IS 12059, Factories Act 1948
- Every isolation point must have: ID, energy source, type, isolation device, location, lock type
- De-energisation sequence must be numbered, step-by-step, with no steps skipped
- Re-energisation sequence must confirm all guards reinstalled before restart
- DANGER signal word mandatory at top of section per IEC 82079-1
- Never use passive voice: use imperative instructions (Turn, Press, Confirm)
- If any LOTO point location is unconfirmed — log as Open Action
- If mechanical stored energy method is unclear — log as Open Action
- Do not assume missing data

---

## OUTPUT FORMAT

- Markdown only
- Match template structure exactly
- Save output to: `/outputs/section-4-[MACHINE_NAME].md`
