# Trial: capture, name and reuse a checked workflow

Status: draft, 2026-11-27. Not taught or tested with learners. This folder is not
part of the built lesson.

## Purpose under test

Learners practise computational thinking through AI-assisted research: define a
problem, break it into clear steps, capture them in a reusable program, and test
whether it meets the research need.

The word is "practise". This trial cannot show that the lesson develops
computational thinking or that skills transfer.

## What the trial can and cannot show

It can show where learners get stuck, whether the reuse step raises the decisions
we expect, and whether tool mechanics crowd out checking. With a handful of
learners it cannot show that this version teaches better than the current one.

## Files

| File | For | What it is |
|---|---|---|
| `episode-map.md` | authors | the learner path mapped to the episodes, with cuts |
| `trial-lesson.md` | learners | self-paced material, planned at 45 minutes |
| `entry-check.md` | learners | 10 minutes, no AI |
| `final-tasks.md` | learners | 10 minutes, no AI |
| `instructor-key.md` | instructor only | expected results and answers |
| `observation-sheet.md` | observer | one per learner |
| `data/batch2/` | learners | second synthetic delivery, 4 samples per site |
| `start/clean_and_merge.py` | learners | the supplied cleaner |

## Before a session

1. Give each learner a copy of `coastal-water-quality` with
   `start/clean_and_merge.py` added. It is the reference cleaner without the
   header and comments that give away answers.
2. Give them `data/batch2/` as a folder named `batch2` next to it.
3. Do not give them `instructor-key.md`. If this branch is public, the key is
   public too, so recruit learners before pointing anyone to the repository.
4. Agree how you will handle consent and notes. If results may be published or
   shared as research, ask whether ethics review is needed first.
