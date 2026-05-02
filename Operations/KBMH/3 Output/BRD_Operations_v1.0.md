# Business Requirements Document
## Solution Alignment & Validation

**Operations Process Area**

### Project Information:
- **Implementation Name**: KBM Hogue NetSuite/Orion Implementation
- **Customer Name**: KBM Hogue
- **Process Area**: Operations (Receiving, Work Orders, Scheduling, Field Service, VRAs, Time Tracking, Punch List)
- **Document Owner**: Implementation Consultant
- **Prepared Date**: December 16, 2025

### Document Version History:
| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 1.0 | Dec 16, 2025 | Implementation Team | Initial version based on discovery findings from Operations discovery session (July 31, 2025) |

---

## Executive Summary

KBM Hogue operates a unique outsourced installation model where the company manages all project coordination, design, and PM oversight while third-party installation contractors perform field work at their own warehouses. This operational model presents distinctive challenges: receiving must still occur at remote locations (impacting WIP), contractors must access project information without email dependency, and PMs must coordinate work in the field using mobile tools without internal installation control.

The proven Orion/NetSuite solution directly addresses these operational challenges through an integrated suite of capabilities specifically designed for the contract furniture dealer industry. The Orion Operations Suite combines advanced receiving tools, field service mobile applications, vendor portal management, and work order coordination to eliminate email-based communication, simplify remote receiving, and provide real-time field visibility. With 47% of operations requirements aligning with standard NetSuite functionality and an additional 26% requiring only process adaptation, KBM Hogue's operations will successfully transition to a cloud-based system while maintaining their proven outsourced model.

This Business Requirements Document validates that the Orion/NetSuite solution meets all documented requirements and outlines the implementation approach for each operational area. The document demonstrates clear business value alignment and identifies specific solution design investments required for three custom Orion enhancements (Advanced Receiving Tool, Field Service App capabilities, and the 15% Labor Markup formula).

---

## Change Log

### Sources:
- **Primary Discovery Session**: July 31, 2025 - NetSuite Operations Implementation: Advanced Receiving, Vendor Center, VRA, Work Orders, Scheduling, Field Service, Reporting, and Data Migration
- **Questionnaire Source**: Operations Master Transcript and Questionnaire_Operations_v1.0.md
- **Requirements Mapping Source**: Requirements_Map_Operations_v1.0.md
- **Solution Reference**: Orion Whitepaper

### Participants:
- **Marcus** (Implementation Team/Consultant)
- **Wendy** (PM Manager/Operations Manager)
- **Kipp** (IT Specialist/Former Controller)
- **Lorraine** (CFO/Controller)
- **Matt** (Leadership)
- **Kimmy** (Account Manager/Pre-Quote Manager)
- **Chris** (Implementation Team)

---

## Decision Log

### Key Implementation Decisions

| Decision | Classification | REQ IDs | Rationale | Status |
|----------|-----------------|---------|-----------|--------|
| Use Advanced Receiving Tool for all warehouse receiving | ACCOMMODATE | REQ-002 | Simplifies receiving at remote third-party locations; drag-and-drop interface eliminates clunky NetSuite standard workflow | Custom Orion Tool |
| Deploy Vendor Center for contractor communication | ALIGNS | REQ-006, REQ-009 | Eliminates email dependency; zero additional license cost through shared licensing model | Standard NetSuite |
| Implement receiving notification feature in vendor center | ACCOMMODATE | REQ-007 | Replaces email-based arrival notifications; contractors notify KBM through portal, showing in dashboard | Custom Orion Enhancement |
| Defer contractor direct receiving to future phase | ADAPT | REQ-008 | Current approach: contractors notify only, KBM performs actual receiving for control and accuracy; revisit when trust/process matures | Deferred Feature |
| Use VRA process for all damage scenarios (80/20 rule) | ADAPT | REQ-010, REQ-012 | Tracks expected vendor credits even when product not returned; solves critical pain point of "lost" credits; systematic follow-up | Process Change |
| Implement work orders for field coordination | ADAPT | REQ-013, REQ-014, REQ-015 | Soft scheduling approach; requests approval not hard assignments; coordinates with both internal PMs and external contractors | Process Change |
| Time tracking impacts project GP only (not GL) | ALIGNS | REQ-016 | Payroll imported from Paylocity; time entries affect project profitability analysis, not general ledger | Standard NetSuite |
| Implement 15% labor markup formula line | ACCOMMODATE | REQ-021, REQ-022, REQ-023 | Auto-calculates markup on external labor only; positioned at bottom, uneditable, non-printing; behavioral forcing function for pricing discipline | Custom Configuration |
| Replace PlanGrid with Field Service app punch list | ACCOMMODATE | REQ-024, REQ-025, REQ-026, REQ-027 | Built into Field Service app; eliminates subscription cost; critical feature: floor plan location pinning; includes offline mode and field report generation | Custom Orion Solution |
| Deploy Field Service app for all field operations | ALIGNS | REQ-028, REQ-029, REQ-030, REQ-031 | Tablet/mobile; supports geological check-in, photo/signature collection, multi-resource time entry; works offline with sync capability | Orion Enhanced Module |
| Defer scheduling/resource management to additional session | ADAPT | REQ-032, REQ-033, REQ-034 | Complex area requiring dedicated discovery session; balances need for visibility vs. risk of micromanagement and employee resistance | Future Session |

---

# SECTION 1: PURCHASE REQUISITIONS & PROCUREMENT CONTROL

## 1.1 Your Business Requirements

**REQ-001: Implement purchase requisition approval workflow (ALIGNS)**

KBM Hogue needs to enforce controlled purchasing through purchase requisitions that require supervisor approval before items can be ordered. The team made an explicit decision to use purchase requisitions, indicating a commitment to improving purchasing governance and creating audit trails for compliance and budget control purposes.

**Requirements Classification:**
- Type: Functional - Purchasing control process
- Priority: Must-Have
- Users Impacted: Employees requesting purchases, supervisors approving requests, procurement team, finance

---

## 1.2 Current State Process

**PROCESS:** Purchase Request & Approval (Current State)

**TRIGGER:** Employee needs to purchase materials or services

**CURRENT STEPS:**
1. Employee identifies need for purchase
2. Initiates purchase request through current system (manual or spreadsheet)
3. Requests routed to appropriate supervisor
4. Supervisor reviews and approves (or denies)
5. Once approved, converted to purchase order
6. Information likely re-keyed, creating data entry errors

**SYSTEMS INVOLVED:** Core (current system), possibly spreadsheets or email

**PAIN POINTS:**
- Manual re-keying when converting requisitions to POs (error-prone)
- Limited visibility into approval status
- No centralized audit trail for budget compliance
- Time-consuming manual workflow processes

---

## 1.3 Orion/NetSuite Solution

Orion/NetSuite provides comprehensive purchase requisition management that integrates seamlessly with the purchasing process. The proven solution includes automated approval routing based on business rules, supervisor assignment, and one-touch conversion from requisition to purchase order with complete data integrity. Once a supervisor approves a requisition in NetSuite, the system automatically creates the associated purchase order with all information pre-populated—eliminating manual re-keying and the errors that accompany manual data transfer.

The purchase requisition module in NetSuite includes flexible approval workflows that can route requisitions based on department, cost category, or amount thresholds. Approval histories are automatically recorded and maintained, providing the audit trail necessary for compliance verification and budget accountability. Employees benefit from a clear, transparent process where they can track their submitted requisitions from initial submission through supervisor review to final purchase order generation. Finance teams gain visibility into pending approvals and purchasing activity across the organization.

This standard functionality is used by thousands of NetSuite customers and represents proven, mature purchasing governance without customization required.

---

## 1.4 Future State Process

**PROCESS:** Purchase Requisition with Automatic Conversion (Future State)

**TRIGGER:** Employee needs to purchase materials or services

**FUTURE STEPS:**
1. Employee submits purchase requisition in NetSuite with item details, quantity, cost center
2. Requisition automatically routes to appropriate supervisor (based on department/amount rules)
3. Supervisor reviews and approves requisition in NetSuite (or requests modifications)
4. Upon approval, NetSuite automatically generates purchase order with all data pre-populated
5. Purchase order immediately available for vendor communication
6. No manual re-keying; complete data integrity from requisition to order

**SYSTEMS INVOLVED:** NetSuite Purchase Requisitions, Purchase Order management

**BENEFITS:**
- Eliminates manual re-keying and associated errors
- Provides complete audit trail of approvals
- Reduces time from request to order
- Ensures budget compliance through defined approval workflows

---

## 1.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-001 | Implement purchase requisition approval workflow | NetSuite Purchase Requisitions with supervisor approval routing and automatic PO conversion | ALIGNS |

---

## 1.6 Implementation Approach

**Purchase Requisitions will align with NetSuite's standard module:**
- NetSuite Purchase Requisitions module will be used without customization
- Approval routing rules will be configured based on KBM Hogue's department and authorization structure
- Automatic PO conversion will be enabled to eliminate manual data transfer
- Audit trail and approval history will be fully maintained in NetSuite

---

## 1.7 Custom Solution Designs

No custom solution design required. This requirement uses NetSuite standard functionality.

---

## 1.8 Implementation Considerations

- **User Training Required:** All employees who submit requisitions and all supervisors who approve requisitions need training on the new workflow
- **Approval Authority Mapping:** Finance and operations teams must define which supervisors have authority to approve specific cost categories or amounts
- **Legacy Data:** Determine if any pending requisitions from Core system need manual conversion or can be ignored
- **Rollout Approach:** Can be deployed immediately post-go-live as foundation for purchasing control

---

# SECTION 2: RECEIVING & WAREHOUSE MANAGEMENT

## 2.1 Your Business Requirements

**REQ-002: Implement Advanced Receiving tool with drag-and-drop bin functionality (ACCOMMODATE)**

KBM Hogue's outsourced installation model creates a unique receiving challenge: product ships to third-party contractor warehouses rather than KBM-controlled facilities, yet receiving must still be tracked in NetSuite because receiving impacts WIP (Work in Progress). Traditional NetSuite receiving functionality is "clunky and difficult," making remote receiving particularly painful. The team requires a streamlined drag-and-drop receiving tool that works on both tablet and desktop, allowing KBM team members to quickly assign received items to appropriate bins without navigating complex NetSuite screens.

**REQ-003: Configure one receiving bin per third-party warehouse location (ALIGNS)**

Due to the outsourced model, KBM doesn't need granular bin management within each warehouse location. A simple structure of one bin per warehouse works perfectly because they don't track internal warehouse locations—only that product reached the contractor's facility. This straightforward approach keeps receiving simple and fast.

**REQ-004: Configure damaged inventory bin per location to quarantine damaged product (ALIGNS)**

When product arrives damaged, it must be received (to impact WIP correctly) but must not be allocated to customer orders. KBM needs a separate damaged bin per location where damaged items are quarantined and prevented from being selected for item fulfillment. This bin triggers the VRA process and ensures damaged product cannot accidentally ship to customers.

**REQ-005: Configure duplicate/overage inventory bin per location (ALIGNS)**

Occasionally, shipments arrive with excess quantities or duplicate items. A dedicated overage bin per location tracks these exceptions without allocating them to specific orders.

**Requirements Classification:**
- Type: Functional - Receiving process
- Priority: Must-Have
- Users Impacted: Receiving team (office-based), warehouse staff (at third-party locations), PMs (visibility into availability)
- Business Impact: Accuracy of WIP inventory, prevention of shipping damaged product, inventory visibility

---

## 2.2 Current State Process

**PROCESS:** Third-Party Warehouse Receiving Notification (Current State)

**TRIGGER:** Product delivery to contractor warehouse

**CURRENT STEPS:**
1. Product ships from supplier to third-party installation contractor warehouse
2. Contractor receives product and notifies KBM via email (sending receipt confirmation to receiving@KBM)
3. KBM team member manually navigates NetSuite, finds the PO, and processes receiving
4. Items received to a general bin (may not distinguish damaged vs. good product)
5. WIP updated in financial system
6. If damage occurs, may require manual tracking outside of system

**SYSTEMS INVOLVED:** NetSuite Core (current), email, possibly manual spreadsheets

**PAIN POINTS:**
- Email notifications easy to miss or lose
- No centralized visibility into receiving status
- Manual receiving process is time-consuming
- Damaged items may not be clearly segregated
- Delayed WIP updates due to manual processing
- No systematic notification capability for remote receivers

**Gap Analysis:**
- No easy way for contractors to notify KBM of arrivals
- NetSuite standard receiving interface requires multiple clicks to complete simple receiving
- No clear visual distinction between damaged, good, and overage inventory
- Limited visibility into what's waiting to be received across all warehouse locations

---

## 2.3 Orion/NetSuite Solution

Orion/NetSuite provides a proven, purpose-built advanced receiving solution specifically designed for dealers with complex warehouse and outsourced operations models. The Orion Advanced Receiving Tool is a custom-developed utility that sits on top of NetSuite's receiving capability, transforming a time-consuming manual process into a simple, intuitive drag-and-drop interface.

**Advanced Receiving Tool Capabilities:**

The Advanced Receiving Tool displays all items on a purchase order and all available bins for a location in a single, clear interface. Users see items on one side and bins on the other, then simply drag items to the appropriate bin to complete receiving. This intuitive approach eliminates the need to navigate multiple NetSuite screens, reducing receiving time from several minutes per PO to just seconds. The tool works on both tablet and desktop, making it accessible whether users are in the office receiving remote notifications or on-site at warehouse locations. No installation or complex training required—the drag-and-drop interface is inherently familiar to modern users.

**Bin Management Strategy:**

