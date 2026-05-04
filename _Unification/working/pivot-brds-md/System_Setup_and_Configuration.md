# Pivot BRD — System Setup and Configuration

_Source: `System Setup and Configuration/Pivot/4 BRD/01_Pivot Interiors BRD Setup & Configuration Process Area_v2.0.docx`_

---

__               __

__              __

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation  __

__                   Setup and Configuration Process Area__

__Prepared for: Pivot Interiors__

__Version 2\.0__

__Date: February 13, 2026__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

__Janet Goldstein \(NetSuite Functional Consultant\)__

__Jeanine Post \(NetSuite Functional Consultant\)__

## <a id="_Toc221888632"></a>Table of Contents 

Table of Contents

[Table of Contents	2](#_Toc221888632)

[1 Version Control	3](#_Toc221888633)

[2 Project Definition	4](#_Toc221888634)

[2\.01 Executive Summary	4](#_Toc221888635)

[2\.02 Company Overview	4](#_Toc221888636)

[2\.03 NetSuite Orion Overview	5](#_Toc221888637)

[2\.04 Project Overview	5](#_Toc221888638)

[2\.05 Document Objectives	6](#_Toc221888639)

[3 Setup and Configuration	7](#_Toc221888640)

[3\.01 Company Structure & Subsidiaries	7](#_Toc221888641)

[3\.02 Accounting Periods & Calendar	9](#_Toc221888642)

[3\.03 Currency & Exchange Rates	10](#_Toc221888643)

[3\.04 Native Segmentation	12](#_Toc221888644)

[3\.05 Custom Segmentation & Orion Enhancements	13](#_Toc221888645)

[3\.06 Chart of Accounts	14](#_Toc221888646)

[3\.07 System Preferences & Features	16](#_Toc221888647)

[3\.08 Location and Warehouse Management	18](#_Toc221888648)

[3\.09 User Roles & Permissions	20](#_Toc221888649)

[3\.10 Item Master Management	22](#_Toc221888650)

[3\.11 Data Migration Overview	24](#_Toc221888651)

[3\.12 Document Management	26](#_Toc221888652)

[4 SuiteApps	30](#_Toc221888653)

[4\.01 SuiteApp Summary	30](#_Toc221888654)

[1\.	Super Sync bundle which facilitates the synchronization with Outlook and all the relevant NetSuite records	30](#_Toc221888655)

[5 Assumptions	30](#_Toc221888656)

[6 Unresolved Requirements	30](#_Toc221888657)

[7 Signatures	31](#_Toc221888658)

# <a id="_Toc221888633"></a>1 Version Control 

Version

Author

Comments

Date

0\.1

Jeanine Post

Initial Draft

11/05/2025

0\.2

Janet Goldstein

Review

11/24/2025

0\.3

Debbie Herbert

Updated Draft

12/03/2025

0\.4

Debbie Herbert

Updated Draft

12/18/2025

1\.0

Debbie Herbert, Chris Trumble

Final Draft

12/22/2025

2\.0

Sandra Massey, Chris Trumble

Final for Approval

02/13/2026

# <a id="_Toc221888634"></a>2 Project Definition 

## <a id="_Toc221888635"></a>2\.01 Executive Summary

This Business Requirements Document validates the alignment between Pivot Interiors' foundational business setup requirements and the NetSuite Orion solution capabilities\. Based on comprehensive discovery sessions conducted on July 8, 2025, and August 13, 2025, and subsequent meetings, this document addresses the critical setup and configuration requirements that will establish the foundation for Pivot's unified business management platform\.

Pivot Interiors operates as a single legal entity across two California locations with a straightforward organizational structure that ALIGNs well with NetSuite Orion's standard configuration capabilities\. The company's current Microsoft Dynamics 365 implementation provides line\-level financial segmentation, multi\-dimensional reporting, and project\-based transaction tracking \- all requirements that NetSuite Orion's standard functionality fully supports\. The discovery process identified minimal customization needs, with most requirements aligning directly with proven NetSuite Orion capabilities designed specifically for contract furniture dealers\.

__Alignment Statistics: __Approximately 85% of requirements ALIGN with standard NetSuite Orion functionality, 10% require process ADAPTATION to leverage best practices, and only 5% require ACCOMMODATION through custom configuration \(primarily project numbering schemes\)\.

Key setup decisions include maintaining Pivot's 12\-period fiscal calendar year \(with consideration for 13 periods pending accounting review\), implementing line\-level segmentation for detailed financial reporting, using SuiteTax rather than Avalara for multi\-state tax compliance across 37 states, cutover data like open orders will no be integrated to the migration\. This document validates that the standard NetSuite Orion platform successfully addresses Pivot's setup and configuration requirements while positioning the organization for scalable growth\.

## <a id="_Toc221888636"></a>2\.02 Company Overview

Pivot Interiors, Inc\. is a leading California\-based design firm recognized for its team of innovators, creators, and thought leaders who specialize in delivering exceptional interior solutions for businesses of all sizes\. Their work captures the essence of each client’s brand while fostering environments that inspire employees to thrive, create, and collaborate\. Headquartered in the Bay Area, Pivot Interiors operates offices and Design Centers across the state, including Santa Clara, Fremont, San Francisco, Costa Mesa, Los Angeles, and La Mirada\. As a MillerKnoll Certified Dealer, Pivot Interiors invites clients to experience its uniquely crafted spaces and the distinctive quality that defines the Pivot Interiors brand\.

[__https://www\.pivotinteriors\.com__](https://www.pivotinteriors.com/)

## <a id="_Toc221888637"></a>2\.03 NetSuite Orion Overview

NetSuite provides cloud\-based Enterprise Resource Planning \(ERP\) with the Financial Premium SKU delivering comprehensive financial management, order management, procurement, inventory, and business intelligence capabilities\. The platform architecture enables real\-time visibility, automated workflows, and scalable multi\-entity management in a unified database accessible from any device\.

The Orion Suite consists of five pre\-built SuiteApps specifically designed for contract furniture dealers, providing industry\-specific functionality including Smart Table for line\-item detail management, project\-centric transaction workflows, vendor cross\-reference \(Catalog Code Manager\), enhanced quoting and order management, and sophisticated commission calculations\. These applications leverage NetSuite's platform capabilities while addressing unique furniture industry requirements not supported by generic ERP systems\.

Key differentiators from Pivot's current D365 environment include unified customer master eliminating HubSpot/D365 synchronization\. HubSpot integration will be further explored after go\-live to ensure alignment with Pivot’s marketing and CRM strategy\.

## <a id="_Toc221888638"></a>2\.04 Project Overview

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

## <a id="_Toc221888639"></a>2\.05 Document Objectives

The purpose of this document is to summarize functional and procedural requirements captured by GSI during the Discover business process mapping phase of the implementation\. 

This Business Requirements Document \(BRD\) documents your goals, the problems you want to solve, and the outcomes you expect\. It is the foundation for the setup of the system, acting as a __roadmap between your business needs and the solution design__\.

This document represents information gathered in meetings held with the Client, which enables the GSI team to map the business requirements to an efficient flow in the NetSuite Orion application\. Once complete, this document will serve as a blueprint for the GSI team to configure the application\. This document does not supersede the Statement of Work\. The Statement of Work determines scope\. 

A series of process mapping discovery sessions, focusing on the key areas of the business, were used as a starting point for this exercise\. This document remains consistent in structure to those discovery sessions as it categorizes the findings into the same key process areas\. The set of business requirements documentation is inclusive of all business requirements provided by the Client\.

# <a id="_Toc221888640"></a>3 Setup and Configuration

## <a id="_Toc221888641"></a>3\.01 Company Structure & Subsidiaries

3\.01\.01 Your Business Requirements

- __REQ\-1\.01\.01: __Single legal entity with no subsidiary management complexity__ __
- __REQ\-1\.01\.02: __two\-location operational visibility \(Fremont and La Mirada\)
- __REQ\-1\.01\.03: __US currency operations \(no international requirements\)__ __
- __REQ\-1\.01\.04: __Future scalability for subsidiary expansion if business requires

3\.01\.02 Current State Process

Pivot operates as a single US legal entity using D365 dimensional reporting for location visibility across two California locations\. While D365 provides subsidiary management functionality, Pivot has not utilized this capability\. The company transacts exclusively in US currency, eliminating multi\-entity consolidations, inter\-company eliminations, or currency translation requirements\. Current dimensional approach requires manual report configuration for cross\-dimensional analysis, creating delays in financial insights\.

3\.01\.03 NetSuite/Orion Solution

NetSuite Orion provides flexible entity management scaling from single\-entity operations to complex multi\-subsidiary structures without infrastructure changes\. For Pivot's current single\-entity structure, the platform delivers streamlined setup with US currency as the base currency, eliminating translation complexity while maintaining capability to add subsidiaries or international currencies if future business expansion requires\. This architecture ensures Pivot's implementation remains simple today while preserving growth optionality\.

The solution's location management enables distinct operational visibility across all two California locations within a single legal entity\. Each location functions as warehouse \(Fremont & La Mirada\), Showrooms, sales office, or both, with independent inventory tracking, location\-specific financial reporting, and user access controls\. This provides operational segmentation without separate legal entity administrative overhead\. NetSuite's location architecture integrates seamlessly with inventory management, enabling real\-time stock visibility by location, inter\-location transfers, and location\-specific fulfillment workflows\.

Unlike D365's dimensional approach requiring manual report configuration, NetSuite's location field provides filtering, rollup, and drill\-down capabilities across all standard reports and dashboards\. Users switch location context with single click viewing location\-specific data or consolidating across all locations for enterprise\-wide analysis\. Location structure supports hierarchical relationships \(regions containing locations\), enabling future organizational scaling if Pivot expands beyond California\.

NetSuite Orion's standard OneWorld functionality \(not required for Pivot's current needs and would need to be purchased and implemented\) remains available should future acquisitions, international expansion, or legal structure changes necessitate subsidiary management\. Platform architecture ensures adding subsidiaries later requires configuration changes rather than system replacement, protecting Pivot's implementation of investment while maintaining operational simplicity for current requirements\.

3\.01\.04 Future State Process

Pivot operates a single NetSuite entity with US currency, maintaining clear operational distinction across two California locations through location segmentation\. Financial reporting aggregates across all locations for consolidated P&L and balance sheet while supporting location\-level analysis for operational management\. Each warehouse/office location has dedicated location records enabling location\-specific inventory tracking, transaction filtering, and performance analysis\.

Users access location\-specific views through standard NetSuite filtering, with favorites and saved searches providing one\-click access to frequently used location\-filtered reports\. The simplified structure eliminates inter\-company transaction complexity and currency translation while preserving the ability to scale if business needs to change\. Location managers have visibility into their specific location operations while corporate management maintains enterprise\-wide visibility across all locations\.

3\.01\.05 Decision Matrix

<a id="_Hlk213148141"></a>REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

<a id="_Hlk213246969"></a>REQ\-3\.01\.01

Single legal entity with no subsidiary management complexity

Standard single\-entity configuration

ALIGN

Simplified setup and administration

REQ\-3\.01\.02

two\-location operational visibility

Warehouses were also loaded in NetSuite

NetSuite location management

ALIGN

Operational segmentation maintained

REQ\-3\.01\.03

US currency operations \(no international requirements\)

Base currency configuration

ALIGN

Eliminates currency translation

REQ\-3\.01\.04

Future scalability for subsidiary expansion

OneWorld functionality available

ALIGN

Protects investment for future growth

## <a id="_Toc221888642"></a>3\.02 Accounting Periods & Calendar

3\.02\.01 Your Business Requirements

- __REQ\-3\.02\.01: __13\-period accounting calendar \(12 months period\)
- __REQ\-3\.02\.02: __Calendar year fiscal year \(January\-December\)
- __REQ\-3\.02\.03: __Period\-level locking with selective reopening capability__ __
- __REQ\-3\.02\.04: __7\-day close window supporting backdating for labor cost matching__ __
- __REQ\-3\.02\.05: __Automated period opening upon prior period close__ __
- __REQ\-3\.02\.06: __Approval workflow for period reopening requests

3\.02\.02 Current State Process

Pivot operates a 12\-period calendar in D365 with year\-end adjustments posted to December\. Controller Connie Chung manages a 10\-day period close with backdating for labor cost timing\. The current system requires manual period opening and administrator involvement for period reopening, creating administrative overhead\. The team prefers a 13\-period structure with a dedicated adjustment period for cleaner separation of operational vs\. adjusting entries\.

3\.02\.03 NetSuite Orion Solution

NetSuite provides a 13\-period calendar standard for businesses requiring a clean adjustment <a id="_Int_tyL85ur9"></a>period separation\. Automated period opening is not standard, but a script can be written to trigger the opening of the next period upon authorized close, eliminating manual administration\. Selective period reopening enables specific period adjustments without impacting other closed periods\. The period locking mechanism allows granular control with multi\-level approval available for reopening\. Approval workflows route reopening requests through management with automatic re\-close after adjustment posts\.

3\.02\.04 Future State Process

Connie monitors the close checklist via a NetSuite dashboard\. Upon completion \(7 days post\-month\-end\), a single\-click close triggers automated next period opening with stakeholder notifications\. A period reopening request will be routed through an approval workflow, enable specific adjustments, then auto\-re\-close\. Period 13 remains open through an audit/year\-end close for year\-end adjustments without impacting December operations\.

3\.02\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.02\.01

12\-period accounting calendar

Standard accounting periods configuration

ADAPT

Clean adjustment separation

REQ\-3\.02\.02

Calendar year fiscal year

Standard fiscal year configuration

ALIGN

Current practice maintained

REQ\-3\.02\.03

Period\-level locking with selective reopening capability

Period close and unlock functionality

ALIGN

Financial integrity

REQ\-3\.02\.04

7\-day close window supporting backdating for labor cost matching

Transaction dating controls

ALIGN

Labor cost matching

REQ\-3\.02\.05

Automated period opening upon prior period close

Custom SuiteScript

ACCOMMODATE

Eliminates lag time for beginning AP for the next month

REQ\-3\.02\.06

Approval workflow for period reopening requests

Periods unlock approval workflow

ALIGN

Controlled adjustments

## <a id="_Toc221888643"></a>3\.03 Currency & Exchange Rates

3\.03\.01 Your Business Requirements

- __REQ\-3\.03\.01: __US Dollar as base currency for all operations__ __
- __REQ\-3\.03\.02: __No multi\-currency requirements \(no international transactions\)
- __REQ\-3\.03\.03: __No currency exchange rate management needed__ __
- __REQ\-3\.03\.04: __Future capability to add currencies if business expands internationally

3\.03\.02 Current State Process

Pivot operates exclusively in US currency with no Canadian or international transaction requirements\. D365 configured with USD base currency; multi\-currency functionality unused\. This straightforward approach eliminates currency translation complexity, exchange rate management, and multi\-currency reporting requirements\.

3\.03\.03 NetSuite Orion Solution

NetSuite Orion provides flexible currency management supporting single currency operations today with the capability \(by converting to OneWorld\) to add multiple currencies and automated exchange rate management if future international expansion requires\. For Pivot's current US\-only operations, base currency will be configured as USD with multi\-currency features disabled, eliminating unnecessary system complexity\.

Should future business needs require international currencies \(Canadian operations, international vendors, foreign customers\), NetSuite's Multi\-Currency Management \(MCM\) functionality can be enabled without system replacement IF your base currency is fixed for the entire account, you do not have different base currencies by entity, and you do not have true consolidated reporting across entities\. MCM supports unlimited currencies with automated exchange rate updates from central banks, transaction\-date exchange rates, realized/unrealized gain/loss tracking, and multi\-currency financial reporting\. NetSuite OneWorld needs evaluation if more functionality is needed for international operations\.

3\.03\.04 Future State Process

All Pivot transactions are processed in US currency\. Financial statements, customer invoices, vendor bills, and management reports display in USD with no currency conversion calculations\. System configuration remains simple, focused on single\-currency operations\.

3\.03\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.03\.01

US Dollar as base currency for all operations

Base currency configuration

ALIGN

Clean adjustment separation

REQ\-3\.03\.02

No multi\-currency requirements \(no international transactions\)

Multi\-currency features disabled

ALIGN

Current practice maintained

REQ\-3\.03\.03

No currency exchange rate management needed

No rate management required

ALIGN

Financial integrity

REQ\-3\.03\.04

Future capability to add currencies if business expands internationally

Multi\-Currency Management \(MCM\) available

ALIGN

Growth flexibility

## <a id="_Toc221888644"></a>3\.04 Native Segmentation

3\.04\.01 Your Business Requirements

- __REQ\-3\.04\.01: __Location tracking \(two California locations\)__ __
	-  Fremont and La Mirada
- __REQ\-3\.04\.02: __Division \(Class\) tracking for operational segments
- __REQ\-3\.04\.03: __Line\-level dimensional tagging on all transactions__ __
- __REQ\-3\.04\.04: __Instant P&L generation by Division \(Class\), Department, and Location
- __REQ\-3\.04\.05: __Cross\-dimensional reporting \(Location \+ Division \(Class\) combinations
- __REQ\-3\.04\.06: __Mandatory segment selection on transactions to ensure data integrity__ __
- __REQ\-3\.04\.07: __Department segmentation for cost center tracking

3\.04\.02 Current State Process

Pivot uses D365 dimensions for location and division visibility, but reporting requires manual configuration and Power BI exports for cross\-dimensional analysis, creating delays and IT dependencies\.

3\.04\.03 NetSuite Orion Solution

NetSuite Orion delivers native multi\-dimensional segmentation using Locations and Classes \(renamed Divisions\)\. Transactions can be tagged at header and line level, with overrides for multi\-location or multi\-division scenarios\. Built\-in reporting enables instant P&L by Location, Division, or combined views without custom development\. Mandatory segment selection ensures data integrity\. This eliminates manual exports and accelerates decision\-making\.

3\.04\.04 Future State Process

Users select Location and Division on transaction headers\. Reports and dashboards provide real\-time visibility by Location, Division, or combined dimensions\.

Dimensions can be tracked at the customer level if needed but the leading practices indicate that is best to track segmentation at the transaction level

3\.04\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.04\.01

Location tracking \(two California locations\) and warehouses were included in the configuration\.

NetSuite Locations

ALIGN

Six\-location visibility

REQ\-3\.04\.02

Division \(Class\) tracking for operational segments

NetSuite Class segment renamed Division

ALIGN

Operational segment tracking

REQ\-3\.04\.03

Mandatory dimensional tagging on transactions

Transaction validation rules

ALIGN

Complete segmentation

REQ\-3\.04\.04

Instant P&L generation by Division \(Class\), Department, Location

Native dimensional reporting engine

ALIGN

Real\-time financial insights

REQ\-3\.04\.05

Cross\-dimensional reporting \(Location \+ Division \(Class\) combinations\)

Native reports, SuiteAnalytics dimensional filters

ALIGN

Combined dimension analysis

REQ\-3\.04\.06

Mandatory data selection on transactions to ensure complete segmentation

Transaction validation rules

ALIGN

Complete segmentation

REQ\-3\.04\.07

Department segmentation

NetSuite Departments

ALIGN

Cost center tracking

## <a id="_Toc221888645"></a>3\.05 Custom Segmentation & Orion Enhancements

3\.05\.01 Your Business Requirements

- __REQ\-3\.05\.01: __Vertical Market segmentation \(Healthcare, Education, Corporate, Government\)
- __REQ\-3\.05\.02: __Ability to add new custom segments as business evolves

3\.05\.02 Current State Process

Pivot lacks integrated department\-level cost tracking and vertical market profitability analysis\. Multi\-dimensional views require manual Power BI dashboards\.

3\.05\.03 NetSuite Orion Solution

Beyond standard dimensions, Orion supports unlimited Custom Segments for vertical markets and other attributes\. Departments are native and provide cost center tracking\. Custom Segments behave like Classes—taggable at header and line level, fully integrated with reporting\. Users can generate P&L by any combination \(e\.g\., Location \+ Department \+ Market\) without custom development\. New segments can be added through configuration, future\-proofing the architecture\.

3\.05\.04 Future State Process

Transactions include Location, Division, Department, and Market tags\. Reports deliver instant profitability analysis across any dimension combination\.

3\.05\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.05\.01

Vertical Market segmentation

Custom Segment: Markets

ALIGN

Market profitability analysis

REQ\-3\.05\.02

Ability to add new custom segments

Custom Segment architecture

ALIGN

Business evolution support

## <a id="_Toc221888646"></a>3\.06 Chart of Accounts

3\.06\.01 Your Business Requirements

- __REQ\-3\.06\.01: __Import existing 200\-250 active accounts \(or inactive accounts if historical balances exist\) from D365__ __
- __REQ\-3\.06\.02: __Flexible account structure leveraging dimensional reporting__ __
- __REQ\-3\.06\.03: __Account hierarchy with parent\-child relationships for rollup reporting__ __
- __REQ\-3\.06\.04: __Project labor costing with dedicated GL accounts
- __REQ\-3\.06\.05: __1099 vendor expense tracking integrated with accounts
- __REQ\-3\.06\.06: __Statistical account evaluation for non\-financial metrics__ __
- __REQ\-3\.06\.07: __Budget vs\. actual reporting at account level

3\.06\.02 Current State Process

Pivot maintains 200\-250 active accounts in D365 including location\-specific revenue and expense accounts\. Kevin Baugh \(CFO\) manages the master chart of accounts requiring extensive customization for dimensional analysis, creating monthly reporting burden through Excel exports and manual consolidation\. The current structure includes location\-specific accounts but the team is exploring whether the simplified structure leveraging NetSuite dimensional reporting provides same visibility with reduced account complexity\.

3\.06\.03 NetSuite Orion Solution

NetSuite's flexible chart of accounts works seamlessly with dimensional segmentation, enabling either streamlined account structure or current location\-specific approach based on business preference\. Dimensional reporting capability means Pivot can simplify accounts \(single revenue account vs\. Two location\-specific revenue accounts\) while maintaining location\-based reporting through dimensional filtering\. Alternatively, current location\-specific structure can be maintained if preferred for consistency with historical practices\.

Parent\-child account hierarchies support unlimited rollup reporting\. Summary accounts aggregate child account balances without accepting direct postings\. NetSuite basic budget module provides instant variance analysis with dimensional drill\-down\. 1099 tracking integrates directly—vendor records flagged for 1099 tracking; expense accounts designated as 1099\-eligible; year\-end 1099 forms are generated and filed using a paid service such as Yearli\. Statistical accounts enable non\-financial metrics \(headcount, square footage, units\) with same dimensional capabilities as financial accounts, enabling KPIs like revenue per employee analyzed by location and department\.

The implementation imports the complete chart of accounts structure including account types, descriptions, hierarchies, and beginning balances\. Account maintenance moves to the finance team through a standard NetSuite interface without IT involvement for adding accounts or adjusting hierarchies\.

3\.06\.04 Future State Process

Finance maintains the chart of accounts through the NetSuite standard interface\. New accounts are added quickly without IT involvement; account hierarchies can be adjusted to support evolving reporting needs\. Budget vs\. actual reports are generated within the basic budgeting module with dimensional filters, eliminating Excel exports\. Statistical accounts \(if implemented\) track operational metrics alongside financial data— such as headcount by department, square footage by location—enabling metrics like revenue per employee or revenue per square foot analyzed by location and department\.

P&L reports can be created to leverage natural account rollups, or other desired account groupings, to drill down to the transaction level\.

3\.06\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.06\.01

Import 200\-250 accounts

CSV import with hierarchy

ALIGN

Seamless D365 transition

REQ\-3\.06\.02

Flexible structure

Dimensional \+ account config

ADAPT

Simplified or current structure

REQ\-3\.06\.03

Account hierarchy

Parent\-child relationships

ALIGN

Rollup reporting

REQ\-3\.06\.04

Project labor accounts

Custom accounts \+ dimensions

ALIGN

Accurate project costing

REQ\-3\.06\.05

1099 tracking

Native 1099 functionality

ALIGN

Automated compliance

REQ\-3\.06\.06

Statistical accounts

Statistical account feature

ALIGN

Non\-financial metrics

REQ\-3\.06\.07

Budget vs\. actual

Budget module

ALIGN

Real\-time variance analysis

## <a id="_Toc221888647"></a>3\.07 System Preferences & Features

3\.07\.01 Your Business Requirements

- __REQ\-3\.07\.01: __Enable required NetSuite features for Pivot operations \(Advanced Financials, Advanced Inventory, Projects, etc\.\)
- __REQ\-3\.07\.02: __Configure system preferences aligned with Pivot business practices
- __REQ\-3\.07\.03: __Disable unnecessary features reducing system complexity__ __
- __REQ\-3\.07\.04: __Enable Orion\-specific features for furniture industry functionality__ __
- __REQ\-3\.07\.05: __Configure transaction numbering and auto\-generation preferences

3\.07\.02 Current State Process

D365 was configured with various features and preferences accumulated over time\. Some features are heavily utilized with others enabled but unused creating unnecessary system complexity\. The team seeks a clean NetSuite configuration focused on required functionality with unnecessary features disabled for simplified user experience and reduced training burden\.

3\.07\.03 NetSuite Orion Solution

NetSuite provides granular feature enablement allowing precise activation of only required functionality\. System preferences control behaviors like transaction numbering, decimal places, default values, and workflow behaviors\. Orion adds furniture industry\-specific features including Smart Table for SIF file display, project\-based workflows, and specialized furniture dealer reports\. Implementation begins with minimal feature set, enabling additional features only as business requirements dictate\. This approach keeps the system simple, reduces training needs, and minimizes unused functionality cluttering user interface\.

Key features for Pivot include: Multi\-Location Inventory, Projects, Classes, Departments, Custom Segments, Advanced PDF/HTML Templates, Approval Routing, SuiteAnalytics, Bank Feeds, and Orion\-specific furniture features\. Features not required for Phase 1 remain disabled \(Advanced Financials components like Revenue Recognition, Fixed Assets until Phase 2, Multi\-Currency, etc\.This modules are free \)\.

There is not additional additional cost for the modules except for installation, configuration and costs

System preferences configured matching Pivot business practices: transaction numbering schemes, required fields, default values, approval thresholds, and workflow behaviors\. Preferences establish the foundation for consistent data entry and process execution across all users\.

3\.07\.04 Future State Process

NetSuite features that are enabled support Pivot's Phase 1 scope with unnecessary features disabled\. Users experience clean interfaces focused on required functionality without clutter from unused features\. As Phase 2 requirements emerge, additional features will be enabled through standard configuration without system disruption\. System preferences enforce consistent transaction entry with required fields, appropriate defaults, and validation rules preventing common data entry errors\. Transaction numbering follows consistent schemes providing meaningful identifiers while maintaining system integrity\.

3\.07\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.07\.01

Enable required features

Feature management

ALIGN

Focused functionality

REQ\-3\.07\.02

Configure preferences

System preferences

ALIGN

Business practice alignment

REQ\-3\.07\.03

Disable unnecessary features

Feature management

ALIGN

Reduced complexity

REQ\-3\.07\.04

Enable Orion features

Orion furniture functionality

ALIGN

Industry\-specific capabilities

REQ\-3\.07\.05

Enable Orion features

Numbering preferences

ALIGN

Consistent identification

## <a id="_Toc221888648"></a>3\.08 Location and Warehouse Management

3\.08\.01 Your Business Requirements

- __REQ\-3\.08\.01: __Configure two locations \(Fremont and La Mirada\), warehouses and sales office combinations
- __REQ\-3\.08\.02: __Enable location\-specific inventory tracking and visibility
- __REQ\-3\.08\.03: __Support inter\-location transfers for inventory movement__ __
- __REQ\-3\.08\.04: __Configure location\-based fulfillment workflows__ __
- __REQ\-3\.08\.05: __Enable location\-specific user access controls__ __
- __REQ\-3\.08\.06: __Support project\-site locations for direct\-ship scenarios

3\.08\.02 Current State Process

Pivot operates two California locations functioning as combination warehouse and sales offices\. D365 location tracking provides basic inventory visibility but lacks robust location\-based workflows and reporting\. Inter\-location transfers require manual coordination\. Location\-based security controls are limited, requiring workarounds for restricting user access to specific locations\. Project\-site deliveries are tracked separately from warehouse locations\.

3\.08\.03 NetSuite Orion Solution

NetSuite's Multi\-Location Inventory provides comprehensive location management with each location functioning as an independent inventory tracking entity\. Locations configured as warehouses, sales offices, or both with location\-specific: inventory on\-hand tracking, item receipt/fulfillment transactions, location\-specific reorder points, and dedicated location users\. This architecture enables real\-time inventory visibility by location with drill\-down to item\-location detail\.

Inter\-location transfers process through standard NetSuite transfer orders, tracking inventory movement between locations with proper GL accounting \(inventory value transfers between location asset accounts\)\. Transfer orders support approval workflows for controlled inventory movement and provide complete audit trails\.

Orion's project\-based architecture supports project\-site locations enabling direct\-ship to customer sites with proper inventory and GL accounting without moving through main warehouse locations\.

Location\-specific user access controls restrict users to designated locations— La Mirada warehouse staff see only La Mirada inventory; sales teams access appropriate locations; corporate users view all locations\. This security model ensures proper segregation while maintaining corporate oversight\.

3\.08\.04 Future State Process

Each California location operates as distinct warehouse in NetSuite with independent inventory tracking\. Warehouse staff perform receipts and fulfillment against their specific location; inventory reports show real\-time on\-hand by location\. When San Francisco needs inventory from Los Angeles, the warehouse team creates a transfer order triggering approval workflow; upon approval, LA fulfills transfer, SF receives, and inventory moves between locations with proper GL entries\. Sales orders fulfill from the optimal location based on inventory availability; system recommends location but allows override for business reasons\. Project\-site locations enable direct\-ship to customer facilities with proper inventory tracking without main warehouse involvement\. User access controls ensure location staff see only their location data while corporate management views the consolidated enterprise inventory\.

3\.08\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.08\.01

Six CA locations

Multi\-Location Inventory

ALIGN

Warehouse/office combination

REQ\-3\.08\.02

Location inventory tracking

Location\-based inventory

ALIGN

Real\-time location visibility

REQ\-3\.08\.03

Inter\-location transfers

Transfer orders

ALIGN

Controlled inventory movement

REQ\-3\.08\.04

Location fulfillment

Location\-based workflows

ALIGN

Optimized fulfillment

REQ\-3\.08\.05

Location access controls

Location\-based security

ALIGN

Proper segregation

REQ\-3\.08\.06

Project\-site locations

Orion project\-site capability

ALIGN

Direct\-ship support

## <a id="_Toc221888649"></a>3\.09 User Roles & Permissions

3\.09\.01 Your Business Requirements

- __REQ\-3\.09\.01: __Configure 25\+ customized user roles supporting Pivot organizational structure__ __
- __REQ\-3\.09\.02: __Role\-based access controls limiting users to appropriate data and transactions__ __
- __REQ\-3\.09\.03: __Location\-specific access restrictions for warehouse and sales staff__ __
- __REQ\-3\.09\.04: __Department\-based access for financial and operational roles
- __REQ\-3\.09\.05: __Executive roles with enterprise\-wide visibility
- __REQ\-3\.09\.06: __Approval workflow roles with appropriate transaction limits
- __REQ\-3\.09\.07: __Super\-user roles for power users and administrators

3\.09\.02 Current State Process

D365 is configured with 10\+ user roles but the current structure is complex with overlapping permissions and unclear delineation\. Role maintenance requires IT involvement; adding users or adjusting permissions is time\-consuming\. The team seeks a simplified role structure with clear permission boundaries while maintaining appropriate security controls and segregation of duties\.

3\.09\.03 NetSuite Orion Solution

NetSuite provides sophisticated role\-based security with granular permission controls at feature, transaction, report, and data level\. Orion includes furniture dealer\-specific standard roles \(Sales, Operations, Purchasing, Finance, Executive\) providing the starting point for Pivot customization\. Implementation approach defines 25\+ custom roles matching Pivot's organizational structure with clear permission boundaries and minimal overlap\.

Role architecture includes: base roles \(generic Sales Rep, Warehouse Staff, AP Processor\), location\-specific variants \(SF Sales Rep, LA Warehouse\), department\-specific variants \(Finance Manager, Operations Manager\), approval roles \(PO Approver, Vendor Bill Approver\), and super\-user roles \(Finance Super User, Operations Super User, NetSuite Administrator\)\. This structure provides flexibility while maintaining manageable role count\.

Permissions are configured at multiple levels: Feature access \(can user access Purchasing feature\), Transaction permissions \(create/edit/delete/view for each transaction type\), Report access \(which reports are accessible\), Data restrictions \(location/department/class restrictions\), Field\-level security \(which fields editable\), and Record restrictions \(which customers/vendors/items are visible\)\. This granular control ensures users access only appropriate functionality and data\.

Location\-based restrictions are configured through role\-location mapping—SF Warehouse role restricted to SF location data only; corporate roles access all locations\. Department restrictions follow a similar pattern\. Approval workflows tie to roles with thresholds \(example \- PO Approver role approves POs up to $50K; Senior Approver required above $50K\)\.

3\.09\.04 Future State Process

User assigned single roles match organizational position \(e\.g\., "San Francisco Sales Representative" role\)\. The role determines: accessible NetSuite features and modules, which transactions can be created/edited/viewed, which reports are accessible, location/department data visibility restrictions, approval limits if applicable, and dashboard/center tab configuration\. Users experience a tailored NetSuite interface showing only relevant functionality for their role without clutter from inapplicable features\.

When a new employee joins, the appropriate role is assigned providing immediate access to required functionality\. Role changes process through standard workflow—employee promoted from Sales Rep to Sales Manager; administrator changes role assignment; user receives new permissions immediately\. Role maintenance is centralized with the NetSuite Administrator updating role definitions affecting all users assigned that role simultaneously\.

3\.09\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.09\.01

Configure 25\+ customized user roles supporting Pivot organizational structure

Role\-based security with custom role creation

ALIGN

Organizational structure match

REQ\-3\.09\.02

Role\-based access controls limiting users to appropriate data and transactions

Granular permission model

ALIGN

Appropriate data access

REQ\-3\.09\.03

Location\-specific access restrictions for warehouse and sales staff

Role\-location security restrictions

ALIGN

Location segregation

REQ\-3\.09\.04

Department\-based access for financial and operational roles

Role\-department security restrictions

ALIGN

Department segregation

REQ\-3\.09\.05

Executive roles with enterprise\-wide visibility

Corporate executive role configuration

ALIGN

Enterprise oversight

REQ\-3\.09\.06

Approval workflow roles with appropriate transaction limits

Approval routing to roles with thresholds

ALIGN

Controlled approvals

REQ\-3\.09\.07

Super\-user roles for power users and administrators

Power user and admin role configuration

ALIGN

Controlled approvals

## <a id="_Toc221888650"></a>3\.10 Item Master Management

3\.10\.01 Your Business Requirements

- __REQ\-3\.10\.01: __Simplified item master with 30\-50 items vs\. thousands of individual SKUs__ __
- __REQ\-3\.10\.02: __SIF file import providing line\-item detail without creating NetSuite items__ __
- __REQ\-3\.10\.03: __Generic items for common categories \(seating, tables, case goods, etc\.\)__ __
- __REQ\-3\.10\.04: __Orion Smart Table displaying SIF line\-item detail for quotes and orders__ __
- __REQ\-3\.10\.05: __Service items for internal labor and installation
- __REQ\-3\.10\.06: __Support for item attributes and specifications without full item records

3\.10\.02 Current State Process

D365 is configured with thousands of individual item SKUs creating a massive item master requiring significant maintenance\. Each furniture piece, configuration, and finish creates a separate item record\. The team recognizes this approach creates unnecessary complexity for furniture dealer operations where project specifications come from design systems via SIF files rather than selecting from ERP item catalog\. Pivot seeks a dramatically simplified item approach leveraging Orion's SIF\-based architecture\.

3\.10\.03 NetSuite Orion Solution

NetSuite Orion provides an item master approach for furniture dealers that is fundamentally different from that of a traditional ERP\. Instead of maintaining thousands of item records for every furniture piece/finish/configuration, Orion uses a simplified item master with 30\-50 generic items representing categories \(seating, tables, case goods, filing, accessories, freight, labor, etc\.\)\. Detailed line\-item specifications come from SIF files imported from design systems rather than selected from an item catalog\.

Orion's Smart Table technology displays line\-item detail from SIF files in a visual interface showing: item descriptions, quantities, manufacturer part numbers, finishes, dimensions, lead times, pricing, and all specification details\. This information is stored as JSON data attached to a quote/order rather than creating NetSuite item records\. Users interact with line items through the Smart Table experiencing full visibility and editability without a bloated item master\.

Generic items enable: transaction processing \(quotes, orders, and POs require item selection—generic item satisfies this requirement\), inventory tracking at category level if needed, GL account mapping \(revenue/COGS accounts assigned to generic items\), reporting and analytics by item category, and purchasing workflows \(POs created with generic items, specifications in line detail\)\.

Service items are configured for internal labor categories \(design, project management, installation, delivery\) and other non\-product charges \(freight, fuel surcharge, restocking fees\)\. Service items support time tracking integration if using NetSuite Orion native time tracking\.

This approach dramatically reduces item master maintenance, eliminates SKU proliferation, maintains complete line\-item detail through SIF imports, and provides all required transaction and reporting functionality\.

3\.10\.04 Future State Process

The item master contains 30\-50 generic items organized by category\. To create a  quote, the user imports a SIF file from design system; Smart Table displays hundreds or thousands of line items with complete specifications, pricing, lead times\. The user reviews, adjusts pricing if needed, generates the quote PDF showing full line\-item detail to the customer\. The quote converts to an order; line\-item detail preserved\. Purchasing generates POs with generic item category; PO line detail includes full specifications from SIF\. Receiving processes against the PO with line\-item detail; the warehouse sees complete specifications for verification\. Financial reporting shows revenue and COGS by item category with drill\-down to project detail\. Item master maintenance is minimal —adding a new category or adjusting GL accounts are the only scenarios requiring item master updates\.

3\.10\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.10\.01

Simplified item master with 30\-50 items vs\. thousands of individual SKUs

Orion simplified item master approach

ADAPT

Minimal maintenance

REQ\-3\.10\.02

SIF file import providing line\-item detail without creating NetSuite items

Orion Smart Table with JSON data storage

ALIGN

Complete specifications without items

REQ\-3\.10\.03

Generic items for common categories \(seating, tables, case goods, etc\.\)

Standard Orion category\-based items

ADAPT

Category\-level operations

REQ\-3\.10\.04

Orion Smart Table displaying SIF line\-item detail for quotes and orders

Orion Smart Table UI

ALIGN

Visual line\-item management

REQ\-3\.10\.05

Service items for internal labor and installation

NetSuite service item types

ALIGN

Labor and services tracking

REQ\-3\.10\.06

Support for item attributes and specifications without full item records

Approval routing to SIF JSON data storage for specifications

ALIGN

Specifications preserved

## <a id="_Toc221888651"></a>3\.11 Data Migration Overview

3\.11\.01 Your Business Requirements

- __REQ\-3\.11\.01: __Level 1 migration \(entities and financial history from currently used applications\)
- __REQ\-3\.11\.03A: __Level 3 migration \(open AP and AR\)__ __
- __REQ\-3\.11\.03B: __Level 3 migration \(AI Driven Document Storage\) decision pending based on complexity and cost__ __
- __REQ\-3\.11\.04: __Import 2\-5 years of historical financial data \(trial balances\)__ __
- __REQ\-3\.11\.05: __Clean data quality before migration \(dedupe, standardize\)
- __REQ\-3\.11\.06: __Validate migrated data accuracy through reconciliation__ __
- __REQ\-3\.11\.07: __Maintain D365 available read\-only post\-go\-live for historical reference

3\.11\.02 Current State Process

Pivot's D365 contains years of customer, vendor, employee, financial, and transaction data requiring migration to NetSuite for operational continuity and historical reporting\. Data quality varies—some duplicate customers/vendors, inconsistent naming conventions,

3\.11\.03 NetSuite Orion Solution

Level 1 \- Core Master Data & Financial History:

- All entity records \(customers, contacts, vendors, employees\)
- Chart of accounts with hierarchies
- Historical trial balances \(2\-5 years as journal entries\)
- Configuration data \(terms, price levels, tax codes\)
- Provides foundation for transaction processing and multi\-year financial reporting

Level 2 \- Sales Order History with Line Detail:

- Historical sales orders with full line\-item detail
- Invoice history linked to sales orders
- Customer PO cross\-references
- Pricing history for analysis
- Orion imports SIF data as JSON attachments displaying in Smart Table
- Enables sales history analysis, forecasting, customer buying patterns

Level 3A \- Open Transactions:

- Open AP
- Open AR

3\.11\.04 Future State Process

All active customers, vendors, and employees are migrated to NetSuite with clean data quality \(inactive entities also migrated if necessary to support migrated transaction data\)\. Historical trial balances provide multi\-year financial trending and budget comparisons\. Sales order history is accessible through the Orion Smart Table enabling analysis of customer buying patterns, product mix, and historical pricing\. Open transactions \(if Level 3B is pursued\) seamlessly continue in NetSuite with preserved project linkages and PO relationships\. Data quality metrics validate migration accuracy before go\-live approval\. D365 available for historical reference queries without operational use\.

3\.11\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.11\.01

Level 1 migration \(entities and financial history\)

Standard CSV import and data migration tools

ALIGN

Operational foundation

REQ\-3\.11\.02

N/A

N/A

N/A

N/A

REQ\-3\.11\.03A

Level 3A migration \(open AP and AR\)

Standard CSV import and data migration tools

ALIGN

Operational foundation

REQ\-3\.11\.03B

Level 3 migration \(open orders and POs\) decision pending based on complexity and cost

Automated, simplified, or manual migration options

Pivot won’t be bringing open orders into Orion\.

N/A

Seamless cutover vs\. cost

REQ\-3\.11\.04

Import 2\-5 years of historical financial data \(trial balances\)

Journal entry import for historical periods

ALIGN

Trending and comparisons

REQ\-3\.11\.05

Clean data quality before migration \(dedupe, standardize\)

Pre\-migration data cleansing process

ALIGN

Accurate system data

REQ\-3\.11\.06

Validate migrated data accuracy through reconciliation

Reconciliation reports and validation scripts

ALIGN

Accuracy assurance

REQ\-3\.11\.07

Maintain D365 available read\-only post\-go\-live for historical reference

D365 remains accessible through subscription

ALIGN

Historical continuity

## <a id="_Toc221888652"></a>3\.12 Document Management

3\.12\.01 Your Business Requirements

- __REQ\-1\.12\.01: __SharePoint integration for centralized document management__ __
- __REQ\-1\.12\.02: __Folder structure aligned with customer and project hierarchy__ __
- __REQ\-1\.12\.03: __Document access directly from NetSuite customer, project, and transaction records__ __
- __REQ\-1\.12\.04: __Replace IQ and Workfront document storage consolidating to SharePoint__ __
- __REQ\-1\.12\.05: __Role\-based document access controls__ __
- __REQ\-1\.12\.06: __Automated folder creation for leads, opportunities, and projects__ __
- __REQ\-1\.12\.07: __Version control and document history__ __
- __REQ\-1\.12\.08: __Document templates for quotes, orders, invoices auto\-saving to SharePoint

3\.12\.02 Current State Process

Pivot manages documents across IQ \(receiving documents\), Workfront \(project documents and tasks\), and likely file shares for general documents\. Fragmentation creates challenges finding correct document versions and ensuring team access to current information\. Workfront expires July 2026 creating hard deadline for document migration\. Project documents, quotes, orders, invoices, receiving documents, photos, and drawings are scattered across systems requiring manual searching and coordination\.

3\.12\.03 NetSuite Orion Solution

NetSuite Orion provides native SharePoint integration through the NetSuite standard SharePoint connector, eliminating fragmentation across IQ and Workfront\. GSI \(SharePoint Integration Specialist\) guides folder structure design and integration configuration ensuring documents are organized optimally for Pivot workflows\.

SharePoint connector works bidirectionally—users access SharePoint folders directly from NetSuite records \(customer, project, order, PO\), and SharePoint document libraries are searchable from within NetSuite\. Document creation triggers from NetSuite transactions—a quote created automatically creates SharePoint folder using a naming convention template \(e\.g\., "Customer Name \- Project Number \- Quote"\), and generated PDFs save directly to that folder\.

The folder structure decision is entirely yours to define\. Common patterns: organize by customer → project → document type, or document type → customer → project, or year → customer → project\. Tyler facilitates the design session for reviewing current practices and proposing structures used successfully by other furniture dealers\. Key consideration: balancing ease of navigation with security requirements\.

For early lead scenarios where project details are unknown, SharePoint folders are created at lead or opportunity stage with placeholder naming\. As details firm up, folders are renamed manually following consistent conventions\. The connector supports automated folder creation at various stages with rules determining when folders are created and how they are named\.

Version control native SharePoint functionality persists through integration\. Documents are edited, SharePoint maintains previous versions which are accessible through version history\. Check\-in/check\-out prevents concurrent editing conflicts\. Role\-based access is managed through SharePoint security groups aligned with NetSuite user roles—project coordinator role read/write access to project folders; warehouse staff read\-only access to receiving documents\. Integration respects both NetSuite role permissions and SharePoint folder permissions\.

Document templates for quotes, orders, invoices are created using NetSuite Advanced PDF Templates generating from live transaction data and auto\-saving to SharePoint in designated folders\. Eliminates manual generation and saving to various locations—every quote generates PDF auto\-saving to project folder with consistent naming\.

3\.12\.04 Future State Process

A new trade show lead captured generates a prospect in NetSuite, automatically creates the SharePoint folder: "2026 Leads\\Hospital Prospects\\Contact Name \- Hospital Name\." The sales rep uploads the lead form and notes\. Opportunity progresses, converts to project; the SharePoint connector renames the folder following project naming: "2026 Projects\\Healthcare Vertical\\St\. Mary's Hospital \- Project 428982\." Original documents move automatically\.

Quote generated saves PDF to SharePoint: "2026 Projects\\Healthcare\\St\. Mary's \- 428982\\Quotes\\Quote\-Rev1\-2026\-02\-15\.pdf\." Customer requests revisions; second quote saves "Quote\-Rev2\-2026\-02\-20\.pdf\." Both versions are accessible with revision history\.

Throughout the project, the team accesses documents from NetSuite—a project coordinator opens the project record, clicks "Documents" tab displaying SharePoint folders and files\. Uploads new documents, downloads existing, opens for editing directly in SharePoint without leaving NetSuite\. The warehouse accesses receiving documents from the PO record, uploads damage photos from a tablet appearing automatically in the project folder for coordinator reference during vendor disputes\.

3\.12\.05 Decision Matrix

REQ\-ID

Requirement

NetSuite Orion Capability

Approach

Business Impact

REQ\-3\.12\.01

SharePoint integration for centralized document management

Native NetSuite SharePoint connector

ALIGN

Unified document management

REQ\-3\.12\.02

Folder structure aligned with customer and project hierarchy

Automated folder creation with naming conventions

ALIGN

Consistent organization

REQ\-3\.12\.03

Document access directly from NetSuite customer, project, and transaction records

Document tabs on NetSuite records

ALIGN

Seamless access

REQ\-3\.12\.04

Replace IQ and Workfront document storage consolidating to SharePoint

SharePoint as central document repository

ALIGN

System consolidation

REQ\-3\.12\.05

Role\-based document access controls

SharePoint security groups aligned with NetSuite roles

ALIGN

Appropriate access control

REQ\-3\.12\.06

Automated folder creation for leads, opportunities, and projects

Connector naming convention rules and triggers

ALIGN

Consistent structure

REQ\-3\.12\.07

Version control and document history

SharePoint native version control

ALIGN

Document history preservation

REQ\-3\.12\.08

Document templates for quotes, orders, invoices auto\-saving to SharePoint

Advanced PDF Templates with SharePoint auto\-save

ALIGN

Automated generation

## <a id="_Toc221888653"></a>4 SuiteApps

## <a id="_Toc221888654"></a>4\.01 SuiteApp Summary

## <a id="_Toc221888655"></a>Super Sync bundle which facilitates the synchronization with Outlook and all the relevant NetSuite records

## <a id="_Toc221888656"></a>5 Assumptions

The following is a list of assumptions based on the solutions proposed in this document\.

## <a id="_Toc221888657"></a>6 Unresolved Requirements

To populate pending Business Requirements Document review with the Client team\.

## <a id="_Toc221888658"></a>7 Signatures

Sign\-off represents agreement on behalf of both Client and GSI of the Business Requirements for this process area of the NetSuite Orion implementation\. Sign\-off provides the go\-ahead to begin the Realize stage\. 

 

__Pivot Interiors, Inc\.__ 

__GSI Inc\.__ 

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

 

