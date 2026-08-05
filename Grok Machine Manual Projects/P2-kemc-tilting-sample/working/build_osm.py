#!/usr/bin/env python3
"""Build KEMC Tilting Machine OSM (Grok Sample) — Indo-MIM style colours/sections.
Writes only under Grok Machine Manual Projects. Uses python-docx.
"""
from __future__ import annotations

import json
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn, nsmap
from docx.shared import Cm, Mm, Pt, RGBColor, Twips

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "KEMC_TiltingMachine_OSM_GrokSample_V1.1.docx"
DATA = json.loads((ROOT / "inputs" / "machine_data.json").read_text(encoding="utf-8"))

NAVY = RGBColor(0x1F, 0x38, 0x64)
BLACK = RGBColor(0, 0, 0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY = RGBColor(0x55, 0x55, 0x55)
WARN_BG = "FFF2CC"
NOTICE_BG = "F2F2F2"
ALT_ROW = "D9E1F2"
PLACE_BG = "F7F7F7"
OA_BG = "FCE4D6"


def set_run(run, *, size=11, bold=False, color=BLACK, italic=False):
    run.font.name = "Calibri"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color


def shade_cell(cell, hex_color: str):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def set_cell_border(cell, color="1F3864", sz="4"):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), sz)
        el.set(qn("w:color"), color)
        tcBorders.append(el)
    tcPr.append(tcBorders)


def cell_para(cell, text, *, bold=False, size=10, color=BLACK, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    set_run(r, size=size, bold=bold, color=color)
    return p


def add_page_number(paragraph):
    run = paragraph.add_run()
    set_run(run, size=9, color=NAVY)
    fld_char_begin = OxmlElement("w:fldChar")
    fld_char_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld_char_end = OxmlElement("w:fldChar")
    fld_char_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_char_begin)
    run._r.append(instr)
    run._r.append(fld_char_end)


def configure_section(section, *, different_first=False):
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.left_margin = Mm(25)
    section.right_margin = Mm(25)
    section.top_margin = Mm(25)
    section.bottom_margin = Mm(25)
    section.header_distance = Mm(12)
    section.footer_distance = Mm(12)
    section.different_first_page_header_footer = different_first


def build_header_footer(doc: Document):
    # Section 0 = cover (no header/footer content)
    # Section 1+ = body
    section = doc.sections[0]
    configure_section(section, different_first=True)
    # empty first header/footer
    section.first_page_header.paragraphs[0].text = ""
    section.first_page_footer.paragraphs[0].text = ""

    header = section.header
    hp = header.paragraphs[0]
    hp.clear()
    hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r1 = hp.add_run("Tilting Machine")
    set_run(r1, size=9, color=NAVY)
    r2 = hp.add_run("  |  Operating & Safety Manual  |  Page ")
    set_run(r2, size=9, color=NAVY)
    add_page_number(hp)

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.clear()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = fp.add_run("CONFIDENTIAL — Grok Sample / Draft")
    set_run(fr, size=9, bold=True, color=GREY)


def h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.page_break_before = True
    r = p.add_run(text)
    set_run(r, size=14, bold=True, color=NAVY)
    # outline level for TOC-like structure
    pPr = p._p.get_or_add_pPr()
    outline = OxmlElement("w:outlineLvl")
    outline.set(qn("w:val"), "0")
    pPr.append(outline)
    return p


def h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    set_run(r, size=13, bold=True, color=NAVY)
    pPr = p._p.get_or_add_pPr()
    outline = OxmlElement("w:outlineLvl")
    outline.set(qn("w:val"), "1")
    pPr.append(outline)
    return p


def body(doc, text):
    for para in text.strip().split("\n"):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(para.strip() if para.strip() else "")
        set_run(r, size=11, color=BLACK)
    return p


