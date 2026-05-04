# Pivot BRD — Marketing

_Source: `Marketing/Pivot/4 BRD/02_Pivot Interiors BRD Marketing Process Area_v1.0.docx`_

---

__Business Requirements Document \(BRD\)__

__for NetSuite Orion Implementation__

__Marketing Process Area__

__Prepared for: Pivot Interiors, Inc\.__

__Version 1\.0__

__Date: November 7, 2025__

__Prepared by:__

__Marcus Dallacqua \(Contract Furniture SME and Functional Consultant\)__

__Chris Trumble \(Contract Furniture SME and Functional Consultant\)__

__Debbie Herbert \(NetSuite Orion Project Manager\)__

__Jeanine Post \(NetSuite Orion Functional Consultant\)__

# <a id="_Toc213407335"></a>__Table of Contents__

[__Table of Contents__	2](#_Toc213407335)

[__1 Version Control__	3](#_Toc213407336)

[__2 Project Definition__	4](#_Toc213407337)

[2\.01 Executive Summary	4](#_Toc213407338)

[2\.02 Company Overview	4](#_Toc213407339)

[2\.03 NetSuite Orion Overview	5](#_Toc213407340)

[2\.04 Project Overview	5](#_Toc213407341)

[2\.05 Document Objectives	5](#_Toc213407342)

[__3 Marketing__	7](#_Toc213407343)

[3\.01 Campaign Management & Orchestration	7](#_Toc213407344)

[3\.02 Event Management & ROI Tracking	9](#_Toc213407345)

[3\.03 Email Marketing & Automation	12](#_Toc213407346)

[3\.04 Lead Management & Nurturing	14](#_Toc213407347)

[3\.05 Marketing Analytics & Attribution	17](#_Toc213407348)

[__4 SuiteApps__	21](#_Toc213407349)

[4\.01 SuiteApp Summary	21](#_Toc213407350)

[__5 Assumptions__	21](#_Toc213407351)

[__6 Unresolved Requirements__	22](#_Toc213407352)

[__7 Signatures__	24](#_Toc213407353)

# <a id="_heading=h.30j0zll"></a><a id="_heading=h.1fob9te"></a><a id="_Toc213407336"></a>__1 Version Control__

__Version__

__Author__

__Comments__

__Date__

0\.1

Marcus Dallacqua

Initial Draft

10/31/2025

0\.2

Debbie Herbert

Second Draft

11/3/2025

1\.0

Debbie Herbert, Jeanine Post, Chris Trumble

Final Draft

11/7/2025

# <a id="_heading=h.2et92p0"></a>

# <a id="_heading=h.tyjcwt"></a>

# <a id="_Toc213407337"></a>__2 Project Definition__

## <a id="_Toc213407338"></a>__2\.01 Executive Summary__

Pivot Interiors is a California\-based office furniture dealership serving Enterprise, Venture, and Public sector markets\. The organization requires an integrated ERP and CRM platform to consolidate operations, automate marketing and sales processes, and establish comprehensive closed\-loop reporting from lead generation through revenue realization\. 

Currently, Pivot operates with disconnected systems where HubSpot manages marketing and lead capture while NetSuite handles opportunities, quotes, and orders\. This fragmentation creates significant operational challenges including manual data entry, duplicate records, lost lead source attribution, inconsistent event tracking, and inability to measure marketing ROI effectively\. 

The NetSuite Orion solution with HubSpot integration addresses Pivot's requirements for automated lead\-to\-opportunity conversion, comprehensive event management with ROI tracking, email marketing automation, lead nurturing workflows, and marketing attribution analytics\. The implementation will establish seamless data flow between marketing and sales systems while preserving HubSpot's sophisticated marketing capabilities and NetSuite's robust ERP functionality\. 

__Note:__ This document describes intended functionality combining standard NetSuite Orion capabilities with planned configurations and customizations\. Specific implementation details including custom dashboard designs, integration field mapping, and attribution models will be defined during the configuration/technical design phase\. 

## <a id="_Toc213407339"></a>__2\.02 Company Overview__

Pivot Interiors, Inc\. comprises a distinguished team of innovators, creators, and thought leaders dedicated to crafting exceptional interior solutions for businesses of all sizes\. Their designs not only embody your brand but also inspire employees to thrive, create, and collaborate in the workplace\. California\-born and raised, they are proudly headquartered in the Bay Area, serving clients state\-wide\. With offices and Design Centers in Santa Clara, Fremont, San Francisco, Costa Mesa, Los Angeles, and La Mirada, they invite you to explore their spaces and experience the Pivot Interiors difference\. Pivot Interiors is a MillerKnoll Certified Dealer\.

[__https://www\.pivotinteriors\.com__](https://www.pivotinteriors.com/)

## <a id="_Toc213407340"></a>__2\.03 NetSuite Orion Overview__

NetSuite Orion is an industry\-specific ERP platform designed for office furniture dealers, providing comprehensive functionality for project\-based operations, financial management, and sales process automation\. The platform includes native CRM capabilities with opportunity management, contact relationship tracking, activity management, and sales pipeline reporting\. 

For marketing operations, NetSuite Orion provides campaign management \(email, events, direct mail\), lead capture and qualification tools, automated workflow engines for nurturing and follow\-up, email marketing with 120,000 monthly email capacity, and comprehensive analytics connecting marketing activities to revenue outcomes\. The platform's integration capabilities enable seamless connection with HubSpot, preserving sophisticated marketing automation while establishing unified data across the organization\. 

## <a id="_Toc213407341"></a>__2\.04 Project Overview__

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

## <a id="_Toc213407342"></a>__2\.05 Document Objectives__

The purpose of this document is to summarize functional and procedural requirements captured by GSI during the Discover business process mapping phase of the implementation\. 

This Business Requirements Document \(BRD\) documents your goals, the problems you want to solve, and the outcomes you expect\. It is the foundation for the setup of the system, acting as a __roadmap between your business needs and the solution design\.__

This document represents information gathered in meetings held with the Client, which enables the GSI team to map the business requirements to an efficient flow in the NetSuite Orion application\. Once complete, this document will serve as a blueprint for the GSI team to configure the application\. This document does not supersede the Statement of Work\. The Statement of Work determines scope\. 

A series of process mapping discovery sessions, focusing on the key areas of the business, were used as a starting point for this exercise\. This document remains consistent in structure to those discovery sessions as it categorizes the findings into the same key process areas\. The set of business requirements documentation is inclusive of all business requirements provided by the Client\.

# <a id="_Toc213407343"></a>__3 Marketing__

## <a id="_Toc213407344"></a>__3\.01 Campaign Management & Orchestration__

3\.01\.01 Your Business Requirements

__REQ\-3\.01\.01:__ Campaign management connecting marketing activities to pipeline and revenue

__REQ\-3\.01\.02:__ Email marketing campaigns with professional templates

__REQ\-3\.01\.03:__ Event campaigns \(Pivotal Insights events, A&D events, showroom tours\)

__REQ\-3\.01\.04:__ Campaign cost tracking and ROI measurement

__REQ\-3\.01\.05:__ Multi\-location campaign coordination across California operations

__REQ\-3\.01\.06:__ Campaign performance analytics with source attribution

3\.01\.02 Current State Process

Pivot currently uses HubSpot for marketing campaign management with limited integration to financial and sales data\. Marketing activities include:

- Email marketing campaigns \(currently paused due to opt\-in limitations \- only 3,400 marketable contacts from 20,000 total records\)
- Social media content marketing on LinkedIn and Instagram
- Showroom events including Pivotal Insights and A&D events
- Website lead capture forms

__Pain Points:__ Campaign data exists separately from opportunity and revenue data, preventing accurate ROI calculation\. Marketing team cannot demonstrate which campaigns influence pipeline or closed deals\. Event attendee tracking is manual using Excel spreadsheets, creating duplicate records when manually entered into HubSpot\. No systematic process connects marketing spend to influenced revenue\.

3\.01\.03 NetSuite Orion Solution

NetSuite Orion provides unified campaign management consolidating marketing operations into the company\-wide platform, eliminating data silos\. The solution delivers critical benefits by connecting marketing directly to sales and financial data within a single database\.

__Campaign Creation:__ The platform provides standard templates and forms for email, event, and nurture campaigns\. While less flexible than HubSpot's drag\-and\-drop builder, it delivers essential functionality with the advantage of native integration to opportunity and revenue data\.

__Email Marketing:__ NetSuite includes 120,000 monthly email capacity, sufficient for Pivot's regional marketing needs\. AI\-assisted template creation enables the marketing team to develop professional email templates using frontier AI tools \(Claude, ChatGPT, Gemini\), then importing the HTML into NetSuite\.

__Primary Value:__ Complete visibility across the customer lifecycle\. Unlike the current state where marketing data lives separately from sales opportunities, NetSuite Orion maintains all interactions in a unified database\. This enables true ROI calculation by connecting campaign costs to influenced pipeline and closed revenue \- impossible with disconnected systems\. Marketing teams can access real\-time data ensuring consistent messaging and coordinated campaigns\.

3\.01\.04 Future State Process

Marketing campaigns will be created in NetSuite with defined budgets, expected costs, and revenue targets\. Campaign members \(leads, contacts, opportunities\) are automatically tracked through the sales cycle\. When opportunities close, the system automatically calculates campaign\-influenced revenue and ROI\.

The marketing team will leverage HubSpot for sophisticated campaign execution while NetSuite serves as the system of record for campaign tracking and financial performance\. Integration ensures campaign member status flows from HubSpot to NetSuite, maintaining complete attribution throughout the sales process\.

 

*​​*

3\.01\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__3\.01\.01__

Unified campaign management

Native campaign module with opportunity linkage

Align \- Configure standard campaign types

__3\.01\.02__

Email marketing campaigns

120,000 monthly emails, template management

Adapt \- Create initial set of custom templates with AI assistance

__3\.01\.03__

Event campaigns

Event campaign type with member tracking

Accommodate

__3\.01\.04__

Campaign cost tracking

Expected cost and actual cost fields on campaigns

Align \- Use standard cost tracking fields

__3\.01\.05__

Multi\-location coordination

Shared campaign database accessible to all locations

Align \- Use standard multi\-subsidiary access

__3\.01\.06__

Campaign performance analytics

Campaign ROI reports with source attribution

Align \- Use standard campaign reports plus custom dashboards

<a id="_heading=h.3fwokq0"></a>__*Client Feedback*__

<a id="_heading=h.1v1yuxt"></a>__*GSI Response*__

<Comment>

## <a id="_Toc213407345"></a>__3\.02 Event Management & ROI Tracking__

3\.02\.01 Your Business Requirements

__REQ\-3\.02\.01__: Comprehensive event management from invitation through post\-event nurturing

__REQ\-3\.02\.02:__ Automated attendee tracking with badge generation and QR code scanning

__REQ\-3\.02\.03:__ Elimination of duplicate records from manual data entry

__REQ\-3\.02\.04:__ Event cost tracking with approval workflows \(sales leader approval required\)

__REQ\-3\.02\.05:__ Post\-event automated follow\-up sequences

__REQ\-3\.02\.06:__ Event ROI measurement comparing costs to influenced pipeline and revenue

__REQ\-3\.02\.07:__ Event types: Pivotal Insights events, A&D events, showroom tours, MillerKnoll events

3\.02\.02 Current State Process

Event management is currently manual and fragmented:

- Invitation lists created in Excel spreadsheets
- Some events use Eventbrite for check\-in, but data must be exported to Excel
- Manual badge creation and attendee information capture
- Yuridia Silvas \(Sales Operations\) tracks attendance in Excel
- Manual entry into HubSpot creates duplicate records
- No centralized visibility into event costs or ROI
- Inconsistent follow\-up with event attendees
- Individual sales reps handle post\-event outreach manually

__Key Stakeholders:__ Lisa Wuller \(Marketing \- event coordination and support\), Yuridia Silvas \(Sales Operations \- current manual tracking\), Roy Stark \(SVP Sales \- interested in ROI measurement\), Prity Lee \(Marketing Director \- overall event strategy\)\.

3\.02\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive event management connecting attendance directly to revenue within a single system\. The solution includes event registration capabilities that capture attendee information through email\-based registration forms, automatically updating the CRM without manual data entry\.

__Custom Attendance Tracking Dashboard:__ GSI will develop a user\-friendly custom dashboard for real\-time attendance monitoring during events\. Event staff will be able to mark attendees as present, add walk\-in guests, and track no\-shows through the dashboard\. All attendance data will immediately update contact records and campaign membership, providing instant visibility without manual data transfer\. This custom solution addresses Pivot's specific need to eliminate Excel\-based tracking\.

__Badge Generation:__ The system can generate attendee badges with QR codes enabling quick check\-in and contact information capture\. Marcus confirmed this capability during discovery: "You can use NetSuite to generate those badges\.\.\. have a little tool that'll generate the content that goes on the badge and then even a QR code that's on the badge\." This eliminates manual spreadsheet management and reduces duplicate record creation\.

__Approval Workflows:__ Purchase requisition functionality will be configured to link event costs to approval processes, ensuring sales leader approval before events proceed\. This addresses the current requirement for cost center validation documented in the follow\-up session\.

__Automated Follow\-up:__ NetSuite's workflow engine will be configured to automatically trigger post\-event email sequences, ensuring consistent follow\-up within 48 hours of event completion\. Marcus shared his experience creating 12\-week automated nurturing campaigns using workflow automation, demonstrating this capability for event follow\-up scenarios\.

__ROI Analytics:__ The platform's standard campaign functionality automatically calculates event ROI by comparing event costs \(venue, catering, staff time, materials\) against influenced pipeline and closed revenue\. This provides the visibility Prity and Roy need to justify event investments to leadership\.

3\.02\.04 Future State Process

1. Marketing creates event campaign in NetSuite with budget and expected outcomes
2. System generates registration forms and invitation emails
3. Registrants automatically added to event campaign as members
4. Event staff uses attendance dashboard during event to mark attendees
5. System automatically updates contact records and campaign membership
6. Automated post\-event workflow sends follow\-up emails within 48 hours
7. Event costs recorded and linked to campaign for ROI tracking
8. As influenced opportunities close, system calculates event ROI
9. Marketing reviews event performance dashboard to optimize future events

3\.02\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__3\.02\.01__

Comprehensive event management

Event campaigns with registration and member tracking

Accommodate \- GSI will develop custom attendance tracking dashboard

__3\.02\.02__

Automated attendee tracking

Custom dashboard with real\-time check\-in capability

Accommodate \- GSI will build custom dashboard with badge generation capability

__3\.02\.03__

Duplicate prevention

Duplicate detection and merge functionality

Align \- Configure duplicate detection rules

__3\.02\.04__

Event cost approval workflows

Purchase requisition with approval routing

Adapt \- Configure approval workflow for event costs

__3\.02\.05__

Post\-event follow\-up automation

Workflow engine with scheduled email triggers

Adapt \- Build automated post\-event email workflow

__3\.02\.06__

Event ROI measurement

Campaign ROI calculation linking costs to influenced revenue

Align \- Use standard campaign ROI reports

__3\.02\.07__

Multiple event types

Campaign category field for event classification

Align \- Configure event type picklist values

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213407346"></a>__3\.03 Email Marketing & Automation__

3\.03\.01 Your Business Requirements

__REQ\-3\.03\.01:__ Professional email templates aligned with Pivot brand guidelines

__REQ\-3\.03\.02:__ Automated drip campaigns for lead nurturing

__REQ\-3\.03\.03:__ Segmentation and targeting by market segment \(NBD, Venture, Public\)

__REQ\-3\.03\.04:__ Email marketing sufficient for regional needs \(not national scale\)

__REQ\-3\.03\.05:__ Ability for non\-technical marketing staff to create email campaigns

__REQ\-3\.03\.06:__ Email performance tracking \(opens, clicks, conversions\)

3\.03\.02 Current State Process

Email marketing capabilities exist in HubSpot but are currently paused due to significant constraints:

- Only 3,400 marketable contacts from 20,000 total records due to opt\-in restrictions
- Blacklisting concerns have led to pausing email campaigns
- Marketing team using LinkedIn and Instagram as workarounds to reach broader audiences
- Limited templates and manual email creation process

Prity Lee expressed strong preference for WYSIWYG interfaces over database\-style UIs, indicating importance of user\-friendly email creation tools for marketing team adoption\.

3\.03\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive email marketing capabilities enhanced through AI tool training and custom template creation\. The implementation includes creating an initial set of professional, reusable marketing templates customized to Pivot's brand and common use cases \(specific number to be determined during implementation planning\)\. NetSuite's sophisticated workflow automation engine enables complex drip campaigns and behavioral triggers comparable to dedicated marketing platforms\.

__AI\-Assisted Template Creation:__ Chris Trumble will provide training and support documentation for non\-technical marketing users to create email templates using frontier AI tools \(Claude, ChatGPT, Gemini\)\. As Marcus explained in discovery: "Along came AI that allowed us to\.\.\. take a screenshot of something, give it to the AI and tell it to create an email template specific for NetSuite using free marker\.\.\. and the whole thing just became extremely easy\." Marketing staff will prompt AI with brand guidelines and content requirements, then paste the generated HTML into NetSuite\. This approach enables the marketing team to create professional templates without technical coding skills\.

__Email Marketing Capacity:__ NetSuite includes 100,000 emails per month \(confirmed by Marcus during discovery\), but limited to 10,00 per blast, sufficient for Pivot's regional marketing needs\. This capacity supports ongoing nurture campaigns, event invitations, and promotional campaigns across all market segments\.

__Workflow Automation:__ NetSuite's workflow engine enables complex drip campaigns and behavioral triggers comparable to dedicated marketing platforms\. Workflows can be configured to trigger emails based on lead score changes, form submissions, opportunity stage progression, or time\-based nurturing sequences\. Marcus shared his experience creating 12\-week automated nurturing campaigns using workflow\-based automation\.

__Segmentation:__ Built\-in segmentation allows targeting by market segment \(NBD, Venture, Public\), lead score, engagement level, opportunity stage, or custom criteria\. This ensures relevant messaging reaches appropriate audience segments\.

3\.03\.04 Future State Process

Marketing team uses AI tools to generate email HTML based on campaign objectives and brand guidelines\. Templates are imported into NetSuite and saved for reuse\. Campaign creation involves selecting templates, defining audience segments, scheduling delivery, and configuring automated workflows for drip campaigns\. Performance metrics track opens, clicks, and conversions, automatically linking engaged prospects to opportunities for closed\-loop reporting\.

3\.03\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__3\.03\.01__

Professional email templates

HTML template management with brand consistency

Accommodate \- Create initial set of custom branded templates

__3\.03\.02__

Automated drip campaigns

Workflow engine with scheduled email sequences

Adapt \- Build multi\-step nurture workflows

__3\.03\.03__

Market segment targeting

Saved searches and campaign segmentation

Align \- Create segment\-based saved searches

__3\.03\.04__

Regional email capacity

100,000 monthly email limit

Align \- Standard NetSuite email capacity

__3\.03\.05__

Non\-technical user access

AI\-assisted template creation methodology

Accommodate \- Training on AI template generation tools

__3\.03\.06__

Email performance tracking

Open rate, click rate, and conversion tracking

Align \- Use standard email analytics

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213407347"></a>__3\.04 Lead Management & Nurturing__

3\.04\.01 Your Business Requirements

__REQ\-3\.04\.01:__ Automated lead capture from multiple sources \(website forms, events, referrals\)

__REQ\-3\.04\.02:__ Lead qualification and scoring to prioritize sales follow\-up

__REQ\-3\.04\.03:__ Automated lead routing to appropriate sales representatives

__REQ\-3\.04\.04:__ Lead nurturing workflows for long sales cycles

__REQ\-3\.04\.05:__ Duplicate prevention and management

__REQ\-3\.04\.06:__ Tracking of influencers \(architects, designers, brokers, GCs\)

__REQ\-3\.05\.07:__ Complex relationship management for multiple stakeholders per opportunity

__REQ\-3\.04\.08:__ Lead status tracking through qualification stages

3\.04\.02 Current State Process

Lead capture occurs through multiple channels feeding into HubSpot:

- Website forms \(contact forms, project inquiry, Sandbox booking\)
- Internal visitor forms for showroom events
- Trade shows and A&D events \(manual data capture\)
- Referrals from clients and partners
- Direct outreach and prospecting

__Current Challenges:__ Sales reps manually create opportunities in NetSuite from HubSpot leads, creating delays and data quality issues\. No automated lead scoring or routing exists\. Lead nurturing is manual with inconsistent follow\-up\. Duplicate records are common, especially from event attendee tracking\. Influencer tracking exists in HubSpot but is not mandatory, leading to incomplete relationship data\.

__Complex Sales Environment:__ "Our buyer technically isn't our client\.\.\. we're selling through the general contractor" \- Nicholas Simmons\. This creates complex stakeholder tracking requirements where the end client, general contractor, architect/designer, and broker may all influence the deal\. Current systems struggle to track these relationships effectively\.

3\.04\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive lead management capabilities<a id="_Hlk211337484"></a>\. The platform enables complex lead nurturing scenarios with multi\-step workflows, conditional branching, and automated task creation\. The solution includes flexible form creation with progressive profiling and sophisticated relationship hierarchies for tracking influencers and end users\.

__Lead Capture & Forms:__ Flexible form creation with progressive profiling allows capturing essential information initially while gathering additional details over time\. Web\-to\-lead forms integrate directly with NetSuite, automatically creating lead records without manual data entry\.

__Lead Qualification:__ Configurable lead statuses enable tracking through stages: Targeting, Unqualified, Qualified, Nurturing\. Additional statuses can be created to match Pivot's specific qualification process\. Lead scoring can be implemented to automatically prioritize hot leads for immediate sales follow\-up \(specific scoring criteria to be defined during implementation\)\.

__Automated Routing:__ Workflow rules will be configured to automatically assign leads to appropriate sales representatives based on geography, market segment \(NBD, Venture, Public\), project size, or other criteria\. This ensures proper lead distribution without manual intervention \(specific routing rules to be defined\)\.

__Nurturing Workflows:__ Marcus Dallacqua shared his experience creating 12\-week email nurturing campaigns with automated workflows: "If I assign a certain status to somebody, they would automatically be opted into that campaign and then they would get those emails\.\.\. , drip marketing emails for the next 12 weeks\." This addresses Roy Stark's comment: "We've been talking about nurturing for five years and haven't found the right tool \- this is great to note this tool will have that capability\." Specific nurture workflow designs will be developed during implementation\.

__Relationship Management:__ NetSuite's sophisticated relationship hierarchies track influencers and end users\. Multiple contacts can be associated with opportunities, each with defined roles \(architect, designer, broker, GC, end client\)\. This addresses the complex buying committee structure where "our buyer technically isn't our client" \(Nicholas Simmons\)\.

__Duplicate Management:__ Built\-in duplicate detection prevents creation of duplicate records during lead import or form submission\. Merge functionality consolidates duplicate records when they occur\.

3\.04\.04 Future State Process

1. Lead captured through website form, event registration, or manual entry
2. System runs duplicate check and either creates new lead or updates existing record
3. Lead scoring algorithm evaluates demographic and behavioral data
4. High\-score leads automatically assigned to sales reps with notification
5. Lower\-score leads enter nurturing workflow for automated follow\-up
6. As leads engage and score increases, they are re\-prioritized for sales outreach
7. When qualified, sales rep converts lead to opportunity with one click
8. Lead source, campaign attribution, and engagement history transfer to opportunity
9. Influencers and multiple stakeholders tracked as related contacts on opportunity

3\.04\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__3\.04\.01__

Automated lead capture

Web form template with direct integration to lead records

Align \- Configure web\-to\-lead forms for website

__3\.04\.02__

Lead qualification and scoring

Custom lead scoring fields and workflow rules

Adapt \- Define and configure lead scoring model \(criteria to be determined\)

__3\.04\.03__

Automated lead routing

Workflow\-based assignment rules

Adapt \- Configure routing rules \(specific criteria to be defined\)

__3\.04\.04__

Lead nurturing workflows

Multi\-step workflow engine with email automation

Adapt \- Create 12\-week nurturing campaigns by segment

__3\.04\.05__

Duplicate prevention

Duplicate detection on lead creation and import

Align \- Configure duplicate detection rules

__3\.04\.06__

Influencer tracking

Related contact records with role definitions

Align \- Use contact relationship management

__3\.04\.07__

Multiple stakeholder management

Multiple contacts per opportunity with defined roles

Align \- Configure contact roles on opportunities

__3\.04\.08__

Lead status tracking

Configurable lead status field with reporting

Adapt \- Define custom statuses \(Targeting, Qualified, Nurturing\)

__*Client Feedback*__

__*GSI Response*__

<Comment>

## <a id="_Toc213407348"></a>__3\.05 Marketing Analytics & Attribution__

3\.05\.01 Your Business Requirements

__REQ\-3\.05\.01:__ Closed\-loop reporting from lead source through closed revenue

__REQ\-3\.05\.02:__ Marketing ROI measurement by campaign and channel

__REQ\-3\.05\.03:__ Pipeline reporting showing marketing\-influenced opportunities

__REQ\-3\.05\.04:__ Campaign performance dashboards for optimization decisions

__REQ\-3\.05\.05:__ Attribution reporting across complex buying committees

__REQ\-3\.05\.06:__ Segment\-specific performance analysis \(NBD, Venture, Public\)

__REQ\-3\.05\.07:__ Event ROI tracking comparing costs to influenced revenue

__REQ\-3\.05\.08:__ Influencer effectiveness tracking

3\.05\.02 Current State Process

Current reporting capabilities are severely limited by disconnected systems:

- HubSpot contains marketing metrics \(form conversions, email performance\)
- NetSuite contains opportunity and revenue data
- No automated connection between lead source and closed revenue
- Yuridia Silvas manually creates forecast reports in Excel
- Kevin creates PowerBI reports combining data from multiple sources
- 80% of HubSpot usage is for pipeline forecasting for adaptive planning
- Cannot see dollar amounts per stage in HubSpot
- No visibility into which marketing activities drive revenue

__Deal Stages with Weighted Percentages:__

- Analysis/Introductory: 25%
- Qualified: 50%
- Quotation: 80%
- Closing: 95%

Sales segments tracked: New Business Development, Venture, Public, Construction Solutions\. Current manual Excel forecasts track: Top Opportunity flag, MK Opportunity flag, Herman Miller %, Construction Solutions involvement, and MTRL inclusion indicators\.

3\.05\.03 NetSuite Orion Solution

NetSuite Orion provides comprehensive marketing analytics with sophisticated attribution capabilities specifically designed for complex B2B scenarios\. To accommodate Pivot's unique influencer marketing model, we will modify the order team assignment utilities to enable sophisticated attribution reporting\. This custom approach allows assigning influence percentages to different contributors on opportunities, providing granular visibility into how various influencer relationships drive revenue\.

__Closed\-Loop Reporting:__ The unified database automatically tracks leads from original source through opportunity creation to closed deal\. Marketing can report on leads generated, opportunities influenced, and revenue closed by campaign, channel, or time period\. This visibility enables data\-driven budget allocation and campaign optimization\.

__Custom Attribution Solution:__ To accommodate Pivot's unique influencer marketing model where architects, designers, brokers, and contractors influence deals, GSI will develop a custom attribution solution by modifying the order team assignment utilities\. This customization will allow assigning influence percentages to different contributors on opportunities, providing granular visibility into how various influencer relationships drive revenue\. This is a planned custom development \(Accommodate approach\) rather than standard functionality\.

__Dashboards & Reports:__ Real\-time dashboards will be configured to display key marketing metrics including lead volume by source, conversion rates by campaign, pipeline by source, and marketing\-influenced revenue\. Segment\-specific dashboards will show performance variations across NBD, Venture, and Public markets\. Event ROI dashboards will compare event costs to influenced pipeline and revenue\. Dashboard designs will be developed during the implementation phase with focus on visual appeal to support marketing team adoption\.

__Forecasting Integration:__ NetSuite's built\-in forecasting capabilities eliminate manual Excel manipulation\. Weighted pipeline reports use stage probabilities \(Analysis 25%, Qualified 50%, Quotation 80%, Closing 95%\) to calculate expected revenue\. Reports can be segmented by sales rep, segment, region, or custom criteria\.

__Competitor & Product Mix Tracking:__ The system tracks competitors on opportunities \(MillerKnoll specifically mentioned\) with percentage estimates\. Product mix indicators \(Herman Miller %, Construction Solutions involvement, MTRL inclusion\) are captured and reportable\. Win/loss analysis reports show performance against specific competitors\.

3\.05\.04 Future State Process

Marketing leadership reviews real\-time dashboards showing campaign performance, lead generation trends, and ROI by channel\. Monthly reports compare marketing investment to influenced pipeline and closed revenue\. Quarterly analysis identifies top\-performing campaigns and channels, informing budget allocation decisions\. Segment\-specific reports show which marketing activities work best for NBD versus Venture versus Public markets\. Event ROI reports justify event investments to leadership\. Attribution reports show how influencer relationships contribute to deal success, guiding relationship investment strategies\.

3\.05\.05 Decision Matrix

__Req \#__

__Requirement Name__

__Info__

__Implementation Approach__

__3\.05\.01__

Closed\-loop reporting

Unified database tracking leads through revenue

Align \- HubSpot integration maintains source attribution

__3\.05\.02__

Marketing ROI measurement

Campaign ROI reports with cost and revenue comparison

Align \- Use standard campaign ROI analytics

__3\.05\.03__

Pipeline reporting

Opportunity reports filtered by campaign membership

Align \- Create saved searches for marketing\-influenced pipeline

__3\.05\.04__

Campaign performance dashboards

Real\-time dashboards with campaign metrics

Accommodate \- Build custom marketing performance dashboards

__3\.05\.05__

Complex attribution reporting

Modified order team assignment for influence percentage

Accommodate \- GSI will develop custom attribution solution using modified order team assignment utilities

__3\.05\.06__

Segment\-specific analysis

Reporting filtered by NBD, Venture, Public segments

Align \- Create segment\-based report filters

__3\.05\.07__

Event ROI tracking

Event campaign costs linked to influenced revenue

Align \- Use campaign ROI reports for events

__3\.05\.08__

Influencer effectiveness tracking

Win/loss analysis by influencer relationships

Accommodate \- GSI will develop custom influencer contribution reports

__*Client Feedback*__

__*GSI Response*__

<Comment>

 

# <a id="_Toc213407349"></a>__4 SuiteApps__

## <a id="_Toc213407350"></a>__4\.01 SuiteApp Summary__

The following SuiteApps or integrations may be considered for the implementation:

- __HubSpot Integration:__ Bi\-directional sync between HubSpot and NetSuite for lead\-to\-opportunity automation
- __SharePoint Integration:__ Document management and version control
- __ZoomInfo \(Under Evaluation\):__ Data enrichment for lead and contact records
- __Event Management Solution:__ Custom attendance tracking dashboard with badge generation

<a id="_heading=h.3ob7dgy"></a>__*Client Feedback*__

<a id="_heading=h.23ghnor"></a>__*GSI Response*__

<Comment>

# <a id="_Toc213407351"></a>__5 Assumptions__

The following is a list of assumptions based on the solutions proposed in this document\.<a id="_heading=h.i80yluglvpw2"></a><a id="_heading=h.d5tidh9kb5f1"></a>

__Document Section__

__Assumptions__

Campaign Management

• HubSpot will remain primary marketing automation platform

• NetSuite will serve as system of record for campaign ROI tracking

• Marketing team will adopt AI\-assisted template creation methodology

Event Management

• Custom attendance tracking dashboard is a planned development, not existing functionality

• Event management solution can be included in Phase 1 without impacting go\-live date

• Sales leader approval workflow is required before events proceed

• Badge generation with QR codes confirmed as standard capability by Marcus during discovery

Email Marketing

• 120,000 monthly emails confirmed as sufficient for Pivot's needs \(verified in discovery\)

• Number of custom email templates to be created will be determined during implementation planning

• Marketing team will be trained on AI\-assisted template creation methodology

Lead Management

• HubSpot\-NetSuite integration specifications will be finalized during technical design phase

• Lead scoring model criteria will be defined during implementation workshops

• Routing rules will be established based on business requirements before go\-live

• Nurture workflow designs will be developed during implementation phase

Analytics

• Historical data migration scope to be determined for trend analysis

• Custom attribution solution is a planned development \(Accommodate approach\), not standard functionality

• Dashboard designs will be created with visual appeal priority to support marketing team adoption

• Specific dashboard layouts and KPIs to be finalized during implementation phase

<a id="_heading=h.spk1rgn9b34d"></a>__*Client Feedback*__

<a id="_heading=h.uwufyw5z0tji"></a>__*GSI Response*__

<Comment>

# <a id="_Toc213407352"></a>__6 Unresolved Requirements__

To be populated pending Business Requirements Document review with the Pivot team\.

__Area__

__Description__

__Impact__

__Proposed Mitigation Strategy__

Lead Scoring

Lead scoring criteria, thresholds, and weighting not defined

Medium \- Affects lead prioritization and routing effectiveness

Schedule workshop with sales and marketing to define comprehensive scoring model including demographic and behavioral factors

Field Mapping

Complete HubSpot to NetSuite field mapping not documented; integration sync rules not defined

High \- Required for integration configuration and data quality

Schedule technical workshop to map all fields, define sync triggers, source of truth rules, and error handling

Nurture Workflows

Specific nurture campaign workflows and content not defined

Medium \- Can be implemented post\-launch

Marketing to prioritize top 3 nurture workflows for initial implementation

Data Migration

Historical data migration scope and approach not finalized

Medium \- Affects reporting and analytics baseline

Determine historical data requirements \(12 months, 24 months, or full history\)

ZoomInfo

Decision pending on data enrichment service

Low \- Nice to have but not required for launch

Evaluate ZoomInfo ROI and make decision before Phase 2

Form Standardization

Online lead forms need standardization across multiple current forms

Medium \- Affects data quality and lead capture consistency

Marketing to define standard form fields and create 2\-3 form templates

Custom Dashboard Design

Attendance tracking dashboard specifications and design not finalized

Medium \- Custom development required for Phase 1 event management

GSI to scope detailed dashboard requirements including check\-in workflow, badge printing integration, and real\-time updates

Attribution Model

Custom attribution solution technical requirements not defined

Medium \- Custom development for influencer tracking ROI

Define attribution model approach, data structure for influence percentages, and reporting requirements

Email Templates

Number and design of email templates to be created not specified

Low \- Can be developed iteratively post\-launch

Marketing to prioritize template needs and provide brand guidelines for initial template set

# <a id="_Toc213407353"></a>__7 Signatures__

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

