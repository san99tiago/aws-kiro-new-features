# Kiro weekly research (2026-11-19)

Findings from headless Kiro CLI sessions for each surface.


---

# Kiro CLI: weekly findings (2026-11-19)

## What is new

- **CLI 3.5.0 (Nov 17, 2026):** This release adds organization sign-in for MCP servers in V3 sessions.
  - You run `kiro-cli mcp idp setup` with your identity provider's issuer and client ID. Then you open `/mcp` and press `Enter` to sign in once. Every server set to organization sign-in shares that sign-in. Those servers stay disconnected until you do.
  - For an HTTP server whose owner issued Kiro a client ID, `kiro-cli mcp add` now accepts `--oauth-client-id <client-id>`. This does not apply when your organization's registry manages that server's OAuth.
  - You can set `auth.portalUrl` so `kiro-cli login` opens a portal of your choice. Administrators can set it with the `AuthPortalUrl` policy or `auth_portal_url` in `managed-settings.json`. If Kiro cannot use the value, it falls back to the default portal.
- **CLI 3.4.0 (Nov 16, 2026):**
  - In V3 sessions, a `PreToolUse` hook can return `updatedInput` to replace a tool call's inputs before the tool runs. It can still return `allow`, `ask`, or `deny`.
  - A new `PermissionRequest` hook runs when a tool call would ask for permission, so a script can answer the prompt.
  - `/memories` now offers four choices.
  - Cloud sessions resume and list in more places.
  - The release also fixes headless, context window, MCP, search, `/tangent`, `/rewind`, and display issues. The changelog text I read was cut off, so I did not see the details.
- **Local sandbox controls for enterprises (Nov 17, 2026):** Administrators can require sandboxing for commands and local stdio MCP servers in Enterprise Management, which is in preview. Developers need Kiro CLI 3.4.0 or later.
- **Kiro CLI 3.0 launched on Nov 3, 2026.** V3 is the default experience. It includes "Approve for me", spec mode (`/spec new`), `/tangent`, a `/sessions` pane, workflows, cloud sessions (`kiro-cli --cloud`), and memory (`/memories`). Inline shell autocomplete, the CLI desktop app, and the Classic experience are retired. To return to V2, run `kiro-cli --v2` (applies to that launch only). Sessions made in V3 cannot be resumed in V2.
- **Headless mode docs:**
  - Authentication uses the `KIRO_API_KEY` environment variable. API keys are available to Pro, Pro+, Pro Max, and Power subscribers.
  - You run `kiro-cli chat --no-interactive "prompt"`, or pipe the prompt through stdin.
  - A local headless run that names no harness runs V2, with some exceptions. The docs recommend adding `--v3` or `--v2` so the run does not depend on the default.
  - With V3, use `--trust-all-tools` or `--trust-tools=<ids>` to approve tools. In CLI 3.3.0 or later, `--trust-tools` also accepts V2 tool names, `@server` or `@server/tool`, `@builtin`, and `*` or `?` patterns.
  - A first message starting with `@<prompt-name>` runs that prompt, and `@agent-sop:<name>` runs the named SOP (CLI 2.33 or later).
  - V3 non-interactive runs load Hooks from the agent and workspace (CLI 2.27.1 or later). `--trust-all-tools` approves Hook confirmation requests automatically, and `--trust-tools` does not.
  - Governance rules from your administrator, such as MCP restrictions and model access policies, apply to headless sessions too.
  - If a sub-agent's tool call is not allowed by the parent session's policy, a headless run denies it. Adding the sub-agent to `trustedAgents` does not change this.

## Why it matters

- Organization MCP sign-in replaces a separate browser login for each server with one sign-in.
- The new hooks let a script apply team rules to every tool call and answer permission prompts. This helps in CI/CD, where nobody is there to approve.
- The headless docs tell you to name the harness explicitly. This keeps CI runs from changing behavior when the default changes.

## What to try this week

- Run a headless job with an explicit harness and a narrow tool list, for example `kiro-cli chat --v3 --no-interactive --trust-tools=read_file,grep_search "Find all TODO comments in src/"`.
- Write a `PermissionRequest` hook or a `PreToolUse` hook with `updatedInput` for one routine tool call.
- If your organization uses an identity provider, try `kiro-cli mcp idp setup` and sign in once through `/mcp`.
- Try `/spec new` or `/tangent` in a V3 session.

## Sources

- https://kiro.dev/docs/cli/headless/
- https://kiro.dev/changelog/
- https://kiro.dev/blog/
- https://kiro.dev/blog/cli-3/


---

# Kiro IDE: weekly findings (2026-11-19)

## What is new