def bullet(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.clear()
        r = p.add_run(item)
        set_run(r, size=11)
        p.paragraph_format.space_after = Pt(4)


def alert_box(doc, kind: str, lines: list[str]):
    colors = {
        "WARNING": (WARN_BG, NAVY),
        "NOTICE": (NOTICE_BG, BLACK),
        "PLACEHOLDER": (PLACE_BG, BLACK),
        "OPEN ACTION": (OA_BG, RGBColor(0xCC, 0, 0)),
        "CAUTION": (OA_BG, RGBColor(0xFF, 0x66, 0)),
    }
    bg, title_color = colors.get(kind, (NOTICE_BG, BLACK))
    table = doc.add_table(rows=1, cols=1)
    table.autofit = True
    cell = table.cell(0, 0)
    shade_cell(cell, bg)
    set_cell_border(cell, "000000" if kind == "WARNING" else "AAAAAA")
    cell.text = ""
    p0 = cell.paragraphs[0]
    r0 = p0.add_run(kind)
    set_run(r0, size=11, bold=True, color=title_color)
    for line in lines:
        p = cell.add_paragraph()
        r = p.add_run(line)
        set_run(r, size=11, bold=(kind == "PLACEHOLDER"), color=BLACK)
    doc.add_paragraph()


def styled_table(doc, headers, rows, col_widths_cm=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell_para(cell, h, bold=True, size=10, color=WHITE, align=WD_ALIGN_PARAGRAPH.CENTER)
        shade_cell(cell, "1F3864")
        set_cell_border(cell)
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.rows[ri + 1].cells[ci]
            cell_para(cell, str(val), size=10)
            set_cell_border(cell)
            if ri % 2 == 1:
                shade_cell(cell, ALT_ROW)
    if col_widths_cm:
        for row in table.rows:
            for i, w in enumerate(col_widths_cm):
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return table


def flowchart(doc, title: str, steps: list[str]):
    h2(doc, title) if title else None
    # vertical flowchart as single-column styled table
    table = doc.add_table(rows=len(steps), cols=1)
    for i, step in enumerate(steps):
        cell = table.rows[i].cells[0]
        is_end = i == 0 or i == len(steps) - 1
        if is_end:
            shade_cell(cell, "1F3864")
            cell_para(cell, step, bold=True, size=11, color=WHITE, align=WD_ALIGN_PARAGRAPH.CENTER)
        else:
            shade_cell(cell, "FFFFFF")
            cell_para(cell, step, bold=False, size=11, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_border(cell, "1F3864", "12")
    doc.add_paragraph()


def cover(doc):
    for _ in range(3):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("OPERATING & SAFETY MANUAL")
    set_run(r, size=22, bold=True, color=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Tilting Machine")
    set_run(r, size=18, bold=True, color=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Clutch Plate Assembly Support")
    set_run(r, size=14, color=NAVY)

    doc.add_paragraph()
    meta = [
        ("Manufacturer", DATA["manufacturer"]),
        ("End User / Site", DATA["site"]),
        ("Machine Type", DATA["machine_type"]),
        ("Document Title", "Operating & Safety Manual"),
        ("Document No.", "KEMC-TILT-OSM-GROK-001"),
        ("Revision", DATA["revision"]),
        ("Date", DATA["date"]),
        ("Prepared By", "Certified Safety Professional"),
        ("Status", DATA["status"]),
        ("Tier", DATA["tier"]),
        ("Assessment Ref.", DATA["assessment_ref"]),
    ]
    table = doc.add_table(rows=len(meta), cols=2)
    for i, (k, v) in enumerate(meta):
        cell_para(table.rows[i].cells[0], k, bold=True, size=11, color=NAVY)
        cell_para(table.rows[i].cells[1], v, size=11)
        set_cell_border(table.rows[i].cells[0])
        set_cell_border(table.rows[i].cells[1])
        shade_cell(table.rows[i].cells[0], ALT_ROW)

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("CONFIDENTIAL — Grok Sample / Draft for capability comparison")
    set_run(r, size=9, bold=True, color=GREY)


def revision_page(doc):
    h1(doc, "Revision History")
    body(doc, "Four-column revision table (Prepared By column not used).")
    styled_table(
        doc,
        ["Revision", "Date", "Description", "Reviewed By"],
        [
            ["V1.0", DATA["date"], "Initial Grok sample draft from Machine Safety Assessment + photos", "Manufacturer / End User"],
            ["V1.1", DATA["date"], DATA.get("revision_note", "Photo-backed control layout enrichment"), "Manufacturer / End User"],
            ["V2.0", "TBD", "Post dry-run / customer release", "Manufacturer / End User"],
        ],
        [2.5, 3, 7, 4],
    )


def toc_page(doc):
    h1(doc, "Table of Contents")
    body(doc, "H1 entries only. After opening in Word: right-click TOC field area → Update Field → Update entire table (if field inserted). This sample uses a static TOC list.")
    entries = [
        "1. Front Matter",
        "2. Machine Overview",
        "3. Hazard Identification & Risk Assessment",
        "4. Lockout / Tagout (LOTO) Procedures",
        "5. Emergency Stop Function",
        "6. Operating Instructions",
        "7. Maintenance & Care",
        "8. Electrical Schematic",
        "9. Pneumatic Schematic",
        "10. HMI / Alarms & Fault Codes",
        "11. Safety Features & Interlocks",
        "12. Compliance & Certifications",
        "Appendix A — Maintenance Log Template",
        "Appendix B — LOTO Log Template",
    ]
    for e in entries:
        p = doc.add_paragraph()
        r = p.add_run(e)
        set_run(r, size=11, color=BLACK)
        p.paragraph_format.space_after = Pt(4)


def section_1(doc):
    h1(doc, "1. Front Matter")
    h2(doc, "1.1 Document Scope")
    body(
        doc,
        """This Operating & Safety Manual (OSM) provides information for safe operation, maintenance, and energy isolation of the Tilting Machine manufactured by Karthick Engineering & Maintenance Consultants (KEMC).

It follows principles of ISO 20607:2019, ISO 12100:2010, IEC 82079-1:2019, and IS 4571:2008, based on the Machine Safety Assessment (report date 16 February 2026).

This document is a Grok capability-sample draft (Tier B). Close all placeholders and Open Actions before treating as customer-released.""",
    )
    h2(doc, "1.2 Intended Audience")
    bullet(
        doc,
        [
            "Production operators (instructed persons)",
            "Maintenance and troubleshooting personnel (skilled persons)",
            "Supervisors and safety representatives",
            "Visitors/contractors near the machine (awareness only)",
        ],
    )
    body(doc, "Untrained personnel shall not operate, adjust, or maintain this machine.")

    h2(doc, "1.3 General Safety Rules")
    bullet(
        doc,
        [
            "Read this manual and the Machine Safety Assessment before work.",
            "Only trained and authorised persons may operate the machine.",
            "Never bypass light curtains, two-hand controls, guards, or interlocks.",
            "Apply full LOTO (Section 4) before work inside guarded zones, jaw setup, fixture changeover, or energy-system work.",
            "Wear PPE: safety footwear and hand protection as specified.",
            "Keep hands clear of clamps, tilting mechanism, and moving parts.",
            "Do not operate with guards removed or disabled.",
            "Report damaged safety devices and stop production until restored.",
        ],
    )

    h2(doc, "1.4 Signal Word Hierarchy")
    styled_table(
        doc,
        ["Signal Word", "Meaning"],
        [
            ["WARNING", "Hazardous situation that could result in death or serious injury if not avoided."],
            ["CAUTION", "Hazardous situation that could result in minor or moderate injury if not avoided."],
            ["NOTICE", "Practices not related to personal injury, or important operational information."],
        ],
        [4, 12],
    )
    alert_box(
        doc,
        "NOTICE",
        ["DANGER signal-word boxes are not used in this manual template."],
    )

    h2(doc, "1.5 Prepared By")
    body(doc, "Prepared by: Certified Safety Professional\nRole only — no individual name in customer-facing attribution fields.")


def section_2(doc):
    h1(doc, "2. Machine Overview")
    h2(doc, "2.1 Machine Identification")
    styled_table(
        doc,
        ["Field", "Value"],
        [
            ["Machine name", DATA["machine_name"]],
            ["Manufacturer", DATA["manufacturer"]],
            ["Machine type", DATA["machine_type"]],
            ["Site (assessment)", DATA["site"]],
            ["Assessment date", DATA["assessment_date"]],
            ["Model / Serial / Asset", "[PLACEHOLDER — confirm from nameplate — OA-P2G-005]"],
        ],
        [5, 11],
    )

    h2(doc, "2.2 Technical Specifications")
    e, pneu, hyd = DATA["electrical"], DATA["pneumatic"], DATA["hydraulic"]
    styled_table(
        doc,
        ["Parameter", "Value", "Source"],
        [
            ["Electrical supply", f"{e['voltage']}, {e['phases']}, {e['frequency']}", "Machine Safety Assessment"],
            ["Pneumatic supply", pneu["pressure"], "Machine Safety Assessment"],
            ["Hydraulic", "NA" if not hyd["applicable"] else hyd["notes"], "Machine Safety Assessment"],
            ["Capacity", DATA["capacity"], "Machine Safety Assessment"],
            ["Operating modes", ", ".join(DATA["operating_modes"]), "Machine Safety Assessment"],
            ["Workpiece", DATA["workpiece"], "Machine Safety Assessment"],
            ["Models (fixtures)", ", ".join(DATA["models_supported"]), "Machine Safety Assessment"],
            ["Time base", f"{DATA['time_limits']['days_per_year']} days/year; {DATA['time_limits']['hours_per_day']} h/day; {DATA['time_limits']['shifts_per_day']} shifts/day", "Machine Safety Assessment"],
        ],
        [4.5, 6.5, 5],
    )

    h2(doc, "2.3 Intended Use")
    body(
        doc,
        """The tilting machine assembly is intended for safe loading, positioning, clamping, and tilting of assembled clutch plates to enable accurate and secure nut installation. It improves ergonomics, fastening consistency, and controlled unloading.

Reasonably foreseeable misuse includes loading beyond specified limits, bypassing clamps or safety interlocks, tilting while unsecured, omitting required crane handling, and maintenance while energised.""",
    )

    h2(doc, "2.4 Station Layout & Line Configuration")
    body(
        doc,
        """Fixed workstation with defined loading/unloading zone. Clearance required for tilting movement and crane operation. Access to moving/clamping areas is restricted by perimeter mesh guards and a Type 4 safety light curtain.

Site photo (full front view) shows the operator face with:
• Central clamp/tilt fixture behind hinged mesh guard door
• Left and right two-hand button stations on the lower front rail
• Stainless control column on the right with HMI and E-Stop
• Lower-right rotary main isolator and pneumatic FRL assembly""",
    )
    alert_box(
        doc,
        "NOTICE",
        [
            "Photo references copied into this pilot: inputs/photo-refs/ (full front, isolator, fixture, guard sign, side interface).",
            "Photos corroborate RA; they do not replace nameplate verification.",
        ],
    )

    h2(doc, "2.5 Key Components")
    bullet(
        doc,
        [
            "Tilting mechanism (motor-driven tilting movement)",
            "Pneumatic clamping cylinders holding clutch plate during tilt/nut install",
            "Gripping jaws / fixtures (model-specific, including 280 jaw adjustment)",
            "Interchangeable base plates for models 230 / 280 / 310",
            "Dual two-hand cycle start stations (left + right front — site photo)",
            "Operator HMI/touch panel on right control column (site photo)",
            "Emergency stop mushroom on control column below HMI (site photo)",
            "Main electrical rotary ON/OFF isolation switch lower right front (site photo)",
            "Pneumatic FRL / regulator bank lower right front (site photo)",
            "Pneumatic air isolation device (SF11 — RA)",
            "Type 4 safety light curtain (top ~1400 mm, lowest ~900 mm, 14 mm resolution — RA)",
            "Hinged wire-mesh perimeter guard door on operator face (site photo)",
            "Safety-rated controller (SRPCS) — model placeholder OA-P2G-007",
            "Awareness signs: crush/cut WARNING; automatic motion; do-not-reach; lockout label",
        ],
    )

    h2(doc, "2.6 Maintenance Access Zones")
    body(
        doc,
        """Cleaning/maintenance includes chips/oil cleaning, lubrication, and cylinder/fixture maintenance. Troubleshooting covers jam/misalignment, sensors/actuators, and manual repositioning. Preventive maintenance is planned approximately once every 15 days (assessment task description). Entry to process zone requires full energy isolation (Section 4).""",
    )


def section_3(doc):
    h1(doc, "3. Hazard Identification & Risk Assessment")
    body(
        doc,
        """Hazard identification and risk estimation were performed under a Machine Safety Assessment (report date 16 February 2026) for production, troubleshooting, cleaning/maintenance, visitor presence, gripping jaw setup, and fixture base-plate changeover.

Principal mechanical hazards include shearing from tilting movement (moving element approaching fixed parts) and injection/crushing from pneumatic clamping cylinders that hold the clutch plate during tilt and nut-running. Electrical hazards include electrocution from power-system faults during troubleshooting and electric shock from control-panel short-circuit conditions. Assessment risk-in values ranged from scores associated with priority around 3 (mechanical) up to 10 (electrical troubleshooting).

Risk reduction measures include fixed perimeter guarding (ISO 14120 / ISO 13857 principles), Type 4 light curtain, two-hand cycle start, emergency stop, electrical power isolation, pneumatic energy isolation, and administrative controls (training, PPE, procedures, ISO 7010 awareness signage). Residual risk remains where measures depend on correct LOTO, PPE use, and non-bypass of devices — clamping-related residual scores remain elevated for some production and setup tasks in the assessment summary.

Personnel categories: Operator (instructed), Maintenance person (skilled), Visitor (unskilled). Visitors must not enter hazard zones.

Full hazard identification and risk assessment is documented in the Machine Safety Assessment Report (Tilting Machine, report date 16 February 2026). This section is a summary only and does not replace that report.""",
    )
    alert_box(
        doc,
        "NOTICE",
        [
            "Open Actions register is maintained as a standalone Excel file — not inside this manual.",
            "File: KEMC_TiltingMachine_OpenActions_GrokSample_V1.0.xlsx",
        ],
    )


def section_4(doc):
    h1(doc, "4. Lockout / Tagout (LOTO) Procedures")
    h2(doc, "4.1 Energy Isolation Points")
    body(
        doc,
        """Isolate and verify all hazardous energy before entering the guarded process zone, performing electrical or pneumatic work, jaw setup, fixture changeover, or maintenance on clamps/tilt equipment.

Energy sources: Electrical 230 V single-phase 50 Hz; Pneumatic 5 bar; Hydraulic NA.""",
    )
    rows = [
        [lp["id"], lp["energy_type"], lp["image_code"], lp["isolation_method"], lp["location"]]
        for lp in DATA["loto_points"]
    ]
    styled_table(
        doc,
        ["Point ID", "Energy Type", "Image Code", "Isolation Method", "Location"],
        rows,
        [2, 2.5, 2.5, 5.5, 4.5],
    )
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Confirm pneumatic isolation device type and lockout hasp as-built — OA-P2G-006]"],
    )

    h2(doc, "4.2 LOTO Equipment Required")
    bullet(
        doc,
        [
            "Personal padlocks (one key per authorised person)",
            "Multi-person lockout hasps",
            "Tags (name, date, reason)",
            "Voltage tester / proving unit (qualified persons)",
            "Pneumatic lockout device / venting method for installed hardware",
            "Task-appropriate PPE",
        ],
    )

    flowchart(
        doc,
        "4.3 De-energization Sequence (Tag-Out)",
        [
            "START",
            "Notify affected personnel",
            "Shut down normal controls",
            "Isolate LP-01 electrical OFF + lock/tag",
            "Isolate LP-02 pneumatic + vent pressure",
            "Verify zero energy (try-start / test)",
            "Perform work",
            "END",
        ],
    )
    flowchart(
        doc,
        "4.4 Re-energization Sequence (Tag-In)",
        [
            "START",
            "Clear tools and personnel from zone",
            "Refit guards; confirm light curtain clear",
            "Remove locks/tags (owner only)",
            "Restore pneumatic then electrical",
            "Functional check of safety devices",
            "Notify personnel; resume production",
            "END",
        ],
    )

    h2(doc, "4.5 Partial Isolation")
    body(
        doc,
        """Partial isolation may be considered only with a documented task risk assessment confirming residual energy cannot cause injury. Default for this machine: isolate both electrical and pneumatic energy for any work inside the process/guarded zone, jaw setup (280 model), or fixture base plate changeover (230 / 280 / 310).""",
    )


def section_5(doc):
    h1(doc, "5. Emergency Stop Function")
    h2(doc, "5.1 E-Stop Device Locations")
    body(
        doc,
        """The Machine Safety Assessment identifies a front emergency stop push button (Front Estop) as an emergency stop safety function (SF99), with related devices assessed at PLr c where stated. Site photos locate a red mushroom E-Stop on the control column below the HMI.""",
    )
    styled_table(
        doc,
        ["ID", "Location", "Type", "Source"],
        [
            [es["id"], es["location"], es["type"], es.get("source", "RA / photo")]
            for es in DATA["e_stops"]
        ],
        [2, 7, 3.5, 4],
    )
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Confirm whether additional E-Stops exist on left/right stations or rear — OA-P2G-001]"],
    )

    h2(doc, "5.2 Stop Category")
    body(
        doc,
        """Emergency stop is implemented according to ISO 13850 and IEC 60204-1 principles as referenced in the Machine Safety Assessment. Exact Category 0 vs Category 1 behaviour for tilt motor and pneumatic dump shall be confirmed from manufacturer electrical documentation.""",
    )
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Confirm stop category for tilt motor and pneumatic dump — manufacturer design]"],
    )

    flowchart(
        doc,
        "5.3 E-Stop Activation Sequence",
        [
            "START",
            "Press nearest E-Stop",
            "Machine enters safe stop state",
            "Do not reset until area clear",
            "Investigate cause",
            "END",
        ],
    )
    flowchart(
        doc,
        "5.4 E-Stop Reset Procedure",
        [
            "START",
            "Confirm hazard removed / area clear",
            "Twist/pull reset E-Stop device",
            "Reset control system per HMI prompts",
            "Verify guards and light curtain OK",
            "Resume only if safe",
            "END",
        ],
    )

    h2(doc, "5.5 What the E-Stop Does NOT Do")
    bullet(
        doc,
        [
            "Not a substitute for Lockout/Tagout",
            "Not a replacement for isolation before maintenance",
            "May not remove all residual pneumatic pressure without air isolation and venting",
            "Not for routine cycle stop during normal production",
        ],
    )

    h2(doc, "5.6 Periodic E-Stop Testing")
    body(
        doc,
        """Test each E-Stop per site safety rules. Recommended minimum for this sample: start of shift/daily activate each known E-Stop, verify safe state, reset only when clear, confirm normal operation can resume. After control changes or incidents: full functional test before production release. Record tests in Appendix A.""",
    )


