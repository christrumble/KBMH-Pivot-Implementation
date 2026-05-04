# Pivot BRD — Business Intellegence

_Source: `Business Intellegence/Pivot/4 BRD/08_Pivot Interiors BRD Business Intelligence Process Area_v2.0.docx`_

---

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation__

__Business Intelligence & Reporting Process Area__

__Prepared for: Pivot Interiors, Inc\.__

__Version 2\.0__

__Date: February 13, 2025__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Sandra Massey \(NetSuite Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

# <a id="_Toc221887124"></a>__Table of Contents__

[__Table of Contents__	2](#_Toc221887124)

[__1 Version Control__	3](#_Toc221887125)

[__2 Project Definition__	3](#_Toc221887126)

[2\.01 Executive Summary	3](#_Toc221887127)

[2\.02 Company Overview	4](#_Toc221887128)

[2\.03 NetSuite Orion Overview	4](#_Toc221887129)

[2\.04 Project Overview	4](#_Toc221887130)

[2\.05 Document Objectives	5](#_Toc221887131)

[__3 Business Intelligence & Reporting__	6](#_Toc221887132)

[3\.01 Core NetSuite BI Tools	6](#_Toc221887133)

[3\.02 Dashboard & Analytics	9](#_Toc221887134)

[3\.03 Standard Reporting	13](#_Toc221887135)

[3\.04 Business Intelligence Tools	16](#_Toc221887136)

[3\.05 Data Export & Distribution	19](#_Toc221887137)

[3\.06 Document Management	23](#_Toc221887138)

[3\.07 Advanced Analytics & Customization	26](#_Toc221887139)

[__4 SuiteApps__	31](#_Toc221887140)

[4\.01 SuiteApp Summary	31](#_Toc221887141)

[__5 Assumptions__	32](#_Toc221887142)

[__6 Unresolved Requirements__	33](#_Toc221887143)

[__7 Signatures__	34](#_Toc221887144)

# <a id="_heading=h.30j0zll"></a>

# <a id="_heading=h.1fob9te"></a><a id="_Toc221887125"></a>__1 Version Control__

__Version__

__Author__

__Comments__

__Date__

0\.1

Debbie Herbert

Initial Draft

11/05/2025

0\.2

Debbie Herbert

Updated Draft

11/13/2025

1\.0

Debbie Herbert, Chris Trumble

Final Draft

11/202025

2\.0

Sandra Massey, Chris Trumble

Final for Approval

02/13/2026

# <a id="_heading=h.2et92p0"></a><a id="_heading=h.tyjcwt"></a>

# <a id="_Toc221887126"></a>__2 Project Definition__

## <a id="_Toc221887127"></a>__2\.01 Executive Summary__

Pivot Interiors operates as a multi\-entity office furniture dealership with locations across multiple markets, requiring unified business intelligence and reporting capabilities to support data\-driven decision\-making across all operational areas\. The organization currently faces significant challenges with D365's reporting limitations, including problematic AP reports, unusable WIP reports requiring manual updates, and weekly AR aging reports that must be manually refreshed\. These limitations force reliance on Excel\-based workarounds and prevent realtime operational visibility\.

The NetSuite Orion solution provides comprehensive, industry\-specific business intelligence and reporting capabilities designed specifically for contract furniture dealers\. The platform delivers real\-time dashboards, role\-based analytics, flexible saved search capabilities, and integrated reporting that eliminate manual reporting processes while providing unprecedented operational visibility\. NetSuite Orion's BI tools support Pivot's requirements for unified AR dashboards, project performance tracking, and executive analytics while maintaining the dual GP tracking \(actual vs\. commissionable\) critical to furniture dealer operations\.

This Business Requirements Document validates that NetSuite Orion's standard business intelligence functionality aligns with Pivot Interiors' reporting and analytics requirements, documenting how the envisioned solution will transform data accessibility and decision\-making capabilities across the organization\.

## <a id="_Toc221887128"></a>__2\.02 Company Overview__

Pivot Interiors, Inc\. is a leading California\-based design firm recognized for its team of innovators, creators, and thought leaders who specialize in delivering exceptional interior solutions for businesses of all sizes\. Their work captures the essence of each client’s brand while fostering environments that inspire employees to thrive, create, and collaborate\. Headquartered in the Bay Area, Pivot Interiors operates offices and Design Centers across the state, including Santa Clara, Fremont, San Francisco, Costa Mesa, Los Angeles, and La Mirada\. As a MillerKnoll Certified Dealer, Pivot Interiors invites clients to experience its uniquely crafted spaces and the distinctive quality that defines the Pivot Interiors brand\.

[__https://www\.pivotinteriors\.com__](https://www.pivotinteriors.com/)

## <a id="_Toc221887129"></a>__2\.03 NetSuite Orion Overview__

NetSuite Orion provides comprehensive business intelligence and reporting capabilities purpose\-built for the contract furniture industry\. The platform delivers real\-time operational dashboards, flexible saved search tools, role\-based analytics, and integrated reporting that address the unique visibility needs of furniture dealerships managing complex project\-based operations\.

NetSuite Orion’s BI architecture eliminates the reporting limitations inherent in general\-purpose ERP systems by providing furniture\-specific KPIs, dual GP tracking capabilities, project\-centric dashboards, and financial analytics integrated directly with transaction processing\. The solution enables sales representatives, project managers, controllers, and executives to access real\-time data through role\-appropriate dashboards and self\-service reporting tools, dramatically reducing dependence on IT resources and manual report generation\.

The platform's BI capabilities support sophisticated operational analytics with real\-time visibility,

automated calculation audit trails, and flexible saved search tools that enable business users to create custom reports without technical expertise\. This combination of standard furniture industry analytics with flexible customization capabilities makes NetSuite Orion the ideal BI foundation for Pivot's multi\-entity operations\.

## <a id="_Toc221887130"></a>__2\.04 Project Overview__

Pivot’s current engagement with GSI is based around the creation and implementation of a set of business requirements appropriate to its business operations both today and scaling into the future\. This project primarily consists of the following stages:

- __D__iscover: Evaluate the dealer’s business processes with NetSuite Orion capabilities
- __R__ealize: Perform initial setup, installation and configuration of your NetSuite instance
- __E__ducate: Empower your team for success through comprehensive training and user adoption support
- __A__ctualize: Bring your NetSuite and Orion solution to life with seamless data migration and go\-live support
- __M__aximize: Support and expand your operations with dedicated ongoing assistance and strategic customizations\.

Our implementation approach is “Align, Adapt, Accommodate”\.

- Align – Existing processes fit in NetSuite Orion as is\.
- Adapt – Pivot will change its processes to fit in NetSuite Orion as is\.
- Accommodate – GSI will create a configuration specific to Pivot Interiors, or if the feature can benefit others, will update the code base to make the feature standard\.

## <a id="_Toc221887131"></a>__2\.05 Document Objectives__

The purpose of this document is to summarize functional and procedural requirements captured by GSI during the Discover business process mapping phase of the implementation\. 

This Business Requirements Document \(BRD\) documents your goals, the problems you want to solve, and the outcomes you expect\. It is the foundation for the setup of the system, acting as a __roadmap between your business needs and the solution design__\.

This document represents information gathered in meetings held with the Client, which enables the GSI team to map the business requirements to an efficient flow in the NetSuite Orion application\. Once complete, this document will serve as a blueprint for the GSI team to configure the application\. This document does not supersede the Statement of Work\. The Statement of Work determines scope\. 

A series of process mapping discovery sessions, focusing on the key areas of the business, were used as a starting point for this exercise\. This document remains consistent in structure to those discovery sessions as it categorizes the findings into the same key process areas\. The set of business requirements documentation is inclusive of all business requirements provided by the Client\.

# <a id="_Toc221887132"></a>__3 Business Intelligence & Reporting__

## <a id="_Toc221887133"></a>__3\.01 Core NetSuite BI Tools__

3\.01\.01 Your Business Requirements

- REQ\-3\.01\.01: Real\-time operational visibility replacing D365's static, manual reporting processes
- REQ\-3\.01\.02: Role\-based dashboard access providing relevant KPIs to each user type \(sales reps, project managers, controllers, executives\)
- REQ\-3\.01\.03: Integrated BI tools eliminating need for external reporting platforms and Excel\-based workarounds
- REQ\-3\.01\.04: Furniture industry\-specific analytics supporting dual GP tracking, project performance, and financial analysis
- REQ\-3\.01\.05: Self\-service reporting capabilities enabling business users to create custom reports without IT dependence

3\.01\.02 Current State Process

PROCESS: Manual Report Generation and Distribution

TRIGGER: Need for operational or financial reporting

CURRENT STATE: Pivot currently relies on D365 for reporting, which presents significant limitations across all reporting areas\. The AP reports are described as problematic, WIP reports are unusable and require constant manual updates, and the weekly AR aging report must be manually updated each time users need current data\. These limitations force the organization to maintain extensive Excel\-based workarounds and prevent real\-time operational visibility\.

The current reporting environment lacks integration between financial and operational data, requires manual consolidation across systems, and cannot support role\-based dashboard delivery\. Users must request reports from IT or finance teams rather than accessing self\-service BI tools, creating bottlenecks and delays in decision\-making processes\.

SYSTEMS INVOLVED: D365 \(limited reporting\), Excel spreadsheets \(extensive workarounds\), manual consolidation processes

PAIN POINTS:

- D365 AP reports described as unusable
- WIP reports require constant manual updates to maintain accuracy
- Weekly AR aging must be manually refreshed each time data is needed
- No real\-time visibility into operations
- Heavy reliance on Excel for report manipulation
- IT dependence for custom report requests
- Lack of integrated view across financial and operational data
- No role\-based dashboard capabilities

3\.01\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive, integrated business intelligence tools purpose\-built for contract furniture dealers, eliminating the reporting limitations that plague general\-purpose ERP systems\. The solution delivers real\-time operational visibility through native BI capabilities that integrate seamlessly with all transaction processing, project management, and financial operations\.

The platform's core BI architecture includes real\-time dashboards, flexible saved search capabilities, custom report builders, and role\-based analytics that provide each user with relevant, actionable data without IT intervention\. Unlike D365's static reporting requiring manual updates, NetSuite Orion’s BI tools automatically reflect current data as transactions occur, ensuring users always access accurate, up\-to\-the\-minute information for decision\-making\.

NetSuite Orion’s furniture industry\-specific BI capabilities support the unique analytics requirements of contract furniture dealers, including dual GP tracking \(actual costs with time tracking vs\. commissionable GP with quoted costs\), project\-centric performance dashboards, financial analysis tools, and vendor relationship analytics\. These specialized capabilities eliminate the custom development and manual workarounds required in generic ERP systems\.

The solution's self\-service reporting architecture empowers business users to create custom saved searches, build personal dashboards, and generate ad\-hoc reports using point\-and\-click tools comparable to Crystal Reports but with real\-time data access\. This eliminates IT bottlenecks while maintaining data security through role\-based permissions, dramatically improving reporting agility and reducing time\-to\-insight across the organization\.

3\.01\.04 Future State Process

Pivot users will access real\-time operational data through role\-based dashboards automatically updated as transactions occur, not all reports can be sent directly to outside emails\. The work around is to create an entity \(simplest approach\) record for that email address, \(simplest approach\) preferably a contact record with their respective email address, you cannot simply type in an external email address\. This security restriction helps prevent unauthorized data sharing and ensures there's a record in NetSuite of who's receiving your company's data\.

The Sales representatives will view personal performance metrics through dedicated portlets\. Project managers will monitor project KPIs, including cash balance, GP performance, and labor tracking through integrated project dashboards\. Controllers and finance staff will access unified AR, AP, and financial performance dashboards, eliminating multi\-screen navigation\. Executives will leverage comprehensive strategic dashboards with drill\-down capabilities for detailed analysis\.

Business users will create custom reports using NetSuite Orion’s saved search functionality, building sophisticated queries without IT support\. Report creation will follow an intuitive point\-and\-click process like Crystal Reports, with immediate access to real\-time data rather than waiting for scheduled report generation\. Users will save and share custom searches across teams, building a library of frequently used reports accessible through personalized dashboard portlets\.

The manual Excel\-based reporting processes will be eliminated as users access data directly through NetSuite's native BI tools\. WIP reports will update as project transactions occur, AR aging will reflect real\-time data without manual refresh, and AP analytics will provide actionable insights through standard NetSuite Orion reporting\. The organization will shift from reactive, manual reporting to proactive, real\-time analytics supporting data\-driven decision\-making across all operational areas\.

3\.01\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.01\.01

Real\-time operational visibility replacing D365's static reporting

Native real\-time dashboards and reporting updated automatically with transaction processing

ALIGNS

REQ\-3\.01\.02

Role\-based dashboard access for different user types

Standard role\-based dashboard configuration with personalized portlets

ALIGNS

REQ\-3\.01\.03

Integrated BI tools eliminating external platforms

Comprehensive native BI tools including dashboards, saved searches, and report builders

ALIGNS

REQ\-3\.01\.04

Furniture industry\-specific analytics \(dual GP, project metrics\)

Orion\-specific KPIs including dual GP tracking, project performance, financial analytics

ALIGNS

REQ\-3\.01\.05

Self\-service reporting without IT dependence

Point\-and\-click saved search builder accessible to business users

ADAPT

<a id="_heading=h.3fwokq0"></a>

__*Client Feedback*__

<a id="_heading=h.1v1yuxt"></a>__*GSI Response*__

<Comment>

## <a id="_Toc221887134"></a>__3\.02 Dashboard & Analytics__

3\.02\.01 Your Business Requirements

- __REQ\-3\.02\.01:__ Unified AR collections dashboard consolidating aging, days past due, credits, and project IDs in single view\. Set up as due date\.__ Due Date__ to use whatever due date you assign for aging bills and invoices\.

Select __Transaction Date__ to age by the date of the bill or invoice, no matter when it is due\.

- __REQ\-3\.02\.02:__ Project performance dashboard displaying cash balance, dual GP tracking \(actual and commissionable\), WIP, and labor tracking
- __REQ\-3\.02\.03:__ Executive dashboard providing Cash Flow360, financial performance summaries, and project portfolio overview with drill\-down capabilities
- __REQ\-3\.02\.04:__ AP dashboard showing aging, open receipts without invoices, and payment processing status
- __REQ\-3\.02\.05:__ Real\-time project KPI tracking including project cash balance \(deposits/payments in vs vendor payments out\)
- __REQ\-3\.02\.06:__ Dual GP visibility showing actual GP \(with time\-tracked costs\) and commissionable GP \(with quoted costs\)
- __REQ\-3\.02\.07:__ Project completion percentage tracking
- __REQ\-3\.02\.08:__ AR aging by project and customer
- __REQ\-3\.02\.09:__ Labor quote vs actual hours and costs

3\.02\.02 Current State Process

__PROCESS: __Multi\-System Dashboard Access and Manual KPI Tracking

__TRIGGER: __Daily operational monitoring and performance tracking

__CURRENT STATE: __Pivot currently lacks unified dashboard capabilities, forcing users to navigate multiple D365 screens and manually compile data from various sources to understand operational status\. AR management requires checking multiple reports and screens to see aging, credits, and project associations\. Project managers cannot access real\-time project performance dashboards showing cash balance or GP tracking, instead relying on periodic reports and Excel analysis\.

The dual GP tracking requirement \(actual vs\. commissionable\) cannot be visualized through dashboards, requiring manual Excel calculations\.

Executive leadership lacks strategic dashboards providing portfolio\-level visibility with drill\-down capabilities\. The Cash Flow360 concept cannot be implemented in D365, limiting cash flow visibility and forecasting capabilities\. KPI tracking across all operational areas requires manual report generation and consolidation rather than real\-time dashboard monitoring\.

__SYSTEMS INVOLVED: __D365 \(limited dashboard capabilities\), Excel \(manual KPI tracking\), manual consolidation processes

__PAIN POINTS:__

- No unified AR dashboard requiring navigation across multiple screens
- Lack of real\-time project performance visibility
- Cannot visualize dual GP \(actual vs\. commissionable\) in real\-time
- Executive dashboards require manual report consolidation
- No Cash Flow360 visibility
- KPI tracking depends on manual report generation
- No drill\-down capabilities from summary to detail

3\.02\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive role\-based dashboard and analytics capabilities designed specifically to address the visibility challenges facing contract furniture dealers\. The solution delivers pre\-configured dashboard portlets for common furniture dealer KPIs while enabling complete customization to match Pivot's specific operational requirements and user preferences\.

The platform's unified AR dashboard consolidates aging analysis, days past due calculations, credit management, and project associations in a single view, eliminating the multi\-screen navigation that hampers efficiency in D365\. AR managers access complete customer and project status through intuitive portlets with one\-click drill\-down to transaction detail, dramatically improving collection effectiveness and reducing time spent navigating between screens\.

NetSuite Orion’s project performance dashboards deliver real\-time visibility into the critical KPIs that drive furniture dealer profitability\. Project cash balance tracking automatically calculates deposits and payments received against vendor payments made, providing instant visibility into project cash position\. The dual GP tracking capability—a unique Orion feature essential to furniture dealers—displays both actual GP \(calculated with time\-tracked labor costs\) and commissionable GP \(calculated with quoted labor rates\) side\-by\-side, ensuring accurate financial analysis while maintaining visibility into true project profitability\.

Executive dashboards provide strategic visibility through the Cash Flow360 portlet and financial performance summaries with drill\-down capabilities enabling detailed analysis of variances and trends\. Unlike D365's static reporting requiring manual consolidation, NetSuite Orion’s executive dashboards update automatically with transaction processing, ensuring leadership always accesses current data for strategic decision\-making\. The portfolio\-level project overview enables executives to monitor project health across the entire organization with filtering, sorting, and drill\-down capabilities providing insights into specific projects, customers, or market segments\.

The platform's AP dashboard consolidates vendor aging, open receipt tracking \(receipts without matched invoices\), and payment processing status in unified views that streamline accounts payable operations\. This integrated visibility enables AP managers to prioritize vendor payments based on aging, identify receipts requiring invoice follow\-up, and monitor payment processing status without navigating multiple systems or reports\.

NetSuite Orion’s analytics architecture supports sophisticated KPI tracking across all operational areas including project completion percentages, AR aging by project and customer, and labor quote vs\. actual analysis\. All calculations include complete audit trail visibility, ensuring transparency and supporting analysis when questions arise\.

3\.02\.04 Future State Process

Pivot users will access personalized dashboards automatically displayed upon login, showing role\-appropriate KPIs updated in real\-time as transactions occur\. AR managers will monitor collections through unified dashboards showing aging, credits, and project status without navigating between screens\. When investigating specific customers, they will drill down from dashboard portlets directly to transaction detail with a single click\.

Project managers will start each day reviewing project performance dashboards showing current cash balance, dual GP tracking, WIP status, and labor utilization\. The dashboard will highlight projects requiring attention through color\-coded indicators and threshold alerts\. When investigating variances, project managers will drill down from KPI summaries to detailed transactions, investigating issues and taking corrective action without leaving the dashboard interface\.

Controllers and finance staff will access dual GP visibility through project dashboards, monitoring both actual GP \(with time\-tracked costs\) and commissionable GP \(with quoted costs\) to ensure accurate financial analysis while maintaining visibility into true project profitability\.

Executives will review strategic dashboards showing Cash Flow360 analysis, financial performance summaries, and project portfolio overview with filtering and drill\-down capabilities\. When investigating variances or trends, they will navigate from high\-level KPIs to detailed analysis without requesting custom reports or waiting for manual consolidation\. The dashboard architecture will support data\-driven strategic decision\-making through immediate access to current operational and financial data\.

3\.02\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REC\-3\.02\.01__

Unified AR collections dashboard

Standard AR dashboard portlets with aging, credits, and project associations

__ALIGNS__

__REC\-3\.02\.02__

Project performance dashboard

Orion project dashboard with cash balance, dual GP, WIP, labor tracking

__ALIGNS__

__REC\-3\.02\.03__

Executive dashboard with Cash Flow360

NetSuite executive dashboards with Cash Flow360 portlet and drill\-down

__ALIGNS__

__REC\-3\.02\.04__

AP dashboard

Standard AP dashboard portlets showing aging and open receipts

__ALIGNS__

__REC\-3\.02\.05__

Real\-time project cash balance tracking

Orion project cash balance calculation \(deposits/payments in vs\. vendor payments out\)

__ALIGNS__

__REC\-3\.02\.06__

Dual GP visibility \(actual and commissionable\)

Orion dual GP tracking showing actual \(time\-tracked\) and commissionable \(quoted\) GP

__ALIGNS__

__REC\-3\.02\.07__

Project completion percentage tracking

Standard project completion KPI based on milestones and billing

__ALIGNS__

__REC\-3\.02\.08__

AR aging by project and customer

Standard AR aging reports with project and customer dimensions

__ALIGNS__

__REC\-3\.02\.09__

Labor quote vs actual tracking

Orion labor tracking comparing quoted hours/costs to actual time\-tracked data

__ALIGNS__

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc221887135"></a>__3\.03 Standard Reporting__

3\.03\.01 Your Business Requirements

Provide copy of crystal report that needs to be emailed

- __REQ\-3\.03\.01:__ Replace D365's AP reports with usable, actionable AP reporting
- __REQ\-3\.03\.02:__ Replace unusable WIP reports requiring constant manual updates with automated WIP reporting
- __REQ\-3\.03\.03:__ Replace weekly AR aging requiring manual refresh with real\-time AR aging reports
- __REQ\-3\.03\.04:__ Standard financial reports with drill\-down capabilities to transaction detail
- __REQ\-3\.03\.05:__ Project performance reports showing actual vs budget analysis

3\.03\.02 Current State Process

__PROCESS: __Manual Report Generation and Maintenance

__TRIGGER: __Need for operational reporting \(AP, AR, WIP, financial analysis\)

__CURRENT STATE: __Pivot's current D365 reporting environment presents significant challenges across all standard report categories\. The AP reports are described as unusable and require extensive manual manipulation to extract actionable information for vendor payment decisions\. The WIP reports are unusable in their native form and require constant manual updates to maintain accuracy, forcing finance staff to spend significant time maintaining parallel tracking systems\.

The weekly AR aging report must be manually refreshed each time users need current data, preventing real\-time collections management and creating delays in customer outreach\. This manual refresh requirement means AR aging data is often stale by the time collections staff access it, reducing collection effectiveness\.

Standard financial reports lack drill\-down capabilities, requiring manual investigation when variances are identified\. Project performance reporting requires manual Excel analysis comparing actual to budget across multiple dimensions\.

__SYSTEMS INVOLVED: __D365 \(inadequate standard reports\), Excel \(extensive manual reporting\), manual analysis processes

__PAIN POINTS:__

- AP reports described as unusable
- WIP reports require constant manual updates
- AR aging requires manual refresh each time data is needed
- No drill\-down capabilities in financial reports
- Manual variance analysis required
- Project performance reporting through Excel
- Time\-consuming report generation processes

3\.03\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive standard reporting capabilities specifically designed to address the reporting failures common in general\-purpose ERP systems\. The solution delivers industry\-standard financial reports with furniture dealer\-specific enhancements, eliminating the manual workarounds and data quality issues that plague D365 implementations\.

The platform's AP reporting suite provides actionable vendor management reports including aging analysis, payment prioritization tools, and open receipt tracking that enable efficient accounts payable operations\. Unlike D365's inadequate AP reports, NetSuite's standard AP reports deliver the information AP managers need to make payment decisions without manual data manipulation or Excel exports\. Reports automatically update with transaction processing, ensuring users always access current data for vendor management decisions\.

NetSuite's WIP reporting eliminates the manual update requirements that make D365 WIP reports unusable\. The system automatically calculates WIP based on project transactions, revenue recognition rules, and billing status, providing accurate work\-in\-progress analysis without manual intervention\. Controllers access real\-time WIP reports showing project\-level detail with drill\-down capabilities to investigate specific projects or cost categories, eliminating the parallel tracking systems required in D365\.

The AR aging reporting capabilities provide real\-time aging analysis without manual refresh requirements\. Collections staff access current aging data automatically updated as payments are received and invoices are generated, enabling proactive collections management based on accurate, up\-to\-the\-minute customer status\. The reports support multiple aging dimensions including by customer, by project, and by salesperson, providing flexibility for different collection strategies\.

Standard financial reports include comprehensive drill\-down capabilities enabling investigation from summary to transaction detail with a single click\. When variance analysis is needed, users navigate directly from financial statements to supporting transactions, dramatically reducing time spent investigating issues\. Project performance reports provide actual vs\. budget analysis across multiple dimensions including labor, materials, and indirect costs, supporting proactive project management and variance correction\.

3\.03\.04 Future State Process

Pivot will access standard operational reports through NetSuite's native reporting interface with automatic updates reflecting current data\. AP managers will generate vendor aging reports, payment prioritization analysis, and open receipt tracking without manual data manipulation or Excel exports\. The reports will provide actionable information supporting efficient vendor payment decisions and cash management\.

Controllers will access automated WIP reports updated in real\-time as project transactions occur\. The manual WIP tracking processes will be eliminated as NetSuite automatically calculates work\-in\-progress based on project status, revenue recognition, and billing\. WIP reports will provide project\-level detail with drill\-down to transaction detail for variance investigation\.

AR aging reports will display current customer status automatically updated as transactions occur, eliminating the manual refresh requirement that hampers D365 collections management\. Collections staff will access real\-time aging data supporting proactive customer outreach and collection prioritization based on accurate current information\.

Finance staff will leverage standard financial reports with drill\-down capabilities, investigating variances by clicking directly from summary to transaction detail\. Project managers will access project performance reports showing actual vs\. budget analysis, identifying variances and taking corrective action based on real\-time data\.

3\.03\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.03\.01

Replace D365's AP reports

Standard NetSuite AP aging, payment, and vendor reports

ADAPT

REQ\-3\.03\.02

Replace unusable WIP reports

Automated WIP reporting based on project transactions and revenue recognition

ADAPT

REQ\-3\.03\.03

Replace manual AR aging refresh

Real\-time AR aging reports automatically updated with transactions

ADAPT

REQ\-3\.03\.04

Standard financial reports with drill\-down

NetSuite financial reports with one\-click drill\-down to transaction detail

ALIGNS

REQ\-3\.03\.05

Project performance reports \(actual vs budget\)

Orion project performance reports with variance analysis

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc221887136"></a>__3\.04 Business Intelligence Tools__

3\.04\.01 Your Business Requirements

- REQ\-3\.04\.01: Flexible custom reporting through NetSuite saved searches for complex business scenarios
- REQ\-3\.04\.02: Point\-and\-click saved search builder accessible to business users without IT support
- REQ\-3\.04\.03: Ability to publish saved searches to specific roles/users
- REQ\-3\.04\.04: Saved search templates for common furniture dealer scenarios
- REQ\-3\.04\.05: Project\-level reporting showing all transactions and adjustments
- REQ\-3\.04\.06: Period\-based financial statements with drill\-down capabilities

3\.04\.02 Current State Process

__PROCESS: __Manual Custom Report Requests and Analysis

__TRIGGER: __Need for custom analysis or exception reporting

__CURRENT STATE: __

Custom analysis requires manual Excel manipulation after exporting data from D365\. The team manually reviews transactions to identify exceptions or issues requiring attention, spending significant time on repetitive manual review that cannot scale efficiently\.

Project\-level financial analysis requires consolidating data from multiple sources with manual calculations\. Period\-based financial analysis involves manual data extraction and consolidation across systems\. There is no automated alerting or exception flagging, forcing manual transaction review\.

__SYSTEMS INVOLVED: __D365, Excel spreadsheets, manual review processes, IT\-dependent custom report development

__PAIN POINTS:__

- IT dependence for custom report creation
- Time\-consuming manual review of transactions
- Cannot scale manual review processes as transaction volume grows
- No automated identification of exception scenarios
- Manual data consolidation for project analysis
- Delays waiting for IT to create custom reports

3\.04\.03 NetSuite Orion Solution

NetSuite Orion provides sophisticated business intelligence tools designed to handle complex business scenarios and exception processing requirements common in furniture dealer operations\. The solution combines flexible saved search capabilities with self\-service report creation that reduces manual workload while maintaining accuracy and control\.

The platform's saved search functionality delivers point\-and\-click report building capabilities comparable to Crystal Reports but with real\-time data access and native integration with all NetSuite data\. Business users with experience creating Crystal Reports—such as Sandra Rudloff—will find NetSuite's saved search builder intuitive and powerful, enabling creation of sophisticated queries without IT intervention\. Saved searches can identify complex business scenarios across any dimension of the business\.

NetSuite Orion’s ability to publish saved searches to specific roles ensures relevant reports reach appropriate users without overwhelming others with irrelevant data\. Users access role\-appropriate searches while administrators maintain centralized control over report distribution and access\.

The platform's project\-level reporting capabilities show all transactions and adjustments by project, providing complete project lifecycle visibility\. Controllers can analyze total financial impact by project, identifying issues and understanding patterns by customer, product line, or market segment\. Period\-based financial statements with drill\-down capabilities enable investigation from summary to transaction detail, supporting reconciliation and verification processes\.

The saved search architecture supports automated alerting through scheduled searches that flag transactions meeting specific criteria\. Rather than manually reviewing all transactions, users receive automated alerts identifying candidates for investigation or action\. This dramatically reduces workload while ensuring no issues are missed\.

3\.04\.04 Future State Process

Pivot will leverage NetSuite's saved search capabilities extensively to identify exceptions and support custom analysis needs\. Sandra Rudloff and other business users will create saved searches using the point\-and\-click builder, quickly defining complex criteria to identify transactions requiring attention\.

Saved searches will run automatically on scheduled intervals \(daily, weekly, or real\-time\), generating alerts identifying transactions requiring review or action\. Users will access personal saved searches through published searches, showing relevant information for their roles\.

Project\-level saved searches will show total financial impact by project, supporting financial analysis and project profitability tracking\. Controllers will leverage saved searches for project analysis without manual data consolidation\.

Business users will create and publish custom reports without IT assistance, building a library of frequently\-used analyses accessible through role\-appropriate permissions\. The organization will shift from IT\-dependent custom reporting to business user self\-service analytics\.

3\.04\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.04\.01

Flexible custom reporting through saved searches

Point\-and\-click saved search builder with full NetSuite data access

ALIGNS

REQ\-3\.04\.02

Point\-and\-click saved search builder

Standard NetSuite saved search interface comparable to Crystal Reports

ADAPT

REQ\-3\.04\.03

Publish saved searches to specific roles

Role\-based saved search publication and access control

ALIGNS

REQ\-3\.04\.04

Saved search templates for common scenarios

Furniture dealer\-specific saved search templates included in Orion

ALIGNS

REQ\-3\.04\.05

Project\-level reporting showing all transactions

Saved searches showing all transactions and adjustments by project

ALIGNS

REQ\-3\.04\.06

Period\-based statements with drill\-down

Standard financial statements with transaction detail access

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc221887137"></a>__3\.05 Data Export & Distribution__

3\.05\.01 Your Business Requirements

- __REQ\-3\.05\.01:__ Excel export capabilities for ad\-hoc analysis and external stakeholder reporting
- __REQ\-3\.05\.02:__ CSV export for data integration with external systems
- __REQ\-3\.05\.03:__ PDF report generation for formal reporting and archival purposes
- __REQ\-3\.05\.04:__ Scheduled report distribution via email to appropriate stakeholders
- __REQ\-3\.05\.05:__ Mass data export capabilities for audits and compliance requirements

3\.05\.02 Current State Process

__PROCESS: __Manual Report Export and Distribution

__TRIGGER: __Need to share data externally or perform analysis outside core system

__CURRENT STATE: __Pivot currently manages report export and distribution through manual processes requiring significant time from finance and accounting staff\. Reports must be manually extracted from D365, formatted in Excel, and distributed via email to appropriate stakeholders\. The manual export process is time\-consuming and prevents timely distribution of operational reports\.

Recurring reports such as monthly financial summaries and weekly AR aging require repetitive manual export and distribution, consuming valuable staff time that could be applied to analysis and decision support\. There are no scheduled distribution capabilities, forcing staff to remember distribution schedules and manually execute report generation and delivery\.

Data export for external analysis or system integration requires IT assistance, creating bottlenecks when business users need data for board presentations, audit support, or special analysis\. The lack of self\-service export capabilities limits business user agility and increases IT workload\.

__SYSTEMS INVOLVED: __D365 \(limited export capabilities\), manual email distribution, Excel \(report formatting\)

__PAIN POINTS:__

- Manual report export is time\-consuming
- Repetitive distribution of recurring reports consumes staff time
- No scheduled distribution capabilities
- IT dependence for mass data exports
- Risk of missing distribution deadlines for recurring reports
- Manual formatting required after export
- Limited export format options

3\.05\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive data export and distribution capabilities designed to streamline reporting workflows and enable efficient data sharing with external stakeholders and systems\. The solution supports multiple export formats, scheduled distribution, and self\-service export capabilities that eliminate the manual processes burdening Pivot's current operations\.

The platform's Excel export functionality enables ad\-hoc analysis and external reporting without IT intervention\. Users export any report, dashboard, or saved search directly to Excel with formatting preserved, enabling immediate analysis or further customization for board presentations and stakeholder reports\. The Excel export maintains data relationships and formulas where appropriate, reducing post\-export formatting requirements\.

CSV export capabilities support data integration with external analytics tools, data warehouses, or specialized analysis platforms\. Business users and IT staff can export data in CSV format for import into other systems, supporting integration workflows and compliance requirements\. The CSV export functionality includes field mapping and delimiter options ensuring compatibility with diverse downstream systems\.

PDF report generation delivers professional\-quality reports suitable for formal distribution to stakeholders, board members, and external parties\. NetSuite automatically formats reports with headers, footers, and branding consistent with organizational standards, eliminating manual formatting requirements\. The PDF generation supports both on\-demand and scheduled distribution, enabling recurring report automation\.

NetSuite Orion's scheduled report distribution capabilities automate recurring reporting workflows through email distribution to defined recipient lists\. Controllers and finance staff configure distribution schedules for monthly financial summaries, weekly AR aging, and other recurring reports, eliminating manual distribution processes and ensuring stakeholders receive timely information without staff intervention\. The scheduled distribution includes delivery confirmation and failure notifications, ensuring reliable report delivery\.

The platform's mass data export capabilities support audit requirements and compliance obligations through bulk data extraction with filtering, date range selection, and field specification options\. These tools enable efficient response to audit requests and regulatory obligations without custom development or IT assistance, reducing compliance costs and improving response times\.

3\.05\.04 Future State Process

Pivot users will export data and reports directly from NetSuite in multiple formats based on use case requirements\. When performing ad\-hoc analysis, controllers and finance staff will export saved searches and reports directly to Excel, immediately beginning analysis without manual reformatting or data manipulation\.

Scheduled report distribution will eliminate manual recurring report processes\. The system will automatically generate monthly financial summaries and weekly AR aging reports, distributing them via email to configured recipient lists without human intervention\. Stakeholders will receive timely reports consistently without dependence on staff availability or workload fluctuations\.

When preparing board presentations or executive summaries, finance staff will export NetSuite reports to PDF format with professional formatting, incorporating them directly into presentation materials without manual formatting\. The PDF exports will maintain branding consistency and professional appearance suitable for external stakeholder distribution\.

Data integration workflows will leverage CSV export capabilities to extract NetSuite data for analysis in external tools or import into data warehouses\. IT staff will configure scheduled CSV exports for recurring integration needs, automating data flow to downstream systems without manual intervention\.

When responding to audit requests, accounting staff will use mass data export capabilities to extract transaction detail, financial records, or compliance documentation efficiently\. The self\-service export tools will enable rapid response to information requests without IT involvement, reducing audit response times and associated costs\.

3\.05\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-03\.05\.01

Excel export for ad\-hoc analysis

Standard Excel export from any report or saved search

ALIGNS

REQ\-03\.05\.02

CSV export for system integration

CSV export with field mapping and delimiter options

ALIGNS

REQ\-03\.05\.03

PDF report generation

Professional PDF generation with branding and formatting

ALIGNS

REQ\-03\.05\.04

Scheduled report distribution

Automated email distribution on configured schedules

ALIGNS

REQ\-03\.05\.05

Mass data export for audits

Bulk export tools with filtering and date range selection

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc221887138"></a>__3\.06 Document Management__

3\.06\.01 Your Business Requirements

- __REQ\-3\.06\.01:__ Centralized document storage associated with projects, customers, and vendors
- __REQ\-3\.06\.02:__ Version control for documents updated over time
- __REQ\-3\.06\.03:__ Document access controls based on user roles and permissions
- __REQ\-3\.06\.04:__ Document search capabilities by project, customer, document type, or keywords
- __REQ\-3\.06\.05:__ Integration between document storage and transaction records

3\.06\.02 Current State Process

__PROCESS: __Decentralized Document Management

__TRIGGER: __Need to store, retrieve, or share project and customer documentation

__CURRENT STATE: __Pivot currently manages documents through decentralized storage, including network drives, local folders, email attachments, and SharePoint\. Project\-related documents are scattered across multiple locations with no consistent organizational structure, making document retrieval time\-consuming and unreliable\.

There is no integration between document storage and D365 transaction records, requiring staff to search multiple systems when looking for customer contracts, vendor agreements, or project documentation\. Version control is manual with file naming conventions that are inconsistently applied, creating confusion about which document version is current\.

Document access controls are limited, with network drive permissions providing only coarse\-grained security\. Sensitive documents may be accessible to users who should not have access, creating compliance and confidentiality risks\.

__SYSTEMS INVOLVED: __Network drives, SharePoint, email, local storage, no integration with D365

__PAIN POINTS:__

- Documents scattered across multiple storage locations
- No integration with transaction records
- Time\-consuming document retrieval
- Inconsistent version control
- Limited document search capabilities
- Coarse\-grained access controls
- Risk of working with outdated document versions

3\.06\.03 NetSuite Orion Solution

NetSuite Orion provides integrated document management capabilities that centralize document storage while maintaining associations with projects, customers, vendors, and transaction records\. The solution eliminates the document scattering and retrieval challenges common in furniture dealer operations through native integration between the document repository and all business records\.

The platform's centralized document storage associates files directly with relevant business records including projects, customers, vendors, orders, and invoices\. Project managers attach project\-related documents to project records, sales representatives attach proposals and contracts to customer records, and purchasing staff attach vendor agreements to vendor records—all within the NetSuite interface without navigating to external storage systems\.

NetSuite's version control capabilities automatically track document changes over time, maintaining historical versions accessible for audit and reference purposes\. When users upload new document versions, the system archives previous versions while marking the latest version as current, eliminating manual version tracking through file naming conventions\.

The solution's role\-based document access controls ensure sensitive documents are only visible to appropriate staff\. Administrators configure access controls based on user roles, ensuring project documents are accessible to project teams, financial documents are restricted to accounting staff, and customer contracts are accessible to sales and executive teams\. This granular security reduces compliance risk while maintaining operational efficiency\.

Document search capabilities enable efficient retrieval by project, customer, vendor, document type, keywords, or date ranges\. Users search for documents without remembering specific storage locations or file names, dramatically reducing document retrieval time and improving information accessibility across the organization\.

The integration between document management and transaction records ensures users access relevant documents directly from the context they're working in\. When reviewing a project, project managers see all project\-related documents\. When investigating customer issues, customer service staff access customer contracts and correspondence\. When processing vendor payments, AP staff access vendor agreements and receiving documents—all without leaving their current workflow\.

3\.06\.04 Future State Process

Pivot will manage all project, customer, and vendor documents through NetSuite's integrated document management system\. Project managers will attach project documentation directly to project records, ensuring all project\-related files are centrally accessible from the project workspace\. Sales representatives will attach proposals, contracts, and customer correspondence to customer records, eliminating scattered email attachments and local storage\.

When documents are updated, users will upload new versions through NetSuite's interface, which will automatically archive previous versions and mark the latest version as current\. Users investigating document history will access previous versions through the version control interface, comparing changes over time for audit or review purposes\.

Document access will be controlled through role\-based permissions configured by administrators\. Sensitive financial documents will be restricted to accounting staff, customer contracts will be accessible to sales and executive teams, and project documents will be visible to project teams\. This granular security will reduce compliance risk while maintaining operational efficiency\.

When users need to locate documents, they will search NetSuite's document repository by project name, customer, vendor, document type, keywords, or date ranges\. Search results will return relevant documents with links to associated business records, enabling immediate access without remembering storage locations or file naming conventions\.

The integration between documents and business records will enable contextual document access throughout daily operations\. Project managers reviewing project status will click to view project documentation\. Customer service staff investigating customer issues will immediately access customer contracts and correspondence\. AP staff processing vendor payments will view vendor agreements and receiving documents—all within their current workflow without navigating to external systems\.

3\.06\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.06\.01__

Centralized document storage with business record associations

SharePoint File Storage

__ALIGNS__

__REQ\-3\.06\.02__

Version control for documents

Automatic version tracking with historical access

__ALIGNS__

__REQ\-3\.06\.03__

Role\-based document access controls

Role\-based permissions for document folders and files

__ALIGNS__

__REQ\-3\.06\.04__

Document search by multiple criteria

Document search by project, customer, type, keywords, dates

__ALIGNS__

__REQ\-3\.06\.05__

Integration with transaction records

Native document associations with all business records

__ALIGNS__

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc221887139"></a>__3\.07 Advanced Analytics & Customization__

3\.07\.01 Your Business Requirements

- __REQ\-3\.07\.01:__ Predictive analytics for project profitability forecasting based on historical performance predictive analysis implies the availability to produce a report even before the project is finilized
- __REQ\-3\.07\.02:__ Custom KPI development for furniture dealer\-specific metrics not available in standard reports
- __REQ\-3\.07\.03:__ Advanced data visualization capabilities beyond standard dashboard portlets
- __REQ\-3\.07\.04:__ Integration with external analytics platforms \(Power BI consideration for specialized analysis\)
- __REQ\-3\.07\.05:__ Custom calculated fields and formulas for complex business logic
- __REQ\-3\.07\.06:__ Trend analysis and period\-over\-period comparison tools
- __REQ\-3\.07\.07:__ What\-if scenario modeling for project budgeting and resource allocation
- __REQ\-3\.07\.08:__ API access for custom integrations with proprietary analytics tools

3\.07\.02 Current State Process

__PROCESS: __Limited Advanced Analytics Capabilities

__TRIGGER: __Need for predictive analysis, trend forecasting, or complex custom calculations

__CURRENT STATE: __\. Predictive analysis requires manual Excel modeling using exported historical data, and manipulation in Power BI\.

Integration with external analytics platforms is limited, with no standardized API access for data extraction\. When specialized analysis is needed, staff must manually export data and load it into external tools, creating delays and preventing real\-time analytics\. The lack of integration capabilities limits the organization's ability to leverage best\-in\-class analytics tools for specialized use cases\.

Period\-over\-period comparison and trend analysis require manual report consolidation across multiple time periods\. Users cannot visualize trends through dynamic charts or interactive dashboards, limiting their ability to identify patterns and make data\-driven decisions\. What\-if scenario modeling is entirely manual, requiring spreadsheet development for each analysis scenario\.

__SYSTEMS INVOLVED: __D365 \(limited analytics\), Excel \(manual modeling and calculations\), manual data export processes

__PAIN POINTS:__

- No predictive analytics capabilities
- Cannot create custom KPIs without extensive development
- Manual Excel\-based forecasting and modeling
- Limited data visualization options
- No API access for external analytics integration
- Time\-consuming manual trend analysis
- Cannot perform real\-time what\-if scenario modeling
- Period\-over\-period analysis requires manual consolidation
- No interactive dashboards for data exploration

3\.07\.03 NetSuite Orion Solution

NetSuite Orion provides advanced analytics and customization capabilities that extend beyond standard reporting to support sophisticated business intelligence requirements\. The solution enables predictive analytics, custom KPI development, advanced visualizations, and flexible integration with external analytics platforms, empowering Pivot to leverage data for competitive advantage\.

The platform's custom calculated fields functionality enables creation of complex formulas and business logic directly within NetSuite without custom coding\. Controllers and finance staff can define custom GP calculations, profitability metrics, and performance indicators that automatically calculate as data is entered, providing real\-time visibility into custom business metrics\. These calculated fields integrate seamlessly with saved searches, dashboards, and standard reports, ensuring custom KPIs are accessible across all BI tools\.

NetSuite's SuiteAnalytics capabilities provide advanced data visualization and exploration tools that enable users to create interactive charts, pivot tables, and multi\-dimensional analysis\. The platform supports trend analysis with period\-over\-period comparisons, variance analysis, and dynamic filtering that helps users identify patterns and anomalies\. Users can create custom visualizations showing project profitability trends, sales performance patterns, and operational efficiency metrics with drill\-down capabilities for detailed investigation\.

SuiteAnalytics Connect, a separate module that must be purchased in addition to the SuiteAnalytics base module, provides the API infrastructure \(RESTlets, SuiteScript, and ODBC/JDBC drivers\) to enable integration with external analytics platforms including Power BI, Tableau, and custom analytics tools\. Organizations can configure scheduled data exports feeding external platforms or establish real\-time API connections for live data access\. This flexibility ensures Pivot can leverage specialized analytics tools for advanced use cases while maintaining NetSuite as the system of record\.

Predictive analytics capabilities through SuiteAnalytics include regression analysis, trend forecasting, and historical pattern recognition that support project profitability forecasting, resource demand planning, and financial performance prediction\. While not replacing dedicated machine learning platforms, NetSuite's native predictive capabilities provide substantial analytical power for common furniture dealer forecasting needs\.

The platform supports what\-if scenario modeling through saved searches with parameter inputs, enabling users to model different assumptions and compare results side\-by\-side\. Project managers can evaluate budget alternatives, controllers can model pricing scenarios, and executives can forecast financial outcomes under different market conditions—all within NetSuite's integrated environment\.

NetSuite's workflow and scripting capabilities enable automation of complex analytics processes including scheduled analysis execution, exception alerting based on custom thresholds, and automated distribution of analytical insights\. This automation reduces manual analytical workload while ensuring stakeholders receive timely insights for decision\-making\.

3\.07\.04 Future State Process

Pivot will leverage NetSuite's advanced analytics capabilities to support sophisticated business intelligence requirements beyond standard reporting\. Sandra Rudloff and finance staff will create custom calculated fields for complex GP calculations, profitability metrics, and furniture dealer\-specific KPIs, making these metrics available throughout NetSuite's reporting infrastructure\.

Users will access advanced visualizations through SuiteAnalytics dashboards showing trend analysis, period\-over\-period comparisons, and interactive charts supporting data exploration\. Sales operations will monitor performance trends identifying patterns across territories, product lines, and market segments\. Finance staff will analyze profitability trends by project type, customer segment, and service category, identifying optimization opportunities\.

When specialized analytics are needed beyond NetSuite's native capabilities, IT staff will leverage API connections feeding external platforms\. Power BI \(if maintained\) will receive scheduled data exports or establish real\-time connections to NetSuite, enabling specialized visualizations and advanced statistical analysis while NetSuite remains the authoritative data source\.

Project managers will use what\-if scenario modeling to evaluate budget alternatives before committing to project decisions\. They will adjust assumptions for labor costs, material pricing, and indirect expenses, comparing scenarios to identify optimal project approaches\. Controllers

Automated analytical workflows will execute scheduled analyses, generate exception alerts when metrics exceed thresholds, and distribute insights to stakeholders without manual intervention\. This automation will ensure decision\-makers receive timely analytics supporting proactive business management\.

3\.07\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.07\.01

Predictive analytics for project profitability forecasting

SuiteAnalytics with trend forecasting and regression analysis

ALIGNS

2REQ\-3\.07\.02

Custom KPI development for furniture dealer\-specific metrics

Custom calculated fields and formulas integrated with reporting

ALIGNS

REQ\-3\.07\.03

Advanced data visualization beyond standard dashboards

SuiteAnalytics with interactive charts and pivot analysis

ADAPT

REQ\-3\.07\.04

Integration with external analytics platforms

SuiteAnalytics Connect is an advanced add\-on that provides direct backend database access to NetSuite data through industry\-standard database drivers\. It is a separate module that must be purchased in addition to SuiteAnalytics\. Drivers are provided at no additional cost once the module is licensed\.

ACCOMMODATE

REQ\-3\.07\.05

Custom calculated fields for complex business logic

Point\-and\-click formula builder with NetSuite data access

ALIGNS

REQ\-3\.07\.06

Trend analysis and period\-over\-period comparisons

SuiteAnalytics comparative reporting with dynamic filtering

ALIGNS

REQ\-3\.07\.07

What\-if scenario modeling for project budgeting

Saved searches with parameter inputs and side\-by\-side comparison

ADAPT

REQ\-3\.07\.08

API access for custom analytics integrations

SuiteAnalytics Connect is an advanced add\-on that provides direct backend database access to NetSuite data through industry\-standard database drivers\. It is a separate module that must be purchased in addition to SuiteAnalytics\. Drivers are provided at no additional cost once the module is licensed\.

ACCOMMODATE

__*Client Feedback*__

__*GSI Response*__

<Comment>

 

# <a id="_Toc221887140"></a>__4 SuiteApps__

## <a id="_Toc221887141"></a>__4\.01 SuiteApp Summary__

__No SuiteApps Required for Business Intelligence & Reporting__

NetSuite Orion's native business intelligence and reporting capabilities satisfy most of Pivot Interiors' requirements without requiring third\-party SuiteApps\. Access to raw data needs additional suiteapp\. The platform's standard functionality provides:

- Real\-time dashboards and analytics
- Flexible saved search capabilities
- Comprehensive standard reporting
- Data export and distribution tools
- Integrated document management

All BI requirements identified during discovery sessions can be met through configuration of NetSuite's native features and Orion's furniture dealer\-specific enhancements\.

__Power BI Consideration:__ During discovery sessions, there was discussion of maintaining Power BI for specialized analytics\. This would be addressed as a future\-phase consideration after initial NetSuite implementation, using NetSuite's data export capabilities to feed Power BI if desired\. However, NetSuite's native BI tools are expected to satisfy the majority of reporting requirements, potentially eliminating the need for external BI platforms\.

<a id="_heading=h.3ob7dgy"></a>__*Client Feedback*__

<a id="_heading=h.23ghnor"></a>__*GSI Response*__

<Comment>

# <a id="_Toc221887142"></a>__5 Assumptions__

The following is a list of assumptions based on the solutions proposed in this document\.

__Document Section__

__Assumptions__

3\.01 Core NetSuite BI Tools

\- Users will adapt from D365's limited reporting to NetSuite's comprehensive BI tools through training

\- Business users with Crystal Reports experience will quickly learn NetSuite saved searches

\- Real\-time data access will eliminate most Excel\-based reporting workarounds

3\.02 Dashboard & Analytics

\- Dashboard configurations will be finalized during Realize phase based on user role definitions

\- Cash Flow360 dashboard will use standard NetSuite configuration

\- Dual GP tracking \(actual vs\. commissionable\) is configured as standard Orion feature

3\.03 Standard Reporting

\- Standard NetSuite AP, AR, and WIP reports will replace D365 reports without customization

\- Report formatting preferences will be configured during Realize phase

\- Historical data from D365 will be migrated to support historical reporting

3\.04 Business Intelligence Tools

\- Sandra Rudloff has experience with Crystal Reports and will lead saved search creation

\- Saved search templates will be provided by GSI as starting points for common scenarios

3\.05 Data Export & Distribution

\- Excel will remain the primary tool for ad\-hoc analysis requiring external manipulation

\- Scheduled report distribution will be configured during Realize phase

\- CSV, excel & PDFs export integration points will be defined based on external system requirements

\- PDF formatting will use standard NetSuite templates with minimal customization

3\.06 Document Management

\- Existing project and customer documents will be migrated to NetSuite File Cabinet

\- Document organization structure will be defined during Realize phase

\- Network drive and SharePoint will be phased out for project documentation

\- Version control will be applied prospectively; historical versions may not be preserved

3\.07 Advanced Analytics & Customization

\- Custom calculated fields will be defined during Realize phase based on business requirements

\- SuiteAnalytics capabilities will be configured as part of standard implementation

\- Power BI integration \(if needed\) will be addressed as post\-implementation enhancement

\- Predictive analytics will use historical data migrated from D365

\- API access will be configured based on specific integration requirements identified during Realize phase

<a id="_heading=h.spk1rgn9b34d"></a>__*Client Feedback*__

<a id="_heading=h.uwufyw5z0tji"></a>__*GSI Response*__

<Comment>

# <a id="_Toc221887143"></a>__6 Unresolved Requirements__

To be populated pending Business Requirements Document review with the Pivot team\.

Data has been added to the team’s folder\. Pending reporting demo

__Area__

__Description__

__Impact__

__Proposed Mitigation Strategy__

__Pivot Interiors Feedback__

Power BI Integration

Determine if Power BI will be maintained for specialized analytics post\-implementation

Low \- Does not affect Phase 1 implementation

Evaluate after NetSuite BI capabilities are fully deployed

Historical Data Migration

Define scope of historical data migration for audit trail continuity

Medium \- Affects data migration workload and timeline

Document during data migration planning

Custom KPI Definitions

Finalize specific custom calculated fields and formulas for furniture dealer metrics

Medium \- Affects Realize phase configuration timeline

Document custom KPI requirements during Realize phase kickoff

API Integration Specifications

Define specific external analytics tools requiring API integration

Low \- Can be addressed post\-implementation

Document integration requirements if Power BI or other platforms are confirmed

# <a id="_Toc221887144"></a>__7 Signatures__

Sign\-off represents agreement on behalf of both Client and GSI of the Business Requirements for this process area of the NetSuite Orion implementation\. Sign\-off provides the go\-ahead to begin the Realize stage\.

__Pivot Interiors, Inc\.__

<a id="_heading=h.3tfr8if"></a>__GSI Inc\.__

Signature:

Signature:

Date:

Date:

Name:

Name:

Title:

Title:

Email:

Email:

<a id="_heading=h.28l1iq8"></a>

