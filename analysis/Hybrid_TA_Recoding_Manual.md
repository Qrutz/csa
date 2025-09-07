
# Hybrid Thematic Analysis — Manual Recoding Guide (for your thesis)

This is a **step‑by‑step manual** for recoding your survey data using a **hybrid (deductive + inductive) thematic analysis** that directly addresses the examiner’s concerns about bias, traceability, and alignment with RQs.

---

## 0) What you’re producing (end goals)

You will end up with:
1) A **Coding Sheet (long form)** where each row is one open‑text answer tagged with Participant ID and Question ID, coded into a **Domain → Subtheme → Codes** structure.  
2) A short **Codebook** (Domains with definitions, include/exclude rules, example codes).  
3) Two small **mapping tables** for the thesis (RQ↔Items and Domain↔Items).  
4) **Prevalence counts** per Domain/Subtheme (number of participants mentioning each).  
5) A cleaned **Results** section that follows the Domain template (Operationalization → Prevalence → Subthemes+Codes → Tagged Quotes → Negative case → Proposed changes).

---

## 1) Lock your analytic frame

### Research Questions
- **RQ1:** What challenges do annotators report in their data‑labeling work?  
- **RQ2:** What changes do annotators propose to make data labeling more fair and sustainable?

### Domains (deductive; chosen to fit your data)
1. **Compensation & Economic Security**  
2. **Task Design & Time Pressure**  
3. **Transparency & QA**  
4. **Content Exposure & Emotional Load**  
5. **Platform Reliability & Access**  
6. **Support & Dispute Resolution**  
**Cross‑cutting tag:** *Fairness & Recognition* (use as a tag across domains, not as a separate domain).

> You’ll derive **inductive Subthemes** and **Codes** inside each Domain from the actual text responses.

---

## 2) Prepare your Coding Sheet (manual, no scripting)

Use Excel/Google Sheets.

### 2.1 Create a new file
- Name it `coding_sheet.xlsx` (or a Google Sheet).  
- Create a sheet named **`coding_long`** with columns:
  - `PID` (Participant ID like P01..P50)  
  - `QuestionID` (e.g., Q7_explain, Q9_followup, Q10_effects, Q11_describe, Q12_challenges, Q13_improvements)  
  - `Text` (the respondent’s open‑text answer)  
  - `Q7_choice`, `Q8_choice`, `Q9_choice`, `Q10_choice`, `Q11_choice` (leave blank unless applicable to that row)  
  - `Domain`, `Subtheme`, `Codes`, `QuoteCandidate (Y/N)`, `Notes`

### 2.2 Populate rows (copy/paste from your survey export)
For each of these **open‑text** items, paste only **non‑empty** responses into `coding_long`:

- **Q7_explain** — “Why or why not?” (pay fairness explanation)  
- **Q9_followup** — “If yes, what happened?” (rejection/unpaid details)  
- **Q10_effects** — “If harmful content, how did it affect you?”  
- **Q11_describe** — “Please describe your transparency experience.”  
- **Q12_challenges** — “Biggest challenges or ethical concerns.”  
- **Q13_improvements** — “What would make labeling more fair/sustainable?”

Tips:  
- Add **`PID`** (P01..P50). If your export lacks IDs, create them via a helper index (e.g., in Sheets: fill 1..50 then format as `P00` using a custom number format).  
- When you paste a Q7_explain row, also copy that respondent’s closed choice (e.g., `Q7_choice = Yes/No/Unsure`) into the same row (helps context later). Repeat similarly for Q9/Q10/Q11 choices when relevant.

---

## 3) Calibration pass (≈20% of rows)

Before full coding, do a calibration pass to set stable rules.
1. Filter `QuestionID = Q12_challenges` and **code ~40–50 rows** spread across PIDs.  
2. For each row:
   - Assign **one best‑fit `Domain`** (use the routing rules below).  
   - Create short **`Codes`** (comma‑separated, e.g., `no_reason_rejection; opaque_ratings`).  
   - Group your codes into a **`Subtheme`** (e.g., *Opaque acceptance criteria*).  
   - Mark **`QuoteCandidate = Y`** for clear, representative quotes.
3. If two people are coding: both code the same calibration slice and **reconcile**. If solo: do a pass, take a break, revisit and tighten.

