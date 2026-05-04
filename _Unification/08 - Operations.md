# 3.05 — Operations

| Field | Value |
|---|---|
| **Decision density** | **High** — Pivot operates Operations in-house (delivery, installation, warehousing, field service); KBM has historically coordinated outsourced installation contractors. The merged company inherits Pivot's operating model as the primary capability with KBM's outsourced-coordination capability preserved for surge and geographic flexibility |
| **Source coverage** | KBM Operations BRD v1.0 (~30+ requirements covering coordination of outsourced installation) + Pivot Operations BRD v2.0 (in-house operations with field service, warehouse, scheduling, dispatch) |
| **KBM BRD** | `Operations/KBMH/3 Output/BRD_Operations_v1.0.md` |
| **Pivot BRD** | `Operations/Pivot/4 BRD/06_Pivot Interiors BRD Operations  Process Area_v2.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/Operations.md`) |

---

## 3.05.1 How each company approaches Operations today

**KBM Hogue** approaches Operations through a coordination-of-outsourced-installation model. KBM's project-management and operations team coordinates third-party installation contractors who perform field work at their own warehouses. The model presents distinctive challenges that KBM's BRD documents in detail: receiving must occur at remote contractor locations (impacting WIP), contractors must access project information without email dependency, and PMs must coordinate work in the field using mobile tools without internal installation control. KBM's BRD addresses these through the proven Orion Operations Suite — Advanced Receiving Tool for warehouse receiving, Vendor Center for contractor communication, VRA process for damage claims (the 80/20 rule), work orders for field coordination with soft-scheduling approach, time tracking for project-GP impact, 15% labor markup formula line for external labor pricing discipline, Field Service app replacing PlanGrid for punch lists with floor-plan location pinning, and the deferred direct-receiving-by-contractor capability for future phase. KBM's BRD identifies stakeholders Wendy (PM Manager / Operations Manager), Kipp (IT Specialist / Former Controller), Lorraine (CFO / Controller), Matt Denning (Leadership), Kimmy (Account Manager / Pre-Quote Manager), and the implementation team.

**Pivot Interiors** approaches Operations as a primarily internal capability supplemented by subcontractor and supplemental labor where needed. Pivot operates its own delivery and installation teams across multiple California Design Centers, with warehousing, dispatch, scheduling, and field service operating internally; subcontractor and supplemental labor extends capacity per Pivot Operations REQ-3.07 series. Its BRD covers the operational depth that an internal operating model requires: dispatch and scheduling capabilities for installation crews, warehouse management with receiving and put-away workflows, daily route planning for trucks, in-house field service with technicians using mobile apps, integrated work order management with tight coupling to the project record, and internal time tracking for installation labor (which feeds dual GP per CRM §3.02 D-6 / Financial Management §3.08 D-5).

The two operating models are fundamentally different in shape: KBM coordinates external resources; Pivot deploys internal resources. The merged company inherits Pivot's in-house operating capability as the primary model — it's the existing infrastructure, the trained field service team, the warehousing and dispatch capability, and the operating norms. KBM's outsourced-coordination capability becomes a complementary capability that supports surge capacity, geographic gaps where Pivot doesn't have direct installation reach, and continued relationships with KBM's existing third-party contractor network where those relationships deliver value.

## 3.05.2 Where the two companies align

**Explicit in both BRDs:**

