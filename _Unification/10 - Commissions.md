# 3.07 — Commissions

| Field | Value |
|---|---|
| **Decision density** | **Medium** — Pivot-only BRD; compensation-model design for the merged company; KBM's commission framework lived inside Order Management and Financial Management without a separate BRD |
| **Source coverage** | Pivot Commissions BRD v2.0 (Pivot-only); KBM commission-related requirements within Order Management and Financial Management source materials |
| **KBM source** | KBM commission structure addressed in Order Management REQ-035, REQ-036, REQ-037, REQ-038 (`Order Management/KBMH/3 Output/Requirements_Map_OrderManagement_v1.0.md`) and Financial Management §8 (15% labor markup, Project GP vs. Commissionable GP framework) |
| **Pivot BRD** | `Commissions/Pivot/4 BRD/09_Pivot Interiors BRD Commissions Process Area_v1.0.docx` (markdown copy at `_Unification/working/pivot-brds-md/Commissions.md`) |

---

## 3.07.1 How each company approaches Commissions today

**KBM Hogue** addresses commissions within its broader Order Management and Financial Management source materials rather than as a separate process area. The framework includes header-level commission assignment with split-percentage capability across multiple sales reps (Order Management REQ-035), a line-level commissionable flag for marking individual lines as commission-eligible (REQ-036), and the Project GP vs. Commissionable GP framework (REQ-037) tied to the 15% labor markup that has been eliminated per Financial Management §3.08 D-4. KBM's framework also includes specific business rules: storage fees are always commissionable, billed back to client; the labor markup formula line was historically used to flow markup-driven commissions. KBM's commission framework reflects its operating model — relationship-led sales with multi-rep splits common, and an explicit distinction between the GP that is commission-eligible and the GP that reflects true project profitability.

**Pivot Interiors** has a dedicated Commissions BRD that articulates the commission framework as a stand-alone process area. Pivot's framework covers commission-rate structures, eligibility rules, payout timing, multi-rep splits, accelerators and SPIFs, internal cross-division referral compensation (cross-references CRM §3.02 D-3c), and reporting on commission performance. Pivot's BRD reflects its larger sales organization (divisional structure with NBD, Venture, Public, and Construction Solutions per CRM §3.02 D-3b) where compensation design is a more complex and structured operational concern.

The merged company needs a unified compensation framework. The merged-company commission decisions span: commission basis (commissionable GP per CRM §3.02 D-6 — quoted labor rates — with the 15% markup eliminated per Financial Management §3.08 D-4), rate structure, multi-rep split mechanics, eligibility rules, payout timing, internal-referral compensation, tiered rates and bonus programs, and reporting. Both companies' inputs contribute, and several decisions belong to merged-company sales and finance leadership rather than the system itself.

## 3.07.2 Where the two companies align

**Common ground across both companies' source materials:**

- Header-level commission assignment with split-percentage across multiple sales reps
- Line-level commissionable flag for individual lines
- Commission rate structures configured per role / sales tier
- Reporting on commission accruals by sales rep and period
- Customer Portal access for sales-rep visibility into their own commission position (where applicable)

**Aligned via locked decisions in other areas:**

- Dual GP framework (actual GP with time-tracked labor vs. commissionable GP with quoted labor) per CRM §3.02 D-6 / Financial Management §3.08 D-5 — commission calculation operates on the framework
- Internal referral attribution captured on opportunities per CRM §3.02 D-3c — referring person is captured at the CRM layer; compensation logic decided here
- 15% labor markup eliminated per Financial Management §3.08 D-4 — commissions calculate on actual labor cost
- 2.5x pipeline multiplier as coaching metric per CRM §3.02 D-9 — separate from commission calculation but provides leading-indicator context
- Sales rep scorecards as BI dashboard component per BI §3.09 D-9 — provides commission-position visibility

These are noted in the merged BRD; configuration proceeds against standard NetSuite Orion commission capabilities and the locked decisions above.

## 3.07.3 Where the two companies differ

Six in-area divergences. Each is presented as: how each company approached it (with attribution to context), the recommendation for the merged company, and the decision the leadership team owns.

---

### D-1. Commission basis — actual labor cost vs. quoted labor cost vs. markup-driven

**Source:** KBM Order Management REQ-038 and Financial Management §8 (15% labor markup); Pivot Commissions BRD §3 (commissionable basis); cross-references Financial Management §3.08 D-4 (labor markup eliminated) and CRM §3.02 D-6 (locked GP framework)

