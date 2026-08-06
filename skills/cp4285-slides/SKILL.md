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

## File Layout per Week

```
static/slides/weekNN/
├── weekNN.qmd       ← Quarto source (author this)
├── weekNN.html      ← Rendered output (committed to repo)
└── custom.scss      ← Copy of templates/custom.scss
```

Always commit both `.qmd` source and rendered `.html`.

---

## Rendering

```bash
cd static/slides/weekNN
quarto render weekNN.qmd
```
