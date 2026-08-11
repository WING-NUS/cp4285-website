# CP4285 Week 1 Lecture Timeline

##### Changelog

- **11 Aug 2026** — Re-timed the delivery plan to the 90-minute teaching slot; retained activities keep their stated timeboxes, while duplicate or non-essential activities are deferred.
- **10 Aug 2026** — Added the Mon, 23:59 SGT default-deadline policy and exact assessment deadlines.
- **10 Aug 2026** — Updated project-team formation: Min may adjust teams to support diversity.

**Lecture:** Recommendation Problems and Classical Methods  
**Scheduled class time:** 90 minutes

**Current run-of-show:** 90 minutes
**Deck:** [`w01.qmd`](./w01.qmd)

**Delivery decision:** Retain the core timed learning activities: the objectives MCQ, *Find the Recommender*, Signal Hunt, the classical-methods table, the cold-start MCQ, and the similarity-axis discussion. The three-minute `Weekly Topics (cont.)` discussion is delivered as a brief instructor-led schedule slide, and the 11-minute `Reprise: Find the Recommender` activity is deferred because it duplicates the earlier audit activity.

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
| **Deferred** | Do not run during this 90-minute session; retain the slide in the deck for later use or independent follow-up. |

## Section overview

| Section | Slides | Time | Running total | Share of run-of-show |
|---|---:|---:|---:|---:|
| 01 Overview | 8 | 20 min | 20 min | 22.2% |
| 02 Schedule | 6 | 5 min | 25 min | 5.6% |
| 03 Assignments & Grading | 8 | 10 min | 35 min | 11.1% |
| Break | 1 | 5 min | 40 min | 5.6% |
| 04 Recommendation Problems and Decision Goals | 13 | 20.5 min | 60.5 min | 22.8% |
| 05 Neighborhood-Based Collaborative Filtering | 23 | 29.5 min | 90 min | 32.8% |
| **Total** | **59** | **90 min** | **90 min** | **100%** |

## Detailed run-of-show

### 01 Overview — 20 minutes (running total: 20 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `01 Overview` | 1 min | 1 min | Instructor | Welcome the class, state the learning goals, and frame the section around recommendation systems and recurring ethics. |
| `🎥 Video: Spotify Recommendations` | 3 min | 4 min | Video | Play the selected excerpt, then take one observation about its user signals and objectives. |
| `Recommendations Everywhere` | 1 min | 5 min | Instructor | Establish the recommendation pattern and emphasise that ranking affects attention. |
| `CP Pilot Course` | 1 min | 6 min | Instructor | Give the essential pilot-course framing; defer process detail to Canvas. |
| `🎰 Bandit Time: Objectives` | 2 min | 8 min | **Student activity — MCQ** | **Student activity:** retain the 20-second countdown, sample justifications, and explain why objectives can alter exposure. |
| `📶 AI Voice Mode` | 1 min | 9 min | **AI Voice Mode** | Ask for one everyday recommendation example and identify one assumption in the response. |
| `👥 Find the Recommender` | 10 min | 19 min | **Student activity — small-group discussion** | **Student activity:** pairs audit one recent recommendation, identify signals and objectives, and name who or what might be left unseen; take one or two reports and synthesise. |
| `📶 Ethics Thread` | 1 min | 20 min | Instructor | Connect the activity back to attention, visibility, and opportunity. |

### 02 Schedule — 5 minutes (running total: 25 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `02 Schedule` | 0.5 min | 20.5 min | Instructor | Signpost the roadmap. |
| `🛣️ Roadmap: Course Learning Outcomes` | 1 min | 21.5 min | Instructor | State the outcome progression and project integration point. |
| `Course Library` | 0.5 min | 22 min | Instructor | Identify the core textbook and specialist references. |
| `Weekly Topics` | 1 min | 23 min | Instructor | Walk through Weeks 1–6. |
| `Weekly Topics (cont.)` | 1 min | 24 min | Instructor | Walk through Weeks 7–13; do not run the optional curiosity discussion in this delivery. |
| `Class Meetings` | 1 min | 25 min | Instructor | Confirm meeting arrangements and recording/attendance expectations. |

