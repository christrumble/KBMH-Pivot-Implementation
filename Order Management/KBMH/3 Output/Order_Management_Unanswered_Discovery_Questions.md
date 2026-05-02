# Order Management - Unanswered Discovery Questions
**Version**: 1.0  
**Date**: December 2, 2025  
**Purpose**: Follow-up questions that have not been fully answered from the discovery questionnaire  
**Source**: Analysis of Questionnaire_OrderManagement_v1.1.md and Discovery_Session_Questions.md

---

## EXECUTIVE SUMMARY

This document identifies all discovery questions that remain unanswered or have confidence ratings below 85%. These questions require follow-up discovery sessions, decisions, or documentation before proceeding to design and configuration phases.

**Total Unanswered Questions**: 67  
**High Priority**: 18 questions  
**Medium Priority**: 31 questions  
**Low Priority**: 18 questions  

---

## SECTION 1: CUSTOMER MANAGEMENT (8 Questions)

### 1.1 Customer Hierarchy & Relationships (Confidence: Below 80%)

**Questions:**

1. Do you have customers with parent-child relationships requiring consolidated billing?
   - **Priority**: Medium
   - **Why Important**: Affects customer record structure and invoicing approach
   - **Who to Ask**: Finance Lead, Account Managers

2. Do government entities need to be grouped under agencies or departments?
   - **Priority**: Medium
   - **Why Important**: 20% of business is government; may need hierarchical tracking
   - **Who to Ask**: Sales team handling government accounts

3. Are there any corporate customers with multiple subsidiaries or locations?
   - **Priority**: Medium
   - **Why Important**: Could require consolidated reporting or billing
   - **Who to Ask**: Account Managers, Finance team

4. Do intermarket dealers need relationship tracking or grouping?
   - **Priority**: Low
   - **Why Important**: High volume of intermarket transactions (thousands annually)
   - **Who to Ask**: Shannon

### 1.2 Deposit Management (Confidence: 80%)

**Questions:**

5. What is the standard deposit percentage or amount you require?
   - **Priority**: High
   - **Why Important**: Currently part of approval requirements; needs to be configured
   - **Who to Ask**: Finance Lead, Matt

6. How is the deposit applied to the final invoice?
   - **Priority**: High
   - **Why Important**: Affects accounting processes and system configuration
   - **Who to Ask**: Finance Lead, Lorraine

7. Do you handle proforma invoices? When and how?
   - **Priority**: Medium
   - **Why Important**: May need separate transaction type or workflow
   - **Who to Ask**: Finance Lead, Lorraine

8. Do you have milestone-based payment scenarios? How do they work?
   - **Priority**: Medium
   - **Why Important**: Could require custom invoicing workflow
   - **Who to Ask**: Finance Lead, Account Managers

---

## SECTION 2: QUOTE/PROPOSAL MANAGEMENT (12 Questions)

### 2.1 Quote Versioning & Revisions (Confidence: Below 80%)

**Questions:**

9. How do you handle client-requested changes to proposals?
   - **Priority**: High
   - **Why Important**: Affects workflow and audit trail requirements
   - **Who to Ask**: Shannon, Project Coordinators, Sales team

10. Do you create new proposal versions or modify existing proposals?
    - **Priority**: High
    - **Why Important**: Determines versioning approach in NetSuite
    - **Who to Ask**: Shannon, Project Coordinators

11. Do you need to track and compare multiple proposal versions?
    - **Priority**: Medium
    - **Why Important**: Audit trail and change management requirements
    - **Who to Ask**: Matt, Shannon

12. How do you ensure the team works from the latest proposal version?
    - **Priority**: Medium
    - **Why Important**: Version control and communication process
    - **Who to Ask**: Shannon, Operations team

13. What triggers a new proposal version vs. modification?
    - **Priority**: Medium
    - **Why Important**: Business rules for version control
    - **Who to Ask**: Shannon, Matt

14. How often do you have to issue revised quotes?
    - **Priority**: Low
    - **Why Important**: Volume indicator for version tracking importance
    - **Who to Ask**: Shannon, Sales team

### 2.2 Upfront Budgeting Workflow

**Questions:**

15. How is the Google Docs collaborative budgeting linked to opportunities in the system?
    - **Priority**: Medium
    - **Why Important**: Integration or manual process definition
    - **Who to Ask**: Sales team, Project Coordinators