**IDE release 1.4.236 (Nov 18, 2026), from the changelog:**
- **Install from GitLab.** You can paste a public GitLab URL to install a custom power or import a skill, the same way you do from GitHub. For a self-hosted GitLab, add its host to the `kiroAgent.powers.trustedGitLabHosts` setting first.
- **Permission Request Hooks.** You can create one in the Hook editor. It runs a command just before Kiro would ask you to approve a tool call, so a script can answer routine prompts in a session nobody is watching. Pre Tool Use Hooks can now replace a tool call's input before it runs. Any approval prompt now shows the final arguments.
- **Organization sign-in for MCP.** Eligible HTTP MCP servers can share one sign-in through your organization's identity provider. You add the provider your administrator gives you to your user MCP configuration. Then you select **Sign in** on the **Organization sign-in** row in the MCP Servers view.
- **Chats and Memory settings.** You can move chats between the Side Bar and the Editor Area. You can also choose Memory settings from the Memories view.

**Recent blog posts that touch the IDE (titles and dates only, I did not open the posts):**
- Nov 17: "Lessons learned from one million evaluations"
- Nov 12: "Grok 4.7 is now available in Kiro"
- Nov 10: "Introducing 'Approve for me' in Kiro"
- Nov 6: "How Kiro Auto uses model cascading to match the model to the work"
- Nov 4: "Share Kiro credits across your team with credit pooling"
- Oct 30: "Spec it safe: shift left and harden your specs with security requirements"
- Oct 20: "Introducing memory in Kiro IDE and CLI"
- Oct 14: "Local sandboxing in Kiro: keep agent commands within boundaries"
- Sep 30: "Introducing Kiro workflows"

I found nothing new about specs or steering in the changelog text I could read. The fetch was truncated, so older IDE entries were not visible. I did not fetch kiro.dev, the docs, or the headless page.

## Why it matters

- Permission Request Hooks let unattended sessions handle routine approvals without a person clicking.
- Seeing final arguments in approval prompts makes it clearer what a tool call will do.
- GitLab installs and shared MCP sign-in help teams that do not use only GitHub or that manage many MCP servers.

## What to try this week

- Create a Permission Request Hook in the Hook editor for one low-risk, routine prompt, and check that the script answers it.
- If you use GitLab, install a power or skill from a public GitLab URL.
- If your organization has an identity provider for MCP, add it to your user MCP configuration and try the **Organization sign-in** row.
- Read the "Spec it safe" post to see how to add security requirements to your specs.

## Sources

- https://kiro.dev/changelog/
- https://kiro.dev/blog/
- https://kiro.dev/blog/spec-it-safe/
- https://kiro.dev/blog/memory-in-ide-cli/
- https://kiro.dev/blog/introducing-approve-for-me/
- https://kiro.dev/blog/local-sandboxing/


---

# Kiro WEB: weekly findings (2026-11-19)

## What is new

I found no Kiro Web release notes dated this week. The Nov 19, 2026 changelog entry that I could read is for Kiro Crew 0.13.0. The Nov 18 entry is for Kiro IDE and the Nov 17 entry is for Kiro CLI. The changelog has a Web filter, but the page I fetched did not apply it, so I could not list Web-only entries. Older Web entries may exist that I did not see.

These items from the official pages relate to Kiro Web:

- **Home page:** kiro.dev links to "Explore Kiro Web" under cloud sessions. It says cloud sessions move long-running tasks to the cloud with parallel agents that can run for hours, so work continues when you close your laptop.
- **Pull requests on the home page:** The delivery flow on kiro.dev shows a build step that opens a pull request on GitHub or GitLab. That step is followed by verification with property tests and steering, adversarial review agents, and human review.
- **Autonomous mode in Kiro Web (blog, Sep 14, 2026):**
  - You can assign work by describing a task on app.kiro.dev, adding the `kiro` label to a GitHub issue, or writing `/kiro` in a comment.
  - Kiro clones the repository into an isolated sandbox and breaks the work into steps. It then makes the changes, runs the full test suite, and opens a pull request.
  - Kiro never merges pull requests on its own and cannot bypass branch protection rules. Every pull request needs the same approvals as human code, including CI and code-owner review.
  - When the task is unclear, Kiro asks clarifying questions instead of guessing.
  - AWS teams used it on the Kani and CBMC repositories. They report 94 pull requests in Nov and Dec 2025, of which 35 are merged as of Sep 2026, and zero regressions.
  - The post says the main bottleneck is that Kiro writes pull requests faster than people can review them.
- **Other recent posts that touch Web:** "Agentic engineering in the cloud" (Sep 3), "Close the laptop, keep the agent: building with cloud sessions" (Aug 18), and "Introducing Kiro workflows" (Sep 30). I saw only their titles and did not open them.
- **Specs:** The home page says specs capture intent before code is written and verify results afterward. It lists property-based tests, requirements analysis that catches gaps before design, and Bugfix Specs. It does not say these are Web-specific.

## Why it matters

