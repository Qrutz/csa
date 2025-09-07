# Codebook — Hybrid Thematic Analysis (Domains → Subthemes → Codes)

This is the **final codebook** to include in your appendix. It is designed to be audit‑friendly for the examiner.

**How to read:**  
- **Domains** = deductive buckets aligned with your instrument and prior work.  
- **Subthemes** = inductive groupings derived from codes in open‑text answers.  
- **Codes** = short labels you apply to specific phrases.  
- **Excludes (route to)** = where to send borderline quotes so headings aren’t mixed.  
- **Primary items** = the survey questions that directly feed this domain.  
- **Exemplar** = short, tagged quote with Participant ID and source question in the format **[PID, Q#]**.

> In the thesis body, use at most **one quote per participant per domain**. Report **prevalence as distinct participants** (not number of quotes).

---

## Global Mapping (put a compact version in Methods/Results)

### RQ ↔ Items
| RQ | Items used |
|---|---|
| **RQ1 (Challenges)** | Q7_explain, Q8_choice, Q9_followup, Q10_effects, Q11_describe, Q12_challenges |
| **RQ2 (Proposed changes)** | Q13_improvements (triangulated with patterns observed in Q7–Q11) |

### Domain ↔ Items
**Legend:** X = direct evidence, (ctx) = contextual/supporting  
| Domain | Q7 | Q8 | Q9 | Q10 | Q11 | Q12 | Q13 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Compensation & Economic Security | **X** | **X** |  |  |  | **X** | (ctx) |
| Task Design & Time Pressure |  |  | **X** |  | (ctx) | **X** | (ctx) |
| Transparency & QA |  |  |  |  | **X** | **X** | (ctx) |
| Content Exposure & Emotional Load |  |  |  | **X** |  | **X** | (ctx) |
| Platform Reliability & Access |  | (ctx) | (ctx) | (ctx) | (ctx) | **X** | (ctx) |
| Support & Dispute Resolution |  |  | (ctx) | (ctx) | (ctx) | **X** | (ctx) |

---

## 1) Compensation & Economic Security

| Field | Content |
|---|---|
| **Definition** | Perceived adequacy/stability of pay, including unpaid overhead and effort–pay mismatch. |
| **Subthemes (inductive)** | Effort–pay mismatch; Pay volatility & unpaid overhead; Unclear bonuses/rates. |
| **Codes (examples)** | `low_effective_hourly`, `unpaid_overhead`, `volatile_income`, `unclear_bonus_rule`, `effort_not_reflected` |
| **Includes** | Hourly/effective pay, unpaid search/quals/admin time, unpredictable earnings. |
| **Excludes →** | If mainly timers/instructions/complexity → **Task Design & Time Pressure**. |
| **Primary items** | **Q7_explain**, **Q8_choice**, **Q12_challenges** (Q13 for fixes). |
| **Exemplar** | “Most tasks pay below minimum wage once you include searching and quals.” **[P01, Q7]** |

---

## 2) Task Design & Time Pressure

| Field | Content |
|---|---|
| **Definition** | Clarity/stability of instructions, examples, time limits; task–description complexity mismatch; rejections tied to unclear rules. |
| **Subthemes** | Vague/shifting instructions; Unrealistic timers; Complexity mismatch. |
| **Codes** | `guidelines_vague`, `rules_change_mid_task`, `missing_examples`, `timer_too_short`, `complexity_misdescribed` |
| **Includes** | Instruction quality, edge-case examples, timing/feasibility. |
| **Excludes →** | If mainly acceptance criteria/ratings/appeals → **Transparency & QA**; if mainly pay → **Compensation**. |
| **Primary items** | **Q9_followup**, **Q12_challenges** (Q11 context; Q13 fixes). |
| **Exemplar** | “Very long task but very short time to complete it.” **[P26, Q12]** |

---

## 3) Transparency & QA (Acceptance, Ratings, Downstream Use)

| Field | Content |
|---|---|
| **Definition** | Opacity in acceptance criteria, missing reason codes, unclear rating effects on task access, unknown downstream data use. |
| **Subthemes** | Opaque acceptance (no reasons); Opaque ratings/access; Unknown downstream use. |
| **Codes** | `no_reason_rejection`, `criteria_unclear`, `rules_post_hoc`, `ratings_gate_tasks`, `rating_algo_opaque`, `unknown_downstream_use` |
| **Includes** | Review/QA rules, reason codes, ratings systems, provenance and where labels go. |
| **Excludes →** | If mainly response speed/appeals availability → **Support & Dispute Resolution**. |
| **Primary items** | **Q11_describe**, **Q12_challenges** (Q13 fixes). |
| **Exemplar** | “Acceptance criteria aren’t explained, so it’s hard to know why you’re rejected.” **[P36, Q12]** |

---

## 4) Content Exposure & Emotional Load

| Field | Content |
|---|---|
| **Definition** | Exposure to disturbing content; fatigue/burnout/desensitization; lingering after‑effects. |
| **Subthemes** | Disturbing/graphic content; Fatigue & burnout; Desensitization/after‑effects. |
| **Codes** | `violent_content`, `hate_abuse`, `lingering_distress`, `numbness_over_time`, `repetitive_strain` |
| **Includes** | Emotional/cognitive impact from content or repetition. |
| **Excludes →** | If mainly policy fairness/mechanics → **Transparency & QA** (add a *Fairness* tag). |
| **Primary items** | **Q10_effects**, **Q12_challenges** (Q13 for exposure‑control fixes). |
| **Exemplar** | “Graphic images and hate speech are mentally draining; it lingers after the task.” **[P01, Q10]** |

---

## 5) Platform Reliability & Access

| Field | Content |
|---|---|
| **Definition** | Technical stability and access to tasks (timeouts/glitches, routing/availability, regional disparities, scheduling instability). |
| **Subthemes** | Timeouts/glitches; Task scarcity/volatility; Regional/routing disparities. |
| **Codes** | `timeouts_glitches`, `task_scarcity`, `unstable_access_good_tasks`, `region_disparity`, `schedule_instability` |
| **Includes** | Platform reliability; availability patterns. |
| **Excludes →** | If mainly clarifications/appeals responsiveness → **Support & Dispute Resolution**. |
| **Primary items** | **Q12_challenges** (context from Q2 platforms, Q6 hours; sometimes Q9–Q11), Q13 for fixes. |
| **Exemplar** | “Platform errors and timeouts waste hours.” **[P12, Q12]** |

---

## 6) Support & Dispute Resolution

| Field | Content |
|---|---|
| **Definition** | Access to clarifications, quality/learning feedback, human support, and time‑bounded appeals. |
| **Subthemes** | Slow/no clarifications; No/weak feedback; Invisible/slow appeals. |
| **Codes** | `no_clar_channel`, `slow_response`, `no_feedback`, `no_appeal_path`, `appeal_stalled` |
| **Includes** | Communication with requesters/moderators, feedback loops, appeal/QA interactions. |
| **Excludes →** | If mainly acceptance criteria/ratings rules → **Transparency & QA**. |
| **Primary items** | **Q12_challenges** (Q13 for fixes). |
| **Exemplar** | “Unlike a real job, no one tells you what you did wrong or how to improve.” **[P28, Q12]** |

---

## Cross‑cutting Tag: Fairness & Recognition *(not a domain)*

| Field | Content |
|---|---|
| **Use** | Apply as a **tag** alongside any domain when respondents talk about procedural fairness, respect/credit, or bias. |
| **Codes** | `unfair_rejection`, `procedural_bias`, `lack_recognition`. |
| **Routing** | If a quote is **primarily** about transparency mechanics (criteria/ratings), keep **Transparency & QA** as the domain and add the *Fairness* tag. |

---

## Proposed Changes (RQ2) — Source & Reporting

- **Primary item for suggestions:** **Q13_improvements**.  
- For each domain, summarize Q13 answers into 2–4 bullets that directly match the pain points, e.g.:  
  - **Compensation:** time‑calibrated pay; pay for substantial quals/training; clear bonus rules.  
  - **Task Design:** versioned guidelines with examples and edge cases; realistic timers matched to observed completion time.  
  - **Transparency & QA:** reason‑coded rejections; published acceptance criteria; visible rating rules; time‑bounded appeals.  
  - **Content Exposure:** severity tagging, penalty‑free opt‑out, rotation/caps, links to support.  
  - **Reliability & Access:** reduce timeouts/glitches; transparent task routing/availability across regions.  
  - **Support:** guaranteed response SLAs for clarifications; exemplar‑based feedback.

---

## Methods snippet to paste in “Data Analysis”

> **Analytic approach.** We used a **hybrid thematic analysis**: a **deductive** frame from our instrument and prior work (Domains: Compensation & Economic Security; Task Design & Time Pressure; Transparency & QA; Content Exposure & Emotional Load; Platform Reliability & Access; Support & Dispute Resolution) and **inductive** open coding of free‑text to derive **codes** and then **subthemes** within each domain. Following Braun & Clarke, we (i) familiarized ourselves with the data, (ii) generated initial codes inductively, (iii) collated codes into candidate subthemes per domain, (iv) reviewed and refined subthemes for coherence and distinction, and (v) defined final subthemes with representative quotes. We conducted an initial calibration on ≈20% of responses, reconciled discrepancies, and then completed coding. We report domain/subtheme prevalence as **distinct participants**, include contrasting cases, and tag quotes with participant and item (e.g., **[P16, Q9]**). One quote per participant per domain was included to avoid overweighting.

---

## Prevalence & Quote Policy (for Results)

- **Prevalence** = number of **distinct participants** contributing to a domain/subtheme (not the number of quotes).  
- **Quotes** = max **2–3 per domain** in the paper, each from a **different participant**; add **one negative/contrast case** to avoid cherry‑picking.  
- **Tagging** = always tag quotes like **[Pxx, Q#]** to preserve the evidence trail.

---

*End of codebook.*
