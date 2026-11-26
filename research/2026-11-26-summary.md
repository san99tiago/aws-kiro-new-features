# Kiro weekly research (2026-11-26)

Findings from headless Kiro CLI sessions for each surface.


---

# Kiro CLI: weekly findings (2026-11-26)

## What is new

- **Kiro CLI 3.6.0 (Nov 23, 2026), "Subagent Stop Hooks and Guided Compaction."** The changelog lists patches 3.6.1 and 3.6.2, both dated Nov 25, 2026.
  - A `SubagentStop` hook runs in a V3 session when a dispatched subagent finishes. It can send that subagent one more instruction before its result returns.
  - When any Hook's output is longer than 3,000 characters, Kiro CLI saves the full output to a file. The agent gets the beginning of the output plus the file path.
  - In a V3 session you can add instructions after `/compact`. An example is `/compact Keep the migration decisions and remaining validation steps`. The instructions apply only to that one compaction.
  - The release also adds conversation recaps, notification controls, managed V2 controls, and an all-users Windows installer. The changelog snippet I saw gave no further detail on these.
- **Headless mode docs.**
  - Headless mode runs with `kiro-cli chat --no-interactive`. The prompt can be a positional argument or piped through stdin.
  - Authentication uses a stored login or the `KIRO_API_KEY` environment variable. A stored login takes precedence over the API key.
  - API keys are available only to Pro, Pro+, Pro Max, and Power subscribers. If an administrator manages your subscription, they must enable API key generation first.
  - Admin governance rules, such as MCP restrictions, model access, and web fetch permissions, also apply to headless sessions.
  - A local headless run that names no harness runs V2. The docs recommend adding `--v3` or `--v2` so the run does not depend on the default.
  - In V3, use `--trust-all-tools` or `--trust-tools=<ids>` because no user is there to approve tool calls.
  - In Kiro CLI 3.6.2 or later, `web_search` and `@builtin` in `--trust-tools` also trust V3 web search. A `use_aws` entry prints a warning that it has no effect on V3.
  - In V3, a sub-agent tool call runs without approval only if the parent session's policy also allows it. Otherwise a headless run denies it. Adding the sub-agent to `trustedAgents` does not change this.
  - In Kiro CLI 2.33 or later, a first message starting with `@<prompt-name>` runs that prompt. `@agent-sop:<name>` runs a named SOP.
- **Blog: "Your agents run for days: now Kiro CLI keeps up" (Nov 23, 2026).** I only saw the title on the blog index. I did not open the post.
- **Earlier context.** The blog lists "Kiro CLI V3 is rolling out as the default experience" (Oct 9, 2026), "Introducing memory in Kiro IDE and CLI" (Oct 20, 2026), and "Local sandboxing in Kiro" (Oct 14, 2026).
- **Models in CLI.** Claude Fable 5.2 Preview (Nov 23) and GPT 6.2 Astra Preview (Nov 25) are rolling out to Kiro Enterprise organizations only. After a rollout, users restart the CLI to load the new model list.

## Why it matters

- `SubagentStop` hooks give scripts a way to steer subagents at the point where they finish.
- Saved Hook output keeps long conversations readable without losing the full output.
- Guided `/compact` lets you choose what a long session keeps.
- Headless runs depend on the harness version and the trust flags. Pinning `--v3` or `--v2` and listing exact tools keeps CI runs predictable.

## What to try this week

- Update to Kiro CLI 3.6.2 and run `/compact` with your own instructions in a V3 session.
- Run a headless job with explicit flags: `kiro-cli chat --v3 --no-interactive --trust-tools=read_file,grep_search "Find all TODO comments in src/"`.
- If you use `use_aws` in `--trust-tools`, check your scripts for the new warning on V3.
- Read the blog post on long-running agents in the CLI.

## Sources

- https://kiro.dev/changelog/
- https://kiro.dev/docs/cli/headless/
- https://kiro.dev/blog/


---

# Kiro IDE: weekly findings (2026-11-26)

## What is new

- **Remote work in the IDE (changelog, IDE 1.5.11, Nov 20, 2026).**
  - **SSH:** "Connect to Host" links a Kiro window to your own Linux machine over SSH. The editor stays on your computer. Files, terminals and the agent run on the remote machine, so the agent can keep working after you disconnect.
  - **Dev Containers:** You can open a project that has a `.devcontainer` folder with "Reopen in Container".
  - **Cloud sessions:** You can open a cloud session in its own Kiro window.
