# 3.03 — Pre-Quote

| Field | Value |
|---|---|
| **Decision density** | **Medium** — labor quotes (KBM emphasis) and request types (Pivot emphasis) anchor the section; the merged-company request engine consolidates the two source patterns |
| **Source coverage** | Pivot Pre-Quote BRD v1.0 (full BRD with 57 → 24 request type consolidation across 10 categories) + KBM Pre-Quote requirements map and gap analysis (17 requirements; final BRD not separately produced — gap analysis and requirements map are the synthesized source) |
| **KBM source** | `Pre-Quote/KBMH/3 Output/Requirements_Map_PreQuote_v1.0.md` plus `GapAnalysis_PreQuote_Labor_Quotes_v2.0_COMPREHENSIVE.md` and supporting files |
| **Pivot BRD** | `Pre-Quote/Pivot/4 BRD/04_Pivot Interiors BRD Pre-Quote Process Area_v2.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/Pre-Quote.md`) |

---

## 3.03.1 How each company approaches Pre-Quote today

**KBM Hogue** approaches Pre-Quote primarily through the lens of labor quote management and vendor coordination. Its requirements map articulates 17 requirements covering labor quote request types (currently active: Third Party and Intermarket per the v2.0 gap analysis; Internal and Long-Term Storage marked inactive in current operations), migration from the legacy "Bridge" platform to the Orion request engine, and detailed vendor-management requirements for service providers including union/non-union classification, location-based filtering, and parent-child structures for multi-location vendors. KBM's emphasis is on the operational discipline that supports labor quoting at scale — capturing the right vendor attributes, providing job-site-analysis records, supporting RFQ (request-for-quote) forms with branded vendor communication, and a labor-quote acceptance workflow with line-level consolidation. KBM's Pre-Quote material identifies a critical process change: launch labor quote requests from the Opportunity or Quote record, not from the Project record, aligning with Orion's design philosophy that operational data lives on transaction records and project records serve as reporting/aggregation layers.

**Pivot Interiors** approaches Pre-Quote as a request-engine consolidation problem. Its BRD documents 57 distinct issue types currently managed in Adobe Workfront across 10 categories (Design Related, Finance, General, Labor Quote, Order Entry, Other, Pre-Sale, Proposal/Quote, Punch, Service). Pivot's BRD maps these 57 issue types to 24 Orion request types — 33 of the legacy types resolve to existing standard Orion processes (orders, quotes, change orders, etc.) without needing a dedicated request type, and the remaining 24 types are configured in the Orion request engine. Pivot's emphasis is on consolidating manual coordination across Workfront, IQ Coordinator, and D365 into a single platform. The BRD names Sherri Nuzum's Workfront knowledge as a key dependency the consolidation reduces, and articulates IPM (Integrated Project Manager) routing for complex projects with sales-coordinator routing for transactional work.

Both companies share the same end-state goals at a high level: a unified request engine inside Orion, automated routing based on request type and team assignment, conditional logic in request forms, document attachment, status tracking with audit trails, and elimination of manual coordination across multiple systems. Where they differ is the volume and breadth of request types (Pivot's 57 → 24 framework is larger and more cross-functional than KBM's labor-quote-centered set), the level of detail in vendor-management requirements (KBM's union/location/parent-child specificity exceeds Pivot's framing), and the source-system migration paths (Pivot from Workfront/IQ Coordinator/D365; KBM from Bridge).

## 3.03.2 Where the two companies align

The following capabilities are common ground across both BRDs/source materials and require no merged-company decision:

**Explicit in both:**

- Configurable request engine with multiple request types
- Automated routing based on request type and team assignment
- Conditional logic in request forms (dynamic fields based on user responses)
- Request approval workflows and status tracking with audit trails
- Document attachment to requests
- Vendor coordination through request workflows
- Replacement of legacy Pre-Quote tools (Pivot's Workfront + IQ Coordinator; KBM's Bridge) with the Orion request engine
- Job site analysis / site conditions record attached to address (KBM REQ-012; Pivot Requirements Management section)

**KBM-explicit; standard capability carried forward for the merged company:**

- CAM reservation number field on labor quote form (KBM REQ-006)
- CAP/SIF file attachment support for project documentation (KBM REQ-015)
- Branded RFQ form for vendor communications (KBM REQ-016)

**Pivot-explicit; standard capability carried forward for the merged company:**