16. Will opportunity tracking become mandatory or remain optional?
    - **Priority**: Medium
    - **Why Important**: Forecasting accuracy and CRM adoption
    - **Who to Ask**: Matt, Sales Leadership

17. What is the pipeline forecasting methodology detail?
    - **Priority**: Low
    - **Why Important**: Reporting and forecasting configuration
    - **Who to Ask**: Sales Leadership, Finance

### 2.3 Spec Creation & Catalog Integration

**Questions:**

18. How will you handle spec creation for small orders, showroom orders, and employee orders without catalog access?
    - **Priority**: Medium
    - **Why Important**: Current pain point; workaround process needed
    - **Who to Ask**: Kipp, Project Coordinators

19. What is the timeline for Configura/CET integration?
    - **Priority**: Low
    - **Why Important**: Long-term solution vs. workaround decision
    - **Who to Ask**: IT Lead, Marcus

20. Will Project Spec training be provided to the team?
    - **Priority**: Low
    - **Why Important**: Change management and adoption
    - **Who to Ask**: Operations Manager, Training Lead

---

## SECTION 3: SALES ORDER MANAGEMENT (7 Questions)

### 3.1 Sales Order Form Fields

**Questions:**

21. What specific additional fields are needed on the SO form vs. the proposal form?
    - **Priority**: High
    - **Why Important**: Form configuration requirement
    - **Who to Ask**: Shannon, Operations team

22. What specific date fields do you capture at the SO stage?
    - **Priority**: High
    - **Why Important**: Mentioned in transcript but not detailed
    - **Who to Ask**: Shannon, Project Coordinators

23. Are these date fields required or optional?
    - **Priority**: Medium
    - **Why Important**: Validation rules configuration
    - **Who to Ask**: Shannon, Operations team

24. Are there other fields beyond dates needed at SO stage?
    - **Priority**: Medium
    - **Why Important**: Complete form design
    - **Who to Ask**: Shannon, Project Coordinators

### 3.2 Order Types

**Questions:**

25. What is the complete list of all order types with descriptions and annual volumes?
    - **Priority**: High
    - **Status**: Action item assigned to team (Matt, Shannon, Kipp)
    - **Why Important**: Configuration and reporting requirements
    - **Who to Provide**: Matt, Shannon, Kipp

26. Are there any other order types beyond the five identified?
    - **Priority**: Medium
    - **Why Important**: Complete configuration
    - **Who to Ask**: Operations team, Finance

27. What default order line configurations are needed by order type?
    - **Priority**: Low
    - **Why Important**: Automation opportunities
    - **Who to Ask**: Operations team

---

## SECTION 4: MULTI-ORDER PROJECT MANAGEMENT (5 Questions)

### 4.1 Project Splitting Strategy

**Questions:**

28. What percentage of projects have multiple orders?
    - **Priority**: Medium
    - **Why Important**: Volume indicator for importance of feature
    - **Who to Ask**: Shannon, Operations team

29. What is the average number of orders per multi-order project?
    - **Priority**: Low
    - **Why Important**: Scaling and performance considerations
    - **Who to Ask**: Shannon, Project Coordinators

30. What project-level reporting is needed beyond GP?
    - **Priority**: Medium
    - **Why Important**: Reporting requirements configuration
    - **Who to Ask**: Finance team, Matt

31. How do you handle project-level customer communications?
    - **Priority**: Low
    - **Why Important**: Communication workflow definition
    - **Who to Ask**: Account Managers, Project Coordinators

32. How do you want to navigate between related orders on a project?
    - **Priority**: Low
    - **Why Important**: User experience design
    - **Who to Ask**: Shannon, Project Coordinators

---

## SECTION 5: PURCHASE ORDER MANAGEMENT (14 Questions)

### 5.1 Draft PO Workflow (HIGH PRIORITY)

**Questions:**

33. What is the complete Draft PO workflow from creation to vendor transmission?
    - **Priority**: HIGH
    - **Status**: Follow-up session completed but requires design clarification
    - **Why Important**: Core operational process; mentioned but not fully explained
    - **Who to Ask**: Kipp, Shannon, Operations team

