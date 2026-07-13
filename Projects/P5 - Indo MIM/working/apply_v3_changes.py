"""
IndoMIM BG Snap OSM - V3.0 Generation Script
Workflow B, Tier A | 26 May 2026 site visit changes applied
Source: IndoMIM_BGSnap_OSM_V2.0.docx
Output: IndoMIM_BGSnap_OSM_V3.0.docx

FIX IN THIS SCRIPT AND RE-RUN — never patch the .docx manually.
"""

import shutil, re, copy, os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import lxml.etree as etree

BASE_DIR = r"c:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Projects\P5 - Indo MIM"
SRC      = os.path.join(BASE_DIR, "IndoMIM_BGSnap_OSM_V2.0.docx")
OUT      = os.path.join(BASE_DIR, "IndoMIM_BGSnap_OSM_V3.0.docx")
LOGO     = os.path.join(BASE_DIR, "Indo MIM Logo", "INDO-MIM-Logo-with-R.png")
MASTER   = r"c:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Master template\IndoMIM_BGSnap_OSM_V3.0.docx"

# ── helpers ──────────────────────────────────────────────────────────────────

def replace_in_run(run, old, new):
    if old in run.text:
        run.text = run.text.replace(old, new)

def replace_in_paragraph(para, replacements):
    """Apply a list of (old, new) replacements across all runs in a paragraph,
    handling splits where a phrase spans multiple runs."""
    for old, new in replacements:
        # fast path: phrase fits in a single run
        for run in para.runs:
            if old in run.text:
                run.text = run.text.replace(old, new)
        # slow path: phrase spans runs — join, replace, put back in first run
        full = "".join(r.text for r in para.runs)
        if old in full:
            new_full = full.replace(old, new)
            if para.runs:
                para.runs[0].text = new_full
                for r in para.runs[1:]:
                    r.text = ""

def global_replace(doc, replacements):
    """Apply replacements in every paragraph, table cell, header and footer."""
    for para in doc.paragraphs:
        replace_in_paragraph(para, replacements)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    replace_in_paragraph(para, replacements)
    for section in doc.sections:
        for hdr in [section.header, section.footer,
                    section.even_page_header, section.even_page_footer,
                    section.first_page_header, section.first_page_footer]:
            if hdr:
                for para in hdr.paragraphs:
                    replace_in_paragraph(para, replacements)

def para_text(para):
    return "".join(r.text for r in para.runs)

def find_paragraphs_containing(doc, substring, case_insensitive=False):
    results = []
    for i, para in enumerate(doc.paragraphs):
        txt = para_text(para)
        match = (substring.lower() in txt.lower()) if case_insensitive else (substring in txt)
        if match:
            results.append((i, para))
    return results

def insert_paragraph_after(para, text, style=None):
    """Insert a new paragraph immediately after *para*."""
    new_para = OxmlElement('w:p')
    para._element.addnext(new_para)
    new_p = para._element.getnext()
    # use docx API on the parent document
    doc = para._element.getroottree().getroot()
    # simpler: just set via XML
    r = OxmlElement('w:r')
    t = OxmlElement('w:t')
    t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    r.append(t)
    new_para.append(r)
    return new_para

def set_run_text_preserve(run, text):
    run.text = text
    run._r.get_or_add_t().set(
        '{http://www.w3.org/XML/1998/namespace}space', 'preserve')

# ── load document ─────────────────────────────────────────────────────────────

print("Loading V2.0 …")
doc = Document(SRC)
print(f"  Paragraphs: {len(doc.paragraphs)}, Tables: {len(doc.tables)}")

# ── STEP 1 — global text replacements ────────────────────────────────────────
print("Applying global text replacements …")

