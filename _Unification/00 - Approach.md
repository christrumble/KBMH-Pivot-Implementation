# KBM + Pivot Unification — Approach Document

**Document Owner:** Marcus Dallacqua (Proprio) & Chris Trumble (GSI)
**Audience:** Matt Denning (merged-company COO), Sandra Rudloff (Pivot leadership), Dustin Doucette & Jennifer Trask (GSI leadership)
**Status:** Draft for stakeholder review
**Date:** May 3, 2026

---

## 1. Why this document exists

KBM Hogue and Pivot Interiors are merging into a single MillerKnoll dealer under Matt Denning's leadership. Both companies completed independent NetSuite/Orion BRD discovery during 2025 and began implementation work shortly afterward. Each company developed thoughtful approaches inside Orion that fit how it ran its business at the time. The merged company will operate from a single set of decisions, and those decisions need to be made before configuration resumes in June.

This document proposes the approach, structure, and methodology for the deliverable that will guide those decisions: a **Process Unification Recommendation** covering all 10 process areas. Once approved, the full recommendation will be drafted, reviewed by both leadership teams, and used as the working agenda for an on-site decision session.

This document is *not* the recommendation itself. It is a proposal for how the recommendation will be built and delivered. **The companion file `01 - CRM (Sample).md` contains a fully worked CRM sample** so reviewers can react to the actual format rather than abstract structure.

## 2. What both companies bring to the merged organization

Each company entered Orion implementation with established business processes shaped by how each operated at the time. KBM Hogue built its approach around a relationship-led California sales motion, with operations work delivered through trusted external partners. Pivot Interiors built its approach around a divisional sales structure spanning California, with delivery, installation, and field-service operations performed in-house. Both approaches are well-suited to the company that designed them. The merged company has elements of both — and choices to make about which direction to operate from going forward.

The unification work is not a comparison of which company "got it right." Both companies' approaches are appropriate to their context. The merged company's question is which approach best fits its situation — operational footprint, customer mix, organizational scale, and strategic direction.

## 3. Reconciliation principle

The recommendation document applies the same principle to every process area. We state it up front because every recommendation in the document is made through this lens.

> **Where the two companies converge, the path is clear. Where they diverge, the recommendation leans toward the approach whose context — operational footprint, customer mix, organizational scale, or strategic priorities — most closely matches the merged company's situation. The recommendation is never about which approach is "better"; it is about which direction the merged company is best positioned to operate from.**

In practice this resolves to three cases:

- **Both companies do the activity.** The recommendation attributes the chosen direction to merged-company context (e.g., "the merged company's scale and divisional structure align more naturally with [Company]'s approach").
- **Only one company does the activity.** That company's process is the natural starting point for the merged company. The recommendation focuses on how the other company's staff onboard into it.
- **The merged company's scale or scope exceeds either legacy company's prior scale.** The recommendation may propose evolving beyond either legacy approach where merged-company demands warrant it.

## 4. Document structure (the deliverable)

The full Process Unification Recommendation will follow this structure:

```
1. Executive Summary               (1–2 pages, leadership-readable in 10 minutes)
2. At-a-Glance Index               (see §5)
3. Process Area Sections           (one section per area, 10 sections)
   3.01 Marketing
   3.02 CRM                        (← sample is in companion file 01 - CRM (Sample).md)
   3.03 Pre-Quote
   3.04 Order Management
   3.05 Operations
   3.06 Project Management
   3.07 Commissions
   3.08 Financial Management
   3.09 Business Intelligence
   3.10 System Setup & Configuration
4. Cross-Area Dependencies         (decisions that touch more than one area)
5. June Resume Plan                (workstream sequencing, decision gates, on-site session agenda, owners)
6. Decisions Register              (consolidated list of every leadership-team decision)
```

Process areas are walked **linearly in the order above**, not reordered by complexity. A complexity-based ordering tempts readers to skip ahead; a linear order matches how configuration is done and how the working session will run.

## 5. The at-a-glance index

The first thing leadership sees after the executive summary is a single page showing every process area at a glance:

| # | Process Area | Decision Density | Source Coverage | Headline |
|---|---|---|---|---|
| 3.01 | Marketing | Low | Both | Both companies relationship-led; HubSpot retention is the primary decision |
| 3.02 | CRM | Medium | Both | Pipeline model, hierarchy, and relationship-tracking design choices |
| 3.03 | Pre-Quote | Medium | Pivot BRD + KBM gap analysis | Labor quotes (KBM emphasis) and request types (Pivot emphasis) |
| 3.04 | Order Management | Medium | Pivot BRD + KBM gap analysis | Approval framework, order types, document workflow |
| 3.05 | Operations | High | Both (asymmetric scope) | Pivot operates in-house; KBM has operated through partners — onboarding shape |
| 3.06 | Project Management | High | Pivot only | Workfront vs. Orion-native project execution |
| 3.07 | Commissions | Medium | Pivot only | Compensation model design for the merged company |
| 3.08 | Financial Management | Medium | Both | Both mature; sequencing of financial close, COA, revenue recognition |
| 3.09 | Business Intelligence | Low | Both | Reporting layer largely follows decisions made in earlier areas |
| 3.10 | System Setup & Configuration | Low | Both | Foundation-level decisions tied to other areas |

