# Week 01 Reference Example

Canonical YAML front matter and structural skeleton from week01.qmd.

## Actual Front Matter

```yaml
---
title: "Recommendation Problems and Classical Methods"
subtitle: "CP4285 Modern Recommendation Systems — Week 1"
author: "CP4285 Instruction Team"
date: "11 Aug 2026"
date-format: "DD MMM YYYY"
format:
  revealjs:
    theme: [default, custom.scss]
    slide-number: true
    show-slide-number: all
    chalkboard: false
    logo: "../../uploads/recommendation-social-media.png"
    footer: "CP4285 · Week 1 · NUS School of Computing"
    self-contained: true
    transition: slide
    highlight-style: github
    code-line-numbers: true
    smaller: false
    scrollable: false
---
```

## Section Structure

| Section | H1 Title | Slides |
|---|---|---|
| 01 | Overview | CP Pilot Course, Ethics Thread |
| 02 | Schedule | Weekly Topics, Weekly Topics (cont.), Class Meetings |
| 03 | Assignments & Grading | Grading Overview, Project, Essays, Quizzes |
| 04 | Types of Recommendation Systems | Card-Suit Framework, Matching Systems, Classical Paradigms, Cold-Start, Ethics Thread, Summary |

## Patterns Used

- Section title slides: `# NN Title {background-color="#EF7C00"}`
- Two-column layout: `.columns` / `.column width="50%"`
- Incremental lists: `.incremental`
- Callouts: `.callout-warning`, `.callout-note`
- Speaker notes on every slide with `<!-- TODO (students): ... -->` placeholders
- Summary slide with comparison table + "Next week:" teaser
