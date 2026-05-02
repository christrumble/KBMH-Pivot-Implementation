# Operations Discovery Session - Detailed Questions
**Version**: 1.0  
**Date**: December 2, 2025  
**Process Area**: Operations  
**Status**: Ready for Scheduling

---

## VALIDATION OF PM'S TOPIC LIST

✅ **EXCELLENT** - Your project manager's topic list is comprehensive and covers all 7 critical sessions identified in Gap Analysis.

**Questionnaire Completion Status:**
- Current: 82% complete
- After Session 7 (Scheduling): 93% complete  
- After Sessions 1-6 (Configuration data): 100% complete

**Coverage:** All 34 requirements from Questionnaire_Operations_v1.0.md are addressed across these 7 sessions.

---

## SESSION 1: Receiving & Warehouse Management (60-75 min)

### Attendees
✅ **PM's Suggestion:** Wendy (PM Manager), Warehouse Staff, Operations/Finance, Kipp (IT/Process)  
📝 **Recommendation:** Add Receiving Coordinator (if different from Wendy)

### Pre-Work Required
- [ ] **Operations Team:** Complete list of third-party warehouse locations with addresses **(GAP-007)**
- [ ] **Marcus:** Schedule Advanced Receiving tool demo

### Questions

#### Warehouse Locations & Bin Setup (GAP-007 - HIGH PRIORITY)
1. What is the complete list of all third-party warehouse locations where you receive product?
   - Warehouse name/company
   - Physical address  
   - Primary contact person
   - Any special receiving requirements

2. For bin naming conventions, do you prefer: **(GAP-011)**
   - Simple format: "Location-RCV", "Location-DMG", "Location-DUP"?
   - Or something else?

3. Do any locations need special bin configurations beyond the standard 3 bins (receiving, damaged, duplicate)?

#### Damaged Product Process
4. When a contractor notifies you of damaged product, who at KBM receives that notification?

5. How quickly do you need to know about damaged items? (real-time alert vs. daily report)

#### Training & Adoption
6. Who will be the primary users of the Advanced Receiving tool?

7. Do you want to train contractors on identifying damage during receiving, or keep that KBM-side only?

#### Phase 2 Planning (REQ-008)
8. For future consideration: Which contractors would you trust with direct receiving capability?

9. What would make you comfortable giving contractors direct receiving access?

---

## SESSION 2: Vendor Center Contractor Portal (60 min)

### Attendees
✅ **PM's Suggestion:** Wendy (PM Manager), Rafina (Design Manager), Kipp (IT/Process)  
📝 **Recommendation:** Add Operations Coordinator

### Pre-Work Required
- [ ] **Wendy/Operations:** Contractor access list with contact information **(GAP-006 - HIGH PRIORITY)**
- [ ] **Rafina:** Design contractor time entry access list **(GAP-006 - HIGH PRIORITY)**

### Questions

#### Contractor Access Lists (GAP-006 - HIGH PRIORITY - CRITICAL DATA NEEDED)
1. **List 1 - Vendor Center Portal Access:**
   - Which installation contractors/subcontractors need portal access?
   - For each: Company name, primary contact, email address

2. **List 2 - Time Entry Access:**
   - Which contractors need direct time entry capability?
   - For each: Company name, contact person, who at KBM reconciles their time?

#### Receiving Notification Workflow (REQ-007)
3. When a contractor clicks "Notify of Arrival" in vendor center:
   - Who at KBM should be notified? (individual email, shared inbox, dashboard only?)
   - Should it auto-assign to someone for follow-up?
   - What's the SLA for KBM to process the receiving?

4. What information should contractors provide when notifying of arrival?
   - Just "it's here"?
   - Quantity counts?
   - Damage notes?
   - Photos?

#### Security & Permissions
5. What should contractors be able to SEE in vendor center?
   - Only their own POs and work orders?
   - Project information?
   - Pricing information? (Yes/No - important security question)

6. What should contractors be able to DO?
   - View only?
   - Add notes/comments?
   - Upload documents/photos?
   - Update status on work orders?

#### Adoption Strategy
7. How do you want to roll out vendor center to contractors?
   - Big bang (everyone at once)?
   - Pilot with 1-2 trusted contractors first?
   - Phased by project type?

8. What's your backup plan if contractors don't adopt vendor center?
   - Keep email process running in parallel?
   - For how long?

9. Who will train contractors on vendor center?

---

## SESSION 3: VRA & Damaged Product Management (75 min)

