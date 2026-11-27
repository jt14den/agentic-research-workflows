# Final tasks (10 minutes, no AI)

Work alone. Decide before you run any supplied validator.

## Task A. A file from someone else

Your instructor gives you a merged file from the first delivery. It has 60 rows.
Would you approve it for a per-site plot?

1. Name one property it must have, other than the row count, and where the
   expected values come from.
2. Write and run a short check. If it passes, say what it leaves untested.
3. Approve, revise or reject. Give your evidence and one thing you did not check.

## Task B. A colleague's record

A colleague sends this record and writes, "All checks passed, so the plot is
good." The plot program is the lesson's `plot_trend.py`, which reads
`data/master_dataset.csv`.

```
$ python validate_data.py data/candidate.csv
...
All checks passed.
$ echo $?
0
$ python plot_trend.py
Wrote fig/score_trend.png
```

1. Does the record support the plot? Say why.
2. What would you run or ask for next?
3. What would still be untested after that?
