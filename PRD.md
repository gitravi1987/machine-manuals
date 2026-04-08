# PRD.md — Product Requirements Document

## Project Name: Machine Manuals — AI-Assisted Industrial Manual Generation
**Version:** 1.0
**Date:** April 2026
**Author:** Ravikumar, Fortress Safety
**Status:** Active

---

## 1. Problem Statement
Industrial machine operating manuals are often:
- Non-compliant with current ISO/IEC/ANSI standards
- Incomplete in hazard identification and safety instructions
- Inconsistent across machines and customers
- Time-consuming to produce manually from scratch

---

## 2. Objective
Build a structured, AI-assisted workflow to produce **accurate, standards-compliant machine operating manuals** for Fortress Safety customers. Each manual must:
- Identify all relevant hazard zones per ISO 12100
- Reference applicable safety distances per ISO 13857
- Document guard specifications per ISO 14120
- Specify interlocking requirements per ISO 14119
- Include operator and maintenance instructions per IEC 82079-1

---

## 3. Scope

### In Scope
- Operating manuals for customer-specific machines
- Safety sections: hazard identification, risk rating, protective measures
- Maintenance sections: lockout/tagout, inspection intervals
- Compliance checklists against applicable standards
- Multi-language adaptation (English primary; Tamil/Hindi as needed)

### Out of Scope
- Electrical schematics (separate deliverable)
- PLC programming documentation
- Commercial proposals or quotations
- DFM reviews for non-Apple / non-Indo MIM projects

---

## 4. Project List

| Project ID | Customer | Machine Type | Status | Priority |
|------------|----------|-------------|--------|----------|
| P1 | Accurate Machines | 48-Spindle Drilling | Complete | High |
| P2 | Karthik Engineering | Tilting Machine | In Progress | High |
| P3 | Valeo | LE Test Bench | Content Complete | Medium |
| IndoMIM-Apple-P1 | Indo MIM (Apple) | TBD | Planned | High |
| P4 | Indo MIM Chennai | TBD | Planned | High |

---

## 5. Standards Compliance Requirements

| Standard | Scope | Mandatory |
|----------|-------|-----------|
| ISO 12100:2010 | Risk assessment & reduction | Yes |
| ISO 13857:2019 | Safety distances | Yes |
| ISO 14120:2015 | Guards — design & construction | Yes |
| ISO 14119:2013 | Interlocking devices | Yes |
| ISO 13855:2010 | Positioning of safeguards | Yes |
| ISO 13849-1:2015 | Safety-related control systems (PLr) | If applicable |
| IEC 62061:2021 | Functional safety (SIL) | If applicable |
| IEC 82079-1:2019 | Instructions for use | Yes |
| ANSI B11.0 | General machine safety | Reference |
| IS 4571:2008 | Indian machinery safety | Reference |
| Factories Act 1948 | Indian industrial law | Reference |

---

## 6. Deliverables Per Project
- [ ] Machine description & specification sheet
- [ ] Hazard identification worksheet
- [ ] Risk assessment matrix
- [ ] Safety distances calculation sheet (ISO 13857)
- [ ] Guard specification document (ISO 14120)
- [ ] Interlocking device list (ISO 14119)
- [ ] Operating manual (draft → review → final)
- [ ] Maintenance manual section
- [ ] Compliance checklist
- [ ] Open Actions Register

---

## 7. Manual Tier System

| Tier | Scope | Price | Timeline |
|------|-------|-------|----------|
| A | Complete data — all 14 sections | ₹15,000–20,000 | 14–21 days |
| B | Partial data — Sections 1–7 full, 8–10 placeholders | ₹10,000–12,000 | 10–14 days |
| C | Legacy/minimal — Sections 1–7 + functional diagrams | ₹8,000–10,000 | 7–10 days |

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

## 10. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Customer delays sending photos/schematics | Timeline slip | Use image placeholders; log as Open Action |
| Risk assessment not available | Cannot start Tier A/B | Recommend third-party RA first |
| Safety gap found during writing | Liability exposure | Document as Open Action with disclaimer |
| Legacy machine — no documentation | Tier C only | On-site observation + operator interview |
| Fabricated standard clause | Legal risk | Perplexity verification before every citation |

---

## 11. Project Archive

| ID | Customer | Machine | Tier | Status | Key Learning |
|----|----------|---------|------|--------|--------------|
| P1 | Accurate Machines | 48-Spindle Drilling | A | Complete | Rich operator interviews improve Sections 9–11 |
| P2 | KEMC / Karthik Engg | Tilting Machine | B | In Progress | Document safety gaps as Open Actions professionally |
| P3 | Valeo | LE Test Bench | A | Content Complete | Legacy machine can still be Tier A with good customer data |
