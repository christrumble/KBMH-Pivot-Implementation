# Codex Review — §3.10 System Setup & Configuration

## Headline assessment
Not ready to lock. Structure is close, but there are source-accuracy and cross-area issues that will propagate: soft cutover is overstated as common ground, Pivot division naming is wrong, CT-6 CRM/HubSpot migration is missing, and divergence citations do not meet the REQ-ID standard.

## Standards compliance
Mostly clean: no banned terminology, emojis, or obvious internal commentary.

Issues:
- Wrong division name: “NBD” should be “Enterprise” in Pivot’s four-division taxonomy. See draft line [105](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:105>) vs. CRM sample line [94](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/01 - CRM (Sample).md:94>).
- Duplicate / malformed references: `Financial Management §3.08 §3.08.8 #8/#9` at lines [115](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:115>) and [129](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:129>).

## Source accuracy
Main problems:
- “Soft-cutover transition strategy” is listed as explicit in both BRDs at line [27](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:27>). KBM explicitly supports it, including new business in NetSuite while existing Core work completes, lines [563-580](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/System Setup and Configuration/KBMH/3 Output/BRD_SystemSetupConfiguration_v1.0.md:563>). Pivot instead says open orders will not be brought into Orion, lines [1224-1230](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/pivot-brds-md/System_Setup_and_Configuration.md:1224>). Reframe as KBM-explicit / Pivot cutover rule pending or different.
- “Change-management approach with named leads” is also listed as explicit in both at line [28](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:28>), but Pivot System Setup does not name change leads. KBM does, lines [39-48](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/System Setup and Configuration/KBMH/3 Output/BRD_SystemSetupConfiguration_v1.0.md:39>).
- Pivot System Setup does not support “HubSpot retained” as a System Setup BRD claim. It says HubSpot integration will be explored after go-live, line [175](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/pivot-brds-md/System_Setup_and_Configuration.md:175>). Retention is locked in Marketing, lines [67-69](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/03 - Marketing.md:67>).
- D-6 omits KBM’s actual System Setup manufacturer integration, Miller Knoll Exemplis, while listing other MillerKnoll integrations. KBM System Setup REQ-020 is Exemplis, lines [296-299](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/System Setup and Configuration/KBMH/3 Output/BRD_SystemSetupConfiguration_v1.0.md:296>).

## Tone calibration
Tone is mostly neutral. Risk: D-1 and D-2 read as KBM-default because Pivot is described as less specific on governance and then assigned KBM’s cutover model. That can be acceptable, but only after the source language is corrected and Pivot’s documented “no open orders into Orion” posture is acknowledged.

## Cross-area consistency
- Missing CT-6: CRM data migration is explicitly owned by System Setup, including Zendesk/Core extracts and Pivot HubSpot extract, lines [91-99](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/cross-area-decisions.md:91>). §3.10 dependencies omit it, lines [141-155](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:141>).
- CT-1 conflict: division taxonomy is open / confirm-at-session, starting from Enterprise, Venture, Public, Construction Solutions, lines [21-31](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/cross-area-decisions.md:21>). Draft line [105](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:105>) makes the wrong taxonomy look fixed.
- CT-14 needs tightening: draft recommends File Cabinet plus external collaboration storage, line [90](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:90>), while CT-14 says project/customer/vendor documents migrate to File Cabinet and SharePoint/network drives phase out for project documentation, line [211](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/cross-area-decisions.md:211>). Clarify transactional/project docs vs. collaboration docs.

## Template fidelity
Header and §3.10.1-§3.10.8 structure are present. Decisions table math reconciles.

Material citation failure: Doc standards require each divergence to cite KBM and Pivot REQ IDs, lines [155-160](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/drafting-standards.md:155>). D-1 through D-6 sources mostly lack Pivot REQ IDs, and several lack KBM REQ IDs, lines [56](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:56>), [70](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:70>), [84](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:84>), [101](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:101>), [115](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:115>), [129](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/07 - System Setup & Configuration.md:129>).

## Decision quality
- D-1: Supported, but should cite Pivot DREAM/project overview and state Pivot role assignments are not named.
- D-2: Default is premature as written. Pivot’s open-order rule needs to be reconciled before “soft cutover for both” is default-yes.
- D-3: Good decision split, but needs owner/date for “both with sunset.”
- D-4: Good concept; fix taxonomy and avoid locking division names.
- D-5: Too broad. Must explicitly include CRM/HubSpot/contact migration, D365 history, Core/Zendesk extracts, financial trial balances, and document migration.
- D-6: Too broad as “all confirmed integrations.” Split confirmed integrations from evaluation items: Coupa, ZoomInfo, SuiteAnalytics Connect, Stripe, and expense platform are not all the same decision type.

## Reconciliation principle audit
Current recommendation lean:
- KBM-leaning: 2 decisions (D-1 governance, D-2 cutover)
- Pivot-leaning: 0
- Hybrid: 4 (D-3 document architecture, D-4 roles, D-5 data migration, D-6 integrations)
- Neutral: 0

Acceptable if source corrections are made, but today the KBM lean in governance/cutover is under-supported for Pivot.

## What's missing
Add or cross-reference:
- KBM COA setup / consolidation as a configuration dependency: REQ-012/013, lines [156-165](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/System Setup and Configuration/KBMH/3 Output/BRD_SystemSetupConfiguration_v1.0.md:156>).
- KBM Teams / status / session recording / change control requirements: REQ-032 through REQ-037, lines [475-505](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/System Setup and Configuration/KBMH/3 Output/BRD_SystemSetupConfiguration_v1.0.md:475>).
- Transaction numbering/search/recent transaction setup: REQ-046 through REQ-048, lines [718-729](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/System Setup and Configuration/KBMH/3 Output/BRD_SystemSetupConfiguration_v1.0.md:718>).
- Pivot company structure, locations, segmentation, COA, system preferences, item master, and document-management requirement groups should either appear or be intentionally cross-referenced. Example Pivot roles are at lines [923-931](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/pivot-brds-md/System_Setup_and_Configuration.md:923>); data migration at [1142-1148](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/pivot-brds-md/System_Setup_and_Configuration.md:1142>); document management at [1280-1287](</Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation/_Unification/working/pivot-brds-md/System_Setup_and_Configuration.md:1280>).

## Internal commentary
No leadership-reaction or political meta-commentary found.

## Recommended edits before lock
1. Fix Pivot division taxonomy: Enterprise, Venture, Public, Construction Solutions.
2. Rework §3.10.2 alignment bullets so soft cutover and named change leads are not “explicit in both.”
3. Add CT-6 CRM/HubSpot migration to D-5 and §3.10.4.
4. Tighten D-3 against CT-14: File Cabinet for project/transaction records; external storage only for defined collaboration use cases.
5. Replace all divergence source lines with KBM/Pivot REQ IDs and section refs.
6. Split D-6 into confirmed integrations vs. evaluation/licensing decisions, and add Exemplis.