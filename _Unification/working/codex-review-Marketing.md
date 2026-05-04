# Codex Review — §3.01 Marketing

## Headline assessment
Needs edits before lock. The section is directionally strong and template-complete, but it has material coverage and reconciliation issues: Pivot requirement count is wrong, several KBM requirements are missing or only implied, email-capacity facts are unresolved, and document-storage language conflicts with BI/System Setup decisions. D-1 and D-3 are plausible recommendations, but D-3b and document storage need tightening before circulation.

## Standards compliance
Fail, minor.
- Pass: KBM Hogue spelling is correct; no `spec'd`, `2.5×`, R/Y/G, stoplight, or emoji issues found.
- Fail: introduces `Jenny` without verified-directory support in the section body: `_Unification/03 - Marketing.md:129`. KBM source only gives first name: `Marketing/KBMH/3 Output/BRD_Marketing_v1.0.md:126`.
- Fail: section refs drift to `CRM D-3b` instead of full `CRM §3.02 D-3b`: `_Unification/03 - Marketing.md:150`, `_Unification/03 - Marketing.md:152`.
- Fail: stakeholder-review item omits Kevin even though Pivot source names Kevin for PowerBI reporting: `_Unification/working/pivot-brds-md/Marketing.md:678`; draft list at `_Unification/03 - Marketing.md:270`.

## Source accuracy
Fail.
- Pivot count is wrong. Draft says 36 requirements: `_Unification/03 - Marketing.md:6`. Markdown source has 35 requirement rows and 34 unique IDs; it also duplicates/misnumbers `REQ-3.05.07` in Lead Management: `_Unification/working/pivot-brds-md/Marketing.md:524`, `_Unification/working/pivot-brds-md/Marketing.md:666`.
- Email capacity is unresolved, not cleanly `100,000+`. KBM says 120,000/month: `Marketing/KBMH/3 Output/BRD_Marketing_v1.0.md:205`. Pivot says both 120,000 and 100,000/month: `_Unification/working/pivot-brds-md/Marketing.md:129`, `:192`, `:434`, `:837`. Draft masks this at `_Unification/03 - Marketing.md:116`.
- D-4 omits Pivot’s current opt-in constraint: 3,400 marketable contacts from 20,000 records: `_Unification/working/pivot-brds-md/Marketing.md:179`, `:421`.
- KBM market-intelligence requirements are materially missed: `REQ-M019`-`REQ-M021` at `Marketing/KBMH/3 Output/BRD_Marketing_v1.0.md:546`-`558`, validated at `:636`-`:638`.
- KBM customer survey future requirements are missed: `REQ-M022`-`REQ-M023` at `Marketing/KBMH/3 Output/BRD_Marketing_v1.0.md:736`-`741`.
- KBM `REQ-M026` content library management is missed: `Marketing/KBMH/3 Output/BRD_Marketing_v1.0.md:1094`.

## Tone calibration
Fail, light edit.
- “Manual qualification doesn't scale” is more evaluative than the CRM/BI pattern: `_Unification/03 - Marketing.md:133`.
- “Migrating Pivot's marketing function to NetSuite native email... would introduce friction without proportional benefit” reads advocacy-heavy: `_Unification/03 - Marketing.md:66`.
- “traditional demand-generation operation” / “traditional B2B marketing operation” framing is defensible but should be softened so KBM does not read as non-traditional in a lesser sense: `_Unification/03 - Marketing.md:14`, `:83`.

