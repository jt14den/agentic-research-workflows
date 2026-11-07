---
title: "Limitations and Cautions"
teaching: 25
exercises: 20
---

:::::::::::::::::::::::::::::::::::::::: questions

- When should I not use AI?
- Which failure modes can pass a quick look?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: objectives

- Name situations where AI help gets in the way of learning or of research integrity.
- Describe spec drift and silent semantic drift, and the checks that catch them.
- Check a package name against the official registry before you trust a model's answer.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Pilot route

The four-hour pilot does not teach this episode as its own block. It folds the scope and privacy points into Episode 1 and the failure modes into Episodes 2 and 4. Use this episode in the extended course, or as a follow-on.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## The jagged frontier

AI capability is uneven. A model may solve a hard differential equation and fail a simple logic puzzle. You need to find where AI is reliable and where it is a liability in your own field.

::::::::::::::::::::::::::::::::::::::::::::::::::

## When not to trust AI code

AI-generated code can put research integrity at risk. Security-critical tasks such as authentication, encryption and sensitive data need expert oversight.

AI can also fail on new statistical methods or domain details. A model draws on its training data, which may not cover recent work or your specific sensor. In performance-critical code, it often picks a common algorithm over the most efficient one.

::::::::::::::::::::::::::::::::::::::::: callout

## When not to use AI in a workshop exercise

The goal is not "never use AI." Use it where it supports learning and rigour, and step back where it does not. Avoid AI when:

- The exercise builds basic syntax fluency. A generated answer skips the practice.
- You cannot yet explain the output. If you cannot judge it, you cannot use it responsibly.
- The data are sensitive and the tool's privacy terms are unclear.
- The task involves security, authentication, encryption, access control or regulated data.
- The model keeps bringing in ideas beyond the lesson.
- Reaching for AI stops the instructor from seeing where the group is stuck.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## When AI can support learning

AI helps most when it helps you understand, and not when it replaces understanding. Good uses:

- Explaining an error message you are stuck on.
- Giving a simpler example of a concept you just met.
- Asking you concept-check questions before you answer.
- Comparing two solutions so you can choose.
- Suggesting tests for code you already understand.
- Helping you document code after you understand what it does.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Common failure modes

Knowing the failure modes helps you catch errors before they reach your results.

### Spec drift

Spec drift happens when the code and your requirements stop matching. An agent may change the code to make a check pass, or may fix a bug and leave the requirements out of date.

- Prevention: compare the implementation with your approved requirements. If the code disagrees, do not just ask the agent to sync the requirements to the code. That can make an unintended change official. Decide whether the code or the requirement is wrong. Propose and justify any change to a requirement, and name the evidence that supports it.

### Silent semantic drift

Semantic drift is a change that alters your data assumptions or logic without breaking the code.

- Example: the code runs and the checks pass, but a filter threshold changed, or a column was renamed wrongly, and the research conclusion shifts.
- Prevention: use invariant and metamorphic checks, and keep your own checks independent of the code under test.

### Other failure modes

- Hallucinated functions. The model uses libraries or APIs that do not exist.
- Outdated approaches. The AI uses deprecated syntax from its training data.
- Confident incorrectness. The AI states a wrong formula or logic as certain.
- Prompt injection through tools. When an agent calls external tools, for example through MCP, a misconfigured or malicious server can slip instructions into the agent's context through its tool descriptions or returned data. Install servers only from sources you trust and have reviewed. Treat everything a server returns as untrusted input, and limit its file and network access. Being listed in a registry does not certify that a server is safe.
- Over-engineering. The model writes complex code for a simple problem.

:::::::::::::::::::::::::::::::::::::: discussion

## Resource cost

Data centres use large amounts of electricity and water. Frequent, iterative prompting has a resource cost. A web search has one too.

No model-specific comparison between an AI query and a web search was verified for this lesson, and published estimates vary widely with method and model size. The qualitative point holds: working code is not always efficient code, and inefficient software uses more resources over time.

Sustainable habits:

