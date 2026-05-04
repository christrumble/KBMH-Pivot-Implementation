# 3.02 — Customer Relationship Management (CRM)

> **Sample Section.** This is a worked example of the per-area format proposed in [`00 - Approach.md`](00%20-%20Approach.md) §6. If the structure works here, it will be used for the other 9 process areas.

| Field | Value |
|---|---|
| **Decision density** | **Medium** — pipeline model, hierarchy, and relationship-tracking design choices |
| **Source coverage** | KBM CRM BRD v1.0 (50 detailed requirements) + Pivot CRM BRD v2.0 (8 higher-level requirements) + Pivot Feb 2026 BRD review session |
| **KBM BRD** | `CRM/KBMH/3 Output/BRD_CRM_v1.0.md` |
| **Pivot BRD** | `CRM/Pivot/4 BRD/03 Pivot Interiors BRD CRM Process Area_v2.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/CRM.md`) |

---

## 3.02.1 How each company approaches CRM today

**KBM Hogue** approaches CRM as the centerpiece of a relationship-led California sales motion. Their BRD captures a detailed, granular view of how a relationship-driven dealership wants its CRM to behave: a rich contact role taxonomy, mandatory data quality discipline, geographic territory ownership across SF, San Jose, and Sacramento, and a 70%+ probability threshold filter that gives leadership a clean view of high-confidence pipeline. Each of these reflects KBM's chosen direction at the time of discovery — to consolidate fragmented activity (previously spread across Zendesk, Core, and Asana) into a single trusted system as part of the Orion implementation.

**Pivot Interiors** approaches CRM as the system of record for a divisional sales organization (Enterprise, Venture, Public, Construction Solutions) operating across California with a hierarchical sales structure. Their BRD captures a higher-level set of requirements that prioritize real-time weighted forecasting, multi-company / multi-contact relationship intelligence to reflect the buying-committee reality of contract furniture deals, cross-division referral workflows, MillerKnoll mix tracking with margin erosion visibility from quote through invoice, and a 2.5× pipeline-to-goal coaching multiplier. These reflect Pivot's chosen direction at the time of discovery — to bring a divisional and operational sales structure into a unified Orion-native experience while continuing to leverage existing platforms (HubSpot, D365) for adjacent functions.

Both companies share the same end-state goal: a unified Opportunity → Quote → Sales Order → Project flow inside Orion with role-based dashboards, mobile capture, and integrated activity tracking. The shape of "what good CRM looks like" is broadly similar. The design choices — how stages are structured, how relationships are modeled, how reporting is sliced, how approvals are sequenced — differ, and those differences are where the merged-company decisions live.

## 3.02.2 Where the two companies align

The following capabilities are common ground across both BRDs and require no merged-company decision. Some are explicit on both sides; some are explicit in one BRD and the natural operating norm in the other. Either way, the merged company arrives at the same direction without needing to reconcile.

