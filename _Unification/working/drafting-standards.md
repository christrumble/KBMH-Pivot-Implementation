# Drafting Standards — KBM + Pivot Unification Documents

Reference for the next 9 process area sections. Derived from Chris Trumble's review of the CRM sample, May 4, 2026. Apply consistently across all sections. Update this file when new conventions surface.

---

## Verified people and entities

Use these names exactly. Do not abbreviate, paraphrase, or reorder.

| Role | Name | Notes |
|---|---|---|
| KBM (the company) | **KBM Hogue** | Not "Hoag." Full company name when first introduced; "KBM" thereafter is acceptable |
| Pivot (the company) | **Pivot Interiors** | Full name when first introduced; "Pivot" thereafter is acceptable |
| Merged-company COO | **Matt Denning** | KBM Hogue's COO; ultimate decision-maker |
| Pivot leadership | **Sandra Rudloff** | |
| GSI leadership | **Dustin Doucette**, **Jennifer Trask** | Both surnames are different — do not assume "Trask" applies to both |
| Authoring team | **Marcus Dallacqua** (Proprio), **Chris Trumble** (GSI), **Debbie Herbert** (GSI PM), **Jeanine Post** (GSI Functional Consultant) | |

**Verification rule:** Before introducing any new named individual in any section, confirm spelling against a primary source (BRD authors block, Decision Makers folder, transcripts). Do not infer or guess.

## Document references

| Don't use | Use |
|---|---|
| "Doc B" | "the recommendation document" or "the unification recommendation" |
| "Doc Zero" | "the approach document" |
| "the pilot" | "the sample" |
| "01 - CRM (Pilot).md" | "01 - CRM (Sample).md" |

Refer to documents by purpose, not by internal numerical labels. Section cross-references use § + section number (e.g., "§3.04" for Order Management).

## Terminology preferences

| Don't use | Use |
|---|---|
| "spec'd" | "specified" |
| "2.5×" (unicode) | "2.5x" (ASCII letter x) |
| "red/yellow/green" / "R/Y/G" / "stoplight" / "traffic-light" indicators | "coaching threshold tiers" / "tiered status indicators" / "tiered indicators" |
| Emoji color codes (🟢🟡🟠🔴) anywhere | Words only ("Low" / "Medium" / "High") |
| "Color guidance for X:" | "X definitions:" |
| Casual abbreviations of any kind | Spell out |
| "Doc B's structure" | "the document's structure" |

