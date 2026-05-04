# 3.04 — Order Management

| Field | Value |
|---|---|
| **Decision density** | **Medium** — approval framework, order types, document workflow, and customer-PO tracking anchor the section; many specific items align cleanly between the two BRDs |
| **Source coverage** | Pivot Order Management BRD v2.0 (12 sub-sections) + KBM Order Management requirements map (43 requirements; gap analysis identifies follow-up sessions for draft PO, customer PO tracking, e-portals, complete order type list) |
| **KBM source** | `Order Management/KBMH/3 Output/Requirements_Map_OrderManagement_v1.0.md` plus `GapAnalysis_OrderManagement_v1.1.md` and supporting files |
| **Pivot BRD** | `Order Management/Pivot/4 BRD/05_Pivot Interiors BRD Order Processing_v2.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/Order_Management.md`) |

---

## 3.04.1 How each company approaches Order Management today

**KBM Hogue** approaches Order Management through 43 detailed requirements covering transaction structure, approval workflows, customer PO tracking, tax management, template ownership, order types, commissions, and integrations. The KBM source material reflects an organization with well-defined approval rules ($25K to Shannon, missing-requirements approval to Matt Denning, cumulative erosion >$1,500 to Matt Denning), a clear order-type taxonomy (Direct Bill ~$1M annually, Intermarket inbound ~40 / outbound thousands, "Intuit Work from Home" renamed from e-commerce, Government ~20% of business), an in-house template-ownership posture (Kipp owns design and self-service modification of customer-facing and vendor-facing templates), and integrations with MillerKnoll's ServiceNet, ServiceTime, and the MillerKnoll Quote Tool. KBM's source material flags a critical change-management item: the move from a single transaction with status changes to separate linked transactions (Opportunity → Proposal → Sales Order with prefixes OP / PROP / SO / DPO / VPO / INV). KBM also flags a future business issue that requires escalation to MillerKnoll: tiered-pricing recognition at the project level when orders are split across vendor POs.

**Pivot Interiors** approaches Order Management through 12 BRD sub-sections covering invoice schedules and deposits, quote approval workflows, SIF import and BOM processing, Smart Table grouping, deposit and pre-payment management, PDF Composer, client quote approval, budget setting at sales-order conversion, pro forma invoice management, purchase order generation, MillerKnoll Order Manager integration, and acknowledgements. The Pivot BRD reflects 91% alignment with standard Orion functionality, articulates invoice schedule templates (50/40/10, 30/40/30, 100% prepay, custom variations) with deposit visibility at quote, sales order, and project levels, and emphasizes the order-modification and pro-forma flexibility that Pivot's current D365 environment does not provide natively. Pivot's BRD documents PDF Composer for line-level detail and summary, and identifies the MillerKnoll Order Manager integration as a primary integration point.

Both companies share the same end-state goals: a clean Opportunity → Quote → Sales Order → Project flow with separate linked transactions, configurable approval workflows for quotes and sales orders, SIF and BOM import via Smart Table, deposit and invoice schedule management, automated purchase order generation, MillerKnoll integration capabilities, acknowledgement automation, and tax automation through SuiteTax. Where they differ is in the specificity of approval-rule thresholds (KBM articulates explicit dollar thresholds and approver assignments; Pivot articulates the framework without the same level of named thresholds), the depth of customer-PO tracking (KBM articulates a custom record / transaction with KPI dashboard; Pivot focuses on standard quote-to-invoice flow), the order-type taxonomy detail (KBM names specific types and volumes; Pivot uses a category framework), and the template-ownership model (KBM emphasizes self-service via Kipp; Pivot uses standard PDF Composer).

## 3.04.2 Where the two companies align

The following capabilities are common ground across both BRDs/source materials and require no merged-company decision:

**Explicit in both:**

- Separate linked transactions: Opportunity → Proposal/Quote → Sales Order with one-click conversion
- Project number as primary reference key across all related transactions
- Hyperlinked relationships between related transactions
- SIF import with Smart Table integration
- Smart Table grouping for PO planning
- BOM processing for vendor purchase orders
- Tax automation through SuiteTax with ship-to-address-based calculation
- Tax-exemption certificate management with expiration tracking
- Pro forma invoice for deposits (no GL impact until payment received)
- Configurable approval workflow framework for quotes and sales orders
- Acknowledgements with automated workflow
- MillerKnoll Order Manager integration / Quote Tool integration
- Header-level commission with split-percentage assignment
- Line-level commissionable flag

