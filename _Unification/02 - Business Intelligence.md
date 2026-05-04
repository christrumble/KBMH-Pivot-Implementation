# 3.09 — Business Intelligence

| Field | Value |
|---|---|
| **Decision density** | **Low** — reporting layer largely follows decisions made in earlier sections; section-specific decisions focus on governance, document management, and analytics scope |
| **Source coverage** | KBM BI BRD v1.0 (27 requirements across 8 sections) + Pivot BI BRD v2.0 (43 requirements across 7 sections) |
| **KBM BRD** | `Business Intellegence/KBMH/3 Output/BRD_BusinessIntelligence_v1.0.md` |
| **Pivot BRD** | `Business Intellegence/Pivot/4 BRD/08_Pivot Interiors BRD Business Intelligence Process Area_v2.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/Business_Intellegence.md`) |

---

## 3.09.1 How each company approaches Business Intelligence today

**KBM Hogue** approaches BI as a governance and discipline opportunity. Its BRD reflects a desire to consolidate fragmented reporting (Excel and Google Sheets distributed alongside multiple unofficial report versions across the team) into a single trusted system inside Orion. KBM's emphasis is on the structural elements that make a BI environment trustworthy: an "official" report convention with a GSI/Orion prefix, role-based dashboard publishing with lock-down to ensure team meetings reference identical data, a reminders portlet positioned as the primary daily work surface, and named technical access (such as SuiteQL for designated power users like Kipp) for advanced queries. KBM's choice to articulate these governance elements reflects its goal of consolidating activity into a single trusted system as part of the Orion implementation, mirroring its CRM-side commitment to mandatory data quality.

**Pivot Interiors** approaches BI as a capability and visibility opportunity. Its BRD reflects a desire to replace D365's reporting limitations (AP reports described as unusable, WIP requiring constant manual updates, AR aging needing weekly manual refresh) with a real-time, integrated reporting environment inside Orion. Pivot's emphasis is on the operational visibility its divisional and operational scope demands: a Cash Flow 360 executive dashboard, project performance dashboards with dual GP tracking (actual vs. commissionable), unified AR collections dashboards, comprehensive document management with version control, and advanced analytics including SuiteAnalytics Connect for integration with external analytics tools. Pivot's choice reflects its MillerKnoll-Certified position, in-house operations footprint, and the breadth of its reporting consumers (sales reps, project managers, controllers, executives).

Both companies share the same end-state goal: real-time dashboards, self-service saved searches, drill-down from any dashboard metric to transaction detail, customized standard reports, and elimination of Excel-centric workarounds. Where they differ is largely a matter of which aspects each company emphasized in its own discovery — KBM articulating governance discipline, Pivot articulating industry-specific capability. The merged company benefits from both contributions.

## 3.09.2 Where the two companies align

The following capabilities are common ground that requires no merged-company decision. Some are explicit on both sides, where each BRD specifically articulated the requirement; others are explicit on one side and standard NetSuite capability that carries forward for the merged company without contention.

**Explicit in both BRDs:**

- Real-time dashboards with role-based access
- Self-service saved searches with point-and-click building
- Drill-down from any dashboard metric to underlying transaction records
- Standard NetSuite reports (400+ available) customized to merged-company needs
- Multi-format export (Excel, CSV, PDF)
- Scheduled report distribution via email
- Manager hierarchy filters ("me only," "me and my team," role-based scopes)
- Department-specific or process-area role centers

**KBM-explicit; standard capability carried forward for the merged company:**

- Workbook analytics for pivot tables and charts (KBM REQ-015)
- SuiteQL access for designated technical users (KBM REQ-016)
- Inline editing on saved search results (KBM REQ-017)
- Highlighting rules for visual priority indicators (KBM REQ-018)
- Mass update functionality on saved searches (KBM REQ-019)
- As-of-date reporting for historical period snapshots (KBM REQ-014)
- Personal Home dashboard for individual customization (KBM Section 1)

**Pivot-explicit; standard capability carried forward for the merged company:**