### Attendees
✅ **PM's Suggestion:** Wendy (PM Manager), Rafina (Design Manager), Operations/Finance, Kipp (IT/Process)  
⚠️ **CRITICAL ADDITION:** **Lorraine (CFO)** - Must attend for accounting treatment decision (GAP-005)

### Pre-Work Required
- [ ] **Lorraine/Kipp:** Decision on damaged product accounting treatment **(GAP-005 - HIGH PRIORITY)**
- [ ] **Finance:** Examples of current end-of-month credit reports (if any)

### Questions

#### VRA Process Workflows
1. **Scenario 1: Damaged on arrival, vendor will replace at no charge**
   - Receive 10 items: 8 good (normal bin), 2 damaged (damaged bin)
   - Add zero-cost line for 2 replacements
   - Receive 2 replacements
   - Create VRA (not shipping back)
   - **Question:** Walk through exactly what happens step-by-step. Who does what, when?

2. **Scenario 2: Damaged on arrival, vendor wants product returned**
   - Same initial receiving
   - Create VRA
   - Create item fulfillment to ship back
   - **Question:** Who arranges the return shipment? Who pays freight?

3. **Scenario 3: Product arrives wrong (not damaged, just wrong item)**
   - Do you use VRA process or handle differently?

#### Accounting Treatment (GAP-005 - HIGH PRIORITY - LORRAINE CRITICAL)
4. For the damaged items sitting in damaged bin:
   - When do you write them off?
   - What GL account?
   - What if vendor credit comes in different accounting period than damage occurred?

5. For zero-cost replacement line:
   - How does this affect project GP?
   - Does it show as $0 cost even though replacement has value?
   - How do you reconcile this for project profitability?

#### VRA Approval Workflow
6. Who needs to approve VRAs before they're finalized?

7. Is there a dollar threshold for approval levels?

8. How quickly do VRAs need to be created after discovering damage?

#### Credit Management (REQ-012)
9. For the end-of-month credit report Marcus mentioned:
   - Who should receive this report?
   - What format? (email, dashboard, PDF export?)
   - Should it automatically go to vendors, or just internal?

10. Marcus mentioned creating bill credits with "TBD" as credit memo number:
    - Do you want to use this approach?
    - Who maintains the "expected credits" list?

#### VRA Reporting
11. What reports do you need for VRA management?
    - Open VRAs by age?
    - VRAs by vendor?
    - Expected credit value outstanding?
    - Damaged inventory value in quarantine bins?

---

## SESSION 4: Work Order Management & Soft Scheduling (75 min)

### Attendees
✅ **PM's Suggestion:** Wendy (PM Manager), Rafina (Design Manager), Kipp (IT/Process)  
⚠️ **CRITICAL ADDITION:** **Matt (Leadership)** - For final approval decision (GAP-002)

### Pre-Work Required
- [ ] **Wendy:** Current PM scheduling process documentation
- [ ] **Operations Team:** Finalize work order event type list **(GAP-009)**

### Questions

#### Final Decision (GAP-002 - HIGH PRIORITY - CRITICAL SIGN-OFF NEEDED)
1. **Final confirmation:** Are you implementing work orders? (Wendy gave soft buy-in, need official approval)

2. **If YES:**
   - Who will create work orders in the system?
   - What triggers work order creation? (when PM assigned? when order approved? when product ships?)

3. **If NO:**
   - How will you track field activities?
   - How will field service app work without work orders?

#### Event Types (GAP-009)
4. Confirm this is the complete list of work order event types:
   - Site verification
   - Delivery and install
   - Site review
   - PM on-site presence
   - Design meetings
   - Punch walks
   - **Any others?**

5. Are there different event types for different project phases or order types?

#### Soft Scheduling Workflow (REQ-015)
6. Walk through soft scheduling process:
   - Someone requests scheduling on a PM → **Who can request?**
   - PM must approve → **How? (email notification, dashboard, mobile app?)**
   - Once PM approves → **Does it become "hard scheduled" or stay flexible?**

7. Can PMs self-schedule events, or must someone else request it?

8. What happens if a PM rejects a scheduling request?
   - Goes back to requester?
   - Escalates to Wendy?
   - Automatically suggests alternative PM?

#### Work Order Creation Process
9. Do you want to generate work orders from sales orders automatically, or manually create each one?

10. Marcus said you can generate work order without picking specific lines:
    - Is that what you want, or do you want line-level detail?

