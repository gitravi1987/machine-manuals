#!/usr/bin/env python3
"""Read-only format comparison: Indo-MIM V5.0 vs P7 Rani OSM V1.0. Does not modify either file."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Emu, Twips

# Primary V5.0 may be open/locked in Word; fall back to V5.0 - 1 copy.
INDO_PRIMARY = Path(
    r"C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals"
    r"\Projects\P5 - Indo MIM\IndoMIM_BGSnap_OSM_V5.0.docx"
)
INDO_FALLBACK = Path(
    r"C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals"
    r"\Projects\P5 - Indo MIM\IndoMIM_BGSnap_OSM_V5.0 - 1.docx"
)
INDO = INDO_PRIMARY
P7 = Path(
    r"C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals"
    r"\Grok Machine Manual Projects\P7 - Rani Enterprises\outputs"
    r"\RaniEnterprises_RoboticSealantDispenser_OSM_V1.0.docx"
)


def rgb_of(run):
    try:
        c = run.font.color.rgb
        return str(c) if c else None
    except Exception:
        return None


def font_name(run):
    return run.font.name


def font_size_pt(run):
    if run.font.size is None:
        return None
    return round(run.font.size.pt, 1)


def para_style(p):
    try:
        return p.style.name if p.style else None
    except Exception:
        return None


def outline_level(p):
    pPr = p._p.pPr
    if pPr is None:
        return None
    ol = pPr.find(qn("w:outlineLvl"))
    if ol is not None:
        return ol.get(qn("w:val"))
    return None


def shading_fill(cell):
    tcPr = cell._tc.tcPr
    if tcPr is None:
        return None
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        return None
    return shd.get(qn("w:fill"))


def border_color(cell):
    tcPr = cell._tc.tcPr
    if tcPr is None:
        return None
    borders = tcPr.find(qn("w:tcBorders"))
    if borders is None:
        return None
    top = borders.find(qn("w:top"))
    if top is None:
        return None
    return top.get(qn("w:color")), top.get(qn("w:sz"))


def section_geom(sec):
    return {
        "page_w_mm": round(sec.page_width.mm, 1) if sec.page_width else None,
        "page_h_mm": round(sec.page_height.mm, 1) if sec.page_height else None,
        "left_mm": round(sec.left_margin.mm, 1) if sec.left_margin else None,
        "right_mm": round(sec.right_margin.mm, 1) if sec.right_margin else None,
        "top_mm": round(sec.top_margin.mm, 1) if sec.top_margin else None,
        "bottom_mm": round(sec.bottom_margin.mm, 1) if sec.bottom_margin else None,
        "header_mm": round(sec.header_distance.mm, 1) if sec.header_distance else None,
        "footer_mm": round(sec.footer_distance.mm, 1) if sec.footer_distance else None,
        "diff_first": sec.different_first_page_header_footer,
        "orientation": str(sec.orientation) if hasattr(sec, "orientation") else None,
    }


def header_footer_text(sec, which="header"):
    out = []
    parts = []
    try:
        hf = sec.header if which == "header" else sec.footer
        for p in hf.paragraphs:
            t = p.text.strip()
            if t:
                parts.append(t)
            # field codes?
            xml = p._p.xml
            if "PAGE" in xml or "NUMPAGES" in xml:
                if "NUMPAGES" in xml:
                    parts.append("[FIELD: PAGE of NUMPAGES]")
                elif "PAGE" in xml:
                    parts.append("[FIELD: PAGE]")
        # first page
        if sec.different_first_page_header_footer:
            fhf = sec.first_page_header if which == "header" else sec.first_page_footer
            ft = " | ".join(x.text.strip() for x in fhf.paragraphs if x.text.strip())
            out.append(f"first_page: {ft!r}")
        out.append("default: " + " | ".join(parts))
    except Exception as e:
        out.append(f"err: {e}")
    return out


def style_snapshot(doc):
    wanted = ["Normal", "Heading 1", "Heading 2", "Heading 3", "Title", "List Bullet"]
    snap = {}
    for name in wanted:
        try:
            st = doc.styles[name]
        except KeyError:
            snap[name] = "MISSING"
            continue
        font = st.font
        pf = st.paragraph_format
        snap[name] = {
            "font": font.name,
            "size_pt": round(font.size.pt, 1) if font.size else None,
            "bold": font.bold,
            "color": str(font.color.rgb) if font.color and font.color.rgb else None,
            "space_before": round(pf.space_before.pt, 1) if pf.space_before else None,
            "space_after": round(pf.space_after.pt, 1) if pf.space_after else None,
        }
    return snap


def collect_run_stats(doc, limit_paras=400):
    fonts = Counter()
    sizes = Counter()
    colors = Counter()
    bold_sizes = Counter()
    style_counts = Counter()
    outline_counts = Counter()
    large_samples = []  # (size, bold, color, font, text[:60], style)

    for i, p in enumerate(doc.paragraphs[:limit_paras]):
        style_counts[para_style(p)] += 1
        ol = outline_level(p)
        if ol is not None:
            outline_counts[ol] += 1
        for r in p.runs:
            t = (r.text or "").strip()
            if not t:
                continue
            fn = font_name(r) or "(inherit/None)"
            fs = font_size_pt(r)
            col = rgb_of(r) or "(auto/None)"
            fonts[fn] += 1
            if fs is not None:
                sizes[fs] += 1
                if r.bold:
                    bold_sizes[fs] += 1
            colors[col] += 1
            if fs and fs >= 12:
                large_samples.append((fs, bool(r.bold), col, fn, t[:70], para_style(p)))

    return {
        "fonts": fonts.most_common(10),
        "sizes": sizes.most_common(15),
        "colors": colors.most_common(12),
        "bold_sizes": bold_sizes.most_common(10),
        "styles": style_counts.most_common(15),
        "outline_levels": outline_counts.most_common(),
        "large_samples": large_samples[:25],
    }


def table_stats(doc, max_tables=40):
    fills = Counter()
    border_cols = Counter()
    border_sz = Counter()
    header_text_colors = Counter()
    n_tables = len(doc.tables)
    n_cells = 0
    col_counts = Counter()
    sample_first_rows = []

    for ti, table in enumerate(doc.tables[:max_tables]):
        col_counts[len(table.columns)] += 1
        if not table.rows:
            continue
        # first row often header
        row0 = table.rows[0]
        row0_texts = []
        for cell in row0.cells:
            n_cells += 1
            fill = shading_fill(cell)
            if fill:
                fills[fill.upper()] += 1
            bc = border_color(cell)
            if bc:
                border_cols[bc[0]] += 1
                border_sz[bc[1]] += 1
            for p in cell.paragraphs:
                for r in p.runs:
                    if (r.text or "").strip():
                        header_text_colors[rgb_of(r) or "(auto)"] += 1
            row0_texts.append(cell.text.strip()[:40])
        if ti < 8:
            sample_first_rows.append(row0_texts)

        # body cells sample from row 1
        if len(table.rows) > 1:
            for cell in table.rows[1].cells:
                n_cells += 1
                fill = shading_fill(cell)
                if fill:
                    fills[fill.upper()] += 1

    return {
        "n_tables_total": len(doc.tables),
        "n_tables_sampled": min(max_tables, n_tables),
        "col_counts": col_counts.most_common(),
        "fills": fills.most_common(15),
        "border_colors": border_cols.most_common(10),
        "border_sizes": border_sz.most_common(10),
        "header_run_colors": header_text_colors.most_common(10),
        "sample_first_rows": sample_first_rows,
    }


def count_images(doc):
    n = 0
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            n += 1
    return n


def h1_like_headings(doc):
    """Collect candidate H1s: outline 0 or large bold navy-ish or style Heading 1."""
    heads = []
    for p in doc.paragraphs:
        text = p.text.strip()
        if not text or len(text) > 120:
            continue
        st = para_style(p)
        ol = outline_level(p)
        bold = any(r.bold for r in p.runs if r.text.strip())
        sizes = [font_size_pt(r) for r in p.runs if r.text.strip() and font_size_pt(r)]
        maxs = max(sizes) if sizes else None
        cols = [rgb_of(r) for r in p.runs if r.text.strip() and rgb_of(r)]
        if st and st.startswith("Heading") or ol == "0" or (bold and maxs and maxs >= 13):
            if text[0].isdigit() or text.startswith("Appendix") or text in (
                "Revision History",
                "Table of Contents",
                "OPERATING & SAFETY MANUAL",
            ) or "SECTION" in text.upper() or st == "Heading 1":
                heads.append((text[:90], st, ol, maxs, cols[:1], bold))
    return heads[:40]


def analyze(label, path: Path):
    print("=" * 80)
    print(label)
    print(path)
    print("size_bytes", path.stat().st_size)
    doc = Document(str(path))
    print("n_sections", len(doc.sections))
    print("n_paragraphs", len(doc.paragraphs))
    print("n_tables", len(doc.tables))
    print("n_images_rels", count_images(doc))

    for i, sec in enumerate(doc.sections[:3]):
        print(f"section[{i}] geom", section_geom(sec))
        print(f"section[{i}] header", header_footer_text(sec, "header"))
        print(f"section[{i}] footer", header_footer_text(sec, "footer"))

    print("styles", style_snapshot(doc))
    rs = collect_run_stats(doc, limit_paras=500)
    print("run fonts", rs["fonts"])
    print("run sizes", rs["sizes"])
    print("run colors", rs["colors"])
    print("bold sizes", rs["bold_sizes"])
    print("para styles used", rs["styles"])
    print("outline levels", rs["outline_levels"])
    print("large text samples:")
    for s in rs["large_samples"][:20]:
        print(" ", s)

    ts = table_stats(doc, max_tables=50)
    print("table stats", {k: v for k, v in ts.items() if k != "sample_first_rows"})
    print("table first-row samples:")
    for row in ts["sample_first_rows"]:
        print(" ", row)

    print("heading-like:")
    for h in h1_like_headings(doc)[:30]:
        print(" ", h)

    # cover first 25 non-empty paragraphs
    print("first 25 non-empty paragraphs:")
    n = 0
    for p in doc.paragraphs:
        t = p.text.strip()
        if not t:
            continue
        runs_info = []
        for r in p.runs:
            if not (r.text or "").strip():
                continue
            runs_info.append(
                f"{font_name(r)}/{font_size_pt(r)}pt/b={r.bold}/c={rgb_of(r)}"
            )
        print(f"  [{para_style(p)}] {t[:100]!r} :: {runs_info[:3]}")
        n += 1
        if n >= 25:
            break

    return doc


def main():
    indo_path = INDO_PRIMARY
    try:
        Document(str(INDO_PRIMARY))
    except Exception as e:
        print("PRIMARY INDO V5.0 not readable:", e)
        indo_path = INDO_FALLBACK
        print("Using fallback:", indo_path)
    analyze("INDO-MIM V5", indo_path)
    analyze("P7 RANI V1.0", P7)


if __name__ == "__main__":
    main()