GLOBAL_REPLACEMENTS = [
    # Voltage / phase — most specific first to avoid double-replacement
    ("415V, 3-phase, 50Hz, 63A",        "230V, Single Phase, 50Hz, [PLACEHOLDER — confirm supply current rating]"),
    ("415V, 3-phase, 50Hz",             "230V, Single Phase, 50Hz"),
    ("415V, 3-phase",                    "230V, Single Phase"),
    ("415V, three-phase",               "230V, Single Phase"),
    ("415V 3-phase",                    "230V Single Phase"),
    ("415 V, 3-phase",                  "230V, Single Phase"),
    ("415V",                            "230V AC"),          # remaining instances (e-stop safe state etc.)
    # HMI → IPC
    ("HMI Configuration",               "IPC Configuration"),
    ("HMI alarm",                        "IPC alarm"),
    ("HMI Alarm",                        "IPC Alarm"),
    ("HMI alarms",                       "IPC alarms"),
    ("HMI Alarms",                       "IPC Alarms"),
    ("HMI fault",                        "IPC fault"),
    ("HMI screen",                       "IPC screen"),
    ("HMI interface",                    "IPC interface"),
    ("HMI panel",                        "IPC panel"),
    ("HMI touch",                        "IPC touch"),
    (" HMI ",                            " IPC "),
    (" HMI.",                            " IPC."),
    (" HMI,",                            " IPC,"),
    (" HMI;",                            " IPC;"),
    ("(HMI)",                            "(IPC)"),
    ("HMI/",                             "IPC/"),
    ("/HMI",                             "/IPC"),
    # Names → role only
    ("Ravikumar, Certified Safety Professional", "Certified Safety Professional"),
    ("Ravi Kumar, Certified Safety Professional","Certified Safety Professional"),
    ("Prepared by: Ravikumar",           "Prepared by: Certified Safety Professional"),
    ("Prepared by: Ravi Kumar",          "Prepared by: Certified Safety Professional"),
    ("Author: Ravikumar",               "Author: Certified Safety Professional"),
    ("Author: Ravi Kumar",              "Author: Certified Safety Professional"),
    ("Ravikumar",                        "Certified Safety Professional"),
    ("Ravi Kumar",                       "Certified Safety Professional"),
    # HMI additional patterns not caught by word-boundary replacements
    ("HMI control panel",               "IPC control panel"),
    ("HMIs",                            "IPCs"),
    ("station HMI",                     "station IPC"),
    ("at HMI",                          "at IPC"),
    ("at the HMI",                      "at the IPC"),
    ("from HMI",                        "from IPC"),
    ("on HMI",                          "on IPC"),
    ("the HMI",                         "the IPC"),
    # Teach pendant — remove reference
    ("robot controller main switch + teach pendant enable switch",
     "robot controller main switch (LP-04)"),
    ("Robot controller main switch + teach pendant enable switch",
     "Robot controller main switch (LP-04)"),
    ("teach pendant enable switch",      "robot controller main switch"),
    ("teach pendant",                    "robot controller"),
    # Supply current placeholder
    ("63A main incoming supply",
     "[PLACEHOLDER — confirm main supply current rating with Indo-MIM Engineering] main incoming supply"),
    ("63A",
     "[PLACEHOLDER — confirm current rating]"),
]

global_replace(doc, GLOBAL_REPLACEMENTS)
print("  Global replacements done.")

# ── STEP 2 — section-specific changes ────────────────────────────────────────
print("Applying section-specific changes …")

# ── 2a. Revision table — add V3.0 row ─────────────────────────────────────

def find_revision_table(doc):
    """Find the table that contains 'Revision' and 'Date' headers (any row)."""
    for table in doc.tables:
        for row in table.rows[:3]:  # check first 3 rows for header
            header_text = " ".join(c.text for c in row.cells).lower()
            if "revision" in header_text and ("date" in header_text or "description" in header_text):
                return table
    # fallback: find table with V1.0 row
    for table in doc.tables:
        for row in table.rows:
            if row.cells and row.cells[0].text.strip() in ("V1.0", "V2.0"):
                return table
    return None

