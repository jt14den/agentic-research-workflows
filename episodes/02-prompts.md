---
title: "Best Practices for Prompting"
teaching: 25
exercises: 30
---

:::::::::::::::::::::::::::::::::::::::: questions

- How do I write a prompt that gets a result I can check?
- How do I review a plan before the agent acts on it?
- How do common AI failures show up, and how do I catch them?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: objectives

- Repair a vague prompt so it states the input, the intended change, the constraints and the evidence you will accept.
- Review an agent's plan, mark one unsupported assumption and approve only a bounded action.
- Name common AI failure modes and a check for each.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Working inside Claude Code

Type the prompts in this episode inside an active Claude Code session. Start one in your project folder:

```bash
cd coastal-water-quality
claude
```

Run shell commands such as `python script.py` in a separate terminal, or inside the session by starting the line with `!`.

::::::::::::::::::::::::::::::::::::::::::::::::::

## A short prompt checklist

Effective prompting is clear technical communication. A good prompt names four things:

1. Input: which files and columns the agent should use.
2. Intended change: what should happen.
3. Constraints: what must not happen, and the facts the data documentation gives you.
4. Evidence: how you will check the result.

Vague requests produce generic answers. Precise ones produce code you can test. Start with a small request and add detail in follow-up prompts.

The table shows each item at work.

| Aspect | Weak prompt | Better prompt |
| :--- | :--- | :--- |
| Input and change | "Clean this data." | "In `data/site_C.csv`, convert `DateTime` to ISO `YYYY-MM-DD`. Do not change any other column." |
| Constraint | "Fix the dates." | "Site C dates are day-month-year. Parse them with `%d-%m-%Y` and do not let pandas guess." |
| Evidence | "Make sure it works." | "After the change, print SC001's date. It must be 2023-01-05." |

The CO-STAR framework is an optional way to structure longer prompts. It is on the [reference page](../learners/reference.md).

## Prompts that preserve learning

A prompt can be specific and still take away the understanding you came to build. These prompts keep you in the loop. The AI helps, and you still do the thinking that makes the result yours.

- "Do not give me the final code yet. Ask me three questions about the data first."
- "Write the simplest version. Avoid list comprehensions, classes and extra libraries."
- "State the assumptions you are making about my data."
- "Give me one small change to make myself, and tell me where."
- "Ask me to predict the output before you show it."
- "Give me a hint, not the solution."

::::::::::::::::::::::::::::::::::::::::: callout

## Prompts to avoid, and what to ask instead

The left column feels efficient but hands over the parts that make code trustworthy.

| Avoid | Ask instead |
| :--- | :--- |
| "Do this exercise for me." | "Walk me through how to approach this. Do not write the final answer." |
| "Fix everything." | "List the problems you see, ranked. I will choose which to fix first." |
| "Make this production ready." | "Name the three biggest risks in this script for research use." |
| "Clean this data." | "Tell me what inconsistencies you find in these files. Do not change anything yet." |
| "Write the whole pipeline." | "Outline the pipeline in steps. We will build and check one step at a time." |

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Instructor note: watch for cognitive load

Generated code often brings in syntax, libraries or abstractions the lesson has not introduced. Signs that AI output is adding extra load:

- The agent uses an advanced feature, such as a comprehension, a class or a decorator, before it has been taught.
- It imports a library that is not installed.
- It writes several files where one short script would do.
- The answer is correct and the learner cannot explain it.

Ask the learner to request a simpler version, remove one abstraction, trace the code line by line or compare it with a minimal reference. Slowing down here is the lesson, not a detour.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: repair a prompt

Start with this prompt, typed inside your Claude Code session:

```
Plot my data.
```

Notice which file it used, whether the plot is useful and where it saved it. Then write a repaired prompt that states the four checklist items for `data/site_A.csv`: the input (file and columns), the intended change (a scatterplot of `WaterQualityScore` over `Collection_Date`), the constraints (label the axes, do not change the data) and the evidence you will accept (the output path and the number of points plotted).

:::::::::::::::::::::::::::::::::::::::: solution

## Example repaired prompt

```
Using data/site_A.csv, write a Python script that plots WaterQualityScore over
Collection_Date as a scatterplot. Label the axes. Do not modify the data file.
Save the plot to fig/site_A_scatter.png and print the number of points plotted.
```

Check that the printed count matches the number of rows with a score. Missing scores are not plotted, so the count may be one less than the row count.

Did naming the output path save you from searching for the file? Did the evidence line give you something to check?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