def section_6(doc):
    h1(doc, "6. Operating Instructions")
    h2(doc, "6.1 Operating Modes")
    body(
        doc,
        """Operating modes documented in the Machine Safety Assessment: Manual and Automatic.

Manual: operator-controlled steps for setup or supervised intervention as designed.
Automatic: production cycle after valid start conditions (guards intact, light curtain clear, two-hand start, no active E-Stop).

Operator interface (site photo): HMI on the right control column; cycle initiation via two-hand stations on the left and right front of the machine (paired red actuators). Green push buttons adjacent to stations are present — exact function (reset/start enable) shall be confirmed from manufacturer documentation.""",
    )
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Exact HMI mode selection path and interlocks — manufacturer HMI docs]"],
    )

    h2(doc, "6.2 Pre-Start Checklist")
    bullet(
        doc,
        [
            "Guards and mesh panels fitted and secure",
            "Light curtain clean, aligned, not improperly muted",
            "E-Stop(s) released and functional",
            "No unexplained lockout tags remaining",
            "Pneumatic supply ~5 bar; no major leaks",
            "Correct fixture base plate for model (230 / 280 / 310)",
            "Area clear of tools, loose parts, unauthorised persons",
            "PPE worn (safety shoes; gloves as required)",
            "Crane and load path clear for clutch plate handling",
            "No active alarms prohibiting start",
        ],
    )

    flowchart(
        doc,
        "6.3 Machine Startup Procedure",
        [
            "START",
            "Complete pre-start checklist",
            "Main isolator ON (if safe)",
            "Enable controls / select mode",
            "Verify safety devices healthy",
            "Ready for production cycle",
            "END",
        ],
    )
    flowchart(
        doc,
        "6.4 Normal Operating Cycle",
        [
            "START",
            "Crane-load clutch plate to fixture",
            "Confirm seating and area clear",
            "Two-hand cycle start",
            "Clamp and tilt to work angle",
            "Operator tightens nuts (nut runner)",
            "Return, unclamp, unload plate",
            "END",
        ],
    )

    h2(doc, "6.5 Process Description")
    body(
        doc,
        """Production task (assessment): Operator loads the clutch plate using a small crane, places it in the machine, and starts the process using cycle start — two-hand push buttons. The machine clamps the part, tilts to a comfortable angle, the operator tightens nuts, the machine returns, clamps release, and the part is unloaded.""",
    )
    alert_box(
        doc,
        "WARNING",
        [
            "Moving parts can crush and cut.",
            "Keep hands clear. Do NOT operate with guard removed.",
        ],
    )

    flowchart(
        doc,
        "6.6 Normal Shutdown",
        [
            "START",
            "Finish / clear cycle",
            "Unload workpiece",
            "Normal stop / idle",
            "Isolate if leaving unattended",
            "END",
        ],
    )
    flowchart(
        doc,
        "6.7 Emergency Shutdown",
        [
            "START",
            "Press E-Stop",
            "Keep personnel clear",
            "Isolate energies if entry needed",
            "Report and investigate",
            "END",
        ],
    )


