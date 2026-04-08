# Prompt: Section 13 — Compliance & Certifications

> Reference: `instructions.md` Section 3.3 | Template: `templates/section-13-compliance.md`

---

## INPUT

- Completed manual draft (all sections)
- Risk assessment document (for standards verification)
- Filled Excel checklist Tab 10 (Compliance & Regulatory)
- Open Actions Register (current status)

---

## TASK

Draft Section 13 — Compliance & Certifications for [MACHINE_NAME]:
- 13.1 Standards Applied (table of all standards used)
- 13.2 Compliance Statement
- 13.3 Compliance Audit Checklist (verify every section)
- 13.4 Customer Sign-Off block
- 13.5 Open Actions for this section

Also perform a full compliance audit of the complete manual:
- Verify every section has required content
- Check no contradictions between sections
- Confirm all hazards from RA are addressed
- Confirm all Open Actions are documented

---

## RULES

- Only cite standards that are actually used in this manual — do not add extras
- Compliance statement must reference: RA document, site observation date, documents provided
- Audit checklist: mark each item as Verified / Not Verified / Open Action
- Flag any contradiction between sections as an Open Action
- Liability disclaimer must be included verbatim from `instructions.md` Section 4.3
- Do not mark compliance as PASS if any safety-critical Open Action is unresolved

---

## OUTPUT FORMAT

- Markdown only
- Match template structure exactly
- Save output to: `/outputs/section-13-[MACHINE_NAME].md`
