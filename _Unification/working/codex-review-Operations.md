# Codex Review — §3.05 Operations

## Headline assessment
Not lock-ready. The recommended direction is plausible, but the draft overstates several Pivot source claims and under-cites Pivot requirements.

## Standards compliance
- `_Unification/08 - Operations.md:14` introduces Wendy, Kipp, Lorraine, and Kimmy by first name only; either verify full names or remove individual names.
- `_Unification/08 - Operations.md:46,103,107,237` says “geological check-in.” Use “geolocation check-in” or “location-based check-in.”
- `_Unification/08 - Operations.md:213` footer does not match required decisions math format: `N decisions: X ... and Y ...`.

## Source accuracy
- Pivot is overstated as “fully in-house” and “all internal” at `_Unification/08 - Operations.md:16`; Pivot source includes subcontractors and supplemental labor (`_Unification/working/pivot-brds-md/Operations.md:836-842`, `888-890`).
- “Vehicle/truck management” and KPIs for on-time delivery/damage rates at `_Unification/08 - Operations.md:16` are not supported. Source supports daily route planning for trucks, not vehicle management or those KPIs (`Operations.md:388-392`, `485-511`).
- PlanGrid retirement is too absolute at `_Unification/08 - Operations.md:121,123,191,208`; Pivot says PlanGrid runs in parallel and can be eliminated after contract expiration, with license date 1/10/2027 (`Operations.md:1040`, `1190-1194`, `1248-1256`).
- VRA is misstated as already within the same Pivot framework at `_Unification/08 - Operations.md:133-135`; Pivot source says formal VRA is a decision point and Phase 1 assumption is informal process (`Operations.md:706-714`, `741-749`, `1164-1167`, `1230-1236`).
- Pivot receiving requirements are underrepresented: lot-numbered inventory, multi-bin receiving, virtual locations, manual 7-day receiving trigger, SnapTracker/CAM/RF Smart are missing from D-2 (`Operations.md:237-251`, `280-298`).
- Pivot work order specifics are compressed into “hard assignment”; source emphasizes PO groupings, phased installations, readiness reminders, custom groupings, and scheduled notifications (`Operations.md:525-543`, `561-590`, `616-692`).

## Tone calibration
- `_Unification/08 - Operations.md:18,65,198` reads more comparative than the CRM sample: “inherits Pivot,” “standing up equivalent...multi-quarter business build,” “operational backbone.” Reframe around lower-change merged-company starting point, not KBM deficiency.
- “Muscle” at `_Unification/08 - Operations.md:18,65,198` is informal; use “capability.”

## Cross-area consistency
- Acknowledgements conflict: Operations says decided in Order Management (`_Unification/08 - Operations.md:179`), while Order Management says acknowledgement processing ownership lives in Operations (`_Unification/06 - Order Management.md:205`).
- CT-8 RFP mechanics are missing. CRM flags Pre-Quote/Operations ownership for task/resource and folder-creation timing, but Operations does not address it.
- Scheduling/resource management overlaps Project Management D-4; Operations D-8 should cross-reference Project Management resource allocation/capacity decisions (`_Unification/09 - Project Management.md:100-110`).

## Template fidelity
- Divergence citations fail the required REQ-ID pattern for Pivot throughout (`_Unification/08 - Operations.md:59,73,87,101,115,129,143,157`). Use Pivot REQ IDs, e.g., REQ-3.01.01 through REQ-3.07.06.
- Header says KBM has “~30+ requirements” (`_Unification/08 - Operations.md:6`); KBM requirements map says 34 (`Operations/KBMH/3 Output/Requirements_Map_Operations_v1.0.md:61`).

## Decision quality
- D-5 should split app/punch capability from PlanGrid retirement timing.
- D-6 should say adopting KBM VRA changes Pivot’s Phase 1 assumption, not that Pivot already operates in that framework.
- D-8 should not be “default yes, no leadership input”; KBM source explicitly requires a dedicated scheduling/resource session (`GapAnalysis_Operations.md:103-132`).
- Footer at `_Unification/08 - Operations.md:213` undercounts input needed; org structure, PlanGrid transition, VRA phase, scheduling depth, and payroll/provider mechanics require more than confirmation.

## Reconciliation principle audit
8 recommendations: Pivot-lean 2 (D-1, D-8), KBM-lean 2 (D-5, D-6), hybrid 4 (D-2, D-3, D-4, D-7), neutral 0. Balance is defensible, but current wording makes the whole section feel more Pivot-default than the decision count supports.

## What's missing
- Pivot receiving specifics: 900,000+ D365 locations, lot inventory, virtual locations, manual audit receiving trigger, SnapTracker/CAM/RF Smart.
- Pivot punch specifics: companion sales orders, $250 approval threshold, MillerKnoll “R” designation, punch issue/reason/resolution lists (`Operations.md:918-928`, `952-1002`).
- Pivot field reporting/filtering requirement from PlanGrid (`Operations.md:1014-1028`).
- KBM open gaps: work order final confirmation, rate matrix, contractor access lists, floor-plan formats, PlanGrid report examples (`GapAnalysis_Operations.md:142-160`, `193-225`, `262-294`, `329-358`, `393-417`).

## Internal commentary
No overt political meta-commentary. `_Unification/08 - Operations.md:240` “Pivot operations stakeholder review” is process commentary, not an input; recast as named operations-owner validation or remove.

## Recommended edits before lock
1. Rework §3.05.1 and D-1 to “Pivot-led internal operations with subcontractor support,” not “fully in-house.”
2. Replace all Pivot generic source labels with Pivot REQ IDs.
3. Rewrite D-5 and D-6 to reflect Pivot phase/transition realities.
4. Expand D-2/D-3/D-8 with Pivot’s actual receiving, work-order, route-planning, and scheduling requirements.
5. Fix cross-area acknowledgement ownership and add CT-8 RFP mechanics.