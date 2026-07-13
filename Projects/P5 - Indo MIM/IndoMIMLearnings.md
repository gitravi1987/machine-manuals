# IndoMIM BG Snap — Project Learnings

**Project:** P5 — IndoMIM / Tata Electronics, BG Snap Assembly Machine (V67)
**Site visit:** 26 May 2026, Tata Electronics, Hosur
**Versions:** V1.0 (initial) → V2.0 (revision) → V3.0 (site visit corrections)
**Workflow:** Workflow B, Tier A

---

## 1. Machine Data Corrections (found on-site)

### 1.1 Voltage — single phase, not three phase
- V1.0 and V2.0 incorrectly stated `415V, 3-phase`.
- **Correct:** `230V, Single Phase, 50Hz`.
- Root cause: spec sheet provided by client had the panel supply voltage, not the machine incoming supply.
- **Rule for future projects:** Verify incoming supply voltage from the machine nameplate or incoming isolator label, not the client spec sheet. Ask specifically "single phase or three phase?" at intake.

### 1.2 Supply current — do not carry forward from spec sheet
- 63A was listed. For a 230V single-phase machine this is plausible but unconfirmed.
- Marked as `[PLACEHOLDER — confirm supply current rating with Indo-MIM Engineering]`.
- **Rule:** Never carry forward current ratings without nameplate confirmation. Mark as placeholder if unverified.

### 1.3 HMI is actually an IPC
- The control interface was described as "HMI" throughout V1.0 and V2.0.
- **Correct term:** IPC (Industrial PC). This is Indo-MIM's standard terminology for this machine.
- All references replaced globally: HMI → IPC, HMI Alarms → IPC Alarms, Section 11 title updated.
- **Rule for future projects:** Ask client what they call the control interface at intake — HMI, IPC, touchscreen, operator panel. Do not assume "HMI" is the right term.

### 1.4 E-stop count — 6 in the document, 11 on the machine
- V1.0 / V2.0 documented ES-01 to ES-06 (6 E-stops).
- Site visit confirmed **11 E-stops** (ES-01 to ES-11).
- ES-07 to ES-11 locations not confirmed during visit — carried as PLACEHOLDERs pending next site visit.
- **Rule:** Always physically count E-stops on the machine. Do not trust the count in the RA if a site visit has been done. Walk the perimeter and log each button.

### 1.5 Pneumatic LOTO — solenoid valve, not ball valve
- LP-02 (Pneumatic) was documented as `Manual quarter-turn ball valve with lockout hasp`.
- **Correct:** Solenoid valve — de-energise via IPC/control panel, then manually verify pressure vented before entry. There is no physical lockout hasp on this point.
- This is a safety-critical error. A technician following the V1.0 procedure could approach a pressurised zone.
- **Rule:** For every LOTO point, physically check isolation method type on-site. "Ball valve" and "solenoid valve" have completely different isolation sequences. RA reports sometimes list the intended design, not the as-built state.

### 1.6 Teach pendant — not present
- V1.0 referenced `teach pendant enable switch` as part of the robot LOTO (LP-04).
- The robot on this machine does not have a teach pendant connected during production.
- **Correct isolation:** Robot controller main switch (LP-04) only.
- **Rule:** Do not assume robot accessories (teach pendants, safety mats) are present unless physically seen on site.

---

## 2. Document Structure Corrections

### 2.1 Liability disclaimer in Section 1
- V2.0 had a liability disclaimer paragraph inside Section 1.
- **Rule (non-negotiable):** Liability disclaimer appears in Section 13 only. If found elsewhere, clear it and add cross-reference: "Refer to Section 13 for the full Liability Disclaimer."

### 2.2 DANGER boxes
- V2.0 had 4 DANGER boxes in various sections.
- **Rule (non-negotiable):** No DANGER boxes anywhere. Convert all to WARNING boxes.
- Script fix: explicit pass over all paragraphs and table cells replacing `DANGER` → `WARNING`.

### 2.3 Residual Risk Summary appendix
- V2.0 included Appendix A — Residual Risk Summary.
- **Rule (non-negotiable):** This appendix is permanently removed from all OSMs.
- V3.0 fix: paragraph content cleared, Heading 1 style stripped so it does not appear in TOC.
- Per OSM standard: Appendix A = Maintenance Log Template, Appendix B = LOTO Log Template.

### 2.4 Author name — never an individual
- V1.0 and V2.0 had `Ravikumar, Certified Safety Professional` in author fields.
- **Rule (non-negotiable):** Role only — `Certified Safety Professional`. No individual name in any customer document.
- Applied globally: author fields, revision table, cover page, Sec 1.6, Sec 13.3.

### 2.5 OA-P4-003 — alarm codes register
- V2.0 had an OPEN ACTION box in the body of the manual for the IPC alarm codes.
- Alarm codes list is too voluminous to include in the manual body (170+ alarm codes across 10 stations).
- **V3.0 fix:** OPEN ACTION box replaced with a NOTICE directing readers to a separate controlled document: `Indo-MIM IPC Alarm Code Register [document reference TBD]`.
- **Rule for future projects:** If the alarm/fault code list exceeds ~20 entries, recommend it as a separate document rather than an appendix or embedded table.