11. For contractor installation work orders:
    - Do they see the same work order as PMs?
    - Different information/fields?

#### Complexity Decision
12. How simple do you want work orders?
    - Basic: Event type, date, resource assigned, location → Done
    - Medium: Add estimated hours, required materials list
    - Complex: Task checklists, dependencies, sign-off requirements

---

## SESSION 5: 15% Labor Markup Business Rules (60 min)

### Attendees
✅ **PM's Suggestion:** Kipp (IT/Process), Operations/Finance, Matt, Lorraine, Rafina (Design Manager)  
⭐ **PERFECT ATTENDEE LIST** - All critical stakeholders included

### Pre-Work Required
- [ ] **Kipp:** Complete exception logic from Core system **(GAP-003 - CRITICAL)**
- [ ] **Kipp:** 5-10 sample orders for testing **(GAP-003 - CRITICAL)**

### Questions

#### Decision Confirmation
1. **Confirm you want to continue the 15% labor markup in NetSuite?** (Just checking - could eliminate if desired)

#### Exception Logic (GAP-003 - CRITICAL PRIORITY - BLOCKING CONFIGURATION)
2. **What is the complete business rule logic:**
   - Which **order types** trigger the markup? (List all)
   - Which **order types** are excluded? (List all)
   - Are there **specific clients** with exceptions? (List client names)
   - How do you identify **"external labor"** lines?
     - Specific item codes?
     - Line codes?
     - Item category?
     - Something else?

3. Can you provide the current formula/logic from Core?
   - Even if it's just notes or SQL, Marcus can translate

4. Can you provide 5-10 sample orders to test against?
   - Include orders that SHOULD have markup
   - Include orders that should NOT have markup
   - Include edge cases