- Autonomous mode turns a GitHub issue into a reviewable pull request without a developer in the loop. People step in at code review.
- The review queue can become the limit, so plan reviewer time before assigning many issues at once.
- Branch protection and CI still apply. Kiro Web does not skip your normal merge rules.

## What to try this week

- Pick a small issue with clear acceptance criteria, such as a dependency update, a well-reproduced bug, or a docs fix. Add the `kiro` label or comment `/kiro`, then review the pull request like any other.
- Skip architectural changes and large refactors, which the blog says are better left to people.
- Open the changelog and use its Web filter to check for Web entries I could not see.

## Sources

- https://kiro.dev
- https://kiro.dev/changelog/
- https://kiro.dev/changelog/?tag=web
- https://kiro.dev/blog/
- https://kiro.dev/blog/tackling-technical-debt-at-scale-with-autonomous-mode/


---

# Kiro CREW: weekly findings (2026-11-19)

## What is new

- **Kiro Crew 0.13.0 (changelog, Nov 19, 2026).** Conductor mode, formerly Ultra Mode, is now on in every standard build. It no longer needs a Feature Preview switch. The LTS edition does not offer it.
  - The conductor plans from your goal and checks each worker's new work as the crew runs. It re-plans only the item that went wrong.
  - **Pause all** on the Board stops every running worker, sub-teams included, until **Resume all**.
  - **Start New Chats in conductor mode** (Settings, Chat, Sessions) is off by default.
- **Replies from anywhere.** Hover over a session that is waiting on you, or press the right arrow key on it. A card shows its recap, each approval and question in full, and a quick reply box. Notification sources have a new **Deliver to** option. It also sends notes to your Slack, Discord, Telegram, Webex, or Feishu DM. Only critical notes are sent unless you lower the floor.
- **Chat tools.**
  - Reopen the last closed session with Cmd/Ctrl+Shift+T.
  - `/fork <prompt>` continues in a copy of the conversation.
  - **Optimize Before Sending** rewrites your message when you send it.
  - **Preferred Reply Language** sets the language of replies.
  - **Continue automatically** resumes a chat when a usage limit resets.
- **Files and Git panels.** The Files tab opens on **Edited**, which lists the files the chat changed. The Git panel adds **Branch changes**. Artifact versions can be compared side by side.
- **Bots choose their harness.** The **Agent harness** row on a Bot's profile is out of preview. A Bot's Dashboard can be downloaded as HTML. Chats a Bot opens stay off your Sessions list unless you turn on **Show in my Sessions list**.
- **Previews you can turn on (off by default).**
  - Secrets vault redesign.
  - Agent Harness for worker chats, which can start worker chats on another harness such as Claude Code or Codex.
  - Mark out-of-date Dashboard fields.
  - Send pending approvals to chat apps.
  - Kiro Memory. Memories saved by other Kiro clients are read-only in Crew.
- **Changes to check before upgrading.**
  - Release notes moved to Settings, About.
  - MCP Servers now have their own tab under Customize.
  - Usage data is on by default. You can turn it off with `telemetry.enabled: false`, `KIROCREW_TELEMETRY=0`, or `DO_NOT_TRACK=1`.
  - `hooks.batch_write_guard` is on by default.
  - On Linux, external edits to config files that Crew does not recognize wait for your review.
- **Blog, Nov 5, 2026:** "Introducing bots in Kiro Crew." Earlier posts are "Introducing Kiro Crew" (Aug 4) and the software factory post about merging 1,000 PRs in a week (Sep 18).
- **Docs.** The Crew quick start describes Crew as an open-source personal AI agent that runs locally or remotely. It works from the desktop app, web dashboard, CLI, and chat apps such as Slack, Discord, Telegram, Teams, Webex, WeCom, and WeChat. It supports parallel subagents, scheduled jobs, heartbeats, and a Task Runner.

## Why it matters

Conductor mode is now available to everyone on standard builds. A planner can coordinate several workers, check their results, and re-plan only what failed. The quick reply card and chat-app delivery let you answer approvals without sitting at the app. The Bot harness choice and the worker harness preview let a team mix agent engines.

## What to try this week

1. Update to Crew 0.13.0 and read the "Before You Upgrade" notes, especially the usage data default.
2. Turn on conductor mode in a new chat. Give it a multi-part goal, and try **Pause all** and **Resume all** on the Board.
3. Set **Deliver to** for one notification source so approvals reach your chat app.
4. Try `/fork` on a long chat and the **Edited** tab in the Files panel.
5. Enable the **Agent Harness for worker chats** preview to try a worker on another harness.

## Sources

- https://kiro.dev/changelog/
- https://kiro.dev/blog/
- https://kiro.dev/docs/
- https://kiro.dev/docs/crew/
- https://kiro.dev
- https://kiro.dev/docs/cli/headless/ (checked; it had no Crew-specific content)
