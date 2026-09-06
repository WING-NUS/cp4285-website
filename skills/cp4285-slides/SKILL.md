---
name: cp4285-slides
description: Create, edit, render, and review CP4285 Quarto RevealJS lecture decks. Use for any work in static/slides/wNN, including shared CP4285 primitives, title QR panels, frames, activities, MCQs, countdown timers, and lecture-delivery timelines.
---

# CP4285 Slide Authoring

## Source of truth

Start with `cp4285-common.scss`; then consult the resource for the component being created or changed. Do not recreate an existing visual rule from memory.

| Resource | Use it for |
|---|---|
| `static/slides/cp4285-common.scss` | Course-wide tokens and all reusable primitives. |
| `static/slides/cp-timer.html` | Shared, data-driven countdown controller. |
| `static/slides/w01/w01.qmd` | Reference for course pacing, title treatment, and activity use. |
| `static/slides/w02/w02.qmd` | Reference for metrics, chips, flow cards, and factorisation MCQ. |
| `templates/prototype-deck.qmd` | Copyable visual reference for every standard slide and activity prototype. |
| `templates/custom.scss` | The only permitted starting point for a week-specific overlay. |
| `templates/break-slide.qmd` | Shared-controller break-slide prototype. |

> Reuse semantic classes from `cp4285-common.scss`. Keep an inline `style` only for a **singular content composition** that does not recur across the course.

## New deck workflow

1. Create `static/slides/wNN/` and copy `templates/prototype-deck.qmd` to `wNN.qmd`.
2. Copy `templates/custom.scss` to `wNN-custom.scss` without adding course-wide rules.
3. Replace all `TODO` values, including the title, date, QR assets, links, and timer identifiers.
4. Retain or remove prototype slides deliberately. Do not ship instructional placeholder text.
5. Render with `quarto render wNN.qmd` and inspect every affected slide in a browser at the 1600×900 canvas.
6. Keep `wNN-timeline.md` synchronized with slide order, timings, and activity delivery mode.
7. Keep the `.qmd`, rendered `.html`, generated `wNN_files/` directory, overlay, timeline, and any changed shared asset synchronized. When the work is committed, include them together.

### Commit attribution

When committing work produced through an agent, use `<Agent> (via Min): <imperative summary>`. For example, use `Codex (via Min): Update Week 04 changelog` for Codex work or `Manus (via Min): Update Week 04 changelog` for Manus work. Do not add agent attribution to work not produced through an agent.

## YAML invariants and defaults

Every deck must use the 1600×900 canvas, the course footer pattern, `DD MMM YYYY` lecture-date format, the shared course theme, a week-specific overlay, and the RevealJS chalkboard. Chalkboard requires `self-contained: false`; retain that pairing unless the instructor explicitly asks to disable the chalkboard. The YAML below is the default starting point. Values such as QR and logo paths and timer inclusion may vary when the deck needs them; keep any variation valid and consistent with the deck's assets and features.

```yaml
---
title: "<Lecture Title>"
subtitle: |
  <span class="title-qr-subtitle">CP4285 Modern Recommendation Systems — Week NN</span>
  <a class="title-qr" href="https://soc-n.us/cp4285-tNN-wNN" target="_blank" rel="noopener" aria-label="Open the Week NN slide deck">
    <picture>
      <source type="image/svg+xml" srcset="../../uploads/cp4285-tNN-wNN-HASH.svg">
      <img class="title-qr-image" src="../../uploads/cp4285-tNN-wNN-HASH.png" alt="QR code for the Week NN slide deck">
    </picture>
    <span class="title-qr-label">Scan for the slides<br><span>soc-n.us/cp4285-tNN-wNN</span></span>
  </a>
author: "CP4285 Instruction Team"
date: "DD MMM YYYY"
date-format: "DD MMM YYYY"
format:
  revealjs:
    theme: [default, ../cp4285-common.scss, wNN-custom.scss]
    include-after-body: ../cp-timer.html
    slide-number: true
    show-slide-number: all
    width: 1600
    height: 900
    chalkboard: true
    logo: "../../uploads/recommendation-social-media.png"
    footer: "CP4285 · Week NN · NUS School of Computing"
    self-contained: false
    transition: slide
    highlight-style: github
    code-line-numbers: true
    smaller: false
    scrollable: false
---
```

