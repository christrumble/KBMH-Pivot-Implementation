# Codex Review Prompt — KBM + Pivot Unification Drafts

Paste the section below into a Codex / ChatGPT 5.x session that has read access to this repo (or attach the relevant files manually). The prompt is calibrated for an adversarial, multi-angle review — not a pat-on-the-back.

---

## Prompt to paste

You are an experienced ERP implementation consultant with deep knowledge of contract furniture dealer operations and NetSuite/Orion. I am asking you to review three documents that another consultant drafted today as the foundation for merging two NetSuite/Orion implementations: KBM Hoag and Pivot Interiors. The two companies were independently going through Orion implementation; mid-implementation, MillerKnoll-driven business consolidation made them merge into a single company. Matt Hoag (KBM's COO) leads the merged company. Sandra Rudloff led Pivot. Configuration on both sides is early enough to redirect, and the working session that will lock decisions has not yet been scheduled — it is gated on these documents.

I need you to do a thorough start-to-finish review. Be skeptical, not generous. Surface real problems. Pretend you will be in the room when Matt reads these and you will be asked to defend or attack each recommendation.

### Documents to review (in this order)

1. `_Unification/00 - Approach.md` — proposed approach, structure, reconciliation principle, traffic-light framework, working-session methodology. This is "Doc Zero": the structural proposal that, once approved, governs how the full unification recommendation gets written for the other 9 process areas.

2. `_Unification/01 - CRM (Pilot).md` — a worked CRM example demonstrating the per-area template. 11 divergences (D-1 through D-11), 13 explicit decisions for Matt. The pilot is the proof of concept for the format. If it doesn't land, the template gets revised once before applying to the other 9 areas.

3. `_Unification/Doc A - Account & Renewal Memo.md` — separate decision memo recommending the merged company operate inside KBM's prepaid 5-year account and let Pivot's annual contract lapse at the May 2026 renewal.

### Source materials you must reference (do not take the drafts at face value)

- `CRM/KBMH/3 Output/BRD_CRM_v1.0.md` — KBM's CRM BRD, 50 requirements, full ALIGN/ADAPT/ACCOMMODATE classification
- `_Unification/working/pivot-brds-md/CRM.md` — Pivot's CRM BRD converted from docx (8 requirements). Original: `CRM/Pivot/4 BRD/03 Pivot Interiors BRD CRM Process Area_v2.0.docx`
- `_Pivot Discovery/Transcripts/2026-04-08_KBM-Pivot-Plan.md` — call between Marcus (Proprio) and Chris Trumble (GSI) where the document structure and approach were originally planned. Read this to understand the prior commitments — the drafts should be consistent with what was agreed there or explicitly diverge with reasoning.
- `_Pivot Discovery/Transcripts/2026-02-19_Pivot-Interiors-Joint-BRD.md` — Pivot v1.0→v2.0 BRD review session (this is *Pivot-only*, not a joint session despite the filename). Useful for tone calibration and understanding Pivot leadership's decision style.
- The other 9 Pivot BRDs in `_Unification/working/pivot-brds-md/` and KBM BRDs in `*/KBMH/3 Output/BRD_*.md` — for assessing whether the per-area template will scale to the rest of the document.

### Reviewer lenses (do all of them)

**1. Substance accuracy.** For every claim made about KBM or Pivot in the CRM pilot's D-1 through D-11 divergences, verify it against the source BRDs. Flag any factual errors, misrepresentations, or claims that go beyond what the source material supports. List specific quotes/sections that contradict or are ambiguous.

**2. Hidden gaps.** Read both CRM BRDs end-to-end. Find requirements or capabilities that *did not* make it into the pilot's 11 divergences but should have. Especially: Pivot's 8 requirements are higher-level than KBM's 50 — did the synthesis miss substance that's hidden in KBM's granularity, or substance that's hidden in Pivot's brevity?

**3. Charitable framing test.** Read the pilot as if you were a member of Pivot's leadership team (Sandra Rudloff, Brian, etc.). Does any section feel dismissive of Pivot's processes? The reverse: does any section feel dismissive of KBM's "agility/outsourcing" model? Cite specific paragraphs that need re-framing.

**4. Decision quality.** For each of the 13 "Decisions for Matt," evaluate: (a) is the recommendation actually supported by the BRD evidence? (b) is the *default* (yes/no) the right one given the reconciliation principle? (c) are there decisions that should be subdivided into multiple finer decisions, or merged into fewer?

**5. Reconciliation principle stress test.** The principle is: "Default to the simpler operating model. Layer in sophistication only where it protects margin, compliance, scale, or a capability one company brings that the other does not." Walk through each recommendation in the pilot and check whether the principle was actually applied or whether it was bent toward Pivot in places where simpler-KBM should have won (or vice versa). Specifically count how many decisions favored Pivot vs. KBM and assess whether the balance is justified by the principle.

**6. Classification asymmetry accuracy.** The drafts use ALIGN/ADAPT/ACCOMMODATE classifications drawn from the BRDs. For each divergence in the CRM pilot, verify the KBM and Pivot classifications match what their BRDs actually say. Flag any classifications that look invented, swapped, or outdated.

**7. Format scalability.** Without writing the other 9 sections, assess: would the same template work for Operations (where Pivot leads, KBM has only an outsourced model)? Project Management (Pivot-only — Workfront)? Commissions (Pivot-only — KBM has nothing)? Financial Management (most mature on both sides)? Where would the template strain or need adaptation, and how should the approach document address that?

**8. Doc A financial logic.** The account memo argues that KBM's 5-year prepayment makes it the surviving account. Stress test: are there scenarios where the math reverses (e.g., Pivot has more sunk infrastructure cost, license dynamics make Pivot's account more valuable, NetSuite's posture might shift)? What counter-arguments would Matt's CFO raise and does the memo answer them? Are the action items complete?

**9. Audience calibration.** Matt is described in the source materials as a COO who "makes decisions; doesn't rely on SMEs." Sandra is described as relying on her SMEs. The documents need to work for both styles simultaneously. Where does the writing bias toward one style at the expense of the other?

**10. What's missing.** What questions would Matt ask after reading these three documents that the documents don't answer? Be specific.

### Output format I want from you

Produce a single structured review document with these sections, in this order:

```
# Review of KBM + Pivot Unification Drafts

## Headline assessment
   [3-5 sentences. The honest top-line: are these drafts ready to circulate to Dustin/Jen/Matt as-is, with edits, or do they need a structural rework? Take a position.]

## Critical issues (blocking — must fix before circulation)
   [Numbered list. Each item: what's wrong, where (file + section), what to change. Be specific. If there are none, say so explicitly.]

## Significant issues (should fix — would weaken the document if not addressed)
   [Same format.]

## Minor issues (nice to fix — polish)
   [Same format.]

## Hidden gaps
   [What's in the source BRDs that didn't make it into the drafts but should have. Cite specific BRD sections.]

## Reconciliation principle audit
   [Decision-by-decision count: how many recommendations lean KBM vs. Pivot vs. neutral? Is the balance defensible? Identify any decisions where the principle was applied weakly.]

## Format scalability assessment
   [For each of the 9 remaining process areas (Marketing, Pre-Quote, Order Management, Operations, Project Management, Commissions, Financial Management, BI, System Setup), one paragraph: will the template work as-is, with adaptation, or needs rethinking?]

## Doc A pressure test
   [Stress-test of the account memo's logic. Counter-arguments. Open risks.]

## What Matt will ask that the document doesn't answer
   [List of specific questions.]

## Recommended next steps
   [Prioritized list of edits before circulation.]
```

Be terse. No filler. Cite file paths and section numbers when you reference text. If you disagree with a recommendation, say what you'd change it to. If you think the drafts are stronger than I think they are, also say that — but only if you mean it.
