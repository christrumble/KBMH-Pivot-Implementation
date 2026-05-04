# Pivot BRD — Commissions

_Source: `Commissions/Pivot/4 BRD/09_Pivot Interiors BRD Commissions Process Area_v1.0.docx`_

---

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation__

__Commissions Process Area__

__Prepared for: Pivot Interiors, Inc\.__

__Version 2\.0__

__Date: February 13, 2026__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

__Sandra Massey \(NetSuite Orion Functional Consultant\)__

# <a id="_Toc217286707"></a>Table of Contents

[Table of Contents	2](#_Toc217286707)

[1 Version Control	3](#_Toc217286708)

[2 Project Definition	4](#_Toc217286709)

[2\.01 Executive Summary	4](#_Toc217286710)

[2\.02 Company Overview	4](#_Toc217286711)

[2\.03 NetSuite Orion Overview	4](#_Toc217286712)

[2\.04 Project Overview	4](#_Toc217286713)

[2\.05 Document Objectives	5](#_Toc217286714)

[3 Commission Management	6](#_Toc217286715)

[3\.01 Commission Plan Configuration	6](#_Toc217286716)

[3\.02 Tiered Commission Calculation	8](#_Toc217286717)

[3\.03 Commission Triggers & Automation	10](#_Toc217286718)

[3\.04 Commission Splits & Allocations	11](#_Toc217286719)

[3\.05 Bonus Structures	13](#_Toc217286720)

[3\.06 Deposit Bonus Processing	15](#_Toc217286721)

[3\.07 Commission Reporting & Reconciliation	17](#_Toc217286722)

[3\.08 Commission Payment Processing	18](#_Toc217286723)

[4 SuiteApps	20](#_Toc217286724)

[4\.01 SuiteApp Summary	20](#_Toc217286725)

[5 Assumptions	20](#_Toc217286726)

[6 Unresolved Requirements	21](#_Toc217286727)

[7 Signatures	22](#_Toc217286728)

[8 Appendix	23](#_Toc217286729)

# <a id="_Toc217286708"></a>1 Version Control

__Version__

__Author__

__Comments__

__Date__

0\.1

Sandra Massey

Initial Draft

12/7/2025

0\.2

Sandra Massey

Updated Draft

12/12/2025

0\.3

Jeanine Post

Updated Draft

12/16/2025

0\.4

Chris Trumble

Updated Draft

12/19/2025

1\.0

Debbie Herbert

Final Draft

12/22/2025

2\.0

Sandra Massey, Chris Trumble

Final for Approval

02/13/2026

# <a id="_Toc217286709"></a>2 Project Definition

## <a id="_Toc217286710"></a>2\.01 Executive Summary

Pivot Interiors is implementing NetSuite Orion to modernize its commission management operations and replace manual processes currently managed through Microsoft Dynamics 365 and Excel spreadsheets\. This Business Requirements Document \(BRD\) captures the business requirements discovered during the Commission Management process mapping phase\.

Through the CRM\-Commissions discovery session conducted on __August 25, 2025, and subsequent meetings__, GSI analyzed Pivot's current state commission processes across multiple sales roles including Account Managers, New Business Development Executives, Customer Success Managers, Key Account Managers, and Construction Solutions Sales Representatives\.

<a id="_Toc217286711"></a>__2\.02 Company Overview__

Pivot Interiors, Inc\. is a leading California\-based design firm recognized for its team of innovators, creators, and thought leaders who specialize in delivering exceptional interior solutions for businesses of all sizes\. Their work captures the essence of each client’s brand while fostering environments that inspire employees to thrive, create, and collaborate\. Headquartered in the Bay Area, Pivot Interiors operates offices and Design Centers across the state, including Santa Clara, Fremont, San Francisco, Costa Mesa, Los Angeles, and La Mirada\. As a MillerKnoll Certified Dealer, Pivot Interiors invites clients to experience its uniquely crafted spaces and the distinctive quality that defines the Pivot Interiors brand\.

[__https://www\.pivotinteriors\.com__](https://www.pivotinteriors.com)

<a id="_Toc217286712"></a>__2\.03 NetSuite Orion Overview__

The NetSuite Orion Commissions Module is a sophisticated sales commission management system designed to automate the calculation, tracking, and payment of sales commissions\.

<a id="_Toc217286713"></a>__2\.04 Project Overview__

Pivot’s current engagement with GSI is based around the creation and implementation of a set of business requirements appropriate to its business operations both today and scaling into the future\. This project primarily consists of the following stages:

- __Discover__: Evaluate the dealer’s business processes with NetSuite Orion capabilities
- __Realize__: Perform initial setup, installation and configuration of your NetSuite instance
- __Educate__: Empower your team for success through comprehensive training and user adoption support
- __Actualize__: Bring your NetSuite and Orion solution to life with seamless data migration and go\-live support
- __Maximize__: Support and expand your operations with dedicated ongoing assistance and strategic customizations\.

Our implementation approach is “Align, Adapt, Accommodate”\.

- Align – Existing processes fit in NetSuite Orion as is\.
- Adapt – Pivot will change its processes to fit in NetSuite Orion as is\.
- Accommodate – GSI will create a configuration specific to Pivot Interiors, or if the feature can benefit others, will update the code base to make the feature standard\.

<a id="_Toc217286714"></a>__2\.05 Document Objectives__

The purpose of this document is to summarize functional and procedural requirements captured by GSI during the Discover business process mapping phase of the implementation\. 

This Business Requirements Document \(BRD\) documents your goals, the problems you want to solve, and the outcomes you expect\. It is the foundation for the setting up of the system, acting as a __roadmap between your business needs and the solution design__\.

This document represents information gathered in meetings held with the Client, which enables the GSI team to map the business requirements to an efficient flow in the NetSuite Orion application\. Once complete, this document will serve as a blueprint for the GSI team to configure the application\. This document does not supersede the Statement of Work\. The Statement of Work determines scope\. 

A series of process mapping discovery sessions, focusing on the key areas of the business, were used as a starting point for this exercise\. This document remains consistent in structure to those discovery sessions as it categorizes the findings into the same key process areas\. The set of business requirements documentation is inclusive of all business requirements provided by the Client\.

# <a id="_Toc217286715"></a>3 Commission Management

## <a id="_Toc217286716"></a>3\.01 Commission Plan Configuration

3\.01\.01 Your Business Requirements

- REQ\-3\.01\.01: Support cumulative annual commission calculations based on calendar year
- REQ\-3\.01\.02: Commission calculations triggered by invoice date
- REQ\-3\.01\.03: Support multiple commission plan types across different sales roles
- REQ\-3\.01\.04: Commission plans stored with complex calculation rules via JSON configurations
- REQ\-3\.01\.05: Support date\-based validity for commission plans with fiscal year alignment

3\.01\.02 Current State Process

Pivot currently manages multiple compensation plans across different sales roles\. The current commission plans are based on cumulative annual calculations tied to calendar year and invoice date\.

__Current State Challenges__:

- Manual calculation processes prone to errors
- Multiple Excel spreadsheets for tracking
- Time\-consuming reconciliation at year\-end
- Difficulty tracking cumulative YTD progress
- Limited visibility for sales representatives

User Story:

- As a Commission Administrator, I need automated cumulative annual commission calculations so that we can eliminate manual tracking and ensure accurate, timely commission payments\.

3\.01\.03 NetSuite Orion Solution

NetSuite Orion's Commission Module will be configured to support Pivot's cumulative annual calculation methodology\. As decided during discovery: "We will build cumulative annual functionality into the Orion module to support the existing commission structure\. Calendar year and based on invoice date\."

3\.01\.04 Future State Process

1. __Plan Assignment:__ Commission plans assigned to sales representatives based on role
2. __Transaction Processing:__ Invoices trigger commission calculation upon posting
3. __Cumulative Tracking:__ System maintains YTD cumulative Invoiced GP totals automatically
4. __Tier Evaluation:__ Appropriate commission rate applied based on cumulative thresholds
5. __Calculation Generation:__ Commission calculation records created with full audit trail
6. __Approval Workflow:__ Calculations route for review and approval
7. __Payment Processing:__ Approved calculations consolidated for payment

3\.01\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.01\.01__

Cumulative annual commission calculations based on calendar year

Custom cumulative tracking to be built into Orion module

__ACCOMMODATE  __

__REQ\-3\.01\.02__

Commission calculations triggered by invoice date

Standard Orion trigger configuration

__ALIGNS__

__REQ\-3\.01\.03__

Multiple commission plan types across different sales roles

Standard multi\-plan support

__ALIGNS__

__REQ\-3\.01\.04__

Commission plans stored with JSON configurations

Standard Orion commission card functionality

__ALIGNS__

__REQ\-3\.01\.05__

Date\-based validity for commission plans

Standard effective dating functionality

__ALIGNS__

__*Client Feedback*__

<a id="_heading=h.1v1yuxt"></a>__*GSI Response*__

<Comment>

## <a id="_Toc217286717"></a>3\.02 Tiered Commission Calculation

3\.02\.01 Your Business Requirements

- REQ\-3\.02\.01: Support tiered commission rates from 4% to 12% based on cumulative Invoiced GP
- REQ\-3\.02\.02: Commission calculated on Invoiced Gross Profit \(IGP\)
- REQ\-3\.02\.03: Exclude web vendor orders from commission eligibility
- REQ\-3\.02\.04: Support adjustments for storage costs, margin splits, and cost variances
- REQ\-3\.02\.05: Reconciliation of advanced commissions at fiscal year\-end
- REQ\-3\.02\.06: option of using actual vs "quoted" \(cost on the sales order line\) for internal services costs\. The design supports this\. The GP Calculation Framework \(Commission Module, deviation \#8\) was "enhanced to incorporate estimated costs with automatic adjustments as actuals are recorded\." The commission plan's rate card and trigger system can be configured to use either actual costs \(from vendor bills, time entries, etc\.\) or quoted costs \(from the SO line\)\. This would be a configurable option on the commission plan — not a code change\. We should add an explicit field on the Commission Plan record for "Internal Services Cost Basis" \(Actual / Quoted\) to make this clear and user\-selectable\.

Pivot uses a tiered commission structure based on Cumulative Invoiced Gross Profit for Account Managers and NBD Sales Executives\.

3\.02\.03 NetSuite Orion Solution

NetSuite Orion's Commissions Module will be configured with custom tiered calculation logic to support Pivot's progressive commission structure\.

3\.02\.04 Future State Process 

1. __Invoice Posting: __System captures IGP at the time of invoice posting\. Rules can be created for both project GP and commissionable GP, which are calculated separately
2. __Cumulative Calculation: __YTD cumulative IGP totals maintained automatically by the system
3. __Tier Determination: __Automated tier progression applies correct rate \(4%\-12%\) based on thresholds
4. __Web Vendor Exclusion: __Automated exclusion of web vendor orders based on vendor/flags for any vendor at any time\.
5. __Adjustment Processing: __Custom adjustment processing for storage costs, margin splits, and variances
6. __Commission Generation: __Commission calculation records created with full audit trail
7. __Year\-End Reconciliation: __Process adaptation for automated year\-end true\-up of advanced vs\. earned commissions

3\.02\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.02\.01__

Tiered commission rates 4%\-12% based on cumulative IGP

Custom tier calculation logic required

__ACCOMMODATE__

__REQ\-3\.02\.02__

Commission calculated on Invoiced Gross Profit

Standard Orion GP\-based calculation

__ALIGNS__

__REQ\-3\.02\.03__

Exclude web vendor orders from commission eligibility

Custom exclusion flag and logic

__ACCOMMODATE__

__REQ\-3\.02\.04__

Support adjustments for storage, standard split variances\.

Custom adjustment processing

__ACCOMMODATE__

__REQ\-3\.02\.05__

Year\-end reconciliation of advanced commissions

Process change to align with Orion

__ADAPT__

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc217286718"></a>3\.03 Commission Triggers & Manual maintenance

3\.03\.01 Your Business Requirements

- REQ\-3\.03\.01: Implement saved search functionality for automated commission record creation
- REQ\-3\.03\.02: Automated trigger monitoring using scheduled Map/Reduce scripts
- REQ\-3\.03\.03: Commission triggers activated based on invoice date
- REQ\-3\.03\.04: Support manual commission record creation for special scenarios

3\.03\.02 Current State Process

The current system uses manual processes with reports for specific scenarios\. As documented during discovery: "$1M example is a saved search also for manual commission record\. This might be something we automate\."

3\.03\.03 NetSuite Orion Solution

NetSuite Orion provides automated trigger monitoring through scheduled Map/Reduce scripts\. As decided during discovery: "We will implement saved search functionality for automated commission record creation\."

3\.03\.04 Future State Process 

1. __Automated Scanning: __System continuously monitors for trigger conditions using scheduled Map/Reduce scripts
2. __Data Source Evaluation: __When triggers fire, system evaluates data sources \(saved searches, SQL queries\) to identify qualifying transactions
3. __Eligibility Checking: __System validates that transactions meet commission plan criteria
4. __Commission Calculation: __Automated calculation based on configured plan rules
5. __Record Creation: __Commission calculation records created with complete audit trails
6. __Manual Override: __Standard manual entry capability for special scenarios

3\.03\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.03\.01__

Saved search functionality for automated commission record creation

Custom saved search templates to be developed by Chris

__ACCOMMODATE__

__REQ\-3\.03\.02__

Automated trigger monitoring via Map/Reduce scripts

Standard Orion scheduled script functionality

__ALIGNS__

__REQ\-3\.03\.03__

Commission triggers based on invoice date

Standard trigger configuration

__ALIGNS__

__REQ\-3\.03\.04__

Manual commission record creation for special scenarios

Standard manual entry capability

__ALIGNS__

__REQ\-3\.03\.05__

support true margin dollar splits where each rep's share runs through their own individual plan,

Build an enhancement

__ACCOMMODATE__

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc217286719"></a>3\.04 Commission Splits & Allocations

3\.04\.01 Your Business Requirements

- REQ\-3\.04\.01: Support commission splits between multiple representatives with different percentage allocations
- REQ\-3\.04\.02: Handle teamed account commission splits \(50/50 or custom percentages\)
- REQ\-3\.04\.03: Support account transition splits \(50/50 for 30 days after transition\)
- REQ\-3\.04\.04: Leave of absence split handling \(50/50 split for quotes converting within 30 days\)

3\.04\.02 Current State Process

Commission splits between representatives are common at Pivot\. As documented during discovery: "Split could be between people and then each has a different percentage\."

3\.04\.03 NetSuite Orion Solution

NetSuite Orion will accommodate Pivot's commission split requirements\. As noted during discovery, Marcus will discuss split commission functionality with Luke regarding multiple people with different percentages\. Sandy will send example calculation sheets\.

3\.04\.04 Future State Process

- Split Configuration: Commission splits configured with customizable percentages per representative
- Teamed Account Processing: Automated teamed account identification with 4% Teamed Bonus calculation
- Account Transition Handling: 50/50 split tracking for 30\-day transition period between reps
- Leave of Absence Processing: 50/50 split for quotes converting within 30 days of leave commencement/return
- Split Agreement Documentation: Split agreements captured in writing and tracked in the system
- Automated Calculation: System calculates each rep's commission based on their configured split percentage

3\.04\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.04\.01__

Commission splits with different percentage allocations

Custom split calculation logic; Marcus to discuss with Luke

__ACCOMMODATE__

__REQ\-3\.04\.02__

Teamed account commission splits

Custom teamed account handling with 4% Teamed Bonus

__ACCOMMODATE__

__REQ\-3\.04\.03__

Account transition splits \(50/50 for 30 days\)

Process alignment with standard transition handling

__ADAPT__

__REQ\-3\.04\.04__

Leave of absence split handling

Process alignment with leave policies

__ADAPT__

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc217286721"></a>3\.06 Deposit Bonus Processing

3\.06\.01 Your Business Requirements

- REQ\-3\.06\.01: Deposit bonus equal to 0\.5% of cash deposit received within 7 days of order entry
- REQ\-3\.06\.02: Minimum deposit threshold of $10,000 for bonus eligibility
- REQ\-3\.06\.03: Support deposit bonus relative to percentage of total project value
- REQ\-3\.06\.04: Deposit bonus will accommodate splits, allowing 50/50 spiff amounts
- __REQ\-3\.06\.05:__ all sectors, such as dollar amount thresholds or days should be adjustable and not hard coded\.

3\.06\.02 Current State Process

"Account Managers will earn a bonus equal to one\-half of one percent \(0\.5%\) of the amount of a cash deposit received by check, credit card or wire within seven \(7\) days of a sales order being entered\. Cash deposits must be $10,000\.00 or more to be bonus eligible\."

3\.06\.03 NetSuite Orion Solution

NetSuite Orion will be configured with custom deposit bonus processing:

- __7\-Day Window Tracking: __Automated monitoring of deposit receipt timing relative to order entry date
- __Threshold Validation: __Standard threshold configuration to validate minimum $10,000 deposit requirement
- __Bonus Calculation: __Automated 0\.5% bonus calculation on qualifying deposits
- __Project Value Relativity: __Support for deposit bonus relative to percentage of total project value \(confirmed by Marcus\)

3\.06\.04 Future State Process

1. __Order Entry: __Sales order entered NetSuite Orion with order date captured
2. __Deposit Receipt: __Customer deposit received \(check, credit card, or wire\)\. The deposits need to be posted to sales orders\. and recorded in the system\.
3. __Timing Validation: __System automatically validates deposit received within 7\-day window
4. __Threshold Check: __System confirms deposit meets minimum $10,000 threshold
5. __Bonus Trigger: __Automatic bonus trigger generates 0\.5% commission calculation
6. __Payment Processing: __Bonus paid the month following deposit receipt

3\.06\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.06\.01__

Deposit bonus 0\.5% within 7 days of order entry

Custom timing validation and trigger

__ACCOMMODATE__

__REQ\-3\.06\.02__

Minimum $10,000 deposit threshold

Standard threshold configuration

__ALIGNS__

__REQ\-3\.06\.03__

Deposit bonus relative to % of total project

Confirmed by Marcus

__ALIGNS__

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc217286722"></a>3\.07 Commission Reporting & Reconciliation

3\.07\.01 Your Business Requirements

- REQ\-3\.07\.01: Commission statements showing monthly and YTD calculations
- REQ\-3\.07\.02: Year\-end reconciliation with advanced commission true\-up
- REQ\-3\.07\.03: Complete audit trail for all commission calculations and changes

3\.07\.02 Current State Process 

Commission statements are currently created manually in Excel\. The process includes:

- Manual creation of commission statements showing monthly and YTD calculations
- Manual reconciliation at fiscal year\-end comparing advanced vs\. earned commissions
- Limited audit trail with changes tracked in separate logs
- Email\-based approval process with manual tracking

3\.07\.03 NetSuite Orion Solution  

NetSuite Orion provides comprehensive commission reporting and reconciliation capabilities:

- __Commission Statements: __Automated commission statement generation with monthly and YTD views
- __Year\-End Reconciliation: __Process adaptation for automated year\-end true\-up comparing advanced vs\. earned
- __Audit Trail: __Complete automated audit trail for all commission calculations and changes
- __Approval Workflow: __Automated approval workflow with status tracking

3\.07\.04 Future State Process 

- __Monthly Reporting: __Automated generation of commission statements showing invoiced sales, gross margin, YTD totals, and commission calculations
- __Real\-Time Visibility: __Sales representatives can view their commission status and YTD progress at any time
- __Year\-End Reconciliation: __Automated comparison of advanced commissions vs\. earned commissions at fiscal year\-end
- __True\-Up Processing: __System calculates additional earned commissions or claw back amounts as of Reconciliation Date
- __Audit Logging: __Complete audit trail maintained for all calculation changes and adjustments

3\.07\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.07\.01__

Commission statements with monthly/YTD calculations

Standard Orion reporting capability

__ALIGNS__

__REQ\-3\.07\.02__

Year\-end reconciliation with true\-up

Process adaptation for annual reconciliation timing

__ADAPT__

__REQ\-3\.07\.03__

Complete audit trail for calculations

Standard Orion audit logging

__ALIGNS__

__*Client Feedback*__

__*GSI Response*__

<Comment>

<a id="_Toc214548277"></a><a id="_Toc217286724"></a>4 SuiteApps

<a id="_Toc214548278"></a><a id="_Toc217286725"></a>__4\.01 SuiteApp Summary__

__No SuiteApps Required for Commissions__

<a id="_Toc217286726"></a>5 Assumptions

The following is a list of assumptions based on the solutions proposed in this document\.

__\#__

__Assumptions__

1

Pivot will provide all current compensation plan documents for configuration

2

Pivot will provide example calculation sheets illustrating commission split scenarios

3

Cumulative annual calculation functionality will be built into Orion module based on calendar year with invoice date as trigger

4

Commission plans will be configured with JSON\-based calculation rules

5

No commision data migration, reports are kept in Crystal reports

6

Marcus will discuss split commission functionality with Luke regarding multiple people with different percentages

7

GSI will develop saved search templates for manual commission record automation

8

Web vendor identification will be maintained in NetSuite for commission exclusion\. commission plans, triggers, rate cards, and invoice schedule templates are all admin\-configurable without developer involvement\. commission plans, triggers, rate cards, and invoice schedule templates are all admin\-configurable without developer involvement

9

Deposit bonus timing validation will track 7\-day window from order entry\.

10

Commissions payments will be handled through payroll entry

11

Year\-end reconciliation process will align with Pivot's fiscal calendar

<a id="_Toc217286727"></a>6 Unresolved Requirements

__\#__

__Requirement__

__Description__

__Owner / Next Step__

1

Commission plan timing confirmation

Confirm when commission plans are applied in workflow

Marcus to confirm

2

Deposit bonus workflow

Validate detailed workflow for deposit bonus based on % of total project value

Marcus to validate and demonstrate

<a id="_Toc217286728"></a>7 Signatures 

Sign\-off represents agreement on behalf of both Client and GSI of the Business Requirements for this process area of the NetSuite Orion implementation\. Sign\-off provides the go\-ahead to begin the Realize stage\. 

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

<a id="_Toc217286729"></a>8 Appendix

#### Current State Definition

Commission Rate Schedule:

- Currently Pivot has a plan where it is 8% and 12% rate\. If they meet their IGP goal, they then go up to the 12% rate, and get a bonus based on 2% of the IGP goal\.

__Tier__

__Invoiced Gross Profit From__

__To__

__Commission Rate__

__1__

$0

$399,999

__4%__

__2__

$400,000

$799,999

__6%__

__3__

$800,000

$1,199,999

__8%__

__4__

$1,200,000

$1,599,999

__10%__

__5__

$1,600,000

\+

__12%__

Key Definitions from Compensation Plans:

__Term__

__Definition__

__Total Sales Price__

The total sales price on a sales order

__Total Costs__

All costs including materials, labor, freight, storage, internal processing fees, interest, taxes, errors, punch, and mock\-ups

__Gross Profit__

Total Sales Price minus Total Costs

__Gross Margin__

Gross Profit divided by Total Sales Price

__Invoiced Gross Profit \(IGP\)__

Gross Profit calculated at the time a sales order is invoiced

__Cumulative IGP__

Year\-to\-date total of IGP invoiced under the sales rep's account

__Reconciliation Date__

The last day of the Company's fiscal year

__Web Vendors__

Vendors where orders are placed using a website and credit card \(not commission eligible\)

CSM Quarterly Bonus Structure:

Sales goals and rate cards are separate records and can both be updated at any time\. Commission plans have effective dates, so you can set up next quarter's plan without affecting anything\.

__Period__

__Goals__

__Bonus Amount__

Q1 \(Jan\-Mar\)

For every $150,000 of IGP

__$1,000 per $150K__

Q2 \(Apr\-Jun\)

For every $150,000 of IGP

__$1,000 per $150K__

Q3 \(Jul\-Sep\)

For every $150,000 of IGP

__$1,000 per $150K__

Q4 \(Oct\-Dec\)

For every $150,000 of IGP

__$1,000 per $150K__

Construction Solutions Sales Rep Bonus Tiers:

__Project Order Amount__

__Bonus__

Below $500K

No bonus

$501K \- $999K

__$1,000__

$1\.00M \- $1\.49M

__$2,000__

$1\.50M \- $1\.99M

__$3,000__

$2\.00M\+

__Continue pattern \(\+$1,000 per $500K\)__