rev_table = find_revision_table(doc)
if rev_table:
    # Remove any existing V3.0 row to avoid duplicates on re-run
    rows_to_remove = []
    for row in rev_table.rows:
        if row.cells[0].text.strip() == "V3.0":
            rows_to_remove.append(row._tr)
    for tr in rows_to_remove:
        rev_table._tbl.remove(tr)
    # Add V3.0 row by copying style from last data row
    last_row = rev_table.rows[-1]
    new_tr = copy.deepcopy(last_row._tr)
    rev_table._tbl.append(new_tr)
    new_row = rev_table.rows[-1]
    values = [
        "V3.0",
        "May 2026",
        "Site visit updates: single phase supply correction, IPC nomenclature (replaces HMI), "
        "E-stop count updated to 11, LOTO corrections, compulsory energy isolation note added, "
        "author field corrected to role only.",
        "Indo-MIM / Tata Electronics"
    ]
    for i, val in enumerate(values):
        if i < len(new_row.cells):
            cell = new_row.cells[i]
            for para in cell.paragraphs:
                for run in para.runs:
                    run.text = ""
            if cell.paragraphs:
                cell.paragraphs[0].runs[0].text = val if cell.paragraphs[0].runs else ""
                if not cell.paragraphs[0].runs:
                    cell.paragraphs[0].add_run(val)
            else:
                cell.add_paragraph(val)
    print("  Revision table: V3.0 row added.")
else:
    print("  WARNING: Revision table not found — add V3.0 row manually.")

# ── 2b. E-stop table — add ES-07 to ES-11 ────────────────────────────────────

def find_estop_table(doc):
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if "ES-01" in cell.text or "E-Stop" in cell.text and "ES-" in cell.text:
                    return table
    return None

estop_table = find_estop_table(doc)
if estop_table:
    # Check how many ES- entries already exist
    existing_ids = set()
    for row in estop_table.rows:
        txt = row.cells[0].text.strip()
        if re.match(r'ES-\d+', txt):
            existing_ids.add(txt)
    # Add ES-07 to ES-11 if not already present
    new_estops = [
        ("ES-07", "[PLACEHOLDER — location TBC: site visit confirmation required]", "[PLACEHOLDER]", "[PLACEHOLDER]"),
        ("ES-08", "[PLACEHOLDER — location TBC: site visit confirmation required]", "[PLACEHOLDER]", "[PLACEHOLDER]"),
        ("ES-09", "[PLACEHOLDER — location TBC: site visit confirmation required]", "[PLACEHOLDER]", "[PLACEHOLDER]"),
        ("ES-10", "[PLACEHOLDER — location TBC: site visit confirmation required]", "[PLACEHOLDER]", "[PLACEHOLDER]"),
        ("ES-11", "[PLACEHOLDER — location TBC: site visit confirmation required]", "[PLACEHOLDER]", "[PLACEHOLDER]"),
    ]
    added = 0
    for es_id, desc, height, panel in new_estops:
        if es_id not in existing_ids:
            last_row = estop_table.rows[-1]
            # skip if last row is a footer/notes row
            if not re.match(r'ES-\d+', estop_table.rows[-1].cells[0].text.strip()):
                # insert before last row
                ref_row = estop_table.rows[-2] if len(estop_table.rows) > 2 else estop_table.rows[-1]
            else:
                ref_row = estop_table.rows[-1]
            new_tr = copy.deepcopy(ref_row._tr)
            ref_row._tr.addnext(new_tr)
            new_row = ref_row._tr.getnext()
            # update cell text
            cells_text = [es_id, desc, height, panel]
            # find the new row object
            for row in estop_table.rows:
                if row._tr is new_row:
                    for i, txt in enumerate(cells_text):
                        if i < len(row.cells):
                            for para in row.cells[i].paragraphs:
                                for run in para.runs:
                                    run.text = ""
                            if row.cells[i].paragraphs and row.cells[i].paragraphs[0].runs:
                                row.cells[i].paragraphs[0].runs[0].text = txt
                            else:
                                row.cells[i].paragraphs[0].add_run(txt) if row.cells[i].paragraphs else row.cells[i].add_paragraph(txt)
                    break
            added += 1
    print(f"  E-stop table: {added} new entries added (ES-07 to ES-11).")