def section_7(doc):
    h1(doc, "7. Maintenance & Care")
    h2(doc, "7.1 Weekly Maintenance")
    bullet(
        doc,
        [
            "Inspect fixed guards and mesh for damage/missing fasteners",
            "Check light curtain lenses and brackets",
            "Function-test E-Stop and two-hand control",
            "Inspect pneumatic hoses, fittings, cylinders for leaks/damage",
            "Verify warning/lockout signs remain legible",
            "Clean chips, oil, debris without defeating guards",
        ],
    )
    h2(doc, "7.2 Monthly Maintenance")
    bullet(
        doc,
        [
            "Inspect tilting mechanism fasteners and stops",
            "Check clamp jaw wear and fixture base plates for active models",
            "Verify isolator switch operation and labels",
            "Review open actions; no temporary safety bypasses for production",
        ],
    )
    h2(doc, "7.3 Periodic Maintenance")
    body(
        doc,
        """Assessment references preventive maintenance planned once in 15 days for sensors, actuators, and related scope. Align site PM with manufacturer recommendations when available. After any safety-affecting change, re-validate light curtain distance, two-hand function, and E-Stop before production.""",
    )
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — OEM spare parts list and lubrication schedule — manufacturer documentation]"],
    )
    h2(doc, "7.4 Consumables & Spare Parts")
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Consumables and critical spares (seals, sensors, light curtain, E-Stop, valves) — manufacturer BOM]"],
    )


