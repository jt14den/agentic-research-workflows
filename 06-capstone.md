---
title: "From AI Output to a Review-Ready Bundle"
teaching: 20
exercises: 90
---

:::::::::::::::::::::::::::::::::::::::: questions

- Can I take one task from prompt to a documented result that someone else can rerun?
- What does "review-ready" include, beyond a script that runs?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: objectives

- Run the full workflow on one project, from messy files to a checked, documented result.
- Assemble a bundle that another person can rerun without AI.
- Make and defend an approve, revise or reject decision on your own output.

::::::::::::::::::::::::::::::::::::::::::::::::::

You have practised each move on its own: requirements, a plan, a cleaning script, a validator. The capstone puts them together on the coastal water quality data. It ends with a descriptive statement: what pattern is visible in the water quality score at each site over the monitoring period?

A line plot can show a visible pattern. It does not establish a significant trend or a difference between sites. That needs a stated method and a measure of uncertainty, which this lesson does not cover. The data are synthetic, so the statement describes the exercise and not real coastal conditions.

The goal is not only a plot. It is a bundle that a collaborator, or you in six months, can rerun and trust.

## The workflow, end to end

Reuse the cleaning script and the validator you already built. Do not repeat their planning and generation.

1. **Confirm the task.** Write one sentence for what "done" means. For example: a merged 60-row dataset and a per-site plot, both checked and documented.
2. **Check your requirements.** Open `CLAUDE.md`. Does it state the schema, the rules about dropped rows and site C dates, and the missing-value rule? Fix it before you generate anything.
3. **Reuse the pipeline.** Run your `clean_and_merge.py` and `validate_data.py`. Every check must pass. An unfinished check is not a pass.
4. **Plan the plot.** Ask the agent to outline a short script that reads `data/master_dataset.csv` and plots `score` over `date`, one line per site. Do not let it write code yet. Review the plan against your requirements.
5. **Generate and read the plot script.** Ask for `plot_trend.py`, which saves `fig/score_trend.png`. Read the code. Explain one block aloud or in a comment. If you cannot, that block is not checked yet.
6. **Run it and look at the plot.** Do all three lines run from January to May as a continuous weekly series? Does site C look scattered or out of order? That would suggest the date trap bit you. A plot can render cleanly and still be wrong.
7. **Record the environment.** Save the Python and package versions you used, for example with `python --version` and `pip freeze` into `environment.txt`.
8. **Write the run instructions.** Create `RUN.md` with the working directory and the exact commands, in order. A partner will follow it with no help from you.
9. **Write the provenance note.** Record the tool version, the model name if you know it, the date, the relevant prompts, the changes you reviewed and the checks that passed.
10. **Decide.** Approve, revise or reject. Write one line of evidence and one remaining uncertainty.

::::::::::::::::::::::::::::::::::::::::: callout

## The likely failure is silent

If the cleaning script parses site C dates with `format="mixed"` and not the explicit `%d-%m-%Y`, some rows swap day and month. `05-01-2023` becomes 1 May. Other rows parse correctly by accident. The script runs, the row count is 60, and the plot misleads. The wrong points scatter, so looking at the plot alone will not reliably catch the error.

"It ran" would hide this. Your validator, which compares each sample's date with its raw source, would not.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: challenge

## Can another researcher rerun and assess your result?

Share one folder with a partner. Include:

- The three unchanged synthetic source CSVs and their description.
- `CLAUDE.md`, plus the approved plan or a short plan summary.
- `clean_and_merge.py`, `validate_data.py` and `plot_trend.py`.
- `environment.txt` with the Python and package versions you used.
- `RUN.md` with the working directory and the exact commands, in order.
- `data/master_dataset.csv` and `fig/score_trend.png`.
- A provenance note: tool version, model name if known, date, relevant prompts, reviewed changes and test results.
- Your approval decision, its evidence and one remaining uncertainty.

Your partner regenerates the dataset and the plot in a fresh copy of the folder, without AI. They confirm that:

1. All 60 source IDs occur once, and each ID has the right site.
2. Every date matches its source record under the documented source format.
3. Every score is a number, none is blank, and all are between 0 and 100.
4. Observed scores are unchanged. The three missing scores use their site's median of observed scores: A004 = 72.0, B-006 = 71.5, SC002 = 71.6.
5. Missing pH and temperature values stay missing, and all other values are preserved.
6. The raw inputs are unchanged. The plot is regenerated from the checked output, with one labelled line per site and dates in order.
7. The validator rejects a copy with wrong dates and a copy where every site is `A`.

Make the bad copies in a separate temporary folder. Restore the correct output before you make the plot.

Then write one descriptive statement about the synthetic series. Do not infer a significant trend, a causal effect or real coastal conditions. In one sentence, say why the workshop's median rule is not automatically right for a real study.

Finally, write three sentences:

- What did I understand? Name one part of the pipeline you could rebuild without AI.
- What did I verify? Name the evidence, not the feeling.
- What remains uncertain? Name one thing you would check before real use.

:::::::::::::::::::::::::::::::::::::::: solution

## Review rubric

A complete bundle reruns without hidden files, agent access or manual edits to the data. The reviewer records each command, its result and any missing dependency.

A correct decision names the checks and limits its claim to those checks.

**Transfer case.** A candidate has 60 rows, correct dates, unique IDs and scores in range, but every `site` value is `A`. A validator without a site check can pass this file. Reject the per-site plot until the ID-to-site check fails on the candidate and passes after repair. Row count and date accuracy do not show site identity.

A "revise" decision that names a precise missing check is stronger than an unsupported approval. If a bundle cannot rerun, name the missing file or instruction. A prompt summary does not replace executable analysis code.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Instructor note

Spend most of the time on doing. Expect the site C date bug to surface for several learners. Treat it as the highlight, because it shows the lesson's central point in one failure.

If a group falls behind, supply the reference cleaner and plot script from `instructors/files/`, and the completed validator. Label which parts you supplied. The learner must still explain one change, predict a failure and defend a decision on the transfer case.

Record whether the partner actually reran the bundle or only inspected saved output. Collect a few approval decisions and read them aloud. The honest "revise" answers teach the most.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: revisit your opening note

Look back at the note from Episode 1: what you wanted from AI and what you feared it would get wrong. Did the workshop change either answer? Post one line in the Etherpad, or add it to your notes file.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- A review-ready bundle holds requirements, code, checks, a result, the environment, exact commands, provenance and a decision. A script that runs is not enough.
- Another person rerunning your work without AI is the strongest test of the bundle.
- A descriptive plot is not a statistical finding.
- A plot can render cleanly and still be wrong. Domain plausibility is your job.
- "Revise" is an honest outcome when the evidence does not yet cover the claim.

::::::::::::::::::::::::::::::::::::::::::::::::::
