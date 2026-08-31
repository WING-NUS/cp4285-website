# Week 04 Delivery Timeline — Neural Recommendation Models

> **Purpose.** This companion file records the delivery sequence for `w04.qmd`, the activity contracts, and the instructor cues that maintain continuity with Week 03. It does **not** modify the slide deck.

## Delivery status

The current source supports a **54-minute instructional run**, calculated from the durations stated in the W04 speaker notes. The total excludes ordinary slide transitions, polling delay, moving into groups, technical setup, and extended class discussion. It is therefore a concise lecture sequence with capacity for an instructor-led worked example, questions, or a longer discussion where the timetable permits.

| Delivery target | Planned teaching time | Buffer in a 60-minute slot | Status |
| --- | ---: | ---: | --- |
| Full source sequence | 54:00 | 6:00 | Feasible, provided group activities are tightly facilitated. |
| Compressed delivery | 46:30 | 13:30 | Skip the explanation discussion report and condense the Week 03 recap to one minute. |

## Full source run-of-show

| Start–end | Duration | Slide block | Mode | Instructor outcome |
| --- | ---: | --- | --- | --- |
| 0:00–8:15 | 8:15 | Week 03 visual recap, missing-interaction exercise, framing, learning outcomes | Retrieval + framing | Reconnect neural capacity to the Week 03 evidence contract: richer scoring cannot recover exposure or interface information absent from the log. |
| 8:15–22:45 | 14:30 | Key point, latent-factor baseline, neural collaborative filtering, GMF/MLP/NeuMF, interaction MCQ and debrief | Explanation + response | Distinguish embeddings, a fixed dot-product interaction, and a learned non-linear interaction function. Confirm that greater capacity is not greater observability. |
| 22:45–36:00 | 13:15 | Implicit feedback, training objective, streaming-service discussion, model-score-to-exposure flow | Explanation + group work | Make the task definition, target event, and treatment of unobserved pairs explicit; separate the score from ranking policy and served exposure. |
| 36:00–49:15 | 13:15 | Prediction/explanation distinction, ethics thread, explanation discussion, documentation table | Ethical critique + group work | Treat user-facing explanations as product claims that should be intelligible, appropriately limited, faithful where possible, and evaluated for consequences. |
| 49:15–54:00 | 4:45 | Summary, Week 05 pre-lecture exercise, Week 05 preview | Synthesis + bridge | Consolidate the evidence/model/product/explanation distinction and prepare students for sequence and session-based recommendation. |

## Activity and timer checklist

| Activity | Intended learning check | Planned time | Source timer ID | Delivery check |
| --- | --- | ---: | --- | --- |
| **What changed in the neural model?** | Identify that an MLP changes the interaction function, not the evidence available in logs. | 0:30 response + 0:45 poll | `w04-interaction` | Visible display, screen-reader status, and controller all specify 30 seconds. Confirm answer **B**. |
| **What should the model be allowed to learn?** | State one prediction pattern and one unresolvable ambiguity in implicit feedback. | 2:00 discussion + 1:00 report | `w04-feedback` | Start the shared timer; hear from one or two groups only. |
| **Evaluate this explanation** | Revise a user-facing explanation and identify an evidence or design check. | 3:00 discussion + 1:00 report | None | Require one revised sentence and one check; avoid treating sponsored-placement disclosure as the only acceptable response. |

## Instructor cues for conceptual continuity

| Transition | Suggested instructor cue |
| --- | --- |
| Week 03 → W04 | “A richer model can change the scoring function, but it cannot recover the exposure or interface information the log never recorded.” |
| Matrix factorisation → NCF | “The representations may look familiar; the modelling change is the rule that combines them.” |
| Interaction function → training target | “A flexible model still needs an objective. The dataset and target tell it which scores to move.” |
| Implicit log → product decision | “The model produces a score; ranking policy and the interface decide what is actually shown.” |
| Prediction → explanation | “A score estimates a pair under the stated model. An explanation is a separate claim made to a person.” |
| W04 → W05 | “A static score pairs a user and item. Next week, sequence and session models ask how the order of events changes the next useful action.” |

## Pre-delivery checklist

| Check | Required state |
| --- | --- |
| Title slide | The Week 04 `soc-n.us` QR link and both QR asset paths resolve. |
| Shared theme | `w04.qmd` loads `../cp4285-common.scss` and `w04-custom.scss`; the overlay contains no duplicated course-wide rules. |
| Timer controller | `include-after-body: ../cp-timer.html` is present; `w04-interaction` and `w04-feedback` start, pause, resume, expire, and pause on slide exit. |
| Activity timing | State the timebox before each activity and limit group reports to preserve the 54-minute run. |
| Evidence language | Do not equate a non-click with dislike or treat a model score as direct proof of a user’s preference. |
| Explanation discussion | Distinguish a faithful and useful explanation from a persuasive but incomplete post-hoc story. |
| Closing | Leave enough time to set the Week 05 Canvas prompt and the bridge to sequential and session-based recommendation. |

## Source basis

This timeline is based on `static/slides/w04/w04.qmd`, audited on 31 Aug 2026. The timing calculation uses all stated speaker-note durations and group-report allowances. It should be treated as a lower bound because normal classroom logistics and unscripted discussion are excluded.