34. Who can create draft POs?
    - **Priority**: HIGH
    - **Why Important**: Permissions and access control
    - **Who to Ask**: Kipp, Operations Manager

35. Who reviews draft POs and what are they checking?
    - **Priority**: HIGH
    - **Why Important**: Approval workflow design
    - **Who to Ask**: Kipp, Shannon, Operations team

36. Who approves draft POs before they become vendor POs?
    - **Priority**: HIGH
    - **Why Important**: Approval authority definition
    - **Who to Ask**: Matt, Kipp, Operations Manager

37. What is the approval criteria for draft POs?
    - **Priority**: HIGH
    - **Why Important**: Business rules configuration
    - **Who to Ask**: Matt, Kipp

38. When does a draft PO convert to a vendor PO?
    - **Priority**: HIGH
    - **Why Important**: Workflow trigger definition
    - **Who to Ask**: Operations team, Shannon

39. Are there dollar thresholds for draft PO approval?
    - **Priority**: Medium
    - **Why Important**: Approval rule configuration
    - **Who to Ask**: Matt, Finance

40. What happens if a draft PO is rejected?
    - **Priority**: Medium
    - **Why Important**: Exception handling workflow
    - **Who to Ask**: Operations team, Kipp

### 5.2 PO Template Redesign

**Questions:**

41. What specific issues make current POs "a shitstorm of information"?
    - **Priority**: HIGH
    - **Status**: Kipp to provide current templates
    - **Why Important**: Template redesign requirements
    - **Who to Ask**: Kipp

42. What information on a PO is most important to vendors?
    - **Priority**: High
    - **Why Important**: Template prioritization
    - **Who to Ask**: Operations team, Purchasing

43. What information on POs is unnecessary or confusing?
    - **Priority**: High
    - **Why Important**: Template simplification
    - **Who to Ask**: Kipp, Operations team

44. If redesigning POs today, what would the new layout look like?
    - **Priority**: High
    - **Why Important**: Design input
    - **Who to Ask**: Kipp

45. Have vendors requested changes or complained about current PO format?
    - **Priority**: Medium
    - **Why Important**: External stakeholder input
    - **Who to Ask**: Operations team, Shannon

### 5.3 PO Transmission & Processing

**Questions:**

46. How are POs transmitted to vendors? (Email, EDI, portal?)
    - **Priority**: Medium
    - **Why Important**: Technical integration requirements
    - **Who to Ask**: Operations team, IT Lead

---

## SECTION 6: CUSTOMER PO TRACKING (HIGH PRIORITY - 10 Questions)

### 6.1 Bank Reporting Requirements

**Questions:**

47. What specific data does the bank require about customer POs?
    - **Priority**: HIGH
    - **Why Important**: External compliance requirement
    - **Who to Ask**: Finance Lead, Matt

48. What does the bank do with this data? (Collateral, compliance, verification?)
    - **Priority**: HIGH
    - **Why Important**: Understanding requirement scope
    - **Who to Ask**: Finance Lead, Matt

49. How often does the bank need this data? (Monthly, quarterly, on-demand?)
    - **Priority**: HIGH
    - **Why Important**: Reporting frequency and automation level
    - **Who to Ask**: Finance Lead

50. What format does the bank need? (Spreadsheet, report format, dashboard access?)
    - **Priority**: HIGH
    - **Why Important**: Output format requirements
    - **Who to Ask**: Finance Lead

### 6.2 Customer PO Scenarios

**Questions:**

51. How often do you get a single PO per project vs. multiple POs per project?
    - **Priority**: High
    - **Why Important**: Solution design complexity
    - **Who to Ask**: Finance Lead, Shannon

52. How often do you get blanket POs vs. project-specific POs?
    - **Priority**: High
    - **Why Important**: Tracking approach design
    - **Who to Ask**: Finance Lead, Account Managers

53. How often do customers issue change orders or amendments to POs?
    - **Priority**: High
    - **Why Important**: Change management workflow
    - **Who to Ask**: Finance Lead, Shannon

54. How do you handle change orders? New PO value or amendment?
    - **Priority**: High
    - **Why Important**: System logic for calculations
    - **Who to Ask**: Finance Lead

55. Do you ever have scenarios where orders aren't covered by a customer PO?
    - **Priority**: Medium
    - **Why Important**: Exception handling
    - **Who to Ask**: Finance Lead, Shannon

