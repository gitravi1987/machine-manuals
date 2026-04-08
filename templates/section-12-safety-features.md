# Section 12 — Safety Features & Interlocks

**Machine Name:** [MACHINE_NAME]
**Standards:** ISO 13849-1:2015, IEC 62061:2021, ISO 14119:2013, ISO 14120:2015

---

## 12.1 Safety Function Summary

| ID | Safety Function | Device | PLr / SIL | Standard |
|----|----------------|--------|-----------|----------|
| SF-1 | Guard door interlock — stops machine when guard opened | [e.g., Fortress safety switch model] | PLd | ISO 13849-1 |
| SF-2 | Emergency stop function | Mushroom head E-stop + safety relay | PLd | ISO 13849-1 / ISO 13850 |
| SF-3 | Two-hand control (if applicable) | [e.g., Two-hand control unit] | PLd | ISO 13851 |
| SF-4 | Light curtain — access detection | [e.g., SICK deTec4] | PLd | ISO 13855 |

*(Confirm PLr ratings from RA documentation — do not fabricate)*

---

## 12.2 Guard Specifications

| Guard ID | Type | Material | Thickness | Fixing Method | Standard |
|----------|------|----------|-----------|---------------|----------|
| G-1 | Fixed guard — top | [e.g., Mild steel] | [e.g., 2mm] | [e.g., Bolted M6] | ISO 14120 |
| G-2 | Movable guard — front access | [e.g., Polycarbonate] | [e.g., 3mm] | [e.g., Hinged + interlocked] | ISO 14120 |

---

## 12.3 Interlock Device List

| ID | Location | Device Make/Model | Type | Actuator | Wiring |
|----|----------|------------------|------|----------|--------|
| IL-1 | Front access door | [e.g., Fortress amGard Pro] | Solenoid interlock | [Actuator type] | [Safety relay / PLC safety input] |
| IL-2 | Rear access panel | [e.g., SICK i10-SA205] | Tongue interlock | [Actuator type] | [Safety relay] |

---

## 12.4 Safety Function Testing

Test all safety functions:
- At commissioning (initial)
- After any modification to control system or guarding
- Every 6 months (preventive maintenance)

Record test results in Maintenance Log (Section 7).

| Safety Function | Test Method | Pass Criteria |
|----------------|------------|---------------|
| SF-1 Guard interlock | Open guard during cycle — machine must stop | Machine stops within [X ms] |
| SF-2 E-stop | Press E-stop during cycle — machine must stop | Machine stops; cannot restart without reset |
| SF-3 Two-hand control | Release one hand during cycle | Machine stops immediately |
| SF-4 Light curtain | Break beam during cycle | Machine stops within [X ms] |

---

## 12.5 Open Actions — This Section

| ID | Item | Status |
|----|------|--------|
| OA-12-001 | [e.g., PLr values not confirmed — verify from RA documentation] | Pending |
| OA-12-002 | [e.g., SF-3 two-hand control — recommended in RA but not installed on machine] | Pending |