Many people find the CLEAR checklist (Concise, Logical, Explicit, Adaptive, Reflective, from [Leo Lo](https://doi.org/10.1016/j.acalib.2023.102720)) a useful reminder once they have repaired a prompt like this. It says: be concise, order your steps, state scope and format, rephrase or split a task when the result is poor, and check the output against other sources.

## Plan before you act

For a larger task, asking for code at once costs more rewrite time. Ask for a plan first and review it.

### Plan mode

Claude Code has a plan mode. Start a session in it with:

```bash
claude --permission-mode plan
```

You can also switch modes in a session. Check `/help` for your version, because the command has changed between releases. Plan mode restricts source edits and supports exploration. It is not a universal no-side-effect sandbox. Check the installed mode, the available tools and your settings. Keep the active mode and the approved scope visible while you work.

Review the plan, push back on steps you disagree with and ask for alternatives. When you are satisfied, approve one bounded action and let the agent continue.

### Checkpoint prompts

Break a large task into phases and review each one:

```
Step 1 only: read the three CSV files and tell me what inconsistencies you find. Do not write any code yet.
```

This catches misunderstandings about your data before they spread into broken code.

### The plan file

For a complex task, ask the agent to write the plan to a file that you can read and edit:

```
Write a PLAN.md outlining the steps to clean and merge these files. I will review and edit it before you write any code.
```

`PLAN.md` and `CLAUDE.md` do different jobs. The instruction file holds rules that last across sessions. The plan holds the steps for one task. Plans are temporary, and instructions are durable.

:::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: review a plan against the evidence

In plan mode, type:

```
Read the three site files in data/ and README.md. They have inconsistent column names and date formats. Outline a step-by-step plan for cleaning and merging them into data/master_dataset.csv. Do not write files.
```

Review the plan:

1. Mark one step that rests on an assumption the files do not support.
2. Revise that step from the evidence in the files and `README.md`.
3. Write down the single action you approve, such as "write `clean_and_merge.py` and run it on a copy."

:::::::::::::::::::::::::::::::::::::::: solution

## What a good plan includes

- An audit step that inspects the files before changing them.
- A step that harmonises column names.
- A date step that names each site's format.
- A missing-value rule.
- A step that checks the output.

If the plan guesses a date format, a column meaning or a missing-value rule, send it back with the evidence that corrects it. The aim is to catch gaps in the plan and not only in the code.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## AI failures

AI agents are built to be helpful, and that can lead them to take shortcuts.

### Common failure modes

- Run-to-run variation. The same task can give different output across runs or after a model update. No setting makes an agentic run reproducible. Log the tool version, the model, the prompt and the relevant outputs so you can compare runs. A log lets you compare. It does not guarantee identical output.
- Over-correction loops. An agent that runs its own tests may change the test to match its buggy code. Write your own requirements and key checks.
- Synthetic data substitution. The agent may invent data if it cannot find the real file.
- Silent failure. The agent may wrap code in `try/except` blocks that hide errors.
- Plausible wrong results. Output can look right and be wrong, as the date exercise in Episode 0 showed.

:::::::::::::::::::::::::::::::::::::: discussion

## How to catch failures

Have you seen an AI make a confident mistake? What signs tell you an answer is wrong?

Strategies to try:

- Ask: "Show me the first 10 rows of the data you loaded."
- Ask: "How did you calculate that value? Show the intermediate steps."
- Check file sizes. Is the cleaned file 0 bytes?
- Run an independent check you wrote from the source documentation.

:::::::::::::::::::::::::::::::::::::::::::::::::

### Asking the agent to review its own work

You can ask an agent to critique its output:

- "Review the code you just wrote. Which edge cases could make it fail?"
- "Did you hard-code any file paths?"

This often surfaces problems. It cannot decide which problems matter for your research. Treat what it finds as something to verify and not as proof.

### Reasoning effort

Some models let you raise a reasoning-effort setting. Availability and defaults depend on the model, the tool version and your organisation's settings. Use the setting your workshop tested, and record it. Check `/status` for the model and effort in use, since both change over time. Higher effort costs more time and tokens, and it does not always give a better answer.

:::::::::::::::::::::::::::::::::::::: challenge

## Challenge: ask for a check, then read it

Ask the agent to draft a check for the coastal data:

```
Write a short Python script, check_site_C_dates.py, that reads data/site_C.csv and prints the ISO date for SC001 and SC002, using the day-month-year format. Do not change any files.
```

1. Before you run it, predict both dates.
2. Read the script. Which line sets the date format? Did the agent use the format the documentation gives?
3. Run it. Do the printed dates match your prediction? If the agent let pandas guess, how would you tell?

:::::::::::::::::::::::::::::::::::::::: solution

SC001 should print `2023-01-05` and SC002 `2023-01-12`. The script should name `%d-%m-%Y` explicitly.

If the script lets pandas infer the format, the output can still look plausible. Your prediction is what shows the difference. A prediction written before the run is evidence. A check that only confirms the output looks like a date is not.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: paste one line you don't understand

In the shared Etherpad, paste one line of AI-generated code from this episode that you cannot fully explain. We will work through a few together. Not understanding a line carries no penalty. Shipping it without knowing what it does does. Working alone? Ask the agent to explain the line, then check its explanation against what you already know before you accept it.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: keypoints

- Name four things in a prompt: input, intended change, constraints and evidence.
- Review the plan before the agent acts. Mark an unsupported assumption and approve one bounded action.
- Plan mode restricts source edits. It is not a universal sandbox.
- Prefer prompts that preserve learning: ask for plans, hints and the simplest version.
- An agent's self-review is a lead to check, not proof.

::::::::::::::::::::::::::::::::::::::::::::::::::