- Saved-search templates for common furniture-dealer scenarios (Pivot REQ-3.04.04)
- Mass data export for audit and compliance requirements (Pivot REQ-3.05.05)
- Document attachment to business records (Pivot Section 3.06; depth covered in §3.09.3 D-5)

These are noted in the merged BRD, and configuration proceeds against standard NetSuite Orion capability.

## 3.09.3 Where the two companies differ

Nine in-area divergences. Each is presented as: how each company approached it (with attribution to context), the recommendation for the merged company, and the decision the leadership team owns.

---

### D-1. Report governance and "official" report designation

**Source:** KBM REQ-008, REQ-009, REQ-010 (`BRD_BusinessIntelligence_v1.0.md` §2); Pivot self-service framing (`Business_Intellegence.md` §3.04, §3.04.03 lines 589, 599; assumptions §5 line 1110 noting Sandra Rudloff's Crystal Reports experience)

**KBM's approach.** KBM articulated a governance model centered on designating "official" reports prefixed with GSI/Orion to clearly distinguish them from user-created ad-hoc searches. The model includes Public/Private saved search controls (personal exploration as Private, shared official reports as Public), and standardized interpretation documentation so users have a consistent definition of metrics like "revenue" and "booked." KBM's emphasis reflects its goal of establishing a single source of truth across the organization as part of the Orion implementation.

**Pivot's approach.** Pivot's BRD does not articulate a formal "official report" governance model. Pivot's existing operating norm is closer to capability-driven self-service, with IT-supported custom reports and saved search creation by experienced users like Sandra Rudloff (whose Crystal Reports background is referenced in the Pivot BRD assumptions as supporting saved-search adoption).

**Recommendation for the merged company.** Adopt KBM's governance model as the merged-company baseline. The reasoning is contextual: a merged organization with both companies' staff coming together benefits from clear authority on which report version is the merged-company source of truth. The GSI/Orion prefix and Public/Private discipline create that clarity. Pivot's self-service strength remains supported (saved search creation by users like Sandra Rudloff), with the addition of governance discipline that prevents version fragmentation as the merged team grows. Standardized interpretation documentation accompanies each official report.

**Decision for the leadership team.** Confirm: official report designation with GSI/Orion prefix, Public/Private saved search controls, and interpretation documentation accompanying each official report. *Recommended default: yes.*

---

### D-2. Dashboard publishing and lock-down

**Source:** KBM REQ-003, REQ-004, REQ-005 (`BRD_BusinessIntelligence_v1.0.md` §1); Pivot REQ-3.01.02, REQ-3.02.01-09 (`Business_Intellegence.md` §3.01, §3.02)

**KBM's approach.** KBM articulated role-based dashboard publishing with lock-down so managers can publish team dashboards that prevent user customization. The model includes Orion-enhanced visual components for modern aesthetics, and department-specific role centers (Finance, Sales, Pre-Quote, Order Management, Operations). KBM's emphasis on lock-down reflects its goal of ensuring weekly team meetings reference identical data and eliminating reconciliation time during meetings.

**Pivot's approach.** Pivot articulated role-based dashboards with personalized portlets per user type (sales reps, project managers, controllers, executives). The model includes specific dashboards (Cash Flow 360 for executives, project performance dashboards with cash balance and dual GP tracking, unified AR/AP dashboards for finance staff). Pivot's BRD does not specifically address whether dashboards are user-customizable or manager-locked.

**Recommendation for the merged company.** Operate the merged company with both philosophies layered: department-specific role centers with locked team dashboards (KBM's model) and personalized portlets within those role centers (Pivot's model). Each role center's locked dashboards ensure team meetings reference identical data; users can additionally configure their personal Home dashboard for individual preference. Both companies' staff get role-appropriate views consistent across teams while retaining personal customization where it doesn't disrupt team alignment.

**Decision for the leadership team.** Confirm: role-based dashboard publishing with lock-down for team dashboards; personal Home dashboard remains user-customizable. *Recommended default: yes.*

---

### D-3. Daily work surface (reminders portlet)

**Source:** KBM REQ-006, REQ-007 (`BRD_BusinessIntelligence_v1.0.md` §1)

**KBM's approach.** KBM articulated the reminders portlet as the primary daily work driver — saved searches showing bills to pay, tasks to complete, acknowledgements to review, period close checklist items, and opportunities needing follow-up. The portlet is positioned prominently on each role center as the first thing users see at the start of each day. KBM's emphasis reflects its stated philosophy that users "shouldn't have to guess" about daily priorities.

**Pivot's approach.** Pivot's BRD references personalized portlets and role-based dashboards but does not articulate the reminders portlet as a specific operating norm or daily work driver.

**Recommendation for the merged company.** Adopt KBM's reminders portlet philosophy as the merged-company default. The portlet is positioned prominently on each role center with department-specific saved searches driving the daily work view. Both individual and departmental scope are supported (e.g., finance team may benefit from departmental reminders for month-end close activities). This is a behavioral practice that supports both teams' productivity without conflicting with Pivot's existing operating norm.

**Decision for the leadership team.** Confirm: reminders portlet positioned as the primary daily work surface on each role center, with both individual and departmental scope supported. *Recommended default: yes.*

---

### D-4. Industry-specific KPIs (dual GP tracking and 360 dashboards)

**Source:** Pivot REQ-3.02.02, REQ-3.02.03, REQ-3.02.06 (`Business_Intellegence.md` §3.02); KBM REQ-026, REQ-027 (`BRD_BusinessIntelligence_v1.0.md` §7)

**KBM's approach.** KBM articulated comprehensive process-area dashboards under the "360" naming convention: Backlog 360 (combining backlog by line, by order, fulfillment status, acknowledgement tracking, customer PO status, and trends) and Bookings 360 (similar comprehensive visibility for bookings). KBM's emphasis reflects its order-management orientation and the value of consolidated process-area views.

**Pivot's approach.** Pivot articulated dual GP tracking (actual GP with time-tracked labor costs vs. commissionable GP with quoted labor rates), Cash Flow 360 executive dashboard, project performance dashboards (cash balance, WIP, labor tracking, project completion percentage), unified AR collections dashboard, and AP dashboard. Pivot's emphasis reflects its MillerKnoll-Certified position and the breadth of its operational scope where margin visibility across the deal lifecycle has high value.

**Recommendation for the merged company.** Build all the 360-style dashboards both companies articulated. They cover different process areas (Backlog, Bookings, Cash Flow, AR Collections, AP, Project Performance) and complement each other rather than compete. Dual GP tracking is adopted as a merged-company capability per Pivot's framework, building on the GP discipline framework already established in CRM §3.02 D-6. The full set of 360 dashboards is designed during the Realize phase based on the merged-company process-area scope.

**Decisions for the leadership team.**
- (4a) Confirm: full set of process-area "360" dashboards (Backlog, Bookings, Cash Flow, AR Collections, AP, Project Performance). *Recommended default: yes.*
- (4b) Confirm: dual GP tracking (actual vs. commissionable) as a merged-company KPI. *Recommended default: yes.*

---

### D-5. Document management

**Source:** Pivot REQ-3.06.01 through REQ-3.06.05 (`Business_Intellegence.md` §3.06); KBM BI BRD does not specifically address document management as a process-area concern

**KBM's approach.** KBM's BI BRD does not specifically address document management. Document attachment to records is a standard NetSuite capability that the merged company will use for operational and customer-relationship needs; no specific KBM-side requirement set drives this area.

**Pivot's approach.** Pivot articulated a comprehensive document management strategy: centralized storage associated with projects, customers, and vendors; version control with historical access; role-based access controls; document search by project, customer, type, keywords, or date ranges; and integration between document storage and transaction records. Pivot's emphasis reflects its operational scope, where project documentation, vendor agreements, and customer contracts are integral to daily workflow across multiple teams.

**Recommendation for the merged company.** Adopt Pivot's document management framework as the merged-company baseline, using NetSuite's File Cabinet with the associations and access-control features Pivot articulated. The merged company's broader operational scope (with Pivot's in-house operations footprint) makes centralized, integrated document management a foundational capability. KBM's existing approach to document attachment continues to work — it operates within the same File Cabinet — but the merged company gains the version control, role-based access, and search capabilities Pivot specified.