**KBM-explicit; standard capability carried forward for the merged company:**

- Transaction-prefix scheme (OP / PROP / SO / DPO / VPO / INV) per KBM REQ-003
- XML import with JSON conversion (KBM REQ-007)
- Storage fees always commissionable, billed back to client (KBM REQ-015)
- 15% labor markup formula lines — see Financial Management §3.08 D-4 for merged-company decision
- Self-service template management via Kipp's ownership pattern (KBM REQ-027, REQ-028)
- ServiceNet integration for MillerKnoll intermarket orders (KBM REQ-039)
- ServiceTime integration for high-volume intermarket orders (KBM REQ-041)
- Coupa email-parsing automation for order creation (KBM REQ-040; evaluation pending)

**Pivot-explicit; standard capability carried forward for the merged company:**

- Invoice schedule templates (50/40/10, 30/40/30, 100% prepay, custom variations) with up to 5 standard templates
- Deposit visibility at quote, sales order, and project levels
- PDF Composer for line-level detail and summary
- Budget setting at Sales Order conversion
- Vendor splitting and acknowledgement processing in PO generation
- Saved-search reporting for Invoice Amount vs. Payment Received

These are noted in the merged BRD, and configuration proceeds against standard NetSuite Orion order-management capability.

## 3.04.3 Where the two companies differ

Eight in-area divergences. Each is presented as: how each company approached it (with attribution to context), the recommendation for the merged company, and the decision the leadership team owns.

---

### D-1. Approval workflow framework — thresholds, approvers, and rule capacity

**Source:** KBM REQ-020 through REQ-024 (`Requirements_Map_OrderManagement_v1.0.md`); Pivot Quote Approval Workflows section (`Order_Management.md` §3 Quote Approval Workflows)

**KBM's approach.** KBM's source material articulates explicit approval rules: orders over $25,000 route to Shannon (Project Coordinator Manager) for completeness check; orders missing any of four required items (deposit, signed proposal, signed drawings, signed lookbook) route to Matt Denning for exception; cumulative erosion exceeding $1,500 routes to Matt Denning with the philosophy that approval is a coaching/training opportunity rather than punitive. KBM allocates capacity for up to 10 approval rules and articulates approval-time tracking and reporting. KBM's framework also includes a double-order detection query (same dollar amount within 30 days flagged for manual review) as a custom requirement.

**Pivot's approach.** Pivot's BRD articulates quote approval workflows as a comprehensive framework with email-based status tracking eliminated through automated workflow routing and real-time approval visibility. Pivot's framework includes margin-based and dollar-threshold approval rules with audit trails and approval visibility, plus a low-margin SVP approval pattern that surfaced in the Pivot Feb 2026 BRD review session (cross-references CRM §3.02 D-6 GP framework). Pivot's BRD does not name specific dollar thresholds or specific KBM-style approver roles.

**Recommendation for the merged company.** Combine the two frameworks into a unified merged-company approval framework with multiple rule classes: KBM's order-value thresholds (e.g., $25K) and missing-requirements rules; KBM's cumulative-erosion approval; Pivot's low-margin SVP approval pattern; Pivot's margin-based and dollar-threshold rules with audit trails. The framework operates within Pivot's broader workflow-routing infrastructure with KBM's specific thresholds as working defaults. Pivot's framework that "Sales order means donezo" — no separate SO approval beyond proposal approval — is preserved as the merged-company default; reapproval triggers (significant scope change, dollar-amount delta beyond a threshold) are configured during Realize. Specific merged-company role assignments for the approver positions (currently Shannon and Matt Denning at KBM Hogue; SVPs at Pivot) are determined during organizational alignment. Approval-time tracking surfaces in BI dashboards (per BI §3.09).

**Decisions for the leadership team.**

- (1a) Confirm: KBM's approval-rule framework (specific thresholds, named-role approvers, up-to-10 rules, approval-time tracking) integrated within Pivot's broader workflow framework. *Recommended default: yes.*
- (1b) Confirm: $25K order-approval threshold, missing-requirements exception threshold, and $1,500 cumulative erosion threshold as merged-company working defaults. *Recommended default: yes.* (Specific merged-company role assignments determined during organizational alignment.)
- (1c) Confirm: double-order detection query (same dollar amount within 30 days flagged for manual review). *Recommended default: yes.*