**Source coverage** is intentionally explicit. KBM Hogue completed final BRDs for 6 of the 10 areas; for Pre-Quote and Order Management, the discovery output is captured in detailed gap analyses and requirements maps. Commissions and Project Management did not have a separate KBM BRD because those activities were structured differently in KBM's organization. Pivot completed BRDs for all 10 areas (including the two that are net-new contributions to the merged organization). The recommendation document is explicit about which evidence underlies each section's content so leadership can calibrate confidence in each recommendation.

**Decision Density** definitions:

- **Low** — recommendations are largely settled; decisions mostly informational
- **Medium** — meaningful design choices; decisions matter but stakes are bounded
- **High** — high-stakes decisions, often involving net-new merged-company capability

The above density assessments are illustrative, drawn from initial reading. The final document calibrates them with stakeholder input.

## 6. Per-area section template

Every process area section follows the same structure so reviewers can move through them at a consistent pace. The CRM sample in [`01 - CRM (Sample).md`](01%20-%20CRM%20(Sample).md) demonstrates the template fully populated; the abstract template is below.

```
3.0X — [Process Area]
  Decision density:    [Low / Medium / High + one-line headline]
  Source coverage:     [What KBM and Pivot evidence is available]

  3.0X.1  How each company approaches [process area] today
    [Two short paragraphs: KBM's approach, Pivot's approach. Both written
     neutrally, attributing each company's choices to context — operating
     footprint, customer mix, scale, etc. No comparison or judgment.]

  3.0X.2  Where the two companies align
    [Bullets on capabilities both companies want from Orion in similar shape.
     These need no decision — recommendation simply confirms direction.]

  3.0X.3  Where the two companies differ
    [The actual decision space. Each divergence gets:
      - How KBM approached it (with attribution to KBM's context)
      - How Pivot approached it (with attribution to Pivot's context)
      - Recommendation for the merged company, with context-based reasoning
      - Decision the leadership team owns]

  3.0X.4  Cross-area dependencies
    [Decisions or capabilities that surface here but are properly decided
     in another process area. Cross-referenced, not duplicated.]

  3.0X.5  Recommendation summary
    [Tight bullet list of merged-company outcomes from this area]

  3.0X.6  Decisions for the leadership team
    [Numbered list of explicit decisions, with default recommendations.
     Defaults are the synthesis position; the working session can confirm or modify.]

  3.0X.7  Open questions / inputs needed
    [What we don't know yet, and who can confirm]
```

The template is the same shape for all 10 areas, but the content density varies. Areas with rich source material on both sides have substantial divergence sections. Areas where only one company has formal BRD content have a shorter divergence section and a longer "How each company approaches it today" section that documents the merged company's likely starting point and the onboarding path for the other company's staff.

## 7. Working session methodology

Once the recommendation document is drafted, an on-site working session is convened with Matt, Sandra, and their respective leadership teams. The format:

1. **Pre-read** — The recommendation document is circulated 5 business days in advance, with the request to come prepared with reactions on each Decisions block.
2. **PowerPoint companion** — A deck mirrors the document's structure to anchor the conversation visually. The deck does not duplicate the document; it summarizes each section to one slide and projects the decisions for that area.
3. **Linear walkthrough** — Process areas are covered in document order, ~30 minutes each, ~5 hours total. Low-density areas may take 10 minutes; high-density areas may take an hour.
4. **Decision capture** — Each decision gets a yes / no / modified / deferred outcome captured in real time.
5. **Output** — A *Merged BRD per area* drafted from the decisions and circulated for sign-off within 10 business days of the session. Configuration resumes from the merged BRDs in June.

The working session is the test of the recommendation, not its ratification. The document's job is to make every decision legible and to recommend a direction; the room's job is to confirm, modify, or defer.

## 8. What we are asking from reviewers

This document and the CRM sample are sent to Matt, Sandra, Dustin, and Jennifer for two questions:

1. **Is the approach right?** Reconciliation principle, at-a-glance framing, source-coverage transparency, linear walkthrough, on-site session format.
2. **Is the sample effective?** [`01 - CRM (Sample).md`](01%20-%20CRM%20(Sample).md) is the proposed CRM section. Read it and react. If the format works for CRM, it'll work for the other 9 areas. If it doesn't, we change the template once rather than rewriting 10 sections.

Feedback turnaround target: **5 business days**. After approval, the full recommendation document is drafted within ~7 business days, putting an on-site working session realistically in the week of May 19 or May 26.

---

*Companion document: [`01 - CRM (Sample).md`](01%20-%20CRM%20(Sample).md) — the worked CRM example.*