**Decision for the leadership team.** Confirm: centralized document management with version control, role-based access, search, and transaction-record associations. *Recommended default: yes.*

---

### D-6. Export security

**Source:** KBM REQ-011, REQ-012 (`BRD_BusinessIntelligence_v1.0.md` §5); Pivot future-state framing on external email recipients (`Business_Intellegence.md` §3.01.04 line 218)

**KBM's approach.** KBM articulated explicit export security controls: role-based export permissions (all-or-nothing per role) and a custom notification workflow that triggers an alert when a user exports more than a defined threshold (50MB working default). The notification routes to IT Security and Department Heads for investigation. KBM's emphasis reflects its awareness of departing-employee data-extraction risk and the desire for reasonable controls without disabling legitimate export use.

**Pivot's approach.** Pivot's BRD notes restrictions on emailing reports to external addresses — an entity record (typically a contact with the external email address) is required, and external addresses cannot be entered directly. Pivot's BRD does not articulate a comprehensive role-based export-permission policy or a large-export notification workflow.

**Recommendation for the merged company.** Adopt KBM's export security framework as the merged-company baseline. The merged company's broader staff base and the value of intellectual property in customer relationships and pricing make data-extraction controls relevant. Role-based export permissions are configured during initial role setup; the large-export notification workflow is implemented as a custom workflow. Pivot's external-email restriction (which is a NetSuite native control) carries forward as a complementary control.

