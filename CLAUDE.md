# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Personal website for Rob Barry (www.robbarry.org), a data journalist at The Wall Street Journal. Hugo static site with fully custom layouts — no active theme. Deployed to GitHub Pages via GitHub Actions on push to `main`.

## Development

```bash
hugo serve          # local dev server with live reload
hugo serve -D       # include draft posts
hugo serve --port 1314  # alternate port
```

Deployment is just `git push` to main. GitHub Actions builds with Hugo 0.157.0 extended, minifies, and deploys to Pages.

## Architecture

**No theme.** Three theme submodules exist (PaperMod, ananke, hugo-book) but `theme` is commented out in `config.yml`. All rendering comes from custom layouts in `layouts/`.

**Layout chain:**
- `layouts/_default/baseof.html` — page shell: dark body, paper-colored `.page` div, header/nav/footer
- `layouts/index.html` — homepage: hero tagline from `_index.md` front matter (`tagline` param), then markdown content
- `layouts/_default/list.html` — category/section pages: optional intro text, then date-grid article entries
- `layouts/_default/single.html` — individual posts: date, title, description, content, tags. Optional MathJax via `math: true` in front matter

**Partials:** `mathjax.html` (conditional math rendering), `ai_disclosure.html` (AI content disclosure box). The `extend_head.html` and `footer.html` partials are deprecated stubs.

**Styling:** Single CSS file at `assets/css/custom.css`. Design system uses CSS variables. Paper-on-dark aesthetic (dark `--bg`, light `--paper` content area). Fonts loaded from Google Fonts: Young Serif (display), Literata (body), JetBrains Mono (mono/metadata). No CSS framework, no JS dependencies.

## Content Structure

- `content/_index.md` — homepage bio (has `tagline` front matter for hero)
- `content/work/` — ~158 journalism articles (2008–2023), each a short entry with title, date, categories, tags, and a brief description linking to the original piece
- `content/posts/` — blog posts/essays
- `content/categories/` — landing pages for `top/`, `docsandpods/`, `audio/`, `videos/`

**Content front matter pattern:**
```yaml
title: "Article Title"
date: 'YYYY-MM-DD'
categories: [Articles, top]    # controls which section pages include it
tags: [topic1, topic2]
description: "One-line summary"
draft: true                    # optional
```

File naming: `YYYY-MM-DD-slug.md`

## Config Notes

- `config.yml` — single config file, no environment splits
- `relativeURLs: true` — all links are relative
- `paginate: 999999` — effectively no pagination
- Permalinks: posts and pages render at `/:slug/`, tags at `/tag/:slug/`
- Menu defined in config under `menu.main` (About, Stories, Docs & Pods, Posts, CV)
- `CNAME` file points to `www.robbarry.org`
