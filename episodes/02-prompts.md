---
title: "Best Practices for Prompting"
teaching: 40
exercises: 35
---

<style>
pre code { white-space: pre-wrap !important; word-break: break-word !important; overflow-wrap: anywhere !important; }
</style>

:::::::::::::::::::::::::::::::::::::::: questions

- How do I write effective prompts?
- How do I review a plan before the agent acts on it, not just after?
- What are common AI failures?
- How can I make the AI fix its own mistakes, and when should I not trust that it has?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Refine a vague prompt into one with context, specificity, and output instructions.
- Use Claude Code's plan mode to review an agent's approach before it writes any files.
- Use introspection to refine AI-generated code.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Working inside Claude Code

All prompts in this episode are typed inside an active Claude Code session. Start one in your project folder before the exercises:

```bash
cd coastal-water-quality
claude
```

Then type prompts directly at the prompt. Shell commands (like `python script.py`) are run in a separate terminal window, or from inside the session by prefixing the line with `!`.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Five principles of effective prompting

Effective prompting is clear technical communication. To get the best results, start by being specific. Include constraints, filenames, and a description of your expected output. Vague requests lead to generic answers, while precise instructions result in usable code.

Provide context. Explain why you need the code and what data you have (e.g., "I am processing a CSV file with these columns..."). This helps the AI understand the goal. Specify outputs clearly, tell the AI where to save files or how to format tables.

Treat prompting as an iterative process. Start with a simple request and add complexity in follow-up prompts. Include validation steps by asking the AI to verify or test its own work.

::::::::::::::::::::::::::::::::::::::::: callout

## The CO-STAR framework

*Optional on a first pass. CLEAR (below) is enough to start; reach for CO-STAR when a prompt gets complex.* While CLEAR helps with conversation flow, CO-STAR structures complex research prompts that eventually become part of your `CLAUDE.md`:

*   **Context**: Provide background (e.g., "I am a biologist analysing RNA-seq data").
*   **Objective**: Define the specific task ("Write a script to normalise these counts").
*   **Style**: Specify the coding style ("Use the Tidyverse style guide in R").
*   **Tone**: Set the personality ("Be concise and prioritise readable code").
*   **Audience**: Who is this for? ("For a graduate student who knows R but not bioinformatics").
*   **Response**: Define the format ("A single R script with comments and a plot output").

::::::::::::::::::::::::::::::::::::::::::::::::::

## The Bootstrap Workflow

Instead of writing a full `CLAUDE.md` by hand, use the **Bootstrap Workflow**. This lets the agent assist in defining the project spec from the start.

1.  **Scan**: Ask the agent to scan your directory and data files.
2.  **Draft**: Ask the agent to write an initial `CLAUDE.md` based on what it sees and your high-level goal.
3.  **Gate**: You review, edit, and approve the spec before any code is written.

::::::::::::::::::::::::::::::::::::::::: callout

## Example bootstrap prompt
"Scan the CSV files in `data/raw/`. Based on my goal of 'Analysing water quality trends', draft an `CLAUDE.md` file that defines the column schema, required libraries, and a plan for cleaning the data."

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Concrete example: From bad to good

| Aspect | Bad prompt | Good prompt |
| :--- | :--- | :--- |
| Vague vs specific | "Clean this data." | "In `data.csv`, remove rows with missing values in the 'age' column and save as `clean_data.csv`." |
| No context vs context | "Write a plot script." | "I am building a report for a climate study. Write a Python script using seaborn to create a line plot of 'temp' over 'year' from `results.csv`." |
| Silent vs validated | "Run a t-test." | "Perform a paired t-test between 'pre' and 'post' columns. Print the t-statistic, p-value, and an interpretation of the result at alpha=0.05." |

::::::::::::::::::::::::::::::::::::::::::::::::::

## Prompts that preserve learning