### Routing rules (to avoid misplacement)
- **Task Design & Time Pressure** = instructions clarity, examples, timers, complexity mismatch.  
  ↳ If the core issue is *why* work was accepted/rejected → **Transparency & QA**.  
- **Transparency & QA** = acceptance criteria, reason codes, ratings, downstream use.  
  ↳ If the core issue is *pay level/volatility* → **Compensation**.  
- **Compensation & Economic Security** = level/stability of pay, unpaid overhead, bonuses.  
  ↳ If the core issue is timer/complexity (not pay) → **Task Design**.  
- **Content Exposure & Emotional Load** = disturbing content, fatigue, after‑effects.  
  ↳ If mainly about policy fairness → keep Domain as Transparency/Support and apply *Fairness* tag.  
- **Platform Reliability & Access** = glitches/timeouts, task availability/routing, regional disparities.  
  ↳ If mainly about comms/appeals → **Support & Dispute Resolution**.  
- **Support & Dispute Resolution** = clarifications, feedback, human support, appeals responsiveness.  
  ↳ If mainly about criteria opacity (not responsiveness) → **Transparency & QA**.

Document any edge rules in your **Codebook** (next step).

---

## 4) Build your Codebook (living document)

In a new sheet **`codebook`**, make a table:

| Domain | Definition | Includes (examples) | Excludes (route to) | Primary Items |
|---|---|---|---|---|
| Compensation & Economic Security | Adequacy/stability of pay; unpaid overhead; effort–pay mismatch | low effective hourly; unpaid search/quals; unclear bonuses | timers/instructions → Task Design | Q7_explain, Q8_choice, Q12_challenges (+Q13 for fixes) |
| Task Design & Time Pressure | Clarity/stability of instructions; time limits; complexity mismatch | vague/shifting guidelines; missing examples; unrealistic timers | criteria/ratings → Transparency & QA | Q9_followup, Q12_challenges (+Q11 context; +Q13) |
| Transparency & QA | Opaque review/acceptance; ratings; downstream use | no reason codes; unclear criteria; opaque rating effects | pay issues → Compensation; response speed → Support | Q11_describe, Q12_challenges (+Q13) |
| Content Exposure & Emotional Load | Disturbing content; fatigue/burnout; after‑effects | violence/abuse; lingering distress; numbness | policy fairness → Transparency/Fairness tag | Q10_effects, Q12_challenges (+Q13) |
| Platform Reliability & Access | Timeouts/glitches; task availability; routing/region | tech issues; scarcity; unstable access to good tasks | comms/appeals → Support | Q12_challenges (+Q2/Q6 context; +Q13) |
| Support & Dispute Resolution | Clarifications; feedback; appeals; human support | slow/no clarifications; no appeals; siloed comms | criteria opacity → Transparency & QA | Q12_challenges (+Q13) |

Also list **Subthemes** you discover under each Domain and 3–6 **example Codes** per Subtheme.

---

## 5) Full coding pass

- Continue coding all rows in `coding_long`.  
- You can give multiple `Codes` to a row, but pick **one** `Domain` (best‑fit).  
- Update the **Codebook** whenever you add/refine a Subtheme or code; keep includes/excludes clear.

**Quote policy:** at most **one quote per participant per Domain**. Prefer clarity and diversity across platforms/regions. Mark your choices with `QuoteCandidate = Y`.

---

## 6) Prevalence counts (participants, not quotes)

In Sheets/Excel:
1. Create a copy filtered to rows where `Domain` is not empty.  
2. **Domain prevalence:** count **distinct PIDs** per Domain.  
   - Excel Pivot: Rows=`Domain`; Values=`Distinct Count of PID` (turn on Data Model).  
   - Sheets: `=COUNTUNIQUE(FILTER(PID_range, Domain_range="Transparency & QA"))`  
3. **Subtheme prevalence:** same logic by `Subtheme`.  
4. Report as “n/50 (x%)” in Results.

Use closed items for **contextual %** (e.g., Q11 transparency ratings, Q9 rejections, Q10 exposure frequency).

---

## 7) Build the thesis mapping tables

### 7.1 RQ ↔ Items (place end of Methods or start of Results)
| RQ | Items used |
|---|---|
| RQ1 (Challenges) | Q7_explain, Q8_choice, Q9_followup, Q10_effects, Q11_describe, Q12_challenges |
| RQ2 (Proposed changes) | Q13_improvements (triangulated with patterns in Q7–Q11) |

