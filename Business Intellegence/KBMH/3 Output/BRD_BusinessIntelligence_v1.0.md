# Business Requirements Document
## Solution Alignment & Validation

**Business Intelligence & Reporting**

---

## Document Header and Project Information

**Document Title:** Business Requirements Document - Solution Alignment & Validation  
**Process Area:** Business Intelligence & Reporting  
**Audience:** C-suite executives approving NetSuite/Orion implementation  
**Purpose:** Validate that the proven Orion/NetSuite solution meets KBM Hoag's BI and reporting requirements

### Project Information
**Implementation Name:** KBM Hoag NetSuite Implementation  
**Customer Name:** KBM Hoag  
**Project Name & Number:** Orion/NetSuite Implementation  
**Document Owner:** Global Systems Integration (GSI)  
**Prepared Date:** December 2025

---

## Document Change Log

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0 | 2025-12-16 | GSI Implementation Team | Initial BRD based on Business Intelligence discovery questionnaire (v1.0), Requirements Map (v1.0), and Master Transcript from July 2025 workshop |

---

## Executive Summary

KBM Hoag currently operates with a **fragmented, manual, and inconsistent reporting environment** where multiple teams create similar reports with different criteria, leading to trust issues and inefficient decision-making. Users reference "Mark's version, Matt's version, Kip's version" of the same report with conflicting data, creating confusion across the organization.

The proven **Orion/NetSuite solution establishes a single source of truth** for all business intelligence and reporting through native, powerful BI capabilities. This BRD validates how the standard Orion/NetSuite platform—enhanced with Orion-specific components—addresses KBM Hoag's requirements without requiring custom development in most areas.

**Key alignment:**
- **27 requirements** identified through discovery
- **18 ALIGNS** with standard NetSuite BI tools (dashboards, saved searches, standard reports, workbook analytics, SuiteQL)
- **3 ADAPT** through process/behavior changes (Power BI strategy, official report adoption, criteria documentation)
- **6 ACCOMMODATE** requiring custom design (dashboard lock-down, export notification workflow, sales rep scorecards, Backlog 360, Bookings 360)

**Strategic objectives:**
1. **"Singing from the Same Songbook"** - Eliminate multiple report versions through official report designation and governance
2. **Real-Time Decision Making** - Replace manual Excel reports with live NetSuite dashboards offering immediate drill-down capability
3. **Daily Work Clarity** - Implement reminders portlet as daily work driver eliminating guesswork
4. **Manager-Team Alignment** - Lock published dashboards ensuring consistent data for weekly team meetings
5. **Data Security** - Implement role-based export controls and large-export notifications to prevent customer data breaches
6. **Self-Service Analytics** - Enable drill-down, workbook analytics, and saved searches for user independence

The Orion/NetSuite solution is proven, scalable, and ready for immediate implementation with minimal custom development required for core BI functionality.

---

## Section 1: Dashboard & Publishing Strategy

### Current State Process

**Process: Weekly Sales Team Meeting**

KBM Hoag currently conducts weekly sales team meetings where managers reference dashboards to discuss opportunities and performance. However, **team members have customized their personal dashboards**, resulting in inconsistent data views. When a manager references an opportunity, team members report "I don't see that," derailing discussions and delaying decisions. This dashboard fragmentation creates accountability challenges and wastes meeting time on reconciliation rather than strategic discussion.

**Monthly Financial Review Process** follows similar patterns: Finance team must manually compile reports from multiple sources into email packages, creating delays and introducing errors. When executives cannot meet in person, static packages limit drill-down capability for follow-up questions.

**Additional Challenges:**
- Users resist standardized dashboards, preferring personal customization
- Manager-team alignment impossible when everyone sees different data
- No clear daily work priorities - "you shouldn't have to guess"
- Multiple unofficial report versions confuse team members

### Your Business Requirements

#### REQ-003: Implement Role-Based Dashboard Publishing with Lock-Down Capability (ACCOMMODATE)
**Business Value:** Ensures weekly team meetings reference identical data, eliminating "I don't see that" excuses and improving decision speed and accountability.

**Requirement Statement:** "I changed my dashboard. No, you're not doing that. So then what I would do is I create a dashboard for them, publish it, and they can't change it." Managers need to publish locked dashboards to their teams, preventing user customization while maintaining option for personal Home dashboard.

**Implementation Approach:** ACCOMMODATE - NetSuite's standard role-based publishing will be enhanced with lock-down configuration to prevent users from modifying published team dashboards. Department managers will have authority to publish and control team dashboard content.

#### REQ-004: Build Orion-Enhanced Dashboard Components for Improved Aesthetics (ALIGNS)
**Business Value:** Creates engaging daily work environment, improving user adoption and satisfaction.

**Requirement Statement:** Dashboard should be "the home you're living in all day - should look good, you feel good about where you're living." Modern, professional appearance matters for daily adoption.

**Implementation Approach:** ALIGNS - Orion's enhanced dashboard components with improved visual design and modern styling provide superior aesthetics to standard NetSuite dashboards out-of-the-box.

#### REQ-005: Create Department-Specific Dashboards on Role Centers (ALIGNS)
**Business Value:** Provides role-appropriate data access and reduces cognitive load by showing only relevant information for each user's responsibilities.

**Requirement Statement:** Each process area needs dedicated dashboard center: Finance Center (CFO/finance team), Sales Center (pipeline, opportunities, scorecards), Pre-Quote Center, Order Management Center (Backlog 360, Bookings 360), Operations Center (PM workload, resource utilization).

**Implementation Approach:** ALIGNS - NetSuite's standard role center architecture enables this natively. Each center will contain process-area-specific dashboards with KPIs, charts, saved searches, and drill-down capabilities.

#### REQ-006: Implement Reminders Portlet as Daily Work Driver (ALIGNS)
**Business Value:** Eliminates daily guessing about priorities. Users start each morning with clear, actionable work list, improving productivity and reducing context-switching.

**Requirement Statement:** "This is all the work that I have to work off of. Like it shouldn't, you shouldn't have to guess." Reminders portlet will display saved searches showing bills to pay, tasks to complete, acknowledgements to review, period close checklist items, opportunities needing follow-up.

**Implementation Approach:** ALIGNS - NetSuite's native reminders portlet will be configured with department-specific and individual saved searches, displayed prominently on each role center as the primary daily work driver.

#### REQ-007: Enable Both Departmental and Individual Reminders Portlets (ALIGNS)
**Business Value:** Allows flexibility for teams to view collective reminders (bills for finance team to collectively address) while individuals see personal priorities.

**Requirement Statement:** Reminders portlet can be scoped to individual users or entire departments, depending on process area needs. Finance team may need departmental reminders for month-end close activities.

**Implementation Approach:** ALIGNS - NetSuite natively supports both individual and departmental scope for reminders portlet through saved search filters.

### Orion/NetSuite Solution

Orion/NetSuite provides comprehensive dashboard capabilities that go far beyond simple report display. The solution includes **role-based publishing controls, department-specific role centers, reminders portlet integration, and Orion-enhanced visual components** that transform dashboards into strategic business tools rather than static information displays.

**Dashboard Architecture:** The system supports multiple dashboard levels—a personal Home dashboard for user customization, plus department-specific centers (Finance, Sales, Pre-Quote, Order Management, Operations) where managers publish locked dashboards. This architecture balances user autonomy (personal Home dashboard) with organizational governance (locked team dashboards for consistency).

**Reminders Portlet Integration:** The proven reminders portlet solution displays actionable items at the top of each role center, eliminating daily ambiguity. Users see bills waiting for payment, tasks requiring completion, acknowledgements needing review, and opportunities ready for follow-up. This saved-search-based approach ensures reminders are always current and can be scoped to individual or departmental needs.

**Orion Visual Enhancement:** Orion components provide modern, aesthetically refined dashboard appearance that improves daily user experience. Instead of default NetSuite styling, Orion dashboards feel like a contemporary business application worthy of daily interaction.

**Lock-Down and Control:** Published dashboards are read-only to prevent unauthorized customization. Managers retain full control over what their teams see, ensuring meeting integrity and preventing the "I don't see that" excuse.

### Future State Process

**Weekly Sales Team Meeting - Future State:**
1. All team members receive identical published dashboard showing current pipeline, opportunities by stage, performance metrics
2. Manager reviews dashboard with team - everyone sees same data
3. Discussion focuses on strategy and action items rather than data reconciliation
4. Decisions made confidently with accountability clear
5. Follow-up assignments documented inline with drill-down to records

