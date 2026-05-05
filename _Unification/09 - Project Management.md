# 3.06 — Project Management

| Field | Value |
|---|---|
| **Decision density** | **High** — Workfront sunset to Orion-native project execution; Pivot has substantial Workfront-based project management infrastructure; KBM does not have a separate project-management platform. The merged-company decisions are transition shape and capability-replacement scope |
| **Source coverage** | Pivot Project Management BRD v2.0 (full BRD — Pivot operates Workfront for project management); KBM does not have a separate project-management BRD because project work has been coordinated through PMs without a dedicated platform |
| **KBM source** | No separate BRD; project-management-related capabilities are addressed within other process areas (CRM project record references, Pre-Quote project request forms, Operations work orders) |
| **Pivot BRD** | `Project Management/Pivot/4 BRD/10_Pivot Interiors BRD Project Management and Workfront Process Area_v2.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/Project_Management.md`) |

---

## 3.06.1 How each company approaches Project Management today

**KBM Hogue** does not operate a dedicated project-management platform. Project coordination happens through PMs working in Asana (for RFP request management — see Marketing §3.01 D-8), Google Drive (for project documentation), email and meetings, and the Core ERP for transactional project tracking. KBM's BRDs do not include a separate Project Management process area because the function has been distributed across other tools and roles. KBM's PMs are involved in Operations (per §3.05), Pre-Quote (per §3.03), and customer-relationship coordination (per CRM §3.02) without a single platform that consolidates project execution.

**Pivot Interiors** operates Adobe Workfront as the dedicated project-management platform. Pivot's BRD documents Workfront-based capabilities including project planning and timeline management, task assignment and dependency tracking, resource allocation and capacity management, time tracking against project tasks, project-status dashboards, and integrations with Pivot's other operating platforms. Pivot's BRD explicitly identifies Workfront as a tool the team relies on heavily and one whose retention or replacement is a significant decision for the merged company. Pivot's BRD also names IPMs (Integrated Project Managers) as a specific role tier, with IPMs handling complex projects while sales coordinators handle transactional work (cross-references Pre-Quote §3.03 D-8).

Pivot's Project Management BRD source-direction is that NetSuite Orion replaces Workfront, and the merged company carries that direction forward. Workfront sunsets; Pivot's project-management activity migrates into NetSuite Orion's native project record framework, augmented with custom enhancements as needed. The merged-company decisions at the working session concern transition shape — sunset timeline, capability-replacement scope (which Workfront features must be present in Orion at cutover vs. phased afterward), and Pivot PM team migration plan — not whether Workfront is retained.

## 3.06.2 Where the two companies align

**Explicit in both BRDs/source materials:**

- Project record as the aggregation layer for transactional data (per the approach document principle that operational data lives on transaction records and project records aggregate)
- Project-level financial tracking (revenue, cost, GP) with budget-vs-actual reporting
- Project documentation attachment via NetSuite File Cabinet or integrated external storage
- Time tracking against projects with project-GP impact

**KBM-implicit; standard NetSuite Orion capability carried forward:**

- NetSuite Orion's native project record (Pre-Quote §3.03 D-4 references this; Operations §3.05 D-7 references project-GP impact)
- Project-level KPI dashboards (per BI §3.09 D-4)

**Pivot-explicit; Workfront capabilities being replaced in Orion native:**

- Project planning and timeline management
- Task assignment and dependency tracking
- Resource allocation and capacity management
- Project-status dashboards
- Integrated time tracking against project tasks
- IPM (Integrated Project Manager) role taxonomy

## 3.06.3 Where the two companies differ

Five in-area divergences. The first is the platform-architecture decision; the others depend on it.

---

### D-1. Project-management platform — Orion-native consolidation with Workfront sunset

**Source:** Pivot Project Management BRD §3 (Workfront capabilities, with stated direction that NetSuite Orion replaces Workfront); KBM source materials (no separate Project Management BRD)

**KBM's approach.** KBM does not operate a dedicated project-management platform. Project coordination happens through PMs working in Asana, Google Drive, email, and Core ERP. The merged-company project-management capability is therefore not constrained by an existing KBM platform.

**Pivot's approach.** Pivot operates Workfront as a dedicated project-management platform with substantial existing investment — task management, dependency tracking, resource allocation, capacity management, and project-status dashboards are all built in Workfront. Pivot's PMs (including IPMs) work primarily in Workfront. Sherri Nuzum is named in the Pre-Quote BRD as a key Workfront knowledge-holder.

