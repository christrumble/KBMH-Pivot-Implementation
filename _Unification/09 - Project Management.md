# 3.06 — Project Management

| Field | Value |
|---|---|
| **Decision density** | **High** — Workfront vs. Orion-native project execution; Pivot has substantial Workfront-based project management infrastructure; KBM does not have a separate project-management platform. The merged-company decision is platform architecture |
| **Source coverage** | Pivot Project Management BRD v2.0 (full BRD — Pivot operates Workfront for project management); KBM does not have a separate project-management BRD because project work has been coordinated through PMs without a dedicated platform |
| **KBM source** | No separate BRD; project-management-related capabilities are addressed within other process areas (CRM project record references, Pre-Quote project request forms, Operations work orders) |
| **Pivot BRD** | `Project Management/Pivot/4 BRD/10_Pivot Interiors BRD Project Management and Workfront Process Area_v2.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/Project_Management.md`) |

---

## 3.06.1 How each company approaches Project Management today

**KBM Hogue** does not operate a dedicated project-management platform. Project coordination happens through PMs working in Asana (for RFP request management — see Marketing §3.01 D-8), Google Drive (for project documentation), email and meetings, and the Core ERP for transactional project tracking. KBM's BRDs do not include a separate Project Management process area because the function has been distributed across other tools and roles. KBM's PMs are involved in Operations (per §3.05), Pre-Quote (per §3.03), and customer-relationship coordination (per CRM §3.02) without a single platform that consolidates project execution.

**Pivot Interiors** operates Adobe Workfront as the dedicated project-management platform. Pivot's BRD documents Workfront-based capabilities including project planning and timeline management, task assignment and dependency tracking, resource allocation and capacity management, time tracking against project tasks, project-status dashboards, and integrations with Pivot's other operating platforms. Pivot's BRD explicitly identifies Workfront as a tool the team relies on heavily and one whose retention or replacement is a significant decision for the merged company. Pivot's BRD also names IPMs (Integrated Project Managers) as a specific role tier, with IPMs handling complex projects while sales coordinators handle transactional work (cross-references Pre-Quote §3.03 D-8).

The merged company faces a meaningful platform-architecture decision: continue Workfront for project management with integration to NetSuite Orion, or migrate Pivot's project-management activity into NetSuite Orion's native project record framework with custom enhancements as needed. Each path has tradeoffs.

## 3.06.2 Where the two companies align

**Explicit in both BRDs/source materials:**

- Project record as the aggregation layer for transactional data (per the approach document principle that operational data lives on transaction records and project records aggregate)
- Project-level financial tracking (revenue, cost, GP) with budget-vs-actual reporting
- Project documentation attachment via NetSuite File Cabinet or integrated external storage
- Time tracking against projects with project-GP impact

**KBM-implicit; standard NetSuite Orion capability carried forward:**

- NetSuite Orion's native project record (Pre-Quote §3.03 D-4 references this; Operations §3.05 D-7 references project-GP impact)
- Project-level KPI dashboards (per BI §3.09 D-4)

**Pivot-explicit; Workfront capabilities to be evaluated for retention or replacement:**

- Project planning and timeline management
- Task assignment and dependency tracking
- Resource allocation and capacity management
- Project-status dashboards
- Integrated time tracking against project tasks
- IPM (Integrated Project Manager) role taxonomy

## 3.06.3 Where the two companies differ

Five in-area divergences. The first is the platform-architecture decision; the others depend on it.

---

### D-1. Project-management platform — Workfront retention vs. Orion-native consolidation

**Source:** Pivot Project Management BRD §3 (Workfront capabilities); KBM source materials (no separate Project Management BRD)

**KBM's approach.** KBM does not operate a dedicated project-management platform. Project coordination happens through PMs working in Asana, Google Drive, email, and Core ERP. The merged-company project-management capability is therefore not constrained by an existing KBM platform.

**Pivot's approach.** Pivot operates Workfront as a dedicated project-management platform with substantial existing investment — task management, dependency tracking, resource allocation, capacity management, and project-status dashboards are all built in Workfront. Pivot's PMs (including IPMs) work primarily in Workfront. Sherri Nuzum is named in the Pre-Quote BRD as a key Workfront knowledge-holder.

**Recommendation for the merged company.** Pivot's Project Management BRD source-direction is that NetSuite Orion replaces Workfront. The merged-company default carries that direction forward unless leadership deliberately reopens the question.

**Path A: Project management consolidated into NetSuite Orion native (source-backed default).** Pivot's Workfront-based project management migrates into Orion's native project record framework, augmented with custom enhancements as needed for task management, resource allocation, and capacity planning. Workfront is sunset on a defined transition timeline. Risk: replicating Workfront's project-management depth in Orion native may require significant custom enhancement and a longer transition for Pivot's PM team.

**Path B: Workfront retained as project-management platform (reopened option).** Workfront continues as Pivot's existing platform; KBM's PMs onboard into Workfront for project execution. Workfront is integrated with NetSuite Orion for project-record-level financial data flow. Risk: continued multi-platform architecture (Workfront + NetSuite + HubSpot per Marketing §3.01 D-1) with ongoing license costs and integration overhead.

