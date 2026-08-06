---
name: cp4285-slides
description: Style guide and authoring conventions for CP4285 Quarto RevealJS slide decks. Use when creating, editing, or extending any weekly lecture slide deck for the CP4285 course. Covers YAML front matter, colour palette, typography, SCSS theme, structural patterns, and content conventions extracted from the week01 reference deck.
---

# CP4285 Slides — Authoring Guide

## Overview

All CP4285 slide decks are authored in **Quarto Markdown (`.qmd`)** and rendered as **RevealJS** presentations. Each deck lives under `static/slides/weekNN/` in the repo and ships with its own `custom.scss` theme file (see `templates/custom.scss`).

---

## Learning Outcomes Quick Reference

Use these outcomes when planning, reviewing, or revising a deck. The authoritative course pages are `content/_index.md` (course outcomes) and `content/docs/schedule.md` (session outcomes).

### Course Learning Outcomes

By the end of the course, students should be able to:

| CLO | Outcome |
|---|---|
| **CLO 1** | Explain and compare classical recommendation methods, including collaborative filtering, content-based filtering, and hybrid approaches. |
| **CLO 2** | Implement matrix factorization and neural recommendation models using modern deep learning frameworks. |
| **CLO 3** | Design and execute rigorous offline evaluation protocols using appropriate ranking metrics. |
| **CLO 4** | Analyse the cold-start problem and propose strategies to address it. |
| **CLO 5** | Critique recommender systems from fairness, privacy, transparency, and stakeholder impact perspectives. |
| **CLO 6** | Explain advanced recommendation architectures including sequential, graph-based, multi-objective, and LLM-enhanced systems. |
| **CLO 7** | Design and justify a complete recommendation system pipeline from problem formulation through evaluation and ethical analysis. |
| **CLO 8** | Communicate and defend recommendation-system designs and results to a technical audience. |

### Session Learning Outcomes

| Session | Outcomes |
|---|---|
| **Week 1 — Recommendation Problems and Classical Methods** | Formulate recommendation problems; differentiate recommendation paradigms; Analyze cold-start challenges; explain how recommendation objectives affect exposure. |
| **Week 2 — Latent Factor Models** | Explain latent-factor models; train embedding-based recommenders; compare prediction and ranking objectives; discuss risks of learning from historical behavior. |
| **Week 3 — Evaluation of Recommendation Systems** | Design evaluation protocols; compute ranking metrics; critique metric selection; explain limitations of offline evaluation. |
| **Week 4 — Neural Recommendation Models** | Build neural recommenders; compare neural and latent-factor approaches; Analyze explainability challenges; assess trade-offs between complexity and transparency. |
| **Week 5 — Sequential and Session-Based Recommendation** | Model temporal preferences; implement next-item prediction; compare static and dynamic representations; critically assess engagement-driven objectives. |
| **Week 6 — Retrieval and Ranking Architectures** | Explain industrial recommendation pipelines; design retrieval-ranking architectures; Analyze scalability trade-offs; evaluate how ranking affects different stakeholders. |
| **Week 7 — Project Design Critique Workshop** | Defend recommendation-system designs; critique evaluation strategies; identify ethical risks early; refine project scope based on feedback. |
| **Week 8 — Learning-to-Rank** | Formulate ranking objectives; compare ranking approaches; Analyze position bias; discuss fairness implications of ranking. |
| **Week 9 — Graph-Based Recommendation** | Represent recommendations as graph problems; explain graph propagation; build graph-based recommenders; Analyze risks of graph-driven feedback loops. |
| **Week 10 — Multi-Objective Recommendation** | Define non-accuracy objectives; measure diversity and novelty; design multi-objective recommenders; justify objective trade-offs. |
| **Week 11 — Exploration and Online Learning** | Explain exploration strategies; design adaptive recommendation policies; Analyze recommendation feedback loops; discuss ethical implications of experimentation. |
| **Week 12 — LLMs, Generative Recommendation, and Research Frontiers** | Explain modern recommendation research directions; evaluate LLM-based recommendation systems; critique emerging approaches; identify open research challenges. |
| **Week 13 — Final Project Presentations** | Present recommendation-system designs professionally; defend technical decisions; interpret evaluation results critically; integrate technical, product, and societal considerations. |

When slides are changed, offer to check their alignment with both the relevant CLOs and the specific session outcomes. An alignment check should map slide content and activities to outcomes, identify missing, weak, or redundant coverage, and suggest targeted revisions; do not silently modify the deck as part of the check.

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
- H3 colour: `#EF7C00` (orange)
- All H1/H2 headings have a `3px solid #EF7C00` bottom border

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

### Summary / Key Point Slide Type

Use a **Summary** or **Key Point** slide to consolidate a section, mark a memorable takeaway, or bridge to the next concept. These slides must be visually distinct from both orange section-title slides and regular body slides:

