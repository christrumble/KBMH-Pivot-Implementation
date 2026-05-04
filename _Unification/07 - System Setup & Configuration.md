# 3.10 — System Setup & Configuration

| Field | Value |
|---|---|
| **Decision density** | **Low** — foundation-level decisions tied to other areas; governance, integrations, migration scope, and identity infrastructure |
| **Source coverage** | KBM System Setup BRD v1.0 + Pivot System Setup & Configuration BRD v2.0 |
| **KBM BRD** | `System Setup and Configuration/KBMH/3 Output/BRD_SystemSetupConfiguration_v1.0.md` |
| **Pivot BRD** | `System Setup and Configuration/Pivot/4 BRD/01_Pivot Interiors BRD Setup & Configuration Process Area_v2.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/System_Setup_and_Configuration.md`) |

---

## 3.10.1 How each company approaches System Setup today

**KBM Hogue** approaches System Setup as the implementation-governance and configuration-foundation layer for the merged-company project. Its BRD articulates the DREAM methodology (Discovery → Realize → Educate → Activate/Naturalize → Maintain), dual executive sponsorship (Sean Scanlon at GSI; Matt Denning at the merged company), program-management leadership (Lorraine Guzman at KBM Hogue), change-management leadership (Kimmy Katsuyoshi), and functional workstream leads from department SMEs. The BRD covers Orion Suite App installation (5 apps), 25+ custom Orion roles with deactivation of standard NetSuite roles, soft-cutover transition strategy, and the structured 8-process-area BRD framework.

**Pivot Interiors** approaches System Setup as the platform-foundation layer for migration from D365 and HubSpot into NetSuite Orion. Its BRD covers subsidiary structure, integration architecture (HubSpot retained per Marketing §3.01 D-1; Comerica banking per Financial Management §3.08 D-6; SharePoint document management; UKG payroll per Financial Management §3.08), data migration scope, Orion-NetSuite-specific configurations including the merged role taxonomy, and configurations to support its operating cadence.

Both companies share the same end-state goals: a single NetSuite Orion environment configured for the merged-company operating model, integrated with the platforms that remain (HubSpot for marketing, banking partners, payroll providers, document management), with role-based access supporting the merged-company organizational structure. Where they differ is largely in starting-state context (KBM coming from NetSuite Core; Pivot coming from D365 + HubSpot + multiple specialty platforms) and in the breadth of integration architecture.

## 3.10.2 Where the two companies align

**Explicit in both BRDs:**

- Single NetSuite Orion environment configured for the merged-company operating model
- Custom Orion roles supporting the merged-company organizational structure
- Standard Orion Suite App installation
- Document migration to NetSuite File Cabinet and/or integrated document storage

**KBM-explicit; standard capability carried forward:**

- DREAM methodology framework (Discovery → Realize → Educate → Activate/Naturalize → Maintain)
- Dual executive sponsorship (Sean Scanlon at GSI; merged-company executive sponsor)
- Named change-management lead, program manager, and functional workstream leads
- Soft-cutover transition strategy (new business in NetSuite while completing legacy work in original systems)
- 6-8 week Discovery phase with validation focus
- 1.5-2 hour discovery sessions with two-part format (capability overview + requirements analysis)

**Pivot-explicit; standard capability carried forward:**

- Multi-Design-Center configuration supporting Pivot's existing California locations + KBM's California territories
- HubSpot integration architecture (per Marketing §3.01 D-1)
- D365-to-NetSuite migration tooling and approach
- SharePoint integration consideration (decided in D-3 below)

These are noted in the merged BRD; configuration proceeds against standard NetSuite Orion implementation patterns and the DREAM methodology.

## 3.10.3 Where the two companies differ

Six in-area divergences.

---

### D-1. Project governance and program management roles

**Source:** KBM REQ-001 through REQ-005 (`BRD_SystemSetupConfiguration_v1.0.md` §1)

**KBM's approach.** KBM's BRD articulates dual executive sponsorship (Sean Scanlon at GSI; Matt Denning at KBM Hogue), Lorraine Guzman as Program Manager, Kimmy Katsuyoshi as Change Management Lead, and functional workstream leads from department SMEs.

**Pivot's approach.** Pivot's BRD addresses governance through the standard DREAM methodology framework but does not name specific role assignments at the same level KBM does.

**Recommendation for the merged company.** Adopt KBM's named-role governance framework as the merged-company default, with Pivot leadership additions: Sean Scanlon as GSI executive sponsor; Matt Denning as merged-company executive sponsor; merged-company Program Manager and Change Management Lead determined during organizational alignment with both leadership teams' input. Functional workstream leads include both KBM and Pivot department SMEs for each process area.

**Decision for the leadership team.** Confirm: named-role governance framework with merged-company assignments determined during organizational alignment. *Recommended default: yes.*

---

### D-2. Migration sequencing — soft cutover vs. cutover-by-process-area

**Source:** KBM BRD §3-§5; Pivot BRD migration sections

**KBM's approach.** KBM's BRD articulates a soft-cutover approach: new business starts in NetSuite while existing projects complete in legacy Core over approximately 6 months.