**KBM's approach.** KBM's historical framework used the 15% labor markup formula line to make commissions calculate on cost-plus-markup. The Project GP vs. Commissionable GP distinction reflected the markup difference.

**Pivot's approach.** Pivot's commission framework calculates on the dual GP basis (per CRM §3.02 D-6) — commissionable GP uses quoted labor rates; actual GP uses time-tracked labor costs. Commissions calculate against commissionable GP.

**Recommendation for the merged company.** Operate the merged company with commissions calculating on commissionable GP per the locked CRM §3.02 D-6 framework (quoted labor rates). The 15% labor markup is eliminated per Financial Management §3.08 D-4; commissions therefore calculate on the commissionable GP basis (quoted labor) rather than the prior cost-plus-markup pattern. Actual labor cost (time-tracked) feeds the actual GP view per the same dual GP framework, but commissions calculate against commissionable GP. Sales-team communication is required to set expectations on commission impact for KBM staff transitioning from the markup-driven framework.

**Decision for the leadership team.** Confirm: commissions calculate on commissionable GP (quoted labor rates) per CRM §3.02 D-6 framework. *Recommended default: yes.* (Sales-team communication required for KBM staff.)

---

### D-2. Commission rate structure

**Source:** Pivot Commissions BRD §3 (rate structures per role/tier); KBM source materials reference rates within commission framework but at less detail

**KBM's approach.** KBM's source materials reference commission rates within the broader framework but do not articulate a comprehensive rate structure with role/tier specificity at the level Pivot does.

**Pivot's approach.** Pivot's BRD articulates commission rate structures organized by role (designer / sales rep), sales tier (NBD vs. Venture vs. Public vs. Construction Solutions), product mix (MillerKnoll vs. non-MillerKnoll), and order type (standard vs. specialized). The structure supports differentiated rates that reflect Pivot's divisional sales motion.

**Recommendation for the merged company.** Design the merged-company commission rate structure as a leadership-team decision during the merged-company organizational alignment. The rate structure reflects the merged-company sales motion (per CRM §3.02 D-3 two-dimensional hierarchy), incorporates the merged-company division taxonomy (per CRM §3.02 D-3b), and accommodates both KBM's existing rate patterns and Pivot's existing rate patterns. Specific rates are not within the unification document's scope; the framework is.

**Decision for the leadership team.** Confirm: merged-company commission rate structure designed during organizational alignment with rates differentiated by role, division (per CRM §3.02 D-3b), and order type. *Recommended default: confirm at session; specific rates determined during organizational alignment.*

---

### D-3. Multi-rep split mechanics

**Source:** KBM Order Management REQ-035 (header-level commission with split capability); Pivot Commissions BRD §3 (multi-rep splits)

**KBM's approach.** KBM articulates header-level commission assignment with split-percentage capability across multiple sales reps. Splits are typically pre-defined at order entry.

**Pivot's approach.** Pivot articulates multi-rep splits within the commission framework with similar capabilities, plus support for influencer attribution (per CRM §3.02 D-3c) where internal cross-division referrals receive compensation.

**Recommendation for the merged company.** Adopt header-level commission assignment with split-percentage capability per both companies' frameworks, integrated with the internal referral attribution capability (per CRM §3.02 D-3c) to support cross-division referral compensation. Specific split-percentage rules and approval requirements are configured during Realize phase.

**Decision for the leadership team.** Confirm: header-level commission with split-percentage capability across multiple reps; integrated with internal referral attribution for cross-division compensation. *Recommended default: yes.*

---

### D-4. Internal cross-division referral compensation

**Source:** Pivot Commissions BRD; cross-references CRM §3.02 D-3c (internal referral attribution capability locked)

**KBM's approach.** KBM does not have multiple sales divisions in its current framework; cross-division referral is therefore not articulated.

**Pivot's approach.** Pivot articulates internal cross-division referral compensation — when furniture sales refers Construction Solutions or vice versa, the referring person receives compensation. The capability is identified as critical for both reporting and referral compensation.

**Recommendation for the merged company.** Adopt Pivot's internal cross-division referral compensation framework as the merged-company default. The capability is enabled by the CRM-locked internal referral attribution (per CRM §3.02 D-3c). Specific compensation rates, eligibility rules, and timing are determined during organizational alignment as part of the merged-company commission rate structure design (D-2).

**Decision for the leadership team.** Confirm: internal cross-division referral compensation framework adopted from Pivot; specific rates determined during organizational alignment. *Recommended default: yes.*

