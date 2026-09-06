# CP4285 Week 03 delivery timeline and deck critique

> **Purpose.** This file is the delivery companion to `w03.qmd`. It records the actual teaching sequence, identifies timing and instructional risks, and supplies a 90-minute cut plan. It does **not** modify the slide deck.

## Changelog

- **5 Sep 2026** — Corrected the split-design timer to 45 seconds and standardised week labels and deadline date-time formatting.
- **25 Aug 2026** — Added the Week 02 Canvas Voices review and Week 04 pre-lecture bridge.

## Executive delivery status

The current source supports a **94 minute 15 second instructional run** when the explicit speaker-note durations, stated activity/report times, and a conservative allowance for the two untimed closing slides are added. This total includes the five-minute break but **excludes slide transitions, polling delay, movement into groups, technology setup, and extended student discussion**. It therefore cannot reliably fit a 90-minute meeting without cuts.

| Delivery target | Planned teaching time | Buffer | Status |
| --- | ---: | ---: | --- |
| Full source sequence | 94:15 | 0:00 | Not suitable for a 90-minute class; fragile even for a 95-minute slot. |
| 90-minute delivery using the cut plan below | 89:15 | 0:45 | Feasible only with firm activity facilitation. |
| Preferred operational target | 85:00–87:00 | 3:00–5:00 | Requires a further instructor decision on one substantive compression. |

## Full source run-of-show

The times below are calculated from the current source rather than inherited from an earlier version of this file. Times are cumulative and deliberately preserve the uneven durations stated in the notes.

| Start–end | Duration | Slide block | Mode | Instructor outcome |
| --- | ---: | --- | --- | --- |
| 0:00–4:15 | 4:15 | Changelog, Week 02 visual recap, yesterday’s deadlines | Orientation | Reconnect score/ranked-list material to the question, “What evidence shows that the resulting list is good?” Confirm deadlines without reopening submission discussion. |
| 4:15–6:15 | 2:00 | Essay `e1` peer review | Logistics | State the assigned-review process, the card-lens-only scope, marking, deadline, and independent-work expectation. |
| 6:15–14:15 | 8:00 | Week 02 pre-lecture exercise and Canvas Voices | Guided discussion | Distinguish an offline-log guardrail from a stress test or intervention. Discuss ideas, not named students’ quality. |
| 14:15–17:45 | 3:30 | Evaluation claim, key point, missing-interaction MCQ and debrief | Framing + response | Establish that an unclicked item is observationally ambiguous and that evaluation begins with a defensible claim. |
| 17:45–23:45 | 6:00 | Evaluation contract; split-design MCQ; train, validate, test | Explanation + response | Make scenario, candidate set, relevance, top-*K* decision, temporal realism, and leakage explicit. |
| 23:45–40:45 | 17:00 | Metric Lens Table, offline metrics, shelf-choice discussion, MAP, NDCG, CTR, metric key point | Pair + group + worked examples | Match a ranking priority to a metric; preserve the binary-MAP versus graded-NDCG distinction; locate CTR as online evidence. |
| 40:45–45:45 | 5:00 | CTR break | Break | Start the timer. On return, restate the like-for-like CTR comparison rule. |
| 45:45–1:17:45 | 32:00 | Accuracy proxy; catalogue comparison; card-lens clinic and debrief; criteria map; engagement/exposure/discovery; ILD; safety/resilience/scalability; p95 latency | Explanation + group work + two worked examples | Show that relevance is necessary but insufficient. Have each group propose a primary measure, two guardrails, and an offline evidence gap. |
| 1:17:45–1:27:15 | 9:30 | Feedback loop hidden in a log; four offline failure modes | Explanation | Connect exposure, selection bias, temporal drift, leakage, and cold-start/long-tail slices to bounded offline claims. |
| 1:27:15–1:29:45 | 2:30 | Offline → online → user impact | Synthesis | Position the offline benchmark as a comparison step before guarded online evidence and longer-term impact interpretation. |
| 1:29:45–1:31:45 | 2:00 | Summary | Close | Restate the four-part evaluation plan: claim, ranked-list metric, guardrails, and proportional claims. |
| 1:31:45–1:34:15 | 2:30 | Week 04 pre-lecture activity and neural-recommendation preview | Bridge | Set the Canvas task and connect missing interactions to the limits of richer scoring models. |

## Instructional critique

