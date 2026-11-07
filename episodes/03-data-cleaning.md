---
title: "Data Cleaning with AI"
teaching: 50
exercises: 48
---

:::::::::::::::::::::::::::::::::::::::: questions

- Can I trust AI to standardise inconsistent files?
- How do I check that a cleaning script did what I needed, and not only what the AI assumed?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: objectives

- Predict what a cleaning script must handle before you prompt for it.
- Build a processing pipeline for inconsistent files from a plan and a set of requirements.
- Read a diff and explain the changed lines before you run the code.
- Validate AI-generated code against checks, and record where it came from.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites

Sign in to Claude Code and keep a session running in your project folder. Generating a script can take 10 to 30 seconds.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Live coding

This episode uses live coding. Learners follow along on their own machines.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Working inside Claude Code

Type the prompts in this episode inside an active Claude Code session. Start one in your project folder:

```bash
cd coastal-water-quality
claude
```

Run Python scripts in a separate terminal window when the text tells you to.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Cleaning messy data

Cleaning and merging inconsistent files takes a lot of research time. In this episode you clean and merge the coastal water quality files into one analysis-ready dataset.

## The project data

The data are synthetic. They were built for this lesson and describe no real study.

Your project folder (`coastal-water-quality`) holds three files in `data/`, one per monitoring site. Samples were taken weekly from January to May 2023. The files are `site_A.csv`, `site_B.csv` and `site_C.csv`, with 20 samples each and 60 in total.

The files are messy in the ways real multi-site data often are. Column names differ, date formats differ and a few values are missing. The folder's `README.md` describes the target schema and what "done" looks like. The goal is one clean `data/master_dataset.csv`. In the capstone you plot score over time by site.

::::::::::::::::::::::::::::::::::::::::: callout

## Optional: generate your own messy data

To practise on a new problem later, ask the AI to synthesise a similar dataset:

```
Create a python script named 'make_messy_data.py' that generates 3 CSV files with inconsistent column names, varied date formats, and some missing values, mimicking a multi-site study.
```

For the lesson, use the provided files so everyone works from the same data.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Cleaning with AI, one checkpoint at a time

It is tempting to type "clean and merge these files" and run whatever comes back. Do not. Work through checkpoints so you can explain the result and not only produce it. The pattern is: predict, plan, inspect, change, read the diff, check, reflect.

### A. Predict before you prompt

Open the three files in `data/` and look at them yourself. Do not use the AI yet. Write down two inconsistencies that any cleaning script has to handle. Real examples in this data:

- The ID column is `SiteID` in site A, `id` in site B and `StationID` in site C.
- The score column is `WaterQualityScore`, `score` and `Quality_Index`.
- The dates differ: `2023/01/05` (A), `Jan 5 2023` (B) and `05-01-2023` (C). Site C writes day-month-year, so `05-01-2023` is 5 January and not 1 May.

Keep your list. You will judge the AI's proposal against it. For a faster overview, ask the AI to write an inspection script, and read its output against your list:

```
Write a Python script called 'inspect_data.py' that reads every CSV in data/. For each file, print the filename, the column names, and the number of missing values per column. Do not change any files.
```

::::::::::::::::::::::::::::::::::::::::: challenge

## Quick check: site C's date format

Site C stores dates as `05-01-2023`, in day-month-year order. What date is that, and what would a parser that assumes month-day-year produce without warning?

1. 5 January. A month-day-year parser also reads it as 5 January.
2. 5 January. A month-day-year parser reads it as 1 May.
3. 1 May. A month-day-year parser reads it as 5 January.
4. There is not enough information to tell.

:::::::::::::::::::::::::::::::::::::::: solution

**2.** In day-month-year order, `05-01-2023` is day 05 of month 01, which is 5 January 2023. A parser that assumes month-day-year reads the same string as month 05, day 01, which is 1 May 2023. It raises no error. The string never changes. Only the format you tell the parser to assume changes.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### B. Ask the AI for a plan only