**Decisions for the leadership team.**
- (6a) Confirm: role-based export permissions configured by role (all-or-nothing per role per NetSuite native capability). *Recommended default: yes.*
- (6b) Confirm: large-export notification workflow at the working 50MB threshold, routed to IT Security and Department Heads. *Recommended default: yes.* (Threshold and recipients confirmed during configuration.)

---

### D-7. Advanced analytics scope and SuiteAnalytics Connect

**Source:** Pivot REQ-3.07.01 through REQ-3.07.08 (`Business_Intellegence.md` §3.07); KBM does not articulate this scope explicitly

**KBM's approach.** KBM's BRD covers SuiteQL access for designated technical users (Kipp identified as a primary user) for complex queries beyond standard tools. KBM does not articulate a broader advanced-analytics scope (predictive analytics, what-if scenario modeling, custom calculated fields, external analytics integration).

**Pivot's approach.** Pivot articulated a broader advanced-analytics scope: predictive analytics for project profitability forecasting, custom KPI development for furniture-dealer-specific metrics, advanced data visualization through SuiteAnalytics, what-if scenario modeling, and SuiteAnalytics Connect for API/ODBC/JDBC access enabling integration with external analytics platforms (Power BI, Tableau, custom tools). SuiteAnalytics Connect is a paid add-on that must be purchased separately. Pivot's emphasis reflects its MillerKnoll-Certified position and the value of advanced analytics for project profitability and resource planning.

**Recommendation for the merged company.** Adopt Pivot's advanced analytics scope as a merged-company capability path. Custom calculated fields, what-if scenario modeling via saved searches with parameter inputs, and SuiteAnalytics native visualization capabilities are configured as part of standard implementation. Predictive analytics is positioned as an enabled capability for use during Realize-phase configuration of specific KPIs (project profitability forecasting, resource demand) rather than a blanket "all predictive analytics enabled" commitment. SuiteAnalytics Connect is a separate licensing decision made during Realize phase against the following triggers: a named external platform requiring direct database access (Power BI, Tableau, or custom analytics), data refresh or volume requirements that NetSuite's native export and scheduled-distribution capabilities cannot satisfy, an identified data-integration owner, and budget approval for the add-on.