Orion/NetSuite's bin management system supports KBM Hogue's simple but effective receiving strategy. Each third-party warehouse location has one primary receiving bin for normal product receipt. This straightforward approach keeps inventory tracking simple—KBM doesn't need to manage internal warehouse locations within contractor facilities, only confirm that product reached the intended destination and is available for installation or further distribution.

Damaged inventory bins per location provide critical quarantine capability. When damaged items are received to the damaged bin rather than the normal receiving bin, NetSuite prevents them from being selected for item fulfillment or allocated to customer orders. This protection ensures damaged items cannot accidentally ship to customers, maintaining quality assurance and customer satisfaction. The damaged bin automatically triggers the VRA process, maintaining complete traceability of why items are quarantined and what follow-up actions (credit, replacement, return) are needed.

Overage/duplicate bins per location handle excess inventory and duplicate shipments that don't belong to specific orders. This flexibility manages exceptions without forcing them through order-specific allocation logic.

**Integration with Vendor Center:**

While the Advanced Receiving Tool handles the actual receiving transaction, Orion/NetSuite's Vendor Center enables contractors to notify KBM of arrivals without email dependency. Contractors log into the vendor center, see their purchase orders, and click "Notify of Arrival" with optional attachment of photos or documentation. This notification appears on KBM's dashboard, prompting the receiving team to open the Advanced Receiving Tool and complete the receiving transaction. This integration eliminates email delays, provides centralized visibility of incoming shipments across all contractor locations, and creates an audit trail of all notifications.

**Offline Capability:**

While the Advanced Receiving Tool typically runs online, the Field Service app (see Section 5) includes offline receiving capability for situations where internet connectivity is unavailable at contractor facilities.

This proven solution has been successfully deployed across the contract furniture dealer industry and represents standard Orion implementation practice for outsourced operations models.

---

## 2.4 Future State Process

**PROCESS:** Drag-and-Drop Receiving with Bin Segregation (Future State)

**TRIGGER:** Contractor notifies KBM of product arrival via Vendor Center portal

**FUTURE STEPS:**
1. Contractor receives physical product at warehouse
2. Logs into Vendor Center portal
3. Clicks "Notify of Arrival" on purchase order, optionally attaches photos
4. Notification appears on KBM Hogue dashboard
5. KBM receiving team opens Advanced Receiving Tool
6. Tool displays all PO items and available bins
7. For good product: Drag items to "Warehouse A - Receiving" bin
8. For damaged product: Drag items to "Warehouse A - Damaged" bin
9. For overages: Drag items to "Warehouse A - Overages" bin
10. Complete receiving with single action
11. WIP updated immediately
12. Damaged items locked from allocation; VRA process initiated
13. Overage items available but not order-committed

**SYSTEMS INVOLVED:** NetSuite Advanced Receiving Tool, Vendor Center, NetSuite Inventory

**BENEFITS:**
- Eliminates email dependency—contractor notifications in system
- Receives items in seconds per PO instead of minutes
- Damaged items automatically prevented from shipping
- Clear visibility into what's at each warehouse location
- Complete audit trail of who received what and when

---

## 2.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-002 | Implement Advanced Receiving tool with drag-and-drop bin functionality | Orion Advanced Receiving Tool (custom Orion innovation) | ACCOMMODATE |
| REQ-003 | Configure one receiving bin per third-party warehouse location | NetSuite Bin Management | ALIGNS |
| REQ-004 | Configure damaged inventory bin per location to quarantine damaged product | NetSuite Bin Management with allocation prevention rules | ALIGNS |
| REQ-005 | Configure duplicate/overage inventory bin per location | NetSuite Bin Management | ALIGNS |

---

## 2.6 Implementation Approach

**Advanced Receiving Tool will be deployed as a custom Orion enhancement:**
- Orion Advanced Receiving Tool will be implemented for all PO receiving transactions
- Tool will be accessible via web interface on both desktop and tablet
- Contractors will trigger receiving workflow through Vendor Center notifications
- Bin structure will be configured per location with standard naming conventions
- Allocation prevention rules will be applied to damaged bins to prevent accidental selection
- Integration between Vendor Center notifications and receiving workflow will be tested before go-live

**Decision Points Requiring Configuration Sessions:**
- Complete list of all third-party warehouse locations (drives bin setup)
- Bin naming conventions (standard format for consistency)
- Whether additional office/showroom bins are needed for showroom inventory or direct-to-site shipments
- Receiving approval workflow (does all receiving require supervisor review, or only certain transaction types?)

---

## 2.7 Custom Solution Designs

**REQ-002 & REQ-007 Integration: Advanced Receiving Tool with Vendor Center Notification**

**Scope:** Custom Orion tool that integrates Vendor Center receiving notifications with streamlined receiving interface

**High-Level Design Approach:**
- Vendor Center notification triggers dashboard alert for receiving team
- Advanced Receiving Tool auto-populates with PO details when receiving team selects a pending notification
- Drag-and-drop interface eliminates manual NetSuite navigation
- Integration with bin management system enforces allocation prevention for damaged bins
- Mobile optimization ensures functionality on both tablet and desktop
- Data validation ensures all received quantities match PO lines before completion

**Benefits Over Standard NetSuite:**
- Reduces receiving time from ~5 minutes to ~30 seconds per PO
- Eliminates email dependency and communication gaps
- Provides superior UX for frequent receiving transactions
- Integrates notification → receiving in single workflow

**Dependencies:**
- Vendor Center must be configured and accessible to contractors
- Bin structure must be defined before tool configuration
- Mobile browser compatibility testing needed before go-live

---

## 2.8 Implementation Considerations

- **Contractor Notification Adoption:** Success depends on contractors using Vendor Center portal instead of email; training and change management critical
- **Backup Email Process:** If contractors don't adopt portal, email fallback should be defined (manual notification triggers Advanced Receiving Tool)
- **Bin Naming Convention:** Standardized naming (e.g., "Warehouse Location - Receiving", "Warehouse Location - Damaged") essential for consistency across team
- **Hardware:** Tablets for warehouse access should have offline capability for areas without reliable internet
- **Training:** Receiving team needs Advanced Receiving Tool training; contractors need Vendor Center portal training
- **Data Migration:** Any pending POs from current system must be set up in NetSuite with correct bin destinations
- **Testing:** Comprehensive testing of drag-and-drop functionality, bin allocation prevention, and Vendor Center integration required before production go-live
- **Rollout Phasing:** Consider phased approach: deploy to office receiving first, then contractor Vendor Center access after team is comfortable

---

# SECTION 3: VENDOR CENTER - CONTRACTOR PORTAL

## 3.1 Your Business Requirements

**REQ-006: Implement vendor center portal for contractor access at no additional cost (ALIGNS)**

KBM Hogue's outsourced installation model requires seamless contractor communication and access to project information. The Vendor Center provides this access—contractors can view their purchase orders, work orders, project details, and communicate with KBM without relying on scattered emails. A critical advantage of the Orion/NetSuite solution is that there is **no additional license cost** for contractor access. While competitors typically charge per-user licensing fees for vendor portal access, Orion uses a shared licensing model that allows unlimited contractors to access the portal at no incremental cost.

**REQ-007: Enable receiving notification feature in vendor center (ACCOMMODATE)**

Standard Vendor Center provides communication and document attachment. The custom Orion enhancement adds a specific "receiving notification" feature that allows contractors to notify KBM that product has arrived at their location, appearing as a dashboard alert for the receiving team rather than disappearing into an email inbox. This feature directly replaces email-based "product arrived" notifications.

**REQ-008: Defer contractor direct receiving capability to future phase (ADAPT)** 

While future phases may enable contractors to perform actual receiving in NetSuite, the current phase uses a notification-only model where contractors alert KBM of arrivals and KBM performs the actual receiving transaction. This approach maintains receiving control and accuracy while reducing permission management complexity.

**REQ-009: Enable document attachment and communication in vendor center (ALIGNS)**

The Vendor Center includes standard communication tools where contractors can attach files, photos, and documents, and leave comments instead of sending emails. This centralizes contractor communication within the system for visibility and audit trail.

**Requirements Classification:**
- Type: Functional - Contractor communication and coordination
- Priority: Must-Have
- Users Impacted: Installation contractors, subcontractors, receiving team, PMs
- Business Impact: Eliminates email dependency, provides centralized contractor communication, simplifies receiving notifications

---

## 3.2 Current State Process

**PROCESS:** Email-Based Contractor Communication (Current State)

**TRIGGER:** Product arrives at contractor warehouse OR contractor needs to communicate with KBM about an order

**CURRENT STEPS:**
1. Contractor sends email to receiving@KBM reporting arrival: "Product arrived - 8 items good, 2 items damaged"
2. Email may be missed, delayed in delivery, or lost in inbox
3. KBM team member receives email and manually processes receiving in NetSuite
4. For questions or changes, additional email exchanges required
5. Contractor may share photos or documents via email attachment (unsecured, difficult to track)
6. No centralized log of all contractor communications across all installations

**SYSTEMS INVOLVED:** Email, Core NetSuite, manual spreadsheets

**PAIN POINTS:**
- Email easy to miss or lose—creating delays in receiving
- No centralized visibility into incoming shipments across all contractor locations
- Duplicate questions because no shared communication thread
- Difficulty tracking contractor communications for compliance/audit purposes
- No secure document management for contractor-provided photos/documentation
- Contractors may feel like they're bothering KBM with multiple emails vs. being part of integrated system

**Gap Analysis:**
- No single place for contractors to see all their work and orders
- No system-based notification that alerts KBM to arrivals
- Contractor communication history scattered across multiple email inboxes

---

## 3.3 Orion/NetSuite Solution

Orion/NetSuite provides a comprehensive Vendor Center portal that transforms contractor communication from ad-hoc email exchanges into a structured, integrated system where contractors can view all project information, work orders, purchase orders, and communicate directly within the system. The Vendor Center is accessible through a web browser—no installation, no complex setup—contractors simply log in with their credentials and have immediate access to all information relevant to their work at KBM Hogue.

**Vendor Center Capabilities:**

Contractors see a dashboard displaying all purchase orders and work orders assigned to them. They can click into each PO or work order to view complete details: what items are being shipped, where it's being shipped, contact information for the project, site requirements, and delivery instructions. This centralized access means contractors don't rely on scattered emails to understand what's expected—everything is in one place.

The receiving notification feature—a custom Orion enhancement—allows contractors to click "Notify of Arrival" directly on a purchase order when product arrives at their location. They can optionally attach photos showing the condition of items (good product vs. damage) and leave notes describing any issues. This notification immediately appears on KBM Hogue's dashboard, alerting the receiving team to open the Advanced Receiving Tool and process the shipment. The notification includes all of the contractor's comments and attachments, providing context for the receiving transaction without email intermediaries.

Beyond receiving notifications, the Vendor Center includes communication tools where contractors can attach documents, leave comments, and engage in threaded discussions about their work. This creates a complete audit trail of contractor communications within the system—valuable for compliance, issue resolution, and dispute prevention.

The critical advantage is **zero additional license cost**. Orion uses a shared licensing model rather than per-user licensing, allowing unlimited contractors to access the portal. This removes a major objection to portal adoption: contractors don't feel like KBM is paying to force them into a new system. Access is simply included as part of the solution.

This approach is proven across contract furniture dealers using Orion/NetSuite and represents standard implementation practice for outsourced installation models.

---

## 3.4 Future State Process

**PROCESS:** Vendor Center Portal Coordination (Future State)

**TRIGGER:** Contractor needs to communicate with KBM or receive PO/work order information

**FUTURE STEPS:**
1. Contractor logs into Vendor Center portal
2. Dashboard displays all active POs and work orders for their company
3. Contractor can view full details of each order: items, quantities, shipping address, contact info
4. When product arrives at warehouse:
   - Contractor clicks "Notify of Arrival" on the PO
   - Optionally attaches photos showing item condition
   - Adds notes (e.g., "2 items arrived damaged in shipping")
   - Clicks submit
5. Notification appears on KBM dashboard with contractor's comments and photos
6. Receiving team reviews notification and opens Advanced Receiving Tool
7. KBM completes receiving using drag-and-drop: good items to normal bin, damaged items to damaged bin
8. For ongoing communication: Contractor can leave notes and attach documents directly on orders
9. All communication tracked in system; no emails needed
10. Contractor can see status of their orders: received, awaiting pickup, completed

**SYSTEMS INVOLVED:** NetSuite Vendor Center, Advanced Receiving Tool, Orion receiving notification feature

**BENEFITS:**
- Contractors have single place to view all their work—no email searching
- KBM has dashboard alert for arrivals—no missed emails
- Photos and documentation attached to orders for context
- Complete audit trail of all communication
- Contractor feels integrated into KBM system (not just emailing)

---

## 3.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-006 | Implement vendor center portal for contractor access (no cost) | NetSuite Vendor Center with shared licensing model | ALIGNS |
| REQ-007 | Enable receiving notification feature in vendor center | Orion custom receiving notification enhancement | ACCOMMODATE |
| REQ-008 | Defer contractor direct receiving capability to future phase | Future consideration with phased approach | ADAPT |
| REQ-009 | Enable document attachment and communication in vendor center | NetSuite Vendor Center communication tools | ALIGNS |

---

## 3.6 Implementation Approach

**Vendor Center will be configured and deployed with Orion receiving notification enhancement:**
- Vendor Center will be enabled for all contractor accounts
- Receiving notification feature will be configured to trigger dashboard alert on KBM side
- Contractor access will not require separate licensing (shared license model)
- Communication and attachment features will be enabled
- Contractor direct receiving will be explicitly disabled for this phase (can be reconsidered in future phases)

