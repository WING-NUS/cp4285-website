---
title: Schedule
weight: 10
changelog:
  - date: 10 Aug 2026
    text: Added Week 03 and Week 08 assessment deadlines.
  - date: 10 Aug 2026
    text: Corrected the final project presentation date to Wed, 11 Nov 2026.
  - date: 08 Aug 2026
    text: Updated the embedded Week 01 slide-deck link.
---

{{< changelog >}}

## Class Meetings

| Day | Time | Venue |
| --- | --- | --- |
| Every Tuesday | 10:00-12:00 SGT | [Seminar Room 12, COM3-01-21](https://nusmods.com/venues/COM3-01-21) |

## Weekly Schedule

<table class="course-schedule-table">
  <thead>
    <tr>
      <th>Week</th>
      <th>Date / Period</th>
      <th>Focus</th>
      <th>Assessment Due</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Tue, 11 Aug 2026</td>
      <td>Recommendation Problems and Classical Methods</td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Tue, 18 Aug 2026</td>
      <td>Latent Factor Models</td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Tue, 25 Aug 2026</td>
      <td>Evaluation of Recommendation Systems</td>
      <td>Essay 1 + Project Mini-team Declaration — Mon, 24 Aug, 23:59 SGT</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Tue, 1 Sep 2026</td>
      <td>Neural Recommendation Models</td>
      <td></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Tue, 8 Sep 2026</td>
      <td>Sequential and Session-Based Recommendation</td>
      <td></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Tue, 15 Sep 2026</td>
      <td>Retrieval and Ranking Architectures</td>
      <td></td>
    </tr>
    <tr class="schedule-break-row">
      <td>Recess Week</td>
      <td>Tue, 22 Sep 2026</td>
      <td>No class</td>
      <td></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Tue, 29 Sep 2026</td>
      <td>Project Design Critique Workshop</td>
      <td>Project design critique</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Tue, 6 Oct 2026</td>
      <td>Learning-to-Rank</td>
      <td>Essay 2 — Mon, 5 Oct, 23:59 SGT</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Tue, 13 Oct 2026</td>
      <td>Graph-Based Recommendation</td>
      <td></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Tue, 20 Oct 2026</td>
      <td>Multi-Objective Recommendation</td>
      <td></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Tue, 27 Oct 2026</td>
      <td>Exploration and Online Learning</td>
      <td></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Tue, 3 Nov 2026</td>
      <td>LLMs, Generative Recommendation, and Research Frontiers</td>
      <td></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Wed, 11 Nov 2026</td>
      <td>Final Project Presentations</td>
      <td>Final project presentation or report (depending on STePS participation)</td>
    </tr>
    <tr class="schedule-break-row">
      <td>Reading Week</td>
      <td>Sat, 14 Nov 2026-Fri, 20 Nov 2026</td>
      <td>Reading week</td>
      <td></td>
    </tr>
    <tr class="schedule-exam-row">
      <td>Examination Week 1</td>
      <td>Mon, 23 Nov 2026</td>
      <td>Examination period</td>
      <td>Final exam, 13:00-15:00 SGT, venue to be announced</td>
    </tr>
    <tr class="schedule-exam-row">
      <td>Examination Week 2</td>
      <td>Sat, 28 Nov 2026-Sat, 5 Dec 2026</td>
      <td>Examination period</td>
      <td></td>
    </tr>
  </tbody>
</table>

## Weekly Details

{{< week-card >}}
### Week 1: Recommendation Problems and Classical Methods (11-17 Aug 2026)

Topics:

- Recommendation tasks
- Explicit vs implicit feedback
- Popularity-based recommendation
- Content-based recommendation
- Collaborative filtering

Ethics thread: popularity bias, exposure inequality, and platform incentives.

Learning outcomes:

- Formulate recommendation problems.
- Differentiate recommendation paradigms.
- Analyze cold-start challenges.
- Explain how recommendation objectives affect exposure.

**Slides:**

{{< slides src="/cp4285-website/slides/w01/w01.html" title="Week 1 Slides" height="520px" >}}
{{< /week-card >}}

{{< week-card >}}
### Week 2: Latent Factor Models (18-24 Aug 2026)

Topics:

- Matrix factorization
- User-item embeddings
- Bias models
- Ranking objectives, including Bayesian Personalized Ranking

Ethics thread: bias encoded in historical interactions, representation, and interpretability.

Learning outcomes:

- Explain latent-factor models.
- Train embedding-based recommenders.
- Compare prediction and ranking objectives.
- Discuss risks of learning from historical behavior.
{{< /week-card >}}

{{< week-card >}}
### Week 3: Evaluation of Recommendation Systems (25-31 Aug 2026)

Topics:

- Offline evaluation
- Precision@K
- Recall@K
- MAP
- NDCG
- Business metrics

Ethics thread: metrics as value choices, and accuracy versus user welfare.

Learning outcomes:

- Design evaluation protocols.
- Compute ranking metrics.
- Critique metric selection.
- Explain limitations of offline evaluation.
{{< /week-card >}}

{{< week-card >}}
### Week 4: Neural Recommendation Models (1-7 Sep 2026)

Topics:

- Neural collaborative filtering
- Deep ranking models
- Representation learning

Ethics thread: explainability versus performance, and transparency concerns.

Learning outcomes:

- Build neural recommenders.
- Compare neural and latent-factor approaches.
- Analyze explainability challenges.
- Assess trade-offs between complexity and transparency.
{{< /week-card >}}

{{< week-card >}}
### Week 5: Sequential and Session-Based Recommendation (8-14 Sep 2026)

Topics:

- User sequences
- GRU4Rec
- SASRec
- Transformer recommenders

Ethics thread: engagement optimization and behavioral manipulation risks.

Learning outcomes:

- Model temporal preferences.
- Implement next-item prediction.
- Compare static and dynamic representations.
- Critically assess engagement-driven objectives.
{{< /week-card >}}

{{< week-card >}}
### Week 6: Retrieval and Ranking Architectures (15-21 Sep 2026)

Topics:

- Candidate generation
- Retrieval
- Ranking
- Re-ranking
- Two-tower architectures

Ethics thread: visibility allocation and stakeholder impacts.

Learning outcomes:

- Explain industrial recommendation pipelines.
- Design retrieval-ranking architectures.
- Analyze scalability trade-offs.
- Evaluate how ranking affects different stakeholders.
{{< /week-card >}}

{{< week-card >}}
### Week 7: Project Design Critique Workshop (29 Sep-5 Oct 2026)

Student deliverables:

- Application domain
- Dataset
- User problem
- Recommendation objective
- Baselines
- Evaluation plan
- Ethical risks

Ethics thread: feasibility, bias, evaluation design, and project scope.

Peer critique themes:

- Is the recommendation task well-defined?
- Are the evaluation metrics appropriate?
- What biases may emerge?
- Is the problem feasible?

Learning outcomes:

- Defend recommendation-system designs.
- Critique evaluation strategies.
- Identify ethical risks early.
- Refine project scope based on feedback.

Suggested weight: 5-10% participation or milestone grade.
{{< /week-card >}}

{{< week-card >}}
### Week 8: Learning-to-Rank (6-12 Oct 2026)

Topics:

- Pointwise ranking
- Pairwise ranking
- Listwise ranking
- LambdaRank intuition

Ethics thread: position bias and fair ranking.

Learning outcomes:

- Formulate ranking objectives.
- Compare ranking approaches.
- Analyze position bias.
- Discuss fairness implications of ranking.
{{< /week-card >}}

{{< week-card >}}
### Week 9: Graph-Based Recommendation (13-19 Oct 2026)

Topics:

- User-item graphs
- Graph embeddings
- Graph neural networks
- LightGCN

Ethics thread: homophily, echo chambers, and community amplification.

Learning outcomes:

- Represent recommendations as graph problems.
- Explain graph propagation.
- Build graph-based recommenders.
- Analyze risks of graph-driven feedback loops.
{{< /week-card >}}

{{< week-card >}}
### Week 10: Multi-Objective Recommendation (20-26 Oct 2026)

Topics:

- Diversity
- Novelty
- Serendipity
- Coverage
- Long-term satisfaction

Ethics thread: balancing stakeholder interests.

Learning outcomes:

- Define non-accuracy objectives.
- Measure diversity and novelty.
- Design multi-objective recommenders.
- Justify objective trade-offs.
{{< /week-card >}}

{{< week-card >}}
### Week 11: Exploration and Online Learning (27 Oct-2 Nov 2026)

Topics:

- Multi-armed bandits
- Contextual bandits
- Exploration-exploitation
- Feedback loops

Ethics thread: online experimentation and fair exposure.

Learning outcomes:

- Explain exploration strategies.
- Design adaptive recommendation policies.
- Analyze recommendation feedback loops.
- Discuss ethical implications of experimentation.
{{< /week-card >}}

{{< week-card >}}
### Week 12: LLMs, Generative Recommendation, and Research Frontiers (3-9 Nov 2026)

Topics:

- Conversational recommendation
- LLM-enhanced recommendation
- Retrieval-augmented recommendation
- Foundation models
- Causal recommendation
- Future directions

Ethics thread: trust, hallucination, persuasive AI, and governance.

Learning outcomes:

- Explain modern recommendation research directions.
- Evaluate LLM-based recommendation systems.
- Critique emerging approaches.
- Identify open research challenges.
{{< /week-card >}}

{{< week-card >}}
### Week 13: Final Project Presentations (10 Nov 2026)

Required presentation components:

1. Problem formulation
2. Dataset and preprocessing
3. Baselines
4. Proposed recommender
5. Evaluation results
6. Error analysis
7. Ethical analysis
8. Future improvements

Ethics thread: technical, product, and societal considerations.

Learning outcomes:

- Present recommendation-system designs professionally.
- Defend technical decisions.
- Interpret evaluation results critically.
- Integrate technical, product, and societal considerations.
{{< /week-card >}}