Avoid casual or AI-flavored phrasing:
- "Stating it up front matters because" → "We state it up front because"
- "Recommendation attributes" → "The recommendation attributes" (don't drop articles)
- "Configuration is straightforward" — fine
- "It's a good fit" — too casual; prefer "It fits the merged company's situation"

## Voice and tone

These rules carry forward from earlier conversations and are non-negotiable.

**Reconciliation principle (verbatim, do not modify):**

> Where the two companies converge, the path is clear. Where they diverge, the recommendation leans toward the approach whose context — operational footprint, customer mix, organizational scale, or strategic priorities — most closely matches the merged company's situation. The recommendation is never about which approach is "better"; it is about which direction the merged company is best positioned to operate from.

**Tone rules:**

1. **No comparative judgment language.** Never "more sophisticated," "more mature," "stronger," "weaker," "where their thinking was sharper," "lacks," "fails to," etc.
2. **Attribute approaches to context.** "KBM's approach reflects [their California sales motion / their relationship-led pipeline / their goal of consolidating activity]." "Pivot's approach reflects [their divisional structure / their MillerKnoll-Certified position / their in-house operations footprint]."
3. **Recommendations are forward-looking.** "Operating from [Company]'s framework positions the merged company well because [context-based reasoning]." Not "[Company] got it right."
4. **No advocacy or political commentary.** No "would do real damage to morale," "doesn't care strongly," "where their thinking was sharper." No internal-drafting commentary about which leadership team gets surprised.
5. **No self-deprecating quotes from BRDs.** Even if a company described its own pain colorfully (e.g., KBM's "poo in, poo out"), don't surface those phrases in the unification doc. Reflecting them back to the team is unnecessary and risks landing wrong.
6. **Both companies are credited.** Each section's "Recommendation summary" or "Net read" paragraph names what each company contributes to the merged-company outcome, framed positively for both.

## Style and grammar

- **Singular pronoun agreement** for "the company" — *it / its*, not *they / their*. ("Each company entered Orion implementation with established business processes shaped by how each operated at the time.")
- **Comma after introductory clauses.** ("Originally framed around Construction Solutions, but explicitly broadened in the Feb 2026 review session...")
- **Active where possible.** "We state it up front because" not "Stating it up front matters because."
- **Em-dash (—) for parenthetical asides**, with spaces on either side.
- **Section references** use § (U+00A7) — do not write "section" in body text when referencing.
- **Em-dash, en-dash, hyphen** — em-dash for breaks, hyphen for compound words; avoid en-dash unless representing a range.

## Per-area section template

Verbatim from Chris-edited Doc Zero §6:

```
3.0X — [Process Area]
  Decision density:    [Low / Medium / High + one-line headline]
  Source coverage:     [What KBM and Pivot evidence is available]

  3.0X.1  How each company approaches [process area] today
  3.0X.2  Where the two companies align
  3.0X.3  Where the two companies differ
  3.0X.4  Cross-area dependencies
  3.0X.5  Recommendation summary
  3.0X.6  Decisions for the leadership team
  3.0X.7  Open questions / inputs needed
```

Plus a header table with: Decision density, Source coverage, KBM source path, Pivot source path.

## Divergence (D-X) entry pattern

Each in §3.0X.3 follows this exact structure:

```
### D-N. [Title — capability or design choice]

**Source:** [KBM REQ-IDs from BRD with section reference]; [Pivot REQ-IDs from BRD with section reference]; [transcript references where applicable]

**KBM's approach.** [Neutral description with attribution to KBM's context]

**Pivot's approach.** [Neutral description with attribution to Pivot's context]

**Recommendation for the merged company.** [Forward-looking, context-attributed, naming what each company contributes when both are involved]

**Decision for the leadership team.** [Explicit decision, with default recommendation]
```

For decisions with sub-parts (e.g., D-3 has 3a / 3b / 3c), use a decisions list:

```
**Decisions for the leadership team.**

- (Na) [...] *Recommended default: yes.*
- (Nb) [...] *Recommended default: confirm at session.*
- (Nc) [...] *Recommended default: yes.*
```

## Decisions table format

In §3.0X.6:

```
| # | Decision | Default | Reference |
|---|---|---|---|
| 1 | [Decision text] | Yes | D-1 |
| 2a | [Decision text] | Yes | D-2a |
| 2b | [Decision text] | Confirm at session | D-2b |
```

Always include a footer line:

> N decisions: X with default-yes recommendations and Y requiring leadership-team input during the working session.

Math must reconcile against the table.

## Cross-area dependencies pattern

Items decided in another area but surfacing here go in §3.0X.4 with this table:

```
| Dependency | Where it surfaced in [Area] | Where it's decided |
|---|---|---|
| **[Dependency name]** | [Source ref] | **[Other Area (§3.0X)]** — [one-line why it lives there] |
```

Do not duplicate the decision in both areas. Cross-reference only.

## Source citation rules

Every divergence cites:
- KBM REQ IDs with file path and section number, e.g., `KBM REQ-016 (BRD_CRM_v1.0.md §5)`
- Pivot REQ IDs with file path, e.g., `Pivot REQ-3.01.01 (CRM.md §3.01)`
- Transcript references where the source is a recorded session, e.g., `Pivot Feb 2026 review session`

If a company's BRD does not address a specific capability, say so explicitly: *"Pivot's CRM BRD does not specifically address [capability]"* — not silence.

## Configuration carryover (§3.0X.7)

Pattern:

```
| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| [Capability] | [State, e.g., "In progress (early Realize)"] | [State] | [Action, with reference to D-N] |
```

Use "Specified" not "Spec'd."

## Open questions (§3.0X.8)

Numbered list of:
1. Items genuinely unknown that depend on leadership-team input
2. Cross-section dependencies that resolve in other process areas
3. Items raised in transcripts but not yet integrated into BRDs

Do not include internal drafting commentary about how the document might be received.

## Pre-circulation check

Before declaring a section ready, verify:

- [ ] All named individuals match the verified people directory
- [ ] No "spec'd," "2.5×," or R/Y/G language
- [ ] No emojis in headers or tables
- [ ] No comparative-judgment language
- [ ] Both companies' contributions named in §3.0X.5
- [ ] Decisions table math reconciles
- [ ] Cross-area dependencies (§3.0X.4) cross-reference; do not duplicate
- [ ] Source citations on every divergence
- [ ] Singular pronoun agreement throughout