- Use the proposed contrastive scheme: NUS Navy `#003D7C` as the slide background, white body text, and NUS Orange `#EF7C00` for borders, labels, or emphasis.
- Always feature at least one of these visual anchors in the slide content: crossed fingers `🤞` or key `🔑` emojis. Use the emoji as a prominent cue, not as an incidental footer decoration.
- Keep the slide focused on one synthesis or takeaway. A Summary slide may retain the deck’s comparison table and **"Next week:"** teaser; a Key Point slide should use a short statement plus supporting evidence or implications.
- Visually emphasize the main takeaway text. Underline the key statement by default (for example, with `<u>...</u>`); a comparably strong treatment such as a highlighted label or accent rule is acceptable when underlining is unsuitable. Do not leave the slide’s central message as unstyled body text.
- Preserve the required speaker notes block and verify that the navy/white/orange treatment remains legible in the classroom PDF.

Example:

```markdown
# Key Point {background-color="#003D7C"}

## 🤞 <u>One takeaway</u>

Popularity is a useful baseline, but its feedback loop can change who receives exposure.
```

### Pre-Lecture Exercise Slide Types

Add these two framed slide types to create continuity between weekly sessions. They reuse the medium-weight, high-contrast frame convention from in-lecture activity slides, but each has its own frame treatment and exact label:

1. **Next Week Pre-Lecture Exercise** — place at the end of the current lecture’s teaching sequence (immediately before the final Summary slide when Summary must remain last). Give students a short prompt, reading check, or preparatory question for the following week. Use a medium NUS Navy frame (`#003D7C`) with an NUS Orange label reading **“Next Week Pre-Lecture Exercise”**.
2. **Previous Week Exercise Review** — place near the beginning of the current lecture, after opening context and before new material. Show the prior exercise prompt or a representative response, then guide a brief review of the expected reasoning. Use a medium NUS Orange frame (`#EF7C00`) with an NUS Navy label reading **“Previous Week Exercise Review”**.

For both types, keep the frame and label inside the slide area, make the exercise or review prompt the visual focus, and include enough space for students to annotate the PDF. Record the slide’s placement, time, delivery mode, and expected student response in the lecture-delivery timeline.

Use the responsive medium frame consistently for both types: `border: clamp(3px, 0.6vw, 6px) solid <contrast-colour>`. Keep the frame thickness proportional to the viewport so it remains visible on projected and printed/PDF versions without dominating the content.

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

Commit all per-week delivery artifacts together: the `.qmd` source, rendered `.html`, `custom.scss`, and `weekNN-timeline.md` when present. Keep the source, rendered output, styling, and delivery timeline synchronized in the same change.

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

#### Activity Slide Treatment

Both in-class activity types use the following visual treatment:

- Include a small countdown timer, occupying approximately one quarter of the slide area, using the same MM:SS SVG donut-bar pattern as the break slide.
- Before designing an activity slide, prompt the user for the intended timer length. Do not silently assume the break-slide default; record the chosen duration in the timeline and configure it in the slide.
- Surround the activity content with a responsive medium-weight, high-contrast frame: use `border: clamp(3px, 0.6vw, 6px) solid <contrast-colour>` so it remains visible without becoming oversized on smaller screens. Use a colour that contrasts with the slide background (NUS Orange `#EF7C00` is the default accent when appropriate).
- Put the exact label **“In Lecture Quiz”** inside the frame for multiple-choice or response questions.
- Put the exact label **“In Lecture Activity”** inside the frame for small-group discussion activities.

Keep the frame, label, prompt, and timer legible in the classroom PDF; the timer should support pacing without crowding out the activity prompt or response space.

### Countdown Timer Expiration Cue

Every countdown timer (break slides and in-lecture activity slides) must use the same shared timer state machine: **Start → Pause → Resume → Expire → Restart**. Pressing the timer button while counting down pauses it; pressing again resumes it. When it reaches `00:00`, it must play one audible ring for **0.5 seconds**, turn the donut ring green (`#00c875`), show a completion status, and expose a **Restart** action that resets the display and ring to the initial state without starting until pressed again. Start the audio from the user-initiated timer interaction so browser autoplay policies do not suppress it. Reuse one `AudioContext` per slide and call the cue exactly once per expiry.

Use a short, non-startling oscillator envelope (for example, a sine tone around 880 Hz with a quick gain fade) and keep the text/status change available for students who cannot hear the audio.

Implement this behavior through one reusable `createCountdownTimer` factory (or an equivalent shared helper) copied into every timer slide; do not maintain separate break/activity timer logic.

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

---

## Break Slides

### When to Use

Insert a break slide whenever a mid-lecture break is planned (typically once per 120-minute session). Place it between two `---` separators so it forms its own slide.

