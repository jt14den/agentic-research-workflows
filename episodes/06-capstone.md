---
title: "From AI Output to Research-Ready Code"
teaching: 10
exercises: 40
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Run the full workflow on one project, from messy files to a validated, documented result.
- Produce a research-ready bundle: spec, plan, code, validation, a result, and provenance.
- Make and defend an approve / revise / reject decision on your own output.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Can I take one task from prompt to trustworthy, documented result?
- What does "research-ready" actually include, beyond a script that runs?

::::::::::::::::::::::::::::::::::::::::::::::::::

So far you have practised each move on its own: a spec, a plan, a cleaning script, a validator. The capstone puts them together on the project you have been carrying all along, the coastal water quality data, and ends with an actual finding: **is the water quality score trending up or down, and does it differ by site?**

Work through the steps below. The goal is not just a plot. It is a bundle you could hand to a collaborator, or your future self, and have them trust.

## The workflow, end to end

Run these as checkpoints, the same pattern as the cleaning episode. Do not rush to the plot.

1. **Confirm the task.** In one sentence, write what "done" means here. (Example: a merged 60-row dataset and a per-site trend plot, both validated and documented.)
2. **Check the spec.** Open your `CLAUDE.md`. Does it state the schema, the no-go zones (no dropped rows, parse site C dates explicitly), and how missing values are handled? Fix it before generating anything.
3. **Ask for a plan only.** Have the agent outline the steps from raw files to merged dataset to trend plot. Do not let it write code yet. Review the plan against your spec.
4. **Generate the cleaning + analysis code.** If you already have `clean_and_merge.py`, reuse it. Then ask for a short analysis script that loads `data/master_dataset.csv` and plots `score` over `date` with one line per site, saved to `fig/score_trend.png`.
5. **Explain one block.** Pick one function or section and explain, out loud or in a comment, what it does and why. If you cannot, that block is not validated yet.
6. **Validate.** Run `python validate_data.py` (with your finished checks). Confirm 60 rows, dates in 2023, scores in range, no lost IDs.
7. **Run the analysis.** Produce the plot. Look at it.
8. **Judge the result (domain plausibility).** Does the trend make sense? Do all three site lines span January to May, or does site C only appear at the May edge, the sign the date trap bit you? A plot can render cleanly and still be wrong.
9. **Document provenance.** Add a header or a short `PROVENANCE.md`: model used, date, the prompt summary, and which checks passed.
10. **Decide.** Approve, revise, or reject, and write one line saying why.

::::::::::::::::::::::::::::::::::::::::: callout

## What can go wrong here (and that is the point)

The most likely failure is silent: site C's `05-01-2023` dates parsed as month-day, so its January samples land in May. The script runs, the row count is 60, and the trend plot still misleads. This is exactly the kind of error that "it ran" would have hidden, and exactly what your validator and your eyes on the plot are for.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Capstone challenge: the research-ready bundle

Produce and submit (or share with a partner) a bundle for the coastal project:

- `CLAUDE.md` (your spec, with constraints)
- `PLAN.md` (the approved plan, or a one-paragraph summary)
- `clean_and_merge.py` (generates `data/master_dataset.csv`)
- `validate_data.py` (all five checks implemented and passing)
- `fig/score_trend.png` (the per-site trend)
- a provenance note (model, date, prompt summary, checks passed)
- a short **approval decision**: approve, revise, or reject, and why

Then write three sentences of reflection:

- **What did I understand?** Name one part of the pipeline you could rebuild without AI.
- **What did I verify?** Name the evidence, not the feeling.
- **What remains uncertain?** Name one thing you would check before using this for real.

:::::::::::::::::::::::::::::::::::::::: solution

## What a strong bundle shows

The script running is the least interesting part. A strong bundle shows *judgement*: the spec names the date trap before the code is written; the validator would fail on a misparsed file; the provenance note lets someone reproduce the run; and the approval decision is honest about what is and is not yet checked. "Revise" is a perfectly good answer when the evidence does not yet cover the claim.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Instructor note

Budget most of the time for doing, not explaining. Expect the site C date bug to surface for several learners; treat it as the highlight, not a snag, it is the lesson's whole thesis in one concrete failure. If a group is far behind, have them use `instructors/files/backup_clean_and_merge.py` so they still reach the validate-and-judge steps, which are the point. Collect a few approval decisions and read them aloud; the honest "revise" answers are the best teaching.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: revisit your opening note

Look back at the sticky note from Episode 1, what you wanted from AI and what you feared it would get wrong. Did the workshop change either answer? Post one line in the Etherpad.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Research-ready means spec, plan, code, validation, a result, provenance, and a decision, not just a script that runs.
- The same checkpoint pattern scales from one script to a whole small project.
- A plot can render cleanly and still be wrong; domain plausibility is your job.
- "Revise" is a valid, honest outcome when the evidence does not yet cover the claim.

::::::::::::::::::::::::::::::::::::::::::::::::::
