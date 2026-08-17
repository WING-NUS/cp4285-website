---
name: cp4285-slides
description: Style guide and authoring conventions for CP4285 Quarto RevealJS slide decks. Use when creating, editing, or extending any weekly lecture slide deck for the CP4285 course. Covers YAML front matter, colour palette, typography, SCSS theme, structural patterns, and content conventions extracted from the w01 reference deck.
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

### Title Slide: QR Access Panel

Treat `static/slides/w01/w01.qmd` and `static/slides/w01/w01-custom.scss` as the **canonical CP4285 title-slide reference**. Preserve the standard RevealJS title treatment: white field, default dark course title, orange rule, and left-aligned subtitle, instruction team, and date. Let the default title sizing and wrapping respond naturally to the lecture title; a short title may occupy one line.

Do **not** add a course/week eyebrow, title-card gradient, bespoke title font size, title width cap, or title-specific colour override. Do **not** create an `include-in-header` title-style file: keep all title-panel CSS in the deck’s `custom.scss` theme.

When a published deck has a course shortlink, make the QR code a prominent, clickable **right-hand title-slide panel**. Keep the lecture title, subtitle, instruction team, and date left aligned on the remaining space. Do not use a small inline QR code beneath the subtitle.

Create and verify the shortlink before creating its QR code. Use the `manage-socn-links` skill for soc-n.us operations. Generate both SVG and PNG QR assets locally in `static/uploads/`: use SVG as the preferred source and PNG as the fallback. Put the exact, verified shortlink in the panel label. The whole panel must link to the shortlink in a new tab.

Place the following metadata in the deck YAML, substituting the verified URL and asset filenames:

```yaml
subtitle: |
  <span class="wNN-title-subtitle">CP4285 Modern Recommendation Systems — Week N</span>
  <a class="wNN-title-qr" href="https://soc-n.us/cp4285-tNN-wNN" target="_blank" rel="noopener" aria-label="Open the Week N slide deck">
    <picture>
      <source type="image/svg+xml" srcset="../../uploads/cp4285-tNN-wNN-HASH.svg">
      <img class="wNN-title-qr-image" src="../../uploads/cp4285-tNN-wNN-HASH.png" alt="QR code for the Week N slide deck">
    </picture>
    <span class="wNN-title-qr-label">Scan for the slides<br><span>soc-n.us/cp4285-tNN-wNN</span></span>
  </a>
```

Add matching theme CSS, changing `wNN` to the week identifier. Keep the panel at least 205 px square on the 1600×900 canvas, with a white background, teal (`#00796B`) border, navy (`#003D7C`) label, and teal shortlink. The title, subtitle, author, and date must all be left aligned.

```scss
.reveal #title-slide {
  box-sizing: border-box;
  padding-right: 340px;
  text-align: left;
}
.reveal #title-slide .title,
.reveal #title-slide .subtitle,
.reveal #title-slide .quarto-title-authors,
.reveal #title-slide .date {
  max-width: 100%;
}
.reveal #title-slide .quarto-title-authors,
.reveal #title-slide .quarto-title-author {
  justify-content: flex-start;
  margin-left: 0;
  margin-right: 0;
  text-align: left;
}
.reveal #title-slide .wNN-title-subtitle { display: block; }
.reveal #title-slide .wNN-title-qr {
  position: absolute;
  top: 50%; right: 1.5em;
  width: 255px;
  transform: translateY(-50%);
  box-sizing: border-box;
  display: block;
  padding: 16px 16px 14px;
  border: 4px solid #00796B;
  border-radius: 12px;
  background: #fff;
  color: #003D7C;
  text-align: center;
  text-decoration: none;
}
.reveal #title-slide .wNN-title-qr-image {
  display: block;
  width: 205px; height: 205px;
  margin: 0 auto 9px;
}
```

**RevealJS guardrail:** Never set `position: relative`, `display`, `top`, `left`, or a transform on `#title-slide` itself. Reveal positions title and content slides; overriding its positioning can place every later slide in normal document flow and cause navigation to land far below the viewport. Scope absolute positioning only to `.wNN-title-qr`.

After changing the title panel, render the deck and compare Slide 1 against the Week 01 reference. Verify the standard dark title, orange rule, left-aligned metadata, QR clearance, and compact QR label. Then navigate from Slide 1 to Slide 2 in the browser and verify that the next slide begins at the normal top position, not below the viewport.

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

## Mathematical Notation

Use Quarto's MathJax display math for every non-trivial equation. Write display equations with `$$ ... $$`, not hand-built HTML fractions or `\[ ... \]`, so they retain correct typesetting in the rendered RevealJS deck.