- **Frequent IDE patches.** The changelog lists patches 1.5.37 (Nov 24), 1.5.44 (Nov 25) and 1.5.49 (Nov 25). I did not read the notes for these patches.
- **New models for Kiro Enterprise, in Preview.**
  - Claude Fable 5.2 (Nov 23): 1M context window, 6x credit multiplier, US-only inference.
  - GPT 6.2 Astra (Nov 25): 1M context window, 7.2x credit multiplier. The multiplier rises to 14.4x for requests over 272K tokens. Inference is US-only.
  - Access is limited. Organizations enable these models through model governance. To see a new model in the IDE, restart it.
- **Blog posts related to the IDE.** I only saw titles and dates for these, not the post contents.
  - Nov 20: "Remote workspaces bring the IDE to where your code and compute already live"
  - Nov 20: "Introducing Kiro for VS Code"
  - Nov 10: "Introducing 'Approve for me' in Kiro"
  - Oct 30: "Spec it safe: shift left and harden your specs with security requirements"
  - Oct 20: "Introducing memory in Kiro IDE and CLI"
  - Oct 14: "Local sandboxing in Kiro: keep agent commands within boundaries"
  - Sep 30: "Introducing Kiro workflows"
- **Docs.**
  - The docs describe one agent harness behind the IDE, VS Code, CLI, Web and Mobile. Your `.kiro/` configuration (specs, steering) is shared across them.
  - The docs list these features: Specs and Bugfix Specs, Steering, Hooks, MCP, Permissions, Custom agents, Workflows, Skills, Powers, Memory, Compaction, Kiroignore, and Checkpoints and rewind.
  - There are also docs pages for "Remote development" and "Kiro for VS Code".

## Why it matters

- Remote SSH and Dev Containers let you keep code and compute where they already live while still using the IDE and its agent.
- Because `.kiro/` configuration is shared across surfaces, the same specs and steering work in the IDE, the VS Code extension, the CLI and Web.
- Enterprise teams can try the newest models under model governance. Fable 5.2 and GPT 6.2 Astra carry high credit multipliers, so their cost is worth checking first.

## What to try this week

- Update the IDE and connect to a Linux host with "Connect to Host". Try leaving the agent running, then disconnect.
- Open a project that has a `.devcontainer` folder and choose "Reopen in Container".
- Read the "Spec it safe" post and add security requirements to one of your specs.
- Look at the docs pages for Hooks, Steering and Workflows, and automate one repeated step in your project.
- Enterprise admins: check model governance to see whether Fable 5.2 or GPT 6.2 Astra is available to you.

## Sources

- https://kiro.dev/blog/
- https://kiro.dev/changelog/
- https://kiro.dev/docs/


---

# Kiro WEB: weekly findings (2026-11-26)

## What is new

- **Referral codes in Kiro Web (Nov 24, 2026, changelog).** Enterprise users can now generate referral codes in Kiro Web and share them with friends and family. Each code gives 20% off any paid individual plan (Pro, Pro+, Pro Max, or Power) for 12 billing cycles.
- **Kiro Enterprise for iPhone (Nov 24, 2026, changelog).** The app is on the App Store for organization accounts and needs iOS 26 or later. You can start cloud sessions, follow the agent, review its changes, and reply when it needs input. Sessions sync with Kiro Web, so you can start on your phone and continue on the web.
- **Cloud sessions reach private networks (Nov 20, 2026, blog post title).** I only saw the title on the blog list. I did not open the post, so I can't give details.
- **Autonomous mode docs (page updated Oct 2, 2026).** This is not new this week, but it is the clearest description of how Web handles specs and pull requests.
  - Autonomous mode is a toggle in the chat input bar. It is off by default.
  - The agent plans the work, generates requirements, and defines acceptance criteria.
  - Sub-agents then write and verify the code in an isolated sandbox.
  - The agent opens one or more pull requests or merge requests with descriptions of the changes, approach, and trade-offs.
  - If the agent needs clarification, the task moves to a "Needs attention" state.
  - On a PR, you can comment and the agent addresses the comments. `/kiro all` addresses all comments across the PR. `/kiro fix` addresses one conversation thread.
- **Docs structure for Web.** The docs list pages for Setup & First Run, Identity Center, Connect your repositories (GitHub and GitLab), Working with the agent, Autonomous mode, Schedule, Configuration Sync, and Sandbox. The docs describe Web as a "browser-based agent for multi-repo tasks that plans, implements, and opens PRs".
- **Background reading (Sep 14, 2026, blog post title).** "Tackling technical debt at scale with autonomous mode in Kiro Web." I saw only the title.

