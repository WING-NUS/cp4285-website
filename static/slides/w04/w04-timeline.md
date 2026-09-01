# Week 04 Delivery Timeline - Neural Recommendation Models

This timeline is synchronized with `w04.qmd`. It is a 90-minute lecture plan, inclusive of the five-minute TriRank break, activities, and the Week 05 pre-lecture exercise.

## Run of show

| Start-end | Duration | Slide block | Mode | Instructor outcome |
| --- | ---: | --- | --- | --- |
| 0:00-3:00 | 3:00 | Week 03 visual recap | Retrieval | Reconnect evaluation protocol, ranking metrics, and feedback loops to today's modelling choices. |
| 3:00-8:00 | 5:00 | Week 04 pre-lecture exercise and synthesis | Canvas Voices | Establish that a missing click does not identify preference, exposure, placement, timing, or availability. |
| 8:00-10:00 | 2:00 | Lecture framing and learning outcomes | Framing | State that a neural model changes the interaction function, not the evidence recorded in the log. |
| 10:00-30:00 | 20:00 | Transformer bridge; MF; GMF, MLP, NeuMF; code lens | Worked explanation | Work through the colourised Transformer bridge, MF score, and shared GMF/MLP/NeuMF example. |
| 30:00-49:00 | 19:00 | Implicit feedback, pointwise-versus-pairwise losses, objectives, BPR, pre-break activities | Worked explanation + activity | Contrast a per-pair prediction loss with BPR’s relative-ranking loss; then work the BPR calculation. Students discuss defensible sampled negatives and complete the BPR Bandit Time MCQ. |
| 49:00-54:00 | 5:00 | TriRank research interlude | Break | Run the shared timer. Ask whether aspect-based reasons are transparency, persuasion, or both. |
| 54:00-74:00 | 20:00 | BPR-MF/NeuMF practical comparison, post-break activities | Practical comparison + activity | Hold split, sampler, metrics, and compute budget fixed. Students make and defend a deployment decision, then complete the post-break MCQ. |
| 74:00-88:00 | 14:00 | Capacity, AI Voice critique, four card-suit ethics lenses, summary | Critique + synthesis | Evaluate whether an observed gain justifies complexity; test the claim through robustness, social influence, discovery, and constraint lenses; distinguish a model score from a user-facing explanation. |
| 88:00-90:00 | 2:00 | Week 05 pre-lecture exercise and preview | Bridge | Set the session-boundary memo and connect static scores to ordered history, recency, and session context. |

## Activity contracts

| Activity | Timing | Expected output | Instructor synthesis |
| --- | ---: | --- | --- |
| **Which negative is defensible?** | 3:00 | One better-supported sampled negative and one residual uncertainty. | Start the `w04-negative` three-minute timer after groups form. Exposure and availability make comparisons more meaningful; they do not make an unclicked item ground-truth dislike. |
| **Bandit Time: What does BPR optimise?** | 2:00 | **A** - widen Aisha’s positive-minus-sampled-item score margin. | BPR optimises score differences. Equal score increases leave the margin unchanged; a standalone click target is pointwise; and missing feedback is not a blanket dislike label. |
| **Deployment decision clinic** | 5:00 | Deploy NeuMF, retain BPR-MF, or collect evidence; cite quality, operations, and an evidence concern. | A small offline gain is not automatically a production decision. |
| **Bandit Time: Which evidence supports NeuMF?** | 3:00 | **D** - a stable meaningful gain under the same split, sampler, and seeds that fits latency budget and documents limits. | Capacity is a claim to test: hold the protocol fixed, check operational feasibility, and report limits honestly. |
| **AI Voice Mode: challenge the deployment explanation** | 3:00 | Two hidden assumptions and one requested check. | Critique the agent's framing; it is not an authority or a production recommender. |

## Worked-example checklist

| Algorithm / mechanism | Worked mathematical example |
| --- | --- |
| Transformer bridge | A colourised query-key compatibility calculation. |
| Matrix factorisation | A colourised dot-product score using the running user/item vectors. |
| GMF, MLP, and NeuMF | One shared numerical input worked through three interaction functions. |
| BPR | Aisha's clicked item versus a sampled unobserved item: margin, sigmoid, loss, and update direction. |

## Delivery checks

- Verify the `soc-n.us` title QR assets resolve in the rendered deck.
- Test every `w04-` timer—especially the new `w04-negative` activity timer and the `w04-break` timer—for start, pause, resume, expiry, and pause on slide exit.
- Do not fabricate Canvas quotations. Use actual anonymised pre-lecture responses if they are available; otherwise facilitate the synthesis prompts on the slides.
- Keep the RecBole comparison illustrative unless a controlled local run and its configuration are available.
- State the timebox before each activity and limit group reports to preserve the 90-minute plan. The 30:00–49:00 block allocates 3:00 to the new loss contrast, 2:00 to the training-question summary, 5:00 to the BPR worked example, 3:00 to negative-sampling discussion, and 2:00 to the BPR MCQ.
- In the final four-slide lens sequence, retain the one-minute pace per lens. The suits are situational treatment lenses—not fixed user categories—and each asks for an additional deployment check rather than selecting a universally better model.