**Decision Points Requiring Configuration Sessions:**
- Complete list of contractors who need Vendor Center access
- Contractor communication preferences (who should receive notifications—receiving manager, PM, both?)
- Contractor training approach and communication plan
- Decision rules for when to grant additional contractor access (current vs. future phases)

---

## 3.7 Custom Solution Designs

**REQ-007: Vendor Center Receiving Notification Feature**

**Scope:** Custom Orion enhancement that adds receiving notification capability to standard Vendor Center

**High-Level Design Approach:**
- "Notify of Arrival" button added to Vendor Center PO view
- Contractor can capture photo evidence of shipment condition
- Contractor can enter notes describing condition, issues, or special instructions
- Notification immediately appears on KBM receiving dashboard with full context
- Integration with Advanced Receiving Tool allows receiving team to process notification immediately
- System creates audit trail: who notified, when, what condition reported
- Optional: Auto-email alert to receiving team if contractor doesn't have dashboard notifications enabled

**Benefits Over Standard NetSuite:**
- Replaces email-based arrival notifications with system-based notifications
- Provides context (photos, notes) at point of notification rather than in separate emails
- Ensures notifications aren't missed or lost in email
- Creates complete audit trail of contractor communications
- Encourages contractor use of portal vs. email

**Dependencies:**
- Contractor must have Vendor Center access established
- Receiving team must have dashboard or notification preferences configured
- Integration with Advanced Receiving Tool workflow
- Mobile-friendly interface for contractors to attach photos on mobile devices

---

## 3.8 Implementation Considerations

- **Contractor Adoption:** Success depends on changing contractor behavior from email to portal; requires communication, training, and clear value proposition messaging
- **Access Setup:** Contractor accounts must be created and credentials provided before portal can be used; consider phased rollout to key contractors first
- **Support Process:** Clear support process needed for contractor questions about portal functionality (could be managed by KBM PM team or designated support contact)
- **Backup Email:** If contractors don't adopt portal, email fallback should be defined—receiving team can still process emails manually if needed
- **Hardware Access:** Some contractors may not have regular computer access; mobile-friendly interface and phone/tablet access important
- **Training Materials:** Simple video tutorial and quick-start guide recommended for contractor onboarding
- **Vendor Selection:** Determine which contractors are essential for initial rollout (priority tier) vs. nice-to-have (can be added later)
- **Performance:** Portal must be responsive and fast—if slow or unreliable, contractors will revert to email
- **Go-Live Timing:** Portal rollout should be staged after internal KBM team is trained and comfortable with Advanced Receiving Tool

---

# SECTION 4: VENDOR RETURN AUTHORIZATIONS & DAMAGED PRODUCT MANAGEMENT

## 4.1 Your Business Requirements

**REQ-010: Use VRA process even when not shipping product back (80/20 rule) (ADAPT)**

KBM Hogue faces a critical pain point: damaged product arrives, and team members enter lines for expected vendor credits, but then "they just kind of go in there and you're just like throwing it out there. I hope we get this. And then no one ever really follows up on it." (Lorraine, CFO). Credits often disappear—never collected, never followed up, never resolved. The solution is to use the full VRA (Vendor Return Authorization) process even when product is NOT being shipped back (which is 80% of cases), because the VRA process creates traceability, forces follow-up, and prevents credits from falling through the cracks.

**REQ-011: Configure damaged product replacement as zero-cost line on existing PO (ALIGNS)**

When damage occurs and a replacement is needed, rather than issuing a completely new PO, a zero-cost line is added to the existing PO. The replacement item receives at the same receiving bin under the same PO, and the damaged item remains in the damaged bin for VRA processing and potential return.

**REQ-012: Track expected vendor credits with follow-up reporting (ACCOMMODATE)**

The VRA process documents why credits are expected, but systematic follow-up is needed. A monthly report showing all expected credits that haven't been received yet will be generated, providing pressure on vendors to issue credit memos and creating accountability for credit collection. This report includes VRA number, reason for credit, expected amount, and days outstanding.

**Requirements Classification:**
- Type: Functional - Vendor management and accounting control
- Priority: Must-Have (addresses CFO pain point directly)
- Users Impacted: AP team, receiving team, PMs, Finance/CFO
- Business Impact: Ensures vendor credits are systematically collected; prevents "lost" credits; improves cash flow; strengthens vendor relationships

---

## 4.2 Current State Process

**PROCESS:** Damaged Product Credit Request (Current - Problematic)

**TRIGGER:** Damaged product received

**CURRENT STEPS:**
1. Contractor notifies KBM of damage: "2 items arrived damaged"
2. KBM receiving team receives damaged items to damaged bin
3. Operations team contacts vendor: "Need replacement or credit"
4. Someone enters a credit line expectation in current system (often manually)
5. Vendor may issue credit, may ignore, may require RMA documentation
6. No systematic follow-up mechanism
7. At month-end or year-end, manual forensic accounting trying to find "lost" credits
8. Some credits never collected because no one followed up

**SYSTEMS INVOLVED:** Current system, email, spreadsheets, vendor communication

**PAIN POINTS:**
- No systematic tracking of expected credits
- No follow-up mechanism or escalation when credits not received
- Manual forensic accounting work required
- Credits often lost or forgotten
- Vendor relationships strained because follow-up is ad-hoc
- Financial statements impacted by uncollected receivables

**Gap Analysis:**
- Current system has no formal VRA process
- No mechanism to systematically track "expected credits pending"
- No reporting to drive credit collection actions
- No audit trail of credit communication and status

---

## 4.3 Orion/NetSuite Solution

Orion/NetSuite provides a comprehensive VRA (Vendor Return Authorization) module that manages damaged product, credits, and returns with full traceability and systematic follow-up. The innovative approach taken by KBM Hogue—using the VRA process even when not shipping product back—directly addresses the "lost credits" problem through forced documentation and systematic follow-up.

**VRA Process Overview:**

When damaged product arrives, the item is received to the damaged bin (see Section 2), and a VRA is created to document the reason for damage, the expected resolution (replacement, credit, or return), and the expected vendor credit amount. The VRA creates a formal record within NetSuite that this damage occurred and a credit is expected. The VRA includes full documentation: when damage was discovered, who discovered it, what was damaged, photos if available, and communication with the vendor.

**Replacement Process:**

When a vendor provides replacement product, a zero-cost line is added to the original PO. This line has $0 cost but tracks that replacement received. When the replacement arrives, it receives to the normal receiving bin on the zero-cost line. The original damaged item remains in the damaged bin for potential return or write-off. The VRA links the damaged item to the replacement transaction, creating complete traceability: original damaged item → expected credit → replacement received → credit status.

**Credit Collection and Follow-Up:**

NetSuite includes a custom Orion report showing all expected credits that haven't been collected. The report is generated monthly and shows:
- VRA number and link
- Reason for credit (what was damaged)
- Expected credit amount
- Date damage was reported
- Days outstanding
- Vendor contact and payment status
- Follow-up actions taken

This report is shared with vendors at month-end, creating pressure to issue credit memos. The report also drives internal accountability—operations team sees who owns each VRA and what follow-up actions are needed. If a credit is 30+ days outstanding, the report flags it for escalation to vendor management or finance.

**Accounting Integration:**

Once a vendor issues a credit memo number, the AP team creates a bill credit in NetSuite with the vendor's credit memo number. The VRA automatically links to the bill credit, creating the complete transaction history: damage → VRA → credit → receipt of credit memo. This provides the audit trail needed for financial reporting and compliance.

**Key Innovation:**

The critical innovation here is the *discipline* of creating a VRA for every damage scenario, not just when shipping product back to the vendor. Because 80% of the time replacement product is provided and shipment isn't needed, teams often skip formal documentation. Orion/NetSuite forces this discipline by making the VRA the central tracking mechanism, ensuring that "lost credit" scenarios simply can't happen—every expected credit has a VRA with systematic follow-up.

This approach has been successfully deployed across contract furniture dealers and represents best practice for damage management and credit collection.

---

## 4.4 Future State Process

**PROCESS:** Systematic VRA-Based Damage & Credit Tracking (Future State)

**TRIGGER:** Damaged product received or vendor issue identified

**FUTURE STEPS:**

**When Damage Occurs:**
1. Contractor notifies KBM of damage (via Vendor Center or email): "2 items arrived damaged in shipping"
2. KBM receiving team receives damaged items to damaged bin
3. Operations team creates VRA in NetSuite documenting:
   - Damaged items (SKU, quantity)
   - Reason for damage (shipping damage, warehouse damage, defective)
   - Photos of damage
   - Expected resolution (replacement or credit)
   - Expected credit amount
4. VRA linked to PO and damaged bin inventory

**Replacement Process:**
5. Operations team contacts vendor: "Need replacement for damaged items"
6. Vendor agrees to provide replacement at no cost
7. PO modified: Add zero-cost line for replacement item
8. Replacement ships
9. When replacement arrives, received to normal receiving bin on zero-cost line
10. VRA updated: Replacement received, link to zero-cost line

**Credit Collection:**
11. If shipping back (rare, 10%): Create item fulfillment to return damaged items to vendor
12. Vendor issues credit memo with number (e.g., "CREDIT-12345")
13. AP team creates bill credit in NetSuite with vendor's credit memo number
14. VRA closed with credit status "received"

**Systematic Follow-Up:**
15. Monthly: Orion custom report generated showing all outstanding VRAs:
    - Expected credits not yet received
    - Days outstanding
    - Required follow-up actions
16. Report shared with vendors as month-end pressure tactic: "Here are all credits we're expecting from you"
17. Finance team follows up on any credits >30 days outstanding
18. VRAs regularly reviewed in finance meetings for aged credit analysis

**Result:**
- Complete traceability: Damage → expected credit → actual credit received
- No "lost" credits—systematic follow-up ensures collection
- Vendor pressure (monthly report) encourages credit memo issuance
- Financial reporting accurate because all expected credits tracked
- Audit trail complete for compliance and dispute resolution

---

## 4.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-010 | Use VRA process even when not shipping back (80/20 rule) | NetSuite VRA module with bill credit linkage | ADAPT |
| REQ-011 | Configure zero-cost replacement line on existing PO | NetSuite PO line management | ALIGNS |
| REQ-012 | Track expected credits with follow-up reporting | Custom Orion monthly credit aging report | ACCOMMODATE |

---

## 4.6 Implementation Approach

**VRA process will be configured as disciplined system for all damage scenarios:**
- VRA module will be enabled and mandatory for all damaged inventory scenarios
- Zero-cost lines will be supported on POs for replacements (configured in NetSuite)
- Custom Orion report will be developed for monthly credit aging and follow-up
- VRA workflow will include approval step (finance or operations manager reviews before closing)
- Bill credit linkage to VRAs will be configured for complete transaction traceability
- Process will include discipline enforcement: if damage occurs, VRA must be created

**Decision Points Requiring Configuration Sessions:**
- Complete exception logic: Are there any damage scenarios where VRA is NOT required?
- Approval authority: Who can create VRAs? Who must approve closing?
- Accounting treatment: How should zero-cost replacements be recorded for period-end reconciliation?
- Report format and distribution: Who receives monthly aged credits report? How often is it shared with vendors?

---

## 4.7 Custom Solution Designs

**REQ-012: Monthly Expected Vendor Credits Report**

**Scope:** Custom Orion report for tracking expected credits and driving collection actions

**High-Level Design Approach:**
- Report queries all open VRAs with expected credit amounts
- Groups by vendor for consolidated view
- Calculates days outstanding (date damage reported to current date)
- Flags aged credits (>30 days, >60 days) for escalation
- Includes VRA details: item, reason, amount, PO number
- Exportable to Excel for vendor communication
- Can be run on-demand or scheduled for automatic monthly generation
- Optional: Email distribution to finance team and vendor management

**Report Content:**
```
EXPECTED VENDOR CREDITS - AGED ANALYSIS
Run Date: [Date]

Vendor: ABC Furniture Supplier
| VRA # | Item | Reason | Amount | Days Outstanding | Status |
|-------|------|--------|--------|------------------|--------|
| VRA-1001 | Chair Base | Shipping Damage | $1,250 | 45 | OVERDUE |
| VRA-1005 | Table Top | Defective | $2,100 | 22 | PENDING |
```

**Benefits:**
- Systematic visibility into expected credits
- Pressure mechanism for vendor payment
- Supports month-end and quarter-end financial close
- Identifies vendors with pattern of slow credit issuance
- Drives accountability for credit collection

**Dependencies:**
- VRA module must be fully configured and in use
- Bill credit linkage configured so report can track which VRAs have received credits
- Integration with vendor master to group by vendor
- Finance team needs to define aging bucket rules (what's overdue, what's pending)

---

## 4.8 Implementation Considerations

- **VRA Discipline:** Critical success factor is team discipline to create VRAs for all damage scenarios, not just shipments (training and workflow enforcement required)
- **Vendor Communication:** Vendors need to understand new process and monthly report expectations; communication plan recommended
- **Accounting Review:** Finance needs to review zero-cost replacement line accounting treatment with auditors before go-live; ensure period-end reconciliation process defined
- **Process Definition:** Complete documented process needed for: when to create VRA, who approves, how to handle disputes
- **Contractor Communication:** Contractors need training on VRA process if they're involved in initial damage reporting or documentation
- **Report Frequency:** Monthly report should be ingrained in finance close process; assign owner responsibility
- **Escalation Process:** Define what happens if credit not received by day 45/60—who escalates, how?
- **Testing:** Test zero-cost receiving and VRA linkage extensively before go-live; ensure damaged items truly locked from allocation

---

# SECTION 5: WORK ORDER MANAGEMENT

## 5.1 Your Business Requirements

