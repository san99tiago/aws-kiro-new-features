# Design

## Overview

Plain HTML, CSS and JS in `site/`. No build framework. Python standard library scripts handle research and rendering.

## Components

- `site/`: static pages, theme toggle, research list loaded from `site/research/manifest.json`.
- `src/run_kiro_research.py`: runs four parallel `kiro-cli chat --no-interactive` sessions (cli, ide, web, crew), writes `research/YYYY-MM-DD-<surface>.md`, a combined summary and `latest.md`.
- `scripts/build_site.py`: renders `research/*.md` to `site/research/*.html` and a manifest.
- `.github/workflows/kiro-weekly-research.yml`: Thursday cron, installs Kiro CLI, runs the research with `KIRO_API_KEY`, uploads artifacts, opens a PR.
- `.github/workflows/deploy-pages.yml`: builds and deploys `site/` to GitHub Pages on push to `main`.

## Flow

Thursday cron -> headless research -> PR with Markdown -> merge -> Pages deploy.

## Security

The API key is exposed only to the research step. No step prints the environment. Rendered Markdown is HTML-escaped.