### Design

| Property | Value |
|---|---|
| Layout | Two-column split: a fun fact, short story, anecdote, or image on the left; timer panel on the right |
| Background | `#000000` (black) |
| Text colour | White (`#ffffff`) |
| Accent colour | NUS Orange `#EF7C00` (donut ring, item highlights, button) |
| Timer default | 5 minutes (configurable per slide) |
| Timer controls | Manual — **▶ Start Timer**, **⏸ Pause**, **▶ Resume**, then **↻ Restart** after expiry |
| Timer display | MM:SS countdown centred inside an SVG donut ring |
| Ring behaviour | Drains clockwise; turns green (`#00c875`) when time is up |

### Template

The complete reusable snippet is in `templates/break-slide.qmd`. Copy it verbatim into the deck at the break point, then:

1. **Replace every occurrence of `BREAKID`** with a short unique identifier (e.g. `wk1b1`) so that multiple break slides in the same HTML file do not share DOM IDs.
2. **Replace the placeholder** inside the `<!-- TODO: insert a fun fact, short story, anecdote, or image ... -->` block with a subject-relevant item for that week (see guidance below).
3. **Adjust `TOTAL`** in the `<script>` block if a duration other than 5 minutes is needed (e.g. `var TOTAL = 10 * 60;`).

### Fun Fact / Short Story / Anecdote / Image Guidelines

The **left-hand pane** must contain one fun fact, short story, anecdote, or image for the week. The **right-hand pane** is reserved for the timer and its controls. The item must be visible without starting the timer.

The fun fact, short story, anecdote, or image caption must be:
- **Directly relevant** to the week's lecture topic or a concept covered that day.
- **Concise** — two to four sentences maximum.
- **Engaging** — a surprising statistic, a historical origin story, or a real-world consequence of the topic.
- Written in the second person or impersonal voice ("Did you know…", "The first…", "In 2006…").
- Key terms or names highlighted with `<strong style="color:#EF7C00">…</strong>`.

When authoring a break slide for a specific week, select the fun fact, short story, anecdote, or image from the week's session learning outcomes and slide content. Replace the generic placeholder before publishing; do not leave placeholder text in the delivered slide.

### Placement in the Deck

```markdown
---

[copy templates/break-slide.qmd here; it already includes its own slide heading]

---

## Next Slide After Break
```

### Placement in the Timeline

Add a row to the lecture delivery timeline for the break slide:

