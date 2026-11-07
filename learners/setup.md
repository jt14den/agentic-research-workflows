---
title: Setup
---

<style>
pre code { white-space: pre-wrap !important; word-break: break-word !important; overflow-wrap: anywhere !important; }
</style>

To follow this lesson you need [Claude Code][claude-code-docs] and Python on your machine. Claude Code is Anthropic's terminal-based AI coding agent. The steps below set up a direct local install.

If you cannot use Claude Code, for example because you have no supported account, you can still follow the lesson. Ask your instructor for the saved-output route. It uses the same terminal and Python files, with saved plans, diffs and command transcripts. You make the same approval decisions and run the same checks.

Allow 20 to 30 minutes before the workshop for this setup. Your instructor may run a separate setup clinic.

## 1. Install Python and two Python packages

- Python: use the workshop's tested environment and the exact versions your instructor gives you. Current Matplotlib needs Python 3.11 or newer. Check with `python --version`.
- Python packages: the lesson scripts use `pandas` for data and `matplotlib` for the plot. Install both in a project environment and not globally. A `venv`, `pixi` or `uv` environment all work:

```bash
python -m pip install pandas matplotlib
```

A bare, unpinned install is not an environment record. Your instructor will give you the tested versions to record.

## 2. Install Claude Code

Use the native installer first:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

On Windows, use `irm https://claude.ai/install.ps1 | iex` in PowerShell. The shell examples in the lesson use Unix commands, so ask your instructor which route they have tested on Windows. If your institution requires npm, that works too and needs Node.js 22 or newer:

```bash
npm install -g @anthropic-ai/claude-code
```

## 3. Authenticate

Confirm a supported account before the workshop. Claude Code can sign in with a Claude subscription or an Anthropic API key, and your organisation may offer other routes. These are not the only options. Subscription usage and API billing differ. A plan name does not promise that you can complete the workshop. Your instructor provides a fallback if access or quota fails.

```bash
claude
```

On first launch, Claude Code walks you through signing in. It stores your credentials locally.

## 4. Get the project folder

The lesson works in one project: a small, messy, synthetic water quality dataset. The data describe no real study. Download the `coastal-water-quality` folder from the [lesson repository](https://github.com/jt14den/agentic-research-workflows) under `learners/files/coastal-water-quality`, or use the copy your instructor provides. Then move into it:

```bash
cd coastal-water-quality
ls data/
```

You should see `site_A.csv`, `site_B.csv` and `site_C.csv`. Start Claude Code from inside this folder throughout the lesson.

## 5. Setup check

A version number confirms that the program is installed. It does not confirm that you can use it. Run these from inside the `coastal-water-quality` folder:

```bash
pwd                       # the folder you are working in
claude --version          # prints a version number
python --version          # prints Python 3.11 or newer
python -c "import pandas, matplotlib; print('packages ok')"   # prints: packages ok
ls data/                  # site_A.csv  site_B.csv  site_C.csv
```

Then confirm account access with one read-only agent action:

```bash
claude -p "List the files in data/. Do not change anything."
```

If the files come back, you are ready. If any step fails, see the troubleshooting notes below, or tell your instructor so you can use the saved-output route.

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Troubleshooting

- `claude: command not found`: the install did not finish, or your `PATH` is not updated. Re-run the install command and restart your terminal, or run `claude doctor` for a diagnostic.
- `ModuleNotFoundError: No module named 'pandas'`: the packages went to a different Python than the one you run. Use the same interpreter: `python -m pip install pandas matplotlib`.
- Claude Code asks you to sign in again: that is normal on a new machine. Sign in once.
- The agent writes different code than the lesson shows: that is expected. AI output varies. The lesson teaches you to check it and not to match it. If you fall behind, your instructor can share a known-good script from `instructors/files/`.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Use the same model, and record it

Inside a Claude Code session, the `/model` command sets the model. Select the same available model as the rest of the class so outputs are comparable. Then record the resolved model name, the Claude Code version and the relevant settings, which `/status` shows. An alias or an identical selection does not guarantee identical output.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: caution

### Security and working directory

Claude Code runs in your terminal and works with the files in your current folder. Starting in a project folder sets its working context. It does not by itself create a security boundary. Check what the agent can read, write and reach on the network, and which integrations are on. Some habits:

1. Start from a dedicated project folder, not your home folder.
2. Keep files under version control (Git) so you can revert a change.
3. Do not start it in a folder with credentials, private data or sensitive system files.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Running in a sandbox (optional, and untested)

Some researchers isolate the agent from their personal files. The repository's `Dockerfile` and `.devcontainer/` are a starting point, but they have not been rebuilt and smoke-tested with the current Claude Code. Do not rely on them for a workshop. The devcontainer uses its own image and does not use the Dockerfile.

Claude Code's Bash sandbox does not cover every file tool, MCP server or hook, and native Windows and WSL2 differ. Test the exact route you plan to offer. Options to know about:

- Docker: see the [Docker documentation](https://docs.docker.com/), or [Docker AI Sandboxes](https://docs.docker.com/ai/sandboxes/).
- Claude Code's own sandboxing: see the [sandboxing documentation](https://code.claude.com/docs/en/sandboxing). It supports macOS, Linux and WSL2, and it needs less setup than a container. On native Windows, commands run unsandboxed.
- A dedicated agent-isolation tool such as [Agent Safehouse](https://agent-safehouse.dev/).

You do not need any of these for this workshop.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Institutional context and access

Read this section before you use these tools with real research data. Your institution decides which AI tools are approved for which kinds of data.

In this workshop, use only the supplied synthetic data. Do not read permission for institutional research data into a personal subscription or into the name of a campus-approved product.

At UCLA, consult [the current campus tool comparison][ucla-ai-tools] for eligibility, price and data classifications. Approved access is tied to a UCLA account and a specific service. The campus tools listed there are not terminal agents, so they cannot run this lesson.

To use a backend with sensitive data, first get confirmation from the responsible campus or unit authority for the specific account, configuration and data category. A tool that can run on a given cloud service, such as Amazon Bedrock, is not thereby approved for sensitive data.

The campus comparison excludes protected health information from the listed campus AI tools and points eligible UCLA Health users to nebulaOne. Check current policy for other restricted categories.

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Consumer accounts, retention and local transcripts

Retention and data use depend on the account type, the provider and your settings. Check the current policy and do not assume.

- On consumer accounts, a training preference affects how long Anthropic keeps data. Consult [Claude Code's current data usage policy](https://code.claude.com/docs/en/data-usage) for the present figures, because they change.
- Claude Code also keeps local transcripts of your sessions on your machine.
- Commands that share feedback or transcripts are a separate control from your training preference.
- First-party API terms, third-party hosting terms such as those of a cloud provider, and your organisation's settings all differ. Check the arrangement that applies to your backend. Do not apply one retention period to all backends. Cloud providers also describe the customer's own configuration duties, for example in [AWS data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html).

::::::::::::::::::::::::::::::::::::::::::::::::::