Good prompting is technical communication, but in a learning setting it is also *learning design*. A prompt can be specific and well-formed and still rob you of the understanding you came to build. The prompts below are written to keep you in the loop: the AI helps, but you still do the thinking that makes the result yours.

Prompts that preserve learning:

- "Do not give me the final code yet. Ask me three questions about the data first."
- "Give me a plan using only concepts we have covered so far."
- "Write the simplest possible version. Avoid list comprehensions, classes, and external libraries."
- "Explain what assumptions you are making about my data."
- "Give me one small change to make myself, and tell me where to make it."
- "Ask me to predict the output before you show me the answer."
- "Give me a hint, not the solution."

::::::::::::::::::::::::::::::::::::::::: callout

## Prompts to avoid, and what to ask instead

The prompts on the left feel efficient but hand over the parts that make code trustworthy. The versions on the right keep you able to explain and validate the result.

| Avoid | Ask instead |
| :--- | :--- |
| "Do this exercise for me." | "Walk me through how to approach this; do not write the final answer." |
| "Fix everything." | "List the problems you see, ranked. I will choose which to fix first." |
| "Make this production ready." | "Name the three biggest risks in this script for research use." |
| "Clean this data." | "Tell me what inconsistencies you find in these files. Do not change anything yet." |
| "Write the whole pipeline." | "Outline the pipeline in steps. We will build and check one step at a time." |

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Instructor note: watch for cognitive load

Generated prompts often pull in syntax, libraries, or abstractions the lesson has not introduced. Signs that AI output is adding extraneous load:

- The agent uses an advanced feature (comprehensions, classes, decorators) before it has been taught.
- It imports a library that is not installed locally.
- It writes several files when one short script would do.
- It buries the core logic under heavy comments.
- The answer is correct but the learner cannot explain it.

Interventions: ask the learner to request a simpler version, to remove one abstraction, to trace the code line by line, or to compare it with a minimal reference solution. Slowing down here is the lesson, not a detour.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching tip: Visual aids
Write CLEAR vertically on a whiteboard. As you explain each letter, add the keyword (Concise, Logical, Explicit, Adaptive, Reflective). This helps students remember the framework.

::::::::::::::::::::::::::::::::::::::::::::::::::

## The CLEAR framework