### 6.3 Solution Design Decisions

**Questions:**

56. Should customer PO tracking be a custom record or custom transaction?
    - **Priority**: HIGH
    - **Status**: Separate working session scheduled
    - **Why Important**: Technical architecture decision
    - **Who to Decide**: Marcus/GSI with Finance Lead, Shannon

57. Who will enter customer PO information?
    - **Priority**: HIGH
    - **Why Important**: Process ownership and permissions
    - **Who to Decide**: Finance Lead, Shannon

58. How often does customer PO information need to be entered or updated?
    - **Priority**: High
    - **Why Important**: Workflow frequency
    - **Who to Ask**: Finance Lead, Shannon

59. Should customer PO utilization update automatically or manually?
    - **Priority**: High
    - **Why Important**: Automation level decision
    - **Who to Ask**: Finance Lead, IT Lead

60. What alert thresholds should trigger warnings? (75%, 80%, 90%?)
    - **Priority**: High
    - **Why Important**: Business rule configuration
    - **Who to Ask**: Finance Lead, Shannon

61. Who should receive alerts when approaching PO limits?
    - **Priority**: Medium
    - **Why Important**: Alert routing configuration
    - **Who to Ask**: Finance Lead, Shannon

---

## SECTION 7: APPROVAL WORKFLOWS (4 Questions)

### 7.1 Approval Process Details

**Questions:**

62. What is the complete approval workflow flowchart with all scenarios?
    - **Priority**: HIGH
    - **Status**: Action item assigned to Shannon
    - **Why Important**: Workflow configuration
    - **Who to Provide**: Shannon

63. Who is the backup approver beyond Mark?
    - **Priority**: Medium
    - **Why Important**: Coverage during absences
    - **Who to Ask**: Matt, Shannon

64. What are the approval SLAs or expected response times?
    - **Priority**: Low
    - **Why Important**: Performance monitoring
    - **Who to Ask**: Matt, Shannon

65. How is approval coverage handled during holidays/vacations?
    - **Priority**: Low
    - **Why Important**: Business continuity
    - **Who to Ask**: Matt, Shannon

---

## SECTION 8: INTEGRATIONS & E-PORTALS (3 Questions)

### 8.1 Coupa Integration (Deferred Topic)

**Questions:**

66. Should Coupa email parsing be automated now, or remain manual?
    - **Priority**: HIGH
    - **Status**: Decision needed - ROI analysis required
    - **Why Important**: Shannon processes thousands of orders; significant time savings potential
    - **Who to Decide**: Matt, Shannon, IT Lead, Marcus

67. What is the detailed Coupa email process step-by-step?
    - **Priority**: High
    - **Why Important**: Automation requirements definition
    - **Who to Ask**: Shannon (detailed walkthrough needed)

68. What other e-portal or integration needs exist beyond Coupa?
    - **Priority**: Medium
    - **Why Important**: Complete integration landscape
    - **Who to Ask**: Shannon, IT Lead

---

## SECTION 9: ACTION ITEMS NOT YET COMPLETED

### Documentation to be Provided

| Item | Assigned To | Due | Priority | Status |
|------|-------------|-----|----------|--------|
| Complete approval workflow flowchart | Shannon | Early implementation | HIGH | Pending |
| All current templates (customer and vendor-facing) | Kipp | Early implementation | HIGH | Pending |
| XML import template example | Matt | Early implementation | Medium | Pending |
| Complete order type list with descriptions | Team (Matt, Shannon, Kipp) | Early implementation | HIGH | Pending |
| Transaction numbering format starting sequences | TBD (IT Admin with Process Owners) | Pre-configuration | Medium | Pending |

### Decisions to be Made

| Decision | Decision Makers | Priority | Status |
|----------|----------------|----------|--------|
| Miller Knoll tiered pricing escalation with Dustin | Matt, Marcus | HIGH | Pending escalation |
| Coupa automation investment decision | Matt, Shannon, IT Lead | HIGH | Pending ROI analysis |
| Draft PO approval authority and workflow | Matt, Kipp, Operations | HIGH | Pending design session |
| Customer PO tracking solution architecture | Finance Lead, Marcus/GSI | HIGH | Session scheduled |
| Vendor credit limit thresholds | Finance/AP Team | Medium | Pending |
| Double order detection parameters | Shannon, Operations/Finance | Medium | Pending |
| Template change control process | Kipp, IT | Medium | Pending |

