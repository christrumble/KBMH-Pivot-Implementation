# Review of KBM + Pivot Unification Drafts

## Headline assessment
These drafts are not ready to circulate to Dustin, Jen, or Matt as-is. The core concept is sound: an approach document, a pilot area, and a separate account memo is the right package. The problem is that the CRM pilot is not following the rules Doc Zero says it is following, and several CRM recommendations are built on overstated, mismatched, or invented source support. This is not a full restart, but it does require a controlled rewrite of Doc Zero and the CRM pilot before the rest of the 9 areas are drafted.

## Critical issues (blocking — must fix before circulation)
1. **The framework and the pilot do not match.** In `_Unification/00 - Approach.md` §4-§7, the decision logic is framed as ALIGN/ADAPT/ACCOMMODATE asymmetry; in `_Unification/01 - CRM (Pilot).md`, several major decisions are made with no valid asymmetry basis at all, or with invented classifications. Fix by rewriting Doc Zero to explicitly allow three evidence types: classification asymmetry, operating-model divergence, and one-sided capability adoption.

2. **D-2 is built on an apples-to-oranges comparison.** `_Unification/01 - CRM (Pilot).md` D-2 treats KBM mandatory opportunity entry/required fields as equivalent to Pivot’s selective activity logging for new and underperforming reps. They are not the same requirement set: KBM CRM REQ-002/003 (`BRD_CRM_v1.0.md` lines 199-207) vs Pivot CRM REQ-3.08.01 (`_Unification/working/pivot-brds-md/CRM.md` lines 487-519). Split this into two decisions: mandatory opportunity creation/data quality, and selective activity/task enforcement.

3. **D-4 materially misstates KBM’s source.** The pilot says KBM has a “single-company contact model” and classifies the comparison as `ALIGN/ALIGN`. KBM’s CRM BRD supports custom contact roles and multiple roles per contact, not multi-company opportunity relationships, and REQ-010 is `ACCOMMODATE`, not `ALIGN` (`BRD_CRM_v1.0.md` lines 275-345). Reframe D-4 as a net-new Pivot capability the merged company may choose to adopt, not as a clean shared alignment.

4. **D-6 materially misstates Pivot’s source.** The pilot turns Pivot’s requirement into “keep Construction Solutions as a continuing division.” The actual BRD says “Divisions (not only Construction Solutions) cross-sell opportunity alert workflow” (`_Unification/working/pivot-brds-md/CRM.md` lines 273-303), and the review session explicitly broadened it beyond Construction Solutions (`2026-02-19_Pivot-Interiors-Joint-BRD.md` lines 159-180). Rewrite D-6 as a cross-division referral/alert design decision, not an org-structure ratification.

5. **D-10 is not stable enough to default.** The pilot defaults to retaining HubSpot with bidirectional sync. Pivot’s CRM BRD does say bidirectional sync in SuiteApps (`CRM.md` lines 531-532), but the Pivot review session later says HubSpot is being kept for marketing only and likely one-directional from Orion to HubSpot (`2026-02-19...` lines 94-98), and Pivot System Setup says HubSpot integration will be explored after go-live (`System_Setup_and_Configuration.md` lines 175-175). This needs to move out of “default yes” territory.

6. **D-11 invents a Pivot classification that is not in the source.** The pilot labels vendor credit / portal as `KBM ACCOMMODATE / Pivot ALIGN`. Pivot’s CRM BRD has no corresponding vendor-credit requirement. Fix by separating vendor credit from customer portal, dropping the fake Pivot classification, and deciding whether vendor credit belongs in CRM at all.

7. **The full 10-area comparison is overpromised.** `_Unification/00 - Approach.md` §5 assumes clean side-by-side BRD comparison across 10 areas, but the repo only has final KBM BRDs for 7 areas. Pre-Quote and Order Management have questionnaires/gap analyses, and commissions/project management do not exist as standalone KBM BRDs. Add an explicit evidence-tier note per area or the document will look more certain than the sources justify.

8. **Doc A is written as settled fact without supporting commercial evidence in the file set.** `_Unification/Doc A - Account & Renewal Memo.md` states a final decision, but within the provided sources there is support only for “don’t consolidate accounts” and the rough Pivot license count (`2026-04-08_KBM-Pivot-Plan.md` lines 99-107), not for the 5-year prepay economics, notice terms, assignment rules, or renewal math. It also contradicts itself: line 33 says “No counter-offer, no extension,” while line 52 contemplates a paid extension contingency.