### 7.2 Domain ↔ Items (immediately after)
| Domain | Q7 | Q8 | Q9 | Q10 | Q11 | Q12 | Q13 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Compensation & Economic Security | **X** | **X** |  |  |  | **X** | (ctx) |
| Task Design & Time Pressure |  |  | **X** |  | (ctx) | **X** | (ctx) |
| Transparency & QA |  |  |  |  | **X** | **X** | (ctx) |
| Content Exposure & Emotional Load |  |  |  | **X** |  | **X** | (ctx) |
| Platform Reliability & Access |  | (ctx) | (ctx) | (ctx) | (ctx) | **X** | (ctx) |
| Support & Dispute Resolution |  |  | (ctx) | (ctx) | (ctx) | **X** | (ctx) |

*(X = direct evidence; (ctx) = contextual)*

---

## 8) Write the Results per Domain (repeat this template)

> **Operationalization.** Supported by **[list Items: e.g., Q11_describe and Q12_challenges]**; **Q13_improvements** supplies proposed changes.  
> **Prevalence.** n/50 (x%). Include relevant closed‑item context (e.g., % who reported rejections, exposure freq).  
> **Subthemes (inductive) + example Codes.** List 2–4 subthemes; under each, 2–4 code labels.  
> **Evidence (tagged quotes).** 2–3 quotes with tags like `[P16, Q9]` from different participants.  
> **Negative case (contrast).** One sentence showing a counterexample so it’s not cherry‑picked.  
> **Proposed changes (from Q13).** 2–4 bullets that match the pain points.

Do this for all six Domains. Then add a separate **“RQ2 — Worker‑proposed changes”** subsection that aggregates the Q13 bullets across Domains.

---

## 9) Methods text to paste (makes TA explicit)

> **Analytic approach.** We used a **hybrid thematic analysis**: a **deductive** frame from our instrument and prior work (Domains: Compensation & Economic Security; Task Design & Time Pressure; Transparency & QA; Content Exposure & Emotional Load; Platform Reliability & Access; Support & Dispute Resolution) and **inductive** open coding of free‑text to derive **codes** and then **subthemes** within each domain. Following Braun & Clarke, we (i) familiarized ourselves with the data, (ii) generated initial codes inductively, (iii) collated codes into candidate subthemes per domain, (iv) reviewed and refined subthemes for coherence and distinction, and (v) defined final subthemes with representative quotes. We double‑coded an initial subset (~20%) to align interpretations, reconciled discrepancies, and then completed coding. We report domain/subtheme prevalence (distinct participants), include contrasting cases, and tag quotes with participant and item (e.g., [P28, Q10]) to preserve traceability.

Add a one‑liner: *“One quote per participant per domain; near‑duplicate quotes were collapsed and represented via prevalence counts.”*

---

## 10) Final checklist (examiner‑proof)

- [ ] RQs reduced to **two** (RQ1 challenges, RQ2 changes).  
- [ ] **No** RQ3/4 mentions anywhere.  
- [ ] Coding Sheet complete; **Domain/Subtheme/Codes** filled.  
- [ ] Codebook has **includes/excludes** and example codes; routing rules captured.  
- [ ] Prevalence = **distinct participants** per Domain/Subtheme.  
- [ ] Quotes tagged **[PID, Q#]**, one per participant per domain; at least one **negative case** per domain.  
- [ ] RQ↔Items and Domain↔Items tables present.  
- [ ] Results re‑written by Domain using the template.  
- [ ] Discussion = interpretation + implications (no new RQs), Limitations explicit.  
- [ ] Cover page fixed; Abstract doesn’t claim measurements you didn’t do.

---

## 11) Common mistakes to avoid

- Mixing up **Task Design** (instructions/timers) with **Transparency & QA** (criteria/ratings/appeals).  
- Using many quotes from the same participant — violates breadth; use prevalence counts instead.  
- Claiming you measured annotation **quality/IAA** — you didn’t; discuss **implications** only.  
- Treating **Fairness** as a dumping ground — keep it as a **cross‑cutting tag**, not its own domain unless the quote is primarily about fairness of process/recognition.

---

### That’s it.
If you follow this manual, you’ll have a clean audit trail from **Items → Codes → Subthemes → Domains → Results**, exactly what the examiner asked for.
