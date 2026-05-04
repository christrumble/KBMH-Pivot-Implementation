# Pivot BRD — Operations

_Source: `Operations/Pivot/4 BRD/06_Pivot Interiors BRD Operations  Process Area_v2.0.docx`_

---

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation__

__Operations Process Area__

__Prepared for: Pivot Interiors, Inc\.__

__Version 1\.0__

__Date: November 13, 2025__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

__Jeanine Post \(NetSuite Orion Functional Consultant\)__

![](data:image/x-emf;base64,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)

[1 Version Control	4](#_Toc213923709)

[2 Project Definition	5](#_Toc213923710)

[2\.01 Executive Summary	5](#_Toc213923711)

[2\.02 Company Overview	5](#_Toc213923712)

[2\.03 NetSuite Orion Overview	5](#_Toc213923713)

[2\.04 Project Overview	6](#_Toc213923714)

[2\.05 Document Objectives	6](#_Toc213923715)

[3 Operations	7](#_Toc213923716)

[3\.01 Receiving & Warehouse Management	7](#_Toc213923717)

[3\.01\.01 Your Business Requirements	7](#_Toc213923718)

[3\.01\.02 Current State Process	7](#_Toc213923719)

[3\.01\.03 NetSuite Orion Solution	8](#_Toc213923720)

[3\.01\.04 Future State Process	8](#_Toc213923721)

[3\.01\.05 Decision Matrix	8](#_Toc213923722)

[3\.02 Scheduling & Resource Management	10](#_Toc213923723)

[3\.02\.01 Your Business Requirements	10](#_Toc213923724)

[3\.02\.02 Current State Process	10](#_Toc213923725)

[3\.02\.03 NetSuite Orion Solution	11](#_Toc213923726)

[3\.02\.04 Future State Process	11](#_Toc213923727)

[3\.02\.05 Decision Matrix	11](#_Toc213923728)

[3\.03 Work Order Management	13](#_Toc213923729)

[3\.03\.01 Your Business Requirements	13](#_Toc213923730)

[3\.03\.02 Current State Process	13](#_Toc213923731)

[3\.03\.03 NetSuite Orion Solution	14](#_Toc213923732)

[3\.03\.04 Future State Process	14](#_Toc213923733)

[3\.03\.05 Decision Matrix	14](#_Toc213923734)

[3\.04 Vendor Returns Management	16](#_Toc213923735)

[3\.04\.01 Your Business Requirements	16](#_Toc213923736)

[3\.04\.02 Current State Process	16](#_Toc213923737)

[3\.04\.03 NetSuite Orion Solution	16](#_Toc213923738)

[3\.04\.04 Future State Process	17](#_Toc213923739)

[3\.04\.05 Decision Matrix	17](#_Toc213923740)

[3\.05 Time Tracking & Project Management	18](#_Toc213923741)

[3\.05\.01 Your Business Requirements	18](#_Toc213923742)

[3\.05\.02 Current State Process	18](#_Toc213923743)

[3\.05\.03 NetSuite Orion Solution	18](#_Toc213923744)

[3\.05\.04 Future State Process	19](#_Toc213923745)

[3\.05\.05 Decision Matrix	19](#_Toc213923746)

[3\.06 Punch List & Issue Management	19](#_Toc213923747)

[3\.06\.01 Your Business Requirements	19](#_Toc213923748)

[3\.06\.02 Current State Process	20](#_Toc213923749)

[3\.06\.03 NetSuite Orion Solution	20](#_Toc213923750)

[3\.06\.04 Future State Process	20](#_Toc213923751)

[3\.06\.05 Decision Matrix	20](#_Toc213923752)

[3\.07 Field Operations	21](#_Toc213923753)

[3\.07\.01 Your Business Requirements	21](#_Toc213923754)

[3\.07\.02 Current State Process	21](#_Toc213923755)

[3\.07\.03 NetSuite Orion Solution	21](#_Toc213923756)

[3\.07\.04 Future State Process	22](#_Toc213923757)

[3\.07\.05 Decision Matrix	22](#_Toc213923758)

[4 SuiteApps	23](#_Toc213923759)

[4\.01 SuiteApp Summary	23](#_Toc213923760)

[5 Assumptions	24](#_Toc213923761)

[6 Unresolved Requirements	25](#_Toc213923762)

[7 Signatures	28](#_Toc213923763)

# <a id="_Toc213923709"></a>1 Version Control

__Version__

__Author__

__Comments__

__Date__

\.01

Jeanine Post

Initial Draft

10/13/2025

\.02

Debbie Herbert

Second Draft

11/06/2025

1\.0

Marcus Dallacqua, Debbie Herbert, Jeanine Post, Chris Trumble

Final Draft

11/13/2025

2\.0

Gary Strickland

Ready for client signature

2/4/2026

<a id="_heading=h.2et92p0"></a>

# <a id="_Toc213923710"></a>2 Project Definition

## <a id="_Toc213923711"></a>2\.01 Executive Summary

Pivot Interiors is implementing NetSuite Orion to transform operational efficiency across receiving, scheduling, work orders, time tracking, punch lists, and field operations\. The current operational environment relies on multiple disconnected systems—IQ Coordinator, D365, Workfront, and PlanGrid—creating significant inefficiencies through manual handoffs, duplicate data entry, and fragmented visibility\.

The organization faces substantial operational friction with 900,000\+ locations in D365 making warehouse management unwieldy, manual work order transfers between systems creating file duplication \("E\-waste"\), and multi\-team coordination required for simple punch orders\. Resource allocation depends on institutional knowledge rather than systematic skills tracking, and time tracking lacks budget vs\. actual reporting with vulnerability to fraud\. Field operations require separate PlanGrid licensing with limited integration to project management systems\.

This Business Requirements Document validates that NetSuite Orion's standard functionality aligns with Pivot Interiors' operational requirements while identifying specific areas where the organization will adapt its processes to leverage proven industry best practices\.

## <a id="_Toc213923712"></a>2\.02 Company Overview

Pivot Interiors, Inc\. comprises a distinguished team of innovators, creators, and thought leaders dedicated to crafting exceptional interior solutions for businesses of all sizes\. Their designs not only embody your brand but also inspire employees to thrive, create, and collaborate in the workplace\. California\-born and raised, they are proudly headquartered in the Bay Area, serving clients state\-wide\. With offices and Design Centers in Santa Clara, Fremont, San Francisco, Costa Mesa, Los Angeles, and La Mirada, they invite you to explore their spaces and experience the Pivot Interiors difference\. Pivot Interiors is a MillerKnoll Certified Dealer\.

[__https://www\.pivotinteriors\.com__](https://www.pivotinteriors.com/)

## <a id="_Toc213923713"></a>2\.03 NetSuite Orion Overview

NetSuite Orion is an industry\-specific ERP solution designed for office furniture dealerships, providing comprehensive functionality for operations management, warehouse operations, field service, and project\-based workflows\. The platform offers robust multi\-entity support, real\-time inventory tracking with lot\-numbered inventory capabilities, work order management, and integrated time tracking for projects\. Key operational features include automated receiving workflows, resource scheduling with skills\-based assignment, punch list management, and mobile field service capabilities\. The system supports complex phased installations, purchase order\-based work order creation, and comprehensive vendor return authorization processes, all while maintaining complete audit trails for compliance requirements\.

## <a id="_Toc213923714"></a>2\.04 Project Overview

Pivot’s current engagement with GSI is based around the creation and implementation of a set of business requirements appropriate to its business operations both today and scaling into the future\. This project primarily consists of the following stages:

- __D__iscover: Evaluate the dealer’s business processes with NetSuite Orion capabilities
- __R__ealize: Perform initial setup, installation and configuration of your NetSuite instance
- __E__ducate: Empower your team for success through comprehensive training and user adoption support
- __A__ctualize: Bring your NetSuite and Orion solution to life with seamless data migration and go\-live support
- __M__aximize: Support and expand your operations with dedicated ongoing assistance and strategic customizations\.

Our implementation approach is “Align, Adapt, Accommodate”\.

- Align – Existing processes fit in NetSuite Orion as is\.
- Adapt – Pivot will change its processes to fit in NetSuite Orion as is\.
- Accommodate – GSI will create a configuration specific to Pivot, or if the feature can benefit others, will update the code base to make the feature standard\.

## <a id="_Toc213923715"></a>2\.05 Document Objectives

The purpose of this document is to summarize functional and procedural requirements captured by GSI during the Discover business process mapping phase of the implementation\. 

This Business Requirements Document \(BRD\) documents your goals, the problems you want to solve, and the outcomes you expect\. It is the foundation for the setup of the system, acting as a __roadmap between your business needs and the solution design\.__

This document represents information gathered in meetings held with the Client, which enables the GSI team to map the business requirements to an efficient flow in the NetSuite Orion application\. Once complete, this document will serve as a blueprint for the GSI team to configure the application\. This document does not supersede the Statement of Work\. The Statement of Work determines scope\. 

A series of process mapping discovery sessions, focusing on the key areas of the business, were used as a starting point for this exercise\. This document remains consistent in structure to those discovery sessions as it categorizes the findings into the same key process areas\. The set of business requirements documentation is inclusive of all business requirements provided by the Client\.

# <a id="_Toc213923716"></a>3 Operations

## <a id="_Toc213923717"></a>3\.01 Receiving & Warehouse Management

### <a id="_Toc213923718"></a>3\.01\.01 Your Business Requirements

Pivot Interiors requires a comprehensive warehouse management solution that addresses current system limitations while supporting audit compliance\. The organization needs to eliminate the burden of maintaining 900,000\+ separate locations created by D365 customizations while maintaining proper inventory tracking for liability purposes\. Key requirements include:

REQ\-3\.01\.01: Lot\-numbered inventory tracking for cost traceability and product location management

REQ\-3\.01\.02: Ability to receive single products to multiple bin locations for items like conference tables with separate bases and tops

REQ\-3\.01\.03: Virtual locations for different inventory types including pre\-sold inventory, showroom inventory, damaged/return inventory, and third\-party warehouses

REQ\-3\.01\.04: Support for product returning from client through transactions and  inventory adjustments and dedicated locations

REQ\-3\.01\.05: Manual receiving triggers to maintain audit trail compliance \(products received approximately 7 days after vendor invoice for liability tracking\)

REQ\-3\.01\.06: Inventory valuation reporting by location\. Integration with client\-owned storage tracking \(SnapTracker functionality\)

REQ\-3\.01\.07: Drag\-and\-drop bin assignment interface for warehouse efficiency

### <a id="_Toc213923719"></a>3\.01\.02 Current State Process

Pivot currently manages receiving and warehouse operations using a combination of IQ Coordinator for live order product location tracking and D365 for financial receiving\. This dual\-system approach exists because D365 has approximately 900,000 locations due to customization that creates a unique site/warehouse for each line item\.

__Process Flow:__

- Product arrives at warehouse and is physically received
- Product location is recorded in IQ Coordinator \(locations do not exist in D365\);  Warehouse team manually writes location on packing slip, BOL from manufacturer then given to admin for entry into IQ and D365\.
- Approximately 7 days after vendor invoice is received, product is formally received in D365 for liability tracking and audit compliance\.  This applies to drop shipments only\.
- Mystery products are segmented in warehouse and tagged for later identification
- Auditors review inventory through reports and physical site visits
- SnapTracker used since 2021 for client\-owned storage tracking

__Pain Points:__

- 900,000\+ locations in D365 making system unwieldy and difficult to manage
- Dual system management requiring manual processes between IQ Coordinator and D365
- Cannot run location\-based reports from IQ Coordinator
- Significant challenge with mystery product identification, especially from dealer partners, Amazon, and various web sources
- Manual receiving processes required for audit compliance

### <a id="_Toc213923720"></a>3\.01\.03 NetSuite Orion Solution

NetSuite Orion addresses Pivot Interiors' warehouse management challenges through lot\-numbered inventory tracking and flexible bin management\. The solution eliminates the need for 900,000\+ separate locations while providing robust location tracking capabilities\.

__Key Capabilities:__

- Lot\-numbered inventory provides complete traceability for cost and location tracking without creating excessive system locations
- Single product can be received to multiple bin locations with drag\-and\-drop assignment
- Virtual locations support different inventory types \(pre\-sold, showroom, damaged/return, third\-party warehouses\)
- Inventory adjustments support mystery product handling with ability to assign part numbers
- Comprehensive inventory valuation reporting by location
- Future Integration potential with CAM \(Client Asset Management\) for client\-owned storage, similar to SnapTracker functionality Snaptracker will not be integrated with Orion\.  RF Smart probable solution with their License Plating functionality

### <a id="_Toc213923721"></a>3\.01\.04 Future State Process

With NetSuite Orion implementation, Pivot Interiors will consolidate warehouse management into a single system with streamlined receiving and location tracking:

- Product arrives at warehouse and is received in NetSuite with lot number assignment
- Warehouse staff uses drag\-and\-drop interface to assign products to bin locations \(including multiple bins for items like conference tables\)
- Financial receiving triggered manually approximately 7 days after vendor invoice to maintain audit compliance
- Mystery products assigned to dedicated location with inventory adjustments used when products are later identified
- All location\-based reporting available in real\-time from single system
- Audit trails maintained automatically through system tracking\.  NetSuite Orion provides 360 view of item transactions\.  Custom reporting possible to meet business requirements\.
- Client\-owned storage potentially managed through CAM integration \(Phase 2 consideration\)
- Current release of Orion will generate ASN’s

### <a id="_Toc213923722"></a>3\.01\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__REQ\-3\.01\.01__

Lot\-numbered inventory tracking

Cost traceability and product location management using lot numbers to eliminate 900,000\+ separate locations while maintaining full traceability\.

Align

__REQ\-3\.01\.02__

Multiple bin receiving

Ability to receive single products to multiple bin locations for items like conference tables with separate bases and tops using drag\-and\-drop assignment\.

Align

__REQ\-3\.01\.03__

Virtual locations

Different inventory types including pre\-sold inventory, showroom inventory, damaged/return inventory, and third\-party warehouses\.

Align

__REQ\-3\.01\.04__

Product Returning from Client handling

Support for unidentifiable products through inventory adjustments and dedicated locations\. Create 'Mystery Product' location and use adjustment workflow when products are later identified\.

Provided NetSuite/Orion receiving transactions are completed, the client will have visibility to location within the warehouse\.

If time to research is needed, item\(s\) can be moved into a “Mystery” bin in Orion until reconciliation is complete\.  If not found, can be removed from inventory using Inventory Adjustment functionality

Adapt

__REQ\-3\.01\.05__

Manual receiving triggers

Maintain audit trail compliance with products received approximately 7 days after vendor invoice for liability tracking\. Manual approval/trigger for item receipt transactions\.

Possible to create a reminder for items pending receipt based on expected receipt date

Align

__REQ\-3\.01\.06__

Inventory valuation reporting

Inventory valuation reporting by location\. Standard reports filtered and grouped by warehouse, virtual location, or specific bin\.

Align

__REQ\-3\.01\.07__

Drag\-and\-drop bin assignment

Drag\-and\-drop bin assignment interface for warehouse efficiency\. Visual interface for quick rack location assignment\.

Align

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213923723"></a>3\.02 Scheduling & Resource Management

### <a id="_Toc213923724"></a>3\.02\.01 Your Business Requirements

Pivot Interiors requires comprehensive scheduling and resource management capabilities that go beyond basic assignment to include skills tracking, certification management, and route optimization\. Key requirements include:

__REQ\-3\.02\.01:__ Track badging/tagging requirements for site access \(healthcare facilities, government buildings, etc\.\)

__REQ\-3\.02\.02:__ Skills matrix tracking for resource capabilities and job complexity matching

__REQ\-3\.02\.03:__ Daily route planning for delivery trucks in Northern and Southern California\.  Tracking capability in Orion

__REQ\-3\.02\.05:__ Resource assignment based on job requirements \(complex jobs require experienced leads, field cuts require specific skilled workers\)

__REQ\-3\.02\.06:__ Integration between route planning and work order system

### <a id="_Toc213923725"></a>3\.02\.02 Current State Process

Resource allocation is currently handled through personal knowledge and manual coordination rather than systematic tracking\. Installation managers coordinate scheduling based on their understanding of team capabilities, but this knowledge is not captured in any formal system\.

__Current Resource Assignment Process:__

- Installation manager reviews work order and assesses job complexity
- Manager assigns resources based on personal knowledge of skills, certifications, and availability
- Basic resource tracking in IQ Coordinator \(Installer 1, 2, 3, 4\)
- Installation proceeds with assigned resources

__Current Route Planning Process:__

- Crystal report generates daily list of DUR orders
- Service operations admin receives report and confirms orders
- Information transferred manually to dispatching system
- Route planning conducted for Northern and Southern California trucks
- Daily trucks dispatched to deliver DUR orders in their areas
- Process is very manual and is difficult for users to ensure correct delivery information

__Pain Points:__

- No formal skills matrix or capability tracking
- Badging/certification requirements not systematically tracked
- Reliance on personal knowledge rather than system tracking
- Notes in IQ Coordinator are outdated
- Manual report generation and order confirmation for route planning
- Separate systems for route planning and order management

### <a id="_Toc213923726"></a>3\.02\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive resource management capabilities including skills tracking, certification management, and route optimization through the Operations Suite\. The platform enables systematic resource assignment based on requirements rather than institutional knowledge\.

__Key Capabilities:__

- Resource badging/tagging system for tracking site access certifications \(healthcare, government, etc\.\)
- Skills matrix functionality to track resource capabilities and match to job requirements
- DUR order type identification and processing
- Work order events support delivery\-only orders
- Route planning integration with work order system
-  daily delivery route generation capabilities
- Resource assignment based on skills, certifications, and job complexity

### <a id="_Toc213923727"></a>3\.02\.04 Future State Process

With NetSuite Orion implementation, Pivot Interiors will move from knowledge\-based to system\-driven resource management:

__Resource Assignment Process:__

- Work order created with job requirements and site access needs
- System identifies qualified resources based on skills matrix and certifications
- Installation manager selects from qualified resources considering availability and job complexity
- Resources assigned in system with complete tracking
- Installation proceeds with system\-tracked resource assignments

__Route Planning Process:__

- DUR orders identified in system
- Automated daily delivery route generation for Northern and Southern California
- Routes optimized based on location and delivery requirements
- Trucks dispatched with integrated work order information
- Delivery completion tracked in real\-time – ss with dashboard

### <a id="_Toc213923728"></a>3\.02\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__REQ\-3\.02\.01__

Resource badging/tagging system

Site access requirements \(healthcare facilities, government buildings, etc\.\)\. Track certifications and credentials required for specific job sites to ensure compliance with client access requirements\.

Align

__REQ\-3\.02\.02__

Skills matrix tracking

Resource capabilities and job complexity matching\. Systematically track worker skills, experience levels, and specialty capabilities \(e\.g\., field cuts, complex installations\) to match resources to job requirements\.

Align

__REQ\-3\.02\.03__

Daily route planning

Two delivery trucks in Northern and Southern California\. Plan and optimize daily delivery routes for final mile deliveries in each region\.

Align

__REQ\-3\.02\.04__

DUR order processing

DUR \(Delivery Upon Receipt\) order processing for final mile deliveries\. Identify and process single\-item deliveries when trucks are in client areas\. Cost\-only orders internal to operations\.

Align

__REQ\-3\.02\.05__

Resource assignment by job requirements

Complex jobs require experienced leads, field cuts require specific skilled workers\. System\-driven resource assignment based on job complexity, required skills, certifications, and availability rather than institutional knowledge\.

Align

__REQ\-3\.02\.06__

Route planning integration

Integration between route planning and work order system\. Seamless connection between daily route optimization and work order management to eliminate manual handoffs and separate dispatching systems\.

Align

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213923729"></a>3\.03 Work Order Management

### <a id="_Toc213923730"></a>3\.03\.01 Your Business Requirements

Pivot Interiors requires sophisticated work order management that streamlines creation, supports complex phased installations, and eliminates manual handoffs between systems\. Key requirements include:

__REQ\-3\.03\.01:__ Streamlined work order creation from sales order lines

__REQ\-3\.03\.02:__ Automated dashboard reminders when all purchase orders are acknowledged and ready for scheduling

__REQ\-3\.03\.03:__ Custom groupings in smart table for purchase order organization

__REQ\-3\.03\.04:__ Work order creation based on purchase order groups rather than line items

__REQ\-3\.03\.05:__ Support for phased installations

__REQ\-3\.03\.06:__ Multiple work order events for single work orders

__REQ\-3\.03\.07:__ Elimination of manual file transfer and duplication across systems

__REQ\-3\.03\.08:__ Coordination with installation managers for scheduling

__REQ\-3\.03\.09:__ Automated notifications when work orders are scheduled

### <a id="_Toc213923731"></a>3\.03\.02 Current State Process

Current work order process involves multiple systems with significant manual handoffs and file duplication\. Project Coordinators and Project Managers create work orders in Workfront after coordinating with installation managers and clients, then work orders are manually transferred to IQ Coordinator for installation team processing\.

__Process Flow:__

- PC/PM reaches out to installation manager outside system to discuss availability for specific week
- Installation manager confirms capacity and provides specific dates
- PC/PM contacts client to confirm dates work for their schedule
- After client approval, formal work order created in Workfront with scope, dates, and PO numbers
- Work order submitted in Workfront to installation team
- Installation team manually transfers text and information from Workfront to IQ Coordinator
- Pick/pack lists printed from D365
- Installation scheduled in IQ
- Automated email sent to PC/PM when installation scheduled

__Phasing Strategy:__

Work orders are intentionally structured at the __purchase\-order level \(rather than individual line items\)__ to support complex, multi\-phase fulfillment models and optimize warehouse picking, staging, and outbound logistics\. Large\-scale installations follow a __sequenced delivery cadence__—for example, Day 1 \(~40% of materials\), Day 3 \(~40%\), and Day 5 \(final ~20%, including chairs and lighter components\)—requiring tightly coordinated inventory availability, labor resourcing, dock scheduling, and carrier management\.

To enable these phased deployments, __custom PO groupings__ are leveraged to align materials to defined installation waves, providing greater control over shipment sequencing, site readiness, dependency management, and downstream field execution while reducing operational risk and re\-handling\.

__Pain Points:__

- Multiple manual handoffs between Workfront and IQ Coordinator
- Significant file duplication across Workfront, quote requests, and IQ \(described as 'E\-waste'\)
- Manual transfer process between systems is time\-consuming and error\-prone
- No automated triggers indicating when scheduling readiness achieved
- Current system doesn't optimize for purchase order grouping needed for warehouse efficiency

### <a id="_Toc213923732"></a>3\.03\.03 NetSuite Orion Solution

NetSuite Orion streamlines work order management by eliminating system handoffs and supporting purchase order\-based work order creation\. The solution provides integrated workflow from sales order through work order creation and execution\.

__Key Capabilities:__

- Work orders created directly from sales order lines within single system
- Dashboard reminders automatically trigger when all POs acknowledged
- Custom groupings in smart table enable purchase order organization by phase
- Mass selection and filtering capabilities by custom groups
- Work orders created based on purchase order groups to avoid pallet splitting
- Multiple work order events support phased installations
- Files attached once and available across all related records
- Coordination workflow supported through system notifications and assignments
- Pick/pack lists generated directly from work orders

### <a id="_Toc213923733"></a>3\.03\.04 Future State Process

With NetSuite Orion implementation, work order creation becomes streamlined within a single system:

- Dashboard alerts PC/PM when all purchase orders acknowledged for project
- PC/PM uses custom groupings in smart table to organize purchase orders by installation phase
- PC/PM coordinates with installation manager through system to discuss availability
- After confirming dates with client, work order created in NetSuite with purchase order groups
- Work order includes all relevant files \(no duplication needed\)
- Multiple work order events created for phased installation \(e\.g\., 40%/40%/20%\)
- Installation manager schedules work order events
- Automated notifications sent to PC/PM upon scheduling
- Warehouse generates pick/pack lists directly from work order
- Installation proceeds with complete system visibility

### <a id="_Toc213923734"></a>3\.03\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__REQ\-3\.03\.01__

Streamlined work order creation

From sales order lines\. Create work orders directly within NetSuite from sales order lines, eliminating manual transfer between Workfront and IQ Coordinator systems\.

Align

__REQ\-3\.03\.02__

Automated dashboard reminders

When all purchase orders are acknowledged and ready for scheduling\. System automatically triggers dashboard alerts to PC/PM when project is ready for work order creation, replacing manual monitoring\.

Reminder can be created to alert user to acknowledge

Accommodate

__REQ\-3\.03\.03__

Custom groupings in smart table

Purchase order organization\. Enable custom groupings to organize purchase orders by installation phase \(Day 1, Day 3, Day 5\) for efficient warehouse pulling and phased delivery planning\.

Align

__REQ\-3\.03\.04__

PO group\-based work order creation

Based on purchase order groups rather than line items\. Create work orders using entire purchase order groups to avoid pallet splitting and optimize warehouse efficiency\. Critical for 40%/40%/20% phasing strategy\.

Align

__REQ\-3\.03\.05__

Phased installations support

Support for phased installations \(e\.g\., 40%/40%/20% splits\)\. Typical phasing: Day 1 \(40% of product\), Day 3 \(40% of product\), Day 5 \(20% \- chairs and easy items\) to manage appropriate product amounts on job sites\.

Additional scenarios to be tested to ensure Orion meets customer’s requirements

Align

__REQ\-3\.03\.06__

Multiple work order events

For single work orders\. Support multiple work order events within a single work order to accommodate phased installations without creating separate work orders for each phase\.

Align

__REQ\-3\.03\.07__

Eliminate file duplication

Elimination of manual file transfer and duplication across systems\. Files attached once in NetSuite and available across all related records \(sales orders, work orders, pick lists\), eliminating 'E\-waste' across Workfront, quote requests, and IQ\.

Align

__REQ\-3\.03\.08__

Coordination workflow

With installation managers for scheduling\. System\-supported coordination workflow through notifications and assignments, replacing outside\-system phone calls and emails for availability discussions\.

Discuss options with developer \(Joe\)

Align

__REQ\-3\.03\.09__

Automated scheduling notifications

When work orders are scheduled\. Automated notifications sent to PC/PM upon work order scheduling by installation manager, maintaining current automated email functionality\.

Accommodate

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213923735"></a>3\.04 Vendor Returns Management

### <a id="_Toc213923736"></a>3\.04\.01 Your Business Requirements

Pivot Interiors requires flexibility in vendor return management as most damaged products do not need to be returned to vendors\. Key requirements include:

__REQ\-3\.04\.01:__ Decision point on implementing formal vendor return authorization \(VRA\) process

__REQ\-3\.04\.02:__ Support for zero\-cost replacement product receiving

__REQ\-3\.04\.03:__ Ability to track replacement products against original orders

__REQ\-3\.04\.04:__ Vendor\-managed return logistics \(call tags and pickup arrangements\)

__REQ\-3\.04\.05:__ Documentation and tracking for audit purposes

### <a id="_Toc213923737"></a>3\.04\.02 Current State Process

Vendor returns are relatively infrequent and handled informally\. Most damaged products are not returned as vendors typically send replacements at zero cost after reviewing damage photos\.

__Process Flow:__

- Issue identified with product \(damaged or wrong item\)
- Vendor contacted with photos and documentation
- Vendor evaluates need for physical return \(most often doesn't want product back\)
- If return required, most often, the vendor provides call tag and arranges pickup at their expense\.  If was responsible for the error, client will pay  additional expenses\.
- Product packaged with documentation and picked up by carrier
- Replacement sent at zero cost on new PO line

__Pain Points:__

- Informal process with no systematic tracking
- Need to decide if formal VRA process would be beneficial
- Managing cost adjustments for replacements

### <a id="_Toc213923738"></a>3\.04\.03 NetSuite Orion Solution

NetSuite Orion can support both formal and informal vendor return processes based on Pivot Interiors' decision\. The platform provides vendor return authorization functionality if needed while also supporting simple replacement tracking\.

__Key Capabilities:__

- Optional formal VRA process with approval workflows
- Zero\-cost replacement product receiving support
- Tracking of replacement products against original purchase orders\.  Will not create issues with invoicing
- Documentation attachment for damage photos and correspondence
- Audit trail for all return\-related activities

### <a id="_Toc213923739"></a>3\.04\.04 Future State Process

Future state process will be determined based on Pivot Interiors' decision on formal VRA implementation\. Regardless of approach, system will track replacements against original orders with proper cost handling\.

__If Formal VRA Process Adopted:__

- Issue identified and documented in NetSuite with photos
- VRA created and submitted to vendor through system
- Vendor response tracked in system
- If physical return required, return authorization and tracking number recorded
- Replacement received at zero cost against original PO
- Complete audit trail maintained

__If Informal Process Maintained:__

- Issue documented in NetSuite with basic details
- Vendor coordination handled outside system
- Replacement received at zero cost with notation linking to original issue

### <a id="_Toc213923740"></a>3\.04\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__REQ\-3\.04\.01__

Formal VRA process decision

Decision point on implementing formal vendor return authorization \(VRA\) process\. Currently vendor returns are infrequent and handled informally\. Team needs to decide if formal VRA workflow with approval processes would be beneficial or if informal process should continue\.

Adapt

__REQ\-3\.04\.02__

Zero\-cost replacement receiving

Support for zero\-cost replacement product receiving\. Most damaged products are not returned \- vendors send replacements at zero cost after reviewing damage photos\. System must support receiving replacement products on new PO lines at zero cost\.

For labor chargebacks, Orion can manage as a vendor credit or create a customer record for the vendor and generate an invoice\. Both should be assigned to project for accurate financial reporting 

Align

__REQ\-3\.04\.03__

Replacement product tracking

Ability to track replacement products against original orders\. Link replacement products to original purchase orders and sales orders for complete audit trail and margin tracking\. Miller Knoll uses 'R' designation for 90% of replacement products\.

This is currently a Pivot practice

Any additional sales orders should be assigned to the project record

Align

__REQ\-3\.04\.04__

Vendor\-managed logistics

Vendor\-managed return logistics \(call tags and pickup arrangements\)\. When physical returns are required \(rare\), vendors provide call tags and arrange pickup at their expense\. System should document return authorization and tracking information but logistics remain vendor responsibility\.

Align

__REQ\-3\.04\.05__

Documentation and audit trail

Documentation and tracking for audit purposes\. Maintain complete audit trail for all return\-related activities including issue identification, vendor communications, damage photos, return authorizations, and replacement product receiving with proper cost handling\.

Align

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213923741"></a>3\.05 Time Tracking & Project Management

### <a id="_Toc213923742"></a>3\.05\.01 Your Business Requirements

Pivot Interiors requires comprehensive time tracking to measure project efficiency and prevent fraud\. Key requirements include:

__REQ\-3\.05\.01:__ Budget vs actual reporting for design and project management work\.  Decision needed if expense records should be report against budget\.  Expensify functionality to be reviewed

__REQ\-3\.05\.02:__ Time tracking for employees, subcontractors, and temporary resources

__REQ\-3\.05\.03:__ Support for both full job subcontracting and supplemental labor

__REQ\-3\.05\.04:__ Time tracking for warranty work and service revenue streams

__REQ\-3\.05\.05:__ Integration with project margin calculations

### <a id="_Toc213923743"></a>3\.05\.02 Current State Process

Current time tracking is limited with no systematic budget vs actual reporting\. The organization has experienced fraud in the past with falsified time records for temporary workers\.

### <a id="_Toc213923744"></a>3\.05\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive time tracking with budget vs actual reporting, support for multiple resource types, and fraud prevention controls including unexpected worker notifications\.

### <a id="_Toc213923745"></a>3\.05\.04 Future State Process

With implementation, all project time will be tracked against budgets with real\-time visibility into variances\. System will flag unexpected workers to prevent fraud\.

### <a id="_Toc213923746"></a>3\.05\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__REQ\-3\.05\.01__

Budget vs actual reporting

For design and project management work\. Capture budgets for Design and PM work, then track actual time spent to measure project efficiency\. Enable real\-time visibility into variances and cost overruns\.

Budget vs\. Actual reporting is at the project level\.  Time can be tracked on the sales order or at the project level

Align

__REQ\-3\.05\.02__

Multi\-resource time tracking

Time tracking for employees, subcontractors, and temporary resources\. Support time entry and tracking across all resource types with appropriate cost allocation and billing rules for each category\.

Align

__REQ\-3\.05\.03__

Subcontracting flexibility

Support for both full job subcontracting and supplemental labor\. Handle scenarios where entire jobs are subcontracted out as well as cases where subcontractors supplement internal installation teams\.

Align

__REQ\-3\.05\.04__

Service revenue time tracking

Time tracking for warranty work and service revenue streams\. Separately track time for warranty work \(cost center\) and billable service work \(revenue stream\) to measure profitability by service type\.

Align

__REQ\-3\.05\.05__

Project margin integration

Integration with project margin calculations\. Time tracking costs automatically flow into project margin reports, showing impact of design, PM, installation, and service time on overall project profitability\.

Align

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213923747"></a>3\.06 Punch List & Issue Management

### <a id="_Toc213923748"></a>3\.06\.01 Your Business Requirements

Pivot Interiors requires streamlined punch list management with companion sales orders for punch items\. Key requirements include:

__REQ\-3\.06\.01:__ Companion sales order functionality for punch orders tied to original projects

__REQ\-3\.06\.02:__ Punch order type with approval workflow \($250 limit\)

__REQ\-3\.06\.03:__ Ability to quickly identify replacement products \(90% have 'R' designation from Miller Knoll\)\.  Need to evaluate possible solutions in Orion to meet Pivot’s requirements

__REQ\-3\.06\.04:__ Track punch resolution costs against project margins

__REQ\-3\.06\.05:__ Punch records tied to punch resolution records for complete tracking

### <a id="_Toc213923749"></a>3\.06\.02 Current State Process

Current punch list management requires involving multiple teams to get punch orders entered\. Replacement products arrive but there are often no open PO lines to receive against, requiring manual coordination\.

### <a id="_Toc213923750"></a>3\.06\.03 NetSuite Orion Solution

NetSuite Orion provides integrated punch list management with companion sales orders, approval workflows, and automatic linking to original projects for margin tracking\.

### <a id="_Toc213923751"></a>3\.06\.04 Future State Process

Punch issues will be created in system with automatic companion sales order generation\. Orders requiring approval above $250 will route through workflow\. All punch costs will be tracked against original project margins\.

### <a id="_Toc213923752"></a>3\.06\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__REQ\-3\.06\.01__

Companion sales order functionality

For punch orders tied to original projects\. Create companion sales orders that automatically link to original project sales orders, maintaining relationship for tracking and margin analysis\.

Align

__REQ\-3\.06\.02__

Punch order approval workflow

Punch order type with approval workflow \($250 limit\)\. Orders under $250 process automatically, orders above $250 route through approval workflow for cost control\. Incremental approval thresholds supported\.

Accommodate

__REQ\-3\.06\.03__

Replacement product identification

Ability to quickly identify replacement products \(90% have 'R' designation from Miller Knoll\)\. System recognizes replacement product codes and corrective action order types\.

Adapt

__REQ\-3\.06\.04__

Link punch to original orders

Link punch orders to original sales orders and projects\. Maintain complete traceability from original order through punch identification, resolution order, and final cost tracking for audit and analysis\.

Align

__REQ\-3\.06\.05__

Punch cost margin tracking

Track punch resolution costs against project margins\. Punch costs automatically flow to original project margin calculations, showing true project profitability including all corrective actions and warranty work\.

Align

__REQ\-3\.06\.06__

Complete punch tracking

Punch records tied to punch resolution records for complete tracking\. Link punch issue records to resolution records \(replacement orders, service calls, etc\.\) creating complete history from problem identification through final resolution\.

A list will be created in Orion for Punch Issue Type, Punch Reason, and Punch Resolution\.

Ticket create with Orion dev team

Align

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213923753"></a>3\.07 Field Operations

### <a id="_Toc213923754"></a>3\.07\.01 Your Business Requirements

Pivot Interiors requires integrated field service capabilities to replace PlanGrid and eliminate licensing costs\. Key requirements include:

__REQ\-3\.07\.01:__ Field service app with floor plan management capabilities

__REQ\-3\.07\.02:__ Document and image pinning to floor plans

__REQ\-3\.07\.03:__ Photo documentation for CYA purposes \(site conditions, damage by others, progress\)

__REQ\-3\.07\.04:__ Offline capability for field teams

__REQ\-3\.07\.05:__ Signature capture and status reporting

__REQ\-3\.07\.06:__ Integration with main project system to eliminate duplication

\+\+ Ability to generate reports from Photos pinned on floor plans and from punch pinned on floor plans\. Plangrid allows exporting to create PDF photo reports, PDF punch reports, and filtering \(so you can create reports based on filters\) – for example, we can add photo stamps and punch stamps in different colors, and then filter by those colors before exporting a report\.

### <a id="_Toc213923755"></a>3\.07\.02 Current State Process

Currently using Autodesk Build/PlanGrid primarily for installation, closeout, and photo documentation\. Pre\-installation meetings include PM, installation manager, lead installer, and designer reviewing scope with floor plans in PlanGrid\.

### <a id="_Toc213923756"></a>3\.07\.03 NetSuite Orion Solution

Orion Field Service app provides floor plan management, document pinning, photo capture, offline capability, and integration with main system\. This can replace PlanGrid functionality and eliminate separate licensing costs\.

### <a id="_Toc213923757"></a>3\.07\.04 Future State Process

Field teams will use integrated Orion Field Service app for floor plans, task management, and photo documentation\. All information syncs automatically with main system\. PlanGrid license can be eliminated after current contract expires \(approximately 1\.5\-2 years from implementation\)\.

### <a id="_Toc213923758"></a>3\.07\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__REQ\-3\.07\.01__

Field service app with floor plans

Floor plan management capabilities\. Mobile field service app that allows field teams to view and interact with floor plans during installation, closeout, and documentation activities\. Replaces PlanGrid functionality\.

Align

__REQ\-3\.07\.02__

Document and image pinning

To floor plans \(lookbooks, clarifications, task instructions\)\. Pin documents and images to specific locations on floor plans so installers can see product specifications, clarifications, and instructions for each building section or room\.

Align

__REQ\-3\.07\.03__

Photo documentation for CYA

For audit purposes \(site conditions, damage by others, progress\)\. Capture and store photos documenting pre\-installation site conditions, damage caused by other trades, and installation progress for liability protection and project documentation\.

Custom report to be created

Align

__REQ\-3\.07\.04__

Offline capability

For field teams\. Field teams can access floor plans, documents, and task information even without internet connectivity\. Photos and updates sync automatically when connection is restored\.

Align

__REQ\-3\.07\.05__

Signature capture and status

Signature capture and status reporting\. Capture client signatures for work completion, delivery acceptance, and change orders\. Update work order status in real\-time from the field\.

Align

__REQ\-3\.07\.06__

Integration with main system

Integration with main project system to eliminate duplication\. Seamless integration between field service app and main NetSuite system ensures information entered once is available everywhere, eliminating duplicate data entry and file management\.

Align

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc213923759"></a>4 SuiteApps

## <a id="_Toc213923760"></a>4\.01 SuiteApp Summary

To be determined based on specific add\-on requirements identified during implementation\.

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc213923761"></a>5 Assumptions

The following is a list of assumptions based on the solutions proposed in this document\.

__Document Section__

__Assumptions__

3\.01 Receiving & Warehouse Management

CAM integration for SnapTracker replacement functionality will be deferred to Phase 2 after core system stabilization\. Pivot will use standard NetSuite inventory valuation reporting in Phase 1\.

Snaptracker will not be integrated with Orion\.  CAM integration will not be included in Phase 1

3\.01 Receiving & Warehouse Management

Mystery product handling process will be established during implementation with dedicated location and inventory adjustment procedures\. Warehouse team will be trained on new workflow\.

3\.01 Receiving & Warehouse Management

Current 7\-day delay between vendor invoice and product receiving will continue to be supported through manual receiving triggers for audit compliance\.

3\.02 Scheduling & Resource Management

Current installation team size and structure supports implementation of skills matrix and badging system without requiring extensive historical data migration\.

3\.02 Scheduling & Resource Management

Daily route planning for Northern and Southern California trucks will be configured during implementation with appropriate geographic territories and delivery parameters\.

3\.03 Work Order Management

Workfront and IQ Coordinator systems can be retired after NetSuite go\-live once all teams are trained and comfortable with new integrated work order process\.

3\.03 Work Order Management

Custom groupings functionality in smart table will adequately support current PO organization and phasing requirements \(40%/40%/20% splits\)\.

3\.03 Work Order Management

Historical work orders from IQ Coordinator will not be migrated; only active/open work orders at cutover will be brought into NetSuite\.

Pivot’s intent is to run all D365 orders through IQ until September and manually recreate in Orion\.

3\.04 Vendor Returns Management

Informal vendor return process will continue \(no formal VRA workflow implemented in Phase 1\)\. Team may revisit formal VRA process in Phase 2 based on business needs\.

3\.04 Vendor Returns Management

Vendors will continue to manage return logistics \(call tags, pickups\) at their expense\. NetSuite will provide documentation and tracking only\.

3\.05 Time Tracking & Project Management

All employees, subcontractors, and temporary workers will adopt consistent time entry practices\. Mobile time entry will be available for field resources\.

UKG does not integrate with Orion at this time

3\.05 Time Tracking & Project Management

Historical time tracking data will not be migrated\. Budget vs actual reporting will begin fresh with Phase 1 projects\.

3\.06 Punch List & Issue Management

$250 approval threshold will be configured as initial setting and can be adjusted post go\-live based on actual usage patterns\. Incremental approval levels can be added as needed\.

3\.06 Punch List & Issue Management

Miller Knoll 'R' designation for replacement products will continue to be used and will be leveraged for streamlined receiving identification\.

3\.07 Field Operations

PlanGrid contract will run concurrent with NetSuite Orion Field Service implementation during transition period \(~1\.5\-2 years remaining\)\. Full migration to NetSuite Orion Field Service after contract expiration\.

PlanGrid license expires 1/10/2027

3\.07 Field Operations

All field team members have or will be provided with appropriate mobile devices \(tablets/smartphones\) capable of running NetSuite Orion Field Service app\.

3\.07 Field Operations

Key floor plans and documents from PlanGrid will be migrated to NetSuite during implementation\. Historical project documentation may remain in PlanGrid archive\.

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc213923762"></a>6 Unresolved Requirements

To be populated pending Business Requirements Document review with the Pivot Interiors team\.

__Area__

__Description__

__Impact__

__Proposed Mitigation Strategy__

3\.01 Receiving & Warehouse

CAM \(Client Asset Management\) integration timeline and approach for SnapTracker replacement functionality

Medium \- Client\-owned storage tracking currently managed in separate system \(SnapTracker since 2021\)

Defer to Phase 2 after core receiving processes are stable\. Evaluate CAM SuiteApp capabilities and integration requirements in follow\-up session\.

3\.04 Vendor Returns

Formal VRA process decision \- implement structured workflow vs\. continue informal vendor\-managed approach

Low \- Vendor returns are infrequent; most vendors don't want products back

Recommend starting with informal process in Phase 1, evaluate formal VRA for Phase 2 based on actual usage patterns and audit requirements\.

3\.05 Time Tracking

User adoption strategy and training approach for comprehensive time entry across all resource types

High \- Success depends on consistent time entry by employees, subcontractors, and temporary workers

Develop comprehensive training program with mobile time entry demo, clear procedures, and management enforcement of time tracking policies\.

Management dashboards available for employee time entries\.

3\.07 Field Operations

PlanGrid migration strategy and document transfer approach

Medium \- Need to plan migration of floor plans, documents, and historical project data from PlanGrid

Run parallel systems during transition period\. Define which historical documents migrate vs\. archive in PlanGrid\. Brian Hagerty to provide field service application screenshots\.

Deadline for migration to Orion Field Service is Q3 2026

3\.07 Field Operations

Mobile device readiness for all field team members

Medium \- Field teams need tablets/smartphones capable of running NetSuite Orion Field Service app

Conduct device inventory assessment\. Determine if existing devices are adequate or if new devices needed\. Budget for any required hardware purchases\.

General

Job site receiving requirements for audit compliance

Medium \- Sandra and Marcus to have preliminary conversation, then include in Financial Management Discovery Session

Coordinate with Finance team to define job site receiving workflow that maintains audit trail compliance while supporting field operations\.

General

Field Service app and Operations Suite updates demonstration

Low \- Team wants to see full capabilities before finalizing requirements

Schedule comprehensive demo of NetSuite Orion Field Service app and latest Operations Suite features with Pivot team\.

General

Historical data migration scope and strategy

Medium \- Need to determine which historical data \(work orders, time entries, punch lists\) should be migrated vs\. archived

Define data migration strategy during Realize phase\. Recommend migrating only active/open items at cutover, archive historical data for reference\.

# <a id="_Toc213923763"></a>7 Signatures

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

# 8 Appendix

APPN\-01:  REQ\-3\.01\.04: Return Authorization

# ![A diagram of a process

Description automatically generated](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0gAAAGcCAYAAADj14DLAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAANUYSURBVHhe7P0FdFTZ168L3zHuuN+444xxznfe97zvX9sNd3d3dycECQRJ0CQkQRMkxIMnEAgerHF3d3dvXBvpBtrgd9dvVna6SIomgVhRcw0eqmrvtaV2VaXWU3Otuf6vP37/DYqiKIqiKIqiKMpvUEFSFEVRFEVRFEVJIlmQXv3xO7Ro0aJFixYtWrRo0aLFNcvrPwWJcvTLyxfYt3c39u3ehUP79yrZxb69OHxgH/bu2omd27dir3k99uzeqSiKoiiKoihKJrB3zy5s37oZ9+/ewatXf9gEieXBvbuoWbUSatWuicbNmqBR08ZKNtGkeRNUqFAWDerUgme3zvDo3AndOrspiqIoiqIoipKBsJ3do2tnVKlQDuOjI8WL3hCkhvXrIjAmGtGLFyN8/nwlG4hYsABRixahYetWiJ00Ab+8fImff3qKn549URRFURRFURQlA2E7++XLFwgeMQzRkWHiRW8IUpPGDRAUF4fYNWswaflyJRuYvGIFpq5ejeYdO2B2/DR5bdgfEq9fKYqiKIqiKIqSkbCdbUpYyBiMj46Q+6kEaeTUqZiyahUmfP+9kg1MXLYMk1euRLMO7ZEwLVZeG44R4+ukKIqiKIqiKErGYSWqGzdmlApSTkUFSVEURVEURVGyBhUkJ0AFSVEURVEURVGyBhUkJ0AFSVEURVEURVGyBhUkJ0AFSVEURVEURVGyBhUkJ0AFSVEURVEURVGyBqcQJMpB7Nq1iF2ThLk/ZfVqIw7LHdZPycTlyyVNuWznhKKngqQoipK5vK04qqsoiqJ83OR4QaIcjImPR0BEBIZERRkiEWgIjp2aLA6OtrOgHEXMny/bBkSEY1RcHCaY7RzVzamoICmKomQe/Ht6/txZ7N+7B4cO7MfBA/tw7OhhPHxwX//eKoqiuCA5WpAoBjxuuy6dkeuLT5Hn6y/wzaf/xLef/htFC+ZHa3c3RC9aJJOpOtqecILVwOhIFM6XG99+8k80a9Mak1askH07qp8TUUFSFEXJHKwvwS6dOuKTf/w3PvvX3/H3//z/4+vPP0GDOjWxcf1aWe9oW0VRFOXjxCkEqYNHN+T+8lPUrF0TnXp6opVbB5QsVhi5zBdY5969MHXtWqlP8WEXvLh16zB1zRqJHokILV2KFu3b4rvP/mVu2yULEtezHutzuzdES469GrFrzTqzf4pWdkmVCpKiKErmYH0Jdu/aGV9++i/07N4N4eNC0MWtPT7/9z9QpXwZXLl8SerYim12dZbXr/6QfaQqr1+9cQzWS1msdbYZ2+2K3baOtrP+9jsq1naKoijKh+E0gvTtJ/9AV28vJGzbjvjNm9HTz9dI02eoXrM6YhYvFsGJXLBAut/5mS+3YRPGm30sFbHg+CPW/9ZOkLhf7n/4xInwDRkr28UsWSz1RUhWrJTueH6h4zA4NBRBU6bIcbJDklSQFEVRMgd7Qfrik39i0/p18vjnZ0/RukVT/Otv/4m1q1fh559/xq4d2/Ds6RPcuH4Nu3dux9Mnj6Uub9ktb8e2LThx/Kjsl8V2axOqC+fOmvVbzT6249aN68nH/f23X3H82BFs37oZhw8dwG+//WKWvsZrI0qsc+rEcdnvvj27cPXKJfz2K9cDTx7/iAP79si6wwcP4OH9e/q9oCiKkkFYf6NzvCB9YydIM7ZsQZ+AABGkGrVqiPCMnDJZ7uf95kt89c+/oWCe79CoRTOEzpmDaevXo/vAAcmCxAQPEUammrVtg4K5v8NX//hv6b7XuGVzWc5jeg4aiBLFCss2PDb3NzQmWiJOjs41M1FBUhRFyRysL0FLkFYu+14eswzs643//t//ExvWr8W5M6eR99uvMKBvH1StWA6f/fPvOH/2jIxdokh99dm/8X/+1/9AvlzfoL93b9y/d08k58WL5xgTHIQSRQrib//xv/A//9//B/28esv+75vv2L59eiK3+d76z//5P/DNl59isO9AI2M/GRH6FaOCRqBQvtz4b7PdP/7rf6NW9cp4YEToyqWLaNuqBb7+/N9yfv/4P/8bQwMGyz4dPUdFURQlfTiNIFGGatWpha79vNGhezeUKV1ClvUYNEC6xtU0674zX1B1GtRFt359UalyBRGb9t06G0HagB5JgtSyQzvErVuPdl274Dvz5cL6vQb7oW6Desj1xSfw6N9PIlFFCuRF4fx5zPZdZH+NmjfFsPHjRa4cnWtmooKkKIqSOaQUpGVLFuOPP/7A4YP7UbVSeXz56T+xf98eEaRSRQuLCNWtWR3T42Jx/dpVuLVrLVGmru4dMXnieDQw30V/+8//hbCQ0bLfObMTZFxTyaKFEDxiGCJCQzB18kS8evUHAvx88O+//xc8Pbpg7pxZaN+mpdRdsihRokNfmO+wyuXLYuL4aERHhsPf1wdPnzzByOFDRLa6uHVA3NQpGOrvhwnRkXI8R89RURRFSR9OI0j5vv0KxQoXQJ6vPhcRosB07t1bxGHUtDgUyP0NypYuiZCZMzF3zx74jBmD/Lm+QYUKZUWgPH0GiSC1duuI6EWLUaVqZVnfta+XRIY4ton7rde4IaIWJqKE+TLL9+2XqG8ed+vfF34hYzF+6VIZt+ToXDMTFSRFUZTMwfoS9PToim+++BQVypRE9coV5Dvm33/7P+jm7oaXL17g6OFDsqxc6RISwWG5dPE8vjPfSTWqVsKd27dkGZM6cFmj+nVk/709PST5Q+yUibLeKowe1ahSEQXyfIeZ0+Owd89uhIwKkgQRfoMG4MSxo7IfHnPQgL5Sh8tYKFp/M/VqVauMcWNHY7H5zrp144asS/n8FEVRlPTjNILEBAu89Q8LQ8niRVG0YD6MmDQRM7dsle51+b75ElWqVDLys1DGKHHMEDPdlS5RTPZjL0iR8xdI3YK5vxWBqlChnEScKpsvq1adOkpiBr/QEBnfVCR/HuT5+nMUypsLPf18bNfB7M/R+WYWKkiKoiiZQ0pBqly+DGpXr4pm5rtvTPDIZPE5sG+vdHerV7uGeWQbV3T61AlJ7NC8SSO8eP5clp09fUq+n6qZ7xSOF+qRFJnauME2tskqt2/dNIJUSbrk1atVHXVqVEOjenUMtRE2bqyp8Rrz5sxGXbMuf+5v8KXZR5kSRSUVOaNIQ/0Hi8x9a86Z+2cE69GD+3j9+rXD56koiqKkHacRpG8//Sc69+mNhG3b4NGvr0R76jaoK+IwbtYsiS7xl7YBQUFmu+Xo1MtTUoPXqltLusVxTBEFqVXH9pi0fIVZXlu66Ln19JRU4WRoTAzGzohHzJIlMm9ScGwsAiPC0bBZY9kXo0k8Hs/L0flmFipIiqIomYP1JWh1sVu+dIk8tpZb5eD+fSJIdWpWS06U8MO1KyhuvnuKFswrkaPnz39GRFgIPvn7f6Fzp/Z4/epVcje6nj264cb1HyTJw+lTJyWxQ9OG9SWdOLvcUbB+evZUEi5Qylhv397dktxhw/p1aNGkIf75X/+BidFR5rjXJJrEMVBxUyebc8iPArm/w8kTtgiTo+epKIqipB2nEKS2nd3x+d/+Q0SJ44eiFy5E1epV8NW//o4uRpqYhtvNs4cID6NCJYoWli55+XN9jf4jh2P6xk0yjujzv/8nmrZuibj16zEgOAiF8uaWpA4lixeRqBQTMQwIGinZ6sqXK22EKw/Kly+D4kUKSte+Lt59zPlkfbpvFSRFUZTMwfoSdGvfVpIhfL94kTxmim3r7yzLvj27JVpTuULZJEF6bdb/IV3cPvvXfyPvd1+jXKniUodJF9atWSXb7di+VcSKY4soU8UK5ZfoFPe/bOli5Pn2S9mmQtlS0n2vYJ5c2Ltrp2TKy2O+xxg1qmW+7zgmlkkiGEGaMnECvjXfd0wWwe6AHBfVuEE9SeAAjSApiqJ8MDlekCgGTLBQrmxJ9PT1lcect8h3XAgqVSqP+o0aIHzeXBln1NPXB7Xr15Hucg2aNsLA0cGS4Y5zGPUdNszsoxTce/eypfk2y/zGjRNhqlK1knSva96uLUZPnybHZbKG2vVqm2NUkAQQfBy1aOGbcyVlESpIiqIomQP/lrJbWvDI4dJ9btvmTam6qfHx6ZMn0Kp5E/T27C6CRMFhhOiXly8wO2EGOnVoK93jevXohi2bNsg2tn2/khTe3r090aRBXemONyEmSvbLsmnDOvTz6mUEpy6aNKyHYYH+0v3u55+eYXTwCLRt2VwSP3R1d8OaVStkm0MH9qOv2YYRKG7j7ztIuvux2J+3oiiK8n7kaEGyYGIEmdzVTk74mNLA8UBMnkBxoQhxmbXOfnJX3trvg48pSZPN8+JywudoCdDklauS9yXrTN3skCOigqQoipK5GNuRv60UH0frrS9LRo7sl1vb2UrqSWT/3I7lz/V/tc6aA+nP8uc62/I/H6fcp6IoivLhWH+Dc7QgUYJEdIjdci6T5Q6WpVxuv87Rsnets1+e1fD4KkiKoiiZB/+m2nerc4RtfWqB4jZM2/1X21v7d1TnbeveZxtFURTlw+HfVZacLUgujgqSoiiKoiiKomQNKkhOgAqSoiiKoiiKomQNKkhOgAqSoiiKoiiKomQNKkhOgAqSoiiKoiiKomQNKkhOgAqSoiiKoiiKomQN7xSkpk0bYWxCAmZs3izzDylZz7T16xG/aRNadHJD4pxZ8tpo0aJFixYtWrRo0aIl80p0RBgmxETK/WRBun/3DurUqo4u/fpiQHAQ+g0fpmQHI4ZjQNBI1KpfF4MH9sfqVSuxasUyrFquKIqiKIqiKEqGYtrZbG937+KOiNAQ8aI3BKlqpfKoXrsGGjRtjPpNGinZBK9/2XKl0bh+HZmp3dOji6IoiqIoiqIomUDP7t1QzXgQo0gsKcYgNURwXBxi167FpOXLlWxg8ooVmLp6NZp37IDZ8dPktbEVzqCuKIqiKIqiKErGYSthIWNSd7GzkjQExcZKA53JApSsh5LEJBlM0jBrepy8Nnj9KnkWdUVRFEVRFEVRMgbznzS3Q8eO1ix2ORVKkmaxUxRFURRFUZTMR9N8OwEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNaggOQEqSIqiKIqiKIqSNWSrILHhH7t2LeLWrfuT9esxZfVqh/UzC54Hnx9vxy9dKjIi58HnbB472iYrUUFSFEVRFEVRlKwh2wRp0ooVCJszB227dEKj5k1Rr1F9oWadmug+cAAmLV8hYuBo24zEkqKxM2cgZvFikTPfsWNRo1YN9PT1zRGRMxUkRVEURVEURckask2Q2OAfEx+PYoXyC206dzKy5I6WHdrBe9hQTF21GtPWb5Dj2kd1eMvtudyKOlnLLOzXUcSItS33xcfTkh5P27ABPmPHoFjhAhgVF4cZmzdj5OTJaO/RFT5jxiRFuP7cduLy5bLfqYxy8bzMvqwo2BRzzvbnkVGoICmKoiiKoihK1pCtgjR2xgyULFYEdRvUw8yt2zBrxw4kbNsmYhQcG4u+w4eJtDCqEzprFvqNGC6PY9esNXI1HQOCRmJAcBBCZ8+W/VkiEWzq9B85QuC60NmzMNDUGzXN7Ms8j3Hcl1k3Zka8nEP9Jo1QMM936OLtJXIUGBkpjEtIMOcxVY4RMnOm7DtywQIMGjMaQ6Kj5LzC580zIjVazi04LlbqpHyuH4oKkqIoiqIoimKh5R3l9SuH1y2tZLsglS5RDNWqVxURoWBQjLh+aEwM8n/3taxjxKdF+7byeOSUyRgcOg5lS5dEmVLFUaxwflSpWlnkh1EcT99BKF6koESlShYrDK/AABGpb/71d7j37oUEI2KUmU/+83+hW7++cOvZA4Xy5kLhfLmlfvcB/dGsTSt89c+/oWN3D/iMHY2v/vU3tOvSGTONvFG0vv3kn2ZfPUWaeH6lihdFyeJFUKpEUYlGZXQkSQVJURRFURRFEUwb8O6d27h4/pyNC4o9ly6cx7OnT+Q6Obx+aSDbBalc2VIiKMWLFEJRIzWUjCFRUZixZQu69vVCwTzfipyUMPLiMaCfdHGrUKEsKleuKNGbgPAwEaeOnt1lfxSjChXKyf2YJUsQtXAh+hshyvP152Z/3pi5ZatEhCg9nj6DMH3jRtSoWV3OYej4GOly52/t0wgSz7VsmZKoVqOqnHO7rp1N3dwYPW0aWnZsj8L582DYhPEYNysBZUqXQPWa1aTrHc8z5XN+X1SQFEVRFEVRFMIywLSRv/vqc5TiD/Smjaz8ybdffoY1q1bKdXJ0/dJCtgtSqRLFUL1GNXM/HmNnzpRl0YsWyXqO+aldtza++fRfqFO/roz7GTFxoowXYpSIclWmVAnk/vJTkSiKzzef/AMe/fth+oaNtrFG5jalIA0cFZwsSDO3bpWEDBSk4RMniDANDgsVQWrftQtmbN6CDh5dUaRAPgyfMAE1ateQLnmR8xegSrXKEnkqV6aUSFT+XF+jUqUKiExMlGM7et7vgwqSoiiKoiiKQlg8Oruhe88eOHjmNLbu26cYth84gO0HD6Jc6ZL4fvFCuU6Orl9ayH5BKl4UtevVsSU6WL9ebikXXM/xPpSn3F9+LhJDUeAYoSIF8sjjIVGR8I8Il9uI+fPRb8QIfP3vf6CzV2+JBPGcp2/chH7DhyH3V59J97nZO3bZBOmf/y2CxEhVNXMMCtLIyZNsghQ6TgSJ0aL4TZsxbPx4FC2YH23cO6FE0cLoO2yoPAfKECNbg0aPQqA5h8DICARNmYLxS5ZggjnXlM/5fVFBUhRFURRFUQiLh3tH+Pj74e7z57hw65ZiuHTnDi7dvYuqlSt+DIJURLq4UXAYeWG3OUaQeLzWbh1lbE+PgQNEYJhZbuKy5aharbIRlnySKIH7GRUXJ9vzlsvLlimFkUZUxs2ebZZNEyHK89XnMo6JyR4aNmsikSYrglSvYX3k++ZLqUdBoyDl+/YrtOviLuOaKCi169eRRA6MWoXNmS3LW7l1QK4vPkVv/8FG6laa480yx4vFpAzsXkdUkBRFURRFURTCwgjSAN9BuP7jjzh19apiOPPDDzhz/TqqVKrg5IIUH4/SJYuhQK5vJEECYZc1N8/ukuwg37dfyv1YIyMNmjRCbiM5viFjpatblaqVJJJUvGgh6d5GqWH0p3fAYInqFCmQV7rhdezRXcSrfuNGEhXi8Vp1bC/HYtY6Zs9jtjvWLZD7G7O9v2Sw47HauLuJMJGefr748u//hdbG2JmEgRnsKHj1mzRMPpaV5GHq6jUOn/P7ooKkKIqiKIqiEBYVpNR8FILERj8jRRz3w6QMARERgn9YmCRAIAGREYheuFCOzXTdTJ7AKNHUNWuk+93QmGhZxm5tnOSViRFYl/MrBbDrXXQUQufYUoCzPh/zeDx+0NQpkoWO3fkY8WEWPP+IMIQkzDR1E6Uu98Pz5HpKFrvQ8Tw4iS33MXmlbY6mEZMmynlQ3FiP29g/1w9FBUlRFEVRFEUhLCpIqfkoBImw4c9oC+c1ovQQRmsoA0TGIxk5sSaKtdZxW4qN1DfbMppjLyU8V2ufVrIE3sbyGFJ3udxyX9w3xwtxH3I8U4+ixe2tYzErHc9Djr+Cy8w2Scficu5Ljmdu+dhal1GoICmKoiiKoiiERQUpNR+NIClpQwVJURRFURRFISwqSKlRQXIxVJAURVEURVEUwqKClBoVJBdDBUlRFEVRFEUhLCpIqVFBcjFUkBRFURRFURTCooKUGhUkF0MFSVEURVEURSEsKkipUUFyMVSQFEVRFEVRFMKigpQaFSQXQwVJURRFURRFISwqSKlRQXIxVJAURVEURVEUwqKClBoVJBdDBUlRFEVRFEUhLCpIqVFBcjFUkBRFURRFURTCooKUGhUkF0MFSVEURVEURSEsKkipUUFyMVSQFEVRFEVRFMKigpQaFSQXQwVJURRFURRFISwqSKlRQXIxVJAURVEURVEUwqKClBoVJBdDBUlRFEVRFEUhLCpIqVFBcjFUkBRFURRFURTCooKUGhUkF0MFSVEURVEURSEsKkipUUFyMVSQFEVRFEVRFMKigpQaFSQXQwVJURRFURRFISwqSKlRQXIxVJAURVEURVEUwqKClJosFaSmTRpidPwMTN+wEVNXr1aygdg1azBt/Qa0cOuIeQkz5LXRokWLFi1atGjR4prFs1tn9PcZqIJkhyVIlSuWx+qVy5Ou1IeVyLBxmBATKfeTBen+3TuoWb0KWnRoD/fePeHWs4eSDXTq6SnXv0r1qvBwd8OE6EhER4QpiqIoiqIoLsbEmChUq1gOAUOHqCDZYQlS7VrV0aNrZ0wcH+3w+qWFmMhwjDft7ZbNGmN8VIoI0v17NkFq2rY1OvbojvYe3ZRsgte/ctXK6Nyxndhs6NjRGKcoiqIoiqK4FFHhYahcvgwCh6kg2WMJUp3aNdC1UwdERYQ7vH5pge3siNAQNG3UQG5ZUnSxa4TRM2Zg+kZ2sVujZAOxa9di2oakLnazZspro0WLFi1atGjRosU1i3axS419F7s1mdnFLjlJQ2wspqxejQnLlinZwMTlyzF51SpJ0jBrWpy8Nq9f/SEDyBRFURRFURTXgUWTNKTGPknDsiWL5Do5un5pge1sFs1il4PRLHaKoiiKoigKYVFBSo29IGmabxdABUlRFEVRFEUhLCpIqVFBcjFUkBRFURRFURTCooKUGhUkF0MFSVEURVGUzACvXylvgeNQHF2z7IZFBSk1KkguhgqSoiiKoiiZxe+//ao4wNG1ygmwqCClRgXJxVBBUhRFURQlI3n9+jXu3b2DFk0aobppUNaoUhE1FaFG5YoyEWunju3w80/PzLV65fAaZhcsKkipUUFyMVSQFEVRFEXJSFhuXL+GQnlzIWjsGEyfMxtT4qcrhhlz58LXfzBKFy+Mn54+MVfqtcNrmF2wqCClRgXJxVBBUhRFURQlI2GhIJUqVhjbDxzEnZ9/xtUHDxXD/Rcv8f2atahYuoQKkhOhguRiqCApiqIoipKRsFiCtHbbNly8c8dho9MVuXLvPuYtWYKKZUqqIDkRKkguhgqSoiiKoigZCYsKkmNUkJwTFSQXQwVJURRFUZSMhEUFyTEqSM6JCpKLoYKkKIqiKEpGwqKC5BgVJOdEBcnFUEFSFEVRFCUjYVFBcowKknOiguRiqCApiqIoipKRsKggOUYFyTlRQXIxVJAURVEURclIWFSQHKOC5JyoILkYKkiKoiiKomQkLCpIjlFBck5UkFwMFSRFURRFUTISFhUkx6ggOScqSC6GCpKiKIqiKBkJiwqSY1SQnBMVJBdDBUlRFEVRlIyERQXJMSpIzokKkouhgqQoiqIoSkbCkhWCdJqNVoOjdR8K93362jWH6z4EFSTnRAXJxVBBUhRFURQlI2FJjyCdvHIF52/dSrdIHTl/HscvXnS4zuLcjRu4cv8+rj54IPd5LEf1UnLi8mWpe+nu3eTG8VnDKWt7I0/nbt5Mt0SpIDknKkguhgqSoiiKoigZCUt6BInisnnPHqzYsMEmIWYZb88bAeG2bJha9SyRIhNjpyJgaKCtDiNJRla4DaXl5JWrUnfPsaOImzkDk+JisWXvXly4fRsXzPKzZl+sd9E8vnj7TrLocD1lalxEOBZ8vxSrNm3CoTNnjIydw0Fza50f6+85elRuCWXp0p27co5c/zZUkJwTFSQXQwVJURRFUZSMhCWtgkS5oNQM9BmIZs2a4NiFCyIhB0+dwvYDB7Bk1UocNctYd//Jk1i/fTtWbtwgUaGla1aj/6D+2HHoYPL+dhw8iGMXL4qwbDuwH159+yA0MgLjp07GktWrcPLyFWzavVv2zTorN27E8vXrZFs+3rpvL5atW4sBgwZgxry5iJ8z2+zzAMaEhhjGyflSotZt24refXqL1F2+exc7Dx3CwuXLsPf4MdmPdT4pUUFyTlSQXAwVJEVRFEVRMhKWtAoSozwbd+3E4AB/DBkxDLMTE3Hj8WMMCxoB/yEB8A8MQODwoUY8jhvZ8cLocWPRx7sPYmfOxKpNGxEwJBCDTGOekrPz8CH07e+Nw2fP4trDhwgJDxOpufnkqQjVJXMe4dHR6NChHdZu3YoZc+dgcKA/gkxDdfrsBCNOu9DDszvGho1D+/ZtMXfxIrNvH5G0vv28zb77isBdvndPoktNmjSUOpv37oG3WT8iOAj9Bw7AdiNpb4skqSA5JypILoYKkqIoiqIoGQlLWgXpyv0HCIkIw/gpk/H9mtUSuWEXt8FGjmYvTMTNp08xyM9HokUUpAOnTmLPsWPw8x8sEZug0aMwJX4axhkZmp24QCI9FBgyclQw4mYl4Ko5Bhu4lKQhw4dhwtQppvH/GF27dRE54vF79PAQwZk+exYe/PKL1KPI8DjrthuZmjMHy9aulf1yXwdOnzayFiJjlChUMZMn4dFvv2OMWRY1cbyIkMPnq4LklKgguRgqSIqiKIqifAi///araT28Nv9e4ZV5zJIWQWJXOkZ72rRphd59ekk0p0GDutiydw+GjRyBWYnzRUD69u8nESIKEruwcbySr7+fCBKjTHuNMDFywyjOig3r5XgcDzR1RrzI1dnrN2Tc0YkrlzFk2FDEzpwhEtazlyeCx4zGwhXLJaI0KmSsyNMPj36UfTE65GO2X7t1C2ImTcKcRQtlO543JY3nwEZzeHSUdOO7/dNPGB40EhNip4pIOXrOKkjOiQqSi6GCpCiKoijK+/L61R948uwpdp88gTsPH5hWhBElU9IiSEyQMNtIh/+QQNtYJCMxURPGI3rSBInmePbsIREldpU7fPYMunRxh89gXxn7M3/pUqzevNmI1HDZP4WqccP6Mv6IAsM03ccvXRLp8e7XV+QrYd486aLHcUU3njwxgrVc9scoFMc17TpyWEQt0EiUp5GnJatWY+iI4diwc6c53hJ4dO+Grfv22WTr8mUZNzXWnBsFjSLG7ngUNo6VspI5pEQFyTlRQXIxVJAURVEURbGHkSBboey8C+Cn5z9j6qqVGG+kZfOhQ3j49Cnu3LyB4oXy/6UgUYoYQaLIUCjYCGVqbcqHX8BgTJ4WZ+TjqIznoXR49vSUBAr7T5yQxA4nLl+SVN+8HxYVKSJF6bL2b+2TyRoYdeKxmPCBEsVjM5kCI0FM2sB1fHzw9Cls279P6pww53Xk3Dk5H9ZnIoZDph7vE65jUghux/vcjySI+ItMdpYgVShVHL+Y62Yrjq5reuDNK4evZXphUUFKjQqSi6GCpCiKoiiKBdsAdx89xIXrP+Dijevv5HKSqExbvRqRixYhLDERceb+wg0bULtOLax7xxgkaXgarMeM/DBLHKNI7C7HcUMUjoOnT2Ns6DgcMKLEZAtS10gK67JLHsce7Tl+PJWciAiZZZQY61g8hjWfEdN9c50s42PTCGZ9Noa5rXVr7Ye31r5Zl9vzPutZx7DWO8ISpGpVK+G0uW5Xbt9yeF3ThTn2PfOaOXo90wuLClJq5L1jrrMKkouggqQoiqI4C1reXRxdt7TC8UNsA2w4eBCHzp3FycuXRX7+ilNXLuPg2bOIM225qMWLEWEkiW2LWWvWoHHzppIO+68EyRGUEHZje0N2KCgUGTtBsWDU6dyNm7ZubdZErilwtF1aseQpI7AEqXr1qtJt8LRZ5ui6phVe//1nTmPr4cP49ZeXeP2BbTgWFaTUqCC5GCpIiqIoijPw6tUfOHr4ECZER2JCVAQmmlvFBq8Hr8vhg/vlOjm6fmmBgvS7YffJk8nJFtJSnr94jrjVqySCtHzXLly/fx/Xr11FicIF3pnFzh6b6NwQ0Tlw6hSOXjgvomTJzYdIzvvC7nXsfsdzc7Q+vdh3sfs1uYvdh5VfjBhxEtuXL1+oIGUSKkguhgqSoiiK4gywhIWMwaf/+juaNm2MRo3qK0nwenz2739gTNAIuU6Orl9asARp14kTeGGkJy3tASZpePzsKTYeOogLpgHJZSy3bvyQpjTf9lCM2JWO6bkH+gxC/4H9MX32bFnOrnSEiRwIZYnjjTj+iMsZYbLqSD2znPvk/TVbNku2OjZymV2O67gtH1sCxsbv+Zu3pMuc7MMsZwa9XYcPSza8o+fPy2Mem+fDbZOPb5alfC5vI6OTNJgXCU9/eiZpx1WQMg8VJBdDBUlRFEVxBlhCTYOiVeuWuPfiRfJcN8o9cz1eol37thg9crhcJ0fXLy28jyCR3377NanR91oa6CxpnQfJgpJCARllJJhZ5Sgd2/bvR/fuHpI5jhOzhoSHSua4BUuXSnc7zp000DTkJ0+Pk8gTRYbbc+JYJnNgHY5X4hxKPn6+WL9jO6InT0TA0ECZw2ifeZ5REyfg8LmzksiB8ylRiIaa69h/0ADZxw4jfqNDxkpyhxnz5shkscyCx8gSU3sze93MeXNFmtIS4VJBck5UkFwMFSRFURTFGWAJGzsazVs0w7WHDyVioNi49vARWrdplS0RJAv7uizpFSRpgBp69e4pIkPx45xDAUMCZb4j3jJL3brt2+Dd10skpaepyyQQPXp2l3mSunl0E1masyhRsuCdvvaDSBdFZ8iIYZiVuACd3N2w68gRmQCWqbspP5wANmH+fITHREtab+5j/c4dkvJ71aaN5px6iQQxokVpO3TmDGJnxstcSZwjienHN+7cKULm6LnZo4LknKgguRgqSIqiKIozwGIJEhvOjhoxrsrVBw+zXZDsYXkfQWJ3tT7efZC47HvcevoUV+8/wIBBA7F09WqJKi1asUKih0ON7IwaOwbt27fFuIhwkaHVmzfJnElb9uzF3uPHZV6kk1cu/ylIw4dizsKFGB48End+fo5JcbEiKss3rEeweV9RjjhZLCePZRTpwS+/yMS0sxbMF5miSAWbBu19s5wTwoaEhaJjx/YIjeTx/bFp9y4VpI8YFSQXQwVJURRFcQZYVJAc8zEIEqHMzJw/Dz08u8skrtETJ6C3V29ZNzgwAIHDhmBq/HT0G9APy9etQ7/+/bDAtGXYhY7Z4DiR69otW2S+Ik4My8QKjEQtWb0KPtIVbp5MDMtJYiPHx2DG3LnSlY/d5ihZPzx6hDFh4zBiVJBEiNjNjnMieXr2wGLTVqK8cRsK18IVyyWitHjlCnl80hxfu9h9vKgguRgqSIqiKIozwKKC5JiPRZAIozCUkTGh42QuJEZzKDSDA/zh6++H8OgobNy1yxYZWrtWxhLFzpwhY4I4Nmnf8eOSdY7SJPu7cUP2sWTVSmzZu1dkiUkY1m7bKpPHUqAYoeKcSxyvxLFGE2OnyrxKHJdE6ZmzaKFMGrty4wZJ9sCueox2MdI1KmQsEozU8VgqSB8vKkguhgqSoiiK4gywqCA55mMSJML6HGd25f4DERxOFjvI1wfzjViwexzlhNEhZpFjPUoOt6M0sSFLUbGOyXpMoMDH3BdvuYzZ6Chjsh+zjNLE+9yex+N+rS5zl81+uU/WufboUfJEtbxlPR6Xj9OCCpJz8lEJ0mSz37h16zBt/QbDekxdvdphvfQwcflyTFqxwuG6d8HjT9uwAbFr18p+5NzMYwrKhKVLHW6T2aggKYqiKM4AiwqSYz42QUoJG6Zb9+6VrHNsqDqq4yyoIDknH4UgsdE/xchIsNm3e++eaNyyOZq3bY0BQSPNuuWy3tF274LbxXCW6PnzMT6dQkOp6u0/GM3MefT088Xo6dPQrktntOrYAUOio2yS5GC7zEYFSVEURXEGWFSQHPOxC5IV8WEk6NTVjJmwNbtQQXJOnF+QKEdmfwOCglC8cAGULF4Ejc0f0wZNGqFRi6YiNozeUApi16yVaI69nFCsGHmi0HDd1DVrpD5FYvqmTXDr2QM1alWX/UxZtVqORaz6lnxxmbU91/FxvxEjkPvLz1C1WmWEz52Lhk2b4Kt//d0Ik4/tOHLuq984Lo/D8+N5cT/W8uTn+4GoICmKoijOAIsKkmM+dkH6mFBBck6cXpDY2B8TH48SRQuJHAWZ/U/fsFGkw4r88HgUlICIcPiHhSFszhxZRlkYOXkyQmbOQGTiAlk3bHxMslSNmDwJFSuWQ+mSxTBo9ChEJSZiVFycRIO4b/+wUEQvWiRd6cbOmAG/0HEIjIqUZTx++Lx5KFeuNKrVqCbn2ScwAPm++wp9Avxl/WQjQMFxsfAbF2KOO16eD89r9LRpCI6NRYTZnuccPm9uhkmSCpKiKIriDLBklSAxsxnHl7Bhz3Erjuq8DY5VOX/zVpoG7GcUKkjOgysJEj8Dl83zZeSPUUCJBN68ma4xW6zP/XA8WHq6V7Ku9Rm2RR4d10srTi9IjAr18vNF7i8/RcfuHjL+SNYZEbAiOezSVrlKRRQtmA9FCuRFpUrlZRklpW6DeqheszoaNm+C4kUKokDub+Hm2QPjZs1CzTq15HFhsw0lifLUyq0jSpcqjpq1a6Kk+UNA8eofFCTriyXtn/sMnztHJKqs+UBw/5OM4LCrHQXJy4gSx0h16+uNUiWKyn64Xdsu7hIxau/RVY5RrXpV2e+QmOgMGU9FVJAURVEUZ4AlKwSJDSpmQAsYGgj/QH+ZpJTLeEx282JDifcJG17WYw7WZ2PulGkEMtsZ98UGFefykQH/RrTYQEx5vIxABcl5cBVB4meDY8Y4f9Seo0fl/c8fHjhfFeecYh0ryQaTYlCCzpo6l+7clfezlXhj+uxZOHLunEwQfNA8R37GLtyyJcuw6lCeuA/un4/5meQ2URPGS+ZDTiLMz+6pq+//o4XzC9Ladeji1Rt5vvoc3Qf0f0MkKAO8rVmrBgrlzY2h5gUKmjoFxQrlR5WqlRBj3rDsjpfn6y/g3rsXIhMXolbdWiiY5zuJ4jBaVMJIU+UqlRBqhInn3doI0ref/hMt2rVBzOJFydGrihXLI8xIUf+RI5Dri0/RprM7IubNR7mypVIJUr/hwxAcO1Xkq3UnN3Oey6UrX95vvsRQI2Fdvb1kHw2aNjb7nCuyZz2nD0UFSVEURXEGWDJbkNjAWrF+Pbr38JB00EwDTTgJ6JT46Vi2bp2kkOb8PEw3vd80ADkpaWhkBMKiI+UxM601bdwQc02bgI2+8VMmIyQiDDsOHkx3NCqtqCA5D64iSJQWzkdVrlQJjBo3Vj6z/Hz1MO1bd/dOcn/jrp0YMy4EU6ZPw8krV+UzsuD7pRgbHop5ixfj0NkziJ40EevMe6hL184IHDZUfmRYvWUzRo4KwgzTzqZkbdq923w+p5nP7GoRM77f+PntY9rPOw8dNPs98ME/TnwcguTdB7m/+gweA/ohds2a5HWTV64SySmcPw/q1K8rEaM484eQSRwK5c0lssT7RQvmFyFK2LoN7bq4I/+3X2FIVJREhyg/VapWTu4217JDO+T/7msMnzgRs3fuxMBRwfjmk39IcogZW7ZIN7wK5cugarUqGBUba+6XfUOQuG3/EcMlgUP+XN9IhKlS5QoSKcr1xSdmf6NEkChLfiEhEmmyf74figqSoiiK4gywZLYgXTKNLc6rw0bZzadPjdDcxK1nz0SA2rZrjT3Hjpn1YzE2bBwmxcVieNBI7D5yBInLl4kEjTRtgPXbt8Ozlyc27dkt+xkePNI05GbLBKUUJuLo2B+CCpLz4EqCtG3/fnRyd4N3Py/sP3lCfnzoZdrHY8NCRZ68+nrLxLtDTTt4ovk8TUtIgHvnTpi/dInUY+THy7SBOUcVJ/KdOiMeG01bmxP2zlowH77mMzV/6VLETJ6Idu3aYIeRIQrSefM5XrVpkxExN6zZukXqcB4tzpVF0XF0vu/C6QWJXdL6mz9YjCA1Nxdr2rr1IgDsXsfudqOnGUHKl1u6vVmC1KRVC5sgTbEJUrFCBRBsRIpjl9qYi1vAiMvQmBjpZle8SAGRHRlrtMYmSIz8cMzQzK1bMTDYCNK//4HOfXr/KUgVyr5bkAb7SeSqlVsH+IaMlYx7vI1auBCdzB/afEbSfMeOzbCudRYqSIqiKIozwJLZgsRfozlBKaM+N588kcYWRYnRocjxMdKlp2u3zhjoMxCBw4aI9Kw2DTEKVA/P7ujbvy8OnzuH0IgI6S7kZRpyZMSoIGnwsYsQ9+no2B+CCpLz4EqCxOgrPyuM9DCKFDRmtEyqy65vcxcvFum5+/w5Nu3ahUF+Pphk2t6Up4e//iqfqUTTRvUfEojtBw4gcuJ4uY2bOQPDRg7Hz+Y8OfkvxYcTCkeafbK7Ho/N+aqGjhgmxw2NipAfNPi5ZgT3fX+gcHpBoghFLliAqlUri1T08h+cnJo70FxsRoFq1KohUSQmXRgzfbp0m+M4JNZr2KyJTZCMzNgL0pDoaNkHxwiVLVNKkjBQxixBokBN37gRo6ZNQ7HCBWSME+WIyRyYua5Vp462JA1v6WLH6FW+b79E/SYNMd58cLhvdtejvHTq2UOei8+YMSpIiqIoikvCktmCxHEK/NW6h6eHjCNidGjX4cMSVWJXoGsPH5kGW4A0thgpYoPNxzTsgs15jTNtDP6yzS54fft5Y9eRwxgVMhYjgoOMJGzFhp07MyV6RFSQnAdXEqSNRnw8PLrh+MWL5jPVA8PN+3P3saMSeeXnp3ef3iJRjLTyMzXZtKFHjArGradP5fEC004dMGgAtuzdI5ITa9rejELxc7bz8CHz+RqDSdPiRI74+eQPGPyM8f3GHy/YdW/15s0oV6o4QsLDZDygo3NNC04vSIQpsUdOmoTqNaqJCDHpQaniRVGrTi0ZwzM0JkqiOhx7VNRQvlxpBESESUSJXe8K5v7Olv1u4yYRoFyffwJ/c2HZXa9tl84iK9zncPOCMEkDxwexC95Usz2fS29jxFzPJA9MtsAEDqGzZ0kWOnbRq1y5oghSj0ED8e1n/5LudXHr1qOLVx9JTU7BoojVrFNTIlUde3THt5/+S7rbqSApiqIorghLViRp4K/Picu+xyBfH/j5+0kjbe6ihZiVuEAatzuNMA030kMxokyt2rxJGmNsgE2blSDb837UxAnYe+y4/HLOgeIckyRJHBwc80NRQXIeXEWQGCnddeQIwqMjccZIC8fnHTl/HntPHEdcQoIRjuvmOizGQJ9BEmFldPV7085m1Ief79mJiTL2aJJpm/LHBnaZG2TOiftk9zp226M08Tjcz6wFC5ISMZhj37iB7QcPYJj5PAQOH4qI8TGImTwJx4youWwXOwvuMypxoaTZHsA/ZGPGSETGWsckCz5jx0iEJ8S8UFxGWRg+YYKk5440LwzTbjOy42vqMfJEkaCwMNU2ZYWyxUgTu8IxumTNl2SNdeJx/cbZ9kVp47b+4eESjWI9RqF4DiEzZ5pjrZT9c388J+6fksZ9jjJ2zHqhc+Zk6BxIRAVJURRFcQZYskKQCAeQE/4KLmMazC3hQG82vihBfMwGE+vwsW2b27I9hYD1uK1VNzO61lmoIDkPriJI5LSRCnZb5X12b+NngBEeEZlrts8Z7/MzwnX8zDBFvpUOXD4/5jPF/UgWPFOP29tvJ+tMXevzaTv2leT6XM604pY8vS8fjSARa2LVuHXrJDpEEbDW8T6XMamD/XJGaLic4mDNmcTtGfHhY97KdmYZZcVaL+Ji1lv7sZazLs+D67hPPuY5WefAOhQx2dast00Uy+3WJV8XCpecA+sl7T+jUEFSFEVRnAGWrBIkZyMnC9K67dulgcqGrXJNunkxaYArCFJGwmvnaHlW8VEJkvJuVJAURVEUZ4AlowWJjR5GNy6bBnxaU3Bbv4I7Wpdd5GRB4hiT648fSyRBuY1bT59hkWl3uaogJUdh0xnRkQQL5vPqaF1WoILkYqggKYqiKM4AS0YKEhtcnHtl2bq1MoaBc6VIIyipEcZbihBvra52vH/o7FlJF2y/jg0naxvW475lnbnlY/tjSkPPbEtkn3br35ecKki5vv4CFSuUQ926tVC7dg3FUK9ubZnKhWPOn7mgIPH9fuDUSWzdty/pM3hFxEc+N/wsmfusZz1m17iDp06hj1dvbNu/D5eSumuyHvclnyl+Ps2tbfmb+8korOOpILkIKkiKoiiKM8CSUYLExs7xy5ckm5bvYD+ERIQjfs5sHL90SQZyU144Ez9FiA04RkH2Hj+GvceOYdjIETIvC7uNsS4nkWVdq7HH+V6Y+Y7HYIPu0Jkz0njjembF23Zgv6xjXWa849xKPJ6j80wrKQWJ3+PvgzSuDR8qSK9Mo/2nZ0+xKHE+Zpi2xYy4qbZbBfFJ12L590vwixEaXitH1zCtmBfJaQTp9DWOwbon2eyaNWuMYxcuiAhZn4Ute/fixJXLIiL8XDD9Nz+DHEfEyZsXr1phExV+fs1n9YARJ25DOGEzlx81++TEsccu2vbt6DzeBzmuCpLroIKkKIqiOAMsGSVI7FbHbFn9+veVgdzXHj2S20UrV8gcSFfu30fQ6GAkLJiPcUaefAb7YGLsFMxeuACNTduF87gcvXAegwP9ZZ6XwQGDJe0w53AZMmKYzIfEdUwJzvtHz5/HYvNdO2AQ508aijkLE7FoxXJ0cu+IeHMe7Hrl6DzTir0gvXr1Cr/99ut78bvhV8NO09j8EEEir03DXctfl4xobzmTIPFHAmaz8/HzRf+B/TE7cQF+MJ89fua8+3mjb7++GBMaIj8qcG4jZqDjjxgUKX6e+PkaHTJWPv/h0VGS3pspwnt79Ya7OWf+kDFk+DAMHTkcQUY+KF0UG0fnkl5UkFwMFSRFURTFGWDJKEFiN53ICTGIiIlJbgRynwu+X4rwmGgRJk4EGzszXlJ4cx6kjbt2SppiNtIYOWL64eHBI3HvxQtJ683lfv6DpcvewuXL4dG9G248eSIRp6WrV2OAEangsWMwdUa8WdcVYVGRIlBsIJ66+mERJP4q79HDAwGjR2HLsWNYu3//e7N6314s2roVDx7/CGM5Dl8LJefgTILEqGtswkz57DHyys/WlfsPJIo7wUjSmes/yP1t5n24efduzFm0EJ3c3bDWvB/52WJX2H4D+sn6geb8WOfu8xfy+WQEePrsBHTp1hlLVq9Chw7tsGDpkgzLoKiC5GKoICmKoijOAEuGRZBu38ashYkyoSvHK1BSGEGat3gRxoSNw43Hj+UX7VmJ86Urz3TT+OIYCM7TEjR6tCybMHWyNMyevH6NyPExZvkomRR2/Y7tIkiDjfzc/uknhBoRoiCxYcdfwdmQY/QoLCpKolM2QXJ8nmmF16Nd+7YIDhqBn3/5BY+MmL0vPz59gn2nT+H2g/sqSE7AhwoSX2OOg7LafiyZIUgyZs8IhmfPHujatbP8ONCgfh2RHf6IMHfRIvkM8jNhm+fIWyJLbdu2lvmQOF/Shp07RK78AgbLXGRXzPt+tvkcjwkLxYNffpUfNDp0aIuZ8+YhdkY8dhw8mDw26UNRQXIxVJAURVEUZ4AlI8cgnTS37IbDrj6chX9qfLz8qs2GWbA5TucunWy/ShtCI8OlHqNIbNhxgsqt+/fJMkaR+g/qbxpvOzE4wB9rt20VQeLksDefPpXo0ooNG5C4fJlp2PnLBLJrtm7BxNipRrDG4trDhw7PMT2wi12r1i0xNmkMEhvN741pMHP8hgqSc8DX7H0FiV0qT125jCu3btpeeyNKLJkhSIzaLtu4Ad09u2P70aPYf/YsxprP1SgDZWfW90tx9uZNhERHYeaihejawwOR5jPSx9sLa3fvlvNZZz6fG/buRbkyJRE7f56MI2xm3vcDB/tikhGi1eYz6D80EGGTJ2GKeXzKyFFGZb5TQXIxVJAURVEUZ4AlowSJcAA3f9VeaRpticu+l+QJXMYZ+NlNjoPEmbGO4xq4nsuZmpiJGpikgdvuO3Fc1jEpA7Nt7TS3HCTOsQ+c8Z/74+DxI+fPSaRqw44dWGi+d3ebBiIzczHxAxtejs4vPWRUFjvCBjbHV6kgOQeWIB08c0aERySHUaF3kVRvmZGKyEWLsGbfXtwwbXMWD/eO6O8zIGMjSOZ9fsJ8Pg6eO4t7ly7hNhOXXL6MU1u24MD587i6LylD3YEDuHbuHHYdPIidCxfisJGg6+azdNh81q6YepePHTUSNASnN27EuXv3sHfVSqxZvRrrzO31EydwjElVEmZiy/59uGaOc/biRZz8wCQoRAXJxVBBUhRFUZwBlowUJMJGD7vbXbrz5zxIzJh18fad5FTBvJWZ+M0t17MeuwJZ97mOdeSxuZWuREnbMTsXu/hYEkTB4rEoToTbsw7XfQgqSK6LJUi7jYjfMa/Zw8c/4v6Pj94Jx5g9MLfLjLRHGBEJN7BduP3kSXTv2UOSiWRE90+LE+bzcH3tWvw6eTJ+HDUKT8eOxU9TpuDn4cPxYsYMPBk6FM/Gj8eziAg8Gz0aL+Pj8WLECHM7A4+HDcPLiRPxLCYGF3v1xMWRI/DTkCH4OTYWz0NC8NukSXhhfOKp2ddzs6+XQUH4zax7YJafOX0aJ81nzdE5pQcVJBdDBUlRFEVxBlg+WJDS8UuyyI1pEH1ohrmsQAXJdeHr9euvv2DV3r2Yu3EjvjfCs3T79ndj6i0xt3GmDT5+6VJpE1KSosz9AWPGIMzIyNX7GfNDhMAfCcxn6poRmPPm2BfMuV6dPx9njNj9YGTm9IkTuDpvniw/b87r2qxZOG1k7Ye4OJw5cgRXFi/GRXOu5/bswS2uM+Lzw/TpOLt/Py6Zduxlc/5nDx3CD9Om4ZRZd23mTJzfuhUnk374+FBUkFwMFSRFURTFGWB5X0FiNIdd4NjIofSkZd4hNobYPW7Nls2yHbsIcbtzN2yRIaueLeL0p0SxDrsKcXtrWWajguTasLvcoXPncPXWTZGlFy9fvJOXv7yU2xW7diF0wQJELFqE2Rs24MyN6/Do6g6fwX4Z1sWOkVNGS/mZOG0+uycZXTXLTpjPCaM7J+7ds93ysVnO9WcePpIxRCfu3rWtM5+xk8SsS17GW9Yxy2U971v74jpT19H5vA8qSC6GCpKiKIriDLC8jyBRjDiR5NARwzBg0ADJgnX84kWZ64jd49jwYSpg7tOapZ9d6O4+f45la9eg34D+Zvs9mL90qczPwhTC1i/r3PekaXGSbYv7EJEygjRiVJAkZrhsGmvcL49ldavjMa1jE67ncu7PeszzSIvEWeRUQbLNhcSB/4ojeH0cXbf0wn0dPX8Bt+/fS97vuzD/yWu9cvduTDPv6SPmNX/+4rnZ3hqDNDBDBIlyxKQlFK6BvgMlQx27sPKzwx8arM8gP3Py3jeP+VlipsdjFy6KWF2+a/scWT9EsC4/W/wccV+8ZR2u448h1mfuzA/X5QcM3re6vNqfW3pQQXIxVJAURVEUZ4AlvYJE8Th09gx69eklaX8PnDopsrP7yBHMTkwUsTl45jQSly2VeY84Mez5WzfxvREjzlnECWADhg7B6s2bMHm6TYSaNG6IlewGZBp4l+7ekfWVypeRxAvXHz82+1qGyhXKGblai/0nT2JUyFiZI2nfiRPYceigZMZjenA2FGNnzhCZYkIHNuTi58ySiS6ZXjw9EaicKki/vHyBn549Vd4Cr4+j65ZeKEWco+umaVubRpzDOo5gUgduwzFM3Ae3ZcmoLHYUmVUbN6CbR1f5wYAJTnYcPCCfH6bu5uczfvZsidQuWb0aI0cFIy5hhiQ+4edsUlys7GdK/DQZE7Vo5XIZ07fUCB0/i0wJTpEaFTJGPt/8YYE/hnA/YdGROHj6tMyhxDnH+Jn+kO6yKkguhgqSoiiK4gywpFeQLty6jcXmO867rxeuPXwkDTL+8rzz0CG0btVS5l5Zt30bevbyxFLTFhnk5yMC03/QAGmkjQkdJ2m9+Qs4o0+LV5l99feWxigbS/ylO3jMaLh37oSYyRNFmoaNHI6BPgOxfP16iVpFm+UTpk4RUZoxdw48khqLzZs3keUhEWES1eIktUwbvmrTJnO+3ubx92me5DInChIb3POM8BUvXAAVy5ZCJSUZXg9el1jz3uB1cnT90sP7ChLha2y/DUtGCRKjQWPGjRNZufXsmXz+fjD7jDFyEzdzpghLD8/u5nO1Ap06dZS5xfh5ZMp8pttn2v3J06dJ+vwV5vPUp28fkaveXr1N3akiPq1bt8SSpM+lTCgb6C/bRMREG4EKQ5D5fLI+M1Jakdr3QQXJxVBBUhRFUZwBlvQL0i0sX7cOfbz74Mq9+yIw7G7DCST79u8n0aL5RkwaN2og8xV5GZHiHEf+gQG49/KlzGnExplNdoabBttujA4Nwa2nT2X/7N4zPGgk4hJmYmx4qESdYiZPwsS4WIkkubu7wcdIl5//YIwy66aZery9//IXkSBOkrl++3ZET5ooAjV1RjyevoY8ZtSJ55ryOTkiZwqSeR4RoahYvqyI5dzFi5Qklq5ZjZo1q2HE0AC5To6uX3r4EEFKCUtGClJ4VJRMvkxB4ueP++TnI2H+fPkc8zPHyZXnLEw0nxM/mViZKfYZZWWXOE4Ky88SY1ycUJbb+g72k6jTyk0bMcjXR7LtRU0Yj9mJC9C5cyeJBnO7ceYzzYgsJ5OVjHzaxU5JKypIiqIoijPAkl5BYqOGjaIBgwaahleE/CLNOYzWbNkCz16eRgQuyK/VnN1/8coVIkQbd+1CH6/e0o1nRHAQBvkMMvdXG9HxxZZ9e9Hd00MacJLi+85dWZ4wf55EhVq1ai5d6fjrNSNAlCf+er5682azzVGJGAWYxhsnkPXw6CbzIvEXcf4Szi53A82xKGH9jLwxuuXcESQgKnwcmjdvKuO5KHuKDQpyJyPPw4f4y3VydP3SQ04VJArRVvOZ8ejeDbOMvKzfvg3rtm+XrqXsMrd8/To0a9rYiM4GbDKfOyZE6dLVXSJCjNiu3rQJ46dOlrr8rFCm2HW1d59e2L5/v4h3b68+0rWOPygsWrFCuryy+x0jsQdOnpIfJ6bGT0/z34y34ZSCxEZ+7Jo1mGrgfUd1iK3eWkwxf+h4n/VjzYW2mLLKttzRtsTanttN+It6aYViwuNOXf3X552Z8LgqSIqiKEpOh+V9kjRQZKxfpAcH+kuEh5PCxibMwJFz56Sbz/ylS2RdxPhoaWiyWx676oRGRog4bdmzR7rH8RdtdoljxIiNPw78njlvnkw2y+58TOLAcRf8xZvbcAwSu+Cxq93arZtFhvhrNrv5TZ4Whz1Hj2L7wYNIXL5MkjJMmT4NvqZBN23WzOSseY6eU0pycgSpSZNGIgWOzttVufbwIdp3aPfRR5AIo7j8gWDI8KFGXgJFlDg2KCQ8VJhi5IURXY4zYtSHMkMZYVdXfv74mYqZMkl+iGD0jVkkJ5n2Kj9bHE/Irnr8jPMHCU7UzHF+I0cFSVfXzbt3Y+6ihfK54+fS0fmlFacTJDbwxy9ZgqEx0Rg+cYLkcnckG7LMrGO9YRPGI3LBAgyfMAEB5uIPNtbpHx6GUXFxmGTsc9Ly5Q63j+FxoqMxYtLEtx4nrUw0xwiOjZVj87xjFi9O//7MOVBu4tate+9z4XYqSIqiKEpOh+V9BIlwYDelhLBbHBs69pnirKxYjNhwGWVH6t+9Kw08jl2QaI5Zx+VcRlkiFCyKknUc3lKeuI015okZts5evyH1eCxuZ2Xv4rmwPo/LiJT9eVjn/y5UkJwLVxIkwve3fA4MvM/3Pe/z/S6fA/MZsD6DXMb3Pj8DhHVZRz4XSZLDx/wBwfpc8vPEzyT3I1nveCzzmbP2+6EZ7IjTCdLU1asxJCoS+XN9jcL584j0cFmqemvWYHBoKHJ/+SmatGiOscY4SxUvigK5v0HJ4kVQtFB+FC9SEB27e4gIUWDe2H71GgREhCPft1+iSMG8GDl54hvHsQnKMrm1sN/+jeUGRrH6BAYg79dfolyZUhg3a1ZyZCvlNg73YR6zPoWvXRd3hM2ZK6Jj1U0r3JcKkqIoipLTYXlfQfrYUUFyLlxNkD4GnE6Q2OWtfbcuyPP1F0Y2voB7757S3e6NekYCeIymrVsi91efiShFzJsrGURq16uNqIULjaAkoE6Dusj1+SfwGTPa1o3Obh983KZzJ9txvvkSXb37vFHHEg3C+4xETV6x0hZpMrLFx5bc8FwmG6LNcatVr2YEqSTGJSTIthK9MnVkn3aSxm24TvbN/Rni1q9H604dUSDXNxgzfZpDMXwX1nmrICmKoig5GRYVJMeoIDkXrixIjP7w88v3BFPbO6rDyBCFxNG67MKpBInSET5vPipWLI/y5ctKBKhKtcpGeBJlnVWPkZagKVNQKF9uVK9Z3YjHMhES1q/fqIGIztzdu+Hp64PP//af6D6gv4wNskSFAhE2Z445RhlUqFBOxIpiE71okUhJSMJM1GvcEL39B6NtF3eUKV0CDZs2xqi4WMStWy9RrfpNGqJc2ZLmXMuhU09P6RZIqteqIec/bPx41KhTE83bthGpmmKO6Wbq8flwP/1GDEMNU7dMqeKoWbsm/EJC0K5rFxQtmE8iZzyngaOCEbtuXfLzTgsqSIqiKIozwKKC5BgVJOfCFQWJ3ebYzY2JGZikgWOMOGaIXU8pH9IV7sYNkSOOO+LzYZdVPmaiFcoJ73M/7DLHdXLf3LJLrNW9lXWsbnUpz+FDcCpBosQMGjMGub/8zMhEd4mmMIrkGzLWJjh29Tp098B3n/1bJCZ+82aMjY9HiaKFRDrGTJ+OEZMnoXqNaiiY5zsZo2QfjYlbuw4DgoOR64tP0blPL7Q0b2pGkThuafqmTbKv0iWLo0iBvOjg0Q1dvHqb8/gcjc0fcemaFxkh27F++25dkeerz9EnYLBEgShsFC8KW92G9WzRoPjpsq6ikTEyIGgkCuT5VtbzuXXt6y1RsAHBQSJMlKOufb1E1Cg71nmnBRUkRVEUxRlgUUFyjAqSc+GKgmSJTwfzvJnlkansmT1y77Gjsp6JFHYdOSz3R44OlkQMvM+EDhxvxG15//ilS5J0hYlWTly+jAOnTknGOiZt4Dikw+fOStIUJmhIzzi+d+E0gmRr2K+QbnMFcn+L0UYqAiIi8N3nnxiBaS/7tBr/ocZSGdUpU6akRIIoPJSaMkZqShYvjApGUCgmlI1Bo0e9EX3iPvi4ccvmIk8hRmT8QkPwrZGtNu5umLZ+PUJmzjTblkAlc9Gs+pUrV0C5sqURPn+enAuFpvugAWhm/oDl+/YrEaVJy1eIIHEMUsyiRUbe/ET2GC0KnT0bhfPlEekLMGJFqapWvao59jhJ6DBt/QaJNFWtXkVEL8Ich8kauMz+Or0LFSRFURTFGWBRQXKMCpJz4aqCRJnx7OkptxSdLl07yzxgnJA5yMjCcPP+5YTJXB4wJADrtm2TddcePZIU+cxAyQmc27dvK5kn55i2c/ce3WXeskHmfHcfOSITOzNrJFN9n7h8KcMkyWkEiY16Sk7JYkVQrHABeJmL4zGgPwrnzy2yQhFinVgjQz19fUSc3Dx7yPgkHo/bFi9SCHUb1pfsdRSaUiWKImzunDeiRxwrNHpaHIobCaGIeA8dgm79+qJQ3lwiNlHmxRk3e5ZEkGrXryvCwa531apVQYUKZSVbXmevPtK9r0qVSrYokRE6JoOwF6TI+fPlPArly4UW5oWnqOX/7mv0Guwn5+PpM8gIWHnZT/lyZeAzdqyIUuUqFeW8xs6I/wDRVEFSFEVRcjYsKkiOUUFyLlw2gnT2LLqK/ASihfkcM+X95j270bJFUyQsmI8+3r1loti4mTNk+da9eyVN/vXHj0WQGHWaMn26zHX08NdfMS4yQuYa4yS0FKyFpk1rTcq8bttWIzXXHZ7L++A0gsRoCbvLMRrD6JCMDzJQcvLn+kYyxE3fuFESITDKwu5vwbHmWEY2/hSkgiJIjAJRsJiggWOI7JMvMNpEwcr77Ze24xg5qVC+bPJx2M0twkgQBalW3dqyDQWpatXKRroqYlRsrNmmNKoaYZq2YaN0n6P4sCuevSBZQscufxyn1LRtKyNhuTFi0iSJSNlkb60Rp2CJMvG8GXXiGCUKYtic2ZK0QSNIiqIoyscIiwqSY1SQnAtXjiD18OyOo+Zcx4aNw6Rpcdh58KARpGYytxjnSOJkzpz0lZM5c34kX38/mVh5VMhYhMdEy7xJnNPs3osXIkicZPnmk6cYFxGO5cYNjpw/h3lLFqObR1es2bpF0oo7Op/04hSCxPE5jJ5QOnJ98QmGREeK1JBBo0fjq3/+TUSDjzlmJ89Xn0nXNjmOEQLectwRU3xXr1ktaX+LpIscs9z5mQtPkaKYMMMdRYdSwkQKHFPE/VKMvvzHf0tyhjFGtooVyo8qRop4fhSk8mVLizRxbFG9RvWle14L82GoVaemEaRvpHseBYkJGooXLij1KHRd+/WVVOJMvMD9MeX4kOgoScxAeWvSqoWMf2I0jJLYrE1ruQa16tSS+ZR43imv11+hgqQoiqI4AyyhpkFBEeCvx9cePsoBPEzC0bqs4+Gvv6F9x/YYPXK4XCdH1y+tqCBlPq4sSL29+tjGE5n7vbx6y1ghdocbMmyoEaAo7D1+DJPiYuHV10sEyS/AX7rQ9TXt4+mzZyF25kwRqDs//4yICeNFmq4/+hGR42NkgucJsVMkgtR/YH9sP7A/w5I1OIcgGXFhxKV5uzboaEyUQsJGPrvDRcyfL+m4OXYnMjHRCEVLEQpOyGql/56ctH1L88eECQ8YdWF0xj88VLLNeQ0JSI7ahM6aJRLSqWcPkTIu4/lybFHrTm4iLaPi4tCua2fpSsf9sx4FhuOMKDjsotfKrQMaNmuCgUas2EWPXfUmLlsO91490a5LZ4TPmyfnEGrOi0L17af/QtvO7iJBjA65mePXa9QADZo2lu52fM6UIUakOvbwkOiVv3mO9tGvtKCCpCiKojgDLKFjR6NkyWKYPH0aoiZOyFYiDRwTwW4/vO+oTlbB61GmdEkVJCfBFQWJMIvd/hMnJLkCs87tPX4ch8+dk3FCHG+0fsd2GZt00qzfuGuneR9ewBGzfu3WrbYEDRcvSX0KFoWFXfZ4n0kcDpv7xy5exM5Dh5KTNjDDnaPzeB+cposdG/aUB44x4v2Uy2ds3iKTqFKOataphQlGgig9KeslC4VZz/NgdzuKVsp6lJc3jsN5iKzl5j7Pw37+JS4nvE8BYV1CqeFy6znb6pnnYPZBUfM11stseuw2N2LiRKlv2/9as/16gfet+pQ97lfOO2neJesc0gKfkwqSoiiKktN5/fo1FiXOR82qlVCvZjXUr1U926jH29o1UMfQoHZNh3WyEl4PXpcFc2fLdXJ0/dLKxyZIbHxbKaEdrX8brM8GsaN1H4qrChKxlxbe53Um7ArHeZHksZERPuZ9Rp54n7ciKQbep2zx9ZHXKOm+1Df7ZDY7K+13RuE0gvRXsNHPfbr16I6CeXOh77ChqSePzWFQeBgV4tgidqdjavCMvi6OUEFSFEVRnIXXpvHHxmDOANh05DAumUadFCMmqetkLbw+jq5benAmQbp8755kOKNwXLx922EdNpqZFprRCN53VMcRJy9fluiFo3UfiisLkrPyUQiSRfi8uQifO9f22C76k5OJSkyUKFB6xxK9LypIiqIoirPA7ydKQHbDcufhA0QvWYLvd+40y16JTDiqm5VkxPe3UwhSUpRhnrn+HKTPeXU49w0bsYxKXLl3X6IITOYx39TxHewn418u3bkj2zO6wHqsz3oULUYpJCphlv1gxIApo5kRjV26uCzVOXwAKkjOx0clSEy+wMa/fde4nA7PmThalxmoICmKoihK2nn1hy2StW7/foQnJspY4yu3bFEkR/WdDWcQJMoRZcajuweiJ06UrGVdu3XBpl27JOozc/48bDTiyrqcU4cZ0PicOD7FiijtPHxY6m7eswdzFy/Cln17RZJYb/GqlZgaH48+3n2MeKggKR+ZICnvRgVJURRFUdIOG6M3793DRPMdSjmKWLQIS01jnOL0MXx/OosgcaB/vwH9sWjFCuwystOvfz8sXb0aw0aOkGxonHR04fJlcHd3w4jgIJmQlHPmMHI0MS5W0kIvWLoE7du3wehxY+Hdz1sG9oeEh0nkiPuhdB27eEEFSVFBcjVUkBRFURQlbbzirfmOXLlnD0LmzzeCtBRRixcjfOFCnP/hmvkG/bAECTkBZxEk3np5e2FwoD+aNW2MhPnzsHn3HjQ1x5syfRq6dHGX26Axo2VOHXaxoyBduHUbU2fOkPTQM+fOxdARw2Wi0TGh4zBz3lxJD80o074TJ9DXSJN2sXP8HFwNFSQXQwVJURRFUdIG5eHlyxc4xvTDpkG6YtcubD96FAfPnMHV27fM9+cfNolyYt5XkFiXWG0IlsyOIHFuHM6Vk5C4QOa+YXe5tu1aY86ihVi8coWkkR4waKB0mTtw+rTcZyroINMwDQkPxQwjRCNGBctYJUaU2FWvnxGknYeZKnqjdM/j66yCpKgguRgqSIqiKIqSPkQGTOH4lHuPHsl9jktyVNfZeB9BYrvh0s0bkriCjXUbmS9IQ4YPl3FHZ67/IIkYVmzYgNiZ8fDx88HYsHEiSCNHj8KydWtx8c4dmWCUUSGunzZrFuYvXYKw6ChJ0sD5rDbt3o2EBfPRq08v+A8JxODAAJFhFSRFBcnFUEFSFEVRlPTDcvDsGdwyjf+0ioQzYAnSvUcP5TmKDL4LUzYdOihZeLccOYz7j3+UZeMjw9C4ccMMFySLE5xUNCnz3InLl2SS0bPXb0gSBnaR4zqKlFWH23Adl/H+SXNr3ZfbK7YMd5zMlBOPsqsdt7WOl1FQkNq1b4uRSYJkLuIHAhy/eFEFKRNRQXIxVJAURVEUJf2wfKyCdOjcWZwxjcKHTx7j/qNH7+SRqbd2/z4ZixWeuBBTTbti/4ULGBsaglatWkiExlGj80MR6Uma24j3KTREJhU12C/n/eR1dnWt8UwO6ySty2iuPXgI986dEDAkALeMLF27c/uDuG6u7+bDh1WQMhG+H1SQXAgVJEVRFEVJPywfpSCZBvaVW7ew//QpSVBw2MjSu+AkrAu3bpV5oWKWLkXoggWIXbsWA4NGoku3Lrh0567DRmd6seSFWELzLtJaLyuhIHF8k58RpMt370ok7MO4KLc/Pf/5g9twLCpIqVFBcjFUkBRFURQl/bB8jIJE0tsO4PPfdPiQZPZjN7uVe3bj3tMniI4IQ9OmjTOki92ZH65Lim6OK+IcRky28Db5+SspcrTOWma7/XM9H79R38G270OqLnZGSj8Y8xpkRPuNRQUpNSpILoYKkqIoiqKkH5aPVZAIs/GlFT7/rUePYOmOHfjhzm2wmx5LTAYlaaCkcCxQaFQE+g3oh0Gm8c7JXa/cuy/RJK6jPPH++Zs3ZRveP3j6NCZPi8OhM2dwziy31nFCWHaf42PWY+OXSRx4HC7jOtaXRrGB45IIt7M/r/clo5M0ZCQsKkipUUFyMVSQFEVRFCX9sHzMgpRenjx7it/NrbkYyQ3AjMpiR3mJS5gpcsRkChQZJmVYtHIF5n+/NDkLHbPYcRJY38G+mDojXjLS1alVXbZlAofRIWPRf0B/RE2cIPuZNisBY0JD4Ofvh/FTJsM/MAAjgkeKcK3ctFGy3QUOG4Ite/fKpLODhwRICvELHyhKKkjOhwqSi6GCpCiKoijph0UF6U9M40EiR8mPTckoQaIAccLXWCM91x48EEH64dEjTImfLkLE+0zzPdU87tKtM6bPnoXdR45g19HDCBg6ROSIAsSJYtk1j+IzOzER/QcNQPyc2Zg5fy7atWsjmet8/HyxZPUq9O3f1+x/GmImTxIxCokIh68RKTaUPzR5gwqS86GC5GKoICmKoihK+mFRQXo7LBkpSGFRkQgJD8PNJ09w+e49/GAa7xQmdqG7/dNPGOQzCEuN2KzbvlWiQMNHjsDGXTtFrJgIYcSoIBGnJ69fy74ixseYekFYu22rzJPEKNLdFy8QbpYnmvaRW6eOGBzoj2CzPaNRrM9byo2jc0wPKkjOhwqSi6GCpCiKoijph0UF6e2wZJQgnbtxE1v370PvPr0QOWG8TPK6ZNUK6WLHZdPN4w7t22H2wkQsWrEcCQvmoXsPD6zavAm9vXpjwfdLsHjVSnj385aIkXdfb6zZsgUDjVStWL9O9uPl3Qe3nj3D6HEhWLR8hRGlaOl+l7jse+w8fEiWR06cgKsPHjg8x/SgguR8qCC5GCpIiqIoipJ+WFSQ3g5LRgkSYYKEHQcPImbKZERNHI/Vmzbh9NVrmLNwISZPn4bVmzdj56FDMkYoIiYaKzdulG0oPzPmzpH7i8398OgoU3eTJGNg5GjfiePYc/Qolq1diwu3b2Pdtm2SKY9psxkxijZStHXfXmzYuRObdu+SZBCOzi89qCA5HypILoYKkqIoiqKkHxYVpLfDkpGCRJhZjhEcCoZklLt2Tbrfcf8Xjdww09ylu3dl/cXbd2QbPrYmquV8TFxHEeJjJn9go5eZ7HifyRmYgIGPOc7oyv0HuGrqU4p4PEoV61jn876oIDkfKkguhgqSoiiKoqQfFhWkt8OS0YL0saCC5HyoILkYKkiKoiiKkn5YVJDeDosKkmNUkJwPFSQXQwVJURRFUdIPiwrS22FRQXKMCpLzoYLkYqggKYqiKEr6YVFBejssKkiOUUFyPlSQXAwVJEVRFEVJPywqSG+HRQXJMSpIzocKkouhgqQoiqIo6YdFBentsKggOUYFyflQQXIxVJAURVEUJf2wqCC9HRYVJMeoIDkfKkguhgqSoiiKoqQfFhWkt8OiguQYFSTnQwXJxVBBUhRFUZT0w6KC9HZYVJAco4LkfKgguRgqSIqiKIqSflhUkN4OiwqSY1SQnA8VJBdDBUlRFEVR0g+LCtLbYVFBcowKkvOhguRiqCApiqIoSvphUUF6OywiSE0bixBIA1MRKB4dOrZXQXIi5LVTQXIdVJAURVEUJf2wqCC9HZZkQXr0SBqXio3rjx+rIDkZKkguhgqSoiiKoqQfFhWkt8MyPjoS//rb/0G1KpWkYanYqFa1Ej75x38jeMQwuU6Orl92waKClBoVJBdDBUlRFEVR0g+LCtLbefXHH7h04TyWmsbk0kWJ0qhUbPB6LF20EGdPn5Lr5Oj6ZRcsKkipUUFyMVSQFEVRFCX9sKgg/TVa3l0cXbfshEUFKTUqSC6GCpKiKIqipB8WFSTlY4NFBSk1KkguhgqSoiiKoqQfFhUk5WODRQUpNSpILoYKkqIoiqKkHxYVJOVjg0UFKTUqSC6GCpKiKIqipB8WFSTlY4NFBSk1KkguhgqSoiiKoqQfFhUk5WODRQUpNdkjSKtXm8b6MiUbmLh8OSYbQbUXpNev/pAXT1EURVEUx7BQkG4/eMBvTod1FMXZYFFBSo29IC1bskiuk6PrlxbYzmZ5qyA1bdIQo+LjMW3DBokiKVnPVCOncevWo7lbR8xLmCGvjRYtWrRo0aLl3eXoxQt48PRp0iMtWj6O4tmtM/r7DFRBssMSpMoVy2PVimVJV+rDSkRoCCbERMr9ZEG6f/cOqlepiLqNG6JFh3Zo3q6Nkk3w+leoWA5tmjdFwGBfDDYfCkVRFEVR3o5P/74YHR2FYSNHwG9gf4d1FMXZCDTtwHIli2HI8KEqSHZYglS3dk20Nu3lQH8/h9cvrQT4+aBuzeqpI0gUpNo1qqGdR1f09B2E7gMHKNlAD4OnzyBUr1UDXj27Y97sBCTET8PM+DhFURRFUd5CwvRYxM6bi/iEGea+4zqK4mzMmzMbtatVhv+QQBUkOyxBqlWzGvp79Zbr5Oj6pQW2s+fOmokObVsjPDREvOiNLnbNmjbC2IQEzNi8BXHr1inZwLT16xG/aTNadHJD4pxZ8tpo0aJFixYtWt5dTly9gifPnyc90qLl4yi9unfVLnYpsO9it27NqqQr9WElOiIsdRc7zWKXM9AsdoqiKIqSflg0i53yscGiSRpSY5+kQdN8uwAqSIqiKIqSflhUkJSPDRYVpNSoILkYKkiKoiiKkn5YVJCUjw0WFaTUqCC5GBktSM5UHJ2/oiiKoqQFFgrS3YcP5T4l6WOAc7Q4er6Ka8CigpQaFSQXIyMF6bX5w7pwwTx07dQR3r175lh6du+G4UP88cvLF3LOjp6LoiiKovwVLPvPnBau3r6FSzdvOD0Xb1zHoyePtSeJC8OigpQaFSQXIyMFiWVowGD85//8H/j6809yLJ/8/b9QoUwJvHzBzEOvHT4XRVEURfkrXr36A/cfPcKJS5dw+uoVp+fstavYe+ok9p0+LZEkR89Z+fhhUUFKjQqSi5HRgjQ6aAS+/OSfKFIgb44l73dfo06NqipIiqIoygdhvjDlu4/fJc4P8OOTxzh49qx5qILkqrCoIKVGBcnFUEFSQVIURVEUyt69Rw9VkFwcFhWk1KgguRgqSCpIiqIoiqKCpBAWFaTUqCC5GCpIKkiKoiiKooKkEBYVpNSoILkY2S1IhfPnQf7c3yJfrm9QIM93DuuQogXzIc+3Xwm876hOWlFBUhRFUZQ3UUFSCIsKUmpUkFyM7BQkyhHFqEaVimjSoB7KlSouj611xLqf6+vP0derF/r26SWCUyhfbsGqZ9233//bUEFSFEVRlDdRQVIIiwpSalSQXIzsFKTc33yJkcOGYMO6tYifFoft27agQ5tWspxRpRJFChrxySWRpTxm2exZM5AQPx2f/evvEkUqWbSQ1KMcsQ7rOzpOSlSQFEVRFOVNVJAUwqKClBoVJBcjuwSJktK0YX3s37sHdWtWw6f//BsC/HywdvUqWb5+zWpMnTxRokoL5s3FosT5OHXiBELHjkaDOjWx/PslWLp4Efp59YJbuzbYvXM7Ro0cLl3w3hVJUkFSFEVRlDdRQVIIiwpSalSQXIzsEqRvv/xM5GbTxvXI9fUX+O6rz9Ggbi1s27oZ3r174tiRwyhZrBCGBQ7GujWrJEJESYqOCMOCubMxKyEevT27Y8f2rZgQE4UtmzbIfgvmzZXqWClRQVIURVGUN1FBUgiLClJqVJBcjOwSJEpRV3c37N+/Vx7/47/+Ax3btcGObVvRp2d3LFu6xCz735g0IRoz46fjf/z//m9MnjgeE6IjsWrFMsNyjBg2BCOGBmLKpPGmXgw+//c/0pTAQQVJURRFUd5EBUkhLCpIqVFBcjGyS5CsJAsL5s7BkkULETjYF3t27cCgAX3h3rEdtm7eiK8//zfat26B/fv2yJvo/LmziAwbB98B/USQ+nn3RqcObTEmeCTmzZmFLz/9l8NjpUQFSVEURVHeRAVJISwqSKlRQXIxsjNJQ4Hc36J0scLS1W5owGARI2axq1y+DNoZMaJAMQkDI0tD/H3Rzd1NxKZgnu/g6dFVtmnTspksa2beS6zr6DgpUUFSFEVRlDdRQVIIiwpSalSQXIzsFKQiBfPJmCGOR/r680+k2x2Xc1nub75I7i7H5VzPcUoUKCZh+O4r2zZ5v/3KiNE36Zof6a8Eic/9ld1jRVEURXEFVJAUwqKClBoVJBcjWwUpg6H4pGUuJEeCZHuzvsZrc/vbr7+kem6KoiiK8jGjgqQQFhWk1KgguRjZIUhpScVtRZa++eJTueXjt0WIuK+iBfOjTs1qMjdS+tJ8sxgxevU7rt6+hXX79+Puw4fm8R8On6OiKM7Ha/mUJ32Zmc82C29T1lMUV0YFSSEsKkipUUFyMbJSkCgulBO39m0kbTfHGLHb3Fef/Vsmh7XqcV3p4kXkjRNvzomZ66pXriBJGFg3l9mG9Th5LB+TMiWKYfvWzahSsRw++cd/yz7eJlSWIP3+y0s55x/u3MHKPXsQvXgxJppr8vDJY1muRYsWZylvH0v4+tUrPDqwC4/27RBJ+v3lc9xZuQi//PjAtqkpIk9JX1gsyTL1Fth41PLxF1frbq2CpBAWFaTUqCC5GFklSJQjSkvfPr1w/NhRePXqIeOJPLt1wdjRwWjfppURl69QOF8eSbYwa2Y8Vi1fhratWqBPzx4yOWyvHt0wZlQQurp3lLqtWjRF0PChGNjf2whSUZksNiYyHP5+g1CpXOm3zolEQapfuwZ+uH0Ly3fvRpQRo/BFixC9ZAkmL1+OXSdP4MTlSzh+8aKiKDmcI+fP4/LNm3j1logQZefZuVM47dsTvz5+hPub1+JS+Ej88duv+HH/LtxaPBs/Xbkg2z/csQm3v59n6p986/64/Nb9ezh8/pzD81Gcn6MXLuDMtav49ZeX7/196IyoICmERQUpNSpILkZWChKFyKuXJ/bt3YPmTRrKfEfbtmzCEH8/7Ni2Ba2aN5GEDKWKFTZ1dosUffXZv6SLXblSxREw2Ae9PD0kUtTNfHgPH9yPyPBQEaiyJYvi5PFjiJ08Ecu/N6IzcbxEp1KeBxFBqlUd9x8+wDazzdSVKxCWmIhII0pTVqzAkQvnccXI06WbNxRFyeFcMF9Ytx7cf/vfraQvortrluLCaH9cGBOAl/fv4vHRA+a+Px5s34DLUaNwY950nPHrhftb1uHJicNmu7cIktnfg8c/muP+4PB8FOfmsuHKrZtYu3+/rTfBW0T5Y4TPVQVJYVFBSo0KkouRlV3s8uX6GvVq1cC8ubNFer5fshiD+vfF//t//18yv9H0uKky5ojd63bt2IFa1SobYfpcut+xuxzTeoeHhuDsmVPw7t3TvLGCscbIzbBAf1QqVwZbNm1AhTIlJcI0d3YCcidlxUuJ1cXut6Qudo+fPcWuEydEjsYvXYr7Pz6S5baONoqi5Hje0Zh7lbT+ZF933Foyx2wDXIuNxmkjRDcXzMTZQC/c27gKV8aPw9XJ4Xh66hhevXr7PtmQtBUH56J8BAAHjCRQhFWQFFeDRQUpNSpILkaWCpIRk0b162Drlk0oXaIoosJDMXdWAsqa+6tWLsNg34ES9SmY9zusWP494qZMQrlSJVC/NrvXeeD82TPSze7cmdMiVjWrVkLrFk1x9PAh+JsPMgWJyzw9umDenNnIZTeuyR5LkKwsdvwiYHn09An2nDyJB0aQNEmDonxEmL9pbPZeChuOBzs2yuf99oqFOBfki2enj+Pp6WN4fv0qXt6+gdvfz8e5Yf3xymzB7RzuT/lo4bgjisK+06dVkBzUUT5+WFSQUqOC5GJkpSAxKQO72sXFTjZviEiZEHaGOSYjSTFREWZd7uTJYRk9Spw/FwsTF2D+3Nno7GbOb8Z0EarZCTPg3rG9dK+bnTAT02KniBhNnTRB9tm2ZTMEjxwuIuToPFIKUvL5iyi9fbC3oihOivmbxijSrYWz8PjYQbx+/Rq/mc//9TlxuBQRhDvLE6XL3dUp4bgcPVq63VlRJ8W1UEFSQXJ1WLq5d8TgIQF4/McfuPbwoWKgLF5//BjVqlTC0kWJcp0cXb+0oILkBGSlIBEKEAWFXeaYRIFRJS7nMq6z6lGSLMHhciZ4sCaJZZpwbmvV53L79ZZkWftKydsESVGUjxv+BGJ1neMto0qyjgJldakz95OXKy6HCpIKkqvD0sWtAwrmywM3dze0bd9GMbRr3xbtOrSVTMlLF2kE6aMnqwWJUGKI/X3rsaN61rq0PLbf1rqfEhUkRXFVUvxt4986C/vH9nUUl0IFSQXJ1eHUCKtWLMPIoYFC0LAhih1s5549c1quk6PrlxZUkJyA7BCk7EYFSVEURXGECpIKkmJrz2n56+LouqUVFSQnQAVJBUlRFEWxoYKkgqQomY0KkhOggqSCpCiKothQQVJBUpTMRgXJCchoQRo+JAD//K//eCPhQk6CY5M4B1OVCmVVkBRFUZQ3UEFSQVKUzCZDBWnS8uWYtGKFMNHcd1THgo1+q+4Ec99RnfTA48lxHewred07zimnkrGC9Brz5sxCxXKlJErDSV+ZTS67ZYlSxLmVcn39Bb4151S8cAGZR+n3337Fa/0SUBRFUZJQQVJBUpTMJkMEieIxdfVqxCxejIj58xGVmGhb/jbxMcujFy2UupGm7vilSxzXSwfRixYhcsEC2zHtjsvH45culXWsY7+Ns5CRgkQoSQ8e3MOypYvRz6s3KpUrLbL07Zc2WXIkMJkFxYwTz3735WciRW7t22J67BScPHFczlUng1UURVHsUUFSQVKUzOaDBckmJN+jT6A/qlatjGKmkVu6VHE0bNYEY2fEY7KD7bivgIhwlCtbGmVLl8DQ8TEiWCnrpQXKGc+hVcf2EoXwGhKIqWvW2NaJWKxCu66dzbrc6Niju4iGnHOK/eRkMlqQrBfdVl7j+g/XsHhhInp7dkd583pQVigtnLPIkdR8KJwfKfc3X8pxCuXLhXatW8iEsqdPnsCvv/ySdF78269ypCiKoryJCpIKkqJkNh8sSLFr14qU5DEN6gZNGhnxicDAUUHo0N0DwbFmOyM+FJZp69cbNkj9yStWSFSnUfNmyPvNFwiIjJA67AYXu3ad1Itbt16kgMewLV8ry7kf7nPC90tlnSVIjZo1xTf//geqVKssESxuQzkbFReHEsUK47vP/41Wbh1ln3wuceuSjmP2x3o8H54Xl1OqrPPgeYlQcb3Z1n47+2tiv06e6wbbc2U0643nxeOZujwenwfrUA65nF0Urf3Zk9GCZA//wCaXV69w+dJFzEmYgc5u7VGuVAl8/dm/pdsbJ3n9q3mL3gWlyOrSx/tNG9ZHRNg4HDqwHy9+/inpBFheZ9hzUxRFUT4+VJBUkBQls/lgQaIMtGjfFt988g/0HT4Mc3btwvSNG6XxzwY/ZaXXYF80bdMKTVo2R2//wdIVb+qatWjb2R35c32NwKhITDPbhM+bh659vdGweVO079YVY+LjRVC4vMfAAWhstud+BgSPFGHg8S1BatKyBfJ8/Tnym0Z4vxHDRDwoWW6ePUTeuLxt505yXkOjo9C2izsateBxumDk5MmINXIzbMJ4uPfyRNCUyXDr2QPNzLH6jxwhx+DxhkRHJ23XTKJSIyZPwhQjU1w3Jn66HKuxWde8XRsjYx3MvnpKtz52Jezaz1uO184cj8+LMtVvxHD0GDQQg8aMRosObRFsrrP1vOzJTEGyh2N97Mu5M6cxa2Y8urp3RIkiBUVuGFkqZATHkQSlhEKV99uvkqWofp2aGG1eu+1bN+OnZ0+TjsKiSRgURVGUtKGCpIKkKJlNhkSQKD25v/wMJYsXMQ3+AQidPUvEhrDR36BpIxEGRozy5/oGnb16i1i1cXcTQRoaEy2Rljr166Jc2VJo3amj3FavWQ2hc+agaetWMlalWdvWaNi0sUiKdT6WIDVu0VzqFDbUqldb1ofNnYvy5cugVPGi0kAXQTLLeXzZj3lcpmRxVKhQFlELF2LgqGAUyP0tKleuaM61qVleTsTKxwjM9I2b0LlPHzRo1ljOu0zpErJvHiMqcQGqVa+K4kYiKEe8T2FsagSLY5/4vMqWLinblStTElWqVhZxopzlMwJRyly3Jq1aYPT06dkqSPawe5tVfv/tN5w5fQqTjEB2bNda5IeixMgSr6u9FPE1yGOeE9fztl6t6hg5bAg2bliHJ/wiSy4aKVIURVHSjwqSCpKiZDYfLEhsvLP7mUf/vihfrgzyfvMlShYrDLeenhIpYsM+JCFBRMl33DhpQNeoVQNxa9cZYegkgsSIjc/YMSJZjMxw7BLlgZGfvsOGiYhwbBPHKvE8GJmS4/L4SfcpNBQNSggjHEOio9DL3w/FixZEB49uKJjnOxEvdmejnLD7X9CUKRKVymfOeWh0tIyLymsa/YwCxRsh4vFyf/UZWnZsj1gje9wuiNtNnWKkraWRp6/gHxZqxGYa8pn7bYxwLT56VCJSuc25Uxa5Po/ZJ9cxysQIUq7PP4GfuRZdvPvI/rv16ytRN5Ejcy0dXeOsFiR77LvhMe32iWNHzZslEq1bNEXRgnnxjXk+jBR9Z54Lxy3VNALo7zsIq1cux/17d5K2tBUdV6QoiqJ8CCpIKkiKktl8sCARCgsjSZGJC+AbEoKq1arImB9GligijAQVLZAXpUsWQyEjKrXq1n5DkEbFxYlMUJBYh5QpVVySOPiHh0lXNEaBOKC/WvUq0pWPiSEoDvZjkEoUKYQhUVEiarXq1kLFiuUkosPIUL5vv5TjcTxQh+7dJGMaRY4w6jTUbGcJUhdvL8Rv3oIRkyaJWLELIZ8nkzxQ1EoUtW3HiInv2LHy/KvVqGpkIb8kp6hUuQKKm3MJjIxE9wH9kT/3NyhVoqjteZUuIYkp2K3QvXcvESs+RwpYyutqkd2CZA8jP1Z5+fIF9u/dLW+eZuZ9MrCfF9atXonbt24m1bAVjRQpipIW7P++6N8N5W28Tmq4nPzhOp48/9mlRMESpAMqSIqSqWSIILEBz/WMgszbt0/G7eT64hO0duuI5m1bG8n4FsNiYqQeu7NVr1n9DUFidMl72FB8++m/JJrCrnkSTTH7ZjIDygPli2N1SpcsbkQkn0RxOJ7IXpAoLONmzZLITK4vPkUBIybsvucbMlbEh5EkRoooJa06dpBECp6+PhKpso8gUVzYpW74hAkomPtbtO3S2dwfL9GxlmY7jh/y9BmEArm+gV/oOIydMQPlypWWKFa7rl3M9j0l0hS/aRN6+vnKuXTt6yVjopgIgs+Lz5Gixi52PL+/yuKXkwTJHvvGzKUffsDtBw+SHmnjRlGUtGOVJz/+iCWJiTi4f1/SEv1boryJVa5euoiQ8AicOXsmaQkc1v/YsARJI0iKkrl8sCBNWbUa/YYPk65t/YNGYkDQCFSvUU1kYoB5zLFHlICefj4iHozIVDPrKUiUlNxffYph42MQOneOyA8zzvUJDMDA4CCJKoXMnIkuXn3QO8BfIi2VKpeXKM7oadPknCxBqt+ooYwfYve8UCNJEm2qUVUiWxS274x8te3sLqLGcVANmjaWZA9VqlaScUaM6HD/rMdkCxSkYeONFBlhYvY7yhLr1W/SCANHj0LVapVtgjQuBN0HDpDny2WMWFF8GD2j1HE8FsdmMeLEZZQ8jwH9ELNkiQgbRZJjnJxRkCxYzl67hvPXr8t9R3UURVFSYv3I8vNPP2HRggVo1rABChbOhTKlisLfxxdnT52W9SwqSq6LdKlLKrdv3kRUaBiqVSyPwkVyoWaVSpgQFYW7d/7szu1oHx8Tv/76C35+/rPDdYqiZAwfLkimYe8zdizq1KuDsmVKolTJYtKlrk9AAKYaOWGkp7ZZR0ngWB5KCrPUxa5ZC/devWQbZo+btmGjZImjuFCUOJdSyw7tELlgPjr19ES5MqWkm1r1WtVFxNhVjse3BInRqormDybH+VA2GA3isZlamwLC7m08HrvDuffpJV34KFCM7LDLHyVtqJEn1mNmOW7HMUrly5aWrnXcrqu3F8qULildCLv195btAiMjZLwTEzQw6x3HUNWoXUOEiRElnidFS56XOSafW/N2ti577H7HLnc813dF6HK6IJ2+cgXnf/hB7juqk13wFzbl7Ti6Zh+C7Q+KafQ6OJbLY66LjsGzYbsewC8vX2L5kqVo1aQpihbPh4ada8IrxgOdh7dFuerFUNb8vRwZOAQXL5yX+iwqSq6FVdgemWy+S2tUrogS5Qqi7cAm6DuxO1r3bYTiZfKjdtUqmGa+s3989DBpi49XlPgZeP1KPweKkpl8sCARkRTD+CVLJDLCjHQS3TG3FATecjnvUzRYj9ux+5zcT0pMwG24nnXHL12SLD+yjanDpA/Wvnlrfw5/7sv2mJEjRrdkfdI61rFkwzoHuc/jE+4nqZ5sZ/eY5/LGduYcuJwy1svPF7m/+BS9BvtJt71R0+JknBIz8THFN7vk8bnL8zJYz4vby/7sjucI65xVkNLH77/9il9fvjCNMMURv/7y0uF1+xB++/UXh8dSbPD6OLpuroIlRry/bvUqtG/REkWK5EXd9lXhPd4D/rP7wXemF/xmecttx4AWKF2lMMqXLokxI4Nw1fydsUrKfSsfF1Z5/OMjTJ8aawSoKoqVyoeWfRpgUFxvDJ7dV94j/uZ2YGwvNOtZD0VL5kW9mjUwOz4ez54+SdqDvlcURUk/GSJIhI14NvwpM7x9c13SctZJqmdtw+Vv1k1KvJBU336Zo31b2O83FUnHsd9f8r5SbGdfL+Vj6xj22zGCxkiVJGkolB+MEpUqUUzGJPUbOcKIje262W9rvz/uP6XspYT1VJDSB16/No2py6hbszqqViiLqhXLKRbmelQoUxLdu7gnXauMiSTxmi9auABlSxYzx3BwXFfGXPMyJYoidsokuU6Ort/HjCVGnGtty8aNcG/XDkUK50HNlhXRO7KLrbE7wwuDpvX+k+m2RrBPfB+092mGkuULolLZ0ogICcHNpO68LI6OpzgvVnn65DHmzJiBBrVqokjxvGjaoy4GTOmJwXNs7wn79wof+8/ph36Te6Bxt1ooUiwPGtWtg8S5c/HTT8+S9qjvFUVR0k6GCZIrw8QLEQvmS1e5AcFBksmPY6ccRbreBxWk9MNy9vQpFMjzHaInT8LshYmYMW+uYpi/dCn6DxooEsMoW4YJkikToiMlS+O8JYsxc/48h8d3RRaYz3H1GlUxZLCvXCdH1+9jxH4+tV3bt6Nbp04oUigvqjUth56h7hIx8puZQoxSwMYvRYn32/RvjGJl8st7d0JkFO7fvZu0d238OjvmD5G8js+f/4zEefNFcAoXzY1GXWqh76QeEilKKUYpoWTzPeU9wQMNOtVA4SK50axBA3y/cJFkXZWSQX/vsgTzPf/K7nxfsYtuDvruV5SPGRWkDIJd6Diuit3p2L3PihxlBCpI6YeFglSqWGEcPHMaN58+xZX7DxTD/ZcvkWCEnn35M1yQoiLQtGkj3H3+HNcePHR4fFfkwS+/onPXzi4jSNYXC8v+vXvRy8MDRQvnQ9VGZdF9rBsGz+oLvwRvh43ct2GJ0sC4XtLNqmipfOY9XAlxkyZJNyyrODofJediRRf5t2j50iVo0aiREZs8qN+pOvpO6O44uvgOWJ/becV0Q90OVUWUWjdrhjXme1qOacrrVzlflH7/5aVgSdLvL5/LY1nPNoC0A1SYFCUzUEFyAlSQ0g+LJUg7Dh3E+Vu3cOrqVcVw9cEDxM6cIdmfMlqQJkZHolGj+rh87x5OX7vm8PiuyLWHj9CxU0cM9feT6+To+n0M2IvRiWPHMMDLGyWKFkDFuiXhMaqDjC1KrxilRLpTze4n3a2aedZFkRJ5Ua9GdcxJSNBxJ06EJUaMimxcu1bGo1GMaretDK9oj/cSo5RwjBL30yeyK2q2qiTdOju1bYutmzaZIydNU5FBf/8yGp7fjwd346RXJ7y8e0tO9dq0GDzcuVnu8+r9Yf5+81n8oclfFCXDUUFyAlSQ0g+LCpJjVJCyno9dkOzF6NyZMwgYNAilihdG+VrF0WVkO5EiEaPpjhuy74PvDFtEieNOmnjUkXEnTerVReK8eXbjTlxvvFdOB69t3S5f/fEHtm3ejM7t2xtxyYtarSuhd0TSeLR3dLtML5Yo9QzrjBotKpjj5YOHeyfs3rHDnI9NlHJahkmWR/t24lDr2rgcPdqc3ytcjhmN+1vX4Y/nP+NabBQujhuKm4kzbduY65lyH4qivD8qSE6AClL6YVFBcowKUtbzsQrSqz9srzvLxfPnMXLIEEnSUbZGUXQa2hp+M40YzfKGz/S/HjvyIVjjTtgdq4F7DRQtnhctGzfGssVLJFOjlBwaJXAlksejGSHheLQeXbqiWNF8qN68vIxHY7fLjBajlPglGFEyx/EMcUPVJmVRvGgB9OneA/t277admyk55buV5cHOzUaKxuDatGjcWb0E1+Ki8eP+Xbi9PBFXp0bi1x8f4sKYADzYsVHqO9qPoijvhwqSE6CClH5YVJAco4KU9XyMgmSVK5cvSwruiqVLonTlwnALaGkbA2IaopkpRimxxp0wXXi9DlVRtFhetG3RAmtXrsLv1vmqKGU59ok6Du7bL0LCbpdVG5VBj3Gd3ms82ofC4/G43cd0ROX6pVGiWEH0690HRw8fTjpT8x2bzRElForPlUmh+P3nn3AxdBhOeLnhyfFD+GHmZNxd+73U+WHGRNxMnCH3He1HUZT3QwXJCVBBSj8sKkiOUUHKej4WQbK+MFhu3riOiLHjULlcWZSqWBgdfJsnJ1LISjFKiRVR6hPVFbXbVEbRIvnQqW07bFq/3jyHpPNXUcp07MXo2JEjGOjljZLFCqFyg9LoPrrjn+PRMrDbZbowx7W6fnYLbo+KdUpKt9DBAwbi9IkTSWeefd+1LPe3rMGFsYFy/9nZk9hbqwQe7t2BJ4f34nywL+6uWoxzIwbip8vn8doFpw9QlMxEBckJUEFKPywqSI5RQcp6PgZBssr9u3ckxXa1CuVRolwBtBnQxDQ2k8ToHWmYsxKZRHROP/QKt407YRa9bm5u2LFtq3nP58xxJx8D9hJ9+tRJEQ7+Ha5QuwS6cjxadotRCnwoSuacBif0RefhbVCuRjGUKV4UQwcPxvmzZ5OeSdZ/53KM1ovbN/Dk1FG5z3fsYyNGL25dl/tM4HBryVw8O3/alrBBs9kpSoaiguQEqCClHxYVJMeoIGU9zixIVnnI982kSeZ9UxnFSuVDS68GGBSXNJlrNkaM3oXVncozpBOqNi6DYkXyo1c3jzfHnagoZQhWOX/uLIb5+8vkyGWrFYX70NYirBQRR69RjsCIEt8njECym2jpKoVRrmRxBA8dhssXLyY9s6z97FJ8JEtd0mMWmwz9ea3t1yuKknGoIDkBKkjph0UFyTEqSFmPMwqSVZ48fmz+7sSjTrVqKFI8j6TWHjC1JwbPef+IkWxnGqRZKVaWKHmM6Shpx4sVzo++PXvh6KFDSc9UI0rvg9WIYLlmvgdGDR8pYlGqUmF0zKbxaB8Cz1PO17xH2W20RIWCqFC6FMaNGo0b123fcSyOroWiKB8PKkhOgApS+mFRQXKMClLW40yCxPcDy/Off8b82XPQsHZtFGYKbY/aklKbESPfD+xKx4xzA2N7CcnLKUxmv8kN6SSBkscp170vZj/WuJOuI9ujfO0SKFGkIHz69sPpkyflebPkpL+vORV7Mbp96ybCxowVkShRviDa+zb7UzQ+9DXLJvh+4/mz+2jbgU1QvGx+VC5bBtFh4dLN1CqvHFwbRVGcHxUkJ0AFKf2wqCA5RgUp63EGQbLG5fz+6y9YvnQpWjRqhCJF80jq7H4Tk8RoxoelYbYay4061kb34I5o49UEPUa7yX65zjvGQ6TJkqH+kz3Rf4qnCFnf8d3f2McHYUSJjV+mIe88rI2kJS9dvAiG+wdI9zCrOLpOiu2zzvLg/j1Mio5BVY5HMwLRul9jub45bTzahyCiZJ4Pu5O29GqIYqXzo2blSoibPBk/PnqYdCWy9r0iDbfXGu1UlMxEBckJUEFKPywqSI5RQcp6crIgWWL022+/Yd3qVWjbvDmKFMkjqbIpLBkhRhb2gtR+QHNUqV0WjTvVRv9JnmjVqyEatKuBFt0boE9kV7T0bIgmXeqifpvqaN6tPhq0rYEm7nVMQ9UIlBGclPt+H7gfipKMOwlsJeNOypcugVEjhkv6cqvkpL+32YlVHjy4j+lTpqB2Vdt4tFbeDTHQvC6ZIUby3kuKIPLWUZ2sgMf3N8+P3Uub966PoiXzol6NakiYHo/HP/6YdGUy/7PN9+KLF8/x8PFjfV8qSiaiguQEqCClHxYVJMeoIGU9OVGQrK50nCNo07r1cG/bDkWL5kXttpXRO7JLhoqRhSVIDTvUQs8Qd5Egr6hu8BzbCVXrlkO3oA6o3awK2ng3Qb1W1dArtDPa9m0q99ktrr6RpF7jOmfKeVnjTtr7NUepSoVQqVwZhI8dK+nMreKqDVKrPH3yBLOMENSvVRPFjCA061UPA6b0zLSI0cC43vL+oHxRTBjF4XIei1FFS5T5+nGZYN1Peq9lNNw3ny+jm02710HREvnQuE5dzJs1Gz89e5Z0pTIv5bZ5E+LuwwfYd/p0hv3tVhQlNSpIToAKUvpheR9BOnvjBq7cv28atA9t25jn5aje2zh/86bD5eSk2deZ69eNoDyU/V+9/wBnr9+Q5Snrcj+ZJRjZLUh8vufM82MdR+szEx77gnldKSx8DS7dvZvqPFnnrHmd+F5w9Nq8DzlJkP6cn+Y1tm/Zim5unVCsaH7UbFFBUmKLGM3MWAGxsBckSlFzj/oSpWI3u4rVSokMte7TGB5BHdHI1OFYpfaDmqNFjwYIXDAAzUx9ilVGC5KFNH6Txs20HdgUJSsURNUK5TA+IgJ3bt9Oum45429cVsD3CMvPPz1D4ty5aFy3LooZIeB4NApCZki0BV+L/ka+6jSvip7j3NG8ewPzPukkokwpY5RR6iVJkvf47nJOvE+pokxlliQRPm8+/36TeqBRFyOM5ro0b9gQSxcuxMsXz+W6ZYYoUZDuPXqIg0xBroKkKJmGCpIToIKUfljSJUg8f9No33fiBGJnxCN60gSs2bJZGvIXTMPI2p73L9+9Jw1oPr6Y9PicaUxTfnbyWEmSxG0oAVzHx2fM9Tlw6iSmxscjIiYaU81x9p88Kfs6fzOprtmW9XYdPmwTCbMt1/M+98t1fMzjSiPewAY/G/pWPXk+f0F2C9K5Gzexbf9+JC77Xp4vl1FGeL2s52Grd0Oe56U7d2Rfp81zZx0+X663v75cb113vg7yepj63N/F27bt5Thm3fod2xEzaSIixkfLOZy4fFmWS11zLO73wKlTOHj6tBzL2r8cwzzmfvl6yX0eyxyX2/G9wWM4IicIkv3EnUxx3bNbNxGjak3LoWeouzT22Ph01BjMKKwGKyNBPYwgterVSGTJK7obmnaug9a9G6OTfytp/DJqRHlq178ZmnWth4B5/dG0S71MFSQLnievB++37tdIBujXqFwJUydMxH3znrOKo+v8MWCJEbtyfb9okTT8ixbLKyJAIfCfk3liZGEJUr1W1eU9UbFqKXm/8L3RyK0WGnWshXb9msp7pHGnOmhi4HumSRfbLbtqSjKRTO6WZ4kSZb6BW3UUKZoXrZo2xUrzvf3rL7/IdcxIUVJBUpSswekEibIwdfVqTFu/3rABcevWYfI7zm3qmjWYvmEDYtesdbg+p6OClH5Y0iNIjORQjvoN6IexYaGIMwIxf+kSHLt4EVv37TOytEUaxRt27MC8xYtw6MwZs90VLF+/DvOWLJbHW/buhUf3bli5caM01jfv2YM5ixbKftnIZgN64fJlaNe2NZasXoVRIWMw0Geg1N1+8ADmmoYIG+Zb9u6BZ09PLFqxAkfOn5ft2RBnHR6HDXeez46DB3Hk3Dk5pwXfL8Xhc2fleTh6fvZkpyBxGUVk2MgRqFOrBnYfPSqCwee9cdcueR58zqzL573CfG6/N59fCszR8xew/cCBZHHdun8f5ixMxJ5jx3D80iWRLorWobNnRDD52vF6r9y4IVlwKDIjRgVj4KCBWLxqJXr28kT8nNlGcu9i8coV8nryWGNCx2HoiGHmmOdl/8cuXMCJpGMcNg2THYcOYd32bSK4e48fl9dz3bZtIk8pnzPJTkGyF6Mj5j3D1NYlihRA5Yal0X2sW3Kygqwc39E7vIv82s/GduchbaX7FBNBdBrcCl2Ht5d1rMOEDWwAs1HMBjNvmbQhq86Vx/Sf3U/Oo0Wf+ihWMp+kO58RF4fHPz5KuqofjyjxbwELG/arli9Hm6bNpMFfr6NNVjnxbmaLkUVyBKlFVXndW/RoKK8DI4x1WlRBl2HtUK1ueXQ1tzUbVZJtGGVq7Fbb1OuJhu1rwjvaI8vOl8fh9ekT3RV121VBkSJ50aFlK6w3f79+499Zlgz4W6uCpChZg1MJ0kTzB5v4hoxFy47t0bhFM3QwDdLAqEhZnqq+EYsJS5fC02cQmplGaU8/X1kmy1PUzcmoIKUflvQIkkjDjHj4mgYsu16xmx0b+QvN+6pVq+ZIWDAfqzZtNEIzCJHjYxA8drQRlAOYFBeLkIgwDDcN/iWmwd28eVMkmtdrzdYtGOg7COEx0aZBHiRiY+2vbz9vaYRTrLi/Tbt3mboDETVxAoLNBzFh/jy0adMSs03jf+bcuZgaP13OycfXB0vXrJZjU8S2GUGgaPTt3xc+g30RNDpYGuiMtDh6jhbZKUgUmN3HjmJwoD9GmvOdMHUKrpjzGTpiuCwbMnwYAocNxU4jIF59vTDafNa9zfXia7N83Tq0b98WM4zQrN++XZ538JjRcg2Xr18v15vH5HMLM38TCCWU+55lXj8KKiNSo8eFIHrSJHkNeCxG8qaYazzUXEte29iZ8SJHvXr3FIEbY+pTdvedOI4+Xn2wbN1aOY+4hBn4fu0auHfuJFLdw7O7yBglLOXzzg5Bsv64s5wwksdU1iWKFkSF2iXQNai9ESNbumtHjb3Mhl34GKVhI5iCZg3Ct6JYXCfd/JKWSyM3ztYIzcxuU2/DOjd27WrSvY7MB9WgVi3MTUjATz89TbrKmTfuJLOxJPrVq9+xYe1adGzVGoUL50HtNpXRJ6qrJCfIrG6XbyNZkJpXRe+ILhI95PKWPRuiesMK6OjTAh0GNpeumpQovj6tvRpLFJLvEUYd2dUuqwTJgteJ16tXRGfUbFkRRcx17Ny+PbZs2pQsoB8y35YKkqJkDU4jSJSESaZx2alnDxTKmwvVa1YX6alRuwZad3ITQZq0YoVEl2LNH3hGjSabxxSL3qZR8t1n/0aNWjWSBUnqmjqsO3nln8/Nfjn3lRNkSgXp3fB62M9HwZIeQWIDlt3qRpkGOWWEonHl/gPMMIIyYNAAPPj1VwwPHolevTylAd66dUuJGDAKMc4IkptbR4kmsIF9+6efERoZAXd3N6nbsmVzrN+xAz88eoSl5j3VyTSUA4cNEQli5GT8lMno2LEdps9KMPvpIFGnmMmTcObaD5huGmBxMxNw/fFjDA7wl8a572A/JC5fhhtPnqJnr54S9Th55TL8AwPMOZyQhr+j52iRnYLE5ZOmxcl1ohhSQricz4kRnGvmGvkPCTT3Vxox6iuRIUbKRHISF2CQny/uvniBUWZ7CuWT16+NnIwT0Yoyrx+jcOw6x0iUu7nOURPHy74H+flIFO/ynbsiM3379xOx8TNSxohVJ/NahYSHGuEcbur7SmSKrwPfC5QwRo4OmvdTX3NOjBZ59/WWSBiFqI93H9x4/AQTYqdgsnluvL4pn3dWC5JVzp4+jQAfX0lhXbZGMUlpzWiRn5GjrIwYfSxIlMA0fhntati5BgoXzYMm9eph8fwFeGnel7by/qLEjm1sQstj8zeNj3mbsl5aSMt3hH10cfuWLaYh38E06POiRvMK6J3J49HehSVITNrhFe2Bxu510KxbPRmPxO51TOTRZWhbiTTWblpZxLpV70YiUNy+aZe62SJIFvycUf7ZfZXdWIsWzofu7p2x23wXWOV9REkFSVGyBqcRJApC2JzZKFIgL8qXK4OYJYuRsH27RIjC5swRiYhKTMSISRPhN24chsZEI9o0lmKN7IwzjcySxYqgToN6Uo/iw3VDoqIwODQUIQkzZf+TV6yU5UPHx8AvdByGmwZY1MKF2S5JKkh/DcXo119/kS8LYr2p0yNIl0zDmV3aepoG+6Ezp6XbGxvn8ea95WcatXd+fi7drhjVYBRn9ebNIjH9B/SXRnGHDu2w++gRDPIdJJEKSk83j65GiFZJRIld4dignm/er4x0sOE9YFB/iUpNnz0Lnbu4y34pUJt270aAkQR2EaPIhEdHSVSC+/veiLuf/2ARMwpcb68+ci7sCjY8aKR0S8tKQTIbJ2/P8leCxG6CJ80to19du3UxzzEAjRrWk25wQ4cPk4jaKbPNgIEDsMw8T15rCuTqTZtEKCkslKebT5+KlPL1uPXsmUR7eA05tohdJMNjoqQbHEV0YlysXCuuo/QygkThmTlvrkSp+g3sL1GiHp49ZDuK2fYDBzElfpoR5okiNjzm2m1bsWbLJnQ3577E/C1k1Irjk5atWyP3rz14JNd08vRpmSpItgbta7lNuc5637NcNcIcNHQoypQoilKVC6NTYGtpKFoJCBw16DITNl7tcVRHokOmUexoXU7DJkr94D3eA/U6VkfhwrnRslFjrFq2/M9xJ+n8XPH1+/naZbx8cA+vjPj//vI5frpyAb+9eG4ev/pTntL4t//335O6dTl4r9iL0f49e+DZpauIUdXGZeBpBEQiedkkRvYwi510tYzrJde664j28h5hlzv3gNYiS+ye2Tuiq7yv2Q2QcFuOa5OJiLPzhwBzbL7f+bnrMdYNlRqUQjEjSl7dPaW7q1XSI0p8PVWQFCXzcR5BMo3X8HnzUKp4ERTKlxu9TSNxvGlsTpOxRWtEIDx9BqJ0yWIoWbyoEal8aNi8qQhPyMyZKFG0sAjSlFWr5THvlyhaCMUKFUC5cqUwxDRCI+bPR/0mjVC8SEGUMg2LEqZx7R8eJtEkR+eUVagg/TWcx+WyEZr1Bw7gvvniYAOSJT2CxMY8G9AxRmzYMPfx85FG8gJz/YNGjZLoz3bzhRY4dIg0yNkNjjLTu08viUj4m8Y+u9Gxi1iQaYBTVBhxYsOeAkXZouSwcc1lNx4/lu5Z7FbGuqPGjpH7jEIwohE4NFAEYOOunXI+Aea47Ea3bvt2BI0eJZGky/fuY3BAANZu3SqCNC4iXIQiKwSJX+gPHv+I7ceP4fEzq4vRXwsSxXGVkR2O/+F4Hl4Pdn1jF8Qhw4dKNIlyFDlhvETjKI18zr379MYiGR+03lzbUbLdHiM1fgGD0d8IzhDzelBA+fpRPmcY+fnh0Y+YMXeOdJkcHjRCpJPH5/uA3R4pVLef/YQQ8/nm60OJYqRphHnNNuzcIeO6OnfuJOOMOBatR88e8vpQrlZsWC9dGxmRWrV5k9y/Yl4LShePye6Z9s+bZIQgvTbv8zPXruKQea7yg4Apr83fAXsxun3zBkJHj0aFMiUlVTVTVvvEZ58Y8Zhs3LbqyTmOasov/x39Wso6/sLOMRs8NzYie47rLJEC3reiFhQR1pMubkn1OPCet7Zts6eLoAXPkzLBbmh12leV7lQdWrXGevOdwdeMJa2NX5aLoUNxsl9X/PHLS/zy6AHOBHrhxb07IkaUpRe3b/wZYfoLeMyT5jO21/w9eG5lVDPL7N8rRw4fQr9evVCsSH5UaVgGHqM7JF9jR881u3jjvZB0bpbs85YSYtXh+8R3hu19bq3j/WzHTpS6BbdHxXqlULxoQQzy7ouTx48nvSJp+17n66iCpCiZj9MIkiUJXkMCUbRQfuT5+gtUrlwR3U0DKcI0Vnl+QVOnIMg0cNlNzs2zO77619/gNy4EEUasKEh1G1KQVqFlh3YiWcNMQyx09myRqkbNmqJPYAC++uff0K5bFxGy4NhYWc+ufY7OKatwBkFiFjhKiq1QULIS07C4bhqGCxbItdp8+DB+/OknXDx7BiUKF0iTIBE2sDn4f++xY5IMgFEIZjhjJIfr2SA+euGCdLc6YOSLImIN0reyx1GE2HjnWBtJHHDA1D11MvkYtv1dSDredZEqisRJs5z7pSxxDJG1H9bheew+ckS24XF4PtwPHzN5ALfl/eNmuXUef4UlSDUqVTCXj82t9yv3Hz/COHPN48xnare5Dr/8/jumjI9+qyDxMc+d8FpbUsrnQGmaMXe2XA9LgDw9e2Dttm2yjBG9N14L85jb8fry+fO14P74+vAx7/P1YoIFii2vp3U+vE7WY16vQ+b6cn+89hxXxv0y2sXXlgkfuI5RJibH4Pb25/HGfbNP7pf3U0JB6uDWAcOSBOl9y17zXho9Zy7mb95s9nvFJkqmwXTLiNHkCTGoVrk8SpQvICmq2Shjgyw7xMhCuklN9pQuUEzl7RXTTQbWMypgG3jfAG5+rdB3YnfUalJJBIqSxLrclvMgeQR3lKhAJ//W6Dy0rWzHAfqcQ8k9oE22Pj8LS5Q4VqZGywooViwfuhvB37ljO35Pklkpf9GgZbk2fTyOebTErUWz8Nuzpzg30gcv7t/GzXnTcSlsOC6M9sfDXVvkr56jfRDrM73fvF9D5s/HzHXrcPj8Obx8+ULWnzh2FIGDfVGqRGFUqFNCGuxsvOcUMWLkKqdJWoaRJEqU/i4j2qJczWIoW6oohg8JwNkzp82rZl5Zvn5/hSmPnjxWQVKUTMZpBImw8TvFiMKY6dPRY9AAVKlSCd99/gnqN2ko60caOWLihvLly6B0qeLI/eWnGBAcJJEhClK9Rg2kS14l0zAsnD+PuS0v5M/1DapVr4qAiHCJHBUx65q2bilyxSgVj5vyXLISZxAkRpA2HzqEizeu4+y1q1nKRdOY3Wa+9GPMaxW9ZAnCEhMRt2YNZprrVrNWdWn0pkWQCBvNbGxTcOwb8dZ6kaikdXwsdQ3WY97ysaO6xH5/cj9lXbvH1n7sj2Ftz1urnv193r4LClJcwkzUrVsb56//YF6zGzj3gxGKdHDBbHPQyEOMud5Rixcj3FzzBTt3os/A/mjRrIlDQSLW+VuPeZ/Pm90V123bKttRSPYbWeE4Lsqhldb7bdumXGYdl7dy7Uwd+3N5o465b22fsi4fJ9/ncfg4aVtrm5T3rfopufbgIbp6dJWI1qXbtx1e03fBa75m316EL1qEyCQSjUDOX27e59Uq4/NP/o5mnvVEigLm9hPBcNhIy0J4DkxsULdFVbTv3wwdfVuIBPUK64wGbZm+uTWadK6L9gOaobF7bbTr10zSeHP8CBuSXM77FKGqdcqJWHFgfo2GFUWWKF4cpG9FELIbnnPA/AESUSpeoQC++vRfEnk8cfECzpr3ya3798zfbscRJUrP1akRuLt6Ka5MCsXdtd/jctRoPNi5CeeDfGT9kxNHcG7YALx6ZRrGDr4DuO+7jx6aY13D2n375O+hfD4XLsSsjRsREx+PEkUKIXe+z6WBHjC/v4hdpkRakmSAkRy+PpQCh/Xs4Pulx5hO8ppmufia85Wok7nP8+B9nn+mfI7MsdhFM3Bef3QKbIVceT5HwTy5EB0ThXuPHslreMf8nXYEo0dnrl6R6KAKkqJkHk4lSBNMg5cJFJjae7r5Y0/ZqWoaBoXz5Ub/oBGoWLEcypUthf4jhsO9d0/k+frzVIJE4alQvqx0r2M0qn/QSAwcFSxd7Cgho6ZPQ6eenmZf5ZH3my/R1dtLlmenJOV0QeKX8rOff8JZ0xB0JDCZzXnTcN121AjSkqXSGIgwDUc2BhLXrkXtOrUkGpRWQSLS0E1q9L4N1mH0gQ10Rjwc1XGEfYP6XViN7dPX/mzQZwTJglSvDk6bL9qz3PeVy+nijNlm7+lTyVIqDbAtW9CjnzdaNn+7IL0Ndn/jtbQiYNyWr5n9Pqz7jCbxmqclWka4XXqvOevbH/tDsQTJxwgSn6eja/oueM1X7d0j72+r0Tvd/D3cf+YMEmbGo17tajKxaau+jWTsBRu+2S1JfwpSNbTu3QiVa5SWNN4cPF+lZhmZq6Zuq2oiRpzviN3sGCHiBLLsQufm1xItPBqIIDXvVh9DEgca0bJNHDts8SAZkM9oUk4QJGtQvue4TqjevDxKly4M716e2Hf4EM5dZ1T4Iq7fvfOXgnR5Qgge7tgoXelO9euC04N7ScTofLCv/N1/evq4EaT+fylItx/cN5+Ny1i9d6+dIC2S98q+06cROi4EFcuXRPnaxSVpB0VAuipmoCTxdWfksIl7HUm3zUl/mcKdy5kghK8t5YN1eWstI5zbqE6zKnI9rWWWuLBu8mNzvnyPW49l32Y9l1kZGpPrxv25rSQoSdoXXy+pY94//MxwgmJGsLoObyfn3bRrPRn7ZB0/Q+B5m+Nyn52GtJIoUpVKZRA8cjg279yOwxfO48iFCzh8/rxDjpj1B86cxhXz99G84KneA4qiZAxOI0iUBCZMYIrvUdOmSda6UdPiULZ0CUnA4D10CArlzY0W7dvKmCRKznef/esNQZIuditXSR3KT/+RI0S0IhcsQNjcORg7I16SPHB7RpPyfv0FGjRtLN3tVJD+GvtBv9lRpItdYiKmrV4t3b2e//ILLqSzi51gGqFWw/ivJIl12FBnJjZONuqwQZ3iMdezC5bVVUvqp9wmCevYrMMoCsfYJO//LduklTe62Emz7P0KxyCxi90k8/7caK7x0xcvMDkm6i+z2DmC9ez5qzqM5HDMFdOlU6pS131ze26T8pq/eYw/79uvY7c+dtf7s+6b+00vGdXFbp+R0lFz5ki3qQPm/f3Tzz8lrTGvx/17mDJ+PKpVLI/i5Qqgdf/GpkFmS0+dXaIkDeVJnpKqmd3oPII7yFgkClLtZpXhHthGutNxoD3nuaH8sDtdvTbVpXsdG6mUKDe/1jIRKCMebfs2RbMu9eQ+573JbkFig5rXuFd4ZxGjokXyoru7O3Zu3570ytiVv/jFn5/EK5PDcG/jSql6f+MqHOvaAi9/fIDrCZNxOSpYutjd37pO6jraB7G6YR0w7/lx5rtvxtq1pkF9Rn7EssoZ8z4K9PVFqWKFUL5WcXQZ2VaEJKOyG3IcEF/j6g0qiChRehkB7GOWMfMco4K8Zd1uIzugg08LkWJOttpjjJu87n3Hd5eU3VzeK6yLCA3fL5SubkEdJMJEmZLMdua9wsyCnc16SjMnlu0U0FrWsdsjnxcTPPC4ImpmW0pQu/5N5T3EY7n7t5bJaHkMvgd53g3a10CHQS3k9U35HNNNkhjxOrsbMS1bvShKlyiCEYGBuHD+XNIrw+92W8PsXXD8oaPXX1GUjIGfM5YcL0gcBxRpGsCMAnHMUJlSxVHMNH5LFissY4fGmzqUmfy5vkbZMiUl2ULBPN+h7/BhIkiF8+WRlODMYDcmfjpq1qkl3exsSR2KoNdgPwRGRRnhKinLmKChrDmG79gxOUIOc7ogZSccvH7tzm3sPHEcj58+MVfH1uhPT5IGCzbsR48bK8kCODEsG8js8mV1reJ+2EifPD0OnJSVyRqYLIARDWZIYx2upzzZbm3HlfUGjjPiJLRstLMLF/fH/VOw2IWL9y/evoM9x45KlIcD/pndjQkdmAUveb9mOx6LdRmRsJanJaqSIUkazDbs6rHOPJ87D+4nN8releY7JfIczHVhQor+g8w1T3pefD68tZ7jCfO8mFiBssikCoFDh+DW06fS/Y517K+BtS23k2t+wFxzcy05Ti75mpt6rMPHvOaX797D5j27MXPePFnH13Xt1i24ktTl78392qJdfG253NHzSklGJGlgMhK+b3YcO/anGCX9gsxMjla5c/sWIseFolLZ0jIeqd2gZiIqbJxldbclHo/y08ariTQ6+as5xw6xQdt9VEfpbscGLxu37FpVv00NaawyctTQiBQbu2xAdw92Q0efltJQZQSK45Z4n130mHXNJ2lgflZCKeM59I7sgtqtK6FwoTzo1LYtNm/cKNEdlvRkJ/vj998lMcOvz57I9sxc9/LebVnHcUxPz57Az1cvpSmTnSRpuHwJu8zfxGc/PZNzMS1qWWd96bNwfqyBXt4oXqQAKtYrKeORBickJWr4AFGiIPH15gSufN0otU061xGZrduyKjzMa1q/dXXzHnCTOYzaejeRCCIjTRSZhuaW74NuI9uLBDXsUFPeB/XbVJOJYXnN2w9ojsbm/cN91m9Xw4hPa9RoUFG2qVq3nBGf+jKpLAWLXTPrNK+CbmbfFHS+h2o2rIhWvRoaGkkdaz4ldv+0RQLd5ZwpZx8UQTLXkdeTktZlZDtUqF0cJYsWgt+AgTjDbnJJxfpO52c5Ldi/3oqiZDxOI0gWY2fOlOjOgKCR8DHyMnraNJEHQhFihGmwaWxFLpiPwMgISfHNcRJM5z1s/HjZB58Lo1EBERGyn8FhYZIhj/WYuIFRp0GjR4lIMeFDynPIalSQ0oZpAbBFIl8eLOkVJDZ6OSif89p07tJJUkNfMg1sNq45F8/BM2dkXh2mpa5Xt7bMvUN56dixvWSxY4YzDtpn+mg+5kSmTB1OueK60KhI2XaceV8yA17A0EDJ3BY5IUYypzE7HseosGEeZkSjQb06kq1uQuxUiVIxcQH3y3mZmNXt8LlziOCktWbfg3x9JJrFxryj52ZPRggSkW0ZOeQ1T/pDkl5BomDsNY04Zurr2rUzNu/eLQLCyVt3HTksSRb4HJl+u7655lHm8zlv8WJJq85sgJxIll0Qt+zdA/9Afwz0GSjzFDECxOvMa87HYdFRkiKd19yzZw9Jw75x1y4MDgyQMSIbd+40khaChg3qydxGzKTHa7/z8CEjwP4ib3zMa85z4ASznFtpuxHEczfefc0zKs239Xq97TV7ZRrZVrl29QpGjxiJsiWLS0a7jv4tjSjZsn9ltSjxV3PrmGws8j4bnZQMaXyaRiRvWU/uc7mBdbmcgidRoqTJYmUba+LYLI6O8ZgcP8KEE8xcxxTfrZs2w1rzHv39tyRRfc/PFJN5U4zksflMWZGiV+ZzxvvyOI1/+5PfK2+RNPuo/8F9+9DbozuKFMqLyg1LS0pqyp+8Hg6uwbuwFySKDLtTUjwotlVqlxVJprB0HtIWjd1qo09EVzle40510NHUoThTatiVskHbGiIujP5QloYt9pGxO5QoJvag3NRrVc1IVlOzfW0MX+IjQsXucuwe16pnIxHpKrXKoIVnA4lm8jzqt6kuUS7vaA8061Zfzre5OZ7fDG9b9Mgcl9IksujgOaYFbsvPm8fojqhUr5QkmGLmwGOHDyddeb5E2k1OUXIiTidIFAVrHBLTb9ufF2Umdq1ZvmZt0n3bLddZE7++UdfUk/2w/vLlIiKsI8sMOeU5qyClH5b0ChLnQmKa5olJQhJqRJyRBc4vtGH7DslyxnmS9hw/KnMjMZMdBYlz+jCTnY+frzTkOafPtFkJ2Lxnj6QBZ/KBVq2aS5pqZkNj+ugDJ09KOu/eXr0kexsjIxtMIz3MNOg5B9Iy8/4bOSpYIkijx4XIpKhDhw+V/VIG+nj3lv1RzlZu3CgNfta7+uChw+dmT0YJErF/H7KkV5BYb9rsBHPNp2DO4kVGaCKMTDyUdOmM6DDixrmHeH25jNKUMH8+uvfwkGyDlCJKZ4CRpXjz2lE0OcHs92tWo6NbB5nMl6nSPXt5SjdFvmYUpNkLEyU1+potW4xkhUhKdqYgDxo9WgSNadV5TpTW2YkLsH77dvTx6oPl5nVp166NyDNlmanVL9xy1NXvTTJKkNLzubfKBfO8hwcEypxIZaoVQachrU3D18hH0lgMJW1YYsSugvXdqssksS0aNcIyI+y//vLSdrE/4LOU0aT1vWIvSrvM+9rD3V0mNeXkpj3D3m9OJAoSE1UwmQa3p5BwoldGgTjxK7tVWl0rmcDDzbeldLlr2K6GJN9oYG6ZtIPRRSblYDIO7oPS0tuIFrvqUYgoSZQYyhQlqF7r6hiaOFCESSJNEV2So0O1m1SWrnndjaxwXFzNxpVE2vqEd0WTLvVEkOq2rGb21VXOi/sbGNvzvX5MoFhKFCqkE6o0KoNihfOjVzcPmXPKKvodrig5G35GWZxGkFwRFaT0w5LeeZDYhaqXaUgPGDQQweYD0bpVSzAlN+cdYkOd6aB7e/WWKBPn7WEXKwoS58658/y5SEr8nNlGXvpItOfey5fw7uslDfp+/fuaBvp5kSymr2ZXuLiEBESMj8adn3+WOoyI9DJCRfliY52ydO/FC5kolpOWMsrChBO3nz2TSMl0cyxGN7iv1WzoiyClnqQ0JRkpSPawpEeQ2K2QUTtOHMt5p0aa69zSiCSjcJTDneZ123X4sLwmHEMUPHYMjl++JF3tGDXj9aXM8ppzPiRGm67/+KNM3Doj6dowukTR6tu/n0TX4hJmyLW89fSZzFvEa87IFSNC63fsQER0jHTd42vOyBX3dfDMaZkHi9G+WYmJ5rXsh2vmGjIKyNeGz8HR87MnowQpvVh/4FnOnDoJ/4ED5TNRoVYJGXfCRpz8Qv4B3ansoURwnxwkLxEfB3XSQnLEyME6R7A+G7K2roS2AfoZ+Zw4kL/f5B5o0q02ihTLg8Z16yJx7jw8Tx7X89rh9XcmLFFitGrLxo1wb9dOJo+t2bqSiAblMK2vCV8HiiS7uHEeLE742rJnI4nYcAwQxxhxfBHXsatdAyZycKslE79y0tf2A1tIwg5GhFp4NoSb2WZAbC/phsfIj9tgIy9mn616N5JoEccbcVtGq/zn9JVbjmHjmCaKDs+n85A2IlQc00ZBatvX1u1TunSa/fG82d2O3UGZsIFjjzh+Lj2CxOtDIexlxLJGiwoimt3c3LBj61bzFrF1/daIkaI4BypIToAKUvphSY8gcXzP0jWrpesWowsLli6BZ8/uRiTiEWkkZkRwkHSF6+TuJoP32SBnQ52NbE4wetM0qtmla/6SJYiZMgnDgobLpK+MKm0/sB+dO7tj/8lTEgmhEDDq0aJ5UxGVbfv3SUOcxwiNiJDJURmxYGSKEZOx4WGInjjRMEEiHRz/xO5dnMzUs1dP6fbFyAa3Z/TF0fOzJ6cIEscIJZrr0KFjO8xZtFCuiUcPDxmjxS5xI0cHS6pvviaUQHZZnDl/LibFxcJ/SCBuGVGkoMwzrxVvOeEshYlitNYII6N9HLPDCBKjSowKNmvaSMYXsUudd19vI12jRYbYdZES3K1bV+lOOWzEcEyZPk1ec8oY5dc/MEBEtGu3zjL2iZMIc5LgnCxIFvZRghNHj2CQlzdKFCuISvVKyi/qjCZ9qFSwIck5jBgJ4EB3Nqpt4mKTDN636lqPrcZnciM0qa63abQy3TcfS72kbXkr21rbmcdskDK5A7trseEriR/GdLLt7wPgvtnYZjShWa96KFoiL+rXrInZM2biyZPHSVcz61/LzIZ/D1h+++03rF+zBu1btkSRInlRt11V6VbIa8LXwNE1ewPz2lnd0/h68b7czrS91wYbKCKMIFFu/OfZZaMzdXif9QTz2NoHsd4DbzzmduY+pYu3fMw6ltRZ8ytZ3Qaljln/Rh3uK+l+mp5jEqxLiWYyilpGKHm93Nu2w+YNG//8kSIHRRcVRXk3KkhOgApS+mFJjyAxekQp4TgTRgsYiWBXNiZHYPSCXdzi58zC6s2bJMKxevNmaUCzWxy7ujGjGrOr8Vjc32SzblxkuERATpvHFKdjFy6KXC1csVy2D4+JkjpMDMBxS4xYULjYfYv7mD5rFhavXIF127dJg56SwP1yfBL3y8Y/BYO3jJ6s2rRRnof983JEThEkjj/i9SQ3Hj821/wxNptrTtnjJK0cB0SZ4WvChBi8nRo/XbrFcZwQu8KxC51ci4sXJXlDeEy0kcojcq15bXjN2K2Or6NccyNSoeaazzESzC6QtmPMlW6QjGhx/xyztGbrFnn9+VpTyLjd3uPHcPT8Bcw3Qsa6fM04Xoz3HT0/e7JbkCzsRemgEUIvT0+UKFoQVRuXQY8Qtz8jSg4agX8JxSbBS8aOcBA+B+XXbm7r0sT9cYyJlS6ZDVev6G7y6z0byGzQUmy4H+sxM5lxcL9EH8wy1mVDtt8kTxk0z+XcV3+zHddxcD+7YnkaqZLU4eYc3Ie0ea/nwvOjdPEYrbwaoHiZ/KhdrSqmT5mKR+azYxVH1/djwvxhkOf56y+/YKX5HmrdtCmKFsuLBp2qS2RGIkrpkAiHxPWWhAncH6+7wzo5GD5/vle8zHuwXoeqKFo0nwjlWtNekr+tLCpGiuKUqCA5ASpI6YclPYLEhrRkkLtzR7Kd8TG3ofgwu9zVhw+l0W+lluYtxwdRSNhQt+qz0U8x4DpGc6zowuW7d2U5kWx0pi5F7JqBj1mP9XkM61y5Dx6Hj60Mavb7tfbFuszGxro8Dz7+K3KKIFnXzLp+9tecz0eux917ya8JI05yzZPqnDTywvusS0m5cv+Bw2vDddwH68o1N7LC8Wa8ptY1tyaj5bXhvvmY7wfbNbft13ptuV+eKx9b272LnCJIFn+K0mvs2rEDPTp3QbEi+VG9WfnkcSdp7U4lUJBM/Ubta8nYjxHf+4kscVA9UzhTYBq51ZaxIOzqxIHyHJBfr3U1Eafm3epJA5lZxig4zETGCWQ9gjuiVpPKyV2mGiZlvWvTt4k0qtk1i92wOACfguQ/tx8CJf13fVt6ZiN8Ds/XAZYY8X6b/o1RolwBVK9UAZNjYsx34b2k6/Xxi1FKLFF6+eI5Ficmoln9+ihaPC8ada1phLXHB4uSRHKcTI74fGU8Gt+D7jVEHFs2bozlS5bmyPFoiqKkHxUkJ0AFKf2wpDdJg6uQUwTJlchpgmSRPO7kjz+wbfMWdO3YUboH1WplG3eSZlFid6qZ3jbpaVUNtZpWlqxjHEzPuXA6GklqaoSH4004kJ5RIEZ+OFCe0SRKDhudlCsKEAfP129bw5YWukU1OY8WPepLZIiCxe0oYMxyxsljuQ3Hp1CQONZFxr7E9pKok8PztYN1RKTMc2jn00wm261SviwiQ0PBlOlWcfW/uZYoPX3yBHMTZqFRndrS7bBZj7roP8VTXiNnjAKlByaf4PPsa8SwsUdtFCmeB03q18PCefPxs5VO/SMYj6YoigqSU6CClH5YVJAco4KU9eRUQbLge4CFwrRp/Tp0aNVKRKl2u8oiMP4Upb+KEthFkCg1HAdE6WFiA85Jw8H0nNuI44TqGoFi1Ijd6pg1jAP3OWif++d2jTrWFkFq0Lam7KuJe10Z39Gsaz1J68wB++6BtklAOU/SsCU+cixGq3gOTOvMwfXvimpYYuQb74WO/i0kFXr5UiUQMmqUpEi3iqPr5cpY5fGPPyJh+nTpfli0VD606F0fA2J7ynvlYxMlPh8+L75nm3rWRREjhvVq1sC8WbPw7OnTpCui7xVF+ZhQQXICVJDSD4sKkmNUkLKenC5IFpYo8X2x8vtlaNmkCQoXySNprSk1ElFyJB52gkTJCZjbDw3a15AMYu36NUOzLnXRxquxZAxjVzhGmTj/TdU65ST6wC5xlCR2xWtqRIjd6SxBamyEid2wOLks1zPTGKNIzHbGLnoUJUpYx0EtpF57s38e562NdHOukulupjc6DWmFstWKonTxohg5ZCguX7woz5/F0fVR/sQqjx4+wJQJE1C9YkUUK50frbwbyXWmfDq7KPH8+Z5nNLJFnwYoWjIfalWpgummTfTk8Y9JV0DfK4ryMaKC5ASoIKUfFhUkx6ggZT3OIkgWlig9f/4zFs2fj8Z16qJw0dxo1LWWpG+2RZRSNH6NeHDSTSZSoERxfAa72DFS0z24owzGpwzxsYxFGtpWJgulzDAhAscdMQsYt2fmOGbE44Sd7IrH/VPAuD9myWOEiY1XRrc4tw6Xsy7rce4ZHofnk/L8KFCky/C2KFezGEoWLYTBAwaavxWn5fmy6N/WtGNNys3C7oiR40JRqUxpFC+XH+0GNjXX3CYYaenqmJOwxIj3W/dvgmJl8qNK+XKYEBkl7SKrOLomiqJ8HKggOQEqSOmHRQXJMSpIWY+zCZKFVZ49eYo5CQmS5lrGXXSvIxLCrm/2UQKKkTyOM/fNLbEXE2kom8cc4E6hYdc4CpKVgjl5e1NH7pv69hEr3mdKcmuZPLbfjsvMvlLKEeswrbTHqA6oUKcEShQpiIFe3jh+9EjSM9S/qR+KVa6bz/24UaNQoXRJlKxYEB0Gt7AJR9I4L/vXJafB95tN6Dgerakk6qhUtgwijPjdvHEj6RmqGCmKK6CC5ASoIKUfFhUkx6ggZT3OKkgWVuG4k/jYqW+MO2H0RxqVSYKSHrito+UZhYiRObfuY91QpWEZydTXp0cPHNi3L+kZ6d/SjMYqlzjJ9tChKFeyGMpULQK3Ia2kWyO7N+Y4UTLn8/+1d99fUV17G8D/gPeXd633rntvejGxoDGKvUsEAUEURMGGvfdesSJWBCygINi75kZjwd69MYmx9957j0lMlOfd3y+MYjxJlHBghnn2Wp81M2f22efMyDpzHvc+++j1aCZcR5hAV756CVQuXwZjRozE+bO8Ho3IHTEguQAGpDcnhQHJGgNS7nP1gOTgKLdv3sC0yVPgU60qSlf4DOE96uqJ5psGJbuGXumJuNkXmbJcpi6XYCRTme/ascPsfcZsbDIhhdVnpL/PcWIh5cSxo4jsPwDly5REpZql0Wp4Iw2uIq+H3mmPkQlGsi8thzRERW9PVDSBbsTgSBPwTmR+Av7eErkjBiQXwID05qQwIFljQMp9+SUgOTjK1cuXET8hBl9UqYyylYujcZ8QHZ6UMUwp909+pQdAti1TlPuGV4VnyaJo1TQCWzdtwrNnGddV5dTfO/21rEHp8IED6NejF8qVLoGqtcqiTVQTHS4p4STXe5TM9hzbbjWiMSr7ldYAN7hfP16PRkSKAckFMCC9OSkMSNYYkHJffgtIDo5ywfxbT4gejaoVyul02U0HhD6/7iQ3gpIjGMmkDf6NveDp6YGm4eHYsHbti5N0BqM8kzUoff/tt+jRqTPKlCqO6kHl0W50s+e9OFb/tjlNtuO4Hq1qQFmULfU5+nTrjv0/8Ho0InqBAckFMCC9OSkMSNYYkHJffg1IIuvJ77kzZzBq2HBUKlcaFWqURLPBYRnhxaagJJMzSDCSKchlKvKSpTzQsF49rDTHzSe//JKxUwxGTuPF30o6/rtrFzq3bYtSnkVRI7iSzj6oQWmWPUEp4/qnF9ejlfYshu6dOmlgcxT+rhKRAwOSC2BAenNSGJCsMSDlvvwckByyBqXTJ45jyIABKF+6JCr5lMq47sScoMqwJhmCZ3UC+ybk5q4y1bhMOS5Tj5fwLIKQwEB8uXQpHv/4Y+ZepFvuJ+U9OeY4/o12bt+G1hHNULKEB3zqV0WnmJYaenU2Qot/+zflCEYdx7dAjZBK8CxRVK9H2/Pf3Zn7ILvD69GI6GUMSC6AAenNSXEEpB17v8fJq1f1hJ3Om5P120iePcvWgHT25k0cvXDBcvvu6MKduyYgNcvXAckha1A6eOAA+vboiTKexVHFr0zGdSezM687sTiZ/Ss6bM+cPPea1hHBbf1QslQRBPrWxMK5c/Hjo0eZW83f329+8jwomcdN69cjIrwhSpQoAr/waugS1zojKGVO6f6msl6P5lO/irbbsklTbNu8OWObpjAYEdEfYUByAQxIb06KIyDt3r9PT9iPX75MxuX795Eyd45tAamuOWZcvHtXe+2stu+Orjx4iOYtm7tFQHLIGpRkGFPX9h1QqkQxVK9dHm2jI97ouhNHMOqd1AmhnQLhWdYDvl5eSJ2ehPv37mZuhcHIVTmCkhyPvja/d2HBIShRsggCImqg66S2bxSUHMMuJWD5N/LSYNQ4tD7SVq9+/jfJYEREf4UByQUwIL05KcePHsHH77+DqlUqwsfbC941qpNR06cGShQvCq/KFTO+qxwMSAmT4/HWP//PbOMLy227K/nO333rnxg2eKB+T1bfX34lJ6OO8t/du9ChVWsd5vRF3YroMK55xsnvHwyneh6MkjshvHsdlCpXFN5Vq+gU47dv3cxslcEovzAHI/33/OnxYyxfsgT1AgNNUCqM2i180H1KO73BcN+Z1teySTCSGxfr9WgmWJUoURgN6gbr9Wi//PyztptTxzoiyv8YkFwAA9Kbe/b0Ke7fvYMvly3BgrlzjNmUxXxjw7q0zO8qZ/6W5Ds/cfwYFszj921FvvOD+/fp92T1/eV3L4JSOrZv2YzWEREalGT4kwyDkiDUPzMovZgqvDMa9w7RKcS9KldCfEyMTi3uKFbbIdfnKI8ePsSiefNQx98fnqU9ENzWHz2nddAg5LjfVj/zKMGpZ0IH1GldUyfqkGC1bPFiE7R4PRoRZQ8DkgtgQMqe9MxhGyx/XKy+t7+D5a+L1ffmTtIz70ckx7ANaWloFt4QniU94N+oOrrEt9GTX+kNaDqgvk4ZXrVieYyPHo2LF87relKs2qX8x1Ee3L+HOSkpqOXjo72IoZ0Ddbil/K30MoEppH0teJYpiiA/PyycOwc/PnqQuSaDERFlDwOSC2BAIqL8RoY7SZHpuFetWIlGoaEoZU5yazX2QlW/MqhcrgxGDR2Oc2dOaz0pPO65J0e5c/sWkhIS4PuFF8pVKa5D6cpVKo5a3jUwMzmZ16MRUY5hQHIBDEhElF/J//JL+emnx1i+eDHCw8IQOTgSJ44e1eVSeLwj4SjXrl7BpJgY1AsKwrQpU3DTnKs4itV6RERvigHJBTAgEVF+5whKpy5dwsnM64x4nCMrjrLjwAGcywxHVvWIiLKLAckFMCARkTuQctqEo8Nnz+hzqzpEMjzz/qOHmG7OS5Zu3arL+JtIRDmJAckFMCARkTuQXqSTFy/iUOZ1R1Z1iOTvZOfBg4hZsgRxy5bh1KWLusyqLhFRdjAguQAGJCJyBwxI9Fek9+jug/uYsXq1hqOJS5di2bZt+M28l87fRSLKIQxILoABiYjcgQSk4xcu4MDpU3qcs6pD7k1u37B13z6MWbgQ8cuXI9aEpPGLF+Ho+XP692O1DhHRm2JAcgEMSETkDuS49ujxj3j46CGPcfQK+Zv45ckv+P74Mew6dBArdu5A2p492L5/vwnW5/V9/t0QUU6QY4kUBiQnxoBERO5ChkmlP3tq+R6RkL8PKQfPnMblGzf0OYfXEVFOYkByAQxIREREL8hwuv2nTuLCtWt6XZJVHSKi7GJAcgEMSERERC8wIBGRnRiQXAADEhHlO1mPYfKcxzR6AwxIRGQnBiQXwIBERPnKr0/08Vnmie2z9HT89uSXl+sQ/QkGJCKy018HpOAgRM2YgaS1a5GwciXlAQlH09esQWhEU8ybmaL/NiwsLCxOXf7gpPXZs6f49fEjnJk8Bg+PH9aqNzevxeXFs/V5eqZnmZ6//ouTYNkei3uVQ2fP4PKtW5mvWFhYWHK+TBg72jog1a0TiMhJkxC/bCkmLlxIeSB20SLEL12K4EYNkTR1sk6Be//eXdy7e4eIyOncvXMbj81x6ulv1j3dEnhubVmH0zHD8dPFczg+vA8em8efLp3DuYQJxngNTw9PHMG5aRNxPjkej04d+5OQ9Bt+fPRAt2u1P5T/PHx4H3sOH8JxE5IePrhvWYeIKLvkPPvhw4eIGj4UUyfHaS56HpBuXr8GryoVUbVaFdT0rwkfXx/KI/L9ly9XGr41vNCkURgahYUSETml2rV8kZI8TX9HXg0zGb1I6c+emeATh8M9W+F62gqte3riCFxamIobG1fjRFQ/nBw9yCyLwoMjB/DzrRu6nlV7UuInTkBQgJ/l/lD+E1avLnpFDkLHrp3RMDTYsg4R0d/RpGEDVCpfBrETxunvzEs9SLUD/dEzaiRGJSVhREIC5YXEREQlTUft0BBMGD0KJ08cx7Ejh3H0yCEiIqdz6OB+XL1y6U8nXpBepEdnT+Jglwg8efhAw8/R/h1xOjYKF2cl4uLsadqDdHHOdJwaNxT3D+5Fenq6ZVuynUsXz+Ow2a7V/lD+c+LYEazftQO7vvsWJ47y95CIcpacZ8v5dv/ePREXM15z0UsBKSQ4CKNSUzFj3XqdqIFy3/TVq5Gctg6hzSKwYNZM/bdhYWFhcfbySpDJ4pmJSD/fvI6j/Trgl3t3NPxIKJLhdPf2f4eHp46ZUPQD7h/4HifHDsGlBTP+tE0W9ytHzp/DtTt3Ml+xsLCw5HyZOH4spkyK1ecvT9LAWezyHGexI6J8RyZrePgAt7au10kbZMidvL62YjEuzEzAg2MH8eDwPu1BumqWPTEh6o+G2JH7kak7OIsdEdmF03y7AAYkIsqXnj7V45ljKJ5MwuAojtnrHOWvZrEj98KARER2YkByAQxIRERELzAgEZGdGJBcAAMSERHRCwxIRGQnBiQXwIBERET0AgMSEdmJAckFMCARkbswBzdl9R6RAwMSEdmJAckFMCARkTtIN8Ho2u1buGR+e2RWO6s6RIIBiYjsxIDkAhiQiMgdyEnvsfPn9cRXilUdIsGARER2YkByAQxIROQO5KT35MWLOHTmtB7nrOoQCQYkIrITA5ILYEAiInfAgESviwGJiOzEgOQCGJCIyB0wINHrYkAiIjsxILkABiQicgcMSPS6GJCIyE4MSC6AAYmI3AEDEr0uBiQishMDkgtgQCIid8CARK+LAYmI7MSA5AIYkIgovzMHNT22nbl8GUfPndXnssyqLhEDEhHZiQHJBTAgEVF+Jcey38zjvpMnsOH777Fi5058uW0bNu7diz1Hj+DXX5/weEevYEAiIjsxILkABiQiys8cJ7vjFi5E7LJliDPGmuc7Dh7Q96zWIffGgEREdmJAcgEMSESUn6U/e4onT37Bos2bEbs0IyDNXLsWDx495DA7ssSARER2YkByAQxIRJTfSTly7qwJSEsxcckSfHPkiFnC3iOyxoBERHZiQHIBDEhEZBc50XSmsuKbb7Bg69bMV85RrL43ylsMSERkJwYkF8CARER2ePbsKa5evoRZqTOQPC1Bzcgjsu0UIzpuIqIMXT498ZV6uSU5caru08b1afo9WX1/lHcYkIjITgxILoABiYjsIGXblk1451//gJ+fDwIC/FCrVt7x96uJsLD6aNS4oXnuY5b5vlIntwQFBaCYRyGE1g3S74nHXOfCgEREdmJAcgEMSERkBynbNm9CpQplcfTiRZy7eQunzQlnnrl+HSevXsXJK1f0uWWdXHLjp58xJmYCGgQzIDkjBiQishMDkgtgQCIiO0iRgFSxfBlzsnkKxy9dwpHz58m4ePceosaMRlhIHf2eeMx1LgxIRGQnBiQXwIBERHaQ4ghI+06exLGLF3H43DkyLty5y4DkxBiQiMhODEgugAGJiOwghQHJGgOSc2NAIiI75V5AMif5SWvXIjktTU/4sy7Xxy+/xNQVK8z76zB9zZoX7/8Nk02b01evxox167RtqzqugAGJiOwghQHJGgOSc2NAIiI75UpAkhP8+KVL0Xf0aCNanztO+iUMJaxcqQEmdtEi9B4VhQETxmu4eSlIZYO0O2RSPLoNHYKJpm1XDUkMSERkBykMSNYYkJwbAxIR2SlXApIElUkmFH1Rwwsen36EUTOSkbpxE3qOHIEa3l6IjI/HzE2bzGMcPnn3LdQNrYfElV8bK3VdR4DK2t7Ur1bosoSsy+W11M9clpy2HkGhIfjorX9ipPkMSWlpmeu+HLxeWi/zPamTdbt/9DpjvZUvesKytmdkXZ5dDEhEZAcpDEjWGJCcGwMSEdkpVwKSSF67Fo1btUDB999BP/OjI0Pt6pgg9P4//hdN27XRwNRl0EB8+t5b6DSgP2asX4/Jy5drr5JwBBJpK3bxYn0tvUzynoQQ2b9Jy5Zh4sIF+pj49SoNSPUahaNIgQ8xOjVV141bsljbkfWn/CdzPbMdWU96tuS1hC/HtmWZtJ/1tQQgCSxxS5aY9RZm1JHPmbkfUtexXOplbOvV7+R1MSARkR2kMCBZY0BybgxIRGSnXAtIcv1Rl8GD4GHCSqtuXTXkVKpYHp8XKYQaPjU0BDRs0RzFixRE5KR4jJ01C74BfihbuqSq2yAU4+fO1f2o6V8T9Zs0gp953y+wlgalXlEj4eVVDaU+L4Zq1aqgT3S0hq7Qxg1RrGABhDVriiqVK6J82dLo0K+vhqRE05asJz1bsl7VqpV0HyW8DZ00CeXLlNLwJtcwyVC9Mp6fo1nH9hqgWnfvZtqrgNIlP9fPMTh2IlI3bEC/sWPhbT5PqRKfoXKlCug+bMjzYJddDEhEZAcpDEjWGJCcGwMSEdkp1wKSrD9symQNQBJa5DqjcmU8Ed48woSM4hg2dQpqBQWgTKkS2pszOjUFnQb0Q1TSdO1RkmAV0b6tTrogAajwR+8jJKwBolNmIDIuDiWKFUGDpo0xOiUFAUGBKG3CjPTwhJn2C334LurWr4eBZpvVTYgqUbQwxsyciZGmbVlPhvlJwAmsG6S9TYPjYs2+TtFg1SCiCVLWr8egiTEo8vEHug/9x4/TnrDgsPo6XLDLoAH6OHpmqgYjCXPRZj/qNQxHSdP+iIQETDP7bfW9vA4GJCKygxQGJGsMSM6NAYmI7JRrAUl6UWSIWsUKZeHt6436jRvBx9dHg5H0EEnvkfTw1PSracJAxhA46d1p1KoFagfXwWeFPzWBI0zbkYAk68SbADRryxY079geRQt+jIA6tbW+1xfVUOCdf2FUcrK2W9gEG7kGacHu3WjRuSM+fvufGoDa9+ltgs7b6DF8GObt3KVBS0JRo9YtMWTSJA1SEuAkIEmAkveadWivYanopx9rD5H0OE2YNxczN21Gh759NLj5B9ZCY9OGj/mcck1VzxEjtFfK6nt5HQxIRGQHKQxI1hiQnBsDEhHZKdcCkkxuICf6MmlCyc88ULKYh4YIGXonw+Skp+Vzj8KIaNdWw0SLTh01FPkH+psw1RCexYvq9UQZAamyBq2ppl2pG96imYaXALOv0oskw+matG2NuCVLzesm2iskYWn21q1o2aWTCS3/xvDEBH3+qQlIg2ImaMAZkTgNnmbfpA3tlTIBqWHL5kjduFGH2Mk2GrZsob1BEt58/X1R0uyX9ID1GzsGbXv2QKEP3tWAJD1P0o4M0ZNwJgHH6nt5HQxIRGQHKQxI1hiQnBsDEhHZKfcCkjnJT1qzRkNJoQ/fQ3GPghoyJLS07t4VRT/5SHtlpDdHhtFV96qqP9rJ69IwZtYsDSIh4Y4epMqoYN6TyRBkZrqO/fqi0EfvoU3P7pi7Y6dpc5vWk3sqOSZpiEpK0m1JD5IEJOlB6jVyBAqaQNOiUwfM2b4dXSMjdeictCPvS0ALNeunbNiAjv37al0JdTKpw6Tly3S5DBWU/a5TPwS9RkWh8Mfvo2nbNrqtudt36H5YfR9vggGJiOwghQHJGgOSc2NAIiI75VpAEtLb0yc6CgXe+bdOiiCTLkiIiYyL1et7pIdGrtdJXrcOYRFNdEpw31q+8Avwx+cehVAnNEQDR/mynhqYJKhMW7UaMfPno6apJ9c3yRA9mbwhJLyBTr8t1wN9+K9/YOS0aZizbZsJL63xzv/+jwYbCR5+gf7aoyW9PqVLfKbBbMK8eYhdvEifFytUQNv0rx1gQl0hHbInvUtyLZNcsyTvFTdBqn3vXvoZg0KDzTqfwLumt7YZGFzHfM45OmX577+P18WARER2kMKAZI0BybkxIBGRnXI1IEm4GTt7Npp36qATLziWyWQKrbt1RZse3XV6bNmWhJ62vXqYQNIMA2Mm6D2TegwbZsLCCrTr3VNnkXPcTFbCg0zsINOEy3A7uQ6pT/QoXS7rNWnTWkOPBDQJRtJm9IwZ+jpmwQKd1U6GxLXp0Q3jJMyY9WS/JFQ169hBh+uNSk5G92FD0du0Kzed7di/n16f1KhlC+0J07C2erV+FrkxrQQpGZ4nPWLynuzn77+P18WARER2kMKAZI0BybkxIBGRnXI1IE0xgUbuIST3OJJw4lgmAUCm0hbyXIKPBBTpSZK6EjzkWqXpa9boOtLrJHWzti31k9amaX0hw/SkbVlHhsLJNVDSrrSVsmGj1n++HbMvMhGDtCs3qHW0KZ9Z21u3XgOK7oNZX/ZRnju2Jc81AEl7ZjtZ33Ps89/BgEREdpDCgGSNAcm5MSARkZ1yNyBRtjAgEZEdpDAgWWNAcm4MSERkJwYkF8CARER2kMKAZI0BybkxIBGRnZwqIMnwNNmODGOTRxkWZ1XP3TAgEZEdpGQ3IB29cAGnr13H6evXcfLqVRw5f96y3h87q9s7cfkyDp09a/H+q2QbUl+e2x3mGJCcGwMSEdnJaQKStv/llzoZwtApkxGdMkOXSzD4fV3bmO3LNUhy7ZAzhTMGJCKyg5TsBCQJKnuPHcNXaWuxYPkyrN2y2Sy7oMuljWOXLj0PTEfN6+NZXjvel8ddP/yAjbt24rgJPc/rm+Alz3+/njzKPm7//nutI9vP2qajrq5r3pdl8iiytvO6GJCcGwMSEdnJKQKStD1qRjICzbZKl/wcpUp8htKen6NO/XoYP2fO821LUNB1zOPz578jy195L/P1S8sz62VdpvthAprc3HWc2a5M4PD7+s9fZ1kuj5bv5RBpmwGJiHKalOwEpNPmpHSGOUY2bhyOydMS0K1HN0xKTMDZmzfx7eHD2LE3I8RIb88PJ05gy55v8MPx4/r6m4MHscOEnFOmjZXr12PWwgXapvQiyTr7TH0JM3uPH8PWb/foe/L65JWrSNu2DT379MK67dsxPGqEtnXiyhV8d+QItn/3na4v9Q+eOYOde/fikHn84cRxfX4k873X9fuAJCfh6c+ekpOQcuD0KQYkIrJFngckCSGxixbhC28vFCv4CboOiUTs4sXo0Le33jw2oE5tvSlrwsqvdR9eojPKrcjs+Vmpr7O+L+1LT5CjrjxK2JBt/r6u1JOZ8Zp16gAPubGs+cxyY1up/1Jd81x7tTJnrHMs0zZsCkkMSERkBynZDUgJSUkmQETjsWlj5rx56GWCy+pNG9G3f18MNsfx1PlztYeotzmW9xvQHyvWpZlAtA59zPuDzPsLvlyO+UuXYtTY0ZicmIjFX/1H2x48bChWpKWh/6BBGDw0EnFTJ2u4kUC1bvs29OnXxyybgjq1A7DMHBfXbduKvqZ9xzZlG33790PksCHo3rO7tt+hYwekzJ2jbfz+s/wRCUijxo5BWGgwHv/yMx48eoj7Dx+Qk3j002PsPnwI569eZUAiohyX5wFJpsHuPnQICn/0vt7DSKbUlmuQZOrt4PAG8PjkQwyOi9UepgCzLz1HDEdg3Tp6o9Z2vXrqVN3TV63GuDmz0aR1S1SrXgU+Nb21nkwT3md0NELC6qPzoIGo4VMD/caMxjDz4yo3ea1SpRJq+tfUexVN+c9XaNahHcp4fo4SxYqgUsVyulxCUo/hQ/Wmr1WrVtJ7H42ZNVOH4XUeOAANTGhpb04M5Mawg2Mnaliy+px/BwMSEdlBSnYDUsrcuWhujtkSRtqbY+e2b/doEBoRHYWUOXPQuk0rDIwchARz7L5w9y5OXrmiPU3y/vSZqWjTthXmL1umIeirtWsw3hw//2MeJ06K1+c9evUwAWglwsJCsWn3Lpy7dUt7kGR763dsx7iJMbhw+w4GDh5owtQAzF600LTZGokpyejZu5fuZzuzX0tWfIX127drnTM3brzyWf7IhTt3MGb8OIQ3DscPp09jz9Ej+OYIOYs9xvb9+3HnwT3tUbL6+yYiyq48D0hyz6Bm7duhyMcf6M1j5bUuN8FEbh4ryyXcDE+cikImREmoad6xvfYsyXtdzI/j9NWrEBAUiArlymgPVL2GYRpyhk6eZMLXUO0RkuDTyASoMeaHudfIEWjatg16R0VpUCpW6BMMjInR8FSujCdKfuahN4cdM3MmekWNMO8XQK2gALTo0gklixeFt6+39h616tpF96Fc6ZJo0bkTxs2e/fKwvBzCgEREdpCS3YCUOGMGRkaPwq4f9qJT547Ye+yo9iJJD9HM+fMwf+kS9BvYH6nz5uHGTz9pOOlo6vXu1wfJc2Zhnnl/4ZfL0X/gAL1GaKQJTkNHDNNeorExEzR0pc6biyRzzN5z6BDOXL+hAalPv77aUyVB69K9e9qj1KVbF6SawCZtzl64AENMO3KdkwS2tVu2Yve+fYgcNlQnlLD6PFayDrFLT0/X7+u3X5+QE5HfQf4WEpEdnCIgRbRriyIFPkBH82PmuLGq9CK16dFdA0hH84M4cvo0fPre2xpy5u3apeGluEchDUpDJ09G8SIF4VvLT3t9mrRphYIfvKsBq9fIkfD45CM0NdtI2bhR25+0fLkJRBPQ3fxg1msUjgLv/NsErUGYu3MXanh7wdOEILkGSer7166Fzwp/guiUFMzdsUOD1afvv6Prd+jbW3u+OvTtg5kbNz0fevf7z/h3MSARkR2kZHuInUyoY4LIzZ9/RqxMrDNuLJasXIEBgwfqdUmrNmwwgWarhqfocWOwdOVK7c2RHp8p5ni+yoQcGVbX2xw/rz76EbGTJ6FL1866D2u3bNGeosnTEjFvyRK9tujU1atYu3WrXoMk1xS1bddGA5FMFCG9Q/EJU83zNA1dAyMH67A8aXuVOY5L/cFDh2Q7IElJl5Nx852Rc7H6uyYi+rucIiBpT4wJGu1699JhcbJchtg169jeBKT3NfSMnJYRkGQY3KwtW/W6pYoVysLH10fDTXGPgpmvveHt8wX8AvzRJ3oUegwbhmIFC5gQ01fblLbDmkegZLEiqFa1Mry+qKYBStpI2bARXl5VNSCNMj/+k80PbbVqVVChbGm9Lmrmpk3oPGAACmfuU/s+vXUIYO9RUSZ45fzQOgcGJCKyg5TsBCSZNEEmSNj5w17t/dlv1t2wY4euL8PZpPdIJk2QULNp926d6U4mZpDpwNNMyJEQI69lJjqpJ709MrmDDNOTNmRWu617vsGCZcuwYedO3Z4EHpnAYdt332qdzf/djdXmmCwTP2zatQvzly3VdaRNCUSyn9K2TBJx4PTpN56ogbPYERG5rzwPSNNWrcagiTEo+ulH8PGrqdcUzdqyBXEmkFQ3YUWGu8nQteFTp2hAapzZgyTTgH9WpCBqB9fB8ISpZv0CqNsgFKkbN2LOtm0meKUhyQSirib4SECS8JWyfoNOviDr1W1QD3NlXPq4sdrb1GXQwIyAZAKTbFN6qFLNiYP0UMn6UclJmLN9Bxq1amnqv6PXG2lAKvChXu8kPV5Wny8nMCARkR2kZCcgCQ0ylzLuYaQz1l25kjnb3BUdDifBSerJcum5kRAkryUkOV47ZrqTNqS9E5ev4HDmPZHkudRz3PdISPuO17IdoXWzbFPalICV0cZlDUWyni57zfstCQYkIiL3lecBSU7+E1au0J4hCRu+Af5o1a0Lavh8YULPx2jbswdSTXCJjI/T1xXMD3njNq2050h6froNidTrlYLDQvX9OqEheq1QcIP6OkW4vC/BqnX3bjqxgiwrX7Y0ypcrrdN5Szufvv82Ovbvi1mbN6N+k0Yo9OF7qFMvWHuR+o4drb1T0jPVsGVzvbZJht1JYGnZpTMKvP0vnWSCAYmIXI2U7Aak/I4BiYjIfeV5QBIysYGEAJk8oW79UJ1tLiS8gc5Al7BiJZLT1iEyLk6v96kdUhdhzZqipr+vziInPU6JX69C7OJFOqudf6A/vGvWQMMWzbQXalDsRNQKCtRhcInmM0jQkF6jgLpB2jvUK2okGjRtjL5mWzKD3ujUVJ2pTtroOWKEDgGU9yR4ybKI9u0wfu5cHQoow+xkdjudvc60a/XZcgIDEhHZQQoDkjUGJCIi9+UUAUnIfYikF0Z6g5LWrNVHeS3hQF5HxsZqb01Eh3aYs327BpfpqzPuU6T3JDIhSyZg0HXlPfNc3pPl8lruk+SYQEE+iyyTujItt9SVehK2tH5mG/Jc6+t+vWjXUVdCS9Z6dmFAIiI7SGFAssaARETkvpwmIP0ZDUjx8Tr0TQKSDJWzqpdfMSARkR2kMCBZY0AiInJfLhGQJCDEL12qU23HLFiQ0WtkUS+/YkAiIjtIYUCyxoBEROS+XCIgCQkJsg92D2dzRgxIRGQHKQxI1hiQiIjcl8sEJHfGgEREdpDCgGSNAYmIyH0xILkABiQisoMUBiRrDEhERO6LAckFMCARkR2kMCBZY0AiInJfDEgugAGJiOwghQHJGgMSEZH7YkByAQxIRGQHKQxI1hiQiIjcFwOSC2BAIiI7SGFAssaARETkvhiQXAADEhHZQQoDkjUGJCIi98WA5AIYkIjIDlIYkKwxIBERuS8GJBfAgEREdpDCgGSNAYmIyH0xILkABiQisoMUBiRrDEhERO6LAckFMCARkR2kbNu0CZUqlMXJq9dw6d49nL99m4y7vz3F+NiJaBAcpN8Tj7lERO6DAckFMCARkR2kbN28ER6FPkF8YgISU2ZganISGanz56Fxk0YIrVNbvycec4mI3AcDkgtgQCIiO6Snp2P/vr2oVdMbft5e8Kfn/GpUR41qVTB00ED9nnjMJSJyHwxILoABiYjslP7sKf0BHmuJiNwPA5ILYEAiIrvIscQqGNALVt8bERHlXwxILoABiYiIiIgodzAguQAGJCIiIiKi3MGA5AIYkIiIiIiIcgcDkgtgQCIiIiIiyh0MSC6AAYmIiIiIKHcwILkABiQiIiIiotzBgOQCGJCIiIiIiHIHA5ILYEAiIiIiIsodDEgugAGJiIiIiCh3/GVACgkOQnRqKmasX29C0mrKA9NXr0HyunUIbRaBBbNn6r8NCwsLCwsLCwsLC4t9ZeL4sa8GpJvXr8HP1xtdhw/HiOnTMGTqFMoDQ6dOxfBpifCrG4Rxo0bi5IkTOH70CI4dPUxERERERDlIzrNPnjiOPj27YcK40ZqLXvQg3byB4KAA1KldC2H1QxAWSnklvH49BPj5oK75t2gS3gCNGoQSEREREZENGofVh2+N6pgzK0VzkQYk8duvT3D3zi3cu3sb9+/dxf27dyivmO//7u1buGPIv8fdO0REREREZId7xp3bN/HLzz9pLnoekAQLCwsLCwsLCwsLC4s7lvRnT18NSERERERERO7rV/w/L6mG3bYljEEAAAAASUVORK5CYII=)