else:
    print("  WARNING: E-stop table not found — add ES-07 to ES-11 manually.")

# ── 2c. Daily E-stop test — add once-per-shift row ───────────────────────────

def find_estop_test_table(doc):
    """Find periodic testing / functional check table in Section 5."""
    for table in doc.tables:
        for row in table.rows:
            row_text = " ".join(c.text for c in row.cells).lower()
            if "weekly" in row_text and ("test" in row_text or "check" in row_text or "e-stop" in row_text):
                return table
    return None

test_table = find_estop_test_table(doc)
if test_table:
    has_daily = any("daily" in " ".join(c.text for c in r.cells).lower() or
                    "per shift" in " ".join(c.text for c in r.cells).lower()
                    for r in test_table.rows)
    if not has_daily:
        # insert daily row before the weekly row
        for i, row in enumerate(test_table.rows):
            row_text = " ".join(c.text for c in row.cells).lower()
            if "weekly" in row_text:
                new_tr = copy.deepcopy(row._tr)
                row._tr.addprevious(new_tr)
                # find new row and update
                for r in test_table.rows:
                    if r._tr is row._tr.getprevious():
                        cell_vals = [
                            "Daily (once per shift)",
                            "Operator activates each accessible E-stop button. "
                            "Machine must enter safe state. Reset and confirm normal "
                            "operation resumes before production starts.",
                            "Operator",
                            "Log in maintenance record"
                        ]
                        for j, val in enumerate(cell_vals):
                            if j < len(r.cells):
                                for para in r.cells[j].paragraphs:
                                    for run in para.runs:
                                        run.text = ""
                                if r.cells[j].paragraphs and r.cells[j].paragraphs[0].runs:
                                    r.cells[j].paragraphs[0].runs[0].text = val
                                else:
                                    r.cells[j].paragraphs[0].add_run(val) if r.cells[j].paragraphs else r.cells[j].add_paragraph(val)
                        break
                break
        print("  E-stop test table: daily/once-per-shift row added.")
    else:
        print("  E-stop test table: daily row already present.")
else:
    print("  INFO: E-stop periodic test table not found — check Section 5 manually.")

# ── 2d. OA-P4-003 block — remove, replace with NOTICE ───────────────────────
# Strategy: find paragraph containing "OA-P4-003" and replace its text.

NOTICE_003 = (
    "NOTICE: The IPC alarm code register is maintained as a separate controlled document "
    "due to its volume. Refer to Indo-MIM IPC Alarm Code Register [document reference TBD] "
    "for the complete alarm code list, descriptions, station references, priority levels, "
    "and response procedures."
)
removed_003 = False
# Search paragraphs
for para in doc.paragraphs:
    txt = para_text(para)
    if "OA-P4-003" in txt:
        for run in para.runs:
            run.text = ""
        if para.runs:
            para.runs[0].text = NOTICE_003
        else:
            para.add_run(NOTICE_003)
        removed_003 = True
        print("  OA-P4-003: replaced with NOTICE (in paragraph).")
        break
# Search table cells
if not removed_003:
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if "OA-P4-003" in cell.text:
                    for para in cell.paragraphs:
                        for run in para.runs:
                            run.text = ""
                    if cell.paragraphs:
                        if cell.paragraphs[0].runs:
                            cell.paragraphs[0].runs[0].text = NOTICE_003
                        else:
                            cell.paragraphs[0].add_run(NOTICE_003)
                    removed_003 = True
                    print("  OA-P4-003: replaced with NOTICE (in table cell).")
                    break
            if removed_003:
                break
        if removed_003:
            break
if not removed_003:
    print("  INFO: OA-P4-003 not found — may already be removed.")

