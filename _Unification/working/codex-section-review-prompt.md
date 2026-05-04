# Codex Section Review Prompt — Reusable Template

Used after each individual process area section is drafted. Pass the section file plus the standing context. The goal is to catch issues at section-N-time, before they propagate into later sections that inherit the same patterns.

---

## How to invoke

```bash
cd /Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation
codex exec --sandbox read-only --skip-git-repo-check -m gpt-5.5 \
  -C /Users/marcusdallacqua/Documents/KBMH-Pivot-Implementation \
  -o _Unification/working/codex-review-{SECTION_SLUG}.md \
  - < _Unification/working/codex-section-review-prompt-rendered.txt \
  > _Unification/working/codex-run-{SECTION_SLUG}.log 2>&1 &
```

Render the prompt by substituting:
- `{SECTION_NUMBER}` (e.g., `3.09`)
- `{SECTION_NAME}` (e.g., `Business Intelligence`)
- `{SECTION_FILENAME}` (e.g., `_Unification/02 - BI.md` — actual filename TBD)
- `{KBM_BRD_PATH}` (e.g., `Business Intellegence/KBMH/3 Output/BRD_BusinessIntelligence_v1.0.md`)
- `{PIVOT_BRD_PATH}` (e.g., `_Unification/working/pivot-brds-md/Business_Intellegence.md`)
- `{COMPLETED_SECTIONS}` — list of locked section files Codex should treat as already-decided context (e.g., `_Unification/01 - CRM (Sample).md`)

---

## Prompt template (copy below the rule, render placeholders, pipe to codex)

---

You are an experienced ERP implementation consultant with deep knowledge of contract furniture dealer operations and NetSuite/Orion. You are reviewing a draft section of the **KBM + Pivot Unification Recommendation**, a multi-section document being produced incrementally for the merged organization led by Matt Denning. Sandra Rudloff leads the Pivot side. The document's purpose, principles, and per-area template are defined in `_Unification/00 - Approach.md`.

This review is **per-section, mid-project**. Catching issues now is much cheaper than after later sections are drafted on top.

### Section under review

- **Section number:** {SECTION_NUMBER}
- **Section name:** {SECTION_NAME}
- **Section file:** `{SECTION_FILENAME}`

### Source materials for this section