Use a verified soc-n.us shortlink and its matching SVG/PNG QR assets before adding the title panel. The shared theme positions the panel and aligns the title, subtitle, author, and date. Do not override `#title-slide` positioning, title widths, or author padding in a week overlay.

## Changelog slides

Create a changelog when the initial deck is created. Every deck must include it on its first section slide, normally slide 2. Retain at most three **distinct update dates**, combining all changes from the same calendar date into one concise entry. Reserve the final entry for the most recent update dated strictly before the lecture date; use the two newest other dates for the remaining slots. If that pre-lecture update is absent from the visible changelog, derive a concise summary from the latest earlier Git commit that touched `wNN.qmd` or `wNN.html`. Compare dates by calendar date with the lecture date in the deck YAML: dates after the lecture must use Orange `#EF7C00` (for example, `<strong style="color:#EF7C00;">DD MMM YYYY</strong>`); lecture-date and pre-lecture entries must use Navy `#003D7C`. Keep the changelog in descending date order and update the rendered HTML after changing it.

## Assets

Put course-wide assets in `static/uploads/` and deck-specific assets in `static/slides/wNN/assets/`. Use descriptive kebab-case filenames. Give every meaningful image useful alt text; record the source and any required attribution in speaker notes. After adding or moving an asset, render the deck and verify the rendered slide resolves the intended file.

## Accessibility

Do not communicate meaning through colour alone: retain visible labels for choices, statuses, and any colour-coded distinction. Use concise, descriptive alternative text for meaningful images, and keep interactive controls keyboard-operable. At the 1600×900 canvas, inspect contrast, readable text size, and clipping for the entire slide. For slides with fragments or other builds, advance through every state and inspect the final fully revealed state as well as the initial state; content that fits initially but overlaps, clips, or loses contrast after animation is not acceptable.

## Change propagation

When changing a course-wide convention, first identify every affected deck source, rendered HTML file, timeline, template, and shared asset. Update and render each affected deck; do not leave a course-wide formatting, primitive, timer, or changelog rule only partially propagated.

## Course visual contract

Use Arial/Helvetica throughout. H1/H2 headings are dark grey with an orange rule; H3 headings are orange. Use NUS Navy `#003D7C`, Orange `#EF7C00`, and Teal `#00796B` as the primary palette. Treat Purple `#5C2D91` as a recap/accent variant, not a replacement palette.

Use a full-bleed orange H1 section slide and normal H2 content slides:

```markdown
# 02 Section Title {background-color="#EF7C00"}

## Content slide title
```

Give every slide a speaker-notes block, even when it is empty:

```markdown
::: notes
<!-- Delivery note, source, or TODO. -->
:::
```

## Shared primitives

### Layout and spacing

| Need | Class | Rule |
|---|---|---|
| Vertical rhythm | `cp-stack` | Adds consistent sibling spacing. |
| Centre a control or compact panel | `cp-center` | Centres text. |
| Equal two-column layout | `cp-grid cp-grid--2` | Uses a **1.4em horizontal gap**. |
| Content plus timer/asides | `cp-grid cp-grid--2-aside` | Uses a **1.6em horizontal gap** and a 220 px aside. |
| Three metric columns | `cp-grid cp-grid--3` | Uses 0.75em horizontal and 0.65em row gaps. |
| Four-answer MCQ grid | `cp-choice-grid` | Uses 0.85em horizontal and 0.75em row gaps. |

Do not use Quarto `.columns` for a reusable visual component. Use the shared grid classes so the horizontal breathing room remains consistent. For singular diagram geometry, keep the exact grid inline and explain it with a nearby comment when needed.

### Text, cards, tables, media, and flow

