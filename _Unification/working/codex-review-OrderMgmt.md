# Codex Review — §3.04 Order Management

## Headline assessment
Mostly sound, but not lock-ready. Source coverage is strong; D-1 needs tightening because approval workflow is the highest-stakes decision.

## Standards compliance
Issue: colorful internal quote should be removed. `POs are a shitstorm...` appears twice, violating drafting standards against surfacing self-deprecating/colorful source quotes. See [06 - Order Management.md:133](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:133>), [06 - Order Management.md:277](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:277>), standard at [drafting-standards.md:65](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/drafting-standards.md:65>).

Issue: use `Matt Denning`, not just `Matt`, when referring to the verified executive. See standards [drafting-standards.md:15](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/drafting-standards.md:15>) and draft uses at [06 - Order Management.md:73](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:73>).

Minor: “lacks” and “Less explicit” are tone misses. See [06 - Order Management.md:16](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:16>), [06 - Order Management.md:259](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:259>), standard [drafting-standards.md:61](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/drafting-standards.md:61>).

No `spec'd`, `2.5×`, R/Y/G, emoji, or section-reference problems found.

## Source accuracy
Strong overall. KBM 43 requirements and gap status are represented; Pivot’s 12 Order Management sub-sections and 91% standard alignment are represented. See KBM source [Requirements_Map_OrderManagement_v1.0.md:10](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/Order Management/KBMH/3 Output/Requirements_Map_OrderManagement_v1.0.md:10>) and Pivot source [Order_Management.md:47](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/pivot-brds-md/Order_Management.md:47>).

Issue: D-1 underplays Pivot margin/low-margin approval. Pivot explicitly has margin and dollar thresholds, audit trails, and approval visibility. See [Order_Management.md:255](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/pivot-brds-md/Order_Management.md:255>) and CRM carryover [CRM (Sample).md:136](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/01 - CRM (Sample).md:136>). Current D-1 says Pivot lacks named thresholds, but should still carry Pivot’s margin/SVP approval pattern into the rule classes. See [06 - Order Management.md:75](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:75>).

Issue: D-1 should preserve KBM nuance that there is no separate SO approval beyond proposal approval. Source: [Requirements_Map_OrderManagement_v1.0.md:34](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/Order Management/KBMH/3 Output/Requirements_Map_OrderManagement_v1.0.md:34>). Draft implies quote and SO approval as common ground at [06 - Order Management.md:35](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:35>).

Issue: tax volume wording could mislead. Government is 20% of business; direct bill is ~$1M / 1% revenue. Source [Requirements_Map_OrderManagement_v1.0.md:91](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/Order Management/KBMH/3 Output/Requirements_Map_OrderManagement_v1.0.md:91>) and [Requirements_Map_OrderManagement_v1.0.md:95](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/Order Management/KBMH/3 Output/Requirements_Map_OrderManagement_v1.0.md:95>). Draft line [06 - Order Management.md:150](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:150>) compresses this.

## Tone calibration
Good Pivot/Matt balance except D-1. As written, D-1 reads too KBM-dominant for a decision that cross-area context says must integrate Pivot’s low-margin SVP approval pattern. See CT-4 [cross-area-decisions.md:71](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/cross-area-decisions.md:71>).

## Cross-area consistency
Mostly good: vendor credit, labor markup, GP, pipeline, multi-company, RFP, tax, document storage are all referenced.

Mismatch: BI says vendor credit framework is decided in Order Management, while this section says Financial Management decides it. Compare [Business Intelligence.md:200](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/02 - Business Intelligence.md:200>) and [06 - Order Management.md:197](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:197>). Financial Management D-9 is already the stronger home, so update BI/cross-area index or clarify the handoff.

Specialized order types are close but circular: Pre-Quote says Order Management owns taxonomy [Pre-Quote.md:185](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/05 - Pre-Quote.md:185>); Order Management says Pre-Quote decides specialized types [06 - Order Management.md:203](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:203>). Make OM own taxonomy/naming/reporting while inheriting Pre-Quote D-7 types.

## Template fidelity
Structure is compliant: header table, §3.04.1 through §3.04.8, three-way alignment split, divergence pattern, config carryover, open questions.

Decision math reconciles: 12 table rows and footer says 12. See [06 - Order Management.md:231](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:231>) and [06 - Order Management.md:246](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/06 - Order Management.md:246>).

## Decision quality
D-1 is the only material weakness. Add Pivot low-margin/margin approval as a merged rule class, keep KBM thresholds as working defaults, and clarify proposal-stage vs SO reapproval triggers.

## Reconciliation principle audit
Lean count: KBM-lean 5, Pivot-lean 1, hybrid 2. Defensible because KBM source is more granular, but D-1 needs a visible Pivot contribution to avoid reading as “KBM rules pasted into Pivot workflow.”

## What's missing
Add or explicitly defer:
- KBM REQ-010 no separate SO approval nuance.
- KBM REQ-014 finance-charge switch, likely cross-reference to Financial Management AR/collections.
- Complete order type list gap, not just naming convention. Source [GapAnalysis_OrderManagement_v1.1.md:185](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/Order Management/KBMH/3 Output/GapAnalysis_OrderManagement_v1.1.md:185>).
- Quote versioning and additional SO form fields as open inputs. Source [GapAnalysis_OrderManagement_v1.1.md:225](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/Order Management/KBMH/3 Output/GapAnalysis_OrderManagement_v1.1.md:225>) and [GapAnalysis_OrderManagement_v1.1.md:231](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/Order Management/KBMH/3 Output/GapAnalysis_OrderManagement_v1.1.md:231>).

## Internal commentary
No obvious internal drafting commentary. The only real issue is the surfaced “shitstorm” quote.

## Recommended edits before lock
1. Rewrite D-1 to integrate Pivot margin/SVP approval and KBM proposal-stage nuance.
2. Remove colorful PO quote; replace with “vendor PO content and organization require redesign.”
3. Normalize `Matt` to `Matt Denning` where executive identity is intended.
4. Fix government/direct-bill volume wording.
5. Add open questions for complete order type list, quote versioning, SO fields, and finance-charge cross-reference.
6. Resolve vendor-credit ownership mismatch across BI / Financial Management / Order Management.