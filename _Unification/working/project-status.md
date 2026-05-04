# Project Status — KBM + Pivot Unification Documentation

**Last updated:** May 4, 2026 — All 10 process area sections drafted and Codex-reviewed; substantive Codex edits applied across all sections. Ready for Chris Trumble review pass.
**Owner:** Marcus Dallacqua (Proprio) with Chris Trumble (GSI)
**Working with:** Claude (Anthropic) for drafting; Codex (OpenAI) for adversarial review per section

---

## What this project is

Producing the **Process Unification Recommendation** that guides how the merged KBM Hogue + Pivot Interiors organization operates inside NetSuite/Orion going forward. Configuration resumes in June; this document drives the decisions that configuration will be built against. Once approved, an on-site working session with Matt Denning and Sandra Rudloff turns the recommendation into a Merged BRD per process area for sign-off.

## Session-resume protocol

When opening a new session (or after auto-compaction), read in this order before drafting:

1. **This file** — current state, blockers, focus
2. [`drafting-standards.md`](drafting-standards.md) — names, terminology, tone rules (locked, do not re-derive)
3. [`cross-area-decisions.md`](cross-area-decisions.md) — decisions in earlier sections that affect the current section
4. Most recently completed section in `_Unification/` — to refresh on tone calibration
5. The current section's source BRDs (KBM-side `*/KBMH/3 Output/BRD_*.md`; Pivot-side `_Unification/working/pivot-brds-md/*.md`)

## Status by section

| # | Section | Status | Files |
|---|---|---|---|
| Doc Zero | Approach Document | **Locked** (Chris-edited) | [`00 - Approach.md`](../00%20-%20Approach.md) |
| 3.01 | Marketing | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`03 - Marketing.md`](../03%20-%20Marketing.md) |
| 3.02 | CRM | **Locked** (Chris-edited sample) | [`01 - CRM (Sample).md`](../01%20-%20CRM%20(Sample).md) |
| 3.03 | Pre-Quote | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`05 - Pre-Quote.md`](../05%20-%20Pre-Quote.md) |
| 3.04 | Order Management | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`06 - Order Management.md`](../06%20-%20Order%20Management.md) |
| 3.05 | Operations | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`08 - Operations.md`](../08%20-%20Operations.md) |
| 3.06 | Project Management | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`09 - Project Management.md`](../09%20-%20Project%20Management.md) |
| 3.07 | Commissions | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`10 - Commissions.md`](../10%20-%20Commissions.md) |
| 3.08 | Financial Management | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`04 - Financial Management.md`](../04%20-%20Financial%20Management.md) |
| 3.09 | Business Intelligence | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`02 - Business Intelligence.md`](../02%20-%20Business%20Intelligence.md) |
| 3.10 | System Setup & Configuration | **Drafted, Codex-reviewed, edits applied — ready for Chris** | [`07 - System Setup & Configuration.md`](../07%20-%20System%20Setup%20%26%20Configuration.md) |
| Front | Executive Summary, At-a-Glance Index | Not started | — |
| Cross | Cross-Area Dependencies | Not started | — |
| Back | June Resume Plan, Decisions Register | Not started | — |

## Drafting order (decided May 4)

Easiest to hardest, to build momentum and validate the template against varying section types:

1. Business Intelligence (mostly downstream of other decisions)
2. Marketing (HubSpot retention is the heavy decision; lots of cross-references from CRM)
3. Financial Management (both BRDs mature; decision-gate driven)
4. Pre-Quote (Pivot BRD + KBM gap analysis only)
5. Order Management (Pivot BRD + KBM gap analysis; many sub-process decisions)
6. System Setup & Configuration (foundation/integration/migration governance)
7. Operations (structural rework — Pivot in-house vs KBM outsourced; net-new capability area)
8. Project Management (Workfront vs Orion-native; platform-replacement decision)
9. Commissions (Pivot-only BRD; risk of duplication with Financial Management)

Front-matter and back-matter (Executive Summary, At-a-Glance, June Resume Plan, Decisions Register) compiled after all 10 sections lock.

## Per-section workflow