#### Markup Mechanics (REQ-021, REQ-022, REQ-023)
5. Kipp's wish list - confirm requirements:
   - Line must exist ✅
   - Always at **bottom** (not top) ✅
   - **Uneditable** by users ✅
   - **Non-printing** (doesn't show on proposals) ✅
   - Always dynamic (recalculates automatically) ✅
   - **All of these still required?**

6. Calculation mechanics:
   - Takes 15% of external labor **cost** → adds to total cost → **reduces GP**
   - Confirm this is correct?
   - Does NOT affect revenue?

#### Commission Impact
7. How does 15% markup line affect sales commissions?
   - Commission calculated on GP before markup?
   - Or after markup? (meaning commission is lower)

8. Do salespeople see this line in their order view?

#### Reporting (Project GP vs Commissionable GP)
9. Do you need separate reports for:
   - **Project GP** (with 15% markup applied) - true profitability
   - **Commissionable GP** (before markup) - for commission calculations
   - Or is it the same?

10. Who needs to see markup line vs. who shouldn't?
    - All users see it?
    - Only finance?
    - Role-based visibility?

#### Testing Approach
11. How will you validate the formula is working correctly before go-live?

12. Who will sign off that calculation is accurate?

---

## SESSION 6: Punch List & Field Service App (90 min)

### Attendees
✅ **PM's Suggestion:** Field Users, Wendy (PM Manager), Rafina (Design Manager), Kipp (IT/Process)  
📝 **Recommendation:** Include actual PM users (not just Wendy as manager)

### Pre-Work Required
- [ ] **Wendy/PMs:** 2-3 PlanGrid status report examples **(GAP-008 - HIGH PRIORITY)**
- [ ] **Design Team:** Sample floor plan files in typical formats **(GAP-010)**
- [ ] **IT:** Tablet/device inventory and specifications

### Questions

#### PlanGrid Status Report Requirements (GAP-008 - HIGH PRIORITY - NEED EXAMPLES)
1. **Please provide 2-3 actual PlanGrid report examples** (redact client names)
   - What format are they? (PDF email, link, embedded in email?)
   - Who receives them? (client, PM manager, both?)

2. What must be included in field-generated status reports:
   - Punch list items with photos?
   - Floor plan markups showing issue locations?
   - Completion percentages?
   - Resource time logged?
   - Next steps/action items?
   - Signatures?

3. Report generation workflow:
   - PM generates report on iPad in field?
   - System auto-emails report?
   - To whom?
   - Subject line format?
   - Any branding/logo requirements?

#### Floor Plan Functionality (GAP-010)
4. **Bring sample floor plan files to session for testing:**
   - What file formats do you typically receive? (PDF, DWG, DXF, JPG, PNG?)
   - Who creates floor plans? (your designers, architects, clients provide?)
   - Average file size?

5. Floor plan upload process:
   - Who uploads floor plans to system? (designers, PMs, admin?)
   - When in project lifecycle?
   - One master floor plan per project, or multiple (per floor, per revision)?

6. Floor plan pinning - when PM pins punch item to location:
   - Can they pin to multiple locations? (issue appears in multiple rooms)
   - Can they draw circles/arrows/markup beyond just pin?
   - Can they add text notes directly on floor plan?

#### Punch List Management
7. Punch item types/categories:
   - Do you have standard punch categories? (damage, wrong product, installation issue, design issue)
   - Who's responsible options? (vendor, installer, designer, manufacturer)
   - Priority levels? (critical, high, medium, low)

8. Punch item workflow:
   - PM creates punch in field
   - Who gets notified?
   - Who assigns it for resolution?
   - Who closes it out?
   - Does it need approval to close?

9. Marcus mentioned Issue Types can be punch, damage, billing discrepancy:
   - Do you want to track non-punch "issues" in the same system?
   - Or punch list only?

#### Mobile Features

10. **Offline Mode & GPS/Geological Check-in:**
    - PMs check in when arriving on site → GPS stamps location and time
    - Who can see check-in history? (Wendy only, or PMs see their own?)
    - Do you want geofencing? (must be within X feet of site to check in)

11. **Multi-Resource Time Entry (REQ-031):**
    - Scenario: PM on site with 3 contractors, all work 4 hours
    - PM enters time once, applies to all 4 resources → Confirm this is desired?
    - Can PM add temporary resources (contractor brought someone not in system)?

12. **Photo/Document Attachments:**
    - File size limits for photos?
    - Photo compression needed? (high res vs optimized for mobile)
    - Document types allowed? (PDF, Word, Excel?)

#### Hardware & Device Management
13. What tablets/devices will PMs use?
    - Company-provided iPads?
    - Personal devices?
    - What models/OS versions?

14. How many PMs need field service app access?

15. Who manages device setup and app installation?

#### PlanGrid Transition Plan
16. When do you want to stop using PlanGrid?
    - Immediate cutover on go-live?
    - Parallel run for X months?
    - Phase by PM or by project?

17. What happens to historical PlanGrid data?
    - Export and archive?
    - Keep PlanGrid for closed projects?
    - Migrate punch lists to NetSuite?

---

## SESSION 7: Scheduling & Resource Management (120 min)
### ⚠️ MOST CRITICAL SESSION - GAP-001

### Attendees
✅ **PM's Suggestion:** Wendy (PM Manager), Matt, Lorraine, Account Managers  
⚠️ **CRITICAL ADDITION:** **Kimmy (Account Manager Leader)** - Essential for pre-quote tracking discussion

### Pre-Work Required
- [ ] **Wendy:** Bring current Google Sheet PM workload calendar **(CRITICAL)**
- [ ] **Wendy:** Document ideal PM task list for typical project
- [ ] **Kimmy:** Document account manager pre-quote activities and timeline
- [ ] **Kimmy:** List most valuable Asana features you want

### Context
**This is GAP-001 - Your #1 Critical Gap covering REQ-032, REQ-033, REQ-034**

Marcus explicitly deferred this during your original session: *"We'll definitely come back to that. So scheduling and resourcing... we'll have another session where we go a little bit deeper on this."*

### Questions

#### Task Management Sophistication Decision (REQ-034)
1. **Matt's question: "10 phases or 300 tasks?"**
   - High-level phases only? (Pre-quote, Design, Procurement, Installation, Closeout)
   - Detailed tasks within phases? (RFI response, kickoff meeting, site survey, drawing review, etc.)
   - How granular do you want to go?

2. **Employee perspective:**
   - Wendy said: *"We have non-process-driven people... Their pushback is, you hired me to do the job. Trust me to do the job."*
   - How do you balance process accountability vs. autonomy?
   - What's the minimum tracking you need vs. what would be nice?

3. **Manager vs. Individual Contributor needs:**
   - Kimmy: *"I don't want to manage all of that. That's the account manager's job to manage individual details. From manager perspective, I want to know what phase they're at, volume, and timeline."*
   - Should managers see high-level phases while individuals see detailed tasks?

#### PM Task List Automation (REQ-032)
4. **Wendy's vision:** *"When you get assigned as PM, you get a list of tasks: site verification, delivery, walkthrough, all these different things."*
   - Should task list auto-generate when PM assigned?
   - Standard task template for all projects?
   - Or varies by project type/order type?

5. What tasks should be on PM standard list?
   - Site verification visit
   - Review drawings/specs
   - Coordinate delivery
   - Attend installation
   - Punch walk
   - Final walkthrough
   - Project closeout
   - **What else?**

6. Task assignment and accountability:
   - Do tasks have due dates?
   - Can PMs self-schedule tasks?
   - Does someone need to sign off when complete?
   - What happens if task goes overdue?

#### Resource Visualizer & Calendar View (REQ-033)
7. **Wendy's current Google Sheet:**
   - Show everyone what it looks like
   - What do you love about it?
   - What drives you crazy?
   - What's missing?

8. **Pain point:** *"It's only as accurate as the information... Not accurate by time accessed"*
   - You need real-time view that auto-updates from NetSuite?
   - Or scheduled refresh (daily, hourly)?

9. Calendar view requirements:
   - Timeline view (Gantt-style bars showing install dates)?
   - Calendar grid (month view with dots/events)?
   - List view with filters?
   - All of the above?

10. Workload visualization:
    - How do you want to see PM capacity/availability?
    - Weighted cards (small/medium/large projects)?
    - Hour estimates per project?
    - Just count of projects?
    - Red/yellow/green indicators for overloaded PMs?

11. Who needs this view?
    - Wendy only (manager)?
    - All PMs see their own workload?
    - Account Managers see PM availability when assigning?

#### Account Manager Pre-Quote Tracking (REQ-033 integration)
12. **Kimmy's need:** *"Account managers need a similar tool... Track from opportunity all the way to the end."*
    - What pre-quote activities need tracking?
    - RFI/RFP response?
    - Estimating time?
    - Client meetings?

13. How do account manager workload and PM workload integrate?
    - Same visualizer showing both?
    - Separate views?
    - Handoff point where it moves from account manager to PM?

14. **Timing shift:** *"We're trying to change where PM gets assigned at same time as designer"*
    - Does this mean PM workload tracking starts earlier?
    - How does that affect resource planning?

#### Task Dependencies (Asana-Style Workflow)
15. **Kimmy's vision:** *"At Asana, when you complete a task, they queue the next thing. If that next thing is assigned to someone else, they know it's ready for them."*
    - Do you want automatic task triggering?
    - Task dependencies? (can't start Task B until Task A complete)
    - Automatic notifications when task assigned/ready?

16. **Marcus's caution:** *"Every time we've proposed it to dealers, it was too much. They wanted more flexibility."*
    - How much structure do you want?
    - Or more flexibility?

17. Asana evaluation:
    - **Wendy:** *"I've held off on rolling out Asana until I understand what NetSuite's going to offer."*
    - What Asana features are must-haves vs. nice-to-haves?
    - If NetSuite can't do certain things, do you keep Asana or adapt process?

#### Implementation Approach
18. If you decide on sophisticated task management:
    - Phase 1: Basic (just track assignments and dates)?
    - Phase 2: Add task lists and dependencies later?
    - Or full implementation from start?

19. What's your risk tolerance for employee pushback?
    - Start simple and add rigor later?
    - Or implement full process from go-live?

---

## PRIORITY SUMMARY

### 🔴 CRITICAL PRIORITY - Must Answer (Blocking Configuration)

| Session | Question Topic | GAP # | Why Critical |
|---------|---------------|-------|--------------|
| **Session 7** | All scheduling & resource management questions | GAP-001 | Affects REQ-032, 033, 034 - No decisions made yet |
| **Session 5** | Complete 15% markup exception logic from Kipp | GAP-003 | Blocking sales order configuration |
| **Session 4** | Work order final confirmation | GAP-002 | Wendy soft buy-in, need leadership approval |
| **Session 3** | Damaged product accounting treatment | GAP-005 | Lorraine explicitly requested - affects financial reporting |

### 🟡 HIGH PRIORITY - Need Data (For Configuration)

| Session | Data Needed | GAP # | Owner |
|---------|-------------|-------|-------|
| **Session 5** | Complete rate matrix | GAP-004 | Kipp/Wendy/Rafina |
| **Session 2** | Contractor access lists (2 lists) | GAP-006 | Wendy/Rafina/Operations |
| **Session 1** | Warehouse location list | GAP-007 | Operations Team |
| **Session 6** | PlanGrid report examples | GAP-008 | Wendy/PM Team |

### 🟢 MEDIUM PRIORITY - Quick Confirmations

| Session | Question Topic | GAP # | Complexity |
|---------|---------------|-------|------------|
| **Session 4** | Work order event types | GAP-009 | Low - just confirm list |
| **Session 6** | Floor plan file formats | GAP-010 | Low - bring samples to test |
| **Session 1** | Bin naming conventions | GAP-011 | Low - simple decision |

---

## RECOMMENDED SESSION ORDER

### Phase 1: Critical Decisions (Weeks 1-2)
1. **Session 7: Scheduling & Resource Management** (FIRST - Most critical)
2. **Session 5: 15% Labor Markup** (Kipp must provide exception logic)
3. **Session 4: Work Orders** (Get final sign-off)

### Phase 2: Configuration Data Collection (Weeks 2-3)
4. **Session 3: VRA & Damaged Product** (Lorraine accounting decision)
5. **Session 2: Vendor Center** (Contractor lists)
6. **Session 1: Receiving** (Warehouse locations)

### Phase 3: Demo & Validation (Week 4)
7. **Session 6: Punch List & Field Service App** (Demo-heavy, need examples)

---

## COMPLETION TIMELINE

| Milestone | Target | Completion % | Dependencies |
|-----------|--------|--------------|--------------|
| **Session 7 Scheduled** | Week 1 | 82% → 85% | Wendy, Kimmy, Matt, Marcus availability |
| **Session 7 Completed** | Week 2 | 93% | Pre-work from Wendy/Kimmy |
| **Sessions 1-5 Data Received** | Week 3 | 97% | Kipp (logic/rates), Operations (lists) |
| **Session 6 Completed** | Week 4 | 100% | PlanGrid examples, floor plans |
| **Requirements Sign-off** | Week 5 | 100% | Leadership approval |

**Expected Timeline to 100% Completion:** 5-6 weeks from scheduling Session 7

---

## NEXT IMMEDIATE ACTIONS

### For Implementation Team (Marcus/Chris):
1. ⚠️ **CRITICAL:** Schedule Session 7 (Scheduling & Resource Management) within 2 weeks
   - Required: Wendy, Kimmy, Matt, Marcus
   - Duration: 2 hours
   - Pre-work: Wendy's Google Sheet, Kimmy's Asana requirements

2. Send data request emails:
   - **To Kipp:** 15% markup exception logic + sample orders (GAP-003)
   - **To Kipp/Wendy/Rafina:** Complete rate matrix (GAP-004)
   - **To Operations Team:** Warehouse locations + contractor access lists (GAP-006, GAP-007)
   - **To Wendy/PMs:** PlanGrid report examples (GAP-008)

### For Client Team:
1. **Wendy:** Prepare Google Sheet calendar for Session 7 demo
2. **Kimmy:** Document Asana must-have features for Session 7
3. **Kipp:** Extract 15% markup logic from Core (blocking configuration)
4. **Lorraine/Kipp:** Discuss damaged product accounting treatment before Session 3

---

## APPENDIX: QUESTIONNAIRE TRACEABILITY

### Requirements Coverage by Session

| Requirement | Session | Status | Question Coverage |
|-------------|---------|--------|-------------------|
| REQ-001 | N/A | ✅ Complete | Purchase requisitions - decision made |
| REQ-002 | Session 1 | ACCOMMODATE | Advanced Receiving demo |
| REQ-003-005 | Session 1 | ALIGNS | Bin structure |
| REQ-006-009 | Session 2 | ALIGNS/ACCOMMODATE | Vendor center |
| REQ-010-012 | Session 3 | ADAPT/ACCOMMODATE | VRA process |
| REQ-013-015 | Session 4 | ADAPT | Work orders |
| REQ-016-020 | N/A | ✅ Complete | Time tracking - decisions made |
| REQ-021-023 | Session 5 | ACCOMMODATE | 15% labor markup |
| REQ-024-027 | Session 6 | ACCOMMODATE | Punch list & field app |
| REQ-028-031 | Session 6 | ALIGNS | Field Service features |
| REQ-032-034 | Session 7 | TBD | **CRITICAL - Scheduling decisions needed** |

---

**Document Status:** Ready for use in discovery sessions  
**Version:** 1.0  
**Date:** December 2, 2025

*This document contains 7 comprehensive discovery sessions covering all gaps identified in Questionnaire_Operations_v1.0.md and GapAnalysis_Operations.md*

