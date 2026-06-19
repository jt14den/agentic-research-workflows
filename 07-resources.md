---
title: "Resources and Next Steps"
teaching: 10
exercises: 15
---

:::::::::::::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Choose an appropriate AI coding tool for a given task and data sensitivity.
- Plan how you will apply this workflow to your own research.
- Know where to keep learning and how to spot hype.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: questions

- Which tool should I reach for, and when?
- How do I take this back to my own data?

::::::::::::::::::::::::::::::::::::::::::::::::::

This episode is a short reference and a plan for what you do next. The detail is deliberately light: the skills you practised (spec, plan, validate, judge, document) transfer across every tool below.

## A tool-choice table

| Tool | What it is | Reach for it when |
|---|---|---|
| **Claude Code** (used in this lesson) | Anthropic's CLI agent | terminal-native work on your real files |
| **Codex CLI** / **Cursor** | OpenAI CLI / AI code editor | you prefer a different vendor or an editor-integrated agent |
| **Aider** + **Ollama** | open CLI agent + local model runner | sensitive data that must stay on your machine, or reproducibility |
| **NotebookLM**, **Elicit**, **Consensus** | document/literature tools | grounding answers in your own PDFs or the literature, not coding |

Local models (run via Ollama) keep data on your hardware and let you pin a frozen version for reproducibility, at the cost of needing a capable GPU. Many researchers use a hybrid approach: a cloud model for general scripting, a local model for sensitive data.

::::::::::::::::::::::::::::::::::::::::: caution

## MCP and the shadow-IT risk

The Model Context Protocol (MCP) lets agents connect to external tools and data sources (databases, file systems, services). It is powerful, but MCP servers are often installed without institutional oversight, and security researchers have shown risks including prompt injection and silent data exfiltration. Before connecting one, check it is actively maintained and from a trusted source, and that your institution's policy covers it.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Citing and crediting AI

Transparent attribution is part of open science. Major standards (COPE, Nature, Elsevier) agree AI tools cannot be authors, because they cannot take accountability. Cite them as methodological tools instead.

- In a repo `README.md`: note the model, its role, and who verified the output (for example, "Claude Sonnet 4.6 drafted the cleaning script; verified by [you] via `validate_data.py`").
- In a manuscript: name the model in methods or acknowledgements, and keep prompts and outputs available.
- References: [COPE on AI authorship](https://publicationethics.org/cope-position-statements/ai-author), [Elsevier AI policy](https://www.elsevier.com/about/policies/publishing-ethics/usage-of-ai-tools-in-writing-for-research), [CRediT taxonomy](https://credit.niso.org/).

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: your Monday workflow card

Pick one real scenario from your own work, then fill out a short plan you could actually use next week. A ready-made template, `monday-worksheet.md`, ships with the lesson (in `learners/files/`); open it and fill it in.

Choose a scenario: a small public CSV, sensitive human-subjects data, large geospatial files, or an existing messy repository.

For it, write down:

1. **Tool and backend:** which tool, and (if your data is sensitive) which approved backend?
2. **What the AI can see / must not touch:** the no-go zones for your `CLAUDE.md`.
3. **First prompt:** your "plan only, no code yet" opener.
4. **Validation:** the one check that would most likely catch a silent error in this task.
5. **Provenance:** where you will record model, date, and prompt.

:::::::::::::::::::::::::::::::::::::::: solution

A good card is specific to your data. The validation line is the tell: if you cannot name a check that would fail when the result is wrong, you do not yet understand the task well enough to delegate it. That is fine, it just means you start by understanding, not generating.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Spotting hype

New tools appear daily, and many are more marketing than substance. Before adopting one:

- **Scope:** beware tools that claim to do everything; specialised tools usually work better.
- **Transparency:** can you see the intermediate steps, or just the answer?
- **Citations:** does it give real, checkable DOIs and URLs?
- **Privacy:** if it is free, is your data used for training?

A few sources that stay practical and skeptical: [Simon Willison](https://simonwillison.net/) (AI engineering and security), [Ethan Mollick](https://www.oneusefulthing.org/) (AI and cognitive work), [Hamel Husain](https://hamel.dev/) (systematic evaluation), and [The Batch](https://www.deeplearning.ai/the-batch/) (balanced industry coverage).

For the tool used here, see the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code).

:::::::::::::::::::::::::::::::::::::::: keypoints

- The workflow transfers across tools; match the tool and backend to the task and data sensitivity.
- Attribute AI use transparently; it cannot be an author.
- Leave with a concrete plan for your own data, including the one check that would catch a silent error.

::::::::::::::::::::::::::::::::::::::::::::::::::