**Recommendation for the merged company.** Project management consolidates into NetSuite Orion's native project record framework, augmented with custom enhancements for task management, resource allocation, dependency tracking, and capacity planning. Workfront is sunset on a defined transition timeline. Pivot's PM team migrates to Orion-native execution; KBM's PMs onboard into the same consolidated environment. The recommendation is grounded in Pivot's own Project Management BRD source-direction (NetSuite Orion replaces Workfront), the merged company's platform-consolidation goal, and the ongoing license and integration overhead that retaining Workfront would carry into a multi-platform architecture (Workfront + NetSuite + HubSpot per Marketing §3.01 D-1).

The merged-company decision at the working session is the **transition shape**, not the platform choice. Leadership confirms the sunset direction and decides on capability-replacement scope (which Workfront features must be present in Orion at cutover vs. phased after) and Workfront sunset timeline.

Risk: replicating Workfront's project-management depth in Orion native requires significant custom enhancement and a measured transition for Pivot's PM team. The transition plan must front-load the capabilities the team relies on most heavily and protect Pivot's PM productivity through cutover.

**Decisions for the leadership team.**

- (1a) Confirm: project management consolidates into NetSuite Orion native; Workfront sunsets on a defined transition timeline. *Recommended default: yes.*
- (1b) Decide: capability-replacement scope at cutover (which Workfront features must be present in Orion at go-live vs. phased afterward) and Workfront sunset timeline. *Recommended default: scope and timeline refined at the working session with Pivot PM team input.*

---

### D-2. Project record framework

**Source:** NetSuite Orion native project record (referenced across multiple sections); Pivot project record sections in BRD

**KBM's approach.** KBM relies on NetSuite Orion's native project record as the financial-and-reporting aggregation layer for transactional data.

**Pivot's approach.** Pivot uses NetSuite Orion's project record for financial tracking with execution data currently residing in Workfront. Per D-1, execution data migrates to the Orion project record on the Workfront sunset timeline.

**Recommendation for the merged company.** Operate the merged company with NetSuite Orion's native project record as the financial-and-reporting aggregation layer and the system of record for project execution after the Workfront sunset. Project-level revenue and cost tracking, dual GP reporting (per Financial Management §3.08 D-5), project KPI dashboards (per BI §3.09 D-4), and project execution data (status, milestones, time, resource utilization) all operate from the Orion project record once consolidation completes.

**Decision for the leadership team.** Confirm: NetSuite Orion native project record as merged-company financial-and-reporting aggregation layer and project-execution system of record. *Recommended default: yes.*

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

**Recommendation for the merged company.** Adopt Pivot's resource allocation and capacity management framework, built in Orion's project module with custom enhancements during the Workfront sunset transition. The framework provides the merged company with capacity visibility that KBM has not had previously, and preserves the operating discipline Pivot's PMs already rely on.

**Decision for the leadership team.** Confirm: Pivot's resource allocation and capacity management framework adopted as merged-company default, built in Orion native per D-1. *Recommended default: yes.*

---

### D-5. Project status visibility and dashboards

**Source:** Pivot project-status dashboard sections; cross-references BI §3.09 D-4 (360 dashboards including Project Performance 360)

**KBM's approach.** KBM articulates project-level KPI dashboards within BI §3.09 D-4 (Project Performance 360 dashboard).

**Pivot's approach.** Pivot articulates project-status dashboards in Workfront with status, milestone, timeline, and resource visibility, plus separate Project Performance 360 dashboard within NetSuite for financial KPIs (per BI §3.09 D-4).

**Recommendation for the merged company.** Operate the merged company with NetSuite Orion as the system of record for both project financial KPIs (Project Performance 360 dashboard per BI §3.09 D-4) and project execution status (timeline, milestones, resource utilization). Execution-status and financial-status dashboards both reside in Orion after the Workfront sunset. Custom enhancements deliver the execution-visibility depth Pivot's PMs rely on today.

**Decision for the leadership team.** Confirm: NetSuite Orion as system of record for project financial KPIs and project execution status. *Recommended default: yes.*

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
| **Workfront sunset and data migration** | Project, task, time, and capacity data migration from Workfront to Orion native | **System Setup & Configuration (§3.10 D-5)** — historical data migration scope; transition plan owned in Project Management D-1 |