The platform-architecture decision is a leadership-team decision at the working session. The source-backed default is Path A (Orion replaces Workfront); Path B is feasible if leadership weighs Pivot's existing Workfront investment and PM-team proficiency as outweighing the consolidation goal.

**Decisions for the leadership team.**

- (1a) Decide: project management consolidated into NetSuite Orion native with Workfront sunset (Path A, source-backed default), or Workfront retained with NetSuite Orion integration (Path B, reopened option). *Recommended default: Path A; confirm at session.*
- (1b) If Path B: confirm bi-directional integration architecture between Workfront and NetSuite Orion. *Recommended default: only if Path B is selected.*

---

### D-2. Project record framework

**Source:** NetSuite Orion native project record (referenced across multiple sections); Pivot project record sections in BRD

**KBM's approach.** KBM relies on NetSuite Orion's native project record as the financial-and-reporting aggregation layer for transactional data.

**Pivot's approach.** Pivot uses NetSuite Orion's project record for financial tracking with execution data residing in Workfront (under Path A) or migrating to Orion (under Path B).

**Recommendation for the merged company.** Operate the merged company with NetSuite Orion's native project record as the financial-and-reporting aggregation layer, regardless of whether Workfront is retained for execution. Project-level revenue and cost tracking, dual GP reporting (per Financial Management §3.08 D-5), and project KPI dashboards (per BI §3.09 D-4) all operate from the Orion project record. Under Path A, the project record receives execution status and time data from Workfront via integration. Under Path B, all project-management activity resides in the project record.

**Decision for the leadership team.** Confirm: NetSuite Orion native project record as merged-company financial-and-reporting aggregation layer. *Recommended default: yes.* (Project execution under Path A or B per D-1.)

---

### D-3. IPM role and project-team taxonomy

**Source:** Pivot BRD references IPM (Integrated Project Manager) role in Pre-Quote §3.03 D-8 and Project Management §3.06; KBM PMs not categorized into the same role tiers

**KBM's approach.** KBM's project coordination roles are PMs without the IPM-specific categorization; coordination work spans Operations, Pre-Quote, and customer relationship management.

**Pivot's approach.** Pivot articulates IPMs as a role tier handling complex projects, with sales coordinators handling transactional work. The IPM role is named in multiple BRDs.

**Recommendation for the merged company.** The IPM-and-sales-coordinator routing model is locked in Pre-Quote §3.03 D-8 as the merged-company default. Project Management inherits the locked routing model and applies it to project-team assignment. KBM's PM staff are categorized into IPM or sales-coordinator roles based on the work they handle; specific role assignments for KBM staff are determined during organizational alignment.

**No additional decision required at the leadership team for routing model itself.** The IPM-and-sales-coordinator routing model is already locked at Pre-Quote §3.03 D-8. Project Management uses the locked model; KBM staff role assignments occur during organizational alignment.

---

### D-4. Resource allocation and capacity management

**Source:** Pivot BRD resource and capacity sections; KBM does not articulate dedicated capacity management

**KBM's approach.** KBM's project coordination has not articulated a formal resource-and-capacity-management framework; resource management has been handled informally by PMs.

**Pivot's approach.** Pivot's BRD articulates resource allocation and capacity management as a Workfront capability — assigning resources to project tasks, tracking capacity utilization, balancing workloads across PMs and field service.

**Recommendation for the merged company.** Adopt Pivot's resource allocation and capacity management framework. Under Path A (Workfront retained), the framework operates in Workfront with utilization data flowing to Orion via integration. Under Path B (Orion native), the framework is built in Orion's project module with custom enhancements. Either path provides the merged company with capacity visibility that KBM has not had previously.

**Decision for the leadership team.** Confirm: Pivot's resource allocation and capacity management framework adopted as merged-company default. *Recommended default: yes.* (Platform per D-1.)

---

### D-5. Project status visibility and dashboards

**Source:** Pivot project-status dashboard sections; cross-references BI §3.09 D-4 (360 dashboards including Project Performance 360)

**KBM's approach.** KBM articulates project-level KPI dashboards within BI §3.09 D-4 (Project Performance 360 dashboard).

**Pivot's approach.** Pivot articulates project-status dashboards in Workfront with status, milestone, timeline, and resource visibility, plus separate Project Performance 360 dashboard within NetSuite for financial KPIs (per BI §3.09 D-4).

**Recommendation for the merged company.** Operate the merged company with NetSuite Orion as the system of record for project financial KPIs (Project Performance 360 dashboard per BI §3.09 D-4) regardless of platform path. Under Path A (Workfront retained), Workfront dashboards provide execution-status visibility and Orion dashboards provide financial visibility. Under Path B (Orion native), execution-status and financial-status dashboards both reside in Orion. Cross-platform unified visibility is achieved through dashboard placement and integration.

**Decision for the leadership team.** Confirm: NetSuite Orion as system of record for project financial KPIs; project-status visibility per platform path (D-1). *Recommended default: yes.*

---

## 3.06.4 Cross-area dependencies