The deck has a coherent and unusually strong central proposition: **a metric is not an evaluation plan**. It makes the progression from protocol, to ranked-list metric, to guardrail, to evidence limitation visible several times, and the music-shelf example provides useful continuity across MAP and NDCG. The Canvas Voices material also gives the card lenses an authentic role rather than presenting them only as an abstract framework.

The principal problem is **density rather than direction**. The full deck introduces the evaluation contract, temporal splitting, four ranking metrics, CTR, coverage, discovery, ILD, trust, robustness, p95 latency, feedback loops, four offline failure modes, online testing, and a pre-lecture bridge. This is closer to two lectures’ worth of conceptual inventory than one 90-minute session once learner processing time is included. The `Beyond Accuracy` sequence alone takes 32 minutes and contains nine distinct conceptual moves.

| Priority | Finding in the current source | Why it matters in delivery | Action recorded in this timeline |
| --- | --- | --- | --- |
| **P0** | The former timeline described sections and activities that are no longer present, including a separate card-lens section, a conversion-only voice interaction, and an exit ticket. | A facilitator using that plan would search for non-existent slides and misallocate class time. | This file supersedes the prior timing and activity checklist. |
| **P1** | The source adds to **94:15** before normal delivery friction. | There is no protection for a productive student question, a slow room poll, or regrouping. | Use the 90-minute cut plan at minimum; do not simply speak faster through worked examples. |
| **P1** | `Beyond Accuracy` combines catalogue coverage, card-lens design, exposure, discovery, ILD, trust, resilience, scalability, and p95 latency. | Students may retain a vocabulary list rather than the decision logic: primary outcome, guardrails, and evidence gap. | Preserve the metric-design clinic; compress supporting inventories before compressing the clinic. |
| **P1** | The stated learning outcome is to compute ranking metrics, but MAP and NDCG are instructor-led worked examples. The pair activity asks for use cases rather than an individual calculation. | Demonstration does not provide direct evidence that each student can compute or interpret a metric. | Either add a one-minute independent check in a later deck/lab, or revise the assessment claim to “interpret ranking metrics.” |
| **P1** | The deck deliberately returns to card lenses after metric mechanics. | This is pedagogically valuable, but the return needs an explicit verbal bridge so learners do not experience it as a topic shift. | On entering the clinic, say: “The metric table named what each score rewards; the card lens now asks what else must not be sacrificed.” |
| **P2** | The break contains advertising CTR benchmarks alongside a recommender-systems lesson. | The slide correctly warns against direct comparison, but the figures can still distract from the key denominator/surface lesson. | Treat the numbers as contrastive examples only; spend the return transition on the comparability rule, not on benchmark discussion. |
| **P2** | The p95 example is correct under its stated nearest-rank convention but introduces a new operational metric late in a concept-heavy segment. | It can become an isolated arithmetic exercise unless connected to an actual recommendation surface. | Keep it only if the instructor can name a surface-specific latency consequence; otherwise use it as a fast optional example. |

## 90-minute cut plan

This plan retains the lecture’s core reasoning chain and saves **five minutes**, producing a 89:15 planned run and a 45-second operational buffer. It deliberately protects the temporal-split lesson, the MAP/NDCG contrast, the metric-design clinic, and the offline-evidence limitation.

| Source block | Full allocation | 90-minute allocation | Saving | Delivery instruction |
| --- | ---: | ---: | ---: | --- |
| Canvas Voices | 3:00 | 2:00 | 1:00 | Use one quotation as the main discussion object and name the second as a contrasting example. |
| Same precision, different catalogue | 3:00 | 2:00 | 1:00 | Ask for a show of hands, then state coverage versus within-list diversity directly. |
| Metric design clinic debrief | 5:00 | 4:00 | 1:00 | Hear from two groups only; use the debrief table to acknowledge the other lenses. |
| Evaluation criteria map | 4:00 | 3:00 | 1:00 | Treat it as a consolidation visual, not a second full explanation of every measure. |
| Week 04 bridge | 2:30 | 1:30 | 1:00 | State the Canvas task, read its single prompt, and use one sentence to connect it to neural models. |
| **Total** | **17:30** | **12:30** | **5:00** | **Result: 89:15 planned time.** |

If an additional three to five minutes are required in the room, shorten or omit the standalone p95 worked calculation first. The deck has already established the operational point with the `Safe and dependable` slide; removing that calculation does not break the central evaluation argument.

## Activity and timer checklist