```markdown
$$
\operatorname{Sim}(u,v)=
\frac{\sum_{\color{orange}{k\in I_u\cap I_v}} \color{teal}{r_{uk}r_{vk}}}
{\color{navy}{\sqrt{\sum_{k\in I_u\cap I_v}r_{uk}^{2}}\;\sqrt{\sum_{k\in I_u\cap I_v}r_{vk}^{2}}}}
$$
```

When teaching an equation, colour-code the meaningful components in the MathJax expression and immediately provide a plain-language key in the same colours. Use the supported named TeX colours `orange`, `teal`, and `navy` inside `\color{...}{...}`; do not use hexadecimal values in MathJax colour commands. Explain what each coloured quantity represents and why it matters, rather than narrating symbols mechanically. Keep the notation and the colour key together on the same slide, and visually inspect the rendered slide after changes.

For multiword function identifiers in equations, prefer lowercase dashed notation over camel case: write `\operatorname{raw\text{-}cosine}(u,v)`, not `RawCosine(u,v)`.

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

### YouTube Video Embed Slide Prototype

Use this prototype when a lecture needs a dedicated video surface. The slide title must begin with the video-camera emoji and the slide must use a black background:

````markdown
## 🎥 Video: <short title> {background-color="#000000"}

```{=html}
<div style="display:flex;align-items:center;justify-content:center;width:100%;height:76vh;background:#000;">
  <a href="https://www.youtube.com/watch?v=VIDEO_ID" target="_blank" rel="noopener" aria-label="Open video: <short title>">
    <img src="https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg" alt="YouTube thumbnail for <short title>" style="display:block;width:100%;max-width:1280px;height:auto;max-height:76vh;object-fit:contain;border:4px solid #EF7C00;">
  </a>
</div>
```
````

Replace `VIDEO_ID` and the title/alt text with the selected video. Use the thumbnail as the visible preview rather than relying on an autoplaying iframe; clicking it opens the YouTube watch page in a new tab. Keep the thumbnail large enough for projection, preserve its 16:9 aspect ratio, and verify that it loads before delivery. Add the video URL and thumbnail source to the slide’s speaker notes `[Sources]` block.

### Card-Suit User-Type Framework

Use the following four user types when discussing how a recommendation system should treat different users. These are treatment lenses, not demographic or permanent personality labels; the same person may occupy different types across tasks or sessions.

| Suit | User type | Treatment lens |
|---|---|---|
| **♣ Clubs** | **Adversarial / Shill user** | Attempts to manipulate the system into recommending or avoiding specific items or users. Consider coordinated behaviour, fake signals, robustness, abuse detection, and incentive-aware safeguards. |
| **♥ Hearts** | **Social user** | Responds strongly to social signals. Consider friends, communities, social similarity, shared taste, influence, and the risks of conformity or social exposure. |
| **♦ Diamonds** | **Novelty seeker** | Is governed by novelty and wants new objects, trends, and emerging items. Consider exploration, diversity, freshness, serendipity, and cold-start exposure for new items. |
| **♠ Spades** | **Loyalist / metadata-driven user** | Relies on particular metadata factors and stable preferences. Consider content features, attribute matching, consistency, explainable filters, and avoiding unnecessary drift. |

The suits should be kept meaningfully different in terms of recommendation treatment: Clubs stress adversarial robustness, Hearts social similarity, Diamonds novelty and diversity, and Spades metadata-based continuity.

#### Per-topic inclusion prompt

When creating slides for any lecture topic or major concept, prompt the user before drafting the topic-specific treatment:

> For **[topic]**, should the slides include considerations for any of these user types: **♣ Clubs (adversarial/shill), ♥ Hearts (social), ♦ Diamonds (novelty), or ♠ Spades (loyalist/metadata-driven)**? Select any that are relevant, or choose “none”.

Use the selected types to add a concrete example, design trade-off, evaluation consideration, ethical question, or activity prompt. Do not force all four types into every topic, and do not silently choose on the user's behalf when the inclusion would materially change the topic's emphasis. If the user selects “none”, proceed without a suit-specific treatment.

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

### To Think About Callout

Use a titled Quarto callout, rather than a raw HTML block, for a short reflective question. It follows the warning/note callout convention while using the deck's teal `to-think-about` visual treatment. Keep it to one concise question and place it only where there is sufficient vertical space.

```markdown
::: {.callout-tip .to-think-about title="To think about"}
Does top-*k* apply to users as well as items?
:::
```