The CLEAR framework, developed by [Leo Lo](https://doi.org/10.1016/j.acalib.2023.102720), provides a structured approach to prompt engineering:

```mermaid
graph LR
    accTitle: The CLEAR prompting loop
    accDescr {Effective prompts move from Concise to Logical to Explicit to Adaptive to Reflective, with a feedback loop from Reflective back to Adaptive when the output needs another pass.}
    C[Concise] --> L[Logical]
    L --> E[Explicit]
    E --> A[Adaptive]
    A --> R[Reflective]
    R -->|Feedback Loop| A
    style R fill:#bbf,stroke:#333,stroke-width:2px
```

The diagram traces the CLEAR loop, from Concise to Logical to Explicit to Adaptive to Reflective, with a feedback arrow from Reflective back to Adaptive. Effective prompts are concise and logical, prioritising important information and following a sequence of steps. They are also explicit, specifying the scope, persona, and tone of the output. When the AI produces poor results, be adaptive by rephrasing or splitting tasks. Finally, be reflective, evaluate the output and verify facts using other sources rather than trusting the response.

## Introspection

The CLEAR framework guides your input, but you can also force the AI to critique its own output. This is often called self-correction.

::::::::::::::::::::::::::::::::::::::::: instructor

## The introspection concept
Emphasize this section. Most learners treat AI output as final. The idea that they can ask the AI to fix its own work is often a new concept. It is like asking a student, "Are you sure you checked your work?", they often find their own mistakes when asked.

::::::::::::::::::::::::::::::::::::::::::::::::::

Asking the AI to review its own code often surfaces problems, but it cannot decide which problems matter for your research; that judgement stays with you. Never accept the first draft. Follow up with an introspection prompt:

*   "Review the code you just wrote. Are there any edge cases or security vulnerabilities?"
*   "Did you hardcode any file paths?"
*   "Critique your own implementation. Is there a more efficient way?"

### Reasoning effort

*Optional: useful once you are comfortable with the basics.* Frontier models no longer split cleanly into separate "standard" and "reasoning" model families the way they did in 2025. The current generation instead lets you turn up a reasoning-effort setting on the same model. In Claude Code this is the `effort` setting (`low` through `xhigh`, with `max` on some models); the default is `high`, which suits most complex reasoning and coding work.

**When to raise it:**

- Reach for more effort when a task has multiple interacting constraints, or chains many steps of tool use together, not just because it "feels hard."
- Leave it at the default for routine formatting, quick scripts, and brainstorming.
- Higher isn't free: it costs more time and tokens, and on some tasks it can lead to overthinking rather than a better answer. Check your session's `/status` for the exact model and effort level in use, since both change over time.

At higher effort levels, a model already does more internal reasoning before answering, so you often need less explicit introspection prompting than you would at a lower setting.

## Plan before you act

As tasks grow more complex, asking the agent to write code immediately leads to more rewrite time. Claude Code has an actual enforced planning mode for this, not just a prompting convention: use it rather than relying on the agent to honor a polite request.

### Use plan mode, not just a polite request

Start a session in plan mode from the command line:

```bash
claude --permission-mode plan
```

You can also switch into plan mode mid-session; check `/help` or your installed version's documentation for the current way to do that, since the exact command has changed across releases. While in plan mode, the agent can read files and reason, but is blocked from writing files or running mutating commands, no matter what it decides to do. That is a real difference from a prompt like "do not write any files yet": a prompt is a request the agent usually follows but is not required to, while plan mode is enforced by the tool itself.

Review the plan, push back on steps you disagree with, and ask for alternatives. When you are satisfied, exit plan mode and let the agent proceed.

### Checkpoint prompts

Break large tasks into explicit phases so you review the output at each stage before moving forward. This is useful whether or not you are in plan mode, since it scopes what the agent does even after you have approved the overall plan:

```
Step 1 only: read the three CSV files and tell me what inconsistencies you find. Do not write any code yet.
```

This is especially valuable in research because it catches misunderstandings about your data before they propagate into broken code.

### The plan file

For complex projects, ask the agent to write a `PLAN.md` first:

```
Write a PLAN.md outlining the steps to clean and merge these files. I will review and edit it before you write any code.
```

This makes the plan a reviewable, editable artefact, a more formal version of the Bootstrap Workflow. Once approved, refer back to it in follow-up prompts: "Proceed with step 2 from PLAN.md."

::::::::::::::::::::::::::::::::::::::::: callout

## Plan files vs. the Living Spec

A `PLAN.md` and your `CLAUDE.md` serve different purposes. The spec defines persistent rules and constraints that apply across all sessions. The plan describes the steps for a specific task. Keep them separate: plans are temporary, specs are durable.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Plan before you clean

Practise using plan mode before moving on to the data cleaning episode. Start (or switch into) plan mode, then inside your Claude Code session, type:

```
Read the three site files in data/. They have inconsistent column names and date formats. Outline a step-by-step plan for cleaning and merging them into a single dataset.
```

You do not need to add "do not write any files yet" here — plan mode already guarantees that. Review the plan. Does it include an audit step? Does it address missing values? Revise the plan in the conversation until you are satisfied, then exit plan mode and save it by asking: "Write this plan to PLAN.md."

:::::::::::::::::::::::::::::::::::::::: solution

## What a good plan includes

- An **audit step**, inspect files before changing them
- A **schema harmonisation step**, standardise column names
- A **date standardisation step**
- A **missing value strategy**
- An **output verification step**

If the agent skipped any of these, ask it to revise before you proceed. The goal is to catch gaps in the plan, not in the code.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## AI failures

AI agents are designed to be helpful, which can lead them to take shortcuts.

### Common failure modes

*   **Determinism collapse:** Small variations in prompts or model updates can lead to different outputs for the same task, which affects reproducibility.
    *   *Fix:* There isn't a setting that makes an agentic run reproducible — tool calls, retries, and file-system state all vary run to run regardless of sampling settings. Instead, log the exact model, prompt, and relevant outputs (a provenance header, see the next episode) so a different run can be compared, not guaranteed identical.
*   **Over-correction loops:** If an agent runs its own tests, it might fix the test to match its buggy code.
    *   *Fix:* Write your own requirements and key tests.
*   **Synthetic data substitution:** The AI may generate fake data if it cannot find the real file.
*   **Silent failure:** The AI uses `try/except` blocks that hide errors.

:::::::::::::::::::::::::::::::::::::: discussion

## How to catch failures

Have you seen an AI make a confident mistake? In your research, what signs indicate the AI is hallucinating?

**Common strategies:**

*   Always ask: "Show me the first 10 rows of the data you loaded."
*   Demand proof: "How did you calculate that p-value? Show the intermediate steps."
*   Check file sizes: Is the cleaned file 0 bytes?

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The prompt refinement loop

Practise the CLEAR framework on a file you already have: one raw site file, `data/site_A.csv`. (You have not cleaned the data yet, so use the raw column names.)

1.  **Start with a vague prompt**, type this inside your Claude Code session:
    ```
    Plot my data.
    ```
    *Observe: Does it work? Which file did it use? Is the plot useful? Where did it save it?*

2.  **Refine the prompt:**
    Write a new prompt that applies context (what the data is), specificity (which file and columns, scatterplot with a trendline), and output instructions (where to save it).

:::::::::::::::::::::::::::::::::::::::: solution

## Example refined prompt

```
Using data/site_A.csv, create a Python script that plots WaterQualityScore over Collection_Date as a scatterplot with a linear trendline. Label the axes. Save the plot to fig/site_A_trend.png (create the directory if it does not exist).
```

### Reflection: prompt refinement

*   How much longer was your refined prompt compared to your first one?
*   Did defining the output filename save you from searching for the file?
*   Extra typing time can save debugging time.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The introspection loop

Test the AI as a verifier principle. Ask the AI to find flaws in its code before you run it.

1.  **Generate a script**, type this prompt inside your Claude Code session:
    ```
    Write a Python script that reads 'data.csv' and calculates the rolling 7-day average of a 'score' column. Handle missing values.
    ```
2.  **Force introspection:** Once the code is generated, do not run it. Follow up in the same session:
    ```
    Review the rolling average script you just wrote. Are there any edge cases (like having fewer than 7 days of data) where this would fail? If so, provide an updated version.
    ```
3.  **Compare:** Did the AI find a mistake in its first draft? Did it add a guard clause like `min_periods=1`?

:::::::::::::::::::::::::::::::::::::::: solution

### Reflection: introspection loop

A second, critique-focused pass often catches issues the first draft missed. Treat it as a prompt to look harder yourself, not as a guarantee the code is now correct.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: paste one line you don't understand

In the shared Etherpad, paste one line of AI-generated code from this episode that you cannot fully explain yet. We will pick a few and work through them together. There is no penalty for not understanding a line; the penalty is shipping it without knowing what it does.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: keypoints

- Be specific and provide context.
- Plan before you act: use plan mode so the agent can't write files until you approve its approach, not just a prompt asking it to wait.
- Prefer prompts that preserve learning: ask for plans, hints, and the simplest version, not the finished answer.
- Always validate AI outputs, and never ship a line you cannot explain.
- Introspection can surface issues the first draft missed, but it is not a guarantee of correctness; treat what it finds as something to verify, not proof.

::::::::::::::::::::::::::::::::::::::::::::::::::
