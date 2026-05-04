# Codex Review — §3.06 Project Management

## Headline assessment
Not ready to lock. The central recommendation reverses the Pivot source direction: the Pivot PM BRD says NetSuite Orion will replace Workfront, while this section defaults to retaining Workfront. That can be a new leadership decision, but it cannot be presented as source-backed without explicitly flagging it as a reopened architecture decision.

## Standards compliance
Mostly clean on banned terms. One direct standards miss: `_Unification/09 - Project Management.md:24` says “Doc Zero,” which standards prohibit; use “the approach document” instead (`_Unification/working/drafting-standards.md:24-31`).

No issue found with listed name spellings. New name “Sherri Nuzum” is source-backed in Pivot materials (`_Unification/working/pivot-brds-md/Project_Management.md:996`, `1074`).

## Source accuracy
Major issue: Workfront retention is not Pivot BRD direction. Pivot PM BRD states “NetSuite Orion will replace Workfront” (`_Unification/working/pivot-brds-md/Project_Management.md:129-131`). The draft instead says Pivot retention/replacement is open and defaults to Workfront retention (`_Unification/09 - Project Management.md:57-64`, `144-151`).

Same conflict with locked Pre-Quote: Pivot “Workfront in use; specified migration to Orion” (`_Unification/05 - Pre-Quote.md:225-236`) and “Workfront-to-Orion transition” (`_Unification/05 - Pre-Quote.md:248`). PM section says retention/sunset transition (`_Unification/09 - Project Management.md:182`), which muddies that locked direction.

KBM under-reach in D-4. Draft says KBM does not articulate capacity management (`_Unification/09 - Project Management.md:102-108`), but KBM Operations has PM task automation, resource visualizer, and task-sophistication requirements (`Operations/KBMH/3 Output/BRD_Operations_v1.0.md:1959-1972`).

Pivot capability overstatement: draft attributes task dependency tracking, capacity management, and dashboards as “built in Workfront” (`_Unification/09 - Project Management.md:55`). Pivot PM source supports current Workfront use and time/task logging, but future-state capability is Orion/resource utilization reporting (`_Unification/working/pivot-brds-md/Project_Management.md:547`, `561`, `640-644`, `677-685`).

Divergence sources lack REQ IDs throughout (`_Unification/09 - Project Management.md:51`, `74`, `88`, `102`, `116`), contrary to citation rules (`_Unification/working/drafting-standards.md:155-162`).

## Tone calibration
Some evaluative language is subtle but present: “substantial existing investment,” “operating proficiently,” and “would re-create work” (`_Unification/09 - Project Management.md:55`, `63`) read like advocacy for Pivot’s current tool rather than neutral synthesis. CRM/locked sections frame recommendations from context, not platform affection.

## Cross-area consistency
Incorrect defer: Workfront integration is said to be decided in System Setup D-6 (`_Unification/09 - Project Management.md:138`, `180`), but System Setup D-6 lists HubSpot, banking, payroll, MillerKnoll, expense, SharePoint, ZoomInfo, SuiteAnalytics Connect; not Workfront (`_Unification/07 - System Setup & Configuration.md:127-137`).

D-3 duplicates a locked Pre-Quote decision. Pre-Quote already locks IPM-and-sales-coordinator routing (`_Unification/05 - Pre-Quote.md:158-168`). PM should inherit it, not create another leadership decision (`_Unification/09 - Project Management.md:86-97`, `160`).

D-4 overlaps Operations D-8 scheduling/resource management, already decided there (`_Unification/08 - Operations.md:155-165`). PM should either cross-reference Operations or clearly narrow to PM workload planning.

## Template fidelity
Structure is present: header, §3.06.1 through §3.06.8, alignment split, divergence pattern, decisions table, carryover, open questions.

Main fidelity miss is citation format: no divergence has KBM/Pivot REQ IDs or file-path citations. The decisions footer math reconciles: 6 decisions, 5 default yes, 1 leadership selection (`_Unification/09 - Project Management.md:155-164`).

## Decision quality
D-1 is not supportable as defaulted. If Workfront retention is a strategic option, make D-1 “reopen/confirm Workfront replacement vs retention” with no default or with Orion replacement as the source-backed default.

D-3 should be removed from the decisions table or reframed as “inherit Pre-Quote D-8; assign KBM staff during org alignment.”

D-4 needs KBM REQ-032 through REQ-034 and Operations D-8 integrated before defaulting to Pivot.

## Reconciliation principle audit
Current lean count: KBM 0, Pivot 3, hybrid/neutral 2.

Pivot-leaning: D-1, D-3, D-4.  
Neutral/hybrid: D-2, D-5.  
This is not automatically wrong, but because D-1 contradicts source direction, the section reads overly Pivot-tool-preserving rather than context-reconciled.

## What's missing
Add KBM Operations REQ-032, REQ-033, REQ-034 for PM tasking/resource visualization (`Operations/KBMH/3 Output/BRD_Operations_v1.0.md:1959-1972`).

Add Pivot PM REQ citations for labor quote, work order, time tracking, reporting, and document integration where used (`_Unification/working/pivot-brds-md/Project_Management.md:175-182`, `298-304`, `535-541`, `658-665`, `781-786`).

Add a new cross-area thread if Workfront retention remains on the table; current CT index has no Workfront platform thread (`_Unification/working/cross-area-decisions.md:231-235`).

## Internal commentary
No overt political/leadership-reaction commentary found. “Pivot project management stakeholder review” (`_Unification/09 - Project Management.md:185`) is operational, but should name Sandra Rudloff/Pivot PM leadership only if ownership is intended.

## Recommended edits before lock
1. Rewrite D-1 around the source-backed default: Orion replaces Workfront, unless leadership deliberately reopens retention.
2. Remove or sharply qualify “Workfront retained” default language across lines 57-64, 144-151, 157-158, 170-174, 179-184.
3. Add REQ IDs/file citations to every D-source line.
4. Fix cross-area defer for Workfront integration; either add it to System Setup/cross-area decisions or stop citing System Setup D-6 as if it already owns it.
5. Reframe D-3 as inherited from Pre-Quote, not a new decision.
6. Revise D-4 with KBM REQ-032 through REQ-034 and Operations D-8.