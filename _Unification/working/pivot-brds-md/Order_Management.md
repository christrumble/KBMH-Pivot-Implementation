# Pivot BRD — Order Management

_Source: `Order Management/Pivot/4 BRD/05_Pivot Interiors BRD Order Processing_v2.0.docx`_

---

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation__

__Order Management Area__

__Prepared for: Pivot Interiors, Inc\.__

__Version 1\.0__

__Date: September 15, 2025__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

# <a id="_Toc208925516"></a>__Table of Contents__

[Table of Contents	2](#_Toc208925516)

[1 Version Control	3](#_Toc208925517)

[2 Project Definition	3](#_Toc208925518)

[2\.01 Executive Summary	3](#_Toc208925519)

[2\.02 Company Overview	3](#_Toc208925520)

[2\.03 Orion/NetSuite Overview	4](#_Toc208925521)

[2\.04 Project Overview	4](#_Toc208925522)

[2\.05 Document Objectives	5](#_Toc208925523)

[3 Order Management Process Area	5](#_Toc208925524)

[Invoice Schedules and Deposits	5](#_Toc208925525)

[Quote Approval Workflows	7](#_Toc208925526)

[SIF Import & BOM Processing	9](#_Toc208925527)

[Smart Table Grouping	12](#_Toc208925528)

[Deposit and Pre\-Payment Management	14](#_Toc208925529)

[PDF Composer	16](#_Toc208925530)

[Client Quote Approval	18](#_Toc208925531)

[Budget Setting at Sales Order Conversion	20](#_Toc208925532)

[Pro Forma Invoice Management	22](#_Toc208925533)

[Purchase Order Generation	24](#_Toc208925534)

[Miller\-Knoll Order Manager Integration	26](#_Toc208925535)

[Acknowledgements	28](#_Toc208925536)

[4 Implementation Timeline and Next Steps	29](#_Toc208925537)

[5 Signatures	30](#_Toc208925538)

<a id="_heading=h.30j0zll"></a># <a id="_heading=h.1fob9te"></a>

# <a id="_Hlk208907748"></a>

# <a id="_Toc208925517"></a>__1 Version Control__

__Version__

__Author__

__Comments__

__Date__

1\.0

Marcus Dallacqua, Chris Trumble, Debbie Herbert

Initial Draft

09/15/2025

2\.0

Gary Strickland

Ready for client signature

02/04/2026

# <a id="_heading=h.2et92p0"></a>

# <a id="_heading=h.tyjcwt"></a>

# <a id="_Toc208925518"></a>__2 Project Definition__

## <a id="_Toc208925519"></a>__2\.01 Executive Summary__

Pivot Interiors requires order management transformation to address critical operational bottlenecks including lengthy import processing, inability to modify orders post\-creation, and fragmented deposit tracking\. These constraints directly impact customer satisfaction and business growth\.

The NetSuite Orion solution provides a unified platform designed for commercial furniture operations\. Analysis shows that 91% of Pivot's requirements align with standard functionality, minimizing customization needs and implementation risk\.

Implementation follows a phased approach with Phase 1 covering core order management, quote processing, and purchase order automation\. This strategy maintains business continuity while delivering immediate operational improvements through systematic workflows and enhanced visibility\.

## <a id="_Toc208925520"></a>__2\.02 Company Overview__

Pivot Interiors, Inc\. comprises a distinguished team of innovators, creators, and thought leaders dedicated to crafting exceptional interior solutions for businesses of all sizes\. Pivot’s designs not only embody your brand but also inspire employees to thrive, create, and collaborate in the workplace\. California\-born and raised, we are proudly headquartered in the Bay Area, serving clients state\-wide\. With offices and Design Centers in Santa Clara, Fremont, San Francisco, Costa Mesa, Los Angeles, and La Mirada, Pivot invites you to explore our spaces and experience the Pivot Interiors difference\. Pivot Interiors is a MillerKnoll Certified Dealer\.

[__https://www\.pivotinteriors\.com__](https://www.pivotinteriors.com/)

## <a id="_Toc208925521"></a>__2\.03 NetSuite Orion Overview__

NetSuite Orion provides a comprehensive order management solution designed to eliminate the manual processes and system fragmentations that create bottlenecks in commercial furniture operations\. The solution includes integrated quote\-to\-cash workflows with configurable approval rules, automated document generation, and systematic deposit tracking that ensures orders flow efficiently from initial quote through final delivery\.

The order processing capabilities within NetSuite Orion enable automated workflow routing with real\-time visibility into approval status, eliminating the email\-based tracking currently required between stakeholders\. Scheduled invoicing functionality provides complete deposit visibility at quote, sales order, and project levels, while integrated purchase order automation handles vendor splitting, acknowledgment processing, and transmission through appropriate channels\. The solution's financial management functionality seamlessly connects order processing to accounts receivable workflows, maintaining clean financials while providing operational teams with the visibility needed for effective project management\.

## <a id="_Toc208925522"></a>__2\.04 Project Overview__

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

## <a id="_Toc208925523"></a>__2\.05 Document Objectives__

The purpose of this document is to summarize functional and procedural requirements captured by GSI during the Discover business process mapping phase of the implementation\. 

This Business Requirements Document \(BRD\) documents your goals, the problems you want to solve, and the outcomes you expect\. It is the foundation for the setup of the system, acting as a __roadmap between your business needs and the solution design\.__

This document represents information gathered in meetings held with the Client, which enables the GSI team to map the business requirements to an efficient flow in the NetSuite Orion application\. Once complete, this document will serve as a blueprint for the GSI team to configure the application\. This document remains consistent in structure to those discovery sessions as it categorizes the findings into the same key process areas\. The set of business requirements documentation is inclusive of all business requirements provided by the Client\.

# <a id="_Toc208925524"></a>__3 Order Management Process Area__

## <a id="_Toc208925525"></a>Invoice Schedules and Deposits

__1\. Your Business Requirements__

- Support complex invoice scheduling including 50/40/10, 30/40/30, and custom variations
- Support 100% prepay scenarios for specific customer requirements
- Provide deposit visibility at both quote and sales order levels for complete project financial tracking
- Handle scenarios where deposit amounts are collected at different timing than project completion
- Generate pro forma invoices without GL impact for deposit tracking
- Enable flexible modification of payment structures to accommodate customer negotiations
- Create up to 5 standard invoice schedule templates for common billing patterns

__2\. Current State Process__

Invoice scheduling currently requires extensive manual management with deposits tracked only at the project level, creating visibility gaps at the sales order level\. The system uses two separate fields for payment terms \- days and discount percentage \- requiring manual calculation for complex schedules\. When deposits are collected but project timing varies, manual tracking and reconciliation is required\. Pro forma invoices must be created manually with limited information, and deposit structures cannot be modified after quote conversion, forcing cancellation and recreation of orders when changes are needed\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides sophisticated invoice scheduling capabilities specifically designed for complex commercial furniture projects where payment timing rarely aligns with delivery or installation – approval workflow can be created if needed\. The solution includes a comprehensive invoice schedule tool that supports unlimited billing structures, with templates for common patterns like 50/40/10 and 30/40/30 while maintaining flexibility for custom arrangements including 100% prepay scenarios\. This functionality is standard within NetSuite Orion and has been refined through implementations at hundreds of furniture dealers facing similar billing complexity\.

The solution's deposit management framework provides complete visibility at quote, sales order, and project levels, ensuring all stakeholders can track financial obligations throughout the project lifecycle\. Pro forma invoices generate with full project details while remaining outside the GL until payment is received\. The system handles various deposit collection and project timing scenarios, maintaining clean financials while providing clear tracking for accounting teams\. Orion PDF composer will provide line level detail and summary\.  This approach eliminates the manual reconciliation burden while ensuring compliance with accounting standards\.  Custom reporting via saved search is for Invoice Amount vs\. Payment Received\.

__4\. Future State Process__

Invoice scheduling will be managed through configured invoice schedules that generate billing milestones based on project parameters\. When negotiating with customers, sales teams will select from standard templates or create custom schedules that flow seamlessly from quote to sales order\. Deposits will be visible at all levels with clear tracking of collected amounts\. Pro forma invoices will generate with complete information, and payment application will trigger appropriate processes based on configured rules\. Finance teams will have real\-time visibility to deposit positions through automated dashboards\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Invoice scheduling

Invoice schedule templates

Automated billing milestones

✓ Validated

100% prepay support

Flexible schedule configuration

Complete prepay capability

✓ Validated

Deposit visibility

Multi\-level deposit tracking

Complete financial visibility

✓ Validated

Pro forma invoices

Non\-GL invoice generation

Proper deposit tracking

✓ Validated

Up to 5 standard templates

Template library

Standardized billing

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your deposit management will adapt from project\-only to comprehensive tracking

- Deposits will be visible at quote and sales order levels
- Variance tracking will be available in the system rather than spreadsheets

__ALIGN__: Your invoice scheduling requirements align with NetSuite Orion's invoice schedule functionality

- Standard templates will be created for 50/40/10 and 30/40/30 structures
- Pro forma invoice generation will use standard functionality
- Deposit tracking will utilize native multi\-level visibility

__7\. Implementation Considerations__

- Up to 5 standard billing templates must be defined during configuration
- Training required for finance team on new processes

## <a id="_Toc208925526"></a>Quote Approval Workflows

__1\. Your Business Requirements__

- Implement automated approval routing for up to 10 business rules including margin and dollar thresholds
- Enforce margin\-based approvals and dollar amount thresholds for management oversight
- Provide systematic workflow tracking with full audit trails for compliance
- Replace manual email and Workfront routing with integrated approval system
- Enable real\-time visibility to approval status for improved customer communication

__2\. Current State Process__

Quote approvals currently rely on manual email routing and limited Workfront system tracking, creating delays and visibility gaps\. The business rules include critical thresholds that require management approval, but the manual process lacks systematic workflow tracking, making it difficult to identify bottlenecks or ensure compliance\. Sales teams cannot see real\-time approval status, leading to delayed customer communications and lost opportunities when approvals stall in email inboxes\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides comprehensive quote approval automation through its Order Approval Rules module, designed specifically for complex commercial furniture quoting scenarios\. The solution supports unlimited approval rules with sophisticated routing logic based on any combination of criteria including margin percentages, dollar amounts, customer types, product categories, and sales territories\. This isn't generic workflow software but purpose\-built functionality refined through hundreds of furniture dealer implementations where margin protection and deal size oversight are critical to profitability\.

The system's approval framework evaluates each quote against configured rules upon user submission, routing to appropriate approvers through system notifications rather than emails that can be overlooked\. Real\-time dashboards show approval queues, aging, and bottlenecks, while mobile capabilities enable executives to approve from anywhere\. Every approval decision is tracked with timestamp, approver, and notes, creating comprehensive audit trails that satisfy both internal controls and external compliance requirements\.

__4\. Future State Process__

Quote approval will trigger when the user hits the Submit for Approval button, with the system evaluating all configured rules simultaneously\. Quotes will route appropriate approval queues based on configured business rules, and approvers will receive system notifications with mobile approval capability – user or role\-based approvers and set up permissions to override approvers\. Sales teams will see real\-time status updates displayed on the dashboard reminders; this will allow leadership to see unapproved PTO\. The entire approval history will be maintained for compliance and process improvement analysis, with metrics tracking approval cycle times and bottleneck identification\.

Approval rules to be created for automating smaller order amounts

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Up to 10 approval rules

Unlimited rule configuration

Complete coverage

✓ Validated

Audit trails

Complete approval tracking

Compliance ready

✓ Validated

Real\-time visibility

Live status dashboards

Improved communication

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your manual approval communication will adapt to systematic workflow

- Email\-based approvals will transition to system notifications
- Manual tracking will be replaced with automated dashboards
- Email alert \(via saved search\) approvals for users if needed

__ALIGN__: Your approval tracking requirements align with standard audit capabilities

- System notifications will replace email routing
- Mobile approval will be enabled for executives
- Audit trails will capture all approval actions

__ACCOMMODATE__: Your specific approval rules will be accommodated through custom configuration

- Up to 10 business rules will be configured with specific thresholds and routing \(example rules will be more clearly defined during the design process\)
- Additional rules will be configured based on complete list from Sales Coordination

__7\. Implementation Considerations__

- Complete list of approval rules needed from Sales Coordination team \(outstanding item\)
- Approval hierarchy and delegation rules must be defined
- Training required for approvers on new system workflows

## <a id="_Toc208925527"></a>SIF Import & BOM Processing

__1\. Your Business Requirements__

- Process up to 1,000\+ line imports in under 15 seconds to eliminate current 30\+ minute delays
- Handle complex BOMs from CAP Studio with full line relationship preservation
- Provide exception handling for incomplete items without failing entire import
- Eliminate redundant tax calculations that currently occur on every save
- Support files up to 1,000\+ lines \(demonstrated requirement\)
- Maintain product groupings and configuration relationships from source systems

__2\. Current State Process__

SIF file imports represent a critical bottleneck with large orders taking 30\+ minutes in D365, primarily due to Avalara tax calculations reprocessing the entire order on each save\. Files from CAP Studio with 1,500\+ lines frequently timeout or fail completely, requiring manual re\-entry or multiple attempts\. The system cannot handle exceptions gracefully \- a single problematic line can fail an entire import\. This performance crisis directly impacts quote turnaround times and sales team productivity, with staff sometimes spending hours on a single import that should take minutes\.

__3\. NetSuite Orion Solution__

NetSuite Orion's SIF import capability represents a significant performance improvement, with live demonstration during discovery showing 1,000 lines imported in approximately 10 seconds \- representing a dramatic improvement over current state\. This is demonstrated functionality actively used by major furniture dealers processing thousands of complex quotes daily\. The solution's architecture processes imports in optimized batches with intelligent caching that eliminates redundant tax calculations, addressing the root cause of current performance issues\.

The system's advanced exception handling ensures problematic lines are flagged for review while successfully importing all valid items, eliminating the all\-or\-nothing failures that plague current processes\. Line relationships, product groupings, and configuration hierarchies from CAP Studio are preserved through sophisticated mapping that maintains the integrity of complex BOMs\. Tax calculations occur on summary lines rather than individual transaction lines \- instead of having a thousand transaction lines, there might only be five summary lines, enabling very fast processing\. These summary lines are broken out for intelligent taxation so products will be taxed differently than labor\.

__4\. Future State Process__

SIF imports will complete in seconds rather than minutes, with sales teams able to import, review, and quote even the largest projects efficiently\. Exception views will immediately highlight any items requiring attention while the valid majority processes successfully\. Tax calculation will occur on NetSuite summary lines, providing significant performance benefits\. Real\-time progress indicators will show import status, and successful imports will maintain all CAP Studio relationships and groupings, ready for immediate pricing and margin analysis\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

1,000 lines in 10 seconds

Demonstrated performance

Dramatic time reduction

✓ Validated

Exception handling

Partial import success\.

Note:  provide training on Orion approach prior to UAT

No complete failures

✓ Validated

Relationship preservation

CAP Studio mapping

Configuration integrity

✓ Validated

Optimized tax calculation

Summary line processing

Eliminate redundancy

✓ Validated

Large file support

No practical limit

Scale ready

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your tax calculation process will adapt to optimized architecture

- Tax calculations will occur on summary lines rather than individual transaction lines
- Batch optimization will be implemented
- Caching strategies will eliminate redundancy

__ALIGN__: Your legacy SIF import requirements align with demonstrated capabilities\.  For Expanded CAPSIF, additional mapping will be required

- Standard import tool will be configured for CAP Studio format
- Exception handling will use native functionality
- Performance targets already demonstrated in testing

__7\. Implementation Considerations__

- CAP Studio file format mapping must be validated
- Tax calculation rules need configuration for summary line processing
- Performance benchmarks should be established for monitoring
- Training needed on exception view procedures\.  If additional views are required, custom reporting will be created by GSI\.

## <a id="_Toc208925528"></a>Smart Table Grouping

__1\. Your Business Requirements__

- Enable custom grouping functionality within Smart Table for efficient order management
- Support grouping by aliases, tags, and other custom criteria for project organization
- Provide filtering and sorting capabilities to manage complex orders with 1000\+ lines
- Implement multi\-grouping structure supporting different grouping methods for PO creation and invoicing workflows
- Enable bulk editing and mass updates across grouped line items
- Support complex project phasing through systematic line organization and group management

__2\. Current State Process__

Current order management lacks sophisticated grouping capabilities for large, complex projects\. When orders require phasing or specific vendor splitting, manual processes are required to break up specifications into appropriate sections\. The Operations team always start sales orders from scratch for accurate phasing on large orders, creating time\-consuming manual processes\. The lack of systematic grouping makes it difficult to manage projects with hundreds or thousands of line items efficiently\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides advanced Smart Table functionality designed specifically for managing complex commercial furniture orders with sophisticated grouping and filtering capabilities\. The solution enables users to filter, sort, select, and edit any combination of line items via Orion’s Smart Table, then create custom groups based on various criteria including aliases, tags, vendors, or any other field\. The system supports multi\-grouping architecture where different grouping methods can be used for purchase order creation versus invoicing workflows, with additional grouping capabilities for other processes\.

The system's grouping capabilities support complex project phasing by allowing project managers to select specific line combinations and assign them to named groups \(such as "First Floor" or "Phase 1"\)\. These groups can then be used for PO splitting functionality, creating separate purchase orders based on group definitions while maintaining project relationships – including sales orders\. The multi\-grouping approach recognizes that PO creation grouping requirements often differ from invoicing grouping needs, providing flexibility for different workflow requirements\.

__4\. Future State Process__

Complex orders will be managed through Smart Table filtering and sorting to identify specific line combinations for grouping\. The Operations team will create named groups based on project phases, installation sequences, or vendor requirements using one grouping method for purchase orders and potentially different grouping methods for invoicing workflows\. Groups will drive PO splitting, creating separate purchase orders while maintaining project relationships\. The multi\-grouping structure will support different organizational needs across procurement, invoicing, and other operational processes\. Bulk editing capabilities will allow mass updates across grouped items when modifications are needed\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Custom grouping

Smart Table group functionality

Lock down of certain columns required

Project organization

✓ Validated

Multiple criteria

Alias, tag, vendor grouping

Complete flexibility

✓ Validated

Multi\-grouping support

Different methods per workflow

Optimized processes

✓ Validated

Bulk editing

Mass update capabilities

Efficiency improvement

✓ Validated

Complex phasing

Systematic organization

Eliminate manual work

✓ Validated

__6\. Implementation Approach__

__ALIGN__: Your grouping requirements align with Smart Table standard functionality

- Custom group creation will use native capabilities, including PO creation
- Filtering and sorting will utilize standard table functions
- Multi\-grouping architecture will support different workflow needs

__7\. Implementation Considerations__

- Smart Table training will be critical for user adoption and efficiency
- Grouping naming conventions need establishment for consistency
- Multi\-grouping structure requires clear definition of workflow\-specific needs
- Integration with existing project management processes requires definition
- Change management support needed for new workflow adoption

## <a id="_Toc208925529"></a>Deposit and Pre\-Payment Management

__1\. Your Business Requirements__

- Enable quote\-level deposit creation and tracking before sales order conversion via link\.  Payment processing gateway decision needed\.
- Support vendor pre\-payment capture for draft purchase orders
- Provide automatic association of deposits with sales orders upon conversion
- Support deposit and pre\-payment application to invoices and vendor bills without manual intervention
- Implement deposit visibility at quote, sales order, and project levels
- Create systematic workflow from deposit request through payment application

__2\. Current State Process__

Quote deposits currently present challenges as most systems only support deposits at the sales order level, not at the quote stage\. When deposits are collected before order conversion, manual tracking and association is required\. The current process involves creating deposit requests through Compass, manual processing by the Accounting team, and complex reconciliation when applying deposits to final invoices\. Similarly, vendor pre\-payments are difficult to manage without systematic tracking capabilities\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides advanced deposit and pre\-payment capabilities through customized functionality that addresses both customer and vendor scenarios\. The Quote Deposit functionality simply allows taking a deposit towards a future sales order from the Quote Record, which NetSuite doesn't natively support\. On the pre\-payment side, since we have draft purchase orders, we're able to capture a pre\-payment for that future purchase order\. In both cases, those deposits and pre\-payments are automatically applied to either the customer invoice or the vendor bill\.

The system's deposit management provides multi\-level visibility ensuring deposits are tracked consistently from quote through project completion, providing all stakeholders with appropriate access to deposit status information\. The integrated approach maintains clean financial records while supporting the complex deposit and pre\-payment timing requirements of commercial furniture operations\.

__4\. Future State Process__

Deposits will be created directly at the quote level with the Accounting team processing actual deposit transactions via Customer Deposit\. Upon quote to sales order conversion, deposits will automatically associate with the new sales order without manual intervention\. Invoice generation will automatically apply available deposits, streamlining the billing process\. Similarly, vendor pre\-payments will be captured against draft purchase orders and automatically applied to vendor bills\. Deposit visibility will span quote, sales order, and project levels with appropriate dashboards for each stakeholder group\.

Solution required to apply partial payments

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Quote\-level deposits

Custom quote deposit functionality

Early collection capability

✓ Validated

Vendor pre\-payments

Draft PO pre\-payment capability

Vendor payment management

✓ Validated

Automatic association

Conversion workflow integration

Eliminate manual tracking

✓ Validated

Automatic application

Automated deposit/pre\-payment application

Streamlined billing

✓ Validated

Multi\-level visibility

Comprehensive tracking

Complete transparency

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your manual deposit tracking will adapt to systematic workflow

- Compass\-based deposit requests will be replaced with system functionality
- Manual association will be replaced with automatic workflows

__ALIGN__: Your deposit application requirements align with NetSuite's standard invoice processing

- Automatic deposit application will use native functionality
- Deposit visibility will utilize standard reporting capabilities
- Financial integration will follow established patterns

__7\. Implementation Considerations__

- Quote deposit workflow must be thoroughly tested before go\-live
- Training required for Accounting team on new deposit processing
- Conversion timing and association rules require clear definition

## <a id="_Toc208925530"></a>PDF Composer

__1\. Your Business Requirements__

- Implement dynamic PDF composer with on\-the\-fly field selection capabilities
- Build 10 unique templates to be used across transaction types
- Support multiple quote formats including budgetary, formal, GSA, and client\-specific formats
- Enable dynamic control of terms & conditions display based on template selection
- Eliminate manual PDF editing in external tools \(Acrobat/Bluebeam\) currently required
- Ensure consistent branding and logo application across all document types

__2\. Current State Process__

Current system requires extensive manual PDF editing in external tools after generation from D365 or CAP\. Multiple PDF formats are needed for different scenarios including budgetary quotes requiring manual modifications, GSA business excluding standard terms and conditions, and client\-specific formats requiring manual editing\. Branding issues create inconsistent logo loading requiring manual fixes\. The manual editing process is time\-consuming and creates delays in quote delivery, with the Sales Coordination team spending significant time on document formatting rather than customer interaction\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides advanced PDF Composer functionality designed to eliminate manual editing processes that plague commercial furniture dealers\. The solution includes dynamic template selection capabilities with on\-the\-fly customization through configurable field options\. Each template can be configured with specific field combinations that control content display dynamically, allowing real\-time customization without external editing tools\.

The system enables template selection at generation time with an additional layer of options to turn fields on and off dynamically\. The Sales and Sales Coordination teams can select budgetary templates with specific field configurations, or exclude terms and conditions for GSA business \- all through the interface without opening external editing software\. GSA templates can be pre\-configured to exclude terms and conditions automatically\. This integrated approach eliminates the manual editing burden while ensuring consistent branding and professional document presentation across all customer interactions\.

__4\. Future State Process__

Quote PDF generation will utilize dynamic template selection from the 10 configured templates based on customer requirements and project types\. The Sales Coordination team will choose from pre\-configured templates \(budgetary, formal, GSA, client\-specific\) and customize field display through intuitive checkboxes\. Logo and branding will load consistently across all templates, and terms exclusion will occur automatically based on template selection for GSA business\. The entire process will complete efficiently rather than the current multi\-step manual editing workflow\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Dynamic field selection

On\-the\-fly customization

Eliminate manual editing

✓ Validated

10 unique templates

Cross\-transaction template library

Complete coverage

✓ Validated

Multiple formats

Template\-based generation

Format consistency

✓ Validated

Terms control

Dynamic field configuration

GSA compliance

✓ Validated

Consistent branding

Automated logo application

Professional presentation

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your manual editing workflow will adapt to automated template system

- External editing tools will be eliminated
- Template selection will replace manual customization
- Branding consistency will be automated

__ALIGN__: Your PDF generation requirements align with NetSuite Orion's standard PDF Composer capabilities

- Dynamic template selection will be configured
- Field customization options will use standard functionality
- 10 unique templates will support all transaction types

__7\. Implementation Considerations__

- Template requirements to NetSuite PDF Composer format
- Training required for Sales Coordination team on template selection and customization
- Template approval process needs definition for new formats
- Integration with existing CAP system for seamless workflow

## <a id="_Toc208925531"></a>Client Quote Approval

__1\. Your Business Requirements__

- Implement web\-based client quote approval system eliminating manual email tracking\. Note:  if terms are updated on the customer record, they will ONLY be applied to future orders\.
- Replace current Docentric email system with integrated customer portal for cost reduction\.  Unique email addresses can be created on customer contacts for quotes and invoices\.
- Provide customers with secure portal access for quote review and approval via mobile devices
- Support dashboard alerts for CSM Team when customers take action in the web portal
- Create systematic tracking of client approval status with real\-time visibility and audit trails

__2\. Current State Process__

Client quote approval currently relies on the Docentric email system add\-on to D365 with manual email communication and limited tracking capabilities\. The Sales Coordination team sends quotes via email and waits for customer responses without systematic visibility into approval status\. There is no centralized tracking of which customers have received, reviewed, or approved quotes, creating gaps in follow\-up communication\. The manual process makes it difficult to identify bottlenecks in customer decision\-making and leads to delayed project starts when approvals are pending without clear status visibility\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides comprehensive client quote approval capabilities through its web\-based customer portal system designed specifically for commercial furniture dealers requiring external approval workflows\. The solution enables customers to access quotes through secure web portals on both desktop and mobile devices, review all project details, and submit approvals directly through the system rather than email responses\. This integrated approach provides real\-time visibility to sales teams on customer approval status while maintaining professional presentation and audit trails\.

The system's approval interface allows customers to review quotes at their convenience while providing the Sales Coordination team with immediate dashboard notifications when customers take any action in the portal\. Users of the system can add attachments that get sent to customers for approval beyond just the proposal PDF, enabling additional documentation or requirements to be included\. Every customer interaction is tracked with timestamps and approval notes, creating comprehensive audit trails that satisfy both internal controls and customer relationship requirements\. This solution replaces Docentric functionality while reducing ongoing software costs and providing enhanced capabilities\.

__4\. Future State Process__

Customer quotes will be delivered through secure web portals where clients can review project details on mobile or desktop devices, ask questions, and submit approvals online\. The Sales Coordination, CSM and Sales teams will have real\-time dashboard visibility to customer approval status with automatic alerts when customers take action in the portal\. Automated notifications will alert both customers and sales teams of status changes, and approval decisions will automatically trigger internal workflows for order processing\. Complete audit trails will track all customer interactions from initial quote delivery through final approval\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Web\-based approval

Customer portal access

Eliminate email tracking

✓ Validated

Docentric replacement

Integrated email functionality

Cost reduction

✓ Validated

Mobile capability

Responsive portal design

Customer convenience

✓ Validated

Dashboard alerts

Real\-time notifications

Immediate visibility

✓ Validated

Audit trails

Complete tracking system

Compliance ready

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your email approval tracking will adapt to systematic dashboard monitoring

- Docentric email system will be replaced with integrated portal
- Manual follow\-up will be replaced with automated notifications
- Status visibility will be real\-time rather than inquiry\-based via portlets on users dashboard

__ALIGN__: Your client approval requirements align with NetSuite Orion's standard customer portal capabilities

- Web\-based approval interface will use standard functionality
- Customer portal access will be configured for quote review
- Mobile responsiveness will utilize native capabilities

__7\. Implementation Considerations__

- Customer portal setup and access management needs definition
- Training required for Sales Coordination team on approval status monitoring
- Customer onboarding process for portal access must be established\.  GSI will train Pivot and Pivot will train their customers
- Cost savings analysis from Docentric replacement should be documented

## <a id="_Toc208925532"></a>Budget Setting at Sales Order Conversion

__1\. Your Business Requirements__

- Implement budget locking functionality at quote to sales order conversion
- Enable budget versus actual tracking for project profitability analysis
- Support future integration with time tracking systems for complete cost analysis
- Provide reporting capabilities for budget variance identification and management
- Create foundation for enhanced project management capabilities
- Maintain clear baseline costs, quantities, and margins for variance analysis

__2\. Current State Process__

Budget versus actual tracking is currently available in D365 but not effectively utilized due to two main limitations: lack of actual time tracking makes labor costs appear as 100% margin, and punch/change management makes cost overruns appear as budget growth rather than variance\. The system can lock budgets at sales order conversion, but without actual cost tracking, the reports provide limited value for project management decisions\. The Operations team expressed interest in using this functionality if time tracking capabilities are implemented in the future\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides comprehensive budget management capabilities designed to support commercial furniture project tracking from initial quote through completion\. The solution enables budget locking at the moment of quote to sales order conversion, establishing baseline costs, quantities, and margins for variance analysis\. This functionality creates a foundation for project profitability tracking that can be enhanced as time tracking and other actual cost components are implemented\.

The system's budget versus actual reporting provides clear visibility to project managers and accounting teams regarding cost performance, with the flexibility to accommodate future enhancements like actual time tracking\. Budget modifications after locking are tracked systematically, ensuring changes are documented and tracked appropriately\. This systematic approach prepares Pivot for enhanced project management capabilities while providing immediate value for cost control and profitability analysis\.

__4\. Future State Process__

Budget locking will occur automatically at quote to sales order conversion, capturing costs, quantities, and margins as baseline metrics\. Sales order modifications after locking will be tracked as additions with separate dating, enabling clear variance analysis between original budget and changes\. Approval workflow can be reinitiated for changes if required\.  Reporting will show budget versus actual performance with the capability to incorporate time tracking and other actual cost components as they become available\. Project managers will have access to variance reports for proactive cost management – standard Orion functionality\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Budget locking

Conversion point capture

Baseline establishment

✓ Validated

Variance tracking

Budget vs actual reports

Project visibility

✓ Validated

Reporting capabilities

Comprehensive analytics

Management insight

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your budget management will adapt from unused functionality to systematic tracking

- Budget locking will be activated at sales order conversion
- Variance analysis will be implemented for project management
- Time tracking integration is required at Go\-live\.  Requirements and solution to be developed\.

__ALIGN__: Your budget locking requirements align with NetSuite's standard sales order management

- Budget capture at conversion will use standard functionality
- Variance reporting will utilize native capabilities
- Tracking workflows will follow established patterns

__7\. Implementation Considerations__

- Budget locking timing and triggers must be clearly defined
- Training required for project managers on variance reporting
- Budget modification tracking workflows need establishment

## <a id="_Toc208925533"></a>Pro Forma Invoice Management

__1\. Your Business Requirements__

- Create pro forma invoice records without GL impact for deposit request tracking purposes
- Enable user\-generated pro forma invoices from selected quotes with multiple quote scenarios
- Implement separate numbering system distinct from regular invoicing sequences
- Utilize existing aging reports for pro forma invoices showing days outstanding
- Support systematic tracking of pro forma to actual deposit conversion
- Replace current PDF tool title\-changing process with integrated pro forma generation

__2\. Current State Process__

Pro forma invoices currently require creation outside the system using PDF tools to manually change titles from "Invoice" to "Deposit Invoice" or "Pro Forma Invoice\." The Accounting team must manually manipulate these documents, creating confusion for customers and internal teams when multiple versions exist\. There is no systematic aging or tracking of outstanding pro forma invoices, making it difficult to follow up on pending deposits\. The lack of separate numbering creates confusion between pro forma requests and actual invoices, complicating accounts receivable processes\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides comprehensive pro forma invoice management through custom records designed specifically to track deposit requests without general ledger impact\. The solution enables users to select from available quotes and generate pro forma invoice records, calculating deposit amounts automatically based on the deposit percentage identified on the quote\. This functionality maintains clear separation between sales\-side deposit requests and accounting\-side actual deposits while providing complete tracking capabilities\.

The system's pro forma management includes separate numbering sequences to eliminate confusion with regular invoices, and existing aging reports can be utilized to show days outstanding for follow\-up purposes\. Pro Forma invoices are associated with customer deposits and represent a custom record that tracks the request for deposit amount\. The Pro Forma Agent Dashboard can be a data point for cash flow management\. The solution enables systematic tracking from initial creation through final payment application while replacing the current manual PDF title\-changing process with integrated pro forma generation\.

__4\. Future State Process__

Pro forma invoices will be generated by users selecting appropriate quotes, with deposit percentages applied automatically based on quote configuration – can be manually overridden is approved by management\. Each pro forma will receive a unique number from a separate sequence, clearly identifying it as a deposit request rather than an actual invoice\. The Sales and Sales Coordination team will have access to existing aging reports adapted for pro forma invoices showing outstanding requests for customer follow\-up\. When payments are received, the Accounting team will process actual deposits with tracking to corresponding pro forma records, providing complete audit trails from request through collection\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

No GL impact

Custom record structure

Clean financials

✓ Validated

User\-generated

Quote selection process

Flexible creation

✓ Validated

Separate numbering

Independent sequence

Eliminate confusion

✓ Validated

Existing aging reports

Adapted reporting

Familiar functionality

✓ Validated

Replace PDF tools

Integrated generation

Eliminate manual process

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your PDF tool process will adapt to integrated pro forma generation

- Manual title changing will be eliminated
- PDF tool dependency will be replaced with system\-generated documents
- Existing aging reports will be adapted for pro forma tracking

__ALIGN__: Your tracking requirements align with standard audit and reporting capabilities

- Aging reports will use standard saved search functionality
- Audit trails will utilize native tracking features
- Customer information transfer will use standard field mapping

__7\. Implementation Considerations__

- Pro forma numbering sequence format needs definition
- Quote selection criteria and user permissions must be specified
- Integration with existing aging report structure requires configuration
- Training needed for Sales Coordination and Accounting teams on pro forma workflows

## <a id="_Toc208925534"></a>Purchase Order Generation

__1\. Your Business Requirements__

- Enable direct purchase order creation from SIF files without requiring sales orders for showroom purchases
- Support draft purchase order functionality for editing before finalization
- Provide mass PO update capabilities to eliminate individual header editing for large orders
- Support automatic PO splitting by vendor and alias rules for efficient procurement via groups
- Implement line constitution functionality for flexible editing until finalization
- Create purchase requisition system for showroom and special approvals – approval workflow need for requisitions for corporate expenses
- Support multiple transmission methods including EDI, email, web portals, and internal routing

__2\. Current State Process__

Purchase order generation currently requires extensive manual processing with significant limitations\. Sales orders must be created before any PO generation, even for showroom orders that don't have sales\. The mass update process requires individual selection of each PO to apply header information, consuming hours for large projects\. Items cannot be added to existing POs, forcing new PO creation for any additions\. The lack of requisition system means showroom approvals occur via email to the Finance team outside the system\. Changes to purchase orders after vendor acknowledgments are difficult to manage in D365, creating operational inefficiencies\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides comprehensive purchase order automation designed specifically for complex commercial furniture procurement scenarios\. The solution enables direct PO creation from multiple sources including SIF files, eliminating the requirement for sales orders in showroom scenarios – controlled via roles in Orion\. We support standalone purchase orders for showroom purchases and have the Smart Table enabled on purchase orders, so SIF files can be imported directly onto purchase orders\.

The draft purchase order functionality is a key benefit \- having a draft purchase order before the final vendor purchase order allows changes to be umade easily once users get feedback from the vendor via an acknowledgment\. Currently in D365, it's very difficult to make those types of changesc, but because we use a draft purchase order, it is easy to make changes on the draft purchase order and it is automatically reflected on the sales order\.

Mass update functionality applies header information across unlimited POs simultaneously through a single form, reducing hours of work to minutes\. The system's intelligent splitting rules automatically separate POs by vendor, alias codes, or custom criteria\. Line constitution functionality defers the transaction lines being constituted in order to enable PO editing and draft PO editing before finalization, supporting the editing needed after receiving an acknowledgment\. Built\-in requisition workflows route special purchases through appropriate approval channels with full audit trails, replacing email\-based approvals with systematic tracking\.

__4\. Future State Process__

Purchase order generation will begin with intelligent automation that creates and splits POs based on configured rules\. Showroom and stock orders will import directly from SIF files without sales order creation\. Draft POs will enable editing and modifications based on vendor feedback before finalization\. Mass updates will apply to all POs simultaneously, with line constitution enabling modifications until transmission\. Requisitions will route through systematic approvals with the Finance team receiving dashboard notifications\. Vendor transmission will occur automatically based on vendor preferences, with confirmation tracking and discrepancy management through integrated workflows\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Direct PO from SIF

Standalone PO creation

Eliminate SO requirement

✓ Validated

Draft PO functionality

Pre\-finalization editing

Confirm change history report has been modified

Easy acknowledgment changes

✓ Validated

Mass PO updates

Bulk header editing

Significant time reduction

✓ Validated

Auto\-splitting

Rule\-based separation

Optimal procurement

✓ Validated

Line constitution

Flexible editing capability

Modification support

✓ Validated

Requisition system

Approval workflows

Systematic approvals

✓ Validated

__6\. Implementation Approach__

__ADAPT__: Your requisition process will adapt from email to systematic workflow

- Finance team approvals will route through system
- Showroom orders will follow requisition path
- Audit trails will replace email threads – standard NetSuite functionality

__ALIGN__: Your vendor transmission requirements align with standard capabilities

- EDI for MillerKnoll will maintain current integration
- Email automationI will use configured templates\.  Modifications recommended to be done outside of Orion using 3rd party tools
- XML export functionality will enable portal integration

__7\. Implementation Considerations__

- Smart Table mass update fields are already defined
- Vendor transmission preferences must be documented
- Requisition approval hierarchies require definition

## <a id="_Toc208925535"></a>Miller\-Knoll Order Manager Integration

__1\. Your Business Requirements__

- Maintain current Miller\-Knoll EDI integration functionality
- Support sending purchase order information from Orion to Miller\-Knoll
- Receive acknowledgment information back from Miller\-Knoll
- Process acknowledgments through vendor response utility for discrepancy management

__2\. Current State Process__

Pivot currently has Miller\-Knoll Order Manager integration that enables sending purchase order information and receiving back acknowledgment information\. This integration is already operational and provides the basic EDI functionality required for Miller\-Knoll transactions\. The existing integration meets current operational requirements for this vendor relationship\.

__3\. NetSuite Orion Solution__

NetSuite Orion maintains and supports the Miller\-Knoll Order Manager integration, enabling continued EDI functionality for purchase order transmission and acknowledgment receipt\. The solution integrates with Orion's vendor response utility to process acknowledgments and manage any discrepancies that arise\. This integration supports the systematic processing of Miller\-Knoll transactions while maintaining continuity with existing operational workflows\.  Automation of acknowledgements required at go\-live

__4\. Future State Process__

Miller\-Knoll purchase orders will continue to be transmitted electronically through the Order Manager integration\. Acknowledgments will be received back through the same integration and processed through the vendor response utility\. Any discrepancies will be flagged for review and resolution through systematic workflows via global tolerance settings \(amount, percentage, days\)\. The integration will maintain current functionality while providing enhanced visibility and tracking capabilities\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Maintain EDI integration

Existing integration support

Continuity ensured

✓ Validated

PO transmission

Order Manager connectivity

Seamless ordering

✓ Validated

Acknowledgment receipt

Electronic processing

Automated workflow

✓ Validated

Discrepancy management

Vendor response utility

Systematic resolution

✓ Validated

__6\. Implementation Approach__

__ALIGN__: Your Miller\-Knoll integration requirements align with existing capabilities

- Current EDI integration will be maintained
- Order Manager connectivity will be preserved
- Existing operational workflows will continue

__7\. Implementation Considerations__

- Integration testing required to ensure continuity
- Training on vendor response utility for discrepancy management
- Documentation of current integration specifications

## <a id="_Toc208925536"></a>Acknowledgements

__1\. Your Business Requirements__

- Process electronic acknowledgments from Miller\-Knoll through existing integration
- Support manual acknowledgment processing for other vendors via Smart Table
- Identify discrepancies between purchase orders and vendor acknowledgments
- Create issues for discrepancies requiring resolution
- Provide systematic acknowledgment tracking and management

__2\. Current State Process__

Acknowledgment processing currently operates through a mix of electronic and manual methods\. Miller\-Knoll acknowledgments are received electronically through the existing Order Manager integration, while other vendor acknowledgments arrive via PDF or email and require manual processing\. Discrepancy identification and resolution lacks systematic tracking, making it difficult to ensure all issues are addressed promptly\.

__3\. NetSuite Orion Solution__

NetSuite Orion provides comprehensive acknowledgment management through two primary methods\. Electronic acknowledgments are available through the Miller\-Knoll Order Manager integration, and those acknowledgments are processed in the vendor response utility, which allows users to create issues if there are discrepancies\. For other vendors, manual acknowledgments can be processed using the Smart Table to identify discrepancies and create issues for resolution\.

The vendor response utility provides systematic discrepancy management with clear tracking of resolution status and ownership\. This approach ensures all acknowledgments are processed consistently whether they arrive electronically or manually, with appropriate escalation and tracking for discrepancy resolution\.

Approval workflow for margin erosion tolerance due to changes in sales price to cost\.

__4\. Future State Process__

Electronic acknowledgments from Miller\-Knoll will be processed automatically through the vendor response utility, with discrepancies flagged for review and issue creation\. Manual acknowledgments from other vendors will be processed through the Smart Table, enabling users to identify discrepancies and create issues systematically\. All acknowledgment processing will include tracking of resolution status and ownership, ensuring discrepancies are addressed promptly and thoroughly\.

__5\. Solution Validation__

__Requirement__

__NetSuite Orion Capability__

__Business Impact__

__Validation Status__

Electronic processing

Miller\-Knoll integration

Automated acknowledgments

✓ Validated

Manual processing

Smart Table functionality

Vendor coverage

✓ Validated

Discrepancy identification

Vendor response utility

Systematic detection

✓ Validated

Issue creation

Integrated issue tracking

Resolution management

✓ Validated

Systematic tracking

Complete audit trail

Process accountability

✓ Validated

__6\. Implementation Approach__

__ALIGN__: Your acknowledgment processing requirements align with existing capabilities

- Miller\-Knoll electronic acknowledgments will continue through existing integration
- Vendor response utility will provide systematic discrepancy management
- Smart Table manual processing will cover other vendors

__7\. Implementation Considerations__

- Training required on vendor response utility for discrepancy management
- Smart Table acknowledgment processing procedures need documentation
- Issue tracking and resolution workflows require definition

# <a id="_Toc208925537"></a>__4 Implementation Timeline and Next Steps__

__Phase 1 Deliverables \(Months 1\-4\)__

- Core order management configuration
- Customer credit and setup workflows
- Quote approval automation
- SIF import optimization
- Smart Table grouping functionality with multi\-grouping support
- Deposit and pre\-payment management
- PDF Composer implementation with 10 unique templates
- Client quote approval portal
- Budget setting at conversion
- Pro forma invoice tracking
- Purchase order automation with draft PO capability
- Miller\-Knoll integration continuity
- Acknowledgment processing workflows
- Time tracking

__Outstanding Items Requiring Resolution__

__Critical \(Before Configuration\):__

- Complete quote approval rules list from Sales Coordination team
- Customer PO limit documentation for Oracle, Apple, Google
- PDF template requirements and specifications for 10 unique templates

__Important \(During Configuration\):__

- Budget locking timing and workflows
- Client approval portal access management
- Smart Table multi\-grouping naming conventions
- Pro forma numbering sequence format

# <a id="_Toc208925538"></a>__5 Signatures__

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