## Significant issues (should fix — would weaken the document if not addressed)
1. **D-1 overstates certainty and drops KBM forecast-accuracy tracking.** The source supports Pivot’s 4-stage model and role-based percentage overrides, but the transcript also raises unresolved low-probability bid/RFP handling (`2026-02-19...` lines 46-70). KBM REQ-018 on forecast accuracy by user (`BRD_CRM_v1.0.md` lines 373-420) is omitted. Split stage model, forecast views, and coaching/accuracy into separate calls.

2. **D-3’s default goes beyond the evidence.** A two-dimensional geography + division model is plausible, but defaulting KBM staff into Pivot’s current four divisions is not stated in either BRD. Add a separate decision for merged-company division taxonomy and include the omitted internal-referral field from Pivot REQ-3.06.01 (`CRM.md` line 403).

3. **D-5 is directionally right but technically sloppy.** KBM’s erosion approval is `ALIGN`, not `ACCOMMODATE` (`BRD_CRM_v1.0.md` lines 447-503), and vendor credit does not belong inside the GP divergence. The Pivot review session also added a concrete low-margin SVP approval concept (`2026-02-19...` lines 354-360) that the pilot ignores.

4. **D-7 is incomplete.** It captures Kanban + early creation + volume tracking, but drops the transcript-only RFP questions around task/resource assignment at opportunity stage and project/folder creation timing (`2026-02-19...` lines 192-248). Those either need to become explicit open questions or move to the proper later area.

5. **D-8 conflates “sales goals dashboard” with “2.5x pipeline multiplier.”** KBM asked for a dashboard replacement for Excel (`BRD_CRM_v1.0.md` lines 519-640); Pivot asked for a specific coaching metric (`CRM.md` lines 445-475). If you keep the recommendation, frame it as adopting a Pivot-only coaching method, not as satisfying the same requirement.

6. **D-9 understates the Pivot evidence and muddies process ownership.** The pilot says Pivot thresholds/approvers are unspecified; the transcript gives a real low-margin SVP-approval pattern (`2026-02-19...` lines 354-360). Also decide whether these approvals live in CRM, Order Management, or Financial so they are not re-litigated later.

7. **Tone slips from synthesis into advocacy.** “Would do real damage to morale” (D-2), “KBM doesn’t care strongly” (D-10), and “where their thinking was sharper” (summary) sound like consultant preference, not neutral recommendation.

8. **The working-session sequencing is wrong in Doc Zero.** `_Unification/00 - Approach.md` line 157 says “Once Doc B is approved,” but the session is what tests Doc B. That should be fixed before anyone reads it closely.

## Minor issues (nice to fix — polish)
1. `_Unification/01 - CRM (Pilot).md` §4.02.2 overstates the convergence logic; several bullets are not clearly proven as “ALIGN on one side / ADAPT on the other.”
2. `_Unification/01 - CRM (Pilot).md` line 10 says the two CRM BRDs cover “the same capability surface.” That is too absolute given the omitted KBM-only and transcript-only items.
3. `_Unification/Doc A - Account & Renewal Memo.md` line 6 overclaims by saying the memo “confirms” NetSuite leadership’s recommendation without attaching written commercial confirmation.

## Hidden gaps
- **Opportunity visibility/security is missing.** KBM explicitly wants owned-opportunity visibility (`BRD_CRM_v1.0.md` lines 214-217); Pivot’s hierarchy/territory discussion shows unresolved manager-vs-location visibility rules (`CRM.md` lines 407-415; `2026-02-19...` lines 380-418).
- **Forecast accuracy tracking is missing.** KBM REQ-018 (`BRD_CRM_v1.0.md` lines 373-420) never makes it into the pilot, even though it changes dashboard/coaching design.
- **Influencer reminders are underweighted.** Pivot REQ-3.02.02 (`CRM.md` lines 223-235, 255-261) is more than “multi-contact”; it is the control layer that makes the richer model usable.
- **Internal referral attribution is missing.** Pivot REQ-3.06.01 includes referral tracking for reporting and compensation (`CRM.md` line 403). That matters to both CRM reporting and commissions.
- **RFP mechanics are only half captured.** The transcript raises task/resource assignment, project creation timing, and folder-creation timing at opportunity stage (`2026-02-19...` lines 192-248). The pilot does not surface them.
- **Duplicate detection/merge is omitted.** KBM REQ-014 (`BRD_CRM_v1.0.md` lines 294-298) and the Pivot review discussion (`2026-02-19...` lines 452-467) support this as a real shared capability.
- **CRM migration/classification effort is omitted.** KBM REQ-038/039/040 (`BRD_CRM_v1.0.md` lines 994-1045) will matter more, not less, if the merged model becomes Pivot-richer.