def section_8(doc):
    h1(doc, "8. Electrical Schematic")
    h2(doc, "8.1 Key Electrical Parameters")
    body(
        doc,
        f"""Supply (Machine Safety Assessment): {DATA['electrical']['voltage']}, {DATA['electrical']['phases']}, {DATA['electrical']['frequency']}.
Power isolation: ON/OFF isolation switch on machine (rotary isolator with lockout warning label observed on site).""",
    )
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Full load current, SCCR, control voltage, cable sizes — electrical design package — OA-P2G-002]"],
    )
    h2(doc, "8.2 Electrical Schematic Drawings")
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Electrical schematic drawings not in assessment package used for this sample — OA-P2G-002]"],
    )


def section_9(doc):
    h1(doc, "9. Pneumatic Schematic")
    h2(doc, "9.1 Key Pneumatic Parameters")
    body(
        doc,
        f"""Supply pressure (Machine Safety Assessment): {DATA['pneumatic']['pressure']}.
Primary actuators: pneumatic clamping cylinders holding the clutch plate during tilt and nut installation.
Isolation: pneumatic energy isolation device (SF11) per assessment.""",
    )
    h2(doc, "9.2 Pneumatic Schematic Drawings")
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Pneumatic schematic drawings not provided — OA-P2G-003]"],
    )