| Pattern | Classes |
|---|---|
| Brand emphasis | `cp-text--navy`, `cp-text--orange`, `cp-text--teal`, `cp-text--muted`, plus `cp-text--strong` where needed. |
| Accessibility-only status | `cp-sr-only`. |
| General panel | `cp-card`, with `cp-card--soft`, `cp-card--prompt`, `cp-card--warning`, or `cp-card--compact`. |
| Panel sub-elements | `cp-card__title`, `cp-card__meta`. |
| Table cells | `cp-table`, `cp-table--compact`, `cp-table__cell`, `cp-table__cell--head`, `cp-table__cell--label`, `cp-table__cell--highlight`, `cp-table__cell--section`. |
| Images | `cp-image`, plus `cp-image--shadow` or `cp-image--contain`. |
| Survey metrics | `cp-metric`, `cp-metric--orange`, `cp-metric__label`, `cp-metric__value`, `cp-metric__meta`. |
| Compact labels | `cp-chip`, `cp-chip--muted`, `cp-chip--navy`, `cp-chip--warning`. |
| Process diagrams | `cp-flow-card`, `cp-flow-arrow`. |

Apply these classes to the smallest meaningful element. Do not colour every word merely because an emphasis class exists.

## Frames and recaps

Use the shared fixed 20 px frame system. Do not reintroduce responsive `clamp()` frame borders.

```html
<div class="cp-frame-bg cp-frame-navy"></div>
<div class="cp-frame-content">
  <div class="cp-frame-label" style="background:#003D7C;color:#EF7C00;">Previous Week Exercise Review</div>
  <div class="cp-frame-title cp-text--navy">Title</div>
  <div class="cp-frame-body" style="color:#333;">Body content</div>
</div>
```

Available frame variants are `cp-frame-orange`, `cp-frame-navy`, `cp-frame-teal`, and `cp-frame-purple`. Use the W02 thumbnail recap classes only for a genuine previous-week composite recap: `cp-thumbnail-recap-content`, `cp-thumbnail-composite-wrap`, and `cp-thumbnail-composite`.

### Four-quadrant previous-week recap

Use [`templates/previous-week-recap.qmd`](templates/previous-week-recap.qmd) for the slide markup. The composite asset is a single 1920x1080 image made from four 16:9 source-slide captures:

- Put the four tiles in a true 2x2 contact sheet. Do not add canvas padding, whitespace, or gutters around the tiles.
- Separate adjacent tiles with a 2 px Purple (`#5C2D91`) cross-rule. Add a 2 px dark (`#1A0A2E`) perimeter around the whole composite; never use a white perimeter.
- Capture each source slide at its complete instructional state. For a fragment/build slide, advance to and capture the final fully revealed state.
- Keep the purple `cp-frame-purple` recap frame and label outside the composite. The image should not recreate a second thick frame.

The recap is a quick retrieval cue, not a re-teaching deck: provide concise alt text, name the four source slides in notes, and end the notes with one bridge question into the new topic.

## Activity grammar

Every activity must state the task, timebox, expected output, and instructor synthesis in speaker notes and in the delivery timeline.

### Pre-lecture activities

Use a pre-lecture prompt to activate an outcome that students have already encountered and to surface a tension that the following lecture will resolve. Do not require students to name, distinguish, or apply architecture vocabulary that the following week is intended to teach. State the response format and deadline visibly; specify the expected output and next-lecture synthesis in the notes.

| Activity type | Title convention | Core classes |
|---|---|---|
| Multiple choice / response | `🎰 Bandit Time: <question>` | `cp-activity cp-activity--navy cp-activity--framed`, `cp-choice-grid`, `cp-choice-card`. |
| Small-group discussion | `👥 <activity title>` | `cp-activity cp-activity--navy cp-activity--framed`, `cp-activity__prompt`, `cp-activity__instructions`. |
| Prompt plus timer | Either convention above | Add `cp-grid cp-grid--2-aside` and `cp-activity__timer`. |

### Canonical MCQ

Use the same answer convention in every deck: **A red**, **B blue**, **C green**, and **D purple**. Always retain the letter in visible text; colour must not carry meaning alone.

```html
<div class="cp-activity cp-activity--navy cp-activity--framed cp-grid cp-grid--2-aside">
  <div>
    <p class="cp-activity__prompt">Which description best fits this model?</p>
    <div class="cp-choice-grid">
      <div class="cp-choice-card cp-choice-card--a"><strong class="cp-choice-card__letter">A.</strong><span class="cp-choice-card__text">Option A</span></div>
      <div class="cp-choice-card cp-choice-card--b"><strong class="cp-choice-card__letter">B.</strong><span class="cp-choice-card__text">Option B</span></div>
      <div class="cp-choice-card cp-choice-card--c"><strong class="cp-choice-card__letter">C.</strong><span class="cp-choice-card__text">Option C</span></div>
      <div class="cp-choice-card cp-choice-card--d"><strong class="cp-choice-card__letter">D.</strong><span class="cp-choice-card__text">Option D</span></div>
    </div>
  </div>
  <div class="cp-activity__timer cp-center">
    <!-- Copy the timer markup below only when a timer is required. -->
  </div>
</div>
```

