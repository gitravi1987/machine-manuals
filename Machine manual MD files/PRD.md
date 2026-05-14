FILE 4 of 7 — PRD.md
text
# PRD.md — Product Requirements Document

**Project:** Machine Manuals — AI-Assisted Industrial Manual Generation
**Version:** 1.0
**Date:** April 2026
**Author:** Ravikumar | Fortress Safety (Halma)
**Status:** Active

---

## 1. Problem Statement
Industrial machine operating manuals are often:
- Non-compliant with current ISO/IEC/ANSI standards
- Incomplete in hazard identification and safety instructions
- Inconsistent across machines and customers
- Time-consuming to produce manually without a structured system

---

## 2. Objective
Build a structured, AI-assisted workflow to produce accurate,
standards-compliant machine operating manuals for customers.

Each manual must:
- Identify all hazard zones per ISO 12100
- Reference safety distances per ISO 13857
- Document guard specifications per ISO 14120
- Specify interlocking requirements per ISO 14119
- Include operator and maintenance instructions per IEC 82079-1
- Document all safety gaps as Open Actions with liability disclaimers

---

## 3. Scope

### In Scope
- Operating manuals for customer-specific machines (Tier A/B/C)
- Safety sections: hazard ID, risk rating, protective measures
- Maintenance sections: LOTO, inspection intervals, lubrication
- Open Actions Register for unresolved safety gaps
- Compliance checklists against applicable standards
- DFM reviews for Indo MIM → Tata Electronics (Apple) only

### Out of Scope
- Electrical schematics (provided by customer — not created here)
- PLC programming documentation
- Commercial proposals or quotations
- DFM for non-Apple / non-Indo MIM projects

---

## 4. Project Register

| ID | Customer | Machine | Tier | Status | DFM |
|----|----------|---------|------|--------|-----|
| P1 | Accurate Machines | 48-Spindle Drilling | A | Complete | No |
| P2 | KEMC / Karthik Engg | Tilting Machine (Valeo Clutch) | B | In Progress | No |
| P3 | Valeo | LE Test Bench | A | Content Complete | No |
| P4 | TBD | Legacy Machines | B/C | Pending | No |
| DFM-P1 | Indo MIM | Tata Electronics / Apple | DFM | TBD | Yes |

---

## 5. Standards Compliance Requirements

| Standard | Scope | Mandatory |
|----------|-------|-----------|
| ISO 12100:2010 | Risk assessment & reduction | Yes |
| ISO 13857:2019 | Safety distances | Yes |
| ISO 14120:2015 | Guards — design & construction | Yes |
| ISO 14119:2013 | Interlocking devices | Yes |
| ISO 13855:2010 | Positioning of safeguards | Yes |
| ISO 13850:2015 | Emergency stop function | Yes |
| ISO 13849-1:2023 | Safety-related control systems (PLr) | If applicable |
| IEC 62061:2021 | Functional safety (SIL) | If applicable |
| IEC 82079-1:2019 | Instructions for use | Yes |
| IS 4571:2008 | Indian machinery safety standard | Yes |
| IS 12100:2012 | Indian adoption of ISO 12100 | Yes |
| Factories Act 1948 | Indian industrial law | Yes |
| ANSI B11.0 / B11.19 | General machine safety (US reference) | Reference |

---

## 6. Deliverables Per Project

| Deliverable | Tier A | Tier B | Tier C |
|------------|--------|--------|--------|
| Full Manual (.docx) | Yes | Yes | Yes |
| Full Manual (.pdf) | Yes | Yes | Yes |
| Quick Reference (.docx/.pdf) | Yes | Optional | No |
| Open Actions Register (.xlsx) | Yes | Yes | Yes |
| Compliance Audit Trail (.docx) | Yes | Yes | Yes |

---

## 7. Pricing & Timeline

| Tier | Price | Timeline |
|------|-------|----------|
| A — Complete data | ₹15,000–20,000 | 14–21 days |
| B — Partial data | ₹10,000–12,000 | 10–14 days |
| C — Legacy/minimal | ₹8,000–10,000 | 7–10 days |

Add-ons:
- Third-party RA (if not provided): +₹20,000–40,000
- Quick Reference for Tier B/C: +₹3,000–5,000
- Schematics digitization: +₹5,000–10,000 per schematic
- HMI alarm code extraction: +₹2,000–3,000

---

## 8. AI Toolchain

| Tool | Role |
|------|------|
| Perplexity | Standards research, clause verification, citations |
| Claude | Drafting, structuring, compliance checking |
| ChatGPT | Review, rephrasing, clarity improvements |
| GitHub | Version control for all documents |

---

## 9. Success Criteria

- Manual passes internal review by B11 LMSS auditor (Ravikumar)
- All safety clauses traceable to specific standard + clause number
- Zero fabricated standard references
- All safety gaps logged in Open Actions Register — none skipped
- Customer sign-off received before final delivery
- Customer-ready document delivered as .docx (editable) + .pdf (locked)

---

## 10. Out of Scope (Explicit Exclusions)

- DFM reviews for non-Apple / non-Indo MIM projects
- Electrical schematics creation (provided by customer)
- PLC programming documentation
- Commercial proposals or quotations
- Notion — not used in this workflow

---

## 11. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Customer delays sending photos/schematics | Timeline slip | Use image placeholders; log as Open Action |
| Risk assessment not available | Cannot start Tier A/B | Recommend third-party RA first |
| Safety gap found during writing | Liability exposure | Document as Open Action with disclaimer |
| Legacy machine — no documentation | Tier C only | On-site observation + operator interview |
| Fabricated standard clause | Legal risk | Perplexity verification before every citation |