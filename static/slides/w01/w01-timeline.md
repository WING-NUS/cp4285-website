# CP4285 Week 1 Lecture Timeline

##### Changelog

- **10 Aug 2026** — Added the Mon, 23:59 SGT default-deadline policy and exact assessment deadlines.
- **10 Aug 2026** — Updated project-team formation: Min may adjust teams to support diversity.
- **10 Aug 2026** — Synced the delivery plan to the authoritative Week 01 slide order and activity treatment.

**Lecture:** Recommendation Problems and Classical Methods  
**Scheduled class time:** 120 minutes (Tuesday, 10:00–12:00 SGT)

**Current run-of-show:** 124 minutes
**Deck:** [`w01.qmd`](./w01.qmd)

**Scoped revision:** Section 04 is now a 51-minute sequence that introduces matrix notation, rating types, decision goals, signals, classical starting points, and situational treatment lenses. It includes a two-minute signal-hunt activity, a table-completion discussion and debrief, a 30-second MCQ, and a five-minute small-group reprise with an AI Voice ethical critique.

This is a delivery run-of-show for the Week 1 slide deck. Times are target durations, including brief transitions between slides. The delivery mode is the primary mode for that slide; the instructor should still handle clarification, pacing, and accessibility throughout.

## Delivery modes

| Mode | How to use it |
|---|---|
| **Instructor** | Explain the slide, connect it to the course framing, and check for quick questions before moving on. |
| **Discussion** | Put the stated prompt to the room, invite multiple perspectives, and synthesise the responses into the slide takeaway. |
| **Video** | Play the selected excerpt, pause for one observation, and connect it back to the slide’s learning objective. |
| **In-class activity** | Timebox the stated task, have students produce the requested response, and synthesise one or two examples. |
| **MCQ** | Have students answer individually, sample justifications, reveal the answer, and correct the central misconception. |
| **Voice-mode AI agent** | Invite students to speak to an AI agent as a short, structured activity. The instructor sets the context and timebox, then debriefs the agent interaction and corrects inaccuracies. Students should treat the agent as a conversation partner, not as an authoritative source. |

## Section overview

| Section | Slides | Time | Running total | Share of run-of-show |
|---|---:|---:|---:|---:|
| 01 Overview | 8 | 24 min | 24 min | 18.3% |
| 02 Schedule | 6 | 17 min | 41 min | 13.0% |
| 03 Assignments & Grading | 7 | 27 min | 68 min | 20.6% |
| Break | 1 | 5 min | 73 min | 3.8% |
| 04 Recommendation Problems and Decision Goals | 12 | 49 min | 122 min | 39.9% |
| 05 Neighborhood-Based Collaborative Filtering | 16 | 57 min | 179 min | 31.8% |
| **Total** | **50** | **179 min** | **179 min** | **100%** |

The run-of-show is **56 minutes over** the scheduled class time. The 120-minute limit is intentionally not being used as a constraint while this extended sequence is developed.

## Detailed run-of-show

### 01 Overview — 24 minutes (running total: 24 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `01 Overview` | 1 min | 1 min | Instructor | Welcome the class, state the learning goals, and frame the section around recommendation systems, course co-development, and recurring ethics. |
| `🎥 Video: Spotify Recommendations` | 3 min | 4 min | Video | Play the selected excerpt, then invite one observation about the user signals and objectives students heard. |
| `Recommendations Everywhere` | 2 min | 6 min | Instructor | Establish recommendations as a general pattern across video, music, shopping, news, jobs, social feeds, and course resources. Distinguish inputs from outputs and emphasise that ranking affects attention. |
| `CP Pilot Course` | 4 min | 10 min | Instructor | Explain that students help shape future course delivery through self-learning, lab/tutorial development, process documentation, and constructive feedback. Clarify that staff retain final review and course standards. |
| `🎰 Bandit Time: Objectives` | 2 min | 12 min | **Student activity — MCQ** | **Student activity:** start the default 20-second countdown for individual responses, sample justifications, and explain why the correct answer is that the systems may rank different items and expose different creators. |
| `📶 AI Voice Mode` | 1 min | 13 min | **AI Voice Mode** | **AI Voice Mode:** ask the agent for one everyday recommendation example and have it identify the signal, item, objective, and one consequence. Stop after one minute and correct oversimplifications. |
| `👥 Find the Recommender` | 10 min | 23 min | **Student activity — small-group discussion** | **Student activity:** in pairs, audit one recent recommendation, identify likely signals and objective, and name who or what might be left unseen. Take one or two observations and synthesise them. |
| `📶 Ethics Thread` | 1 min | 24 min | **AI Voice Mode** | **AI Voice Mode:** briefly ask the agent to name one stakeholder affected by a recommendation decision, then identify one assumption or omission in its response. |

