# WORKFLOW_C.md — VS Code IDE Workflow
## Codex (Prep Assistant) → Claude Code (Main Author) → .docx + .xlsx

**Owner:** Certified Safety Professional
**Use When:** Working inside VS Code with both Codex and Claude Code installed, raw RA + drawings + images need processing before authoring begins
**Last Updated:** May 2026
**Formatting Spec:** `OSM_WORD_FORMAT_STANDARD_V1_2.md`
**Relationship to other workflows:**
- WORKFLOW_A = Chat-based (ChatGPT + Claude Chat). No IDE.
- WORKFLOW_B = Code generation only, assumes inputs already prepared.
- **WORKFLOW_C (this file) = bridges raw inputs → WORKFLOW_B inputs, all inside VS Code.**

---

## ROLE SPLIT — THE GOLDEN RULE

| Tool | Role | What It Does | What It Does NOT Do |
|------|------|--------------|---------------------|
| **Codex** | Prep Assistant | Parses RA PDFs, extracts specs, organises images, builds `machine_data.json` + `section_content.yaml` skeleton, lists placeholders, seeds open actions | Authors manual content, generates Word file, makes safety judgments |
| **Claude Code** | Main Author | Reviews Codex output, fills in narrative sections, applies tier rules, generates `.docx` and `.xlsx`, runs validation | Parses raw PDFs (slower, more token-heavy than Codex), reorganises raw files |
| **Claude Chat (Anthropic web app)** | Reviewer | Final compliance audit, tier scoping decisions, catches gaps Codex/Claude Code missed | Generates files (not its strength) |

> **Why this split?** Codex is faster and cheaper for mechanical parsing tasks. Claude Code is stronger for structured authoring against a spec. Using both keeps token costs down and reduces the chance of either tool inventing content.

---

## PROJECT FOLDER SETUP (Before Either Tool Runs)

Inside your VS Code workspace `MACHINE MANUALS/Projects/`, create the project folder per `PROJECT-README-TEMPLATE.md`:

```
Pxx-customer-name/
├── PROJECT-README.md          ← Filled from template
├── 00-raw-inputs/             ← Drop everything here first
│   ├── RA/                    ← SICK / TÜV RA reports
│   ├── drawings/              ← GA, schematics, layouts
│   ├── photos/                ← Site photos (raw, unsorted)
│   └── customer-docs/         ← OEM manuals, datasheets, BOM
├── 01-codex-output/           ← Codex writes here
│   ├── machine_data.json
│   ├── section_content.yaml
│   ├── placeholders.md
│   ├── open_actions_seed.md
│   └── image_manifest.json
├── 02-claude-code-work/       ← Claude Code working directory
│   ├── sections/              ← Individual section .js files
│   └── temp/                  ← Intermediate Word files
└── 03-deliverables/           ← Final .docx + .xlsx + .pdf
```

> **Rule:** Codex never writes to `02-` or `03-`. Claude Code never writes to `00-` or `01-`. This prevents either tool from overwriting the other's work.

---

## STEP 1 — CODEX PREP PHASE

### Prompt to Paste in Codex (Inside VS Code)

```
CODEX PREP BRIEF — [Project Code] [Machine Name]

You are the prep assistant for an Operating & Safety Manual project.
Working directory: Projects/[Pxx-customer-name]/

INPUTS (in 00-raw-inputs/):
- RA report(s) in /RA/
- Drawings in /drawings/
- Site photos in /photos/
- OEM docs in /customer-docs/

OUTPUTS (write to 01-codex-output/):

1. machine_data.json — populate per WORKFLOW_B.md File 1 schema:
   - project_code, end_user, client, machine_name, machine_ref, site
   - tier (leave as "TBD" — Ravi confirms)
   - loto_points[] (extract from RA energy isolation section)
   - open_actions[] (seed only — from RA recommendations marked open)

2. section_content.yaml — skeleton only, per WORKFLOW_B.md File 2 schema:
   - section_2 through section_13 keys present
   - subsection titles filled
   - content blocks left as empty strings OR
     "[CODEX-EXTRACT: <one-line summary of what RA says here>]"
   - DO NOT write narrative prose. That's Claude Code's job.

3. placeholders.md — flat list of every missing data point:
   - Format: "- [SECTION x.y] Description — Source: <where to get it>"
   - Examples: motor nameplate ratings, servo specs, pneumatic pressure setpoints

4. open_actions_seed.md — preliminary OAs spotted in RA:
   - One per line: "OA-Pxx-NNN | Description | Category | Priority"
   - Categories per WORKFLOW_B: Safety Gap / Documentation / Schematic / Software / Maintenance

5. image_manifest.json — every file in /photos/ and /drawings/:
   - filename, suggested_caption, suggested_section, status
   - status = "raw" | "needs_crop" | "needs_annotation" | "ready"

HARD RULES — DO NOT BREAK:
- NEVER invent machine specs not present in source files
- If a value is unclear or missing, list it in placeholders.md — do NOT guess
- NEVER write Section 1 (cover, TOC) — Claude Code generates that
- NEVER write narrative content — only structured extraction
- NEVER reference SICK, TÜV, or any RA firm name — use "Independent Safety Consultant"
- NEVER create files outside 01-codex-output/
- If RA PDF table extraction fails, write "[EXTRACTION FAILED — manual entry needed]"
  in the relevant field. Do not fabricate values.

REFERENCE FILES (read before starting):
- WORKFLOW_B.md (input file schemas)
- OSM_WORD_FORMAT_STANDARD_V1_2.md (formatting constraints to be aware of)
- CLAUDE.md (AI behaviour rules — apply these to Codex too)
- INDEX.md (project context)

Confirm the project folder structure exists before writing anything.
Then proceed file by file. Report any extraction failures explicitly.
```