- 33 of Pivot's legacy 57 issue types resolve to standard Orion processes without dedicated request types (orders, quotes, change orders, etc.)
- Quick Quote functionality for rapid transactional quotes
- Demo request workflow with delivery coordination
- GSA (government sales) order type and proposal workflow
- Mockup order type with approval workflow

These are noted in the merged BRD, and configuration proceeds against standard Orion request engine and process capability.

## 3.03.3 Where the two companies differ

Eight in-area divergences. Each is presented as: how each company approached it (with attribution to context), the recommendation for the merged company, and the decision the leadership team owns.

---

### D-1. Request engine scope and request type taxonomy

**Source:** Pivot §3.01 Request Management (`Pre-Quote.md` §3.01); KBM REQ-001, REQ-002, REQ-014 (`Requirements_Map_PreQuote_v1.0.md`)

**KBM's approach.** KBM's source material focuses on a focused set of request types: multiple labor quote categories (Internal, External, Intermarket, LTS), a project request form with service-type checkboxes (Estimating needed, Design needed, PM needed) triggering appropriate notifications, and the migration from Bridge to the Orion request engine. The breadth is narrower than Pivot's because KBM's pre-quote operations are more focused on labor quoting and project initiation.

**Pivot's approach.** Pivot's BRD documents a comprehensive request engine consolidation: 57 distinct Workfront issue types across 10 categories (Design Related, Finance, General, Labor Quote, Order Entry, Other, Pre-Sale, Proposal/Quote, Punch, Service) mapped to 24 Orion request types, with 33 of the legacy types resolving to standard Orion processes. The breadth reflects Pivot's existing operational scope (in-house operations, divisional sales structure, government and specialty workflows).

**Recommendation for the merged company.** Adopt Pivot's request type taxonomy as the merged-company baseline (24 Orion request types organized across the 10 categories). KBM's labor-quote categories (Third Party, Intermarket, with Internal and Long-Term Storage marked inactive in current operations) are configured as **subtypes or values inside the Labor Quote request type** rather than as additional top-level request types — preserving Pivot's 24-type math while supporting KBM's labor-quote operational specificity. The reasoning is contextual: the merged company inherits Pivot's broader operational scope (in-house operations, GSA workflows, design support, demo coordination, punch, service) and benefits from a comprehensive request engine that covers all those activities at the request-type level. KBM's labor categories add depth at the subtype/value level without inflating the top-level taxonomy. The 33 issue types Pivot maps to standard Orion processes carry forward as standard processes for the merged company.

**Decisions for the leadership team.**

- (1a) Confirm: Pivot's 24-request-type taxonomy adopted as merged-company baseline. *Recommended default: yes.*
- (1b) Confirm: KBM's labor-quote categories configured as subtypes/values inside the Labor Quote request type rather than as additional top-level request types. *Recommended default: yes.*

---

### D-2. Labor quote workflow depth

**Source:** KBM REQ-001, REQ-007, REQ-008, REQ-013 (`Requirements_Map_PreQuote_v1.0.md`); Pivot Labor Quote category (`Pre-Quote.md` §3.01 lines 271-283)

**KBM's approach.** KBM's source material articulates a comprehensive labor-quote workflow: multiple request types (Internal, External, Intermarket, LTS), labor-quote acceptance workflow with line-level consolidation, manual labor calculations with notes fields for institutional knowledge, pending-quote dashboard showing RFQs sent to subcontractors with status tracking, and rate-table calculations identified as a future enhancement. KBM source material names labor-quote workflow as a primary marketing-and-operations focus.

**Pivot's approach.** Pivot's BRD treats labor quote as one category within the broader 24-request-type taxonomy. Pivot articulates Quick Quote functionality for simple transactional quotes and notes a discussion-needed item for HealthCare/CSHDP labor quotes (where one person communicates with the customer and another does the work).

**Recommendation for the merged company.** Adopt KBM's labor-quote workflow depth as the merged-company labor-quote framework, integrated within Pivot's broader request engine. The reasoning is contextual: KBM's labor-quote workflow specificity (multiple request types, acceptance workflow with line consolidation, pending-quote dashboard, RFQ branding) is operationally valuable for the merged company's labor-quote volume across both legacy companies, and the framework slots cleanly into Pivot's Labor Quote category. The HealthCare/CSHDP customer-communicator-vs-worker scenario Pivot raised is addressed during configuration as a labor-quote sub-workflow. Rate-table calculations remain a future enhancement consistent with KBM's framing.