---

### D-2. Customer PO tracking and KPI dashboard

**Source:** KBM REQ-016, REQ-017, REQ-018, REQ-019 (`Requirements_Map_OrderManagement_v1.0.md`); Pivot's BRD addresses customer PO information through standard PO-on-invoice fields without a dedicated tracking record

**KBM's approach.** KBM's source material articulates a custom transaction or record for customer PO tracking, with PO value aggregated at the project level and a KPI dashboard showing PO utilization, amount billed, and remaining balance with alerts when approaching the limit. The framework supports complex scenarios (multiple POs per project, change orders, blanket POs) and is identified as bank-reporting-driven and competitive-advantage-relevant. KBM identifies a separate design session as required.

**Pivot's approach.** Pivot's BRD addresses customer PO information through standard quote-to-invoice flow (customer PO number as a field on invoices and proposals) without a dedicated custom record for tracking PO utilization across multiple orders.

**Recommendation for the merged company.** Adopt KBM's customer PO tracking framework as a merged-company capability — custom record/transaction for tracking, project-level aggregation, KPI dashboard with utilization and remaining balance, and threshold alerts. The reasoning is contextual: the merged company's customer base (combining KBM's and Pivot's customers) includes large customers with project-level POs spanning multiple orders, and the bank-reporting and competitive-advantage value KBM articulates applies to the merged operation. The detailed design session KBM identified runs jointly with Pivot's order-processing leads.

**Decision for the leadership team.** Confirm: customer PO tracking framework adopted from KBM source (custom record, project-level aggregation, KPI dashboard, threshold alerts). *Recommended default: yes.* (Detailed design completed during Realize phase joint design session.)

---

### D-3. Order-type taxonomy

**Source:** KBM REQ-031 through REQ-034 (`Requirements_Map_OrderManagement_v1.0.md`); Pivot's BRD addresses order types through specialized order patterns mentioned across sub-sections

**KBM's approach.** KBM's source material names specific order types with associated volumes: Direct Bill (~$1M annually, gross up for commission, separate reporting), Intermarket (inbound ~40/year; outbound thousands handled by Shannon at 8-10/day with ServiceTime integration), "Intuit Work from Home" (renamed from e-commerce, separate reporting visibility), Government (~20% of business, special tax handling tied to KBM REQ-013). KBM's BRD identifies the dealer-as-vendor-and-customer dual setup as the first-time pain point for intermarket orders.

**Pivot's approach.** Pivot's Order Management BRD addresses order types through the broader request-engine framework documented in Pre-Quote (cross-reference Pre-Quote §3.03 D-7), which includes specialized types like WIX, ServiceNet, DUR (Delivery Upon Receipt), GSA (government), mockup, lease/third-party billing, and storage agreements. The order-type field drives automation; the typing structure is broader than KBM's named set.

**Recommendation for the merged company.** Combine the two taxonomies. KBM's named order types (Direct Bill, Intermarket, "Intuit Work from Home", Government) are integrated into Pivot's broader specialized-order-type framework (per Pre-Quote §3.03 D-7). The order-type field drives automation across both; volumes and reporting cuts reflect the merged-company business. Intermarket order processing leverages the ServiceTime and ServiceNet integrations (KBM framework) for high-volume order handling. Specific naming convention reconciliation (e.g., whether to use "Intuit Work from Home" vs. a more generic name) is finalized during configuration.

**Decision for the leadership team.** Confirm: combined order-type taxonomy — KBM's named types integrated into Pivot's broader specialized-order-type framework, with order-type field driving automation. *Recommended default: yes.* (Naming convention finalized during configuration.)

---

### D-4. Invoice schedule templates and deposit management

**Source:** Pivot Invoice Schedules and Deposits section (`Order_Management.md` §3 Invoice Schedules); KBM addresses deposits through pro forma invoice (KBM Financial Management REQ-032) but does not articulate invoice schedule templates at Pivot's level

**KBM's approach.** KBM's source materials cover deposits through the pro forma invoice mechanism (KBM Financial Management REQ-032) but do not articulate complex invoice schedule templates with predefined patterns.

**Pivot's approach.** Pivot's BRD articulates invoice schedule templates supporting common patterns (50/40/10, 30/40/30, 100% prepay) plus custom variations, with up to 5 standard templates configured. Deposit visibility spans quote, sales order, and project levels. Pro forma invoices generate with full project details while remaining outside the GL until payment is received. The framework supports invoice-amount-vs-payment-received reporting via saved search.