**Monthly Financial Review - Future State:**
1. Finance lead opens NetSuite financial dashboard in real-time
2. Walks through income statement, balance sheet, trial balance with Lorraine and Mark
3. Executive asks "Why is AR past 90 days so high?" - Finance lead clicks through saved search, drills to invoice detail
4. Root cause identified immediately - collections task assigned to sales rep from meeting
5. No follow-up emails needed - decisions actionable in real-time

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Evidence |
|--------|-------------|---------------------------|----------|----------|
| REQ-003 | Role-based dashboard publishing with lock-down | NetSuite role-based publishing + custom lock-down configuration | ACCOMMODATE | "I create a dashboard for them, publish it, and they can't change it" |
| REQ-004 | Orion-enhanced dashboard components | Orion visual components, modern styling, improved aesthetics | ALIGNS | "The home you're living in all day - should look good" |
| REQ-005 | Department-specific dashboards on role centers | NetSuite role centers (Finance, Sales, Order Mgmt, Pre-Quote, Operations) | ALIGNS | "You can have a dashboard on each one of these tabs...process specific" |
| REQ-006 | Reminders portlet as daily work driver | NetSuite reminders portlet with saved searches | ALIGNS | "This reminders portlet is key...all the work that I have to work off of" |
| REQ-007 | Individual and departmental reminders portlets | NetSuite scope configuration - individual or department | ALIGNS | "Either one. Yep." (individual or departmental) |

### Implementation Approach

**Dashboard Strategy will be used:**
- Role-based publishing will be configured for all managers
- Lock-down will be applied to team dashboards to ensure consistency
- Personal Home dashboard will remain customizable for individual preference
- Orion-enhanced components will be applied to all dashboards for modern appearance
- Department-specific role centers will be created for Finance, Sales, Pre-Quote, Order Management, Operations
- Reminders portlet will be positioned as primary daily work view on each role center
- Reminders portlets will be configured for both individual and departmental scope based on process area needs

---

## Section 2: Official Reports & Data Governance

### Current State Process

**Problem: "Mark's Version, Matt's Version, Kip's Version"**

KBM Hoag currently has a critical data governance problem where multiple team members create similar reports with different criteria, resulting in conflicting numbers and widespread distrust of reporting. The same "revenue report" might be written "four or five different ways" depending on whether taxes are included, how discounts are applied, and what date ranges are used. This fundamental problem—described as "singing from different songbooks"—undermines organizational confidence in decision-making data.

**Specific Examples:**
- Booking reports exist in "Director's tab in shared folder" showing YTD performance by sales rep
- Financial reports manually compiled for executive review from multiple source documents
- Sales goals in Excel distributed weekly
- Google Sheets used extensively for reporting outside ERP system
- No central authority designates which report is "official"

**Consequences:**
- "People don't trust the reporting"
- Time wasted reconciling different versions
- Inconsistent business decisions based on conflicting data
- New employees create yet another version instead of using standard
- Decision meetings derailed by "we don't see the same numbers"

### Your Business Requirements

#### REQ-008: Establish "Official" Report Designation with GSI/Orion Prefix (ADAPT)
**Business Value:** Creates single source of truth, builds organizational confidence in reporting, reduces time spent reconciling data versions.

**Requirement Statement:** "We prefix our saved search, the ones that we create, and then we also sometimes will nominate something as being like an official saved search." All implementation-created reports will carry GSI/Orion prefix, clearly distinguishing them from user-created ad-hoc searches. Specific reports will be designated as "official" for department-wide use.

**Implementation Approach:** ADAPT - This requires organizational process change and naming discipline, not system customization. NetSuite saved search capabilities are used with GSI/Orion naming convention applied by implementation team. User adoption of official reports represents business process adaptation.

#### REQ-009: Implement Public/Private Saved Search Controls (ALIGNS)
**Business Value:** Reduces clutter in report listings, prevents confusion between official and personal exploration searches, enables users to create ad-hoc analyses without cluttering team views.

**Requirement Statement:** "If you're going to make your own search, make it public [or] no one else needs to see that." Users should create personal searches as Private (personal only), while shared searches should be Public (department-visible). Official searches remain visibly branded with GSI/Orion prefix.

**Implementation Approach:** ALIGNS - NetSuite native saved search visibility controls support Public, Private, and role-based scoping. This will be configured at go-live with training on appropriate usage.

#### REQ-010: Create Standardized Report Criteria and Interpretation Documentation (ADAPT)
**Business Value:** Ensures all users interpret metrics consistently, eliminates misunderstandings about what "revenue" means, provides reference for new employees.

**Requirement Statement:** Each official report will include documentation explaining exactly what is included/excluded: Are taxes included in revenue? Discounts before or after? What date range? What status includes in forecast? This answers the "there's so many different ways to write that" problem.

**Implementation Approach:** ADAPT - Requires business process documentation creation and maintenance. NetSuite capabilities are used; the adaptation is documenting and communicating criteria consistently across the organization.

### Orion/NetSuite Solution

Orion/NetSuite provides a **comprehensive governance framework for official reporting** that has successfully transformed organizations' data trust and decision-making quality. The solution uses NetSuite's powerful saved search capabilities combined with clear naming conventions, visibility controls, and standardized interpretation documentation to establish the "single source of truth" that KBM Hoag needs.

**Official Report Strategy:** Rather than creating report chaos, implementation will establish a curated set of **"official" reports prefixed with GSI/Orion** that become the system-of-record for each business metric. These official reports combine NetSuite's 400+ standard reports (customized for KBM Hoag needs) with custom-built saved searches for operational metrics. Each official report will be locked (published) and read-only for most users, preventing accidental modification.

**Naming Convention Power:** The simple GSI/Orion prefix immediately signals to all users "this is the official version." When a user searches for "Revenue Report," they see: "GSI/Orion: Revenue Report - YTD" (official) alongside "Mark's Revenue Report - Experimental" (personal). The prefix becomes a trust indicator.

**Documentation Integration:** Each official report will link to standardized interpretation documentation answering the common questions: What is included? What date range? How are taxes/discounts handled? What status qualifies as "booked"? This documentation ensures the entire organization is "singing from the same songbook" with shared understanding of metric definitions.

**Visibility Controls:** Personal searches remain Private, reducing clutter and anxiety about cluttering the system. Official searches are Public to department/role, visible to all users who need them. This transparency builds confidence.

### Future State Process

**Finding and Using Official Reports - Future State:**
1. User needs financial data - searches for "Revenue"
2. Results show: "GSI/Orion: Revenue Report - YTD" with documentation link
3. User clicks report - opens standardized official revenue report
4. User reads interpretation guide explaining: Includes all invoice amounts, excludes discounts applied, requires Status="Booked", date range is calendar year
5. User sees data with confidence - everyone in organization seeing same revenue definition
6. User trusts the number - "singing from same songbook"

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Evidence |
|--------|-------------|---------------------------|----------|----------|
| REQ-008 | Official report designation with GSI/Orion prefix | NetSuite saved search naming + implementation discipline | ADAPT | "We prefix our saved search...nominate something as being like an official saved search" |
| REQ-009 | Public/private saved search controls | NetSuite saved search visibility settings | ALIGNS | "If you're going to make your own search, make it public [or] no one else needs to see that" |
| REQ-010 | Standardized report criteria documentation | Documentation creation and maintenance process | ADAPT | "I want a revenue report for this time frame...can be written four or five different ways" |

### Implementation Approach

**Governance and Standardization will be used:**
- GSI/Orion prefix will be consistently applied to all implementation-created reports
- Official reports will be designated and locked to read-only status for most users
- Interpretation documentation will be created for each official report during implementation
- Public/Private saved search controls will be configured with training on appropriate usage
- Change control process will be established for official report modifications (approval required before changes)
- Users will be trained on official report adoption philosophy - "singing from same songbook"
- Informal "personal" searches encouraged as Private to support exploration while maintaining governance

---

## Section 3: Real-Time Reporting & Analytics

### Current State Process

**Problem: Manual, Fragmented, Aged Reporting**

KBM Hoag currently relies heavily on manual Excel and Google Sheets reporting across all departments. Financial reporting requires manual compilation of multiple reports into email packages for executive review. Sales goals exist in Excel spreadsheets distributed weekly. Google Sheets are used extensively for reporting functions that should be in the ERP system, creating data age and integration challenges.

Monthly financial reviews, when executives cannot meet in person, are delayed by email transmission of static packages, making drill-down investigation impossible and preventing real-time decision-making during meetings.

