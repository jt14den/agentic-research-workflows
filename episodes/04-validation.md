---
title: "Validation Strategies: The Approval Gate"
teaching: 35
exercises: 60
---

:::::::::::::::::::::::::::::::::::::::::::::::::::: questions

- What evidence makes AI-generated code safe to approve?
- What can rewrite time tell me about my workflow, and what can it not?
- How do I know my own check would catch a wrong result?

::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: objectives

- Given an AI-generated script, state the evidence supporting it, name the missing evidence, and decide to approve, revise, or reject.
- Describe the four-layer validation stack (recorded requirements, automated checks, metamorphic tests, domain plausibility).
- Write one independent check in `validate_data.py` from the source documentation.
- Show that a check fails on bad data and passes on good data.

::::::::::::::::::::::::::::::::::::::::::::::::::

## The approval gate

When an agent writes your code, you spend more of your time reading, questioning and approving. The approval gate is the point where you decide a result is good enough to use.

This gate supports one decision: whether to accept a bounded piece of code. Passing it does not validate your study design or your scientific claim.

:::::::::::::::::::::::::::::::::::::::::::::::::::::: callout

## A review cycle

1. Write the requirements.
2. Let the agent implement one bounded change.
3. Run checks you trust.
4. Read the changes and decide.

The agent's confidence is not evidence. Your checks are.

::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Rewrite time: a signal, not a score

Rewrite time is the effort, in minutes, you spend making AI output ready to trust. It is useful if you keep its limits in mind.