| Slide | Time | Mode | Delivery plan |
|---|---:|---|---|
| `Break` | 5 min | — | Click **▶ Start Timer** when announcing the break; **⏸ Pause**/**▶ Resume** as needed; click **↻ Restart Timer** after expiry to reset. Students return when the ring completes. |

The break duration counts against the total lecture time; adjust adjacent slide timings accordingly.

---

## Frame System

All framed slides use a **fixed-size background frame** implemented as a `position:absolute` element, independent of content. This ensures consistent, thick borders at every viewport size and in PDF thumbnails.

### Frame Dimensions (1600×900 canvas)

| Property | Value |
|---|---|
| Slide canvas | 1600 × 900 px |
| Frame inset | 40 px on all sides |
| Frame outer rect | 1520 × 820 px |
| Frame border thickness | **20 px** solid |
| Frame border radius | 8 px |
| Content layer inset | matches frame (40 px all sides) |
| Content padding | 32 px top, 36 px sides, 28 px bottom |

### Required CSS Classes

Include the following CSS in the deck's `include-in-header` block (or in `custom.scss`). Do not inline these styles per-slide.

```css
.cp-frame-bg {
  position: absolute;
  inset: 40px;
  border-width: 20px;
  border-style: solid;
  border-radius: 8px;
  pointer-events: none;
  z-index: 0;
}
.cp-frame-content {
  position: absolute;
  inset: 40px;
  padding: 32px 36px 28px 36px;
  box-sizing: border-box;
  overflow-y: auto;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  font-family: Arial, Helvetica, sans-serif;
}
.cp-frame-label {
  display: inline-block;
  font-weight: bold;
  font-size: 0.7em;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  padding: 0.28em 0.9em;
  border-radius: 4px;
  margin-bottom: 0.9em;
  align-self: flex-start;
  flex-shrink: 0;
}
.cp-frame-title  { font-size: 1.25em; font-weight: bold; margin-bottom: 0.55em; flex-shrink: 0; }
.cp-frame-body   { font-size: 0.92em; line-height: 1.6; }
/* Colour variants */
.cp-frame-orange { border-color: #EF7C00; }
.cp-frame-navy   { border-color: #003D7C; }
.cp-frame-teal   { border-color: #00796B; }
.cp-frame-purple { border-color: #5C2D91; }
```

### Framed Slide Markup Pattern

```markdown
## {background-color="#ffffff"}

```{=html}
<div class="cp-frame-bg cp-frame-COLOUR"></div>
<div class="cp-frame-content">
  <div class="cp-frame-label" style="background:COLOUR;color:LABEL_TEXT;">LABEL</div>
  <div class="cp-frame-title" style="color:TITLE_COLOUR;">Title</div>
  <div class="cp-frame-body" style="color:#333;">Body content</div>
</div>
```
```

### Colour Variants by Slide Type

| Slide Type | Frame class | Label bg | Label text | Slide bg |
|---|---|---|---|---|
| Previous Week Exercise Review | `cp-frame-orange` | `#EF7C00` | `#003D7C` | `#ffffff` |
| Next Week Pre-Lecture Exercise | `cp-frame-navy` | `#003D7C` | `#EF7C00` | `#ffffff` |
| In Lecture Quiz | `cp-frame-orange` | `#EF7C00` | `white` | `#ffffff` |
| In Lecture Activity | `cp-frame-navy` | `#003D7C` | `white` | `#ffffff` |
| **Next Week Preview** | `cp-frame-teal` | `#00796B` | `white` | `#002a26` |
| **Previous Week 4-Summary** | `cp-frame-purple` | `#5C2D91` | `white` | `#1a0a2e` |

---

## Next Week Preview Slide

### Purpose

Placed at the end of the current lecture (after the Summary slide) to give students a conceptual hook for the following week before they encounter the formal material.

### Design

- Teal frame (`#00796B`), dark teal background (`#002a26`), white text
- Label: **"Next Week Preview — Week N"**
- Title: the next week's lecture title in light teal (`#80cbc4`)
- Body: 3–5 bullet points covering the key ideas coming up, plus an optional italic reminder of the pre-lecture exercise

### Markup

```markdown
## {background-color="#002a26"}

```{=html}
<div class="cp-frame-bg cp-frame-teal"></div>
<div class="cp-frame-content" style="color:white;">
  <div class="cp-frame-label" style="background:#00796B;color:white;">Next Week Preview — Week N</div>
  <div class="cp-frame-title" style="color:#80cbc4;">Lecture Title</div>
  <div class="cp-frame-body" style="color:#cce8e5;">
    [2–3 sentence framing of the conceptual shift]
    <ul style="margin-top:0.5em;line-height:1.7;">
      <li><strong>Key idea 1</strong> — one sentence</li>
      <li><strong>Key idea 2</strong> — one sentence</li>
      <li><strong>Key idea 3</strong> — one sentence</li>
    </ul>
    <em style="color:#aaa;font-size:0.88em;">Pre-lecture exercise reminder (optional)</em>
  </div>
</div>
```
```

---

## Previous Week 4-Summary Slide

### Purpose

Placed at the start of the current lecture (after the Previous Week Exercise Review, before new material) to anchor recall of the four most important concepts from the prior week.

### Design

- Purple frame (`#5C2D91`), dark purple background (`#1a0a2e`), white text
- Label: **"Previous Week Summary — Week N–1 [Topic]"**
- Title: "Four things to carry into today" (or equivalent)
- Body: a 2×2 grid of four cells, each with a numbered heading in NUS Orange and 2–4 lines of white body text

### Four-Quadrant Grid CSS

```css
.cp-quad-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 16px;
  flex: 1;
  min-height: 0;
}
.cp-quad-cell {
  background: rgba(255,255,255,0.07);
  border-radius: 5px;
  padding: 14px 16px;
  overflow: hidden;
}
.cp-quad-cell h4 { margin: 0 0 6px 0; font-size: 0.88em; font-weight: bold; color: #EF7C00; }
.cp-quad-cell p, .cp-quad-cell ul { margin: 0; font-size: 0.8em; line-height: 1.45; color: #e0e0e0; }
.cp-quad-cell ul { padding-left: 1.1em; }
```

### Markup

```markdown
## {background-color="#1a0a2e"}

```{=html}
<div class="cp-frame-bg cp-frame-purple"></div>
<div class="cp-frame-content" style="color:white;">
  <div class="cp-frame-label" style="background:#5C2D91;color:white;">Previous Week Summary — Week N [Topic]</div>
  <div class="cp-frame-title" style="color:#e0c8ff;">Four things to carry into today</div>
  <div class="cp-quad-grid">
    <div class="cp-quad-cell"><h4>① Concept one</h4><p>One or two sentences.</p></div>
    <div class="cp-quad-cell"><h4>② Concept two</h4><ul><li>Point</li><li>Point</li></ul></div>
    <div class="cp-quad-cell"><h4>③ Concept three</h4><ul><li>Point</li><li>Point</li></ul></div>
    <div class="cp-quad-cell"><h4>④ Concept four</h4><p>One or two sentences.</p></div>
  </div>
</div>
```
```
