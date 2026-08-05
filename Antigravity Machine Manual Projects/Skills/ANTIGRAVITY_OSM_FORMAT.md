# ANTIGRAVITY_OSM_FORMAT — Word Format (Indo-MIM V5 Style)

Derived for Antigravity sandbox from Indo-MIM OSM V5 visual style and OSM Word Format Standard V1.2.  
**Does not modify** root `Skills/Word-format/`.

## Output location

Generated manuals always under:

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Antigravity Machine Manual Projects\<pilot>\outputs\
```

Never under worktrees.

## Page

| Parameter | Value |
|-----------|-------|
| Paper | A4 portrait |
| Margins | 25 mm all sides |
| Header from edge | 12 mm |
| Footer from edge | 12 mm |

## Typography

**Calibri throughout.**

| Element | Size | Weight | Colour |
|---------|------|--------|--------|
| Cover title | 22 pt | Bold | #1F3864 |
| Cover machine name | 18 pt | Bold | #1F3864 |
| H1 | 14 pt | Bold | #1F3864 |
| H2 | 13 pt | Bold | #1F3864 |
| H3 | 12 pt | Bold | #1F3864 |
| Body | 11 pt | Regular | #000000 |
| Table header | 10 pt | Bold | #FFFFFF |
| Table body | 10 pt | Regular | #000000 |
| Caption | 10 pt | Italic | #555555 |
| Header/footer | 9 pt | Regular | #1F3864 / #555555 |

## Colours

| Use | Hex |
|-----|-----|
| Headings, table headers, borders, flowchart borders | #1F3864 |
| Alt table rows, flowchart sub-steps | #D9E1F2 |
| WARNING box fill | #FFF2CC |
| CAUTION / OPEN ACTION fill | #FCE4D6 |
| NOTICE fill | #F2F2F2 |
| PLACEHOLDER fill | #F7F7F7 |

**No DANGER boxes.**

## Header / footer

- Header (not cover): Left = machine name · Centre = Operating & Safety Manual · Right = Page N of N  
- Footer: **CONFIDENTIAL** centred  
- Cover: no header/footer  

## Document order

1. Cover  
2. Revision history (4 columns: Revision / Date / Description / Reviewed By)  
3. TOC (H1 only)  
4. Sections 1–12 (Indo-MIM V5 map)  
5. Appendix A — Maintenance Log Template  
6. Appendix B — LOTO Log Template  

Each major section starts on a new page.

## Section map (Indo-MIM V5 style)

| Sec | Title |
|-----|-------|
| 1 | Front Matter |
| 2 | Machine Overview |
| 3 | Hazard Identification & Risk Assessment |
| 4 | Lockout / Tagout (LOTO) Procedures |
| 5 | Emergency Stop Function |
| 6 | Operating Instructions |
| 7 | Maintenance & Care |
| 8 | Electrical Schematic |
| 9 | Pneumatic Schematic |
| 10 | HMI / Alarms & Fault Codes |
| 11 | Safety Features & Interlocks |
| 12 | Compliance & Certifications |

## Tables

- Header fill #1F3864, text white  
- Alternating rows white / #D9E1F2  
- Border 0.5 pt #1F3864  

## Flowcharts

Table-based vertical flow (greyscale-readable):

- Start/End: fill #1F3864, text white  
- Steps: white fill, #1F3864 border/text  