## Why it matters

- Web sessions now sync with the iPhone app for organization accounts, so you can start a task on one device and finish it on another.
- Autonomous mode plus the `/kiro all` and `/kiro fix` commands let you review and steer a Web-created PR from the PR itself.
- The docs say shared `.kiro/` configuration (specs, steering) works across all surfaces, including Web.

## What to try this week

- Turn on **Autonomous** in a Web session for a well-defined task, such as writing tests or a small refactor. Review the PR it opens.
- Leave a comment on the PR and use `/kiro fix` on one thread to see the agent push an update.
- If you have an Enterprise account, generate a referral code in Kiro Web.
- Read the private networks post if your repositories sit behind a private network.

## Sources

- https://kiro.dev/changelog/
- https://kiro.dev/blog/
- https://kiro.dev/docs/
- https://kiro.dev/docs/web/autonomous-mode/


---

# Kiro CREW: weekly findings (2026-11-26)

## What is new

- **Conductor mode in Kiro Crew.** The Kiro blog lists a post titled "Introducing conductor mode in Kiro Crew" (Nov 20, 2026). I could not open the post itself, so I have no details on what the mode does.
- **Bots in Kiro Crew.** The blog lists "Introducing bots in Kiro Crew" (Nov 5, 2026). The docs describe a bot as a persistent agent in Crew. Each bot has its own threads, memory and workspace. It can track ongoing goals, delegate tasks to workers and follow up on progress over time. The docs suggest bots for these jobs:
  - contributing to a project
  - working through a bug backlog
  - improving CI reliability
  - monitoring build health
- **Claude Fable 5.2 Preview (Nov 23, 2026).** It is rolling out to Kiro Enterprise organizations. The changelog says the model coordinates subagents on long runs. To load the new model list in Crew, run `kirocrew restart`.
- **Crew docs overview.** The docs describe Crew as an open-source personal AI agent that runs locally or on remote hardware. You can reach it from the desktop app, a web dashboard, the CLI, and chat channels such as Slack, Discord, Telegram, Teams, Webex, WeCom and WeChat. The Features section lists these areas:
  - subagents
  - scheduling
  - artifacts
  - agent backends (Kiro CLI, Claude Code, Kiro Agent, Codex, OpenCode, Pi, goose)
  - multi-instance (Preview)
  - Task Runner
  - workflows
  - memory
  - knowledge
  - snapshot and restore
  - browser
  - Computer Use
- **Crew on the kiro.dev homepage.** The homepage shows Crew as one sandboxed run in a software delivery loop. Signals come from Slack, Teams, GitHub, GitLab and MCP. Triggers include hourly channel watch (heartbeat), mention, DM or webhook. Small fixes are built in a sandbox, then reviewed. Big items become specs for a human.
- **Related CLI change.** CLI 3.6.0 added `SubagentStop` hooks (V3 only). They run when a dispatched subagent finishes and can send it one more instruction. This is a CLI feature, not a Crew feature.

## Why it matters

- Bots give Crew agents that own a goal over time. A single chat or a scheduled job does not do that.
- Crew can run on your own machine, in a container or on a remote host. Its sessions, memory and schedules persist across restarts.
- The homepage flow, from signal to sandboxed fix to PR to human review, shows how Kiro expects teams to use Crew.

## What to try this week

- Install Crew with `curl -fsSL https://download.crew.kiro.dev/cli.sh | sh`. Then run `kirocrew setup`, `kirocrew doctor` and `kirocrew gateway`. Open http://localhost:5476.
- Read the Bots docs and set up one bot for a small, ongoing goal, such as keeping nightly builds green.
- In chat, ask Crew to "research these three options in parallel and recommend one". This uses its subagents.
- Add a scheduled job with natural language, for example "Every weekday at 9, summarize my open work".
- Read the conductor mode blog post. I could not open it, so check the Nov 20 entry on the blog page.

## Sources

- https://kiro.dev
- https://kiro.dev/docs/
- https://kiro.dev/docs/crew/
- https://kiro.dev/docs/crew/bots/
- https://kiro.dev/docs/crew/features/
- https://kiro.dev/docs/cli/headless/
- https://kiro.dev/changelog/
- https://kiro.dev/blog/
