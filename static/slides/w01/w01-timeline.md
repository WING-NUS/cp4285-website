# CP4285 Week 1 Lecture Timeline

**Lecture:** Recommendation Problems and Classical Methods  
**Class time:** 120 minutes (Tuesday, 10:00–12:00 SGT)  
**Deck:** [`w01.qmd`](./w01.qmd)

**Scoped revision:** Section 01 now takes 20 minutes. The run-of-show has been rebalanced to the 120-minute class and matches the rebuilt 16:9 deck.

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

| Section | Slides | Time | Share of class |
|---|---:|---:|---:|
| 01 Overview | 8 | 20 min | 17%* |
| 02 Schedule | 5 | 15 min | 13% |
| 03 Assignments & Grading | 5 | 27 min | 23% |
| 04 Types of Recommendation Systems | 7 | 58 min | 48% |
| **Total** | **25** | **120 min** | 100% |

\* Section 01 now targets 20 minutes in this scoped revision. The remaining section timings are intentionally unchanged, so the full run-of-show will require a later six-minute rebalancing.

## Detailed run-of-show

### 01 Overview — 20 minutes

| Slide | Time | Mode | Delivery plan |
|---|---:|---|---|
| `01 Overview` | 1 min | Instructor | Welcome the class, state the learning goals, and frame the section around recommendation systems, course co-development, and recurring ethics. |
| `🎥 Video: Spotify Recommendations` | 3 min | Video | Open the linked thumbnail, play the selected excerpt, and pause once to ask which user signals and objectives students heard. |
| `Recommendations Everywhere` | 2 min | Instructor | Establish recommendations as a general pattern across video, music, shopping, news, jobs, social feeds, and course resources. Distinguish inputs from outputs and emphasise that ranking affects attention. |
| `CP Pilot Course` | 4 min | Instructor | Explain that students help shape future course delivery through self-learning, lab/tutorial development, process documentation, and constructive feedback. Clarify that staff retain final review and course standards. |
| `🎰 Bandit Time: Objectives` | 2 min | MCQ | Start the default 20-second countdown for individual responses, then sample justifications and explain why the correct answer is that the systems may rank different items and expose different creators. |
| `📶 AI Voice Mode` | 2 min | Voice-mode AI agent | Ask the agent for one everyday recommendation example and have it identify the signal, item, objective, and one consequence. Stop after two minutes and correct oversimplifications. |
| `Ethics Thread` | 3 min | Instructor | Establish ethics as a recurring motif: recommendations allocate attention and opportunity, encode values, and create risks involving bias, privacy, exposure, transparency, fairness, and stakeholder impact. |
| `👥 Find the Recommender` | 3 min | In-class activity | Students audit one recent recommendation, identify likely signals and objective, and name who or what might be left unseen. Use pairs, then take one or two observations. The title emoji identifies this as the small-group activity. |

### 02 Schedule — 15 minutes

| Slide | Time | Mode | Delivery plan |
|---|---:|---|---|
| `02 Schedule` | 1 min | Instructor | Signpost the course roadmap and explain how the next topics build from classical methods to modern recommendation systems. |
| `Course Learning Outcomes` | 3 min | Instructor | Introduce the eight course outcomes and show how the weekly sequence and group project develop them. Highlight the project as the integration point for implementation, evaluation, ethics, and communication. |
| `Weekly Topics` | 4 min | Instructor | Walk through Weeks 1–6, highlighting the progression from recommendation problems and classical methods to retrieval and ranking architectures. |
| `Weekly Topics (cont.)` | 3 min | Discussion | Ask students to identify one later topic they are curious or uncertain about. Use responses to surface expectations and clarify the recess week and project workshop. |
| `Class Meetings` | 4 min | Instructor | Cover meeting time, venue, recording expectations, attendance, and the absence of tutorials. Confirm that students know where course logistics will be posted. |

### 03 Assignments & Grading — 27 minutes

| Slide | Time | Mode | Delivery plan |
|---|---:|---|---|
| `03 Assignments & Grading` | 2 min | Instructor | Explain why assessment information comes before the technical material and preview the balance between exam, project, essays, quizzes, and participation. |
| `Grading Overview` | 5 min | Instructor | Walk through each assessment weight, key dates, and how the components collectively assess technical understanding and critical judgement. Take clarification questions. |
| `Project` | 9 min | Discussion | In small groups, ask students to propose a recommendation dataset and a problem statement that could be investigated. Invite one or two examples and distinguish a researchable question from a broad product idea. |
| `Essays` | 6 min | Voice-mode AI agent | Ask the agent: “What would count as original critical analysis in an essay about a recommender system, and where could AI assistance become inappropriate?” Have students compare the response with the slide’s AI-declaration requirement, then debrief the limits. |
| `Quizzes` | 5 min | Instructor | Explain the Pre-Flight Survey, Midterm Survey, deadlines, and participation impact. End with a concrete reminder of the Week 2 deadline. |

### 04 Types of Recommendation Systems — 58 minutes

| Slide | Time | Mode | Delivery plan |
|---|---:|---|---|
| `04 Types of Recommendation Systems` | 2 min | Instructor | Introduce the technical core of the lecture and state that the class will compare paradigms by user need, available data, and objective. |
| `A Card-Suit Framework for User Types` | 12 min | Discussion | Ask students to choose the card-suit archetype that best describes their behaviour on a familiar platform. Discuss disagreements and emphasise that user types can be mixed and can change by context. |
| `Matching Systems to User Types` | 8 min | Instructor | Explain the mapping from archetype to diversity-aware, social, retrieval-ranking, and content-based approaches. Point out that this is a heuristic, not a fixed taxonomy. |
| `Classical Recommendation Paradigms` | 10 min | Instructor | Teach popularity-based, content-based, collaborative-filtering, and hybrid approaches. For each, name the signal it uses, the personalisation it provides, and one limitation. |
| `The Cold-Start Problem` | 10 min | Voice-mode AI agent | Role-play with the agent as a product manager launching a new platform. Ask it to propose onboarding, content-feature, and popularity-fallback strategies for a new user, a new item, and a new system. Students challenge one recommendation and the instructor synthesises the trade-offs. |
| `Ethics Thread: Popularity Bias and Exposure Inequality` | 10 min | Voice-mode AI agent | Ask the agent to argue both for and against optimising recommendations for engagement. Students question its assumptions about creators, minority preferences, and long-tail exposure; the instructor closes by identifying the feedback loop and the affected stakeholders. |
| `Summary` | 6 min | Discussion | Have students use the comparison table to answer: “Which method would you choose for a new user, a catalogue with rich item features, and a mature platform?” Collect answers, correct misconceptions, and preview latent factor models for Week 2. |

## Pacing and facilitation notes

- Keep the three section-title slides short; they are orientation points, not content lectures.
- Protect the 10-minute voice-mode activities by stopping the agent conversation at the time limit and debriefing aloud.
- If discussion runs long, shorten the `Weekly Topics (cont.)` discussion first, then the `Summary` discussion. Do not cut the cold-start or ethics activities below 7 minutes each.
- If the class is quiet, use pairs for 60–90 seconds before taking responses from the room.
- The instructor remains responsible for factual accuracy, course policy, and the final synthesis after every AI interaction.