### Codex Output Validation (Before Handing to Claude Code)

Open each file in `01-codex-output/` and check manually:

- [ ] `machine_data.json` parses as valid JSON (no syntax errors)
- [ ] No invented specs — every value traceable to a source file
- [ ] `tier` field still says "TBD" (you set this, not Codex)
- [ ] `section_content.yaml` has empty content blocks, not fake prose
- [ ] `placeholders.md` lists everything you'd expect to be missing
- [ ] `image_manifest.json` covers every file in `00-raw-inputs/photos/` and `/drawings/`
- [ ] No mention of SICK / TÜV / RA firm anywhere
- [ ] No DANGER box references (Codex shouldn't be writing alert boxes at all)

If any check fails, fix the prompt and re-run Codex. Don't proceed to Step 2 with broken prep files.

---

## STEP 2 — TIER DECISION (You, Not the Tools)

Before Claude Code starts, you decide tier based on what Codex extracted. Use the tier scoping table from WORKFLOW_A.md / WORKFLOW_B.md.

Update `machine_data.json` → `"tier": "A"` (or B or C).

Update `PROJECT-README.md` with the tier and reasoning.

---

## STEP 3 — CLAUDE CODE AUTHORING PHASE

### Prompt to Paste in Claude Code (Inside VS Code)

```
CLAUDE CODE AUTHOR BRIEF — [Project Code] [Machine Name]

You are the main author for this Operating & Safety Manual.
Working directory: Projects/[Pxx-customer-name]/

INPUTS (read from 01-codex-output/):
- machine_data.json (tier now confirmed)
- section_content.yaml (skeleton — you fill the narrative)
- placeholders.md (missing data — preserve as [PLACEHOLDER — ...] bold tags)
- open_actions_seed.md (carry into final .xlsx)
- image_manifest.json (image references)

WORKING DIRECTORY: 02-claude-code-work/
OUTPUT DIRECTORY: 03-deliverables/

REFERENCE FILES (read before starting):
- WORKFLOW_B.md (generation technical brief — sections "STEP 2" onward)
- OSM_WORD_FORMAT_STANDARD_V1_2.md (formatting — apply throughout)
- CLAUDE.md (AI behaviour rules)
- /mnt/skills/public/docx/SKILL.md (Node.js docx library guidance)

YOUR JOB:
1. Read all inputs above
2. For each section in section_content.yaml:
   - Fill the empty content blocks with proper narrative
   - Apply tier rules (Section Map by Tier from WORKFLOW_B)
   - Use [PLACEHOLDER — description, source, status] bold for missing data
   - Generate flowcharts for sections 4.4, 4.5, 5.4, 5.5, 6.4, 6.5, 6.7, 6.8, 6.9, 11.4, 12.2
   - Section 3 = max 2 pages, narrative only, no tables, no boxes
3. Generate .docx using Node.js docx v9.6.1
   - One .js file per section in 02-claude-code-work/sections/
   - Inject via Python content.replace() — NEVER str_replace for Unicode
   - Validate after each section: python3 /mnt/skills/public/docx/scripts/office/validate.py
4. Generate Open Actions .xlsx using openpyxl
   - 3 sheets per WORKFLOW_B spec
   - Carry over seed entries from open_actions_seed.md
5. Place final files in 03-deliverables/:
   - [EndUser]_[MachineName]_OSM_V1.0.docx
   - [Client]_[MachineName]_OpenActions_V1.0.xlsx

HARD RULES — DO NOT BREAK:
- NEVER invent specs — if not in machine_data.json or placeholders.md, leave as placeholder
- NEVER use DANGER boxes anywhere
- NEVER put liability disclaimer outside Section 13
- NEVER put Open Actions Register inside the .docx — standalone .xlsx only
- NEVER name SICK or any RA firm — use "Independent Safety Consultant" / "Machine Safety Assessment"
- NEVER include Residual Risk appendix (permanently removed)
- NEVER reference IEC 61508 or IEC 61800-5-2
- NEVER write the individual name — use "Certified Safety Professional"
- NEVER patch the .docx manually — fix source files and regenerate

PROCEED SECTION BY SECTION. Confirm completion of each section before next.
Run validation after each section. Stop and report any failure.
```

---

## STEP 4 — REVIEW (Claude Chat — Web App, Not Inside VS Code)

Open Claude Chat (web/desktop app, not Claude Code in IDE). Upload the generated `.docx` from `03-deliverables/`.

Run the Compliance Audit Checklist from WORKFLOW_B.md.

If anything fails:
1. Identify which source file in `01-codex-output/` caused it
2. Fix the source file (not the .docx)
3. Re-run Claude Code Step 3 to regenerate

**Never edit the .docx manually.** This is the same rule as WORKFLOW_B.

---

## QUICK DECISION TREE — WHICH TOOL FOR WHICH TASK?

| Task | Tool | Why |
|------|------|-----|
| "Read this RA PDF and pull out hazards" | Codex | Faster, mechanical extraction |
| "Extract LOTO points table from RA" | Codex | Structured table parsing |
| "Rename 30 site photos to P5_Photo_NN format" | Codex | Bulk file ops |
| "Build machine_data.json from RA" | Codex | Schema-driven extraction |
| "Write Section 4 narrative for LOTO procedures" | Claude Code | Authoring against spec |
| "Generate the .docx file" | Claude Code | Better with Node.js docx library |
| "Apply OSM formatting standard" | Claude Code | Holds long spec in context |
| "Generate flowcharts for Section 6" | Claude Code | Authoring decision required |
| "Check if manual passes compliance audit" | Claude Chat | Best for review/audit reasoning |
| "Should this be Tier A or Tier B?" | You (with Claude Chat help) | Tools shouldn't decide tier alone |
| "Is this safety gap a real OA?" | You (with Claude Chat help) | Judgment call |

---

## COMMON PITFALLS — LEARNED FROM P1–P4

1. **Codex hallucination on PDF tables.** SICK RA reports have complex nested tables. Always spot-check the first 3 extracted rows against the PDF before trusting the rest. If wrong, switch to `pdfplumber` via a Python script.

2. **The coolant lesson (P1).** Codex may infer "this is a machining centre → has coolant." It does not. If the RA doesn't mention coolant, it doesn't exist. Add to prompt: "Do not infer subsystems not explicitly named in RA."

3. **Image manifest drift.** Codex sometimes misses photos in nested folders. Verify the count: `ls 00-raw-inputs/photos/ | wc -l` should match entries in `image_manifest.json`.

4. **Tier confusion.** If Codex sets tier itself, Claude Code will follow it blindly. Always leave tier = "TBD" in Codex output and set it yourself.

5. **Permission mode.** In VS Code Codex panel, "Medium" permission requires approval for each file write. For bulk prep work, switch to higher trust temporarily, then revert. Never leave on max permission.

6. **Token economy.** Don't ask Codex to read every PDF page if only the energy isolation section matters. Point it to specific page ranges in the prompt: "Read pages 12–18 of RA.pdf for LOTO data."

7. **Don't mix workflows mid-project.** If you started with WORKFLOW_A (chat-only), don't switch to WORKFLOW_C halfway. Finish the project on one workflow.

---

## PROJECT REGISTRY (Same as WORKFLOW_A/B — for context)

| Code | Client | Machine | Tier | Status | Workflow Used |
|------|--------|---------|------|--------|---------------|
| P1 | Accurate Machines | 48-Spindle Drilling | A | ✅ Complete | A |
| P2 | KEMC / Valeo | Tilting Machine | B | ✅ Complete | A |
| P3 | Valeo | LE Test Bench | A | ✅ Complete | A |
| P4 | Indo-MIM / Tata | BG Snap Assembly (V67) | A | ✅ Complete | B |
| P5+ | TBD | TBD | TBD | — | Try Workflow C |

---

## CROSS-REFERENCE TO OTHER FILES

| When you need... | Refer to... |
|------------------|-------------|
| Input file schemas (`machine_data.json`, `section_content.yaml`) | WORKFLOW_B.md |
| Authoring brief for chat-based work | WORKFLOW_A.md |
| Formatting rules (colours, fonts, alert boxes, flowcharts) | OSM_WORD_FORMAT_STANDARD_V1_2.md |
| AI behaviour rules (tone, what not to do) | CLAUDE.md |
| Tier scoping decision tree | WORKFLOW_A.md or WORKFLOW_B.md (identical tables) |
| Compliance audit checklist | WORKFLOW_B.md |
| Project folder structure | INDEX.md + PROJECT-README-TEMPLATE.md |
| DFM-specific rules (Indo MIM / Apple only) | DFM.md |

This file does NOT repeat content from the above — it only adds the Codex prep stage and the role split.

---

## WHAT THIS WORKFLOW IS NOT

- ❌ Not a replacement for WORKFLOW_A or WORKFLOW_B
- ❌ Not for projects without VS Code access
- ❌ Not for one-off small jobs (overhead too high for Tier C with single RA)
- ❌ Not a way to skip the compliance audit (Step 4 is mandatory)
- ❌ Not Codex-only or Claude-Code-only — both must participate
