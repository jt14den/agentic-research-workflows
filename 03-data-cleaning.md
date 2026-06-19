---
title: "Data Cleaning with AI"
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Predict what a cleaning script must handle before you prompt for it.
- Build a data processing pipeline for inconsistent files using a spec.
- Explain and validate AI-generated code before you trust its output.
- Document the cleaning process and record its provenance.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Can I trust AI to standardise inconsistent files?
- How do I check that a cleaning script did what I needed, not only what the AI assumed?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Live coding
This episode uses live coding. Learners should follow along by running commands on their own machines.

:::::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites
Ensure you are signed in to Claude Code and have a session running in your project folder. Generating scripts can take 10-30 seconds.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Working inside Claude Code

All prompts in this episode are typed inside an active Claude Code session. Start one in your project folder before the exercises:

```bash
cd coastal-water-quality
claude
```

Run Python scripts in a separate terminal window when instructed.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Cleaning messy data

Cleaning and merging inconsistent files is a common bottleneck in research. We will use Claude Code to clean and merge the coastal water quality files into one analysis-ready dataset.

## The project data

Your project folder (`coastal-water-quality`) contains three files in `data/`, one per monitoring site, collected weekly from January to May 2023: `site_A.csv`, `site_B.csv`, and `site_C.csv` (20 samples each, 60 in total). They are messy in exactly the ways real multi-site data is: the site, date, and score columns are named differently in each file, the date formats differ, and a few values are missing. The folder's `README.md` describes the target schema and what "done" looks like. Our goal is one clean `data/master_dataset.csv`, then (in the capstone) a trend plot of score over time by site.

::::::::::::::::::::::::::::::::::::::::: callout

## Optional: generate your own messy data

To practise on a fresh problem later, you can have the AI synthesise a similar dataset:

```
Create a python script named 'make_messy_data.py' that generates 3 CSV files with inconsistent column names, varied date formats, and some missing values, mimicking a multi-site study.
```

For the lesson, use the provided files so everyone is working from the same data.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Cleaning with AI, one checkpoint at a time

It is tempting to type "clean and merge these files" and run whatever comes back. Resist that. We will work the task as a sequence of checkpoints so that you can explain and validate the result, not only produce one. This is the pattern you will reuse for the rest of the lesson: **predict, prompt for a plan, inspect, modify, validate, reflect.**

### A. Predict before you prompt

Open the three files in `data/` and look at them yourself first. Without using the AI, write down **two inconsistencies you expect any cleaning script will have to handle**. Real examples in this data:

- The site column is `SiteID` in site A, `id` in site B, and `StationID` in site C.
- The score column is `WaterQualityScore`, `score`, and `Quality_Index`.
- The dates differ: `2023/01/05` (A), `Jan 5 2023` (B), and `05-01-2023` (C). Watch site C: `05-01-2023` is day-month-year, so it means 5 January, not 1 May.

Keep your list. It is your yardstick for judging what the AI proposes. If you want a faster overview, you can have the AI write an inspection script, but read its output against your own list:

```
Write a Python script called 'inspect_data.py' that reads every CSV in data/. For each file, print the filename, the column names, and the number of missing values per column. Do not change any files.
```

### B. Ask the AI for a plan only

Do not ask for code yet. Inside your Claude Code session:

```
Read 'CLAUDE.md' and the three CSVs in data/. Before writing any code, give me a numbered plan for cleaning and merging them into data/master_dataset.csv. Do not write any files yet.
```

Compare the plan with the inconsistencies you wrote down in step A. Did it catch the site C date format? Did it say how it will handle missing values? Did it propose anything you did not expect?

### C. Approve or revise the plan

If the plan is missing a constraint you care about, add it to `CLAUDE.md` rather than only mentioning it in chat. The spec is what travels across sessions. For example:

```markdown
- Site C dates are day-month-year; parse them explicitly, do not let the tool guess.
- Fill missing score with the site median. Do not drop any rows: the merge must have 60.
```

### D. Generate the code

Now ask for the script, pointing it at the spec:

```
Read 'CLAUDE.md' and the three CSVs in data/. Write a script called 'clean_and_merge.py' that follows the plan and the spec rules. Save the result to data/master_dataset.csv. Add comments linking code steps to spec rules.
```

::::::::::::::::::::::::::::::::::::::::: callout

## Your script will not match the lesson's, and that is fine

AI output varies, so your `clean_and_merge.py` will look different from your neighbour's and from any example. That is the point: the goal is not to match a reference, it is to read what you got and decide whether it is correct. Judge it against your spec and the checks below, not against someone else's code.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Backup scripts
If a learner's AI fails to generate working code on the coastal data, provide the pre-written versions from `instructors/files/`:
- `backup_inspect_data.py`
- `backup_clean_and_merge.py`