Quarto places the custom class on a wrapper around the generated callout. Define `.to-think-about .callout`, `.callout-body`, `.callout-title`, `.callout-title-container`, and `.callout-content` styles in the week theme. Match the standard callout convention: use a teal title band and a white content area, with the same dark neutral text (`#333333`) used by Warning and Note callouts; reset paragraph margins and `min-height` so the callout has no surplus vertical space. Hide the default tip icon and use `.to-think-about .callout-icon-container::before { content: "🤔"; }`; make the title a flex row with a `0.35em` gap so the thinker and title have one clear space. Do not recreate the callout shell with an inline `<div>`.

### Tables

Use Markdown pipe tables. Comparison tables use ✓ / ✗ for boolean values with `:---:` centre-alignment.

### Ethics Thread Convention

Each week includes at least one slide titled **"Ethics Thread: \<Topic\>"** using `.callout-warning` for the key concern.

### Ethics-Focused AI Voice Mode Slides

When AI Voice Mode is used to investigate recommender ethics, prefix the slide title with the Wi-Fi/signal emoji: **`📶 AI Voice Mode`**. Keep the experiment’s purpose explicit: students are examining assumptions, uncertainty, omissions, and ethical reasoning in an AI-mediated conversation. The emoji is a visual cue for the live voice interaction; it does not imply that the agent is authoritative or connected to a production recommender.

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

- A countdown timer is optional. Before designing an activity slide, ask the user: **“Should this activity use the default three-minute countdown timer?”** If they decline, omit the timer and record the untimed timebox in the timeline. If they choose a timer, use their specified duration or the three-minute default and configure it in the slide.
- For timer-enabled activities, use a small countdown timer occupying approximately one quarter of the slide area, using the same MM:SS SVG donut-bar pattern as the break slide.
- Use a shared NUS Navy slide background (`#003D7C`) with white body text and NUS Orange (`#EF7C00`) for the frame and emphasis; apply the timer treatment when one is enabled.
- Surround the activity content with a responsive medium-weight, high-contrast frame: use `border: clamp(3px, 0.6vw, 6px) solid #EF7C00` so it remains visible without becoming oversized on smaller screens.
- Put the format emoji in the slide title: **`🎰 Bandit Time: <short question>`** for multiple-choice/response questions and **`👥 <short activity title>`** for small-group discussion.
- Do not add a reverse-contrast “In Lecture …” label box inside the frame. The title prefix is the activity-format cue; keep the frame for the prompt, response content, and timer when present.
- Set foreground colours explicitly on every nested element; do not rely on inherited white text. White answer cards must set a dark text colour (for example, `color:#003D7C`), and prompts/controls on the navy background must set `color:#fff`.
- For timer-enabled slides, make the timer self-contained and visible on navy slides: give the donut a visible stroke, place an opaque white centre circle behind the MM:SS text, set the timer text to navy (`#003D7C`), and keep the orange start/pause control visible. Never use `display:none`, transparent text, or a transparent timer centre for the classroom/PDF version.

Keep the frame, title, prompt, and any timer legible in the classroom PDF; a timer should support pacing without crowding out the activity prompt or response space.

#### MCQ / Bandit Time Slide Treatment

For every multiple-choice quiz, use the visible slide-title pattern **`🎰 Bandit Time: <short question>`**. The slot-machine emoji must be the first visible token; do not add a separate in-frame quiz label or a generic `MCQ:` heading. The navy background and orange frame are shared with `👥` activity slides.

Render the answer choices as readable cards rather than a plain bullet list. Use a responsive two-column card grid for four choices (additional choices may continue on subsequent rows), with a clearly visible letter/number and the full answer text in every card. Give each option a different primary-colour outline; use this default accessible palette unless the user specifies another:

- A — red `#D32F2F`
- B — blue `#1976D2`
- C — green `#388E3C`
- D — purple `#7B1FA2`

Use a medium-weight outline (for example, `border: 4px solid <option-colour>`), a light/neutral card fill, explicit dark card text (for example, `color:#003D7C`), and enough padding for projection. Maintain strong text contrast and include the letter/number label so meaning never depends on colour alone. Keep the cards static and printable; do not hide choices behind animation or interaction. Add a countdown timer only when the user has opted in under the activity treatment above.

Example structure:

```markdown
## 🎰 Bandit Time: Which signal should rank this item first?

<div class="bandit-options">
  <div class="bandit-option" style="border-color:#D32F2F"><strong>A.</strong> ...</div>
  <div class="bandit-option" style="border-color:#1976D2"><strong>B.</strong> ...</div>
  <div class="bandit-option" style="border-color:#388E3C"><strong>C.</strong> ...</div>
  <div class="bandit-option" style="border-color:#7B1FA2"><strong>D.</strong> ...</div>
</div>
```