## Reconciliation principle audit
The pilot’s own center of gravity is Pivot-heavy: `8/13` decisions are Pivot-leaning if you count D-1, D-2, D-3, D-4, D-5a, D-6, D-8, and D-10 that way; `3/13` are KBM-leaning (`5c`, `9a`, `11`); `1/13` is true hybrid (`7`); `2/13` stay open (`5b`, `9b`). The imbalance is only partly defensible.

Pivot-leaning decisions that fit the principle: D-4, D-5a, and probably D-7, because they add capability tied to relationship intelligence or margin protection. Pivot-leaning decisions where the principle is weakly applied: D-2, D-3 default mapping, D-6 as drafted, D-8, and D-10; those read more like “Pivot is more mature” than “this protects margin/compliance/scale.” KBM-leaning decisions on approvals and vendor credit fit the principle better than several of the Pivot defaults.

## Format scalability assessment
**Marketing:** The template can work with adaptation, but Marketing is the real home for the HubSpot decision. If CRM locks HubSpot first, the Marketing section becomes a cleanup exercise instead of a decision section.

**Pre-Quote:** The template needs rethinking. Pivot’s Pre-Quote BRD is Workfront/request-engine heavy with 20+ request types collapsed into 24 Orion types, while KBM does not have a final matching BRD in this repo. This area needs a “one-sided capability plus partial KBM evidence” format.

**Order Management:** The template can work only if it groups decisions by sub-process. Pivot’s Order Management BRD is large and modular; a flat D-1/D-2 style list will become unreadable.

**Operations:** The template needs rethinking. This is not a classification-asymmetry problem; it is a business-model problem: KBM outsourced ops vs Pivot in-house ops. It needs a “surviving operating model / onboarding impact / capability adoption” structure.

**Project Management:** The template needs rethinking. Pivot’s Project Management/Workfront area is effectively a platform-replacement decision tree, not a side-by-side requirement comparison.

**Commissions:** The template needs rethinking. Pivot has a full commissions BRD; KBM commission logic sits inside Financial Management. If treated as a normal side-by-side section, GP/commission decisions will duplicate or conflict with Financial Management.

**Financial Management:** The template can work with adaptation, but it needs a decision-gate format, not a long divergence list. Both sides are mature enough that the real challenge is sequencing high-stakes decisions, not describing current state.

**Business Intelligence:** The template can work with adaptation. BI is mostly downstream of earlier decisions, so the section should emphasize governance, official reports, role centers, and dependencies rather than pretending every reporting choice is standalone.

**System Setup:** The template can work only if it acknowledges foundational cross-area decisions. Account structure, integrations, migration posture, roles, and segmentation are not cleanly local to one section.

## Doc A pressure test
The memo’s core instinct is probably right if the KBM prepay is real, non-refundable, and usable by the merged company. But the memo does not prove that in the current source set, and it skips the questions a CFO will ask first.

The missing pressure-test items are: remaining prepaid dollar value; non-renewal notice date; assignment/change-of-control terms; module and user entitlements on each account; one-time rebuild/migration cost if KBM survives; whether a short Pivot renewal is cheaper than a rushed cutover; and written NetSuite confirmation, not verbal recollection. The action list also needs owners and dates.

## What Matt will ask that the document doesn't answer
- Which 5 decisions actually gate June resume work, and which can wait?
- Which recommendations are based on final BRDs, which on transcripts, and which are consultant inference?
- How much rework does each recommendation create in the existing KBM and Pivot configurations?
- Which recommendations add custom scope, cost, or timeline risk?
- Why should the merged company keep HubSpot, Workfront-like logic, or a 2.5x multiplier on day one instead of simplifying?
- What merged-company org model is assumed behind divisional reporting, approvals, and Construction Solutions/cross-sell?
- Where are the areas with no clean KBM counterpart BRD, and what source is being used instead?
- What commercial facts still need to be proven before the account decision is actually locked?

## Recommended next steps
1. Rewrite Doc Zero first: add evidence tiers, source-confidence rules, and a “single home per decision” rule.
2. Rebuild the CRM pilot before drafting any other area: split D-2, fix D-4/D-6/D-10/D-11, and add requirement-ID crosswalks to every divergence.
3. Move HubSpot, vendor credit, and approval decisions to their proper home areas or explicitly mark them as cross-referenced dependencies.
4. Recast Doc A as a recommendation pending contract fact-check, and attach the missing commercial assumptions in one table.
5. Only circulate after those edits. The current CRM pilot is not a safe template for the other 9 sections.