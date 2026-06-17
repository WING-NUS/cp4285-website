---
title: Schedule
weight: 10
---

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
      <td></td>
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
      <td></td>
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
      <td>Tue, 10 Nov 2026</td>
      <td>Final Project Presentations</td>
      <td>Final project presentation</td>
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

### Week 1: Recommendation Problems and Classical Methods

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

### Week 2: Latent Factor Models

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

### Week 3: Evaluation of Recommendation Systems

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

### Week 4: Neural Recommendation Models

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

### Week 5: Sequential and Session-Based Recommendation

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

### Week 6: Retrieval and Ranking Architectures

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

### Week 7: Project Design Critique Workshop

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

### Week 8: Learning-to-Rank

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

### Week 9: Graph-Based Recommendation

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

### Week 10: Multi-Objective Recommendation

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

### Week 11: Exploration and Online Learning

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

### Week 12: LLMs, Generative Recommendation, and Research Frontiers

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

### Week 13: Final Project Presentations

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