def section_10(doc):
    h1(doc, "10. HMI / Alarms & Fault Codes")
    h2(doc, "10.1 Alarm Priority Levels")
    body(
        doc,
        """The assessment references an HMI providing operator information during gripping jaw setup (including sensor misalignment guidance). Full alarm taxonomy was not in the source package.""",
    )
    styled_table(
        doc,
        ["Priority", "Meaning", "Typical response"],
        [
            ["High", "Safety or major process stop", "Stop; do not bypass; escalate"],
            ["Medium", "Process fault / sensor issue", "Correct condition; follow HMI guidance"],
            ["Low / Info", "Operator guidance", "Acknowledge; continue if safe"],
        ],
        [3, 5, 8],
    )
    h2(doc, "10.2 Alarm / Fault Code List")
    alert_box(
        doc,
        "PLACEHOLDER",
        ["[PLACEHOLDER — Complete HMI/PLC alarm code register — OA-P2G-004]"],
    )
    flowchart(
        doc,
        "10.3 General Alarm Response Procedure",
        [
            "START",
            "Note alarm code / message",
            "Stop if unsafe condition",
            "Correct root cause",
            "Reset only when clear",
            "Escalate if unresolved",
            "END",
        ],
    )


def section_11(doc):
    h1(doc, "11. Safety Features & Interlocks")
    h2(doc, "11.1 Safety Architecture")
    body(
        doc,
        """Safety measures combine fixed guarding, electro-sensitive protective equipment (light curtain), two-hand control for cycle start, emergency stop, electrical isolation, and pneumatic isolation, supported by administrative controls (training, PPE, procedures, signage).""",
    )
    h2(doc, "11.2 Safety Control System")
    body(
        doc,
        """A safety-rated controller (SRPCS) is identified in the Machine Safety Assessment documentation imagery. Exact product model, I/O map, and validated safety functions shall be confirmed from manufacturer documentation (OA-P2G-007).""",
    )
    h2(doc, "11.3 Safety Device Inventory")
    rows = [[d["id"], d["name"], d["detail"], d.get("plr", "")] for d in DATA["safety_devices"]]
    styled_table(doc, ["ID", "Device", "Detail", "Notes / PLr"], rows, [2, 3.5, 7, 4])

    flowchart(
        doc,
        "11.4 Safety Interlock Logic (Overview)",
        [
            "START",
            "Guards + light curtain OK",
            "No E-Stop active",
            "Two-hand start valid",
            "Safety logic enables motion",
            "Hazard motion allowed",
            "END",
        ],
    )

    h2(doc, "11.5 Safety Function Testing Requirements")
    bullet(
        doc,
        [
            "Daily/shift: E-Stop; visual guard check; light curtain checks per site procedure",
            "After maintenance affecting safety: re-test affected functions before production",
            "Record results in Appendix A",
        ],
    )
    h2(doc, "11.6 Prohibited Actions")
    bullet(
        doc,
        [
            "Muting, bypassing, or defeating light curtains, two-hand controls, E-Stops, or guards",
            "Reaching into the process zone during automatic motion",
            "Operating with missing or open fixed guards",
            "Maintenance without LOTO",
            "Allowing untrained visitors inside barriers",
        ],
    )