**Pivot's approach.** Pivot's BRD addresses migration as a platform replacement (D365 to NetSuite) with its own cutover sequencing.

**Recommendation for the merged company.** Adopt the soft-cutover approach for both companies, sequenced by process area where dependencies allow. New opportunities, new orders, and new project work originate in the merged-company NetSuite Orion environment from cutover; in-flight work in either legacy system completes there or migrates as scope permits. Specific cutover timing per process area is finalized during the implementation timeline confirmation.

**Decision for the leadership team.** Confirm: soft-cutover approach for both legacy systems with process-area sequencing determined during implementation planning. *Recommended default: yes.*

---

### D-3. Document management and storage architecture

**Source:** KBM Google Drive integration (Marketing §3.01); Pivot SharePoint integration; cross-references CT-14

**KBM's approach.** KBM's existing document collaboration uses Google Drive, integrated with NetSuite via the Google Drive connector for opportunity, project, and RFP documents.

**Pivot's approach.** Pivot's existing document management uses SharePoint, with a SharePoint integration listed as one of the considered SuiteApps.

**Recommendation for the merged company.** Operate the merged company with NetSuite File Cabinet as the primary document repository for transactional documents (invoices, POs, contracts, signed proposals) and integrated external storage for collaboration documents. The specific external-storage choice between Google Drive (KBM) and SharePoint (Pivot) is a leadership-team decision. Working default: maintain both integrations during transition with a defined sunset date for one or the other determined during the working session, prioritizing the platform with greater current adoption across the merged organization.

**Decisions for the leadership team.**

- (3a) Confirm: NetSuite File Cabinet as primary repository for transactional documents. *Recommended default: yes.*
- (3b) Decide: external-storage platform for collaboration documents (Google Drive, SharePoint, or maintain both with sunset path). *Recommended default: confirm at session.*

---

### D-4. Identity and access management — merged-company role taxonomy

**Source:** KBM REQ-010 (`BRD_SystemSetupConfiguration_v1.0.md` §3); Pivot role configuration

**KBM's approach.** KBM's BRD specifies 25+ custom Orion roles deactivating standard NetSuite roles to reduce confusion.

**Pivot's approach.** Pivot's BRD articulates role-based access aligned with its divisional sales structure (Enterprise, Venture, Public, Construction Solutions per CRM §3.02 D-3b) and its in-house operations footprint.

**Recommendation for the merged company.** Adopt the standard Orion 25+ custom role taxonomy with merged-company adaptations: roles support both Pivot's divisional structure and KBM's geographic territories per the two-dimensional model locked in CRM §3.02 D-3a. Operations-specific roles reflect Pivot's in-house operations team plus KBM's outsourced-operations coordination roles (per Operations §3.05).

**Decision for the leadership team.** Confirm: standard Orion 25+ custom role taxonomy adapted for the merged-company operating model. *Recommended default: yes.* (Specific role configurations finalized during configuration.)

---

### D-5. Historical data migration scope

**Source:** Cross-references CT-13 (BI predictive analytics dependency) and Financial Management §3.08.8 #8

**KBM's approach.** KBM's source materials reference historical data migration back to 2017 for KBM Financial Management trend analysis (Financial Management REQ-017), Zendesk and Core extracts for CRM, and similar historical scope across other process areas.

**Pivot's approach.** Pivot's BRDs reference D365 historical data migration with scope determined during data-migration planning. Pivot's BRD assumes historical data is migrated to support historical reporting and predictive analytics.

**Recommendation for the merged company.** Migrate historical data sufficient to support merged-company historical reporting, period-over-period analysis, predictive analytics (per BI §3.09 D-7a), and audit-trail continuity. The specific cutover-back date is determined during data-migration planning with finance and BI leadership input — KBM's 2017 baseline and Pivot's D365 history both contribute.

**Decision for the leadership team.** Confirm: historical data migration scope sufficient for merged-company historical reporting and predictive analytics; specific date back-cutoff determined during data-migration planning. *Recommended default: yes.* (Scope finalized during configuration.)

---

### D-6. Integration architecture and field mapping