**Decisions for the leadership team.**
- (7a) Confirm: advanced analytics scope (custom calculated fields, what-if modeling, SuiteAnalytics native dashboards; predictive analytics enabled for specific KPIs designed during Realize). *Recommended default: yes.*
- (7b) Confirm: SuiteAnalytics Connect licensing deferred to Realize-phase decision against the trigger criteria above. *Recommended default: yes.*

---

### D-8. Power BI strategy

**Source:** KBM REQ-002 (`BRD_BusinessIntelligence_v1.0.md` §3); Pivot SuiteApp summary (`Business_Intellegence.md` §4.01)

**KBM's approach.** KBM positioned Power BI as optional retention with a live connection requirement. If Power BI is retained, a live connection to NetSuite is required; without a live connection, users must accept that data becomes aged. KBM's stated guidance is to use NetSuite native tools first and Power BI only if a specific business case justifies it.

**Pivot's approach.** Pivot positioned Power BI as a post-implementation consideration. The BRD notes that NetSuite's native BI tools are expected to satisfy the majority of reporting requirements, potentially eliminating the need for Power BI at all. If Power BI is needed, NetSuite's data export or SuiteAnalytics Connect (per D-7) supports integration.

**Recommendation for the merged company.** Defer the Power BI decision to a post-go-live evaluation conducted after reporting needs have stabilized inside Orion. The merged company starts with NetSuite native BI tools (which both companies' BRDs agree are expected to satisfy most needs). The Power BI evaluation is triggered by a documented reporting need that NetSuite native tools, SuiteAnalytics dashboards, scheduled report distribution, and exported workbook analytics cannot satisfy. If Power BI is retained, integration uses live connection per KBM's framework or SuiteAnalytics Connect per Pivot's framework (cross-references D-7b). This deferred approach prevents pre-emptive licensing of a tool that may not be needed.

**Decision for the leadership team.** Confirm: Power BI evaluation deferred to post-go-live, triggered by a documented reporting gap. *Recommended default: yes.*

---

### D-9. Sales rep and manager scorecards

**Source:** KBM REQ-020, REQ-021 (`BRD_BusinessIntelligence_v1.0.md` §8); Pivot 2.5x pipeline multiplier and goal-management framework via CRM REQ-3.07.01 (`CRM.md` §3.07)

**KBM's approach.** KBM articulated sales-rep scorecards as a dedicated BI dashboard component combining metrics: total revenue, total GP, year-to-date performance, period comparison, pipeline value, and deals closed. The individual view uses a "me only" filter; the manager view uses a "me and my team" filter built on the employee hierarchy. KBM's emphasis reflects its goal of replacing the current manual booking-report distribution and giving reps real-time self-monitoring access.

**Pivot's approach.** Pivot's scorecard concept lives in the CRM area as the 2.5x pipeline multiplier with coaching status indicators (locked in CRM §3.02 D-9). Pivot's BI BRD does not articulate a separate individual sales scorecard with the broader metric set KBM specified.

**Recommendation for the merged company.** Build sales rep and manager scorecards as a BI dashboard component, combining KBM's metric structure (revenue, GP, YTD, period comparison, pipeline value, deals closed) with Pivot's 2.5x pipeline multiplier as one of the components. The individual view uses the rep-level "owned opportunities" visibility model already locked in CRM §3.02 D-5; the manager view uses "me and my team" filters via the employee hierarchy decided in System Setup §3.10. The scorecard is a single dashboard component that satisfies both KBM's specified metric structure and Pivot's coaching cadence.

**Decision for the leadership team.** Confirm: sales rep and manager scorecards as a BI dashboard component combining KBM's metric structure and the CRM-locked pipeline multiplier. *Recommended default: yes.*

---

## 3.09.4 Cross-area dependencies

The following surfaced in BI discovery but are decided in other process areas. They are flagged here so the working session understands the connections; the decisions themselves live in their proper home area.

| Dependency | Where it surfaced in BI | Where it's decided |
|---|---|---|
| **Pipeline stage reporting structure** | Real-time dashboards, executive presentation capability, sales scorecards | **CRM (§3.02 D-1)** — pipeline model is locked at 4-stage weighted with Commit Forecast view at Quote+ |
| **Sales rep visibility model** | Sales rep scorecard individual view (D-9) | **CRM (§3.02 D-5)** — rep-level "owned opportunities" default view drives the scorecard "me only" filter; the scorecard composition itself is decided in BI §3.09 D-9 |
| **Pipeline multiplier coaching component** | Sales rep scorecard inclusion of 2.5x multiplier (D-9) | **CRM (§3.02 D-9)** — multiplier is locked in CRM as the coaching metric; BI scorecards include it as one component alongside the broader metric set |
| **Vendor credit dashboard visibility** | Vendor credit limit warnings and proactive monitoring portlet | **Order Management (§3.04)** — vendor credit framework is decided there; BI surfaces the resulting dashboard portlets |
| **Division and territory reporting cuts** | Manager hierarchy filters, role centers, executive dashboards | **CRM (§3.02 D-3)** — two-dimensional model (geography + division) determines reporting axes |
| **GP and margin reporting (erosion, MillerKnoll mix)** | Project performance dashboards, executive financial summaries | **CRM (§3.02 D-6)** — GP framework is locked; BI dashboards reflect the locked framework |
| **Internal referral source reporting** | Cross-division referral analytics, sales attribution reporting | **CRM (§3.02 D-3c)** — capability locked in CRM; **Commissions (§3.07)** — compensation logic |
| **HubSpot campaign attribution** | Marketing campaign reporting, lead source analytics | **Marketing (§3.01)** — depends on HubSpot retention decision |
| **Approval workflow status reporting** | Approval bottleneck dashboards, approval-time tracking | **Order Management (§3.04)** — approval workflow design lives there |
| **Manager hierarchy configuration** | "Me and my team" filters across all dashboards and scorecards | **System Setup & Configuration (§3.10)** — employee-record manager assignments are foundational |

## 3.09.5 Recommendation summary

The merged-company BI playbook in shorthand:

- **Governance:** Official report designation with GSI/Orion prefix, Public/Private saved search controls, interpretation documentation per official report
- **Dashboards:** Role-based publishing with lock-down for team dashboards; personal Home dashboard remains user-customizable; department-specific role centers (Finance, Sales, Pre-Quote, Order Management, Operations, Project Management)
- **Daily work surface:** Reminders portlet positioned prominently on each role center with both individual and departmental scope
- **360 dashboards:** Full set built — Backlog 360, Bookings 360, Cash Flow 360, AR Collections, AP, Project Performance
- **Industry KPIs:** Dual GP tracking (actual vs. commissionable) as a merged-company KPI
- **Sales scorecards:** Sales rep and manager scorecards combining KBM's metric structure (revenue, GP, YTD, period comparison, pipeline value, deals closed) with the CRM-locked 2.5x pipeline multiplier as one component
- **Document management:** Centralized storage with version control, role-based access, search, and transaction-record associations
- **Export security:** Role-based export permissions per role; large-export notification workflow at 50MB working threshold
- **Advanced analytics:** Predictive analytics, custom KPIs, what-if scenario modeling, SuiteAnalytics dashboards configured as standard; SuiteAnalytics Connect licensing decided during Realize based on actual integration needs
- **Power BI:** Deferred to post-implementation evaluation
- **Standard reporting:** 400+ NetSuite reports customized for merged-company needs; AP, WIP, AR aging reports as native real-time replacements for D365 equivalents
- **Self-service tools:** Saved searches, workbook analytics, SuiteQL for designated technical users, inline editing, highlighting rules, mass update

Net read: the merged-company BI environment combines KBM's emphasis on governance discipline (official reports, dashboard lock-down, reminders portlet, export security) with Pivot's emphasis on industry-specific capability (dual GP tracking, Cash Flow 360, project performance dashboards, document management, advanced analytics). Both companies' contributions are foundational; neither displaces the other.

## 3.09.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1 | Official report designation with GSI/Orion prefix and interpretation documentation | Yes | D-1 |
| 2 | Role-based dashboard publishing with lock-down; personal Home dashboard remains customizable | Yes | D-2 |
| 3 | Reminders portlet as primary daily work surface | Yes | D-3 |
| 4a | Full set of process-area "360" dashboards (Backlog, Bookings, Cash Flow, AR, AP, Project Performance) | Yes | D-4 |
| 4b | Dual GP tracking (actual vs. commissionable) as merged-company KPI | Yes | D-4 |
| 5 | Centralized document management with version control, role-based access, search | Yes | D-5 |
| 6a | Role-based export permissions per role | Yes | D-6 |
| 6b | Large-export notification workflow at 50MB working threshold | Yes | D-6 |
| 7a | Advanced analytics scope (predictive, custom KPIs, what-if, SuiteAnalytics) configured standard | Yes | D-7 |
| 7b | SuiteAnalytics Connect licensing deferred to Realize-phase decision | Yes | D-7 |
| 8 | Power BI evaluation deferred to post-go-live | Yes | D-8 |
| 9 | Sales rep and manager scorecards as a BI dashboard component | Yes | D-9 |

> 12 decisions, all with default-yes recommendations. None require leadership-team input during the working session beyond confirmation.

## 3.09.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| Role centers (Finance, Sales, Pre-Quote, Order Management, Operations, Project Management) | Specified, in progress | Specified | Continue in surviving account; align role-center scope to merged sections |
| Dashboard lock-down configuration | Specified | Not yet built | Build per D-2 |
| Official report naming convention | Naming convention specified (GSI/Orion prefix) | Not specified | Apply per D-1 |
| Reminders portlet | Specified | Not specified | Configure per D-3 |
| 360 dashboards | Backlog 360 / Bookings 360 specified | Cash Flow 360 / project performance / AR / AP specified | Build full set per D-4 |
| Dual GP tracking | Not specified | Specified | Build per D-4b |
| Document management (File Cabinet associations + version control) | Not specified in KBM BI BRD | Specified | Build per D-5 |
| Export security (role permissions + 50MB notification workflow) | Specified (custom workflow design) | Not specified | Build per D-6 |
| SuiteAnalytics native capabilities | SuiteQL specified | SuiteAnalytics + Connect specified | Configure native; defer Connect per D-7 |
| Power BI integration | Optional with live connection | Post-implementation consideration | Defer per D-8 |
| Sales rep / manager scorecards | Specified (custom dashboard component design) | Not specified in BI BRD | Build per D-9 |
| Historical data migration (D365 / Zendesk / Core / HubSpot) supporting historical reporting and predictive analytics | Specified (Zendesk + Core extracts with deduplication) | Specified (D365 history for audit-trail continuity) | Decided in System Setup §3.10 |
| Existing document migration to NetSuite File Cabinet (network drives, SharePoint phaseout) | Not specified | Specified | Decided in System Setup §3.10 |

Configuration is early enough on both sides that the merged direction is achievable without significant rework.

## 3.09.8 Open questions / inputs needed

1. **Role-center scope for the merged company** — KBM articulated five role centers (Finance, Sales, Pre-Quote, Order Management, Operations); Pivot's structure suggests adding a Project Management center given Pivot's PM scope. Final list confirmed during configuration.
2. **Official report list per department** — the specific reports designated as "official" per department are determined during configuration with department leadership input.
3. **Dashboard component specifications for each 360 dashboard** — detailed component lists (what specific KPIs, charts, saved searches each 360 dashboard contains) are designed during the Realize phase with process-area leadership input.
4. **Export security policy details** — final 50MB threshold, notification recipients, and response procedure are confirmed during Realize phase.
5. **SuiteAnalytics Connect integration requirements** — specific external-platform integration needs that would justify licensing the add-on are documented during Realize phase.
6. **Manager hierarchy configuration** — accurate manager assignments across all employee records are foundational; depends on org-chart finalization (cross-references System Setup §3.10).