---

### D-5. Commission eligibility rules and timing

**Source:** Pivot Commissions BRD (invoice-date trigger with cumulative annual calculation); KBM Financial Management raises booking-vs-invoicing-vs-payment as an open question

**KBM's approach.** KBM addresses commission eligibility within Order Management decisions: storage fees always commissionable (KBM REQ-015), line-level commissionable flag for individual lines, header-level multi-rep split. KBM's Financial Management materials raise commission timing (booking vs. invoicing vs. payment collection) as an open question for organizational decision-making.

**Pivot's approach.** Pivot's Commissions BRD specifies commissions are triggered on invoice date with cumulative annual calculation. Pivot's framework does not contemplate booking-trigger or payment-collection-trigger as alternative options; invoice-date with cumulative annual is the established pattern. Pivot's BRD also articulates web-vendor exclusions from commissionable revenue and a year-end reconciliation / true-up process.

**Recommendation for the merged company.** Adopt Pivot's invoice-date-trigger commission timing with cumulative annual calculation as the merged-company default. The reasoning is contextual: Pivot has the established pattern with year-end reconciliation, and the invoice-date trigger aligns commissions with revenue recognition (per Financial Management §3.08 D-3). KBM's Financial Management open question on timing is resolved by adopting this framework. Web-vendor exclusions (per Pivot Commissions BRD) and year-end reconciliation / true-up are configured per Pivot framework.

**Decisions for the leadership team.**

- (5a) Confirm: invoice-date commission trigger with cumulative annual calculation per Pivot framework. *Recommended default: yes.*
- (5b) Confirm: web-vendor exclusion rules and year-end reconciliation / true-up process per Pivot framework. *Recommended default: yes.*

---

### D-6. Tiered rates and bonus programs

**Source:** Pivot Commissions BRD (tiered rates, deposit bonus, teamed-account bonus, CS bonus tiers); KBM source materials reference rate structure but do not specifically articulate bonus programs

**KBM's approach.** KBM's source materials reference rate structure but do not specifically articulate tiered-rate accelerators or named bonus programs.

**Pivot's approach.** Pivot's BRD articulates tiered rates (rates that vary by attainment), a deposit bonus (0.5% on opportunities meeting a 7-day deposit threshold above $10,000), a teamed-account bonus for collaboration scenarios, and CS (Construction Solutions) bonus tiers. The framework supports time-bound and threshold-based programs that recognize specific operational behaviors.

**Recommendation for the merged company.** Adopt Pivot's tiered-rate and bonus-program framework as a merged-company capability. Whether the merged company carries each specific program (deposit bonus, teamed-account bonus, CS bonus tiers) into Phase 1 is a leadership-team decision during organizational alignment; the capability is configured to support each program when activated.

**Decision for the leadership team.** Confirm: tiered-rate and bonus-program capability configured for the merged company per Pivot framework (deposit bonus, teamed-account bonus, CS bonus tiers); specific program activation determined during organizational alignment. *Recommended default: yes.*

---

## 3.07.4 Cross-area dependencies

| Dependency | Where it surfaced in Commissions | Where it's decided |
|---|---|---|
| **Dual GP framework (actual vs. commissionable)** | Commission basis (D-1) | **CRM (§3.02 D-6)** — GP framework locked; **Financial Management (§3.08 D-5)** — operationalized |
| **15% labor markup elimination** | Commission basis on actual vs. cost-plus-markup (D-1) | **Financial Management (§3.08 D-4)** — labor markup eliminated |
| **Internal referral attribution capability** | Cross-division referral compensation (D-4) | **CRM (§3.02 D-3c)** — capability locked; compensation logic decided here |
| **Division taxonomy** | Rate differentiation by division (D-2) | **CRM (§3.02 D-3b)** — division taxonomy pending |
| **Sales rep scorecards** | Commission-position visibility on rep dashboards | **BI (§3.09 D-9)** — scorecards as BI dashboard component |
| **Pipeline multiplier (2.5x)** | Coaching metric separate from commission calculation | **CRM (§3.02 D-9)** — multiplier locked |
| **Approval workflow framework** | Commission approval / adjustments | **Order Management (§3.04 D-1)** — approval framework |
| **Payroll provider integration** | Commission payouts feed payroll | **Financial Management §3.08.8 #9** — payroll provider |
| **Sales hierarchy** | Manager visibility into team commission performance | **CRM (§3.02 D-3a, D-3b)** — two-dimensional hierarchy |