**Source:** Cross-references multiple sections — HubSpot (Marketing §3.01 D-1), banking (Financial Management §3.08 D-6), payroll (Financial Management §3.08.8 #9), MillerKnoll integrations (Order Management §3.04 D-7), expense platform (Financial Management §3.08 D-7), KBM REQ-020 Exemplis manufacturer integration (`BRD_SystemSetupConfiguration_v1.0.md` §6)

**KBM's approach.** KBM's source materials specify integration patterns for ServiceNet, ServiceTime, Coupa (evaluation pending), MillerKnoll Quote Tool, MillerKnoll Exemplis manufacturer integration (KBM REQ-020), Stripe, Paylocity, West Coast Community Bank, Google Drive.

**Pivot's approach.** Pivot's source materials specify HubSpot bi-directional sync, Comerica banking, UKG payroll, MillerKnoll Order Manager, SharePoint, ZoomInfo (evaluation), and SuiteAnalytics Connect (per BI §3.09 D-7b).

**Recommendation for the merged company.** Integration architecture combines all confirmed integrations from both companies. Field mappings, sync triggers, source-of-truth rules per object, and error handling are finalized during the technical design phase. NetSuite Orion is the system of record for the unified customer database, opportunity and revenue data, and project records; integrated platforms (HubSpot for marketing, banking platforms, payroll providers, MillerKnoll integrations) maintain their domain-specific roles.

**Decision for the leadership team.** Confirm: combined integration architecture with NetSuite Orion as system of record; technical design finalized during Realize phase. *Recommended default: yes.*

---

## 3.10.4 Cross-area dependencies

| Dependency | Where it surfaced in System Setup | Where it's decided |
|---|---|---|
| **HubSpot integration architecture and field mapping** | D-6 | **Marketing (§3.01 D-1)** — platform decision; technical design here |
| **Banking integration (West Coast Community Bank, Comerica)** | D-6 | **Financial Management (§3.08 D-6)** — bank decision; technical setup here |
| **Payroll provider (Paylocity, UKG)** | D-6 | **Financial Management (§3.08)** — provider decision; CSV import setup here |
| **MillerKnoll integrations (ServiceNet, ServiceTime, Quote Tool, Order Manager)** | D-6 | **Order Management (§3.04 D-7)** — integration suite decision; technical setup here |
| **Expense platform integration** | D-6 | **Financial Management (§3.08 D-7)** — platform decision; technical setup here |
| **SuiteAnalytics Connect licensing** | D-6 | **BI (§3.09 D-7b)** — licensing decision; technical setup here if licensed |
| **Document storage architecture (Google Drive vs. SharePoint)** | D-3 | **Decided here in System Setup §3.10 D-3** |
| **Manager hierarchy configuration for "Me and My Team" filters** | D-4 | Decided here in System Setup §3.10; depends on org-chart finalization |
| **Sales Locations / location taxonomy** | D-4 | Decided here in System Setup §3.10; cross-references CRM §3.02 D-3a |
| **Historical data migration scope** | D-5 | **Decided here in System Setup §3.10 D-5** |
| **CRM data migration approach (Zendesk, Core, HubSpot extracts and consolidation)** | D-5; cross-references CT-6 from CRM §3.02.4 | **Decided here in System Setup §3.10 D-5** — CRM-specific extraction and classification approach detailed during configuration |

## 3.10.5 Recommendation summary

The merged-company System Setup playbook in shorthand:

- **Governance:** DREAM methodology with named-role assignments determined during organizational alignment
- **Cutover strategy:** Soft cutover for both legacy systems, sequenced by process area
- **Document management:** NetSuite File Cabinet as primary; external storage decision (Google Drive vs. SharePoint) at working session
- **Roles:** 25+ custom Orion roles adapted for two-dimensional hierarchy (geography + division)
- **Historical data migration:** Scope sufficient for historical reporting and predictive analytics; specific back-cutoff during data-migration planning
- **Integration architecture:** Combined integrations across both companies with NetSuite Orion as system of record

## 3.10.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1 | Named-role governance framework with merged-company assignments | Yes | D-1 |
| 2 | Soft-cutover approach with process-area sequencing | Yes | D-2 |
| 3a | NetSuite File Cabinet as primary transactional document repository | Yes | D-3 |
| 3b | External-storage platform decision (Google Drive, SharePoint, or both with sunset) | Confirm at session | D-3 |
| 4 | Standard Orion 25+ custom role taxonomy adapted for merged-company operating model | Yes | D-4 |
| 5 | Historical data migration scope sufficient for merged-company reporting; specific back-cutoff during data-migration planning | Yes | D-5 |
| 6 | Combined integration architecture with NetSuite Orion as system of record | Yes | D-6 |

> 7 decisions: 6 with default-yes recommendations and 1 (decision 3b, external-storage platform) requiring leadership-team selection during the working session.

## 3.10.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| NetSuite Orion environment | KBM prepaid account (operating account) | Pivot D365 in use; migrating | Configure merged-company environment in KBM's prepaid account |
| Orion Suite Apps | Specified, in progress | Specified | Install per common-ground items |
| Custom Orion roles | Specified | Specified | Build merged role taxonomy per D-4 |
| Document management (File Cabinet + external storage) | Google Drive integration specified | SharePoint integration considered | Build per D-3 |
| Integration architecture | Multiple integrations specified | Multiple integrations specified | Build combined per D-6 |
| Historical data migration | 2017+ scope specified for KBM | D365 history specified | Plan combined migration per D-5 |

## 3.10.8 Open questions / inputs needed

1. **Merged-company role assignments** — Program Manager, Change Management Lead, and other named roles determined during organizational alignment.
2. **External-storage platform choice** — Google Drive vs. SharePoint vs. parallel during transition; decided at working session.
3. **Historical data migration back-cutoff date** — finalized during data-migration planning with finance and BI leadership input.
4. **Integration field mappings, sync triggers, source-of-truth rules, error handling** — completed during Realize-phase technical design.
5. **Manager hierarchy configuration** — depends on merged-company org-chart finalization.
6. **Workstream lead assignments** — KBM and Pivot department SMEs paired for each process area.
