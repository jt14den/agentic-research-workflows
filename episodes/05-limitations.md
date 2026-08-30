---
title: "Limitations and Cautions"
teaching: 30
exercises: 20
---

:::::::::::::::::::::::::::::::::::::::: questions

- When should I not use AI?
- What are common failure modes?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: objectives

- Identify a hallucinated package name using the official package registry.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## The jagged frontier

AI capability is inconsistent. A model may solve a complex differential equation but fail a simple logic puzzle. Researchers must identify where AI is reliable and where it is a liability for their specific field.

::::::::::::::::::::::::::::::::::::::::::::::::::

## When not to trust AI code

Using AI-generated code can introduce risks to research integrity. Security-critical tasks, like authentication, encryption, or handling sensitive data, require expert oversight.

AI may also fail when research involves new statistical methods or domain-specific details. Models synthesise information from training data, which might not include the latest breakthroughs or specific sensor patterns. In performance-critical code, AI often prioritises common algorithms over the most efficient ones, which can cause bottlenecks in large-scale processing.

::::::::::::::::::::::::::::::::::::::::: callout

## When not to use AI in a workshop exercise

The goal of this lesson is not "never use AI." It is to use AI where it supports learning and rigor, and to step back where it does not. Avoid AI when:

- The exercise is designed to build basic syntax fluency. Generating the answer skips the practice that builds the skill.
- You cannot yet explain the output. If you cannot judge it, you cannot use it responsibly.
- The data are sensitive and the tool's privacy terms are unclear.
- The task involves security, authentication, encryption, access control, or regulated data.
- The model keeps introducing concepts beyond the scope of the lesson.
- Reaching for AI prevents the instructor from seeing where the group is actually stuck.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## When AI can support learning

AI is genuinely useful when it helps you understand, not when it replaces understanding. Good uses include:

- Explaining an error message you are stuck on.
- Generating a simpler example of a concept you just met.
- Asking you concept-check questions before you answer.
- Comparing two possible solutions so you can choose.
- Suggesting tests for code you already understand.
- Helping you document code *after* you understand what it does.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Common failure modes

Understanding AI failure modes helps you identify errors before they affect results.

### Spec Drift
Spec Drift occurs when the code and the `CLAUDE.md` (Living Spec) become unaligned. The agent may fix a bug in the code but forget to update the spec, leading to future hallucinations.
- *Prevention:* Regularly ask the agent to "Sync the spec with the current code."

### Bootstrap Failures
In the "Bootstrap Workflow," the AI may miss nuances in raw data during the initial scan. If you approve a flawed spec, the error will propagate through the entire project.
- *Prevention:* Thoroughly audit the agent's first draft of `CLAUDE.md`.

### Silent semantic drift
Semantic drift occurs when an agent makes a change that alters data assumptions or logic without breaking the code.
- *Example:* The code runs and tests pass, but a filtering threshold was changed or a column was renamed incorrectly, affecting the research conclusion.
- *Prevention:* Use metamorphic testing and invariant checks to ensure core logic remains unchanged.

### Other failure modes
*   **Hallucinated functions:** The model uses libraries or APIs that do not exist.
*   **Outdated approaches:** The AI uses deprecated syntax from its training data.
*   **Confident incorrectness:** The AI presents wrong formulas or logic as certain.
*   **Tool poisoning via MCP:** When an agent calls external tools through MCP, a misconfigured or malicious MCP server can inject instructions into the agent's context (prompt injection) through its tool descriptions or returned data, even from a server that is otherwise sandboxed. This can cause the agent to take unintended actions or leak data. Mitigation: only install MCP servers from trusted, audited sources; treat everything a server returns as untrusted input, not just the server itself; and sandbox with minimal filesystem/network access where you can. Registry listing (MCP now has an official one) is not a safety certification.
*   **Over-engineering:** The model generates complex code for simple problems.

:::::::::::::::::::::::::::::::::::::: discussion

## Environmental cost

Data centers consume large amounts of electricity and water. Frequent, iterative prompting can be resource-intensive.