## 3.06.5 Recommendation summary

The merged-company Project Management playbook in shorthand:

- **Platform architecture:** NetSuite Orion native project record consolidation; Workfront sunsets on a defined transition timeline
- **Project record:** NetSuite Orion native project record as financial-and-reporting aggregation layer and project-execution system of record
- **Role taxonomy:** IPM-and-sales-coordinator routing per Pivot framework; KBM staff role assignments during organizational alignment
- **Resource allocation and capacity management:** Pivot framework adopted, built in Orion native with custom enhancements during the Workfront sunset transition
- **Project status dashboards:** NetSuite Orion for both project financial KPIs (Project Performance 360 per BI §3.09 D-4) and project execution status
- **Time tracking:** Per Operations §3.05 D-7 framework; feeds dual GP and project profitability

Net read: project management is the most operationally significant transition in the unification because Pivot's PMs work primarily in Workfront today. The recommendation commits to Orion-native consolidation in line with Pivot's own BRD direction; the working-session decisions are about transition shape — capability-replacement scope at cutover, sunset timeline, and Pivot PM team migration plan — not about whether Workfront is retained.

## 3.06.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1a | Project management consolidates into NetSuite Orion native; Workfront sunsets on a defined transition timeline | Yes | D-1 |
| 1b | Capability-replacement scope at cutover and Workfront sunset timeline | Refine at working session with Pivot PM team input | D-1 |
| 2 | NetSuite Orion native project record as merged-company financial-and-reporting aggregation layer and project-execution system of record | Yes | D-2 |
| 3 | Pivot's resource allocation and capacity management framework adopted, built in Orion native (cross-references Operations §3.05 D-8 scheduling/resource management) | Yes | D-4 |
| 4 | NetSuite Orion as system of record for project financial KPIs and project execution status | Yes | D-5 |

> 5 decisions: 4 with default-yes recommendations and 1 (decision 1b, transition shape) refined at the working session with Pivot PM team input. The platform-consolidation direction is committed; the working-session focus is the transition plan that protects Pivot PM productivity through cutover. (D-3 IPM-and-sales-coordinator routing is inherited from Pre-Quote §3.03 D-8 and does not require a separate decision here.)

## 3.06.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| Dedicated project-management platform | Not built (no platform) | Workfront in production | Sunset Workfront per D-1 transition plan; Orion native is the merged-company platform |
| NetSuite Orion native project record | In progress | In progress | Configure per D-2 as financial aggregation layer and execution system of record |
| Workfront sunset and data migration | N/A | Workfront in production | Plan migration of project, task, time, and capacity data per D-1; align with System Setup §3.10 D-5 |
| IPM role taxonomy | Not present | Present | Adopt per D-3 |
| Resource allocation and capacity management | Not built | Built in Workfront | Build in Orion native per D-4 with custom enhancements during the Workfront sunset transition |
| Project Performance 360 dashboard | Specified per BI §3.09 D-4 | Specified per BI §3.09 D-4 | Build per BI §3.09 |

## 3.06.8 Open questions / inputs needed

1. **Capability-replacement scope at cutover** (decision 1b) — which Workfront features must be present in Orion at go-live (task management depth, dependency tracking, resource allocation, capacity management, status dashboards) vs. phased afterward; refined at the working session with Pivot PM team input.
2. **Workfront sunset timeline** (decision 1b) — date for Workfront subscription wind-down and the transition shape that gets the Pivot PM team there without operational disruption; refined at the working session.
3. **KBM staff role assignments** — IPM vs. sales-coordinator categorization for KBM PMs during organizational alignment.
4. **Sherri Nuzum knowledge transfer** — Pivot's Workfront knowledge-holder named in Pre-Quote BRD; knowledge-transfer plan during the Workfront sunset transition documented during change-management planning.
5. **Workfront historical data migration scope** — project, task, time, and capacity data extraction from Workfront and migration to Orion native; planned with System Setup §3.10 D-5.
6. **Custom enhancement design** — task management depth, dependency tracking, and capacity management enhancements documented during Realize-phase design.
7. **Pivot project management stakeholder review** — Pivot project-management leadership reviews merged-company recommendations and the transition plan before the working session.
