# Pivot BRD — Project Management

_Source: `Project Management/Pivot/4 BRD/10_Pivot Interiors BRD Project Management and Workfront Process Area_v2.0.docx`_

---

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation__

__Project Management \- Workfront Process Area__

__Prepared for: Pivot Interiors, Inc\.__

__Version 2\.0__

__Date March 10th, 2025__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

__Jeanine Post \(NetSuite Orion Functional Consultant\)__

__Table of Contents__

[1 Version Control	3](#_Toc215670890)

[2 Project Definition	4](#_Toc215670891)

[2\.01 Executive Summary	4](#_Toc215670892)

[2\.02 Company Overview	4](#_Toc215670893)

[2\.03 NetSuite Orion Overview	4](#_Toc215670894)

[2\.04 Project Overview	4](#_Toc215670895)

[2\.05 Document Objectives	5](#_Toc215670896)

[3 Project Management & Workfront	6](#_Toc215670897)

[3\.01 Labor Quote Management	6](#_Toc215670898)

[3\.02 Work Order Scheduling & Coordination	8](#_Toc215670899)

[3\.03 Proposal & Order Entry Management	10](#_Toc215670900)

[3\.04 Resource Management & Time Tracking	13](#_Toc215670901)

[3\.05 Reporting & Business Intelligence	15](#_Toc215670902)

[3\.06 Document Management & System Integration	17](#_Toc215670903)

[4 SuiteApps & Integrations	20](#_Toc215670904)

[4\.01 Required SuiteApps	20](#_Toc215670905)

[4\.02 Third\-Party Integrations	20](#_Toc215670906)

[5 Assumptions	21](#_Toc215670907)

[5\.01 Business Process Assumptions	21](#_Toc215670908)

[5\.02 Technical Assumptions	21](#_Toc215670909)

[5\.03 Organizational Assumptions	22](#_Toc215670910)

[6 Unresolved Requirements	23](#_Toc215670911)

[6\.01 Pending Decisions	23](#_Toc215670912)

[6\.02 Information Gathering Required	23](#_Toc215670913)

[7 Signatures	24](#_Toc215670914)

# <a id="_Toc215670890"></a>1 Version Control

__Version__

__Author__

__Comments__

__Date__

0\.1

Jeanine Post

Initial Draft

11/7/2025

0\.2

Jeanine Post

Revised draft

11/26/2025

1\.0

Debbie Herbert, Chris Trumble

Final Draft

12/03/2025

1\.5

Chris Trumble

Answered additional comments

3/11/2026

<a id="_heading=h.2et92p0"></a>

# <a id="_Toc215670891"></a>2 Project Definition

## <a id="_Toc215670892"></a>2\.01 Executive Summary

Pivot Interiors manages 32,000\+ Workfront requests over 18 months: labor quotes \(5,300\), work orders \(3,200\), order entries \(10,596\), proposals \(7,324\), and others\. The current state requires manual data re\-entry across Workfront, IQ, and D365 with no real\-time visibility\.

NetSuite Orion will replace Workfront with an integrated Request Engine, Smart Table functionality, and automated workflows while maintaining governance controls\.

## <a id="_Toc215670893"></a>2\.02 Company Overview

Pivot Interiors, Inc\. is a leading California\-based design firm recognized for its team of innovators, creators, and thought leaders who specialize in delivering exceptional interior solutions for businesses of all sizes\. Their work captures the essence of each client’s brand while fostering environments that inspire employees to thrive, create, and collaborate\. Headquartered in the Bay Area, Pivot Interiors operates offices and Design Centers across the state, including Santa Clara, Fremont, San Francisco, Costa Mesa, Los Angeles, and La Mirada\. As a MillerKnoll Certified Dealer, Pivot Interiors invites clients to experience its uniquely crafted spaces and the distinctive quality that defines the Pivot Interiors brand\.

[__https://www\.pivotinteriors\.com__](https://www.pivotinteriors.com/)

## <a id="_Toc215670894"></a>2\.03 NetSuite Orion Overview

NetSuite Orion is an industry\-specific ERP for office furniture dealerships providing operations management, warehouse operations, field service, and project\-based workflows with multi\-entity support, real\-time inventory tracking, work order management, and integrated time tracking\.

## <a id="_Toc215670895"></a>2\.04 Project Overview

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

## <a id="_Toc215670896"></a>2\.05 Document Objectives

The purpose of this document is to summarize functional and procedural requirements captured by GSI during the Discover business process mapping phase of the implementation\. 

This Business Requirements Document \(BRD\) documents your goals, the problems you want to solve, and the outcomes you expect\. It is the foundation for the setup of the system, acting as a __roadmap between your business needs and the solution design__\.

This document represents information gathered in meetings held with the Client, which enables the GSI team to map the business requirements to an efficient flow in the NetSuite Orion application\. Once complete, this document will serve as a blueprint for the GSI team to configure the application\. This document does not supersede the Statement of Work\. The Statement of Work determines scope\. 

A series of process mapping discovery sessions, focusing on the key areas of the business, were used as a starting point for this exercise\. This document remains consistent in structure to those discovery sessions as it categorizes the findings into the same key process areas\. The set of business requirements documentation is inclusive of all business requirements provided by the Client\.

# <a id="_Toc215670897"></a>3 Project Management & Workfront

## <a id="_Toc215670898"></a>3\.01 Labor Quote Management

3\.01\.01 Your Business Requirements

- REQ\-3\.01\.01: Manage 5,300\+ annual labor quote requests from initiation through sales order integration
	- Support Designer/Sales initiation → PM review → Estimator → PM finalization → Sales workflow
- __REQ\-3\.01\.02: __Eliminate manual data re\-entry between Workfront, IQ, and D365 systems
- __REQ\-3\.01\.03: __Support automatic routing of labor quote requests to appropriate estimators \(internal or external vendors\)
- __REQ\-3\.01\.04: __Enable partial acceptance of multiple labor quote options \(accept Option 1, reject Option 2\)
- __REQ\-3\.01\.05: __Configure client\-specific quote formatting templates \(80% single line, 20% custom breakdowns\)
- __REQ\-3\.01\.06: __Automatically transfer accepted labor quotes to sales order lines \(replace CAP spec upload\)
- __REQ\-3\.01\.07: __Support USD standard with CAD quote notation capability

3\.01\.02 Current State Process

Labor quoting is fragmented across three disconnected systems with manual data transfer at each handoff:

- Designer/Sales initiates a request in Workfront with scope documents and floor plans
- Admin on the Service Operations Team\. Design / Sales submits request, PM modifies and sends to the estimator in Workfront\. Then admin transfers to IQ\. Estimator completes quote in IQ, and then PM copies info back into Workfront\. \(no integration\)
- Estimator completes quote in IQ; PM manually copies results back to Workfront
- Sales Coordinator manually enters labor line into D365 via CAP spec upload
- Client formatting preferences \(80/20 split\) managed through tribal knowledge
- Multi\-option quotes require manual coordination with no systematic acceptance workflow

3\.01\.03 NetSuite Orion Solution

Request Engine provides integrated labor quote management, eliminating manual transfers:

- Designers/Sales initiate requests with attached documents directly in the system
- Automatic routing to estimators based on configurable business rules with audit trail
- Labor Quote Acceptance feature enables selection of specific options or combined quotes
- PDF Composer provides client\-default templates with custom override capability
- Accepted quotes auto\-populate sales order lines with proper GL posting via vendor cross\-reference

3\.01\.04 Future State Process

- Designer/Sales initiates labor quote request in Orion Request Engine with integrated document attachment\. In the case of generating multiple quotes \(ST vs OT\) Status for not selected quotes is “cancelled’ but the hidden setting can be configured and also inactivate the record is an option\. Custom status can also be added for the different type request types
- System automatically routes to the assigned Project Manager based on project assignment rules
- PM reviews and enhances the request directly in the system, the system routes to the estimator automatically\. Emails can be sent to an Orion sub vendor, but you will have to select the quoter\. Select a vendor contact and the email can be review and send\. This is included in scope
- Estimator accesses the request directly in NetSuite Orion; provides quote options with line\-item detail
- PM uses Labor Quote Acceptance feature to select option\(s\); system generates sales order lines automatically\. Additionally, the PM has its own customized dashboard that contains assigned requests and status
- Sales team reviews the auto\-populated quote with the proper client template; no manual data entry required

Process Improvements:

- Eliminates manual copy/paste between Workfront and IQ systems
- Automated routing reduces request turnaround time from hours to minutes
- Labor Quote Acceptance feature eliminates CAP spec manual upload process
- Client\-specific templates automatically format quotes per established requirements\. Labor comes over as a labor line or lines on the overall quote,
- Integrated approval workflows replace email\-based approvals\. This will be based on approval matrix that will generate reminders on the role specific dashboards, emails, or both

3\.01\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

<a id="_Hlk213232245"></a>REQ\-3\.01\.01

Manage 5,300\+ labor quote requests annually

Request Engine with unlimited request capacity and automated routing

__ALIGNS__

<a id="_Hlk213232269"></a>REQ\-3\.01\.02

Eliminate manual data re\-entry between systems

Labor Quote Acceptance feature with automatic sales order line generation

__ADAPT__

REQ\-3\.01\.03

Support automatic routing of labor quote requests

Configurable routing rules with audit trail

__ALIGNS__

REQ\-3\.01\.04

Support partial acceptance of multiple quote options

Multi\-option quote management with selective acceptance workflow

__ALIGNS__

REQ\-3\.01\.05

Auto\-transfer accepted quotes to sales order

Auto\-generation replaces CAP spec upload

__ADAPT__

REQ\-3\.01\.07

Support USD standard with CAD quote notation

Standard capability

__ALIGNS__

3\.01\.06 Implementation Requirements:

- Configure Request Engine with labor quote request types matching current Workfront issue categories, Custom fields \(requirements\) can be added to the cases\.
- Set up automatic routing rules based on project type, PM assignment, and estimator availability
- Configure Labor Quote Acceptance workflow to support single\-option and multi\-option scenarios
- Establish client\-default quote templates in PDF Composer \(80% single line configuration\)
- Labor quote approval thresholds will not be implemented at Day 1 launch \(future phase consideration\)\. Approvals workflow are not implemented, if it is needed a decision  that can be made now and configure approvals\.

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc215670899"></a>3\.02 Work Order Scheduling & Coordination

3\.02\.01 Your Business Requirements

- __REQ\-3\.02\.01: __Schedule 3,200\+ annual work orders against approved labor budgets with capacity display
- __REQ\-3\.02\.02: __Maintain project\-subproject numbering convention \(6\-digit project \+ 2\-digit suffix: project\-XX format\)
- __REQ\-3\.02\.03: __Provide installation team scheduling with resource requirements visibility \(installer count, dates, site access\)
- __REQ\-3\.02\.04: __Integrate site logistics documentation with work order records via SharePoint
- __REQ\-3\.02\.05: __Enable Field Service app access for installation teams \(web\-based, no app download required\)
	- Lead installer: read/write | Crew member: view\-only
- __REQ\-3\.02\.06: __Automate budget\-to\-actual tracking with alerting \(80% PM notification, 100% escalation\)

3\.02\.02 Current State Process

Work order scheduling is manual and disconnected from labor budgets:

- PM initiates work order in Workfront after receiving customer PO
- PM manually references IQ to identify applicable sub\-project labor budget \(no Workfront connection\)
- Project\-subproject numbering requires manual entry with no system enforcement
- Service Operations manually checks team availability and assigns installers
- Documents scattered across Workfront, SharePoint, email, and local folders
- Installation teams lack mobile access; they rely on printed documents and phone calls

3\.02\.03 NetSuite Orion Solution

NetSuite Orion provides integrated work order management with real\-time budget visibility:

- PMs initiate work orders directly from sales order sub\-projects with automatic budget display
- Project hierarchy preserves numbering convention \(project\-XX\) with automatic enforcement
- SharePoint integration provides single\-source document storage attached to work orders
- Field Service app provides web\-based mobile access with configurable permission levels, define by routine and rules
- Automatic budget\-to\-actual comparison with threshold alerts \(80%/100%\)

3\.02\.04 Future State Process

- PM navigates to sub\-project and initiates work order; system displays labor budget and remaining capacity
- PM specifies resource requirements and attaches documents via integrated SharePoint
- System validates work against available budget and routes to Service Operations
- Service Operations views availability calendar and assigns teams
- Installers access work order details via Field Service app; log hours directly
- System compares actual to budgeted hours with automatic alerts at thresholds

3\.02\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.02\.01

Schedule 3,200\+ annual work orders against approved labor budgets

Work Order Management with integrated budget visibility

__ALIGNS__

REQ\-3\.02\.02

Maintain project\-subproject numbering \(project\-XX format\)

Configurable project hierarchy with automatic numbering

__ALIGNS__

REQ\-3\.02\.03

Installation team scheduling with visibility

Resource scheduling interface with availability calendar

__ALIGNS__

REQ\-3\.02\.04

Integrate site logistics documentation

SharePoint integration with direct work order attachment

__ADAPT__

REQ\-3\.02\.05

Field Service app access for installation teams

Web\-based Field Service app with configurable permission levels

__ALIGNS__

REQ\-3\.02\.06

Automate budget\-to\-actual tracking with alerting

Real\-time tracking with configurable threshold alerts

__ACCOMODATE__

3\.02\.06 Key Implementation Requirements

- Configure project hierarchy to support 6\-digit project numbers with 2\-digit sub\-project structure \(XX format\), ensuring automatic numbering enforcement and validation
- Link work order functionality directly to sales order sub\-projects, enabling automatic display of associated labor budgets and remaining capacity
- Configure Work Order Management to capture resource requirements \(installer count, date range, site access details\) with routing to Service Operations team
- Set up SharePoint integration for direct document attachment to work orders \(floor plans, site analysis, logistics notes, building contacts\)
- Configure Field Service app with two permission levels: lead installer \(read/write for task completion, time entry, issue reporting\) and crew member \(view\-only for scope review\)
- Establish real\-time time tracking integration with work orders, enabling automatic budget\-to\-actual comparison
- Configure alert thresholds at 80% \(PM notification\) and 100% \(Service Operations escalation\) of budgeted hours
- Establish resource scheduling interface for Service Operations team showing team availability calendar alongside work order requests

## <a id="_Toc215670900"></a>3\.03 Proposal & Order Entry Management

3\.03\.01 Your Business Requirements

- __REQ\-3\.03\.01: __Manage 7,300\+ annual proposals across types \(Standard, Transactional, Revisions, Bill\-back, Change Orders, GSA\)
- __REQ\-3\.03\.02: __Process 10,596\+ annual orders from customer PO through fulfillment with SC → PC handoff
- __REQ\-3\.03\.03: __Eliminate quadruple work in spec file processing \(PM highlights PDF → SC adds aliases → PC processes → multi\-vendor form\)
- __REQ\-3\.03\.04: __Support Smart Table custom grouping for PO splitting and phasing \(Phase 1, Phase 2, Late Ancillary, etc\.\)
- __REQ\-3\.03\.05: __Replace manual multi\-vendor Excel forms \(required for 10\+ vendors, complex phasing, multiple ship\-to\)
- __REQ\-3\.03\.06: __Implement system\-based approval workflows for change orders with audit trail
- __REQ\-3\.03\.07: __Enable web\-based client quote approval capability \(secure external access\)

3\.03\.02 Current State Process

Proposal and order entry spans Workfront, CAP, D365, and manual Excel with quadruple handling of spec data:

- Salesperson initiates proposal in Workfront; SC executes in CAP with extensive validation
- Upon PO receipt, SC initiates order entry request and hands off to PC
- Quadruple work:
- PM highlights spec PDF \-\-> SC adds alias codes \-\-> SC re\-processes spec \-\-> SC creates multi\-vendor Excel form and includes with PC order entry \-\-> PC issues PO’s based on Alias’s and order entry directions
- Multi\-vendor forms are maintained outside any system for complex orders
- Change order approvals tracked via email with no system workflow or audit trail
- Limited D365 access creates bottlenecks; only SC/PC/Finance have access

3\.03\.03 NetSuite Orion Solution

Smart Table eliminates quadruple work with direct PM/PC access to spec data:

- Service Ops change orders are tracked in IQ; but this is ONLY for labor hours that are a change order\. Service ops creates an order in IQ and verifies when the costs have been passed on to the client on D365\.
- Custom groups \(Phase 1, Phase 2, Vendor A, etc\.\) auto\-flow to PO generation and invoicing
- Order Approval Rules enable configurable multi\-level approval with complete audit trail
- Client Quote Approval provides secure web\-based external access for proposal acceptance
- PDF Composer with client\-specific templates; SharePoint integration for centralized documents

3\.03\.04 Future State Process

- Salesperson initiates a proposal; SC imports spec to Smart Table and validates with auto\-template application
- Proposal routes through Order Approval Rules; client accepts via secure web link
- SC converts to sales order; system auto\-notifies PC with complete context
- PM and PC collaborate in Smart Table for phasing/aliasing/grouping—single system, one activity, which can change or manage later
- Custom groups auto\-flow to PO generation with correct ship\-to addresses and vendor assignments
- Change orders route through system workflow with real\-time status and audit trail

3\.03\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.03\.01

Manage 7,300\+ annual proposals across types

Proposal management with type\-specific workflows

__ALIGNS__

REQ\-3\.03\.02

Process 10,596\+ annual orders through fulfillment

Integrated order management with SC to PC handoff

__ALIGNS__

REQ\-3\.03\.03

Eliminate quadruple work in spec processing

Smart Table with direct PM/PC access for bulk operations

__ADAPT__

REQ\-3\.03\.04

Support Smart Table custom grouping for PO splitting

Unlimited custom groups with auto\-flow to PO/invoicing

__ALIGNS__

REQ\-3\.03\.05

Replace manual multi\-vendor Excel forms

System\-generated coordination via Smart Table groups

__ADAPT__

REQ\-3\.03\.06

Implement system\-based change order approvals

Order Approval Rules with configurable routing and audit

__ADAPT__

REQ\-3\.03\.07

Enable web\-based client quote approval

Client Quote Approval with secure web interface

__ALIGNS__

3\.03\.06 Key Implementation Requirements

- Configure Order Approval Rules for all proposal types with appropriate approval routing, value thresholds, and stakeholder notifications
- Set up Smart Table with bulk alias assignment capabilities, custom grouping functionality, and filtering tools for PM/PC collaboration
- Configure PDF Composer with client\-specific proposal templates for the top 20 clients representing 80% of proposal volume
- Establish Client Quote Approval feature with secure web\-based access, electronic acceptance capability, and audit trail capture\. Based on a search that can be added to the reminders or the dashboard\.
- Configure automatic SC to PC handoff workflow triggered by customer PO receipt or proposal acceptance
- Set up SharePoint integration for centralized document storage accessible from proposals, sales orders, and customer records
- Configure change order workflow with Order Approval Rules matching current governance requirements, but providing system visibility
- Establish custom groups in Smart Table for common phasing patterns \(Phase 1/2, Late Ancillary, etc\.\) as starting templates

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc215670901"></a>3\.04 Resource Management & Time Tracking

3\.04\.01 Your Business Requirements

- __REQ\-3\.04\.01: __Support billable PM service pricing \- Greater than $1M\. $400 minimum charge14% of labor for orders between $1 and $250K12% of labor for order between $250K and $1M Projects over $1M will get manual PM quote
- __REQ\-3\.04\.02: __Track time for both hourly employees \(match HR/payroll\) and salaried employees \(budget analysis\) Ther is not direct integration with UKG\. Rates need to be managed in Netsuite
- __REQ\-3\.04\.03: __Capture project time and admin time separately \(expect 80% project / 20% admin split\)
- __REQ\-3\.04\.04: __Implement flexible PM rate cards by project type \(General PM rate, Healthcare PM rate—PM selects at time entry\)\. This is based on an on pending integration design and PM and additional work to set it up automatically\.
- __REQ\-3\.04\.05: __Automate cost calculation on time records \(replace manual Excel compilation\)
- __REQ\-3\.04\.06: __Generate budget\-to\-actual reports with exception alerting \(80% PM notification, 100% escalation\) This reports can generate alerts also\.
- __REQ\-3\.04\.07: __Enable export to HR systems for payroll processing

3\.04\.02 Current State Process

PM is sold as billable service requiring accurate time tracking for budget analysis and billing:

- PMs log time daily in Workfront against projects, tasks, or admin activities
- Two rate tiers: General PM and Healthcare PM \(based on project type, not employee\)
- Brian Hagerty manually compiles monthly cost reports in Excel \(3\-4 hours/month\)
- No real\-time budget visibility—variance discovered after\-the\-fact
- No proactive alerts; projects can exceed budget by 20\-30% before detection

3\.04\.03 NetSuite Orion Solution

 Integrated time tracking with automated cost calculation and real\-time visibility:

- Unified interface for hourly and salaried employees with appropriate rate card application
- PM selects General or Healthcare rate at time entry based on project characteristics
- Automatic cost calculation eliminates the manual Excel process
- Labor Quote to Actual reporting with configurable alert thresholds
- Resource utilization reports by forecasted installation dates for capacity management

3\.04\.04 Future State Process

- PM logs time in NetSuite Orion selecting General or Healthcare rate; system auto\-calculates cost
- PM dashboard displays real\-time hours logged vs\. budgeted with visual health indicators
- At 80% budget, system notifies PM; at 100%, escalates to leadership
- Hourly employee time exports to HR/payroll in the required format no needed
- Resource utilization forecasting enables proactive PM assignment by installation month

3\.04\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.04\.01

Support billable PM pricing \(14%/12%/custom\)

Configurable percentage and hour\-based pricing models

__ALIGNS__

REQ\-3\.04\.02

Track time for hourly and salaried employees

Unified time tracking with employee type awareness

__ALIGNS__

REQ\-3\.04\.03

Capture project and admin time separately

Project\-specific and admin time tracking with split reporting

__ALIGNS__

REQ\-3\.04\.04

Flexible PM rate cards by project type

Configurable rate cards with project\-based selection

__ACCOMMODATE__

REQ\-3\.04\.05

Automate cost calculation on time records

Automatic cost calculation via rate card lookup

__ADAPT__

REQ\-3\.04\.06

Budget\-to\-actual reporting with alerts

Real\-time dashboards with configurable threshold alerts

__ADAPT__

REQ\-3\.04\.07

Export to HR systems for payroll

Configurable export formats matching HR requirements

__ALIGNS__

3\.04\.06 Key Implementation Requirements

- Configure two\-tier rate card structure \(General PM and Healthcare PM and same for Design\) with clear selection criteria documentation
- Set up time tracking interface with project/task selection, admin time capability, and rate card selection
- Configure automatic cost calculation rules matching rate cards to resources and project selections
- Establish budget\-to\-actual dashboard with real\-time hours logged vs\. budgeted display
- Configure alert thresholds at 80% \(PM and Design notification\) and 100% \(leadership escalation\) of budgeted hours
- Set up resource utilization forecasting by PM showing workload by installation month
- Configure payroll export format matching HR system requirements for hourly employees
- Define admin time tracking categories for non\-project work \(meetings, training, administrative tasks\)

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc215670902"></a>3\.05 Reporting & Business Intelligence

3\.05\.01 Your Business Requirements

- __REQ\-3\.05\.01: __Provide real\-time KPI dashboards eliminating manual Excel compilation \(currently 3\-4 hrs/month\)
	- Required KPIs: Punch resolution <5 days, monthly labor invoicing by PM, PM\-specific punch budget tracking
- __REQ\-3\.05\.02: __Implement forecasted utilization report by PM \(workload by installation month with order value/labor costs\)
- __REQ\-3\.05\.03: __Redesign Job Status Report \("Project Bible"\) leveraging full NetSuite Orion data model
- __REQ\-3\.05\.04: __Enable PM team self\-service report creation \(saved search training post\-implementation\)
- __REQ\-3\.05\.05: __Integrate with existing Power BI analytics investments \(maintain Kevin Baugh's dashboards\)
- __REQ\-3\.05\.06: __Consolidate reporting from Workfront, D365, IQ, and Crystal Reports into unified source
- __REQ\-3\.05\.07: __Support 3\-month rolling average calculations for PM metrics

3\.05\.02 Current State Process

Reporting is fragmented across four systems requiring manual compilation:

- Brian manually extracts data from Workfront, D365, IQ; calculates KPIs in Excel \(3\-4 hrs/month\)
- Job Status Report \(Crystal/D365\) lacks Workfront and IQ context—incomplete picture
- No forecasted PM utilization—workload managed reactively
- New reports require IT/consultant intervention \(weeks\-long backlog\)
- Power BI dashboards have 24\-hour data warehouse refresh lag

3\.05\.03 NetSuite Orion Solution

Integrated real\-time dashboards with self\-service capabilities:

- Configurable KPI tracking with automated calculations and exception alerting
- Forecasted utilization by installation month for proactive capacity management
- Job Status redesigned with full data model: PM, financial, procurement, installation, punch data
- PM team creates saved searches post\-training—minutes instead of weeks
- Data warehouse connectivity maintains Power BI investments

3\.05\.04 Future State Process

- Brian accesses real\-time KPI dashboard—no manual compilation required
- PM utilization forecast displays projected workload, enabling proactive reassignment
- Job Status "bible" provides a complete project view with drill\-down from a single source
- PMs create their own saved searches for custom reports without IT involvement
- Exception alerts auto\-notify stakeholders when KPIs exceed thresholds

3\.05\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.05\.01

Real\-time KPI dashboards

Executive dashboards with automated KPI calculations

__ADAPT__

REQ\-3\.05\.02

Forecasted PM utilization reporting

Resource utilization forecast by installation month

__ADAPT__

REQ\-3\.05\.03

Redesigned Job Status "Bible" report

Comprehensive project report leveraging full Orion data model showing all projects by: Sales Person/Project Manager\.PC

__ACCOMMODATE__

REQ\-3\.05\.04

PM team self\-service reporting

Saved search functionality with PM training

__ALIGNS__

REQ\-3\.05\.05

Power BI integration

Data warehouse connectivity with dual\-platform option

__ALIGNS__

REQ\-3\.05\.06

Consolidated reporting

Unified platform replacing four separate systems

__ADAPT__

REQ\-3\.05\.07

3\-month rolling average calculations

Automated rolling average formulas in saved searches

__ALIGNS__

3\.05\.06 Key Implementation Requirements

- Configure executive KPI dashboard with Brian's current metrics: punch resolution <5 days, monthly labor invoicing by PM, PM\-specific punch budget tracking
- Build saved search for forecasted PM utilization by installation month, showing order value and labor costs per PM
- Redesign Job Status "Bible" report incorporating project management, financial, procurement, installation, and punch data from the integrated platform
- Configure 3\-month rolling average formulas in saved searches for labor invoicing and other metrics requiring smoothing
- Establish data warehouse connectivity, maintaining Kevin Baugh's Power BI dashboard refresh schedules
- Create role\-based dashboard views for PM team, leadership, and operations, showing relevant metrics for each stakeholder group
- Configure exception alerting for key metrics: aging punch items, budget variance, utilization thresholds

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc215670903"></a>3\.06 Document Management & System Integration

3\.06\.01 Your Business Requirements

- __REQ\-3\.06\.01: __Establish centralized SharePoint document storage accessible from any NetSuite record
- __REQ\-3\.06\.02: __Implement vendor portal for external design partners \(Riverstone primary; D3 for RFP; Azusa special scenarios\)
- __REQ\-3\.06\.03: __Configure granular vendor portal permissions \(Portfolio: Venture/Healthcare/Education/Enterprise; Studio: NorCal/Healthcare/SoCal\)
- __REQ\-3\.06\.05: __Maintain Azure data warehouse connectivity \(hourly order detail refresh, nightly full refresh\)
- __REQ\-3\.06\.06: __Enable universal NetSuite Orion access for all team members \(replace limited D365 access\)
- __REQ\-3\.06\.07: __Provide version control and audit trail for all documents via SharePoint

3\.06\.02 Current State Process

Documents are scattered across disconnected systems with limited access and integration visibility:

- Documents live in IQ, D365, Workfront, email, and local folders with no central repository
- Version control via manual file naming \(v1, v2\_FINAL, v3\_FINAL\_REALFINAL\)
- Riverstone uploads to dedicated SharePoint; Pivot manually re\-uploads to appropriate systems
- Fusion middleware manages 10\-15 integrations with limited visibility into status/errors
- Only SC/PC/Finance have D365 access—everyone else depends on intermediaries

3\.06\.03 NetSuite Orion Solution

Seamless SharePoint integration with vendor portal and universal access:

- SharePoint as a single source of truth accessible from any NetSuite record
- Vendor Portal for Riverstone/D3/Azusa with dashboard, time tracking, document upload, status updates
- Granular permissions by portfolio and studio ensure appropriate vendor visibility
- Native NetSuite connectivity replaces Fusion with superior visibility and error handling

Universal role\-based access eliminates SC/PC bottlenecks\.

3\.06\.04 Future State Process

- All documents stored in SharePoint with a consistent folder structure aligned to NetSuite hierarchy
- Documents attached from any NetSuite record are auto\-stored in SharePoint with version control
- Riverstone uploads directly to project records via Vendor Portal—no manual transfers
- Native integrations replace Fusion with monitoring dashboards and diagnostic capabilities
- All team members self\-serve through role\-based NetSuite Orion access
- Audit trail captures document access, modifications, and sharing automatically

3\.06\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.06\.01

Centralized SharePoint document storage

SharePoint integration with single\-source management

__ADAPT__

REQ\-3\.06\.02

Vendor portal for external design partners

NetSuite Vendor Portal with dashboard and time tracking

__ALIGNS__

REQ\-3\.06\.03

Granular vendor portal permissions

Portfolio and studio\-level permission controls

__ACCOMMODATE__

REQ\-3\.06\.05

Maintain Azure data warehouse connectivity

Scheduled exports maintaining refresh cadence

__ALIGNS__

REQ\-3\.06\.06

Universal NetSuite Orion access

Role\-based access for all team members

__ADAPT__

REQ\-3\.06\.07

Version control and audit trail

Automatic SharePoint version tracking and access history

__ALIGNS__

3\.06\.06 Key Implementation Requirements

- Configure SharePoint integration with folder structure aligned to NetSuite record hierarchy \(Customer → Project → Sales Order → Documents\)
- Establish document attachment capabilities from all relevant NetSuite records \(projects, sales orders, POs, customer records\)
- Set up NetSuite Vendor Portal for Riverstone with dashboard, time tracking, document upload, and project status capabilities
- Configure granular vendor portal permissions mapping portfolios \(Venture/Healthcare/Education/Enterprise\) and studios \(NorCal/Healthcare/SoCal\) to vendor access
- Conduct detailed Fusion integration inventory documenting all 10\-15 current integrations for replacement planning
- Establish native NetSuite integration architecture, replacing Fusion middleware with enhanced monitoring and error handling
- Configure Azure data warehouse connectivity, maintaining current refresh cadence \(hourly order detail, nightly full refresh\)
- Define role\-based access permissions for universal NetSuite Orion access, ensuring appropriate data visibility for each user group
- Migrate critical historical documents from IQ/D365/Workfront to SharePoint repository during implementation \(Action: Document migration strategy required\)

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc215670904"></a>4 SuiteApps & Integrations 

This section documents the SuiteApps, third\-party integrations, and external system connections required to support the Project Management/Workfront process area\. These components extend core NetSuite Orion functionality to meet Pivot Interiors' specific operational requirements\.

## <a id="_Toc215670905"></a>4\.01 Required SuiteApps

__SuiteApp__

__Purpose__

__Status__

PDF Composer

Client\-specific quote formatting and proposal generation with configurable templates

Included in Orion

Field Service App

Web\-based mobile/tablet access for installation crews with time tracking and document access

Included in Orion

BOM Import Tool

Specification file import with line item processing for Smart Table access

Included in Orion

Smart Table

Order line management with custom grouping, filtering, and bulk operations for PO splitting and phasing

Included in Orion

Customer Portal

External client access for proposal review and approval

Included in Orion

Vendor Portal

External design vendor access for project visibility, time tracking, and document collaboration

Included in Orion

Request Engine

Workflow routing for labor quotes, work orders, and internal requests with @mention and audit trail

Included in Orion

## <a id="_Toc215670906"></a>4\.02 Third\-Party Integrations

__Integration__

__Purpose__

__Status__

SharePoint \(Microsoft 365\)

Centralized document storage with view, upload, and folder navigation from NetSuite records

Phase 1

Azure Data Warehouse

Data export to existing data warehouse for Power BI analytics continuation

Phase 2

HR Payroll System

Time data export for hourly employee payroll processing

Phase 1

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc215670907"></a>5 Assumptions

The following is a list of assumptions based on the solutions proposed in this document\.

## <a id="_Toc215670908"></a>5\.01 Business Process Assumptions

__Assumption__

__Impact if Invalid__

__Validated By__

Current Workfront request volumes \(5,300 labor quotes, 3,200 work orders, 10,596 orders, 7,324 proposals over 18 months\) represent typical operational load and will not significantly increase at go\-live\.

Capacity planning and performance testing scope may need adjustment

Sherri Nuzum

The project\-subproject numbering convention \(6\-digit project \+ 2\-digit suffix\) will be maintained in NetSuite without modification to the numbering scheme\.

Custom numbering logic may require development

Brian Hagerty

Labor quote approval workflows do not require dollar\-value thresholds on Day 1; all quotes follow the same routing regardless of value\.

Additional workflow configuration needed

Brian Hagerty

The 80% single\-line / 20% custom breakdown split for client quote formatting represents a stable distribution that will not change significantly\.

Template configuration scope may need expansion

Amanda Beaudin

PM service pricing models \(14% small projects, 12% large projects, custom for >$1M\) will remain stable through implementation\.

Pricing configuration updates required

Brian Hagerty

The two\-tier PM rate structure \(General PM and Healthcare PM\) adequately covers all billing scenarios; no additional rate tiers are required\.

Rate card expansion needed

Brian Hagerty

## <a id="_Toc215670909"></a>5\.02 Technical Assumptions

__Assumption__

__Impact if Invalid__

__Validated By__

SharePoint Online \(Microsoft 365\) is the approved document management platform; no alternative platforms are under consideration\.

Integration approach requires redesign

IT Leadership

The Azure data warehouse infrastructure and Power BI licensing will remain in place; there are no plans to migrate to alternative analytics platforms\.

Analytics integration approach requires revision

Kevin Baugh

Field Service app will be accessed via web browser on company\-provisioned tablets; no native mobile app development is required\.

Mobile app Completed

Chris Trumble

Fusion integration inventory will be completed during Discovery phase, enabling systematic migration planning during Realize phase\.

Integration migration timeline at risk

Sandy Rudloff

HR payroll system can accept time data in a standard export format; no custom integration development is required\.

Custom payroll integration needed

HR Team

## <a id="_Toc215670910"></a>5\.03 Organizational Assumptions

__Assumption__

__Impact if Invalid__

__Validated By__

Key stakeholders \(Brian Hagerty, Amanda Beaudin, Sandra Rudloff, Marie Guerrero, Sherri Nuzum\) will remain available for discovery validation, UAT, and training activities\.

Knowledge gaps may delay validation

Project Sponsor

Riverstone will participate in Vendor Portal pilot and provide feedback during UAT; their engagement is confirmed\.

Vendor Portal validation delayed

Brian Hagerty

The transition from limited D365 access to universal NetSuite Orion access will be supported by organizational change management resources\.

Adoption challenges at go\-live

Project Sponsor

PM team members will complete saved search training during the Educate phase and will be responsible for self\-service reporting post\-go\-live\.

Ongoing IT reporting support required

Brian Hagerty

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc215670911"></a>6 Unresolved Requirements

To be populated pending Business Requirements Document review with the Pivot Interiors team\.

## <a id="_Toc215670912"></a>6\.01 Pending Decisions

__Decision Required__

__Owner__

__Target Date__

__Status__

Change order approval threshold values and routing paths

Brian Hagerty

Realize Phase

Open

Customer Portal rollout priority—which clients to enable first

Sales Leadership

Realize Phase

Can be addressed post go live

General PM and Healthcare PM rate values

Brian Hagerty / Finance

End of Discovery

Open

80/20 project\-to\-admin expectation—informational only

Brian Hagerty

Realize Phase

Open

Field Service app device requirements and provisioning approach

IT

End of Discovery

Open

Budget alert notification recipients by project type

Brian Hagerty

Realize Phase

Open

## <a id="_Toc215670913"></a>6\.02 Information Gathering Required

__Information Needed__

__Owner__

__Target Date__

__Status__

Top 20 client template preferences for quote formatting

Sales Coordination

Realize Phase

Not Started

Vendor cross\-reference validation rules for labor quote transfer

Finance / Sandra Rudloff

Realize Phase

Not Started

External estimator access requirements and security protocols

IT / Sherri Nuzum

Realize Phase

Not Started

Proposal type validation rules from current Workfront custom forms

Amanda Beaudin / Sherri Nuzum

Realize Phase

Not Started

SharePoint folder structure and naming convention standards

IT / PM Leadership

Realize Phase

Not Started

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc215670914"></a>7 Signatures

Sign\-off represents agreement on behalf of both Client and GSI of the Business Requirements for this process area of the NetSuite Orion implementation\. Sign\-off provides the go\-ahead to begin the Realize stage\.

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

