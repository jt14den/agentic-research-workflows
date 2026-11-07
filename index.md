---
title: "Agentic Research Workflows: AI Coding, Validation, and Research Responsibility"
start: true
---

### Plans, CLI agents, and a four-layer validation stack

This lesson introduces researchers to working with AI (artificial intelligence) coding agents without giving up the learning, feedback, checking and research judgement that make code trustworthy. AI changes what you need to practise. You spend less time recalling syntax and more time understanding intent, dependencies, assumptions, tests and failure modes.

The lesson does not replace research thinking, and it does not aim to code faster. It teaches you to judge whether AI-generated code is correct for your data and your research question, and to document that judgement so the work can be reproduced.

## From vibes to research judgement

"Vibe coding" is an informal term for guiding AI with natural-language prompts and intuition. Intuition is where people start, but research demands evidence as well as output. This lesson teaches a workflow built around recorded requirements, a validation stack and an explicit approval gate.

Throughout, "orchestration" means active review and not passive delegation. You stay the reviewer, tester and domain judge.

### What the workflow asks of you

- You read the code, question its assumptions and decide whether it is correct. A short instruction file (`CLAUDE.md`) records the constraints it must follow.
- You define what the data should look like, and why, before generation. Then you can tell when the generated code drifts from your intent.
- A result is not done because it runs. It is done when you can explain it and show evidence that it is correct.

### What it does not do

- It does not validate your research question or choose your methods.
- It does not detect subtle statistical or causal errors by default.
- It does not reduce your responsibility for the final output.

Using AI to generate code is research-adjacent work. It becomes research when it sits inside a process of validation, documentation and justification.

## Three ways of working with AI

You practise three methods on one synthetic dataset:

1. Ask AI to help you understand. Predict what a script does, ask for an explanation, and compare it with the data.
2. Delegate one small change. Read the plan, the action and the diff, and compare the result with an expectation you chose yourself.
3. Test and hand off a result. Write a check, show that it fails on bad data, and have another person rerun your work without AI.

## Two ways to use this lesson

- A four-hour pilot route for researchers who use basic Python and tabular data. The instructor notes give the timed agenda.
- The full eight-episode course, about nine and a half hours of material before breaks and installation.

:::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites

- Basic familiarity with the command line.
- Python with pandas. You have cleaned a CSV and can read a short script that selects columns, filters rows, handles missing values and parses dates.
- No prior experience with AI coding agents is needed.
- No account? A saved-output route lets you follow the same tasks and checks.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Learning objectives

At the end of this lesson, you will be able to:

- Tell code generation, code understanding and code validation apart, and explain why AI-generated code can raise a novice's cognitive load.
- Use a CLI agent with a short instruction file (`CLAUDE.md`) to plan and generate research code, reviewing each step instead of accepting it wholesale.
- Validate an AI-generated result with runnable checks (invariants and domain plausibility), show that a check fails on bad data, and decide whether to approve, revise or reject.
- Document an AI-assisted workflow (requirements, checks, environment, commands and provenance) so another researcher can rerun and judge the result.

## Acknowledgements

This lesson is adapted from the workshop "Vibe Coding for Research" developed by Bruno Smaniotto and Tom van Nuenen at the UC Berkeley D-Lab.

The original materials are at [dlab-berkeley/Vibe-Coding-for-Research](https://github.com/dlab-berkeley/Vibe-Coding-for-Research).
