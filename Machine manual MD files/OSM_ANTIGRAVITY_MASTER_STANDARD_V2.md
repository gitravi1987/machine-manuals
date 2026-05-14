# MACHINE MANUAL CREATION — GOOGLE ANTIGRAVITY MASTER STANDARD V2

**For: Certified Safety Professional's Machine Safety Documentation**
**Status: Active (V2)**
**Last Updated: May 2026**

---

## 1. WORKFLOW & SYSTEM INSTRUCTIONS

This is the **single source of truth** for all Operating & Safety Manuals generated via Google Antigravity. It replaces all prior `CLAUDE.md`, `instructions.md`, and multi-LLM prompts.

**Core Rules for AI Generation:**
- You are a technical writing assistant and safety standards verifier.
- Ensure brevity and clarity. Do not hallucinate standards. 
- You must follow this formatting standard exactly when generating `.docx` or Markdown content.
- Replace all missing values with placeholders formatted strictly as **[BOLD TEXT]** (e.g. **[MACHINE NAME]**). No grey boxes or italics.

---

## 2. PROJECT TIERING

Determine the manual tier based on available data before starting:

| Tier | Data Condition | Output |
|---|---|---|
| **A — Complete** | Full RA + schematics + PLC + photos | Full manual (all sections) |
| **B — Partial** | RA available, some schematics missing | Manual + Placeholders as **[BOLD TEXT]** |
| **C — Legacy** | Minimal data / site visit only | Sections 1-7 complete, functional diagrams |

---

## 3. DOCUMENT STRUCTURE & FLOW (V2)

The document must strictly follow this order and formatting. **Do not deviate.**

### 3.1 Cover Page & Front Matter (Merged Section 1)
*This section merges the Cover Page and Front Matter to avoid duplication.*

- **Title Block:** `OPERATING & SAFETY MANUAL` / `[MACHINE NAME]`
- **Document Control Table:** Contains Document Title, Document Number, Revision, Date, Status. *(Note: The "Prepared by" column has been removed).*
- **Author:** "Certified Safety Professional" (Do not use personal names like "Ravikumar").
- **Liability Disclaimer:** Place the liability disclaimer here on the front page. **Do not repeat the liability disclaimer in Section 13.**
- **Table of Contents:** Include a 50% shortened TOC that lists **only H1 headings**. Do not repeat the TOC anywhere else in the document.

### 3.2 Machine Overview (Section 2)
- Summarize nameplate, specs, intended use, layout.
- **Rule:** Do not include any Warning boxes in Section 2.4.

### 3.3 Hazard ID & Risk Assessment (Section 3)
- **Constraint:** This section must be **compacted to a maximum of 2 pages**.
- Do not reproduce exhaustive hazard tables (the customer receives the RA file separately).
- Provide only a brief summary of the ISO 12100 methodology and a high-level summary of risks.
- **Rule:** Remove all WARNING boxes from Section 3.

### 3.4 LOTO Procedures (Section 4)
- **Section 4.2 (Energy Isolation Table):** Must include these columns: `Energy Type` | `Image` | `Isolation Method`. Use ISO 7010 energy type images in the `Image` column.
- **Section 4.3:** No DANGER boxes allowed in this subsection.
- **Sections 4.4 & 4.5 (De-energization/Re-energization):** Do not write long text. Replace entirely with a **Simple Flowchart** (Design: Blue borders, white background).

### 3.5 Emergency Stop (Section 5)
- **Sections 5.4 & 5.5:** Replace procedural text entirely with a **Flowchart**.

### 3.6 Operating Instructions (Section 6)
- **Sections 6.4, 6.5, 6.7, 6.8, 6.9:** Replace textual instructions with **Flowcharts**.
- Ensure any extraneous WARNINGs from these procedural sections are removed to maintain flow.

### 3.7 Maintenance & Care (Section 7)
- Scheduled maintenance (Weekly, Monthly, Six-Monthly).

### 3.8 Schematics (Sections 8, 9, 10)
- Electrical, Pneumatic, Hydraulic. Use **[BOLD TEXT]** for placeholders if missing.

### 3.9 HMI Alarms (Section 11)
- **Section 11.4:** Replace textual instructions with a **Flowchart**.

### 3.10 Safety Features (Section 12)
- **Section 12.2:** Replace textual context with a **Flowchart** and reduced text.
- **Section 12.5:** Reduce context to concise **Bullet Points**.
- Ensure no DANGER boxes are placed near the end of this section.

### 3.11 Compliance & Sign-off (Section 13)
- **Section 13.2:** List applicable standards (ISO 12100, etc.).
- **Author Reference:** Use "Certified Safety Professional" only.
- **Liability Section:** Must be removed from here (it belongs only in Section 1).
- **Single Sign-off Block:** Replace sections 13.5, 13.6, 13.7 with a single, unified "Authorizations" block at the very end of the document. Do not duplicate sign-off tables.

### 3.12 Appendices
- **Appendix A (Residual Risk Summary):** **REMOVED COMPLETELY.** Do not generate this appendix.
- **Appendix B:** Maintenance Log Template.
- **Appendix C:** LOTO Log Template.

---

## 4. TYPOGRAPHY & VISUALS

- **Font:** Calibri throughout.
- **Placeholders:** Must be written as **[PENDING: LOTO DIAGRAM]** in bold. No background shading.
- **Table Colors:** Header row #1F3864 (Dark blue) with white text. Alternating rows #D9E1F2 (Light blue) and white. 
- **Flowcharts:** Must use White Backgrounds and Blue Borders (#1F3864).
- **Alert Boxes:** 
  - DANGER: #FCE4D6 (Light red), red left border
  - WARNING: #FFF2CC (Yellow), black full border
  - CAUTION: #FCE4D6 (Orange), orange left border
  - NOTICE: #F2F2F2 (Light grey), black left border

---

## 5. OPEN ACTIONS REGISTER

- All missing schematics, missing photos, or unresolved safety gaps must be logged.
- The Open Actions Register is maintained as a **separate spreadsheet**, never printed inside the Word document.

*(End of V2 Standard)*