def section_12(doc):
    h1(doc, "12. Compliance & Certifications")
    h2(doc, "12.1 International Safety Standards")
    bullet(
        doc,
        [
            "ISO 12100:2010 — Risk assessment and risk reduction",
            "ISO 20607:2019 — Instruction handbooks for machinery",
            "IEC 82079-1:2019 — Preparation of instructions for use",
            "ISO 13850 — Emergency stop function",
            "ISO 13849-1 — Safety-related parts of control systems (PLr concepts as in assessment)",
            "ISO 13851 / ISO 13855 — Two-hand control and safeguard positioning (as referenced)",
            "ISO 14120 / ISO 13857 — Guards and safety distances (as referenced)",
            "ISO 4414 — Pneumatic fluid power (as referenced)",
            "IEC 60204-1 — Electrical equipment of machines (as referenced)",
            "ANSI B11.19 — Safeguarding performance criteria (as referenced for awareness signs)",
        ],
    )
    h2(doc, "12.2 Indian Standards & Regulations")
    bullet(
        doc,
        [
            "IS 4571:2008 — machinery safety documentation practice as applied by this framework",
            "Factories Act, 1948 and applicable State Factory Rules",
        ],
    )
    h2(doc, "12.3 Component-Level Standards")
    body(
        doc,
        """Component conformity (light curtain Type 4, safety controller, etc.) shall be verified against manufacturer declarations. This sample does not restate unconfirmed certificates.""",
    )
    h2(doc, "12.4 Compliance Statement — Liability Disclaimer")
    body(
        doc,
        """LIABILITY DISCLAIMER

This Operating & Safety Manual has been prepared by a Certified Safety Professional in accordance with ISO 12100:2010, ISO 20607:2019, IEC 82079-1:2019, and IS 4571:2008, based on the Machine Safety Assessment and technical information available for this Grok sample draft.

Where original technical data was unavailable, items are marked as placeholders or logged as Open Actions. The customer and manufacturer are responsible for final review and verification before the machine is placed into service or this manual is released as controlled issue.

Neither the consulting practice nor the author assumes liability for injuries or damages resulting from: non-compliance with this manual; failure to maintain per the schedule; operation by untrained personnel; or use of superseded draft sample content without formal release.""",
    )
    h2(doc, "12.5 Document Control")
    styled_table(
        doc,
        ["Field", "Value"],
        [
            ["Document title", "Operating & Safety Manual — Tilting Machine"],
            ["Status", DATA["status"]],
            ["Revision", DATA["revision"]],
            ["Date", DATA["date"]],
            ["Open Actions file", f"KEMC_TiltingMachine_OpenActions_GrokSample_{DATA.get('revision', 'V1.0')}.xlsx"],
        ],
        [5, 11],
    )
    h2(doc, "12.6 Customer Sign-Off")
    body(doc, "Sign-off blocks — single instance at end of Section 12 only.")
    for role in [
        "Manufacturer Authorization — Name / Signature / Date",
        "End User Authorization — Name / Signature / Date",
        "Certified Safety Professional — Manual Author — Signature / Date (role only; no individual name printed as author title)",
    ]:
        p = doc.add_paragraph()
        r = p.add_run(role)
        set_run(r, size=11)
        p2 = doc.add_paragraph()
        r2 = p2.add_run("Signature: ________________________     Date: ______________")
        set_run(r2, size=11)
        doc.add_paragraph()


