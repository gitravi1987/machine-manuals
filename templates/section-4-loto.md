# Section 4 — Lockout / Tagout (LOTO) Procedures

**Machine Name:** [MACHINE_NAME]
**Standards:** ISO 12100:2010, ISO 13849-1:2015, IS 12059, Factories Act 1948

---

> DANGER: Always complete the full LOTO procedure before performing
> any maintenance, adjustment, cleaning, or fault-clearing task.
> Failure to isolate energy sources can result in death or serious injury.

---

## 4.1 Energy Isolation Points

| ID | Energy Source | Type | Isolation Device | Location | Lock Type |
|----|--------------|------|-----------------|----------|-----------|
| LP-1 | Electrical | 3-phase 415V | Rotary disconnect switch | [e.g., Right side panel, 1.5m height] | Hasp + padlock |
| LP-2 | Pneumatic | [X] bar | Ball valve + bleed-down | [e.g., Left base] | Hasp + padlock |
| LP-3 | Hydraulic | [X] bar | Isolation valve | [e.g., Hydraulic unit, rear] | Hasp + padlock |
| LP-4 | Mechanical | Stored energy | [e.g., Cam lock / gravity block] | [e.g., Top centre] | Pin + tag |

---

## 4.2 De-energisation Sequence (Lockout)

Follow this exact sequence. Do not skip steps.

1. Notify all personnel in the area that the machine is being shut down.
2. Press EMERGENCY STOP — confirm machine is at rest.
3. Press MAIN STOP on control panel — confirm all motion has ceased.
4. Isolate LP-1 (Electrical): Turn rotary disconnect to OFF. Apply hasp and padlock. Attach tag with name and date.
5. Isolate LP-2 (Pneumatic): Close ball valve. Allow pressure to bleed to zero. Verify gauge reads 0 bar.
6. Isolate LP-3 (Hydraulic): Close isolation valve. Allow pressure to bleed to zero. Verify gauge reads 0 bar.
7. Secure LP-4 (Mechanical): Insert gravity block / cam lock pin. Confirm visually.
8. Attempt to restart using START button — confirm machine does NOT start.
9. Begin maintenance task only after Step 8 is confirmed.

---

## 4.3 Re-energisation Sequence (Lockout Removal)

1. Confirm maintenance task is complete. All tools removed from machine.
2. Confirm all guards are reinstalled and secured.
3. Notify all personnel to stand clear.
4. Remove LP-4 mechanical lock (gravity block / cam lock pin).
5. Remove padlock from LP-3 (Hydraulic). Open isolation valve.
6. Remove padlock from LP-2 (Pneumatic). Open ball valve. Confirm pressure builds normally.
7. Remove padlock from LP-1 (Electrical). Turn rotary disconnect to ON.
8. Reset EMERGENCY STOP button.
9. Perform test start — confirm normal operation before resuming production.

---

## 4.4 LOTO Diagram

[IMAGE: LOTO Point Identification Diagram showing LP-1 to LP-4.
Colour coded: Red=Electrical, Blue=Pneumatic, Orange=Hydraulic, Green=Mechanical.
Resolution: 300 DPI. Suitable for 24x18 inch shop poster.
Status: Provided by customer / Pending]

---

## 4.5 Open Actions — This Section

| ID | Item | Status |
|----|------|--------|
| OA-4-001 | [e.g., LP-3 hydraulic isolation valve location not confirmed on-site] | Pending |
| OA-4-002 | [e.g., Mechanical stored energy — gravity block design not verified] | Pending |