# ── 2e. Compulsory energy isolation in Maintenance mode ──────────────────────

for i, para in enumerate(doc.paragraphs):
    txt = para_text(para)
    if ("maintenance mode" in txt.lower() or "Maintenance Mode" in txt) and \
       "compulsory" not in txt.lower() and "energy isolation" not in txt.lower():
        # append note to this paragraph
        if para.runs:
            last_run = para.runs[-1]
            last_run.text = last_run.text.rstrip() + \
                " NOTE: Compulsory energy isolation (full LOTO per Section 4) is required " \
                "before any personnel enter guarded zones, even in Maintenance Mode."
        break

print("  Maintenance mode: compulsory energy isolation note applied.")

# ── 2f. Pre-start checklist — update item count 14 → 15 ─────────────────────
for para in doc.paragraphs:
    txt = para_text(para)
    if "14" in txt and ("pre-start" in txt.lower() or "pre start" in txt.lower() or "check" in txt.lower()):
        replace_in_paragraph(para, [("14 ", "15 "), ("14.", "15."), ("fourteen", "fifteen")])

# Also do a targeted replacement in the pre-start section context
global_replace(doc, [
    ("numbered 1 through 14", "numbered 1 through 15"),
    ("1 through 14 with",     "1 through 15 with"),
    ("points numbered 1 through 14", "points numbered 1 through 15"),
])
print("  Pre-start checklist: item count updated to 15.")

# ── 2g. Section 6.6 — DFM flowchart reference ────────────────────────────────
for i, para in enumerate(doc.paragraphs):
    txt = para_text(para)
    if ("6.6" in txt or "Normal Operating Cycle" in txt) and "flowchart" in txt.lower():
        if "DFM" not in txt:
            if para.runs:
                para.runs[-1].text = para.runs[-1].text.rstrip() + \
                    " Refer DFM V1.4, Page 12 for the detailed process flowchart. " \
                    "Final flowchart to be inserted here following dry-run confirmation."
        break
print("  Section 6.6: DFM flowchart reference added.")

# ── 2h. Figure 6-1 caption — post commissioning note ────────────────────────
for para in doc.paragraphs:
    txt = para_text(para)
    if "Figure 6-1" in txt and ("PLACEHOLDER" in txt or "pre-start" in txt.lower()):
        replace_in_paragraph(para, [
            ("Figure 6-1:", "Figure 6-1: [PLACEHOLDER — Pre-start check point reference photograph to be added post commissioning]"),
        ])
        if "post commissioning" not in para_text(para):
            replace_in_paragraph(para, [
                ("Source:", "[PLACEHOLDER — to be added post commissioning] Source:"),
            ])
        break

# ── 2i. Section 4.6 — energy isolation diagram placeholder ──────────────────
for i, para in enumerate(doc.paragraphs):
    txt = para_text(para)
    if "4.6" in txt and ("Energy Isolation Diagram" in txt or "isolation diagram" in txt.lower()):
        # Ensure the top-view identification note is present
        if "top-view" not in txt.lower() and "top view" not in txt.lower():
            if para.runs:
                para.runs[-1].text = para.runs[-1].text.rstrip() + \
                    " [PLACEHOLDER — LOTO Energy Isolation Diagram (Figure 4-1): " \
                    "top-view layout of machine showing LP-01 to LP-05 with colour-coded " \
                    "energy type identification. To be created post site visit. OA-P4-014.]"
        break

# ── 2j. Pneumatic LOTO — solenoid valve correction ───────────────────────────
# Already handled partially by global replace of "quarter-turn ball valve with lockout hasp"
global_replace(doc, [
    ("Manual quarter-turn ball valve with lockout hasp",
     "Solenoid valve — de-energise via IPC/control panel; manually verify vent before entry"),
    ("quarter-turn ball valve with lockout hasp",
     "solenoid valve (de-energise via IPC); verify pressure vented before entry"),
    ("Quarter-turn ball valve",
     "Solenoid valve"),
])
print("  Pneumatic LOTO: solenoid valve correction applied.")

