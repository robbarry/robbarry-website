# Rob Barry's website

Personal site at [www.robbarry.org](https://www.robbarry.org). Built with [Hugo](https://gohugo.io/) using custom layouts (no theme). Deployed to GitHub Pages.

## Local development

```bash
hugo serve
```

Or, to include content marked as `draft: true`:

```bash
hugo serve -D
```

## Deployment

```bash
git push
```

Push to `main` triggers a GitHub Actions workflow that builds with Hugo 0.157.0 (extended) and deploys to GitHub Pages.

## Stack

- **Hugo** — static site generator, custom layouts in `layouts/`
- **CSS** — single stylesheet at `assets/css/custom.css`, no framework
- **Fonts** — Young Serif, Literata, JetBrains Mono via Google Fonts
- **Hosting** — GitHub Pages with custom domain (`CNAME`)
