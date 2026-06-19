---
title: Setup
---

To follow this lesson, you will need [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and Python installed on your machine. Claude Code is Anthropic's terminal-based AI coding agent. The steps below get you set up with a direct local install, which is the approach used throughout the lesson.

## 1. Install Node.js and Python

- **Node.js**: Download the LTS version from [nodejs.org](https://nodejs.org) or use a package manager (`brew install node` on macOS).
- **Python**: Ensure you have Python 3.9+ installed. Check with `python --version`.

## 2. Install Claude Code

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

::::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Keep everyone on the same model

Inside a Claude Code session you can set the model with the `/model` command (for example, `claude-sonnet-4-6`). Pinning the whole class to one model keeps outputs comparable and makes provenance records meaningful. Your instructor will tell you which model to select.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: caution

### Security and working directory

Claude Code runs in your terminal and has direct access to the files in your current folder. A few habits to keep in mind:

1. Always start it from a dedicated project folder, not your home directory.
2. Keep files under version control (Git) so you can revert unwanted changes.
3. Never start it in folders with sensitive system files, credentials, or private data.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Running in a sandbox (optional)

Some researchers prefer to isolate the agent from their personal files entirely. Two options worth knowing about:

- **Docker**: The lesson repository includes a `Dockerfile` that builds a container with the agent pre-installed. It can only see files you explicitly mount into it. See the [Docker documentation](https://docs.docker.com/) for setup, or [Docker AI Sandboxes](https://docs.docker.com/ai/sandboxes/) for a purpose-built option.
- **Agent Safehouse**: [agent-safehouse.dev](https://agent-safehouse.dev/) is a dedicated environment for running AI agents with built-in isolation controls.

Both approaches require more setup and are not needed for this workshop, but are worth exploring if you plan to use these tools regularly with sensitive data.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Institutional context and access

This is the most important section to read before using these tools with real research data. Your institution decides which AI tools are approved for which kinds of data.

**At UCLA**, the centrally provided free AI tools (Gemini Basic, Microsoft Copilot, ChatGPT web) are **web-only** and approved for data classified **P1-P3** (P4 requires CISO/Unit Head approval). They are not terminal agents and cannot run this lesson. See [UCLA's available AI tools list](https://dts.ucla.edu/initiatives/ai/available-tools) for the current details and data-tier rules.

For the terminal workflow this lesson teaches, there are two paths:

- **Personal plan or API key (P1-P3, non-sensitive data).** A personal Claude Pro/Max subscription or Anthropic API key. This is the simplest setup and what most workshop exercises assume. Do not use it with sensitive or restricted research data.
- **UCLA Amazon Bedrock (sensitive data).** Claude Code can run against Anthropic models hosted in **Amazon Bedrock**, which UCLA provides as an enterprise, privacy-bounded service. The same lesson commands work; only the backend changes. Use this path for P3/P4 research data, and confirm your unit's Bedrock access and data-tier approval first. See your instructor or UCLA DTS for setup.

**Always follow your institution's data privacy policies.** PHI and attorney-client privileged information are not approved for these tools; UCLA Health users should use the HIPAA-compliant alternative (nebulaOne).