---

## 3. Content Additions from Site Visit

### 3.1 Daily E-stop functional test
- No daily test was documented in V1.0 / V2.0 — only weekly.
- Site practice confirmed operators test E-stops at shift start.
- Added row to Section 5 periodic testing table: Daily (once per shift) — operator activates each E-stop, verifies safe state, resets, confirms normal operation before production.

### 3.2 Compulsory energy isolation — Maintenance Mode
- V2.0 described Maintenance Mode without explicitly stating that LOTO is still required.
- Added note: "Compulsory energy isolation (full LOTO per Section 4) is required before any personnel enter guarded zones, even in Maintenance Mode."
- **Rule for future projects:** Always explicitly state in the Maintenance Mode description that LOTO overrides mode. Do not let operators infer that Maintenance Mode removes the LOTO requirement.

### 3.3 Individual station isolation — Section 4.7
- The machine has per-station isolators. Individual station work is possible while other stations run.
- Added to Section 4.7: individual station isolation note with reference back to Table 4.2 for isolator locations.
- Full LOTO per Section 4.4 still mandatory for any work inside guarded zones.

### 3.4 Section 6.6 — DFM process flowchart reference
- Detailed process flowchart is in DFM V1.4, Page 12.
- Added cross-reference in Section 6.6 pending final dry-run confirmation for the manual flowchart.

### 3.5 Pre-start checklist — 14 to 15 items
- One additional check point identified on site.
- Updated count from 14 to 15 in Section 6.

---

## 4. Python Script Lessons (apply_v3_changes.py)

### 4.1 Multi-run text replacement
- python-docx stores paragraph text across multiple `Run` objects. A phrase like `415V, 3-phase` may be split across 2–3 runs.
- Solution: "slow path" — join all run texts, replace, write back to first run, clear remaining runs.
- Never use `str_replace` on `.js` content containing Unicode; use Python `content.replace()`.

### 4.2 TOC requires Word paragraph styles, not just direct formatting
- V2.0 used direct run-level formatting for section headings (14pt, bold, #1F3864) but had no Word `pStyle` set.
- Word's TOC field (`TOC \o "1-1" \h \z \u`) finds headings by paragraph style, not by visual formatting.
- Result: TOC was empty / showed only the "Update field" prompt.
- **Fix:** Apply `Heading 1` paragraph style programmatically via python-docx to all section heading paragraphs. Direct formatting (bold, colour, size) overrides the style visually, so the appearance is unchanged.
- **Rule for all future generation scripts:** Always assign Heading paragraph styles to section title paragraphs — do not rely on direct formatting alone.

### 4.3 TOC field depth — H1 only
- OSM standard requires TOC to show H1 entries only (per OSM_WORD_FORMAT_STANDARD_V1_2).
- V2.0 had `\o "1-3"` (H1 through H3).
- **Fix:** Update instrText in TOC field to `\o "1-1"`.

### 4.4 Searching comments in a Word document
- Comments were embedded in the `.docx` file itself (`word/comments.xml`), not in the PDF or xlsx.
- Extract via `zipfile` + `xml.etree.ElementTree`: unzip `.docx`, parse `word/comments.xml` for `w:comment` elements.
- 25 comments were found, all dated 26 May 2026 (site visit date).

### 4.5 Appendix heading — strip style to hide from TOC
- When an appendix is permanently removed, both its content paragraphs AND its heading paragraph must have the Heading style stripped (set to Normal) — otherwise the heading alone will appear as a TOC entry with no content below it.

### 4.6 Idempotent script design
- Script checks for existing V3.0 rows before adding (revision table, E-stop rows, test rows).
- Re-running the script on V2.0 always produces consistent output — no duplicate rows.
- **Rule:** Always make generation scripts idempotent. "Fix in script, re-run" only works if re-running doesn't compound changes.

---

## 5. Open Actions Carried Forward to V4.0

| OA | Description |
|----|-------------|
| Confirm ES-07 to ES-11 locations | Next site visit required |
| Confirm 230V supply current rating | Indo-MIM Engineering to provide nameplate data |
| Figure 4-1 LOTO Energy Isolation Diagram | Top-view layout to be drawn post site visit |
| IPC Alarm Code Register document reference | Indo-MIM to assign document number |
| Figure 6-1 Pre-start check photograph | Post commissioning |
| Figure 7-1 Full lubrication schedule table | Indo-MIM Engineering to supply |
| Figure 8-1 Electrical schematic drawing set | Indo-MIM Engineering to supply |
| Machine layout diagram (Sec 2.6) | Refer DFM V1.4 pending final drawing |

---

## 6. Process Notes

- **Workflow used:** Workflow B, Tier A. No YAML, no ChatGPT. python-docx script as source of truth.
- **Never edit the .docx directly.** All fixes go into `apply_v3_changes.py` and the script is re-run from V2.0.
- **DFM V1.4** (Indo-MIM's internal process document) is the authoritative reference for the assembly cycle detail. Cross-reference it rather than duplicating content in the OSM.
- V3.0 delivered post site visit. V4.0 to be issued once all PLACEHOLDER items above are confirmed by Indo-MIM Engineering.