**Specific Challenges:**
- Over 400+ report opportunities in NetSuite underutilized
- As-of-date historical reporting not used (executives cannot get period-end snapshots)
- Workbook analytics not leveraged for pivot table analysis
- Saved searches not used for operational metrics and drill-down
- No SuiteQL access for technical users requiring complex queries

### Your Business Requirements

#### REQ-001: Use NetSuite Native BI Tools as Primary Platform (ALIGNS)
**Business Value:** Consolidates reporting into single system with real-time data, eliminates data duplication across Excel/Google Sheets/ERP, improves data freshness and decision quality.

**Requirement Statement:** NetSuite's comprehensive BI tool suite (dashboards, saved searches, standard reports, workbook analytics, SuiteQL) becomes the primary reporting platform. Excel and Google Sheets move from reporting to ad-hoc analysis only.

**Implementation Approach:** ALIGNS - NetSuite native BI tools are proven, standard functionality ready for immediate use. This represents user process adaptation from Excel-centric to system-centric reporting, not system customization.

#### REQ-002: Power BI Remains Optional for Aged Data Analysis with Live Connection (ADAPT)
**Business Value:** Allows continued use of Power BI if organization has deep investment, while protecting against data aging through live connection requirement.

**Requirement Statement:** Power BI can be retained if live connection to NetSuite is implemented. If used without live connection, users must accept that data becomes aged (historical snapshots only). Standard guidance: use NetSuite native tools first, Power BI only if specific business case justifies.

**Implementation Approach:** ADAPT - This is a business decision about BI platform strategy. If Power BI is retained, technical adaptation required for live connection implementation. If not retained, this requirement becomes moot.

#### REQ-013: Utilize 400+ Standard NetSuite Reports with Customization (ALIGNS)
**Business Value:** Provides ready-made reporting foundation for all common business needs without building from scratch.

**Requirement Statement:** NetSuite ships with 400+ pre-built reports including Income Statement, Balance Sheet, Trial Balance, Cash Flow, AR/AP Aging, Receive Not Invoiced, Order Status, Backlog, Bookings, Pipeline, and hundreds more. Each can be customized for KBM Hoag's specific needs without custom development.

**Implementation Approach:** ALIGNS - These standard reports will be customized during implementation configuration for KBM Hoag's specific requirements (date ranges, filters, columns, formatting). No custom development required.

#### REQ-014: Implement As-Of-Date Reporting Capability for Historical Snapshots (ALIGNS)
**Business Value:** Enables period-end financial snapshots and historical comparison. "What was my balance sheet as of September 1st?" becomes answerable, supporting audit, trend analysis, and executive review.

**Requirement Statement:** "Reporting in NetSuite is unique because you can get the as of dates for those reports. So like what was my balance sheet as of September 1st. You can get that."

**Implementation Approach:** ALIGNS - NetSuite's native as-of-date reporting is standard functionality. Users will be trained on when and how to use historical date parameters.

#### REQ-015: Enable Workbook Analytics for Pivot Tables and Charts (ALIGNS)
**Business Value:** Provides Excel-like pivot table and chart creation within NetSuite, reducing dependency on Excel for analysis while maintaining real-time data.

**Requirement Statement:** "Workbook analytics...think of like Excel. It's called workbook analytics. So pivot table charts, you can build those out inside NetSuite." Users need Excel-like analytical flexibility without exporting to Excel.

**Implementation Approach:** ALIGNS - NetSuite's native workbook analytics module will be configured and users trained on pivot table and chart creation.

#### REQ-016: Configure SuiteQL Access for Technical Users (ALIGNS)
**Business Value:** Enables technical users (like Kipp) to write custom SQL queries for complex reporting beyond standard tools' capability, supporting advanced analysis and performance-critical queries.

**Requirement Statement:** "SuiteQL, which is NetSuite's kind of own version of SQL. You can, so that means you can write queries." Technical users need direct database query access for specialized reporting.

**Implementation Approach:** ALIGNS - NetSuite's native SuiteQL module will be granted to identified technical users (Kipp and others) with proper query governance and performance monitoring.

#### REQ-024: Enable Scheduled Report Distribution via Email (ALIGNS)
**Business Value:** Automates routine report generation and distribution, eliminating manual packaging effort and ensuring timely delivery to executives and stakeholders.

**Requirement Statement:** Reports can be scheduled to generate automatically (daily, weekly, monthly) and distributed via email in PDF or Excel format. Executive financial packages can be automated instead of manually compiled.

**Implementation Approach:** ALIGNS - NetSuite's native scheduled report distribution will be configured for high-frequency reports (executive financial packages, department dashboards exported for review).

#### REQ-025: Support Executive Financial Review Presentations from System (ALIGNS)
**Business Value:** Enables real-time financial presentation with drill-down capability instead of static package review. "Why is AR high?" can be answered immediately during meeting rather than requiring follow-up analysis.

**Requirement Statement:** Lorraine and Mark should be able to present financial dashboards directly from NetSuite during month-end review, drilling down from summary (income statement) to transaction detail (specific invoice) without exporting to Excel first.

**Implementation Approach:** ALIGNS - NetSuite's native dashboard and drill-down capabilities enable this. Executive training on navigation and drill-down will be provided.

### Orion/NetSuite Solution

Orion/NetSuite provides a **complete real-time reporting ecosystem** that fundamentally changes how organizations make decisions. Instead of waiting for manual report compilation, teams access live dashboards that update throughout the day, drill down from summary to transaction detail instantly, and create ad-hoc analyses without IT support.

**Four-Part Reporting Architecture:**

**1. Standard Reports (400+):** NetSuite includes Income Statement, Balance Sheet, Trial Balance, Cash Flow, AR/AP Aging, Receive Not Invoiced, Order Status, Backlog, Bookings, Pipeline, and hundreds more—all proven by thousands of customers. During implementation, these will be customized for KBM Hoag's needs: date ranges, columns, filters, subtotals. No custom development required; just configuration.

**2. Saved Searches (Custom Queries):** For operational metrics not covered by standard reports—"which sales reps exceeded quota," "what projects are over budget," "which acknowledgements haven't been sent"—saved searches provide instant answers. These combine NetSuite record data with custom filters and sorting, and importantly, can include inline-edit functionality for rapid data correction.

**3. Workbook Analytics (Pivot Tables/Charts):** Users who need Excel-like analytical flexibility can build pivot tables and charts directly in NetSuite. Instead of exporting data to Excel (where data ages immediately), users filter, slice, pivot, and visualize using real-time system data. Charts can be pinned to dashboards for executive visibility.

**4. SuiteQL (Advanced Queries):** For technical users like Kipp, SuiteQL provides SQL-like query access to NetSuite's database, enabling complex joins, advanced calculations, and performance-optimized queries that would be impossible through the user interface.

**Real-Time Executive Presentations:** The game-changer is dashboard-based executive review. Instead of Finance team emailing static packages, they present the NetSuite financial dashboard in real-time. Lorraine and Mark see current Income Statement, Balance Sheet, Trial Balance. When Mark asks "Why is AR past 90 days so high?" the Finance lead clicks the AR report, sees the aging detail, clicks a specific invoice, and immediately identifies the issue—all during the meeting. Follow-up email is unnecessary; action items are assigned and tracked in NetSuite right then.

**Scheduled Report Automation:** Routine reports (weekly sales goals, monthly financial packages, daily operational summaries) can be automated to generate and email at scheduled times, eliminating manual packaging effort.

### Future State Process

**Financial Analysis - Future State:**
1. Finance team opens NetSuite financial dashboard
2. Income statement shows current year vs. prior year side-by-side
3. Expense category appears high - click to drill to expense detail report
4. Specific vendor invoice appears excessive - click to view transaction
5. Mistake identified (duplicate invoice) - correct inline in saved search
6. Real-time data updated automatically for all dashboards