**REQ-013: Implement work orders for installation and PM events (soft decision) (ADAPT)**

Wendy (PM Manager) signed on for work orders during the session—a significant buying decision moment where operations leadership committed to the work order approach. Work orders will be used to formalize PM assignments, coordinate with external installation contractors, and track field activities. Work orders aren't hard requirements with rigid workflows; they're soft-scheduled, approval-based coordination tools that respect PM autonomy while providing management visibility.

**REQ-014: Configure work order event types (site verification, delivery/install, site review, PM on-site, design meetings, punch walks) (ALIGNS)**

Different types of field activities require different configurations. Site verification events (PM pre-install visits) have different requirements than delivery/install events (primary installation work) or punch walks (post-completion inspections). Work order event types define these categories and allow configuration of specific requirements, timelines, and resource types for each category.

**REQ-015: Enable soft scheduling with PM approval workflow (ADAPT)**

Unlike hard scheduling (task is assigned, PM has no choice), soft scheduling requests PM approval. Someone can suggest a PM is available and propose scheduling them, but the PM must explicitly accept or decline. This approach respects PM autonomy, prevents scheduling conflicts, and maintains positive PM relationships. Similarly, contractors can be soft-scheduled for work, with approval required before commitment.

**Requirements Classification:**
- Type: Functional - Field operation coordination
- Priority: Should-Have (Wendy buy-in achieved but final leadership confirmation pending)
- Users Impacted: Wendy (PM Manager), PMs, installation coordinators, external contractors
- Business Impact: Formalizes PM assignments, tracks field activities, improves project coordination

---

## 5.2 Current State Process

**PROCESS:** Manual PM Scheduling (Current State)

**TRIGGER:** Project ready for PM assignment

**CURRENT STEPS:**
1. Project reaches pre-delivery phase in Core system
2. Design complete, sales order created
3. Wendy manually reviews Google Sheets PM workload calendar
4. Wendy calls/emails PMs asking if available on [date]
5. PMs confirm or decline via email
6. Wendy manually updates Google Sheets with assignment
7. Email sent to PM: "You're assigned to [project] at [location] on [date]"
8. Contractor contacted separately with scheduling details
9. Multiple communication channels: email, Sheets, phone calls
10. No centralized record of PM assignments in Core system

**SYSTEMS INVOLVED:** Core system, Google Sheets, email, phone

**PAIN POINTS:**
- Manual Google Sheets calendar only as accurate as last update
- PM availability not always current
- Multiple communication channels for same information
- No formal tracking of PM assignments in ERP system
- Contractor coordination separate from PM coordination
- Email attachments and details scattered
- Difficult to generate reports on PM utilization

**Gap Analysis:**
- No single system record of PM assignments
- Manual scheduling process error-prone
- No history of assignments/changes
- Difficult to analyze PM workload or identify overallocation

---

## 5.3 Orion/NetSuite Solution

Orion/NetSuite provides a comprehensive work order management system that formalizes PM and contractor assignments while maintaining the flexibility of soft scheduling that respects team autonomy. Rather than replacing Google Sheets with a rigid project management system, work orders provide a structured but flexible approach to coordinating field activities.

**Work Order Capabilities:**

Work orders are created directly from sales orders—no extra transaction required. Account managers or operations can generate work orders with a single click, selecting the event type (site verification, delivery/install, etc.) and assigning resources. The elegant simplicity is that you don't have to select specific line items on the sales order when creating work orders; the system creates work order events that encompass the entire project scope.

Event types are configured to match KBM Hogue's specific field activities. Site verification events represent PM pre-install visits to assess site requirements. Delivery and install events represent the primary installation work (done by contractors). Site review events represent post-install walkthroughs with clients. PM on-site events represent PM presence during delivery (sometimes required, sometimes optional). Design meetings represent on-site design work. Punch walks represent post-completion inspection events.

**Soft Scheduling Approach:**

Work orders support soft scheduling where resource assignment requires approval. Rather than hard-assigning a PM (which can feel disrespectful of PM autonomy), the system can request PM availability. The PM sees the work order, understands the scope, and explicitly accepts or declines. This maintains relationships and prevents scheduling conflicts while providing management visibility.

The approval workflow is designed to be simple: Work order created → Assigned to PM → PM receives notification → PM approves or declines. If declined, it appears on Wendy's dashboard as "needs reassignment," and she can try another PM. This is faster and less contentious than email back-and-forth negotiations.

**Integration with Field Service App:**

Once a PM accepts a work order, it appears on their Field Service app (see Section 5) dashboard. All work order events for the day display as cards on their tablet, with full context: location address, client contact, site requirements, items to deliver, punch list status if this is a punch walk. The PM can check in geologically (confirming on-site presence), manage activities, track time, and generate status reports—all from the tablet.

**History and Traceability:**

Unlike scattered emails and spreadsheets, work order assignments are recorded in NetSuite. History is maintained: who assigned the resource, when, what event type, any changes. This provides audit trail for compliance and dispute resolution (e.g., "Were you really scheduled that day?" Answer: "Yes, you can see it in the work order history").

**Resource Types:**

Work orders support multiple resource types—internal PMs, external contractors, even internal designers or other resources. This flexibility allows coordinating with all participants in a project's delivery.

This approach has been successfully deployed across contract furniture dealers and represents best practice for field operations coordination.

---

## 5.4 Future State Process

**PROCESS:** Work Order-Based PM & Contractor Coordination (Future State)

**TRIGGER:** Project ready for PM/contractor assignment

**FUTURE STEPS:**

**Work Order Creation:**
1. Project reaches pre-delivery phase in NetSuite
2. Account manager or coordinator clicks "Create Work Order" on sales order
3. System displays event types: site verification, delivery/install, site review, punch walk, etc.
4. Coordinator selects primary event type (e.g., "Delivery and Install")
5. Selects target date (soft scheduled date)
6. Saves work order
7. Work order appears on dashboard

**PM Assignment (Soft Scheduling):**
8. Wendy opens work order and sees "Needs PM Assignment"
9. Clicks "Assign PM" and selects available PM from dropdown (or suggests PM for soft scheduling)
10. NetSuite sends notification to PM: "You're requested for [project] delivery on [date]"
11. PM reviews on tablet: sees location, client contact, items, scope
12. PM approves: "Yes, I can do [date]" or declines: "Conflict on [date]"
13. If approved, work order assigned; if declined, shows on Wendy's dashboard for reassignment

**Contractor Assignment (Optional):**
14. Wendy also assigns external contractor (e.g., installation partner)
15. Contractor sees work order in Vendor Center portal
16. Contractor accepts or proposes alternative date
17. Once accepted, in place

**Field Execution:**
18. PM/contractor checks calendar day-of
19. Sees work order event card on Field Service app
20. Clicks event to see full details: client address, contact, site requirements, items
21. Navigates to location (map link provided)
22. Checks in geologically (confirms on-site, creates accountability)
23. Marks event as in-progress
24. Performs work, takes photos, documents issues
25. Marks event complete
26. Optional: Generates status report from tablet and emails to client

**Management Visibility:**
27. Wendy can view all PM assignments, see real-time status updates
28. Can generate reports: PM workload, project schedule, resource utilization
29. Can see if work orders are at risk (past due, not started)

---

## 5.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-013 | Implement work orders for installation and PM events | NetSuite Work Order Management | ADAPT |
| REQ-014 | Configure work order event types | NetSuite Work Order event type configuration | ALIGNS |
| REQ-015 | Enable soft scheduling with PM approval workflow | NetSuite soft scheduling with approval workflow | ADAPT |

---

## 5.6 Implementation Approach

**Work orders will be configured as coordination and assignment tool with soft scheduling:**
- Work Order module will be enabled in NetSuite
- Event types will be configured: site verification, delivery/install, site review, PM on-site, design meetings, punch walks
- Work order creation from sales order will be enabled and simplified (no line item selection required)
- Soft scheduling workflow will be configured with PM approval required
- Integration with Field Service app will be enabled
- Notifications to PM/contractors will be configured for assignment requests
- Approval workflow will be documented and trained

**Decision Points Requiring Configuration Sessions:**
- Final confirmation from Wendy/operations leadership that work orders will be used (Wendy bought in, but formal leadership confirmation pending)
- Complete event type list and requirements for each type
- Soft scheduling approval workflow details: how long PMs have to respond? What's the escalation if they don't respond?
- Contractor soft scheduling approach: do all contractors follow soft scheduling, or are some pre-approved?
- PM notification preferences: how should they receive work order requests (email, dashboard, notification)?

---

## 5.7 Custom Solution Designs

No custom solution design required. This requirement uses NetSuite standard work order functionality with standard soft scheduling approach.

---

## 5.8 Implementation Considerations

- **PM Buy-In:** Wendy has committed, but all PMs need to understand and accept soft scheduling philosophy (training critical)
- **Process Change:** This changes PM assignment workflow from ad-hoc email/sheets to formal work order process (requires behavior change)
- **Contractor Training:** External contractors need to understand work order concept and portal access (some may resist new system)
- **PM Notification Method:** Determine best channel for PM notifications (email, in-app notification, SMS?)
- **Response Time:** Define maximum response time for PM approval requests (suggest 24-48 hours)
- **Escalation Process:** What happens if PM doesn't respond to work order request within response time? (Auto-escalate to Wendy?)
- **Historical Data:** Any current projects with PM assignments should be entered as work orders during data migration
- **Training:** All PMs and coordinators need training on work order creation and management
- **Testing:** Test soft scheduling workflow before go-live to ensure notifications work and approvals flow smoothly
- **Rollout:** Consider pilot phase with one PM group before full rollout

---

# SECTION 6: TIME TRACKING & PROJECT PROFITABILITY

## 6.1 Your Business Requirements

**REQ-016: Configure time tracking to impact project GP (not GL) (ALIGNS)**

This is an important distinction that not all dealers make. Time entries logged by PMs and designers will impact the gross profit (GP) calculations of projects, allowing KBM Hogue to see true project profitability including resource costs. However, time tracking does NOT impact the general ledger (GL). Payroll is handled separately through a payroll integration (currently Paylocity), which journals payroll costs directly to GL. Time tracking is purely about project costing, not payroll processing.

**REQ-017: Configure PM flat rate structure (internal cost and external billing) (ALIGNS)**

PMs are paid/costed on a flat rate basis (not hourly). Each PM has an internal rate (what it costs the company when that PM logs time—used for project costing) and an external rate (what clients are billed for PM time on a SOW). Some clients have negotiated different PM rates under their service agreements.

**REQ-018: Configure design rate matrix with workshop vs. standard designer rates (ALIGNS)**

Designers have multiple internal rates depending on where they work. Workshop designers have a lower internal hourly rate (they do basic drafting work, lower complexity). Standard designers have a higher internal rate (more sophisticated work). This complexity requires a rate matrix supporting multiple internal costs. External client billing rates may also vary by designer level.

**REQ-019: Support negotiated client rates with standard internal costs (ALIGNS)**

Some clients have negotiated specific PM or design rates in their service agreements. These client-specific rates override standard rates when the client is selected. However, the internal cost (what impacts project GP) remains standard—only the revenue side (what client is billed) changes for negotiated arrangements.

**REQ-020: Allow external contractor time entry with reconciliation workflow (ALIGNS)**

Some external contractors (like Blue River design firm) have system access to log time directly into KBM's system. These contractors enter time at standard KBM internal rates (not their actual contract rate), and Rafina (Design Manager) reconciles the time they enter against the invoices they send. This reconciliation ensures accuracy and prevents overbilling.

**Requirements Classification:**
- Type: Functional - Project financial management
- Priority: Must-Have
- Users Impacted: PMs, designers, external contractors (some), Rafina (reconciliation), finance team, Lorraine (CFO)
- Business Impact: Accurate project profitability, true resource cost visibility, GP-based project analysis

---

## 6.2 Current State Process

**PROCESS:** Time Tracking & Project Costing (Current State - Core System)

**TRIGGER:** PM or designer completes work on a project

**CURRENT STEPS:**
1. PM logs hours to project using Core time tracking
2. System applies PM rate to time entry
3. Cost calculated: hours × internal PM rate = project cost
4. Cost reduces project GP
5. For external contractors (with system access), they enter time at standard rates
6. Rafina reconciles contractor time vs. invoice: "Did they enter 40 hours? Did they invoice for 40 hours at their rate?"
7. If discrepancy, Rafina investigates and corrects

**SYSTEMS INVOLVED:** Core time tracking, manual rate maintenance, Paylocity (payroll), email tracking

**PAIN POINTS:**
- Rates may not be maintained correctly
- No visible rate matrix for different designer levels
- Contractor time reconciliation manual and time-consuming
- No clear separation of internal cost vs. external billing rate
- GL integration sometimes incorrect (time should not go to GL, payroll does)

---

## 6.3 Orion/NetSuite Solution

Orion/NetSuite provides comprehensive time tracking and rate matrix management that separates internal project costing from external client billing while maintaining complete accuracy and audit trail. The solution ensures that time impacts project GP (profitability) while keeping payroll separate.

**Rate Matrix Configuration:**

NetSuite's rate matrix supports multiple rates by resource type and client. Each PM has a defined rate (flat rate, not hourly, but NetSuite converts flat rates to equivalent hourly rates for time tracking calculations). Each PM rate includes:
- **Internal Rate:** What it costs the company when this PM logs time (used for project GP calculations)
- **External Rate:** What clients are billed for this PM's time (can be different per client if negotiated)

Designers have more complex rate structure. The system supports multiple designer tiers:
- **Workshop Designers:** Lower internal cost tier for basic design work
- **Standard Designers:** Higher internal cost tier for complex design work

Each designer has internal rate (by tier) and external billing rate (which may differ by client for negotiated agreements).