---

## SECTION 10: FOLLOW-UP SESSIONS REQUIRED

### Session 1: Draft PO Workflow & Template Redesign
- **Duration**: 2 hours
- **Participants**: Kipp, Shannon, Operations team, Marcus (GSI)
- **Priority**: HIGH
- **Status**: Topic introduced but not completed
- **Questions to Address**: Questions 33-46 above
- **Deliverables**: 
  - Complete draft PO workflow diagram
  - PO approval authority matrix
  - PO template redesign specifications
  - Transmission method determination

### Session 2: Customer PO Tracking Solution Design
- **Duration**: 2 hours
- **Participants**: Finance Lead, Shannon, Matt, Marcus (GSI), potential bank liaison
- **Priority**: HIGH
- **Status**: Scheduled
- **Questions to Address**: Questions 47-61 above
- **Deliverables**:
  - Technical architecture decision (record vs. transaction)
  - Data entry process workflow
  - Dashboard KPI definitions
  - Alert threshold configuration
  - Bank reporting format specification

### Session 3: E-Portals & Coupa Integration Decision
- **Duration**: 1 hour
- **Participants**: Shannon, Matt, IT Lead, Marcus (GSI)
- **Priority**: HIGH
- **Status**: Deferred; needs scheduling
- **Questions to Address**: Questions 66-68 above
- **Deliverables**:
  - Coupa automation go/no-go decision
  - ROI analysis
  - Detailed process documentation
  - Implementation timeline (if approved)

### Session 4: Template Design Review & Change Control
- **Duration**: 1.5 hours
- **Participants**: Kipp (design owner), Marcus (GSI), customer-facing teams
- **Priority**: Medium
- **Status**: Pending template delivery from Kipp
- **Deliverables**:
  - Template design approval
  - Change control process definition
  - Version control standards
  - Authorization matrix for post go-live changes

### Session 5: Quick Gap Closure
- **Duration**: 1 hour
- **Participants**: Shannon, Finance Lead, Sales team, Operations team
- **Priority**: Medium
- **Status**: Not scheduled
- **Questions to Address**: Remaining questions 9-32, 62-65
- **Deliverables**:
  - Complete order type list
  - Quote versioning process definition
  - Deposit policy documentation
  - SO form field requirements
  - Customer hierarchy needs determination

---

## SECTION 11: QUESTIONS BY PRIORITY

### HIGH PRIORITY (Must Answer Before Design - 18 Questions)

1. Deposit percentage/amount standards (Q5)
2. Deposit application to final invoice (Q6)
3. Client-requested changes to proposals (Q9)
4. New version vs. modify existing (Q10)
5. Additional SO form fields needed (Q21)
6. Date fields captured at SO stage (Q22)
7. Complete order type list (Q25)
8. Draft PO workflow complete definition (Q33)
9. Who creates draft POs (Q34)
10. Who reviews draft POs (Q35)
11. Who approves draft POs (Q36)
12. Draft PO approval criteria (Q37)
13. Draft to vendor PO conversion trigger (Q38)
14. Current PO template issues (Q41-44)
15. Bank data requirements for customer PO (Q47-50)
16. Customer PO scenario frequencies (Q51-54)
17. Customer PO tracking architecture (Q56-60)
18. Approval workflow flowchart (Q62)

### MEDIUM PRIORITY (Should Answer During Design - 31 Questions)

Questions: 1-4, 7-8, 11-18, 23-24, 26, 28, 30, 40, 45-46, 55, 61, 63, 67-68

### LOW PRIORITY (Nice to Have - 18 Questions)

Questions: 14, 17, 19-20, 27, 29, 31-32, 64-65, and remaining detail questions

---

## SECTION 12: RISK ASSESSMENT

### High Risk - No Answer

1. **Draft PO Workflow** - Core operational process not fully defined
2. **Customer PO Tracking** - Bank requirement; compliance risk
3. **Deposit Management** - Financial process not documented
4. **Quote Versioning** - Audit trail and version control unclear

### Medium Risk - Partial Answer