Do not ask for code yet. Inside your Claude Code session, type:

```
Read 'CLAUDE.md' and the three CSVs in data/. Before writing any code, give me a numbered plan for cleaning and merging them into data/master_dataset.csv. Do not write any files yet.
```

Compare the plan with your list from step A. Did it catch the site C date format? Does it say how it will handle missing values? Does it propose anything you did not expect?

### C. Approve or revise the plan

Mark one step in the plan that rests on an assumption the data do not support. Revise it from the evidence in the files and `README.md`. Approve only the bounded action you can describe.

If the plan lacks a constraint you care about, add it to `CLAUDE.md`. Do not only mention it in chat, because the file travels with the project. For example:

```markdown
- Site C dates are day-month-year. Parse them explicitly. Do not let the tool guess.
- Fill a missing score with the median of that site's observed scores. Do not drop any rows. The merge must have 60.
```

The median rule is this exercise's fixed choice. It is not automatically right for a real study. A real analysis would justify its method for missing values.

### D. Generate the code

Now ask for the script and point it at your requirements:

```
Read 'CLAUDE.md' and the three CSVs in data/. Write a script called 'clean_and_merge.py' that follows the plan and the rules in CLAUDE.md. Save the result to data/master_dataset.csv. Add comments that link each code step to a rule.
```

::::::::::::::::::::::::::::::::::::::::: callout

## Your script will not match the lesson's

AI output varies, so your `clean_and_merge.py` will differ from your neighbour's and from any example. Judge it against your requirements and the checks below, not against someone else's code.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Backup scripts

If a learner's AI fails to produce working code twice, hand over the prepared versions from `instructors/files/`:

- `backup_inspect_data.py`
- `backup_clean_and_merge.py`

The learner still predicts, explains, tests and decides. Label which parts were supplied.

::::::::::::::::::::::::::::::::::::::::::::::::::

### E. Explain before you run

Take your hands off the keyboard and read `clean_and_merge.py`. In pairs, each person explains one section aloud: what it does and which rule it serves. If a section uses something you have not seen, ask about that line. Working alone? Explain each section aloud, or write the explanation as a comment above it. Then ask the agent to compare your explanation with what the code does.

You are responsible for the final output. You cannot validate what you cannot explain.

### F. Check against evidence

Run `python clean_and_merge.py`. A correct run prints something like `Wrote data/master_dataset.csv with 60 rows.` Then test the result with concrete checks. "It ran" is not a check.

- **Row count.** There are 60 rows (3 sites x 20 samples). Nothing was dropped.
- **Missing values.** Missing scores are filled by your rule. Nothing was filled that should stay blank.
- **Dates.** Do not stop at "the dates parse and fall in 2023". A wrong parse still produces valid-looking 2023 dates. Compare a few site C dates with the raw file by hand. `05-01-2023` must become `2023-01-05` and not `2023-05-01`. Better, re-parse site C's raw dates with the explicit `%d-%m-%Y` format and compare the result with your merged file row by row.

You can ask the AI to write these checks. Read them before you trust them. The project folder ships a `validate_data.py` with most checks written and one left for you. You finish it in the next episode.

### G. Reflect

- What did the AI handle well?
- What did you already need to know to judge its answer?
- Did anything in the script change the data in a way the plan did not mention?

:::::::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: surprises and uncertainty

Post two short lines in the shared Etherpad. Write one thing the AI did that surprised you, and one thing it sounded certain about that you still doubt. Bring both back to the room. Working alone? Write both lines in your notes file and follow up on the doubt before you move on.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Instructor note: cognitive load in this episode

This is the most demanding episode. Generated cleaning code is where extra load shows up most. Watch for `apply` with lambdas, regular-expression date parsing, or several helper files where a short linear script would do. If a learner cannot explain a block in step E, ask them to request a simpler version before they continue.