## Cross-area consistency
Issues.
- HubSpot ownership: pass. Marketing owns D-1: `_Unification/03 - Marketing.md:58`-`73`; CT-3 says Marketing owns it: `_Unification/working/cross-area-decisions.md:49`-`59`.
- CT-3 must be updated after lock because draft changes the working default from one-directional sync to bi-directional sync: `_Unification/working/cross-area-decisions.md:57`; `_Unification/03 - Marketing.md:73`.
- Approval workflow: fail. D-3b locks “sales-leader approval” in Marketing: `_Unification/03 - Marketing.md:104`, `:226`; approval routing should remain Order Management-owned per CT-4: `_Unification/working/cross-area-decisions.md:63`-`73`.
- Document storage: fail. Draft says Google Drive integration retained: `_Unification/03 - Marketing.md:214`; BI/CT-14 establish File Cabinet/System Setup ownership and SharePoint phaseout direction: `_Unification/02 - Business Intelligence.md:117`-`127`; `_Unification/working/cross-area-decisions.md:203`-`211`.
- Division taxonomy is over-restated as `NBD / Venture / Public / Construction Solutions`: `_Unification/03 - Marketing.md:16`, `:133`, `:192`; CT-1 says refer to merged-company division taxonomy per CRM D-3b: `_Unification/working/cross-area-decisions.md:31`.

## Template fidelity
Mostly pass, with content failures.
- Header table: pass.
- §3.01.1: pass structurally; tone edits needed.
- §3.01.2: pass structurally, but source classification needs tightening. “Multiple contacts per opportunity” belongs as CRM-locked dependency, not common-ground Marketing alignment: `_Unification/03 - Marketing.md:28`, `:190`.
- §3.01.3: pass structurally.
- §3.01.4: structurally pass; document/approval issues above.
- §3.01.5: pass; credits both companies.
- §3.01.6: pass math: 12 rows, footer reconciles at `_Unification/03 - Marketing.md:220`-`235`.
- §3.01.7/§3.01.8: present, but missing KBM market intelligence, surveys, content library; stakeholder-review item is not a real open question: `_Unification/03 - Marketing.md:270`.

## Decision quality
- D-1: Direction supported. Clarify object-level source of truth and update CT-3.
- D-2: Acceptable, but broad operating model may be summary-level rather than a leadership decision.
- D-3: Recommendation supported by Pivot scale. D-3b should confirm event-cost approval requirement only; approver/routing stays §3.04.
- D-4: Needs opt-in/contactability constraint and email-capacity discrepancy surfaced.
- D-5: Supported; tone edit for KBM qualification path.
- D-6: Supported; avoid hard-coding division names.
- D-7: Supported; add/correct citation for Pivot multiple-stakeholder requirement at source line 524.
- D-8: Supported; keep document-storage mechanics deferred.

## Reconciliation principle audit
Count: KBM-leaning 1 (D-8), Pivot-leaning 5 (D-1, D-3, D-4, D-5, D-7), hybrid 2 (D-2, D-6), neutral 0. The Pivot lean is explainable by merged-company scale, but the missing KBM market-intelligence/content/survey requirements make the balance look more Pivot-heavy than the evidence requires. With eight divergences and 12 decisions, it reads closer to medium-density than low unless several items are reframed as carryover/open questions.

## What's missing
- KBM `REQ-M019`-`REQ-M021` market intelligence/content planning.
- KBM `REQ-M022`-`REQ-M023` customer surveys.
- KBM `REQ-M026` content library management.
- Pivot opt-in constraint: 3,400 marketable / 20,000 total.
- Pivot email-capacity discrepancy as an open question.
- Kevin/PowerBI if stakeholder list is retained.
- Cross-area update for CT-3 after Marketing locks HubSpot architecture.

## Internal commentary
- `_Unification/03 - Marketing.md:270` — “benefit from review...” is process commentary, not an open question. Remove or convert to a routing note outside the section.

## Recommended edits before lock
1. Fix Pivot requirement count and note source numbering defect.
2. Add KBM market intelligence, surveys, and content library coverage.
3. Surface Pivot opt-in constraint and email-capacity discrepancy in D-4/open questions.
4. Rewrite D-3b to defer approver/routing to §3.04.
5. Replace Google Drive “retained” language with System Setup/File Cabinet-compatible wording.
6. Remove `Jenny` or verify full name; remove stakeholder-review open question.
7. Normalize CRM cross-references to `§3.02 D-X` style and avoid hard-coded division names.