**Recommendation for the merged company.** Adopt Pivot's invoice schedule template framework as the merged-company default. The reasoning is contextual: Pivot's framework supports the complex billing scenarios common to commercial furniture projects (deposits, milestone billing, prepay arrangements), and KBM's pro forma invoice approach integrates as one billing pattern within the broader framework. The 5-template starting point covers the merged company's typical billing cadence, with custom variations available for specific customer arrangements.

**Decision for the leadership team.** Confirm: Pivot's invoice schedule template framework adopted as merged-company default (50/40/10, 30/40/30, 100% prepay, custom variations; up to 5 standard templates). *Recommended default: yes.*

---

### D-5. Template management — customer-facing and vendor-facing PDFs

**Source:** KBM REQ-027 through REQ-030 (`Requirements_Map_OrderManagement_v1.0.md`); Pivot PDF Composer section (`Order_Management.md` §3 PDF Composer)

**KBM's approach.** KBM's source material articulates self-service template management as a major value driver — Kipp and the team can modify templates without GSI billable hours, and Kipp owns the design ownership for customer-facing templates (proposals, invoices, order confirmations) and vendor-facing templates (purchase orders). KBM specifically identifies vendor PO redesign as a priority (vendor PO content and organization require redesign). KBM articulates template version control and change documentation as a process requirement.

**Pivot's approach.** Pivot's BRD articulates PDF Composer for line-level detail and summary on customer-facing documents but does not specifically address template ownership or vendor-PO redesign at the same level.