::::::::::::::::::::::::::::::::::::::::::::::::::

### E. Explain before you run

Hands off the keyboard. Open `clean_and_merge.py` and read it. In pairs, **each person explains one section of the script out loud** to the other: what it does and which spec rule it serves. If a section uses something you have not seen, that is exactly the line to ask about.

You are responsible for the final output. You cannot validate what you cannot explain.

### F. Validate against checks, not vibes

Run `python clean_and_merge.py`. A correct run prints something like `Wrote data/master_dataset.csv with 60 rows.` Then confirm the result with concrete checks. "It ran" is not one of them.

- **Row-count check:** 60 rows (3 sites x 20 samples), nothing dropped.
- **Missing-value check:** missing scores filled per your strategy; nothing filled that should have stayed blank.
- **Date check:** all dates in 2023, and site C's January samples are in January, not May. Sort the file by date and look at the earliest site C rows: if they landed in May, the day-month-year format was misread.

You can ask the AI to write these checks, but read them before you trust them. The project folder already ships a `validate_data.py` with some checks written and others left as TODO; you will finish it in the next episode.

### G. Reflect

- What did the AI handle well?
- What did you have to already know in order to judge its answer?
- Did anything in the script change the data in a way the plan did not mention?

:::::::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: surprises and uncertainty

In the shared Etherpad, post two short lines: one thing the AI did that surprised you, and one thing it made sound certain that you are still unsure about. Bring these back into the room.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Instructor note: cognitive load in this episode

This is the most technically demanding episode, and generated cleaning code is where extraneous load shows up most. Watch for scripts that reach for `apply` with lambdas, regex date parsing, or multiple helper files when a short linear script would do. If a learner cannot explain a block in step E, have them ask the agent for a simpler version before continuing. The "hands off keyboard" read in step E is a feedback checkpoint: it is where you find out who is lost.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Challenge tip
This challenge requires modifying existing code. If learners are stuck, suggest they ask the AI to read `clean_and_merge.py` before asking for modifications.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Update the script

Imagine your analysis should cover February to May only, so you need to exclude the January samples.

1. **Predict first.** Before prompting, write down how many rows you expect this to remove and the row count you expect afterward. (Samples are weekly; January has four sampling dates per site.)
2. **Then update.** Use Claude Code to update `clean_and_merge.py` instead of editing it manually. Ask the AI to read the file and add the filtering logic.
3. **Verify against your prediction.** Run the updated script and compare the actual row count to what you predicted. If they differ, explain why in one sentence. Pay special attention to site C: if its January samples were misparsed as May, this filter will keep rows it should have dropped.

:::::::::::::::::::::::::::::::::::::::: solution

## What to expect

January has four weekly sampling dates per site (5, 12, 19, 26), so a correct filter removes 12 rows, leaving 48. If you get a different number, the most likely cause is the site C date format: misparsed January dates land in May and survive the filter. This is a small, safe version of a silent error that would quietly bias a real trend analysis.

```
Read 'clean_and_merge.py'. Modify the script to keep only samples collected in February 2023 or later. Keep all other logic the same. Save the updated script.
```

Did the AI edit the relevant part or rewrite the whole file? Did it parse the dates correctly before filtering? Did you check the changes before running?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Automating documentation

For the final step, have the AI generate a README that explains the data pipeline, including the raw files, cleaning steps, and final output format.

```
Create a README.md file that explains the data processing pipeline we just built. List the original files, the cleaning steps performed, and the final output format.
```

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Provenance tracking

To ensure research is reproducible, track which model generated your code and when.

1. Use Claude Code to add a provenance header to `clean_and_merge.py`.
2. The header should be a Python docstring containing:
    - The model used (e.g., Claude Sonnet 4.6)
    - The date
    - A summary of the prompt.

:::::::::::::::::::::::::::::::::::::::: solution

## Example command

```
Read 'clean_and_merge.py'. Add a docstring at the very top of the file as a provenance header. Include the model name 'Claude Sonnet 4.6', today's date, and a summary of the prompt: 'Standardise site IDs, format dates, and impute missing scores with site medians.'
```

### Reflection
- Why record the model version and date?
- Does it matter if the AI model is updated later?
- How does this header help with reproducibility?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Predict the inconsistencies yourself before prompting, so you can judge the AI's plan.
- Ask for a plan first, put constraints in the spec, then generate code.
- Explain the script before you run it; you cannot validate what you cannot explain.
- Validate with concrete checks (row count, missing values, date format), not because it ran.

::::::::::::::::::::::::::::::::::::::::::::::::::