Step E is a feedback checkpoint. It shows you who is lost. Ask helpers to note unresolved concepts, not only installation problems.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Challenge tip

The next challenge changes existing code. If learners get stuck, suggest that they ask the AI to read `clean_and_merge.py` first.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: read a diff, then run it

Imagine your analysis should cover February to May only, so you must leave out the January samples.

1. **Predict first.** Before you prompt, write down how many rows you expect to remove and how many you expect to keep. Samples are weekly, and January has four sampling dates per site.
2. **Ask for a new script.** Ask Claude Code to write a new script, `clean_feb_onward.py`. It reuses the cleaning logic from `clean_and_merge.py`, keeps only samples from February 2023 onward, and writes `data/feb_onward.csv`. It must not touch `clean_and_merge.py` or `data/master_dataset.csv`. The capstone and later episodes expect the full 60-row dataset.
3. **Read before you run.** Compare the new script with `clean_and_merge.py` (for example, `diff clean_and_merge.py clean_feb_onward.py`). Pick one changed line and explain it to a partner. Check that the output path is `data/feb_onward.csv`.
4. **Check against your prediction.** Run the new script. Compare the row count with your prediction. If they differ, explain why in one sentence. Then confirm that both files kept the counts you intended: 60 rows in `data/master_dataset.csv` and your predicted count in `data/feb_onward.csv`. Pay attention to site C. A naive parse can swap day and month for some rows and not others, so some misparsed January rows can land outside the window and vanish, while others land inside it and wrongly stay.

:::::::::::::::::::::::::::::::::::::::: solution

## What to expect

January has four weekly sampling dates per site (the 5th, 12th, 19th and 26th). A correct filter removes 12 rows and leaves 48.

A different number most likely comes from the site C date format. A naive parse swaps day and month for some rows only. For example, `05-01-2023` becomes 1 May and `12-01-2023` becomes 1 December, while `19-01-2023` parses correctly either way because 19 cannot be a month. A partial misparse does not shift the whole series to one edge. It scatters points. This is a small, safe version of a silent error that would bias a real trend analysis.

```
Read 'clean_and_merge.py'. Write a new script, 'clean_feb_onward.py', that reuses its cleaning logic, keeps only samples collected in February 2023 or later, and writes data/feb_onward.csv. Do not modify clean_and_merge.py or data/master_dataset.csv.
```

Did the AI edit the right part or rewrite the whole file? Did it parse the dates before it filtered? Did you read the changes before you ran the script?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Automating documentation

Ask the AI for a short pipeline summary. The folder already has a `README.md` that describes the schema and the target output, so ask for a differently named file:

```
Create a PIPELINE.md file that explains the data processing pipeline we just built. List the original files, the cleaning steps performed, and the final output format. Do not modify or overwrite README.md.
```

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: provenance tracking

For research to be reproducible, record which tool generated your code and when.

1. Use Claude Code to add a provenance header to `clean_and_merge.py`.
2. The header is a Python docstring with:
    - The tool version and the model name, if your session shows it (check `/status` or the status line).
    - The date.
    - A summary of the prompt.

:::::::::::::::::::::::::::::::::::::::: solution

## Example prompt

```
Read 'clean_and_merge.py'. Add a docstring at the very top of the file as a provenance header. Include the tool version and the exact model name from this session (check /status if unsure), today's date, and a summary of the prompt: 'Standardise site IDs, format dates, and impute missing scores with site medians.'
```

### Reflection

- Why record the tool version, model name and date?
- Does it matter if the model is updated later?
- How does the header help someone rerun your work? A header records history. The code, the data, the environment and the commands are what let another person rerun it.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Predict the inconsistencies yourself before you prompt, so you can judge the AI's plan.
- Ask for a plan first, mark the assumption the data do not support, then generate code.
- Read the diff and explain a changed line before you run it.
- Check with concrete evidence (row count, missing values, dates), not because the script ran.

::::::::::::::::::::::::::::::::::::::::::::::::::
