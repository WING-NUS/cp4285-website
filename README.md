# CS4285 Website

Documentation website for CS4285 at the National University of Singapore.

The site is built with the Hugo Blox Documentation template and customized with:

- NUS orange and blue theme colors
- dark mode as the default theme
- Arial/Helvetica sans serif base typography
- course-focused documentation pages for schedule, assignments, policies, and resources

## Requirements

- Hugo Extended 0.161.1 or newer
- Node.js 22 or newer
- pnpm 10 or newer

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

## Deployment

GitHub Pages deployment is handled by `.github/workflows/deploy.yml`.

The workflow runs on pushes to `main` and can also be started manually from the GitHub Actions tab. It builds the Hugo site, generates the Pagefind search index, and deploys `public/` to GitHub Pages.

## Content

Course pages live in `content/docs/`. The homepage is configured in `content/_index.md`.

Branding and visual defaults live in:

- `config/_default/params.yaml`
- `data/themes/nus.yaml`
- `data/fonts/arial.yaml`
- `assets/css/custom.css`
