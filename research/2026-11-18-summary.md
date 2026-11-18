# Kiro weekly research (2026-11-18)

Findings from headless Kiro CLI sessions for each surface.


---

# Kiro CLI: weekly findings (2026-11-18)

## What is new

- **Kiro CLI 3.4.0 (Nov 16, 2026): hooks that rewrite tool inputs and answer permission prompts.**
  - In a V3 session, a `PreToolUse` hook can return `updatedInput` to replace a tool call's inputs before the tool runs. It can also return `allow`, `ask`, or `deny`.
  - A new `PermissionRequest` hook runs when a tool call would ask for permission. It can answer `allow` or `deny`.
  - A `deny` from any hook wins over an `allow`. A hook's permission answer applies to that one tool call only.
  - The release also offers four `/memories` choices. It resumes and lists cloud sessions in more places. It fixes issues with headless mode, the context window, MCP, search, `/tangent`, `/rewind`, and display.
- **Kiro CLI 3.3.0 (Nov 12, 2026): copy and compaction controls.**
  - `/copy N` copies the Nth-latest response. `/copy last N` copies the latest N messages, oldest first.
  - You can choose the context usage at which automatic compaction starts.
  - The agent monitor shows each sub-agent's task.
  - The `/model` search, sort, and edit controls moved to `Up`.
  - A V2 agent's allow rules no longer widen when it is upgraded to V3.
  - A stalled workflow session reloads after an agent restart.
  - Fixes cover headless, resume, `/memories`, `/goal`, voice, clipboard, session, and search display issues.
- **Headless mode docs (current):**
  - Run `kiro-cli chat --no-interactive "prompt"`, or pipe the prompt through stdin. Authenticate with the `KIRO_API_KEY` environment variable.
  - A local headless run that names no harness runs V2. Add `--v3` or `--v2` so the run does not depend on the default.
  - V3 runs can use `--trust-all-tools` or `--trust-tools` with a comma-separated list of tool IDs.
  - In CLI 3.3.0 or later, a `--trust-tools` entry can also be a V2 tool name, `@server`, `@server/tool`, `@builtin`, or a `*`/`?` pattern.
  - A V3 sub-agent's tool call runs without approval only if the parent session's policy also allows it. Otherwise a headless run denies it.
  - A first message starting with `@<prompt-name>` runs that prompt. `@agent-sop:<name>` runs a named SOP. This needs CLI 2.33 or later.
  - V3 non-interactive runs load Hooks from the selected agent and workspace, starting with CLI 2.27.1.
  - API key authentication is only for Pro, Pro+, Pro Max, and Power subscribers. Administrator governance rules apply to headless sessions too.
- **Local sandbox controls for enterprises (Nov 17, 2026).** Enterprise administrators can require sandboxing for commands and local stdio MCP servers in Kiro CLI and IDE. This is in preview in US East (N. Virginia). It needs Kiro CLI 3.4.0 or later.
- **Recent blog posts relevant to the CLI:**
  - "Introducing memory in Kiro IDE and CLI" (Oct 20, 2026)
  - "Local sandboxing in Kiro: keep agent commands within boundaries" (Oct 14, 2026)
  - "Kiro CLI V3 is rolling out as the default experience" (Oct 9, 2026)
  - "Introducing 'Approve for me' in Kiro" (Nov 10, 2026)

## Why it matters

- Hooks can now apply a team's rules to every tool call in V3 sessions. A script can answer permission prompts, so you don't have to approve each call by hand.
- Headless runs are easier to control. The `--trust-tools` options are more flexible, and the docs say to pin `--v3` or `--v2` explicitly.
- Administrators can enforce sandboxing, which developers cannot turn off through client settings.

## What to try this week

- Upgrade to Kiro CLI 3.4.0. Write a `PermissionRequest` hook that allows safe read-only commands and denies the rest.
- Run a headless job with scoped permissions: `kiro-cli chat --v3 --no-interactive --trust-tools=read_file,grep_search "Find all TODO comments in src/"`.
- Try `/copy 2` and `/copy last 3`. Then set your own compaction start level.

## Sources

- https://kiro.dev/changelog/
- https://kiro.dev/blog/
- https://kiro.dev/docs/cli/headless/


---

# Kiro IDE: weekly findings (2026-11-18)

## What is new