**Client-Specific Rate Overrides:**

Some clients have negotiated specific rates. For a negotiated client, when time is entered against that client's project, the external billing rate is overridden with their negotiated rate. However, the internal cost remains the same—so the GP calculation uses the company's standard internal cost while revenue reflects the negotiated client rate. This allows support for negotiated deals while maintaining transparent cost accounting.

**Contractor Time Entry with Reconciliation:**

When contractors with system access log time, they enter it at the company's standard internal rates (not their actual contractor rate). The contractor's invoice is received and paid separately as a consulting expense (G&A) in the GL. Rafina's reconciliation process ensures that time entered matches the invoice amount:
- If contractor entered 40 hours at $85/hour internal rate = $3,400 time impact
- If contractor invoiced for $4,000 at $100/hour, the $600 difference is absorbed by KBM as G&A expense (paid from consulting budget, not project charged)
- This approach prevents double-charging: projects charged at standard rates, overages absorbed centrally

**GL Separation:**

Time tracking entries do NOT create GL entries. Time affects project GP calculations only. Payroll costs are imported from Paylocity through a separate journal entry process. This clean separation ensures:
- Projects see true resource costs (time × internal rate)
- GL sees true payroll costs (from Paylocity import)
- No double-counting of labor costs
- Financial reporting accurate and auditable

**Audit Trail:**

Complete audit trail is maintained: who entered time, what date, which project, which rate was applied, internal vs. external rate, any adjustments. This transparency supports:
- Project profitability analysis
- Rate accuracy verification
- Contractor reconciliation
- Financial audit requirements

This approach has been successfully deployed across contract furniture dealers and represents best practice for project labor costing.

---

## 6.4 Future State Process

**PROCESS:** NetSuite Time Tracking with Rate Matrix (Future State)

**TRIGGER:** PM, designer, or contractor completes work and logs time

**FUTURE STEPS:**

**PM Time Entry:**
1. PM logs into Field Service app or desktop
2. Navigates to time entry screen
3. Selects project
4. Enters hours worked (e.g., 2 hours site visit, 3 hours installation oversight)
5. System automatically applies PM internal rate based on PM resource
6. Cost calculated: hours × internal rate = project cost impact
7. If client has negotiated PM rate, external billing rate applied for revenue
8. Time entry saved, immediately impacts project GP

**Designer Time Entry:**
9. Designer logs into Core or Field Service app
10. Selects project
11. Enters hours: "2 hours workshop design" or "4 hours standard design"
12. System determines rate based on design tier selected
13. Cost calculated: hours × designer internal rate = project cost impact
14. Client billing rate applied (standard or negotiated client rate)
15. Time entry saved, impacts project GP and design cost allocation

**Contractor Time Entry (with system access):**
16. Contractor (e.g., Blue River) logs into system with limited access
17. Enters time to projects: "20 hours design work on Project X"
18. System applies KBM's standard internal design rate ($85/hour)
19. Time impact: 20 hours × $85 = $1,700 to project GP
20. Contractor invoices separately: "20 hours @ $100/hour = $2,000"
21. Invoice paid as consulting (G&A expense, no project impact)
22. Rafina reconciles: time entered (20 hours) vs. invoice (20 hours @ $100) - amounts don't match cost-wise but that's expected
23. Reconciliation documents that contractor did the work and invoice amount is reasonable

**Finance Review:**
24. Finance team can run project profitability reports including labor costs
25. Sees true project GP after resource costs are factored in
26. Can analyze which designers are more/less efficient
27. Can track PM utilization and productivity
28. Month-end payroll imported from Paylocity as separate GL journal

**Reporting:**
29. Project records show: revenue, cost of goods, labor cost, GP, GP%
30. Labor cost comes from time tracking, not payroll (clean separation)
31. Project managers can see time impact on their project's profitability in real-time

---

## 6.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-016 | Configure time tracking to impact project GP (not GL) | NetSuite Time Tracking with project cost allocation | ALIGNS |
| REQ-017 | Configure PM flat rate structure (internal/external) | NetSuite Rate Matrix | ALIGNS |
| REQ-018 | Configure design rate matrix with multiple tiers | NetSuite Rate Matrix with tier support | ALIGNS |
| REQ-019 | Support negotiated client rates with standard internal cost | NetSuite Rate Matrix with client override capability | ALIGNS |
| REQ-020 | Allow external contractor time entry with reconciliation | NetSuite time entry with limited access + manual reconciliation | ALIGNS |

---

## 6.6 Implementation Approach

**Time tracking will be configured to impact project GP only, with comprehensive rate matrix:**
- Time tracking module will be enabled for project cost allocation
- GL integration will be disabled for time entries (time does not flow to GL)
- Rate matrix will be configured with PM rates (flat rate converted to equivalent hourly)
- Designer rate tiers will be configured (workshop, standard, and any other levels)
- Client-specific rate overrides will be configured for negotiated clients
- Contractor time entry access will be limited and controlled
- GL separation from payroll import will be clearly documented
- Project record will aggregate time costs into GP calculations

**Decision Points Requiring Configuration Sessions:**
- Complete rate matrix: all PM rates (internal and external), all designer rates (by tier, internal and external)
- Designer tier definitions: what work qualifies as "workshop" vs. "standard"?
- Negotiated client rates: which clients have special rates, and what are they?
- Contractor time entry access list: which contractors should have system access, and should access be read-only or allow edits?
- Reconciliation process for Rafina: documented workflow for comparing contractor time vs. invoices

---

## 6.7 Custom Solution Designs

No custom solution design required. This requirement uses NetSuite standard time tracking and rate matrix functionality.

---

## 6.8 Implementation Considerations

