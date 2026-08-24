# CP4285 Website

Documentation website for CP4285: Modern Recommendation Systems, Emerging Topics in Computer Science V, at the National University of Singapore.

The site is built with the Hugo Blox Documentation template and customized with:

- NUS orange and blue theme colors
- dark mode as the default theme
- Arial/Helvetica sans serif base typography
- course-focused documentation pages for schedule, assignments, policies, and resources

## Requirements

- Hugo Extended 0.161.1 or newer
- Node.js 22 or newer
- pnpm 10 or newer
- Quarto CLI 1.10.18 (required when editing lecture-slide sources)

## Local Development

Install dependencies:

```bash
pnpm install
```

Start the development server:

```bash
pnpm run dev
```

Build the production site:

```bash
pnpm run build
```

If you only want to validate Hugo configuration and module resolution:

```bash
hugo config
```

## Lecture Slides (Quarto)

Lecture decks live in `static/slides/wNN/`. Each deck is authored as a Quarto RevealJS source file (`wNN.qmd`) and committed with its rendered self-contained HTML (`wNN.html`). Hugo serves these static outputs; the GitHub Pages deployment workflow does not render Quarto sources.

To edit a deck, render it from its own directory:

```bash
cd static/slides/wNN
quarto render wNN.qmd
```

For an interactive local review:

```bash
quarto preview wNN.qmd
```

For new decks and any shared visual, activity, MCQ, timer, QR, or frame work, follow the [CP4285 slide-authoring guide](skills/cp4285-slides/SKILL.md). The current reference system is `w01`, `w02`, and the [prototype deck](skills/cp4285-slides/templates/prototype-deck.qmd); use the shared `cp4285-common.scss` and `cp-timer.html` rather than copying week-local styles or timer scripts.

When a slide deck changes, commit its `.qmd`, regenerated `.html`, changed local assets, and any related overlay or timeline together. Render and visually inspect every affected slide before committing.

## Deployment

GitHub Pages deployment is handled by `.github/workflows/deploy.yml`.

The workflow runs on pushes to `main` and can also be started manually from the GitHub Actions tab. It builds the Hugo site, generates the Pagefind search index, and deploys `public/` to GitHub Pages. The deployment uses the rendered slide HTML already committed under `static/slides/`; it does not run `quarto render`.

## Content

The homepage (`content/_index.md`) contains the course description, prerequisites, learning outcomes, and links to sub-pages. Course sub-pages (schedule, assignments, grading, FAQ) live in `content/docs/`.

Branding and visual defaults live in:

- `config/_default/params.yaml`
- `data/themes/nus.yaml`
- `data/fonts/arial.yaml`
- `assets/css/custom.css`