**Executive Review - Future State:**
1. Lorraine and Mark schedule month-end financial review
2. Finance lead shares screen showing NetSuite financial dashboard
3. Walk through Income Statement, Balance Sheet, Trial Balance with real-time data
4. "AR looks elevated" - click AR aging report to see past 90-day detail
5. "Why is that customer past due?" - drill to invoice to see issue
6. Discussion identifies root cause - assign collection task to sales rep
7. Meeting concludes with action items assigned and tracked in system

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Evidence |
|--------|-------------|---------------------------|----------|----------|
| REQ-001 | NetSuite native BI tools as primary platform | NetSuite BI tools, dashboards, saved searches, workbook analytics, SuiteQL | ALIGNS | "Just to kind of give you the highlights of what's available to you inside NetSuite" |
| REQ-002 | Power BI optional with live connection | Power BI connector with live NetSuite connection | ADAPT | "If you love Power BI, use it...if you have a live connection" |
| REQ-013 | Utilize 400+ standard reports with customization | NetSuite standard reports library, customization | ALIGNS | "NetSuite ships with over 400 standard reports...every single one can be customized" |
| REQ-014 | As-of-date reporting capability | NetSuite as-of-date report parameter | ALIGNS | "What was my balance sheet as of September 1st. You can get that." |
| REQ-015 | Workbook analytics for pivot tables/charts | NetSuite workbook analytics module | ALIGNS | "Like Excel...pivot table charts, you can build those out inside NetSuite" |
| REQ-016 | SuiteQL access for technical users | NetSuite SuiteQL module with permissions | ALIGNS | "NetSuite's kind of own version of SQL...you can write queries" |
| REQ-024 | Scheduled report distribution via email | NetSuite scheduled reports with email distribution | ALIGNS | "Can schedule reports and email automatically" |
| REQ-025 | Executive presentations from system | NetSuite dashboards with drill-down capability | ALIGNS | "I would just pull up the income statement...walk through it...drill down" |

### Implementation Approach

**Real-Time Reporting capabilities will be used:**
- 400+ standard NetSuite reports will be customized for KBM Hoag needs during implementation
- As-of-date reporting will be enabled for financial period comparisons and audit support
- Workbook analytics will be configured for users needing Excel-like pivot table/chart capability
- SuiteQL access will be granted to identified technical users (Kipp and others) with query governance
- Scheduled report distribution will be configured for routine automated reports
- Executive dashboards will be designed for real-time presentation with drill-down capability
- Users will be trained on how to navigate, filter, drill-down, and explore data without requiring Excel exports

---

## Section 4: Saved Searches & Operational Efficiency

### Current State Process

**Problem: Record-by-Record, Manual Data Updates**

Currently, updating multiple opportunity statuses or acknowledging multiple orders requires opening each record individually, updating the status field, saving, and closing—then repeating for the next record. A sales manager might spend 30-45 minutes updating 20-30 opportunity statuses manually. Finance team members manually extract data for analysis instead of using system-provided search results. There's no visual highlighting to quickly identify overdue items.

### Your Business Requirements

#### REQ-017: Enable Inline Editing from Saved Searches (ALIGNS)
**Business Value:** Reduces time spent opening/closing records repeatedly, maintaining context while updating multiple records, improves productivity for status-update-heavy workflows.

**Requirement Statement:** "Whenever you see a pencil here, that means you can edit right here without having to go in and edit the whole record." Opportunity status can be changed inline from saved search view. Tasks can be marked complete without opening. Acknowledgements can be updated without navigating to full record.

**Implementation Approach:** ALIGNS - NetSuite's native inline-edit capability on saved searches will be enabled for appropriate fields (opportunity status, task status, acknowledgement status, etc.) during configuration.

#### REQ-018: Implement Highlighting Rules for Visual Indicators (ALIGNS)
**Business Value:** Provides visual priority signaling, enabling users to quickly identify high-priority items without scanning entire list.

**Requirement Statement:** Conditional formatting rules apply colors to highlight critical situations: "If the expected close date is before today that's a problem" - highlight in red. Visual indicators enable quick scanning to identify issues needing attention.

**Implementation Approach:** ALIGNS - NetSuite's native highlighting rules on saved searches will be configured with appropriate visual indicators (red for overdue, yellow for approaching deadline, green for on-track, etc.).

#### REQ-019: Enable Mass Update Functionality (ALIGNS)
**Business Value:** Allows bulk operations for large-scale status changes or field updates, dramatically reducing manual processing time for routine updates.

**Requirement Statement:** "You can, in a safe search, do a mass update." When multiple records need same update (change status for entire product line, update assignment for department), mass update completes operation in seconds rather than individual record edits.

**Implementation Approach:** ALIGNS - NetSuite's native mass update functionality on saved searches will be configured and users trained on appropriate usage with safeguards against accidental bulk changes.

### Orion/NetSuite Solution

Orion/NetSuite transforms operational efficiency through **saved search capabilities that serve as command centers for data management**. Instead of inefficient record-by-record editing, teams use saved searches as focused work surfaces where they can see context (related fields, status, priority), update fields inline without losing context, apply visual highlighting to identify priorities, and perform bulk operations for efficiency.

**Saved Search Power:** A saved search displays records in table format with multiple columns showing context. Sales manager views opportunity list with columns: Opportunity, Stage, Expected Close Date, Amount, Probability, Sales Rep. From this single view, entire context is visible while making decisions.

**Inline Editing:** When a status needs updating, instead of clicking the record (opens full record, hides context), clicking the pencil icon on the Status field shows a dropdown allowing instant update. The change saves immediately and the view stays on the list—next status update is one click away. A sales manager can update 20 opportunity statuses in 5-10 minutes instead of 30-45 minutes.

**Highlighting Rules:** Visual rules immediately flag critical items. "Expected Close before Today" shows in red—no scanning required. "Days Overdue" shows different colors by severity. These visual cues enable rapid priority identification and workflow routing.

**Mass Update:** For large operations, mass update performs field changes across multiple records simultaneously. Change all "pending acknowledgement" orders in a product line to "acknowledgement sent"? One mass update operation completes in seconds.

### Future State Process

**Updating Opportunity Status - Future State:**
1. Sales manager opens "Opportunity List" saved search
2. Table displays: Opportunity, Stage, Expected Close, Amount, Probability, Sales Rep
3. Red highlighting shows opportunities with expected close date before today
4. Sales manager clicks pencil on first opportunity's Stage field
5. Dropdown appears - selects new stage
6. Auto-saves, moves to next opportunity
7. Updates 20 opportunities in 8 minutes (vs. 35+ minutes opening each record)
8. Context maintained throughout - sees all related information while updating

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Evidence |
|--------|-------------|---------------------------|----------|----------|
| REQ-017 | Inline editing from saved searches | NetSuite saved search inline edit capability | ALIGNS | "Whenever you see a pencil here, that means you can edit right here" |
| REQ-018 | Highlighting rules for visual indicators | NetSuite saved search highlighting rules | ALIGNS | "If the expected close date is before today that's a problem...highlight" |
| REQ-019 | Mass update functionality | NetSuite saved search mass update capability | ALIGNS | "You can, in a safe search, do a mass update" |

### Implementation Approach

**Saved Search Optimization will be used:**
- Inline editing will be enabled for status fields and other frequently-updated fields across operational saved searches
- Highlighting rules will be configured to visually identify priorities: red for critical, yellow for approaching deadline, green for on-track
- Mass update capability will be explained with training on safeguards to prevent accidental bulk changes
- Users will be trained on when inline-edit is appropriate vs. when full record edit is needed (complex changes)

---

## Section 5: Export Security & Data Protection

### Current State Process

**Problem: Uncontrolled Data Export Risk**

Currently, there are "not a lot of control in Core to determine who can export what information." An employee departing to a competitor could export the entire customer list containing sales rep assignments, contact information, and relationship history—creating immediate competitive disadvantage. While this specific incident hasn't occurred yet, the risk is acknowledged as significant.

### Your Business Requirements

#### REQ-011: Implement Role-Based Export Permissions (All-or-Nothing) (ALIGNS)
**Business Value:** Provides basic control mechanism to prevent data exfiltration, especially protecting against departing employee risks. Role-based permissions offer baseline security without completely disabling export capability.

**Requirement Statement:** "For a given role there is a report export [permission] and that's what actually shows the button for like PDF and Excel and everything. You can turn that off on a role basis." Each role should have export enabled/disabled as all-or-nothing: either users in that role can export anything, or cannot export anything.

**Implementation Approach:** ALIGNS - NetSuite's native role-based export permission (Boolean flag per role) will be configured during setup. Note: NetSuite limitation means cannot restrict specific reports per role—only all-or-nothing by role.

#### REQ-012: Configure Notification System for Large Data Exports (>50MB) (ACCOMMODATE)
**Business Value:** Provides visibility into large data extracts, enabling management intervention if suspicious activity detected. While not preventive, alerts provide awareness and opportunity to investigate.

**Requirement Statement:** "Trigger system to alert if more than 50 megabytes of data are being downloaded." When user exports more than threshold (proposed 50MB), system triggers notification to IT Security and Department Head, allowing investigation of potentially suspicious activity.

**Implementation Approach:** ACCOMMODATE - Custom workflow/notification engine will be designed to monitor export events and trigger alerts when data volume exceeds threshold. This requires custom development to add notification logic to export process.