**Recommendation for the merged company.** Adopt KBM's self-service template management framework with Kipp-pattern ownership for the merged company. The reasoning is contextual: Kipp's design ownership is operationally valuable, and the self-service modification capability eliminates ongoing vendor billable hours. PDF Composer (Pivot's framework) provides the standard infrastructure; KBM's customer-facing and vendor-facing template designs are recreated using PDF Composer during configuration. Template version control and change documentation follow KBM's process framework.

**Decisions for the leadership team.**

- (5a) Confirm: self-service template management with merged-company design ownership (KBM's Kipp-pattern ownership extended to the merged-company team). *Recommended default: yes.*
- (5b) Confirm: customer-facing templates (proposals, invoices, order confirmations) and vendor-facing templates (purchase orders) recreated via PDF Composer during configuration. *Recommended default: yes.*

---

### D-6. Tax management — government tax overrides

**Source:** KBM REQ-013 (`Requirements_Map_OrderManagement_v1.0.md`); cross-references Financial Management §3.08 (SuiteTax framework) and CT-related tax management threads

**KBM's approach.** KBM's source material flags government order tax handling as a specific pain point. KBM has historically taxed to final destination, while MillerKnoll's policy directs tax to warehouse location for direct bill orders. The mismatch creates government-customer dissatisfaction. Government work represents approximately 20% of KBM's business; direct-bill orders represent approximately $1M annually (~1% of revenue) and are the specific intersection where the tax-handling conflict applies.

**Pivot's approach.** Pivot's BRD addresses tax through SuiteTax framework (covered in Financial Management §3.08); the BRD does not articulate the same MillerKnoll-policy-vs-final-destination conflict KBM names.

**Recommendation for the merged company.** Adopt the manual tax-override capability for government and MillerKnoll-direct-bill orders per KBM's framework. The merged company maintains the operational pattern KBM has used (escalation path documented; manual override applied per merged-company tax policy). The broader SuiteTax framework lives in Financial Management §3.08; this divergence flags the override-specific operational pattern. Communication with affected government customers about the tax-handling approach is part of the merged-company customer-relationship governance.

**Decision for the leadership team.** Confirm: manual tax-override capability for government and MillerKnoll-direct-bill orders adopted from KBM framework. *Recommended default: yes.* (Broader SuiteTax framework decided in Financial Management §3.08.)

---

### D-7. MillerKnoll integrations — ServiceNet, ServiceTime, Coupa, Quote Tool, Order Manager

**Source:** KBM REQ-039 through REQ-042 (`Requirements_Map_OrderManagement_v1.0.md`); Pivot Miller-Knoll Order Manager Integration section (`Order_Management.md` §3 Miller-Knoll Order Manager Integration)

**KBM's approach.** KBM's source material articulates four MillerKnoll-related integrations: ServiceNet for intermarket orders (REQ-039), ServiceTime for high-volume intermarket order handling (~thousands annually, Shannon's primary workload at 8-10/day, REQ-041), Coupa email-parsing automation for order creation (REQ-040, evaluation pending based on ROI), and the MillerKnoll Quote Tool at proposal and PO level (REQ-042). KBM identifies Shannon as a potential bottleneck risk for thousands of intermarket orders.

**Pivot's approach.** Pivot's BRD identifies MillerKnoll Order Manager as a primary integration with vendor splitting, acknowledgement processing, and transmission through appropriate channels. The integration framework addresses PO generation and vendor coordination but does not specifically articulate ServiceNet, ServiceTime, or Coupa.

**Recommendation for the merged company.** Combine the integration suite. ServiceNet, ServiceTime, MillerKnoll Quote Tool, and the broader MillerKnoll Order Manager integration are all configured for the merged company. Coupa email-parsing automation evaluation is preserved as a Phase-1-or-Phase-2 decision based on the merged-company's combined intermarket volume and ROI analysis. KBM staff (including Shannon) and Pivot order-processing staff jointly inherit the integrated MillerKnoll integration suite. Shannon's intermarket-order workload pattern is preserved through the same ServiceTime integration; merged-company role assignment for the high-volume intermarket position is part of the organizational alignment.

**Decisions for the leadership team.**

- (7a) Confirm: combined MillerKnoll integration suite (ServiceNet, ServiceTime, Quote Tool, Order Manager). *Recommended default: yes.*
- (7b) Confirm: Coupa email-parsing automation evaluation preserved as Phase-1-or-Phase-2 decision based on merged-company intermarket volume and ROI. *Recommended default: yes (evaluate during Realize).*

---

### D-8. Tiered pricing recognition at project level (FUTURE / escalation)

**Source:** KBM REQ-043 (`Requirements_Map_OrderManagement_v1.0.md`); not addressed in Pivot BRD

**KBM's approach.** KBM's source material flags a major future business issue: MillerKnoll's tiered-pricing program does not currently recognize project-level discount accumulation when orders are split across multiple vendor POs. The result is GP erosion on large multi-order projects, creating an installation-strategy-vs-pricing-optimization trade-off. KBM identifies an escalation path to Dustin Doucette (referenced in the source as the MillerKnoll product owner) to request project-number plus contract-number acceptance for tiered pricing.

**Pivot's approach.** Pivot's BRD does not address this issue at the requirements level.

**Recommendation for the merged company.** Carry KBM's escalation path forward as a merged-company business issue. The merged company's increased combined volume strengthens the case for MillerKnoll policy change. The escalation is owned by the merged-company commercial team in coordination with GSI's MillerKnoll relationship, with the goal of project-level tiered-pricing recognition for the merged company.

**Decision for the leadership team.** Confirm: escalation to MillerKnoll for project-level tiered-pricing recognition retained as a merged-company business issue with cross-organization commercial ownership. *Recommended default: yes.* (Resolution timing dependent on MillerKnoll response; not gating implementation.)

---

## 3.04.4 Cross-area dependencies

The following surfaced in Order Management discovery but are decided in other process areas. They are flagged here so the working session understands the connections; the decisions themselves live in their proper home area.

| Dependency | Where it surfaced in Order Management | Where it's decided |
|---|---|---|
| **Vendor credit limit tracking and alerts** | KBM REQ-026 vendor credit limit warnings at threshold | **Financial Management (§3.08 D-9)** — vendor credit framework decided there |
| **15% labor markup formula lines** | KBM REQ-038 | **Financial Management (§3.08 D-4)** — labor markup eliminated for the merged company |
| **Project GP vs. Commissionable GP** | KBM REQ-037 | **Financial Management (§3.08 D-5)** — dual GP framework operationalized; **CRM (§3.02 D-6)** — GP framework locked |
| **Pipeline stage model and forecasting** | Quote-to-Sales-Order conversion triggers | **CRM (§3.02 D-1)** — pipeline model is locked |
| **Multi-company / multi-contact relationship model** | Customer PO tracking with multiple companies on opportunity; vendor coordination | **CRM (§3.02 D-4)** — relationship model is locked |
| **RFP coordination workflow** | Pre-Quote-to-Order transitions for RFP-driven opportunities | **Marketing (§3.01 D-8)** — RFP coordination workflow lives there |
| **Order types and specialized order workflows** | Cross-reference to Pre-Quote D-7 specialized order types (WIX, ServiceNet, DUR, GSA, mockup, lease/third-party billing, storage agreements) | **Pre-Quote (§3.03 D-7)** — specialized order types decided there; Order Management uses them |
| **Tax management framework (SuiteTax, certificate management)** | Tax automation for orders | **Financial Management (§3.08)** — broader tax framework lives there |
| **Acknowledgement workflow detail** | Acknowledgements on POs | **Operations (§3.05)** — acknowledgement processing operational ownership lives there with cross-references |
| **Document storage architecture** | Customer PO documents, signed proposals, drawings, lookbooks | **System Setup & Configuration (§3.10)** — document migration plan |
| **Approval routing in Financial Management** | Bill-payment approval workflow integrates with order-approval framework | **Financial Management (§3.08 D-6)** — banking approval cross-reference |

## 3.04.5 Recommendation summary

The merged-company Order Management playbook in shorthand:

- **Transaction structure:** Separate linked transactions (Opportunity → Proposal/Quote → Sales Order → DPO/VPO/Invoice) with project number as primary reference and KBM's transaction-prefix scheme
- **Approval framework:** KBM's rule framework (specific thresholds, named-role approvers, up-to-10 rules, approval-time tracking) integrated within Pivot's workflow infrastructure; double-order detection query
- **Customer PO tracking:** Custom record / transaction with project-level aggregation, KPI dashboard, threshold alerts (KBM framework)
- **Order types:** Combined taxonomy — KBM's named types (Direct Bill, Intermarket, Intuit Work from Home, Government) integrated into Pivot's specialized-order-type framework
- **Invoice schedule templates:** Pivot's framework (50/40/10, 30/40/30, 100% prepay, custom variations; up to 5 standard templates)
- **Template management:** Self-service via PDF Composer with merged-company design ownership (KBM's Kipp-pattern)
- **Tax overrides:** Manual override capability for government and MillerKnoll-direct-bill orders
- **MillerKnoll integrations:** Combined suite (ServiceNet, ServiceTime, Quote Tool, Order Manager); Coupa evaluation deferred to Realize-phase ROI analysis
- **Tiered pricing escalation:** Retained as merged-company business issue with cross-organization commercial ownership
- **Commission:** Header-level with split-percentage (CRM-locked); line-level commissionable flag; storage fees always commissionable
- **SIF/BOM import:** Standard via Smart Table grouping
- **Acknowledgements:** Standard automation
- **PO generation:** Vendor splitting, acknowledgement processing, transmission per Pivot framework

Net read: the merged-company Order Management combines design choices that fit the merged-company's situation. Pivot's contributions reflect its invoice schedule template depth, PDF Composer infrastructure, MillerKnoll Order Manager integration framework, and process-flow orientation. KBM's contributions reflect its operational specifics — named approval thresholds, customer PO tracking framework, order-type taxonomy with volumes, self-service template ownership pattern, ServiceNet/ServiceTime/Coupa integration paths, and the MillerKnoll tiered-pricing escalation. The merged company benefits from both — Pivot's process infrastructure becomes the operational baseline; KBM's operational specifics become the implementation detail.

## 3.04.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1a | KBM's approval-rule framework integrated within Pivot's broader workflow framework | Yes | D-1 |
| 1b | $25K order-approval, missing-requirements exception, $1,500 cumulative erosion thresholds as working defaults | Yes | D-1 |
| 1c | Double-order detection query (same dollar amount within 30 days) | Yes | D-1 |
| 2 | Customer PO tracking framework adopted from KBM source | Yes | D-2 |
| 3 | Combined order-type taxonomy with KBM's named types in Pivot's broader framework | Yes | D-3 |
| 4 | Pivot's invoice schedule template framework as merged-company default | Yes | D-4 |
| 5a | Self-service template management with merged-company design ownership | Yes | D-5 |
| 5b | Customer-facing and vendor-facing templates recreated via PDF Composer during configuration | Yes | D-5 |
| 6 | Manual tax-override capability for government and MillerKnoll-direct-bill orders | Yes | D-6 |
| 7a | Combined MillerKnoll integration suite (ServiceNet, ServiceTime, Quote Tool, Order Manager) | Yes | D-7 |
| 7b | Coupa email-parsing automation evaluation preserved as Phase-1-or-Phase-2 decision | Yes (evaluate during Realize) | D-7 |
| 8 | MillerKnoll tiered-pricing escalation retained as merged-company business issue | Yes | D-8 |

> 12 decisions, all with default-yes recommendations. None require leadership-team input during the working session beyond confirmation; specific merged-company role assignments and threshold values are operational decisions during configuration.

## 3.04.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| Transaction structure (separate linked transactions) | Specified, in progress | In progress | Configure unified per common-ground items |
| Transaction prefixes (OP/PROP/SO/DPO/VPO/INV) | Specified | Not specified | Apply per KBM framework |
| Approval rules (thresholds, approvers, up to 10 rules) | Specified | Workflow framework specified, not yet thresholds | Build per D-1 |
| Customer PO tracking (custom record + KPI dashboard) | Specified, design session pending | Not specified | Build per D-2 |
| Order types (Direct Bill, Intermarket, IWFH, Government, plus Pivot specialized) | Specified | Specified (specialized types) | Build merged taxonomy per D-3 |
| Invoice schedule templates (50/40/10, 30/40/30, 100% prepay) | Not specified | Specified | Build per D-4 |
| PDF Composer for templates | Specified (KBM) | Specified (Pivot) | Configure shared infrastructure per D-5 |
| Self-service template ownership | Specified (Kipp pattern) | Not specified at the same level | Adopt Kipp-pattern ownership per D-5 |
| Tax-override capability (government, MK direct bill) | Specified | Not articulated | Configure per D-6 |
| MillerKnoll integrations (ServiceNet, ServiceTime, Quote Tool, Order Manager) | Specified | Specified (Order Manager) | Build combined suite per D-7 |
| Coupa email-parsing automation | Evaluation pending | Not specified | Defer per D-7 |
| Tiered pricing escalation to MillerKnoll | Specified (KBM REQ-043 FUTURE) | Not specified | Carry per D-8 |
| Double-order detection query | Specified (KBM REQ-025) | Not specified | Build per D-1 |
| 15% labor markup formula lines | Specified (KBM REQ-038) | Not present | Eliminate per Financial Management §3.08 D-4 |
| Storage fees always commissionable | Specified | Not specified | Configure per common-ground |

Configuration is in progress on both sides. The merged direction combines the two BRDs without significant rework.

## 3.04.8 Open questions / inputs needed

1. **Specific merged-company role assignments for approver positions** — currently Shannon ($25K) and Matt (missing requirements, erosion) at KBM; merged-company role assignments determined during organizational alignment.
2. **Customer PO tracking detailed design** (decision 2) — joint design session with Pivot's order-processing leads completed during Realize phase.
3. **Order type naming convention** — particularly whether "Intuit Work from Home" remains as a merged-company order type name or is renamed; decided during configuration.
4. **Coupa email-parsing automation ROI analysis** (decision 7b) — merged-company combined intermarket volume analysis and ROI evaluation completed during Realize phase.
5. **MillerKnoll tiered-pricing escalation timing** (decision 8) — escalation sequencing with Dustin Doucette and MillerKnoll commercial team coordinated outside implementation timeline.
6. **Vendor PO redesign specifications** (decision 5b) — KBM's identified pain point (vendor PO content and organization require redesign); detailed redesign specifications collected during template recreation phase.
7. **XML import template** (KBM REQ-007) — Matt to provide template example; rare-use case.
8. **E-Portals discovery** (KBM gap analysis flag) — Coupa and other portal requirements explored during Realize phase.
9. **Draft PO concept** (KBM gap analysis flag) — session completion needed to articulate draft PO workflow.
10. **Complete order type list** — KBM v1.1 gap analysis flags this as outstanding; merged-company complete order type list (combining KBM's named types and Pivot's specialized types) finalized during configuration.
11. **Quote versioning** — KBM v1.1 gap analysis identifies quote versioning as an open input; configuration approach (version field, version history, approval re-trigger on version change) decided during Realize.
12. **Sales order form fields** — KBM v1.1 gap analysis identifies additional SO form fields as an open input; specific field set finalized during configuration.
13. **Finance-charge capability** (KBM REQ-014) — finance-charge configuration cross-references Financial Management AR/collections framework; on/off setting and trigger conditions decided as part of merged-company AR governance.