One timing on one task says little about productivity in general. People also misjudge their own productivity. A 2025 survey of 868 scientists who program, revised in 2026, found that *feeling* productive with a generative AI tool was linked to less programming experience and less use of testing and code review. The strongest predictor was how many lines of generated code a person accepted at once ([O'Brien et al.][obrien-2026]). The survey measures perceived productivity. It does not show better correctness or a causal speed-up.

Treat rewrite time as a signal about this workflow on this task:

- It is local.
- High rewrite time usually means the task was underspecified, the model overreached, or you did not yet have the mental model to judge the output.
- It tells you what to improve next: the prompt, the requirements, or the checks.

::::::::::::::::::::::::::::::::::::::::: caution

## Do not turn rewrite time into a productivity claim

A low rewrite time on one script does not show that AI saved you time. It leaves out the time you spent prompting, reviewing, debugging and validating. It also says nothing about whether the result is correct.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: discussion

## Think aloud while you work

Work in pairs. One person uses the AI for five minutes on a small task, such as adding one check to the cleaning script. Say out loud what you expect, what you trust and where you hesitate.

The observer takes notes. Where did the worker hesitate? Where did they trust the output without checking? Where did they backtrack?

Then discuss as a group. Which one change to the prompt, the requirements or the checks would have helped most?

Working alone? Keep a two-column log: what you expected before each step, and what you had to change afterward.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## The four-layer validation stack

### Layer 1: Recorded requirements

Write down what the result must satisfy before the agent writes code. Put the requirements in your `CLAUDE.md` so you and the agent can both read them.

*Example from our project:* "Do not change the column names in `data/site_*.csv`" and "Do not drop any rows: the merge must have 60."

A requirement in a Markdown file is a request. It does not stop the agent from breaking it. Tool permissions and isolation enforce access limits. Tests show whether the output meets the requirements.

### Layer 2: Automated checks you can run

Write checks that run. A check turns "it looked fine" into "these checks passed." Your project ships `validate_data.py` with most checks written and one left for you.

Take your expected values from the raw files and the documentation. Do not take them from the cleaning script. If the script contains the error, a check that copies its logic copies the error.

### Layer 3: Metamorphic and invariant checks

Test relationships in your data that should never change.

- An invariant: the merged file has 60 rows (3 sites x 20 samples), and no `sample_id` is lost.
- A metamorphic check: if you shuffle the input rows, the merged mean score does not change.

### Layer 4: Domain plausibility

This is where your research expertise counts. A check can pass while the science is wrong. A water quality score above 100 is impossible. Site C's January samples should not appear in May.

The clearest case is the date trap. If you miss it, the cleaning runs, the row count is right, and the trend you plot is still wrong.

::::::::::::::::::::::::::::::::::::::::: callout

## Validation is yours to own

- You cannot validate code you cannot explain. If you cannot say what it does, you are hoping.
- Passing tests is not the same as being scientifically correct. Tests check what you thought to check.
- A second model is a reviewer, not an authority. It has its own blind spots.
- Domain plausibility is your job. No model knows what a sensible result looks like in your field better than you do.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: write one independent check

Open `validate_data.py`. Six checks exist. Five are written for you. One is a stub: every sample's date matches the raw source.

An unfinished check makes the script exit with an error. Run it now and read what it reports.

1. Open `README.md` and find each site's date format. Write them down. Do not copy them from `clean_and_merge.py`.
2. Write the date check yourself, or ask the agent for a draft and read every line before you trust it. Re-parse each raw site file with its documented format and compare the result with `data/master_dataset.csv`, sample by sample. A check that only confirms the dates parse and fall in 2023 is too weak. A misparsed site C date still looks like a valid 2023 date.
3. Run `python validate_data.py`. Fix the data or the cleaning script until every check passes. Never edit a value to satisfy a check. A passing run looks like this, captured from the reference validator (`instructors/files/backup_validate_data.py`, which has eight checks):

   ```
   [PASS] row count is 60
   [PASS] all canonical columns present
   [PASS] every original sample_id is present exactly once
   [PASS] every sample_id carries its source site
   [PASS] every sample's date matches the raw source
   [PASS] every score is a number within 0-100 (none blank or text)
   [PASS] observed scores are unchanged and missing scores use the site median
   [PASS] pH and temp_c keep their source values (blanks stay blank)

   All 8 checks passed.
   ```

4. Now test the check. Copy `data/master_dataset.csv` to `data/candidate.csv`. In the copy, make site C's dates month-first, as `pd.to_datetime(..., format="mixed")` would read them. Run `python validate_data.py data/candidate.csv`. A good date check fails:

   ```
   [FAIL] every sample's date matches the raw source - 8 mismatch(es), e.g. ['SC001', 'SC002', 'SC006']
   ```

   The run does not crash. The plot would not bunch site C at one edge either. Only some rows are wrong, because `format="mixed"` guesses each date on its own and gets some right by accident.

5. Delete `data/candidate.csv`. Confirm `data/master_dataset.csv` is still the correct output, and run the validator on it once more.

If everything still passes in step 4, your date check is too weak.

::::::::::::::::::::::::::::::::::::::::::::::::::: solution

A good date check rebuilds the expected date for each sample from the raw file and compares it exactly. It does not stop at "no error" or "the year is 2023." See `instructors/files/backup_validate_data.py` for a reference.

A validator that cannot fail on a known-bad input does not protect you.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: this check passes. Is the file right?

A colleague hands you a merged file. It has 60 rows. Every date matches the raw source. Every `sample_id` appears once. Every score is between 0 and 100. Every `site` value is `A`.

1. Which of the checks you have run would catch this?
2. Would you approve the per-site plot?
3. What check would you add, and where would its expected values come from?

::::::::::::::::::::::::::::::::::::::::::::::::::: solution

Row count, date accuracy, ID uniqueness and score range can all pass on this file. Reject the per-site plot. Row count and date accuracy do not show site identity.

The missing check compares each `sample_id` with the site its raw file says it belongs to. The reference validator and the starter both include it. Run it against the file and watch it fail, then fix the labels and watch it pass.

A passing validator tells you only what it checked. Any property you did not write a check for is still unverified.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching tip: approval fatigue

Warn learners about approval fatigue, the habit of accepting suggestions without reading them. Ask for the check output before the diff discussion. Review the requirements and the critical changes yourself, and use independent checks to test defined properties. An agent's assurance that its code is correct is not proof.

Before the session, run `python instructors/files/test_validators.py`. It builds a good file and eight bad ones in a temporary folder and confirms that the validator rejects each bad one for the right reason.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: explain the approval gate

Take a script you or a partner generated earlier. Walk through the gate out loud or in writing. Answer all five:

1. What did the AI produce?
2. What evidence do you have that it works?
3. What evidence is missing?
4. Which domain assumption could still be wrong?
5. Would you approve, revise or reject this output, and why?

::::::::::::::::::::::::::::::::::::::::::::::::::: solution

## What a good answer looks like

A strong answer names the output precisely and points to specific checks as evidence: row counts, a failing-then-passing test. It admits gaps, such as "I have not checked the date parsing on the 2019 files."

The domain-assumption answer is hardest and most useful. It shows you are judging the science and not only the code. Approve only when the evidence covers the claim. Otherwise the honest answer is "revise."

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Going further: a critique from a second model

This section is optional. A second model can widen your review. Switching models inside the same Claude Code session is not independent, because the second model sees the same conversation, tools and framing. Treat what it returns as a hypothesis to check.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: get a critique from a second model

1. Use one model to generate a data cleaning script.
2. Give the specification, the code and any tests to a different model in a fresh session. Use a new terminal, a different tool, or at least `/clear`. Do not pass along the first model's account of its own work. Then use this prompt:

   "Read this script. Act as a skeptical senior data scientist. Name three edge cases where this script could fail, such as empty strings, NaN values or encoding problems. Suggest specific assert statements to catch each one."

3. Reflect. Did the second model find something the first one missed? Which findings still need a deterministic check or your own judgment before you act on them?

::::::::::::::::::::::::::::::::::::::::::::::::: solution

## Why this works, and its limit

Different models have different blind spots, so a second read can surface edge cases the first one skipped. But the second model shares training data and habits with the first, and a same-session switch shares even more. Treat its findings as questions to investigate with a check or your own expertise.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: keypoints

- The approval gate supports one decision: accept, revise or reject a bounded piece of code.
- Passing checks does not validate the study or the scientific claim.
- Take expected values from the source documentation, not from the code under test.
- A check earns trust when it fails on a known-bad input.
- Rewrite time is a local signal about your workflow, not a productivity score.
- You cannot validate what you cannot explain.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