- **IDE 1.4.215 (Nov 16, 2026):** You can fork a chat from any turn. This lets you try a different prompt from the same point without losing the original chat. The release also shows the credits a workflow run reports and gives the Memory levels clearer names. Chats that use a custom agent or Plan can now run at the same time as other chats. Kiro profiles in Europe (Frankfurt) can use cloud sessions from the IDE.
- **IDE 1.4.178 (Nov 12, 2026):** You can follow a workflow run step by step from its Workflow tab. After Kiro compacts a conversation, the agent reloads the skills and steering files you asked for. Large Mermaid diagrams in chat stay readable. Fixes cover freezes after a permissions change, stalls before large file writes, and missed reloads after you edit configuration on a Windows network drive.
- **Local sandbox controls (Nov 17, 2026):** Enterprise administrators can require sandboxing for commands and local stdio MCP servers in Enterprise Management (preview, US East N. Virginia). Developers need Kiro IDE 1.4.215 or later. Developers cannot turn off a required sandbox through client settings.
- **Blog posts:**
  - Nov 10: "Introducing 'Approve for me' in Kiro"
  - Oct 20: "Introducing memory in Kiro IDE and CLI"
  - Oct 14: "Local sandboxing in Kiro: keep agent commands within boundaries"
  - Oct 30: "Spec it safe: shift left and harden your specs with security requirements"
  - Sep 30: "Introducing Kiro workflows"
  I only saw the titles of these posts, not their contents.
- **Models:** Grok 4.7 was announced on Nov 12 (blog post title only).
- **Docs:** The IDE docs now sit under "IDE 1.x", with a "What's new in 1.0" page. The docs list Specs, Bugfix Specs, Steering, Hooks, MCP, Permissions, Custom agents, Workflows, Agent Skills, Powers, Cloud sessions, Memory, Compaction, Kiroignore, and Checkpoints and rewind as features. The docs say your `.kiro/` configuration is shared across IDE, CLI, Web, and Mobile.
- **Hooks (CLI 3.4.0, Nov 16):** A `PreToolUse` hook can return `updatedInput` to rewrite a tool call's inputs. A new `PermissionRequest` hook can answer a permission prompt with `allow` or `deny`. This is in the CLI changelog, so I did not see it announced for the IDE.

## Why it matters

- Forking a chat lets you compare prompt approaches without losing earlier work.
- Reloading skills and steering after compaction keeps project rules in force during long sessions.
- Running custom-agent and Plan chats in parallel removes a waiting step.
- Organization-enforced sandboxing gives teams a way to limit what the agent can run.
- Because configuration is shared across surfaces, specs, steering, and hooks set up in the IDE also work in the CLI, Web, and Mobile.

## What to try this week

- Update to IDE 1.4.215 or later and fork a chat from an earlier turn to test a different prompt.
- Start a workflow run and follow it from the Workflow tab.
- Compact a long conversation and check that your steering files and skills are reloaded.
- Read the "Spec it safe" blog post and the Specs and Steering docs. Then add security requirements to one of your specs.
- Read the "Introducing memory in Kiro IDE and CLI" post and try the renamed Memory levels.

## Sources

- https://kiro.dev/changelog/
- https://kiro.dev/blog/
- https://kiro.dev/docs/


---

# Kiro WEB: weekly findings (2026-11-18)

## What is new

I found little that is specific to Kiro Web this week. The Web-related items on the official pages are below.

- **Kiro Mobile for Android (Nov 12, 2026, changelog and blog).** You can start a cloud session on your phone or pick up one you began in Kiro Web, the IDE, or the CLI. Turning on "Build with spec" makes the agent plan first. Each session shows its pull request status, and you review and merge in your Git provider. It needs a Pro, Pro+, Pro Max, or Power plan.
- **Kiro home page.** It describes Kiro Web as the place for cloud sessions. These move long tasks to the cloud with parallel agents that can run for hours, so work continues after you close your laptop. The page also describes Workflows as isolated, checked steps that agents cannot skip.
- **Kiro home page, specs.** Specs capture intent before code is written and verify results afterward. The page lists property-based tests, requirements analysis that catches gaps before design, and Bugfix Specs.
- **Kiro home page, pull requests.** The Crew flow shows a build step that produces evidence such as test results. It then opens a pull request on GitHub or GitLab, followed by verification and human review.
- **Blog posts that mention Web (earlier dates).** "Tackling technical debt at scale with autonomous mode in Kiro Web" (Sep 14, 2026) and "Close the laptop, keep the agent: building with cloud sessions" (Aug 18, 2026). I only saw the titles in the blog list and did not read the posts.
- **Not Web-specific, seen on the changelog.** Nov 16: IDE 1.4.215 (fork conversations, cloud sessions in Europe Frankfurt) and CLI 3.4.0 (hooks that rewrite tool inputs). Nov 16 also brought Enterprise real-time OpenTelemetry events.