| Activity | Intended learning check | Planned time | Source timer ID | Delivery check |
| --- | --- | ---: | --- | --- |
| Missing-interaction TempoQuiz | Identify that no click does not establish preference. | 0:30 response plus debrief | `w03-tempo` | Controller and display both specify 30 seconds. |
| Split-design MCQ | Select a forward-looking split with separate validation and test periods. | 0:45 response, included in the 3:30 block | `w03-split` | Controller, visible display, and notes specify 45 seconds. |
| Metric Lens Table | Connect Precision, Recall, MAP, and NDCG to a use case. | 2:00 | None | Collect one justification; do not attempt to hear every pair. |
| Which recommender wins? | State a surface assumption, metric, and reason the alternative may still be preferred. | 3:00 discussion + 1:00 report | `w03-ranking` | The 180-second timer matches the notes. |
| Metric design clinic | Propose one primary measure, two guardrails, and one evidence gap. | 3:00 discussion + 2:00 reports | `w03-lens` | The 180-second timer matches the notes. Limit oral reporting using the cut plan. |
| CTR break | Distinguish a surface-specific online denominator from a recommender-quality verdict. | 5:00 | `w03-ctr-break` | The 300-second timer matches the notes. Restate the rule after the break. |

## Learning-outcome and assessment critique

| Intended outcome | Evidence currently in the deck | Assessment strength | Recommended interpretation |
| --- | --- | --- | --- |
| Design an evaluation protocol | Evaluation contract, temporal-split MCQ, train/validate/test slide, metric-design clinic. | **Strong** | Students repeatedly connect a claim to a split, candidate set, relevance definition, and top-*K* decision. |
| Compute ranking metrics | Instructor-led MAP and NDCG examples; no individual numerical computation. | **Partial** | Claim that students can *read and interpret* the calculations. Add an independent micro-check if computation must be assessed. |
| Critique metric selection | Shelf-choice discussion, CTR warning, catalogue example, card-lens clinic. | **Strong** | Students must name a priority and acknowledge trade-offs or guardrails. |
| Explain limits of offline evaluation | Missing-interaction MCQ, feedback-loop diagram, failure-mode repairs, offline-to-online flow. | **Strong** | The deck correctly limits rather than dismisses offline evidence. |
| Reason about operational constraints | Scalability/p95 segment. | **Introductory** | Treat this as an applied extension, not a core assessed outcome unless a later activity uses it. |

## Instructor cues for conceptual continuity

The following transitions are the highest-value spoken links. They should be delivered even if content needs to be compressed.

| Transition | Suggested instructor cue |
| --- | --- |
| Week 02 → evaluation | “Last week we learned ways to score candidates. Today we ask what evidence makes a ranking decision defensible.” |
| Protocol → metric | “Only after we know the surface, candidates, relevant outcome, and rank depth can a metric answer the right question.” |
| MAP → NDCG | “MAP treats the chosen relevance threshold as binary; NDCG preserves differences in graded value and discounts late ranks.” |
| CTR → beyond accuracy | “CTR records action after an exposure. It does not, by itself, establish benefit, discovery, fairness, safety, or long-term value.” |
| Metric mechanics → card-lens clinic | “The metric table named what each score rewards; the card lens now asks what else must not be sacrificed.” |
| Offline failures → product decision | “An offline benchmark is a disciplined comparison, not a deployment verdict. The next evidence comes from guarded exposure and outcomes.” |
| W03 → W04 | “A richer model can change the scoring function, but it cannot recover the exposure or interface information the log never recorded.” |

## Pre-delivery checklist

| Check | Required state |
| --- | --- |
| Timing | Select the full-source run only for a session longer than 95 minutes; otherwise commit to the cut plan before class. |
| Split MCQ timer | Controller, visible text, screen-reader status, and notes all specify 45 seconds. |
| Activity reports | Decide in advance which two groups will report from the metric-design clinic. |
| Worked examples | State the binary relevance threshold before MAP and the graded gain before NDCG. |
| CTR | Repeat that CTR comparisons require matching surface, placement, audience, and impression definition. |
| Canvas Voices | Discuss proposals without evaluating named contributors publicly. |
| Closing | Leave enough time to state the Week 04 Canvas task; this is the retrieval bridge for the missing-interaction lesson. |

## Source basis

This review is based on `static/slides/w03/w03.qmd`, rechecked on 5 Sep 2026. The timeline calculations intentionally include the source-note durations and stated group-report allowances. They exclude ordinary slide movement and unscripted interaction, so they should be interpreted as a lower bound rather than a guaranteed wall-clock duration.