*   **Energy use:** Every AI query requires complex calculations, and running them costs real electricity and water. Published estimates of exactly how a single query compares to a web search vary widely by methodology and model size, and the comparison is genuinely disputed, but the underlying point holds regardless of the exact multiplier: iterative, exploratory prompting has a real resource cost that a single web search does not.
*   **Code efficiency:** AI models often prioritise working code over efficient code. Inefficient software uses more energy and resources over time.

### Sustainable practices

To code responsibly:

1.  **Think before prompting:** Use the CLEAR framework to get the right answer in fewer attempts.
2.  **Request optimisation:** Prompt the AI to optimise for memory or speed once the logic is correct.
3.  **Use documentation:** If you need simple syntax, check the documentation instead of querying an LLM.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Managing expectations
Current models tend to flag uncertainty more often than older ones, but they still hallucinate. Do not promise learners it won't happen.
*   **If it refuses:** Acknowledge that the model correctly identified its own limitations.
*   **Backup:** Have a screenshot of a known hallucination ready to show if the AI performs perfectly during the session.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Test for hallucinations, then verify independently

Inside your Claude Code session, type:

```
How do I use the 'pypanda-researcher' library to automatically write my conclusion?
```

Note whether the model admits it does not know, hedges with uncertainty, or confidently invents instructions. Then check for yourself, independent of what the model told you: search PyPI (or your language's package index) for `pypanda-researcher`. Record what you find and the date you checked. Would you accept, revise, or reject the model's answer based on that evidence, not on how confident it sounded?

:::::::::::::::::::::::::::::::::::::::: solution

## Discussion

Current models are somewhat better at flagging uncertainty than earlier generations — you may get a clean "this doesn't exist" response, and that's the correct behaviour when it happens. But don't count on it: a 2026 study testing five frontier models found they still hallucinate nonexistent package names 4.6-6.1% of the time, and more surprisingly, 127 of those hallucinated package names were invented *identically* by all five models ([Churilov, 2026](https://arxiv.org/abs/2605.17062)). That second finding matters for your validation habits specifically: asking a different model to double-check a package name is weaker protection than it sounds, because current models increasingly confabulate the same wrong answers, not different ones. The lesson here is not that hallucination always happens, but that you cannot assume it won't, and cross-checking with another model is not a substitute for checking the official package registry or documentation directly.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Open science and proprietary AI

Claude Code is not open source, which creates a tension in open research.

*   **Proprietary models (Gemini, GPT, Claude):** These are closed-weight models. You cannot verify their training data, and they may update silently. Institutional agreements provide data privacy but do not solve reproducibility issues.
*   **Open-weight models (e.g. Qwen3, Gemma, OpenAI's gpt-oss):** These can be run locally using tools like Ollama. They offer better reproducibility because you can pin a specific, frozen model revision — though license terms still vary by model, so check them alongside the version. "Open-weight" is the precise term here: the weights are downloadable, but that alone doesn't make the system open source under the fuller definition (training data, code, and license may still be closed or restricted).

**Recommendation:**
There is no blanket right answer between proprietary and open-weight for prototyping and cleaning. Base the choice on your data's classification and authorization, the task's reproducibility and auditability needs, and cost, not on a default. Whichever you use, archive the generated code rather than relying on the model to regenerate the same result later.

::::::::::::::::::::::::::::::::::::::::: callout

## Key lesson

AI can generate code, but it does not take on your expertise or your responsibility. Your work shifts towards understanding, questioning, and verifying the code the AI produces. The accountability for the result stays with you.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: certainty vs evidence

In the shared Etherpad, post one thing an AI tool told you this session that it made sound certain, but that you have not actually verified. These are the items most worth a second look.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Avoid AI for security-critical tasks, sensitive data, and basic syntax practice.
- Know when AI supports learning and when it gets in the way.
- You are responsible for the final output.
- Open-weight models offer better reproducibility (a pinned revision); the right choice for a task still depends on data sensitivity, auditability, and cost, not a default.

::::::::::::::::::::::::::::::::::::::::::::::::::