**Decision for the leadership team.** Confirm: KBM's labor-quote workflow depth (multiple request types, acceptance workflow with line consolidation, pending-quote dashboard, branded RFQ form) adopted as merged-company labor-quote framework, integrated within the 24-request-type taxonomy. *Recommended default: yes.*

---

### D-3. Vendor management for service providers

**Source:** KBM REQ-003, REQ-004, REQ-005, REQ-017 (`Requirements_Map_PreQuote_v1.0.md`); Pivot vendor management addressed primarily in Financial Management §3.15

**KBM's approach.** KBM's source material articulates detailed vendor-management requirements for Pre-Quote service providers: union/non-union status tracking on vendor records (with dropdown values for filtering), location-based identification using a custom field sourced from the COR location list, parent-child vendor relationships for multi-location service providers, and vendor filtering by union status, intermarket classification, and location. The cluster is identified as tightly coupled and requires a technical design session.

**Pivot's approach.** Pivot's Pre-Quote BRD does not articulate vendor-management requirements at the same level of detail; vendor management is addressed primarily in Financial Management §3.15 with a focus on vendor-customer dual setup and vendor credit limit tracking.

**Recommendation for the merged company.** Adopt KBM's vendor-management framework for Pre-Quote service providers as the merged-company default. Custom fields for union status, location (sourced from the merged-company location list per the System Setup §3.10 location taxonomy), and parent-child structure for multi-location vendors are configured per KBM's specification. Vendor filtering by union status, intermarket classification, and location is enabled in labor-quote creation workflows. The merged company's vendor-coordination capability across labor-quote operations benefits from this depth, and Pivot's vendor base is incorporated into the same vendor-record model.

**Decision for the leadership team.** Confirm: vendor-management framework for Pre-Quote service providers adopted from KBM source (union/non-union, location, parent-child, intermarket filtering). *Recommended default: yes.* (Specific dropdown values and field configuration finalized during Realize phase.)

---

### D-4. Request initiation point — Opportunity/Quote vs. Project record

**Source:** KBM REQ-010, REQ-011 (`Requirements_Map_PreQuote_v1.0.md`); Pivot's BRD assumes standard Orion request initiation patterns

**KBM's approach.** KBM's source material identifies a critical process change: launch labor quote requests from the Opportunity or Quote record rather than from the Project record. The change reflects Orion's design philosophy that operational data lives on transaction records and project records serve as reporting/aggregation layers. KBM names this as a significant process change from the Bridge platform requiring training and change management.

**Pivot's approach.** Pivot's BRD does not articulate this specifically because Pivot's Workfront-driven workflows have a different launch-point pattern. Pivot's BRD treats request initiation through the broader Orion request engine without specifying Opportunity/Quote vs. Project as a distinct decision.