```
1. Read KBM BRD + Pivot BRD for the area
2. Draft section to drafting-standards
3. Codex review using codex-section-review-prompt
4. Apply edits
5. Update project-status.md (this file) + cross-area-decisions.md
6. User checkpoint
7. Optional Chris review
8. Apply feedback
9. Lock section; move to next
```

## Locked decisions (carry into all subsequent sections)

- **Reconciliation principle** — verbatim in Doc Zero §3
- **Account decision** — KBM Hogue's account is the surviving NetSuite account (decided outside the unification document; see Doc A in working/ for context)
- **Pipeline model** — Pivot's 4-stage (25/50/80/95) per CRM D-1
- **Hierarchy model** — two-dimensional (geography + division) per CRM D-3a
- **Division taxonomy starting point** — Pivot's 4 divisions (Enterprise, Venture, Public, Construction Solutions); merged-company final taxonomy is a working-session decision per CRM D-3b
- **Multi-company / multi-contact** — Pivot's model adopted per CRM D-4
- **GP framework structural baseline** — Pivot's framework per CRM D-6a
- **Internal referral attribution** — captured on opportunities per CRM D-3c
- **HubSpot retention** — deferred to Marketing §3.01 (working defaults: keep for marketing only, sunset for CRM)
- **Approval workflow specifics** — deferred to Order Management §3.04
- **Vendor credit limits** — deferred to Order Management §3.04 or Financial Management §3.08
- **Internal referral compensation** — deferred to Commissions §3.07
- **CRM data migration approach** — deferred to System Setup §3.10
- **Report governance** — official report designation with GSI/Orion prefix per BI §3.09 D-1
- **Dashboard publishing** — role-based publishing with lock-down for team dashboards; personal Home dashboard remains user-customizable per BI §3.09 D-2
- **Reminders portlet** — primary daily work surface on each role center per BI §3.09 D-3
- **360 dashboards** — full set built (Backlog, Bookings, Cash Flow, AR, AP, Project Performance) per BI §3.09 D-4
- **Dual GP tracking** — actual vs. commissionable as merged-company KPI per BI §3.09 D-4b
- **Document management framework** — centralized storage with version control, role-based access, search per BI §3.09 D-5
- **Export security framework** — role-based permissions + 50MB notification workflow per BI §3.09 D-6
- **Advanced analytics scope** — custom calculated fields, what-if modeling, SuiteAnalytics native; predictive analytics enabled for specific KPIs designed during Realize per BI §3.09 D-7a
- **SuiteAnalytics Connect licensing** — deferred to Realize-phase decision against documented trigger criteria per BI §3.09 D-7b
- **Power BI evaluation** — deferred to post-go-live, triggered by documented reporting gap per BI §3.09 D-8
- **Sales rep and manager scorecards** — BI dashboard component combining KBM metric structure + CRM-locked 2.5x multiplier per BI §3.09 D-9

## Recent feedback (May 4)

Chris Trumble reviewed the CRM sample and Doc Zero. Edits applied directly to canonical files. Patterns extracted into `drafting-standards.md`. Critical signal: the framework holds; the edits were name fixes + terminology polish + grammar refinement.

Codex (gpt-5.5) reviewed the BI section draft. Surfaced 7 categories of edits: Pivot requirement count fix (41 → 43), §3.09.2 reframe to distinguish explicit-both-side alignment from standard-capability-carried-forward, D-5 KBM wording correction (KBM BI BRD does not specifically address document management), addition of D-9 sales rep and manager scorecards as a missing item, citation tightening, trigger criteria for D-7b (SuiteAnalytics Connect licensing) and D-8 (Power BI evaluation), tone polish, and section-reference style normalization (§ vs "Section"). All edits applied.

## Active blockers

None.

## Pending inputs

- Sandra Rudloff and Pivot leadership reaction to the CRM sample (informational — not blocking next sections)
- Matt Denning's reaction to the CRM sample (informational)
- User checkpoint on BI section before locking
- Any structural feedback that would change the per-area template

## Current focus

Awaiting user checkpoint on the Business Intelligence section. Once locked, beginning Marketing (§3.01) drafting — heavy dependency from CRM is the HubSpot retention decision.
