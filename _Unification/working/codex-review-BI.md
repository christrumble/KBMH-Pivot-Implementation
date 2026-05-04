# Codex Review — §3.09 Business Intelligence

## Headline assessment
Ready with edits, not ready to lock as-is. The section is directionally sound and politically balanced, but it has source-count error risk, some overclaimed “common ground,” and a few unsupported absence / light-coverage claims. No structural rewrite needed if those are corrected before later sections build on BI.

## Standards compliance
Fail with limited issues.

- Pass: no `spec'd`, `2.5×`, `R/Y/G`, “stoplight,” emoji headers/tables, or bad verified-name spelling found.
- Pass: Sandra Rudloff and Kipp are correctly spelled against sources. Kipp is not in the directory but is source-verified at `Business Intellegence/KBMH/3 Output/BRD_BusinessIntelligence_v1.0.md:302-307`.
- Fail: singular pronoun agreement drifts: `_Unification/02 - Business Intelligence.md:14`, `:16`, `:18` use `Their/their` for singular company references / “each company.”
- Fail: section reference style uses `Section` instead of `§`: `_Unification/02 - Business Intelligence.md:51`, `:65`, `:79`, `:93`, `:123`, `:155`, `:174`. Standards require § style at `_Unification/working/drafting-standards.md:31`, `:155-160`.
- Fail: §3.09.6 footer is not in required blockquote format: `_Unification/02 - Business Intelligence.md:216`; required at `_Unification/working/drafting-standards.md:137-141`.

## Source accuracy
Fail, but fixable.

- Pivot count appears wrong. Draft says 41 requirements at `_Unification/02 - Business Intelligence.md:6`; markdown source contains 43 requirement bullets across 7 sections: `Business_Intellegence.md:177-181`, `:288-299`, `:443-447`, `:555-560`, `:675-679`, `:791-795`, `:907-914`.
- KBM count is correct: 27 requirements.
- D-5 overstates KBM evidence. Draft says KBM addresses document attachment “within other sections” and “lightly specified” at `_Unification/02 - Business Intelligence.md:109-111`, `:228`, but the KBM BI BRD does not articulate document management or document attachment. Pivot does at `Business_Intellegence.md:791-795`.
- §3.09.2 overclaims common ground. Workbook analytics, SuiteQL, inline editing, highlighting rules, and saved-search mass update are KBM-explicit, but not Pivot-explicit in the Pivot BI requirement lists. See draft lines `_Unification/02 - Business Intelligence.md:30`, `:35-38`; Pivot’s relevant BI tool/export requirements are `Business_Intellegence.md:555-560`, `:675-679`.
- D-6 Pivot export-security claim is true but uncited. External-email restriction is at `Business_Intellegence.md:218`; draft cites only KBM at `_Unification/02 - Business Intelligence.md:123`.
- D-1 Sandra Rudloff / Crystal Reports claim is supported but uncited: `Business_Intellegence.md:589`, `:599`, `:1110`.

## Tone calibration
Pass with minor polish. The section does not read as anti-Pivot or anti-KBM. Minor phrases to soften: “The merged company gets both” at `_Unification/02 - Business Intelligence.md:18` is casual, and “Lightly specified / Comprehensively specified” at `:228` reads slightly comparative. Neither is politically loaded.

## Cross-area consistency
Mostly pass.

- Correctly reflects CT-1, CT-2, CT-3, CT-7, CT-10, and approval deferral.
- Missing CT-5 carryover: vendor credit limits / PO blocks include proactive dashboard visibility in `_Unification/working/cross-area-decisions.md:77-87`; BI should add a dependency row if dashboarding/reporting will surface it.
- `_Unification/02 - Business Intelligence.md:174` over-defers sales rep scorecards to CRM. CRM owns the 2.5x multiplier, but KBM BI REQ-020/021 define scorecard components broader than multiplier only: revenue, GP, YTD, period comparison, pipeline, closed deals at `BRD_BusinessIntelligence_v1.0.md:681-691`.
- Add cross-area threads for historical data migration supporting BI / predictive analytics and document migration to File Cabinet. Pivot assumptions surface both at `Business_Intellegence.md:1106`, `:1126`, `:1130`, `:1142`.

## Template fidelity
- Header table: Pass.
- §3.09.1: Pass.
- §3.09.2: Fail; several items are standard/KBM-explicit, not both-BRD alignment.
- §3.09.3: Structure pass; citation completeness fail.
- §3.09.4: Format pass; missing dependency rows noted above.
- §3.09.5: Pass; credits both companies.
- §3.09.6: Math pass; footer format fail.
- §3.09.7 and §3.09.8: Present and appropriate.

## Decision quality
D-1, D-2, D-3, D-4, D-5, and D-6 are directionally supported once citations/absence wording are fixed.

D-7a is too broad if “predictive analytics” is treated as standard implementation without dependency language. D-7b needs clearer licensing trigger: named external platform, required refresh/currency, native tool/export insufficiency, data scope, owner, and cost approval. D-8 also needs trigger language: evaluate after go-live/reporting stabilization against unmet reporting needs, not just “post-implementation.”

## Reconciliation principle audit
By decision: KBM-leaning 4, Pivot-leaning 3, hybrid 2, neutral/deferred 2. Balance is reasonable for BI. Low decision density mostly holds because all decisions are confirmation/default-yes, but the section feels closer to low-medium until §3.09.2 is cleaned up and the scorecard/document gaps are tightened.

## What's missing
- Correct Pivot requirement count or documented rationale for excluding two requirements.
- KBM BI REQ-020/021 sales rep and manager scorecards as BI dashboard components.
- Pivot REQ-3.04.04 saved-search templates.
- Pivot REQ-3.05.05 mass data export for audits/compliance.
- Historical reporting / predictive analytics dependency on D365 historical data migration.
- Existing document migration to NetSuite File Cabinet and SharePoint/network-drive phaseout.

## Internal commentary
No leadership-reaction or political meta-commentary found. Minor internal shorthand should be removed: `CT — see cross-area dependencies` at `_Unification/02 - Business Intelligence.md:99`.

## Recommended edits before lock
1. Resolve Pivot count: change 41 to 43 or document exclusions.
2. Rewrite §3.09.2 into “explicit both-side alignment” vs “standard capability carried forward.”
3. Fix D-5 KBM wording: “KBM BI BRD does not specifically address document management.”
4. Add/repair citations for Pivot self-service, reminders absence, external-email restriction, Sandra Rudloff, and KBM SuiteQL.
5. Add BI treatment for KBM sales scorecards and the missing cross-area dependencies.
6. Clarify D-7b and D-8 trigger criteria.
7. Clean § references, singular pronouns, footer blockquote, and remove `CT` shorthand.