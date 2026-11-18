# Requirements

## Introduction

A public site that explains, in simple terms, the new features of Kiro across Kiro CLI, Kiro IDE, Kiro Web and Kiro Crew, kept current by a weekly headless Kiro research job.

## Requirements

### 1. Static site
**User story:** As a reader, I want a simple, nice page that explains each Kiro surface, so that I can understand what is new quickly.

Acceptance criteria:
1. WHEN the site is opened THEN it SHALL show sections for CLI, IDE, Web and Crew.
2. The site SHALL be responsive and support dark and light themes.
3. The site SHALL link to the latest research report.

### 2. Publishing
**User story:** As the maintainer, I want the site published automatically, so that merges to main go live.

Acceptance criteria:
1. WHEN changes under `site/` or `research/` are pushed to `main` THEN a workflow SHALL deploy to GitHub Pages.

### 3. Weekly research
**User story:** As the maintainer, I want Kiro to research official pages weekly, so that I get news for all surfaces.

Acceptance criteria:
1. The workflow SHALL run every Thursday morning and on manual dispatch.
2. It SHALL use the `KIRO_API_KEY` GitHub Actions secret and never print the environment.
3. It SHALL write Markdown reports per surface plus a summary, and open a pull request.

### 4. Licensing
1. The repo SHALL be licensed Apache 2.0, Copyright 2026 Santiago Garcia Arango.