### Orion/NetSuite Solution

Orion/NetSuite provides **multi-layered data protection** through role-based permissions, export audit trails, and custom monitoring workflows. While no system can completely prevent data extraction (users can copy-paste data visible on screen), the combination of role-based controls and monitoring creates significant friction that prevents casual or unintentional data exfiltration.

**Role-Based Export Control:** NetSuite's role permission for "Export to PDF" and "Export to Excel" acts as the primary gate. If a role has this permission enabled, users in that role see export buttons on all reports and can export. If disabled, export buttons disappear entirely, preventing accidental or casual export.

**Export Audit Trail:** All exports are logged, creating audit trail for forensic investigation if needed. "Who exported what data and when?" becomes answerable from audit logs.

**Large Export Notification:** Custom workflow monitors export events and triggers alerts when data volume exceeds threshold (50MB suggested). Instead of disabling all exports (which would impact legitimate business uses like "export order list for external analysis"), system allows normal exports but alerts security team to unusually large extracts. Security lead can then investigate: "Why did this user just export 500MB of customer data at 11 PM on Friday?"

**Practical Reality Check:** As Marcus noted, "if they don't have the ability to export it, they can technically, because it's browser-based, just highlight everything, Control-C, Control-V, and Excel, and they got it." Perfect security is impossible. The goal is reasonable controls that prevent casual extraction while allowing legitimate use.

### Future State Process

**Export Scenario 1 - Normal Usage:**
1. Finance analyst needs to analyze AR data in Excel
2. Clicks "Export to Excel" on AR Aging report
3. Report exports successfully (10MB) to desktop
4. No alert triggered - within normal parameters
5. Analyst performs analysis offline, no security concern

**Export Scenario 2 - Large Extract (Suspicious):**
1. Employee scheduled to depart next week attempts large export
2. Clicks export on Customer List - 500MB data file
3. Export happens BUT triggers large-export notification
4. Alert goes to IT Security Lead and Department Head: "User [Name] exported 500MB on [Date/Time]"
5. IT investigates: "Why did departing employee need entire customer list?"
6. Additional security measures triggered if appropriate

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Evidence |
|--------|-------------|---------------------------|----------|----------|
| REQ-011 | Role-based export permissions (all-or-nothing) | NetSuite role export permission setting | ALIGNS | "For a given role there is a report export [permission]...you can turn that off on a role basis" |
| REQ-012 | Notification for large data exports (>50MB) | Custom workflow for export monitoring | ACCOMMODATE | "Trigger system to alert if more than 50 megabytes of data are being downloaded" |

### Implementation Approach

**Data Protection and Export Security will be used:**
- Role-based export permissions will be configured: most roles enabled, sensitive roles (departing employees, contractors) disabled
- Export audit trail will provide forensic capability if needed
- Custom notification workflow will be designed to alert when exports exceed 50MB threshold
- IT Security Lead and Department Heads will receive alerts for large exports
- Investigation and response process will be established (defined in Export Security Policy)
- User training will explain export limitations and security rationale

---

## Section 6: Organizational Structure & Manager Hierarchy

### Current State Process

**Problem: "Me and My Team" Filters Don't Work**

A significant frustration from current system (Core) is that "me and my team" filters allegedly should work based on manager assignments but consistently fail: "They do allegedly have this hierarchy of permissions, roles and permissions, and, like, this is the manager. They report to that manager, and that manager is supposed to see everyone, and it doesn't. I've never gotten that."

This broken functionality prevents managers from seeing their direct reports' data on dashboards, scorecards, or analytics without manual filtering or workarounds.

### Your Business Requirements

#### REQ-022: Implement "Me Only" and "Me and My Team" Filters (ALIGNS)
**Business Value:** Enables managers to automatically see their team's performance data without manual filtering. Enables individuals to focus on their own metrics without being overwhelmed by organization-wide data.

**Requirement Statement:** Filter scope should include: "Me Only" (individual sees only own data, like sales rep seeing only their opportunities), "Me and My Team" (manager sees direct reports, like sales manager seeing all rep opportunities), "Specific People" (select individuals manually), "Department" (all department members).

**Implementation Approach:** ALIGNS - NetSuite's native employee hierarchy filters will be configured based on proper org structure setup in REQ-023.

#### REQ-023: Configure Proper Manager Hierarchy for Filter Functionality (ALIGNS)
**Business Value:** Makes all hierarchy-dependent features work correctly (manager filters, manager scorecards, team dashboards, subordinate visibility). Fixes the Core frustration where org structure supposedly didn't work.

**Requirement Statement:** "You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works. Good." Each employee record must have correct manager assigned. Manager hierarchy must be properly configured during setup and maintained by HR.

**Implementation Approach:** ALIGNS - During implementation, current org structure will be documented and configured in NetSuite employee records. Manager assignments will be accurate and maintained going forward through HR/HRIS processes.

### Orion/NetSuite Solution

Orion/NetSuite delivers **reliable organizational hierarchy that actually works**, unlike the frustrating broken behavior in Core. The difference is simple: if org structure is configured correctly, hierarchy filters work flawlessly. NetSuite's approach is proven by thousands of organizations using similar filter patterns.

**Manager Assignments:** Each employee record includes a "Manager" field. This single field creates the entire hierarchy when configured properly. Manager rollups, team visibility, and filter scoping all derive from this manager assignment.

**Hierarchy-Based Filters:** Once org structure is in place, "me and my team" automatically shows manager the correct subset: their direct reports only (not entire organization, not unrelated departments, just their direct reports).

**Why It Works:** Unlike Core, NetSuite doesn't have known issues with org structure configuration. The system has been proven thousands of times by large enterprise implementations.

### Future State Process

**Scorecard Viewing - Future State:**
1. Sales rep opens their personal dashboard
2. Scorecard shows: "Me Only" view - their revenue, GP, pipeline, deals closed
3. Sales manager opens same dashboard system
4. Same scorecard automatically shows "Me and My Team" view - all direct reports' metrics
5. Manager can click individual rep to drill to their detailed scorecard
6. Org structure maintained by HR automatically filters correctly

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Evidence |
|--------|-------------|---------------------------|----------|----------|
| REQ-022 | "Me only" and "me and my team" filters | NetSuite employee hierarchy filters | ALIGNS | Discussion of filter scoping options |
| REQ-023 | Configure proper manager hierarchy | NetSuite employee record manager assignment | ALIGNS | "You have to have the right managers assigned...if we set that up, it actually works" |

### Implementation Approach

**Organizational Structure configuration will be used:**
- Current org structure will be documented and reviewed with HR/Finance
- Manager assignments will be configured accurately in all employee records during implementation
- Hierarchy filters ("me only," "me and my team") will be applied to dashboards, scorecards, and workbook analytics
- HR will be trained on maintaining manager assignments through standard HRIS processes
- Testing will validate filters work correctly pre-go-live
- Ongoing maintenance will be HR responsibility to keep org structure current

---

## Section 7: Department-Specific Reporting

### Current State Process

**Problem: Fragmented Process Area Reporting**

Each department (Finance, Sales, Order Management, Operations, Pre-Quote) currently maintains separate reporting approaches:
- **Finance**: Manual compilation of Excel reports and Google Sheets analyses
- **Sales**: Booking reports in shared folder, Excel-based goals
- **Order Management**: Multiple tools tracking backlog and bookings
- **Operations**: PM workload visibility fragmented across systems
- **Pre-Quote**: RFP tracking in external systems

No comprehensive dashboards exist that bring together "everything you could ever imagine" for a process area in single unified view.

### Your Business Requirements

#### REQ-026: Build Comprehensive Backlog 360 Dashboard (ACCOMMODATE)
**Business Value:** Single comprehensive dashboard for all backlog management—eliminates context-switching between multiple tools/reports. Provides complete backlog visibility: by line item, by order, by status, by customer, trends.

**Requirement Statement:** "We're building on a backlog 360 dashboard, so it's just one dashboard that has everything you could ever imagine for backlog in one place." Backlog status visibility across entire organization without toggling between multiple reports.

**Implementation Approach:** ACCOMMODATE - Custom comprehensive dashboard will be designed during implementation combining: backlog by line, backlog by order, unfilled orders, customer PO status, acknowledgement tracking, fulfillment status. Detailed specifications will be developed during dashboard design sessions.

#### REQ-027: Build Comprehensive Bookings 360 Dashboard (ACCOMMODATE)
**Business Value:** Similar to Backlog 360—comprehensive bookings visibility in single dashboard. Historical booking trends, bookings by rep, by customer, by product.