- Unified Opportunity → Quote → Sales Order → Project flow inside Orion
- Mobile quick-add for leads and opportunities
- Activity tracking (calls, emails, meetings) with email-platform integration (Outlook SuperSync on Pivot side; equivalent on KBM)
- Document attachment to opportunity records
- Role-based dashboards (rep, manager, executive)
- Drill-down from any dashboard metric to underlying records
- Multi-role contacts (one person can carry multiple roles)
- Win / loss reason code capture
- Customer Portal for self-service quote / invoice visibility *(KBM-explicit; standard Orion capability)*
- Segmented contact lists for marketing *(KBM-explicit on segmentation; Pivot's marketing motion already operates this way)*
- Migration of legacy CRM data with deduplication *(KBM-explicit on Zendesk and Core extracts; Pivot also has HubSpot and D365 data to migrate; common need)*

These are noted in the merged BRD, and configuration proceeds against standard Orion capability.

## 3.02.3 Where the two companies differ

Eleven in-area divergences. Each is presented as: how each company approached it (with attribution to context), the recommendation for the merged company, and the decision the leadership team owns.

---

### D-1. Pipeline stage model and weighted forecasting

**Source:** KBM REQ-016, REQ-017, REQ-019 (`BRD_CRM_v1.0.md` §5); Pivot REQ-3.01.01 (`CRM.md` §3.01)

**KBM's approach.** KBM defined a 7-stage pipeline (Lead/Prospect, Qualification, Needs Analysis, Proposal/RFP, Negotiation, Closed Won, Closed Lost) with a 70%+ probability threshold for forecast inclusion. The threshold reflects KBM's preference for executive forecast discipline — a clean view of "what will close" as distinct from broader pipeline. Stages and probability assignments were planned to be configured during Realize.

**Pivot's approach.** Pivot defined a 4-stage pipeline (Analysis 25%, Qualified 50%, Quote 80%, Closing 95%) with weighted real-time forecasting at all stages and per-role permission to override percentages. The Feb 2026 BRD review session noted an open question about handling low-probability bid/RFP opportunities (~5–25%) outside the standard stages. Pivot's approach reflects their executive cadence of monthly weighted-pipeline review, combined with a coaching emphasis on every stage, not just the high-confidence end.

**Recommendation for the merged company.** Operating from Pivot's 4-stage model with real-time weighted forecasting positions the merged company well — the staged probabilities map cleanly to Orion's native opportunity structure with low configuration overhead, and the weighted real-time view supports a divisional sales organization where leadership at multiple levels needs current pipeline visibility. KBM's preferred discipline of seeing only high-confidence opportunities is preserved by making a "Commit Forecast" view available alongside the standard weighted-pipeline view; that view filters to opportunities at the Quote stage (80%) and above, the closest analogue to KBM's 70%+ inclusion intent. Per-role percentage override (Pivot's approach) is supported. The open question on low-probability bid/RFP handling surfaces in the working session for confirmation.

**Decision for the leadership team.** Confirm: 4-stage pipeline (Analysis 25%, Qualified 50%, Quote 80%, Closing 95%, Win/Loss) plus a Commit Forecast view filtering to Quote+ stages. *Recommended default: yes.*

---

### D-2a. Opportunity creation discipline

**Source:** KBM REQ-002, REQ-003 (`BRD_CRM_v1.0.md` §3); Pivot CRM BRD does not specifically address mandatory opportunity entry

**KBM's approach.** KBM identified mandatory opportunity creation as a primary unification opportunity for their team — moving from optional CRM entry to required, with validation rules and required-field enforcement on every opportunity. This reflects KBM's specific desire to consolidate activity into a single trusted system for the merged-company moment, and to strengthen the data foundation that drives forecasting and reporting.

**Pivot's approach.** Pivot's BRD does not articulate a discipline change because mandatory opportunity entry is already the operating norm for Pivot's team.

**Recommendation for the merged company.** Adopt mandatory opportunity creation with required-field validation on every opportunity. Both companies' staff will operate the same way: an opportunity record exists for every active deal, with the minimum required fields completed before the record can be advanced through stages. The discipline aligns with how Pivot's team already operates and with the direction KBM specifically asked Orion to enforce as part of this implementation. The minimum required-field set is finalized during configuration with input from both leadership teams.

**Decision for the leadership team.** Confirm: mandatory opportunity creation with required-field validation. *Recommended default: yes.* (Field set to be confirmed during configuration.)

---

### D-2b. Activity and task logging

**Source:** KBM REQ-033, REQ-034, REQ-035 (`BRD_CRM_v1.0.md` §10); Pivot REQ-3.08.01 (`CRM.md` §3.08)

**KBM's approach.** KBM treats activity tracking (calls, emails, meetings) and task management as standard Orion capability, and expects activity history to be maintained for all opportunities going forward. The BRD frames activity logging as a discipline change supported by Orion's standard activity engine.

**Pivot's approach.** Pivot's BRD specified selective enforcement of activity logging — required for new hires and for reps flagged as underperforming, with experienced reps in good standing maintaining flexibility. This reflects Pivot's existing operating norm, where senior reps have demonstrated coaching effectiveness and don't require the same data-discipline scaffolding as new or developing team members.

**Recommendation for the merged company.** Adopt Pivot's role-based / performance-tier model for activity logging. The reasoning is contextual: a tiered model provides the right scaffolding for new hires and a meaningful coaching cadence for developing reps, while preserving the operating norm that experienced reps from both companies are accustomed to. KBM's intent — that activity history is maintained for opportunities — is supported through Outlook SuperSync. With SuperSync, a rep logs the first email in a thread to a record, and subsequent messages in that thread auto-log to the same record. The merged company gets significant activity coverage from light-touch logging behavior without making manual logging a universal requirement.

**Decision for the leadership team.** Confirm: tiered activity-logging model (required for New Reps and Developing Reps; flexible for established reps), supported by Outlook SuperSync for thread-based email logging. *Recommended default: yes.*

---

### D-3. Sales hierarchy and territory reporting

**Source:** KBM REQ-013 (`BRD_CRM_v1.0.md` §4); Pivot REQ-3.06.01 (`CRM.md` §3.06)

**KBM's approach.** KBM organized around three California geographic territories — SF, San Jose, and Sacramento — with one BD rep per territory. Reporting is "Me and My Team" by manager hierarchy. Geography is the primary lens.

**Pivot's approach.** Pivot organized around four divisions (Enterprise, Venture, Public, Construction Solutions) layered on a hierarchy (Executive → Regional SVP/GM → Sales Operations → Designers/Reps). Reporting slices by division, SVP, and rep. Pivot's BRD also flags internal referral attribution as a critical capability — when furniture sales refer Construction Solutions, or vice versa, the referring person is captured for both reporting and compensation purposes.

**Recommendation for the merged company.** Operate the merged company with a two-dimensional model: every rep is tagged with both a Sales Location (geography) and a Sales Division (segment). Orion's native employee hierarchy and Sales Locations support both dimensions, and dashboards can pivot on either or both. KBM's three California geographies remain valid as merged-company locations alongside Pivot's existing design centers. The merged company's specific division taxonomy is itself a leadership-team decision; Pivot's existing four divisions are the working starting point that the working session can confirm, expand, or refine. The internal referral capability is built in from the start. The specific assignment of staff to divisions is a configuration-time exercise with both leadership teams.

**Decisions for the leadership team.**

- (3a) Confirm: two-dimensional reporting model (geography + division). *Recommended default: yes.*
- (3b) Confirm or refine: division taxonomy for the merged company (starting from Pivot's four). *Recommended default: confirm Pivot's four for working-session start; refine if leadership identifies a better merged-company shape.*
- (3c) Confirm: internal referral attribution captured on opportunities. *Recommended default: yes.* (Cross-references Commissions §3.07.)

---

### D-4. Multi-company / multi-contact relationship model

**Source:** KBM REQ-010, REQ-011 (`BRD_CRM_v1.0.md` §4); Pivot REQ-3.02.01, REQ-3.02.02 (`CRM.md` §3.02)

**KBM's approach.** KBM developed a rich custom contact role taxonomy supporting multiple roles per contact (Primary Contact, Decision Maker, Finance, Procurement, Facilities, PM, Executive Sponsor, Influencer, A&D, CM, GC, Mfr Rep, Vendor Contact). The model is single-company per opportunity but supports the contact-side complexity that contract furniture deals carry.

**Pivot's approach.** Pivot's BRD adds multi-company per opportunity to the relationship model — a deal can carry the customer, a general contractor, an architect, and a broker simultaneously, each as a distinct company record with its own contacts. Pivot also specified soft reminders that prompt reps when key influencer roles are missing from an opportunity, preserving quick-entry while encouraging data completeness over time. Pivot's emphasis reflects their attention to the full buying committee in larger projects and the operational reality that contacts move between firms.

**Recommendation for the merged company.** Operate the merged company from Pivot's multi-company / multi-contact model, combined with KBM's contact role detail. The two are complementary: Pivot's multi-company structure provides the architectural shell, and KBM's role taxonomy fills it in. Soft reminders (Pivot's approach) are adopted because they support data completeness without the friction of hard requirements.

**Decision for the leadership team.** Confirm: multi-company / multi-contact relationship model with rich role taxonomy and soft reminders for missing influencer roles. *Recommended default: yes.* (Specific role list finalized during configuration.)

---

### D-5. Owned-opportunity visibility

**Source:** KBM REQ-005 (`BRD_CRM_v1.0.md` §3); Pivot CRM BRD does not specifically address visibility scope

**KBM's approach.** KBM articulated a preference that reps see only their own opportunities by default, citing focus and avoiding "doom-scrolling" the company-wide activity feed. This reflects KBM's smaller team size and tightly defined territories, where rep-by-rep ownership is unambiguous.

**Pivot's approach.** Pivot's BRD does not explicitly address rep-level visibility scope. The Feb 2026 review session raised manager-vs-location visibility rules as an open question — i.e., does an SVP see all of their division's opportunities regardless of geographic location, or are visibility rules layered?

**Recommendation for the merged company.** Adopt rep-level "owned opportunities" visibility as the default rep view (KBM's approach), with manager and SVP visibility extended through the hierarchy (consistent with Pivot's reporting needs). This combines KBM's focus orientation for individual contributors with Pivot's hierarchical reporting needs at higher levels. The exact visibility rules at the SVP-and-above level are confirmed during configuration with both leadership teams, since the merged company's organizational shape will inform them.

**Decision for the leadership team.** Confirm: rep-level "owned opportunities" default view, plus hierarchical visibility above the rep level. *Recommended default: yes.* (Specific SVP and executive visibility rules confirmed during configuration.)

---

### D-6. Gross profit and margin discipline

**Source:** KBM REQ-021, REQ-022, REQ-023, REQ-032 (`BRD_CRM_v1.0.md` §6, §9); Pivot REQ-3.05.01 (`CRM.md` §3.05); Pivot Feb 2026 review session (low-margin SVP approval pattern)

**KBM's approach.** KBM established a 22% GP target default at the customer level, with opportunity-level override capability, and an erosion approval workflow when cumulative erosion exceeds $1,500 (routed to executive review). KBM's framework reflects their executive's stated philosophy that approval-on-erosion is a coaching/training opportunity rather than punitive — the threshold flags deals where review adds value, not where it punishes.

**Pivot's approach.** Pivot's framework spans target GP %, MillerKnoll mix tracking on opportunities, margin erosion tracked from quote through invoice via D365 integration, and an approval workflow for low-margin deals (with the Feb 2026 review session adding a specific SVP-level approval pattern at thresholds Pivot was finalizing). Margin erosion sharpens through the budget-vs-actuals view on the project record as additional transactions are actualized. Pivot's framework reflects their MillerKnoll-Certified position and the breadth of their operational scope, which exposes margin to more variables across the deal lifecycle.

**Recommendation for the merged company.** Operate the merged company from Pivot's framework as the structural baseline — opportunity-level Target GP %, MillerKnoll mix tracking, and erosion tracked across quote → invoice → project actuals. This direction reflects the merged company's MillerKnoll-Certified position and the scale of operations Pivot brings, both of which make the layered visibility valuable. KBM's coaching philosophy and the $1,500 erosion threshold are carried into the framework as the working defaults for the approval workflow; the actual approval routing (who reviews what) is finalized as part of the Order Management approval design (cross-reference §3.04). The merged-company default GP target itself is a leadership-team decision rather than an inherited number.

**Decisions for the leadership team.**

- (6a) Confirm: Pivot's GP framework structure (Target GP %, MillerKnoll mix, erosion across quote → invoice → project actuals). *Recommended default: yes.*
- (6b) Set: merged-company default GP target. *Recommended default: confirmed during the working session with leadership input; KBM's 22% is the carry-over starting point.*
- (6c) Confirm: erosion-threshold approval ($1,500 working default, with the actual routing decided in §3.04). *Recommended default: yes.*

---

### D-7. Cross-division opportunity referrals

**Source:** Pivot REQ-3.03.01 (`CRM.md` §3.03); KBM CRM BRD does not address this (KBM did not have multiple sales divisions)

**KBM's approach.** KBM's single-company sales organization did not have a cross-division referral concept. The KBM BRD does not address this capability.

**Pivot's approach.** Pivot's BRD specified a workflow that triggers immediate notifications (email and dashboard) when an opportunity is flagged for cross-division involvement — originally framed around Construction Solutions, but explicitly broadened in the Feb 2026 review session to "divisions (not only Construction Solutions)." The receiving division gets a real-time work queue rather than relying on manual report monitoring. Pivot's approach reflects their multi-division structure and the operational value of routing cross-sell opportunities at the moment they're identified.

**Recommendation for the merged company.** Adopt Pivot's cross-division referral workflow as a merged-company capability. The recommendation depends on the merged company adopting a divisional reporting dimension (per §3.02.3 D-3); once divisions exist as a primary organizing axis, cross-division referrals become a relevant operational pattern, and the workflow is straightforward to configure. KBM's sales staff are trained on the referral mechanic during onboarding. The specific divisions and referral routing are finalized after §3.02.3 D-3b lands.

**Decision for the leadership team.** Confirm: cross-division referral workflow with real-time alerting. *Recommended default: yes.* (Routing finalized after division taxonomy confirmation.)

---

### D-8. RFP management

**Source:** KBM REQ-036, REQ-037, plus implicit volume tracking (`BRD_CRM_v1.0.md` §11); Pivot REQ-3.04.01 (`CRM.md` §3.04); Pivot Feb 2026 review session (open questions on task/resource assignment, project/folder creation timing)

**KBM's approach.** KBM emphasized creating opportunities early at RFP identification (rather than waiting for formal request) so marketing has visibility for resource planning, and tracking projected volume on quote / actual volume on sales order/project to improve estimation accuracy over time. KBM's focus reflects a relationship-led pipeline where early visibility into incoming RFPs supports proactive marketing and resource readiness.

**Pivot's approach.** Pivot specified an RFP-specific opportunity type with a Kanban-style Work Board (replacing Monday.com), custom fields for due dates, budget spend, and status, and unified RFP + standard pipeline reporting. Pivot's emphasis reflects their workflow visibility needs across an RFP team that operates with Kanban discipline, and the value of consolidating RFP tracking inside the same system as the rest of the pipeline.

**Recommendation for the merged company.** Combine both approaches: an RFP opportunity type with a Kanban Work Board (Pivot), early creation at RFP identification (KBM), and projected-vs-actual volume tracking (KBM). The combination doesn't require sacrifice from either side — Pivot's workflow visibility and KBM's marketing-readiness lens are complementary. The Feb 2026 review session raised additional RFP mechanics (task/resource assignment timing, project/folder creation timing) that are flagged as open questions for the working session and may resolve into Pre-Quote or Operations rather than CRM.

**Decision for the leadership team.** Confirm: combined RFP model with Kanban Work Board, early creation, and volume tracking. *Recommended default: yes.* (Cross-reference: task/resource and folder-creation timing decisions in Pre-Quote §3.03.)

---

### D-9. Pipeline multiplier and coaching dashboards

**Source:** Pivot REQ-3.07.01 (`CRM.md` §3.07); KBM REQ-020, REQ-041, REQ-042 (`BRD_CRM_v1.0.md` §7) on dashboards (related but distinct)

**KBM's approach.** KBM's BRD captured a Sales Goals dashboard requirement to replace Excel-based goal tracking, plus rep, manager, and executive dashboards with drill-down capability and "Me and My Team" filtering. KBM's emphasis is on real-time goal visibility and manager-team rollups.

**Pivot's approach.** Pivot's BRD specified a 2.5× pipeline-to-goal multiplier with coaching status indicators on rep dashboards, aggregated multiplier status on leadership dashboards, and goal management records storing annual targets per rep. Pivot's framework reflects an intentional coaching cadence — the multiplier surfaces reps whose pipeline isn't keeping pace with their goals before the quarter ends, providing leadership a structured intervention point.

**Recommendation for the merged company.** Adopt the 2.5× pipeline multiplier and coaching indicators (Pivot's approach) as a merged-company coaching method. KBM's underlying intent — real-time goal visibility replacing Excel — is satisfied by the multiplier dashboard, since the dashboard naturally shows goal-vs-pipeline data in real time. The two requirements are closely related but distinct, and presenting the multiplier as the merged-company answer is a deliberate choice to adopt Pivot's coaching framework rather than build a separate goals-only dashboard. Coaching threshold tiers are confirmed during configuration with leadership input.

**Decisions for the leadership team.**

- (9a) Confirm: 2.5× pipeline multiplier as the merged-company coaching metric. *Recommended default: yes.*
- (9b) Confirm: coaching threshold tier definitions. *Recommended default: confirm during configuration; Pivot's existing thresholds as the starting point.*

---

### D-10. Forecast accuracy tracking

**Source:** KBM REQ-018 (`BRD_CRM_v1.0.md` §5); Pivot CRM BRD does not specifically address per-rep forecast accuracy

**KBM's approach.** KBM specified forecast accuracy tracking by user over time — comparing forecasted vs. actual revenue per rep to identify accurate forecasters, learn from best practices, and coach developing forecasters. KBM's approach reflects their focus on data quality and continuous improvement of forecasting reliability.

**Pivot's approach.** Pivot's BRD does not articulate this as a specific requirement. Pivot's focus on the 2.5× multiplier and weighted-pipeline real-time forecasting addresses pipeline health, but not forecast-accuracy-by-rep as a coaching mechanism.

**Recommendation for the merged company.** Adopt forecast accuracy tracking by user as a merged-company capability. The recommendation reflects the merged company's larger sales organization (KBM's three reps plus Pivot's divisional teams), where rep-by-rep accuracy patterns become more meaningful for coaching, and where leadership benefits from structured feedback on forecasting reliability across the broader team.

**Decision for the leadership team.** Confirm: forecast accuracy tracking by user, surfaced on manager dashboards. *Recommended default: yes.*

---

### D-11. Duplicate detection and data hygiene

**Source:** KBM REQ-014 (`BRD_CRM_v1.0.md` §4); Pivot Feb 2026 review session (HubSpot has no duplicate detection; this surfaces as an issue Pivot wants to solve in Orion)

**KBM's approach.** KBM specified duplicate detection and merge capabilities as a Core-replacement need — Core lacked these, leading to data integrity issues. KBM noted Orion's AI-enhanced duplicate identification as a meaningful upgrade.

**Pivot's approach.** Not articulated in the BRD, but the Feb 2026 review session surfaced the same need — HubSpot has no duplicate detection, and Pivot wants to solve this through Orion as part of the migration.

**Recommendation for the merged company.** Adopt Orion's standard duplicate detection and merge capabilities as a merged-company default. Both companies independently identified this as a need; configuration is straightforward.

**Decision for the leadership team.** Confirm: duplicate detection and merge capabilities enabled. *Recommended default: yes.*

---

## 3.02.4 Cross-area dependencies

The following surfaced in CRM discovery but are decided in other process areas. They are flagged here so the working session understands the connections; the decisions themselves live in their proper home area.

| Dependency | Where it surfaced in CRM | Where it's decided |
|---|---|---|
| **HubSpot retention and integration** | Pivot CRM BRD §4 (SuiteApps); Pivot Feb 2026 review session (HubSpot retained for marketing only, likely one-directional from Orion → HubSpot) | **Marketing (§3.01)** — HubSpot is fundamentally a marketing platform decision, including whether the merged company keeps it, sunsets it, or migrates marketing into Orion native |
| **Approval workflow specifics** ($25K orders, document approvals, erosion approvals, low-margin SVP approvals) | KBM REQ-021/022/023 (`BRD_CRM_v1.0.md` §6); Pivot Feb 2026 review session (low-margin SVP approval pattern) | **Order Management (§3.04)** — approval workflow design is an Order Management decision; the merged-company role assignments (who reviews what) are finalized there |
| **Vendor credit limits and PO blocks** | KBM REQ-029, REQ-030 (`BRD_CRM_v1.0.md` §9) | **Order Management (§3.04)** or **Financial Management (§3.08)** — vendor credit is a procurement / finance control, not a CRM capability |
| **Internal referral compensation** | Pivot REQ-3.06.01 (`CRM.md` §3.06) | **Commissions (§3.07)** — the referring-person attribution capability is built in CRM (per D-3c above), but the compensation logic is a Commissions decision |
| **CRM data migration approach** (Zendesk, Core, HubSpot extracts and consolidation) | KBM REQ-038, REQ-039, REQ-040 (`BRD_CRM_v1.0.md` §13) | **System Setup & Configuration (§3.10)** — overall data migration plan is a System Setup decision; the CRM-specific extraction and classification approach is detailed there |

## 3.02.5 Recommendation summary

The merged-company CRM playbook in shorthand:

- **Pipeline:** Pivot's 4-stage weighted model plus a Commit Forecast view at the Closing+ stage filter
- **Opportunity discipline:** Mandatory creation with required-field validation
- **Activity discipline:** Tiered model (required for New / Developing reps; flexible for established reps); universal email auto-capture via SuperSync
- **Hierarchy:** Two-dimensional — division (Pivot) + geography (KBM); internal referral attribution captured
- **Relationship model:** Pivot's multi-company / multi-contact + soft influencer reminders + KBM's role taxonomy
- **Visibility:** Rep-level "owned opportunities" default; hierarchical visibility above
- **GP discipline:** Pivot's framework as structural baseline (target + MillerKnoll mix + erosion across stages)
- **Cross-division referrals:** Pivot's workflow with real-time alerts
- **RFP:** Combined model — Kanban Work Board + early creation + volume tracking
- **Coaching:** Pivot's 2.5× pipeline multiplier with tiered coaching indicators
- **Forecast accuracy:** Tracked per-user, surfaced on manager dashboards
- **Data hygiene:** Standard Orion duplicate detection and merge

Net read: the merged CRM combines design choices that fit the merged company's situation. Pivot's contributions reflect their divisional sales structure, MillerKnoll-Certified position, and broader operational scope (pipeline model, hierarchy, GP framework, multi-company relationship model, coaching multiplier). KBM's contributions reflect their focus on data discipline and rep-level orientation (mandatory opportunity creation, role taxonomy depth, owned-opportunity visibility, RFP volume tracking, forecast accuracy tracking). The merged company benefits from both.

## 3.02.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1 | Adopt 4-stage pipeline (25/50/80/95) + Commit Forecast view at Closing+ | Yes | D-1 |
| 2a | Mandatory opportunity creation with required-field validation | Yes | D-2a |
| 2b | Tiered activity-logging model with universal email auto-capture | Yes | D-2b |
| 3a | Two-dimensional reporting (geography + division) | Yes | D-3 |
| 3b | Confirm or refine merged-company division taxonomy (start from Pivot's 4) | Confirm at session | D-3 |
| 3c | Internal referral attribution captured on opportunities | Yes | D-3 |
| 4 | Multi-company / multi-contact + soft influencer reminders + role taxonomy | Yes | D-4 |
| 5 | Rep-level "owned opportunities" default + hierarchical visibility above | Yes | D-5 |
| 6a | Pivot's GP framework as structural baseline | Yes | D-6 |
| 6b | Set merged-company default GP target | Confirm at session | D-6 |
| 6c | Erosion-threshold approval ($1,500 starting default) | Yes | D-6 |
| 7 | Cross-division referral workflow with real-time alerts | Yes | D-7 |
| 8 | Combined RFP model (Kanban + early creation + volume tracking) | Yes | D-8 |
| 9a | 2.5× pipeline multiplier as coaching metric | Yes | D-9 |
| 9b | Confirm coaching threshold tier definitions | Confirm at session | D-9 |
| 10 | Forecast accuracy tracking by user | Yes | D-10 |
| 11 | Duplicate detection and merge enabled | Yes | D-11 |

17 decisions: 14 with default-yes recommendations and 3 (3b, 6b, 9b) requiring leadership-team input during the working session.

## 3.02.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| Orion CRM record types | In progress (early Realize) | In progress | Continue in surviving account; align configuration to merged decisions |
| Pipeline stage configuration | 7-stage in progress | 4-stage in progress | Reconfigure to merged 4-stage per D-1 |
| Sales Locations / hierarchy | KBM's 3 locations | Pivot's divisions | Build two-dimensional model per D-3 |
| Multi-company / multi-contact | Single-company contact model in progress | Specified, not yet built | Build per D-4 |
| Required-field validation rules | Specified | Not yet built | Build per D-2a |
| Goal management + 2.5× multiplier | Sales Goals dashboard specified | Specified, not yet built | Build per D-9 |
| Forecast accuracy reports | Specified | Not in scope | Build per D-10 |
| HubSpot integration | N/A (no HubSpot at KBM) | Specified, not yet built | Decided in Marketing §3.01 |
| Vendor credit / PO blocks | Custom field specified | Not in scope | Decided in Order Management §3.04 |

Configuration is early enough on both sides that the merged direction is achievable without significant rework. None of the recommendations above require undoing locked configuration.

## 3.02.8 Open questions / inputs needed

1. **Merged-company default GP target** (decision 6b) — needs leadership-team input during the working session
2. **Division taxonomy** (decision 3b) — confirm Pivot's 4 divisions or refine for the merged company; depends on operational decisions about Construction Solutions and any other potential divisions
3. **Coaching threshold tier definitions** (decision 9b) — confirm Pivot's existing thresholds or set new ones
4. **Low-probability bid/RFP handling** (D-1) — open question from the Feb 2026 Pivot review session; how opportunities below the standard 25% Analysis stage are tracked
5. **Operational referral routing for cross-division alerts** (D-7) — depends on division taxonomy confirmation in 3b
6. **Pre-Quote and Operations cross-references for RFP mechanics** (D-8) — task/resource assignment, project / folder creation timing surface from CRM but resolve in Pre-Quote and Operations sections; flagged here for cross-section coherence

---

*This is the sample. If the format and tone work, the same template applies to the other 9 process areas. Reviewer feedback on length, depth, neutrality, and decision-density is the goal of circulating this.*