def appendix_a(doc):
    h1(doc, "Appendix A — Maintenance Log Template")
    body(doc, "Blank log for recording maintenance and safety-function tests. Minimum 10 rows.")
    headers = ["Date", "Task / Test", "Result (Pass/Fail)", "Technician", "Remarks"]
    rows = [["", "", "", "", ""] for _ in range(10)]
    styled_table(doc, headers, rows, [2.5, 5, 3, 3, 3.5])


def appendix_b(doc):
    h1(doc, "Appendix B — LOTO Log Template")
    body(doc, "Blank log for Lockout/Tagout events. Minimum 10 rows.")
    headers = ["Date", "Point ID(s)", "Reason", "Locked By", "Removed By", "Time On", "Time Off"]
    rows = [["", "", "", "", "", "", ""] for _ in range(10)]
    styled_table(doc, headers, rows, [2, 2, 3, 2.5, 2.5, 2, 2])


def main():
    doc = Document()
    # default style
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

    cover(doc)
    build_header_footer(doc)
    revision_page(doc)
    toc_page(doc)
    section_1(doc)
    section_2(doc)
    section_3(doc)
    section_4(doc)
    section_5(doc)
    section_6(doc)
    section_7(doc)
    section_8(doc)
    section_9(doc)
    section_10(doc)
    section_11(doc)
    section_12(doc)
    appendix_a(doc)
    appendix_b(doc)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUT))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
