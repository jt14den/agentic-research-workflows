---
title: "Agentic Research Workflows: AI Coding, Validation, and Research Responsibility"
start: true
---

### Natural-language specifications, CLI agents, and a four-layer validation stack

This lesson introduces researchers to working with AI coding agents without giving up the learning, feedback, validation, and research judgment that make code trustworthy. AI changes *what you need to practice*: less time recalling every line of syntax, more time understanding intent, dependencies, assumptions, tests, and failure modes.

The focus is not on replacing research thinking, and not on coding faster. It is on judging whether AI-generated code is correct for your data and your research question, and on documenting that judgment so the work is reproducible.

## From 'Vibes' to Research Judgment

The term "vibe coding" (coined by Andrej Karpathy) describes the early 2023-2024 shift toward guiding AI with natural-language prompts. Intuition is where people start, but research demands evidence, not just output. This lesson teaches a disciplined workflow built around a **Living Spec**, a validation stack, and an explicit approval gate.

Throughout, the word "orchestration" means *active review*, not passive delegation. You remain the reviewer, tester, and domain judge.

### What the workflow asks of you

- **Active reviewer, not just author**: You still need to understand the code. Your job is to read it, question its assumptions, and decide whether it is correct, using a **Living Spec (CLAUDE.md)** to record the constraints it must follow.
- **Specification before generation**: You spend time defining what the data should look like and why, so you can tell when generated code drifts from your intent.
- **Evidence before approval**: A result is not done because it runs. It is done when you can explain it and show it is correct.

### What it does not do

- Validate your research question or choose your methods.
- Detect subtle statistical or causal errors by default.
- Reduce your responsibility for the final output.

Using AI to generate code is research-adjacent labor. It becomes research only when embedded in a disciplined process of validation, documentation, and justification.

:::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites

- Basic familiarity with the command line.
- Fundamental understanding of Python (variables, functions, scripts).
- No prior experience with AI coding agents is required.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Learning Objectives

By the end of this lesson, participants will be able to:

- Manage changes across a project using CLI-based AI agents.
- Orchestrate agents using a **Living Spec (CLAUDE.md)**.
- Apply a four-layer validation stack (requirements, tests, metamorphic checks, **domain plausibility**).
- Implement approval gates to prevent fatigue and spec drift.
- Track the provenance and reproducibility of agent-generated results using Git.

## Acknowledgements
This lesson is adapted from the workshop "Vibe Coding for Research" developed by Bruno Smaniotto and Tom van Nuenen at the UC Berkeley D-Lab. 

The original materials can be found at [dlab-berkeley/Vibe-Coding-for-Research](https://github.com/dlab-berkeley/Vibe-Coding-for-Research).