Keep the correct answer and explanation in notes, not on the student-facing question slide unless the slide is explicitly an answer/debrief slide.

### Shared countdown timer

The YAML `include-after-body: ../cp-timer.html` loads the controller. **Never paste an inline timer script.** For each timer, give all IDs a unique prefix and place the data attributes on its button.

```html
<div class="cp-timer">
  <svg width="140" height="140" viewBox="0 0 180 180" aria-label="Three-minute countdown timer">
    <circle cx="90" cy="90" r="75" fill="none" stroke="#ddd" stroke-width="14"></circle>
    <circle id="TIMERID-ring" class="cp-timer__ring" cx="90" cy="90" r="75" fill="none" stroke="#EF7C00" stroke-width="14" stroke-dasharray="471.24" stroke-dashoffset="0" stroke-linecap="round" transform="rotate(-90 90 90)"></circle>
    <text id="TIMERID-text" class="cp-timer__text" x="90" y="98" text-anchor="middle" font-family="Arial" font-size="26" font-weight="bold" fill="#00796B">03:00</text>
  </svg>
  <span id="TIMERID-status" role="timer" aria-live="polite" class="cp-sr-only">03:00</span>
  <button id="TIMERID-btn" type="button" class="cp-timer__button" data-cp-timer data-seconds="180" data-ring="TIMERID-ring" data-text="TIMERID-text" data-status="TIMERID-status">▶ Start Timer</button>
</div>
```

The controller provides **Start → Pause → Resume → Expire → Restart**, plays one short expiry tone, turns the ring green at expiry, and pauses a running timer when the slide is left. Do not duplicate this behaviour in a week file.

### Break slide

Copy `templates/break-slide.qmd`. Replace every `BREAKID` with a unique identifier and replace the fun-fact placeholder. The shared timer controller requires no local script. Keep the black background, white text, orange accents, content-left/timer-right layout, and a large horizontal gap between columns.

## Course content conventions

End a blockquote with a blank line before the next heading or fenced div. Without that boundary, Pandoc can absorb the following heading and fence into the quote, leaving literal fence markers in the output and triggering Quarto warnings.

Use Quarto MathJax for non-trivial equations. Colour meaningful mathematical quantities with named `orange`, `teal`, and `navy` TeX colours, then explain them in plain language on the same slide.

Use `.callout-warning` for ethical risks and `.callout-note` for supplementary information. Use the shared `.to-think-about` callout treatment for one concise reflective question; do not recreate it as raw HTML.

Each week should include an ethical thread appropriate to the topic. When a topic materially benefits from a user-treatment lens, ask whether to include the following dimensions rather than silently adding them: ♣ adversarial/shill, ♥ social, ♦ novelty, or ♠ loyalist/metadata-driven. Treat these as contextual design lenses, never fixed demographic labels.

Finish a deck with a concise Summary slide and an explicit next-week bridge. Use a navy background, white text, orange emphasis, and a visible `🔑` or `🤞` synthesis cue for a Key Point or Summary slide.

## Validation and delivery

Run:

```bash
cd static/slides/wNN
quarto render wNN.qmd
```

After a shared-theme, primitive, timer, or template change, inspect every affected instance in W01 and W02. Verify title-slide navigation, two-column gaps, framed-slide geometry, MCQ card colours, timer start/pause/resume and slide-exit pause behaviour, text contrast, and absence of clipping. Update the rendered HTML and timeline before committing.

## File layout

```text
static/slides/
├── cp4285-common.scss
├── cp-timer.html
└── wNN/
    ├── wNN.qmd
    ├── wNN.html
    ├── wNN_files/      # Required RevealJS assets when chalkboard is enabled
    ├── wNN-custom.scss
    └── wNN-timeline.md
```

Commit source, rendered output, overlay, timeline, and all changed shared assets in one change.
