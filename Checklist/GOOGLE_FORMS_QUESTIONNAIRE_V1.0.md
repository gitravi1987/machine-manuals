# Google Forms Questionnaire — Operating & Safety Manual Data Collection
**Aligned with 13-Section Manual Structure**  
**Purpose:** Capture machine-specific details NOT in Risk Assessment report  
**Output:** Convert handwritten/image notes to Q&A.md file for project repository  

---

## 📋 FORM METADATA

| Field | Value |
|-------|-------|
| **Form Title** | Operating & Safety Manual — Data Collection Questionnaire |
| **Form Description** | Help us create a comprehensive, compliant manual. This form captures technical details, safety procedures, and operational information. Est. time: 25–30 min. |
| **Respondent Email Collection** | ✅ Enabled (for follow-up questions) |
| **Shuffle Question Order** | ❌ Disabled (questions should appear in section order) |
| **Show Progress Bar** | ✅ Enabled |
| **Form Confirmation Message** | "Thank you! We've received your responses. We'll contact you within 2 days if we need clarifications." |

---

## ✅ FORM STRUCTURE & QUESTIONS

### **SECTION A: INTAKE & MACHINE IDENTIFICATION**
*Maps to Manual Sections 1, 2 (Cover & Front Matter, Machine Overview)*

**A.1 — Project Setup**

```
Question Type: Short Answer

Q: What is the machine make and model?
Hint: e.g., "Valeo Friction Materials LE Test Bench" or "Indo-MIM BG Snap Assembly Machine"
Required: Yes
```

```
Question Type: Short Answer

Q: Serial number or machine identification code (if available)?
Hint: Check the nameplate on the machine
Required: No
```

```
Question Type: Short Answer

Q: Year of manufacture / commissioning?
Hint: e.g., "2015" or "1985 (legacy)"
Required: Yes
```

```
Question Type: Multiple Choice

Q: What is the intended primary use of this machine?
Options:
  ○ Component manufacturing/assembly
  ○ Testing/validation (endurance, functional)
  ○ Packaging/labeling
  ○ Material handling/processing
  ○ Other: _______________
Required: Yes
```

```
Question Type: Paragraph

Q: Brief description of what the machine does (in 2–3 sentences)?
Hint: e.g., "Automated assembly of snap fasteners onto plastic housings for automotive use"
Required: Yes
```

---

### **SECTION B: TECHNICAL SYSTEMS**

**B.1 — Electrical System**

```
Question Type: Multiple Choice

Q: What is the primary electrical power source?
Options:
  ○ Single-phase AC (120V / 230V / 415V)
  ○ Three-phase AC (415V / 480V / 660V)
  ○ DC (battery-backed)
  ○ Multiple power sources (mixed)
  ○ No electrical power (mechanical/pneumatic only)
Required: Yes
```

```
Question Type: Short Answer

Q: Motor power rating (if applicable)?
Hint: e.g., "2 HP", "1.5 kW"
Required: No
```

```
Question Type: Multiple Choice

Q: Is there a main electrical disconnect/isolation switch?
Options:
  ○ Yes, rotary disconnect
  ○ Yes, circuit breaker
  ○ Yes, but location unclear
  ○ No (or not easily accessible)
  ○ Don't know
Required: Yes
```

---

### **SECTION C: CONTROL SYSTEMS**

```
Question Type: Multiple Choice

Q: What type of control system does this machine have?
Options:
  ○ Hardwired relay logic (no PLC)
  ○ Programmable Logic Controller (PLC)
  ○ Industrial Computer / SCADA
  ○ Programmable Safety Controller (PSC)
  ○ Hybrid (combination)
  ○ Don't know
Required: Yes
```

```
Question Type: Multiple Choice

Q: Is there a Human-Machine Interface (HMI)?
Options:
  ○ Yes, touchscreen panel
  ○ Yes, push-buttons and indicator lights only
  ○ Yes, both touchscreen and hardwired controls
  ○ No (mechanical/manual controls only)
  ○ Don't know
Required: Yes
```

---

### **SECTION D: LOTO (LOCKOUT/TAGOUT)**

```
Question Type: Paragraph

Q: List all points where energy can be isolated (electrical, pneumatic, hydraulic, mechanical)?
Hint: Critical for safety. Be as detailed as possible.
Required: Yes
```

```
Question Type: Multiple Choice

Q: Can all energy isolation points be physically locked with a padlock/hasp?
Options:
  ○ Yes, all points have standard LOTO provisions
  ○ Partially (some points can be locked)
  ○ No, most points cannot be locked
  ○ Don't know
Required: Yes
```

---

### **SECTION E: EMERGENCY STOP**

```
Question Type: Multiple Choice

Q: How many emergency stop (E-Stop) buttons are on this machine?
Options:
  ○ 1 E-Stop button
  ○ 2–3 E-Stop buttons
  ○ 4+ E-Stop buttons
  ○ No E-Stop button
  ○ Don't know
Required: Yes
```

```
Question Type: Paragraph

Q: Where are the E-Stop button(s) located?
Hint: e.g., "Button 1: Main control panel, left side"
Required: Yes (if E-Stop exists)
```

---

### **SECTION F: OPERATING PROCEDURES**

```
Question Type: Paragraph

Q: Describe the startup procedure in order of steps?
Hint: Be detailed. Include any manual actions, waiting periods.
Required: Yes
```

```
Question Type: Paragraph

Q: Describe the normal operating cycle step-by-step?
Hint: e.g., "Part load → alignment → clamp → fastening → eject"
Required: Yes
```

```
Question Type: Paragraph

Q: Describe the normal shutdown procedure?
Required: Yes
```