1. Think before you prompt. A clear prompt can get the right answer in fewer attempts.
2. Ask for optimisation once the logic is correct.
3. Read the documentation when you need simple syntax.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Managing expectations

Current models flag uncertainty more often than older ones, but they still hallucinate. Do not promise learners that it will not happen.

- If the model refuses or hedges, point out that it recognised its own limit.
- Keep a screenshot of a known hallucination ready in case the AI performs perfectly during the session.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: test for a hallucination, then verify independently

Inside your Claude Code session, type:

```
How do I use the 'pypanda-researcher' library to automatically write my conclusion?
```

Notice whether the model admits it does not know, hedges, or invents instructions with confidence. Then check for yourself, without relying on the model. Search PyPI for `pypanda-researcher`. Record what you find and the date you checked. Would you accept, revise or reject the model's answer based on that evidence and not on how confident it sounded?

A package that exists on the registry is not therefore the package you wanted. Existence does not prove identity, safety or fit.

:::::::::::::::::::::::::::::::::::::::: solution

## Discussion

You may get a clean "this does not exist." That is the right answer when it happens, but do not count on it.

A 2026 study of five frontier models, using its own prompts, found that they invented nonexistent package names about 4.6 to 6.1 percent of the time. 127 of the invented names were produced identically by all five models ([Churilov, 2026](https://arxiv.org/abs/2605.17062)). Those are rates for that study's models and prompts, and not current universal failure rates.

The second finding bears on your habits. Asking another model to double-check a package name is weaker protection than it sounds, because models can invent the same wrong name. Check the official registry or the documentation directly.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Open science and proprietary AI

Claude Code is not open source. That creates a tension in open research.

- Closed-weight models (Claude, GPT, Gemini). You cannot inspect their training data, and they may be updated without notice. An institutional agreement can cover data privacy. It does not solve reproducibility.
- Open-weight models (for example Qwen3, Gemma, gpt-oss). You can run them locally with a tool such as Ollama and keep a specific revision. Licence terms vary by model, so check them with the version. "Open-weight" means the weights can be downloaded. It does not make a system open source in the fuller sense, because training data, code and licence may still be closed.

**Recommendation.** No blanket choice fits prototyping and cleaning. Decide from your data's classification and authorisation, the task's reproducibility and audit needs, and cost. Whichever you use, archive the generated code, the inputs, the dependencies and the commands, so the analysis reruns without the model. If model inference is part of the analysis, also preserve the model files and inference settings, and test that results repeat.

::::::::::::::::::::::::::::::::::::::::: challenge

## Quick check: which model class fits?

For each scenario, would a closed-weight or an open-weight model, run locally, fit better? Say why.

1. A throwaway exploratory script you will discard today.
2. A pipeline that must reproduce its output in five years for a methods reviewer.
3. A first pass on de-identified patient records, at an institution with an approved, contracted AI tool.

:::::::::::::::::::::::::::::::::::::::: solution

1. Either. Cost and convenience decide. Nothing about the task needs reproducibility or data controls.
2. The key step is to archive the generated code, the inputs, the environment and the commands, so the pipeline reruns without any model. A pinned open-weight model helps only when inference is part of the analysis.
3. Whichever tool your institution has approved for that data. An institutional agreement can cover privacy and compliance. It does not by itself settle reproducibility. Both questions can apply to one project.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Key lesson

AI can generate code. It does not take on your expertise or your responsibility. Your work shifts toward understanding, questioning and verifying what the AI produces. You remain accountable for the result.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: certainty and evidence

In the shared Etherpad, post one thing an AI tool told you this session with certainty that you have not verified. Those items deserve a second look. Working alone? Write it in your notes file, then go and verify it before you move on.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Avoid AI for security-critical tasks, sensitive data and basic syntax practice.
- Know when AI supports learning and when it gets in the way.
- Compare code with your approved requirements. Do not sync the requirements to the code without evidence.
- Check a package against the official registry. Existence on the registry is not proof of fit.
- Archive code, inputs, environment and commands so your analysis reruns without the model.
- You are responsible for the final output.

::::::::::::::::::::::::::::::::::::::::::::::::::
