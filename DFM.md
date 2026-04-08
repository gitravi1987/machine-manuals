# DFM.md — Design for Manufacturability Instructions

> **IMPORTANT: DFM scope is LIMITED to Apple projects (Indo MIM) only.**
> For all other projects, use standard Machine Manual mode.

---

## Purpose
This file defines how AI tools should help with **Design for Manufacturability** (DFM) reviews related to machine designs, guarding solutions, and safety components. It is separate from operating manuals and focuses on making designs easier, cheaper, and more reliable to manufacture and assemble.

---

## Scope of DFM Work
- Guard and enclosure design (materials, fastening, panelization)
- Brackets, mounting plates, and mechanical interfaces for safety devices
- Cable routing, conduit, and interface design for interlocks and safety switches
- Standardization of components (fasteners, profiles, sensors)
- Tolerance, fit, and assembly sequence considerations
- Design simplifications that reduce manufacturing steps or special processes

DFM must **never** compromise safety or standards compliance. If a DFM suggestion conflicts with ISO/ANSI/IEC safety requirements, safety wins.

---

## AI Roles in DFM

### Perplexity
- Research manufacturing best practices for sheet metal, fabrication, machining, welding, and assembly
- Compare options (e.g., welded vs. bolted guards) with pros/cons
- Provide cost/complexity implications at a high level

### Claude
- Analyze a given design description or sketch and suggest DFM improvements
- Rewrite design notes and internal specs to be clearer for fabrication vendors
- Generate checklists for design reviews (DFM + safety combined)
- Propose design alternatives that reduce part count or simplify assembly while maintaining safety intent

### ChatGPT
- Review DFM proposals for clarity and practicality
- Help convert technical DFM review comments into clean action items
- Suggest better wording for internal design guidelines

---

## DFM Review Checklist (High-Level)

When asking AI to perform a DFM review, provide:
- Brief machine description
- Guarding concept (materials, thickness, mounting)
- Safety devices used (interlocks, solenoids, light curtains, etc.)
- Manufacturing process assumptions (laser cut + bend, machining, extrusion, welding, etc.)

Ask the AI to evaluate at least:

1. **Part Count & Complexity**
   - Can parts be combined without affecting safety?
   - Any overly complex shapes that are hard to cut/bend/machine?

2. **Standardization**
   - Can fastener types and sizes be reduced?
   - Can profiles or plates be reused across machines?

3. **Fabrication Friendliness**
   - Reasonable bend radii and tool access?
   - Avoid very tight internal corners or unnecessary small features

4. **Assembly & Maintenance**
   - Can guards be mounted and removed without dismantling half the machine?
   - Is there enough access for tools, hands, and replacement parts?

5. **Safety & Compliance**
   - No change should reduce safety distances, guard strength, or interlock reliability
   - If any DFM idea touches a safety parameter, mark it: `REQUIRES SAFETY REVIEW`

---

## How to Use This File
- For manual work: Open `DFM.md` before prompting AI so you remember the constraints
- For AI system prompts: Paste relevant sections of `DFM.md` as system/instruction context
- For reviews: Use the DFM checklist headings as bullet points and ask AI to comment under each

---

## Important Rule

> **DFM suggestions must not override safety standards.**
> If a DFM improvement conflicts with ISO 12100, ISO 13857, ISO 14120, ISO 14119, or related standards, mark it clearly and treat it as **not acceptable** unless re-engineered with full safety review.

---

## Applicable Projects

| Project | DFM Applicable? |
|---------|----------------|
| P1 - Accurate Machines | NO |
| P2 - Karthik Engineering | NO |
| P3 - Valeo | NO |
| IndoMIM-Apple-P1 | YES |
| Future Apple projects | YES |
| All other projects | NO |