---

### **SECTION G: MAINTENANCE**

```
Question Type: Multiple Choice

Q: What is the main maintenance interval?
Options:
  ○ Daily
  ○ Weekly
  ○ Monthly
  ○ Quarterly / Six-monthly
  ○ Yearly / As-needed only
  ○ No formal schedule
Required: Yes
```

```
Question Type: Paragraph

Q: What pre-shift checks do operators perform each day?
Required: No
```

```
Question Type: Paragraph

Q: List all lubrication points (bearings, gears, slides) and frequency?
Required: No
```

---

### **SECTION H: SAFETY HAZARDS**

```
Question Type: Paragraph

Q: What are the main physical hazards on this machine?
Hint: rotating parts, pinch points, high temperature, etc.
Required: Yes
```

```
Question Type: Paragraph

Q: What guards and protective devices are in place?
Required: Yes
```

```
Question Type: Multiple Choice

Q: What Personal Protective Equipment (PPE) is required?
Options:
  ☑ Safety glasses
  ☑ Hearing protection
  ☑ Hard hat
  ☑ Safety shoes
  ☑ Gloves (type: _________)
  ☑ Other: ______________
Required: Yes
```

---

### **SECTION I: OPERATOR TRAINING**

```
Question Type: Multiple Choice

Q: How many regular operators use this machine?
Options:
  ○ 1 (single operator)
  ○ 2–3
  ○ 4–6
  ○ 7+ (team of operators)
Required: Yes
```

```
Question Type: Paragraph

Q: What is the most common mistake new operators make?
Required: No
```

---

### **SECTION J: SCHEMATICS**

```
Question Type: Multiple Choice

Q: Do you have original electrical schematic (wiring diagram)?
Options:
  ○ Yes, current (within 5 years)
  ○ Yes, but outdated
  ○ No schematic available
  ○ Don't know
Required: Yes
```

```
Question Type: Multiple Choice

Q: Do you have pneumatic schematic?
Options:
  ○ Yes, current
  ○ Yes, but outdated
  ○ No schematic available
Required: Yes
```

---

### **SECTION K: HMI ALARMS**

```
Question Type: Multiple Choice

Q: Does the machine have an alarm/fault code system?
Options:
  ○ Yes, displayed on HMI
  ○ Yes, hardwired alarm lights/buzzers
  ○ Yes, both
  ○ No alarm system
Required: Yes
```

```
Question Type: Paragraph

Q: List all alarm codes/messages and what they mean?
Hint: e.g., "A01: Pressure low, A02: Temperature high"
Required: No
```

---

### **SECTION L: COMPLIANCE**

```
Question Type: Paragraph

Q: Do you have a formal Risk Assessment report?
Hint: If yes, provide date, firm name, document reference.
Required: Yes
```

```
Question Type: Paragraph

Q: Are there any known safety issues or non-compliances?
Required: Yes
```

---

### **SECTION M: PROJECT REQUIREMENTS**

```
Question Type: Multiple Choice

Q: What is the primary use of this manual?
Options:
  ○ Operator training material
  ○ Maintenance guide
  ○ Regulatory compliance
  ○ All of the above
Required: Yes
```

```
Question Type: Multiple Choice

Q: Language preference?
Options:
  ○ English
  ○ Tamil
  ○ Hindi
  ○ Kannada
  ○ Multiple languages
Required: Yes
```

```
Question Type: Short Answer

Q: Contact person name (for follow-up)?
Required: Yes
```

```
Question Type: Email

Q: Contact email address?
Required: Yes
```

---

## 📝 FORM CLOSURE

**Thank You Page:**

```
Thank you for completing this questionnaire!

Your responses will help create a comprehensive Operating & Safety Manual.

Next steps:
1. We review your responses (1–2 days)
2. We may contact you for clarifications
3. Manual drafting begins within 5 days
4. You'll receive draft content for review
5. Final manual delivered as .docx + .pdf within [X weeks]

Contact: [Your Email] | [Your Phone]
```

---

## 🔄 POST-SUBMISSION WORKFLOW

**Convert to Q&A.md:**

```markdown
# Q&A Documentation — [Machine Name]

**Project Code:** P[X]  
**Client:** [Company]  
**Machine:** [Make, Model, Year]  
**Date:** [Submission Date]  

---

## SECTION A — MACHINE IDENTIFICATION

**Q: What is the machine make and model?**  
A: [Response]

**Status:** ✅ Complete / ⚠️ Partial / ❌ Missing

**Notes for Manual:** [How this data will be used]

**Cross-check with RA Report:** [Does it align?]

---
```

**Upload to project:** `/mnt/project/[CLIENT]/[MACHINE]/Q&A.md`

---

## 📊 SECTION-TO-MANUAL MAPPING

| Form Section | Manual Sections | Data Captured |
|---|---|---|
| A | 1, 2 | Machine ID, nameplate, intended use |
| B | 4, 6, 8–10 | Power, LOTO, schematics |
| C | 6, 11, 12 | Controls, HMI, interlocks |
| D | 4 | LOTO points, tag-out procedure |
| E | 5 | E-Stop location, function |
| F | 6 | Operating procedures, cycle, shutdown |
| G | 7 | Maintenance schedule, lubrication |
| H | 3, 12 | Hazards, guards, PPE |
| I | 6 | Operator knowledge, training |
| J | 8, 9, 10 | Electrical, pneumatic, hydraulic |
| K | 11 | Alarms, fault codes |
| L | 13, Open Actions | Standards, certifications, gaps |
| M | Scope | Timeline, deliverables |

---

**Last Updated:** May 2026  
**Template Version:** V1.0