**Requirement Statement:** Comprehensive bookings dashboard similar to Backlog 360 structure. Replaces current booking report in "Director's tab in shared folder" with system-based, real-time dashboard.

**Implementation Approach:** ACCOMMODATE - Custom comprehensive dashboard will be designed during implementation. Specifications to be developed based on current booking report requirements.

### Orion/NetSuite Solution

Orion/NetSuite provides **comprehensive, unified dashboards for each process area** that consolidate information fragmented across current tools. Instead of checking four different reports to understand backlog status, users see Backlog 360 dashboard showing: current backlog by customer (summary), backlog by line item (detail), unfilled orders, acknowledgement status, fulfillment progress, and historical trends—all in one screen.

**360 Dashboard Architecture:** The "360" concept means: complete visibility across the entire process. Backlog 360 isn't just "backlog value"—it's backlog combined with acknowledgement status, customer PO status, fulfillment progress, and related order information. When order management team opens Backlog 360, they see everything needed to understand backlog health at a glance.

**Consolidation Benefit:** Currently, discovering that an order's backlog is high requires checking: original backlog report (status), acknowledgement system (is ack sent?), fulfillment system (when does customer want delivery?), customer PO system (what's authorized amount?). With 360 dashboard, all this information is in one screen with drill-down to detail.

**Bookings 360 Replacement:** Current booking report (revenue, GP by sales rep, distributed manually) becomes Backlog 360 with additional dimensions: historical trends, forecast accuracy, pipeline comparison. Real-time system dashboard replaces manual Excel distribution.

### Future State Process

**Backlog 360 Usage - Future State:**
1. Order Management Lead opens Backlog 360 dashboard each morning
2. KPI summary shows: Total backlog value, fulfilled orders, pending acknowledgements, at-risk orders
3. Drill to "At Risk" orders → sees which customers requesting pull-in dates
4. Drill to specific order → sees current status, next required action, customer PO status
5. Identifies acknowledgements not sent - task assignments created
6. Real-time visibility enables proactive management rather than reactive issue resolution

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Evidence |
|--------|-------------|---------------------------|----------|----------|
| REQ-026 | Comprehensive Backlog 360 dashboard | Custom comprehensive dashboard design | ACCOMMODATE | "We're building on a backlog 360 dashboard...everything you could ever imagine for backlog in one place" |
| REQ-027 | Comprehensive Bookings 360 dashboard | Custom comprehensive dashboard design | ACCOMMODATE | Similar comprehensive structure to Backlog 360 |

### Implementation Approach

**360 Comprehensive Dashboards will be used:**
- Backlog 360 will be designed during implementation with order management team input
- Components will include: backlog summary, by line item detail, fulfillment status, acknowledgement tracking, customer PO status
- Bookings 360 will be designed replacing current manual booking report
- Components will include: current bookings, by sales rep, trends, forecast accuracy, pipeline comparison
- Detailed specifications will be developed during dashboard design workshop sessions
- Additional 360 dashboards (Finance, Operations, Pre-Quote) to be considered post-Phase 1

---

## Section 8: Sales Performance & Scorecards

### Current State Process

**Problem: Manual Scorecard Distribution**

Sales performance tracking currently relies on "booking report" in shared folder showing YTD performance and GP by sales rep. This manual approach means:
- Delayed updates (not real-time)
- Manual Excel distribution required
- Sales reps must request reports from management rather than seeing own performance
- Managers cannot see team performance at a glance
- No drill-down capability—can't investigate why specific rep is underperforming

### Your Business Requirements

#### REQ-020: Create Sales Rep Scorecards for Individual Dashboards (ACCOMMODATE)
**Business Value:** Sales reps see own performance metrics on personal dashboard, enabling self-monitoring without requesting reports. Creates immediate performance visibility and accountability.

**Requirement Statement:** "I would love them to see that on their own dashboard." Each sales rep sees personal scorecard showing: total revenue, total GP, year-to-date performance, period comparison, pipeline value, deals closed. Scorecard auto-updates with real-time data.

**Implementation Approach:** ACCOMMODATE - Custom scorecard component will be designed based on current booking report metrics. Metrics and target definitions will be specified during implementation planning. Configuration required: "me only" filter so rep sees only own data.

#### REQ-021: Build Manager View Scorecards Showing Team Performance (ACCOMMODATE)
**Business Value:** Sales managers see all direct reports' scorecards on single screen, enabling team performance management without scrolling through multiple reports.

**Requirement Statement:** When manager opens same scorecard dashboard, "me and my team" filter automatically shows all direct reports' scorecards. Manager can click individual rep to drill to detailed view. Enables visual team performance comparison and identifies high performers and underperformers immediately.

**Implementation Approach:** ACCOMMODATE - Same scorecard component as REQ-020 but configured with "me and my team" filter. Depends on proper org structure (REQ-023) to work correctly.

### Orion/NetSuite Solution

Orion/NetSuite delivers **sales performance visibility to every team member** through custom-designed scorecards that provide both individual accountability and team visibility. Instead of managers emailing performance reports, scorecards update in real-time and are always available on personal dashboards.

**Scorecard Architecture:** A scorecard is custom dashboard component showing key metrics: Revenue (actual vs. target), Gross Profit (actual vs. target), Number of Deals Closed, Win Rate, Pipeline Value, and trends. Data refreshes real-time from system records.

**"Me Only" Individual View:** Sales rep opens personal dashboard and sees own metrics. Personal accountability is clear: "Here's my revenue to date, here's my GP, here's my pipeline." No need to request report from manager; information is always current and immediately visible.

**"Me and My Team" Manager View:** Manager opens same dashboard component; system automatically shows team member metrics instead of personal metrics (via org structure filter). Manager sees all direct reports' scorecards without additional configuration. Visual comparison enables talent management: "Rep A is ahead of quota, Rep B is behind."

**Drill-Down Capability:** Clicking individual rep's scorecard drills to detailed view showing all related transactions, enabling investigation: "Why is Rep B's GP lower than others?" → Can see if it's pricing issue, deal mix issue, or other factor.

### Future State Process

**Sales Scorecard Usage - Future State:**
1. Sales rep opens personal dashboard each morning
2. Sees scorecard: Revenue YTD $2.1M (Target $2.0M), GP YTD $420K (Target $400K)
3. This week's deals: 3 closed, 2 pending, 5 in negotiation
4. Pipeline value: $1.8M (8 opportunities)
5. Rep immediately sees own performance vs. target - motivating and accountability-oriented

**Manager Perspective - Same Dashboard:**
1. Sales manager opens same scorecard component
2. Sees "Me and My Team" - displays all 8 direct reports' scorecards
3. Visual scan shows: Rep A $2.1M (ahead), Rep B $1.7M (behind), Rep C $2.0M (on target)
4. Identifies Rep B needs coaching or support - makes conversation happen proactively
5. Recognizes Rep A's performance - considers for incentive or promotion

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Evidence |
|--------|-------------|---------------------------|----------|----------|
| REQ-020 | Sales rep scorecards for individual dashboards | Custom scorecard component with "me only" filter | ACCOMMODATE | "I would love them to see that on their own dashboard" |
| REQ-021 | Manager scorecards showing team performance | Custom scorecard component with "me and my team" filter | ACCOMMODATE | "If he was ever managing them on their dashboard, it shows them all of their people" |

### Implementation Approach

**Sales Performance Scorecards will be used:**
- Scorecard metrics will be defined based on current booking report (revenue, GP, YTD performance)
- Additional metrics to be discussed: win rate, pipeline value, deals closed, forecast accuracy
- Target-setting process will be defined (who sets targets, update frequency?)
- Scorecard design mockup will be created during implementation
- Scorecard will be configured with "me only" individual filter and "me and my team" manager filter
- Sales team training will explain scorecard usage and motivation
- Rep access to own data will enable performance self-monitoring

---

## Implementation Considerations

### Dependencies

The following requirements have interdependencies requiring sequenced implementation:

1. **Org Structure Foundation (REQ-023) → Manager Filters (REQ-022)**
   - Cannot configure "me and my team" filters until org structure is configured
   - Manager assignments must be accurate for filters to work
   - Recommend: Configure org structure in Phase 1 before any filter-dependent functionality

2. **Org Structure (REQ-023) → Scorecards (REQ-020, REQ-021)**
   - Scorecard "me and my team" functionality requires working manager hierarchy
   - Recommend: Complete org structure before designing scorecard components

