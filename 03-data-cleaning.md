---
title: "Data cleaning with AI"
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

- Can I trust AI to standardize inconsistent files?
- How do I check that a cleaning script did what I needed, not just what the AI assumed?

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
cd path/to/your/project
claude
```

Run Python scripts in a separate terminal window when instructed.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Cleaning messy data

Cleaning and merging inconsistent files is a common bottleneck in research. We will use Claude Code to standardize messy CSV files.

### Generating test data

To practice cleaning, we need a dataset with inconsistencies. We can use AI to simulate a multi-site study where each location used different naming conventions or date formats. Run this command to generate three files: `site_A.csv`, `site_B.csv`, and `site_C.csv`.

```
Create a python script named 'make_messy_data.py'. It should generate 3 CSV files ('site_A.csv', 'site_B.csv', 'site_C.csv') with 50 rows each. Columns should include 'ID', 'Date', and 'Score', but make them inconsistent (e.g., 'ParticipantID' vs 'id', 'date' vs 'Date_Time'). Add some missing values and varied date formats (like '2023/01/05' vs 'Jan 5, 2023').
```

After running `python make_messy_data.py`, you will have three inconsistent files in your directory.

### Auditing the data

Before fixing the files, we need to understand the inconsistencies. We can ask the AI to write an inspection script that reads every CSV in the folder and reports the filenames, column names, and missing value counts.

```
Write a Python script called 'inspect_data.py' that reads every CSV file in the current folder. For each file, print the filename, the list of column names, and the number of missing values in each column.
```

Run the inspection script. You should see inconsistencies like `site_A` using `ParticipantID` while `site_B` uses `id`.

::::::::::::::::::::::::::::::::::::::::: callout

## Reasoning models
If your data files are extremely inconsistent, reasoning models (like o1 or DeepSeek-R1) are often more effective. They can identify subtle naming patterns that standard models might miss.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Cleaning with AI, one checkpoint at a time

It is tempting to type "clean and merge these files" and run whatever comes back. Resist that. We will work the same task as a sequence of checkpoints so that you can explain and validate the result, not just produce one. This is the pattern you will reuse for the rest of the lesson: **predict, prompt for a plan, inspect, modify, validate, reflect.**

### A. Predict before you prompt

Open the three CSV files and look at them yourself first. Without using the AI, write down **two inconsistencies you expect any cleaning script will have to handle** (for example: `site_A` uses `ParticipantID` but `site_B` uses `id`, or the dates are in different formats).

Keep this list. It is your yardstick for judging what the AI proposes.

### B. Ask the AI for a plan only

Do not ask for code yet. Inside your Claude Code session:

```
Read 'CLAUDE.md' and the three site CSVs. Before writing any code, give me a numbered plan for cleaning and merging them into 'master_dataset.csv'. Do not write any files yet.
```

Compare the plan with the two inconsistencies you wrote down in step A. Did the plan catch them? Did it miss any? Did it propose anything you did not expect (for example, filling missing values a particular way)?

### C. Approve or revise the plan

If the plan is missing a constraint you care about, add it to `CLAUDE.md` rather than only mentioning it in chat. The spec is what travels across sessions. For example, you might add:

```markdown
- Missing scores must be filled with the site median, never the global mean.
- Do not drop any participant rows during cleaning.
```

### D. Generate the code

Now ask for the script, pointing it at the spec:

```
Read 'CLAUDE.md' and the three site CSVs. Write a script called 'clean_and_merge.py' that follows the plan and the spec rules. Save the result to 'master_dataset.csv'. Add comments linking code steps to spec rules.
```

::::::::::::::::::::::::::::::::::::::::: instructor

## Backup scripts
If a learner's AI fails to generate working code, provide the pre-written versions from `instructors/files/`:
- `backup_make_messy_data.py`
- `backup_inspect_data.py`
- `backup_clean_and_merge.py`

::::::::::::::::::::::::::::::::::::::::::::::::::

### E. Explain before you run

Hands off the keyboard. Open `clean_and_merge.py` and read it. In pairs, **each person explains one section of the script out loud** to the other: what it does and which spec rule it serves. If a section uses something you have not seen, that is exactly the line to ask about.

You are responsible for the final output. You cannot validate what you cannot explain.

### F. Validate against checks, not vibes

Run `python clean_and_merge.py`, then confirm the result with three concrete checks. "It ran" is not one of them.

- **Row-count check:** Does the merged file have the number of rows you expected (for example, 150 if three sites of 50 should all be kept)?
- **Missing-value check:** Are there still missing values where there should be none? Are there none where some should remain?
- **Date-format check:** Are all dates in a single consistent format?

You can ask the AI to write these checks, but read them before you trust them.

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

Imagine you need to exclude any participant with a score below 10.

1. **Predict first.** Before prompting, write down how many rows you expect this to remove and which `master_dataset.csv` row count you expect afterward. Base it on what you saw when you inspected the data.
2. **Then update.** Use Claude Code to update `clean_and_merge.py` instead of editing it manually. Ask the AI to read the file and add the filtering logic.
3. **Verify against your prediction.** Run the updated script and compare the actual row count to what you predicted. If they differ, explain why in one sentence (for example: missing scores, ties at exactly 10, or the filter ran in the wrong order).

:::::::::::::::::::::::::::::::::::::::: solution

## Example command

```
Read 'clean_and_merge.py'. Modify the script to filter out any rows where 'score' is less than 10. Keep all other logic the same. Save the updated script.
```

### Reflection

*   Did the AI edit the relevant part or rewrite the whole file?
*   Did it include the necessary imports?
*   Did you check the changes before running the script?

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
Read 'clean_and_merge.py'. Add a docstring at the very top of the file as a provenance header. Include the model name 'Claude Sonnet 4.6', today's date, and a summary of the prompt: 'Standardize site IDs, format dates, and impute missing scores with site medians.'
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
