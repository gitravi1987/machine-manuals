FILE 7 of 7 — PROJECT-README-TEMPLATE.md
text
# PROJECT-README-TEMPLATE.md
# Copy this file into each project folder and rename to PROJECT-README.md
# Fill in all fields marked with [brackets]
# Delete this top instruction block before committing

---

# [Customer Name] — [Machine Name/Type]

**Project ID:** [P1 / P2 / P3 / IndoMIM-Apple-P1 / etc.]
**Customer:** [Company name]
**End User:** [If different from customer — e.g., Valeo, Apple/Tata]
**Machine:** [Make, model, year, serial number]
**Location:** [Plant name, city]
**Auditor:** Ravikumar | B11 LMSS Cert No. [XXXXX]
**Date Started:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]
**Manual Tier:** [A / B / C]
**DFM Project:** [Yes — Indo MIM Apple only / No]

---

## Project Status

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1: Data Consolidation | [ ] Not started / [ ] In Progress / [ ] Complete | |
| Phase 2: Manual Writing | [ ] Not started / [ ] In Progress / [ ] Complete | |
| Phase 3: Review & Refinement | [ ] Not started / [ ] In Progress / [ ] Complete | |
| Phase 4: Word & PDF Generation | [ ] Not started / [ ] In Progress / [ ] Complete | |

---

## Machine Summary

- **Machine Type:** [e.g., Drilling, Tilting, Test Bench, Press]
- **Power Source:** [e.g., 3-phase 415V / Pneumatic 6.5 bar / Hydraulic]
- **Control System:** [Hardwired / PLC — make & model / HMI — make & model]
- **Age:** [Year of manufacture or approx. age]
- **Last Maintained:** [Date or "Unknown"]
- **No. of Operators:** [X per shift]
- **Shifts per Day:** [1 / 2 / 3]

---

## Tier Rationale

**Tier [A/B/C] selected because:**

| Item | Available |
|------|-----------|
| Risk Assessment | Yes / Partial / No |
| Electrical Schematic | Yes / Partial / No |
| Pneumatic Schematic | Yes / Partial / No |
| Hydraulic Schematic | Yes / Partial / No |
| PLC / HMI Documentation | Yes / Partial / No |
| Operating Procedures | Yes / Informal / No |
| Maintenance Records | Yes / Partial / No |
| LOTO Points Labeled | Yes / Partial / No |
| Site Photos | Yes / Partial / No |

---

## Hazard Summary (from Risk Assessment)

| ID | Hazard | Zone | Severity | Probability | Risk Level |
|----|--------|------|----------|-------------|------------|
| H1 | [e.g., Rotating spindle] | [e.g., Top of machine] | [H/M/L] | [H/M/L] | [H/M/L] |
| H2 | | | | | |
| H3 | | | | | |

*(Fill from RA document — do not fabricate)*

---

## LOTO Points Summary

| ID | Energy Source | Isolation Method | Location on Machine |
|----|--------------|-----------------|-------------------|
| LP-1 | Electrical | Main disconnect rotary switch | [e.g., Right side panel] |
| LP-2 | Pneumatic | Ball valve + lockout hasp | [e.g., Left base] |
| LP-3 | Hydraulic | [Method] | [Location] |
| LP-4 | Mechanical | [Method] | [Location] |

---

## Open Actions Register

| ID | Item | Category | Status | Responsibility | Target Date |
|----|------|----------|--------|----------------|-------------|
| OA-001 | [e.g., Electrical schematic not available] | Documentation | Pending | Customer | [date] |
| OA-002 | [e.g., Two-hand start not implemented] | Safety Gap | Documented | [Customer/Engg] | [date] |

**Category options:** Safety Gap / Documentation / Schematic / Software / Maintenance / Other
**Status options:** Documented / Pending / Closed

---

## Folder Contents
[Pxx-customer-name]/
├── PROJECT-README.md ← This file
├── manual/ ← All drafts → final .docx + .pdf
│ ├── [Customer]_[Machine]_TierX_Manual_v1.md
│ ├── [Customer]_[Machine]_TierX_Manual_v1.docx
│ ├── [Customer]_[Machine]_TierX_Manual_v1.pdf
│ └── [Customer]_[Machine]_TierX_QuickRef_v1.docx (Tier A only)
├── risk-assessment/ ← RA documents from SICK/TÜV (read-only)
│ └── [Customer]RA[date].pdf
├── pictures/ ← Site photos
│ └── [Pxx]Photo[seq]_[Subject]_[Detail].jpg
├── schematics/ ← Electrical / Pneumatic / Hydraulic
│ └── [Customer][Type]_Schematic[rev].pdf
└── compliance/ ← Audit trail + Open Actions
├── [Customer]_ComplianceAudit_v1.docx
└── [Customer]_OpenActions_v1.xlsx

text

> For Indo MIM Apple projects only — add:
└── dfm/
├── DFM-review-template.md
└── DFM-review-[desc]-v1.md

text

---

## Deliverables Checklist

- [ ] Full Manual (.docx) — editable
- [ ] Full Manual (.pdf) — locked
- [ ] Quick Reference (.docx/.pdf) — Tier A only
- [ ] Open Actions Register (.xlsx)
- [ ] Compliance Audit Trail (.docx)
- [ ] Customer sign-off received

---

## Standards Applied

- ISO 12100:2010 — Risk Assessment
- ISO 13849-1:2015 — Safety Control Systems
- ISO 13850:2015 — Emergency Stop
- ISO 14120:2015 — Guards
- ISO 14119:2013 — Interlocking Devices
- ISO 13857:2019 — Safety Distances
- IEC 82079-1:2019 — Instructions for Use
- IS 4571:2008 — Indian Machinery Safety
- Factories Act 1948
- ANSI B11.19:2010 — Reference

---

## Liability Disclaimer

This Operating & Safety Manual has been prepared by Ravikumar,
B11 LMSS Licensed Machinery Safety Specialist (Cert. #[XXXXX]),
in accordance with ISO 12100:2010, ANSI B11.19:2010, and IS 4571:2008.

Where original technical data was unavailable, professional judgment
and industry best practices have been applied. All such areas are
noted as Open Actions in the appendix.

The customer is responsible for final review and verification of all
information in this manual before the machine is placed into service.

**Auditor:** Ravikumar | B11 LMSS Cert. #[XXXXX]
**Date:** [YYYY-MM-DD]
**Status:** [ ] Draft | [ ] Under Review | [ ] Approved