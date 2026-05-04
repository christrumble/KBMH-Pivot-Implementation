# Pivot BRD — Financial Management

_Source: `Financial Management/Pivot/4 BRD/Pivot Interiors BRD Financial Management Process Area_v2.0.docx`_

---

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation__

__Financial Management Process Area__

__Prepared for: Pivot Interiors, Inc\.__

__Version 1\.0__

__Date: November 24, 2025__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

# <a id="_Toc214911978"></a>__Table of Contents__

[__Table of Contents__	2](#_Toc214911978)

[__1 Version Control__	3](#_Toc214911979)

[__2 Project Definition__	4](#_Toc214911980)

[2\.01 Executive Summary	4](#_Toc214911981)

[2\.02 Company Overview	4](#_Toc214911982)

[2\.03 NetSuite Orion Overview	5](#_Toc214911983)

[2\.04 Project Overview	5](#_Toc214911984)

[2\.05 Document Objectives	6](#_Toc214911985)

[__3 Financial Management__	7](#_Toc214911986)

[3\.01 Revenue & Cost Recognition	7](#_Toc214911987)

[3\.02 Project Accounting & GP Calculation	9](#_Toc214911988)

[3\.03 Banking & Electronic Payments	14](#_Toc214911989)

[3\.04 Collections Management	17](#_Toc214911990)

[3\.05 Accounts Payable Automation	20](#_Toc214911991)

[3\.06 Tax Management	24](#_Toc214911992)

[3\.07 Fixed Asset Management	27](#_Toc214911993)

[3\.08 Document Management	31](#_Toc214911994)

[3\.09 Expense Management	33](#_Toc214911995)

[3\.10 Payroll Integration	35](#_Toc214911996)

[3\.11 Chart of Accounts	39](#_Toc214911997)

[3\.12 Period Close	42](#_Toc214911998)

[3\.13 Budgeting & Planning	45](#_Toc214911999)

[3\.14 Accounts Receivable Management	48](#_Toc214912000)

[3\.15 Vendor Management	51](#_Toc214912001)

[3\.16 Implementation Strategy	53](#_Toc214912002)

[__4 SuiteApps__	56](#_Toc214912003)

[4\.01 SuiteApp Summary	56](#_Toc214912004)

[__5 Assumptions__	57](#_Toc214912005)

[__6 Unresolved Requirements__	61](#_Toc214912006)

[__7 Signatures__	63](#_Toc214912007)

# <a id="_heading=h.30j0zll"></a>

# <a id="_heading=h.1fob9te"></a><a id="_Toc214911979"></a>__1 Version Control__

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

Marcus Dallacqua, Debbie Herbert

Final Draft

11/24/2025

# <a id="_heading=h.2et92p0"></a>

# <a id="_heading=h.tyjcwt"></a>

# <a id="_Toc214911980"></a>__2 Project Definition__

## <a id="_Toc214911981"></a>__2\.01 Executive Summary__

Pivot Interiors is implementing NetSuite Orion to modernize its financial management operations and replace Microsoft Dynamics 365\. This Business Requirements Document \(BRD\) captures the business requirements discovered during the Financial Management process mapping phase and documents how the NetSuite Orion solution aligns with Pivot's operational needs\.

Through comprehensive discovery sessions conducted in August 2025, GSI analyzed Pivot's current state financial processes, pain points, and requirements across 15 process areas including revenue recognition, project accounting, banking operations, accounts payable/receivable, tax management, fixed asset management, and period close procedures\. The analysis identified 58 validated business requirements with documented evidence from stakeholder interviews and discovery sessions\.

The NetSuite Orion solution provides an integrated financial management platform specifically designed for the contract furniture dealer industry\.  Of the 58 requirements, 35 align with standard NetSuite Orion functionality \(ALIGNS\), 5 require process adaptation \(ADAPT\), 17 require custom configuration \(ACCOMMODATE\), and 1 is planned for future phases\. This high alignment rate \(60% standard functionality\) demonstrates that NetSuite Orion is purpose\-built for Pivot's industry and business model, with specific automation wins including elimination of 42 manual ACH/wire journal entries, automated AR cash application via bank feeds, and maintenance of Pivot's above\-average 7\-day period close performance\.

## <a id="_Toc214911982"></a>__2\.02 Company Overview__

Pivot Interiors, Inc\. is a leading California\-based design firm recognized for its team of innovators, creators, and thought leaders who specialize in delivering exceptional interior solutions for businesses of all sizes\. Their work captures the essence of each client’s brand while fostering environments that inspire employees to thrive, create, and collaborate\. Headquartered in the Bay Area, Pivot Interiors operates offices and Design Centers across the state, including Santa Clara, Fremont, San Francisco, Costa Mesa, Los Angeles, and La Mirada\. As a MillerKnoll Certified Dealer, Pivot Interiors invites clients to experience its uniquely crafted spaces and the distinctive quality that defines the Pivot Interiors brand\.

[__https://www\.pivotinteriors\.com__](https://www.pivotinteriors.com/)

## <a id="_Toc214911983"></a>__2\.03 NetSuite Orion Overview__

NetSuite Orion is an advanced suite of customizations designed to meet the specific needs of the contract office furniture dealer industry, built entirely within the NetSuite platform\. Created to optimize workflows, enhance operational efficiency, and provide extensive visibility, NetSuite Orion addresses industry challenges from pre\-quote to project completion\.

By leveraging NetSuite Orion’s established cloud ERP foundation, NetSuite Orion ensures robust security, scalability, and consistent performance\. This foundation allows NetSuite Orion to inherit all of NetSuite's security features and integrate seamlessly with the latest NetSuite releases, meaning users can take advantage of NetSuite's extensibility without fear of version lock\-in\.

__Core Financial Management Capabilities:__

- Comprehensive GL and chart of accounts management
- Multi\-entity, multi\-currency support
- Advanced revenue and cost recognition
- Project\-based accounting with furniture dealer\-specific KPIs
- Integrated AP/AR with automation capabilities
- Bank reconciliation and electronic payment processing
- Tax management with SuiteTax platform
- Fixed Asset Management module
- Period close automation and controls
- Real\-time financial reporting and dashboards

## <a id="_Toc214911984"></a>__2\.04 Project Overview__

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

## <a id="_Toc214911985"></a>__2\.05 Document Objectives__

The purpose of this document is to summarize functional and procedural requirements captured by GSI during the Discover business process mapping phase of the implementation\. 

This Business Requirements Document \(BRD\) documents your goals, the problems you want to solve, and the outcomes you expect\. It is the foundation for the setup of the system, acting as a __roadmap between your business needs and the solution design__\.

This document represents information gathered in meetings held with the Client, which enables the GSI team to map the business requirements to an efficient flow in the NetSuite Orion application\. Once complete, this document will serve as a blueprint for the GSI team to configure the application\. This document does not supersede the Statement of Work\. The Statement of Work determines scope\. 

A series of process mapping discovery sessions, focusing on the key areas of the business, were used as a starting point for this exercise\. This document remains consistent in structure to those discovery sessions as it categorizes the findings into the same key process areas\. The set of business requirements documentation is inclusive of all business requirements provided by the Client\.

# <a id="_Toc214911986"></a>__3 Financial Management__

## <a id="_Toc214911987"></a>__3\.01 Revenue & Cost Recognition__

3\.01\.01 Your Business Requirements

- __REQ\-3\.01\.01__: Use NetSuite Orion setting to prevent invoicing before fulfillment \(ALIGNS\)
- __REQ\-3\.01\.02__: Implement accrued revenue journal entries for delivered\-but\-not\-invoiced items \(ALIGNS\)
- __REQ\-3\.01\.03__: Accrued revenue journal entries require approval before posting \(ALIGNS\)

3\.01\.02 Current State Process

Pivot currently manages revenue and cost recognition in Microsoft Dynamics 365 with concerns about ensuring costs are recognized appropriately when items are fulfilled but not yet invoiced\. The organization needs controls to prevent premature revenue recognition while ensuring accurate matching of revenue and costs\.

__Current State Challenges:__

- Manual monitoring required to ensure costs are matched and posted automatically when lines are invoiced
- Risk of invoicing before fulfillment without system controls
- Need for automated journal entries to handle timing differences
- Approval processes must be maintained for financial controls

__User Story:__

- As a Controller, I need automated controls to prevent invoicing before fulfillment so that we maintain financial compliance and accurate revenue recognition timing\. This can be handled by a NetSuite native functionality called Advanced Shipping and have separate transactions to fulfill sales orders and bill sales orders\. With this feature, you can invoice customers for an entire sales order even if all items on the order are not shipped\.

Once you enable Advanced Shipping, you cannot turn it off until all fulfilled sales orders have been billed\.

3\.01\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive revenue and cost recognition capabilities designed specifically to address the complex timing requirements of project\-based businesses in the furniture dealer industry\. The solution includes built\-in controls that prevent premature revenue recognition while ensuring accurate cost matching\.

__NetSuite Setting for Fulfillment Controls:__
NetSuite Orion includes a standard configuration setting that prevents invoices from being created until items have been fulfilled\. This system\-level control eliminates the risk of premature revenue recognition by enforcing the business rule at the transaction level\. The setting is configurable per account preferences and provides consistent enforcement across all users and transactions\.

__Automated Accrued Revenue Journal Entries:__
The system includes standard functionality to automatically generate accrued revenue journal entries for scenarios where items have been fulfilled \(cost recognized\) but not yet invoiced \(revenue not recognized\)\. The correct impact will debit COGS and\. Credit the asset account\. built\-in report identifies all item fulfillment lines that are not yet on invoices, and automated journal entry processing creates reversing journal entries to post to accrued revenue accounts\. This ensures proper revenue and cost matching while maintaining accurate financial statements\. \(DR\) COGS and \(CR\) Asset Account Sales are correct for the revenue accrual\. Debiting the Unearned Revenue asset account and crediting Sales

__Approval Workflow Controls:__
All automatically generated accrued revenue journal entries flow through NetSuite Orion’s standard approval workflow functionality before posting\. Journal entries are created in an unapproved state, requiring designated approvers to review and approve before the entries affect the general ledger\. This control ensures management oversight of automated processes while maintaining audit trails\.

Please see an example of an approval matrix to review GL impact\.

The journals will not affect your GL until they are approved

3\.01\.04 Future State Process

In the NetSuite Orion environment, revenue and cost recognition will be controlled systematically with minimal manual intervention:

1. __Fulfillment Controls__: System prevents invoice creation until items are fulfilled, enforced at the transaction level
2. __Automated Identification__: Standard reports identify fulfilled\-but\-not\-invoiced items automatically
3. __Journal Entry Generation__: The System creates reversing accrued revenue journal entries automatically
4. __Approval Process__: Automated journal entries route to designated approvers for review
5. __GL Posting__: Upon approval, journal entries post automatically to maintain accurate financial position

Approval Matrix is needed, see Appendix Example

This automated process reduces manual monitoring, ensures consistent application of revenue recognition policies, and maintains proper controls through approval workflows\.

3\.01\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.01\.01

Use NetSuite Orion setting to prevent invoicing before fulfillment

Standard NetSuite Orion preference setting enforces rule at transaction level

ALIGNS

REQ\-3\.01\.02

Implement accrued revenue journal entries for delivered\-but\-not\-invoiced items

Standard report identifies items \+ automated JE processing

ALIGNS

REQ\-3\.01\.03

Accrued revenue journal entries require approval before posting

Standard NetSuite Orion approval workflow functionality

ALIGNS

<a id="_heading=h.3fwokq0"></a>

__*Client Feedback*__

<a id="_heading=h.1v1yuxt"></a>__*GSI Response*__

<Comment>

## <a id="_Toc214911988"></a>__3\.02 Project Accounting & GP Calculation__

3\.02\.01 Your Business Requirements

- __REQ\-3\.02\.01__: Official project GP includes all calculated costs including time tracked \(ACCOMMODATE\)
- __REQ\-3\.02\.02__: Commission calculations use quoted costs from sales orders not actual \(ACCOMMODATE\)
- __REQ\-3\.02\.03__: Project KPIs reflect actual calculated costs from time tracking \(ACCOMMODATE\)
- __REQ\-3\.02\.04__: Commissionable GP KPIs initially use selling costs from sales orders, but actualize to actual costs as vendor bills and invoices are received, with final commission calculations based on actual revenue and actual costs Work is already in NetSuite \(ALIGN\) Need proper treatment when  a transaction component from GP comes from multiple divisions
- __REQ\-3\.02\.05__: Use Default NetSuite items for tracking external services\. The recommendation is to use the native functionality first, based on the frequency of this case\. Automation can be revisited if finance charges volume increases significantly\.

See appendix for further information

- \(ALIGNS\)
- __REQ\-3\.02\.06__: External services post to WIP and use receive function \(ALIGNS\)
- __REQ\-3\.02\.07__: Labor cost posting proposal evaluation and decision \(ACCOMMODATE\)

3\.02\.02 Current State Process

Pivot's commission structure is based on project profitability, but commission calculations must use quoted/selling costs from sales orders rather than actual costs to avoid penalizing sales representatives for operational inefficiencies beyond their control\. This creates a requirement for dual GP calculations:

- __Official Project GP__: Reflects true project performance using all actual costs including labor time tracking
- __Commissionable GP__: Used for sales commission calculations using quoted/selling costs from sales orders

As stated during discovery: "Official project GP should include all calculated costs including time tracked, but if they keep current policy commission will use quote cost" – emphasizing the critical business requirement for dual GP calculations that serve different operational purposes\.

Actual costs, including cost adjustments that happen in AP after SO invoicing, should be on the commissionable GP report/process

__Current State Challenges:__

- Need separate GP calculations for operational performance vs\. commission calculations
- Commission structure must isolate sales representatives from operational cost overruns
- Project KPIs must reflect true financial performance with actual costs
- Commission KPIs must use selling costs to compensate sales teams
- External services tracking requires proper WIP management \(confirmed: "Yes, they do want lot numbered inventory for external services to post to WIP"\)
- Labor cost posting timing requires evaluation and decision \(currently posts at point of invoicing through upload process\)

__User Story:__

- As a CFO, I need dual GP calculations so that we can measure true project performance while compensating sales representatives based on quoted costs they can control\.

3\.02\.03 NetSuite Orion Solution

NetSuite Orion's project accounting module will be customized to support Pivot's unique dual GP calculation methodology\. This accommodation is necessary because standard NetSuite Orion commission modules do not support GP\-based split calculations with separate actual vs\. quoted cost tracking\.

__Dual GP Calculation Engine:__
NetSuite Orion will accommodate Pivot's business requirement through custom project accounting enhancements that maintain two parallel GP calculations on each project record\. The official project GP will calculate using all actual costs including time tracked labor, providing true financial performance visibility\. The commissionable GP will calculate using quoted/selling costs from sales orders, isolating sales representatives from operational variances\. Both calculations will be visible on project records with clear labeling to avoid confusion\.

__Dual KPI Configuration:__
Project dashboards and reports will display both KPI sets: operational KPIs showing actual costs and financial performance, and commission KPIs showing commissionable GP\. The commissionable GP initially uses selling costs from sales orders to protect sales representatives from early operational variances, but the project actualizes as vendor bills and invoices are received\. Final commission calculations use actual revenue from invoices and actual costs from the costing method, ensuring commissions reflect true project outcomes while maintaining fairness during project execution\.

NetSuite Orion's project record includes furniture dealer\-specific KPIs not available in standard NetSuite: cash balance tracking \(customer deposits vs\. vendor payments\), commissionable GP separate from actual GP, margin erosion tracking, and overhead fee calculation at the project level\. These purpose\-built capabilities eliminate the need for extensive custom development that would be required in standard NetSuite to achieve the same business visibility\.

__External Services WIP Management:__
As confirmed during discovery: "We will use lot numbered inventory for tracking external services\. They will post to WIP, which means you will have a receive function, which means if there is a variance at the time of the vendor bill, the post vendor variance would fix that imbalance\." External services with purchase orders are treated as items in NetSuite\. NetSuite Orion provides standard lot\-numbered inventory functionality for tracking external services through WIP accounts\. External services post to WIP using the standard receive function, ensuring proper cost accumulation and project tracking\. This approach enables vendor bill variance processing to automatically adjust project costs and commissions when actual vendor bills differ from expected amounts, addressing Sandra's concern: "if we get a vendor Invoice and it's $500 more than expected\.\.\. it does hit the projects and commissions\."

This is largely due to the limitation of 2 decimal points in D365\. Does Orion solve this by allowing 4 decimal points? An example would be for a 10% invoice on a $2m can be quite a rounding difference\.

This is largely due to the limitation of 2 decimal points in D365\. Does Orion solve this by allowing 4 decimal points? An example would be for a 10% invoice on a $2m can be quite a rounding difference

__Labor Cost Posting Methodology:__
As documented in discovery: "Team will evaluate options between current process vs\. posting to asset account earlier" and "Marcus to map out proposal for labor cost posting\." Currently, Pivot posts labor costs at the point of invoicing through an upload process that hits a labor offset account, then moves to cost of goods sold during billing\. GSI will provide a proposal evaluating timing options for labor cost posting \(immediate posting vs\. deferred to asset account vs\. current invoicing\-based approach\)\. This decision affects when labor costs impact project GP calculations and requires business input on preferred methodology\. The solution will be designed based on Pivot's selected approach during configuration sessions, with a dedicated commission structure and labor costing session planned to finalize the approach\.

3\.02\.04 Future State Process

In the NetSuite Orion environment with customized dual GP calculation:

1. __Sales Order Creation__: Quoted/selling costs captured on sales order lines
2. __Project Execution__: Actual costs accumulate through purchasing, time tracking, and external services
3. __Dual GP Calculation__: The System maintains two GP calculations:
	- Official Project GP = Revenue \- All Actual Costs \(including time tracked\)

Commissionable GP uses the same base calculation as Official GP but allows certain lines and transactions to be flagged as exempt from the commission calculation\.

-
	- Commissionable GP = Revenue − Actual Costs \(excluding exempt items\)

GP is not using quoted bur actuals \(except for internal labor\)\.

Notify when costs are understated or overstated – Saved searches possible solution

1. __Dashboard Display__: Both KPI sets visible on project records and reports
2. __Project Actualization__: As vendor bills and invoices are received, project actualizes with actualization percentage tracking
3. __Commission Processing__: Initial commission calculations use Commissionable GP KPIs with selling costs; final commission calculations use actual revenue from invoices and actual costs from costing method
4. __Financial Reporting__: Official Project GP used for financial statements and management reporting

This approach provides accurate financial visibility while maintaining fair commission calculations\.

3\.02\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.02\.01__

Official project GP includes all calculated costs including time tracked

Custom GP calculation engine required

__ACCOMMODATE__

__REQ\-3\.02\.02__

Commission calculations use quoted costs from sales orders not actual

Custom commission calculation logic

__ACCOMMODATE__

__REQ\-3\.02\.03__

Project KPIs reflect actual calculated costs from time tracking

Custom KPI configuration for operational metrics

__ACCOMMODATE__

__REQ\-3\.02\.04__

Commissionable GP KPIs initially use selling costs from sales orders, but actualize to actual costs as vendor bills and invoices are received, with final commission calculations based on actual revenue and actual costs

Custom KPI configuration with actualization process

__ACCOMMODATE__

__REQ\-3\.02\.05__

Use lot numbered inventory for tracking external services

Standard NetSuite lot tracking functionality\. Confirmed in discovery: "We will use lot numbered inventory for tracking external services"

__ALIGNS__

__REQ\-3\.02\.06__

External services post to WIP and use receive function

Standard WIP posting process\. Confirmed in discovery: "They will post to WIP, which means you will have a receive function\.\.\. External services with a PO is considered an item"

__ALIGNS__

__REQ\-3\.02\.07__

Labor cost posting proposal evaluation and decision

Design proposal to be provided by GSI\. Current process: labor costs post at point of invoicing through upload to labor offset account\. Team will evaluate options between current process vs\. posting to asset account earlier

__ACCOMMODATE__

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214911989"></a>__3\.03 Banking & Electronic Payments__

3\.03\.01 Your Business Requirements

- __REQ\-3\.03\.01__: Bank Feeds SuiteApp for automated AR cash application \(ALIGNS\)
- __REQ\-3\.03\.02__: Electronic Advanced Bill Payment SuiteApp for AP ACH/wire integration \(ALIGNS\)
- __REQ\-3\.03\.03__: Comerica Bank integration confirmed and supported \(ALIGNS\)

  Bank feeds will allow you to add more than 1 account under the financial           institution configuration

__REQ\-3\.03\.04__: Automated bank reconciliation with custom matching rules \(ALIGNS\)

- __REQ\-3\.03\.05__: Credit card account reconciliation within system \(ALIGNS\)

Credit card reconciliation will be the same as bank accounts

- __REQ\-3\.03\.06__: Eliminate 42 manual journal entries for ACH/wire processing \(ALIGNS\)

3\.03\.02 Current State Process

Pivot currently processes ACH and wire payments in D365 with significant manual effort\. On check run days, the accounting team must create 42 individual journal entries manually to record ACH and wire transfers\. This process is time\-consuming, error\-prone, and creates bottlenecks in the payment processing workflow\.

As documented during discovery: "They had started to cut and paste data into file to send to bank for ACH/Wires" – highlighting the manual effort required for the 42 individual journal entries on each check run day, representing a significant automation opportunity\.

__Current State Challenges:__

- 42 manual journal entries required on check run day for ACH/wire processing
- Manual cash application to AR invoices
- Manual bank reconciliation processes
- Credit card reconciliation requires manual effort each month
- Tracy has created an integrated payables file format for Comerica but process is manual

__User Story:__

- As an AP Manager, I need automated electronic payment processing so that we can eliminate 42 manual journal entries and streamline our payment workflow\.

3\.03\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive banking automation through two standard SuiteApps that integrate directly with Comerica Bank \(verified compatible\)\. The Bank Feeds SuiteApp creates a live feed from Comerica into NetSuite, automatically importing bank deposits and matching them to open AR invoices using configurable rules\. This eliminates manual cash application and ensures timely payment posting\. The Electronic Advanced Bill Payment SuiteApp enables users to create bill payments in NetSuite Orion and mark them for electronic transfer; the system automatically transmits payment instructions to Comerica, eliminating the 42 manual journal entries currently required on check run day\. Both SuiteApps are included at no additional cost\.

NetSuite's bank reconciliation functionality supports custom matching rules that automatically match transactions based on configurable criteria \(amount, date, transaction type\), significantly reducing manual reconciliation effort\. The same capabilities extend to credit card account reconciliation\. You should be able to use the Match bank data and create reconciliation rules, based on preset criteria\. Additionally, The system also will be looking for consistency of transactions and create the rules automatically

3\.03\.04 Future State Process

In the NetSuite Orion environment with banking automation:

1. __AR Cash Application__:
	- Bank deposits flow automatically from Comerica via Bank Feeds
	- System matches deposits to open AR invoices using matching rules
	- Payments post automatically with proper cash application
2. __AP Electronic Payments__:
	- Create bill payments in NetSuite
	- Mark for electronic transfer \(ACH/wire\)
	- System automatically sends payment instructions to Comerica\. Payments to be processed can be selected before creating the nacha file
	- GL posting occurs automatically \(eliminating 42 manual JEs\)
3. __Bank Reconciliation__:
	- Bank transactions import automatically
	- Custom matching rules automatically match transactions\.
	- Review exceptions only\.
	- Click to reconcile matched transactions
4. __Credit Card Reconciliation__:
	- Same process as bank reconciliation
	- Automated matching reduces monthly effort\. Credit card matching can be automated provided that cardholders create the transaction in NetSuite upfront\. When the credit card charges are later imported, NetSuite will automatically match them\. However, in practice, many companies do not consistently have cardholders manually create these transactions\.
	- Clear exception reporting for review

This automated environment eliminates manual journal entries, reduces reconciliation time, and ensures accurate, timely financial records\.

3\.03\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.03\.01

Bank Feeds SuiteApp for automated AR cash application

Standard SuiteApp included at no additional cost

ALIGNS

REQ\-3\.03\.02

Electronic Advanced Bill Payment SuiteApp for AP ACH/wire integration

Standard SuiteApp included at no additional cost

ALIGNS

REQ\-3\.03\.03

Comerica Bank integration confirmed and supported

Verified compatibility with both SuiteApps

ALIGNS

REQ\-3\.03\.04

Support multiple FedEx accounts per warehouse location

Standard NetSuite shipping configuration

ALIGNS

REQ\-3\.03\.05

Automated bank reconciliation with custom matching rules

Standard NetSuite reconciliation with configurable rules

ALIGNS

REQ\-3\.03\.06

Credit card account reconciliation within system

Standard NetSuite functionality for card accounts

ALIGNS

REQ\-3\.03\.07

Eliminate 42 manual journal entries for ACH/wire processing

Automated through Electronic Bill Payment integration

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

3\.04\.06 Current State Process

Pivot's current collections processes in D365 are highly manual and lack integrated reporting capabilities\. The team struggles with collecting interest charges, with some customers significantly past due\. Finance charge customization is challenging \- some customers require interest fees while others do not, but the current system lacks per\-customer configuration flexibility\.

__Current State Challenges:__

- Manual collections processes requiring significant effort
- Cannot generate useful collections reports from notes added in D365
- Finance charge functionality is limited \- if finance charges print on invoice, they automatically book an entry requiring manual reversal if customer doesn't pay
- No per\-customer finance charge configuration \- system applies charges globally or not at all
- Collections notes cannot be extracted into useful reports
- Manual dunning letter processes
- Lack of sophisticated collections tools for tracking aging and payment performance

As documented during discovery: "We struggle with collecting interest charges\. Some customers we don't want to charge interest fees, others we do\. How easy is it to do that within NetSuite?" and "You can add notes in D365, but you can't get a report out that looks very good or useful" – highlighting the need for better collections management tools and flexible finance charge configuration\.

__User Story:__

- As an AR Manager, I need flexible finance charge configuration and better collections reporting so that we can effectively manage aging receivables and apply charges appropriately per customer\.

<a id="_Hlk219116189"></a>3\.04\.03 NetSuite Orion Solution

NetSuite Orion provides standard finance charge functionality that enables automated assessment of late payment fees based on configurable rules\. Finance charges can be assessed globally or per customer based on payment terms and aging thresholds\. GSI will verify whether NetSuite's finance charge functionality supports per\-customer configuration \(as requested by Kevin Baugh\) or if it is global\-only, and provide recommendations accordingly\.

__Standard Finance Charge Functionality:__
NetSuite Orion includes built\-in finance charge calculation and assessment capabilities\. The system can automatically calculate late fees based on configured percentage rates and aging periods\. Finance charges can be added to invoices as a line item after a certain time period, and unlike D365, NetSuite allows removal of the finance charge line without requiring a reversing journal entry \- users can simply remove or close the line\. This provides flexibility for Pivot's approach where finance charges may be used more as a deterrent than actual charges\. Some NetSuite clients add the finance charge line and then add a discount to offset it, creating a "doing you a favor" dynamic while maintaining the deterrent effect\.

Finance charges book to a designated income account as a separate Finance Charge Invoice—they don't modify the original invoice\. Reprinting a past\-due invoice will show the original amount only; any assessed finance charges appear on their own invoice\(s\)\. Here is a link to the NetSuite help docs on this feature\. This link will provide more information [https://docs\.oracle\.com/en/cloud/saas/netsuite/ns\-online\-help/section\_N1301640\.html](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1301640.html)

See appendix for additional information\.

__Collections Reporting and Notes:__
NetSuite Orion provides integrated collections dashboards and reporting that extract collections notes into useful reports, addressing Pivot's current pain point where "you can add notes in D365, but you can't get a report out that looks very good or useful\." Collections notes, activities, and aging information are integrated into standard reports and dashboards, eliminating the need for manual report compilation\.

3\.04\.04 Future State Process

__Phase 1 \(Standard Finance Charges\):__

1. __Finance Charge Configuration__:
	- GSI verifies per\-customer vs\. global finance charge capability
	- Configure finance charge rules based on payment terms and aging thresholds
	- Set up customer\-specific finance charge exceptions supported by native functionality\.
	- Configure finance charge calculation rates and periods
2. __Finance Charge Assessment__:
	- System automatically calculates finance charges based on aging and payment terms
	- Finance charges added as line items to invoices after configured time period
	- Users can remove or close finance charge lines without reversing journal entries
	- Option to add offsetting discounts for strategic customer management

3\.04\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.04\.01

Explore NetSuite's basic finance charge functionality

Standard NetSuite finance charge capability

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214911991"></a>__3\.05 Accounts Payable Automation__

Avanto white paper

[https://acrobat\.adobe\.com/id/urn:aaid:sc:US:90f2cd13\-cfb3\-4262\-b56f\-0e4d9209ca46?viewer%21megaVerb=group\-discover](https://acrobat.adobe.com/id/urn:aaid:sc:US:90f2cd13-cfb3-4262-b56f-0e4d9209ca46?viewer%21megaVerb=group-discover)

3\.05\.01 Your Business Requirements

- __REQ\-3\.05\.01__: Automated standalone expense vendor bill processing Phase 1 \(ACCOMMODATE\)
- __REQ\-3\.05\.02__: Dedicated inbox for expense invoice forwarding \(ACCOMMODATE\)
- __REQ\-3\.05\.03__: Approval workflow for auto\-created vendor bills \(ACCOMMODATE\)
- __REQ\-3\.05\.04__: Phase 2 inclusion of AP automation, to a later phase \(Avanto, ezCollect, Proprio solutions\) \(ACCOMMODATE\)
- __REQ\-3\.05\.05__: Automated vendor invoice follow\-up capability \(ACCOMMODATE \- Future Phase\)

3\.05\.02 Current State Process

Pivot currently processes standalone expense vendor bills manually\. When expense invoices arrive \(utilities, rent, insurance, etc\.\), the AP team must:

1. Receive invoice in email
2. Forward to manager \(e\.g\., Ken\) for approval
3. Wait for approval response
4. Manually enter bill into system
5. Mark as approved and post

This process is cumbersome, creates delays, and risks bills being forgotten in hold status awaiting approval\.

__Current State Challenges:__

- Manual entry of standalone expense vendor bills
- Email\-based approval process is inefficient
- Risk of forgetting bills in hold status
- Time\-consuming for routine expense invoices
- No automated tracking or follow\-up

__User Story:__

- As an AP Manager, I need automated processing for standalone expense invoices so that we can eliminate manual entry, streamline approvals, and reduce the risk of missing bills\.

3\.05\.03 NetSuite Orion Solution

Pivot requires accommodation through custom AP automation workflow for standalone expense vendor bills\. This custom solution will be scoped for Phase 1 inclusion, pending timeline and budget analysis\. Pending decision based on offered solutions\.

__Email\-to\-Vendor\-Bill Automation:__
A dedicated email inbox will be configured for expense invoice forwarding\. When invoices are received at this inbox, automated processing will:

1. Extract invoice data from PDF attachments
2. This requirement can be met using NetSuite’s native allocation functionality\.
3. Attach PDF to vendor bill record
4. Route requests the appropriate approver based on predefined rules\. Reminders or saved searches can be used to support this process\.

__Technical Approach:__
The custom automation will leverage NetSuite's email integration framework to monitor the dedicated inbox and extract vendor, amount, date, and GL account information from PDF attachments\. Automated workflows will create vendor bill records with proper approval routing based on configurable thresholds and GL account classifications\. The solution will include exception handling for invoices that cannot be parsed automatically, routing them to a manual review queue\.

__Automated Approval Workflow:__
Auto\-created vendor bills will be placed in unapproved state and routed through configurable approval workflows\. Approvers will receive notifications, can review bills with attached PDFs in NetSuite Orion, and approve/reject directly in the system\. Upon approval, bills post automatically to GL\. This eliminates the manual email\-based approval process and ensures bills are tracked in the system from receipt through payment\.

__Phase 1 Inclusion Decision:__
The AP automation solution requires custom development and integration effort\. GSI will provide timeline and hour impact analysis to determine feasibility of Phase 1 inclusion\. If scope or budget constraints necessitate deferral, this functionality can be implemented in Phase 2 while using standard manual bill entry processes in Phase 1\.

__Future Phase: Vendor Invoice Follow\-Up:__
Automated vendor invoice follow\-up capability \(tracking expected invoices, sending reminders to vendors\) is acknowledged as a valuable future enhancement but is planned for Phase 2 or Phase 3 implementation\.

3\.05\.04 Future State Process

__Phase 1 \(with AP automation\) third party solution:__

1. Expense invoices forwarded to dedicated email inbox
2. System automatically creates vendor bill from PDF
3. PDF attached to vendor bill record
4. Approval workflow routes to designated approver
5. Approver reviews and approves in NetSuite
6. Bill posts automatically to GL

__Phase 1 \(without AP automation \- if deferred\):__

1. Manual vendor bill entry continues
2. Standard NetSuite approval workflow used
3. AP automation implemented in Phase 2

__Future Phase:__

- Automated vendor invoice follow\-up and tracking

3\.05\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.05\.01

Automated standalone expense vendor bill processing Phase 1

Custom email\-to\-VB workflow with PDF parsing

ACCOMMODATE

REQ\-3\.05\.02

Dedicated inbox for expense invoice forwarding

Email integration configuration

ACCOMMODATE

REQ\-3\.05\.03

Approval workflow for auto\-created vendor bills

Custom approval routing for auto\-created bills

ACCOMMODATE

REQ\-3\.05\.04

Phase 1 inclusion of AP automation

Timeline/budget analysis required

ACCOMMODATE

REQ\-3\.05\.05

Automated vendor invoice follow\-up capability

Future phase enhancement

ACCOMMODATE \(Future\)

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214911992"></a>__3\.06 Tax Management__

3\.06\.01 Your Business Requirements

- __REQ\-3\.06\.01__: Evaluate SuiteTax vs Avalara with cost\-benefit analysis\. The Pivot team will validate this\. Report generation can be automated based on required dates\. Avalara maintains NetSuite connectors to deliver end\-to\-end compliance solutions\.
- __REQ\-3\.06\.02__: SuiteTax included in NetSuite platform at no additional cost \(ALIGNS\)
- __REQ\-3\.06\.03__: Tax tables automatically updated monthly \(ALIGNS\)
- __REQ\-3\.06\.04__: SuiteTax supports exemption management for resale certificates \(ALIGNS\)
- __REQ\-3\.06\.05__: Economic nexus monitoring reports for unregistered states \(ALIGNS\)
- __REQ\-3\.06\.06__: Specific taxable item in catalog for asset purchases \(ACCOMMODATE\)
- __REQ\-3\.06\.07__: Support for 37\+ states sales tax collection \(ALIGNS\)
- __REQ\-3\.06\.08__: Tax filing approach decision \(in\-house, CPA, or Avalara\) \(ADAPT\)

3\.06\.02 Current State Process

Pivot collects sales tax across 37\+ states and currently uses third\-party support for tax management\. The organization needs to evaluate whether to bring tax management in\-house using SuiteTax, continue with external CPA support, or use Avalara's managed filing service\.

__Current State Challenges:__

- Multi\-state tax compliance complexity \(37\+ states\)
- Third\-party costs for tax filing services
- Economic nexus monitoring requirements
- Resale certificate management
- Use tax on fixed asset purchases
- Monthly tax table maintenance

__Decision Required:__

- Platform selection: SuiteTax vs\. Avalara
- Filing approach: In\-house vs\. CPA vs\. Avalara managed service
- Cost\-benefit analysis of alternatives

__User Story:__

- As a CFO, I need to evaluate tax management options so that we can optimize costs while maintaining compliance across 37\+ states\.

3\.06\.03 NetSuite Orion Solution

NetSuite Orion includes the SuiteTax platform at no additional cost, providing comprehensive multi\-state tax management for Pivot's 37\+ state compliance requirements\. SuiteTax automatically calculates sales tax on transactions, updates tax rates and rules monthly, manages exemption certificates and resale transactions, and provides economic nexus monitoring reports for unregistered states\. The item catalog will be configured with specific taxable items for fixed asset purchases to ensure proper use tax calculation supporting property tax reporting\.

Pivot must decide between SuiteTax \(included, no cost\) and Avalara \(subscription cost with managed filing services\)\. SuiteTax handles calculation and provides filing reports; Avalara additionally files returns on Pivot's behalf\. Separately, Pivot must decide whether to file returns in\-house using SuiteTax reports \(lowest cost, highest effort\), continue with CPA support \(moderate cost\), or use Avalara managed filing \(highest cost, lowest effort\)\. Baker Tilly is providing cost analysis to inform these decisions\.

3\.06\.04 Future State Process

__Tax Calculation \(Regardless of Filing Approach\):__

1. SuiteTax calculates sales tax automatically on transactions
2. Tax tables update automatically monthly
3. Exemption certificates managed in system
4. Economic nexus monitoring reports run quarterly/annually

__Tax Filing \(Decision\-Dependent\):__

- __Option A \- In\-House__: Extract SuiteTax reports, file returns directly with states
- __Option B \- CPA Support__: Provide SuiteTax reports to CPA firm for filing
- __Option C \- Avalara__: Avalara files returns automatically using integrated data

3\.06\.05 Decision Matrix

__Req \#__

__Requirement__

__Info__

__Implementation Approach__

__REQ\-3\.06\.01__

Evaluate SuiteTax vs Avalara with cost\-benefit analysis

Decision pending cost analysis from Baker Tilly

__ADAPT__

__REQ\-3\.06\.02__

SuiteTax included in NetSuite platform at no additional cost

No incremental licensing cost

__ALIGNS__

__REQ\-3\.06\.03__

Tax tables automatically updated monthly

Standard SuiteTax functionality

__ALIGNS__

__REQ\-3\.06\.04__

SuiteTax supports exemption management for resale certificates

Standard exemption certificate tracking

__ALIGNS__

__REQ\-3\.06\.05__

Economic nexus monitoring reports for unregistered states

Standard SuiteTax reporting

__ALIGNS__

__REQ\-3\.06\.06__

Specific taxable item in catalog for asset purchases

Custom item configuration for use tax

__ACCOMMODATE__

__REQ\-3\.06\.07__

Support for 37\+ states sales tax collection

Standard SuiteTax multi\-state capability

__ALIGNS__

__REQ\-3\.06\.08__

Tax filing approach decision \(in\-house, CPA, or Avalara\)

Resource allocation decision pending

__ADAPT__

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214911993"></a>__3\.07 Fixed Asset Management__

3\.07\.01 Your Business Requirements

- __REQ\-3\.07\.01__: Bring fixed asset management in\-house to replace third\-party\. The fix assets module will be included in phase 2
-  \(ACCOMMODATE\)
- __REQ\-3\.07\.02__: NetSuite Fixed Asset Module at $4,500 annual cost\. This will be  implemented for phase 2\. \(ACCOMMODATE\)
- __REQ\-3\.07\.03__: AP invoice coding integrates automatically into FAM \(ALIGNS\)
- __REQ\-3\.07\.04__: Track 300\-500 assets post\-cleanup \(ALIGNS\)
- __REQ\-3\.07\.05__: Implement $2,500 capitalization threshold \(ADAPT\)
- __REQ\-3\.07\.06__: Standard depreciation rules 5\-10 years useful life \(ALIGNS\)
- __REQ\-3\.07\.07__: Data migration from Excel\-based fixed asset reports \(ALIGNS\)
- __REQ\-3\.07\.08__: Carry assets with net book value of zero \(ALIGNS\)
- __REQ\-3\.07\.09__: Phase 1 inclusion evaluation with budget/timeline impact \(ACCOMMODATE\)
- __REQ\-3\.07\.10__: SuiteTax integration with FAM for use tax and property tax \(ACCOMMODATE\)

3\.07\.02 Current State Process

Pivot currently uses a third\-party service provider for fixed asset management\. The provider maintains asset records in Excel and provides depreciation reports\. Pivot is considering bringing fixed asset management in\-house using NetSuite's Fixed Asset Module to reduce third\-party costs and improve integration\.

As noted during the fixed asset discovery session: "Normally we have the third party manage our fixed asset\.\.\. So that's why I need to know more detail about how NetSuite Orion can provide that to us" – indicating the desire to bring asset management in\-house for cost savings and improved integration with AP and GL processes\.

__Current State:__

- 500\+ assets currently tracked \(cleanup will reduce to 300\-500\)
- Third\-party service provides Excel\-based reporting
- Currently do not follow $2,500 capitalization threshold consistently
- Standard depreciation: 5\-10 years useful life \(leasehold improvements up to 10 years based on lease term\)
- Assets with NBV of zero are retained on books

__Business Drivers:__

- Cost savings from eliminating third\-party service
- Improved integration between AP and fixed assets\. This will be included on phase 2

In NetSuite, AP sales/use tax accruals are recorded by entering vendor bills with the correct tax codes, automatically calculating and posting liabilities to the sales/use tax payable account\. Period\-end accruals capture unpaid or partially processed bills, and payments adjust the liability accordingly\. Integrations with tools like Avalara, along with saved searches, reports, and recurring journal entries, automate calculations, posting, and filing, ensuring timely compliance\. Best practices include proper vendor tax coding, monthly reconciliations, and exception reviews to maintain accuracy and control\.

- Real\-time visibility into asset data
- Automated depreciation processing
- Integration with tax management for property tax reporting

__User Story:__

- As a Controller, I need integrated fixed asset management so that we can reduce third\-party costs, improve real\-time visibility, and streamline asset tracking with automatic AP integration\.

3\.07\.03 NetSuite Orion Solution

NetSuite's Fixed Asset Module \(FAM\) provides comprehensive asset management with direct integration to AP, GL, and SuiteTax\. The module \($4,500 annual license\) will replace third\-party service costs\. FAM automatically creates asset records when AP invoices are coded to asset accounts, calculates and posts monthly depreciation based on configured rules \(5\-10 years useful life\), and supports Pivot's 300\-500 assets well within system capacity\. Standard functionality includes carrying assets with net book value of zero for physical tracking, plus depreciation schedules, acquisition reports, and property tax reports\. If an AP invoice is mistakenly coded to an asset, you can reverse or edit the invoice to post it to the correct account\. If the invoice was already capitalized in FAM, the asset record must be adjusted or retired, which will automatically update future depreciation\. NetSuite recalculates depreciation based on the corrected asset cost, ensuring schedules remain accurate, though prior depreciation may need to be reversed\. Proper reconciliation of AP, assets, and depreciation is recommended after any corrections\.

Implementation of FAM provides opportunity to enforce consistent $2,500 capitalization threshold \(not currently followed\), representing a process improvement aligning with accounting best practices\. Fixed asset data will be migrated from the third\-party provider's Excel reports through standard migration process\. FAM integrates with SuiteTax for use tax calculation on asset purchases and property tax reporting, including 571L property tax return support \(to be confirmed\)\.

The Phase 1 decision hinges on budget impact \($4,500 annual license plus implementation effort\), timeline impact \(additional Phase 1 scope\), business value \(immediate third\-party cost savings\), and integration benefit \(clean integration from inception vs\. post\-implementation retrofit\)\. GSI will provide timeline and budget analysis to support Pivot's decision\.

3\.07\.04 Future State Process

__With FAM in Phase 1:__

1. __Asset Acquisition__:
	- Code AP invoice to asset account
	- FAM automatically creates asset record
	- Depreciation rules applied based on asset type
2. __Monthly Depreciation__:
	- FAM calculates depreciation automatically
	- Depreciation entries post to GL
	- Depreciation schedules available in real\-time
3. __Asset Disposal__:
	- Record disposal in FAM
	- System calculates gain/loss
	- GL entries post automatically
4. __Property Tax Reporting__:
	- FAM provides depreciation reports for property tax
	- Integration with SuiteTax for use tax and property tax
	- 571L tax return support \(to be confirmed\)

__Without FAM in Phase 1:__

- Continue with third\-party service for Phase 1\.
- Implement FAM in Phase 2
- Integration added post\-go\-live

3\.07\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.07\.01

Bring fixed asset management in\-house to replace third\-party

NetSuite FAM replaces third\-party service

ACCOMMODATE

REQ\-3\.07\.02

NetSuite Fixed Asset Module at $4,500 annual cost

Additional annual license fee

ACCOMMODATE

REQ\-3\.07\.03

AP invoice coding integrates automatically into FAM

Standard FAM integration with AP

ALIGNS

REQ\-3\.07\.04

Track 300\-500 assets post\-cleanup

Well within FAM capacity

ALIGNS

REQ\-3\.07\.05

Implement $2,500 capitalization threshold

Process change from current practice

ADAPT

REQ\-3\.07\.06

Standard depreciation rules 5\-10 years useful life

Standard FAM depreciation rules

ALIGNS

REQ\-3\.07\.07

Data migration from Excel\-based fixed asset reports

Standard data migration from third\-party

ALIGNS

REQ\-3\.07\.08

Carry assets with net book value of zero

Standard FAM functionality

ALIGNS

REQ\-3\.07\.09

Phase 1 inclusion evaluation with budget/timeline impact

Decision pending impact analysis

ACCOMMODATE

REQ\-3\.07\.10

SuiteTax integration with FAM for use tax and property tax

Custom integration configuration

ACCOMMODATE

__*Client Feedback*__

__*GSI Response*__

<Comment>

 

## <a id="_Toc214911994"></a>__3\.08 Document Management__

3\.08\.01 Your Business Requirements

- __REQ\-3\.08\.01__: Explore dynamic terms and conditions capability \(ACCOMMODATE\)
- __REQ\-3\.08\.02__: Global terms with customer\-specific exceptions for MSA \(ACCOMMODATE\)
- __REQ\-3\.08\.03__: Different document numbers between proforma invoice and invoice \(ACCOMMODATE\)

3\.08\.02 Current State Process

Pivot currently uses global terms and conditions on quotes and invoices, but when Master Service Agreements \(MSAs\) dictate different terms, they must print quotes without the standard verbiage\. This manual workaround is inefficient and creates risk of using incorrect terms\.

__Current State Challenges:__

- Global T&Cs don't accommodate customer\-specific MSA requirements
- Risk of using incorrect terms for MSA customers
- Need for different document numbers between proforma and final invoices

__User Story:__

- As a Sales Operations Manager, I need dynamic terms and conditions so that we can automatically apply customer\-specific MSA terms without manual workarounds\.

3\.08\.03 NetSuite Orion Solution

NetSuite Orion will accommodate Pivot's requirement for dynamic terms and conditions through custom document generation logic\. This solution requires a workshop session to define detailed requirements and design the custom T&C management approach\.

__Dynamic Terms & Conditions:__
Custom logic will enable management of global default terms and conditions with customer\-specific exceptions\. When MSAs dictate alternative terms, customer records will store the customer\-specific T&C language\. Document generation \(quotes, invoices\) will automatically select the appropriate T&C text based on customer configuration, eliminating manual workarounds\.

__Custom Document Numbering:__
Standard NetSuite assigns the same document number to proforma invoices and final invoices\. Pivot requires different document numbers for these document types\. Custom document numbering logic will accommodate this requirement, ensuring proforma invoices receive separate numbering from final invoices\.

__Implementation Approach:__
A Terms and Conditions workshop \(scheduled for 30 minutes\) will capture detailed requirements including:

- T&C text variations needed
- Customer assignment logic
- Document types requiring T&Cs
- Approval workflows for T&C changes
- Exception handling rules

3\.08\.04 Future State Process

1. __Customer Setup__:
	- Configure global default T&Cs
	- Assign customer\-specific T&Cs for MSA customers
2. __Document Generation__:
	- System selects appropriate T&C text based on customer
	- Proforma invoices receive unique document numbers
	- Final invoices receive separate document numbers
3. __Maintenance__:
	- Update T&C text as needed
	- Reassign customers when MSAs change

3\.08\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.08\.01

Explore dynamic terms and conditions capability

Custom T&C management logic required; workshop needed

ACCOMMODATE

REQ\-3\.08\.02

Global terms with customer\-specific exceptions for MSA

Custom customer\-specific T&C assignment

ACCOMMODATE

REQ\-3\.08\.03

Different document numbers between proforma invoice and invoice

Custom document numbering logic

ACCOMMODATE

__*Client Feedback*__

__*GSI Response*__

<Comment>

 

## <a id="_Toc214911995"></a>__3\.09 Expense Management__

3\.09\.01 Your Business Requirements

- __REQ\-3\.09\.01__: Expensify integration for expense reporting \(ALIGNS\)
- __REQ\-3\.09\.02__: Corporate credit card reconciliation automation \(ADAPT\)
- __REQ\-3\.09\.03__: Project coordinators submit expenses with PO identification \(ALIGNS\)

3\.09\.02 Current State Process

Pivot currently uses Expensify for expense reporting\. Project coordinators submit expenses through Expensify with PO identification for project expense tracking\. Corporate credit card reconciliation requires manual effort each month to match transactions\.

__Current State:__

- Expensify is used for employee expense reporting
- Project coordinators include PO numbers for expense allocation
- Monthly credit card reconciliation is manual process requiring "order hitting"

__User Story:__

- As an Accounting Manager, I need automated credit card reconciliation so that we can reduce monthly manual effort and ensure timely expense processing\.

3\.09\.03 NetSuite Orion Solution

NetSuite Orion provides standard integration with Expensify, enabling continued use of Pivot's current expense management tool while integrating expense reports directly into NetSuite's AP module\.

__Expensify Integration:__
NetSuite offers a standard Expensify connector that synchronizes expense reports from Expensify into NetSuite\. Approved expense reports in Expensify automatically create expense report records in NetSuite with line\-level detail, PO references, and project allocation\. This integration is proven and requires minimal configuration\.

__Project Expense Tracking:__
NetSuite's standard expense report functionality supports PO identification and project allocation\. When project coordinators submit expenses in Expensify with PO references, those references flow through to NetSuite Orion for accurate project cost tracking and expense reporting\.

__Corporate Credit Card Reconciliation:__
NetSuite's Bank Feeds functionality \(discussed in Section 3\.03\) extends to credit card accounts, enabling automated matching of credit card transactions to expense reports and other transactions\. This adaptation will replace Pivot's current manual "order hitting" process with automated matching rules, significantly reducing monthly reconciliation effort while maintaining accuracy\.

3\.09\.04 Future State Process

1. __Expense Submission__:
	- Employees submit expenses in Expensify \(no change\)
	- Include PO numbers for project expenses
	- Supervisor approves in Expensify
2. __Integration to NetSuite__:
	- Approved expense reports sync to NetSuite Orion automatically
	- Expense reports created in NetSuite Orion with line detail
	- PO references and project allocation preserved
3. __Credit Card Reconciliation__:
	- Credit card transactions import via Bank Feeds
	- Automated matching rules match to expense reports
	- Review exceptions only
	- Reconcile matched transactions

3\.09\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.09\.01

Expensify integration for expense reporting

Standard NetSuite/Expensify connector

ALIGNS

REQ\-3\.09\.02

Corporate credit card reconciliation automation

Process improvement using Bank Feeds for cards

ADAPT

REQ\-3\.09\.03

Project coordinators submit expenses with PO identification

Standard NetSuite expense report functionality

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214911996"></a>__3\.10 Payroll Integration__

3\.10\.01 Your Business Requirements

- __REQ\-3\.10\.01__: UKG payroll journal entry CSV import template \(ALIGNS\)
- __REQ\-3\.10\.02__: Create CSV import map for UKG payroll integration \(ALIGNS\)

3\.10\.02 Current State Process

Pivot uses UKG \(Ultimate Kronos Group\) for payroll processing\. The current process requires manual transformation and import of payroll journal entries from UKG into D365\. Connie Chung downloads payroll data from UKG in Excel format, uses a template provided by UKG, and then uploads that template into D365\. The template may include macros or manual data rearrangement to properly format the data for import, and includes department tagging for proper cost allocation\.

__Current State Challenges:__

- Manual download from UKG in Excel format
- Template manipulation required \(may include macros\)
- Manual upload process into D365
- Risk of data entry errors during transformation
- Time\-consuming process for each payroll cycle
- Department allocation must be handled during import process

As documented during discovery: "I normally download from UKG in Excel and then using whatever the format that they have the template for me to use and then I using that template to upload back into the D365\. So I hope pretty much the same thing with Orion" – indicating the process should be similar but streamlined in NetSuite\.

__User Story:__

- As a Payroll Accountant, I need automated payroll JE import from UKG so that we can eliminate manual entry, reduce errors, and ensure accurate, timely GL posting with proper department allocation\.

3\.10\.03 NetSuite Orion Solution

NetSuite Orion provides standard CSV import functionality for journal entries\. GSI will work with Pivot to review the current UKG export template and create a NetSuite Orion CSV import map that replicates and improves upon the current D365 import process\. NetSuite calls this a "CSV import map" \- a configuration tool that defines how UKG's payroll journal entry export format maps to NetSuite's journal entry import format\.

__CSV Import Map Configuration:__
GSI will review Pivot's current UKG template to understand the data structure and any transformations currently being performed \(including macros if present\)\. The NetSuite Orion CSV import map will be configured to:

- Map column mappings \(UKG field → NetSuite field\)
- Map account mappings \(UKG accounts → NetSuite COA\)
- Handle data transformations \(date formats, number formats, etc\.\)
- Configure department allocation and tagging
- Set up validation rules to catch errors before import
- Replicate any current template logic or macros in NetSuite's import mapping

__Import Process:__
Once the CSV import map is configured, importing payroll journal entries becomes a simple, repeatable process that mirrors Pivot's current workflow:

1. Export payroll journal entry from UKG in CSV format \(same as current process\)
2. Upload CSV file to NetSuite
3. Select UKG Payroll CSV import map
4. Review validation results and error reports
5. Process import to create journal entries automatically
6. Review imported journal entries before posting

This standard NetSuite Orion functionality requires no custom development, only configuration of the import map to match UKG's data format\. GSI will work with Connie to ensure the NetSuite Orion import map handles all current template requirements including department tagging and any data transformations currently performed manually or through macros\.

3\.10\.04 Future State Process

In the NetSuite Orion environment with UKG payroll integration:

1. __Payroll Processing \(No Change\)__:
	- Process payroll in UKG \(unchanged from current process\)
	- Export payroll journal entry to CSV format \(same export as current\)
2. __CSV Import to NetSuite__:
	- Upload CSV file to NetSuite \(no template manipulation required\)
	- Select pre\-configured UKG Payroll CSV import map
	- System automatically validates data format and account mappings
	- Review validation results and error reports \(if any\)
	- System transforms data and creates journal entries automatically
	- Department allocation handled automatically through import map configuration
3. __Journal Entry Review and Posting__:
	- Review imported journal entries in NetSuite
	- Verify account mappings and department allocations
	- Post journal entries to GL
	- Journal entries flow to project accounting and financial reporting automatically

__Benefits:__

- Eliminates manual template manipulation and macros
- Reduces risk of data entry errors through automated validation
- Faster import process with built\-in error checking
- Consistent department allocation through configured mapping
- Audit trail of all imports maintained in NetSuite

3\.10\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.10\.01

UKG payroll journal entry CSV import template

Standard NetSuite CSV import functionality

ALIGNS

REQ\-3\.10\.02

Create CSV import map for UKG payroll integration

Configuration of import mapping rules

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214911997"></a>__3\.11 Chart of Accounts__

3\.11\.01 Your Business Requirements

- __REQ\-3\.11\.01__: Baseline NetSuite Orion COA with client\-specific modifications \(ALIGNS\)
- __REQ\-3\.11\.02__: Finalize and deliver scrubbed chart of accounts \(ALIGNS\)

3\.11\.02 Current State Process

Pivot's chart of accounts from D365 requires review and rationalization for NetSuite Orion implementation\. GSI provided a baseline NetSuite Orion COA that reflects furniture dealer best practices, developed in collaboration with Miller Knoll and pilot dealers\. The baseline COA includes some Canadian accounts since one of the pilot dealers is Canadian, but the overall framework is designed for contract furniture dealers\.

__Current State:__

- D365 COA structure needs scrubbing and rationalization
- Some accounts may be redundant or no longer needed
- Account numbering system may need adjustment
- Need to identify accounts not in baseline that are required for Pivot's operations

__Review Process:__
The Pivot team \(led by Kevin Baugh\) reviewed the baseline NetSuite Orion COA and found the overall framework acceptable\. As Ken Baugh noted: "As long as we have the ability to add accounts which, you know, there's certain things that we'll track\. I think the overall framework is flexible enough\. I mean, it works\. That would be my take\. And then we can use\. We can change the numbering system as well\."

__Status:__

- Baseline NetSuite Orion COA provided to Pivot team early in discovery
- Initial review complete \- framework acceptable with flexibility to add accounts and modify numbering
- Pivot team scrubbed current D365 COA list
- Finalized scrubbed list received from Kevin Baugh \(KBM\) on 8/13
- Complete COA requirements delivered for deployment configuration

__User Story:__

- As a Controller, I need a chart of accounts that maintains our required account structure while leveraging industry best practices, so that we can streamline financial reporting and ensure proper account organization\.

3\.11\.03 NetSuite Orion Solution

NetSuite Orion provides a baseline chart of accounts structure designed for contract furniture dealers, incorporating industry best practices and common account structures developed in collaboration with Miller Knoll and pilot dealers\. This baseline serves as the starting point for Pivot's COA configuration, reducing setup effort while providing a tailored framework\.

__COA Configuration Approach:__
GSI will configure Pivot's NetSuite Orion COA using the finalized scrubbed list provided by Kevin Baugh \(completed 8/13\)\. The configuration process includes:

- Start with the NetSuite Orion baseline COA structure as a foundation
- Add Pivot\-specific accounts identified during COA scrubbing
- Modify account numbering system to match Pivot's preferences \(not limited to 4\-digit numbering\)
- Map all D365 accounts to new NetSuite COA accounts
- Configure account hierarchies for financial reporting
- Set up account types, sub\-accounts, and parent\-child relationships
- Configure account segments for department/project tracking if needed

__Account Numbering Flexibility:__
As confirmed during discovery, Pivot has full flexibility to modify the account numbering system\. The baseline uses a 4\-digit numbering scheme, but Pivot can change this to match their preferences or D365 numbering if desired\. NetSuite Orion supports various numbering formats and account code structures\.

__Import Process:__
Once the finalized COA is configured, GSI will import all accounts into NetSuite Orion using the scrubbed list provided by Kevin Baugh\. This is one of the very first configuration tasks after discovery, as noted: "There's not much we can do without a chart of accounts\. So that's like really one of the very first things\."

The baseline COA reduces configuration effort by providing a tailored starting point while allowing full flexibility for client\-specific modifications, ensuring Pivot's COA meets their unique business requirements while leveraging industry best practices\.

3\.11\.04 Future State Process

In the NetSuite Orion environment with configured chart of accounts:

1. __COA Finalization \(Completed 8/13\)__:
	- Pivot team \(Kevin Baugh\) scrubbed current D365 COA
	- Identified required accounts not in baseline Orion COA
	- Removed redundant or obsolete accounts
	- Delivered finalized COA requirements spreadsheet to GSI
2. __COA Configuration \(Phase 1 \- Early Configuration\)__:
	- GSI imports finalized COA into NetSuite Orion based on Kevin Baugh's scrubbed list
	- Maps all D365 accounts to corresponding NetSuite Orion accounts
	- Configures account hierarchies and parent\-child relationships
	- Sets up account types, sub\-accounts, and account segments
	- Configures account numbering system per Pivot's preferences
	- Validates account structure with Pivot team
3. __Account Mapping and Data Migration__:
	- Historical GL data mapped from D365 accounts to NetSuite accounts
	- Opening balances imported using account mapping
	- Validation of account mappings before data migration
4. __Ongoing Maintenance__:
	- Standard NetSuite account maintenance processes
	- Account change controls and approval workflows
	- Ability to add new accounts as business needs evolve
	- Account hierarchy modifications as organizational structure changes

__Benefits:__

- Industry best practices built into baseline structure
- Flexibility to customize for Pivot's specific needs
- Streamlined setup using a tailored framework
- Proper account organization for financial reporting
- Foundation for all other financial module configuration

3\.11\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.11\.01

Baseline NetSuite Orion COA with client\-specific modifications

NetSuite Orion baseline COA with Pivot\-specific additions

ALIGNS

REQ\-3\.11\.02

Finalize and deliver scrubbed chart of accounts

Completed 8/13 by Kevin Baugh

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214911998"></a>__3\.12 Period Close__

3\.12\.01 Your Business Requirements

- __REQ\-3\.12\.01__: Maintain or improve 7\-day period close performance \(ALIGNS\)
- __REQ\-3\.12\.02__: Official period close process with walkthroughs and checklists \(ALIGNS\)

3\.12\.02 Current State Process

Pivot currently closes accounting periods in 7 working days, which is above average performance for their industry\. The organization wants to maintain or improve upon this performance level while implementing proper period close controls and procedures\.

__Current State:__

- 7\-day period close cycle \(above average\)
- Manual processes contribute to close timeline
- Need for formalized close process and checklists

__User Story:__

- As a Controller, I need to maintain our 7\-day close performance while implementing proper controls and automation so that we can continue providing timely financial reporting\.

3\.12\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive period close functionality including official accounting period close processes, automated controls, and standard checklists to ensure consistent, efficient period closes\.

__Period Close Capabilities:__

- __Period Locking__: Close accounting periods to prevent backdated transactions

See appendix

- __AR/AP Locking__: Lock receivables and payables separately during close process
- __Close Checklists__: Standard NetSuite Orion close checklist functionality to track required close tasks
- __Automated Close Tasks__: System\-generated journal entries \(e\.g\., accrued revenue, depreciation\) streamline close process
- __Close Walkthroughs__: GSI will provide period close training and walkthrough documentation
- __Real\-Time Visibility__: Continuous access to financial data accelerates close process

__Performance Improvement Opportunities:__
Several automated processes discussed in this BRD will improve close efficiency:

- Automated bank reconciliation \(Section 3\.03\)
- Automated accrued revenue journal entries \(Section 3\.01\)
- Automated depreciation if FAM implemented \(Section 3\.07\)
- Electronic payment integration eliminating 42 manual JEs \(Section 3\.03\)
- Reduced manual AR cash application \(Section 3\.03\)

These automations should enable Pivot to maintain or improve upon its current 7\-day close performance\.

3\.12\.04 Future State Process

__Monthly Period Close:__

1. __Pre\-Close__ \(Days 1\-3\):
	- Automated bank reconciliation
	- Automated accrued revenue JEs
	- Automated depreciation posting \(if FAM implemented\)
	- Review dashboards for exceptions
2. __Close Activities__ \(Days 4\-6\):
	- Process manual adjusting entries
	- Review close checklist completion
	- Lock AR and AP
	- Generate financial statements
3. __Review & Lock__ \(Day 7\):
	- Management review of financials
	- Close accounting period
	- Lock GL to prevent backdating

3\.12\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.12\.01

Maintain or improve 7\-day period close performance

Automation improvements should maintain/improve performance

ALIGNS

REQ\-3\.12\.02

Official period close process with walkthroughs and checklists

Standard NetSuite period close functionality \+ GSI training

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214911999"></a>__3\.13 Budgeting & Planning__

3\.13\.01 Your Business Requirements

- __REQ\-3\.13\.01__: Evaluate NSPB vs\. continuing with Adaptive Planning \(ADAPT\)
- __REQ\-3\.13\.02__: Prior year data import capabilities for budgeting system \(ALIGNS\)

3\.13\.02 Current State Process

Pivot currently uses Adaptive Planning for budgeting and planning\. With the NetSuite Orion  implementation, they need to evaluate whether NetSuite Planning and Budgeting \(NSPB\) provides sufficient functionality to replace Adaptive Planning, or whether continuing with Adaptive Planning is the better approach\.

__Evaluation Criteria:__

- NSPB capabilities vs\. Adaptive Planning features
- Integration benefits of NSPB with NetSuite Orion
- Cost comparison
- User experience and learning curve
- Prior year data import requirements

__User Story:__

- As a Financial Planning Manager, I need to evaluate budgeting platform options so that we can optimize integration with NetSuite Orion while maintaining our planning capabilities\.

3\.13\.03 NetSuite Orion Solution

NetSuite offers both native budgeting tools \(NSPB\) and proven integration with Adaptive Planning, providing flexibility in budgeting platform selection\.

__NetSuite Planning and Budgeting \(NSPB\):__
NSPB is NetSuite's native planning and budgeting module with direct integration to GL actuals\. Capabilities include:

- Multi\-year, multi\-scenario planning
- Driver\-based budgeting models
- Variance reporting \(budget vs\. actual\) Orion can generate backlog reports\.
- Department and project\-level budgets
- Rolling forecast capabilities
- Prior year data import from GL actuals
- Automated Budgeting & Forecasting: Pulls actuals directly from NetSuite, creates rolling forecasts, and identifies trends using embedded AI/ML for faster, more accurate plans\.
- __Scenario Modeling \("What\-If"\):__ Allows creation and comparison of multiple financial scenarios \(best, worst, baseline\) to prepare for uncertainty\.
- __Real\-Time Insights & Dashboards:__ Provides live dashboards and reporting with drill\-downs to visualize performance against targets\.

__Adaptive Planning Integration:__
If Pivot chooses to continue with Adaptive Planning, NetSuite provides standard integration capabilities to synchronize actual data from NetSuite into Adaptive Planning\. This integration enables:

- Automated actual data feeds to Adaptive Planning
- Prior year data import from NetSuite GL
- Consistent reporting between actual \(NetSuite\) and budget \(Adaptive\)

__Decision Process:__
Pivot needs to:

1. Review NSPB capabilities against current Adaptive Planning usage
2. Assess which features are critical vs\. nice\-to\-have
3. Compare total cost of ownership
4. Evaluate change management impact
5. Make platform decision before implementation

Prior year data import capabilities exist for both options, ensuring historical data is available regardless of platform choice\.

3\.13\.04 Future State Process

__Option A \- NSPB: Preferred__

1. Configure NSPB for Pivot's budgeting structure
2. Import prior year actuals from NetSuite GL
3. Build budgeting models in NSPB
4. Train users on NSPB functionality
5. Execute budgeting process in NSPB

__Option B \- Adaptive Planning:__

1. Configure integration between NetSuite and Adaptive Planning
2. Import prior year actuals from NetSuite GL to Adaptive
3. Continue existing budgeting models in Adaptive Planning
4. Automate actual data feeds from NetSuite
5. Execute budgeting process in Adaptive Planning \(no change\)

3\.13\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.13\.01

Evaluate NSPB vs\. continuing with Adaptive Planning

Platform decision required; both options supported

ADAPT

REQ\-3\.13\.02

Prior year data import capabilities for budgeting system

Standard import from GL actuals \(either platform\)

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214912000"></a>__3\.14 Accounts Receivable Management__

3\.14\.01 Your Business Requirements

- __REQ\-3\.14\.01__: Integrated AR dashboard with project ID visibility \(ALIGNS\)
- __REQ\-3\.14\.02__: Automated aging reports without manual augmentation \(ALIGNS\)

3\.14\.02 Current State Process

Pivot's current AR management in D365 lacks integrated dashboard visibility with project IDs\. The team runs weekly aging reports that require manual augmentation to include certain fields needed for internal questioning and analysis\.

As documented in discovery: "Use various dashboards but lack integrated view with all needed information\. Need project ID visibility for internal questioning" – highlighting the need for real\-time AR dashboards with embedded project context\.

__Current State Challenges:__

- Dashboards lack integrated view with all needed information
- Need project ID visibility for internal questioning
- Weekly aging reports require manual augmentation
- Time spent manually updating reports with additional fields

__User Story:__

- As an AR Manager, I need integrated AR dashboards with project visibility so that I can quickly answer internal questions without running and augmenting reports\.

3\.14\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive AR dashboard capabilities with built\-in project integration and customizable aging reports that eliminate manual augmentation requirements\.

__Integrated AR Dashboards:__
NetSuite Orion’s standard dashboards \(portlets\) provide real\-time AR visibility including:

- Open AR balance by customer
- Aging summaries by aging bucket
- Collection status and activities
- Customer payment performance
- Project ID visibility on all AR transactions

NetSuite Orion's enhanced dashboards provide furniture dealer\-specific project visibility integrated with AR aging, eliminating the need for manual report augmentation\. Dashboards are configurable to display the specific fields and KPIs Pivot needs for internal questioning, eliminating the need to run separate reports for routine inquiries\. Project IDs are integrated throughout AR records, enabling drill\-down from dashboard to transaction to project with full project context\.

__Automated Aging Reports:__
NetSuite Orion provides standard AR aging reports that include all standard fields without manual augmentation\. Reports can be configured to include:

- Customer information
- Invoice details
- Project IDs
- Payment terms
- Contact information
- Custom fields as needed

Once configured, aging reports run automatically with all required fields, eliminating the manual process of adding fields to reports each week\. Reports can be scheduled to run automatically and distribute to stakeholders\.

3\.14\.04 Future State Process

1. __Daily AR Monitoring__:
	- Access AR dashboard for real\-time visibility
	- View open AR by customer and aging bucket
	- Drill to project details via project ID links
	- Answer internal questions from dashboard
2. __Weekly Aging Report__:
	- System runs aging report automatically
	- All required fields included in standard report
	- No manual augmentation required
	- Distribute report to stakeholders
	- Credit scores can be incorporated via suiteapps\. The recomended app will be easy collect
3. __Collections Activities__:
	- Log collection activities in NetSuite
	- Track communication history
	- Monitor collection effectiveness

3\.14\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.14\.01

Integrated AR dashboard with project ID visibility

Standard NetSuite Orion dashboards with project integration

ALIGNS

REQ\-3\.14\.02

Automated aging reports without manual augmentation

Configurable standard aging reports with all required fields

ALIGNS

__*Client Feedback*__

__*GSI Response*__

## <a id="_Toc214912001"></a>__3\.15 Vendor Management__

3\.15\.01 Your Business Requirements

- __REQ\-3\.15\.01__: Comprehensive vendor return authorization process \(ACCOMMODATE\)
- __REQ\-3\.15\.02__: FedEx integration for vendor returns \(ALIGNS\)

3\.15\.02 Current State Process

Pivot does not currently process vendor return authorizations \(VRAs\) in their system\. This functionality is needed in the new system to properly track vendor returns, manage return authorization workflows, and integrate with FedEx shipping for return shipments\.

__Current State:__

- Vendor returns processed manually outside system
- No VRA tracking or workflow in current system
- Want to implement VRA in new system\. After VRA is marked as approve by vendor, it will generate a credit memo that will math the correspondent AP transaction
- Need FedEx integration for return shipping

__User Story:__

- As a Warehouse Manager, I need a comprehensive VRA process in the system so that we can track vendor returns, manage credits, and integrate shipping\.

3\.15\.03 NetSuite Orion Solution

NetSuite/Orion provides standard Vendor Return Authorization \(VRA\) functionality with integrated shipping capabilities\. The VRA process will require custom configuration and a dedicated discovery session with warehouse personnel to define detailed requirements\.

__Standard VRA Functionality:__

NetSuite Orion includes built\-in VRA capabilities that:

- Create VRA records linked to original purchase orders
- Track return quantities and reasons
- Generate return packing slips
- Link to vendor credits when credits are received
- Provide VRA reporting and tracking

__Approval Workflow:__
The standard VRA process includes an optional approval workflow\. GSI recommends bypassing the approval requirement since the warehouse manager creating the VRA likely has authority to execute returns\. This streamlines the process while maintaining tracking and audit trail\.

__FedEx Integration:__
NetSuite provides standard FedEx integration for shipping, including return shipments\. The integration supports multiple FedEx accounts per warehouse location \(REQ\-3\.03\.04\), enabling proper cost allocation across Pivot's multi\-location operations\. When creating VRAs, users can generate FedEx return labels directly from NetSuite Orion\.

__Warehouse Session Required:__
A dedicated discovery session with Marie Guerrero, Brian Hagerty, Brad, and Sandra Rudloff is needed to define detailed VRA requirements including:

- VRA creation workflow
- Return reason codes
- Disposition tracking
- Credit processing workflow
- Receiving process for returned items
- Integration with inventory management

3\.15\.04 Future State Process

1. __VRA Creation__:
	- Warehouse identifies need for vendor return
	- Create VRA record in NetSuite linked to PO
	- Specify return quantities and reason codes
	- Generate return packing slip
2. __Shipping__:
	- Create FedEx return shipment from VRA
	- Generate and print return label
	- Ship return to vendor
	- Tracking number captured in VRA record
3. __Credit Processing__:
	- Receive vendor credit
	- Link credit to VRA record
	- Update status to complete
	- Close VRA

3\.15\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.15\.01

Comprehensive vendor return authorization process

Standard VRA with custom workflow; warehouse session needed

ACCOMMODATE

REQ\-3\.15\.02

FedEx integration for vendor returns

Standard FedEx shipping integration

ALIGNS

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc214912002"></a>__3\.16 Implementation Strategy__

3\.16\.01 Your Business Requirements

- __REQ\-3\.16\.01__: Prioritized automation roadmap with Phase 1 focus \(ADAPT\)

3\.16\.02 Current State Process

Pivot has identified multiple automation opportunities throughout the discovery process\. With finite implementation resources and timeline constraints, Pivot needs a prioritized automation roadmap that focuses Phase 1 efforts on highest\-value, lowest\-risk automation while deferring other automation to future phases\.

__Prioritization Considerations:__

- Business value and ROI
- Implementation complexity
- Risk profile
- Resource requirements
- Dependencies
- Change management impact

__User Story:__

As a CFO, I need a prioritized automation roadmap so that we focus Phase 1 resources on high\-value automation while managing implementation risk and timeline\.

3\.16\.03 NetSuite Orion Solution

GSI will work with Pivot to develop a prioritized automation roadmap based on the 58 validated requirements identified in this BRD\. The roadmap will classify requirements into implementation phases based on business value, risk, and complexity\.

__Phase 1 Priorities \(MUST\-HAVE\):__
Based on discovery analysis, the following automation priorities are recommended for Phase 1:

- Revenue/cost recognition controls \(REQ\-3\.01\.01 \- REQ\-3\.01\.03\)
- Project accounting dual GP \(REQ\-3\.02\.01 \- REQ\-3\.02\.04\)
- Banking automation \(REQ\-3\.03\.01 \- REQ\-3\.03\.07\)
- Tax management \(REQ\-3\.06\.02 \- REQ\-3\.06\.07\)
- UKG payroll integration \(REQ\-3\.10\.01 \- REQ\-3\.10\.02\)
- Chart of accounts \(REQ\-3\.11\.01 \- REQ\-3\.11\.02\)
- Period close \(REQ\-3\.12\.01 \- REQ\-3\.12\.02\)

__Phase 1 Pending Decisions:__
The following require business decisions to determine Phase 1 inclusion:

- AP automation for expense invoices \(REQ\-3\.05\.01 \- REQ\-3\.05\.04\) \- pending timeline/budget analysis
- Fixed Asset Management \(REQ\-3\.07\.01 \- REQ\-3\.07\.10\) \- pending budget/timeline analysis

__Future Phases:__
Lower priority or higher complexity automations recommended for future phases:

- Easy Collect advanced collections \(REQ\-3\.04\.01\) \- evaluate in Phase 2
- Automated vendor invoice follow\-up \(REQ\-3\.05\.05\) \- Phase 2/3
- Dynamic Terms & Conditions \(REQ\-3\.08\.01 \- REQ\-3\.08\.03\) \- evaluate complexity and priority

__Roadmap Development:__
GSI and Pivot will collaboratively finalize the automation roadmap during project planning, considering:

- Total Phase 1 scope and budget
- Implementation timeline targets
- Resource availability
- Risk tolerance
- Change management capacity

3\.16\.04 Future State Process

__Phase 1 Implementation:__

- Focus on Must\-Have automation requirements
- Finalize decisions on pending requirements \(AP automation, FAM\)
- Implement proven, lower\-risk automation
- Establish foundation for future enhancements

__Future Phase Planning:__

- Monitor Phase 1 adoption and lessons learned
- Reassess priorities based on business value
- Plan Phase 2/3 enhancements
- Implement advanced automation incrementally

3\.16\.05 Decision Matrix

Req \#

Requirement

Info

Implementation Approach

REQ\-3\.16\.01

Prioritized automation roadmap with Phase 1 focus

Phasing strategy based on value, risk, complexity

ADAPT

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc214912003"></a>__4 SuiteApps__

## <a id="_Toc214912004"></a>__4\.01 SuiteApp Summary__

NetSuite SuiteApps are pre\-built applications that extend NetSuite's core functionality\. Pivot's Financial Management implementation will leverage the following SuiteApps included in the NetSuite platform at no additional cost:

__Bank Feeds SuiteApp \(REQ\-3\.03\.01\)__
Provides live bank feed integration with Comerica Bank for automated AR cash application\. The SuiteApp creates a direct connection between Comerica's banking system and NetSuite, automatically importing bank transactions and enabling automated matching to open AR invoices\. This eliminates manual cash application processes and ensures timely recording of customer payments\.

__Electronic Advanced Bill Payment SuiteApp \(REQ\-3\.03\.02\)__
Enables electronic ACH and wire payments directly from NetSuite to Comerica Bank\. Users create bill payments in NetSuite, mark them for electronic transfer, and the system automatically transmits payment instructions to the bank\. This integration eliminates the need for 42 manual journal entries currently required on check run day, significantly streamlining the AP payment process\.

__Expensify Connector \(REQ\-3\.09\.01\)__
Standard integration between NetSuite and Expensify expense management system\. Approved expense reports in Expensify automatically synchronize to NetSuite, creating expense report records with full line\-level detail, PO references, and project allocation\. This integration is maintains Pivot's current Expensify workflow while ensuring seamless integration with NetSuite's financial records\.

This requirement is still under business decision

The pivot team is still deciding between expensify and native Netsuite expense functionality\.

__Fixed Asset Management Module \(REQ\-3\.07\.02\)__ *\(Pending Phase 2 Decision\)*
The NetSuite Fixed Asset Management \(FAM\) module is a licensed module \(not a SuiteApp\) priced at approximately $4,500 annually\. If included in Phase 1, FAM will replace Pivot's third\-party fixed asset service, providing integrated asset tracking, automated depreciation, AP integration for asset creation, and SuiteTax integration for property tax reporting\.

<a id="_heading=h.3ob7dgy"></a>__*Client Feedback*__

<a id="_heading=h.23ghnor"></a>__*GSI Response*__

<Comment>

# <a id="_Toc214912005"></a>__5 Assumptions__

The following is a list of assumptions based on the solutions proposed in this document\.

__Document Section__

__Assumptions__

__Revenue & Cost Recognition__

• NetSuite fulfillment control setting will be enabled globally
• Accrued revenue JE automation will be configured during implementation
• Approval routing for accrued revenue JEs will align with standard GL approval workflows

__Project Accounting & GP Calculation__

• Dual GP calculation customization will be scoped and designed in detailed design phase
• Labor cost posting methodology decision will be made before development begins
• Time tracking system \(Operations scope\) will provide accurate labor cost data
• Commission processing \(CRM scope\) will consume commissionable GP KPIs

__Banking & Electronic Payments__

• Comerica Bank will provide necessary integration credentials and support
• Bank Feeds and Electronic Bill Payment SuiteApps will be activated in Phase 1
• Custom matching rules for bank reconciliation will be configured based on Pivot's requirements
• Multiple FedEx account configuration will be provided during warehouse discovery session

__Accounts Payable Automation__

• AP automation Phase 1 inclusion is pending timeline and budget impact analysis
• If deferred, standard manual vendor bill entry will be used in Phase 1
• Approval workflow will be configured for both manual and automated bill entry
• Vendor invoice follow\-up automation is confirmed as future phase requirement

__Tax Management__

• SuiteTax vs Avalara decision will be made before implementation begins
• Tax filing approach decision \(in\-house, CPA, Avalara\) is separate from tax calculation platform
• Baker Tilly cost analysis will inform filing approach decision
• 37\+ states tax collection is confirmed as accurate count

__Fixed Asset Management__

• FAM Phase 1 inclusion is pending budget and timeline impact analysis
• If deferred, third\-party service will continue through Phase 1
• $2,500 capitalization threshold will be enforced consistently in FAM

• 571L property tax return capability will be confirmed with NetSuite during implementation
• Fixed asset data migration will use third\-party Excel reports as source

__Document Management__

• Terms & Conditions workshop will define detailed requirements for dynamic T&C logic
• Customer\-specific T&C assignments will be maintained by Pivot team
• Custom document numbering for proforma vs\. final invoices is confirmed requirement

__Expense Management__

• Expensify will continue as expense reporting platform
• Expensify integration is standard connector requiring minimal configuration
• Corporate credit card reconciliation automation will use Bank Feeds functionality
• Project coordinators will continue including PO numbers in expense submissions

__Payroll Integration__

• UKG will continue as payroll processing platform
• UKG can export payroll JE data in CSV format
• CSV import map will be configured based on UKG's export format
• Payroll JE imports will occur monthly \(or per pay period if needed\)

__Chart of Accounts__

• Finalized COA from Kevin Baugh \(completed 8/13\) is approved for use
• COA modifications will be documented in configuration workbook
• D365 to NetSuite account mapping will be completed during data migration planning

__Period Close__

• 7\-day close performance target is achievable with NetSuite automation
• Period close checklists will be configured during implementation
• AR/AP locking procedures will be documented in period close process
• Automation improvements should maintain or improve close timeline

__Budgeting & Planning__

• NSPB vs Adaptive Planning decision will be made before implementation
• Prior year data import is required regardless of platform selection
• Integration approach will be defined based on platform selection

__Accounts Receivable Management__

• AR dashboard configuration will include project ID visibility
• Aging reports will be configured with all required fields
• Weekly aging report is sufficient frequency \(not daily\)

__Vendor Management__

• Warehouse discovery session will define detailed VRA requirements
• FedEx integration will support multiple accounts per location
• VRA approval workflow will be bypassed as recommended
• Return reason codes and disposition tracking requirements will be defined in warehouse session

__Implementation Strategy__

• Prioritized roadmap will be finalized during project planning
• Phase 1 decisions \(AP automation, FAM\) will be made before development begins
• Future phase enhancements will be evaluated based on Phase 1 lessons learned

__General Assumptions__

• All discovery session transcripts accurately reflect Pivot's requirements
• Requirements validated with >80% confidence based on transcript evidence
• Pivot stakeholders are available for design workshops and decision points
• Data migration approach will be defined in separate data migration plan
• Integration requirements will be detailed in separate integration specifications
• Testing approach and success criteria will be defined in separate test plan

<a id="_heading=h.spk1rgn9b34d"></a>__*Client Feedback*__

<a id="_heading=h.uwufyw5z0tji"></a>__*GSI Response*__

<Comment>

# <a id="_Toc214912006"></a>__6 Unresolved Requirements__

To be populated pending Business Requirements Document review with the Pivot team\.

__Area__

__Description__

__Impact__

__Proposed Mitigation Strategy__

__AP Automation \- Phase 1 Inclusion__

Decision pending on whether automated expense VB processing will be included in Phase 1 or deferred to Phase 2\. Requires timeline and budget impact analysis\.

If included in Phase 1: Increases scope, cost, and timeline\. If deferred: Manual bill entry continues in Phase 1, automation implemented later\.

GSI to provide detailed effort estimate \(estimated 80\-120 hours custom development \+ 20\-30 hours for PDF parsing integration\) and timeline impact \(\+2\-3 weeks to Phase 1 schedule\)\. Pivot leadership to evaluate ROI: estimated 15\-20 hours/month AP time savings vs\. implementation cost and Phase 1 timeline extension\. Decision gate: 2 weeks before design phase begins to allow proper scoping\.

__Fixed Asset Management \- Phase 1 Inclusion__

Decision pending on whether NetSuite FAM will be implemented in Phase 1 or deferred to future phase\. Requires evaluation of $4,500 annual license cost, implementation effort, and third\-party service elimination timing\.

If included in Phase 1: Additional $4,500 annual cost \+ implementation effort\. If deferred: Third\-party service continues, integration added post\-go\-live\.

GSI to provide implementation effort estimate and timeline impact\. Pivot finance team to complete cost\-benefit analysis comparing third\-party service costs vs\. NetSuite FAM costs plus implementation\. Decision required before design phase begins\.

__Tax Management Platform__

Decision pending on SuiteTax vs Avalara platform selection\. Requires Baker Tilly cost analysis for filing services across 37 states\.

Platform selection affects implementation approach and ongoing costs\. SuiteTax has no incremental license cost but may require more internal effort for filing\. Avalara has subscription cost but provides managed filing service\.

Sandra Rudloff to obtain cost estimates from Baker Tilly \(David Welsh\)\. GSI to provide SuiteTax vs Avalara feature comparison and recommendation\. Decision required before tax configuration begins\.

__Tax Filing Approach__

Decision pending on whether to file tax returns in\-house, continue with CPA support, or use Avalara managed filing\. Separate from platform selection\.

Affects ongoing operational costs, internal resource requirements, and risk profile\.

Pivot finance team to evaluate internal resource capacity for tax filing\. Consider cost analysis from Baker Tilly in decision\. Decision can be made independently of platform selection timing\.

__Budgeting Platform__

Decision pending on NetSuite Planning and Budgeting \(NSPB\) vs continuing with Adaptive Planning\.

NSPB provides deeper NetSuite integration but requires new platform learning\. Adaptive Planning continuation maintains current workflows but requires integration configuration\.

Pivot finance team to review NSPB capabilities and compare to current Adaptive Planning usage\. Consider total cost of ownership, integration benefits, and change management impact\. Decision required before budgeting configuration begins\.

__Labor Cost Posting Methodology__

Evaluation needed on timing of labor cost posting \(immediate vs deferred to asset account\)\. Affects when labor costs impact project GP calculations\.

Timing methodology affects project GP visibility, period close procedures, and financial reporting\.

Marcus Dallacqua to provide proposal evaluating timing options with pros/cons of each approach\. Pivot finance team to review and select preferred methodology\. Decision required before project accounting configuration\.

__Dynamic Terms & Conditions__

Detailed requirements need definition through Terms & Conditions workshop\. Scope and complexity affects whether Phase 1 or future implementation\.

If complex: May warrant future phase deferral\. If straightforward: Can be included in Phase 1 configuration\.

Schedule 30\-minute Terms & Conditions workshop with finance and sales teams\. Define detailed requirements, assess complexity, determine Phase 1 feasibility\.

__571L Property Tax Return__

Confirmation needed on whether NetSuite Fixed Asset Module supports 571L property tax return generation capability\.

If not supported: May require custom reporting or external tool for property tax filing\.

GSI to confirm 571L capability with NetSuite product team\. If not available, evaluate alternative approaches \(custom report, third\-party tool, CPA support\)\. Resolution required if FAM implemented in Phase 1\.

__Multi\-Location FedEx Accounts__

Verification needed that NetSuite supports multiple FedEx accounts per warehouse location as stated\.

If not supported at location level: May need alternate configuration approach\.

Marcus Dallacqua to verify multi\-FedEx account capability and configuration approach\. Confirm during warehouse management discovery session\.

__Direct Deposit for Expense Reimbursement__

Confirmation needed on direct deposit capability for employee expense reimbursement\.

If not supported: May affect employee payment preferences\.

Verify direct deposit capability for expense reimbursement\. Confirm payment method options in NetSuite payables\.

# <a id="_Toc214912007"></a>__7 Signatures__

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

__Financial Management – Appendix__

3\.01\.02 Current State Process Response – Billing before shipping

__Overview__

This native functionality allows invoices to be issued __before goods are shipped or services __delivered\. It supports business scenarios where customers are required to pay in advance as part of agreed payment terms\.

__How the Process Works__

            We will have to enable advance shipping, which works as follows:

Once a sales order is created and approved, an invoice can be generated immediately—__without waiting for fulfillment__\. This enables the business to collect payment upfront\. After payment is received, the order can proceed to fulfillment as usual\.

__Key Benefits__

- Supports __prepaid and advance billing__ scenarios
- Improves __cash flow__ by collecting payment earlier
- Reduces __credit and collection risk__
- Aligns with contractual and customer payment requirements

__What the Client Will See__

- The invoice reflects the __items and quantities ordered__, not yet shipped\.
- Customers can pay the invoice __before delivery__\.
- Fulfillment and shipment occur __after payment__, without impacting the invoice\.

__Important Notes__

- Inventory is updated only when items are fulfilled or shipped\.
- Fulfillment can occur fully or partially after invoicing\.
- Financial posting and revenue handling follow agreed accounting rules\.

__Typical Use Cases__

- Customers with __payment required before delivery__
- Customs or made\-to\-order products
- Subscription or service\-based engagements
- New customers or high\-value orders

![A flowchart of a customer

AI-generated content may be incorrect.](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAdQAAALkCAIAAAA511MLAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAOxAAADsQBlSsOGwAA/7VJREFUeF7svQVgJMeVPj5MYmZc8TKzF7xeM0NiSOzYDjgOXfCSy50v/0t+l7tcLpdLLuAkdhzbMeOa1kteZtayVrtaMdPMaHj+X0H39IxGLK0F1Za1o57qqlevqr/66tWrV2qfz6cSl9DA2GpAPbjs/YNLJlIJDUwGDagF+E6GZpwAdQD+MmyVP0wAoYWIQgNjpwHN2GUtchYaUGhAZrWC3op+ITRANCDAV/SDq6wBMF/2Iy6hgSmtAQG+U7r5ReWFBoQGPi0NCPD9tDQvyhUaEBqY0hoQ4Dulm/+qV55YGySjg9LyIKwQV70pRIGftgYmAPh6vd5R0ZKfXqOSVdhMkLfH43U5XV7vxPPec7lcdnvPaKk6RD/wqHG53B6PR+X3K1CWNQhrkTFsl7FrcZGz0MBINDBSVzO8rk3NrRqNJikxHr9HIkrYZ2tq6usam0uLp0VFRowk847OrvqGpujoqNTkRK1WO9SsnE5HV5fNYDTEREf19Szw5VJVdU1tQ0nxtIy0lKEW8Wml93l9dQ2N5yout7Z3LV04Jz0tSavh+vH7fVabHfhIuKqaklaNxmI2sc9hL3tPT119k8/vz0xLtVhMANXO7u4r1XX1jc0J8XHZmWlOl9to0MfFRgORKy9dQb652Zkmk/FyVU231VZYkGsyGj8tVQy6XDU0g7HEQ2mBWqXWajU6na4ftQw65zFJiBZ0uz1oFIhKBzoMdX6DXu9xeyouVVnM5syMVMg/FmWjTWvrG80mY2pKktFgGI0iJo+rovapp54aiUY6u7r++Mzfz5yvnDOjFM05uEXsISx2//lvr/3qDy/On1WSnpYyks695+CR//3j39AVSoumDfX1Rt/df/DoW+99jGFgRmmxRhMeerq6u99+7+NnXnijIC+7IC9ncKoYie5H4VlUrba24XfPvLLh4+0nT18oKylKT8XgxAdRIOnb7285dfbCmXMVZy9UnquovHylLis91Wjs8y1Cil//8a879x6eXlKQmBBns9s/3rbn6eff2L77IGC3x+F6670tdQ1NudnpNpvtp//1+0NHTs6bXYZB8T9/9cenn3tl7TVLY6OjR9LQg1SK2+32+fxoymGVpXa6nGfPVRw6erKi4hKGkOq6hq5uK/DLbOpvZBqkbKOeDO149MSZE6fOgRxcqroCga/U1qN12js7v/fP/3H5Ss3CebMg+aiXiwzLT5/7+a//dKW6tqRoWnRU5EiKQF/FnBLjvlo9+iRvJIIN+9mRVsPe4/xkz4Htew/2OBx0RB3wGoJ1D9kVTsudN7sUg/OA+fafAIx1Wl5OYnzCUFsOTe50uv7011deeuP93//l702tbf3ZLjRqrU7D6cUIJQ56fAhKG1KxyHfLjn0HjpxctWzBv/7gyVnTC/QSA0I1ASi//N2z//fnF9/+YPPr73782tsb33pvU3untR8NENuL10ugjbLCS1U1H3+yFzcfffCue++4wWg2OlwudBUQMfIu+bwerxuMDCltdlt7ewfI5OB6Eatl2FF84KG9pbVt94GjFy9XwxYyJHVJif3d3da3Nmx86v/9z/89/bf/+9PzP/3P3/74//vla2+939jcMqwMx/Ah6LmtvfPZF1//55/99y9/8+ff/un5p5976eU33m9u7XC5PDaHw97j6KNBB+MUOFDPVKthhPOAdqOZQ41+Az2r0AqMVhgzDhw50dVtmzRGqpGCL/QDnfroO4Orp8fR3tHZ43CCY5KpZkuby+1GGkzJOzu78S2bw+IhvJ/owU6XC8/hb/zZ1t4BywB9A/krgZTXrl724+9+uaQ4X2YoyKqxufXyldqWljY5JT6QxxubgRdhe9KMksKvPvbAjetWREaY8cbbYeAEDXO5IG1DU4vVZutnp9+Fi5f2Hz8FdtDa3v7Jrv0hLwoMLx2d3e3tnWB2yAS9DOOz2+t1OJySeKTGgCSH08UmqpDQ4XR2gipbrYAbliG56XC6XS6oE8LhhXE6nSFlAbNQFvqfPOFFAggA4wB++t+syAyvULicDCUin8orNU5nz5yZxQXTsqMiLSFMECQ4JzPtx9978kffeeKH3/7yPzzxcHJiHOUgXmVxpN7s1aLzWqIC8suLuUJzS0tBXuai+TML8rLWXbP4B9/4wqMP3pmemkRS+/Gcl3QAtQo47PEQBfIehQzoRdXIZvdERWgyKEFCXj67QDboP0zbvV9oiEEm3TRn9u2hY+X/9dtndu0/isyHB3sQGTVOTIx/4LN3fuebX7rv7lv0Rv0bGzbu2HWAqYJpA0XjkjskNIKZfq9moiojVXOjbsrei8+oF7priJDIgdxXBAYgTenx4HEU3rtGNE8/DG733HHjk1/8/Ne//IUnHnswLTWRNgERUsmamDKpkNTcFFApJZ1BCuYWAKm6TLu04T1kcGX1IjfwHzHUeFFHqfqBhiLpvTx9b+FZeuDJq29/+N+/f66+qWUsF26G1x2G+dRIzQ6Ajzc3fKTV6e68+Tq9Vn/qXMXH23Z3dXUfOnZy8/Y9p86cx2sYHxfb0tq+bdfB1vaO5MR4g0EPYcvPXPhk9wGLyZQQH9vY1IJ5/dad+/YdPHbuQiUej4mOhp0IQHDg8DHkk5WeFh1N5izVNfU79x76aMuO7bv2VV66HBsTC1sz7Lm79h3+ZOf+/YePV16uhukZ5sUQw25VTd3OfYcAf8mJCW0dnTv3HKqurb9SU7973+G9B4/V1DWAGkdFRYYxW/tVf3vl7ZOnz//bP/3Dlh17gJg3XrdapyNWUXQs/Ln/8IltO/cdPXkagwHLcxEmcWYjcgbFS05MxNwWwz6m7YePlWPCbjDoTp2tQE0PHj1x+txF5BAbEw2jJ4Bg8/a9mJKjOnsOHNt76Hh9YxP0wAARZV26XL330LFd+46cOXexo7MzPTUFObe2dew/dHzfweOnz1faenoiIiywyfZ+V5HtyVPnjpWfOXu+EkMilINkNrsDz6LQ5pZ2QGp7V3dGaorSpICR7KU3N6SnJD/5+ENZGamwDML4A6NEc0vr/kPH8EZBzygLpqfDR0+CTiYlJHR0dO49eBRv79IFc9s7u7fu2IsSDXqdXq9HLfDuYYoOAEWtYJFAy+JtXrViSWxs9Acfbbl0pebeu27BdBi2iwNHjkOSU2fPHTpyAipFn9FptUeOnzp87DSaEqbn+Nho2AwgA7rWsfKzx8rPVV6uAQBHRkYgaWeX9VzFJfQ3tPXx8nOnz19sa2+PQJ1NpqrqWsAumiA2OgotAw3j5lCNDxjq9h08AuUDzq5Ztqi0uADwsXv/kdSU5LmzyiAhZIb20MAY3eNiojEwV1y+gj9Pn6uAjcLR44iMsEAnQDaMtbV1DehgR06cPl9xGd0gJTkR8oBhoF7HT569VF2Lx+NjY6B5wCt6+LGTZ8pPX6hraEZ3ReexWm2wCx0+fgrdCWM2KhkRETRTRB/bvvsAutCD9912zbKF+blZmempMBK2d3S99/E26GHtqmXQDeC7orLq5KnzJ8+ch5a6rXa8Eejqnd3Ww8dPo6HxjmCwBKNCAqB8THQkkBFdC+VCNtQIb+75ikv4FhYqdCqz2YTq79l/GL0yMT6m4tKVMxcuoUWiIyONJgPQFwo8c/4i7F1oLGSLdR1m/UCex0+e0+u1QAlMUFD3fYeO7Tt8HB0vJSURjCEhLlY2jg0T+cbBY6MAvm9v+EinB/her9aoP9m9/7dPv1Df2Nja2mHtth48evLEqfOZGWnQ6WvvfoyXp2haDkzvYHbPvfQW7Ikzy4oT42Nfees9ABzIo0arrayq3rh5J9q4GMZZg+FvL7/xu7+8eO2qZVkZaehDv/njc8+98g7ooU6jxtseGxuTk5X+wabtv/vLS+CJYE8Hj5w8Xn4WVleUolTvwSPH//S3V9FXZs8oAdT+8ZmX9x88Vt/U3NXZBYPUxi070d1hDu5l3/B3dnb9x/8+nZeT88Sj9588fe7oyTOrVy5NSgDoqEGf39u47ffPvHS5qhoj88XKK5VVNejBi+bPwpDzh2dewBs4b/b0yIgIfPvia++8//H24oI8vV731vubjxw7BaoOQARwpyQnZWem4xX653//DabDmDFU1zSgE7/z4RawG+SGfoZVi1//8W8bNm4DZW9oasZ0HveBca+/u/GF1zYAgHBn/+GTGBDyc7LY8MYugtpV1S+9vgE2ayDO2fMXd+8/DLKP1w+cCsaE8tPnnQ6nrcfR2NS2ZMFs5cImFP7yW+9Hx0SvX7MCrJ0SKx9Y0pFjJ5/66S8Neu2ShfPBhCouXv7Zf/8W2Ldq+WIgzr5DAF/P4nmz8EZ98PGOtrZ2TDJq6ptgasfb/swLrzW1tELVoEKbP9kN891qgG9MzIcfb0PTf+auWxIS4t9898N//6/f2Xvsx06cwYABRtmMSXJ390dbd8N2+fG2XZB/zvQSLOhhsff1DZte37AZqAGbJsZ+IAJWOy9UVv3lxbf2HTwK4+ahY6d27Dmwe9/BqIgI6HnXvkO79h7CeI85xJXq6sKCPIzHQ12DhcF67wGixmuWLYYmwdxQIgbX0pKC4sK819/Z+Pb7EOnytp37obSszDSA13OvboA80Al+Hz952mIyYvhES2Fe9bdX30GXQO8qP322rq5x1YrFQLGnX3j9rQ+3YMH5WPlp4E5WWgq69KXLV377pxcwXqIPI3902qKC3AOHjsOYAA6B6WBtfXNyUjwWNpWdHz1tx+4DNpt94dxZcbGx6KIg51qNpr2r6/2PtgJ8161ehjcUk/o/P//qJzsPQMgDh4/v3HNAq1bDWAcS8E//73/Qpkvmz4KNYsv2Pf/zx7+BYS+YMwO98cMtO1955+PcrIxIi3Hjll0vvf4eKMK58xfPV1SmJidhcN2z7zCGZywtgGxs3bkXYzPGbLzOQP+Pt+5+d+N2NBBeq03b9qC3zigtQlts+mT3z3/1Z4ez5/1NO85XVM2eWfzsC69frKxCFVraOqCcOTPLTH0vPIwDXB2UCKNgdiCsQV63ILMUf1pK0g+++aWf/Ohbd96yHgN4+dmK9LTkWdMLa+vr8YaA+OBVOXO+oqw4Pz83E03yweZdhXk5P/zWl//fj7/91Pe/lpuT8fLr7wHLqH1dA1oNjgMUAbd9fcPGxfNngoT+57/96Kf/8j2szgOVXn7rg+TkxO9980s/+NaXH7j3NrxXW7bvDZncoathDKf5qMCMTGYDqMpN113zzz/4Op7Ky07ft/8QWEOozvwq9CRQlZvXr0YOt914LfBu2459xNLi8+LFfv7Vd8EyvvO1R3/2428/9JnbUYJGrdFp9dPysufPmXmlpg79GHliTaPick1ZcUHRtFywgOvXrsQs/mf//J0nv/gQVmlA2AHxyBMg29rWPqOs+Iff/sqPvv1lMCC8wzDXoLBX3/pw6679d9983U9/9M1/+9E3v/j5e+EzUH7mPCAViv3xd7/yva8/mpOZsuGjraASilr4YVHBKwGFlJUUfuuJR773jS+uWLIA+Lt15370/s9/9vZ5c8pAru+/68ZvPP5AQnyMUgN0fVwDZAc6vPDau39/4z2QOzKv9PttPRh67Mw+C/pJrRl+jL7E+kRtcuC6SxfOvf3GNSnJCTPLih574K61KxdFR0cgpcPhoHNzNifl81qMu6TrSMXD/oKu8tm7b0VHAj5u2PgJ4OmuW9d/98kvzJ5RDB506Pgp5AOgf+eDLbPKiv7xm49/6eF7MSq/9f6mhsYWUGBgN1AjNTHuS5+/58G7b4IOgSYwTIGZzp87I8JiKi7Mvee2G3Iy0ymH4iWjc2KoAKbY7D1Wu93KfoOl23t6z3ZB5DGoXLhUvffg8f1HTiYlJpQWTsPLgNQg7xhxb75+9dprltTWN7389keAjPtuv+F7X3/sgbtvqatv+NNzL5E03d1/e+WdLTv3LVs45x++8vB3nnwMA5hGq3nv460vvLHh2pVLf/ydr3z10fsxWfnr39/s6rISTNx3eNnieT/+3hNf/sJnS4vykS2UgA526/Wr/+m7T3z+M7fmZqX3mvoQTaN7Y8r4/Ctvv/DK27v2HgSQkdeBWnPwg3Hx98/8/Xxl1d23Xf/9b3zxSw9/Bnd/+Zs/HTt5Ni4mBq2JXkrNiVYMhzAQnT53AWYz0Fj4S8B3BXCPKSB6CPT4wN23fvMrX7jz5vUwdBDrlN+PoSItNfnh+++8+5broF50SDAtyIS3+9qVS7755Qe//cTDGKKeffFNDMy4jykjFgMxd7xhzfJH7r8d0+W7br2uuCAn0mJeu3zRTdeuNJtGxXFiUBA5dolGCr4Mdyn+UqMvJiMxUXNmlUGVMAgU5OfqDXo0s0GnKynMxaQCE0m8EhjoCHmZWYrmOXbqHAYzLHMXTMs1mY15OVlLF86DORbzDbxC1MWJ5I9G/XDrDpTy0L23AtowQUH+MLrV1Decu3jZ5XJ+uPmT5195F8zI4XJX1zcyW7N8IQfS1ejFXnc4hJUUFcRERUJIzJdhSAWwhigaPWfDR9uMekNaahJKAUGLiIgAjQIlRGKQ05b2rmUL561cuhBACYhZPH8WkRWT4rjYkqJCvLowEQBuzl68DPZRVjwtKSk+Pi4mJTm+tq4eU/Jz5yvJxLmtHWt6xGVJrQJtuX7N8pSk+OnQV25mt80OCwMmCu9v2g5dPXTfbaA/6IsgCBAVq+2QBPTkwOGjBw8f64GbV1PTmQuVylrgzQcfTEiIu3HdNUsWzgH0YETMzMw4Wn6OuHbl58DggPldXm5WQUEubCLKZxnc2DHFPnB01/5Du/cdOneBIzu+YQtllF3DYktMhLJ2oQOtTosZT3FRfmSkBQLPnlmSk51B3xnJQsgekEx/yok/NOHze2+9YR3s7HDAADVG7pgkrV6+EE6Ha1cucbrdNbX1xD6z/wi8AGOiLFdq62CRN1uMVdV1mOBDNuB70bS8a69ZNnt68YqlC+DQBh4A7EAHK8zPNhr1MKQsmD8bVg6l+wrsVy+/+f4Lr77z/MsAqXeAU+T3q++AfZPeGNSjNB1dtvc+/uSPf33lhdfe6+y03nHTOrABOjj5QGlXLJ7/mTtumj295OyFS7AVXHfN0uvXrJhZWnTbjesWzp9dUXkFrX/q3IXDx09iooaWhZBLF829cf0qiP76exsj8S5kpgDaYL0BXT11vrK5rQ31wgDv6LHDxkUIzYwS6A3ICPsD6Sd2OzUNJYfiBVU51AXj3kebP/lg09ajJ8rtDgd7uVhimDgwMVq9fPHdt9+A2eH6tSsfeeAedL+PNm+HTQw6xIt2uaYW5OByde2yRfPaOjowUwEPralvzMtKMxp0YO7I84Z1K2+5Ye28OdOvXbMcbzRpCMzGcnNuvmEtGP0dt1yfkZFe19gIeEXBa69ZWDQtC/wAbQebRnuXrb6hGQokZmi1f9H8OffffTPeKbykMOXl5WTCEjW9tGjmjBLl3G7swHGscx4p+EI+4q5D30Bc6PGYVsPyyBBZoyUukGxshfdVUUEOIPXo8VNnzl3AZAcvEiyUDgeWmFQms4m6lxIEiomJBn5hPQxPESopgSbmG+hkAFyWjIzZPh9a0eP1wHh07MRpcCVYi+AggVktQbKgVwVZslt03VXlxzwLorKxg9hw6c0QdYO6HjlRjqdee/uD3/7pb3/7+5voF3DlBerB8ATQxKCCvs4qi9yiIiMpyCNDHfoKDL7nLl4C+YUtD6ZtSAXDJawiYDGvv/MREA0zR9j4yOIVLRpPwhiKfFiGsHpjsQbLFLC+gZhgsiYrFomBBRjAQL7Kz1VghNi0bTfApbSogNgNAvVQY1Gvq6srLiYKObM3LTE+Dgb0LqsViM9WsUjjKYFQ0gJr15SkxO8++ej3nnzsO0984abrVpNbfNWUaxj6hDZILmzVldQELh/kWz4u8+YiTkLMuYt8ScvmHxiE0+dp4WhYFXCE6QHCQ6lp1HUaH/AGIh8UCgs+DEc9jp79R46/+d7GDzfvAEnHUh7Hdz+xUeIHOeARkAA3pMRcitXO78MESB6P+T2/H3OyA4eO7T1wBFaFvfvx+wjwfc+BI7CYBe1AYZKpVWajITYqYuHssscfuufeO29C56R68MMwlZmRgqbEHB/WTFDyxIRY2EBRdXQ2mM7RQ+qbWy5eugL+Pi03k/iocR6jwmJsU1Mrxp93P9yCfgJqj5U42KZQe0wmgNGHjp763Z9fxJBw/NQ5LFXA6IzZ0uYd+379h+fe2PAxwFG5akeqRuZ7KhDz++66+R+++ui3v/r4LevXAtFwG1Wg/FddeanK7XZhGGA6Qd1KiwsxHcEgB3v7wtnTUYWjx0/DuoX3Z+XS+ZAfpcMChg5cUpCH33gHE+Ji0lJRNfABqh1aNK7U1CQsXuAObAVoC7Ici8kTTBabd/7xuVdffvODDz7eDuMYZpMgEEgP5oTnMAYE8qFapcuzmA0Hvdoh7+wE+nOk4Cu/PHSJlyxrspeLqUB66cjfSQnxmHdjlgSDDkBn1vRiwBPSJiXGmQx6WAy7bXAiUWFtFw0MypmSkgDkBXYDwRk25GSkIT2MGKxN6WuqBpvGZGTWjOJ/+u5Xf/LDbzz1g6/96B++fMdN1xrJakbgYq3IZrpkKkSwQrroO0+xPLThME2zWq2whMZFR+EH5uk1KxbjJdy4dRd+413CLBVWDmbisNsd9Y0tMpuAVWt6aSHMcB9s2olFg+JpuXk5GcRGtmn7tl37Z5QVPfHYAw/dd3tKYgIFHVZ6kATcK06tQn816nXgziAvMkxAXiCc2WhctWzh1770uW8+8QVMWp989AEwBeWKNGgLXmygEh5nasQaCGg+3hC2ZEGpCWisTF2DlIbRDkYJzFHwM3tmKfgjfTMJjDI/LeZEAVMgWx+nkx8oM9AHmGOABAfEsQHTavZqkpdfbgSyTk93BtJGwtfARvZlkP8/ERX+uRqs4UH+CLM5Nipq9bKF995642fvvPkLD9z14D23FU/Lo28qEYOsdtJ+iHwwjCmNUWxUV+IUbtx6w9pvPfGF7379i9/7xpe++43Hv/v1x7/3jce/9/UvfuWR+wHgsmqY2Fjsuu/2G7/79ce+/OhnVy5bgGGP9DEqPwCLuL1TFNNpND6PD5t0MNqxJrDaejCsYnCFHRzfAp0VPnZEatyEN/n61Stuv+G6229c98hn73zswbthm87LyQZ6PvLgPekZae98sPWVN9/HKiua5ltf/cL9d99qNJne3LAJhmbiRBTU+WEM08B2D1PYmpVLwEBLigvYyip5v+jeKLK+rVJjuw2TELVAb4O+MBmF9yHMZQDrQ0fLsQKWlpKYm52RlBCLVROs6MB4XVyQC+aEFgGRgoVGqVKG7BISI1+O7GgQMOWn//YayMHq5Yseuu9WWJDRH5gri9NBnKCwah1UC9KCnpCqhb6xE+rvkYIv7V20q1PuwzxdlBBCEYT0SHRHmB0x74bBDhPe2TNKE+PBYVXzZ0/PykzdumMfOtOOvYff3bht14FjBXm5QCu8dUAItCvjQzdcew2o5Stvf/zeJngrnNi660D5+YsZ6WkYrisuVsE41dzaDviD3aqtsytkeOTgS+ktNUMFLHh8tkzlVLYdusWmT/ZgleYbX/nC97/55X/8hye+/w9f+fpXHgbVxXIz1pqn5ZLZK2gRFs3gTA7pDx4tJ9qgCsAKPurr8vg+3r4XxjJMl0BS0HU6urpRvtliwWwLiz8NzS1UAIJK+F9Jv8kbg5FHpcZbjeW1hsYmrK1h4f5C5WXoEABaVJhHttVdxiqfHwvTGFRgnYSKlLWAmQLz/dr6BryTWFLHutBH23ZjSCjIzcIqPFKixSinCGVL5M3E1IW8m3wMZTrE31hC1Gp11XVN5y9eRoa7DxzGOhud6bOq+PHKsbk8ne8SOGY2CpYDnmXzA4Z+TF8BIwb9TBPwzgkhWFasXviXwJNOB+s5bKzwcnS5vdPyc8H+4GwAXcXFxkgakIg0YbpsDKD2aC1WiPUtrR1NLe1oGmXNYZqEqQSjJkZHGDqknyLcDPWEoZ0F1hWwOXRTZX8jWiIDDFEc5ASxjY2OgJ0dXbSppQ2/8RMfF1dUkFdSmB8Lk8LZij0Hj2Liglk8rEZAbayFEMdEn3fB/JlLF89F6bBHYXUBCcCm165acuN1q+CkAVMv1jywJoEh9qb1q9etWQ5mCJebEBc6Qm/Rk0BIeVtKYx+ZSMA1nagXc3nMjbbv3I+l4ObWNpg7Xnv3I7QY5v5s/2pZcSHkhEcGZlewv+VmZx0/dR5rZWkpyehjGIew9I0p2v5DmH9exGCP1WZM19DWeJwrnqmfjp3QDPx/8IrBvHbN0gUYV+Drgg5Mp1DEwQ5pGXCzpqSa1EAnWNOG8Xq4DtrjC5tHuqcQ0JiYEA/NsAklOgQgRuYIGNgx/wJ1ghLR6bEQDwzCHLykcBp+yKxfpcJkHAsp73647Z0Pt8IKAS6ZAvv6zeswNSPveWRkXFysXk8cU5YsmAtfmS07Dz79/Kux0ZEYkLFydcu6lQ/de/ub72168fX34JLCOsqtN6wJUTPceiItFjBI8vJrNABNk5FYyigiqGBBjomKYA5k8lV+9gL6EBb08SbgfWBrE5irrly2EOtg8O667aY1t92wFkYx7J0DHUDXwVI71hMYZcMLCYvqtLysT3YfWjhnxvTiAhQN2JpRWgiXozff/QjrvoT5GAxgrwTSwOYklywKxiAjBghJhh+t5uEH7rLabW+8+9Gps+dRcUwxvvrYg8uXzMd0GF5Z6OgwJYM15OflwKEC1ZGxADpZvWIxvHzgiHKxqgYE53JNfWZaMiynxFGMzgYISvTi/RRByDcojrBU6TXAZCQ9PXXe3JkwZf7m6ecBdi2trQaDUbIYEP3hKQ5VHFo5bpK3DvYZvEbELoE02N3OhxvuHkvHLWqGoe8ee/HUGsKFuZDkA/6DUgAW1yxfdLri0oaN289cuBwZYcLiJHSOOQd9jA9qpGowIUNltDBkiqkxZvFHT5zr6rbfeet1sIMrls7DTml7zYkCs2BKrBUXG1RQOOP2EHXxgtkYL+Gi8PtnXgS4Y9GvqbntrluuB5zBIA5LDmDu2b+/AfxFn8FY8tT3n/zsXbc2Nj/3h2deBExDWxhoczIzUbVd+w9jVSMqwtLY0grrxNyZJSCD7320tbq2ET52dY1NmArAPwFYHCISHxFDbHF03sMGOXSbO26+7o0NH/36D3+FJ1pHR8fhE6fXr1kJ4y9qAi+gRQvmYMaGRpg7G8uV5vycTKvNCq98zDPQi9GNlyycC7dCrMuRdc5keFhqrl+7Ar+hCdn5mOqE/I9+gYVBGJQ+2bUP1mr428Dbx+2B8zJxOqaNFfCPhnh4fzMz0mF+2fDhVswh7rrtemLuG19YOmRpRupqhvcA+0FnTcfaVT4QCjhCptslBYx9AM7g+YANDqkpiQTyDEa60ywbS7qYyFA/RzKphJ9KdlY6ogpkpqfMmVly47XXLJg3k3UghFPIy86EZwkABWa7sqKC9JQkLH/BRXxGScGCWdNTkxOwuJedgRcqEQs703KzFs0FByoAyiiVgXcVSysA+sx0LA4YYmIi8TknMwNLTHhTcAeLA/DWhCVBfgpBCdCH1q1eDtclBhaMuWGwAb7nZGQUF+ajOGQLgINhdPHCOSuWzM/NyZw5vZhVH/MmLATnZWdgYoX60ggAWizuQVQ4RcJ/FlQF3KestBDvFQQGKkFyLGFjPYFYFTQadFBMx2A3ALnIzUzHvAFp4CYJBMeaBmzK0/JzIABAHyMcYGfJ/Nnw4lTO05EJaAUaBdQYTYC3aO6MkttvuHbOjBJWWbCJjNTkebOmM6ucUmmEkHq9c2aUYciU75Mh1miEGkGxUR0oZ/ni+WA9M0uLwWKYQSEvOwtLgnhFybzVYCCdIycblQL6wc0Z1Al6g84BqdPycpESUmHQQg9YvmRhVFQEghPFREUtX7IAwwOywyuJgrCwCacuhqTQFTYlo7dAz3BXwJ/YrIVvUBEgKXCBCmmAzmEnQbcE6MKchQXAObNK8QiUD+s5icagUmH2gOYA6g3p1YGVBiwhIS5u4bzZsOaHPIt6oedAG5j94CtoHkwCa7AgdLDwpiQlXLd6GTAXvQjDLTo/poCQBEsa0HZhfu68WcS8A9YCtcBChNkSbFNgHjAiwz0OK6i4idphcQ/kAzqBqwxYAqyliXGxa1cuvmbJAozEyvaCPDBr4D2aVVbM/OXpkEbiugDO4B6HYQB9DKgN72myxtBtRdvBQPHZO2+BbRCJ0XMwzwDyojfCzAWOhZcXSoPnCSzO0AByQy+EMPAXhkUOEzIsLRMNxEQB4EsKCcdHdTD4wSUUTYZoBEiMtkaHgRczmhIOyCh9+aL5sE2jysDlJQvmMEdyXBhs0SXQecBP0HZ4wwmlm+DXSAPr9O52vGHpP73NqMS2qQjU0vvxkPefvGzB1IJNY3Ep1+JIMnox2hG2Ubh5IVxKNvEMhR46j+69/Z8JwMART1GjpwfPomdQEUg+8gI62fPm8xHTtUIqMDssKQBQ0H3JVJ1yQDBrsumWkGseooU+SvzPmGDIGlgGkKKwbmJ4QW56fQ4nTK5+YhruI3YJkmEqiiUOlEVmAGTNimuJrfhhqOvt64qnYKSGAHjZQlSK4sC8cLF1S0jFkkFiso9RpcKbhjuYRcLQiQ8QDCWiIPyJKTkZ84D72JKOtVaTEZpEQdAJeDTEQM7YhoB3jA3PeJPh7wVOx8yU4HqQmVSVfgtJgIOwt+Az2UVhNpHNF3j/3R5olUxZ6BYVslMOZnqTkY1MdBnTCmkxhGBQHyqHwoMwbqIumOeFrLwTzbCyqLVU1hvZ5NnVjaphegf7qXKABM9r7eiALQ7pAegkIBFtWboH0gb5wfHJOiqFS7BgGKzIGAz4MZugauTMNotiUIyOimBKU17oNtRVzo/0ynLJ3kirHb0QIrH+CbVgbQB2ZGSFMV3p/YLEsCqg02LoYq2AP+msMTBlJB2mx0FsUF4fkuEH/RlNQzf1oD/Afkj0BhUB3PEnKa6jAznHx8biWXwFKx9aFqvo0CFyZpNjdvHMu7qhcNg9JsEmi1EG37CoJ24KDQgNTHkNyANcGBvO1FTOyBfcpqbeRK2FBoQGhqQBMuntPRUeUhaTLLEA30nWoKI6QgNCAxNDAwJ8J0Y7CSmFBoQGJpkGBPhOsgYV1REaEBqYGBoQ4Dsx2klIKTQgNDDJNCDAd5I1qKiO0IDQwMTQgADfidFOQkqhAaGBSaYB4o4+yaokqiM0IDQgNDAONRCyjUv9l2efV4Z2InEv6J4rtgebb1KjUa9I4Csp6iLZ34VtXCRSBwkfTjKVgqTgIXkTGg0nxTadyTEyeBYsxkYgBg8NnSCl5GGoWD7cN1DeoCZtUWPhr1hMAFnRvDCyyYwH1qKp6OY3kogKRD/wKrIb0m1WfR7om0dIpFvWaIb8eS44KVRKQj+zv6X6shAEPIAM0ySJncNTsspKYpMwBCiY/MnrTD+zhqFKYpviabQAoklpSx6tCKsJ3U7IWohXmJUlZ0GjDZBq8Jg2tHS6fZBqiuyfZkqje6kl6ZhGWHAcEh2Ba5uJxRMpNMu0S+7TcmnrsX1/fA8haxkST4ApQ1IISyv1OFIZvk1Q0hv5lnRBxIQMNDLvMJIeWW+gHTXQKeS+LKuUhLOgdSVx+mmQF1pL8jBCCuAfL/2XKov0cxaNlNWBtZksgaxqqUUCEtHOKXVhaWOnsrkCOzfldpXelMCGBKmAwE5P3ldZkkDP5++TlJ43A88w6B1iOpf7hvxqyO+p/EawHip3VNagUncgCqN9gKaQwpfxLstFk9qUvv+sU1Ft855H+yw90F6qjXI7q0LfElJI1ZX1z14Iucfjk3SEHtnsSoWnzah42XhnkUokfYVtmaUNpgzwREVmm0/5/8HV4v2BFcN7OK+JhJ60W+BhZIJthKtWrUxJJhFomQzqqivVUtdV4EfgFpeRvUSB27Q8FpYmpHPLICQnDiRgXZhfvfJjqpJ/s2QkJocEbVJvVfS4EJkUig1AW5BEUr3l7s3LlPOW0D5QKJGIiiX/CnRfpUYCuMq7BG8BBcgGXgKGKQEpZBiSeqb0gihKUAgQ1BKBbJSa4R2FpmRq4toN0TAfFwLvWW+0olnRYI480+CeoNQMLS4IGOSHFAUFwCW4Ir3/kuosAwYvINCOTIvyOM4AX66zsnYsd7nLBHCSZMHAnY1dAZYhd/DgOsmdRsoyoJDAay4LEcQyeLsrWz7Qt6S7vZE1AL6yfkOUpaxzmE4T1GSBlzC4cxAgZQ0YIh+9L3fJAIFiBclooig3XBcJSjxQy4fNK4C+XExyg6IvbwllA/McQgGql96kviNxhGDt9f+4PFowAXo3K79PgvlpEaoCMYjk7MX24iH0AZFUaEBoQGhgtDQgFtxGS5MiH6EBoQGhgSFoQIDvEJQlkgoNCA0IDYyWBgT4jpYmRT5CA0IDQgND0IAA3yEoSyQVGhAaEBoYLQ0I8B0tTYp8hAaEBoQGhqABAb5DUJZIKjQgNCA0MFoaEOA7WpoU+QgNCA0IDQxBAwJ8h6AskVRoQGhAaGC0NCDAd7Q0KfIRGhAaEBoYggYE+A5BWSKp0IDQgNDAaGlAgO9oaVLkIzQgNCA0MAQNCPAdgrJEUqEBoQGhgdHSgADf0dKkyEdoQGhAaGAIGhDgOwRliaRCA0IDQgOjpQERUnK0NDnV8wkKTaxQRiAObL8a6hU/dmj6lKPHDj5S8NAKEKmFBkZbAwJ8R1ujkz0/ctyD1+fxunEAFT4rqxsSPzvoqJJgdAwN1j0Y6FUECw8T65vJES4f3EMcax25cPIKP99ksreSqN8E0IAA3wnQSJ+6iDhepcfpslrt1h6rrcdmtVlb29s6u7ucTqfPz84A5LDHj62gp17wU1nIsUzsnBZ63AzgjxzdEzg7hjysPI9IOjCBHd1CMyfP0kN++Okn/FQX9iWl1oHjBqQnaLYkZ51WFxUZlRifEB8da8FZLkZLVGRkhMUMRP7UFSsEmMoaEOA7lVt/4Lp7PJ6W9o62ztbzVy4eP1t+9vKZzp56j9quN/sNFq3egKPQGPAS/FPgHoNLdkobP4FKOsaNHYjFkJGd/sWxm6Az+UiP9ZJgld5jpJdmIB3FR26TjNj3TAJ2BhCDa/6bPORVexwql02l9hgijHHZyflzSmZPLyhNS05LiIvT6/WDod0Da0qkEBoYogYE+A5RYVMmOYhmc3PLpbrL2w7tPHpxj9vUkpyhs8QadCZ+aJaMmUwlDAdDTp6TjA2K8/rYmX8BNSrO2pNhU3HMmpS54hmaaR+nySm/ksugYhGw9oOmu6zq1hqvtytudu6iFXOW52flpSQm6nW6sCaLKdPaoqKfggYE+H4KSh/PRTKeabP1nL9YsWXf5n0XNsfluRLSTOCnxJbAZ/hSDXqfF8i+kUFXRuOAzZc/E5ZvStgtHYuoPHS214peHydGKrSrMELz04X5+ZCAYXV3s7/rirk0Y/GaBatnFZdFRUX0PuJ2PLeUkG2ia0CA70RvwdGUnyFvU1PLroN7X//kFX1qfUoubKMMTYFXwWfH9oHACuwNx1BDma+Ui+KQYyUt7ssmMDDyhg4DTBiaH8N2tdrr97ZecbkbU25afNeqRSvTkpO1WuF8OZo9SuTVjwYE+IruoaSK/qorNe9u2bDt7Ds5s9XGSMzUAb0B2OV23WDyKuOZnFGI24OSz7I1tPCQKh//LmcU5NYgP6SwbQRKCnW14HkEOHhQQ3NbNIYTtd9p9dScUC+ddtud627Lz86SFuK4rVn0D6GBMdKAAN8xUuwEzNavqqi8/NKGF89Zt2eU6rV6smam8gczwSDUpH/0cvsKglqZ1wbroz+bQy/NUbQOfkJhQw5NLtuLQ77ohex09c7HRgKP31913Dszfu2DNz84LTcb7hgTsP2EyBNMAwJ8J1iDjZW4fv+VmvpnXv5LtW9fcpFWoyV+AwR8g9bGBoGgyiT9QKQE25IrA3tMWkWTMlGieyjvJclDlvd66SY8G1aODiQL5rjmV3lrTzrLYm585K5H0tOShf13rHqayFfSgBjhRV8gGujstr7+/rvVrkNJ0zQEeZmpQeabxFWAKUr6RL4K+6PQJ/MpC8NkuQcv+y6QN/M0C/zQjzQL/ov5lwUGBJ6W+QOH+ZEd2nqVQgqijm60ipQEq9WZs41nOza/9eF73Vb7AAOH6DVCAyPWgADfEatw4meAHWvbdu8pb9wZP82rMRCXBiCvDGzByMZgLCykcpSUgJLrhQGggkFLy3bKPOTtFBysZYjn3glByCpDcJh9cn0MCdJt7lzMRWLQH9jLgb8yZun2Vb63c/9B7OkI4t8Tv5VFDcabBgT4jrcWueryEIND7ebDH0Zn2/RmgmeE80p+AYyKyjgqYWEYmqmUO4SrSpn0zXElzhuu8jL5DWHR3CYxOIhUoj+nwZT28ouMJ+C+GHE06pRZ7je3vFRT16BwWg4z2Fz1dhIFTjYNCPCdbC061PqA4n208xNPdJ0x2ke3jGkIDFEMJtsSZMRTzPyDwbhPYFJQ5N5pwkE6J9TSV8wIEYS9IfnQFOHKZ0Urf6jMwRCs0BQbLRj+GiLUvvjLr214V7I8sAIE/g61Z4n0A2hAgO/U7iJ+VX1j8/GqQ8YYl1bHGG9g1Yu5w/IND6F6CjbDKowUIdZXalXlP3CeIFuO+UY4ho3ogWSHMjMhKOI5yLgqmWaVBuiAMOENIBJUBtBWYSruE4JJrmQ/sj+hQL3l4EcNTS2KSvfhyja1u4+o/Ug0IMB3JNqbBM/6D508qbK06k2IjwMrJ/d/ZSDEd6qFzO8ZDQwFPQnRlNZVrh6CqBq1Nj4iuTBpVnHK3Nz44ghDNIVdOReJ5bJbshmWWAVIJB6EkKAfFKRYwXiVuUhkWImw/DNn4jy1PCT0akSMDnq/ObVr6659YtltEnTxcVsFAb7jtmmuhmDA1/KKU/ooh85AbQxs97DyJzRaQ7+0UZqfy6yYgbReYyhMnr2m8N51xQ9ch5+ih/LiSvU6g0UfkRKREaGPJLDKF+YoK2YsMwDDQF8SCA2BIRMj01Ois/n6nMJMMbBYkjoZzCt+gh6lfh5wsVOnFeu27v6Egq/gvFejK07BMgT4TsFGD1TZ0eNs7m5Q6VyAt8FhDE01FPsn8CsxMm1B9vqchOlN3XXnGk40ddV7vX6NRp+fNGtl4Z34lpROjcyIGelFGDLyL3W5IKHRvOSm2utTqc3G2OXT7pifdS39RiFEOPvuENqVU2JaM7bW6FebYtR1Lec7O7v72rQxhPxFUqGBcBoQ4Dt1+wVgsaW1za21qrWwOQyMvTyFHOGhD81RrsjNF+xztDkp3pLSZms4WLVp24U3Np97pbLlTKI5Y3rq8uLURaVpC3Liy/QaU5w5pTB53pyMVaUpi026SGRv1JlmZ6xNjk6bnrqsKHlBWcri0tQl0xJnFSfPjTUlDDgMBNPhwY8Y1OQCU0ektaq6bur2D1HzMdaA9qmnnhrjIkT241QDmLxXXKo8WrVHG92lN3CvgnCsNmAlla0Bg6wSW6wz681ZsUXxllTAvc1lbbe39DithclzilPnR5sTYA7GkRht1salebcWJM7JiCksSp5n0hur2y/EW9Jun/XV5Ki0gsT5Jq0hM74w0Zym0+gNWn2no6nN3tSPGP1gbZClOTgLtgmZcHCVv6fdmx+3oKggV+x2G2Rzi2RD0oBgvkNS1+RKrFb19PQgxjjZWyvZEgaycQ7euEpAjFlQG7qqD1/eYu3pmJu56qayz6/MvznBnFLTXtHUfcXtdZ1rPFHRdNLlc9V0VByq2nLg4sdGrWV+7jqzzhKhi0mISEmNzj9Ss6W8Yd+xmt1dzvaOnuYjVdtbu+vhOSFFaw9ql1ARAzAc+Ka/asAAQjE4Mk4LV5ChGVkmVwcRtRlTDQjwHVP1jvfMQXf9sKYOOIFn9Rgq8JJnCP72uGzldXs/OPHMgYsfmfURS/JvnJGx2OZob7M24Cy4mo7Kms5Kp9fu9jjTY/MKUmcb9MZIY4JRZ9GpsQ6outBy9GjNtkutZyoaj/W4bd2OtjN1B9ts8APjh2P0KRoVmK+wBZpiEPYHJPGrdQa11WYbjEFmvDezkG9cakCA77hslqsllMlk8ru1oJAgv0qjb28D8CAQK0RoRh9plAiVqsfdVdF2fPult3dceMflduUmTbcYIzxeD77XIX6aWpWbMH35tNvgjlbbfbHT0UrxVKshTmb+JusVj8+Dw+JwKBxzUOOnBTGRFbL2z2cHtU5ItplQpw9E+/X4DXrd1WoKUc6U04AA3ynX5IEK+1VJiYlqt9Hn5dDaD/4OvB4XrEh+DBtFx3hzysz0FVguS4nIjjYm6LUGr8/p87l9Pg9gLs6UGKWPTYvKT4rKqmo51dh5RafRweXBr/L41PB9gOuDW6VGxAlyB7lZDJEJEcnIhG/W6GsBMOxwEWy+DhaZQjc1wIAuA/XtVm9KUsJQKz6F+5Oo+tA0IMB3aPqaVKnVAN8EvT9K5Q3fDSTcGSr+hNiN1RHG+BkZq66f8egdc766ZNoNLp/tbOMBq7OzsbvK6upckLtuddFtdmeb02NfkLP+upL7sNXOp3L7gbkEcH0ILcyij/n8nhZrbVJkzs2zvpQdX0wcEiSEHchUrWg3BSj3VTGyyRqR3lp82VmZQ6f8k6qPiMqMnQZEPN+x0+0EyBmHsf/sN//bbN5pTnaoAyepB0BJgh5qOO1lPe2jhtRhgBociFUWPrM6S3JEdlJUulFvcXmdrfa6xs7LMATjz8zYgpiIJJurvbnrSkZcSYw5vsPRaHd1WfQx5xuOmPWRpelLa7rO1HdewcodCGlyZHZuXKlX5a1oOdZmq+cCKGh20OqaJF8oyMoCsgTKQYadgUydfQ+94Xn5ly8nJsaRLXaDcMWbAO0tRBxPGhDgO55a46rLAkT7YOuOD47+2ZTdjpBmZJ2J4SXDmmAfK+mvAbmgAtu46xZBR7iIaTQ6mG49PrBaGqYdhxSptbhPI7f7tBqdVqt3e51guPA/83m92FGs15nxp5fYfAmWw8bAzk8GiCMrjp39gS+pUzjwZajLrcY8gWRDBt122lSdB0v+/Iv/0ukwKFHFiEtoYFQ1IMwOo6rOiZYZ8G/hrJkqW4KnBytLdJdb8IbaEUMOW73Cfl2fy+d0eKwuX48PxgR6eBq0BQB1+xwevws33UjgtgKagbNkhQ2OGABBjw3uaD5QdPqDDw6P3eGxAZGZK0W/KmfjRPBoEfQEGWXYDZYXYbzYYKFW1Z51r1txrXSe5ojVMNE6hpD3KmhAgO9VUPI4LkKtSoiPnT1tvqvN6HEDE2kkdRnVgimjcnY+2CpJK3k8viOoLEE2KYYZRz2OgCz/IKTk0oD00kPrGcPl8tH9yDQIZDgqHuL4ECaJElAVW/IQRN3vc6sdjfHrVy0bbDVFOqGBoWtAgO/QdTa5nkDEmpvXrfc0Jzo7GUKRoI9sps7ttor6KvC3TzLI6Wjge2ky30tv5Itgy0ZYKkvpOJMpTKEhjwRLyGrRN0FW5IhEcGSjxwmpa866b77mzsT4WLG3bXJ19vFVGwG+46s9rr40wJe05KQbl93edtHohEmAUs8gVij/0Rfe9udeK1UobBrKWSWiHRZYKeaGj20zKPQPxetg9h6aBSX9bqtf1znt7huuF8h79XvjlCpRgO+Uau7wlcVJ6devWVmYsLzjkt4L/y56EcyTYE9xTLASCMPw4OC5PF+2CylVSUSV/JhxW+UPA2YJnYM+MBn7sfn2SaKlZ6S8GcGXPHy96sq9+q9+5isJsYL2ildjbDUgwHds9TtRco+wmJ948PNRtrKuBth9ifEX+xpgZA2YDBhMUqAKnqyHr2IAVbmDGqO+AQKs5NMcKAOFUcztbS9QwLDyY58cWCEaSa9IR/9k92Ry7dd4VOd2uO9Z/fDs6aXSUttEaUAh58TTgADfiddmYyKxWpWcGP/9r3xLVVuILWYElmiMXY63AYYZcqxQyPKYJFowJ+4FjhyC2TKabOPg+Ehd3aSg7sHwqaz5YBFX4ccQoji5dlQKtVt9YZdn/ZyHb11/ncloHBMli0yFBhQaEH6+ojsENAA0bGxq+X+//d9288G0mWQxTE0wmOAc22PGPV7l7RbKHWYKEwDbqRBA4H6BkuN3YAcHQcLeoCvzVvk7sumCi8ST9+H20Hudjq8nygZln1NVsUt9x/LH77zxuuioCGHtFW/FVdCAAN+roOSJVAS8abtt9j/9/aVNR/9evEofGYltEQw76UGWMjBK4X/lulGDhMyUZW+JXnWX0ym/ocgrwS/LBS5kZFMFTdU/yw1yNQv2OwtdPCSlBMYFYtNGPdrrvC1nEr5y9xNLF8y3WExhPdcmUhMKWSeIBgT4TpCGuppi+lUuj+fgkaP/+cdfalKvTFscYcAmNOz6ovgoH+bO6LC0SUxy6KVYyaCXQ2bQgT9BUBpEVJUZ9BV/LBS4pQyCCDDDcOI1xuPkSOBNbpLBg1s6ILuz03fxmLokcfVj9342NytTrw/ssL6a+hZlTU0NCPCdmu0+cK2BoA6H6833Nj791l8tmXXTZkVERBtJREcfPU2YIhwHyZCFMkZWuUGXfJZi6oZ3GQuIIuGvfDZyEOPtRX9DzBMMgcMxchb3jMRIJ+xdgyPh/B3NzrrzqgzTggdv++zcmSUmowEHdA6sFJFCaGD0NCDAd/R0OSlz8qscTvfOA8de2/BWedVBS0pXWrY5LslsidZqDdisxub1FAaJmYCSXn7kL11NY7SX2lAlWJSMGAESTBGT2hnIEZoEQGWCStfeCFtVICPj1YzaKmg1CRVBigmcg8xEwz0Sj9Kjclh9ba2elhq10Zk8t3D5HdetKynI1ut1wsI7KXvu+K+UAN/x30aftoQE7Aj29ThcZ85dPHnqTHV9XX1zfWd3K86eYJvhOBzSU4UpAvsQhYGCHrkQE51ComyMoHjK1vPUINIwaPhIYAmdtq21LTrCZISVA5Ed/BofXe5DArolGb+49VeGeIrLUtgbBvDYsUdCTWpx2jyHYY3GYDTFRiemJ6cX5U2bUVyYlZFsMOoJLgu2+2l3rqlcvgDfqdz6g6l7kOMBWaFibFcyIYwQvxSWCILIv/rdX+fOKFm2eL7BaODWisHIOGAayUJBxWYiy0g+4MMigdDAmGhA+PmOiVonUaaM17IfwBbvMIS10ovWlFl/lT+DVQAnp5QG0xxI3DJOlAebxyDS8cwp2eYy9+9BMYg8RRKhgZFpQIDvyPQ3tZ7mBoZelVYCdF9pBtYU4aLAXh7VZ+D0Q0mhlErA7lA0J9KOmQYE+I6ZakXGQ9cAi9o7kGPv0PMVTwgNjD8NCPAdf20ytSVi3hFTWwei9lNCAwJ8p0QzT5RKcj8xIq7A34nSaELOYWpAgO8wFSceGwsNEJc04YYwFpoVeY4/DQjwHX9tMmUlIl66zDsXKhDLYlO2H0yVigvwnSotPSHqCdTFJglhcZgQjSWEHKEGBPiOUIHi8VHVAN2iNqo5isyEBsapBkRHH6cNM0XFIhuKBfGdoo0/1aotwHeqtfj4ri/f6ja+hRTSCQ2MhgYE+I6GFkUeo6QBHq1ScN9R0qfIZjxrQIDveG6dKSebWGubck0+hSsswHcKN/74qzrx8hU+ZuOvXYREY6EBAb5joVWR5zA1QA8rEug7TO2JxyaWBgT4Tqz2muTSIp4kDWsmAHiSN7SoHjQgwFd0g09ZAwhw7vX58APY9fr9bo/X5Xa78L/H8ylLJooXGhhLDYiTLMZSuyLvQWjA4/Fu27m3uaUd4Lt1556U5KSczHSNVpuXlbFu9bIRnpQxiPJFEqGBT0cDAnw/Hb2LUmUNeLze3z39/Fvvb7LZe5xOF/ZYYIcxokr+4Btf/sydN9GT28QlNDAJNSDMDpOwUSdWlXRa7fprV8bERDidTq/Pi8vldhXm51y3erkI7DuxmlJIOyQNCPAdkrpE4rHQgLpwWt41yxbhRGFYHnBptboH77k9NjZKuP2OhbpFnuNEAwJ8x0lDTFkxiFVBq9XcesO61JQkWHiBvwvmzFyxdIFGRNiZsp1ialRcgO/UaOdxX8u83Owbrl1lNhvNJuNn77ktJhq0V1h7x32zCQFHoAEBviNQnnh0FDTAj8vUgfzetG5aXvbqlUsWzJkOLjwKeYsshAbGsQaEt8M4bhxJNGoIDd33Rf5md3t/Rx8kB0JI/9FNC1IWck5KZhnIPuwGM5pUTq/MLZz+eOrg/AmRJacEhSG0BICJh69nw4dbcrIyZk0v1ul0rDx+rkUfraRQAqswLULWG6m08klZA+yulJD921+9WdYsTUgmLP+gMoOFDXzFRMNvYVHpoz2n1m0BvuO9vYFKL7++4WJNC958svuLHnFGt4DhR01QmexOkJAjgHfSm86QgaKGAjl4rYNBiGM5TUq+kSCHZSqjGiteAn6Wk5SRBIA8NT0Qk3xL/wXqAHe0YLXkE7lFc6bHxXu9fo/H09XVbYbdwWRAQlaGWs2yJpWVa8H+ZnWiqZi8SMxrzSBSuh+Ej1x6mmHQOBAOfBUHekrFsIEweBde0NAkD3kMamkp9Df/EGXR33HztVmZ6eO95wn5xlgDAnzHWMEjzh6v+pe+/RNXZIFGo5eRlyGLdNQkQQOKTBx6GXBKkEM+SWAq0zYJMClqK/NhSMfykgisAtE5EHIsZw9Kj1OEluhqKLRJ4lDIZRippJNkXAEGq/w+/jWJsEPFkIBNgloqHflS1mxgzAiBU8WgoMTf4EkEVQ0bBILbSqFM5RdMqqCkygcZ4NKLg69cc3ZT5Wi68I9P3Dd3VumIu4bIYGJrQIDveG8/oNKj33gqqvBajc5EEUnGiSCwCH7TGZCE8FpWU4kDh/zFwymEp3996ygIhSTQYSAjYSspk2fLrCT9a1yGciWEBQtL0C8Q/kHKW8Y7OX+FBNyG0bt0JpJy/OiFq4FphYIpM5AdoC5U3/LjlIyrVC1ndnz/i7fBrj3ee56Qb4w1IJY1xljBI86eUETigAVuiAAIZIbOnGHJ3JdNuQN/Kv4Kk0D5FHuWTt79sF1wFAGllH74vJ5R7HBXSOmSPBRp8UOFlEqRP0jf9v5K1pOMZwyqlCmpiYGXG/jMTRBU8uASJUUpdRUqEi2XPKvIXJGG6wc508wRci1I7SG5hdETYfPSD9MpzERBE5AR9xCRwQTVgADfCdBwMsbKpk6F0Aycg+fBktGAmQ4CBgR5Qhy4KVNCmk8gPbPIBn4UT/D8pGy5LCESyKxTMhswOtzbMMDLGGQzSASfSct/wj4bIl6vNL2+5/ZdOc+A2uSSFMacEMsDy16p797EnSZhw6a4hAZEVLMJ0QcY16WvLpOXk0LyukurVgNVhFtZgwBWelqC7v5AQYErZJIuQ20o6gfLwb5ldl6lLZSbfGXjbyhsKVEsUFmOcL1hU65I0GAji9JbRqX4gW+DBp9Qw27AYhEmO2kc6LsVJN3S9UOBvgN11ynxvWC+E6CZZa4UMHQOQWqOVYEXPpgPc5CRqWS/+EGdLYLAR2ElGIjRKeCXAfIQKhFIGiCkQYgdIJ69c2WzfcWYFSopr3yQVLScXlZjOfPw+BngyFyeEGEE8g6rzSfpQwJ8J0TDMuQIvXoZG4ISKMlmn1SLQ1kvXhpu0h52Ih+CoLQgjlshFI/dDZaZOT5I7g/hm0IeK/jXUhG9OLY00e+/RSVVBlTKoFeGcgq4CogPwLpCSwP1mj6aRh5yhjfwDFSq+H5CaUCA74RqrmBhw1NNNslnxtFQvJQAUPJflbA3yH6hJnYFeoVCRBB77GWA5m5mjDH2fckGEO6LJeFU6DOhVmepWuGor1Raf/gbWGKUFhGDngogLkdfPmBR8eiSWWD8CxrL+h8CeSvI6hCoO4FfuFEWXYDvKCt0LLLDzgRypjq7+rcXKumuhJ8BQ7FESkMYqAwISOnzuhHXUVEI+xiAHu4zoUATOArwH+xyoLgrGTalpzjmS4MCSaXBd17q2Ut2YDCAC9SQPBhYmFIsrck2bv4ETSiNMtQYzfw1AhcfMIK9Q+i2FOq7QCVXkaDB0g+5Q3LgX1HgxVkbHuKlIOlBHtsGQt4A1vItFkxWcQkNiAW3CdEHyG5U/soO8OL29TV1JvNHGrWZiRG5SRHxkTqdNnh1n/4VYdQ9vK5wcVGCVttnQSGuFXI6jA4RZk1Woik7yRhjBnwBwSnwUShkyTgpR7R0v3paStS9y3NKMqP0OmVZAdyUHiGb4cgP2RNH76n90Ed8tCE90RwfhZgQ1LFNdpZjKBpGfOUoAjglPns+9iD1NJONH7wQNntAZHeVKi3a8JUbi6dnxdAqKGYV/fYeJaPnYE2LGb65e0J0ViHkoDUgmO+gVfXpJcSWXCU5lQTpBTAhkMNoKP3RafxLShK/fGvJl24ufOzGwgfXTstIMCsqxEBNbdLr8tJjk2NNiu0D+ErJgyVXKWrykNBQbTZoFxclfu32siduLX3ilrInb5+xbm56pIH7zrIcGJYx+MKv2AhTSXZcUowJ8CkZIJSElTshM+BmkAf8ReLSrJhv3Dn923fN+NptpU/eVrZuXjrznA2YCai1pTf+Kv2hQXtTY/Rl6REWIxmFGLBT6fggERBFrYow6Yqy42KjjaPSBUhR/U9fRqUYkcm414AA33HfRJzHKU2Qg5A5iCmrM5Ii5xUkeL2qDw41vvhJ1c5TzV09XhBqxuLAHQnaEmOARkt+CBxi2u3zq/FRgjGCaMQuAaADX6SzdQZUOrW6IC36pkXZOInizV1XXttxuaHNfs3M9CUlKVqAomJPAcrB1B3ZIFctYueQMA8g2RhaqAjU1iBv3sCJmrh0fp9kxNboNNrs5MjPrp4WY9ZvPFT39HvnX/uk8mKdlZ42T3dBMAILKwKHUz5wsFzJxSsAi4Nq8czMa+dnRZhI/DTUGtEkdBq1Hk8rQmVAHtzwg6pzZYUMeLK1go8RTCOysVxYGAbRU6duEu1TTz01dWs/QWq+4eMd2tgcAGEwoWM0UlEHme0pZ7wUMeMj9SVZsbDmlle21bZY27rdbq8KdPWamcnr52csKk026bXNnQ6jQbe4JKGh1V5RZ8O5Erctzbl1cdaS0hSvSl3X4jKZtDctyLxhfub03NimdofdReMwqFQxFt3S0pQIs/79A7Wnqrsa23s6rK6MREIq65utM3Lil01PK8uOy02JaLd58tKi71iatWpWaloCjAaGi/VddW2uCIvh1kUZNyzMmJkX39rlsvV4FpWm3rY8W6fRfHZdQfmlDkiLuhr1mvXz0lJjTZuPNuw40dDa1dPU4Wju6EmNMd2wIKs0OxYDTEK0qb7Ntagk+fZlOaiXQadr7fIYjIYlpck3L85aOTs9Kcbc0ulcVJyCO6lxlvy06E6rq8ejXj0z5bal2atmp0ZH6C/Wdfm8qoL0qPtXT1s2Iy0xzpIaZzpX3VndZGOoLl3cxCEpPgyhVTYQhgCMELbmqhXzS9LTkidI7xNijpUGBPMdK82OYr4kmFmoAwEH3YF8a5kU/to2++Wm7vzUyAevzVs3JzXWoiWIHGOxGHWnKlu7uhzr5qZlJ0XqydGVNMCNz3/X8twFBXEHTjV0drnuWZ6dEmdcNztt+YwUYFB9oxUQRM65pKdbGvW6xBhTm9V1qckOrupV+Rs73TUtPQD3CIMuMcq0sDgxKyWizepMiTVcOys5IcpQ09AdYYCxQqPV6Q16zR3LMnNSIo6db4qLNHxmTb7ZrE9PiizKiLl2fub56i6PFxFICHVFeWnxlh6X70RlpwdnzdOj5j0+P8aM0pz4xaUpCTFmm905Ozdq+fTE2iZrS7sDApfmxCVHm9PjzA2tPS3tzkVFySW5id0On9tDqHKb1dPd41o7O3n59KQrLba6VseqmekFKdFxZsNj1xdFGLUnLzTnpURy20fv0zylwW9QcR7YfCGMPXoUO4vIasJoQIDvBGgqaZ19IFF7IbHMxHpcnvf2Vb/8SaXd6Vk1O+2+a3IyEyxVjbZPjjXanbAuqA06baxFr6XGSOBnXJRlVm4MILvH6atpsuLbvNRIEhCSzusPXWit73DwmTy1mBKjNDEwgCKzIDUIQ0Fm714/udPc5fjgQM3O8ubYSGNMpGHzodoXPr6w+XBdu9WFNLAkZMSba1ts3T0+QDaswHEWI1tifHX75Q1766wON8FZmiHsFfjH5fFgrYyrA6OAVoP1wzNXOn733rnKxp7i7HiX29fQ5mjtdiFNUqyltsO16XhjbasDAA5bR4zFcKGmq6nT2d3j2X6i0e5Sl2bGON0+qKK1y4lyy3KiCrOjLWbdq9subjtW9/HBGlKlgR1NBgGrkgPIQG0pvp/8GhDgOwHaOFw0gH6XbEJQmK402V2uHSfrfvXGyQNnmtITIxJj9GtmJX3tztIFJYlALuZ6BTczmFi9PpXRSOy+MFYsKkuekR93qaHbZnd9sLfq8LmW6xZmfOu+WbNyY5kTA34D6TBzjzSB5OpJcGGfD8w6JdbUZXPB/oBEth63HfDvg/WWOEH0ONxAzy672+3xIYYvNen6C9Oj185NS483NbTZXHB28/k8Pm9ds93jcwPTyV8+r8fjbet2GnSa9DgTtQ9T3y9aWYQcQoZOt1er0+h0avD05TOTZ+TGoKzWLtuiwuiv3Vq4dk5ybAQGCmL39XqRPQlTRBweiE1XHROhn5MXNz07GnaMLpRiJE4YwH0YPFq6HGRMgl74smE4kOUrdQPhr9JKPAG6nhBxDDUgwHcMlTuqWUtvdQB1w+BvX5AcF2mclR1XmIJ1ew3Ir8OF+bo3J8WCGfdLm85W1nYSzAT4csdbf2N7t83pbely/eG98l++dvT5jy8cudAUE2F8eVvFf798VKfWFGbEABQJ+qn8nT3uM9WdqfEWGF4z481psfolxQlp8aaKuq5mcFusYIEAE6j02R0ueKTlpUYlxRqLs6KjzXrgaVOHHfB9+Hzzr1499ssXD/3lrZPVTe3E9kFgnMVx46F+nS73nvJGi0l/67KsorQYENjsBEtheiSxpFJqDGJud3g6rc76Nsdbuy//9q3yv31wvryiNT7SACPDS1su7DhW1+PwAMUB+06vFzwapL7T2mNzuDtt7qc/PPtvLx76w1vlm47UdxFWrl4Ma7hJN784CYrFwMTaoH/8ZObg8MYFSnuHu696VHuTyGwcaEAsuI2DRhhIhHc++kQfn88X3NjbL0+5yQdygkPglvyZfyA+W3ER+mvnZty2LP+a2WlZyZGnLrUePt9iNuqL0qOXz0qHgdVk0B692N5m884rjK9q7Dp9BYjoxVIbDKArZqbPK0rYf67lliVZD6wrXFCSYnV4Nh8jRgNWAg6h6La7IdbcwsQVM1KxvBYXZdxxon7niUZwSphuo8z6C3VdnTaXzeFJijUDy1bMTIUJQq/XHL/YXlHTCda5pCwZBa2dnxUfZz5d3VmUFZcWZ9p+sgHsWHa8xcS/wwoE9s/IwyJe8urZZKkQaqlptWO1rbnDcaG224XDiLy+ksyYx25f+72v3Ll6aVFzlwt2i2lpUUvKUvLSYiwmHfK/0mRPjDFPS4tcUBB/pdlW19ZTkBF9zczUFTPS1sxNO1vdfqnBWpYTNyM/fk4ebOMwhmuOV7Y2dzrD+bCFab9+CLC9tXr5vOL0VLHgNlC/n+zfi2Dq472Fweke/da/mvPXarR6hrvhHJhkfzCagNWJpCNUmPm3gvSmxJgjzfq2buIhAO6LZ2D5xWpVXWuPUacC9cMUOyFC1213YbYPXpsYG4UdGT1eX3Vjl93ptWAdLM4CE2ttm63H6aQFyet+JLe4KBMSuDze2pZuoCR18PJFmnVwOUB5mLVDGh2MBgmY/KvrOuxRBg1Q24kVOr8/JSYiJcbgcHvqWm1YUouKNMQYsE7oJkuNyhk9rV+UxZyVGGkyarCIV99ixePRFq3T5bU6YGImNBjs+I/fvTc1Z9qKOx+zJOVjBTE+Sm8x6lutbhg+nC4PaCw8y+DtAPZd39bT4/REWowZ8RaDTgUBWjp7UH0cZFSaEwtzyfm67qQoQ6cNpgru4MG02k/XoV/yBHJK+sHfen739x6/df7ssvHe84R8Y6wBAb5jrOARZ4839rF/+Ikpb7VGa+CYGoZWKbhvMA2mVlH6HwUMMh+mYMZnwAwkiDcruemjG7rIRJ9HquRr+PgOyMmhFpN8uitMOX3m+CJtY6D586xZecQ7Qh406I5iVij5kmGrBGUkKyYl1rjIWiDXIK+WNLjI/3Jo5luapajoftWzP7zf1nk5q2TV4tu+kJxdTKvJ6s2tAsyBWcqWOm5wJVFTcAA8A/qhI5o03kg59m7hYOQNQWGA767vPX6bAN8RvxkTPgNh850ITTjQKk5gE1oI8tJtxQyyOXCwsAWKjQDyfeAK2VtB/qG7L+hqmlwy/YoFXGAhDhSXzAG5+ys2a0h7gmlMCoK8ClMpg1y2w4MZR5Vfy/dxl3/mCQMVkcqWKb40EDA4VWzgrT67ff+7zzZdOUe/YLEnyI4S0u/lPXF04ZBdbIMF3xooZQaFsFwV41af3YbR25CvWeYMhvunzBOhOwoZR0cDAnxHR49jmkvI6xzYr9V/qYp5MSOXIWtFAUgPY8hgwEORmZZCIIMRZ/4jPd1r9s0hiiWTAEsaFGSkVTBhtjEtAJqBz8qhRCFLr2pTxwsJ+aWhRkrF8LexiuIvr084r1wKmLJOJI2NqGGVFDiQ0bCiMo9IDvHwuNSAAN9x2SyhQjHC1J+RccBqhGfPCgxUYrOUmP3LQuPwexz6hyKMAkNJRXpB6oCySwlY2TIfZzIEaYX9EepQQPB3A/D3fJiS2BMhqg1nVmep+m+DXm0UJjk1Ao2oKQetL5FwXGtAgO+4bh6FcDKhpOgSDKWhcDa4OoUAQF94IBM1IAY2rWEzcZRZp4cbsIKQhyA7XLjMBp0esRI401XkrTipkts/uIGYzcoHg0psDi8ZaKVVRSpPMHNV6AH4e+C9vzZUneNrkBxK+aimjP1AsbhfMfgYEMa2ECiQBqJkf4YgMgzZg6rl4BpRpJq4GhDgOwHaTrlYNVrI27va4agxp3rMGAqHsLVzM+9eOe2O5Xkz8xKAsDKISDhE0/v9yTGmxcVJJenRAGuyckYBl5coIRK9R4L0qKUzgcmmCcnuyk2wnNtSJONfUXdkfoIzgzGSibxYRvUTNFDJNb1y5pP9G/7acOU8HTWCGTxFfhZITWkLDtVS3xafIISVVzjDwTjzXJ4A3U6IOMYaEOA7xgoejezZYlfYqzfnHfC1ZoA6wPSZEUMpGaGUav/S0uRrZqZg80WEUX/jwsyEKGwzY9YQBliciloMmrkFCXetzLt2fkZWUiRd42Jikk3CajVcKhjIsvRkKwVgXBM4913KlaMhc1AgezXohb0UJBQv23fBAqJzY4QKm49VLE6xHIotRGkXT2wh9ocr1P4gjywsUT966YPqypn3hbyMZStkkM8IGbCVRqPfiDzGtwYE+I7v9mHSBVkZhv/eDoi5MgqFU4raYjJg/9juUy1na61Y/4+OMEaatIg0xhNTOgmMTY4z56REYUuFyajPSIxEZDJAYVK0KTc5Am7FhWmRRWlRCZEGg0aTFG3ISYxArJzijKjizJjEKMTW1UQjeG5aZHKMESnNep1Rr81MQoIY/KTGGkG3oy26vJSIKBPsHj6zUZOZSHx19TptWqIFoX6LMqIToowI4BB2wIJT86n97wN/wX8lxA3jf8BxeCDM5eoKprGB5gniv0qTvcLrbiL0PiHjGGlA7HAbI8WOZrbvfrxdG5NLd7gxKFb6KQzW+qsAhb7hO+CKy4sKwDE1384rSEyNN6UnmC432StqO+bnx3s8/nYbiV/DPAkMWg1CpBdmxl6o6QDeAD5rWnsQcmHF9LTrF2TjflF2/PzilCizARvSlpSlXjsvKzs5GqFwlk5PRTTIqnpbSVbMQ+uKEJ9sVl7Cpbru4qy4WxZnF2fGlmbHY9sbnkqNQ0jfQrvDXdvWU5Ydf/PibMSOiIowrp+bUZYN8I2JjSJBI3d/8PIPf/DN3s1gMhkevPeWf/nhj+JSsyNjE0LUySF7cGaB8M4MYfzMlFL4bS0kpGSGCCk5mq/IhMxLMN8J0GxKKOjTANFvPQaFvMhBMntKmbFpM/mNw34Soo1Wpych2hBt0Z+s6sxLiV5YlmI06sjXVCw8HRNlnJYegx2+l+q62rqcqfERmUkkmA2ipkdZ9Ai/u+lQTWVdV3FWLHLTa7VREfr6dufbe2vPXOmanhOfCN6LpAhdptK8trPK6fHduSIHwSje3FG18WANNgSvmpVe1WLv8fjz02IQgzg3LRaxGrCbbnFJMmj4gTONl+u78pIt+SkRxCTdx5WSkrTn4xfBf3t9zwwYA8wtFPbo0JTKR8PlwvTLVyEnQM8TIo6lBgT4jqV2RylvEnerDyTpvXTT+53ndwYBK+HlpbvGMuIjbl6UefJy+9v7aoChN8xLXVSSiE3D9e12eQsFKHkKwpOnR8MIkJIQER1pjI4wZCRYELEXWWAL79nqjjPVHVVN3eDI8IXATYTUKa/qqm6xn6vpQqx3hJhgh77tP9uEXb9GoxZLdoi5c662+1RNJ+KsA38dLv/pKySOT2ZCRHq8GXnaHL7UODMCYibHm80msj3aCAau0JjNRsKS4cosWcV+lq1/UDnADL6hhrVWRscwZnggm/tCnVUGX7pIOZk0IMB3ArQmW1uSrmFx34HYnEILYRgb4CI+CsCovljXfaaqfe/ZlqykiKxkS32rHREheKAutQoxa3BAJ1AVwRlwkoXZqEOYm4xECw67xPiBmL9IYDZqYYvAKhuwGLHFYA6OMeuwRhcXqQfowkLBVu/AZ/GI1UnCTsZF4FQNEpsCVBlGZxgxyqvaEZUHC4BA9fLLHTiqE3HaXG5vU3tPRW3nUYQbbrHJ1QDyJiblvvf+FlpH9ezVd93+5L+Tn6/9O7szyFGJJuuPFPdhhWBzAuWDgvlOgJfuKogowPcqKHnERWBNPwC5/XqJSgAQBBJDQN4+RUWwc0QfXzUjadXM5KK0iObOnoZ2J047zkuGPwPfi4FgZrnJkZcbrK/vuPzC5osvbb144GxLtMUAzzPAj8mgK8uJXTEjpTAjurbF3tTpQAgeOCfMzo9dVpaI3ygCtlrizeBDfEgidIfVfbyyvSwXMcxSVpSlwG/4xOV2JMABQgipU5ab0G51NiD8rs15vroDIxSQHSMEHCJwiBxxp1WpGPK++Pqr3/7OD/Hnno9f2PfuM8HcU54YhIfWwa26DWir4Iod/mrpiDuRyGC8aUCA73hrkbDyyC5KhKlRKhVIJnmsSnf6WnwPfC8bLfticny1nxXGsBWB0D44VAuei9OGcGPT4drNx+o77a74aCMJfEDPuMAYgdiMRyta69tt3Q4XYpCfvNQGSwUiSSIHMFYAYlK0ubHdsau8Ad/iHB/c7HG5Yf+90mzfeKS+24kjiJw4KcPmJEHWcW3YX33mSmduagyMGLtPNx6uaMUBxm6X98DZpv1nG49WtCBPq8O1/0zj2ZqupLiojOQYrR7U243AkkDepKTcXzz9V2NCbmR86s6dB7KzM6MSUi+fOhisZVZfRlFDfpRo2SdySiofGFqpPidElxNCjrkGRFSzMVfxCAsAQH7hG/8SUXCtmkY1C9o5q3iN+9jkhhQhJDgEIJSOE+EllWEJOxn0OHRNq8YE34OpPj1VCLhDfckIcDGkpsf9sDk6eRTf4tyI9Qsy5xUmvb+3CoYL5IMDItxu902LshYUJT/70YXmbjfZiEFDs+MgYzBcxlsJKNIdCdgvh2BqbjeJ7ctm/8hTsqPyGBQAZYNeh5s4HBQPvf1/P2q6dPa+7/xXQmYBbBdN1ee3Pv/LtobyM2fOrbzus5/9x/8LV9tQdQ2m7fpCXvk+m41IAx2Javb9L92xQISUHIxyJ3UawXwnQPPScIccJWVSGgKifZDYAblYIEFY44TC1EwwzuMlRJUYcOnh8sBBBrsM4gkm0lPllZSZbopQ4bS0hvYeHBCEH3I0DzEBa3DOUF2LDdkBHBHul8dL85Po7DJNpzs0/A632+UCfeZ2V1SWbJyj5VAbAvmNgiAbsWWQVS3VHV/79y/+15sxafmgwPg2OasoOikDyFtaWqyRnPZ6tf2A6gp6QmEsDn0wjDJlxksCvYlLaICEbxXXeNcAA1a2Vq5ksiErRQMuxA8I0MpJNy+pF1GmaEcZuIR6gWgNvRTJBg0QY7iX7T7ZAC9dyT5Mbl6st+4obwAuywjON/jKbF3p5UE3M0vnHHHcZdvneLGKyGnsjhTojO83Xv2Zry1fc3fpss+suf9bI2zyYM0PCrKJlNL/IyxdPD45NCDAdwK0owS7HFLoP+EZcD/42/9Cfe8Mgwvlu9cYmAawV4K9YN9Vvv5GoYb5oakb23su1HZZKc4yxITRornLWdlghXmW7h6mcCkPLhTepJuSVSO4DjRv2WyiNKUq78vtq46Iib//n/649v5vJmbmj6TVFVLw8TAkN6WYvUWmNF3YfUfSApPkWQG+E6AhiacZfVvDUizuQCrVI7AFQOKxEk2Tjbehy0oDqEBhSAhgL3uGDwEKB4wgfywO1MwWzKBSwl5SHxZOnUIRtRcrjA0M+ulvGeAC8itWHQOgLdeCaaD/Sg30fUBFynz6I7ySwH3mHABqgb0T4KW7CiIK8L0KSh5pEWQJiyAd+xUWW/hNpd2AxZ4hwC09EmKmUKAVN6YG4DpMfsq8g6CNw470iDLbUA8sCRTleGhshSsAXIqM6Ue2cserQI+lVwwugfGIgnQw7MnpJH0poF2yUAdViWYglxUYWBQZhcwPQjQiCRxUMh+keJwHJqNgviN9IybH8wJ8x3s74nVlEWC5E0GA4Yb1i5K4aAj2DOpPGaYDqWkZwZgThLX95SutwilyC4wenDhLgCez+sBYwfhr8MjRu7hQz7BBVFRatgutmCxcGD2EDGAKQA8RWDGOKFFbQvY+Zi/jvRMK+cZCAwJ8x0Kro5wncbcKcDKJx4YrROZiEmcMm7jfKbnyy0CpMsYF07pwuKygsqFsNATugqwVshGDc0VmdqCMMYB8YYaB3maBgBKCSDWvQgDmQ116+dRC9txQQL/MquUK88GDiBeQQB5KGNYq2DObuLDxRFxCA1QDAnwnQkcgr61ivk1faxJ6PCwp5d8G4SJ955XAER41A1yTz+L7BVcCJ9SqEfZHyfsUtmFl4gCAMQuDJLlEEzn3Vdha5LIU5crQ3Esbclm9lhP7qZcC+4Ns7OFxM2heQM1CTHMBAszqpYBlxSLhROh7QsYx04AA3zFT7WhlTJervF43cYX1edgPwWIaWZyCspcc7sA/U7soiTju9WInBP2hf5LfLBn7lv/JopKT3Lw+r8fPkrEMscWXZUYMrfQm2fRLilPmL4nEMic5+H0QlQrJop/z4lhBVGAC2ewzk5/nryLlerBJQsXz4TJL8rO6u1ldArWg0uImqSlREYu2LteUJ5aqSRQTqL4cl53qk6tRoStWI65zWclS/rQU9iBTlLLQICG9XGYI6SULi8LZYbTejomcj9jhNt5bD8TpX3/+m5oOgmYqcgwEdQ+gm8qUTq6kGmz7F/cSoGSLeBGwIFpBabmHLtkSTKFdeowQNnk1iHymlJH8xsX+oRYQupOCpuU5SWdVyLSRlKxghWxGr7y4nwPzgyBZ0kXFxubWCLM5wmRkp9jzkD3M4M25MfP7oBuamTOFREm56wR1oWBck04WyLY55l5A0rMK0ov7WdDv6NRCVh1jsJLlhu27Q3Kyo0+LuSJ7nptEuIIk84P0KNOM5JUnMW9SIXW0wf3lz91RVJA33nuekG+MNSDAd4wVPBrZX6iobO+wgloxTGCus4rdBXIZFIoUJYYjWBIMKTNiUBOYDzNAoqEk5ezoB8lkKf3LBwClj62ywuzpwC/pD4Zf3AeYPUBNBKq/v/ZuScG0mdOLdDrsMQ7SHZ/TEyGppAp/LSYjq5i000IJjrw4LolMO4PzkBFXkkcCYGXmoaVKDwW3sozu0m2pJhTDLWZjXk5mRIRlNLqGyGMCa0CA7wRuvEkiuoT6+Pfnv/y/ebNnrVq52Ggw9IXo463W8vA0oC2BjUUTpV7jTc+TTx5h8518bTrRaiSBFv4l1lUcsslJ8cSoiGRcGFhabooYOKFIMSU0IMB3SjTzhKgk9WiGaYWBMcM0cQkNTFoNCPCdtE07MSumDJUTukg3MWskpBYaCK8BAb6iZ4wXDZAID4EFs/EilZBDaGCMNCDAd4wUK7IdsgbgXUE86EiEdjwraO+QFSgemFgaEOA7sdprMksLEy8irONiXmOTuaqibkIDYnux6APjSAPEy4GCr7iEBqaABkRHnwKNPHGqKO2YmzgSC0mFBoarAQG+w9WceG4MNEB2znF7g7D5joF+RZbjSQMCfMdTawhZ+JEdQhFCA5NfAwJ8J38bT6AawubLgzdMIKGFqEIDw9KAAN9hqU08NDYaoGFxSPyyscle5Co0MI40IMB3HDWGECX4QGKhD6GByawBAb6TuXUnYN1olF5xCQ1MAQ0I8J0CjTyhqkjNvuISGpj8GhAdffK38QSqIVzNcF4EthlPIJmFqEIDw9OA6OXD05t4akw04PF46AFJ4hIamPwaEOA7+dt4nNcQbLenx2G12bqtNqfHjTMmrTY7PtvtPeNcciGe0MBINCCOERqJ9sSzI9UAdrQ5nc6XXn3nfOVlu9N9vuJSXFxsdGSERqeZO6P0sYfuEaEeRqpi8fx41YAA3/HaMlNJrlfe/OD3z7zY3tGJM4zJucQatdFofOY3/1FWki8fiDmV9CHqOiU0IMwOU6KZx3MlQX5vvG5Vfm4mbL04RggXDBE3XLe6qCBHIO94bjgh2wg1IMB3hAoUj49UA8DcqEjLnTdfFx0ZSc6P9/tjY2I+d9/tWq12pFmL54UGxrEGBPiO48aZKqKRszKvXb2ipChPp9P61arbblqXlZ4C48NUUYCo55TUgADfKdns46vSsPOqLGbT/ffcFhcXnZqccNct1+n1+vElo5BGaGC0NSDAd7Q1KvIbrgaWL1mwZMHsB++5LS01SdDe4WpRPDdhNCC8HSZAU3V3ddsdTixDhQT7YhHAyC/5C7pBQTFdZx+DnuOPhN5W5CGrJCgzRSk0TynTEOMAS4YTgQKKlT6Sm+yzvJImHZVJcvN5fRWVlxMS4uNiooI9zFhRxDoh5RDIipQn/ceyZgVLyuktRh8x00K1Kz1IMqJ5cl32H3EN3/JKkuRM17IotAVNRkN0dJROp5sAPU+IOJYaEOA7ltodpbzffPfjqqYur9dHEY+cdMawQM1AB3fJOpWMO/T8dZJKOhOCIRzH7gCGKoGb5sLF5ce383JkEKWF8IJ4wRLKBaBOOUIERJDkhcz0eGIiHT7J6sFTcHHwYoOFzwfOqyFLbeQQY3quBcNyhr38QSThlUQa7iEB5SjSyVgp1UnZFMHwyRRCBKcaoHrkqlNiLgdVmog/wLRPZQqkZMMf0z87loPmTFw46LPqxCjDjdcuT09LGaXeIbKZqBoQ4DveWw5v7CNf/5eeiEKtXk/xSkNcYVnsRUKpFKBBUEHND+KRqWcQXwulzkCPAEdl4EMzZnSNYxBBQcrgpKIUXJtijISiFJkZYnIcZNApMVP+BSuAPIb6SHXh6CpF8/WRtCwhA0RGPiWw4wBOJQvgGoE2iSTLUvE7MrAqRhkpR6kI6Xn+CB9amKIVvBgq5iMYV6eEvjICs/pzvTDgxf/Uhw4Ev+X8Pz35mbmzysZ7zxPyjbEGBPiOsYJHnD1e2C98/V+M09boDWYW9oCsTwUALjTyuIyvAWJJZJCxSxaIM+FeAgY/xx7lEKpIG/R0kEVCgr+QjJW4r/DflVm8VAwFfiqDArelCvC8Q40r4ZVMSuFsVia1ckppfAh9VALpMFkqeLCsUCmZrLRANdknPl8I/OPtqtjz/S/eMXe2AN8RvxsTPAOx4DYBGhAzci0744FxUz9oIJ38UkOARBalD+xm7/vsEelHAhnlTaaKcBly7knK5UUTTJb/VOowKI0it6A08n0pE5abZBFGBWkdyY/0QTHIDFw7nj+nq4w4B9eL/CUpSvlBqmngW7nuVKqQ+8Hq8gX9SVl5oCFYq+E/r7evcW8C9EUh4uhpQIDv6OlyzHIi1l569SKl4fgZne/2igzGoCdwKY3CATooPctyYGmkK5Anm4jLBgPpT/kR+VuWJkjIcLIF16uX6CGVpJyVE1cZr3srQpodBGqtzBj2WEUdZc0qE1ONIRkH7tBaBJcYqt5++oJsNR6z/iIynhgaEOA77tuJki1p9WsgZBpubXqjJDPMKuGagV4QZklLS8FpQx8MeUSB9b1NHGxuH6hmCHgz5OUFSEDO/pTzCnwblBPLWDkyKaCW47miuszIHGpF4JkMTs0hox0dpOSJw+CyEKkmsQYE+E6ExpW55fCF7YcjhmaqpLrBaKvgwYpEki2UrjtRqttriOiNjQpKzGbj7GIGB+oVEABTCW1l5A2CwBCWzvIJYrlKMOdfS3UOsrrIQM9WDllGzNIzuFlHQJOK9bnATT5XGKsBdPidQzz5qWhAgO+novahFEqcAnC4A8eiIDY12GwGY67geUkAxME1xPQQBn05n5PxidNQpb1CEpPDcljLQ696ccyTxQoypvSDX71yZxaKYGofVovUNMxUxbzCSCpMOnArvO1CAuUQ5h2mVQK+F1yOIbTIYBtZpJtoGhDgOwFaTKMdSZgDbiOVzKQKdsYwReERzCFeyUplKtsLdyV7MHXbpYgl5RZidOZcmBsLQqwDbHIvO7GF2mLDmblZcUHyKIwhYWiqRM1Dnumr5dUqrVZt0nF/MmonUOpQfmxoACrTXqqOCdDrhIhjrQEBvmOt4VHIHwFuGUINPS+OGuzBEPxlGJAYZUyOMeq0ATzgnzhaMERlcKG0+JLNELiwZyLCpJ+dHzczL04fPEgo6GkvsJGME5EmXV5K5Mzc2Ok5sRkJZqUYTGLm1ByAcynT4BwVfwXTUGkhjN6V8ZprIySPAJxnp0TfuDDDpCc+Jr0MKQPz3H6bKZiCD71FxROTRgMCfCdAUwaY6DDgd6D6zcmPX1ScZDGA6cm7yYAvGmlbA2N9CgCmIEZRl8OvSafNSooAhuo0QCu2hS1gJ5GeRE+TMJyNJD5fVoJ5zay0GxZkrp6dsXpm2vr5GVFGHZ3kS3vDiPCcgeJ5mWPLzFHCZbaURoume+jo54DtmXHyhChjWVZMYqSBbY+TBxNK2WlqJrZanZEQuWZettmgoyEm+A99pDdlDbIaD6RsUh2Zhw8isUgymTUgwHcitC6f0JNXd8TiBnJgG67SEiOzkqP0iDWg1YDrAW4iTDqLUUutnWrsqiP0k66BGfXkVGHsPQMERRi1kUatju76sLm8xyvbT1xq95BHsDdYG2HWIxMAF4pAYrNRazHStBJ5R8lRZu3y6SlzpiW2d3uOX2w7fKG5srbb4fRgHxg2GYN0xkUYTDp4yhLnWZ3Gp9OoAIaxFr1ep2E7xrAmptWoIk1aJMYfKA4JDHot+Y3KaDVGvTbSpMdvgrUaTVZS1NLSlLT4SBY4AvgcYdZFmzlf91Pkjbbooy0GNylUcjoOpt0KOj9wW4SZqwz80IhbWGQwQTSgfeqppyaIqFNXzLc+3GqIz1eBVzKKNoRLNiHIz/A7MgjMyU80GbQnK9vzUiMXlSQlxZnnF8aXZMb0OD16nfq6eRkur6+ty5MQZbhubprV7gKgLC1LnjstvigjKiHG2N2DEy99OckR0RHGxg5nUpxpSUninPw43HG6PADT2dMSFpcmIUOAYKfd5fIQXAPCTs+NXVKWWlFr3VXeeLam41J958W6TqSHnaEwI2bl9JSynNhp6VGdNlen1XXt3IyC9OjCzJiZ+XFJsabGDgfEyEuNWl6WXJYdmxpvsfZ4TAbd4pLE4syYaWlRFqM+0mJcUpIEa0ZuapTT7Y2NMCwuTsxPi4qyGLp73A63d3Z+wsKixNLsmLhoY3O3E5R0SVnS4uIk5JAaZ0mLM207Wo+691Z2f+aUPpqGjEGS4ntaryyfX4LIbUNoRpF0MmpAMN8J0KoIHTNcKTnGBna9SRkpTbwggkiXnRyxqDgxJdbUYXUBkpZNTwIUluXELCtNUvv8QE8YKMA3ga0LpsX32FxOh2tBQfyCwvgIgwYIOD0nJtaim18QPzMnxuHwNLc7vB5/UUbM/MJEfADPnFeYkJFgIeVT3pqWEAGKeqGuC1A4vyjphkXZNyzMSokzxZj1189Px5Qf40FOcuza2enguAuKU+YXJbpcyEe3tCQ5Py0mMdq8amaqWa9p63IVpsfMzo+PscD0HF+SFQ0KDAINom11eBrbnGlxlnnTEiJ0alQHhVt7XN1257S0SECzy+XttLoXFicVpEUVpUeunpli0usgeVqcGQoZttJlHcswHTxiSobo4TaqeG5yaECA7wRoR5/PO3qzVYXXFLWnEtdaiogsCNepy+07TjQ2dxIAau92XqjpAsONMKrLcmMb23pau5yz8uPbux2bD9fuPF5f32ablhoRaSTuGLApRFu0eSkR9a22TYdr955u6rB6pqXHAM1hBABpT4k1J8eaiTGCuipQg7EaMAw7RkyEMSclevWcjPQES3ZyZE5KpNGgTYg2GnTqsuw4UGa9Tmu1e3afajh8oRVfISvYEArSwXB1FhNsCzoQVdglUIPaFusnJ+ou1nY4nG5kHW3RRVl0kMHW46lutoPOn77cWlnbnpVgiYs04HGzQQtSnJMUWZYdHWXS7TrVvONkQ3lVB7h5P5MMxdJl+ImIvC7Y21IsfB0mwCt3VUQU4HtV1DySQlgkg+Fbe5U8KxTD5ahjLH8YW9u6XTaHu8flBXwAUY9XtAGh5kyLz0qynKlq83lVsFE4Xd6ObleXzdltdwNMYXFliKrTwcyq6XF4um0uhIcE2wXu4oPd6aprth4401TbbKcTcLIcBhz3eP25KRGwBh+/2HqiohU34TgRZSFGWKfXbzHpT1a27j/bpCUwrQJudjvcVocLBem1WjNdmnN7fDanp/xy27maDhBkyN9pdbZ09hh1qpk50VmJZthJ7D1uGH1BY4kBGnX0ej1ur1arcbm9IN3t3T0HzzRcaegmpmSVCqzf4fF225zUst2fhUdyeCMVD9u8wbRXXqyTlvpG0iXEs5NCAwJ8x30zDsnG22dt+pjq0jUxFhQYvJF99oKN0vCHgI+L9V1dds/K2amgrqcutSLg7uWG7sykiEUliTPz4rOTIutabcBEEgBBrbY7fS1dzry0qGVlSbNyYRnQdQGdtRrYjt1eL6y31h6+lAXOe66uq7bVPj03bs3c1NLs6PxULPohpbYRhl+3L9Ks67A6nC53u9Xl5aHBfMzdAGV5fd7mjh6312cxawHzDpcbxgQs1ZHFOgCwH8CtS4s3azV+GKQhAIs7CaSGesDN0xPMzR123DHoNXaHG/c7bO6mDidyXlQSDzPxrLxYfGYx5Pq5FPg7QEL+NfXwFb5m4/6Vu0oCCvC9SooeSTGMLI3J5Sdcr7Xb7fOrrT3e+jYgGqGmTe2OmlbCUm0O77GLbVggO1/d0dAByuvdcqT2UoN1AdaypiVWNnRtP9mIRbjWbheYbGuXa+/pFiy7zSlMnDktAWAKN4Yz1V3JcREluXFRkXoa9YtGw1SrUe6mI3Xn67pzU6KWlabkpkdXNnTXtzsa2hwfHa43aNWzp8UX58R2O7Do5W9osyF/DBGgq4B74HhNs21neZPJoAd8J8dbYOTFV61dPZ12N4h1u81d2WAzGvSpiZEdPR6gPFbYqlpsFxut2akxOWmxZ650ll9qT4m1zC5Iiok2odrHL7WXX+4oSo9aUJzU2Omsa7UD4get80E00CCSDLo4kXAyaEDE8x3vrQgG+rmv/VNM0XqNztjbd2Ek0rNtZUnYYaHTtHQ6YRuFCaCp0wnimRhF5v4gg7B8wvYKByysVtW32YGb4IMJ0SbYUvFVl90FmNOp1XFRRowQwEe4qsVGEj8zcOS2LifMFzERhugIA76FjQKgifuB+bhGHRdpjIk0AKZBP2FYaKP+DrDDJsaYYN8AjW1ot1nt7tREi8/ta+5yGojB19Rt91gdXpSCZIBp8OnWLgcwOi5Sb3d4220umEGizAYUDXaMCI5gw+Dg8FyIjzbCQw627E6bE6beWPgVazWAd7hPIBlUAVE9Pn+33QVfutoWsONBKbgfuxDzNiOKZpZ1SFKx47uP3zFHBFMflGoncyIBvuO9dfHefv5rPwb4qnWGkYAvQwEGfMFgwcLYUKst/cQ3+8LsoCEetQpnVW57ZmLwvV+S/mR6Tq0YHHIUyqUzbl4OeZpamalZlZ1HQf8lOdPDMJgdhMTDZTYHGAFogXynHReXUmhpwwSPV06L5I7AckbUzMxBkFST6YJLx80LwR68xLd5KBOOvvCX3Ze/xaeuCzu++0UBvuP9vbsK8gmzw1VQ8siLkM7CGW5OMoAyn7Pgi20F4/bIAK6ynQiKeAjyXq+gvWqKPwKgTEFeXuhn+Mhgn+Uv/ybJsD9CpcKpbRyJZTSXNoPRx/neM462HLNZUmay5uceyZN7accb3YwnZc023rHaMjnIIMDGCoVVnOzGGwry9tUsIeOWJO7wdooPt+3Fc+NVAwJ8x2vLKOUaS+8kBofBgMz/omSYEcuAwVJCWBlDeyuQn7dGnw5CMRnRZLyXIFB5bJrEz6XnJSkYyQ0SRsbeYG0xqzLNW7E/jaVRml4Z3soakJUwOGNDUMXDYnXYm0FziYnQ+4SMY6QBAb5jpNjRzJaCoJyhEj0GVUovqsufks0L5AN1b+B3lIQ3iOVShsmsACFckeA3uSUZRsIIpuCSSgsBe0jG68BYIIMUtYVQqwQ1RXDLCQ+FxuRR/Faw62CcViKtAoXJ46zu1MShzHZQ2g0kGiRZ7qs5hliaSD7hNSDAdwI0IT9tfbiS9jOBZmjrJdArnW3O5u+SEYBP2Dl/lM2mxLGXIR5B3WBG2cfgwG9LTDNgCuVPB8E2tTtTLzi4YWBfdYzFgJALNIgaAWssBsL1jQAl9t5JJuIwFJ7bGGgJvOCAcYGhtvwNPlFnDDVOWCM7LCRL7XC1HvJcYCAYBq0eJRlENuNLAwJ8x1d7hJWGxtZi16gZIOTIYQCoBYWJ6XERaQmRcwsSF5SQYDfJ8WaYfLnRgIM3kQHODNgu/KWbS69fkNm/4oJpIP+LeZlFmo0zc+MXl6YsLEmek58AFwtWtQBq+1VZSZEPXVuEMGmA2RsXZH711rL7rpm2anbm3cvzoi2mVbOyblqUgx0cK8tSrylLpg6+8lgQkEuaMTDEZj9kGOGb+ej6IkdZkgXyIMbl+QXJK0qT+b6/ICvF8LuK0lgySII8/MLEkxNEAwJ8J0BDsZX6kVyBlz84J0DPrLz4kuxYkF9Eb1g3N316dsyKmSmPXF+UGh9Bo3/JoSDJ7mOtXr+wNBVuW0cq2pmNIWCuCDIcS+yZAR4DP26z1aTGWpaVJS8oSpxDiwaGSg4LPBFSRkUY8tKiDWYD4uMsLU2uaLDtKm92O33YZKzX6uKjTIkxZp1elxxrQZwdyn7ZKhaF94DJmsovrbFRy4XMQEliumOD8GdEYls1M70gK06nN7Q7fdctyEyMIu5xfMAbtOolk3SwwSOUBPf77aDLEgknugYE+E6IFuTxbUMXxoYquwwmEgQbdLp5hck1LT1wm7WYdQ6X5729l1/bcRkutMnRZiCXDw6zESZgHBxsQXvjI42RZkNHtxPbwkiQG70e8XGAgzQsoxr70yJMBrPRgECOJKijRoPgC/HRuIFglBL0woqgw2Zf9e5TzW/sqdl4uKHb7kUES7IPjWzv8CfFGuH2q9HosIfYqDekxUVGmXVWxPFxeS42dp6r7YaVBJiJApElSlHDCKHRRJgNFrMpJtKUFI2NF7q4KBOC+GCfG6rgV2khJ8RIjDYRt16VBkmizBDMkpcajbASyIKMB9NTEEQtPd5U197T1O1eNl0mvyO3EyhGvBCXjqG2oEg/iTQgQkpOgMZ856Pthvg84m41FA8ogmVsui1dQayX/pEaF4HwjwjFi0g6YL5J0WbsMctIikCAhZ0nmxxO721Lcm9cmI7YZohVdupS+x1Ls3JTIxDLBgbZTpfvobUFy6cnzylIQBRHhN2JizLftCQHASRzkyOdLl9ZTtxNizIXFCWAqDZ3Igga3TDmVwEZEXDyUoOtxeoEcQaM37I0G6HRGtudMRG6R9YXVVS3W8wGFHr4QuPD62Bn0CXFmDRaEiUHUdOOVrTlpiGApQbhbxDDDOaCxvaeW5fmrp6Vgrhri0uSZ+XGU7NGEownLR0uxIm/YUH6mtkp84oS8VhLh3PFjLTVc9IQZW1uYcLM/Piqhu7V89LzUqKwVQTbSS422rQq9fxpcXtONY+S1UEB336Vo+3K8nkipOQEeO/GWkTBfMdaw6OQP59QDzGnEKeswHRcygeQgIC82PiFcLcseHhyvOnz6wtvX5qNUAkAy8Qoy/yi2L/vqP3LpiuREaaV0xNf2XKhucO190TD0fOta2ZnqP3e37xz6vXtlQiCs6AkEbbpKLO+vrXnrf01epM2LzXio4M1L225hKMuELqBFktMA9hLhjhk96zI+totRbcuzsBKGoi20QCK6tNqdQhwriLLaMSK22n3/vHDiwhP9v6BOkTXRdQes1HP8qHyErsBMdMifLtJV9duf2Hn5XO1XTBjYNPzthPNAP3UONPMvFiTSfvyJ5ff3VOdHGtKiTcbjDCfaN/dV/X8pgvIMzrC9O7e6oZO576Kto1H6lFyU3sPtrohds8QVT6o5CM1IQ2qEJFoAmhAgO8EaCS4IgxPSqVXE2VfyjUtAmAGTPZ9QENiukWMsUv13b945dgvXz2WHGO+fmF6XhYgV/PQWqDkNLMBIccQz4wsTLldHnghxEfoaltsbd3Opk5HVZMtyoRDL7wwXNQ0WxG3AbHQCjOiH1yb/8UbC6fnwjAh+Uf4fdjs63C4PzhQ89zG85sO1HR029ELEdsXkrAjgCC218OMt75uG+Km+3vsPdh8DOgmRxcxLwWyiYJ7ZeABNwnsYG/tsHdZna2dPZfrOxB0DVuWDToVAl3OyI55/MaiB9bmI5g6MVSo/DXN3UjcaSWZIw32ICNImt/jQZgeyAejCowsMGdQnQm0HF7vE08NoAEBvhOhi9AwjHyHAcfQgdeCuB+YNOWVIERe9SeL/XanGzQTZBRwRsOBqbqsjsq6DlghgJ4IL+bxeH+74dx/vlL+7y8d+2DvFRLvjLh/Aax8Xg9ijxmwM02vRSAFHcE6hGvEbbcH8dHApqubba9sq3zq2YM/+9uhvafq8TXxKCDo7fH4EcXc3tgOy4MDaAfvrqQYM/piUhSOASIndiBEGQFhD4nJi29VPjdxO/N6NCoffrDOh2rA9kFHE+qoiwoQugwKj/whBcg8DXOGwrze8kttv3v75L88s+8nf9l3/EIj5EBcSeL4QLu/QcucfFU6MHmPBxnodH6YXHDsRlgj+zDAmDvlce4/ciPyROi0QsaBNCDAdyANjYPveeSDUEn6A4EgT/5Q/A1kVNtkBfm1UFqKkGWIZf75G0r+4b55eWmRe840nLjYXN/m+uL1+XeuynnsxuIICxa3gG9++AY4PeojF5pn5MQ9efv0e1cXJEbrD51vRMgcGHABsIDNS3XdiLNz4+LMx28tveuavIwkC3MlZuEqmY8BM0rjZnWjtSgz+tEbi+5ZlYcD35j3LWWohJLzQBHEs0JFPX056BIXYGpbYR679AvEKuFoTEcJguuVdd3x0aa7V+d//vrim5fnwjsC9zHiICfCbgHiag2esjk88/Ljr5+XqvN7cxIja1ptOPKIOaKFKH7w2BncCvJzwdv5xkEHEyJ8KhoQgXU+FbUPoVAgy8PfeCqmeD2cC6QZsAy74XGg9x4qydOVl8v8W4kBwe1+aM20hvae/edbEmIsmUnwU9Ag+uKFmo5OmxvkE/4BcAgzGdSX67sq6rrgIpuVZOy0+no8Pq1OnRBpzEmNhEGgsr4LQcsQCj0p2thl83T2eODihYPUEPA32qytbUasSDuNpkugFmbW1BhDa5fH7vaRwywQ20GrKciIgUPCxQZbeoz+TFUrMk+NNVxqtKv92qJMc22zo8cNdmyItRgv1VvjYnHcjxpRxxJjydpfS6cjKd7U43K3drkR2Aw+Djg9CId4xkcbOq3eDrsHdmSE90Ut6mAn6XSlJRD8bbMRhw0sFSJ+JgTG2cZYGwR/33u68Vu3z/jocM3Jyx1sj8ngL0nzvF3kP2XmiwGh48Ku733x9rkiqtng1TpJUwrwHe8Ni/f28wDfouvUGrLW1L8Fsq+tq2HAlzrGghpmxpuunZf1yYl6cD1YXHGTAg47SJ7N6sm2BBIM0U/cFViQG7Lvg2aKbPAtWx9jccDYF8ShlsfupbvV6KYFAvqBXch0rYy5MNOsWPxGekoot05zYfAt23PGcmbEF6DNTvqhFWFqUWAcPUiZ8WJ2aDLzAqYPSyEiyDMM/cl39KAL/LF8RgrOpvvNhrMk/yH5l/TaFBcOfP0dF3Z+7/Hb584uG+89T8g3xhoQZocxVvCoZM+YKt+NFS7HAANmSfkDctLeDJmePQHo0dS2Ozfsv9LU2UPdB/h5bhT9iEWU/FAPBQAwFqCIS62SDVLbAfuPACnbgcdgkhUpwa6MqNJ+CoLTioGEpAYO890kMsNnZVEHYPpDYZf0WVaitH1CtmdLpnEqJr9LgkOSsYBUDfd5kDP6MPlfCrTLSscNxHf/84fnifWY14AOHoO4eicLO1KGts0gchZJJqUGBPiO+2ZlgV8C9I0BWpApkhG7/jFC+c4rp9IACMQ4d8HGELRBlzFJDvi9p950LJAHBBlnuVRcPI5rQRomWTFMUiwgslvsh+I+o88UbqWQO/K3DNyDLwVblr5gZbD8pM/B9aD5sCoqtz60tNvt5Ai7oMThdi8HROhL+X2A9hBtGeO+hwoBh6cBAb7D09vVewrQQJaqyBSYvcsKlhvYVht0XxJOgVLy00rBWaiFvqya/bM9JoqE6Hw8CKMVNqWXEDWArXSKzsGpN7aHV69yyJFGoJBMAhAdVFGpLhIa8nDqgUkCG8y4nH02LoPg3peyUZhagkQNzk+OqnH1+pAoaVxqQIDvuGyWYKGowVN+5RWfAuaF3ojMuTA3uLIMFbAhWyfCQYkM5dQcSlGpdzIpqgNzP6MXc2cIunjBARYdwtklU6ySJMrgxbi1jLNKJQRnGEjDIF0JzYoJAVMjmyLwDwG1MrM1e1wqiRc/6D7Cnw9n+RH+woPW4lRJKMB3ArQ0lsUYqCkAtTcYSsghvfkBWCEPymG/GMELQE8v1iYBEIUhvlYVwDPJwEEyZH60LGvq/ksZOr8bhMIBwaXSZRCUrSWsvKBLQtJAZYMHoYDlQ8Zi5QjTe8RhyCtdynGCnSsvoa5C2cFjVp9ql2A3QHvZwMWxXFmtwRL9CdAzhYgj0YAA35Fo7+o8S/Y/cNDgL7MMoOzdlslpEOML5rYysgTNiHshSyhnVKCVDKD8QxDzZdgroXAYnixLGpiSBwYACXZlB1gOggxJZRraB/KFlBZoFBkQQ5h7uAxZJgzNe+UQYkcITiFBPFeLrHY6X5CTymuCZGXy6vQbUco414DoB+O8gSAeWe8n+8nAfwkFpj90qxh+yBGTnNiyzxwFGf1kO8qkBAxayPYw8kMPblDyNBk6+S42zmTptjTOc8nWMP5DbtO9ZPw3ue9n+5SDZONSSYIp/qTCy4nluvBhhn7Liqa1YOXyO2RDWt8/TFqFNoiTXICbc2rOhA/ILxVBKyJVOXSqQe/LRfMBJ9AQISYXMiGQFS4Rez+JUdy/w+D475JCwtHQgPDzHQ0tjmUeeLUf/9ZT/oRSjdagof5hzEuK+kmx/+jFfFrJJzbTDTBM5l3F/bKU7l2cGUqTYzxGfRFo3iiKk2XGrJm7hcK0TObpgeUt6oAb5ERBCqXBF+jFZ9/EnYufRsFHFSo6ccYlTr/qHocTkSR1WoQVI6gFnOP0UZ69c6lo7dm4RHNnsvKP/BvmBEyTSPxZ8nxgGuNaY0qTsiJ/UO9jlgt/lleD6ZwVFTAo8Epy5TBt8XbiamcF0FEUuywufu1zt8wsLeB5in+mqgYE+I73lsc7/uY7H1y8VIuwA2o1iWkAh1qCp/SoCXk2y7CIb22g03+ygMSChwPVKPyy9NRpVvLC4nZJErqH/E8ABcmws5dsPmBoJk/F2a5gyvtIQioJSYjc+e4Hcp98S8cHhvgsB45+NDUdCgi6UX9dya5M1hTVmr0Hj6QmJWWlJ+l0engWB0lJkEuyzErDDqmORJWZxUBCUmUKaSjiYMsRlOOvVD/qzkfvEfH4cfKkPmx7B73PnN+Ia7Ns0ZZQOTAKUpSlacnYIw97HPfV6pTEuDWrlqYkJY73nifkG2MNCPAdYwWPRvaSSTQkL4YVwUZK5XxWab9k9wMEkcMJz7HXSpeEer2kV/JD+UuO6cH5K6bWgWKD/dpk0sqwDZD2q9/+efbMGSuWLTDosZ2Pga8CgoPEkfIKI3xAMulT6FKehJlcX0GScKBVKJdXQCF9X5qUG6RvX165PqPRNUQeE1gDwuY7ARqPsadeF6NXwZe0VYESXsXF7oeklxP3mbm01YFTuXCZSCAbmr9Cr9JXoR7FQUJSgam3BNvEzOSXf/eqKUW30Gr2Ugdnq31oUJo39MpHEl4qQhIjoLFw6g0ouS/faTrKTIAeJ0S8GhoQ4Hs1tCzKGKQGpFWpQSYXyYQGJrAGBPhO4MabbKKTCXm4LcmTrZ6iPkIDRAMCfEU/GC8aoMZQealrvEgl5BAaGCMNCPAdI8WKbIesAeIAwbwyxCU0MAU0IMB3CjTyxKki9aAT6DtxGkxIOgINCPAdgfLEo6OrAUp5qf/y6OYrchMaGI8aEOA7HltlyspE9ngI4jtlm3+KVVyA7xRr8PFdXXj5CtY7vptISDdqGhDgO2qqFBmNXANkL69gviPXo8hhImhAgO9EaKUpI2MgWM2UqbKo6JTVgADfKdv047Hi/cVpGI/yCpmEBoavAQG+w9edeHLUNcDOqhOX0MBU0IAA36nQyhOmjuwUoqAjICaM7EJQoYGhaUCA79D0JVKPugYAty6Xy+F02h1Oj9/vcLpsPbgcDodz1MsSGQoNjB8NiHi+46ctpqgkQN5X3niv4nK1y+0pP302IT4uMT4O+9xmlhU+9Jm7hNvvFO0WU6DagvlOgUYe31XU0kODPtm1772NWy5VVR86euKjLZ9s3LojLTV1fAsupBMaGJEGBPiOSH3i4ZFrAOB73ZoVGWlJanL4ETs307t88fwlC+cK2jty9Yocxq0GBPiO26aZQoKlJCfevH6NxWIirg5qdUSE5eH777GYzVNIBaKqU08DAnynXpuPvxqD4V5/7ar8/GydTotj3m+6bs30siJ6hLC4hAYmrQYE+E7app1QFVNjne2eW2+yWMzxMTGfufMWi8k0oeQXwgoNDFkDwtthyCqb0A/0cRDyeKiTv6Or+9s/+tn0ksInHntwfNochA16PHSUSSODAN9J05QDVASwu+fA0UPHTjtcTp+XbmYgx1VSKyuJohs4QgI7HfgX9Gt21Ll8lHAg2C7bi8ZtAxSX2C/6iB8HwZPdauRfmpAdIIx/EC+dfJJ+sTPjIY7X4/EdPX4qLi42JyvNZDQijdfr83h9+I0ULA/2SzrpXd4NJxso6B2pPCY0rUOgTixoMP1PzocKzk84VpyXzOqDGqj8EWbzLTdcm5WRKvB3qrwwY19PAb5jr+PxUYLL5X7+lXc0Wu2s6SXAIoAKCSHGkBXn90jQSLCLYCGFXw6+HGU59NH0vTcBMzxjKEjhjuZA8VeZGLHSeVkUjymySanJgODTwu6r1THMJ34P8H+AMBJespBnDHwV4M8gUcZVCeypQBTZ5bEmSHA5h8DR8vQcDQa6DJ3xqMPheu2djyJ02qd+/A9mk0ng7/jo0RNeCgG+E74JB1MBAJC9p+f1t9/PzspcvmShBJFBzFG5vMW/CBvnZpDLYMEopyhJej6YrUqgzWGUQnI4jB+wtgrxOLeV8uF59s5WJu9y5sG6sNl7/un//WpmYYHH5/nqFz9HqfuAcogEQgMDaECA75ToIgDfru7u9z/akpebvWThPMHdhtTqVpvthz/5xbeffOy1N94tKSm89ab1AnuHpECROKwGhLfDVOkYmHqDsGnJCWkCOobc6B63JzMj7Y5bb9i+a8/5isohPy8eEBropQEBvlOlUzBzKi4BvUNtcoxbiDuh1+kwb7j79pv/+Ofnurqtva3eQ81WpJ/iGhDgO1U6gNPpwlKWwaCfKhUepXrCYoNAaxqNFvkZ9IZZ08tWLlv8698/QzxGRqkIkc3U1IAA36nS7j2OHvgZGA2GqVLhUaonwLezuzsywsIW6iIjI5YvXZQYG/3am+8F+3GMUnkimymjAQG+U6WpsWQP51qj0ThVKjxK9YTXXVeXLToqUspPnZSYcP36tecuVOw9cGQcb1oZpfqLbMZMAwJ8x0y14yxje48DLrYGwXyH2C5w9+3s7IyLi6J+d8QnGWNYbnbmbbdcv+HDzXUNzUPMTyQXGuAaEOA7VbqCy+nSarQGvbD5Dq3FwW2bmluTkxIDW/tUfgxjpcWF165a8adnX8SoJoy/Q9OpSE01IMB3qnQEp8sF+NDpsXlMXEPQAAhvW1t7YmxsiJeIyWiYP3dGWUnhS6++g8W3IeQokgoNCPCdOn0Auyrcbg/my/CXmjq1Hp2a+v1t7V1R0VFk73PwFRMdtXjBHLfb+/HW3WQbtLiEBoaiAcF8h6KtiZzW4/FoYXfQEZepoV6YeuOkNeQw1AeV6RGhAediwuNtGItUXq/X6XaDvLs9OGPzqs7yibeDzarVGxqaWmrrm6pr66uu1Fy8fOXchcryU+cam1p1eu3GLdsrL10ZiXLEs1NQA2J78VRp9Dff/TAmOnrtqmXgv0MKmgCsczod723clp+bPW/29OHpCxDW2tb27POvZ2ak33zDGoXzQF/5BUI/4BzjC5VVp89dRHiK1OSka5YtjLAM9pALjBlgq3qDgWztG9aFGcNfX3nzQgWw1ceispHAPzot5hDIE/+zg5avW7ti9cqlwypBPDRFNSDAd6o0/MtvbEiIi71u7cqhVhi42dLSdv29jyPG+Q+++Zj8OEA57EblQDgbFnpMCiSBZau33tuUnpqyZuXiyEjqNssCWkq5KP6UQkfSwJQwqv7nb/+ckZaKuI5I/Yt/+1FOFjlbk8Vco2NJ0IX7LE/g5ic7djc2t6y+Znlm+vCP45RCv4XXXE1t/Y49+3Ozs5Ytnj9U3Yr0U1kDw6QDU1llE7HusEgiKi6LczsM+bG4D5MFojNiZam1rb2+oam5pe3ylZq6+iaH09lttdU3NmMbGHIGDWxqbe/BHy43TVOLSXprewdwMCE+9q5b169cvgBntcGC0drWcbm6FgmsNjvIaUdnFz5XVtW0tHXgT1lKfH7m76/Hxif89Xe/ePEv//OHX/00JTkeYR67rVYcdXy+4jKsATBGoLzGppaGxua6hibQZCZPU0vLxk92b9y29+KlK3BzHkbF2SN9qIzfdnvcsKUg1ORVtocMuzriwXGiAe1TTz01TkQRYoyVBvwql9t9+uyFqKjI/NysYZSCafWLr76Flf3ZM0r+47//8Pwr716pqX/mb69u3b4nJSX53MXKX/zmTxnpqRmpKVt37n/272+AYjc0Nv3uLy+++PqGDzdtr6i8nJqciLAS//37v8Ixdlpu9sWLl//43Csvvfnepq270lJTDAbd03999U9/e/X9jdtOn6ucO6sMhgXGXsF8P/x4W119IyRPjI+NiYky6HWdnd0vv/n+L/73zx9s+uToidMourvb+vNf/fG9j7cfOXH6d3968cSpsykpSfsPHX/7/c31Dc3VNbXZmelZmWnDqPuAjzS3tMLgWzgtDychiXBxA6pLJJA1IJjv5O8MmLu73W5AGayUw6wtg0EaIb2jra2pqWnBnBlPPP4g2Ou+A0ex40Cv1x08fLyto+PUufNIhkOA3nx/U0dn9ze//PAD99x29nzlx9t2dXR1IaylzWZv7+j8099ea2pq+9aXH/npP327uCD3/U3bN23fd+8dN337qw8fOHRs6+6DHi9Z3EOxIN1f/8oX0pLjfvGr3//0P3+DUmBiPXP+0nMvvb121fJvPfEIaO8b72zscbrau7rhcrt+zfKHPnPbpctXTp46t+aapcsXzysrLnjkgXtmTS8eZt0HegxnbcDRIcJCDCniEhoYvAYE+A5eVxM4JQFfzfD9zMjhDvLRF2pVakrS+nXXgAjn5GTAzpCekjx/1nQEWjx7obKurnF2aZGtx17b0LRo4Zy11yy9dtXS4qL8hqbWjo4uGC68XjfMC1dqGlYsmT93VmlpcX5megqcB5D9ifJTO/ceio2Lrq1voEdp0NMs1Orli+f/9ff//fgjn62uqfnxv/3ixOkLZysuWa12GEAOHDmBVLA5gJubjfq5M4pvuHZlafG0pMQ4GFpg6EhIwLFE0RkZqYjJMEbtB8MIwqvj6M8xyl9kO1k1IMB3srZsoF7AL+JnBvAd/vY2LGuhq5DT0zRajU6nJ4ewaTXYLweIhCkARxPZrD2bP9njcrsWzJ+NsvDjdLjsDgez/yKaGhIDwdnRcTAggwiDw0Iwj9dLHeB8cXExWI679prl82eWgvDKR6zBqhsVGXHvnbc8/sj97V1dh46fgs0X2cHNtqggb83KJddes9RsQglg9joIRksnNgsiMTnJiB5PNGYOamx9z2QyikDJk/9dGtUaCvAdVXWO18yYk+/wwZeYLIBsdIOGGqYAflgbEBm4CdDLykyPjon6ZPf+5MTEgrzstJSkgrysCxcvf7x116Ztu9rbO0sK88FAtWoVkBHHUII0Hzp6YuOWndt2HbhUVTurrDjSYoqLjSkqzM1KS5g9vZiCL7F1gMA+88KrGzZu3fTJ7r0Hj8GuOi03q3habkZaEg7ZzMvKnJaThWfMRjiT8SOI6CFsJGa8Vqu1mE2wfhwvP4vVvzFqHIgIOdnQIi6hgcFrQCy4DV5XEzhlY0srPL3SUhCiIH4Y1XB7vRcuXpo9vayoIPdSVU1CfPyKZQuxxF9b35iRnoJVOCA79mD4vT7w1uLCPKzsJcbHNbW0Hjt5GuUunj8bbrARERZ4I2RlpM+aUZKdlQ6338PHT584dT4vJ2vp/DlOt/PgoWPHjp+C08KyxQvgi8agFJx12849ew8cPVF+Bhz55nVrbl6/JjkxHkzz2MlTR0+caqhvBF9OTIxvbmnPzsqYWVaECJBtnd1F0/Jgf8AjtXUNVVfqsjPTRuJt1o/SUKna2oYF82aK1bZhdK2p/Ijw8538rY8J98nTZ89fvDx3Ztm0vOxhVJiev+kA+cXUHj5byBDgCLcz2A1AUcEucQcGB5gXELISaVgRWApDYlBd+JZhYwLdJod1PzVW5/Ab2A0fNTyODRdg1QDZtvZOJIARAxkqgQwACvYK+wXstjA1MLdgrHLZ7T12uwORdi0RZjzudnlo2DYdDBlOl1tPI8ejUJvdgWwjIkCORz+oEPI/duI0lgG/9OgDw1CseGQqa0CA7+RvfSDjgSPH4ZW7eN5sUM7hVZjslqA2B+XOiF67JELNnsQeKh8oz+wIiq0ZYTdZkEJ6bd6QXWiDvqLnztM7yo0dtBT5HHn5FOSxMQpg3zOc246fOP34w58ZnmLFU1NWA8LmOyWaHqQU4APKOexlJw5xFBllBFR+pqAZqkySMvimMk2vx9mNMDDJvwj5imz2lRMzCOY/UqlSFIixQV5CwL0+r8croiRPibdotCspwHe0NTou80MwX7hDDX/BbVxWql+hrlLwHYq9HtharlJ5E68hhMR9akCA75ToHDDIwkUBNtCpcWz81UNCmB28Ho8FfmZXr8wp0WOnQiUF+E7+VgbgYpOFRktWuq5ObVEcws3sP3xs554Dx0+expa2QZQ7EtPAp4Z88OFDZcUOi0G0r0gSqgEBvlOiTyCsDol/ONxI6vAlOHHyNNxsB6Msq9W2e//hPz33yp//+soLL7/98mvvnjlbMYigM4j269i15wDCOKC4wRQUnIZEOJN+hv70cJ/wuD3ElYJsb/vUBoDhyi6e+5Q1IMD3U26Aq1M8IprBDQv+XsMrDht5X3v3Q+x1aG5tI9HRSFh0B5x8afAwpzJPBDs/Vn722RferLxcPW/2jDUrl04vLYY3GJzS4FhGw7HD9wtOYj1sqxuQGu7AXfQrbDv+v6efP3i0vLPbSqJIII5EZzcCqCGAGSsCU3wESEMUNIiB6GUoC7uKEWINmzgYuFOXuB7EkOzs6mb5I5QEAkqglK5uKyKrDa/6/Tzl9ngdLid840Y9Z5HhpNeA2GQx6ZuYQNLpsxXwwC2clju82r76+oYPNu+orq3r6ujIz8tu7+h6+c33tu3aj4hiNXWN8XExcL9lOSPUzjsfbDl34dKjD91z7+03zp5ZCvBFgIV9h44ePlaOOAvwyn3vg83nK69gY0T5qTMbt+0+evIsNkFEmIx/f/ODbTv3wjUY+F5ckLdj98G33t8E28XR46cBqdmZGS2t7X95/rVLV6q37diz7+DR1tb28jNnt2zfg9rFxsUg5BlCR77z/mbsmjtzrgKDDYKr7d53eNfewwhyVlVTm5yUgG3Kw9NAX0+1tXdUXr6Sn5MdHx87ujmL3Ca9BgTznfRNrMKmA9BCacPucOobGRWBWApetwvQabX1IFDkho2fYDcwNhy/++HWd97fAlc2Dr4Aoys1CN44Z2YJztche5Fh79Bojp08s/mT3U1NLWCvO3bv3777APb7vr5h4/FTZ6OjECTdBK8xs8mIoA3YsYxxoqq69n8Qf7KxJTEhHhT7N394FlF6ETXtjXc/PHD4BCj8qdNnn33+5SvVdch+6449W7bvRQiIdz/csmvf4aiIiIrKqnc/2FJVUwcnXASfRNhfbI6Gv8dwKt/vMzD4IoRFRMQoY/qoyykyHIcaGP3uOA4rOcVFwvScnFus0w7bKnnLDetKivKwPffLjz4IoNy6c++smSVPPPrAw/ffCSK87/BJTOrZxB/WA2xdo3EgZBMHNwgAdhHihpw9oUHUBRKIARjqsPcY9bo504tysjPuvvU6HAm8fu2Km6675ujJ0+cqqr7w4D1ffuT+xx66t7a6FhZnRFHQatUzy0oefei+hfNmwpRx/bo199xxI+KiYQvJpSu1u/cfsduwp87vdjmBv1XVddiFERUVsf7albdcv2Z4W6v77zzYfQdXM7iRTPE+Jqo/DA0I8B2G0ibYI4yWktW24aIv3CTMRiNOs4BDK9AGBt/EhDgYOi0mU1JCPCI/eDx8iSwqwoLACwggCQMuUZNUIgn8iP2/MCj4/BgMYJDFxgQE8J09s2TH7gPPvvg6TirSgymrVIhPBuBua+tEcclJ8TgkjYCmWtXS1k78urxeGDFQNHYh643GlJREo8EQYTGhjjibE4epYQ8x4BCR11evWITHgfEpyYnpaSlwSADij3rLkYBpNCrbcFU76hKJDCeMBka/O06Yqk8ZQXGMBd3eNnx2BpZqNptb27sQBwc2BBxLceL0+QPHyo+dOnvq/MWczLSY6Ei22Sw5MWHRvFmOHueLr7//zofbtu899OHmXQgrAajFAezlZyp27D1YXVePRTsAsclsXrFkIaKdwVbQ2t6JGGkgxWcQFLihCUQbJBcxKs+cu/jeh5uxroV4PYRmshOU6UGWSE1sKdRFDbw7NiYadmSDUV+KEzdmliHccEZaCgKboeL4PUatTYJVer2I60alGIm33BgJKLIdvxoQC27jt21GSzI4A8BsCuMpIj0ON/KWGsB38Fh5fX3jzNIiRCbDYWvHT58/c+5CbHTUPbfdkJuTwYAH/Brhy01m46Xq2vIzF06drUCUspzMdLBXLLLhSAuQ0+4ua1Ymwo8V79pzcN/BY82tHbNmlOFM4riYaGQLcwFi/65cOh+werz81MlTZ06dOb96xdLbb1lvt9t27t63bPFChAeqvFyFcGI3XrcW4AcxwMIROA0sGIHYYS+m9Y0ryMsF7sPJAYcuY/FttPSpzAeH2V2uql60YC49HZltbhaX0MCgNCAC6wxKTRM60cVLVSdPnS0qzC8tKhgu+Kq6bXa4K7idrrmzp+OwyHMXL9U3tcBym52RXpifo9y+ARIKXzEgYHNrO9b64qKjgJVgvjjnAkCckpzg83gjIyOxKIcjOHEHtHRaHvA5BZP38xWXYL0FfZ5RWogjNeG0ADcxo8FYUjQtNTW5o6PzyLGTRYUFaSmJoM+Njc1zZ88EG4aTA4hwWUkBTim6VHUFBgq9Vk+yTE9BEYh8BivEqPs5sC4Bh41Pdux58iuPSvF9CAuf0L1FCH/VNCDA96qp+lMrCPEkL1ZWYSaem5M1QmLWT0yy3tWTNlZwwA+JYcbS938qe+8ELDBQ/5ukB8xzFFviRPlp+L1986uPKzivAN9RVPBkzkrYfCdz67K6gfoBD3DuwwiRNwT1+opAJitUCkXGb4RNP6BIIQlIlLSBnhno+1FrcSwfgtpj88qo5SgymkoaEOA7+VsbscRRyZEsuE1+HQ2rhghp5nJ5hGKHpTzxEDljUFyTXAOIP4BJ8bADO0xy7YygevB7c3nI2aCKPITNYQQKnWKPCvCd/A0O9yxM1RW7HiZ/la9ODXGQEgY2bAyhxbGwPuISGhisBgT4DlZTEzcdZsfsKN+JW4XxKTnb3oYtfwJ0x2cDjXOpBPiO8wYaBfGAENjohY0Ao5CXyEKhARpJ3UviSRL0vWrrfKINJokGBPhOkobspxrY0QvwHYvNtZNfd/3WELvbQH4RbGiK60FUf3gaEOA7PL1NqKfIxqtBuGhNqDqNB2FJMF+HE+A7oPfbeJBWyDDeNCDAd7y1yCjLA0dUnx/xJLUk/MHEvMhx8/1K/mlVze1yW+0OC48nKQy/o9x1J312YofbJG9iW4/j7Q+34hQ1hG30k7MdeH2JhVKyUlJk499hny49vZ18B8zDXQJtPC25zb6lKaRtEyy0DWLxkmwA9eQrhL0hcW8oJ6R5kIMllBva6F+kYCoISqXZkVA5iBBGpWRikYvmTT/goofYk5ylY+bxN89Eca49E4YVyW/zU+nZhjtpnzWPdyn3AiaVBOf0aVIhdiGAA6s5UmCHBQ7yqKyqfvCeW3Oy0qmGBP5O8rdpdKsnwHd09TnuckNYmaPlZ06ePu8nx/9wLKUg5iMww5CPh4RhoCTt3iVgQmGGeVHxjb2kghSgVeR/eZFJQktWf47LDMYpiEt4xjJjwE9zYTlQadwe35Hj5XlZmYiJQwP+qojEFHHxicpMwZrhJZdDMQaQrIPGFJqzVFooBLNK8RRcB2yk4MMNh2GmE/IfibnGhx5JHf6UxIR1a1bA4UEst427rj/uBRLgO+6baMQCIn4uj8QogxFlczJPGyZwhDwWQvv6yjS0VAl9KRb+6nd/Wbpw/oJ5MwORehTZ9kUshyl/b8UOhrwGCiM6BBfGDrdhhysacduKDCawBgT4TuDGm2Sig3P+12/+uHThgsULZuv1bOdCYLiYZJUV1REaEAtuog+MIw1QA4NMcAkZHkfCCVGEBkZVAwJ8R1WdIrORaQCb8ZhdV8DuyBQpnp4AGhDgOwEaaeqIGPDGmDp1FjWdqhoQ4DtVW3581ttPNuONT9GEVEIDo6sBAb6jq0+R24g0QBwIqMfviHIRDwsNTAQNCPCdCK00ZWSk2yxE9LUp095Tu6ICfKd2+4+n2oPvwm1WR7dXiEtoYNJrQIDvpG/iCVRBEnRYOJdNoAYToo5EAwJ8R6I98ewoaABoS8I2IFaC16vWaFmQXMQDwjUKuYsshAbGqwbEDrfx2jJTRi7sfq6prbPa7ADc1975oKSwsKx4Gky/cTFR+TnZIkb5lOkIU66iAnynXJOPtwr3OBz//svfb96+227rAf2Fq4Nep9XqtF997KFHHribOD+IS2hgMmpAmB0mY6tOqDqZTabbb7kuJibKQyOY4ZfT5U5KTLjzlvWC9k6olhTCDk0DAnyHpi+Reiw0MGdG6ZwZZTiDncXSBebef/etkZE4IULQ3rHQt8hzXGhAgO+4aIYpLgQiqN9xy3UJ8bEIVg5VFORnX7/uGnHc8hTvFZO++gJ8J30TT4AKguDOnz1z0byZJqPBYNA9cv/dWG0TtHcCtJwQcQQaEOA7AuWJR0dNA2qssH3mrltTUxMXzJ25euUSnTjoftR0KzIapxoQ4DtOG2aqiQVzQ15OZmFezrXXLDcZjYL2TrUOMAXrK8B3Cjb6eKuyv7vbevpk+d5N76erWrsuHjmwb++V2gaxyWK8tZOQZ3Q1IPx8R1efIrehaaCjs6uy8lLN+ZMNx3doW07NSFJ1OnznHcnJs1alT1+Uk1+YkZYsYj0MTaci9QTRgADfCdJQk07MbputoqLywsnD9Sd3W9rPzkt0pUbxWJII6lvRoT3nTYsqWpwwbV5JSWlWeqowREy6LjDVKyTAd6r3gKtff5u958LFysozx+tO7tI2lc+Nd2ZFs41s9NA2doC9X4PD5I+3+MrtKbFFS7OmL5k9a1ZqSmLoafVXX3pRotDAKGlAgO8oKVJkMwgN9Didly5XV5w+Xnd6l7rh5PTI7uxotU5DsJY8zQKa8bPk+V9Ot2pfjbdWl5k9e1VS6ZJZM2YkxEYNoiiRRGhgvGtAgO94b6HJIR92DFdevnLu9PHWi0c0DScLTW2ZkT6D2kdr52cb2dixxdKeNrLTjdz0+RHuwe5Rn27V1JsL40pWpJfMn1lWHBcVMTk0I2oxZTUgwHfKNv1VqjhiQ1bX1J08drjh7H51Y/k0c2dejN9IjAr8ZPigHcSKc4sJ+tIkPrbjWKXucqhOthu7YooiCxZkFs+dVVYSGx2WBUvk+SpVURQjNDAcDQjwHY7WxDOD0YDP66trbDpx/Gj96f2+miNZ2ubCOLVFr/Zz825fYXOkcOo00AP+DwCyX40/Wh3+M13G7pgiY9ac/JmL5s6cbrEgCgSTCP+Qc+DEyfODaSCR5tPVgADfT1f/k7F0wKVf1dTSdvzY8drT+3x1R1I8dQXR3miTRgW3chkme8XMCfBVBr8S7ErgS0GbACyB4Gar6kynwRFfbMlfkDtr6czSYrPJEC4Mj2DBk7GPTYo6CfCdFM04TipBYNff0tZx8sSJ6lP7VPXHE53VuZHuWBN11SU/0snECq+FgJFXqgUz/srwy8wPMrAy+zCW6BD7t9muumiP6I4rM+YvKpmzuKwwz6DXKZzSQtBYHFE0TjqKEIOyCIRPFZoQGhihBhhJbevoPH78eE35PkNzeWzPlUyLM87EQJNgLcVfhsEBKO3FVTk+yvjLkFc2I/D0fgK+LBuPT1VvVV92xVnjivTZ86bPXVRalG/QGyjD7k2FBf6OsKnF46OmAQG+o6bKKZsRkLejy3r02PGKY7stbeXJ7poswK4RxgFmtaUXg8LAbwUCh6y4BUy+CsutkvoCeVmWAYRWubzqGpuqyhnTGllsyZm7aOmKomm5er2uF/4K8J2y/XTcVVyA77hrkgkkEOC1p8d5tPzssT3b9I1H0ry1eVHOxAg1DYnO2HDwpWCjAcgNT0/lh8FxOfsNprIEgkkRBNLxL8mlx62q6tTUeGJ74opiipbOX7IiNzMNR9FPIJUKUaeOBgT4Tp22HtWa+v0Ol7v87PkDe3aoGo6nOyuzjNaUSC12TICRUktBADGlggkIKjdSKEhxONlCsTv0b4q5iovybJ9fbXer6u2aOl9Ca3RpUtmKJYsXZ6YksjDtfVwExkdVOyIzoYGBNSDAd2AdiRRBEOf3w3W3orJq+5aPvbWHM321abrutEifnq+nEbtukLcuQdx+uedgiKlkClZK0tuPgRo6GO1W2Vz+Opuu1p/cHluSOWvF4kWLUhLjcWQGzSFskQJ/RU+/qhoQ4HtV1T2hCyO80uerqWvYvOkj68W9ed6qVF13aqQKHl5AV7aeRjwNZGQLRrORYJu0ziZT54DLGt8Zx73TqH+a/J9f1e1SNTl0deqUxojinNkrly9ZnJgQr1iLUzoFC/47obvnxBNegO/Ea7OrLzF1IVM1NLdv/OjjzjNb89XVyer2dMCulpBIYm+V/5OdyQhO9om3QwLiwTFjycoR2JRB+LZapcGNbqe/ocdQ609siSydtmT9kkXz46IjFcaQgH2Z3hySdFe/NUSJk0QDAnwnSUOOUTWAXICwxtb2D97/qOHk9hJddbq6JSVSY9QFdksE7ZtQgq8SyAig9UEtJTMFB1n6D2ekbB1tcDvWpO3IQdApUWYcSa/qcvqbXaZKT3JLwpyFa26aN6OM7MsIHJAs/NLGqBOJbMNrQICv6BnhNUAZpL+tw/ru+x82HN9cpqtNVnWkRHgscN8ihJLSSqX3Av0sOfPKeXIfsYD/WAjLHFD9AXsxx+++nqCGZsnaTD8E0BQgTsk7luO6nKpml+WCL6krac6Ca9bPnVlm5qcWCUPwgI0hEoymBgT4jqY2J0debOLeZbVv+HBT+e73F0fUZ+s74o1eM4FdhoUcdhnCSaAl7aQIv5wVtFcirKI4TvejRE6E+0wh429QCmoFZsYE9tHrU3c6Ve0ewwl7cmv87PU33TpnRinOTVbAtdIWPDlaVdRi3GlAgO+4a5JPUyCKuy6P9+PtB/Z89Hqp5kKRqTPFTNku29IAast8a0MvZvSVNlME0c6AEbWX95mM3Bwd2b61fq7+7L/02XD4yxfjpD0fLFia2ou9IQ51k8tS3hPvzlxyw+13F+fn6LSyO8RAonya7STKngwaCA++sn+80gwnde3BbdqU3pKQRZeAhW0g7fW9WtPvyyn7H1ED4yBfIMXsWcpcejbkq76kmvCH3NCKOd2eHfsOb9v0YZ737BxTU7zOZTEgGA4C6lLAVQeOWw1EPydGYRKoTOoqkpFW6iaBJpB0p3A8U2Kp/HVvXA/T4rTAXs0bsG7I7ciRl5kk2P8M6elnlder6nKrmz3mHW2JhpK19911e25GGmwqwQ2qLEs4RQz06orvB6eB8ODb2NJ2ubrW7XH7vT4f951kAVj5RR2KFG8O7axqnAXDVkvYxZ4kV2DZg/7JKZSUnhkLA3nLn6iZjgZzRVLkLeVOZMICCs1YQwolD5N05D6K5UWQGN2KV58mZ2lZevaL32DVkeGavaD4rfialsRqyitKDr8xmkzT8nIjLObBKXzcpWJY5PX59xw88t6bL2c4zi9OsCcZnBFan5rYSOkxE3wZjTcB0RrrDCFgJ/eKfk77kXQqPapUe2/slPpbL7X1SYGDAVn2gaDNKTmhMRgm+Et7CDyXYQt2qK70ROzuSshYdPO9d92aFB9HuyXKEbbgcddpJ4dAYcAXb+PTz79afXp3lF6l1XKXdYpoDDklSKVvWuAVUq61AAEpDsrfki7MKBF917hXKIEw8j774Q+kMCbylLQo5MMxkiIfTpxhQki/JY9+CrxITM49oNjAxaEH1PAs2D90NyqtB6EwJC19xRi+M1QJjBo0PcN3Kid/l8nBN8RdX+Py+DB1XXvzHddds2widgg2Sp44c+GN1/4e3XBgWbw11eK16FFlpjYJRNmooyUOvezYCaIm+kO1KEe5UQyi/NGAIUHSHm07BmrS2KeEyFAHNcXwzQ0b/VBP1rCheMn7Ie+PSgimnUVaplO7/VqHR3XZrt/cmp69+IbP3Xt7XEw06x1y71e0sqDAE7HLjyOZw4Pvf/3huQJj7aJci0mvpZNE+soFuA59WTiYytRAms7RlyqQVuq37N8gFsGyZo6i/D0nz1HApD2bspKA8YBBdQgTkd9pEmmbMRkmmQT19C8+DASGA1kWJZpzGXsTMFquhk6uOUVm2XfavVuONaVOX33r+tXjqFUHFIXRPr/qdEXVG6++5q3cdk1iV1akhwy3wF2+E1cyD7BqR0To4jL9bVV+r0eFFAajKjLV337F73KRvDiQSojLmo+3LG8LCKWJjNdaYqBen9fjs3WoemwcvnlLk2w4NvMBk3PVoMYkbSHx56Caktu84/EuJe+tk8ZfOjZTyWjHUhimKD8gF8KkOT3qcx26DfXxM66976H77oiJlKc1vXuL1FkG1LlIIDQQrIHw4PuL3z8zO6ZxcX600aBlK8x8nVmJv0EIJ8/YQ4Ar0DVlRJRAMSAIo6PskpLJJcl4ybMKMXjIM1+OsOzdVfwv5xwg4koVSEnle5LEQcMEs1bINgouKsDX5t54pCGueNVt69dMjK5FtYBfpy9cfvX1tztPbVoT31ocr4o0anRaSu4lR10+ZnEE1uhnro9Z9mjHhm+rOtr8ar02Y07kks91b/4Pd30FDV9G5xpsDJWtQJw788kNvotY+IB5xo1qLZyEtX6X3Xb4Bde5XX5nDzVpsakSbB1czxJAyi3MJyicBfAWoTspyCogEZ1ZvNikhpMCAtT0PrIxRWiTi73tdd6uem4ao20mM3zFlEvl8SJSmupws/bj9uzVdz9y941rTAay7Ehr14tb87YfRSBWovzE6FlCyqFqILCEonwSpl4N68K0D8sePoSZcFDifZuxG/ruyeAp4Sd9LWREDeA2m+cxXss5qfQv/ybwlaI78wIYZVM+zApWdnxGxJR4KkN40E3yGLP6cRIkEaYg5GWTbFZziUHREhnQE/tDSPqhtsLVSc9sDP4Ll6t/9otf/+Ffn5xR9/KXCprnpfiijX4dGWQDyCvpU9Y5NcoYo70kEQ6k0Ph1RrUx0qfVE2uPyuPReD0alYcct8a4qhdmZGq/8TKmySBSrTf5HB1tm3/d9sFPvT2dllm3aaNT1D6PxudBiV6Px+eB8dmjUrsl44Pfp9V6PX6PD2cS+X1YHVNrvPgX/+l0PqMZN6W+4Cc2MsiD+NT4IQsO9H8AvV7HPuvSZ0QufdiQVkytXn5iw+J2LzqgcxHJZ7SoQeOL1PmWpbp/WHDJu/Fn33rySxs273C6XCzXPhpsaN2ANUfgBSF2M1qfwDW0DK9ONxKljJYGtE899VTvvHYdOJRucaTHmbXc84YxX+lHYjjccsef5/2Xvrc8JSEJnDQyIJexWOpVfEFDgnKZWSi4SwD9qa2YZhLyE0Bf0nXluS9lcTIHYtNg6QpIG5xbEGrLVgb5DeGjiVRlp9t/qcluTsqDl9JoNclY5MNe8obm1mf+/srGF/93sefQ7bnO3BiVmZj1yfoh+Y8pTqZ/8gSCGlH1qQXG3MW28g3qHjtQVRuVbMxZ3FOxG0gcterLMWu/E7XoAX1itqe1Qm+JjVz8uei13zHPvJUYGJpBjUle0L8he642Otl+YY/z0hFj+nRDfIa7Yp95+vrIa78ZtexRS+laT+1Jy8wbYq/9R7+12t/ZqMssS/zMr9Xu9qh5d8csusdYcl3MNV82F67QRibG3vAvEfPu1cUkuaqPwZRhmX93zLrvW+bdrY1K8LZcMuYuilr7JcvM6yMWP2xZ8Fm1VquNz7IseFCfVmbImAPTgrejxu9xM9ANXCG4BxTWqHR6dU6MekFk89E9W/7y3gG/KWZaTgYC9DDTt+KJIdPenTv3/OnPzyclJSUkxEGGP/zpuY82bl20YK5erx+LPiDyHG8aCA++ew8fTbf0pMaadDotMcEGQSQlwsF36CtLOTJ/eznIMq7I6DJdeZEJsgzY9NxwNk8kC1oMJaQppTR3JKnlvs07vAIGpa+YBY+VIVmH6Zw4sIgTwGJFFYKyl3BWHmmYqFJxLG96Bz8A38tNdktiXmFe9nhrWlkeaKCty/r6ho2v/eW/Czq335lrz4/xGeDMgIuACF9O5MgbGAcVdQZnTS00F6+15C8zT7/JMutmY8EqJHRd3uuzd8L+a7+w09fZYC5YpvK7NYZY88zr3Wc3OY6842mv8VnbadOShjBkzdUn5Xud7aacWZaiNT5rvaNit99ocVQfc5Z/ZMpfoo6Js5/ZETnndrXJZD27M3rFI7r4TPueF4xl1+tSZ3Wf2eKuPm6ecbMmKqn72OtqvVEfn+9sOKtLn2OZdbvz5Hu++rOmwiV+8Gi/1jTjFk9Xk/P8Zq0lTpuU5647qXJb9XGZrvObnOe2eq0dYMesI3NDS2BAl5uXfAft6DQ+k15dlEgg+Mjurc98cMgQk5Kbla6IFDwcihoRGfHs83+vrq1bMG9WU1Pz9//pJzfdcP2sGSUU2UMyDBDkcdvNhGBD1UB4s4NWi4OwMCtjE2r5dewNUgEMlQqW2SUFXuolptYQBCfZwKmBgShDZW488/W43G12uPZ73W5ni9Xh9rqD/NoC/IJOjSV0lEqUUZnZDnxkYYxWi9seiVcCsxywn14WCQVVD6msQpsBgJdWdZj4mIVrNJjwSrUaagOMaXrgXXuX9ZUNm3/0g+90b/vFV3MvXZelitLTFTWJ77EWkhAojAGFLKchPXEk8birdnoqtrgrd3paL6J7+LVGn8fu99gjSlaZilbDEKE1IGANbMKRutzF6qQ8j62DLHFxpZN/tJGpcSuejFn6Rb+jxX7oBV9XjafuqM5iMcy4Xh2VrI1M8nY1ehpOGbOXa6LTDDnL3dUHPZ0ASr/f1mDd+2LP+T0+e7vj8oHug285qo7CdqyJSNYll2r0EdrEfE1yvkpn1MVna8yR/p5Wx9mt1oNvuxvPE2OFtcvT0ehzO9ytVd6uZmoYQbUo3w/u4dLAylFZ7jBw/Ik2qu4p9n8jvXzfn77zxD98f/fRU3DFpC1Iuf0Qr8SEhPXrVn+yc8+5C5eeffGljMysddeuRGN8+PHmH/3r//vL8y9bbXaYIS5V1fz26b/+7um/lp8+N8QSRPJxrYHw4As0kZeYpF4l+WyFqw5DJvpbMbEnhMv2wf6KP7xz6Ol3Dv/l/RMHzzV5Ar1UZsOaF7ec+/qvt56r6fjwwOWHf7bt3JVOYrVjpmaZA7Dy6ZoMLYa9FLw4yWbra27vfnNXxfbyBor4mqrmzpe2ndt7uoEYBwkG4FkK+tQjY1ATxWBazWvPvAVoPnh9udfvsN7AsegdxMTp83V2db/z4aYfffeb1W//5OuZp+7O98UQC61XTV2k5dUrGTM4AQzAsjzFoAAFtPI4wS7te/9u3/d395mPiGJ0RkPu4ug13/ao9F0V+1TObqjFfeWQ8+DzmOlHrvxi5JLPaMwRfOBDep/H03au+8N/7PjL7V1vfMdVdVKdlBN9238Yiq931p/x2ZrJtEWjdp7bptKZ4pZ+VmOKsZ/cqFZ5VV64nHvVarB1bEwD4rmoSLAOo5Hp9jvIp9HCJmu/dLDn8iGPy+Hzwj5LbNR+rxvGD2KaJhWnDjG0X8moy8lvkBEtQIPlYQniA3+xFpJs8X9phu9R864Nv3jyx//6b+XnKtywVjPH8yCD2MBte+ftN0dFR//xmRfeeOu9B+67E55tv/rtH3/6X79LSE76/Z+e+8l//E9bW8dnH3nig03ba+qb9u0/PHCOIsXE0UB48CWWANBF1kHZRafb/dRLwiipT1OMq2u1v7ar8tktF97ed/n1nZXHK1rdXuCf1uPXwK2dAiHhpfTVxhuFaSBDB0wbiUsQjqf14G+Gmn6V20c/0/VsfIUNAIToEg95CsOU1za0217dcW7HsWr6hmmrW5zvH6g5dakdXxEvYB/NkwOxPLUbLGcJ9k1iAw7dShK4BoXnY9c9oARMILqttu079/zbP3//zMv/+qXUsw+WqBIMbBlK4VrFZwac33FPBW5Qkhtd4YXiw9IZWsXpVaOpPF63CyAOWNQYIn1Oq7uhXA1A1OlVPrdPq3M2nu/Z/xdf8zlgqIr4NrCBEwK4VV6Xt8fm6bH53MBEtzYmQ6M3u0+/q+npVusB0z6Mma6qI/6eDtP023ydl1zV5X70AlgSfF6NBj/oG16N360lPpAeIrbH6mmq8Dp6bFVnOo5t6rl0wt1S7feQlTGKqhRz4R4HmR3duK+NSVVHxjJP5qBZEEdkOiPo3UJEE/zwOEKYNf7cRN3XZ3tudnzw958+8e//+atTZ887nU6sC0qcYFA9ISU5+f777jh05Eh6SuqqFUu6rdbX3nr/+nXXrFm+7M7bb9qy6ZPG1rauzs4ZJYVffOSBB++/e+x6jsj56mugL/CVeyB7/ZQYrCAFfcnLX3I6zdTp7lhR/O6/3fPRzz/zpZtnWfQ6h9Nd1dhx8krLlRZrj8dLfTv9bixgE06rBTiC3Gj9fqfTc7G+7cjFxorGzh63R6f2HTxfd7amHVDtdXvPVLd12hx4sr3LXtViVxgx8LbpvX5u4ICseAXhuuF0uS/Vd9Q2dVU3tB+72FTfZgWS04oNFnkVvIbBLkFeRr7ZprpP9yKw6/F0dHXv3nvw5z/5591/+v5nog4/PN2fagH6kJpKhntK14NYX7ABP3w1/D6Xw9txReVyEggCxDi7PV21/q56T+MZv7MzZu4d0XnTsdrmtTXrUooib3rKvPYfCRW9cgBeDQzmSDu7un09jX6vjU5fQEtV7tpyT+sly/InLQvv8vU0+G1wAvP6ejpdF3dg4mMrf98PDgv3hs56b3cjVn816By2JpWrW6MFAvd4bU3+nhbXpR3u6j3xi29Pv/P7kdOv0RoName7l/gg94BJ+xxWj7XZ73W4Gs866s8aS24ylFynMkXxtYg+mi3I1sbTsNkCYb+g51q/V6/2FSVpvz7dtrr1tVd++rVf/vevy89e6HE4Bn8iOFrt2lUrIiMjr7tubXRUVEdXl93es+2TnT//5f+cOHm6oDA/NSXln3/wjf3799/92YdfeOnVwU3WPt2eKEofrAbC+/n+7zMvzIppmZ0dadQTayadZPP/emXcC3e4HxnZ83C8svlX755Mj7V8+fpivd4QF2nstLv+/EH5vvIasAe3X3Xn2tL7VhW9vq38w/2Xnvr8EuDj/7179tePz89Kif23F4/sPlmHQ3Bbbc51y4p+/PDSR3/2RrdT+/bP79p3uOoL//XhQ+tnfuPuRb986aDDr/vPL87DKwreVH6p5f975URZVuJPHlqM1aTdp+p+897J1TNTF+TF/PqN040dTrhV1bZac9LjvvXZeQuLUgIOGP30a3n9T0JqGbC77O6t5a0JxWtuXLu8t8qpyXuwLTH8dBLbPX++4sN33/Be3HpDlisvjkaqZaWz4VP6j/8d2I6iKFkpLVv6ZFMKip5++Az4MPfXELaPeQRGNUw6gIIGA9a+gHEET8kSlUarMxDO6XGBbrKlT5oVciBbFNFMJMI5zRn5aLQmtSXGZ+8ATqp1kT6XS2vQRy3/gqH0+tZnP+framZjOAE9nw/WaTxARjvAKoxjKi1h0GyBQm/EL1h1Qf5VxGxGg1KgEI2GzE7oI8TarTPBEIF+T/fy9D32Sv0hqH9Txw9JX8y7krpxwD/O4ytv8m7tSEpfctuNN9yQkZZmhJM8P7Woz7aFAmrqG+596Et33HbTVx/7nM1uu/2+LyxaOOfH3/8WnrU7HCmJCVdqiVfyb37/p9aW9hee/b10EtLw+4t4cpxooA8/X2odG4KIsvWVr60wWkiycHp97x+69Pmfv//4Lz54d8/FjYcuHTtf+5XbZ7/yk5tvXpaz+UDl2SttKIyQBcoj8QGv5saDl7ccq/32Z+e9/h+3/vDBuW9+cu7clbbbV04HOle3ubYer0pNij5d1dZkdVfUtC2flUw3uDIbLIEJsFq6z5i+c7BV4OXV4gVx56ZF/NuXVv5/X7rG6lEdvdhqxWZSCZz6q2wvXA5Uly/kheoKlbDZ7d3d3ZiiD0GNQ08Kttve2XXs+Imnf/PLD377ndWuzU/M9ufHk43AIS0YNHnhsCGVJ1PhIAFIIloxvntYg7oQms+sNpiAEChD/AeVy+G3dxE482E6TgJCeF1On9MBEw/1peBNQ7ICdns9aAk2aUABcHGDKcDX3QIfXtiPvPZOY0pu9LXfMhSvc57b6O9sYbu7NcTUQMwIRBqvF+iLqQ0cxlQeF9mRxxYDIIbTTsQA8tLBgu69ICYtYiFh9jAUDTqMB6VZS9/dnCssSDdBY6lEjqlVDFtB56Vpnixqyznz3HM//94rr7x06XKVzWaXVuT6bFq4NsTERBl0OugqOSnpkc/dd/DQkYe//K1HvvytV976qKml7aHHn3zsq985dLR85Ypl1KlcXJNEA+HbkkIh7VsKKsRcIsPUW0YemSwoXnyTXrNietoPH1j6g88sXlCU2tRuAyFIjbdEm7Rl2XFYXum0waIn8SAVDLKwPWgqGrpj4qOWzky16HRzpiUiWU1D54oZmXi1Dp2qPXa65gvXz2hq7Th6tt7W455fmEBDQBBWggsH6GIBBLtgkdgDHwof/PEJSTLo1SXZsfmp0QWpUWnxFrvT63QDlwd3BVEe/gibTTOUl3MBCDiczqrq2r+99PZzL71ps9kk5ji4ggadCrbd9o7O8lOnn336t+//5vsrbZu/Mt1dHEewju02Y61FQYe1WzgTiwQg4eFXAc4MiDldJRUG8yU/wDOVhv6mITrYKCjvvCH+LQp/AgXXpMsK7AJ2EqFJDkBZjcmsNkY5Lm6z7vwLiSYBOJeE4xt5eMek4jBkp49TeZgAbLxgu97Yn6QIaR8Q8XyTYn6wNgyndKY7xcVVJY1bge/oF2TQ0agwB1iSrf1ibl3M4T/+7Rc/fOONNyorL3f3DcFomJSkpD/8+j8/d//dFosZ+PuVxx5+9fm//OTH3/vPnz31jS9+Hgz6+af/75c///9e+PP/femxz4V7/QbdY0TCcaaBPmy+wR1P+daGd0AM34Uxy1SbdJrCjPgblxauXZCflx4bZdTZHa661u6Wbge2J8CfPCbSoNPjHSWvKTHkqXRYsclIjgajqmzoburqOVrZBXiOijBnJEROz0l6e8c5l0+1cl52YrRp+6GKtISItHgTfd/JS4BoFEmRxtpm+4W6tsa2zov17VimS4wxa3WYy+qsdmdTp7W6pRsm4BiL3qAfEY9gbwKl2dQBA3Zql6uhsXnzJ3v/5d//93+f/lt1bUPIjqVRaX2v19vW0Xn6zNm/P/fsq//9g5lN7zxWasuLJcuQbGkeE22FwSEwLlAUklE0IEsongSvyykGYDabkRBABmwG9JK7muw1EXAf6PUELZuBKBvT2UVdHaoOdbz1bevG/1I5bNzTgA8joXXiz/MxhkggZUYzZ+ON9FGGTg7lkgR8TOlrEOaVkUFP+bSkQNL1CEEnv4mTucdk8K3IUT+Wfdly6Pcv/vpf333n7YpLl4nfGPdLC+oFOq02NysDQdSYey/+z85MXzJ/7vTiQpPJgF1ORQV5C+fOzM/LxgRgVPqPyGScaCD8Jot9R46lmR0psUbs9+eCBg30Qe8zg6DALekjnmjvdpyrbkvG/qOCFCQAJoCQnr7cevZKR0Vt1+FzLQtL01bNzqhu7KxqtK6YmeH0eI9Xdq6blzFvWvzhcw1bTzafudL29q4LuSmWL94616BRNXU5Pz5Wvago+eYV06obOo6db752cf78kiSYFgiV8uNIR7XP7frkRMOBCy2HzjfuPd9cmh1/68IcuBAfutB0+kpHfUv3vjONgMsbF2XnpcTQt59y5sE0SGDkIZXEs063r7KxRx+bOS03s6Wl7cjx08+++PoLr75TXVOH6TlemCUL5hgMBhBzLChSLwGElMGHfi+SEltteXryCP3x4Bd2ZnV2Xq6s3PjBO5v+/n+lPQfvzHOlRpKqS/SQE94gnivZXBW+C0pgktivrAGZacoIRbTDqhx8ScAXQDoJ8JTEkX1mErIP0mdmh6Z2U8JWeTuwfR+MTjLezv4lOxzZCgTnmvRZXjvFCMLxPEhUeaRgtimpzooKKWmF3J3Z97wyvd+FAP4qakWrAjc8DbbGqUpMbVdOH9lx+HS302swWQwGvFNwog+WjefPSmXVDeg6MDYNqo8Oph+LNONCA+EX3H795+fmxLXPyokiUc3CrLbJM2nZdYn3VnlxhtrU/M0dtuMVTUmxEXMLk1mPhC329MWGXSeqO6yu0vzUlXOykmJNRy80nq1qXz0no7vHvf9sy/ULs1NijA2tnW/uOF9V3wWGe9ea6TnJMUBuODl8crx22fT0mfkx5y63HjzfvnZRfka8kTF18u76/fYe59GKxh1nW20uf1F69JpZGdlJEeeutPzxvXKDUZ+daLHaXKvmZc8uSDHqyboQa4dBdWyeWIYhNRbcNh5rMWUunFla8PLrG7bt3me12knVCXp65s+def+9t+OscqxUEYpMoxMQTKU+oQFzBH/pOE+jsMP/YzN9Kht53OlyHDqwr/7IRwvjOlZkG0xEnZyJUtEkxJNRQn7LQ2rJMUX5llPl8UGU/0ubnuiVCcA7LOsQ0p8c/hRwooD43kql7JA9ywwEUmgNpRscz4zWSOpY8gOclqt1Bnj4ws5L5WNYSqrA/mGX4lnpD6C6MQIMwO+BqwwrXqFjqmmpNcJ1C/JdOJL8/7f3HuCRJdd1cOeckHMGJsedmZ08s2k2aEkuKZKSZUmWqOwkybLlIPu3bDl/DvotB0VTtvxLFGmLkpiWefPOxskZEzDIOXXO/6nwXr8OABqzaKAbuG8x2EZ3vapbp16fd96tW7cyfic5HMKPJtw0aGMhmnpn0nLftGP78Re279ptt9kUmSvmPXMntAUBC5h43eptib8t3UjiSpEjrzxBiNuR8q5AhP8pbmhuj8tht0l+LwsK2rpGLBHt8D/+aH/V7L52Rr6a8ddQrebrmfe15NcKnwJhM9TC7yavWObYw2vMQ+tZxWy2Rn5j2OQI4kZxVSDMTCbxhQdQhElhMgayh39ZUCE8iyK5Cea7kTOFz6zwS4xfoaI+PHkriWd5RPDtIUa+2zrqfvK57Q6ECDH3JFuFoe7OUBT5iutEU9TPydfc+FhtjffPv/rtu/cfwg8bj2MeD9PfybaWxscPH/B6vZx8WQdxsPQx/GBfTv5V4l8uEaasBOorBCawE1mNwdwzszOR4Rs/3hOosSxU2dJsTzXmnJffL/Gt06hB5bLOGKzVbvJLqZK7lq0MFquxup2vFMREF9I/Tun8sxqGUclXgixkKcdGq9qkMapPXA9Pj69Zb7Gz/iI5TnghFZwFUrL/GUJXKhERCRwkOW8nKNNsNXU8brB74je/hftcPk2qJCmtUmne7rHufg5ZzRJDF412n95Zg7UYKf9kOjDHwVevonzopB3KB0KFS9sYH6qXn7i3sGHleaHZ5aeLJNOhuPFOwP1euENX3WWyMfozGCCBeaClSBXEYkjYCYwowZQsHI+9wwLg+eUuMlrzX/ic+ygQEiH/ZO/hL/xj//FJSm6gQrucfMPhyNFD+6AJHA5H4bvI1mXCDeh5YfL9L5//3/t8MyBfhJpJflDuzdJGeTuWzCGuQXnJqf8X2XX59azMrigXt3jA1AhJcfVKGaWwqKRw7a2/wCXDVU9G+kghJN5Tv7oPRuf+7LX+zpaajx/vsmJKjjXNF0+rKmGV4PMLWwfl+50r077u0x9//ompqdnvvfbW9197+97AECg4Fo+/+NyTv/Yrf8Pn9eQ8ZqpNFRJRhe0QX3TUeeni1Ve/9ReWqQu7bLMt9qjPylLAK7zH+6WstxNcmH1oyVd8MxmnZea+BJuk9daWHZ6P/UusX0hFozqLMzL4TviV/45gaUm67HbHh1XUp2pH9TGC3w2lQlOmt/A3ciy4Tv0CctzoIn6sjktMXo++/6fJmRHcksA/QiuKTBPceBaQxq4BpRXhl2D/nNX2oz9psLlCr/x7HcIqRAlRWNyi2V+ZhXxiRo+d6G7yPPursYnrkRvfc+7/hKlpl87iio9eCJ//X6nFGXVGTrkh5QOo9Je3l9H4mhlXKda5KeDSYEw/g53ikt4hc5e778SJ0090tDap+aqWueg0T5ecn/nNmfG0fCG2bZGHksNN+wYKsFxw4G6oAcxGYA3I+XcvOOzWF559EmEV2p6s8tqn4muDQGGf77sXrjTZw3j2x36C6vdXcb7xhtVnHWGGZBGVTORzoOb7z3lVnCq+Tgr9aQmIKzdlVkHwqThDajoeJSrrFtwtmVd55hJUqv1ISie7xdzbWr2ttcppQ8Ro1rm8N7kstRK68osXTaTujfvtNd07+zpdDseuHb1IkuJ1uyKRaCgc7uxoO3PiiDWzM3kBLlT6IG8fS/0p7IGCbm5uOnT0RNTd+fpAdC4QQayVSZe0mfh6RHZDUZ44OWyaI4OmdlCEUtYU5AJLp0fedNueF6N3vxO5+k1TdbOt56nw9a+lQiGdxWbwNhqctTqotniENYnoWld92u5L603peAxJHSFIdWaz3uYyuGpYW1jdy+9U0NHIRmbtOh6ffhC587rR4rZ0PJ6evpWcH0ewsA6FHdVsxi0RZ9ccHKOuGvwg7U4qGmZmuWsM7ga9za1PxrBiLbk4Ep9+mA7MIMkOm2JEijKLFeURKswCXRxeg7setw2mi7EuGbU5qnSuBoOjytJ5JO2fTEwNJAMzkQfvgcocO56KPXwv6Z8VzyLigsxgkn9pKJdlgYtGkRtAJhLXjwZNt8LVV9O9yW3PPfWpnzh96mRNFR6DZCYjfpdZ+WDhelzVYvRxmPhhNpssiJzHb4sZ+y7brBabzWrHj90GrwI2tcKPy+lwu5wet6vK56mtqWqoq52angEFd3W2Y1lHTi9XuuDp87VHYKkJt4uNtjCfcMuQb8HGs7+3ShGZCljVtsqzsNRlUthkkauQryKxocLN4nugqFPBteLJWqgj5cKVZCq+MoLXFQqWEk2HOWWX3Wy3QshLvlYKK8ULdS+jgPI+FdoMwWr94wFXXff2nk523zAYcLnv2bV9724sKjE1NtTu37MTX5HVUvsy48zozmTq6mg/dOTYgrXt8oTOj9WB8YhZn7RA0fPh0v4r8B3L4pUc8hUt602+ZuRvjA9fjo3fM1V3pI3m8JWXIaWsO87a9zxv6TpiqmlPIStjOm3uOWbb9Zylbb+xqgULJQxWp23vs6bGPnPzLqTa0VntqcVJHUiZJzYzuGstnY/HpgeiDy8aHW7UHB/6MLUwaeo4aNnxtLn9MS6K5/SJkKlzv23X8+aO/abGHeGHVw3eZqQ6s/SeMrcd0KfCyJRm7ngMCSpTwQXrgU/BSZKcHTA19Jn3vYTVkfDo2Pecs207y4QtkjQtTpnqumy7n7f1nbI09JrrehLT97GyDvcAyEiYbbS7ov1vpANY5ZEVyiFHocAdU165ecPKz9frwgn9ZMT0IFZ73bRbv+O5c5/6sSfOnKqtrhKsu4ScfqTv9hLULb4ByvdAFkIDd+8NIPwcWw4q5Jt1l3kkC+ikR0dgCfL94EKTPQryNSv5fEULmWdANmrs2lN0q3A6KM4uPG1FY1jCi2vRbjUzMuBPdJF4YmjSH44lnTbMlrCLIzuYmPOmXh9NpIMxFqGLJ2q2UimLUSXlChLmNshIUh5nJC85qVs0olrMHGXpGo35Mi5V9lERNtzTyI0XLkPlUF7h/5FY8u5YwN3Qs03J5wtzQcHVVb4De3bu6O1mwZslCIxHK9A7fb3d+w4fXbS135pJBTAZFw0b9UkEVjPIhMkcHvlCe5GoXeRUm637GY7IkwvyNdqc5tZ9lpaDoXuvxe+9a27Y7n7+HyRBpmG/vfeULh1NRqKuJ/8m063RgK3zkMHmxDIH5+N/xehrTgUmTVVtIMTU7MPUwgTLhgB3vrPa2nEE8hPK2tpxKLkwErn5qt7hcZ75G3A6pMJzjp0vmOwWXXDC8fSv6S3OxOg1xLFEx+65T/2MtetEZOyO0ddibtkbH7po7jppbtgVvfeupeeEqbYzNnbV1HrQ3HEsNnXf0n7I1nMyPjuExBEmXyMc1tadz1vbD6XmR4w2j7G6E+6OxPhNLAVxHPqMtW1P+NrX48PXWP4HcVHljrPwKWRBJq4UUVpMP/BrSx9JpMfC5gepxoe2vbrtL5z52I+cPnGMq12x8GODj/sDg4FAsKe7wy2V7wbbs8WbXyJyULCoSq2ZyzFfBkAuYKKMO7jwRcGCU+6/Gx6f/fL3bly4PYUrdCEYnVoIxpLJqbngH3/z2svvPAzH8U3MNC0j83FyInFjcPZr7w188bW7X3jt3ju3JuGzUlzG0nEs7+hSsLJoefi25oII4A0bdEk5ec6N56FKfMqDT10InxlnUjavwfO8sI9Y0iwxgycm70R31C+V4s7LMLkAhv+IuvK9FjASD4Ber4dPtZXkEOLf43Y+/cSpH/q5v+s88QvXXWcvh1tuzZkwty69Mxklp+GPXHPU6VB1zDGSyF+jS/qnYiM3Y5N3HN2nLc3bLe37DXDUzg4hh286HjLV9phqOuFJQNaFdHhBFwsZPXUGhxNgIlY38OYfxh9+oDOYdRYHh4rdKvkQ6Cy+JnvbXqO7Njb0YXxmxNy8z2j3poIzqUgoHQ0YazrNbfsMrsbgxS8E3/tK8N0v4kJx9JzShacTC7NJ/4zeVoOJMp4nKImkDbGHFw2OanPbIUNVV2J2OBVatDbvSMcCifnxZHAOWS5NTbuNvtb48KXIu38c/fBLTLCzxXhJIx7Wm3bE774Sv/26DsEPWi3BuVVeEPKrIP8S3lcRySBcsOJKiMZ0w4u668G6644Tod0/fupHfuVTn/50Vztz767eqVWSCwZGwl/Bv3dlcB8oTRcrq9alwrbFxjniulvyYDzIKmAUxFiIT+fzOFbk6jZWuaF6jeFw/M3LD792/v5sMI6o2KGpwOhcKM4yA/CMZprLAKe+e3vsN//88pdevXv5zuTFO9NvXx/HxjJ8yp2TCSSkgUthHCzJihFeRHgJ/eHEq5dGvn1hhC93lY4GdY6CT6wrZCz7wwIPRLI0zrF4IbIViO+b3FEMpiHKgm2ILCk7Bwf+FeQTIBv77cIzRLXP++yzT/3gT/+K48TP3/ScvRhuvTVvXmR3OKF+ceRSSz4DqzEJbDjZvj7p2N03Fl773fCd75o8zcb6Tp2RRXchXAGpzML3340OX9NjMyGDGTSattjjU3fjgxdY+jHcu7A/JotVZqke+MSmOOSNMPbwfPjCnybnxyydxwyeOqxnw1CanTWQpfHx64nBD4XXipmBU7E8xmxlgWVYJeOtSUX9kbuvJ4OLMvohEY5P3ErHg7beM9hcIzZ+PR0L4g4Bh7IZqYH9M+GBiwn/HHNnsaoMyA3Bho3pgxR8x5GBd6KDV7ClhXw4KEhK2m+A8qWQN1/up8Bum4PzxksLNdetR/y7f+T4Z//WD37q411tjXwz7PI6uADnX206ygCBJRdZNNoijVWIC+AT6JrREj4AHJhFHRhfuDMy31hli0Ti790YmVqIVrltyBx2fWC62u3AJIDPbRudnv/8165cvjtVX+2Aw/XinUms6bWYjHeHoc9SboeFx1Ow79rkbOA/fPlaKJb8qR/Y/aNPb3v6sZaeBqfHYXrt2ijmFjx22zxI9spYC9KppvWXHkxfezA7OhPEdMPbV0f/7PX+BxOBllpXtdu84I++f2fy8r2poSk/Hvk9Dht8HVcfTI9O+28+nB2bDQcj8RsPZpCCB18Pjx2r61L3RuYv3Jm8N7yAeQ2P0zw0vnDh7vRCAEHKCx2NThbYw+hL++AoHuaZ2+HOWMDX1LexO1kIJ7fLaYcjom3bvhlj00jYMh+Oh0NBiwG+YLkXiXC85DtQcpwQ6JvB6bbv/pg+GTJ4Gqw9J3GrC1/+i3R4EW7W6MAHkdFbqchcbPACSNrctjsB2h2+nApMID8Z7oXWrqOJ2fux4UuWxl1wtiZGr0Isi/z2BleVpeMw0qVHbr0CEgD5IsMZvAFm7DQxeTs2fgObTSRHr0K9mjqPwzuhS0VNjTuTcw8tjTtwL8CuRYnF0dTieGJ60Nq5HwVCN7+LvJRmX72l6yQEeOjGy7rYoqkKxGeKDlxILIzFZh4m5kYtjdvMdZ2YJDQ27cROQrHRK7GxWyyywtcCrQ1XNVMP+X6BLNrNKBEWOMEfqyIp/XDQeDdSM+Lal+h75sC5z5w+fby+xlu2S9Gw9mdhYbG7s93tFhNudGwkAkuQ74eXGu2RRj7hlmed/KpC2bxzc/z3v3bt+M6G6bnAb/zRW4OT4QO9Da9cGPjOhaH6GveXX7sZjiaxe+Frl4fC0VhDlc3rtCA/zvDEfCyaOH994tbIYleLt85j4y6C1Hs3xr7+/thfOdv77KEWr80EVgSVB0LJX/zd1zrqfdtb60Bzf/d33njpZNfYlP8/fvlyIBhf8Mfqqt3vXBu98XA6lkzVuJ21Xus33xv8+ruD4OVL/RNjs6Gu5uoP+yc//40reOf24PwbV0b7R+YHJxe/98HQzEJke2vV1Gzwj793v38siBQ//SOLuzurXr848LtfvTEzPz80GTm9v4U9OeaSL0NFkG8/yLdxg8lXHSNQsNvp6O3taerdN2tqHA2bsYw7EApaDWncSCX5cv8kP/L+J33EcPqa2NaWRh12hdAlo+HbL8fuv58MzugtNsxZWerbja7qxPRdqFek0jDXdpnqehBgkFwcT4XgFnDEJ/oT0w8NzhpwbnzsRiqAKC7euMmqs3kScw8x5ZVYGEHALzI5RO6fx6pEc22PpbYToQvxidvxKZB42uhuNlW3gP2jD95Lzg+ZvI1oCDNvWB+RnLqHfdsSkcXY0GVdPMrSpVscsaELYHxdNIiEkzDP3NCDOA34H5JT9yFysXec3t2QTkYTwZnY0MXE3IjObLfveBo7caAX0MLZ3Kvh3YzfSUSyMS2CtNSDftPNRMOE76Cu79l9T//g2TMnG+vFapqyE7zq5TE8MjY/P8/J172RrENtcwSW2sPtUpODka/kHQ1YcuaKv4OHuC+9eru5yjG/GH792ghm4Tsaq9+/PYYZBiRheOPqw6Y67+n97cjk4HDaPvvcXo/d9P71UQTH/Mi5nTUu85vXxntaqnpasMaXXbAf3p649GDhY0dbO+qYRhZPdrFo+ne+c/P49sa9XfVjc+HPf/v2Xzu3/c7gzBdevfvJEz3H9rY217irPbaBsZnGWvfnfmDP4Jj/T1+5e7Cv4cfP7cKzJZqo9XkiydTbN0dP7Gs/uafpg9sTsVTqh5/qBVlfvT+7t6fulStj528vHNzV7HIaXz5/79COxofj8+dvTjx1uPXjx3vqa5wydiL7WyW+YVGQ76jf04jMqx3lckVxcxFp1NXdXd+5a87cOBIyj82HoIIdljTLcqhspCc8EgpVKO5hPmmZTkTjkzdBZ1H8PHg7MXQNg5FKxhNj1xMTd2KjN2IDH2CDS/Ay49mJW4nxW7GHHyYn+9MRf3zyTnIG21MmUuHFxNS9JIpxXwQO8CZiDBKzLNMuto5Pzj7AZpfpwCxcB4mJG3BcxAbeSc4MwmURG7+ZnLqTmBmMDryHcAVo2MTYNZBybORqfPAizEsujMbH76AStmowMB0bvpgYvw0iZh6lwFRi/Aasig1eTGIPoVgI4joxcTs2dj1y980o7ATzIgAjEU3MDTED4lFhnhKJINxRfDzlLvQ8bz9/M5bQ3ZvX3QxXT9ceNe76gceefOn0yWONtVVl5Ntd+kIcGR2fm53v6mxD7uByuVy3sB1LpZRc0i2kaCPEnBoaffaeRvcrl4bvDC8e39XqcZivPpiaXow+1tcIschThuG53uKzWRw2W43XZTZhZ29dR6Nve3sdsos5LEaEavFckiyrTpXTCmaAVo0jNlNEyPN/4Aq+gQWfw08yp9WOjpqn9jV+cGv4u+/1z/rDDVVOB1KlmcxehxWrHqBK9nZW7Wj17WyrQTzk5CJbGuByWLqaPDvafNVuO/L77Oyoaq9zwYsciCb7JwIGY3Jicja4GGry2WEOUkwgauvpx7q2dSA5I2uXz92pRxY45elEg80YgqbG+nPPPvfEZ37edewnB+ueetffdHPeEMqk2GV8o810IHrIbnt4rpmfTCxMJefGUv45ufIKgxCPgRBBqSm/2AYNaejwzlB89GZqDvqRZXRn5SMhdp1EFrCrJlKe8xq5bEzE08FZtsICaR4xxoHZ5OxIGhl4sQxgbjw+djs5O8Y3KYFDNgkWhrBNTg/y5RLpRGABu7Elpx5gckyPqV2kDw4vsNs2eBGbDGGzOOSKlNOgqWQ4EJ8dTqJ1tv4Yfvs45uLi4/2pwELaP4OQDLGhVAqaN8Iy8fPbv7g/SAiEINDKYYQL35lOf3+q6rb3dPrQjz/2yZ/7zKc+saunFflPyiGSoSgS4xt7FFWSCpUegaXz+SpjlD1WyrXJh9BmMT2+vfHi3fEHE/PPHOnuaHC9f2sI1/pjPTV6bBiD+RJ9GksakDssFI7M+lluUzACfvA+/BlsoZlclsRm37Z3VLfU2r59YRxy9eF0cHAqeHssiLWWZr1xeDIwtRi5dn+aL1VKV3scn35yR3dLFfL8Xr07iXk3cHcgnER+XiTWwWTPwMQiAt2Gp8OY20XAnFGHCcC0GcawKRy2hgot8x3TkaTb4AbnpxMdLa7HdjW+cLyzp81tNhuxp7qdxc2qX8esocgQMetA4TKlH7uVW2AUbDRgn92Pvfji2c/8vPfET402nHs32HJ7wRBFTIcyI6QJd9DUyach5Zw/n9qX0SOC4GRIrJyBEq5kIR/VV4LGlGcY8VoeCs/JiStB+LxapYQSVcDOYm/iIxaFIm4WaiFBkaJZyYCc5VWztbpeiVmUfm9hmNKpTKVqnbwaViqZ0kPtvjFTda/2Ccuxnzj2g7/w2c9+dk9fh3DkVNAhYhBpwq1MhmxJ5assHc22U16PYu48hZmcg901iVgc+Qr2dVf3NDqHx2Y765zNtTZsseW0mBDtgCQBDbWuqdnAt9++PzUfctlNDubMYLrMadFb+L7G/HupR370z57pRJ1f/P79//JnV3/3K9ffuDqB2JjHe6vfujb6+W9cfjA27cTsui555+HU197oH5pcqKtyNVTZsWtMW53rwfDsn71+1+00HeqteufWxG9/9frb18f2ddUc6qu1GdLVNrMdQcuIADPrHWa2Uggr3VxWA9T2Eweaalym2wNTl/vHY7GE1232OS0+MROo0An/ems0otRFAhwRfFTWB3z33W3Nzz//womXftp7/HMj9U+/MV9/czqNuFSZT1ewH4/Kk7uMKtFhkhg5AaqHSnkKk8nFK9kltJFuCk1neW/UcC4ZUCLpUCFjfmEINs0QroztEm9m8b14UtLaKfMLcyN53SrrK5HQMv8vH0dNOyLsBc9cyQez6e/N1A00nnOc+umjn/7rP/xDn923o9tsKlUEYUkvI+3K85I2RJUXg0Bhn+/bH1xoccYafTbNhFuuPBL847QZq93Wx3c272ivsluMdT7XqX3ITooIAX2Nx7Gjq7apxu12WrxOa53X0d1a1Vrn6murbq5zI3N/jde2vb0aERFSgxmMbfXuzgaX22GCa7Kh2r6ns6at3tlWgwWTpiqn5djuhq7GqkPbahAnNLcQRELeJw52HNnRiKyntR6Lw6qvclj29dRub/NiDTEIdkdb9VOH2joa3HgwbK1197VhQs7qcti2tde01CEOzojf29qre1t8tZjgS+twt+hpqe5ogrHW9jrP9s5qxEXy5DsiplbhF0Xu4P9swm3U727oZSvcyvzgC/B8XndnZ7ezoTdoaxqPWPtH56PhoAehXGzRCx9i0btlJd3SH2YWVqkSmDNiRvJy0tPe05ZHTUZ1S10rVLX6Iz0DMvhQjlIh09l5Sny4MpbCqyBVteamwreXY/vU6Qdmk+/Neudbz7oPfmLv6RePHzvaAN8uT2VT5kO9lHljE1NYYYwJN4+HfL4bP4aFE+v8h9/+g8O1/v2dHr6HG5cYGXGn+iOEG4/vCczlHy/EU0KLby9fUSq+ZyJlFL9q+VO62HiCuRBEuG/mYCWYxzHJXWnYfYu9wXajgFxmm3HJJWfIDIY6+R5Z+GE6hW8cy5tnbTPPIeQt/oRN4gFTrkRij4rcQOZGFuYws5CckT+kiyxu8rl16Qhe+fA7F4h9/f3R5gPPf/zc2Y0fzNVYEE8kBx4O375xeer2+6nRS93W2V6fDg4acWif7eU7nDQzrJPDP3nSX74hblmycPY5SzHYyo8RmsbyHzly3xFXr/qL90ZtWgkolm+J6bW0fmAmcdPv1bcdrNp+pHff4W1dbYXCflYDdxmUxfV+4fL16zduPXn2ZFtLs8aicn9uKwPwSmLCUrsXYzGo+vXRNpxhXnk5q8/iTFlw3mWMKpSKysL4hDl6xbeAkaD8UKZ9zGkAnMslp5Hln+QlwYmok80ViHxVbI0FyzMi14PyMvgbP4ouwh6O7LVyS1A4FjJWcULym4DaMsvOh3+4KYjVb5lnVK3QKjQEnL1LMjYlrRQPzn09Hc89/+LJT/50+7m/Ptb8wjcna67PpLFLSMZNy5eXSLd89mK5XNsKIiBvwqLsMhiJ2yEvINEsVDiL+JXyRSCvDpBsRruEWK4l4nG72H9VZ7y/oP/2mO9u/XN1z/71xz75sy98/KVdvR2bgHnlGMjvZ0mvLKq8WASWWOEm1lYoqSA1a3YlfwoWlSkROKkKOuWUm70OOPOQyKhT+dIoF0PmcVB8/5QvPv9D+8wpHvuVr6mkd+UUUVIeoqLshsS3XzEy87iaZbNoPVNMncPJZgUl8iFzHyqCAYodj3Uuh6nFbb2dT557/tjHP9f53N8cbXruq6PeG1MJhJfw2yh7PmA3O8G8uZpUJc0CACijxztUUFrJK0hzbtbVoa08M87Z+CgCYTnU8myT0WMq2XOZgRVDc6mvj9fer3+h6dm/+dgnfurcix/fu7MH2ZHWeURK2hybb1OWrpa0Iaq8GASWIF8WCZB1usqMmu+BJFO2SFh81bJITXWyZd4Xy4lRUiQ+zJwia1AoVTlVpV+R81zld9GQ4ovNkG4WXYv6c9/KqUS5X0jppTCvosS4mZmu8ZPlPBR/X9wqsmfgi0G9zMrA/97d2fLEU08f/8Tntr34Sw/qn/viA9etKTYZJxxH+SSX904B/tVwtfZT9bXygjejfQrRwsN5O+d0lZfz/COFWF7bnriEMqoCd5ak7vZ08qvD7v6G5zqe/xtHPvYTZ889u6OvA/OtZTZKa2KOAIP8DGsC5ketZKloBy4zc9WjJB6VmiTfMm+D3D1RZtrnmfj5a+Zu4B4HzrciGb9IaCakbTYDawlWS5vcFpGPT3g3WM28HvaDLA+MnVXpyz4QTWh/JHtzH7HwCwt/cYbSuT3Z20CqUluytCACzV2DvcROS5vhwBoZTMWcefLp05/86b2f+tV7DS9+8b771mwizaM+ONtmKDfXKVzI+aKwXj7z5l5YCnwF3i9A6irYMnhBw8U5NC5Lsjok62QC39hZ/dPpLw/67ja80P2xXzr2iZ984okntnW3wiGzXKMVPtQ5sSMV3pvKNr/whNu//90/PNEU2NOGnSzgJGX+MOn4U78lysOLqm4EAXFZoTBw5ppXb7ciKEsJnFADKPLmWHj4LP8KyO9B9gyzUC/qLTzbfcuM0NChUoFog58pb/6cgblTU/tl08aayuYl9Uh/teabrJ8Pxr/+7njj3mc+9szpyr4Qsq3HdNzD4bGRgf4HV87P3nz1WPVCT5WJBdkqjwgCumxNqgKrXiUCV+04FjxFbVury7R3NNlYLsI54665sgpKYnkFsM/0AwupG/4qY8fxlj3HOnp2tDU3WJF2Wb06NtNYKn3Bd+/ytZsXL115+onT7W2tmi5uDvFQeWNWmHx/8/f/aOr+JZdFx2NdGT+xzR/5QiPGX4oM5FuR8SgCOXxcIsnPeTYa+b1jXx7JupmYWKEfBREq5wvu5u8JqpNxEbxVrpXFGZr/CSJmBbHdFd9kRTFS7nclv1LcNs2FKHZhkX5MxbegVC66qG5GLjma95aFdogdNfD/SDw9F0x97NM/eu7M0cob/JUsjidSw6PjIw/u9H/w6vztN45U+/tqGUPJ25VgYu6aEMOo5U5llBT+LSwm895dgmYLPSkXWhqi0Ai/pap3Wn4pCd2eSj+cS10I1Ji7jvYeONnWs7O5CfuoolMrYVH5n+Nqv3L91ocXLoF8O9rbiHw3fEgLkC9sunN/YHwMm5/z53n+ZWP8y+PCFHrlMzGSe+XXQLgQBNdJolP4TiXU7JusvObVNyUfK3zKyVdspimCvpRaeUAF+1vwOwvE5yFvYgtC4RdQDg3nirck3/NckWL+QdST8wVkbfH7B7uLcKIWN4JMefZ1xlYIJtO2vr66mqoNH8sSGQAVPDIyNjzQf/PdV2duvXaiNri90co8UOJ+mrkPZsZWeaXe8DT3PQl/1k1Ucz/N+ji7R9nXTsGINF5E80u5qfM78vBC6uKcO912tPvwmc4+Rrs2i2Ur0K6AERfwtZt33nv/wjNPEvmW6LuyumoLky/bMJVtCiuEa5YaEdpUMpiUs5KS8glM2qLhteWfcHL0R0Yla07j5JfRsPyVsshXsUfKrbwvVg7B5q5MY/4KjXbirainSI+JkHmC+IWY51urbe4nVvQR2RdGxyYGH/RfO//90N23jjcG+mqMWInAaC1X8aqXoOZJZWnlqxCk5sItfJXkkK+klKzrXfKulLnygQq0O5+6OAvafXzbkdMdfTsaG+qx3dmmH7IcJsAFfON2/zvvfYjs+53t7SvCvToiodKrR6Aw+a6+HjpjSyCA5dfjE5OjDx9cfe8V/+1Xjtf6e2qYL1iEKxRwIqi6eCW3QxYFFyLfLEe+om8Vd4RyG+QyQOTb5Qt7DAOL6Utzbn3L47uPnu3o6aurr0We6a1Gu6ryvXnn3vl33mfk20Hku/FfWCLfjR+DCrMAaRXjicnp6aH7dy6++a3F/jdP1Yf6ai3s+UhsQZGZYRNuB/Ze/pK5vF4XCNoVz1y8zjw+lm/wMGReF+d/7pKHGyqZHlxIn5+rSbcfPXT8bHdvX01tDUsCsgV8u0tdThidW/333jr/3jNPnCbyLYcvHZFvOYxC5dkAgRmLxaamp+/f63/31ZcjD95+qinSW4PMccwHpDiGxLQkP3KFa26XxTlais3myQLkqziJ5BphoXmx89P9ufQ7sy5d+7FDp5/t7dtWW+2zYcPWysN4jS3m5Hv/rfPvEvmuMbKPWh2R76MiR+dxqRuNxWdm5+7fv/v+q9+KP3jzdGOgt9okF6dn4lm4+M3QsJZJpRM982lG52bm8hSwc3z/QhbzkBU+GQzf7qsTzmjr8eNPPrtj+7Yqn88KtUsjJZ4MBPm+/e7TT57uIrdDGVwVRL5lMAgVbgK+1XBEzM8v3r939/wr30w9fP1sY7DDh+wcmgnMwtJXzm8qU7q5QRFSNEtnRs6EG59VY2sMGfkOB/RvTzsSzccOP/lCX1+v1+PBFoJEu9orS5Dvm29D+Z7q6uzQfFR4frPCr8oKMJ/ItwIGqSJMBAfGE4mFRf+9O7ff/v7X04NvnWkMdvosQnPx6Tihf2XkuJDCSpQid0xIHcv/n+FjtffqnBzzLSPnI1Lh4NfoYvL1aW+k7fTpZ57b3tfrdLmwTxXRbv41I8j3jbfOn3vyDJFvOXyniHzLYRQ2jw0gyEQ84Q8Ebt+69f1v/kX64VtPtUS7a7CBp4yFkCQs1tBkTaNx8tWwZrYjghG1/JCFXLOFl+ML6e+MWPxNR5996TO7dmxzOpAAf1PlwVnby0KS75vnn3nqTDcp37UF95FqI/J9JNjopJUQgAoOBINXr11/5Rt/YRl796m2WJcPW9gzghVpKtXgcKUmqXzVgLXsh2Gumvnp+DcdSH3jvmHSe+jZT37m8UN7QbubLP3YSug+yucg39v991978/w5It9HwW/tzyHyXXtMqUZBkfi2Iyl+OBy5fvPWd772Z5aRt6GC23xmhk8ayzN4bJg8hOxVQyPUODKRA1Gsp2N77s1GDd98aJr2HD730qcP7d+NtRLY5H5rxu2u9jKT5PvG24x8uzqV08nhu1og16w8ke+aQUkV5SEgQhGwS0gqEo1ABX/ty1+0jr39XHuyw2dlIbnYpVjZS41zrwzYVaIcmG8X+xhjxxKkd5wLJr8yaB+tPfODn/70kX3bTUg+hoWFBHrRCADNO3cfvPo6yPc0kW/RsJWwIJFvCcGlqlUEeEhCKhqLvf3exf/zpf+vbub9T/ToWr0saZ5CtSIoODMxJxZtIOnntD/1J/36saoTP/a5z508uANbQ9FGkI9waTHyvTfAyPfJU0S+jwDgmp9C5LvmkFKFSyIg8mNEE8nX3rn4l1/8340LoOBUs9vEdogSqZXFwR0SoNhQLP2/LsVve07+zM/89Jkju5CmmcB9ZAQAfv/9h99/9c1nSfk+MohreiKR75rCSZUVgYCg4Hgy/c6HV//8S3/SMP/OD3QkarHhNds3mGeCTKf9SfOf39OPOg5/5sd/8uRju/A+OXaLgHa5IoD93oPB777yBtwOPeTz/YhorsXpRL5rgSLVsXoE2Dwa4tLS6Xfev/Tn//dPGuffe7411mBPLSaM33hoHaw9+8M//COH9m5DGaLd1aNb4AyQ74PBke98/zUssiDyXRNIP2IlRL4fEUA6/aMgwJy8YGFkVn73w0tf+tM/SQ5d0Tfu/uGf+OmjB3dgM2qaT/so4OacC6AHh8e+9b3Xnj57gsh3DYF95KqIfB8ZOjpxLRFgqzOSqZGxqebGGguiG7Zy/rG1xDVTF8h3eHTim9959amzx4l8S4Px6mqlGYzV4UWlS4QARK7JoO9oqbeYeFIIOkqAgLJ1rVo1BfmWAOWiqyTyLRoqKlhiBDS7PJW4pa1avfCeE+OWyfgT+ZbJQJAZhEDJEcCOjCKbkXLQE0bJMV+mASLfjUSf2iYE1gGBWDweCASRcA4Jj8LR2EIgOLewML+wgHT4udsYroM11IR668NWmYQGIUAIbGIEhkZG3/vg8vjkzNzCItZZtDQ3Vld5rWbzx559sr2tCau0N3Hfy7lrFO1QzqNDthECHxEBFsw3Oj757//z77z6xjtJCC22hAVH6uCeXb/xT36ls72VZjc/IsSPfDq5HR4ZOjqRECh/BJh/t7mx/tTxI/UNtTyrPdtsGvnmX/r4cw11NcS8GziERL4bCD41TQisAwJsVu3ksSO7dvQZTUZk0cCSlj27dhzct8tut69D89TEUggQ+dK1QQhsfgQgcs89cbq1uRFM7LDbP/HCM431dSR7N3bgiXw3Fn9qnRAoKQJqwk79iaOHHjuw2263HTqw97H9u50OW0kbpspXRIDId0WIqAAhULkIZGJ6vR73C888sX/39heeOdNYX1u5Xdo0llO0w6YZSupICRHATFU0Gp2bX9Bsucx5Tf7KXTXGs2ay2S3NRkli++bsI2sfJXwk8slnjtyN7ZTtnmWJ7Ar5AjY1B5wmOzLfNS+VSgeCobfOv7971zbmf+CH2ChaPU3ZYZqfILeXVqxW3hEfKIYppvL+5qGQ3RdFhfNzRNksz0cGUFGrim1mZYgeiUdtVmtVVRXSPZdwvNelaiLfdYGZGqlwBBLJ5LUb/d9546LF7hAcwxK+S1LQUKzckJnFciFXG/5TGIkzHacaTYZMDX2wdyWnZZEvO4mdKf5TWIgXkWTOM8NJJhMsqpKwrJ9ZgyOZiifisXjCYmE7MGE3EJacHr+kaSqdipgIlmwuw7NiPyjBsCzjsqYjyu1C+ZBjI7ZIzTNMcqqsi/WXW8w7kyktrxW+yR9mB2E9+8dKGgx4Ue+zfebj55zOip8tJPKtcFYg89cFAWyA9JffeOUP/vKDxrYenohYbMSc17ZgQclcjDcUapIaU3AmZx15yKqkzMsQr1YTZ8hOUYo5LSsaW94GBDWqqlaapNmxFGwmNmxC3JmUvsxssd4qw6I5MlyQLr8dyA7kQ8BZW1Kv/FQ5gf0piB0iXCPhVSbnlig94/HIojxuY1IG6/WhoN+nn/m3//Dn6mqqKn3CkMh3Xb671EiFIwDy/eq33vjj7/a3bdsnZeeyPVLEcK5bIf+kpVLF5y/8lSUFO+U+4atqsdAHOXXxP7XVFJOuXlsmV/myyqTml7eeosDJKpRjA/5U9bEU4jpIcX1occ4evv8bv/xjm4B8acKtwlmBzF8vBJSnbvYsXXRKBK4UCyjkjNF8vZkUpSpxLsm8gnZXxbxcBWsP8SfTmBn1vQKI+cyr6QD3Fyxh0jL1in6ovZE4qHctpc6sqsV9jw/Aeg17Cdsh8i0huFT1ZkJAYUj+/V9pskf1KRSJQA5JK45beXYxylTl2BVbzKlcW17jDMm8XZB5izRpCWOkl7fgrWkZaLmLhFEvz0hT8fxL5LvitUoFCAGOgKK21AmilXHJlpxL0ArXoYWOpajwoxFfhtC1LJxP9zmt5xRepu8rmrc8gAV1bXadgnwr/iDyrfghpA6sDwKZKTM5mSUdCsrkU+YZXhV02hdCMIsH/uUNXsFVsdJDdw7h5//J4xwy0jyfggucgsAu5WCvFGfKUj1V6lyyp8LnsZRDpvDNSNykWFAIZqoqXvbiGiDyXZ9vLrWyCRDImo3XPpZn9U1xpwqnqvzRun6z2DdL0uWKzTxyKjjZlsOAKzC7xtur3g607WrvJYJxM7wr7x2afinxc1m+C+UPDcNm8blaWFsgKwCk4HMAv32JSOiife5lfdUR+Zb18JBx5YMAo8mC8zwrSdECXZDSjnGpWqUi7Nh7BeSxGlS87AN/7txahgc1UlfzZhZpKtyqZUrGvBn25bcSeY5mwowTtnqbyTcwT8lmad5lT9WGRSvsq41TK5/rY/WWEPmuHjM6YwsigGddLK5CsNNSj8rLz79nntQldloRyRUof54G7bIfPqHPXwiqE+sMUskki8/NOngZcYhXUgYrCzA07gWFujRBDpwUUSNfySAj6LhfRONiyGJe6a1VjRR28oalYcrpquWscu4lyMTwKnK5gFOiIIqZp4MVHDYVdl0S+VbYgJG5G4QA038ffYJd63KAH9XrsNS4rS6rySBoVyUoqQYzi3Br3daTu+qbq2ya0CvBvJz+VO2pWSpsMemrnMY6j7nWY3bZDEaDwuaysFgizPjzyLbax3fUYvdoTtCSP5lrGH5J9pvteixcveI+kUX0mmgx9S4gZDDKuazGg12+7S1um4XVnuVkydwxMkNa2NubfyKFmm3Q14CaJQQ2AgHBWY98iMkiRc02VdufP9T6mTNdnz3b9UNnu87saXRajaA5ITsZJ7KFcOyVEI3VLsuTB1o66ly5/JV5aM+1rbPB/cKRts+c7vrM6e7Pnuk+s6cBlcjVxJz4mFjlLtSDPTVH+urMJqPi+uAEm31k/hYWZuSuFNuSkjUeBZQC+T7WW72j1Ws3525WtCospTDnd56lA50feWw25kRSvhuDO7VaeQhkdOkSthctxxiT7m96rK82GkuOToecNvPp/U2H+mpNoF+d3sgn9kTiGLANeBgv4e/wuKxWaGRIWPwz6vESJY0oiTe4Qxo/4vvMnQFpr8vS0+IzmUyT8xGfy3Zqb1N7vdMEfQv/iSpNeXmrxWS3mvRomclcpvHxitXC/4ToxTv4mB+cvXUwQShjprqZiXKJm3A+4B3pZsDfqNxmNTLxLIWxQtys7OqDFniYLxwZlXf95Fls/PVf//VN0A3qAiFQUgTgbu1/MHT1/rSnunEpry+nnZWkcVoHxy149vHtdR/emX775uS90cWhqeDuzuqWaueHd2d3tvse662p9tj2dVffH/X3tXqefaxlT0eV3WbqavTcHfFPLsZ7W73g7oO9NfVV9sVw3GWzHNlet63F29PicVhN43NhHg6Qbq519jZ7bg3Nv3ltzGQyQgg/nAiMz0VrPPbDfbWHemva6hzzgWgoHD+yvd5i1H/QP6czGnFLOLGzbnd7FUhudjFut1ke314Dk3a2edwO88RsBFsQ7e+qPrGrDpWDBef88foqx9HtdShT57MFI8lwNFnrsaKJ4zvqO+qdLbXOmcXIg/FAJP4ojKkGNgi3dCwaNkanTx7eXeXz5DkxSnoJrH3lpHzXHlOqcTMiIJa0rsStK/ecacQ2eA90utvD81Pz4cVwbGDSPzoTqvHZ7GZDZ6Pr+O6Gvd3V8WTKbta/+Hh7V4NrfjHUXO3AKfAMNPocTx9oqnJZ/KHYnq7qQ9tqq1xm+A0e31HXUuPispfNzoHiRTBsncd6oKcGRIm2wMsQuGd31/c1uQKByLZmD3wRcA2LubZEMnWwp/rp/Q3hSBQ7zD97uKXOa3VaLeDoSCxhMZuO7wDFuxq9ttN76+0W00IwbjGavA7zse21vc2uaCze1eB8fHttU5XtSF8tyBdLIWxWk8thli4OAU7RzweiL9mIckm/SVYXU5zvyt8WKkEICNJY6Rm5oOzNf1Ovg3MVGcTiCdBjmuWPSaWRshLP8ciYaDYa4AF48/rkm9fGazy2llrH+zfH37o6duP+NJrHiU3VtpZqWyKRhGcAPoi2WofTYrCZDfAtfO/iaP/Iogw+QC4wnruss9FzandTg89+6d7M8HSgo87R3eRKJFiAA1rc2V4FihezY6jzYE+V02oAjSLzZJ3X1tPoCkRit4cW0Hmr2eBxWup9VrMpXe2yws6FQGx0OgiRu63VwxgcdwuLsbvBiek1+DemFyPv3Jx69/r4xGxIvYCyEVwOTyXjhTw1o3+z/BuVfWWS8q3s8SPr1wcBRXGxrLIFjoLuYPXNzJyYiC7Q42HfaNJ7nRa4blEbeK3eZ4/HU8FwXOjWeyPzc/6IFa5SnW4W6jgUn1mIiKAGMxjXoLeYjV6X1R+KQs+yXL3p9Iw/MjQdDEYSwo+KNvEufq4/mH3v1mQ0lgAtgli9TrMdZG01Vfsc0M5oBfvJw3GMI5nWQUSDguH08DjNd4Zm/YFwd4MNHga7RT8142cxDwb90GTw/I3JKrflqYNNB/tqXHaTx4EUwSa3ywaHA6faNJzXgVAM3Zz1R6CalRm6jGRd+U6WhzJXvJx6HymPz/pcJ6tqhch3VXBR4a2LAJ8fEup3JQks47Uy648lalwFg8KuPphZDMWeONC8v7MaXtHnj7TBe3v53jQcpknOLCKidzEYw6zWrp66phrnYzsbUF08kZjzh+EfGJnyf/eDgVc+HLx0ZyoSY+zLTlHy3oq4DFSF6uAceO/29N0xf2+Lr6/JHUskY4nUQij+we2J1y8PQ1ODMVEzblzFQF0AAFatSURBVAOoZXI+DHq9+XDizUsDl26NPxxb6G50VjktF++ilSQXyOzucGdk4fVrE8jJ3l4PR4chGkeF0Qt3Jt66MnLh9iQ8y5F4srXW2VHv2NZWVedzyPCNlWGTTxg51Kz5c9NEOrCeEvluXTahnq8OgUyEbbb8zXYsiJiAnJoz0VgsXEA3PB369ocjULAvHmv/0Wf64JP94PbUty+MRBPYbCIFlwCiHkCCY3PhS/dn93TX/LXnd7Y2eOAFDkbjg1PBm0ML+7prf/BM74l9zS6XFWo5ngT3SlXOG2f/wMioCpNcgVjyQv/0fDB2fHfTXCjRPxbobnJ/6nT3p073+jwWcAA0LyIWLGbDy+8NLYQSzx/p+aFndh3a1RhJ6QanQ2az8WPHuzpbvKFoAtZ3NLlfOtH25P4GnHR3PPBgKvTunelqj/2lk93PHe1oqnNPLkZvDy847eaXTnYd3lFnsRi5Ni/ilsVRKwhgFp7FkfjqBncjSlMy9Y1AndqsNAQi0djXvv36F757p3XbAf70rzkUquWkt8KMnHBfQDyajXqf01bvcyBObD4YxeO/PwxJmqp22zwO8/BUkC9m08PN2lDlxBKMKX/UZdbPhePhqM7rNPmccDwYQ1E82kP3pqvdVpw964+p81nwODhsZrgmwpGEP5w0GnVwzsLhMD4fM5tM8Oc6bMZYLD4+G5wLRGurnIgkQyQDiNjnMvtYyLE+EI5NzUXMZgP8xZimmw3GzAY9JG00mW6qcpgNBryehlchmrRajB67Bb/huV4MRkORJNwa9V6r3WpeCMdNel04mgD1406gfWxY3vOQ9Sn/g//SBxZnTIu3f+0Xfri7q40te6nkg8i3kkePbF8vBCT5fq+/tW9/PvlKDiiCC6TvQiznxcwbi+bVM33Kt/ARJMNrk1XiXUys4V2UAYux6F95sDUSyn8chWwyE8/n6ooHse8aTmZeDTgZUJEBr9mKZbFTm5xN5G4FEcGrXcqMepiyFhNzfNkbV/fcBCWsWB0KHgvMlDsOHnHBy4jlHLK0LLui51cbZyZODS7OmhZv/iNGvu2VTr7kdlivry+1U+kIFHzaLYJwC2ac4ewF2oWTgT2R8wUVUhhqyV2QILgZ68MU9aekelAWOAi5nW+dVhayldF8G03RFqddJVWE4hAQbCoYgYVhaLgbBC1WSbBVd/xTNsenzIAJyzXuWPYnWhKpKPiPcnsq4uFAe5moDpzM+TIXZaVfTPwethk6QX0gBDYagZX9kIVoWpPqQUySaR0Xkv0k2yhFtWpxxadubQGFBzlNaz5QLRcvpKbVRmjI1WrifiHszJyvBuCpb+VNimWZuaLNOSMp+Veix1vnNmz0gK9B+0S+awAiVbFVEMgJ9VX4VPJXwUDggpyrOVG4MzmAkhUVXlmKLTOxVspp/HytUlXGQ4ppxWcqhKiUrUIM88aZilVryB7LZW4qSiiu8CUIIZzpifhTrUxLzZoWiuNQXkrxtxSa0KzM64/ItzLHjaxefwT443qm2TzeyHFoLmMge9AXuRiYRyFlMRnq3VgAvBITZclVQXdshQZbpMF+JLMKL4LynI5sD0mTgblx4eb1uSxttXaPDQke4PFFdwxoFK3r4c7VpbHyAwZlBxtouVdzMxA8yw7RtHbdsMLCgoizKTgPk5UfGHhfhOgWmls8HqyE1fpfHqtvkXI7rB4zOmPrIQAHaf/9wSv3pry1Tbz34sm7AAUU4IUcptByaFq3p7Pqp57b9vShFoRn+UNx1XerebQGQ0ntpwLvsWNRb93+7hpE73bUu8wG3cxiWBGvogHMp6X3dno/earTqDfOzEcOb6v9oTNdTx1oNpn0zx9u3d3hHZ4MvfB4GxYrX+2fO7m36cee6rs2MItwtyxlmrFWWpTJy6u4eTOeB77HjzBWkrLiohWwKM5hUWB1l5Fg33gsbIrNnj6y2+el3A6rA5BKEwKVigBXXx/tSVENShP0hH9Gw+M7G5H36w++eX98LsaZS24codXYwtkqnJ3iTISpPbG/+cy+xlO76p/c27Sr3cfLs3iIjAtDp3fYrdVuRHwZDWZTe6MHqyn+/Pzge7dnByZD0/54Im0wm81YaIc0Z7ABEWw86bnSlmiQx0moDKwoUE6egl/ZHB4T8aoyxRtI03Nie92pHXVuq2nFkIaVLwj1RiRueOK/yj8+2sVU+f2nHhACxSAgHnbZ6jRNDIDmxAxVFuCaXNenTOsL4qpxmt12czSetFtYSBlqZ4lsapzN1cixIx63wbNml8XoxYJgl0UJiGAUifiD6wOL//IL1//NF6++/P6ow2xCRhuv3QQahDPBYQXfGpB1kmWMMBqRtR0JzxBqy35iyTevjp+/Nh2PJpFlF22kEkn+TM96BwdFrdOIRJQ1LgtidXEygnzrvRakj+Cto0asbLa317mR5AydxXqQapeZ/diNHTU2j01vTKfq3OZ9PUiE5q1zmhAdvAT/Fit9Rf5LZeatoHO7mDEsuzLkdii7ISGDyhABuB3uPBi69mDGU92gOAGkCJUiTGhGfgivZG4vxHO3LMFpzqD/q0/1bm/xIN/C/u7q20OzO9qqP/f8trP7Gk/vbcLCtpsDc9Cxf++vPHZqb+PJPY0Om+n6gznOQWmfy3qor27BH7t+b5avZUv3tfo+faYHSzb6hxdO7WlEAnXkigQLdzd5xmaDB/qqD3RVV7stO9q8/mjy+SMtB3urH4z6e5o9SOPw5uWhjiZvb7P7rWvjdT7P3/+hvbvbvS8ebTu1r6m5xv7sobbnDrft760ZmgmFI9j2ou6nzvXAnr3dtaFIyqQ3/vBTfU8fajuyqwHp3jsbPNDBR3Y0HOirra921frso3Ph+WBchBg/2qFR/LpENGKMz5w6BLeDu9I9v6R8H+16oLO2HAL82Vfrr1WoVExEMWbVsEs+02innpS5qP/1nf5bI/7hqdB/+fMbi4HEs0daHowt/PM/uvjH3+1vrnU8d6Q1wVsEh/7x9we+9f4I/4vRvJCcOzo9v/jZ3T/14rb9vdViEYRIp8Nm1/jSDOElgCf5y2+NnL893T/q/71v3r14dzGRFEIesljMifH4XSy+gLQ3gsB1k3Ohf/Q/PphZjG1v8f7la3f/+Lt3vU7rrrYqn9N0dn/DGzcm/utXbs/MRw/11jqx/M1omlqIfuF797757hCSBSMF8OtXxnHnuHB3+s/eejg0Fcr3EqzKF6GEVaiX3KaYbqM43y1HIdThR0ZA0bYq2S5VkwwLkPEHhUopbIQ0N8juCP5D3rIaHxKmG967NYPU4+/fmYGoRD6dFI9AeDgevHJ/djEYl85fPtOF9DoTc9HzN6dwCiM4vt4LStmQTon9iET0A2fZNFLdxOJJJI7AamDQNN7lqyTEphDw2MqdMLGOmbktdPo7D2fm5uNTi9FgJH53cGFw0h9PpjFTV+3EpnPmXW2+l4611vpAuwYbUjekdWMzoav350ZmkcMsCQKPIElFEhamkaaNpQricR3Kk8IjDoCsQfh/N4PL9yNOIDwijHQaIVCJCGQkbqEFZXniV2hhbehrptN8zogJVAO4CaWQCDIUZ3vj1LjMyDDpshmR/CGMdGFslVg6gIw28PGyXX74dBzbB4jlPh+dDrxxeeRC/9TEXAiUCt8IfLhwzmKGDRoW5iYhaeW0GFvCLKbHeOI0kGMygTPYp8IsSdNirTEYGvwcR7IGtv4Yf8izk6lEKJJAAraX3x18+Z2B1y+PzAfCLNQMbGjMBCDDtkQ6jSA27HWkcQ48qt9BxY2NAFPpK+bQqIjLi9wOFTFMZGSZIKClD1VZZtuWH9kqAnKzDikDQVk8jRnzAgyMLQxOBLCZ24ld9R8/0QHee+PqKIgvGk8guzkXszIQgjl90zqoZiwXZqKSiVs9OHEhGNvdXftj57ZjhyG+mQUm0hLRBA5QeBJsC7LVpZN4E6yKNLt4B3N9+I0QCVSFN2FnNB5H+jTG8kY9PsU7IH1wNt6NxOJjU4EZfxQ7aHQ3O9vqnVarIYY8xExrIymaCcagEpweiiWRWbjRZ9vX7vE5TEveq3KRk8HD/La1NFNvlmgHmnArk281mVHWCLAJt/vYw22WT7hJMsmlBxkSoXRkGc+keGpmiRT0PocZecexkxuShMFPiiTlmDoD933zvYeX7s0hAw608MhMeHQ2LPde50oSuXRddjPmspCdUkShgXzxyI8QNNSDpGgjM8HBySBS/aId7BE3549h83YQ7ggmzaJJBD9Mz0cGxoPwJgciiXujfmQvQ8lrA/MgXqdFf3vEP+dPuBzYKyhyZ9gPNzCm+5Cod2AiMDQVaKh2Nte6oon0neGFcBg5zMyTC9HRmYgNG1ro9QOTwbFZJB1Ow0Lkg5+Yj/pDUO6Z8c0hVsbvbDpuSbbVhrqxON/47JnDuz2evI2cy/oKKmAcZTWrtBEjezcCgWgMKSXf/ML3+5t79orptQJUUYhtC8/IZzERf5Tm7MPy3op9eRWRi5cQq2yLYu5q0JynZ8luRK4wHv+AksxBINe5MUEM8cq9HsjzyzYYRs3MKYx6eDYyznb6BDwGqTSCyKC9eQQc38+Nr1jD6WgapdkEHD9dDbAVdMnn98S+xdwILJTjypX9IbZe5nVxZ0m27M/m2WIm30TXYUEoMGcL3v21n/9sS3MDZTXbiK8CtUkIrDsCfBEtT4iw1FO0cDjkMYvwOmRRjJySU3mLkxPfkN3IDxP/zfZnNxjMfK/4TD4ZwbY8PyRjNYXlGJXycAX5g//xMgjLFfu8Y3KMeYK5D5Z9xrkTSpV5ZY2ICMYvti09O50fKCROYdHNOEWYw6lUMY3Vhnd4i1Dx4FkYwH5A2Yy1Wf3shei79CmsnnnVc7U3vU0w5UY+33X/ElODlYgA24+SS0ipewXPLkHDBZ6gM+yzVO/VhWWcKrUaV1miK6bElHAzUaO0QdHhIh6On57FTvJ9tjZDfqB8LCrn6xik/1gaKG8IQtUqPzx6TVG94o8cQZ7pnkRHIFZQ3hajeSvxYinSZiLfIoGiYlsdAbETOyc7ziY8kEtNMKPRsqJIQZ3HK1COfEDzyEj6FERz2kNxGhfi/0ICPKctQayCccWhJXttYUnxmWKcqXlxeYpmNrF4NSoweLRL6hFPe7TGSnkWkW8p0aW6NxECIihLas18zZsf5CD7LnlGpVyVczQELV/moZVDfZLyBevnZqbRkLp6J1gK/izek2RWiDmVbqpEqWVMcZ5yR5K3FUWJS0meQ7DKfSGLP9WbRT4guRwtuv2orF1uFyORb7mNCNlTpghw5yrPIqM+6ys+3ozs1QheDacItauVw0vxjLaYoquzFbbC5WJyS83pyBkpu8mc9vJhVWlMUJqkT2mqyqqS67T8m8PFStd4BYrbO/fJQECQrdQVbl3hZqEBldeuRCaX6YVStFlEvkVDRQW3NgL8cVvwjEJ8CisoPgjBW8IfkX+Is3LPLVAuu0h2XdmfiS2GMj8KIbN1a3zL4MIHV6xSuCqsnXHLKvypnJ3lRJEcutSNRNXmqk98CROUejSEvXJJ4dDBahKV/Sv6kiTyrejhI+PXEQHhIJWMplKeUI08obiGdoVfIJ+2itC/MjO6Sql5HKoUYJZo6ZWvFJacK9/n58p9KhSZqbgKMm5kyXpqUnal6azqs+8oWsZf/vVSlJrxl2vlsOqX0JwmbxUKoAzUwgF863gtrElTFOe7JjBSJZscgWg09hcvv/ql1x7UtvbIrL5iaRk7hLdUmbxSfKcZv6YSIcFOyAQHMB0tK+Dva48cclGXdGXOkV4ClUn52aI+bpi2PhnNIANzuaXCU6uR4pxbQaNc3qsV8fp4XJrSVc3rjPGaxjO9yDiD2StNcIUMF1Zx4v4OBQstVqI3fBdk2TGsJfHPWQP9/+wXf6y5qb7SKZjIN+uipz8IgYIIxGLxb796/v9894rTW6OGTgkvphKSxYlVPVmEEjAq0fCckGwyOkshUu6pYMsbNBSVIXR1MQOrLeOWFZ5n8YakXUlFS669RQVYcByLxZwOh8lklnpVOCfY/vHSJcLNYCHEYrd5EdkgnCm8ObGuQiVEDdmKzmqoNJt0ZUiaDINjNUvLRa9kT9QqFM8CM4UtDBF5gwzxSKjG4v97P/+jtTU+Il/6thICmx8B0NbDweEPL14HS/AN2FmemtwAsIy6E+JOhmSpT/WcYmSUlyaQV1V9AsYMn4uIXb6wQTic+U6XnCXVCbIM9BpWEzSekd5is/e0bmZ2/k7/vb27dtTVIfmDTLQj/i+9AGITe9YsFjYLGyUdyi0r5J1ChPuqS8x4+LPG0y2sElUJsc+w4N2Q9FwoYkFLwNyJo1ajtMVFeGOd78TRw1arpdIvO1K+lT6CZP86IaCqTKU9LbkVtEFRwnlnrspirb7L0NMKVYj7QJaF+GPg4dC3v/vaM0+e7u3plB/LIvl9Yc1qpGl+e5nbh3LyCoAIOBShvgRi8u0C9qi3Jc19a1VAll1hmnAruyEhg8oTAa7dtD/SI7D0/+Qzu3AzPPKhRUOxYcXKpG8jq5xw8oL9pINjebukdF3adq5s+Y/qSlneLE3hpQouU5XAULMspDyvktVYReS7GrSoLCFQ4QiIjD0V3olNYj6R7yYZSOoGIbAyAsyDTNS7Mk7rU4LId31wplYIgY1HQMx6ZduRN2248WZuFQuIfLfKSFM/CQEZfpEBYsU5Q8KshAgQ+ZYQXKqaECg3BIhuy2dEiHzLZyzIEkKgtAhgjQdrgObbSgtzsbUT+RaLFJUjBDYJAqR+y2MgiXzLYxzICkJgXRCg+bV1gbmoRoh8i4KJChECmwABHmZGurdcRpLIt1xGguwgBEqNgEz/UOpmqP7iECDyLQ4nKkUIVD4CtLatrMaQyLeshoOMIQRKjUCBnDulbpLqL4gAkS9dGITAVkEg2+1Azt8NHnci3w0eAGqeEFg/BLKy6CpJydaveWopCwEiX7ogCIGtggAySmr2nqSosw0edyLfDR4Aap4QKDUCiUQiGo2GQuGFQDAcieEXfvBnMpmiyLNSg79M/bSTxQaCT00TAuuBwLsfXPzSX3xjcGgsEo0tBoIej8ths9b4vL/6Sz/X2d5KIRDrMQaF2iDlu1HIU7uEwDoh0NfThRTqd+4PDAyNzM7NPxwavXnnfldnh9vlIuZdpzEg8t1AoKlpQmCjEKjyeU8fe7ypoZ5v/cl2E6qpqX7i9DGfz7NRJlG7QICUL10GhMAmRwBhDWdPPr57V5/ZbMJr7Fv83FOnO9ubTUbjJu95eXePyLe8x4esIwQ+OgJ6vdfj/ti5Jztam6F7G+vrnzx9rMrn++gVUw0fBQEi34+CHp1LCFQGAvDtHjvy2KGDexwOx3NPn+lqbzUZ6bu/wWNHA7DBA0DNVxACbOP1vANvrdCF/HNWeic39RgLyS3qWMYYm9X8ieefOX744Jnjh2qqPGwXeXZkqtX0gocAF+otM4y/rzS0Ut/VSgtBp+3SyjBW0IVSnKkUalYcTlRqyyOA2ap4PC5mrCQ56sWmEFkhA4zT8vao5BSl/SVfs4pkeWVjS1Yn/0+70yVjqQyNqa/Fe6w1Xl45VZaUZyhNpdLpaDQ2O7fg87rtNpt2PNm5mTZZfRr7sgZe2zNuoIBAvuRcLvHJ9FbDv+pnsuMqeGqvFezyUETFaIXhYDQazGbzJrgeiXw3wSBSF0qOQCgc/u0/+JNvvHEV3398Z9L6dCoFJmBUrOxKKRInKBv1KOyp6EupJHGO5C9eAIQiyIqTs0KxjGEEKYvComKDjqXjlWQnO6yQnpCV7Bdsg1WMqRRC5jUJwQpz8cKIiTZWHcLP8CfKsVa4Ccwe3gZrkhmIEsIyUb/gVkn57GTxB6ducSYvz99nRjBjkmkAxTvHWxC/xL2CIwcQxEe80zDBgFYNOIz4Pz/krU6P/hsNyVS8r6X6X/zaL7ndiJMr+biXtAEi35LCS5VvEgSCwfB//L0vDMSaXU434wutuBUCUPEUcO7KiE5Qi6QkBQmFwxSakjq6YLKxjPzNpl2F9iSjcQsUPayKSs5bgrwFxeOWwdlVsiRXuFpFrXF2iIYLkdsSThZOz6oIFs1pe5q5DhSFLiW/InGzNbWgXXY34BWz+xzuHKBx//yMI3jvX/69z9VU+SqdfMnnu0nYgbpRUgQYs/C8CCmdPolYLfajHuw1U3r8h78rCvA/QRnKn/lv8lO0ztWMQ1UVspm6eeVCH6taVIhKZhgXtpkfFlImJLR4wV6n9HosKBYmcWEqP5FqWekCKyn7onZLfaGxEJYrP7wmWTPT1/xPxW+c3SkBUZK3INpX28oGKplMJ6CcUzrgnpRdVh4zSjrY61U5ke96IU3tVDgCyURS0Il4uhbaTHl4Xl3f5MO36rFY4mxNE4qvQiP2uBman4w9irgVz+1qGeW10MLqb6Fwl+pRbiuaFrVWZ0wV3gThUtCipPq0V4Wb9FUIXwj7B8Ji/o4l9PfqhmGjSxP5bvQIUPuVgACTcczLK7io8AP5kmSUYWntw7fwRkgHRRZ5FSpfPEgacit8kmBecWhf55f+aJ8KttR2WdyqVjgKlpH3BsnqemhlFbqV6ivfz4l8y3dsyLJyQoA9S0uFmMe92vcV3VfAdqFDtWcvT5TZ1Urm0rypqNoc5l761lDQNiEqH+1YgkxVJS2fD1a+Wak3g2Xt4HqaaV8+01nxB5FvxQ8hdWB9EGAzQxqaKkDEKhmqD/KaF4rUXI7qeJ3yiV11NIgH/Szalg0ptQsNq/4ly+f5RuQ8W6bwMiYpDhWl8NK+Am1JdSA0SPAaZA9W6rti4TJ3A+HL4Mq34g8i34ofQurAeiIgHKdaV2rGC6qQYJY9+YSynNBUPlNdtVkEK2lMW7+0JuPazbBwliwt9LyvivAcJsvySwjuzKHVpREX2GiKa/4W0GWfqxXJS9eqRpeIe5OI8av4g8i34oeQOrA+CHAPLQ9rXYZ68rSffINzzkqP94pPQp2bUk/RcHGmQnkPUGJ0ZWHNDJlqjPSQCj+pGtXLWDXDYXlsJn0UeaydT3tKvJrWo5L1YJBDuSoOGXWvmCqrWMo1zMdAxJ6tz6CXtBUi35LCS5VvIgS45lq5P5qn+4ISmEtJrT5cknByBalUwfLkDIWpXtscF7LKedKTwcwRZ4mH98zf7JUMRxM2ZwrkdTjnFpLjAMgspVgJqRzm1TJ34VOVE1aquGI+J/KtmKEiQzcWgfznZdUeVeataKHKh9yDLCiYq9EltF4u2QvXr3IgN47dajSbDDg/1zkgSTSb03hUsMWkt1uMCENT4rhYUZvFaGapdpQGVXuyal5Juwvi1utRm8OK1D0FyovwN0b26g1g5WcCLdIrRGisOATlU4DIt3zGgiwpcwQKi7MsglnqeVnTM3APaKnGbe1qcPc2e7oa3fVeK1/pKxRnbisa/s00hUrwvsduOtxb1dXgVD2/gptFVZzk9A6bqana0dPk6W3y1HqsFpNxe4vnQLfPZcUaY+nOMBj0j2+v3dXuU9YTq/4VqZk1Uj2fT1UDZfgXereNNVHldpi1K+iESe11zkafzWRcOsiiAIasI/IE2X4RjyBlfjVRMvWyHyAysGwQUGlNsSiXJotgXjykg2e7G90fO9b+2bPdnzrZiZ+nDzRbzQauSkV6BrbyS9ttuRJM+An4wYolk2C347uatrVWKSESyvID7uRFXDIU6KHe6s+c7vzUqc6XTnY+1lfntlsP9DYc29XkslvY4l1EDrBMCsadndW7O6qQPQFzW2yJmlidJ/JEKCvqeMYGsXaNS1dl8Z5cQCfKpVJGfXpbq3dfT7XbbuLdEf1i1Xrs1o+d6DzUV2czf6Q87psi2IF2siibrzYZUu4IyFmej6i50q21jheOtDZV2a/en/nO+0OvXhgeGA/EkX8mrbOYDXVea1ONvcplEQIW5AWxWue14cdtg1ZlNGsy6H0uS63Xio8EGYM9HTZzjddW7bHaLIzH+TrjdGuN4/C2WsjM1y+Pff384IMxfwyLoxnl6jwOMxryuczQyqFY6tsXRt+4OonPan02t8PkcZobvFYXY0/Wgs9tcdnNaBQi3Wox8gQ9eovFWOe1N1TZnTaTWP1rMRlgVZXHajYbOTWz9cc8NkEsI05tb/M6LMb+EX84huWCj3CoLuWiHCCP0MB6nmL89V//9fVsj9oiBCoRgXgsfv69y4tpn8Vqz/KuajtThPJF8TN7GvtaPa9eHjt/Y2I2EJtZjIzNBSPxtM1qeqy3+vC2uu2tvvZ6VyCamPfHvU7r4zvq9nfXwEGBp/VQNBmNp1rrXCd21fc0eWvBfdW2idnwxHz0QG/N3g5vS40DWRNmFqLCBQDnxrZWTzSauDuyMDQZmF6IIGHCvu6aag9z+u7u8LXVOqcXI5F48sTOWpvJMDITfulke3ONo6nKcbCnGsQ6F4yhoucONcN30dHo2tdVbbeaZhZjFotpbxeztq/F63NaZv0ROHP39dQc21EPd0pzrTMaS9wenp8PxCRCaT2o+Yl9jaFY4uLdmWAkwUKac5bAiaJLu7/Ro3g0bIrNnD6yx+N2LuUor5QLjHy+lTJSZOdGI5AJFMizpDjaBR8adOkqtzWeSI1NBbGfGjytTx5oOr2nwW7RHej0feJYuyGdnpwN9Ta5P3W8AxL26Pa6Zw82gR1jscSR7fVPH2gC053a07izzZOMJ6ocJnhPwbYNXvPR7dUumykEUoPYFCSm043Nhm4+XKjy2M4dajm5p6Glxm6GszWdRkn8zx+IHeytOdBV7bKYHt9WjzpxSm+z9/TuBsyWBSKJM3sbz+5ttJjMYP99XVVQzHAZP72/GQ6Knkb30/sb7WY93AdHttfu767ua/XivmIx6GORODS6zJgjs+YwX0pzlb3Gbbk9OO8Px0Xqt2yPMFf6OVEXCtKK60N4OzZHpBm5HTb6G03tVxQCxfocVHew9oUgDfAIFB9UD4IL8MC+t7v2mUPtDpsRPIj0Xd94Z+g77w9euDPd3eT22g3w2IKLv/zmwNfPPxyaDrfWOSFmW+qcd4cX/uL1+29dGQ1FkfkrHYrEoGr9ofjIdHB0JojnfeFnXQzFXr88+vJ7g/OB6MndDaDgajdzaERiyXeuT752aSwUiTf4rGblvsIzBuvnArGX3xmCmyIQSUKDYzoOScVuDy9+7d3hV6+Om0yGrkYXVDD81Gg0EE4g025LrbujwQOKfePy6FfefHBzYFabq42lbtOltrV5I9HE4CQ0fSITMb2E+zbjRxZOZ0U/s1fFDkK5X1mkfMt9hMi+MkFAEyFVrEXZjklBvLrxuRCSmYOJQHNfPz9wY2A2nkibjHCbMrUIty9CDvjMlQ6iEgSNU7DpMDJaMr8wT8QIjwF21BA5Lvl0VnpsNvzOzUkUfvZQ88HeWgSfcRPTRgPOSly8M/mN8wOjM6HuZq/HZQH3g3yTyVQswbeST6dEiJlkubQunkzBBAOaBmWm8JrVFYaVuqSwBweasJqNNT47XLvwacAA+HkR52AywQPNIudE0kpRK6bp4MXubHQPTAQyjohiUcwuJ1TvZnD5kvJ9tCuAztp6CMjv/CN+7WX0F1jj+sO5gQn/gW21Tx9qPbWvqbXehTkwvcF0e8RvNBjgUji8rR7P9f0j89PB+KX7s9Ue++m9jYe31zf4LA9GF6fmQlPzoY4G97HdjXu6aliYRFrnc5oQPjA0FUBVCIFQA2zdDuv+3tqTe5t2dFTBVzsF926MZyXmrCuoEQzMszSyCTp4MPAb4vrEvsYTzBmifzCxiOKosbPe+Vhf9f6uqkg0fnd0fnjKPxeIQvkOTvgfji8+GF+cWQzbbeaD2+pO7G1qb3SD3NkNQlwnad3OjirMBN4f80Oqs3e4o2ZVElYtXOmuXvWrQxNuW49FqMerRyCGCbf3Ly+kvRZLoQk3uVpMUk0hflYWmRn08KUuhuII76rx2uurnJF46tbQ/L2xwPhcFA/4dT57rc+xGI5979LotD82OR9GdEFDlQMzb0OT/ndvTc74I3Ds+lw2vBNOJFFgaCoILtvTXYt3Zhaj1x7OgxMFsznt5u4mbwem5nzOxXDiw7tTg1Mhm8UEr+u9UX80kfK5zQ8nAsMzIcT9Qhr3jwZO72+OxuM4t6HaAUp988YE9OvxnfXRWNJuMTut5iv3Zy70Ty8EYyaTCVNz9XA8m/Rjs8GphSh2V4NhBqMR03QPJwMwDE4RVOV1WU7vbYbr4+rAXDia5NmDNDHLChevMCw88IJNuMVnzhzZ6678CTfaRmj1X0Q6Y+shEAgE/+N//6PBZJvTXV1gOp5PH6nvFxbH/F1VvoEBPQ4Lpr/AT4vwrUJ94pndaKx12cxmPVRkIBTjhdMmg6HKacXreRRlDgG2gyQ4DgFk0J4mA5twg4Z1ozaDAUWC4Rj3DIim9HabyYnGjIZwNBGKxiFIsSgODg3EG+BEj8OEqC/8uJ2WVCI1F0r+xueOjE4tfOXtAVD51EI4FEsiXveXXtr13u2p9+/Mwu0wOR+Kx5MgT6vFUu22wf+AwDE/otXScGEb3XYLQjegr2EA+FpEKDdUO+HRhkYG48OnkUO2yi1rhWcKVpFeH1qctQVu/+O/+aPNTfXMQ13JB/l8K3n0yPZ1RkA4HFf1tJyxUMy9yR/Q0+RcaGQ6MLfImJfP/qfhiJ2YDw5PBaBtFRezHqERkwuhqYVQnG2lwYgLjDa7GJmYDcXAm1HEQSQTiSTqAS0GQ1HulM3MUIUj8en5EILa/EHEmTEuROVQvsLDAIkahus3nYYsnQtFDfpUNBqPxhMIgBsYxxmYGWMrKyBXA+H4yEwQBoN5RZ9i8QSqhf9hIRAV2c3RwvhsCLoeJA/m5SSLGGQ9Kn/z6jiYF3zP3ny0UdNkqHi0CsrtLCLfchsRsqd8ERDT7mITGy3DaS3OYRZNSc3KMLFmTFCpuqCYh16JQ/1o6XbUTJbLyT+lnUzsQKYN0Qr3ZENNgwggsfHitcvDF/unee4zHoeb1oOsX70y1j+8mL1/DwtZ4zVo7kX8tQzw4Hbx6Ak9OBe6G7/Z40GGfdVIkKJGXInI0GBT1HnlW4jIt3zHhiwrNwRktGkO40gKzTWW0674JWlV7jepeYfHrIpIA366wmNaCs5ldpF4kpEaHrv5lmZq3oOsOkQULa9bPZQdMznBy9sHp0C+TI4vloNb+frDebyhciqWYJy/MTk8HeThD5reinQLapoc1fj8eAQJHBhdu++zev8qVgpL4v4oe2+U0yVF5FtOo0G2lDcCPHZquSObRVRpKelV6FCxSKDAOgHlY1X5ypbypa1kPSl+tQZl3A2qIJVvZTUuxbv4SCxQzvywl4wX+WbL+D8PhRC/c+8zGtGbf+/RfriEy0A1cgn5rknoo7YtxHSFu3t5b4h8y/vrTtaVEwKSMqVKzWaeQmygJS0srnVYjTYzz4pTqFNSpqrqNRNBwdgGIWUddQ6kgmS0I/6pleQJxwx9C6IXQpeLTv7DfAoszw3fDyIz3yU4jf9ghg6r79pqkC9N11zjRGYJUbJYjaqoaeX+oc5G8gq4TV0NLiQ/wzLnFSuVFKxtu3g7yun6ybGFyLeMB4dMKysEsh+rVzRNUZw6pKQ5sr3upRMdnz7Fsot1N3ngXVXcAVqXKSM3ttSC/XCuk1SIRGiGxir780faepo9wj2genylz6Eg9eetw0XY2QtH2j91qvuTJ7s+dqwDWSMQI8FFL69TaR2VOy3m5w639bYg/Y7x2cNtj/XVCu5VPAVCe+cmZ1AwkbeG3HuMchKCFnAneKy35vSeRmS0WB5JjQecMy6zYpOw1ibpxorfBCpACHxEBEQysGWOAh/y1GLIr/jkviakkXTZLA1eB6KzWIwUFqixQAKZshHV8ugDsYZNSQOmEDGWts0H4zeHFueDSRAxI0HFjSw5mslJdjLex4oNXoD/yasXNuP/bXWuo7vqOxpcNR5bX6vvmUNtIHSf245MknqWpIEtreM/CHoz1fkcCEpDeMK90cDIVBiV8t6w6thiYR5bJ2Q0a1SEOwhPMd9ija3cEHwt+yOs4PSdYqs5qtw2BDVnJVxXncAKyhrjVUfNphC9vIO0yOIjfiXp9C2BQJQvsphPeiw2RyYbV7bnMccPKfgR/w721SL114d3Zs5fn7gzsjg6i+DZlNNm3tNVtasdIbzGBWSUTKUO9dVUuaydDW6sAN7d7sOqh8n5OERpV5MLS84QlwbxO+ePY9kC5CrS3Gxv9SAhpD8Yt5hNyMiOP5EHEnG+SJBW7bHtbPX1tLhBhsEwW+cgqLGnxdPT5H73xsT7d6aQXrLWa9vVUTUXiE8sJF0OC9Kf72jzwoapxRiCjc/uq78/unB3LIA1xJxB09C/EYSphbDEw4wVa4g51hnM29t8uzqYtcFwEooe95jmamdTjQP5gsMxXWO1Y29nFege8WyIrgNEEO/QvA0+OzL4IN74g9vTWOsh7h0aR8oSDMsXWZgTc2eP7HW5HJXu+CXy3RLcQZ38iAiIFW7zKS/Il+k3xSGbRRLZZKB6hmt9drAPnA8I40XMADQscpw/daAJGR2xFHhnhy8Uis8tRj91qgssBj2IONk9nVWg5g/vziNdwg+ebINWxKI1uCxAwVidi0Ro+7t9dgtS3OhRGDtQgLg9TktHPZLdGMOx1OPb63qa3dguiEXsYiEbW/HA+BfEB5q+fHf63nhgejGK0C+QL+4EY3OxFw419jQ64VPe31PtjyRmF+NP7KsbGPMPTARfONpe7TQPT4VePNGBFO73RheRvvLQtjpwNCj4cK8PKzU66t1Y+hGJpdH0wb4abJmxGIkjzdrJXfU4t6XG2VLrmFyIIOMlMsfX++zVSA9U60Dw2Qe3pxBNkUOj3KNRkH/18VjYHJ89+/g+l7PiyZfcDh/xW0mnbwkE2POzwhBaplhmul/F5frA7FtXx+BsOL236ZMn29tqHaC5vV1Vc/7InYdzWH22q8OLnR3ARwaj/pXLo1htfGNoHjzVVmOr99q7G1zjc2Es7UX2Xqxra/RZd7d7Hoz7v/XBCJLpIKUD6BLENzgZRIt9LZ7OekdbHVy1+jtDCw/GA8j/y3SlGnAmHv6Z41SPbMJslVs61d1g39vpnV0I3R2ax8QgUqnxuA7OgQYdlrFhqnAhmAhEUr0t3iqveVdnNU6MxZN72t3IFnF7YB7ekp4mV5XLjHsMKrx8f254KtzXAhVsnfdHZhbCIP32WrRShZSYH9yaeufa2CIyBUvvtoiKyxzCd7H0hbXcZxV0ORL5VtBgkakbiYCB7y/JCGklxtW4LtnL+UDknZsTX3z17uX7M821ru0d3vZGF3JIQgBua/PF4ikQIDgObDgxG8QysLlg9Mr92WA0uafDvaPFGY0ysWlGJjSsgzDqkYUSL248nB0YWxxBVgdkTPdYvU4LVK0bxJdMI7Fk//ACSPDMvia4EZCZV3CV6koW0blwvNb7HFgcPDod9NqNyIMGR3B3qxepJ1CJsvUlHLrsTGhkZIO8NjCPLD/7umoaqxx3RxYTybTPaYaLAxnauK5PsSTB6TSSu98ZmkeySriMsYNca4Mb7mPmBU6loPRZ3sspdBP+ayyDXtKNrkxIKpEamZCNjBd7I6+GtWibyHctUKQ6Nj0CLCIg78vCWU1LxXkzRpiiSjVX2+vdlrmFMPaSANWCsEQE7cjM4mtXHn7trf43L4+xLI5I2xhDzkYWKgBVeGtw/kB3zcGeqrsj8/5QEkGhqBzTXyBHJHGAXxWa12pkjBaJJUZnAq9dHvnGOw+RvXdkOnTlwdzL7w9B1h7orcWkFnf4sumyFGiVZ1Kv81jh2Ti5u94fTtwZnp+YC2HC7PbQ3CsXh77x1r3XL42hr0Lss+k1PoEGAX13zA9aPrWnGRVBnicSLI/E+Gzg+xcHv/rWvdcuDs8shtAOFDF+sLw4Ek1iddzV+1Pfevf+V16/e/PBNMpjayK3w9hS54KDhT1D5EJY6EpSIVbc6Jtj0o3Id9PTBnVwbRBQvQ1qgoeVno4lL3c1eF461f1TP7DrmUOtOAXBAxfuzsJLsK21+plDHc8cbrc5zEJWsxyMSraYd29PYzM0bOn23q0JfCqy/YKjR+ci98aCJ3Y3/uwP7PjBM11wONwYXMAeP0/sbzqzH7kcXdhF7fTehrP7mqCsZ/wx0KuM7NXp+f5tujMHmv/qM70fP96B5r5yfmBqPnJzcPbeyOLBvrpzh1vPHWk3sJy8jBlQOTQwSzXJ3RALgRgS8kJoI4HDxEJs1h+9fG8GUcBPPdZ6Yk9TU70TWSrUIAusJ742MIeMFIe21597vH17RxWyXl55MAsEPn6i86VTXWBhZLPM2ip0JXfCSo8cazPQ61YLZTVbN6ipoQpGIBAM/dbvf+FusN7pqeYxVshuLrsjSFn+pZkm4o/57D/2ON/krXbZo8kkMqnjoRtTTHDgdja6nFYTnAzYlgJUtaPVs8CS10QYH6XTyE2+t8MH78CVB/PIwmi3GLC3EHKWL4RxrrW11om930F/8OpiG01syglfKibjkMhxMRzHXFat2wpFjKSOmKnjypVRO+i4rR4nIp+6HklwJueDyEgJgQzzEX7Q3eiBpsZsW//IInTu/k7P5Gx4ZC6yvdmNRDkPJpAD3oBdNVtrrCMzoYfTYdwm4EaAI8XrMGNmD3OJi8E4dipKxFMjs5DS2A/UhGobqmxg8om54OhUELeWrkYvvBZzIeZtwfRd/yhzXwgotZ5fFU/tmyyrmX/WHuz/p3/7xxrrays92oHIt4IZgUxfNwRAvv/59/7kXrjBgZSS4lB4VqUJ7bOweNDnoWasIAIT4F0FySAzmVhsBra2Ih2k0YCkZSzjTBqbVrANLFiWc74zPIoghTnewAYWnNz1cPjKJWl69hH+RGU4nUlUA/uUTYKxzSlSiILAO/BsQCkLv6p4uBfFkLIdvmsUZO0qCxfwudWMxJN4P4330Rym7PA5zGVm6PAm73Eafmc0yumciWOWlAcRZpCwsIS9x2OYeQodGQmMRJdoBR5hARu6jDk91imODGtLQTJn2i1/cHEGI99Q/z/9Wz/W2FDx5Etuh3X7/lJDFY6AoMyM/1GQqPKGnBFS0tXwD8QyMJSCuoTcxYa+YlGFYGbISZHri1M5/Llifwk50Y8z8RnoVaxV4PTHThbngsRxLk8yyRR2Iok/scMy9nNjqx9QEi5XNKrSGXfgMu8tTIDWjcRlu3IhBG8CtbF8v4x5WXMs9pjH3oJUWbphPpkGZo8x5uV9464QFILs5Vl6ubyGX1n0gncERWOJRJwZJt9EebGJEaqXfVfKFnd9SNiLK1zWpYh8y3p4yLhyQUBO9Qg9K/PiMLIRSykkKarxXIVn5AUBZT1Hq+/kuDslUy0TRizJTa1TVqvJGiYIt1C8bHa1gvuV+0QB+Sk6KHup2K++IVrkBmfq5bAIEufvaz/JBUetueBYaxqXzwybxvNL5Fsu326yo8wR4DKOky3nXkkZfPZNsLDCytrPM95MSdkK2+ZymVR/smohb7O4XcN9WXyURYtCNstzRYhDoR+lLs6NqnzXvCjYguhffi+lHhefig4owldRwHnadnnCFaRdoAyvO3uSrsyvmuXMI/Kt4MEj09cVAeGRVclOdetKQpJEluGfXOJTyVQSlOQRDdFpfBgqiSlEJjSzSuEqfyp0l1HV4gzResZLkgcVZ2mFHaUyVY0v+EJR7dk9V+41mseBLE7XEnCuvucdEqbmtqixPIOQes9bMRPaul4Zj9gYke8jAkenbTUEwE8yUU0O+UitmWHlfCZRdGzGL6EqUi33qtIyW0xLASt9FoIzVXnNq1SUt0pjCuOparQQC3ONrFWZhXWyyo7ahhSbVDGcrbBlTzI+FuVGIO4f2puCZN08ia52QaOjeUeZQ2NTBPoS+W41DqH+PiICLNxV+h2k7FQcDhkfhNYdoT44c85StajWS5GR0TkFlCduVb5maDnDdoKEpXTMiFytjpQkLilLIy5Vz0AhIuTVZlBSiVRpjndGsL/CohkHh+J2UD9ULVSFeObGsexQaN0OKu9zH8emoF5Kpv6IX0Q6beshwJcDiNW24uArv+SPJArV4SmpSaGwPHmbecoWtKvxKEi1qDlFvsyUk+dklVQIMaMqNfpSealKW9WHkXESZ+g0S+Eq5K7Sv+xjIQS4klbqyaJv9S6i9QlrnwMyKKhPEOIS0/C7ItTl2xV/CZLyrfghpA6sAwJSTopI1wwrsOW3mc3O+PuZ8F/G1appMqZL+7wsX7MNepRwMo2kW2IFAU/vo5gg13doIo5FTnTRquYVfymDEsQzOzdO2RNDbsyj2clCbB4ht5CQK43l7j2yNU1Gd96Wkimdvy+bV3rPjWb/+DZxGYg0TQjosppVm+f9Zefh/4gK1hmQengzHLTIYjOMIvWh1Aj4A6F/85u/891LMyaTBYwrWUnZwFJxnmJxsNhmQmwMoZmvz9AMpyamDjMLa7mkFk/x0jks6FMwPfcA8Id4rE/Ayl/85ikXeEgvfthLWV7ULahV/GMJezhtcVLm1sF7khBZ0Xm6M+bKZpWwKnhhzo/CoIwEVkxgZnGDJHNn1kfIFlmNCj1L/y6LOZNbbzAjWGwwbxy/OCEzSlbf5z1lKzeYMUIa8pQU7IdVlIgGexpM/+mf/WpdbbXSUKkHv1T1E/mWClmqdzMhAAIYGR0fHZ9i1CC4ifMQ/z+nDqn2xP80ohdkopZVlKZERrpvBffxSjIVSyrmFMWXM/DNfsC7fCcL2XDGmyydA4rEzHCieGqXanNwZOzu3QcH9+yur6vhdK5spJGxV9igcjBrQWyvod4FOP1yZhe8zw6RBE0oauk24IioGpx1MLuHqnxXHMzyvqFcNZk/OQICOm6a2+XoaG81IhN7hR9EvhU+gGT+eiEgdKDKm2s/66NxkspWFNbO+nO1/VVleVp383b/BxevPnX6eFtb82qrKaPynMmV+0sZ2bVaU8jnu1rEqPwWRYALPOWHKdC1/kGdOT+iCfXNR2uR5XmAZGaqmYlM+Bx0afyp1LrWvXg0I1d1lnTqVPx1SORb8UNIHSAEikeAhSprowbWXsAXb8tWL0nku9WvAOr/1kFAOGWzuJd1Xnpmtw4OZdJTIt8yGQgygxBYDwTkmraspvKdzethCbVB5EvXACGwZRDYDNNUm2ewiHw3z1hSTwiBIhAgJ0MRIK1LESLfdYGZGiEEygQB4t4yGQjK7VA2A0GGEAKlR0AuWtM2RA7f0sO+RAukfDcMemqYECAEtjICRL5befSp71sPgULhDlsPhbLoMZFvWQwDGUEIrAsCbINkTUPkc1gX1MntsJEwU9uEQBkgoObbKQNbyATkbaODECAEtg4CIs0ZHWWAAJFvGQwCmUAIrAsCPDkjLSdeF6yLaITItwiQqAghsCkQyJO8FPS7keNK5LuR6FPbhMC6IqDuMbeurVJjhREg8qUrgxDYQgiQv7d8BpvIt3zGgiwhBAiBLYQAke8WGmzq6hZHgCU1o2iHsrkIiHzLZijIEEKgxAhQRskSA7y66ol8V4cXlSYEKhsBCnAom/Ej8i2boSBDCIHSI4At2EvfCLVQFAJEvkXBRIUIgU2AAIs0o/VtZTOQRL5lMxRkCCFQcgQo0qzkEBffAJFv8VhRSUKgshGgSIeyGj8i37IaDjKGECAEtgoCRL5bZaSpn4QA/L1I6EtHmSBA5FsmA0FmEAKEwNZCgMh3a4039XarI4BFbkpO9a0OxUb3n8h3o0eA2icE1hEBWuS2jmCv0BSRb/mMBVlCCJQcAcqlXnKIi26AyLdoqKggIVDhCDDZSwvcymYQiXzLZijIEEKgxAiAfMntUGKMV1E9ke8qwKKihEBFI2AwgHvpK18uY0gjUS4jQXYQAuuBAPI70FEeCBD5lsc4kBWEQOkRIJ9D6TFeRQtEvqsAi4oSAhWNAKnesho+It+yGg4yhhAoKQLkcygpvKurnMh3dXhRaUKgchFI46B8vmUzfkS+ZTMUZAghQAhsJQSIfLfSaFNfCQFCoGwQIPItm6EgQwiB0iNAC9xKj3GxLRD5FosUlSMEKh8BPfP60lEeCBD5lsc4kBWEQOkRYLkkSfqWHuciWyDyLRIoKkYIVDwCXPQS+5bLOBL5lstIkB2EQMkRIJ9DySFeRQNEvqsAi4oSApWOAA/1paMsECDyLYthICMIgXVCgKh3nYBeuRki35UxohKEwKZBgLi3fIaSyLd8xoIsIQTWAQHQLzHwOuC8chNEvitjRCUIgc2CAI81I+4tj+Ek8i2PcSArCIH1QIBk73qgXGQbRL5FAkXFCIFNgUCu7KWw3w0bViLfDYOeGiYE1hkBCjNbZ8CXb47It6yGg4whBEqIAAvypTDfEgK8uqqJfFeHF5UmBCoXAUqmXlZjR+RbVsNBxhACpUaAnLylRrjY+ol8i0WKyhEClY8Ay2tGR5kgQORbJgNBZhACJUcA1EvsW3KUi26AyLdoqKggIVDxCOhxEAGXyTAS+ZbJQJAZhMC6IKA3kOdhXYBeuREi35UxohKEwGZBIJ23uJjWGm/Y2BL5bhj01DAhsP4IUJjv+mO+VItEvuUzFmQJIVByBNI6ot+Sg1xkA0S+RQJFxQiBTYEAczOQq6EshpLItyyGgYwgBNYBARbqQEfZIEDkWzZDQYYQAiVGAFFmTPaS8C0xzkVWT+RbJFBUjBCofARYLnUSv+UyjkS+5TISZAchUHoEOPUS/ZYe6GJaIPItBiUqQwhsDgTI41BG40jkW0aDQaYQAiVFgJL5lhTe1VZO5LtaxKg8IVDpCJDfoSxGkMi3LIaBjCAE1gEBHmpGzLsOSBfVBJFvUTBRIUJgEyFAnt+yGEwi37IYBjKCEFgHBHg+yXVoh5ooCgEi36JgokKEwOZAgHMvEXBZDCaRb1kMAxlBCKwXArTKYr2QXqkdIt+VEKLPCYHNggAPNSOHb7kMJ5FvuYwE2UEIlBoBkG+KETDxb6mRLqp+It+iYKJChMAmQADES9xbPuNI5Fs+Y0GWEAKEwBZCgMh3Cw02dZUQIJdD+VwDRL7lMxZkCSGwDgiQw3cdQC6qCSLfomCiQoTAJkGAIs3KZiCJfMtmKMgQQmA9EKBFbuuBcjFtEPkWgxKVIQQ2DQI5kWa02m3DRpbId8Ogp4YJgXVGALkdSPeuM+bLNEfkWz5jQZYQAqVFQK83sD3cSOyWFuZiayfyLRYpKkcIVDwCIF5K6Vs2o0jkWzZDQYYQAiVGgCIdSgzw6qon8l0dXlSaEKhcBJjwZasstKG+FPa7YeNJ5Lth0FPDhMAGIEBzbhsAeuEmiXzLZijIEEKgxAjwrDokdUuMctHVE/kWDRUVJAQqHAGR1UwT6EtEvJEjSuS7kehT24TAOiPA6JYod51BX6I5It/yGAeyghBYFwTI67AuMBfVCJFvUTBRIUJgUyBAwWZlNIxEvmU0GGQKIVBSBIh6Swrvaisn8l0tYlSeEKhgBIh/y2fwiHzLZyzIEkKg5AhQmG/JIS66ASLfoqGigoRAhSPAt45HXh01sw6l2NnIESXy3Uj0qW1CgBDYsggQ+W7ZoaeObzkEmPIlp2/ZDDuRb9kMBRlCCJQcAcrmW3KIi2+AyLd4rKgkIVDhCJCPt5wGkMi3nEaDbCEESopAVmIH0RLxcUkRX65yIt8Ng54aJgQ2AAFaX7wBoBduksi3bIaCDCEECIGthACR71Yaberr1kaA55PMOSjF2YZdE0S+GwY9NUwIbAAC5HbYANDJ7VA2oJMhhMDGIUAzbBuHfXbLpHzLZSTIDkKg9AjQEovSY1x0C0S+RUNFBQmBCkeAZ9Uh5Vsuo0jkWy4jQXYQAqVGgJEvHWWDAJFv2QwFGUIIlBgBxr3EvyUGufjqiXyLx4pKEgIVjwBJ3/IZQiLf8hkLsoQQKC0CBcJ8S9sg1b4cAkS+dH0QAlsFAb7IglZVlMtwE/mWy0iQHYRAyREgh2/JIV5FA0S+qwCLihICFY0AOXzLaviIfMtqOMgYQqC0CBRK71DaFqn2pRAg8qVrgxDYSgiw3A7k9i2LESfyLYthICMIgXVAgGTvOoBcfBNEvsVjRSUJAUKAEFgzBIh81wxKqogQKHMEKJ1kWQ0QkW9ZDQcZQwiUEAHkdqCAhxLiu8qqiXxXCRgVJwQqFgGe1MyAXxXbg01lOJHvphpO6gwhsAwCBgNJ3zK6QIh8y2gwyBRCoMQI6NOkeksMcfHVE/kWjxWVJAQqHQHy+ZbRCBL5ltFgkCmEQIkRwPIKkr4lxrjo6ol8i4aKChICFY4AT2pGy9vKZRSJfMtlJMgOQqDUCKRS6RSRb6lRLrp+It+ioaKChECFI5Bm3EspfctlFIl8y2UkyA5CYB0QyM6rQy6IdYB8ySaIfDcSfWqbEFhfBHJm22jybX3hz26NyHcj0ae2CYH1RACBZlhmQRsYryfmy7RF5FsmA0FmEAIlRwDr2wxY5VbydqiBohAg8i0KJipECGwCBFhiHZbagei3LAaTyLcshoGMIATWBwEDY186ygIBIt+yGAYyghBYBwSY8iWf7zoAXVwTRL7F4USlCIHKR4A5HcjnWzbjSORbNkNBhhACpUQA3gbu8jWQz7eUMK+ibiLfVYBFRQmBikaA8W+W8qVFFhs5nkS+G4k+tU0IrBsCINoU8urIjeNpA/l1A37Jhoh8N34MyAJCoKQIxGKxYCgUCIaCoXAkFl/0B+cX/QuL/ngiUdJ2qfLlEdCnUinCiBAgBDYxAv33H1y5dnt+ITA1Mzs6PtHUWO/zul1Ox7knTjfUVdPOQhs19ES+G4U8tUsIrBMCl67e+K3f/Z+XrtxESkl4HeB7SOnSZ08c/fu/+PNtLU205GKdhiGvGXI7bBTy1C4hsE4I7N6x7eihfV63Q5dOgnv1+nSV1/PSD5xrqK8h5l2nMSjUDJHvBoJPTRMC64GA2Ww6c+Jod2cbX9vGUvqeePzQ7h19VotlPZqnNpZAgMiXLg1CYPMj0NvddfTwQZ/Pgxme2tqaZ586U1tdtfm7Xd49JPIt7/Eh6wiBtUDAZDI9dfbk9m3dRpMRKnjnth6LxbwWFVMdj44Ake+jY0dnEgKVggB8u10dbWdPHtu5vefMicdrq32VYvkmtpOiHTbx4FLXKgcBtvwhjWyPfGd3ts9aKY7R8ckr12/u37OzsaFOtLRmh2o66wWONa18zawsr4qIfMtrPMiaLYWAYFlEgM0vLo5PzszMzC34F0ORUCIZT6aSbLPLVCqZxOds60vGzDw5A09MJv8xntOzSlS+lltk4j1RBNENehAiawo1hSNhIybgTEa21Jjta8Hy+/JVb2ol3CjxHquc3xAEVYvYCA2vireNelRpcdodXo+nvramsaEWUcSsZoqlWPZqJvLdUl926my5IMB5NTU4PHrtzp2hyYG50GQouRhPBGPJcDwdTenAvEkWkMvIF/SbZkEKBkaWjH8ZqXJmVeWrIETOnyyWVxCnKCHYWVAyp3NBqijDyVeUkUpbEDAryU4R5UD6PAWw+CcqVGpX3jIYDWaL0WozOmwmt8tcW+9p29GzfXtPF2Nhydzlgnz52EHkWz5jQZZsDQTSumg0du3m7Ys3Loz4++cSY8HkTEofsTr0VrvebNEbTIxfFYZkZKm4IcCDUkxmWFfVodJjofCofF/9mNUiCZo7BlRyzSFWTr8KB8sTCvoQVF3L+JmReiKdiOti4XQsZDSnPFXmlgZn797eAwd270RYMfkh8i9uIt+t8YWnXpYHAuC1yamZ//uXX3nz2nfsrfPuBp3NpWc+AM5gjPO4D0GSnmIzX5fGfAHqc3wBOpR8vJyzVZJ4jkM5l6bV9hWyLg46LpelYwJL6OIxfWTRGBp0d9Ue/txnfxhrmk1GY3E1bZVSRL5bZaSpnxuOQCwW/+Dy9d/+0n9P1zz0tCYdTqPZAImrSFYlz26ByTZOzAVJModr892smdqEoJX/ssHI+HKlC0J1Q6inrzSDJpW0Uj1zKeOteDQVmjYG7tV97lM/e/zwYw67XWk44+vY8HHZKAOIfDcKeWp3ayEQCAS/+NWvfffql2u2z1tdKYOJz2Wl+X6WTC9mfKkqLkuFPGTxIJtSY+4InLUUP6r1LB9FkXN6VutLmZI9hjxkI6PaRQJLHOFAeuqK68n9n/2rL33C43YplhZX6ea9TIh8N+/YUs/KBoH5+cX//od/eCf63druJByijC+5e0EJNliWO5fshdSrwoO7vFN1Rf7NaN+s5jI+EG0LOa+zz5BhF4LoefwcC7iIRVMLt62dzmd++Wd/yutxl83IbKQhRL4biT61vRUQmF9Y/K3P/8Fg4rXqrrjRmE7pU9KvK2MR2OTacsI1F6Ns94P4awnvANPWysdiFk1bVnvWEuSrtJ1LvRkngyhRyLmhTvDx/ul1yUQyPOBsMj7ziz/zk1z/bvWDVrht9SuA+l9SBILB0P/40z/tD79a3ZUwmficFPc3KHFiq2FdjaHSUaEJdchRvtyRkeeHyNm6WHg7MqWW9gNoaxIm556rGKeKeOlMEeWY/8FkNjq6gyORV/7vV74VCkVKCntFVE7kWxHDREZWJALQet9/6/x7D19u7IuboHl1cuMCHhSQ0ZrL+j5zCDRfoYqpLU5vGU2c4dSlHMESULb8QuVRpfIVzhGnKoXyC2diMrSfsWg0o9Ho2L741fN/eHfgvmYfjaw7QEWO9CMZTeT7SLDRSYRAEQiMjU/86bf+pGlXzGQyiLXDyo9KX4ryzaUwrbDU6ltJepyvJWcpr1U6Z4SaWTfBSjG9LY48ope8rSxoUwWsUv1yxJjh39y1bJkgYKnx+SI7ZpfJaOo+mfq1f/eP/X5/FokXgecmK0Lku8kGlLpTLggkEslvvfaqtWnC5hLTa/kCdynmze9CIQrk72Vka8aDgMZUZc2ayMy2KRUr1mQoP8e45e4FWdZpCuZq9JwFeMpCurTOaE827459+esvR2MxjUXlMnDrZgeR77pBTQ1tLQTGJybP33jV15Jiq3vVpRMCA43vVdWkq0RH0nnWg72mClUOq4uB1Q81XMzmxPgPc4lgJpBNBUreXsL1UODtjLMjz8msKm7F0c1uBax9V0f8z77zhUAgoK6EXmX3N0NxIt/NMIrUh3JDAA7OD69eTjjGsWg4Q6/cA6CspZAmF+VfVbuXVzpDssjUYNCZDCajwYhMN0Yd++EP+4zseQCu8EZoso7xl/hnTBtOdn/sTPenLQYzS/iwTPBFYf/00vpXNKDhZ2GL3pau6Yl++/W3YvE479yyfu9yG901sodCzdYISKqGENAggK3a//3v/78z9jc8jcYUZOVSR4GIBKmNC5+RYTlNTh3uWkC2nf2tZ872/hCENkvDk0pNLj78xpX/uRibx3aZUuBymuPilq8/k6yXTieSP/fUf/KYvb/95i/HkgmczqcG8xJbLseQ2UFsGjrNWfomMlWgdDyom3i/6/f/9X9wOUXY2ZbjX1K+xBmEwNojsOgPDM88tHuMq8zMu/TDfo7XN18C6w0Oi89rb9KnLcFwOByNBiKheCrO8vJwGoX7A6s7uBOEUx3PV4bfCXBvConLLCasdmakvLQWX0mlZ33O/8iNB1ZYFgaZ7LpQ7GEwFNbcGNZ+IMq5RiLfch4dsq1SEUD2nEhi0WSRCyhWYi21m4IYleKCcFc4WZGcbI0xuD717uC3P3/+n33+3V//2vX/EYoFkD7CZfbhI7fF2+XbXW1t0qEYi3/QG4ymNs+2Xu8eu94OmjToTSxx8PIKtOieKAI+43EQr2SfeOyHrzl59fZdzEyu2MlKvQ6WtZvId1MOK3VqgxGYW1zQWxMsbc4jP1EXwblqJ2VZ5t8AfSYMxjRPlGbA3wfbz/3tJ3/zZ4/+o19+4r/9zMl//UtP/tbuxscNRrPd4viJo//0507/u585+2/+8Sf+d5Or1aCHhwQ+B3UW7iNjqLlzqGHIwunBaVjvaTJfvXV7ObfMRzahnCsg8i3n0SHbKhWBWCKaNiIbOmOybF+m5q8l6TVDUAX6n6+FeRs8YXrKZDA/vf2zf+/p3/3lJ//r0Z7noW2tJpbg3Gat/csbv/PWw7+A3j3V+0mDUX+446nu6t3T/uHPv/Xr7z78lsmAbeT1SWQP5scKHtgClmvn1LKt1sYAS/UrFpnorS7D+Mw4T+++5Ry+wIjIt1K/3mR3OSNgMBg4JebQqHS3Prrly8hh6WNN+UMLY3MPJxfGorEIGM5stMC7e2ns+9fG3nmr/6vB6ALoGBS8o/EYpO7Lt//XoP/2WwP/dzY6g80zsGHRUh7YjNNAfbVEN5aX7Mq9g5UymtP+wPzyudYeHauyP5PIt+yHiAysNARAu04k69WZeZhD/hIH8dAte1VA8q289Vm2+lX+QoxCIpX4YORbv3/+H/ze+V99b/AbaX0SO/zg/XAsnEwkoMeT6STyWKJRu8mNzYr8kQVYG0klkHeXxUhAjS2tQXNZtXj/r6ZHmsA7dj7bn67Sxnet7CXyXSskqR5CIIOAz+01ppwpzCQJnlXZstAcWhb7LMO8yzzZs1Z48IIe+2JYjSazCXuq6ZHIh4Wd4QaQTMXZL+bSBdsl9fpENB5CWHB3zc6UQeezN1RZsZ8xi8HFYrwlQxR4b1Yk5yVCgbOpmv2VTiTSNpt95XvNJr2yiHw36cBStzYOAbBJbXWVy+xNxMR2afxZHr+KkYorC0FGbpLMNQoYLlQDUrOnjUfbXvyl07/9i6f+28+c+LfNvk5QHHcnxMHDKIPZrWQ6btSnPhz8RiIVfWHn5372yD//2SP/wmKwplKJTEaIJdBbUaWynEF5C0lyKhP8ntanouFEW2Mj9mPeuLHayJa3aLc3EnJqewsggHy1HbWdEb9YrctDapft9YqklnV2IfkM3lyIzjyYuT62ODAfmZoLT00HRhLJwGxovH/q4lxoij/ix+/PXBmav6lPGS6PvPZK/59Oh8bd9up3Bv7yytibd6Yuip3i1+ZYVtCK21FgOrVn204D3xx5Cx60wm0LDjp1ufQIpNNf++53vvzBf2vcw4Rn5ll9adeB0LPyKMhcysdqyjAhppXffGEbD7Dgq8iYCwLu3ZQhAbELRYyyPIFD0qgzIChCJPthK+H4kre0LoGd6c16M99onoUi5KSjKAxZfiSHlkgL5G6XTwFABG3e/77pt/7RHzY11GML+9IPSdm1QMq37IaEDNoMCOj1B3bvM0brYpjH0orJjxzvwMBRKC/DWDLaTA9ixVO8kW0/b8SCYyxqgy8Czl/uCYBXAuRqMuiMwhMC+sM7Jr5XvVlvMsFHzGvnrpLiBiGfMznz82pkFZo7iuYeBKdDxGBNt3tdrq3JvECIyLe4i4xKEQKrRKChrnZ3+2Ozo7E0tCfzcirU89H4V/oFNDEUYjc4QZsqqXI/B0IXkFsHv/FgD+WL3/i+s98sqkE4RLg+5sl0mDTmU27sZ/VCNDtGbSnPtagYFht000OJp44/YbaYV4nr5ilO5Lt5xpJ6UlYImE2m5049GxquiiFvoiJ+MxRcSF1mE9hKvcmqKydppZLmV5PBnQlhTMrxpGqZH81+QIK/hfhdqW3N57Kulb0UihJmXK9LGmbvV33i3DMWM8h39VS/CvvKtyiRb/mODVlW2Qjodb1dnU/se3Hijj7J98zU/KyQQmE15KeAtIRa5TQs2E0psSTXaYInxP1iVawoVW3uOWpf2Af8H7CYu2f4zNN/1eP2cP/1o3S3sq8Nbj2R7yYYROpCmSJgNps+8+JLntCOwIgRU11SU6pO0cI5v5bui3ClFvxcrglWP8tjTYV/FeGrkqtWB2tOVysonn+zXQ25Kp47mZkLOq1LzhuTU3teOveMzYo1zVv3IPLdumNPPV8HBGprq37lZ395+qozPJ9O6JC7UWauWaJpKVGX1IIK/2ZEtIhsKFCd4g5Qw8dk+K3KtoVNkMnetT4N4afNXixSqEF+6hLeXuaOxgMAwitCyevfd/zLv/N3PC7nOuBfzk0Q+Zbz6JBtmwGB3u7Of/gL/8/Dt+2xOab7BJFxcuN+0gxxKszLO73Eo7iyN2ZGWBb5zF6ME2HJMsJboP6osW7q8EgjlJQ8WpvEa9TANikK6C9/2/1f/vl/aKyrRfqLzTC6H6EPFOf7EcCjUwmB4hBAMO3Fqzf+1e/9s+ZDizYvNvnBvJfYzliwmuTknEf8bC/u0s//Wgpf1ktQDE8XqABmcmNzDo3GzbzMUuFoT/pa9CmssAsYb75V9Z9/7V91tjWbsMnRlj+IfLf8JUAArAsCYKU79x78i9/6DWf7jKctabTKsC7NHpOKRNTak0V6WfynpTnxgfBJyEJ582+FmFewo8KRmnZzbwNCvGa/m0++uczLK0zB1xDVBYdturn9/+Rv/Y3Ghhoj07xbd55NhZnId12+edQIIcCXHczMzv7RF7/wTv836w/ELU6dyYyk50L+sl0lFXLjbKj8wT9V4MvMuWVzaVZIgWDKTHSDOFlzgrJ9W8G1xBkqzuLvnAqzHSZKFLNkX2El+yMe1UXnUzO3Pc8+/qOf+YFzHo9rWWm+ta4SIt+tNd7U2w1HIBFP3nsw8Jt/9NuTiZsNfXqbM22xGrD3hEj/m2FaDUsJFmSsmJVwTJGeWh7mJeUvDbfmO2FldflwZJhf0dCyTD5Vi62R5S9BvOINbMKZiOhi84bpAWur58jP/8iPdrU1WbbweoqCVx2R74Z/GcmArYhAJBp7MDj0x1/98/sTFz0NMYsvZjAndOaUie35jiXCPMGCzLLA6Ew4iNUnfYXpeCm5lFdlbuZEZnNiilOZnaiRvkqMsULIiuNDw+wZ4perNFTxnUXIcvYPxqRwYBuMJDIKI1ulKTZnjcxXbW/a/4mnz/V0ttltcLLQkYsAkS9dE4TAhiGAvSMnp2f67z5879L7A+P3/KkpgyVstuuMljTPep4S1CqdEGBLlg1HiSzgL0QIgkLPjJOlm0KwpsaRwYQ1r0lsOcT7LPhaLocTwppnnpRkzVwiYkGcwrnKzKBYlMwWKuM3y9aT0CejRn3c6TY39TRvO7zvYG9nq8/rxo0kPzRiw+Aus4aJfMtsQMiczY9AjttTkil2e1/w+/2BwNzC4mIgAGmcSmJnH8a4SDzG+VVSpupVADWynSeY0lV8DUtnZcjwssaFrJ004/Vr/Bpi5TGvULgi+EuWBkflUzSPiDGz2ex1uX1e5NF04QdLJ5a2YvOPbvE9JPItHisqSQisLQKap3vmUlAkbd5SscJBvwWny1ZpYPa8WebkR2NPErmrgp/Id1VwUWFCgBAgBNYGga2+yGRtUKRaCAFCgBBYJQJEvqsEjIoTAoQAIbAWCBD5rgWKVAchQAgQAqtEgMh3lYBRcUKAECAE1gIBIt+1QJHqIAQIAUJglQgQ+a4SMCpOCBAChMBaIEDkuxYoUh2EACFACKwSASLfVQJGxQkBQoAQWAsEiHzXAkWqgxAgBAiBVSJA5LtKwKg4IUAIEAJrgQCR71qgSHUQAoQAIbBKBIh8VwkYFScECAFCYC0QIPJdCxSpDkKAECAEVokAke8qAaPihAAhQAisBQJEvmuBItVBCBAChMAqEfj/AQ2+gtqWEzRzAAAAAElFTkSuQmCC)

3\.01\.04 Future State Process

Approval Matrix Example:

__Sample Approval Matrix__

__Vendor Bills__

Limits

AP Clerk

Accountant

Controller

CFO

Upto $1000

X

 

 

 

Upto $5000

 

X

 

 

Upto $10,000

 

 

X

 

> 10,000

 

 

 

X

__Purchase Orders__

Limits

AP Clerk

Accountant

Controller

CFO

Upto $1000

X

 

 

 

Upto $5000

 

X

 

 

Upto $10,000

 

 

X

 

> 10,000

 

 

 

X

__3\.04\.04 Financial Charges Example__

The following process is the native NetSuite process\.

NetSuite computes the finance charge using the following formula:

> \(Annual Rate / 365\) x age of invoices x amount of outstanding invoices being assessed\.

Age of invoices is counted from Transaction Date or Due Date, depending on your finance charge setup\.

For a customer with multiple overdue invoices subject for assessment, finance charge is computed for each invoice\. The sum of finance charge for each invoice is the total finance charge assessed for that customer\.

Finance Charge Preferences:

> Annual Rate = 12% > Grace Period = 0 > Minimum Finance Charge = 0\.00 > Assess From = Due Date > Assessment Date = July 27, 2021[1](https://suiteanswers.custhelp.com/app/answers/detail/a_id/12664)

Invoice 1:

> Transaction Date = January 1, 2021 > Due Date = February 1, 2021 > Amount = $500\.00[1](https://suiteanswers.custhelp.com/app/answers/detail/a_id/12664)

Invoice 2:

> Transaction Date = March 1, 2021 > Due Date = April 1, 2021 > Amount = $1000\.00[1](https://suiteanswers.custhelp.com/app/answers/detail/a_id/12664)

Finance charge is computed as follows:

> Invoice 1: \(12% / 365\) x 176 days x $500\.00 = $28\.93 >

Invoice 2: \(12% / 365\) x 117 days x $1000\.00 = $38\.47 > Total finance charge = $67\.40

__3\.12\.02__ __Financial periods__

In __NetSuite__, financial periods are used to manage your accounting periods for reporting, posting transactions, and ensuring compliance with your fiscal calendar\. Each financial period has a __status__ that controls what actions can or cannot be performed in that period\. Understanding these statuses is key for accounting and finance teams\. Here’s a detailed breakdown:

__Financial Period Statuses in NetSuite__

NetSuite uses three main types of period status:

__Status__

__Description__

__Effect on Transactions__

__Open__

The period is currently open for posting\.

Transactions \(invoices, bills, journal entries, etc\.\) can be created, edited, or posted\.

__Closed__

The period is completely closed\.

No new transactions can be posted, and existing transactions cannot be edited\. Reports can still be run\.

__Locked__

The period is temporarily restricted for posting or editing\.

In __NetSuite__, financial periods are used to manage your accounting periods for reporting, posting transactions, and ensuring compliance with your fiscal calendar\. Each financial period has a __status__ that controls what actions can or cannot be performed in that period\. Understanding these statuses is key for accounting and finance teams\. Here’s a detailed breakdown:

__Financial Period Statuses in NetSuite__

NetSuite uses __three main types of period status__:

__Status__

__Description__

__Effect on Transactions__

__Open__

The period is currently open for posting\.

Transactions \(invoices, bills, journal entries, etc\.\) can be created, edited, or posted\.

__Closed__

The period is completely closed\.

No new transactions can be posted, and existing transactions cannot be edited\. Reports can still be run\.

__Locked__

The period is temporarily restricted for posting or editing\.

Typically used during reconciliation or review; transactions may be restricted depending on user permissions\. \(Override Period Restrictions Permission\)  and accounting preferences

__Detailed Explanation of NetSuite Period Statuses__

1. __Open__
	- This is the default status when a period is first created for the fiscal calendar\.
	- All posting activities are allowed\.
	- Accounting staff often leave the current period open until month\-end close activities are complete\.
2. __Closed__
	- Once all reconciliations, adjustments, and reporting are done for a period, it is closed\.
	- Closing prevents accidental posting or edits after the period has been finalized\.
	- Period close is usually controlled under __Setup > Accounting > Manage G/L > Close Accounting Period__\.
3. __Locked__
	- Locking is usually temporary and can occur during audits, review, or mass data imports\.
	- Locked periods may allow some limited operations depending on user roles\. \(Override Period Restrictions Permission\) \.and accounting preferences
	- Can be set manually or automatically via workflows or scripts\.

