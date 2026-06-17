---
title: 'CP4285: Modern Recommendation Systems'
date: 2026-06-15
type: landing

sections:
  - block: hero
    content:
      title: "CP4285: Modern Recommendation Systems"
      text: 'Emerging Topics in Computer Science V<br>A course covering recommendation foundations, modern recommender methods and hands-on group work.'
      primary_action:
        text: Go to Canvas
        url: https://canvas.nus.edu.sg/courses/98339
        icon: arrow-top-right-on-square
      media:
        src: /uploads/recommendation-social-media.png
        alt: Recommendation icon showing a social media recommendation interaction
      trust:
        text: '<span class="hero-attribution">Recommendation icons created by <a href="https://www.flaticon.com/free-icons/recommendation" title="recommendation icons">Freepik - Flaticon</a></span>'
      announcement:
        text: "NUS School of Computing — Emerging Topics in Computer Science V"
    design:
      spacing:
        padding: ["5rem", 0, "4rem", 0]
        margin: [0, 0, 0, 0]
      layout: split-right
      alignment: left
      css_class: "nus-hero"
      background:
        color: "#061323"
  - block: course-notice
    content:
      text: This website is provided for external and public reference. Course materials and any timely course information are communicated only within Canvas.
    design:
      css_class: "bg-white dark:bg-gray-950"
  - block: markdown
    content:
      title: About Emerging Topics in Computer Science Courses
      text: |
        CP4285 is part of the **CP428x Emerging Topics in Computer Science** series at NUS. These are pilot courses, each run for a single semester only, with the intention of eventually becoming a permanent offering. Students should expect that the course is not yet fully mature: content, assessments, and delivery are actively evolving. The series exists to expose undergraduates to emerging areas of computer science before they become established parts of the curriculum.
    design:
      css_class: "bg-slate-50 dark:bg-gray-950"
  - block: markdown
    content:
      title: About the Course
      text: |
        CP4285: Modern Recommendation Systems examines the algorithms, data, and design trade-offs behind contemporary recommender systems. The course connects classical recommendation methods with modern neural approaches, and emphasizes practical implementation, careful evaluation, and responsible deployment in real-world settings.

        Recommendation systems now shape many everyday decisions: what people read, watch, buy, study, apply for, and who or what receives attention. Their influence extends beyond convenience into visibility, opportunity, trust, and social outcomes, making it important to understand not only how these systems work, but also what values and trade-offs they encode.

        CP4285 covers classical methods, neural architectures, ranking and retrieval pipelines, sequential models, graph-based recommendation, online learning, and emerging LLM-based approaches. Ethical issues are interwoven throughout, including bias, fairness, privacy, exposure, transparency, and stakeholder impact. Students apply these ideas in a hands-on group project requiring problem formulation, dataset work, baselines, model design, evaluation, critique, and final presentation.

        **Prerequisites:** [CS2109S](https://nusmods.com/courses/CS2109S/introduction-to-ai-and-machine-learning) (Introduction to AI and Machine Learning) or equivalent, and completion of at least 120 units. Students without CS2109S but with equivalent background may seek approval from Min.

        **Workload:** [(2-0-0-3-5)](https://nusmods.com/courses/CP4285/emerging-topics-in-computing-v#timetable) — 2 hours lecture, 3 hours projects and assignments, 5 hours preparatory and other work; approximately 10 hours per week.
    design:
      css_class: "bg-white dark:bg-gray-950"
  - block: features
    id: rhythm
    content:
      title: Course Rhythm
      text: The semester moves from foundations into project critique, then advanced methods and final presentations.
      items:
        - name: "Weeks 1-6: Foundations"
          icon: calendar-days
          description: Recommendation tasks, latent factors, evaluation, neural models, sequence models, and retrieval-ranking architectures.
        - name: "Week 7: Design Review"
          icon: shield-check
          description: Teams critique project domains, datasets, objectives, baselines, evaluation plans, feasibility, and ethical risks.
        - name: "Weeks 8-12: Modern Recommenders"
          icon: chart-bar
          description: Learning-to-rank, graph recommendation, multi-objective systems, online learning, LLMs, and research frontiers.
        - name: "Week 13: Project Showcase"
          icon: presentation-chart-bar
          description: Final project presentations integrate technical design, evaluation results, error analysis, and ethical analysis.
    design:
      css_class: "bg-slate-50 dark:bg-gray-950"
  - block: markdown
    id: outcomes
    content:
      title: Learning Outcomes
      text: |
        By the end of the course, students should be able to:

        | CLO | Outcome |
        | :-- | :--- |
        | **CLO 1** | Explain and compare classical recommendation methods, including collaborative filtering, content-based filtering, and hybrid approaches. |
        | **CLO 2** | Implement matrix factorization and neural recommendation models using modern deep learning frameworks. |
        | **CLO 3** | Design and execute rigorous offline evaluation protocols using appropriate ranking metrics. |
        | **CLO 4** | Analyse the cold-start problem and propose strategies to address it. |
        | **CLO 5** | Critique recommender systems from fairness, privacy, transparency, and stakeholder impact perspectives. |
        | **CLO 6** | Explain advanced recommendation architectures including sequential, graph-based, multi-objective, and LLM-enhanced systems. |
        | **CLO 7** | Design and justify a complete recommendation system pipeline from problem formulation through evaluation and ethical analysis. |
        | **CLO 8** | Communicate and defend recommendation-system designs and results to a technical audience. |
    design:
      css_class: "bg-white dark:bg-gray-950"
  - block: features
    id: links
    content:
      title: Course Pages
      items:
        - name: Schedule
          icon: calendar-days
          description: Weekly topics, milestones, and important dates.
          url: docs/schedule/
        - name: Assignments & Projects
          icon: clipboard-document-check
          description: Coursework components, project milestones, and submission notes.
          url: docs/assignments/
        - name: Grading
          icon: chart-bar
          description: Assessment components, weights, academic honesty, and AI use policy.
          url: docs/grading/
        - name: FAQ
          icon: question-mark-circle
          description: Frequently asked questions about the course.
          url: docs/faq/
    design:
      css_class: "bg-slate-50 dark:bg-gray-950"
---