**Recommendation for the merged company.** Adopt the Opportunity/Quote launch-point pattern (KBM's framing) as the merged-company default for Pre-Quote requests, consistent with Orion's design philosophy. The reasoning is contextual: the merged company operates from Orion's record model where transaction records (Opportunities, Quotes, Sales Orders) are the operational surface and Project records are the aggregation layer. KBM's framing aligns with this architecture; Pivot's team adopts the same pattern as part of the Workfront-to-Orion transition. Training and change management apply to both companies' staff during onboarding.

**Decision for the leadership team.** Confirm: Pre-Quote requests (labor quotes, design requests, project requests) launched from Opportunity or Quote records, not Project records. *Recommended default: yes.*

---

### D-5. Project request form — service-type triggers

**Source:** KBM REQ-014 (`Requirements_Map_PreQuote_v1.0.md`); Pivot Design Related and project-routing categories (`Pre-Quote.md` §3.01)

**KBM's approach.** KBM's source material articulates a project request form with service-type checkboxes (Estimating needed, Design needed, PM needed) triggering appropriate notifications and workflows. KBM also flags that Design and PM request workflows are currently undocumented and need additional discovery.

**Pivot's approach.** Pivot's BRD addresses design-related requests through six issue types in the Design Related category (Design Double Check, Design Support External, Design Support Internal, Design Production Support, Design Fee per Contract, Design Sub Contract Contract, Design Sub Contract Support, Design Invoice Submittal), several of which consolidate to a single design-support request record using a type field. PM routing is addressed through IPM assignment for complex projects.

**Recommendation for the merged company.** Combine: KBM's service-type-trigger pattern (Estimating, Design, PM checkboxes on project request forms) provides a clean entry point that automatically triggers the appropriate downstream workflow; Pivot's design-related request consolidation provides the depth in design-support workflows. The merged-company project request form uses service-type triggers as the user-facing entry, with the downstream workflows mapped to Pivot's consolidated request types and IPM-vs-sales-coordinator routing pattern. The Design and PM workflows that KBM flagged as undocumented are addressed through Pivot's existing design-related request structure during configuration.

**Decision for the leadership team.** Confirm: project request form with service-type triggers (KBM pattern) routing to Pivot's consolidated downstream request types (design-support, IPM assignment). *Recommended default: yes.*

---

### D-6. Request rejection / send-back workflow

**Source:** KBM REQ-009 (`Requirements_Map_PreQuote_v1.0.md`); Pivot's BRD addresses request approval workflows broadly (`Pre-Quote.md` §3.01)

**KBM's approach.** KBM's source material articulates a request rejection / send-back-for-more-information workflow as a custom requirement, with a note that confirmation is needed on whether this functionality exists in the Orion request engine or whether mandatory fields can serve as an alternative.

**Pivot's approach.** Pivot's BRD articulates request approval workflows broadly within the request engine framework but does not specifically articulate the rejection/send-back pattern at the same level.

**Recommendation for the merged company.** Adopt the rejection/send-back workflow as a merged-company capability, configured via the Orion request engine's approval routing. Whether this is built as a dedicated rejection action or addressed through mandatory-field validation is finalized during the configuration phase based on Orion request-engine capabilities. KBM's framing flags the requirement; the configuration approach is determined during Realize.

**Decision for the leadership team.** Confirm: rejection/send-back workflow is a merged-company request-engine capability. *Recommended default: yes.* (Specific configuration approach — dedicated rejection action vs. mandatory-field validation — determined during Realize phase.)

---

### D-7. Specialized order types — WIX, ServiceNet, DUR, GSA, Mockup, Storage

**Source:** Pivot §3.01 Request Management (`Pre-Quote.md` §3.01); KBM source material does not articulate these as specific specialized types

**KBM's approach.** KBM's source material does not specifically articulate WIX, ServiceNet, DUR (Delivery Upon Receipt), or GSA-specific specialized order types or quote-bypass processes.

**Pivot's approach.** Pivot's BRD documents specialized order types and quote-bypass processes for WIX, ServiceNet, DUR, Quick Quotes, warranty claims, GSA proposals, mockup orders, lease/third-party/direct billing, and storage agreements. These reflect Pivot's existing operational scope (government work, specialty fulfillment patterns, multi-channel order flows).

**Recommendation for the merged company.** Adopt Pivot's specialized order types and quote-bypass processes as merged-company capabilities. The reasoning is contextual: the merged company inherits Pivot's operational scope including government workflows (GSA), specialty fulfillment patterns (DUR, WIX, ServiceNet), and lease/third-party billing. KBM's team learns these specialized order types as part of onboarding into the merged-company operational scope. Specific configuration of each specialized type follows Pivot's BRD mapping (order-type field driving automation; vendor-type field for GSA; etc.).

**Decision for the leadership team.** Confirm: Pivot's specialized order types and quote-bypass processes (WIX, ServiceNet, DUR, GSA, mockup, lease/third-party billing, storage agreements) adopted as merged-company capabilities. *Recommended default: yes.*

---

### D-8. IPM and sales-coordinator routing model

**Source:** Pivot §3.01 Request Management (`Pre-Quote.md` §3.01); KBM source material addresses routing through service-type checkboxes (REQ-014)

**KBM's approach.** KBM's source material addresses routing through the service-type-trigger pattern on the project request form (Estimating, Design, PM checkboxes), with downstream notification and workflow assignment. KBM does not articulate a specific IPM (Integrated Project Manager) role.

**Pivot's approach.** Pivot's BRD articulates a routing model where IPMs receive complex projects while sales reps handle transactional work directly. The routing logic is built into the request engine's automated assignment rules.

**Recommendation for the merged company.** Adopt Pivot's IPM-and-sales-coordinator routing model as the merged-company default for Pre-Quote request routing. The reasoning is contextual: the merged company's project complexity spans the divisional sales motion (where Pivot's IPM model fits) and KBM's transactional patterns. The routing model assigns complex projects to IPMs and transactional work to sales coordinators, with both KBM's service-type-trigger pattern and Pivot's existing IPM assignments preserved through configuration. The specific IPM role assignment for KBM staff is part of the merged-company organizational alignment.

**Decision for the leadership team.** Confirm: IPM-and-sales-coordinator routing model adopted from Pivot framework as merged-company default. *Recommended default: yes.* (Specific IPM role assignments for KBM staff finalized during organizational alignment.)

---

## 3.03.4 Cross-area dependencies

The following surfaced in Pre-Quote discovery but are decided in other process areas. They are flagged here so the working session understands the connections; the decisions themselves live in their proper home area.

| Dependency | Where it surfaced in Pre-Quote | Where it's decided |
|---|---|---|
| **Multi-company / multi-contact relationship model for vendor coordination** | Vendor management for service providers (D-3) | **CRM (§3.02 D-4)** — relationship model is locked; Pre-Quote uses the model for vendor and contact coordination |
| **Approval workflow framework for request approvals** | Request rejection / send-back workflow (D-6); approval routing for Pre-Quote requests | **Order Management (§3.04)** — approval framework design lives there |
| **Document storage architecture (CAP/SIF files, project documentation)** | Document attachment support (KBM REQ-015) | **System Setup & Configuration (§3.10)** — document migration plan |
| **Location taxonomy for vendor location field (KBM REQ-004)** | Vendor location-based filtering (D-3) | **System Setup & Configuration (§3.10)** — Sales Locations / location taxonomy |
| **RFP coordination workflow** | RFP requests are a Pre-Quote-adjacent activity | **Marketing (§3.01 D-8)** — RFP coordination workflow lives there with cross-references |
| **Pipeline stage model** | Quote stage triggers, Pre-Quote-to-Quote transitions | **CRM (§3.02 D-1)** — pipeline model is locked |
| **Project record framework** | Pre-Quote-to-Project transitions; project request workflows | **Project Management (§3.06)** — project record structure decided there |
| **Order types and specialized order workflows** | Specialized order types (D-7) — order-type field configuration | **Order Management (§3.04)** — order-type taxonomy |
| **GP and margin discipline** | Pre-Quote labor pricing, margin calculations | **CRM (§3.02 D-6)** — GP framework is locked; **Financial Management (§3.08 D-5)** — dual GP framework operationalized |

## 3.03.5 Recommendation summary

The merged-company Pre-Quote playbook in shorthand:

- **Request engine:** Pivot's 24-request-type taxonomy across 10 categories adopted as the merged-company baseline; KBM's labor-quote request types integrated into the Labor Quote category
- **Labor quotes:** KBM's labor-quote workflow depth (multiple request types, acceptance workflow with line consolidation, pending-quote dashboard, branded RFQ form) adopted as merged-company framework
- **Vendor management for service providers:** KBM's framework adopted (union/non-union status, location field, parent-child structure, intermarket filtering)
- **Request initiation:** Launched from Opportunity or Quote records (KBM's framing, consistent with Orion design philosophy)
- **Project request form:** Service-type triggers (Estimating / Design / PM checkboxes from KBM) routing to Pivot's consolidated downstream request types
- **Rejection / send-back workflow:** Merged-company request-engine capability; specific configuration approach determined during Realize
- **Specialized order types:** Pivot's framework adopted (WIX, ServiceNet, DUR, GSA, mockup, lease/third-party billing, storage agreements)
- **Routing model:** IPM and sales-coordinator routing per Pivot framework
- **Job site analysis / site conditions:** KBM's standard Orion record framework
- **Document attachment:** Standard NetSuite document management (architecture per System Setup §3.10)

Net read: the merged-company Pre-Quote function combines design choices that fit the merged-company's situation. Pivot's contributions reflect its operational breadth (24-request-type taxonomy across 10 categories, specialized order types for government and specialty workflows, IPM routing model). KBM's contributions reflect its labor-quote operational depth and vendor-management specificity (multi-type labor quotes, acceptance workflow with line consolidation, vendor union/location/parent-child framework, RFQ branding, Opportunity/Quote launch-point discipline). The merged company benefits from both — Pivot's request-engine breadth becomes the operational baseline; KBM's labor-quote and vendor-management depth fills in the operational specifics.

## 3.03.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1a | Pivot's 24-request-type taxonomy adopted as merged-company baseline | Yes | D-1 |
| 1b | KBM's labor-quote request types integrated into the Labor Quote category | Yes | D-1 |
| 2 | KBM's labor-quote workflow depth adopted (multi-type, acceptance workflow with line consolidation, pending-quote dashboard, RFQ branding) | Yes | D-2 |
| 3 | Vendor-management framework for service providers (union/non-union, location, parent-child, intermarket filtering) | Yes | D-3 |
| 4 | Pre-Quote requests launched from Opportunity / Quote records (not Project records) | Yes | D-4 |
| 5 | Project request form with service-type triggers routing to Pivot's consolidated downstream request types | Yes | D-5 |
| 6 | Rejection / send-back workflow as merged-company request-engine capability | Yes (configuration approach during Realize) | D-6 |
| 7 | Pivot's specialized order types and quote-bypass processes (WIX, ServiceNet, DUR, GSA, mockup, lease/third-party billing, storage agreements) | Yes | D-7 |
| 8 | IPM-and-sales-coordinator routing model adopted from Pivot framework | Yes | D-8 |

> 9 decisions, all with default-yes recommendations. None require leadership-team input during the working session beyond confirmation.

## 3.03.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| Request engine | Bridge in use; specified migration to Orion | Workfront in use; specified migration to Orion | Configure unified Orion request engine per D-1 |
| Request type taxonomy | Labor-quote-focused subset | 24 types across 10 categories specified | Build Pivot taxonomy with KBM labor-quote integration per D-1 |
| Labor quote workflow | Specified (multi-type, acceptance workflow, pending-quote dashboard) | Lighter framing; integrated into Labor Quote category | Build per D-2 |
| Vendor management for Pre-Quote (union, location, parent-child) | Specified | Not specified at same depth | Build per D-3 |
| Project request form (service-type triggers) | Specified | Addressed via design-related category | Build merged form per D-5 |
| Specialized order types (WIX, ServiceNet, DUR, GSA, mockup) | Not specified | Specified | Build per D-7 |
| IPM-and-sales-coordinator routing | Not specified | Specified | Configure per D-8 |
| Branded RFQ form | Specified | Not specified | Build per D-2 |
| Job site analysis / site conditions record | Specified | Not specified | Configure standard Orion record |
| Rejection / send-back workflow | Specified (custom) | Not specified | Configure per D-6 |

Configuration is in early enough state on both sides that the merged direction is achievable. Pivot's Workfront-to-Orion mapping work and KBM's Bridge-to-Orion migration provide the framework; the merged-company configuration combines them.

## 3.03.8 Open questions / inputs needed

1. **Labor quote rate-table calculations** — KBM identifies rate-table calculations as a future enhancement (multiple dealers requesting). Decision on Phase 1 vs. post-go-live evaluation finalized during configuration.
2. **HealthCare/CSHDP labor quote sub-workflow** — Pivot flagged this scenario where one person communicates with the customer and another does the work. Specific sub-workflow design completed during configuration.
3. **Design and PM request workflow detail** — KBM source material flags Design and PM workflows as undocumented. Pivot's design-related request consolidation provides a baseline; specific workflow steps confirmed during configuration with both companies' design and PM leads.
4. **Vendor-management technical confirmations** — KBM's source material lists technical confirmations needed (does NetSuite track union status natively? multi-select vs. parent-child for location?). Confirmed during Realize phase technical design session.
5. **CAP/SIF file handling** — KBM flags that PDF vs. SIF import handling needs clarification. Specific file-handling approach decided during configuration in coordination with System Setup §3.10.
6. **IPM role assignment for KBM staff** — operational decision finalized during the merged-company organizational alignment.
7. **GSA workflow detail** — Pivot's GSA-specific workflows (Order - GSA System, Proposal - GSA, Proposal - Standard GSA) configured per Pivot framework; KBM staff training on government-sales workflows during onboarding.
8. **Specialized order type details** — WIX, ServiceNet, DUR specifics documented during configuration based on Pivot's existing operating norms.
9. **Sherri Nuzum's Workfront knowledge transfer** — Pivot's BRD names this as a key dependency. Knowledge transfer plan during the Workfront-to-Orion transition documented during change-management planning.
10. **Scope source-of-truth** — KBM v2.0 gap analysis identifies a pending decision on whether scope authoritatively lives on the labor quote form vs. the project record vs. the opportunity. Resolved during Realize phase with merged-company sales and operations leadership input.
11. **Multiple accepted labor quotes for one scope** — KBM v2.0 gap analysis identifies a pending question on auto-rejection logic when multiple competing labor quotes are accepted. Configuration approach finalized during Realize.
12. **PO-as-acceptance pattern** — KBM v2.0 gap analysis raises whether the merged company treats vendor-PO issuance as the formal acceptance event for labor quotes. Decided during Realize.
13. **External pre-quote URL linkage** — KBM source material identifies external-link handling for vendor pre-quote tools as a pending design item.