### 03 Assignments & Grading — 10 minutes (running total: 35 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `03 Assignments & Grading` | 0.5 min | 25.5 min | Instructor | Preview the assessment balance. |
| `Grading Overview` | 1 min | 26.5 min | Instructor | State weights and individual/group components. |
| `Class Participation (10%)` | 1 min | 27.5 min | Instructor | Highlight surveys and participation consequences. |
| `Essays (20%)` | 2 min | 29.5 min | Instructor | Cover individual work, peer-review split, AI declaration, and deadlines. |
| `Project (30%)` | 3 min | 32.5 min | Instructor | Cover teams, declaration, design critique, and mutually exclusive final deliverables. |
| `Recommendation Dataset Catalogue` | 0.5 min | 33 min | Instructor | Point students to the catalogue and its provenance/licence checks. |
| `Quizzes` | 1 min | 34 min | Instructor | State the quiz policy and AI restriction. |
| `Authority Chain` | 1 min | 35 min | Instructor | Confirm that slides are authoritative and restate the default deadline convention. |

### Break — 5 minutes (running total: 40 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `☕ Break` | 5 min | 40 min | Break | Announce the break and use the existing five-minute timer. |

### 04 Recommendation Problems and Decision Goals — 20.5 minutes (running total: 60.5 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `04 Recommendation Problems and Decision Goals` | 0.5 min | 40.5 min | Instructor | Preview the decision problem, evidence, objectives, and method choices. |
| `The User–Item Matrix` | 2 min | 42.5 min | Instructor | Introduce $U$, $I$, $R$, observed feedback, and missingness. |
| `From a Score to a Useful List` | 1 min | 43.5 min | Instructor | Contrast prediction and top-$k$ ranking. |
| `Signals and Usefulness` | 1 min | 44.5 min | Instructor | Distinguish inputs from the qualities by which a list is judged. |
| `👥 Signal Hunt` | 4 min | 48.5 min | **Student activity — small-group discussion** | **Student activity:** retain the two-minute timer, pair work, reports, and ethics synthesis. |
| `👥 Complete the Classical Methods Table` | 3 min | 51.5 min | **Student activity — small-group discussion (untimed)** | **Student activity:** retain the stated untimed pair task and immediate evidence-based debrief. |
| `Four Classical Starting Points` | 1 min | 52.5 min | Instructor | Reveal the complete comparison and correct the activity. |
| `When the Matrix Has No Answer` | 1.5 min | 54 min | Instructor | Frame cold start as an information gap and name suitable responses. |
| `🎰 Bandit Time: What should this system optimise?` | 3 min | 57 min | **Student activity — MCQ** | **Student activity:** retain individual response, 20-second timer, justifications, and explanation. |
| `“What types of users are there?”` | 0.5 min | 57.5 min | Instructor | Introduce situational treatment lenses. |
| `🃏 Treatment Lenses Change With the Task` | 1.5 min | 59 min | Instructor | Explain the four lenses without treating them as fixed identities. |
| `🃏 Four Different Safeguards` | 1.5 min | 60.5 min | Instructor | Connect the lenses to robustness, social exposure, novelty, and metadata/constraints. |
| `👥 Reprise: Find the Recommender 📶` | 0 min | 60.5 min | **Deferred** | Do not run in this session. It duplicates the earlier 10-minute audit; use it as a Week 2 recap or Canvas follow-up if needed. |

### 05 Neighborhood-Based Collaborative Filtering — 29.5 minutes (running total: 90 minutes)