### 02 Schedule — 17 minutes (running total: 41 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `02 Schedule` | 1 min | 25 min | Instructor | Signpost the course roadmap and explain how the next topics build from classical methods to modern recommendation systems. |
| `🛣️ Roadmap: Course Learning Outcomes` | 3 min | 28 min | Instructor | Introduce the eight course outcomes and show how the weekly sequence and group project develop them. Highlight the project as the integration point for implementation, evaluation, ethics, and communication. |
| `Course Library` | 2 min | 30 min | Instructor | Introduce Aggarwal's *Recommender Systems: The Textbook* as the core text, then briefly show the specialist books students can consult for ethics, sessions, groups, industry, LLMs, and personalized learning. |
| `Weekly Topics` | 4 min | 34 min | Instructor | Walk through Weeks 1–6, highlighting the progression from recommendation problems and classical methods to retrieval and ranking architectures. |
| `Weekly Topics (cont.)` | 3 min | 37 min | **Student activity — discussion** | **Student activity:** ask students to identify one later topic they are curious or uncertain about. Use responses to surface expectations and clarify the recess week and project workshop. |
| `Class Meetings` | 4 min | 41 min | Instructor | Cover meeting time, venue, recording expectations, attendance, and the absence of tutorials. Confirm that students know where course logistics will be posted. |

### 03 Assignments & Grading — 27 minutes (running total: 68 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `03 Assignments & Grading` | 2 min | 43 min | Instructor | Explain why assessment information comes before the technical material and preview the balance between exam, project, essays, quizzes, and participation. |
| `Grading Overview` | 3 min | 46 min | Instructor | Walk through the assessment weights and the relationship between individual work, group work, peer review, and the final examination. |
| `Class Participation (10%)` | 3 min | 49 min | Instructor | Explain the pre-flight and midterm surveys, in-lecture and pre-lecture activities, and the direct participation consequences of missing required surveys. |
| `Essays (20%)` | 5 min | 54 min | Instructor | Explain the two individual essays, the 8% written-analysis and 2% randomized-peer-review split, AI declaration, and deadlines: Mon, 24 Aug and Mon, 5 Oct 2026 at 23:59 SGT. |
| `Project (30%)` | 7 min | 61 min | Instructor | Explain that students may form 2–4-person teams, but Min has final authority and may override groups for diversity. Cover the declaration due Mon, 24 Aug 2026, 23:59 SGT, the Week 07 design critique, and the mutually exclusive final deliverables: teams presenting at 29th STePS on Wed, 11 Nov do not submit a report; other teams submit a report instead. |
| `Quizzes` | 4 min | 65 min | Instructor | Explain that AI tools are not permitted during in-class quizzes, then describe the peer-and-instructor co-creation workflow, including random assignment of peers to a week and section and instructor curation of final questions. |
| `Authority Chain` | 3 min | 68 min | Instructor | Establish the lecture slides as the authoritative course record, explain how Canvas and the public website support it, and state the default assignment deadline: Mon, 23:59 SGT unless otherwise announced. |

### Break — 5 minutes (running total: 73 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `☕ Break` | 5 min | 73 min | Break | Announce the break, start the five-minute timer, and resume with Section 04 when the timer completes. |

### 04 Recommendation Problems and Decision Goals — 49 minutes (running total: 122 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `04 Recommendation Problems and Decision Goals` | 1 min | 74 min | Instructor | Preview user–item matrices and missingness; prediction, ranking, and useful lists; signals and classical strategies; cold start and long-tail exposure; and situational treatment lenses. |
| `The User–Item Matrix` | 5 min | 79 min | Instructor | Introduce $U$, $I$, $R$, $r_{ui}$, and the observed set $\Omega$. Use dense, sparse, new, and possible-shill rows as evidence situations, not as diagnoses of permanent user type. |
| `From a Score to a Useful List` | 4 min | 83 min | Instructor | Contrast response prediction with top-k ranking and explain why the latter is normally the product decision surface. |
| `Signals and Usefulness` | 4 min | 87 min | Instructor | Use the left-hand taxonomy to distinguish interaction, item, context, and social/operational signals; use the right-hand list to show that evaluation follows usefulness, not merely data availability. |
| `👥 Signal Hunt` | 4 min | 91 min | **Student activity — small-group discussion** | **Student activity:** start the two-minute timer. Pairs name three additional signals, classify them or propose a new category, and identify one benefit and one privacy, fairness, or manipulation risk. Take two reports and distinguish collectable from appropriate data. |
| `👥 Complete the Classical Methods Table` | 3 min | 94 min | **Student activity — small-group discussion (untimed)** | **Student activity:** pairs complete the four highlighted cells and prepare one evidence-based justification. This activity intentionally has no timer, per instructor direction. Probe the relationship between evidence and blind spots, then advance to the debrief. |
| `Four Classical Starting Points` | 2 min | 96 min | Instructor | Reveal the complete cloned table, correct the four answers, and connect popularity to heavy-head exposure and knowledge-based recommendation to stated requirements. |
| `When the Matrix Has No Answer` | 4 min | 100 min | Instructor | Treat new users, items, and systems as information gaps. Contrast requirement elicitation, metadata, transparent fallbacks, and long-tail exposure reserves. |
| `🎰 Bandit Time: What should this system optimise?` | 3 min | 103 min | **Student activity — MCQ** | **Student activity:** give 20 seconds for an individual response, collect justifications, then explain why stated requirements and an explanation best serve the library task while acknowledging trade-offs. |
| `🃏 Treatment Lenses Change With the Task` | 4 min | 107 min | Instructor | Introduce Clubs, Hearts, Diamonds, and Spades as situational treatment lenses, not fixed or demographic user types. |
| `🃏 Four Different Safeguards` | 4 min | 111 min | Instructor | Show how the same catalogue produces different robustness, social, novelty/exposure, and metadata/explanation questions. |
| `👥 Reprise: Find the Recommender 📶` | 11 min | 122 min | **Student activity — small-group discussion + AI Voice critique** | **Student activity:** pairs write a four-line audit of their Section 01 recommendation, including the heavy-head/long-tail exposure consequence and one safeguard. Start the 3-minute timer. Then let the AI Voice agent critique one omitted stakeholder or assumption; students challenge its response. Take two reports and correct misconceptions. |

