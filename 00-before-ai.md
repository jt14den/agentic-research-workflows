---
title: "Before We Use AI: What Are We Practising?"
teaching: 15
exercises: 30
---

:::::::::::::::::::::::::::::::::::::::: questions

- What are we practising in this lesson?
- When does an AI coding tool help me learn, and when does it get in the way?
- How do I decide whether to trust a result the AI gave me?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: objectives

- Tell code generation, code understanding and code validation apart.
- Use a checkpoint to decide whether to run, revise or reject an AI-generated result.
- Reject a plausible wrong result with evidence from a check you chose yourself.

::::::::::::::::::::::::::::::::::::::::::::::::::

## This is not a lesson about letting AI do the work

It is tempting to treat an AI coding agent as a machine that turns a sentence into a finished script. You type "clean this data," code appears, it runs, and you move on.

This lesson teaches the opposite skill. You learn to inspect, question, constrain and validate AI-generated code until a result is trustworthy enough for research. You will often explain what the AI did, and not only run what it produced.

Three skills are easy to confuse:

- Code generation is getting the AI to produce something that runs.
- Code understanding is saying in plain language what the code does and why.
- Code validation is having evidence that the code is correct for your data and your research question.

Generation is the easy part now. Understanding and validation make code trustworthy, and they are still your job.

::::::::::::::::::::::::::::::::::::::::: callout

## Code can appear before understanding does

An agent can produce a working-looking script faster than you can read it. If the code shows up before you understand it, you skip the step where learning happens.

Research adds a second cost. Working code is not the same as trustworthy code. A script can run cleanly, pass a quick check, and still change a threshold, drop rows or misread a date format in a way that changes your conclusion.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Why generated code can raise your cognitive load

It sounds backwards. If the AI writes the code, you should have less to do. But to judge generated code you have to hold four things in mind:

- what you asked for,
- what the code does,
- what assumptions it made,
- and whether those assumptions fit your data.

Reviewing unfamiliar generated code can add load, especially when it uses a library, a language feature or an abstraction you have not met. We name these moments when they come up.

::::::::::::::::::::::::::::::::::::::::: instructor

## Instructor note: set the tone early

Reset expectations before learners open a terminal. Some arrive expecting a productivity demo. Say clearly that the workshop measures whether they can explain and validate AI output, not how fast they can generate it.

Watch for these signs throughout the workshop:

- Learners who are impressed that the agent can read their files but cannot say what it changed.
- Learners who accept output they cannot explain because "it ran."
- Learners who turn to the AI before a helper, which hides where they are stuck.

Bring AI confusion back into the room. Treat confusing output as a shared teaching example and not a personal failure.

::::::::::::::::::::::::::::::::::::::::::::::::::

## The run, revise or reject checkpoint

Every time the AI hands you something, you make a decision. Make it on purpose. Two different questions are involved:

- Action permission: may this command run? Check what it reads and writes.
- Result approval: is this result good enough to use? That needs evidence.

Permission to run an action is not approval of its result. Ask:

1. Can I explain what this does? If not, you are not ready to approve it.
2. What did it assume about my data? Name at least one assumption.
3. What evidence shows it is correct? "It ran" is not evidence.
4. Decision: run it, revise it or reject it.

You will use this checkpoint, in more detail, throughout the lesson.

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: practise the checkpoint

An agent produced this snippet when asked to "remove the bad rows from my data":

```python
import pandas as pd
df = pd.read_csv("data.csv")
df = df.dropna()
df.to_csv("clean.csv", index=False)
```

Without running anything, answer in a sentence or two each:

1. What does this script do, in plain language?
2. What does it assume "bad rows" means?
3. Name one way it could quietly damage a real research dataset.
4. Would you run it, revise it or reject it for a dataset where missing values carry meaning, such as a survey where "no answer" is a valid response?

:::::::::::::::::::::::::::::::::::::::: solution

1. It reads `data.csv`, drops every row with a missing value in any column, and writes the result to `clean.csv`.
2. It assumes "bad rows" means "rows with any missing value." That is the AI's reading, not yours.
3. `dropna()` with no arguments removes a row if any column is empty. In a wide dataset, one empty optional field deletes an otherwise complete observation, and the sample shrinks without notice.
4. Revise or reject. If missingness has meaning, dropping those rows changes what the data represent. You would limit which columns to check, or impute. The code runs perfectly and is still wrong for your question.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Quick check: what does `dropna()` remove?