- **KBM BRD (or equivalent):** `{KBM_BRD_PATH}` (use exactly this path; if a section has gap-analysis-only or no KBM source, the section file's header will note it)
- **Pivot BRD (markdown copy):** `{PIVOT_BRD_PATH}`
- **Pivot original docx:** in `*/Pivot/4 BRD/` (markdown copy is the working source)
- **Transcripts** in `_Pivot Discovery/Transcripts/` and `_Raw Transcripts/` may be relevant; cite if used

### Standing context the section must respect

These files are the project's working memory and must be treated as authoritative:

1. **`_Unification/00 - Approach.md`** — Doc Zero (locked). Reconciliation principle, per-area template, traffic-light index, working-session methodology.
2. **`_Unification/01 - CRM (Sample).md`** — CRM section (locked). Tone calibration reference. Decision-density and template-execution example.
3. **`_Unification/working/drafting-standards.md`** — Names, terminology, tone rules, formatting conventions. Treat as binding.
4. **`_Unification/working/cross-area-decisions.md`** — Cross-section decision threads. The section under review must reflect any locked decisions and must defer correctly to home sections for any deferred decisions.
5. **`_Unification/working/project-status.md`** — Where the project is. Locked decisions list at the bottom.
6. **Already-locked sections:** {COMPLETED_SECTIONS}

### Reviewer lenses (apply all)

**1. Standards compliance.** Does the draft follow `drafting-standards.md` exactly? Specifically check:
- All named individuals match the verified people directory (KBM Hogue, Matt Denning, Sandra Rudloff, Dustin Doucette, Jennifer Trask, Chris Trumble, Debbie Herbert, Jeanine Post)
- No "spec'd," "2.5×," "R/Y/G," or "stoplight" language
- No emojis in headers or tables
- Singular pronoun agreement ("the company...it...its")
- Em-dash usage with spaces
- "Specified" not "Spec'd"
- Section reference style (§3.0X)

**2. Source accuracy.** For every claim made about KBM or Pivot in the section, verify against the source BRDs at the paths above. Flag any factual errors, misrepresentations, or claims that go beyond what the source supports. Cite specific source lines or section numbers.

**3. Tone calibration.** Read the section as a Pivot leadership team member and as Matt Denning. Surface any sentence, phrase, or framing that reads as evaluative, comparative-in-a-grading-sense, or politically loaded. Compare tone calibration against the locked CRM sample — the section's tone should be consistent with it. Quote specific lines that drift.

**4. Cross-area consistency.** Check `cross-area-decisions.md` and verify:
- The section correctly defers decisions that belong to other sections (do not over-commit on cross-area items)
- The section correctly reflects locked decisions from earlier sections (do not contradict them)
- New cross-area dependencies the section surfaces are properly flagged for inclusion in `cross-area-decisions.md`
- The section does not duplicate decisions that are owned elsewhere

**5. Template fidelity.** Does the section follow the per-area template defined in `00 - Approach.md` §6 exactly? Specifically check:
- Header table includes Decision density, Source coverage, both BRD paths
- §3.0X.1 "How each company approaches today" written neutrally with attribution to context
- §3.0X.2 "Where they align" — items are credible alignment, not stretches
- §3.0X.3 "Where they differ" — every divergence has Source / KBM's approach / Pivot's approach / Recommendation / Decision
- §3.0X.4 "Cross-area dependencies" — flag and cross-reference, do not duplicate
- §3.0X.5 "Recommendation summary" — credits both companies' contributions
- §3.0X.6 "Decisions for the leadership team" — table format with reconciling math footer
- §3.0X.7 "Open questions / inputs needed" — no internal drafting commentary

**6. Decision quality.** For each decision presented:
- Is the recommendation supported by the BRD evidence?
- Is the *default* (Yes / Confirm at session) the right one given the reconciliation principle?
- Is the decision granularity right? Should any decision be split or combined?

**7. Reconciliation principle audit.** Count merged-company recommendations leaning KBM / leaning Pivot / hybrid / neutral. Is the balance defensible on context grounds? The principle is: lean toward the approach whose context most closely matches the merged company's situation. Flag decisions where the principle was applied weakly.

**8. What's missing.** Any requirement, capability, or transcript-derived item that should appear in this section but doesn't?

**9. Internal commentary check.** Drafting commentary about how leadership might react, internal political signals, or meta-notes about the document itself must NOT appear in the body of the section. Quote any that slipped in.

### Output format

```
# Codex Review — §{SECTION_NUMBER} {SECTION_NAME}

## Headline assessment
   [3-5 sentences. Is the section ready to lock, ready with edits, or needs structural rework?]

## Standards compliance
   [Pass / Fail per check. Cite specific violations with line refs.]

## Source accuracy
   [Pass / Fail. List factual errors with source citations.]

## Tone calibration
   [Pass / Fail. Quote any drift from CRM-sample-equivalent tone.]

## Cross-area consistency
   [Issues with deferred / locked decisions. New cross-area threads to add to cross-area-decisions.md.]

## Template fidelity
   [Pass / Fail per template element.]

## Decision quality
   [Per-decision notes where applicable.]

## Reconciliation principle audit
   [Count + assessment of balance.]

## What's missing
   [List of items.]

## Internal commentary
   [Quote any that slipped in.]

## Recommended edits before lock
   [Prioritized list. If "ready to lock as-is," say so explicitly.]
```

Be terse. Cite file paths and line numbers. If the draft is sound, say so plainly — do not manufacture issues. If the draft has structural problems, say so plainly even if uncomfortable.
