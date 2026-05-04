# Pivot BRD — CRM

_Source: `CRM/Pivot/4 BRD/03 Pivot Interiors BRD CRM Process Area_v2.0.docx`_

---

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation__

__CRM Process Area__

__                                                                                            Prepared for: Pivot Interiors__

__Version 2\.0__

__Date: February 24, 2026__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

__Jeanine Post \(NetSuite Orion Functional Consultant\)__

# <a id="_Toc887647882"></a><a id="_Toc213932301"></a>__Table of Contents__

[__Table of Contents__	2](#_Toc213932301)

[__1 Version Control__	3](#_Toc213932302)

[__2 Project Definition__	4](#_Toc213932303)

[2\.01 Executive Summary	4](#_Toc213932304)

[2\.02 Company Overview	4](#_Toc213932305)

[2\.03 NetSuite Orion Overview	4](#_Toc213932306)

[2\.04 Project Overview	5](#_Toc213932307)

[2\.05 Document Objectives	5](#_Toc213932308)

[__3 Customer Relationship Management \(CRM\)__	6](#_Toc213932309)

[3\.01 Pipeline Forecasting & Opportunity Management	6](#_Toc213932310)

[3\.02 Complex Buyer Relationship Tracking	7](#_Toc213932311)

[3\.03 Construction Solutions Cross\-Sell Management	8](#_Toc213932312)

[3\.04 RFP Opportunity Management	10](#_Toc213932313)

[3\.05 Gross Profit Tracking & Margin Discipline	11](#_Toc213932314)

[3\.06 Sales Organization Hierarchy & Territory Reporting	12](#_Toc213932315)

[3\.07 Annual Goals & Pipeline Multiplier Tracking	13](#_Toc213932316)

[3\.08 Activity Tracking & Task Management	14](#_Toc213932317)

[__4 SuiteApps__	15](#_Toc213932318)

[4\.01 SuiteApp Summary	15](#_Toc213932319)

[__5 Assumptions__	15](#_Toc213932320)

[__6 Unresolved Requirements__	16](#_Toc213932321)

[__7 Signatures__	17](#_Toc213932322)

# <a id="_heading=h.30j0zll"></a><a id="_heading=h.1fob9te"></a><a id="_Toc360701688"></a><a id="_Toc213932302"></a>__1 Version Control__

__Version__

__Author__

__Comments__

__Date__

0\.1

Jeanine Post

Initial Draft

11/07/2025

0\.2

Marcus Dallacqua

Updated Draft

11/13/2025

1\.0

Debbie Herbert, Chris Trumble

Final Draft

11/13/2025

2\.0

Debbie Herbert, Chris Trumble

Version ready for signoff

02/24/2026

# <a id="_heading=h.2et92p0"></a>

# <a id="_heading=h.tyjcwt"></a>

# <a id="_Toc2044109163"></a><a id="_Toc213932303"></a>__2 Project Definition__

## <a id="_Toc693253150"></a><a id="_Toc213932304"></a>__2\.01 Executive Summary__

Pivot Interiors operates a complex, relationship\-driven sales organization spanning Enterprise, Venture, Public, and Construction Solutions segments across California\. The company currently relies on HubSpot for pipeline forecasting and opportunity tracking while NetSuite handles downstream quoting, ordering, and financial processes\. Manual forecasting, fragmented stakeholder visibility, and disconnected analytics limit leadership's ability to manage pipeline health, cross\-sell opportunities, and margin discipline in real time\. 

The NetSuite Orion CRM solution consolidates opportunity management, activity tracking, goal management, and analytics into a single platform tightly integrated with downstream quoting and invoicing\. The implementation replaces manual Excel\-based forecasting, unifies stakeholder relationship intelligence, introduces automated cross\-sell alerts, and delivers real\-time dashboards for leadership\. The Align/Adapt/Accommodate decisions captured in this document demonstrate that Pivot's critical CRM requirements are met largely through NetSuite Orion functionality, with targeted process adaptations to maximize value\.

## <a id="_Toc2052208158"></a><a id="_Toc213932305"></a>__2\.02 Company Overview__

Pivot Interiors is a MillerKnoll Certified dealer headquartered in the San Francisco Bay Area with offices and design centers throughout California\. The organization delivers workplace strategy, design, and installation services for clients ranging from high\-growth ventures to public institutions\. Pivot's sales organization is structured hierarchically, with executive leadership overseeing regional SVPs/GMs, sales operations, and individual designers/reps\. The business depends on orchestrating complex buying committees that include clients, general contractors, architects, designers, brokers, and project managers\. 

[https://www\.pivotinteriors\.com](https://www.pivotinteriors.com)

## <a id="_Toc1593108613"></a><a id="_Toc213932306"></a>__2\.03 NetSuite Orion Overview__<a id="_Toc710028221"></a>

NetSuite Orion is an industry\-specific configuration of NetSuite tailored for contract furniture dealers\. It unifies CRM, quoting, project execution, procurement, and financial management on a single cloud platform\. CRM capabilities include opportunity management with custom stages and probabilities, multi\-company relationship tracking, activity and task management, goal tracking, and robust analytics\. Native integration with NetSuite ERP ensures that quote, order, and invoice data feed directly back into CRM dashboards for real\-time visibility\. NetSuite Orion's workflow engine and saved search analytics enable low\-code automation and executive\-ready reporting without extensive customization\.

## <a id="_Toc213932307"></a>__2\.04 Project Overview__

Pivot Interiors' engagement with GSI focuses on creating and implementing business requirements aligned with current operations and future growth\. The project methodology follows five stages:

- __D__iscover: Evaluate the dealer’s business processes with NetSuite Orion capabilities
- __R__ealize: Perform initial setup, installation, and configuration of your NetSuite instance
- __E__ducate: Empower your team for success through comprehensive training and user adoption support
- __A__ctualize: Bring your NetSuite and Orion solution to life with seamless data migration and go\-live support
- __M__aximize: Support and expand your operations with dedicated ongoing assistance and strategic customizations\.

Our implementation approach is “Align, Adapt, Accommodate\.”

- Align – Existing processes fit in NetSuite Orion as is\.
- Adapt – Pivot Interiors will change its processes to fit in NetSuite Orion as is\.
- Accommodate – GSI will create a configuration specific to Pivot Interiors, or if the feature can benefit others, will update the code base to make the feature standard\.

This CRM BRD documents the solution alignment outcomes from the Discover phase and provides the roadmap for configuration during Realize\.

## <a id="_Toc451684085"></a><a id="_Toc213932308"></a>__2\.05 Document Objectives__

This document summarizes the CRM business requirements validated during discovery workshops and maps them to NetSuite Orion capabilities\. It captures current state challenges, target\-state processes, Align/Adapt decisions, risks, assumptions, and open items\. Once approved, the BRD serves as the blueprint for configuration, testing, and training activities in subsequent phases\. The Statement of Work continues to define contractual scope; this document describes how the agreed scope will be executed in NetSuite Orion\. 

# <a id="_Toc710078099"></a><a id="_Toc213932309"></a>__3 Customer Relationship Management \(CRM\)__

## <a id="_Toc2081811543"></a><a id="_Toc213932310"></a>__3\.01 Pipeline Forecasting & Opportunity Management__

3\.01\.01 Your Business Requirements

__REQ\-3\.01\.01: __Four\-stage pipeline \(Analysis 25%, Qualified 50%, Quote 80%, Closing 95%, Win/Loss\) with real\-time weighted forecasting\.  Percentages should be able to be changed by user with Role which has that permission\. Last status should be Win or Loss\.  Capture whether or not this is for RFP\.

__REQ\-3\.01\.02:__ Quick opportunity and quick lead entry forms with minimal required fields and mobile support\. Should track notes, columns, data that someone in the field would gather\.

3\.01\.02 Current State Process

HubSpot is the system of record for opportunity management and forecasting\. Sales operations exports the pipeline monthly, applies weighted probabilities in Excel, and produces a pivot table for executive review\. Forecast data is manually fed into downstream leadership reports, delaying insight by days or weeks\. Opportunity and lead creation relies on HubSpot quick forms with minimal required fields, enabling reps to enter deals in under two minutes and progressively enrich data later\. Mobile usability is critical because many reps work from job sites\. 

__3\.01\.03 NetSuite Orion Solution__

NetSuite Orion replaces HubSpot as the CRM system of record, delivering native opportunity management with configurable probability percentages that mirror Pivot's four\-stage methodology\. Weighted pipeline calculations update in real time, driving dashboards and saved searches sliced by division, SVP, and rep\. Quick\-add opportunity and lead forms leverage role\-based defaults and required field logic to match Pivot's "speed first, enrich later" workflow, including full mobile parity through the NetSuite mobile app\. This ensures rapid adoption while improving data quality and governance\. 

3\.01\.04 Future State Process

Sales reps create and update opportunities directly in NetSuite Orion; probabilities drive real\-time weighted forecasts visible to leadership dashboards\. Scheduled integrations deliver up\-to\-date forecast data without manual effort\. Quick\-add forms with field defaults allow reps to capture minimal information upfront and enrich records as deals progress\. Mobile\-ready forms keep pace with field usage\.

3\.01\.05 Decision Matrix

Req \# 

Requirement Name 

Info 

Implementation Approach 

3\.01\.01 

Four\-stage weighted pipeline forecasting 

Opportunity management with configurable stages/probabilities and dashboards 

Align 

3\.01\.02 

Quick lead/opportunity entry forms 

Quick\-add forms, field defaults, mobile app support\.

Align 

__*Client Feedback*__

<a id="_heading=h.1v1yuxt"></a>__*GSI Response*__

<Comment>

## <a id="_Toc249939363"></a>

## <a id="_Toc213932311"></a>__3\.02 Complex Buyer Relationship Tracking__

3\.02\.01 Your Business Requirements

REQ\-3\.02\.01: Multi\-company and multi\-contact association per opportunity with primary/secondary designation\. The actual, multiple contacts should be tied to an opportunity \(this is critical\)\.

REQ\-3\.02\.02: Influencer role tracking with soft reminders for required roles 

3\.02\.02 Current State Process

HubSpot allows only one primary company per opportunity\. Secondary stakeholders like architects, general contractors, and project managers are tracked manually in notes or spreadsheets, limiting visibility into cross\-sell potential\. Influencer data is inconsistently captured because there are no structured reminders, undermining win/loss analysis\. 

3\.02\.03 NetSuite Orion Solution

NetSuite Orion supports multiple company and contact relationships per opportunity using Company Link and Contact Link fields with primary/secondary designations\. Standard Contact Roles and the People Assignment Utility provide structured influencer tracking with configurable role types\. Workflows deliver soft reminders when critical influencer roles are missing, preserving Pivot's quick\-entry philosophy while nudging data completeness\. Dashboards highlight opportunities lacking key influencers for manager follow\-up\. 

3\.02\.04 Future State Process

Reps associate all participating companies and contacts with each opportunity, tagging roles for architects, designers, brokers, and GCs\. Leadership can filter opportunities by company or role to surface cross\-sell trends\. Soft reminders prompt reps to add missing influencers during deal progression, ensuring relationship intelligence is captured\. The workflow for sales reps to select, create and maintain influencer data should be intuitive and capture the source of the connection\.

3\.02\.05 Decision Matrix

__Req \# __

__Requirement Name __

__Info __

__Implementation Approach __

__3\.02\.01 __

Multi\-company/multi\-contact tracking 

Company Link, Contact Link, People Assignment Utility 

__Align __

__3\.02\.02 __

Influencer role tracking with reminders 

Contact Roles with dashboard indicators 

__Align __

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc869422981"></a><a id="_Toc213932312"></a>__3\.03 Construction Solutions Cross\-Sell Management__

3\.03\.01 Your Business Requirements

REQ\-3\.03\.01: Divisions \(not only Construction Solutions\) cross\-sell opportunity alert workflow when reps mark opportunities as eligible or vice versa\.

3\.03\.02 Current State Process

Reps identify Construction Solutions’ involvement via a field in HubSpot, but no automated alert notifies the Construction Solutions team\. Nicholas' team relies on manual report monitoring, causing missed revenue opportunities\. 

3\.03\.03 NetSuite Orion Solution

NetSuite Orion workflows trigger immediate notifications \(email and dashboard\) when an opportunity is flagged for Construction Solutions\. The Construction Solutions team receives a real\-time work queue with opportunity details, eliminating manual report checks and ensuring timely engagement\. 

3\.03\.04 Future State Process

Reps mark "Include Construction Solutions?" on opportunities\. Workflows notify Nicholas' team and populate dashboards\. Construction Solutions evaluates scope promptly and collaborates with the originating rep to qualify upsell potential\. 

3\.03\.05 Decision Matrix

Req \# 

Requirement Name 

Info 

Implementation Approach 

3\.03\.01 

Construction Solutions cross\-sell alert workflow 

Workflow automation with email alerts and dashboard portlet 

Adapt 

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc470850147"></a><a id="_Toc213932313"></a>__3\.04 RFP Opportunity Management__

3\.04\.01 Your Business Requirements

REQ\-3\.04\.01: RFP opportunity type with Kanban board and RFP\-specific metrics 

3\.04\.02 Current State Process

RFP tracking occurs in Monday\.com, creating duplicate entry and preventing unified pipeline reporting\. Leadership lacks visibility into RFP workload and win/loss performance alongside standard opportunities\. 

3\.04\.03 NetSuite Orion Solution

NetSuite Orion introduces an RFP opportunity type with custom fields for due dates, budget spend, and status\. Work Boards deliver Kanban\-style visualization similar to Monday\.com, while dashboards unite RFP and standard pipeline metrics in one system\. Saved searches produce workload analytics and win/loss reporting\. 

3\.04\.04 Future State Process

RFP opportunities are created and managed in NetSuite Orion\. The RFP team uses Work Boards for drag\-and\-drop status updates\. Similar to design requests or labor requests\. Leadership reviews unified dashboards for all opportunities, industries, plus RFP\-specific workload metrics for resource planning\. 

3\.04\.05 Decision Matrix

Req \# 

Requirement Name 

Info 

Implementation Approach 

3\.04\.01 

RFP opportunity management 

RFP Type of request record that will have iys own card\-based board Opportunity Type\. Work Boards, saved searches, dashboards for both\.

Accommodate 

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc1020306769"></a><a id="_Toc213932314"></a>__3\.05 Gross Profit Tracking & Margin Discipline__

3\.05\.01 Your Business Requirements

REQ\-3\.05\.01: Target GP %, MillerKnoll mix tracking, and margin erosion reporting from quote to invoice 

3\.05\.02 Current State Process

Target GP is set manually at opportunity creation, while quote and invoice GP live in D365\. Finance compiles margin reports manually after deals close, offering no mid\-deal visibility\. 

Currently, HubSpot does not capture GP\. Only the deal amount is entered at the opportunity stage\. No gross profit fields or margin calculations are being tracked within HubSpot today\.

3\.05\.03 NetSuite Orion Solution

NetSuite Orion captures Target GP % and MillerKnoll mix fields directly on opportunities\. Saved search\(es\) can compute forecast, quote and invoice GP, enabling dashboards that highlight erosion between stages\. Leadership gains real\-time insight to coach reps before margins deteriorate\. 

3\.05\.04 Future State Process

Reps enter Target GP and MillerKnoll mix on opportunities\. Integration populates quote and invoice GP as the deal progresses\. Dashboards surface erosion trends, enabling proactive interventions and strategic vendor mix analysis\. Approval workflow for low margins is required\.

Margin erosion is tracked through the budget vs actuals table on the project record and sharpens as additional transactions are actualized\.

3\.05\.05 Decision Matrix

Req \# 

Requirement Name 

Info 

Implementation Approach 

3\.05\.01 

Margin discipline tracking 

Opportunity custom fields, D365 quote/invoice sync, erosion dashboards 

Adapt 

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc1300560704"></a><a id="_Toc213932315"></a>__3\.06 Sales Organization Hierarchy & Territory Reporting__

3\.06\.01 Your Business Requirements

__REQ\-3\.06\.01:__ Sales org hierarchy and territory reporting by division/SVP/rep\.  It is critical to track internal referrals from furniture to CS for reporting and referral compensation purposes – this should be a drop down as an optional field\.

3\.06\.02 Current State Process

Hierarchy\-based reporting is maintained manually in PowerBI and PowerPoint\. Role\-based access is lacking, and territory changes require manual updates to spreadsheets\. 

3\.06\.03 NetSuite Orion Solution

NetSuite Orion models the employee hierarchy and Sales Locations natively, driving role\-based dashboards and access control\. Reports slice pipeline, forecasts, and activities by hierarchy level without manual manipulation\. Updates to the hierarchy automatically cascade across analytics and security\. 

3\.06\.04 Future State Process

Leadership views dashboards scoped to their teams\. Sales operations updates the hierarchy in NetSuite Orion, and reports adjust automatically\. Territory\-based reporting ensures SVPs and reps see relevant data in real time\. 

3\.06\.05 Decision Matrix

Req \# 

Requirement Name 

Info 

Implementation Approach 

3\.06\.01 

Sales hierarchy and location reporting 

Employee hierarchy, location records, role\-based dashboards 

Align 

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213932316"></a>__3\.07 Annual Goals & Pipeline Multiplier Tracking__

3\.07\.01 Your Business Requirements

REQ\-3\.07\.01: Annual sales goals with 2\.5× pipeline multiplier visibility and coaching indicators 

3\.07\.02 Current State Process

Annual goals live in HubSpot, while the 2\.5× multiplier is calculated manually in 15:5 reviews and PowerBI\. Reps lack real\-time visibility into multiplier status\. 

3\.07\.03 NetSuite Orion Solution

Goal management records store annual order\-book targets per rep\. Calculated fields compute Pipeline ÷ Goal multipliers displayed on rep dashboards with red/yellow/green indicators\. Leadership dashboards aggregate multiplier status for coaching\. 

3\.07\.04 Future State Process

Sales ops loads goals; NetSuite Orion calculates multiplier status continuously\. Reps and leaders monitor dashboards to maintain the 2\.5× pipeline threshold and trigger coaching actions when targets slip\. 

3\.07\.05 Decision Matrix

Req \# 

Requirement Name 

Info 

Implementation Approach 

3\.07\.01 

Pipeline multiplier tracking 

Goal management, calculated fields, dashboard indicators 

Accommodate 

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213932317"></a>__3\.08 Activity Tracking & Task Management__

3\.08\.01 Your Business Requirements

__REQ\-3\.08\.01: __Activity tracking and task management for new and underperforming reps \(flexible enforcement\)__ __

3\.08\.02 Current State Process

Activity logging in HubSpot is enforced manually for new hires and underperformers\. Experienced reps have flexibility, and there is limited visibility into coaching effectiveness\. 

3\.08\.03 NetSuite Orion Solution

NetSuite Orion activities and tasks support selective enforcement via role\-based workflow rules that require logging for designated users while allowing flexibility for experienced reps\. Coaching dashboards summarize activities, tasks, and follow\-ups by rep and manager\. 

Orion’s Outlook Mail Integration \(SuperSync\) lets you log individual emails from Outlook into NetSuite and associate them to existing records, including customers and opportunities \(your “deals”\), plus sales orders and other record types\. It also supports auto\-logging the rest of an email thread after you log the first message, so the full conversation stays tied to the same deal/records\. Emails are saved as native NetSuite message records, with attachments stored in the file cabinet\.

3\.08\.04 Future State Process

Workflow rules enforce activity logging for specific roles or performance tiers\. Managers assign tasks and review activity dashboards during one\-on\-ones\. Experienced reps maintain autonomy while leaders coach new and underperforming reps with objective data\. 

3\.08\.05 Decision Matrix

Req \# 

Requirement Name 

Info 

Implementation Approach 

3\.08\.01 

Selective activity tracking and task management 

Activities, tasks, coaching dashboards 

Align 

__*Client Feedback*__

__*GSI Response*__

<Comment>

# <a id="_Toc1254384440"></a><a id="_Toc213932318"></a>__4 SuiteApps__

## <a id="_Toc802264751"></a><a id="_Toc213932319"></a>__4\.01 SuiteApp Summary__

1. HubSpot Integration: Bi\-directional sync for lead capture, marketing campaign membership, and opportunity creation\. 
2. Microsoft 365 \(Outlook/Teams\) Integration: Activity capture and calendar synchronization for sales teams\. 

<a id="_heading=h.3ob7dgy"></a>__*Client Feedback*__

<a id="_heading=h.23ghnor"></a>__*GSI Response*__

<Comment>

<a id="_Toc2125619621"></a>

# <a id="_Toc213932320"></a>__5 Assumptions__

The following is a list of assumptions based on the solutions proposed in this document\.

__Document Section __

__Assumptions __

Pipeline Forecasting & Opportunity Management 

• Reps will adopt NetSuite Orion as the single opportunity system of record\.

• Mobile app deployment is included in the rollout plan\. 

Complex Buyer Relationship Tracking 

• Stakeholder role taxonomy \(architect, GC, designer, broker, PM\) will be finalized during configuration workshops\.

• Sales leadership will reinforce data completeness using dashboard indicators\. 

Construction Solutions Cross\-Sell Management 

• "Include Construction Solutions?" field will be standardized across opportunity entry forms\.

• Nicholas' team will manage alert queue through dashboards\. 

RFP Opportunity Management 

• RFP opportunity type and custom fields will be defined during configuration\.

• Monday\.com will be decommissioned for RFP tracking post go\-live\.

Gross Profit Tracking & Margin Discipline 

• D365 integration will provide timely quote/invoice GP data\.

• Reps will consistently enter Target GP and MillerKnoll mix at opportunity creation\. 

Sales Hierarchy & Territory Reporting 

• Employee hierarchy will be maintained by Sales Operations\.

• Territory definitions are approved prior to configuration\. 

Annual Goals & Pipeline Multiplier 

• Annual goal values will be loaded before user acceptance testing\.

• Multiplier status indicators \(red/yellow/green\) thresholds align with leadership expectations\. 

Activity Tracking & Task Management 

• Role\-based workflow rules will be defined for "New Rep" and "Underperformer" segments\.

• Managers will review activity dashboards during 1:1 coaching sessions\. 

<a id="_heading=h.spk1rgn9b34d"></a>__*Client Feedback*__

<a id="_heading=h.uwufyw5z0tji"></a>__*GSI Response*__

<Comment>

# <a id="_Toc60857636"></a><a id="_Toc213932321"></a>__6 Unresolved Requirements__

To be populated pending Business Requirements Document review with the Pivot Interiors team\.

__Area__

__Description__

__Impact__

__Proposed Mitigation Strategy__

__Pivot Interiors, Inc\. Feedback__

# <a id="_Toc1886137734"></a><a id="_Toc213932322"></a>__7 Signatures__

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

