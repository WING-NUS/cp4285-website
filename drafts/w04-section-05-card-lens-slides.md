# Draft: W04 Section 05 — Card-Suit Lenses for BPR and NeuMF

**Purpose.** These four content drafts extend W04 §05, *Capacity Has Costs*, without changing the existing model-comparison claim. Each card suit is a **situational treatment lens**, not a user category. The recurring question is therefore not “Which model wins?” but “What additional evidence, safeguard, or product policy is needed before a BPR or NeuMF score can support this decision?”

The proposed sequence belongs **after “When is neural complexity justified?” and before “Ethics debrief: a score is not an explanation.”** It follows the existing deployment clinic: BPR-MF has lower cost; NeuMF has a small higher NDCG@10 under a stated evaluation protocol. The slides make clear that neither the architecture nor BPR’s pairwise loss settles the four ethical concerns.

| Slide | W01 treatment lens | W04 connection | Core conclusion |
|---|---|---|---|
| 1 | ♣ Clubs | Implicit feedback and negative sampling | Neither BPR nor NeuMF is robust by default. |
| 2 | ♥ Hearts | Exposure bias and the difference between score and explanation | A click after social exposure is not proof of independent preference. |
| 3 | ♦ Diamonds | Evaluation contract and aggregate NDCG | A quality gain can coexist with reduced discovery and long-tail opportunity. |
| 4 | ♠ Spades | Accountable user-facing claims | Constraints must be enforced in the decision policy, not inferred from a score. |

---

## Slide 1 — ♣ Clubs: BPR and NeuMF can both learn an attack

**On-slide title:** ♣ Clubs — A pairwise win is not a robustness guarantee

**On-slide layout:** Use a three-column comparison grid. The first two columns give equal visual weight to **BPR-MF** and **NeuMF**; the third, orange-accented column states the deployment check. End with a warning callout.

| BPR-MF: what the loss sees | NeuMF: what added capacity changes | Before a deployment claim |
|---|---|---|
| BPR trains an observed interaction to score above a sampled unobserved item. Coordinated fake positives can therefore create many favourable pairwise comparisons for a target item. | NeuMF can fit richer interaction patterns, including an attack pattern if it is present in the logged evidence. More parameters are **not** an abuse defence. | Stress-test both models with plausible shill or coordinated-interaction scenarios. Report how rankings, affected users, and the target item’s exposure change. |

> **Safeguard:** Compare sensitivity to suspicious accounts, repeated events, and concentrated interaction bursts before treating an offline gain as deployable.

**Bottom-line statement:** **Neither model is robust merely because it ranks held-out interactions well.**

**Speaker notes.** Link this directly to the W01 Clubs lens: coordinated ratings or actions can force a target item into a list. BPR is not “the vulnerable one” and NeuMF is not “the unsafe one.” Both learn from the same interaction record; their different loss and capacity only change how they use it. Ask students what would count as meaningful robustness evidence: an attack-injection test, sensitivity analysis after excluding suspicious accounts, and a concentration check on who benefits from the target item. The key correction is that a stable NDCG result establishes only the declared ranking protocol, not resilience to strategic data creation.

---

## Slide 2 — ♥ Hearts: Neither score identifies free preference

**On-slide title:** ♥ Hearts — Is the model learning interest, influence, or exposure?

**On-slide layout:** Present a shared trace across the top: **social cue or peer activity → item is shown prominently → click is logged**. Beneath it, place two model cards and one shared evidence card.

| BPR-MF: pairwise interpretation | NeuMF: richer pattern interpretation | Evidence and user protection |
|---|---|---|
| The clicked item is pushed above a sampled unobserved item. The loss does not reveal whether the click followed independent interest, a friend’s cue, or ranking-induced visibility. | NeuMF may learn more complex co-occurrences among users, items, and contexts. That flexibility cannot turn observational social traces into causal evidence of preference. | Log exposure and social context where appropriate; evaluate social and non-social contexts separately; give users meaningful controls over social cues and sharing. |

> **Question for the claim:** “What in the data lets us say this reflects the user’s preference rather than the system’s or peers’ influence?”

**Bottom-line statement:** **A high score may be a prediction of behaviour after influence, not an explanation of what the person independently wants.**

**Speaker notes.** This applies the W01 Hearts lens: social evidence can inform, but it can also create unwanted exposure or conformity pressure. Tie it to W04’s opening exercise on missing interactions. The same non-click can reflect no exposure or poor placement; similarly, a click can reflect the presentation and social framing rather than a stable preference. Do not claim that BPR removes social influence because it is simpler, or that NeuMF can identify it because it is more expressive. The appropriate response is better measurement, carefully scoped evaluation, and user controls—not an architectural inference.

---