3. **Department Dashboards (REQ-005) → Dashboard Publishing (REQ-003)**
   - Cannot publish dashboards until role centers are created
   - Recommend: Create centers first, then configure publishing and lock-down

4. **Official Reports (REQ-008) → Documentation (REQ-010)**
   - Reports need criteria documentation to achieve standardization goal
   - Recommend: Create official report list first, then documentation follows

5. **Dashboard Design (REQ-005) → Reminders Portlet (REQ-006, REQ-007)**
   - Reminders portlet should be prominent on each role center dashboard
   - Recommend: Design dashboards with reminders portlet placement in mind

### Risks and Mitigation

#### High Risk 1: User Resistance to Locked Dashboards (REQ-003)

**Risk:** Users accustomed to customizing dashboards resist locked published dashboards, perceiving loss of control and autonomy. "I want my dashboard my way" mindset challenges official dashboard approach.

**Mitigation:**
- Communicate clear rationale: Team alignment in weekly meetings requires consistent data
- Allow personal Home dashboard customization to balance control needs
- Demonstrate productivity improvement: "Meetings will be 20 minutes shorter when we're not reconciling different numbers"
- Change management messaging: "You get your own personal dashboard plus guaranteed team consistency"
- Manager enforcement: Managers reinforce importance and model behavior

#### High Risk 2: Continuous Creation of Personal Report Versions (REQ-008)

**Risk:** Despite official report designation and training, users continue creating personal report variations, defeating purpose of "singing from same songbook" governance.

**Mitigation:**
- Make official reports easily discoverable: clear naming, documentation links, featured placement
- Acknowledge personal exploration: allow Private saved searches for personal analysis without judgment
- Manager reinforcement: managers reference official reports, question personal versions
- Measurement: track saved search creation patterns, celebrate adoption of official reports
- Refinement: if official report doesn't meet need, fix it rather than allowing workaround versions

#### High Risk 3: Departing Employee Data Export (REQ-011, REQ-012)