# ── 2k. Remove Residual Risk Summary appendix ────────────────────────────────
# Mark any paragraph that references "Residual Risk Summary" as removed
rrs_found = False
i = 0
while i < len(doc.paragraphs):
    para = doc.paragraphs[i]
    txt = para_text(para)
    if "Residual Risk Summary" in txt or "RESIDUAL RISK SUMMARY" in txt or \
       "Appendix A — Residual Risk" in txt or "Appendix A: Residual Risk" in txt:
        for run in para.runs:
            run.text = ""
        # If this is the section heading, remove it entirely (blank line, no heading style)
        # so it does not appear in the TOC
        is_heading = "APPENDIX A" in txt or "Appendix A" in txt
        if not is_heading:
            if para.runs:
                para.runs[0].text = "[SECTION REMOVED — Residual Risk Summary appendix permanently removed per OSM standard V1.2]"
        # Strip any heading style so TOC ignores this paragraph
        try:
            para.style = doc.styles['Normal']
        except Exception:
            pass
        rrs_found = True
        print(f"  Residual Risk Summary: paragraph cleared at index {i}.")
    i += 1

if not rrs_found:
    print("  Residual Risk Summary: not found in V2.0 (already removed or never present).")

# ── 2n-extra-0. Remove Liability Disclaimer from Section 1 ──────────────────
# Rule: liability disclaimer must appear in Section 13 ONLY. Never in Section 1.
in_sec1 = True
liability_cleared = 0
for para in doc.paragraphs:
    txt = para_text(para)
    # Once we hit Section 2, we're past the front matter
    if txt.strip() in ("2.  MACHINE OVERVIEW", "2. MACHINE OVERVIEW", "MACHINE OVERVIEW") or \
       txt.strip().startswith("2.  ") or txt.strip().startswith("2. "):
        in_sec1 = False
    if in_sec1 and ("liability" in txt.lower() or "Liability Disclaimer" in txt):
        # Replace with a cross-reference to Section 13
        for run in para.runs:
            run.text = ""
        if para.runs:
            para.runs[0].text = "Refer to Section 13 for the full Liability Disclaimer."
        else:
            para.add_run("Refer to Section 13 for the full Liability Disclaimer.")
        liability_cleared += 1
print(f"  Liability Disclaimer: {liability_cleared} instance(s) cleared from Section 1 (moved to Sec 13 only).")

# ── 2n-extra. Remove DANGER boxes — convert to WARNING ───────────────────────
# DANGER boxes are permanently removed per OSM standard V1.2.
# Convert any remaining DANGER label to WARNING.
danger_count = 0
for para in doc.paragraphs:
    txt = para_text(para)
    if txt.strip() == "DANGER" or txt.strip().startswith("DANGER ") or txt.strip().startswith("DANGER\t"):
        for run in para.runs:
            if "DANGER" in run.text:
                run.text = run.text.replace("DANGER", "WARNING")
                danger_count += 1
# Also handle in table cells
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                txt = para_text(para)
                if "DANGER" in txt:
                    for run in para.runs:
                        if "DANGER" in run.text:
                            run.text = run.text.replace("DANGER", "WARNING")
                            danger_count += 1
print(f"  DANGER boxes: {danger_count} instance(s) converted to WARNING.")

# ── 2l. Cover page — logo ────────────────────────────────────────────────────
# Add logo to first paragraph of document if a logo placeholder exists
logo_placed = False
for para in doc.paragraphs:
    txt = para_text(para)
    if "LOGO" in txt.upper() or "logo" in txt.lower() or "Company Logo" in txt:
        # Replace placeholder text with actual logo image
        for run in para.runs:
            run.text = ""
        if os.path.exists(LOGO):
            run = para.add_run()
            run.add_picture(LOGO, width=Inches(2.5))
            logo_placed = True
            print("  Cover: Indo-MIM logo inserted.")
        else:
            if para.runs:
                para.runs[0].text = "[PLACEHOLDER — Indo-MIM company logo: INDO-MIM-Logo-with-R.png]"
            print("  Cover: logo file not found — placeholder text set.")
        break