## Slide 3 — ♦ Diamonds: An NDCG gain may still narrow discovery

**On-slide title:** ♦ Diamonds — Better ranking can still mean less discovery

**On-slide layout:** Use a left-to-right pipeline: **sparse long-tail evidence → BPR or NeuMF ranking → top-\(K\) exposure**. Place BPR and NeuMF cards below the shared pipeline, with a third card for reporting.

| BPR-MF: implications for the tail | NeuMF: implications for the tail | Report alongside NDCG@\(K\) |
|---|---|---|
| Tail items have few observed positives. With implicit data, sampled unobserved items can be treated as training alternatives despite weak evidence about whether they were ever seen. | NeuMF may use richer signals where they exist, but it has no inherent novelty, diversity, or coverage objective. A small aggregate gain can still concentrate exposure on familiar items. | Catalogue coverage, long-tail share in top-\(K\), new-item exposure, and quality by relevant item or user segments. State the candidate policy and sampler. |

> **Decision rule:** Do not infer discovery from aggregate NDCG. Evaluate it explicitly, then decide whether a coverage or exploration policy is needed.

**Bottom-line statement:** **BPR and NeuMF optimise the ranking objective supplied to them; neither automatically protects long-tail opportunity.**

**Speaker notes.** Return to the W01 Diamonds lens and its question: does the list include genuinely new, long-tail, or emerging options? W01 established that the long tail is under-observed, not empty. W04 adds the mechanism: negative sampling creates a modelling decision about unobserved feedback, while metric choice defines the quality claim being made. Avoid saying that either model necessarily reduces diversity; that requires measurement. The defensible claim is narrower: standard BPR training and NeuMF capacity do not themselves introduce a discovery guarantee, so a model-selection result must report the outcomes relevant to that product goal.

---

## Slide 4 — ♠ Spades: Requirements need policy, not a persuasive score

**On-slide title:** ♠ Spades — A constraint is not something a model should merely “learn”

**On-slide layout:** Build a three-stage horizontal flow: **stated requirement → eligibility / constraint policy → BPR-MF or NeuMF ranking → faithful explanation**. Under the ranking stage, contrast the two models with concise cards.

| BPR-MF | NeuMF | Product-policy requirement |
|---|---|---|
| BPR learns an ordering from observed-versus-sampled interactions. It does not guarantee that an important attribute or rule is satisfied. | NeuMF can produce a more flexible score, but a more complex interaction function does not make the score a truthful explanation or a hard constraint. | Apply non-negotiable filters and constraints before ranking; distinguish them from soft preferences; explain the actual eligibility, ranking policy, and limits of the recommendation. |

> **Accountable claim:** “Among items that satisfy the stated requirements, this item ranked highly under our declared data, objective, and ranking policy.”

**Bottom-line statement:** **Use the model to rank eligible options; do not use a model score as evidence that an unstated or critical requirement has been met.**

**Speaker notes.** Close with the W01 Spades lens: a user should be able to hold an important attribute fixed and understand why an item appears. This is the most direct bridge to W04’s “a score is not an explanation” debrief. Neither BPR’s relative ordering nor NeuMF’s nonlinear score can, by itself, promise a correct explanation or a satisfied requirement. The system should encode hard conditions in candidate eligibility or constrained ranking, keep soft trade-offs visible, and use language that describes the actual decision process. This turns “explainability” from a persuasive afterthought into an accountable product behaviour.

## Facilitation bridge into the existing W04 ethics debrief

After the fourth slide, return to the existing two-column contrast between the overclaim and the accountable claim. The instructor can ask students to complete the accountable version with one safeguard from each suit: a **robustness check** for Clubs, an **exposure or social-context check** for Hearts, a **coverage report** for Diamonds, and a **constraint policy** for Spades. The synthesis is that model selection requires more than a quality and cost comparison: it also requires evidence that the decision policy protects the outcomes the service claims to value.

## Source grounding

This draft is grounded entirely in the existing course material. W01 defines the four suits as situational treatment lenses and associates them with robustness, social influence, discovery/long-tail exposure, and constraints/explanation. W04 establishes that implicit feedback is ambiguous; negative sampling is an assumption about missing feedback; model comparisons need a fixed evaluation contract; neural capacity does not make the evidence causal or value-neutral; and a score is not an explanation.

## References

[1]: file:///mnt/fe30a975-6196-4f77-a9f6-f881f516d608/cp4285-website/static/slides/w01/w01.qmd "CP4285 Week 01: Recommendation Problems and Classical Methods"

[2]: file:///mnt/fe30a975-6196-4f77-a9f6-f881f516d608/cp4285-website/static/slides/w04/w04.qmd "CP4285 Week 04: Neural Recommendation Models"
