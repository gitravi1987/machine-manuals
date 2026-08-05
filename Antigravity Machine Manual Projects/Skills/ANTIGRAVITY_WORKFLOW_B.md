# ANTIGRAVITY_WORKFLOW_B — Code-Based Manual Creation (Sandbox)

## ALWAYS CREATE FILES HERE

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Antigravity Machine Manual Projects\
```

Machine Manuals root:

```
C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals
```

Never write Antigravity pilots under worktrees. Use the absolute path above even if the session workspace is a worktree.

## Overview

```
RA PDF + photos (read-only from Machine Manuals\Projects\)
        ↓
STEP 1 — Extract data, list gaps, draft machine_data.json + section_content.yaml
          → under Antigravity Machine Manual Projects\<pilot>\inputs\
        ↓
STEP 2 — Generate .docx + .xlsx under pilot outputs/
        ↓
STEP 3 — Self-QA against format + integrity checklist
```

## STEP 1 — Ingest & draft

1. Read full Machine Safety Assessment (RA) PDF from `Projects\`  
2. Review site photos in batches (panel, E-stop, LOTO, guards, process zone)  
3. Confirm tier (A/B/C)  
4. Write `inputs\machine_data.json` (absolute pilot path under Machine Manuals)  
5. Write `inputs\section_content.yaml`  
6. Log open actions for every unresolved safety-critical gap  

## STEP 2 — Generate

- Word: **python-docx** (or Node `docx` if available), Calibri, A4, colours per `ANTIGRAVITY_OSM_FORMAT.md`  
- Excel: openpyxl — columns ID / Description / Category / Priority / Responsibility / Target Date / Status  
- Working files only under pilot `working\`  
- Never patch final `.docx` by hand — fix sources and regenerate  

## STEP 3 — Checklist

- [ ] All files under  
  `C:\Users\Ravi.Kumar\OneDrive - Halma Holdings Inc\Desktop\Halma\Ravi\Work\Machine Manuals\Antigravity Machine Manual Projects\`  
- [ ] Nothing created under worktrees  
- [ ] No SICK / RA firm names  
- [ ] No individual author names  
- [ ] No DANGER boxes  
- [ ] No DFM content (unless pilot is DFM)  
- [ ] Specs match RA or marked PLACEHOLDER  
- [ ] Appendices A/B only as log templates  
- [ ] Open Actions in `.xlsx` only  
