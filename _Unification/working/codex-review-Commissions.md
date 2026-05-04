# Codex Review — §3.07 Commissions

## Headline assessment
Not ready to lock. Structure is mostly sound, but source accuracy needs a pass. The main issues are overstatements of Pivot’s Commissions BRD, incorrect timing claims, and a contradiction around “actual labor cost” vs. “quoted labor / commissionable GP.”

## Standards compliance
Mostly clean. No forbidden `spec'd`, `2.5×`, R/Y/G, emojis, or name-directory issues found.

Fix malformed reference at `_Unification/10 - Commissions.md:144`: `Financial Management (§3.08 §3.08.8 #9)` should be `Financial Management §3.08.8 #9` or just `Financial Management §3.08`.

Tone watch: `_Unification/10 - Commissions.md:16`, `:64` use comparative framing (“more complex,” “at less detail”). Reword to neutral source-coverage language.

## Source accuracy
Several material issues:

- Pivot source version mismatch: draft says Pivot Commissions BRD v1.0 at `_Unification/10 - Commissions.md:6`; converted BRD says Version 2.0 at `_Unification/working/pivot-brds-md/Commissions.md:15-17`.
- Draft says commission basis is “now actual labor cost” at `_Unification/10 - Commissions.md:18` and `:34`, but D-1 recommends quoted labor / commissionable GP at `:54-56`. Align wording.
- Pivot timing is misstated. Draft says Pivot articulates booking / invoicing / payment options at `_Unification/10 - Commissions.md:108-110`; Pivot source repeatedly states invoice-date trigger and cumulative annual calculation (`Commissions.md:185-186`, `:193`, `:209`, `:214`, `:366`, `:414`, `:686`). KBM raises booking/invoice/payment as an open question in Financial Management, not Pivot (`BRD_FinancialManagement_v2.0.md:202-205`).
- Pivot “accelerators and SPIFs” are overreached at `_Unification/10 - Commissions.md:121-129`. Source supports tiered rates, bonuses, deposit bonus, teamed-account bonus, and CS bonus tiers (`Commissions.md:281-288`, `:520-546`, `:778-926`), not vendor/product SPIFs.
- Pivot rate-structure detail is overclaimed at `_Unification/10 - Commissions.md:66`: I found role/tier support, but not MillerKnoll vs. non-MillerKnoll product mix or standard vs. specialized order-type rate differentiation in the Commissions BRD.
- Internal cross-division referral compensation is sourced to CRM, not the Pivot Commissions BRD. See `_Unification/working/pivot-brds-md/CRM.md:403`; draft cites only Pivot Commissions at `_Unification/10 - Commissions.md:90`.

## Tone calibration
Generally leadership-safe. The “Net read” is balanced enough, but the body leans toward “Pivot has the real framework; KBM is less detailed.” Recast KBM as “embedded in Order Management / Financial Management” rather than “less articulated.”

## Cross-area consistency
Main conflict: Financial Management locks markup elimination and dual GP, but wording is inconsistent across sources and this draft. Financial says markup eliminated at `_Unification/04 - Financial Management.md:121-123`; dual GP quote-vs-actual is locked at `:133-137`. Commissions should say: markup eliminated; commissions use commissionable GP per the dual GP framework; do not say “actual labor cost” unless referring to actual GP.

Add/update cross-area thread for commission basis / dual GP / labor markup if cross-area-decisions.md is the control file; current CT index does not clearly carry that lock.

## Template fidelity
Shape is good: header table, §3.07.1-§3.07.8, divergence pattern, decisions table, and reconciled footer are present.

Citation fidelity is not compliant. Divergences cite “Pivot Commissions BRD §3” or “Pivot Commissions BRD” without REQ IDs at `_Unification/10 - Commissions.md:48`, `:62`, `:76`, `:90`, `:104`, `:121`. Standards require REQ IDs and file/section references.

## Decision quality
D-1 is directionally supportable after wording fix.

D-2 is appropriate as leadership-owned, but source support must be narrowed.

D-3 is good, but Pivot source supports split mechanics, not necessarily “header-level” splits; cite `Commissions.md:446-466`.

D-4 is appropriate, but cite CRM REQ-3.06.01.

D-5 is not sound until timing is corrected.

D-6 should be rewritten around “tiered rates and bonus programs,” not SPIFs.

## Reconciliation principle audit
Current recommendation lean: KBM 0, Pivot 4, hybrid 1, neutral/leadership-designed 1.

That lean is defensible because Pivot has the dedicated Commissions BRD, but KBM’s specific contributions need sharper carry-forward: storage fees commissionable, line-level commissionable flag, dual GP visibility, and markup-transition communication.

## What's missing
Add or explicitly cross-reference:

- Pivot invoice-date trigger and cumulative annual calculation.
- Pivot web-vendor exclusion (`Commissions.md:281-286`, `:332-334`, `:866`).
- Pivot deposit bonus: 0.5%, 7 days, $10k threshold (`Commissions.md:520-546`).
- Pivot year-end reconciliation / true-up (`Commissions.md:592-619`).
- Pivot no commission data migration assumption (`Commissions.md:694`) before saying migration scope is open at `_Unification/10 - Commissions.md:198`.
- KBM REQ-015 storage fees in header/source citations (`Requirements_Map_OrderManagement_v1.0.md:39`).
- KBM Financial REQ-023/024/025/038 in D-1 citations (`BRD_FinancialManagement_v2.0.md:872-927`, `:1273-1298`).

## Internal commentary
No political or leadership-reaction meta-commentary found. `_Unification/10 - Commissions.md:197` is process due diligence, not internal commentary.

## Recommended edits before lock
1. Rewrite D-1/D-5/D-6 for source accuracy.
2. Replace all generic Pivot citations with REQ IDs.
3. Normalize “actual labor cost” vs. “quoted labor / commissionable GP.”
4. Add missing Pivot requirements above, especially invoice-date timing, deposit bonus, web-vendor exclusion, reconciliation, and no-data-migration assumption.
5. Tone-polish comparative KBM/Pivot language before circulation.