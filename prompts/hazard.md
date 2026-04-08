# Prompt: Section 3 — Hazard Identification & Risk Assessment

> Reference: `instructions.md` Section 3.2 | Template: `templates/section-3-hazard-risk.md`

---

## INPUT

- Risk assessment document (SICK / TUV / third-party RA)
- Filled Excel checklist Tab 4 (Safety & Hazards)
- Site photos showing machine zones and guarding

---

## TASK

Draft Section 3 — Hazard Identification & Risk Assessment for [MACHINE_NAME]:
- 3.1 Risk Assessment Methodology
- 3.2 Hazard Identification Table (all hazards from RA)
- 3.3 Residual Risk Disclosure
- 3.4 Open Actions for this section

---

## RULES

- Populate hazard table ONLY from the RA document — do not fabricate hazards
- Every hazard must have: ID, description, zone, severity, probability, risk level, control measure, residual risk
- Risk methodology must reference ISO 12100:2010
- If RA is missing for any hazard zone — log as Open Action
- If mismatch between RA recommendation and actual machine — log as Open Action
- Use signal words per IEC 82079-1: DANGER / WARNING / CAUTION / NOTICE
- Do not assume missing data

---

## OUTPUT FORMAT

- Markdown only
- Match template structure exactly
- Save output to: `/outputs/section-3-[MACHINE_NAME].md`
