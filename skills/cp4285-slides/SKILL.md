---
name: cp4285-slides
description: Style guide and authoring conventions for CP4285 Quarto RevealJS slide decks. Use when creating, editing, or extending any weekly lecture slide deck for the CP4285 course. Covers YAML front matter, colour palette, typography, SCSS theme, structural patterns, and content conventions extracted from the week01 reference deck.
---

# CP4285 Slides — Authoring Guide

## Overview

All CP4285 slide decks are authored in **Quarto Markdown (`.qmd`)** and rendered as **RevealJS** presentations. Each deck lives under `static/slides/weekNN/` in the repo and ships with its own `custom.scss` theme file (see `templates/custom.scss`).

---

## YAML Front Matter Template

```yaml
---
title: "<Lecture Title>"
subtitle: "CP4285 Modern Recommendation Systems — Week N"
author: "CP4285 Instruction Team"
date: "DD MMM YYYY"
date-format: "DD MMM YYYY"
format:
  revealjs:
    theme: [default, custom.scss]
    slide-number: true
    show-slide-number: all
    chalkboard: false
    logo: "../../uploads/recommendation-social-media.png"
    footer: "CP4285 · Week N · NUS School of Computing"
    self-contained: true
    transition: slide
    highlight-style: github
    code-line-numbers: true
    smaller: false
    scrollable: false
---
```

Key rules:
- `self-contained: true` — produces a single portable HTML file.
- `logo` path is always relative: `../../uploads/recommendation-social-media.png`.
- Footer format: `CP4285 · Week N · NUS School of Computing`.
- Never enable `chalkboard`.

---

## Colour Palette

| Role | Hex | Usage |
|---|---|---|
| NUS Navy | `#003D7C` | H1/H2 headings, table headers |
| NUS Orange | `#EF7C00` | Section title backgrounds, H3, links, accents |
| Mid-grey | `#6b7280` | Footer text |
| Orange tint | `rgba(239,124,0,0.07)` | Blockquote background |

These are NUS brand colours. **Do not substitute** other colours.

---

## Typography

- **Body font:** Arial, Helvetica, sans-serif
- **Heading font:** Arial, Helvetica, sans-serif (same family)
- Heading colour: `#003D7C` (navy)
- H3 colour: `#EF7C00` (orang- H3 colour: `#EF7C00` (orang- H3 colour: `#EF7C00` (orom border

---

## SCSS Theme

Copy `templates/custom.scss` verbatim into each new `static/slides/weekNN/` directory alongside the `.qmd` file. Do not modify it unless a deliberate style change is intended for the whole course.

---

## Slide Structure Conventions

### Section Title Slides (H1)

Every major section opens with a full-bleed orange title slide:

```markdown
# NN Section Title {background-color="#EF7C00"}
```

Section numbers are zero-padded two-digit integers (e.g. `01`, `02`).

### Content Slides (H2)

Regular slides use H2 headings.

### Horizontal Rule Separators

Use `---` (bare horizontal rule) to separate major sections before the H1 title slide.

### Speaker Notes

Every slide should have a speaker notes block, even if empty or a TODO:

```markdown
::: notes
<!-- TODO (students): ... -->
:::
```

---

## Content Patterns

### Two-Column Layout

```markdown
::: {.columns}
::: {.column width="50%"}
Left content
:::
::: {.column width="50%"}
Right content
:::
:::
```

### Incremental Bullet Lists

```markdown
::: {.incremental}
- Point one
- Point two
:::
```

### Callout Boxes

- `.callout-warning` — ethical issues, caveats, risks
- `.callout-note` — supplementary information, reminders

### Tables

Use Markdown pipe tables. Comparison tables use ✓ / ✗ for boolean values with `:---:` centre-alignment.

### Ethics Thread Convention

Each week includes at least one slide titled **"Ethics Thread: \<Topic\>"** using `.callout-warning` for the key concern.

### Summary Slide Convention

Final slide of each deck: titled **"Summary"**, contains a comparison table and a bold **"Next week:"** teaser.

---

## Classroom PDF and RevealJS Review

The slides are exported to **PDF for in-class markup**, so the PDF is a primary classroom artifact. Every slide must remain legible and useful as a static page for students annotating during the lecture:

- use readable font sizes, strong contrast, generous spacing, and tables/code that do not become illegible when exported or printed;
- keep essential definitions, labels, context, and conclusions visible without requiring an animation step;
- verify that the exported PDF has no clipped content, overflow, broken links, missing fonts, or content hidden by a fragment; and
- inspect representative PDF pages at their intended viewing/printing size before delivery.

RevealJS fragments, incremental lists, and other animation features are primarily for **self-paced review** and optional pacing during the live lecture. They must not be the only way a student can access information needed to understand or annotate a slide. When fragments are used, ensure the PDF export contains the complete intended content or provide an equivalent static presentation of that content.

---

## File Layout per Week

```
static/slides/weekNN/
├── weekNN.qmd       ← Quarto source (author this)
├── weekNN.html      ← Rendered output (committed to repo)
├── weekNN-timeline.md ← Lecture delivery timeline (keep synced with weekNN.qmd)
└── custom.scss      ← Copy of templates/custom.scss
```

Always commit both `.qmd` source and rendered `.html`.

### Lecture Delivery Timeline

Each week’s `weekNN-timeline.md` is a delivery companion to the slide deck, not a separate source of slide content. It **must be updated whenever the `.qmd` changes** so that it remains synced with the most current version of the slides. Before considering a deck update complete:

- verify that every current section and slide appears in the timeline, with renamed or removed slides removed from the timeline;
- update the timing and delivery mode when slide content or sequencing changes; and
- verify that the individual slide times still add up to the stated lecture duration.

Treat `weekNN.qmd` as the source of truth for slide order and titles. Do not modify the slides merely to make the timeline fit; revise the timeline to reflect the current deck.

### In-Class Activity Delivery Mode

The lecture timeline may assign a slide the **In-class activity** delivery mode. Every in-class activity must use one of these two formats:

1. **Multiple-choice or response question:** Ask students to complete a quiz-style multiple-choice question or a short-response question. Collect or sample their answers, then go over the correct answer and the reasoning immediately in class. Address why plausible alternatives are wrong and resolve misconceptions before continuing.
2. **Small-group discussion:** Put students into small groups for a few minutes to discuss a prompt and formulate an answer. Set a clear time limit and reporting expectation, then call on groups to share their answers. Synthesize the responses, correct inaccuracies, and connect the discussion back to the slide’s learning objective.

For either format, state the task and expected output before starting, timebox the activity, and reserve time for the instructor’s immediate synthesis. Record the activity type in the lecture-delivery timeline so another instructor can run it without guessing which format is intended.

---

## Rendering

```bash
cd static/slides/weekNN
quarto render weekNN.qmd
```

### Post-Change PDF Preview

Whenever any slide source (`weekNN.qmd`) or slide styling (`custom.scss`) is modified:

1. Run the deck’s PDF export workflow to generate a fresh PDF from the current slides.
2. Open the PDF preview and navigate directly to every affected slide, including adjacent slides when a shared layout or style change could shift content.
3. Check the affected pages for legibility, clipping, overflow, missing content, and static completeness for classroom markup.
4. If the change affects a shared template or theme, inspect representative examples of every affected layout before delivery.

The PDF preview is a required visual check after slide changes; an HTML render alone is not sufficient.