- Purchase requisition approval workflow with one-click conversion to PO (KBM REQ-001; Pivot's procurement controls)
- Advanced Receiving Tool / receiving workflows
- Work order management
- Time tracking with project-GP impact
- VRA (vendor return authorization) process for damage scenarios
- Mobile field service app for technicians and PMs
- Punch list management with photo and signature collection
- Project documentation attachment

**KBM-explicit; standard capability carried forward for the merged company:**

- Coordination of outsourced installation contractors via Vendor Center
- Receiving notification feature for contractor-initiated arrivals (KBM REQ-007)
- Soft-scheduling approach for work orders (requests approval, not hard assignments) (KBM REQ-013-015)
- 15% labor markup formula line for external labor pricing — see Financial Management §3.08 D-4 for merged-company decision

**Pivot-explicit; standard capability carried forward for the merged company:**

- In-house dispatch and scheduling for installation crews
- Warehouse management with receiving, put-away, and inventory tracking
- Vehicle and truck management for delivery operations
- In-house field service with internal technicians
- Geological check-in for field workers (mobile location-based check-in)
- Integrated work-order coupling with project record

These are noted in the merged BRD; the merged-company operations function operates from Pivot's framework with KBM's outsourced-coordination capability layered in.

## 3.05.3 Where the two companies differ

Eight in-area divergences. Each is presented as: how each company approached it (with attribution to context), the recommendation for the merged company, and the decision the leadership team owns.

---

### D-1. Operating model — in-house vs. outsourced installation

**Source:** Pivot Operations BRD §3 (in-house operating model articulated throughout); KBM Operations BRD Executive Summary (outsourced installation model articulated explicitly)

**KBM's approach.** KBM coordinates outsourced installation contractors. The model is explicit and KBM's BRD is built around it: receiving at remote contractor warehouses, Vendor Center for contractor communication, soft-scheduling work orders that request approval rather than hard-assign internal crews.

**Pivot's approach.** Pivot operates installation in-house with its own field service team, dispatch, scheduling, warehousing, and vehicle management. Pivot's BRD is built around an internal operations capability with full operational depth.

**Recommendation for the merged company.** The merged-company Operations function operates from Pivot's in-house model as the primary operating capability. The reasoning is contextual: Pivot has the existing infrastructure (field service team, warehouses, dispatch capability, vehicles, operating norms); KBM has historically coordinated external resources rather than deployed internal ones. Standing up an equivalent in-house capability at KBM would be a multi-quarter business build. KBM's outsourced-coordination capability is preserved as a complementary capability for surge capacity, geographic gaps where Pivot doesn't have installation reach, and continued relationships with KBM's third-party contractor network where those relationships deliver value. KBM's project-management and operations staff onboard into Pivot's operating model; the merged-company operations team is structured around Pivot's existing model with the addition of outsourced-coordination roles.

**Decision for the leadership team.** Confirm: Pivot's in-house installation model adopted as the merged-company primary operating capability; KBM's outsourced-coordination capability preserved as complementary for surge and geographic flexibility. *Recommended default: yes.* (Specific operational org structure determined during organizational alignment.)

---

### D-2. Receiving — internal warehouse vs. contractor-remote

**Source:** KBM REQ-002, REQ-007, REQ-008 (`BRD_Operations_v1.0.md` §1-§2); Pivot warehouse receiving sections

**KBM's approach.** KBM articulates the Advanced Receiving Tool for receiving at remote third-party contractor warehouses, with a receiving notification feature where contractors notify KBM through the Vendor Center portal. Direct receiving by contractors is deferred to a future phase pending trust/process maturity.

**Pivot's approach.** Pivot operates internal warehouses with standard receiving and put-away workflows, including warehouse management for inventory tracking.

**Recommendation for the merged company.** Operate the merged company with both receiving patterns supported. Pivot's internal warehouse receiving is the primary pattern for operations Pivot performs. KBM's Advanced Receiving Tool with contractor-remote receiving notification is preserved for ongoing outsourced-installation relationships and for any geographic locations where the merged company continues to use contractor networks. The Vendor Center and contractor-notification workflow per KBM's framework remain available; direct receiving by contractors stays deferred consistent with KBM's framing.

**Decision for the leadership team.** Confirm: dual receiving pattern — Pivot's internal warehouse receiving as primary; KBM's Advanced Receiving Tool with contractor-remote notification preserved for outsourced-installation work. *Recommended default: yes.*

---

### D-3. Work orders — soft scheduling vs. hard assignment

**Source:** KBM REQ-013, REQ-014, REQ-015 (`BRD_Operations_v1.0.md` §6); Pivot work order section with dispatch and scheduling

**KBM's approach.** KBM articulates a soft-scheduling approach for work orders where requests are sent to contractors for approval rather than hard-assigned. This reflects the outsourced model where KBM doesn't directly control installation crews.

**Pivot's approach.** Pivot articulates work orders with hard scheduling and assignment to internal crews via dispatch.

**Recommendation for the merged company.** Operate the merged company with both work-order patterns. Pivot's hard-assignment pattern is the primary pattern for in-house installation work. KBM's soft-scheduling pattern remains available for work orders directed to outsourced contractors. The work-order configuration supports both modes through assignment-type fields that drive the appropriate workflow. The work order includes the assignment-type designation (internal crew vs. outsourced contractor) which determines whether it follows hard-assignment or soft-scheduling routing.

**Decision for the leadership team.** Confirm: dual work-order pattern — hard assignment for internal crews; soft scheduling for outsourced contractor coordination. *Recommended default: yes.*

---

### D-4. Field service — internal technicians vs. contractor coordination

**Source:** KBM REQ-024 through REQ-031 (`BRD_Operations_v1.0.md` §8-§9); Pivot field service sections

**KBM's approach.** KBM articulates Field Service app deployment for PMs and contractor coordination, replacing PlanGrid. The app supports tablet/mobile use, geolocation check-in, photo and signature collection, multi-resource time entry, and offline mode with sync. KBM uses the app primarily for PM oversight of contractor work rather than for direct technician dispatch.

**Pivot's approach.** Pivot articulates Field Service app deployment for internal technicians performing installation work directly. The app supports the same capabilities KBM articulates plus the work-order-to-technician dispatch flow.

**Recommendation for the merged company.** Deploy the Field Service app for both internal technicians (Pivot operating model) and PM oversight of outsourced contractors (KBM operating model). The same app supports both use cases through role configuration. Internal technicians use the app for work-order receipt, time entry, geolocation check-in, photo capture, and customer signature. PMs use the app for oversight of contractor work, punch list management, and field reporting.

**Decision for the leadership team.** Confirm: Field Service app deployed for both internal technicians and PM oversight of outsourced contractor work. *Recommended default: yes.*

---

### D-5. Punch list management — Field Service app replacing PlanGrid

**Source:** KBM REQ-024 through REQ-027 (`BRD_Operations_v1.0.md` §8); Pivot punch list workflow

**KBM's approach.** KBM articulates Field Service app punch-list capability replacing PlanGrid (a separate subscription). The capability includes floor-plan location pinning identified as a critical feature, offline mode, and field report generation.

**Pivot's approach.** Pivot articulates punch-list capability within its broader field service framework, with similar tracking, photo, and signature features.

**Recommendation for the merged company.** Adopt the Field Service app punch-list capability per KBM's framework as the merged-company default. Floor-plan location pinning is identified as a critical feature. PlanGrid runs in parallel during the transition; PlanGrid retirement is timed against contract expiration (current Pivot license date 1/10/2027 per Pivot Operations BRD). Pivot's existing punch-list workflow integrates into the Field Service app punch-list capability.

**Decisions for the leadership team.**

- (5a) Confirm: Field Service app punch list as merged-company default with floor-plan location pinning. *Recommended default: yes.*
- (5b) Confirm: PlanGrid retirement timed against contract expiration (1/10/2027) with parallel run during transition. *Recommended default: yes.*

---

### D-6. VRA (vendor return authorization) process

**Source:** KBM REQ-010, REQ-012 (`BRD_Operations_v1.0.md` §3); Pivot VRA workflow

**KBM's approach.** KBM articulates VRA process for all damage scenarios using the 80/20 rule (track expected vendor credits even when product not returned). The framework solves a critical pain point of "lost" credits and provides systematic follow-up.

**Pivot's approach.** Pivot's BRD identifies formal VRA as a decision point and assumes an informal VRA process for Phase 1 with vendor credit recovery handled outside a structured workflow. Adopting KBM's framework would change Pivot's Phase 1 assumption.

**Recommendation for the merged company.** Adopt KBM's VRA process framework with the 80/20 rule as the merged-company default. The reasoning is contextual: KBM has explicitly identified the lost-credits pain point and the 80/20 rule that solves it. Pivot adopts the formal VRA workflow as part of the merged company, replacing Pivot's informal Phase 1 assumption.

**Decision for the leadership team.** Confirm: VRA process with 80/20 rule (track expected vendor credits even when product not returned) as merged-company default; replaces Pivot's informal Phase 1 assumption. *Recommended default: yes.*

---

### D-7. Time tracking — internal labor vs. project-GP-only impact

**Source:** KBM REQ-016 (`BRD_Operations_v1.0.md` §7); Pivot time tracking sections; cross-references Financial Management §3.08 D-5 dual GP

**KBM's approach.** KBM articulates time tracking that impacts project GP only (not GL) — payroll comes from Paylocity via CSV, time entries affect project profitability analysis, not general-ledger entries.

**Pivot's approach.** Pivot articulates time tracking for internal installation labor. Time entries feed both project profitability and the dual GP framework (actual GP with time-tracked labor vs. commissionable GP with quoted labor) per CRM §3.02 D-6.

**Recommendation for the merged company.** Operate the merged company with time tracking that feeds the dual GP framework (per Financial Management §3.08 D-5) and project profitability analysis. Time entries do not directly post to GL; payroll posts to GL via the merged-company payroll provider. The framework supports both internal technician time (Pivot model) and time entries on PM oversight of outsourced contractor work (KBM model).

**Decision for the leadership team.** Confirm: time tracking feeds dual GP framework and project profitability; time entries do not directly post to GL. *Recommended default: yes.*

---

### D-8. Scheduling and resource management — depth and visibility

**Source:** KBM REQ-032 through REQ-034 (`BRD_Operations_v1.0.md` §11; KBM defers to additional discovery session); Pivot dispatch and scheduling depth

**KBM's approach.** KBM defers scheduling and resource management to an additional dedicated discovery session, citing the complexity and the balance of visibility-vs-micromanagement-and-employee-resistance.

**Pivot's approach.** Pivot articulates dispatch and scheduling capabilities with full operational depth — installation crew assignments, vehicle utilization, multi-day project scheduling, and resource utilization KPIs.

**Recommendation for the merged company.** Adopt Pivot's dispatch and scheduling framework as the merged-company default. The reasoning is contextual: Pivot has the in-house operating model that requires this depth, and the merged company inherits the model. KBM's deferred discovery session can run jointly with Pivot's operations leadership to surface KBM-specific concerns (visibility-vs-micromanagement, employee resistance) and integrate them into the merged-company configuration.

**Decision for the leadership team.** Confirm: Pivot's dispatch and scheduling framework adopted as merged-company default with KBM joint discovery session integrated. *Recommended default: yes.* (Specific configuration finalized during Realize phase.)

---

## 3.05.4 Cross-area dependencies

| Dependency | Where it surfaced in Operations | Where it's decided |
|---|---|---|
| **15% labor markup elimination** | KBM REQ-021, REQ-022, REQ-023 (formula line for external labor) | **Financial Management (§3.08 D-4)** — labor markup eliminated |
| **Dual GP framework (actual vs. commissionable)** | Time tracking impact on project profitability (D-7) | **CRM (§3.02 D-6)** — GP framework locked; **Financial Management (§3.08 D-5)** — operationalized |
| **Project record framework** | Work order coupling, project-level financial tracking | **Project Management (§3.06)** — project record decided there |
| **Document storage architecture** | Field reports, signed photos, completion certificates | **System Setup & Configuration (§3.10 D-3)** |
| **Approval workflow framework** | Purchase requisition approval (REQ-001) | **Order Management (§3.04 D-1)** |
| **Vendor management** | Outsourced installation contractor records, vendor credits, VRA | **Financial Management (§3.08)** — vendor master; cross-references CRM §3.02 D-4 multi-company model |
| **Acknowledgement workflow** | Acknowledgements on POs and work orders | **Order Management (§3.04)** |
| **Payroll provider** | Time-entry-to-payroll integration | **Financial Management (§3.08 §3.08.8 #9)** — provider decision |
| **Multi-Design-Center / multi-warehouse configuration** | Pivot's California Design Centers + KBM's territories | **System Setup & Configuration (§3.10 D-4)** |

## 3.05.5 Recommendation summary

The merged-company Operations playbook in shorthand:

- **Operating model:** Pivot's in-house installation model as primary; KBM's outsourced-coordination capability preserved for surge and geographic flexibility
- **Receiving:** Dual pattern — Pivot's internal warehouse receiving as primary; KBM's Advanced Receiving Tool with contractor-remote notification for outsourced installation work
- **Work orders:** Dual pattern — hard assignment for internal crews; soft scheduling for outsourced contractor coordination
- **Field Service app:** Deployed for both internal technicians and PM oversight of outsourced contractor work
- **Punch list:** Field Service app punch list with floor-plan location pinning; PlanGrid retired
- **VRA process:** KBM framework with 80/20 rule
- **Time tracking:** Feeds dual GP framework and project profitability; not directly to GL
- **Scheduling and dispatch:** Pivot framework adopted; KBM joint discovery session integrated
- **Vendor Center:** Standard NetSuite for contractor communication
- **Receiving notification:** Custom Orion enhancement per KBM framework

Net read: the merged-company Operations function operates primarily from Pivot's in-house framework because Pivot has the existing infrastructure and operational depth. KBM's outsourced-coordination capability is preserved and integrated as a complementary capability for the merged-company operating model. Each company contributes — Pivot the operational backbone, KBM the contractor-coordination capability and several specific features (VRA 80/20 rule, soft-scheduling for outsourced work, contractor-remote receiving notification).

## 3.05.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1 | Pivot's in-house installation model as primary; KBM's outsourced-coordination preserved as complementary | Yes | D-1 |
| 2 | Dual receiving pattern (Pivot internal warehouse + KBM contractor-remote notification) | Yes | D-2 |
| 3 | Dual work-order pattern (hard assignment for internal; soft scheduling for outsourced) | Yes | D-3 |
| 4 | Field Service app for internal technicians and PM oversight | Yes | D-4 |
| 5a | Field Service app punch list with floor-plan pinning | Yes | D-5 |
| 5b | PlanGrid retirement timed against contract expiration (1/10/2027) with parallel run | Yes | D-5 |
| 6 | VRA process with KBM 80/20 rule framework | Yes | D-6 |
| 7 | Time tracking feeds dual GP framework and project profitability (not GL) | Yes | D-7 |
| 8 | Pivot's dispatch and scheduling framework with KBM joint discovery session integrated | Yes | D-8 |

> 9 decisions, all with default-yes recommendations. Specific configurations and operational org structure (org structure for the merged operations function, PlanGrid transition, scheduling depth, payroll integration mechanics) are determined during organizational alignment and Realize phase.

## 3.05.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| In-house installation operating model | Not built (KBM uses outsourced contractors) | Existing infrastructure | Operate per Pivot model per D-1 |
| Outsourced-contractor coordination via Vendor Center | Specified | Not specified | Configure per D-1 (preserved capability) |
| Advanced Receiving Tool | Specified (Custom Orion Tool) | Standard receiving | Build per D-2 |
| Receiving notification feature | Specified (Custom Orion Enhancement) | Not specified | Configure per D-2 |
| Work orders — soft scheduling | Specified | Not specified | Configure per D-3 (preserved for outsourced) |
| Work orders — hard scheduling | Not specified | Specified | Configure per D-3 (primary for internal) |
| Field Service app | Specified (Custom Orion Solution; replaces PlanGrid) | Specified | Build per D-4, D-5 |
| VRA process with 80/20 rule | Specified | Specified | Configure per D-6 |
| Time tracking with project-GP impact | Specified | Specified | Configure per D-7 |
| Dispatch and scheduling depth | Deferred to additional session | Specified | Build per D-8 |
| 15% labor markup formula line | Specified | Not present | Eliminate per Financial Management §3.08 D-4 |

## 3.05.8 Open questions / inputs needed

1. **Operational org structure for the merged company** (decision 1) — determined during organizational alignment with both leadership teams' input.
2. **KBM joint discovery session for scheduling and resource management** (decision 8) — KBM's deferred session runs jointly with Pivot's operations leadership during Realize phase.
3. **KBM staff onboarding into Pivot's operating model** — change-management plan and timing finalized during organizational alignment.
4. **Continuing third-party contractor relationships** (decision 1) — which KBM contractor relationships continue post-merger, surge-capacity arrangements, geographic-coverage gaps determined operationally.
5. **Geological check-in and offline-mode field service requirements** — specific configuration details finalized during Realize phase.
6. **Floor-plan location pinning** (decision 5) — technical configuration and any custom Orion enhancement details documented during Realize phase.
7. **Receiving-notification workflow specifics** (decision 2) — alert recipients, response procedures, and contractor-portal access patterns finalized during Realize phase.
8. **Pivot operations stakeholder review** — Pivot operations leadership reviews merged-company recommendations before the working session.