| Dependency | Where it surfaced in Project Management | Where it's decided |
|---|---|---|
| **Project record framework (financial KPIs)** | D-2 | **BI (§3.09 D-4)** — Project Performance 360 dashboard locked; **Financial Management (§3.08)** — project accounting decided there |
| **IPM and sales-coordinator routing** | D-3 | **Pre-Quote (§3.03 D-8)** — routing model locked; Project Management uses the model |
| **Time tracking (project-GP impact)** | Time tracking against project tasks | **Operations (§3.05 D-7)** — time tracking framework decided |
| **Document storage architecture** | Project documentation, contracts, drawings | **System Setup & Configuration (§3.10 D-3)** |
| **Multi-company / multi-contact relationship model** | Project-level customer / vendor / influencer relationships | **CRM (§3.02 D-4)** — relationship model locked |
| **GP framework (actual vs. commissionable)** | Project profitability reporting | **CRM (§3.02 D-6)** — GP framework locked |
| **Workfront integration (if Path A)** | Bi-directional Workfront ↔ NetSuite Orion sync | **System Setup & Configuration (§3.10 D-6)** — integration architecture |

## 3.06.5 Recommendation summary

The merged-company Project Management playbook in shorthand:

- **Platform architecture:** Path A working default — Workfront retained for project management with NetSuite Orion integration; Path B (Orion native consolidation) feasible if leadership prioritizes platform consolidation
- **Project record:** NetSuite Orion native project record as financial-and-reporting aggregation layer regardless of platform path
- **Role taxonomy:** IPM-and-sales-coordinator routing per Pivot framework; KBM staff role assignments during organizational alignment
- **Resource allocation and capacity management:** Pivot framework adopted; in Workfront under Path A, in Orion native under Path B
- **Project status dashboards:** NetSuite Orion for financial KPIs (Project Performance 360 per BI §3.09 D-4); Workfront for execution status under Path A
- **Time tracking:** Per Operations §3.05 D-7 framework; feeds dual GP and project profitability

Net read: project management is the most platform-architecture-significant decision in the unification. The recommendation defaults to Workfront retention because Pivot's existing investment is substantial and the PM team is operating proficiently. The alternative (Orion native consolidation) is feasible and may be preferred by leadership for platform-consolidation reasons. Either path leaves NetSuite Orion as the system of record for project financial data.

## 3.06.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1a | Project-management platform: Path A (Orion native consolidation, source-backed default) or Path B (Workfront retained, reopened option) | Path A working default; confirm at session | D-1 |
| 1b | If Path B: bi-directional Workfront ↔ NetSuite Orion integration | Conditional | D-1 |
| 2 | NetSuite Orion native project record as merged-company financial-and-reporting aggregation layer | Yes | D-2 |
| 4 | Pivot's resource allocation and capacity management framework adopted (cross-references Operations §3.05 D-8 scheduling/resource management) | Yes | D-4 |
| 5 | NetSuite Orion as system of record for project financial KPIs | Yes | D-5 |

> 5 decisions: 3 with default-yes recommendations, 1 (decision 1a, platform architecture) requiring leadership-team selection during the working session, and 1 conditional (decision 1b, conditional on Path B). This is the highest-stakes decision in this section. (D-3 IPM-and-sales-coordinator routing is inherited from Pre-Quote §3.03 D-8 and does not require a separate decision here.)

## 3.06.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| Dedicated project-management platform | Not built (no platform) | Workfront in production | Decided per D-1 |
| NetSuite Orion native project record | In progress | In progress | Configure per D-2 (regardless of D-1 path) |
| Workfront-NetSuite integration | N/A | Not yet built (Pivot uses Workfront standalone) | Build per D-1 if Path A |
| IPM role taxonomy | Not present | Present | Adopt per D-3 |
| Resource allocation and capacity management | Not built | Built in Workfront | Per D-4 (Workfront Path A or Orion Path B) |
| Project Performance 360 dashboard | Specified per BI §3.09 D-4 | Specified per BI §3.09 D-4 | Build per BI §3.09 |

## 3.06.8 Open questions / inputs needed

1. **Path A vs. Path B platform decision** (decision 1a) — leadership-team decision at working session weighing Pivot's existing Workfront investment against platform-consolidation goals.
2. **Workfront-NetSuite integration scope** (decision 1b, conditional on Path A) — bi-directional sync configuration, source-of-truth rules per object, and field mappings finalized during Realize-phase technical design (cross-references System Setup §3.10 D-6).
3. **KBM staff role assignments** (decision 3) — IPM vs. sales-coordinator categorization for KBM PMs during organizational alignment.
4. **Sherri Nuzum knowledge transfer** — Pivot's Workfront knowledge-holder named in Pre-Quote BRD; knowledge-transfer plan during the Workfront retention or sunset transition documented during change-management planning.
5. **Workfront license cost** (Path A consideration) — annual Workfront subscription cost factored into platform-decision economics during the working session.
6. **Custom enhancement scope for Path B** — if Orion native consolidation is selected, the custom enhancement scope (task management depth, dependency tracking, capacity management) is documented during Realize-phase design.
7. **Pivot project management stakeholder review** — Pivot project-management leadership reviews merged-company recommendations and platform-decision tradeoffs before the working session.