### Countdown Timer Expiration Cue

Every countdown timer (break slides and in-lecture activity slides) must use the same shared timer state machine: **Start → Pause → Resume → Expire → Restart**. Pressing the timer button while counting down pauses it; pressing again resumes it. When it reaches `00:00`, it must play one audible ring for **0.5 seconds**, turn the donut ring green (`#00c875`), show a completion status, and expose a **Restart** action that resets the display and ring to the initial state without starting until pressed again. Start the audio from the user-initiated timer interaction so browser autoplay policies do not suppress it. Reuse one `AudioContext` per slide and call the cue exactly once per expiry.

Use a short, non-startling oscillator envelope (for example, a sine tone around 880 Hz with a quick gain fade) and keep the text/status change available for students who cannot hear the audio.

Implement this behavior through one reusable `createCountdownTimer` factory (or an equivalent shared helper) copied into every timer slide; do not maintain separate break/activity timer logic.

**Auto-pause on slide exit is mandatory.** Every timer must register itself in the global `window._cpTimers` registry using its `slideIndex` (0-based index of its parent `<section>`). A single `Reveal.on("slidechanged", ...)` listener — injected once in `include-in-header` after the `</style>` tag — fires on every slide transition and calls the pause function for the departing slide if a timer is running. The timer must pause silently at its current value and switch its button label to **▶ Resume**. See the **Timer Auto-Pause on Slide Exit** section for the full implementation pattern.

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
| 🎰 Bandit Time | `cp-frame-orange` | `#EF7C00` | — (no label box) | `#003D7C` |
| 👥 In Lecture Activity | `cp-frame-orange` | `#EF7C00` | — (no label box) | `#003D7C` |
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

## Previous Week 4-Concept Recap Slide (Quarto Reveal)

### Purpose and Placement

Use this screenshot-based recap after the Previous Week Exercise Review and before new material. Use the original slides that introduced four consequential concepts from Week N–1 to reactivate the conceptual sequence students need for the current lecture.

### Why Use One Unified Graphic

Build the four thumbnails into **one 16:9 recap composite** before inserting it into Quarto. Do not embed four separate image elements in the slide. A single composite prevents visual seams, inconsistent scaling, stale per-image references, and partial replacement errors when one source thumbnail changes.

### Prepare the Recap Asset

1. Select four **non-overlapping**, technically central source slides in reading order: representation or premise; goal or decision; method choice or trade-off; and procedure, limitation, or bridge to the current lecture.
2. Capture each source slide at 16:9 without cropping, browser controls, or presenter overlays.
3. Build the unified graphic with the reusable builder. The command below retains complete source slides and gives every quadrant a 1px purple outline (`#5C2D91`):

   ```bash
   python skills/cp4285-slides/scripts/build_recap_composite.py \
     static/slides/weekNN/assets/recap/week-n-minus-1-four-concept-recap.png \
     static/slides/weekNN/assets/recap/01.png \
     static/slides/weekNN/assets/recap/02.png \
     static/slides/weekNN/assets/recap/03.png \
     static/slides/weekNN/assets/recap/04.png
   ```

4. Use descriptive `alt` text that names the four source concepts, not merely the week number.
5. For Week 01, use: **The User–Item Matrix → From a Score to a Useful List → Similarity I: Pearson Correlation → From Neighbours to a Prediction**.

### Quarto Source Template

Copy `templates/previous-week-recap.qmd` into the destination lecture’s `.qmd` source. Replace the standard all-caps label and the single composite-image path. This is Quarto Reveal syntax, not standalone Markdown or HTML. The template includes the required speaker-notes block.

### Styling Rules

- Use a dark-purple background (`#1a0a2e`) and a purple frame (`#5C2D91`).
- Use the standard `.cp-frame-label` as one compact, boxed, all-caps label, for example **"WEEK 01 RECAP"**. Do not add the prior lecture title or a secondary title such as "Four things to carry into today".
- Preserve the composite’s zero-gap 2×2 layout and 1px purple quadrant outlines. Do not recreate outlines with four separate HTML image boxes.
- Do not overlay explanatory text, icons, tables, or animations on the composite. Use speaker notes to supply the recall prompt and bridge to the current lecture.
- Use `.cp-thumbnail-recap-content`, `.cp-thumbnail-composite-wrap`, and `.cp-thumbnail-composite` from `templates/custom.scss`. Copy the full stylesheet into a new deck’s local `custom.scss`.