A table has columns `site`, `date`, `score` and `notes`. Only `notes` has blank cells. What does `df.dropna()` with no arguments do?

1. Drops rows where every column is blank.
2. Drops rows where the `notes` column is blank.
3. Drops rows where any column is blank, including `notes`.
4. Drops the `notes` column and keeps all rows.

:::::::::::::::::::::::::::::::::::::::: solution

**3.** With no arguments, `dropna()` checks every column and drops a row if any of them is blank, even in a column you think of as optional. Options 1 and 2 describe common wrong assumptions about how it scopes the check. Option 4 confuses dropping rows with dropping a column, which is a different method (`drop(columns=...)`).

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: challenge

## A result can pass one check and still be wrong

The source documentation says site C writes dates as day-month-year. The first record in `data/site_C.csv` is `SC001,05-01-2023,69.4,7.0,14.2`.

Before you run code or ask an agent, write down:

1. What ISO date should SC001 have?
2. Would keeping all 20 site C rows prove the dates are correct?
3. What must you see before you approve these dates for a plot?

With a partner, read this candidate transformation. It is in your project folder as `date_review.py`. Explain what each line does.

```python
import pandas as pd

raw = pd.read_csv("data/site_C.csv")
candidate = pd.DataFrame({
    "sample_id": raw["StationID"],
    "date": pd.to_datetime(raw["DateTime"], format="mixed").dt.strftime("%Y-%m-%d")
})
print("Rows:", len(candidate))
print(candidate.head(2).to_string(index=False))
```

Run `python date_review.py`. It reads the raw file and prints output. It does not change the raw data. Permission to run this action is separate from accepting its result.

Now add these checks to the end of the script. Fill in the blank from the source format, without AI.

```python
assert len(candidate) == 20
actual = candidate.set_index("sample_id").loc["SC001", "date"]
assert actual == "__________", f"SC001 became {actual}"
```

Run it again. Which check fails? What does the passing check establish?

Change the date parser, by hand or by asking for one change. Read the changed line, rerun, and write one of: approve, revise, reject. Add your evidence. Also say what a check on one record does not yet establish.

:::::::::::::::::::::::::::::::::::::::: solution

SC001 should be `2023-01-05`. The faulty parser gives `2023-05-01`. Both are valid dates, and the row-count check still passes. SC002 becomes `2023-12-01` and not `2023-01-12`.

Replace `format="mixed"` with `format="%d-%m-%Y"`. Both checks then pass. They cover the row count and one expected date. They do not show that every date and score is right. Before you approve the full output, compare every sample's date with its source record under the documented format.

A strong answer names the wrong value, the independent expected value, the failed assertion and the coverage that is still missing.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Fallback and pacing for the date exercise

If a learner cannot run the script, give them the saved output in `instructors/files/date-review-output.txt`:

```text
Rows: 20
sample_id       date
    SC001 2023-05-01
    SC002 2023-12-01
AssertionError: SC001 became 2023-05-01
```

Ask for the same prediction, explanation and decision. Do not wait for a live agent to make this mistake. The script is deliberately faulty, and nothing here claims that every agent makes it.

After two failed attempts, give the learner a working script. After the repair, show the reference validator catching eight mismatched dates in the faulty version and none in the repaired one (`instructors/files/backup_validate_data.py`). Do not present the saved transcript as the learner's own run.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: what do you want from AI?

On a sticky note or in the shared Etherpad, write one line: what do you most want an AI tool to do for your research, and what worries you most about it? Working alone? Write the line in your notes file. You will return to it at the end of the lesson.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- This lesson teaches you to inspect, question, constrain and validate AI output. It does not teach you to hand off your thinking.
- Generation, understanding and validation are different skills. Generation is the easy one.
- Reviewing unfamiliar generated code can cost real effort, especially when it brings in ideas you do not know.
- Working code is not the same as trustworthy code. A result can pass one check and still be wrong.
- Permission to run an action is separate from approval of its result.

::::::::::::::::::::::::::::::::::::::::::::::::::