### 05 Neighborhood-Based Collaborative Filtering — 57 minutes (running total: 179 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `05 Neighborhood-Based Collaborative Filtering (CF)` | 1 min | 123 min | Instructor | Frame neighbourhood collaborative filtering around rating types, sparse and long-tail evidence, user/item neighbourhoods, similarity measures, worked examples, and prediction. Reserve the suit lenses for the closing modelling-choice discussion. |
| `Rating Types` | 2 min | 125 min | Instructor | Name the textbook's rating types before treating Chapter 2's observed rating matrix; state that scale and observation process change what a missing entry means. |
| `The Point of the Long Tail` | 4 min | 129 min | Instructor | Use Figure 2.1 to contrast the heavily rated head with the under-observed tail. Connect thin tail evidence to sparse overlap and exposure concentration. |
| `From a Sparse Matrix to a Neighborhood` | 4 min | 133 min | Instructor | Combine the previous matrix, user/item-neighbourhood, and evidence caveat material. Define $I_u$, $U_i$, overlap, and $P_u(j)$ before equations. |
| `Similarity I: Pearson Correlation` | 5 min | 138 min | Instructor | Decode the orange overlap, teal centred ratings, and navy normalisation. Relate centring to generous versus harsh rating habits. |
| `Worked Example I: Pearson Correlation` | 4 min | 142 min | Instructor | Reveal the shared ratings, user means, centred vectors, and Pearson correlation step by step. |
| `Similarity II: Raw Cosine` | 4 min | 146 min | Instructor | Contrast the raw dot product with Pearson. State explicitly that cosine retains scale bias when raw ratings differ in generosity. |
| `Worked Example II: Raw Cosine` | 4 min | 150 min | Instructor | Reveal the shared ratings, raw vectors, and normalised dot product step by step. |
| `Similarity III: Adjusted Cosine for Items` | 4 min | 154 min | Instructor | Swap the comparison axis from user rows to item columns and show why shared raters are centred before item similarity. |
| `Worked Example III: Item–Item` | 4 min | 158 min | Instructor | Use the Section 04 matrix's mean-centred item columns to calculate adjusted cosine. |
| `Similarity IV: Significance Weighting` | 4 min | 162 min | Instructor | Explain the discount factor and beta. Use the one-versus-twenty shared-rating contrast to make reliability tangible. |
| `Worked Example IV: Significance Weighting` | 4 min | 166 min | Instructor | Reveal the base score, overlap count, threshold, and confidence discount step by step. |
| `👥 Discussion: Which Similarity Axis?` | 3 min | 169 min | **Student activity — paired discussion** | **Student activity:** start the three-minute timer. Pairs choose a setting, argue for user- or item-based similarity, then name a data or product condition that could reverse their decision. Reprise the suit treatments—♣ robustness/shill, ♥ social, ♦ novelty/exposure, ♠ metadata/constraints—and ask which changes their choice or confidence. |
| `🔑 Key Point: Similarity Is a Modelling Choice` | 4 min | 173 min | Instructor | Consolidate the evidence, baseline, and confidence trade-offs without declaring a universal winner. |
| `From Neighbours to a Prediction` | 4 min | 177 min | Instructor | Decode the mean-centred prediction equation and explain target-item-specific valid top-k neighbours. |
| `🔑 Key Point: A Neighbourhood Is a Choice` | 2 min | 179 min | Instructor | Synthesize the modelling choices: overlap, centring, discounting, and top-k selection. |

## Pacing and facilitation notes

- Keep the three section-title slides short; they are orientation points, not content lectures.
- Protect the 10-minute `👥 Find the Recommender` small-group activity: timebox the pairs, then reserve time for synthesis.
- If discussion runs long, shorten the `Weekly Topics (cont.)` discussion first, then reduce the report-out after `👥 Reprise: Find the Recommender 📶`.
- If the class is quiet, use pairs for 60–90 seconds before taking responses from the room.
- The instructor remains responsible for factual accuracy, course policy, and the final synthesis after every AI interaction.