---

## Last Week Pre-Lecture Exercise: Canvas Voices

Use this recap when a prior Canvas pre-lecture discussion should become evidence for the current lecture. Place it in an empty **Last Week Pre-Lecture Exercise** navy frame after the exercise prompt and before the new technical content.

### Select Evidence

1. Expand the complete Canvas discussion thread before selecting material.
2. Select three or four primary student contributions that illustrate distinct, instructionally useful latent dimensions or reasoning moves.
3. Add a direct reply only when a real follow-up response exists and extends the same theme, such as subjectivity, measurement, segmentation, variability, or a counterexample.
4. Quote faithfully. Shorten only for fit with an ellipsis; do not rewrite student meaning or treat excerpts as quantitative evidence.

### Protect Student Privacy

- Omit names, initials, usernames, timestamps, and reply counts.
- Use a participant avatar only when the instructor explicitly requests it. Save it locally under `assets/canvas-avatars/`, use the alt text `Anonymous Canvas participant avatar`, and never include the identity-to-asset mapping in the deck.
- Label the slide as anonymised and state that quotations are shortened only for fit.

### Build the Frame

Copy `templates/last-week-canvas-voices.qmd` into the target deck. Use one `voice-bubble` per theme, with an avatar, a primary quotation, an optional `voice-reply`, and a terse theme label. Use a two-by-two `voice-bubble-grid` inside `.canvas-voices-frame`.

### Layout Rules

- Keep bubbles compact but spread them across the usable frame area with staggered vertical offsets.
- Position each avatar just outside the lower-left edge of its bubble. Aim the bubble tail toward the avatar so the text reads as emitted by that participant.
- Keep the primary quotation visually dominant. Render the actual follow-up reply as a smaller `Reply` line separated by a fine rule.
- Scope all additions below `.canvas-voices-frame` in the deck's local `custom.scss`. Append overrides; do not alter shared `.cp-frame-*` rules.
- Use course colours subtly to distinguish themes and preserve the navy frame treatment.

### Validate

Before delivery, confirm that every reply is thematically linked to the displayed quotation, names are absent, avatar files resolve locally, all bubbles fit in the frame, and `quarto render wNN.qmd` succeeds. Run `git diff --check` on the `.qmd` and `.scss` files.

---

## Timer Auto-Pause on Slide Exit

### Behaviour

When the presenter navigates away from a slide that contains a running timer, the timer **automatically pauses** at its current value. The button label switches to **▶ Resume**. The timer does not reset; it resumes from where it left off when the presenter returns to the slide and clicks Resume.

### Implementation

Two additions are required in every deck that uses timers:

**1. Global registry + Reveal listener** — add once in `include-in-header`, after the `</style>` tag:

```html
<script>
window._cpTimers = window._cpTimers || {};
document.addEventListener('DOMContentLoaded', function() {
  function tryBind() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady || !Reveal.isReady()) {
      setTimeout(tryBind, 200); return;
    }
    Reveal.on('slidechanged', function(e) {
      var prev = e.previousSlide;
      if (!prev) return;
      var all = Array.prototype.slice.call(
        document.querySelectorAll('.reveal .slides > section'));
      var idx = all.indexOf(prev);
      if (idx >= 0 && window._cpTimers[idx]) window._cpTimers[idx]();
    });
  }
  tryBind();
});
</script>
```

**2. `slideIndex` option in `createCountdownTimer`** — each timer factory must:
- Accept `o.slideIndex` (0-based index of the slide `<section>` that owns the timer)
- Register a pause function in `window._cpTimers[o.slideIndex]` immediately after the `audioContext=null` declaration:

```js
if (typeof o.slideIndex === 'number') {
  window._cpTimers = window._cpTimers || {};
  window._cpTimers[o.slideIndex] = function() {
    if (state === 'running') {
      clearInterval(interval); interval = null; state = 'paused';
      buttonEl.textContent = '▶ Resume';
    }
  };
}
```

**3. Pass `slideIndex` in the call:**

```js
createCountdownTimer({
  total: TOTAL,
  textId: 'timer-text-XXXX',
  statusId: 'timer-status-XXXX',
  ringId: 'donut-ring-XXXX',
  buttonId: 'break-btn-XXXX',
  slideIndex: N   // ← 0-based index of this slide's <section>
});
```

### Determining `slideIndex`

Count all top-level `<section>` elements in `.reveal .slides` (i.e., every `## ` or `# ` heading in the `.qmd`, plus the implicit title slide at index 0). The title slide is index 0; each subsequent `---`-separated slide increments the index by 1.
