---
title: Setup
---

<style>
pre code { white-space: pre-wrap !important; word-break: break-word !important; overflow-wrap: anywhere !important; }
</style>

To follow this lesson, you will need [Claude Code][claude-code-docs] and Python installed on your machine. Claude Code is Anthropic's terminal-based AI coding agent. The steps below get you set up with a direct local install, which is the approach used throughout the lesson.

## 1. Install Python and two Python packages

- **Python**: Ensure you have Python 3.11+ installed (current Matplotlib requires it). Check with `python --version`.
- **Python packages**: the lesson scripts use `pandas` (data handling) and `matplotlib` (the trend plot). Install both, ideally in a project-scoped environment rather than globally (a `venv`, `pixi`, or `uv` environment all work):

```bash
python -m pip install pandas matplotlib
```

## 2. Install Claude Code

Use the native installer as your primary path:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

(Windows: `irm https://claude.ai/install.ps1 | iex` in PowerShell.) If your institution requires installing via npm instead, that also works, but needs Node.js 22 or newer:

```bash
npm install -g @anthropic-ai/claude-code
```

## 3. Authenticate

How you authenticate depends on which path you are using (see "Institutional context and access" below). For the workshop, most learners will sign in with a personal Claude account:

```bash
claude
```

On first launch, Claude Code walks you through signing in. A Claude Pro or Max subscription, or an Anthropic API key, will work. The credentials are stored locally; you will not need to repeat this step.

## 4. Verify the install

```bash
claude --version
```

If you see a version number, you are ready. If the command is not found, restart your terminal and try again.

## 5. Get the project folder

The whole lesson works in one project: a small, messy water quality dataset. Download the `coastal-water-quality` folder that ships with this lesson (from the [lesson repository](https://github.com/jt14den/agentic-research-workflows) under `learners/files/coastal-water-quality`, or from a copy your instructor provides), then move into it:

```bash
cd coastal-water-quality
ls data/
```

You should see `site_A.csv`, `site_B.csv`, and `site_C.csv`. Throughout the lesson, start Claude Code from inside this folder.

## 6. Setup check

Run these from inside the `coastal-water-quality` folder. Each should produce the output shown:

```bash
claude --version          # prints a version number
python --version          # prints Python 3.11 or newer
python -c "import pandas, matplotlib; print('packages ok')"   # prints: packages ok
ls data/                  # site_A.csv  site_B.csv  site_C.csv
```

If all four work, you are ready. If any fails, see the troubleshooting notes below.

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Troubleshooting

- **`claude: command not found`**: the install did not finish or your `PATH` is not updated. Re-run the install command and restart your terminal, or run `claude doctor` for a diagnostic.
- **`ModuleNotFoundError: No module named 'pandas'`**: the packages went to a different Python than the one you are running. Use the same interpreter: `python -m pip install pandas matplotlib`.
- **Claude Code asks to sign in again**: that is normal on a new machine; complete the sign-in once.
- **The agent produces different code or output than the lesson shows**: that is expected, AI output varies. The lesson teaches you to check it, not to match it. If you fall behind, your instructor can share a known-good script from `instructors/files/`.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Keep everyone on the same model

Inside a Claude Code session you can set the model with the `/model` command. Pinning the whole class to one model keeps outputs comparable and makes provenance records meaningful. Your instructor will tell you which model to select (check `/status` to confirm the exact model and version once you've set it).

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: caution

### Security and working directory

Claude Code runs in your terminal and has direct access to the files in your current folder. A few habits to keep in mind:

1. Always start it from a dedicated project folder, not your home directory.
2. Keep files under version control (Git) so you can revert unwanted changes.
3. Never start it in folders with sensitive system files, credentials, or private data.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Running in a sandbox (optional, and currently untested)

Some researchers prefer to isolate the agent from their personal files entirely. The repository's `Dockerfile` and `.devcontainer/` are a starting point for that, but as of this writing they have not been rebuilt and smoke-tested against the current Claude Code toolchain — don't rely on them working out of the box for a workshop. Options worth knowing about generally:

- **Docker**: see the [Docker documentation](https://docs.docker.com/), or [Docker AI Sandboxes](https://docs.docker.com/ai/sandboxes/) for a purpose-built option, and expect to update this repo's `Dockerfile` yourself before using it.
- **Claude Code's own sandboxing**: see the [sandboxing documentation](https://code.claude.com/docs/en/sandboxing) for filesystem/network isolation options built into the tool itself, which need less setup than a full container.
- **Agent Safehouse**: [agent-safehouse.dev](https://agent-safehouse.dev/) is a dedicated environment for running AI agents with built-in isolation controls.

None of these are needed for this workshop. If you want a tested container path, budget time to rebuild and verify the `Dockerfile` first.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Institutional context and access

This is the most important section to read before using these tools with real research data. Your institution decides which AI tools are approved for which kinds of data.

**At UCLA**, the centrally provided free AI tools (Gemini Basic, Microsoft Copilot, ChatGPT web) are **web-only** and approved for data classified **P1-P3** (P4 requires CISO/Unit Head approval). They are not terminal agents and cannot run this lesson. See [UCLA's available AI tools list][ucla-ai-tools] for the current details and data-tier rules.

For the terminal workflow this lesson teaches, there are two paths:

- **Personal plan or API key (P1-P3, non-sensitive data).** A personal Claude Pro/Max subscription or Anthropic API key. This is the simplest setup and what most workshop exercises assume. Do not use it with sensitive or restricted research data.
- **UCLA Amazon Bedrock (sensitive data).** Claude Code can run against Anthropic models hosted in **Amazon Bedrock**, which UCLA provides as an enterprise, privacy-bounded service. The same lesson commands work; only the backend changes. Use this path for P3/P4 research data, and confirm your unit's Bedrock access and data-tier approval first. See your instructor or UCLA DTS for setup.

**Always follow your institution's data privacy policies.** PHI and attorney-client privileged information are not approved for these tools; UCLA Health users should use the HIPAA-compliant alternative (nebulaOne).

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### What does a personal Pro/Max subscription actually give you?

The two paths above differ in a way that is easy to miss: they are governed by different terms with different defaults, not just different backends.

- **Personal Pro/Max/Free (Consumer Terms):** you get an explicit, changeable choice whether your conversations, including Claude Code sessions, are used to train future models — set it at [claude.ai/settings/data-privacy-controls](https://claude.ai/settings/data-privacy-controls). That choice changes how long Anthropic retains your data: **5 years if training is on, 30 days if it is off.** Even with training off, Claude Code also keeps a local plaintext copy of session transcripts on your own machine for 30 days by default. The `/feedback`, `/bug`, and `/share` commands are a separate path: they send your actual conversation history, including code, to Anthropic regardless of your training setting, unless you disable it.
- **UCLA Amazon Bedrock and other commercial/API paths (Commercial Terms):** training on your data is contractually prohibited by default, not a toggle you set. Standard retention is 30 days; Zero Data Retention is available to qualifying Enterprise accounts.

If you are using a personal subscription for this workshop, check your own setting rather than assuming: see [Claude Code's current data usage policy](https://code.claude.com/docs/en/data-usage) for the full, current breakdown by account type.

::::::::::::::::::::::::::::::::::::::::::::::::::