**Risk:** Role-based export permissions may be too permissive (enable export for users who shouldn't have it) or too restrictive (block legitimate business needs). Large export notification is reactive—export already occurred when alert sent.

**Mitigation:**
- Develop clear export security policy: which roles can export, which cannot, exceptions process
- Consider context-specific role variants if needed (same job, different export permissions for senior vs. junior)
- Implement pre-departure protocol: when termination date reaches, disable export for that user
- Notification recipients should have response procedures: investigate immediately if large export detected
- Accept that perfect prevention is impossible—focus on detection and deterrence

#### Medium Risk: Organizational Structure Maintenance (REQ-023)

**Risk:** Org structure configured at go-live but becomes stale if HR doesn't maintain manager assignments. New hires don't have correct managers, promotions don't update managers, departures leave orphaned reports. Filters stop working.

**Mitigation:**
- Establish clear ownership: HR responsible for maintaining employee records including manager assignment
- Provide HR training on manager assignment process during go-live training
- Define update frequency: managers review team assignments quarterly, HR confirms correct
- Implement monitoring: quarterly report of employees without managers or with incorrect managers
- Include in HR processes: new hire onboarding must include manager assignment; promotion process must include manager update

#### Medium Risk: SuiteQL Query Performance (REQ-016)

**Risk:** Technical users with SuiteQL access write inefficient queries that impact system performance. Poorly written SQL can consume resources and slow system for other users.

**Mitigation:**
- Limit SuiteQL access to identified technical users (Kipp and selected others) after training
- Implement query monitoring and review: queries should be reviewed before production use
- Establish query optimization standards: queries running longer than X seconds require review
- Provide SuiteQL training covering best practices and performance optimization
- Consider scheduled query execution instead of real-time for heavy queries

#### Medium Risk: Export Policy Complexity (REQ-011, REQ-012)

**Risk:** All-or-nothing export permission limitation means cannot restrict specific reports. Sales team might need to export order details for analysis but shouldn't export customer list. Current binary choice doesn't match business nuance.

**Mitigation:**
- Develop pragmatic policy: err on side of enabling exports (productivity first), rely on notifications for security
- Use role variants if needed: "Sales Rep" role with export enabled, "Contractor Sales" role with export disabled
- For sensitive roles (departing employees, contractors), disable export entirely
- Monitor large exports closely; investigate anomalies quickly
- Accept that some data extraction risk exists—cannot be eliminated without eliminating legitimate use

### Outstanding Items Requiring Decision

1. **Export Security Policy Definition**
   - Which roles can export? Which roles cannot?
   - Final threshold for large export notifications (50MB proposed)?
   - Who receives large export notifications?
   - Response procedure if suspicious large export detected?
   - **Timeline:** Needs to be defined during implementation planning

2. **Official Reports Definition**
   - What is complete list of official reports by department?
   - Who has authority to designate new official reports?
   - Process for updating official reports (who approves changes)?
   - Change notification to user community process?
   - **Timeline:** Can start post-discovery, before detailed design sessions

3. **Dashboard Design Details**
   - What specific KPIs for each department dashboard?
   - Which roles have locked vs. flexible dashboards?
   - What specific items in reminders portlet by department?
   - Executive dashboard requirements (Lorraine, Mark)?
   - **Timeline:** Needs design workshop sessions per department during implementation

4. **Scorecard Metrics and Targets**
   - Beyond revenue and GP, what metrics should scorecards show?
   - How are targets set? By whom? Update frequency?
   - Design mockup approval needed?
   - Other department scorecards needed besides Sales?
   - **Timeline:** Needs sales leadership input during implementation

5. **Backlog 360 and Bookings 360 Specifications**
   - Detailed component list for Backlog 360?
   - What "everything you could ever imagine" includes specifically?
   - Similar specifications for Bookings 360?
   - **Timeline:** Needs design sessions with order management team

6. **Organizational Hierarchy Documentation**
   - Current org structure mapping (who reports to whom)?
   - Matrix organizational relationships (dotted-line reporting)?
   - Process for maintaining manager assignments post-go-live?
   - **Timeline:** Needs HR collaboration immediately during implementation

### Training Requirements

**Foundational Training (All Users)**
- Navigation of role centers and home dashboard
- How to use saved searches to find data
- How to filter and sort data
- When and how to use drill-down for investigation
- Official report usage and interpretation

**Role-Specific Training**

**Finance Team:**
- Standard financial reports (Income Statement, Balance Sheet, Trial Balance)
- As-of-date reporting for period comparisons
- Financial dashboard interpretation
- Scheduled report setup for executive packages
- Executive presentation drill-down technique

**Sales Team:**
- Sales rep scorecards (personal view)
- Pipeline reports and saved searches
- Inline editing for opportunity status updates
- Sales manager coaching (for managers on "me and my team" views)
- Highlighting rules interpretation (red for overdue, etc.)

**Operations Team:**
- Backlog 360 dashboard usage
- PM workload visibility
- Resource utilization reports
- Inline editing for status updates
- Priority highlighting

**Order Management Team:**
- Bookings 360 dashboard usage
- Acknowledgement tracking
- Fulfillment status visibility
- Invoice tracking
- Customer PO utilization

**IT/System Administrators:**
- Export permission configuration by role
- Large export notification workflow setup
- Org structure configuration and maintenance
- SuiteQL governance and query review
- Dashboard publishing and lock-down configuration

**Executive Leadership (Lorraine, Mark):**
- Financial dashboard drill-down
- Executive presentation capability
- Scheduled report review and interpretation
- Dashboard performance KPIs

### Change Management Strategy

The Business Intelligence & Reporting implementation represents significant behavioral change for KBM Hoag:

1. **From Excel to System:** Users must shift from Excel-centric reporting to NetSuite-native tools. This is productivity-enabling (drill-down, real-time, no export needed) but requires adoption discipline.

2. **From Personal to Official:** Users accustomed to creating personal report versions must adopt official reports as single source of truth. This is governance-enabling but requires trust in standardization.

3. **From Customized to Locked:** Dashboard customization freedom is replaced with publisher-controlled locked dashboards. This enables consistency but feels restrictive initially.

4. **From Guessing to Clarity:** Daily work changes from email/to-do lists to system-based reminders portlet. This is productivity-enabling but requires daily habit change.

**Change Management Approach:**

- **Early Communication:** Begin messaging "singing from same songbook" philosophy during discovery phase
- **Leadership Modeling:** Have Lorraine, Mark, and department heads use new tools first, publicly demonstrate value
- **Quick Wins:** Prioritize training on features with immediate value (reminders portlet, inline editing, drill-down) first
- **Hands-On Practice:** Live training sessions with real data, not presentation slides
- **Buddy System:** Pair power users with hesitant users for peer coaching
- **Feedback Loops:** Quickly address adoption barriers; if official report doesn't meet need, fix it
- **Measurement:** Track metrics—adoption of official reports, reminders portlet usage, reduction in Excel reporting—to demonstrate progress
- **Celebration:** Publicly recognize teams/individuals successfully adopting new approach

---

## Decision Log

### FUNCTIONALITY Decisions

| REQ-ID | Requirement | Decision | Evidence |
|--------|-------------|----------|----------|
| REQ-001 | NetSuite native BI tools primary platform | Use NetSuite dashboards, saved searches, workbook analytics, SuiteQL as primary reporting platform | "Just to kind of give you the highlights of what's available to you inside NetSuite" |
| REQ-003 | Dashboard lock-down capability | Implement role-based publishing with lock-down preventing customization | "'I changed my dashboard.' 'No, you're not doing that.'" |
| REQ-005 | Department-specific role centers | Create Finance, Sales, Pre-Quote, Order Management, Operations centers | "You can have a dashboard on each one of these tabs...process specific" |
| REQ-006 | Reminders portlet daily work driver | Implement reminders portlet as primary daily work surface | "This is all the work that I have to work off of...you shouldn't have to guess" |
| REQ-008 | Official report designation | Establish GSI/Orion prefix for official reports, nominate specific reports as official | "We prefix our saved search...nominate something as being like an official saved search" |
| REQ-013 | Standard NetSuite reports | Utilize 400+ standard reports, customize for KBM Hoag needs | "NetSuite ships with over 400 standard reports...every single one can be customized" |
| REQ-014 | As-of-date reporting | Enable as-of-date reporting for historical period snapshots | "What was my balance sheet as of September 1st. You can get that." |
| REQ-020 | Sales rep scorecards | Design custom scorecard component for individual performance visibility | "I would love them to see that on their own dashboard" |
| REQ-026 | Backlog 360 dashboard | Build comprehensive backlog dashboard combining line, order, fulfillment, acknowledgement views | "Everything you could ever imagine for backlog in one place" |
| REQ-027 | Bookings 360 dashboard | Build comprehensive bookings dashboard similar to Backlog 360 | Similar comprehensive structure requested |

### SOLUTIONDESIGN Decisions (Custom Development Required)

| REQ-ID | Requirement | Solution Design Approach |
|--------|-------------|--------------------------|
| REQ-003 | Dashboard lock-down | Implement NetSuite role-based dashboard publishing with configuration to prevent user customization |
| REQ-004 | Orion-enhanced components | Deploy Orion aesthetic components on all dashboards for modern visual appearance |
| REQ-012 | Large export notification | Design custom workflow to monitor export events and trigger alerts for exports >50MB threshold |
| REQ-020 | Sales rep scorecards | Design custom scorecard component with "me only" and "me and my team" filter variants |
| REQ-021 | Manager scorecards | Design custom scorecard component for team performance visibility (extends REQ-020) |
| REQ-026 | Backlog 360 | Design comprehensive dashboard combining: backlog by line, by order, fulfillment status, acknowledgement tracking, customer PO status, trends |
| REQ-027 | Bookings 360 | Design comprehensive dashboard combining: bookings by rep, by customer, by product, trends, forecast accuracy, pipeline comparison |

---

## Implementation Timeline

### Phase 1: Foundation (Weeks 1-4)
- Configure NetSuite base platform and user access
- Set up organizational hierarchy and manager assignments (REQ-023)
- Create role centers for Finance, Sales, Pre-Quote, Order Management, Operations (REQ-005)
- Configure base role permissions and export controls (REQ-011)

### Phase 2: Core Reporting (Weeks 5-8)
- Customize 400+ standard NetSuite reports for KBM Hoag needs (REQ-013)
- Enable as-of-date reporting capability (REQ-014)
- Configure workbook analytics for user access (REQ-015)
- Grant SuiteQL access to technical users (REQ-016)
- Begin official report identification and documentation (REQ-008, REQ-010)

### Phase 3: Governance (Weeks 9-12)
- Finalize official report list with department heads
- Create standardized report interpretation documentation (REQ-010)
- Configure public/private saved search controls (REQ-009)
- Establish report version control and change process

### Phase 4: Daily Operations (Weeks 13-16)
- Configure reminders portlet for all role centers (REQ-006, REQ-007)
- Design department-specific dashboards with KPI components
- Enable inline editing on operational saved searches (REQ-017)
- Configure highlighting rules for visual indicators (REQ-018)

### Phase 5: Security (Weeks 17-20)
- Finalize export security policy (role export permissions - REQ-011)
- Design and develop large export notification workflow (REQ-012)
- Configure export audit trail and monitoring
- IT Security training on policy enforcement

### Phase 6: Manager Tools (Weeks 21-24)
- Test "me and my team" filters on dashboards and reports
- Configure role-based dashboard publishing (REQ-003)
- Implement dashboard lock-down configuration
- Design manager-specific dashboards

### Phase 7: Executive Tools (Weeks 25-28)
- Configure scheduled report distribution for automated packages (REQ-024)
- Design executive financial dashboards with drill-down (REQ-025)
- Test executive presentation capability
- Lorraine and Mark training on real-time drill-down

### Phase 8: Custom Enhancements (Weeks 29-32)
- Design and build Backlog 360 dashboard (REQ-026)
- Design and build Bookings 360 dashboard (REQ-027)
- Implement Orion-enhanced dashboard components (REQ-004)
- Test comprehensive dashboards

### Phase 9: Power User Features (Weeks 33-36)
- Enable mass update functionality with training (REQ-019)
- Advanced SuiteQL training for technical users
- Workbook analytics advanced training
- Power BI integration if approved (REQ-002)

### Phase 10: Change Management & Go-Live (Weeks 37-40)
- Complete all user training
- Soft launch with early adopter groups
- Monitor adoption and quickly address issues
- Full go-live with support team available
- Post-go-live coaching and reinforcement

---

## Success Criteria

Implementation will be considered successful when:

1. **Official Reports Adoption:** 95%+ of team members use official reports for business decisions within 30 days of go-live (tracked via saved search usage)

2. **Reminders Portlet Usage:** 90%+ of daily users log in and view reminders portlet as first action each day within 2 weeks of go-live

3. **Dashboard Lock-Down Compliance:** 0 unauthorized dashboard customizations (locked dashboards remain published as-is) within 4 weeks of go-live

4. **Executive Presentation Capability:** Lorraine and Mark successfully conduct month-end financial review from live NetSuite dashboard with drill-down (no manual package needed) in first review cycle post-go-live

5. **Org Structure Accuracy:** Manager hierarchy configured correctly for all employees with "me and my team" filters working as expected across all dashboards

6. **Export Security:** Export permission policy implemented with zero breaches for departing employees; large export notification workflow responding appropriately within 24 hours

7. **Data Governance:** No unauthorized personal report versions created; all new saved searches follow GSI/Orion naming convention within first month

8. **User Adoption:** Net Promoter Score of 7+/10 for Business Intelligence features in post-go-live survey

9. **Dashboard Utilization:** 80%+ of team members access dashboards at least 3x per week within 4 weeks of go-live

10. **Training Effectiveness:** 90%+ of users demonstrate competency on core BI features (navigation, filtering, drill-down, saved searches) in post-training assessments

---

## Acceptance Signature Block

By signing below, stakeholders confirm that this Business Requirements Document accurately represents their Business Intelligence & Reporting requirements and that they approve proceeding with implementation based on these specifications.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CFO | Lorraine | _______________ | _______ |
| Executive | Mark | _______________ | _______ |
| Sales Leadership | Wendy | _______________ | _______ |
| Order Management Lead | [TBD] | _______________ | _______ |
| Finance Manager | [TBD] | _______________ | _______ |
| Operations Manager | [TBD] | _______________ | _______ |
| Pre-Quote Lead | [TBD] | _______________ | _______ |
| IT Director | [TBD] | _______________ | _______ |
| Implementation Lead | GSI | _______________ | _______ |

---

**End of Business Requirements Document - Business Intelligence & Reporting v1.0**

*This document represents the agreed-upon business requirements for KBM Hoag's Business Intelligence & Reporting functionality in the Orion/NetSuite implementation. The proven Orion/NetSuite solution meets these requirements with 18 standard capabilities (ALIGNS), 3 process adaptations (ADAPT), and 6 custom enhancements (ACCOMMODATE). Implementation can proceed with confidence that the solution is validated, appropriate, and ready for deployment.*




