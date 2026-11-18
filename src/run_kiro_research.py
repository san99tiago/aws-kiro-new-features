#!/usr/bin/env python3
"""Run parallel headless Kiro CLI sessions, one per Kiro surface.

Writes research/YYYY-MM-DD-<surface>.md and research/YYYY-MM-DD-summary.md,
and refreshes research/latest.md. Requires KIRO_API_KEY in the environment
(never printed) and kiro-cli on PATH.
"""
import datetime
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "research"
TIMEOUT_SECONDS = 20 * 60

SOURCES = (
    "https://kiro.dev, https://kiro.dev/docs/, https://kiro.dev/changelog/, "
    "https://kiro.dev/blog/, https://kiro.dev/docs/cli/headless/"
)

SURFACES = {
    "cli": "Kiro CLI (terminal agent, headless mode, commands, tools)",
    "ide": "Kiro IDE (specs, hooks, steering, agent features)",
    "web": "Kiro Web (browser experience, specs in the web, pull requests)",
    "crew": "Kiro Crew (multi-agent or team capabilities)",
}

PROMPT = """You are a research agent. Use web fetch on the official Kiro pages ({sources}) \
to find the latest news and features for: {surface}.
Rules:
- Only report facts you saw on official pages. If you find nothing for this surface, say so plainly.
- Write simple, plain-language Markdown with no em dashes.
- Output format: start with "# Kiro {name}: weekly findings ({date})", then sections
  "## What is new", "## Why it matters", "## What to try this week", "## Sources" (list of URLs).
- Respond with the Markdown report only."""


def run_surface(name, surface, date):
    prompt = PROMPT.format(sources=SOURCES, surface=surface, name=name.upper(), date=date)
    cmd = [
        "kiro-cli", "chat", "--no-interactive",
        "--trust-tools=web_fetch,web_search",
        prompt,
    ]
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=TIMEOUT_SECONDS, check=False
        )
        body = proc.stdout.strip()
        if proc.returncode != 0 or not body:
            err = proc.stderr.strip().splitlines()[-1:] or ["no output"]
            body = "# Kiro %s: weekly findings (%s)\n\nResearch failed (exit %d): %s\n" % (
                name.upper(), date, proc.returncode, err[0][:200]
            )
    except subprocess.TimeoutExpired:
        body = "# Kiro %s: weekly findings (%s)\n\nResearch timed out.\n" % (name.upper(), date)
    path = OUT_DIR / ("%s-%s.md" % (date, name))
    path.write_text(body.rstrip() + "\n", encoding="utf-8")
    return name, path, body


def main():
    date = datetime.date.today().isoformat()
    OUT_DIR.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=len(SURFACES)) as pool:
        futures = [pool.submit(run_surface, n, s, date) for n, s in SURFACES.items()]
        results = [f.result() for f in futures]

    parts = [
        "# Kiro weekly research (%s)\n" % date,
        "Findings from headless Kiro CLI sessions for each surface.\n",
    ]
    for name, path, body in results:
        parts.append("\n---\n\n" + body.strip() + "\n")
        print("wrote", path.relative_to(ROOT))
    summary = "\n".join(parts)
    (OUT_DIR / ("%s-summary.md" % date)).write_text(summary, encoding="utf-8")
    (OUT_DIR / "latest.md").write_text(summary, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