| Slide | Time | Running total | Mode | Delivery plan |
|---|---:|---:|---|---|
| `05 Neighborhood-Based Collaborative Filtering (CF)` | 0.5 min | 61 min | Instructor | Frame CF as local inference from sparse interaction evidence. |
| `Rating Types` | 0.5 min | 61.5 min | Instructor | Identify rating types and the meaning of missingness. |
| `The Point of the Long Tail` | 2.5 min | 64 min | Instructor | Connect sparse tail evidence to similarity uncertainty and exposure concentration. |
| `From a Sparse Matrix to a Neighborhood` | 2.5 min | 66.5 min | Instructor | Define overlap and user/item neighborhoods before the similarity measures. |
| `Similarity I: Pearson Correlation` | 2 min | 68.5 min | Instructor | Explain centring and rating-scale differences. |
| `Worked Example I: Pearson Correlation` | 1.5 min | 70 min | Instructor | Step through the shared ratings, means, and correlation. |
| `Similarity II: Raw Cosine` | 1.5 min | 71.5 min | Instructor | Contrast raw magnitude with Pearson's centring. |
| `Worked Example II: Raw Cosine` | 1 min | 72.5 min | Instructor | Show the normalised dot product. |
| `Similarity III: Adjusted Cosine for Items` | 1.5 min | 74 min | Instructor | Switch the comparison axis to items and centre shared raters. |
| `Worked Example III: Item–Item` | 1 min | 75 min | Instructor | Apply adjusted cosine to the item columns. |
| `From Item Neighbours to a Prediction` | 2 min | 77 min | Instructor | Turn item similarity into a prediction from the target user's ratings. |
| `Similarity IV: Significance Weighting` | 1.5 min | 78.5 min | Instructor | Explain confidence discounts for thin overlap. |
| `Worked Example IV: Significance Weighting` | 1 min | 79.5 min | Instructor | Apply the overlap discount. |
| `User–User KNN in RecBole` | 1 min | 80.5 min | Instructor | Map the minimal configuration to the preceding concepts. |
| `👥 Discussion: Which Similarity Axis?` | 3 min | 83.5 min | **Student activity — paired discussion** | **Student activity:** retain the three-minute timer, pair argument, reversal condition, and brief report. |
| `🔑 Key Point: Similarity Is a Modelling Choice` | 1 min | 84.5 min | Instructor | Consolidate evidence, baseline, and confidence trade-offs. |
| `Neighbourhood Choices` | 1 min | 85.5 min | Instructor | Distinguish eligibility choices from aggregation choices. |
| `From Neighbours to a Prediction` | 1.5 min | 87 min | Instructor | Decode the mean-centred user-based prediction pipeline. |
| `Practicality: Making Neighbourhoods Work` | 1 min | 88 min | Instructor | Contrast offline preparation and online serving. |
| `Section 05 Summary: Neighbourhood CF` | 0.5 min | 88.5 min | Instructor | Rehearse represent, compare, predict, and rank. |
| `🔑 Summary` | 0.5 min | 89 min | Instructor | Close the week with evidence, objectives, and consequences. |
| `👥 Pre-lecture: Look for Hidden Structure` | 0.5 min | 89.5 min | Instructor | Set the Canvas prompt and reply expectation. |
| `Next Week: Latent Factor Models` | 0.5 min | 90 min | Instructor | Preview the transition from local overlap to latent structure. |

## Pacing and facilitation notes

- The retained activity timeboxes are fixed. If one overruns, reduce instructor explanation, not the next activity's discussion or synthesis.
- Protect the 10-minute `👥 Find the Recommender` activity and the five-minute break; together they provide the primary reflection and recovery time in the compact session.
- Do not reinstate the `Weekly Topics (cont.)` discussion or `👥 Reprise: Find the Recommender 📶` unless other material is intentionally removed.
- If time is tight in Section 05, use the worked examples to point to the matching equation steps rather than deriving every arithmetic operation aloud.
- The instructor remains responsible for factual accuracy, course policy, and the final synthesis after every AI interaction.