if not logo_placed:
    # Check if logo is already in the document (as an image)
    # Just ensure the placeholder is meaningful
    for para in doc.paragraphs[:10]:  # first 10 paragraphs = cover area
        txt = para_text(para)
        if "PLACEHOLDER" in txt and ("logo" in txt.lower() or "Logo" in txt):
            if os.path.exists(LOGO):
                for run in para.runs:
                    run.text = ""
                run = para.add_run()
                run.add_picture(LOGO, width=Inches(2.5))
                print("  Cover: Indo-MIM logo inserted (second pass).")
            break

# ── 2m. Company name — ensure consistent ─────────────────────────────────────
global_replace(doc, [
    ("Indo MIM P.Ltd",    "IndoMIM Technologies Pvt. Ltd."),
    ("Indo MIM Pvt Ltd",  "IndoMIM Technologies Pvt. Ltd."),
    ("IndoMIM P.Ltd",     "IndoMIM Technologies Pvt. Ltd."),
])

# ── 2n. Sec 4.7 — individual station isolation note ──────────────────────────
for i, para in enumerate(doc.paragraphs):
    txt = para_text(para)
    if "4.7" in txt and ("Partial Isolation" in txt or "partial isolation" in txt.lower()):
        if "individual station" not in txt.lower():
            if para.runs:
                para.runs[-1].text = para.runs[-1].text.rstrip() + \
                    " Individual station isolation is possible for maintenance at a single " \
                    "station while other stations remain operational. Full LOTO per Section 4.4 " \
                    "remains mandatory for any work inside guarded zones."
        break

# ── STEP 2-p. Apply Heading 1 style to section heading paragraphs ────────────
# The section titles use direct formatting only (no pStyle), so Word's TOC field
# cannot find them. Apply built-in Heading 1 style — run-level direct formatting
# (14pt bold #1F3864) will still override the style visually.
import re as _re

H1_SECTION_PATTERN = _re.compile(
    r'^(\d+\.?\s+)[A-Z][A-Z\s&/()\\-]{4,}$'
)
APPENDIX_PATTERN = _re.compile(
    r'^(APPENDIX\s+[AB]|Appendix\s+[AB])\b'
)

h1_applied = 0
for para in doc.paragraphs:
    txt = para_text(para).strip()
    if not txt:
        continue
    # Identify H1 by pattern + formatting signature (28 half-pt = 14pt, bold, blue)
    is_h1_pattern = bool(H1_SECTION_PATTERN.match(txt)) or bool(APPENDIX_PATTERN.match(txt))
    # Also check run formatting as secondary confirmation
    has_h1_format = False
    if para.runs:
        r = para.runs[0]
        if r.bold and r.font.color.rgb is not None:
            from docx.shared import RGBColor
            if r.font.color.rgb == RGBColor(0x1F, 0x38, 0x64):
                has_h1_format = True
    if is_h1_pattern and (has_h1_format or 'APPENDIX' in txt.upper()):
        try:
            para.style = doc.styles['Heading 1']
            h1_applied += 1
        except Exception:
            # Style not in document yet — apply via XML directly
            pPr = para._element.get_or_add_pPr()
            pStyle = OxmlElement('w:pStyle')
            pStyle.set(qn('w:val'), 'Heading1')
            # Remove existing pStyle if any
            for existing in pPr.findall(qn('w:pStyle')):
                pPr.remove(existing)
            pPr.insert(0, pStyle)
            h1_applied += 1

print(f"  Heading styles: Heading 1 applied to {h1_applied} section heading paragraphs.")

