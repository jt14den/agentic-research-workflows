---
title: "Before We Use AI: What Are We Practicing?"
teaching: 15
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Distinguish between code generation, code understanding, and code validation.
- Explain why AI-generated code can increase cognitive load for novices.
- Use a structured checkpoint to decide whether an AI-generated result is safe to run, revise, or reject.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What are we actually practicing in this lesson?
- When does an AI coding tool help me learn, and when does it get in the way?
- How do I decide whether to trust a result the AI gave me?

::::::::::::::::::::::::::::::::::::::::::::::::::

## This is not a lesson about letting AI do the work

It is tempting to treat an AI coding agent as a machine that turns a sentence into a finished script. You type "clean this data," code appears, it runs, and you move on.

This lesson is about the opposite skill. The point is to learn how to **inspect, question, constrain, and validate** AI-generated code so that the result is trustworthy enough for research. Throughout the lesson you will be asked to explain what the AI did, not just run what it produced.

Three things are easy to confuse:

- **Code generation** is getting the AI to produce something that runs.
- **Code understanding** is being able to say, in plain language, what the code does and why.
- **Code validation** is having evidence that the code is correct for *your* data and *your* research question.

Generation is the easy part now. Understanding and validation are the parts that make code trustworthy, and they are still your job.

::::::::::::::::::::::::::::::::::::::::: callout

## AI can make code appear before understanding appears

A chatbot or agent can produce a working-looking script faster than you can read it. That is the core risk for a learner. If the code shows up before you understand it, you have skipped the step where learning actually happens.

In research this has a second cost. **Working code is not the same as trustworthy code.** A script can run cleanly, pass a quick check, and still quietly change a threshold, drop rows, or misread a date format in a way that changes your conclusion.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Why generated code can raise your cognitive load

It sounds backwards: if the AI writes the code, shouldn't that be *less* work? For a novice, often the opposite is true. To judge whether generated code is correct, you have to hold in your head:

- what you asked for,
- what the code actually does,
- what assumptions it made,
- and whether those assumptions fit your data.

Verifying code you did not write is frequently harder than writing it yourself. When the AI also reaches for a library you have not seen, an advanced language feature, or an abstraction the lesson has not covered, the work of understanding grows instead of shrinks. We will name these moments when they come up.

::::::::::::::::::::::::::::::::::::::::: instructor

## Instructor note: set the tone early

The goal of this episode is to reset expectations before learners open a terminal. Some will arrive expecting a productivity demo. Be explicit that the workshop measures whether they can *explain and validate* AI output, not how fast they can generate it.

Signs to watch for across the whole workshop:

- Learners who are impressed that the agent can read their files but cannot say what it changed.
- Learners who accept output they cannot explain because "it ran."
- Learners who turn to the AI before turning to a helper, which hides where they are stuck.

Normalise bringing AI confusion back into the room. Treat confusing AI output as a shared teaching artifact, not a personal failure.

::::::::::::::::::::::::::::::::::::::::::::::::::

## The run / revise / reject checkpoint

Every time the AI hands you something, you make a decision. Make it on purpose. Ask:

1. **Can I explain what this does?** If not, you are not ready to approve it.
2. **What did it assume about my data?** Name at least one assumption.
3. **What evidence do I have that it is correct?** "It ran" is not evidence of correctness.
4. **Decision:** run it, revise it, or reject it.

You will use this same checkpoint, in more detail, throughout the lesson.

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: practise the checkpoint

Read this short snippet that an agent produced in response to "remove the bad rows from my data":

```python
import pandas as pd
df = pd.read_csv("data.csv")
df = df.dropna()
df.to_csv("clean.csv", index=False)
```

Without running anything, answer in a sentence or two each:

1. In plain language, what does this script do?
2. What does it assume "bad rows" means?
3. Name one way this could quietly damage a real research dataset.
4. Would you run it, revise it, or reject it for a dataset where missing values are meaningful (for example, a survey where "no answer" is a valid response)?

:::::::::::::::::::::::::::::::::::::::: solution

1. It reads `data.csv`, drops every row that has a missing value in *any* column, and writes the result to `clean.csv`.
2. It assumes "bad rows" means "rows with any missing value." That is the AI's interpretation, not yours.
3. `dropna()` with no arguments removes a row if *any* column is empty. In a wide dataset, one empty optional field can delete an otherwise complete observation, silently shrinking your sample.
4. Revise or reject. For data where missingness is meaningful, dropping those rows changes what the data represents. You would constrain which columns to check, or impute, instead. The code runs perfectly and is still wrong for your question.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: discussion

## Feedback checkpoint: what do you want from AI?

On a sticky note or in the shared Etherpad, write one line: *what do you most want an AI tool to do for your research, and what are you most worried it will get wrong?*

We will come back to these at the end of the lesson.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- This lesson teaches you to inspect, question, constrain, and validate AI output, not to delegate your thinking.
- Generation, understanding, and validation are different skills. Generation is the easy one.
- For a novice, verifying generated code can cost more effort than writing it.
- Working code is not the same as trustworthy code. Use the run / revise / reject checkpoint every time.

::::::::::::::::::::::::::::::::::::::::::::::::::