## 3.07.5 Recommendation summary

The merged-company Commissions playbook in shorthand:

- **Commission basis:** Commissionable GP per CRM §3.02 D-6 framework (quoted labor rates); 15% labor markup eliminated per Financial Management §3.08 D-4
- **Rate structure:** Designed during organizational alignment, differentiated by role, division (per CRM §3.02 D-3b), and order type
- **Multi-rep splits:** Header-level commission with split-percentage; integrated with internal referral attribution for cross-division compensation
- **Internal cross-division referral compensation:** Pivot framework adopted; rates during organizational alignment
- **Commission eligibility and timing:** Pivot framework adopted; specific timing (booking / invoicing / payment) at working session
- **Accelerators and SPIFs:** Capability configured; usage determined during organizational alignment
- **Reporting:** Commission accruals visible on rep dashboards (per BI §3.09 D-9 sales scorecards) and on manager dashboards via two-dimensional hierarchy (per CRM §3.02 D-3a, D-3b)

Net read: the merged-company Commissions function builds on Pivot's structured commission framework while incorporating KBM's specific patterns (storage fees commissionable, line-level commissionable flag, header-level multi-rep splits). The biggest operational decisions — specific rates, timing, and accelerator usage — are leadership-team decisions made during the merged-company organizational alignment, not within the unification document's scope. The system supports the framework regardless of those operational choices.

## 3.07.6 Decisions for the leadership team

| # | Decision | Default | Reference |
|---|---|---|---|
| 1 | Commissions calculate on commissionable GP per CRM §3.02 D-6 (quoted labor rates) | Yes | D-1 |
| 2 | Merged-company commission rate structure designed during organizational alignment | Confirm at session | D-2 |
| 3 | Header-level commission with split-percentage; integrated with internal referral attribution | Yes | D-3 |
| 4 | Internal cross-division referral compensation framework adopted from Pivot | Yes | D-4 |
| 5a | Pivot's commission eligibility and timing framework adopted | Yes | D-5 |
| 5b | Commission timing (booking / invoicing / payment / staged) | Confirm at session | D-5 |
| 6 | Accelerator and SPIF capability configured; usage during organizational alignment | Yes | D-6 |

> 7 decisions: 5 with default-yes recommendations and 2 (decisions 2 and 5b) requiring leadership-team selection during the working session and organizational alignment.

## 3.07.7 Configuration carryover

| Item | KBM-side built? | Pivot-side built? | Action for merged company |
|---|---|---|---|
| Header-level commission with split-percentage | Specified | Specified | Configure per common-ground items |
| Line-level commissionable flag | Specified | Specified | Configure per common-ground |
| 15% labor markup formula line | Specified | Not present | Eliminate per Financial Management §3.08 D-4 |
| Dual GP framework (commission basis) | Specified (markup-driven) | Specified (quoted labor) | Operate on Pivot framework per D-1 |
| Commission rate structure | Specified at lower detail | Specified | Build merged structure per D-2 |
| Internal cross-division referral compensation | Not specified (no divisions) | Specified | Configure per D-4 |
| Commission timing rules | Less articulated | Specified | Configure per D-5 |
| Accelerators and SPIFs | Not specified | Specified | Build per D-6 |
| Storage fees commissionable | Specified | Not specified | Configure per common-ground |

## 3.07.8 Open questions / inputs needed

1. **Merged-company commission rate structure** (decision 2) — specific rates by role, division, order type determined during organizational alignment with sales and finance leadership.
2. **Commission timing decision** (decision 5b) — at booking, invoicing, payment collection, or staged; affects cash flow and rep behavior; confirmed at working session.
3. **KBM staff transition communication** (decision 1) — sales-team communication plan for KBM staff moving from markup-driven commission framework to commissionable-GP-on-quoted-labor framework.
4. **Specific cross-division referral rates** (decision 4) — internal referral compensation rates determined during organizational alignment.
5. **Accelerator and SPIF Phase 1 usage** (decision 6) — whether to actively use accelerators and SPIFs at go-live or defer; leadership-team decision.
6. **Commission approval and adjustment workflow** — specific approval thresholds and approver roles for commission adjustments; determined during organizational alignment in coordination with Order Management §3.04 D-1 approval framework.
7. **Pivot Commissions stakeholder review** — Pivot Commissions BRD stakeholders review merged-company recommendations before the working session.
8. **Historical commission data migration** — historical commission records and accruals migration scope finalized during data-migration planning (cross-references System Setup §3.10 D-5).
