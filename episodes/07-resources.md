---
title: "Resources and Next Steps"
teaching: 15
exercises: 25
---

:::::::::::::::::::::::::::::::::::::::::::::::::: questions

- Which tool should I reach for, and when?
- How do I take this back to my own data?

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: objectives

- Pick an AI tool for a task and a data category, and say what evidence supports the choice.
- Draft a workflow plan for one of your own datasets: tool, backend, no-go zones, opening prompt, check, provenance record and one unchecked claim.
- Spot signs of AI hype using a stated set of criteria (scope, transparency, citations, privacy).

::::::::::::::::::::::::::::::::::::::::::::::::::

This episode is a short reference and a plan for what you do next. The skills you practised transfer across tools: state requirements, plan, check, judge and document.

## A short tool table

Tools change fast. Treat this table as examples, and check each tool's current documentation before you rely on it.

| Tool | What it is | Reach for it when |
|---|---|---|
| Claude Code (used in this lesson) | A command-line agent | terminal-native work on your real files |
| Codex CLI, Cursor | A command-line agent, an AI code editor | you prefer another vendor or an editor-integrated agent |
| Aider with a local model runner | An open command-line agent with a model on your machine | you need data to stay on your machine |
| NotebookLM, Elicit, Consensus | Document and literature tools | you want answers grounded in your own PDFs or the literature, and not coding |

Hardware needs for a local model depend on the model and the speed you want. Test your chosen setup. Many researchers use a cloud model for general scripting and a local model for sensitive data. Whether any given tool is approved for your data is your institution's call.

::::::::::::::::::::::::::::::::::::::::: challenge

## Quick check: which pairing gives you pause?

1. Claude Code, for cleaning a public, already-published dataset.
2. A local model, for a pipeline you must rerun in five years.
3. Claude Code on its default cloud backend, with no institutional approval, for a first pass on sensitive, unpublished human-subjects data.
4. NotebookLM, for questions grounded in a folder of your own PDFs.

:::::::::::::::::::::::::::::::::::::::: solution

**3.** Sending sensitive, unpublished human-subjects data to a general cloud endpoint with no approval behind it is the pairing to avoid. "Which approved backend" on the workflow card asks you to settle that before you start.

The others are reasonable. Public data carries no sensitivity limit (1). For (2), the key step is to archive the code, inputs, environment and commands so the pipeline reruns without a model. A pinned local model helps only if model inference is part of the analysis. A document tool used on your own files is what it was built for (4).

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: caution

## External tools and connectors

The Model Context Protocol (MCP) lets agents connect to external tools and data sources. Many servers are installed without institutional review. Prompt injection and data leaks remain real risks. Treat a server's tool descriptions and returned data as untrusted input. Before you connect one, check that it is maintained and comes from a source you trust, limit its file and network access, and confirm that your institution's policy covers it. Being listed in a registry does not show that a server is safe.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Citing and crediting AI

Transparent credit is part of open science. Follow the target publisher's current disclosure policy, and keep enough provenance to explain AI's role. Major publishers and COPE say that AI tools cannot be authors, because they cannot be held accountable.

- In a repository `README.md`: note the tool, its role and who verified the output. For example: "Claude drafted the cleaning script. [Your name] verified it with `validate_data.py`."
- In a manuscript: name the tool in the methods or acknowledgements, and keep prompts and outputs available.
- Check the current policy: [COPE on AI authorship](https://publicationethics.org/cope-position-statements/ai-author), [CRediT taxonomy](https://credit.niso.org/).

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: your Monday workflow card

Pick one real scenario from your own work and fill in a short plan you could use next week. The lesson ships a template, `monday-worksheet.md`, in `learners/files/`. Open it and fill it in.

Choose a scenario: a small public CSV, sensitive human-subjects data, large geospatial files, or an existing messy repository.

Write down:

1. Tool and backend. Which tool, and for sensitive data, which approved backend? Name your evidence source, such as the campus policy page.
2. What the AI can see and must not touch. These are the no-go zones for your `CLAUDE.md`. Note how access is enforced, not only requested.
3. First prompt. Your "plan only, no code yet" opener.
4. One likely error and the check that would catch it.
5. Provenance. Where you will record the tool version, model, date and prompt, and where you will archive the code, data, environment and commands.
6. One unchecked claim. What are you still taking on trust?

:::::::::::::::::::::::::::::::::::::::: solution

A good card is specific to your data. The check line is the test. If you cannot name a check that would fail when the result is wrong, you do not yet understand the task well enough to hand it off. That is fine. It means you start by understanding, not by generating.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Spotting hype

New tools appear daily, and many are more marketing than substance. Before you adopt one, ask:

- Scope. Be wary of tools that claim to do everything. Specialised tools often work better.
- Transparency. Can you see the intermediate steps, or only the answer?
- Citations. Does it give real DOIs and URLs you can check?
- Privacy. If it is free, is your data used for training?

::::::::::::::::::::::::::::::::::::::::: challenge

## Quick check: spot the hype

For each description, name the criterion it fails most clearly.

1. "Answers any research question instantly, in any field, with no setup."
2. "Summarises your uploaded PDFs and gives you a final answer. You do not need to see the search or the reasoning."
3. "Free forever. Sign up and start uploading your data today."

:::::::::::::::::::::::::::::::::::::::: solution

1. Scope. A tool with no stated domain limits often has little depth in any one domain.
2. Transparency. If you cannot see the intermediate steps, you cannot check the work. You can only trust the answer.
3. Privacy. A free tool that asks for your data and says nothing about what happens to it is the case this criterion exists for. Check before you upload.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

Some sources that stay practical and skeptical: [Simon Willison](https://simonwillison.net/) (AI engineering and security), [Ethan Mollick](https://www.oneusefulthing.org/) (AI and cognitive work), [Hamel Husain](https://hamel.dev/) (systematic evaluation) and [The Batch](https://www.deeplearning.ai/the-batch/) (industry news).

For the tool used here, see the [Claude Code documentation][claude-code-docs]. For the terms used in this lesson, see the [learner reference page](../learners/reference.md).

:::::::::::::::::::::::::::::::::::::::: keypoints

- The workflow transfers across tools. Match the tool and backend to the task and the data category.
- Credit AI use openly. It cannot be an author.
- Leave with a plan for your own data, including one check that would catch a likely error.
- Before adopting a tool, check its scope claims, transparency, citations and privacy terms.

::::::::::::::::::::::::::::::::::::::::::::::::::