1. **Multi-Order Projects** - Functionality exists but process details needed
2. **Approval Workflows** - Rules known but detailed flowchart pending
3. **Order Types** - Main types identified but complete list pending

### Low Risk - Can Proceed

1. **Transaction Structure** - Well understood
2. **Tax Management** - Clear requirements
3. **Commission Tracking** - Process defined
4. **BOM Import** - Requirements clear

---

## SECTION 13: RECOMMENDATIONS

### Immediate Actions (This Week)

1. **Schedule Session 1** (Draft PO Workflow) - 2 hours with Kipp, Shannon, Operations
2. **Request Documentation**:
   - Shannon: Approval workflow flowchart
   - Kipp: Current templates (all customer and vendor-facing)
   - Matt: XML import template
   - Team: Complete order type list

### Next Week Actions

3. **Complete Session 2** (Customer PO Tracking) - Already scheduled
4. **Schedule Session 3** (Coupa/E-Portals) - 1 hour
5. **Begin ROI analysis** for Coupa automation decision

### Following Week Actions

6. **Schedule Session 5** (Quick Gap Closure) - 1 hour
7. **Schedule Session 4** (Template Review) - After Kipp provides templates
8. **Escalate** Miller Knoll tiered pricing to Dustin

---

## SECTION 14: QUESTIONS ORGANIZED BY WHO TO ASK

### Matt (Executive - 8 Questions)
- Q5, 6, 9, 11, 30, 36, 37, 47, 48, 66

### Shannon (Project Coordinator Manager - 18 Questions)
- Q9, 10, 12, 21, 22, 23, 24, 25, 28, 33, 35, 38, 51, 52, 53, 57, 58, 60, 61, 62, 67

### Kipp (Design/Operations - 8 Questions)
- Q18, 25, 33, 34, 35, 36, 37, 41, 42, 43, 44

### Finance Lead (8 Questions)
- Q1, 5, 6, 7, 8, 26, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60

### Operations Team (10 Questions)
- Q21, 23, 24, 26, 27, 28, 33, 34, 35, 38, 40, 42, 43, 45, 46

### Sales Team (6 Questions)
- Q1, 2, 9, 15, 16, 17

### IT Lead (5 Questions)
- Q19, 46, 59, 66, 67, 68

---

## APPENDIX: CONFIDENCE RATINGS FROM QUESTIONNAIRE

| Question Area | Confidence | Status |
|--------------|-----------|--------|
| Customer tax configuration | 97% | ✅ Good |
| Approval workflows | 98% | ✅ Good (flowchart pending) |
| Transaction structure | 98% | ✅ Good |
| Quote management | 95% | ✅ Good |
| BOM import | 95% | ✅ Good |
| Order types | 96% | ⚠️ List pending |
| Commission structure | 93% | ✅ Good |
| Multi-order projects | 93% | ✅ Good |
| PO splitting | 85% | ⚠️ Draft PO workflow needed |
| Erosion monitoring | 94% | ✅ Good |
| Templates | 97% | ⚠️ Awaiting Kipp's delivery |
| **Customer hierarchy** | **<80%** | ❌ Needs investigation |
| **Quote versioning** | **<80%** | ❌ Needs investigation |
| **Deposit management** | **80%** | ⚠️ Needs more detail |
| **Customer PO tracking** | **<80%** | ❌ Session scheduled |
| **Draft PO workflow** | **85%** | ⚠️ Clarification needed |

---

**END OF DOCUMENT**

---

## NEXT STEPS

1. ☐ Review this document with project team
2. ☐ Prioritize which sessions to schedule first
3. ☐ Send to stakeholders for documentation preparation
4. ☐ Schedule Session 1 (Draft PO Workflow)
5. ☐ Confirm Session 2 (Customer PO Tracking) date
6. ☐ Schedule Session 3 (Coupa/E-Portals)
7. ☐ Track action item completion
8. ☐ Update questionnaire v1.2 after sessions complete

---

**Document Owner**: Marcus (GSI)  
**Last Updated**: December 2, 2025  
**Next Review**: After completion of follow-up sessions  
**Related Documents**: 
- Questionnaire_OrderManagement_v1.1.md
- Discovery_Session_Questions.md
- Master_Transcript_Order_Management.md


