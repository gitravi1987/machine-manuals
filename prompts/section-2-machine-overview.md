# Prompt: Section 2 — Machine Overview

> Load this prompt when drafting Section 2 of any machine manual.
> Reference: `instructions.md` Section 3.2 for full writing guidelines.

---

## INPUT

Provide the following before running this prompt:
- Filled Excel checklist (Tab 1: Cover, Tab 2: Machine ID, Tab 3: Tech Specs)
- Site photos: machine front, rear, nameplate, control panel
- Risk assessment document (for machine type and intended use)
- Any existing OEM manual or datasheet

---

## TASK

Draft Section 2 — Machine Overview for [MACHINE_NAME] using:
1. The filled template: `templates/section-2-machine-overview.md`
2. All data from the INPUT documents above
3. The writing rules below

Structure the output to match the template exactly:
- 2.1 Machine Identification (Nameplate Data)
- 2.2 Intended Use
- 2.3 Key Technical Specifications
- 2.4 Machine Layout (image placeholder if photo not yet provided)
- 2.5 Personnel and Roles
- 2.6 Open Actions for this section

---

## RULES

- Follow ISO 12100:2010 for intended use and foreseeable misuse statements
- Follow IEC 82079-1:2019 for structure and language of instructions
- Do NOT assume or fabricate any nameplate data — use only what is provided
- If any field is missing — insert placeholder [FIELD_NAME] and log as Open Action
- Use clear, operator-friendly language — avoid jargon
- Tone: professional, authoritative, safety-focused
- Output in Markdown matching template structure

---

## OUTPUT FORMAT

- Markdown only
- Match template structure exactly
- Include image placeholder for machine layout if photo not provided
- List all Open Actions at end of section under 2.6
- Save output to: `/outputs/section-2-[MACHINE_NAME].md`