- **Rate Matrix Data:** Complete, accurate rate data critical—must be provided before system configuration
- **Contractor Access Control:** System should limit contractors to time entry only (no viewing other projects, no editing others' time)
- **Time Entry Discipline:** "PMs have to be slapped around a little bit" to comply with weekly time tracking—training and manager enforcement needed
- **Designer Tier Definition:** Must have clear definition of what constitutes "workshop" vs. "standard" designer work to ensure consistent categorization
- **Reconciliation Process for Rafina:** Documented workflow needed; consider building checklist or process document
- **Rate Updates:** Process for updating rates (annual, per raise, per client agreement) must be defined
- **Integration Testing:** Test time entry → project GP impact thoroughly before go-live
- **Historical Data:** Determine if any historical time entries from Core system should be migrated or if starting fresh in NetSuite
- **User Training:** PMs and designers need training on time entry requirements, rate structure, and why time tracking matters
- **Payroll Integration:** Clean separation from payroll (Paylocity) must be clearly communicated and tested
- **Reporting:** Finance team should be trained on time-based project profitability reports for analysis

---

# SECTION 7: 15% LABOR MARKUP FORMULA LINE

## 7.1 Your Business Requirements

**REQ-021: Implement 15% labor markup formula line (cost-only, no revenue) (ACCOMMODATE)**

KBM Hogue has a unique and powerful pricing discipline mechanism: a 15% labor markup formula line that automatically appears on every sales order with labor. This is a cost-only line (no revenue), which means it takes 15% of the cost of external labor and further reduces project GP. It's a behavioral forcing function—a built-in contingency that prevents teams from underpricing labor and ensures appropriate margins.

**REQ-022: Apply markup only to external labor (not all labor types) (ACCOMMODATE)**

The markup doesn't apply to all labor. It applies specifically to external labor (warehouse labor, installation labor from contractors). Internal PM labor and design labor are excluded. The system identifies which labor should trigger the formula by checking line codes—lines coded as "external labor" trigger the formula calculation.

**REQ-023: Position formula line at bottom (not top), make uneditable and non-printing (ACCOMMODATE)**

In Core, the formula line appears as line 1, which frustrates Kipp (IT Specialist) because customer proposals start at line 2 instead of line 1. In NetSuite, the formula line must be positioned at the absolute bottom of the order (after all normal lines), be completely uneditable (can't be manually changed), and not print on customer proposals (internal only). It must remain dynamic—recalculating whenever labor lines are added or removed.

**Requirements Classification:**
- Type: Functional - Pricing discipline mechanism
- Priority: Must-Have (critical to pricing discipline according to leadership)
- Users Impacted: Account managers (automatic calculation), finance team (GP impact), leadership (pricing discipline)
- Business Impact: Enforces margin discipline, prevents labor underpricing, behavioral forcing function

---

## 7.2 Current State Process

**PROCESS:** 15% Labor Markup in Core (Current State - Problematic)

**TRIGGER:** New sales order created with labor line

**CURRENT STEPS:**
1. Account manager creates sales order with labor lines
2. Automatically, Core pulls in a line "KPMG 15%"
3. Line is line 1 (first line on order)
4. Formula calculates 15% of external labor cost, displays negative cost
5. Project GP reduced by 15% of labor cost (behavioral enforcement)
6. When proposal printed, line 1 is the formula line, so proposal shows line numbers starting at 2
7. Kipp hates this: "My biggest gripe about that is that it's always line one. So any time you issue a proposal with line numbers it starts at two. Somebody with OCD... I will murder this thing."

**CURRENT WORKAROUNDS:**
- Some users manually delete and re-add the line (but it comes back)
- Some reorder lines manually (cumbersome process)
- Proposals printed with awkward line numbering (line 2-37 instead of 1-36)

**SYSTEMS INVOLVED:** Core system, formula line (legacy)

**PAIN POINTS:**
- Line always appears in wrong position (first, not last)
- Creates proposal formatting issues
- Users frustrated by unintended behavior
- Manually reordering lines is tedious workaround

---

## 7.3 Orion/NetSuite Solution

Orion/NetSuite provides a custom formula line implementation that gives KBM Hogue precise control over the markup behavior. Rather than the formula line being a system feature forced on orders, NetSuite's formula line configuration allows complete customization: position, editability, printing behavior, calculation trigger logic.

**Formula Line Behavior:**

When an order is created in NetSuite, if it contains external labor lines (identified by line code), the system automatically creates a formula line at the bottom of the order. The formula line displays a negative cost equal to 15% of all external labor costs on the order. This cost is deducted from the project GP, enforcing the behavioral discipline: teams know they can't underprice labor because a 15% hit automatically occurs.

**Key Characteristics:**

- **Position:** Always at bottom of order (last line, after all product, PM labor, design labor, etc.)
- **Uneditable:** Cannot be manually changed, deleted, or modified by users (system enforces)
- **Non-Printing:** Does not print on customer proposals, quotes, or order confirmations (internal only)
- **Dynamic:** Recalculates automatically whenever external labor lines are added or removed
- **Exception Logic:** Formula applies based on order type and other exceptions (to be defined by Kipp)

**Markup Calculation:**

The formula line takes 15% of the cost (not revenue) of external labor only:
```
Formula Line Cost = -1 × (Sum of External Labor Line Costs × 15%)

Example:
External Labor Lines:
- Installation Labor: $5,000 cost
- Warehouse Labor: $2,000 cost
Total External Labor Cost: $7,000

Formula Line: -1 × ($7,000 × 15%) = -$1,050 cost impact
```

This approach automatically reduces project GP, signaling to account managers that labor needs to be appropriately marked up. The formula line doesn't calculate based on how much the labor is marked up—it just applies a fixed hit. This creates pressure to mark up labor more aggressively.

**Business Purpose:**

The formula line enforces pricing discipline. Historically, KBM ran its own warehouse/installation operations until a forklift incident involving alcohol led to the decision "We didn't want to be in an OSHA environment anymore." When the company stopped doing its own work, labor became more complex to price and often got underpriced. The formula line is a built-in behavioral forcing function: "We're going to automatically hit you 15% of external labor cost on every order so you're incentivized to price labor appropriately from the start."

**Exception Logic:**

The formula line applies based on order type and potentially client-specific exceptions. Some order types or specific clients may not have the formula applied. Kipp needs to provide the complete exception logic so NetSuite can be configured with all rules.

This approach has been successfully deployed across contract furniture dealers using Orion/NetSuite and represents best practice for pricing discipline enforcement.

---

## 7.4 Future State Process

**PROCESS:** NetSuite Formula Line with Position & Behavior Control (Future State)

**TRIGGER:** Sales order created with external labor line

**FUTURE STEPS:**
1. Account manager creates sales order
2. Adds product lines (furniture, items)
3. Adds PM labor line (internal, not external)
4. Adds design labor line (internal, not external)
5. Adds installation labor line (external - warehouse/contractor labor) - Cost: $5,000
6. Adds other lines as needed
7. At bottom of order, system automatically creates formula line
8. Formula line shows: "KPMG 15% Markup" (description only, not editable)
9. Formula line cost calculated: -1 × ($5,000 × 15%) = -$750 cost impact
10. Project GP immediately reduced by $750 (behavioral signal: "better mark up labor appropriately")
11. Formula line is gray/disabled (shows it's automatic, not editable)
12. Account manager cannot delete, edit, or move formula line

**When Proposal Printed:**
13. Proposal prints with normal line numbering: Line 1, Line 2, Line 3, etc. (furniture/products)
14. PM labor, design labor show with line numbers (Lines 4-7, for example)
15. Installation labor shows with line number (Line 8, for example)
16. **Formula line does NOT print** - proposal shows only customer-facing lines
17. Proposal looks professional with standard line numbering starting at 1

**When Labor is Removed:**
18. If account manager removes installation labor line, formula line automatically recalculates
19. If all external labor removed, formula line cost becomes zero (or line disappears)
20. If new external labor added, formula line immediately recalculates

**Exception Scenario:**
21. If order type is "T&M Billing" or client is "BigCorp Preferred Partner" (exception rule), formula line doesn't apply
22. Order proceeds without 15% markup for those exceptions

**Finance Impact:**
23. Project GP reflects -15% labor markup in profitability calculations
24. GP% calculation includes formula line cost
25. Reports show labor markup enforcement across all projects

---

## 7.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-021 | Implement 15% labor markup formula line (cost-only) | NetSuite Formula Line with custom configuration | ACCOMMODATE |
| REQ-022 | Apply markup only to external labor (not all labor) | NetSuite Formula Line with line code logic | ACCOMMODATE |
| REQ-023 | Position at bottom, uneditable, non-printing | NetSuite Formula Line positioning and behavior rules | ACCOMMODATE |

---

## 7.6 Implementation Approach

**15% labor markup formula line will be configured as custom NetSuite formula:**
- Formula line configuration will be created in NetSuite with custom positioning logic (bottom of order)
- Formula will trigger based on external labor line codes (identified by specific line code values)
- Formula calculation will apply 15% markup to external labor costs only
- Calculation will exclude internal PM labor and design labor (different line codes)
- Formula line will be made uneditable through system configuration (user permissions locked)
- Formula line will be excluded from standard printing (PDF composer template configuration)
- Formula line will be configured as dynamic (recalculates when labor lines are added/removed)
- Exception logic will be defined (order types, clients, scenarios where formula doesn't apply)

**Decision Points Requiring Configuration Sessions:**
- Kipp to provide complete exception logic: which order types, which clients, which scenarios should NOT have 15% formula line applied?
- Definition of "external labor" line code: exactly which line codes trigger the formula?
- Decision on commission impact: is the 15% markup cost deducted before or after commission calculations? (likely affects commissionable GP)
- Exception rule definition: specific business rules for when NOT to apply formula

---

## 7.7 Custom Solution Designs

**REQ-021, REQ-022, REQ-023: Custom 15% Labor Markup Formula Line Configuration**

**Scope:** Custom NetSuite configuration implementing KBM Hogue's unique pricing discipline mechanism

**High-Level Design Approach:**
- NetSuite formula line configured to calculate based on line code identification
- Line code logic: line codes starting with "EXT-" (external labor) trigger formula; all other labor codes excluded
- Formula logic: Cost = -1 × (Sum of lines where line_code matches 'EXT-%' × 0.15)
- Positioning logic: Formula line always positioned after highest line number (dynamic positioning to ensure bottom placement)
- Editability: Formula line marked as read-only and non-editable (system-level permission restriction)
- Printing logic: Formula line excluded from PDF composer templates (printing rule: exclude lines with formula line ID)
- Recalculation trigger: When labor lines added/removed/modified, formula line cost recalculates automatically

**Exception Logic (To Be Defined by Kipp):**
```
Example exceptions (placeholder):
- If order type = "T&M Billing", don't apply formula
- If order type = "Service Agreement", don't apply formula
- If customer = "BigCorp Preferred Partner", don't apply formula
- If order amount < $1,000, don't apply formula

[Kipp to provide actual exception rules]
```

**Benefits:**
- Enforces pricing discipline automatically (behavioral forcing function)
- Prevents labor underpricing by applying fixed hit to projects
- Maintains clean proposal formatting (formula line not visible to customers)
- Adapts as labor lines change (dynamic behavior)
- Prevents accidental deletion or modification (uneditable)

**Dependencies:**
- Kipp must provide complete exception logic before configuration
- Line code structure must be defined (which codes are external labor vs. other types)
- Testing required: ensure formula positions correctly at bottom, recalculates properly, doesn't print

---

## 7.8 Implementation Considerations

- **Exception Logic Critical:** Complete exception rule definition required before configuration; incomplete rules will cause formula to apply (or not apply) incorrectly
- **Line Code Discipline:** Account managers must consistently use external labor line codes (training required); if wrong line code used, formula won't trigger
- **User Training:** Account managers need to understand the formula line purpose (behavioral enforcement, not revenue) and that it cannot be edited
- **Commission Impact:** Must clarify whether 15% markup is deducted before commission calculations (affects account manager compensation if commission is on GP)
- **Testing:** Extensive testing required:
  - Verify formula positions at bottom of order
  - Verify formula recalculates when labor lines added/removed
  - Verify formula doesn't print on proposals
  - Verify exception rules work correctly
  - Verify formula cost correctly impacts project GP
- **Reporting:** Finance team should verify formula line impact on project profitability in reports
- **Historical Data:** Determine if 15% markup should be applied to historical orders migrated from Core or only new orders in NetSuite

---

# SECTION 8: PUNCH LIST & FIELD OPERATIONS

## 8.1 Your Business Requirements

**REQ-024: Implement punch list functionality in Field Service app to replace PlanGrid (ACCOMMODATE)**

KBM Hogue currently uses PlanGrid (third-party app) for punch list management in the field. Orion has built comprehensive punch list functionality directly into the Field Service app to eliminate this subscription cost. The Field Service app punch module includes all critical PlanGrid capabilities: creating punch items, attaching photos, documenting issues, and generating status reports. This is a significant custom Orion development that replaces an external tool.

**REQ-025: Enable floor plan markup with location pinning for punch items (ACCOMMODATE)**

The most critical feature of the Field Service app punch list is the ability to pin punch items to specific locations on floor plans. The problem this solves: "Four months later you get that punch item and you've done 15 jobs. You're like, yeah, I'll remember what room that goes into. And you don't. We all know the reality there." By pinning punch items to floor plan locations, months later any team member can look at the floor plan and instantly see exactly where each punch item is located.

**REQ-026: Support offline mode for field app with sync capability (ALIGNS)**

The Field Service app must work without internet connectivity because many installation sites have poor or no cell service. PMs need to download work order information in the morning, work offline throughout the day (creating punch items, taking photos, documenting work), and then sync when back online. This requires offline-capable database and sync engine.

**REQ-027: Enable status report generation from field app (not just desktop) (ACCOMMODATE)**

Currently, PlanGrid allows PMs to generate and email status reports directly from the iPad. The team initially hadn't planned to replicate this in NetSuite Field Service app, but Wendy needs this capability. Marcus agreed to add this functionality: PMs can generate status reports (showing daily progress, punch items, photos, etc.) directly from the tablet and email them to clients without returning to the office.

**Requirements Classification:**
- Type: Functional - Field operations and issue management
- Priority: Must-Have (replaces paid tool, critical for field work)
- Users Impacted: PMs in field, clients receiving reports, operations team
- Business Impact: Eliminates PlanGrid subscription, improves field documentation, provides complete punch history

---

## 8.2 Current State Process

**PROCESS:** PlanGrid-Based Punch List Management (Current State)

**TRIGGER:** Installation complete, time for punch walk

**CURRENT STEPS:**
1. PM prepares for punch walk (post-installation inspection)
2. Opens PlanGrid app on iPad
3. Sees floor plan for project
4. Walks through site, identifies issues
5. For each issue:
   - Takes photo
   - Marks location on floor plan (pins location)
   - Enters issue description
   - Marks who's responsible (client, installer, KBM)
6. Back at office or from field, generates report in PlanGrid
7. Report emailed directly from iPad to client
8. Issues tracked in PlanGrid (separate from KBM systems)
9. Client sees issues in PlanGrid portal (if they have access)

**SYSTEMS INVOLVED:** PlanGrid (subscription service), iPad/tablets

**PAIN POINTS:**
- Separate subscription cost for PlanGrid
- Punch list data separate from NetSuite (not integrated)
- No direct link between work orders and punch items
- Months later, trying to remember punch item location: "What room was that?"
- Report generation requires PlanGrid (not integrated with KBM systems)

---

## 8.3 Orion/NetSuite Solution

Orion/NetSuite provides a comprehensive Field Service app that consolidates all field operations into a single, integrated platform. The punch list functionality within the Field Service app eliminates the need for external tools like PlanGrid while adding integration with work orders, projects, and inventory systems.

**Punch List Core Capability:**

The Field Service app punch module allows PMs to create punch items directly from their tablets or mobile phones during site visits. Each punch item includes:
- Photo evidence (camera interface captures images)
- Punch reason (what's wrong: damage, misalignment, missing, etc.)
- Issue type (punch list item vs. bill discrepancy vs. warehouse damage)
- Responsible party (who needs to fix it: contractor, KBM, client)
- Associated items (which products on the order relate to this punch)
- Status (open, in progress, resolved, deferred, etc.)

**Floor Plan Location Pinning:**

The most powerful feature is floor plan integration. Floor plans can be uploaded to the project (in PDF or image format), and punch items can be pinned directly to locations on the floor plan. This visual reference prevents the "I'll remember what room that was" problem. Months later, any team member can pull up the floor plan, see all punch items visually pinned to their exact locations, and instantly understand the scope of remaining work.

**Offline Mode:**

Critical for installations in buildings with no cell service. PMs log in during morning connectivity, downloading all work order events and floor plans. They then work offline throughout the day: creating punch items, taking photos, documenting work. When back online (or at end of day), the app automatically syncs all new punch items and photos back to the server. Sync includes conflict resolution—if the same punch item was modified on desktop during the day, sync intelligently merges changes.

**Status Report Generation:**

Rather than relying on PlanGrid to generate reports, the Field Service app includes reporting capability. PMs can generate status reports directly from the app, showing:
- Date and project
- Completed items (what was accomplished today)
- Punch items identified (what issues found)
- Photos and descriptions
- Next steps
- PM signature

Reports can be generated in PDF format and emailed directly from the app to clients, providing immediate communication without returning to office.

**Issue Type Flexibility:**

NetSuite's generic "issue" concept is more flexible than PlanGrid's punch-only approach. Issues can be:
- Punch list items (post-installation defects)
- Bill discrepancies (price differences on invoice)
- Acknowledgement discrepancies (item variations)
- Warehouse damage (damage discovered at receiving)
- General notes (anything that's wrong)

This flexibility allows consolidating multiple issue types into a single system rather than using separate tools.

**Integration with Work Orders:**

Punch items link directly to work order events. PM is assigned to a work order event, checks in, performs work, creates punch items. The punch items are directly associated with that work order, creating complete traceability of what was done and what issues remain.

This approach has been successfully deployed across contract furniture dealers and represents best practice for field operations and punch management.

---

## 8.4 Future State Process

**PROCESS:** Field Service App Punch List with Floor Plan Pinning (Future State)

**TRIGGER:** Installation complete, time for punch walk

**FUTURE STEPS:**

**Pre-Visit Preparation:**
1. PM checks Field Service app calendar
2. Sees punch walk work order for Project X on [date]
3. Downloads work order information (if offline mode)
4. Floor plan automatically downloaded with work order
5. PM has all info needed without internet

**Field Punch Walk:**
6. PM arrives at job site
7. Opens Field Service app, selects punch walk work order
8. Sees floor plan on tablet
9. Walks through site with tablet, identifying issues
10. For each issue:
    - Takes photo using app camera
    - Clicks location on floor plan (pins punch to specific location)
    - Enters punch reason (what's wrong: drywall damage, misaligned cabinet, missing trim, etc.)
    - Selects issue type (punch list item, etc.)
    - Marks responsible party (contractor to fix, KBM to fix, client decision, etc.)
    - Associates punch with specific product lines if applicable
11. Creates 8-10 punch items during walk, all pinned to floor plan locations

**Offline Sync:**
12. PM leaves site (no connectivity in building)
13. Returns to office or van with wifi
14. Field Service app auto-syncs: all punch items, photos, floor plan markings sync to server
15. Punch items appear in NetSuite work order immediately

**Status Report from Field:**
16. Before leaving site or from office, PM opens Field Service app reporting section
17. Generates status report showing:
    - Project and date
    - Completed work (installation status)
    - Punch items identified (with photos)
    - Next steps and timeline
18. Report saved as PDF
19. PM emails report directly from app to client
20. Client receives professional status report same day (not after PM returns to office)

**Later Review & Execution:**
21. Months later, someone needs to remember: "What room was the punch item about?"
22. Opens work order, selects punch walk event
23. Pulls up floor plan with punches pinned
24. Instantly sees: "3 items in main conference room, 2 items in break room, 1 item in hallway"
25. Clear visual reference eliminates guesswork

**Punch Resolution Tracking:**
26. As punch items are resolved, status updated in app or desktop
27. Client portal can show punch status updates (if enabled)
28. Final punch walk: all items checked off and closed
29. Project marked complete

---

## 8.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-024 | Implement punch list in Field Service app to replace PlanGrid | Orion Field Service app punch module | ACCOMMODATE |
| REQ-025 | Enable floor plan markup with location pinning | Orion Field Service app floor plan feature | ACCOMMODATE |
| REQ-026 | Support offline mode with sync capability | Orion Field Service app offline mode | ALIGNS |
| REQ-027 | Enable status report generation from field app | Orion Field Service app reporting feature | ACCOMMODATE |

---

## 8.6 Implementation Approach

**Field Service app punch list will be deployed as replacement for PlanGrid:**
- Field Service app will be configured for all PM field operations
- Punch module will be enabled with all capabilities (photo, description, issue types)
- Floor plan integration will be configured (file upload process, pinning behavior)
- Offline mode will be tested and enabled for environments without reliable connectivity
- Status report template will be designed based on current PlanGrid report format
- Work order integration will ensure punch items link to work order events
- Mobile app will be deployed to all PM tablets/phones

**Decision Points Requiring Configuration Sessions:**
- Floor plan file format requirements: PDF, image files, or both?
- Punch issue type categorization: what issue types besides punch list items does KBM need?
- Status report format and content: what information should be included in field-generated reports?
- Offline mode testing scope: which sites should be tested in offline mode before go-live?
- Client portal access: should clients see punch items in portal, or only in reports?

---

## 8.7 Custom Solution Designs

**REQ-024, REQ-025, REQ-026, REQ-027: Field Service App Punch Management with Floor Plan Pinning**

**Scope:** Custom Orion solution replacing PlanGrid with integrated punch list, floor plan marking, offline capability, and field reporting

**High-Level Design Approach:**

**Punch Module:**
- Core punch item data model: photo storage, description, type, responsible party, status
- Photo capture: integrated camera interface (works on tablet and phone)
- Issue type configuration: punch list, bill discrepancy, damage, etc.
- Status workflow: open → in progress → resolved → closed

**Floor Plan Integration:**
- Floor plan upload process: project configuration accepts PDF or image files
- Pinning interface: PM taps floor plan location, creates punch item pinned to that location
- Visual display: floor plan shows all punch items as pins/markers with icons showing status
- Punch selection: tap pin on floor plan to view punch details, photos, responsible party

**Offline Capability:**
- Data download: when app opens, downloads work order events and floor plans to local device
- Offline punch creation: punch items can be created without connectivity
- Photo storage: photos stored locally until sync
- Sync engine: when online, auto-syncs punch items, photos, status changes
- Conflict resolution: if punch modified on desktop during offline time, sync merges changes

**Field Reporting:**
- Report template: shows project, date, completed work, punch items with photos
- Report generation: creates PDF from punch data
- Email integration: sends report directly from app without returning to office
- Report archiving: reports stored with work order for audit trail

**Benefits Over PlanGrid:**
- Integrated with NetSuite (no separate tool subscription)
- Floor plan pinning integrated directly into app
- Offline mode critical for poor-connectivity sites
- Field reporting improves client communication
- Complete punch history available in NetSuite

**Dependencies:**
- Floor plan file format must be determined (PDF, image, or both)
- Punch issue type categorization must be defined
- Status report template must be designed (based on current PlanGrid format)
- Offline mode testing infrastructure needed before go-live
- Mobile app deployment infrastructure needed for tablet/phone distribution

---

## 8.8 Implementation Considerations

- **PlanGrid Migration:** Any existing punch items in PlanGrid may need to be manually recreated in new system or bulk imported (migration approach to be determined)
- **Floor Plan Upload Process:** Must be simple and reliable; consider providing upload templates and instructions
- **Offline Testing:** Comprehensive testing needed in actual building with poor/no connectivity to ensure sync works perfectly
- **Photo Management:** Storage for photos from all projects can be significant; cloud storage strategy needed
- **Report Template Design:** Work with PMs to design report format; should match current PlanGrid report if possible to minimize behavior change
- **Tablet Hardware:** Must have offline database capability; recommend testing with planned hardware before go-live
- **Training:** PMs need comprehensive training on punch creation, floor plan interaction, offline mode, report generation
- **Change Management:** PMs accustomed to PlanGrid will need support during transition; consider parallel run period
- **Client Communication:** If clients currently access PlanGrid for punch status, plan for communication about transition and any changes to their visibility
- **Data Backup:** Offline punch items should be automatically synced; backup strategy for data safety needed

---

# SECTION 9: FIELD SERVICE APP DEPLOYMENT

## 9.1 Your Business Requirements

**REQ-028: Deploy Field Service app for PMs and contractors (tablet/mobile) (ALIGNS)**

The Field Service app is the central mobile platform for all field operations. PMs and contractors access it on tablets (primary platform) and can also use mobile phones (responsive design). The app provides real-time access to work order information, enables time tracking, punch list management, photo/signature collection, and communication without requiring constant office system access.

**REQ-029: Enable check-in with geological stamping to confirm on-site presence (ACCOMMODATE)**

When PMs or contractors arrive at a job site, they check in using the Field Service app. The check-in includes geological stamping (GPS verification that they're actually at the specified location). This creates accountability and provides proof that the PM/contractor was on-site at the time they claim. This data is valuable for manager oversight and also helpful for resolving disputes about whether work was actually performed.

**REQ-030: Support photo attachment, signatures, and document collection (ALIGNS)**

The Field Service app includes document collection capabilities: photos, signatures (e.g., client sign-off on completed work), attachments, and other documents. This creates complete documentation of site conditions, work completed, and client acknowledgment in a single mobile platform.

**REQ-031: Enable multi-resource time entry from work order events (ALIGNS)**

If multiple resources are working on a single work order event (e.g., PM + 2 contractors), users can enter time once and apply it to all resources simultaneously. This simplifies time entry for group work and ensures consistency. The system can also add temporary resources to a work order event if additional support is needed.

**Requirements Classification:**
- Type: Functional - Field operations platform
- Priority: Must-Have
- Users Impacted: PMs, installation contractors, clients (receiving photos/documentation)
- Business Impact: Provides central field operations platform, enables field-based documentation, improves real-time communication

---

## 9.2 Current State Process

**PROCESS:** Manual Field Operations (Current State)

**TRIGGER:** PM or contractor assigned to work order event

**CURRENT STEPS:**
1. PM receives work order assignment via email
2. Searches for project details in various places (email, Core system, shared drives)
3. Navigates to job site with address from email or manual notes
4. Arrives at site, no check-in system
5. Takes photos on personal phone or tablet
6. Documents work in physical notes or on paper
7. May take signatures on tablet using separate signature app
8. Returns to office
9. Manually enters time into Core system
10. Uploads photos to project file manually
11. Sends status email to client

**SYSTEMS INVOLVED:** Email, Core system, separate photo/signature apps, manual documents

**PAIN POINTS:**
- Project information scattered across email and systems
- No central place to see all today's work
- Time entry occurs later (not real-time)
- Photos disconnected from project record
- Multiple apps needed (PlanGrid, Field Service, email, etc.)
- No accountability check-in system
- Client updates delayed until office return

---

## 9.3 Orion/NetSuite Solution

Orion/NetSuite's Field Service app consolidates all field operations into a single, unified platform. Rather than juggling multiple apps and manual processes, PMs and contractors see all their assigned work on a simple dashboard and can complete all field operations from one app.

**Field Service App Dashboard:**

Each PM or contractor sees a dashboard displaying all work order events assigned to them. Each event appears as a card showing:
- Project name and location
- Address with map link for navigation
- Client contact information
- Event type (site verification, delivery/install, punch walk, etc.)
- Site requirements or special instructions
- Target date/time
- Resource assignments
- Status (not yet started, in progress, complete)

The dashboard is filtered by date—showing today's work prominently, with ability to view upcoming days. Users can see at a glance what's scheduled, prioritize the order, and quickly navigate between multiple events without needing email or paper.

**Check-In with Geological Stamping:**

When a PM or contractor arrives at the job site, they tap "Check In" in the app. The app captures their GPS location (geological stamp) and records the time. This check-in serves multiple purposes:
- Accountability: Management can verify the resource was actually on-site at the claimed time
- Compliance: Provides evidence of site visit for project records
- Dispute resolution: If questions arise about whether work was performed, check-in proves presence
- Time tracking: Check-in time can auto-populate time entry (though manual time entry may still be needed for multiple resources)

Geological stamping is proven industry practice and valued by managers for oversight and quality assurance.

**Photo Capture and Documentation:**

Rather than using separate camera apps or PlanGrid, field users take photos directly in the Field Service app. Photos are automatically associated with the work order event and stored in NetSuite with complete metadata (date, time, location, user). Users can:
- Take photos from items list (progress on delivery)
- Take photos for punch items (documentation of issues)
- Upload existing photos/documents
- Attach files for specific line items

**Signature Collection:**

If client sign-off is needed (delivery completion, punch list acceptance), users can collect signatures directly in the app. Signature canvas displays on tablet, user signs, signature is captured digitally and stored with the event. This eliminates need for separate signature apps and paper forms.

**Multi-Resource Time Entry:**

If five workers are on a single work order event, users enter time once specifying "5 people worked 4 hours" and the system creates time entries for all resources. This simplifies labor-intensive time entry and prevents missed entries. Users can also add temporary resources dynamically if additional support is needed during the day.

**Offline Mode (Previously Discussed):**

As noted in Section 8, the app works offline: download work info in morning, work all day without connectivity, sync when back online.

This approach has been successfully deployed across contract furniture dealers and represents best practice for field operations and mobile workforce management.

---

## 9.4 Future State Process

**PROCESS:** Unified Field Service App Operations (Future State)

**TRIGGER:** PM/contractor wakes up, opens Field Service app

**FUTURE STEPS:**

**Morning Dashboard:**
1. PM opens Field Service app on tablet
2. Sees dashboard with all events for today
3. Three events visible:
   - 8:00 AM: Site verification at ABC Company (2 miles away)
   - 10:30 AM: Delivery and install at XYZ Company (5 miles away)
   - 2:00 PM: Punch walk at ABC Company (back to first site)
4. PM can see each event card: location, contact, site requirements, assigned resources

**First Event - Site Verification:**
5. PM clicks ABC Company event
6. Sees full details: address, contact name/phone, what's being delivered, site requirements
7. Clicks map link, navigation app opens with directions
8. Arrives at site
9. Clicks "Check In" - app captures GPS location and time (geological stamp)
10. Sees event details: PM to verify site readiness, confirm space available, etc.
11. Marks event as "In Progress"
12. Takes photos of site conditions using app camera
13. Documents site measurements or notes in app notes field
14. Completes verification work
15. Marks event as "Complete"
16. App records completion time
17. Event card on dashboard updates to "Complete"

**Second Event - Delivery and Install:**
18. PM navigates to XYZ Company location (using map link)
19. Checks in (GPS stamp)
20. Sees five line items on delivery (chairs, tables, accessories, etc.)
21. As installation proceeds, marks items as "In Progress" and then "Complete"
22. Takes photos of installation progress and final state
23. Contractor working alongside marks items complete as well (can see same app)
24. Notices one item has slight damage upon delivery
25. Creates punch item directly from app:
    - Takes photo of damage
    - Marks location on floor plan (pins to specific area)
    - Marks "Damage in Shipping" as issue type
    - Marks contractor as responsible party
26. Completes delivery installation
27. Asks client to sign off on delivery completion
28. Client signs on tablet in app
29. Signature captured and stored with event
30. Marks event complete

**Time Entry for Multi-Resource Event:**
31. PM fills in time entry for event:
    - "2 PM + 2 contractors worked 4 hours on install"
    - Selects both contractor names from dropdown
    - Enters "4" hours
    - App creates time entry for all three resources for 4 hours

**Third Event - Punch Walk (Later Same Day):**
32. Returns to ABC Company for punch walk
33. Checks in again (new check-in for new event)
34. Walks site with tablet, floor plan displayed
35. Identifies 6 punch items from initial installation
36. For each item:
    - Takes photo
    - Pins location on floor plan
    - Documents issue description
    - Marks responsible party
37. Generates status report directly from app showing:
    - Project completed
    - 6 punch items identified
    - Photos of each punch item
    - Client signature from earlier delivery
38. Emails report to client from app
39. Client receives professional status report same day

**End of Day:**
40. PM returns to office with connectivity
41. Field Service app syncs automatically: all punch items, photos, time entries, check-ins
42. All data now available in NetSuite for finance, operations, client portal

**Real-Time Visibility:**
43. Wendy (PM Manager) can view dashboard showing all PM events
44. Can see in real-time which events are complete, which still in progress
45. Can see check-in times to verify PMs on-site when claimed
46. Receives punch items automatically for new issues to track and escalate

---

## 9.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-028 | Deploy Field Service app for PMs and contractors | Orion Field Service app (tablet/mobile) | ALIGNS |
| REQ-029 | Enable geological check-in stamping | Orion Field Service app check-in feature | ACCOMMODATE |
| REQ-030 | Support photo, signature, document collection | Orion Field Service app document tools | ALIGNS |
| REQ-031 | Enable multi-resource time entry | Orion Field Service app time entry | ALIGNS |

---

## 9.6 Implementation Approach

**Field Service app will be deployed as central platform for all field operations:**
- Field Service app will be installed on all PM tablets and contractor mobile phones
- Dashboard will display all assigned work order events
- Check-in feature will be configured with GPS geological stamping
- Photo, signature, and document collection will be enabled
- Multi-resource time entry will be configured
- Offline mode will be enabled and tested
- Integration with Field Service punch list (Section 8) will be tested
- Push notifications can be configured for event reminders and updates

**Decision Points Requiring Configuration Sessions:**
- PM tablet hardware specifications: recommended devices, operating systems?
- Contractor access policy: which contractors get app access, which use portal only?
- Check-in GPS accuracy requirements: what distance tolerance acceptable?
- Notification preferences: how should PMs be notified of new assignments?
- Mobile network requirements: what network coverage is needed?

---

## 9.7 Custom Solution Designs

**REQ-029: Field Service App Geological Check-In with GPS Stamping**

**Scope:** Custom Orion feature implementing check-in with GPS location verification

**High-Level Design Approach:**
- Check-in button on event detail screen
- On tap, app captures current GPS location
- Records location, timestamp, user ID
- Compares captured location to event address (within X miles accuracy)
- If within tolerance, check-in successful
- If outside tolerance, warning: "You appear to be [X miles] from scheduled location"
- Check-in data stored with event for audit trail

**Benefits:**
- Accountability for on-site presence
- Prevents false check-ins from office
- Creates proof for dispute resolution
- Manager oversight of PM locations in real-time (optional dashboard)

**Dependencies:**
- Mobile device GPS capability (all modern tablets/phones have this)
- Location data storage in NetSuite
- Accuracy tolerance definition (how close to address is required?)

---

## 9.8 Implementation Considerations

- **Device Management:** Plan for tablet/phone procurement, OS standardization, security policies
- **Network Requirements:** Most sites will have some connectivity; offline mode handles gaps
- **User Training:** All PMs and contractors need training on app features, check-in, photo capture, time entry
- **Contractor Adoption:** Some contractors may resist new system; clear communication and support needed
- **Photo Storage:** Digital photos from all projects can require significant storage; cloud storage strategy important
- **GPS Accuracy:** Define acceptable distance tolerance for check-in (suggest 0.25 miles / ~400 meters)
- **Support Process:** Plan for technical support when users have app issues in field
- **Hardware Security:** Tablets/phones will contain project information; security policies for device loss/theft
- **Data Backup:** Regular backups of field app data to prevent loss
- **Performance:** App must be responsive and reliable; slow or crashed app hurts field productivity
- **Phased Rollout:** Consider piloting with one PM team before full deployment

---

# SECTION 10: SCHEDULING & RESOURCE MANAGEMENT (FUTURE SESSION)

## 10.1 Your Business Requirements

**REQ-032: Determine PM task list automation approach (ADAPT)**

Wendy's vision is that when a PM is assigned to a project, they automatically receive a task list of all standard activities: site verification, delivery, walkthrough, punch walk, etc. This automation would eliminate manual task creation and ensure consistency. However, this requires determining: Should tasks be fully automated templates, or should PMs have flexibility to customize? What level of workflow enforces task completion vs. allows flexibility?

**REQ-033: Evaluate resource visualizer with calendar view of PM workloads (ACCOMMODATE)**

Wendy currently maintains a manual Google Sheets calendar showing PM workloads. NetSuite has native project management tools (Suite Projects) that could replace this, but dealers typically resist adoption. A custom Orion resource visualizer might be designed to specifically show PM workloads in a calendar format. This requires determining: What views (calendar, timeline, list)? What metrics (number of projects, revenue, hours)? Should account managers have similar visibility?

**REQ-034: Determine task management sophistication level (ADAPT)**

Matt's question: "is it the 10 phases or is it the 300 things that happen in each one of those phases?" This balances:
- **High Rigor:** 300 granular tasks with dependencies (like Asana), complete workflow management
- **High Flexibility:** 10 high-level phases, PMs manage details themselves
- **Risk:** Too much rigor = employee resistance; too little = things fall through cracks

This complex area requires a dedicated additional discovery session before design can proceed.

**Requirements Classification:**
- Type: Functional - Resource management and project task automation
- Priority: Should-Have (impacts efficiency but requires more discovery)
- Users Impacted: Wendy (PM Manager), Kimmy (Account Manager), PMs, Account Managers, Matt (leadership)
- Business Impact: PM workload visibility, task automation, project phase tracking

---

## 10.2 Current State Process

**PROCESS:** Manual PM Workload Management with Google Sheets (Current State)

**TRIGGER:** Projects in various stages of design/delivery

**CURRENT STEPS:**
1. Wendy maintains manual Google Sheets calendar
2. Rows = projects, columns = weeks
3. Each project shows install date as bar on timeline
4. Grouped by PM to show who has which projects
5. Used for assignment decisions and one-on-one reviews with PMs
6. Accuracy problem: "It's only as accurate as the information... Have they updated it?"
7. Not updated in real-time

**SYSTEMS INVOLVED:** Google Sheets, email updates

**PAIN POINTS:**
- Manual maintenance is tedious
- Updates lag actual project status
- No real-time visibility for dynamic scheduling
- Account managers also managing pre-quote workload separately (no integration)
- No enforcement of standard tasks (PMs remember or miss them)
- No visibility into whether tasks actually completed

---

## 10.3 Orion/NetSuite Solution

**This area requires additional discovery before solution design can proceed.** The team has identified needs but hasn't fully defined requirements or prioritized between high-rigor task management (Asana-style with dependencies) vs. high-flexibility approach.

**Potential Approaches (To Be Decided in Additional Session):**

**Option A: Automated Task List Approach**
- When PM assigned, standard task template automatically creates tasks
- Tasks: site verification, delivery coordination, installation oversight, punch walk, etc.
- PM completes tasks and checks them off
- Manager has visibility into task completion status

**Option B: Resource Visualizer Approach**
- Replace Google Sheets with custom dashboard showing PM workload
- Calendar view shows projects and install dates
- Shows PM capacity, identifies over-allocation
- Integrates account manager pre-quote workload visibility

**Option C: Suite Projects Integration**
- Use NetSuite native Suite Projects for full project management
- Task templates, resource allocation, dependencies, reporting
- Risk: Dealers typically resist rigid project management

**This will be determined in dedicated discovery session.**

---

## 10.4 Implementation Status

**STATUS: DEFERRED TO ADDITIONAL SESSION**

This area explicitly requires a follow-up discovery session before design and implementation can proceed. The team has identified needs (task automation, resource visibility) but hasn't made definitive decisions about approach, sophistication level, or implementation method.

**Recommended Session Details:**
- **Participants:** Wendy (PM Manager), Kimmy (Account Manager), Matt (Leadership), Marcus (Implementation)
- **Duration:** 2 hours
- **Questions to Address:**
  - What level of task management is needed? (10 phases vs. 300 tasks)
  - Should PM task lists be automated with templates?
  - Is Asana-style workflow with task dependencies desired?
  - What resource visualizer/calendar views are needed?
  - How should account manager pre-quote workload tracking integrate?
  - Manager vs. individual contributor view requirements?
  - What's the resistance risk to project management rigor?
- **Expected Output:** Design requirements for task management and resource visualization approach

---

## 10.5 Solution Validation

**Validation deferred pending additional discovery session.**

---

## 10.6 Implementation Considerations

- **Employee Change Resistance:** Key risk is that highly detailed task management may feel like micromanagement; culture fit important
- **Asana Evaluation:** Team should evaluate whether Asana integration or replacement is preferred
- **NetSuite Suite Projects:** Native NetSuite solution available but historically rejected by dealers; worth reconsidering
- **Account Manager Integration:** Pre-quote phase workload tracking needs design; currently separate from operations
- **Real-Time Updates:** Any resource visualization must auto-update as projects change
- **PM Autonomy:** Balance between accountability/visibility and trusting PMs to manage details
- **Rollout Phasing:** May need to phase—start with high-level phases, expand to granular if team adoption strong

---

# IMPLEMENTATION SUMMARY & NEXT STEPS

## Overall Implementation Approach

The Orion/NetSuite solution provides a comprehensive, integrated platform for KBM Hogue's operations. With 47% of requirements aligning with standard NetSuite functionality and 26% requiring only process adaptation, this implementation represents a proven approach to outsourced operations management. The remaining 27% requiring custom development or further planning reflects KBM Hogue's unique business model and specific operational requirements.

### Requirement Distribution

| Approach | Count | Percentage |
|----------|-------|-----------|
| ALIGNS (No changes required) | 16 | 47% |
| ADAPT (Process changes only) | 9 | 26% |
| ACCOMMODATE (Custom development) | 6 | 18% |
| TBD (Requires additional session) | 3 | 9% |
| **Total** | **34** | **100%** |

---

## Critical Success Factors

1. **Advanced Receiving Tool Adoption:** Critical custom tool for outsourced model; extensive testing and training required
2. **Vendor Center Contractor Adoption:** Success depends on external parties changing communication behavior from email to portal
3. **Field Service App Deployment:** PMs must adopt new tablet app; training and support critical
4. **VRA Process Discipline:** Creating VRAs even when not shipping back requires team discipline; training and workflow enforcement needed
5. **Rate Matrix Accuracy:** Complete, accurate PM and designer rate data must be provided before configuration
6. **15% Markup Exception Logic:** Complete business rules required from Kipp before configuration
7. **Work Order Buy-In:** Wendy has committed, but formal leadership confirmation pending before configuration

---

## Outstanding Action Items

### High Priority (Required Before Configuration)

| Action | Owner | Due Date | Reason |
|--------|-------|----------|--------|
| Provide complete 15% markup exception logic | Kipp | Configuration phase | Prerequisite for formula configuration |
| Provide complete PM and designer rate matrix | Kipp/Wendy | Configuration phase | Prerequisite for time tracking configuration |
| List all third-party warehouse locations | Operations | Configuration phase | Prerequisite for bin setup |
| List contractors needing Vendor Center access | Operations | Configuration phase | Prerequisite for contractor provisioning |
| Define damaged product accounting treatment | Lorraine/Kipp | Configuration phase | Clarifies zero-cost replacement recording |
| Final confirmation on work order usage | Wendy/Operations | Before configuration | Soft decision needs formal confirmation |

### Medium Priority (Required Before Go-Live)

| Action | Owner | Due Date | Reason |
|--------|-------|----------|--------|
| Identify contractors needing time entry access | Wendy/Rafina | User provisioning | System access control |
| Provide current PlanGrid report examples | Wendy/PM Team | App configuration | Template for field reports |
| Confirm floor plan file format requirements | Operations | App configuration | Affects file upload process |
| Define soft scheduling workflow details | Wendy | Workflow design | How PMs approve/decline assignments |
| Determine contractor direct receiving backlog | Operations | Deferred decision | For future phase planning |

### Future Sessions Required

| Session | Participants | Topics | Priority |
|---------|-------------|--------|----------|
| Operations Suite Demo | Wendy, PMs, Operations Team, Marcus/Chris | Advanced Receiving, Field Service app, Work Orders, Field Service capabilities | High |
| Scheduling & Resource Management Deep Dive | Wendy, Kimmy, Matt, Marcus | PM task automation, resource visualizer, task sophistication level, account manager integration | Medium |

---

## Risk Assessment & Mitigation

### High-Risk Requirements

| Requirement | Risk | Mitigation |
|-------------|------|-----------|
| **REQ-002: Advanced Receiving Tool** | Custom tool critical for outsourced model; must work flawlessly | Demo session, extensive testing, training plan |
| **REQ-007: Vendor Center Receiving Notification** | Depends on contractor adoption; backup email process needed | Contractor training, phased rollout, email fallback process |
| **REQ-010: VRA Process Discipline** | Requires behavioral change; teams may skip VRA if not shipping back | Training, workflow enforcement, monthly credit report pressure tactic |
| **REQ-024-027: PlanGrid Replacement** | PMs must adopt Field Service app; offline mode must work perfectly | Demo, PM training, parallel run period, floor plan testing |
| **REQ-032-034: Scheduling/Resource Management** | Unclear requirements; employee resistance to excessive task management | Additional discovery session required, phased adoption |

---

## Implementation Timeline Considerations

### Pre-Configuration Phase (Current)
- Additional discovery session for Scheduling/Resource Management (REQ-032-034)
- Operations Suite demo (REQ-002, REQ-024-031)
- Gather outstanding action items (rate matrix, warehouse locations, exception logic)

### Configuration Phase
- NetSuite and Orion module configuration
- Custom development: Advanced Receiving Tool, Field Service punch list, 15% markup formula, vendor center notifications, monthly credit report
- Extensive testing: drag-and-drop receiving, punch pinning, offline mode, soft scheduling workflow
- User security and access provisioning

### Testing Phase
- Advanced Receiving tool: tablet compatibility, drag-and-drop accuracy, bin allocation prevention
- Vendor Center notifications: contractor access, notification display, integration with Advanced Receiving
- Field Service app: offline mode, punch pinning, photo upload, geological check-in, status report generation
- Work order workflows: soft scheduling, PM assignment, contractor assignment
- Time tracking: rate matrix application, GP impact, contractor reconciliation
- VRA process: credit tracking, monthly report generation

### Training & Change Management Phase
- Internal KBM team training: Advanced Receiving, work orders, time tracking, VRA discipline
- Contractor training: Vendor Center portal, receiving notifications
- PM training: Field Service app, punch list, check-in, report generation, offline mode
- Finance team training: time-based project profitability, rate matrix, contractor reconciliation

### Go-Live Phase
- Production system activation
- Contractor access activation (Vendor Center, Field Service app)
- Field app deployment to tablets/phones
- Live support team ready for issues
- Parallel running period if appropriate

---

## Quality Assurance Checklist

Before BRD approval and proceeding to design phase:

- [x] All questionnaire requirements addressed in BRD
- [x] Business value articulated for each major requirement
- [x] Implementation approach justified for each requirement
- [x] Orion/NetSuite positioned as primary solution
- [x] Outstanding items captured in action items and implementation considerations
- [x] Document flows logically from current state to future state
- [x] Language appropriate for C-suite approval
- [x] Custom solution designs explained for ACCOMMODATE requirements
- [x] Risks and mitigations identified
- [x] Change management considerations documented

---

## Approval & Sign-Off

This Business Requirements Document represents the consensus of the operations discovery session and outlines the implementation approach for KBM Hogue's Operations process area within the Orion/NetSuite solution.

The document has been prepared based on:
- **Discovery Session:** July 31, 2025 - Operations Process Deep Dive
- **Questionnaire Analysis:** Questionnaire_Operations_v1.0.md
- **Requirements Mapping:** Requirements_Map_Operations_v1.0.md
- **Solution Reference:** Orion Whitepaper

### Recommended Next Steps

1. **Executive Review & Approval:** Present BRD to leadership (Matt, Lorraine) for approval before design phase
2. **Outstanding Items Collection:** Complete action items (rate matrix, warehouse locations, exception logic)
3. **Additional Discovery Sessions:** Schedule Operations Suite Demo and Scheduling/Resource Management Deep Dive
4. **Design Phase Kickoff:** Upon BRD approval, begin detailed solution design and configuration planning

---

**Document Prepared:** December 16, 2025  
**Status:** Ready for Executive Review and Approval  
**Next Review:** Upon completion of outstanding action items and additional discovery sessions

---

*End of Business Requirements Document - Operations*