# ── STEP 2-p2. Apply Heading 2 style to sub-section heading paragraphs ────────
# Sub-section headings: 13pt bold #1F3864, pattern like "1.1  Title"
H2_SECTION_PATTERN = _re.compile(r'^\d+\.\d+\s+\S')

h2_applied = 0
for para in doc.paragraphs:
    if para.style.name.startswith('Heading'):
        continue  # already styled — skip
    txt = para_text(para).strip()
    if not txt:
        continue
    if not H2_SECTION_PATTERN.match(txt):
        continue
    if not para.runs:
        continue
    r0 = para.runs[0]
    # Confirm 13pt bold #1F3864 formatting signature
    is_13pt = (r0.font.size is not None and abs(r0.font.size.pt - 13.0) < 0.5)
    is_bold = bool(r0.bold)
    try:
        is_blue = (r0.font.color.rgb == RGBColor(0x1F, 0x38, 0x64))
    except Exception:
        is_blue = False
    if is_13pt and is_bold and is_blue:
        try:
            para.style = doc.styles['Heading 2']
            h2_applied += 1
        except Exception:
            pPr = para._element.get_or_add_pPr()
            pStyle = OxmlElement('w:pStyle')
            pStyle.set(qn('w:val'), 'Heading2')
            for existing in pPr.findall(qn('w:pStyle')):
                pPr.remove(existing)
            pPr.insert(0, pStyle)
            h2_applied += 1

print(f"  Heading styles: Heading 2 applied to {h2_applied} sub-section heading paragraphs.")

# ── STEP 2-q. Fix TOC field — H1+H2 per user requirement ────────────────────
# Set TOC \o "1-2" (H1 + H2 = section and sub-section headings)
toc_fixed = 0
for para in doc.paragraphs:
    for run in para.runs:
        elem = run._r
        for instr in elem.findall('.//' + qn('w:instrText')):
            if instr.text and 'TOC' in instr.text:
                old_instr = instr.text
                instr.text = instr.text.replace(
                    r'\o "1-3"', r'\o "1-2"'
                ).replace(
                    r'\o "1-1"', r'\o "1-2"'
                )
                if instr.text != old_instr:
                    toc_fixed += 1

# Also search at paragraph level (instrText can be in fldChar runs)
for para in doc.paragraphs:
    for elem in para._element.iter():
        tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
        if tag == 'instrText' and elem.text and 'TOC' in elem.text:
            old_t = elem.text
            elem.text = elem.text.replace(r'\o "1-3"', r'\o "1-2"').replace(r'\o "1-1"', r'\o "1-2"')
            if elem.text != old_t:
                toc_fixed += 1

print(f"  TOC field: updated to H1+H2 (\\o \"1-2\"). Instances fixed: {toc_fixed}.")

# ── STEP 3 — document metadata / properties ───────────────────────────────────
print("Updating document properties …")
try:
    cp = doc.core_properties
    cp.revision = 3
    cp.author = "Certified Safety Professional"
    cp.last_modified_by = "Certified Safety Professional"
    cp.comments = "V3.0 - Site visit changes applied 26 May 2026. Workflow B, Tier A."
    print("  Core properties updated.")
except Exception as e:
    print(f"  WARNING: Could not update core properties: {e}")

# ── STEP 4 — save ─────────────────────────────────────────────────────────────
print("Saving V3.0 -> " + OUT)
doc.save(OUT)
print("  Saved.")

# ── STEP 5 — copy to Master template ─────────────────────────────────────────
os.makedirs(os.path.dirname(MASTER), exist_ok=True)
shutil.copy2(OUT, MASTER)
print(f"  Copied to Master template: {MASTER}")

print("\nDONE: V3.0 generation complete.")
print("  Next: open in Word, right-click TOC -> Update Field -> Update entire table.")
print("  TOC will show section headings (H1) and sub-section headings (H2) -- 1.1, 1.2 etc.")
print("  Review all PLACEHOLDERs: ES-07 to ES-11 locations, supply current, schematics.")