I did not find a changelog entry dedicated to Kiro Web for this week. I did not open the docs or headless pages, so I report nothing from them.

## Why it matters

- You can now start work in Kiro Web and continue it from your phone, or the reverse. Sessions, repositories and model choices carry over.
- Pull request status is visible in the session list, which makes it easier to follow work that runs while you are away.
- Specs and Workflows add checks before and after the agent writes code.

## What to try this week

- Start a cloud session in Kiro Web with a spec-first plan, then open it in Kiro Mobile on Android and check the pull request status.
- Read the Sep 14 blog post on autonomous mode in Kiro Web.
- Read the Aug 18 blog post on cloud sessions.

## Sources

- https://kiro.dev
- https://kiro.dev/changelog/
- https://kiro.dev/blog/


---

# Kiro CREW: weekly findings (2026-11-18)

## What is new

I found no Crew entry in the changelog dated this week. The Nov 17, 2026 entries I saw were tagged "General" (Local Sandbox Controls in Enterprise Management, and Migrate Existing Profiles to Controls). Neither one mentions Crew.

The most recent Crew news is on the blog and in the docs:

- **Bots in Kiro Crew (blog, Nov 5, 2026).** I saw the post title but could not open the post itself. Its URL guess returned a 404. The docs page for bots says a bot is a persistent agent in Kiro Crew. Each bot has its own threads, memory and workspace. A bot can track ongoing goals, delegate tasks to workers, and follow up on progress over time.
- **Bot use cases (docs).** The bots page lists these examples:
  - Submit one pull request per week to an open-source project.
  - Work through a critical bug backlog.
  - Improve CI reliability by reducing flaky tests.
  - Keep nightly builds green and monitor system health.
- **When to use a bot (docs).** The docs say to use a bot for an ongoing goal. A custom agent fits reusable instructions for a specialized task. A regular chat session fits interactive work. A scheduled job fits a task that runs at set times.
- **Crew docs structure.** The docs sidebar lists these Crew pages: Quick start, Installation, Kiro Crew LTS, Running 24/7, Bots, Chat, Agent Capabilities, Features, Interfaces, Apps, System and storage, Configuration, Security, Troubleshooting.
- **Crew description on the docs home page.** It reads "Personal AI agent with autonomous tasks, scheduling, memory, and multi-channel access".
- **Crew pipeline on the kiro.dev homepage.** The homepage shows a delivery loop from signals to triggers, triage, build, review and production. Signals include Slack, Microsoft Teams, GitHub, GitLab and meeting notes through MCP. Crew handles channel watch (hourly heartbeat) and explicit requests (mention, DM or webhook) as local sessions.
- **Earlier Crew blog posts.**
  - "Introducing Kiro Crew" (Aug 4, 2026).
  - "How we built a software factory with Kiro Crew to merge 1,000 PRs in a week" (Sep 18, 2026).
  - "Keeping a software factory stable at 1,000 PRs a week" (Oct 26, 2026).

## Why it matters

Bots change Crew from a one-task helper into an agent that keeps working on a goal over days or weeks. It keeps its own memory and workspace, and it can hand work to workers. The homepage shows Crew picking up work from Slack, Teams, GitHub and GitLab, so a team can use it without opening an editor.

## What to try this week

- Read the Bots docs, then set up one bot with a narrow, measurable goal. Examples are "keep nightly builds green" or "reduce flaky tests".
- Check the Running 24/7 and Security pages before leaving a bot running unattended.
- Read the Crew software factory blog post to see how the Kiro team used Crew at scale.

## Sources

- https://kiro.dev
- https://kiro.dev/docs/
- https://kiro.dev/changelog/
- https://kiro.dev/blog/
- https://kiro.dev/docs/cli/headless/
- https://kiro.dev/docs/crew/bots/
