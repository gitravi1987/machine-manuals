# Prompt: Open Actions Register

> Reference: `instructions.md` Section 4.2 | Template: `templates/open-actions-template.md`

---

## INPUT

- All drafted manual sections (Sections 2 through 13)
- Risk assessment document
- All Open Actions logged during section drafting (OA-X-001 format)
- Customer confirmation of any resolved items

---

## TASK

Generate the complete Open Actions Register for [MACHINE_NAME]:
1. Consolidate ALL Open Actions from every section into one master register
2. Assign sequential IDs (OA-001, OA-002...)
3. Categorise each item
4. Assign responsibility and target date
5. Add liability disclaimer
6. Add customer sign-off block

---

## RULES

Create an Open Action when:
- Data is missing or unconfirmed
- RA recommendation is not implemented on the actual machine
- Any schematic is missing or unverified
- Any safety function PL/SIL rating is not confirmed
- Any contradiction is found between sections
- Any assumption was made due to lack of data

Do NOT:
- Mark any safety-critical item as Closed without customer confirmation
- Skip or ignore any gap identified during drafting
- Assume items will be resolved — document them

Categories: Safety Gap / Documentation / Schematic / Software / Maintenance / Other
Status: Pending / Documented / Closed

---

## OUTPUT FORMAT

- Markdown only
- Match template structure exactly: `templates/open-actions-template.md`
- Save output to: `/outputs/open-actions-[MACHINE_NAME].md`
- This file must also be exported as .xlsx for customer delivery
