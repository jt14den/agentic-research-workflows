# Instructor key (do not give to learners)

Values below were produced on 2026-11-27 with the reference scripts.

## Part 2

The bad copy changes 8 site C dates. All stay valid dates. A good date check fails.
A non-zero exit status reports that a check failed or is unfinished.

## Part 3

| Step | Expected |
|---|---|
| Cleaner on batch 2 | writes 12 rows without error |
| Validator before the change | the 60-row check fails |
| Expected count taken from the raw files, one row deleted from site A | every check can pass on 11 rows. In our run the reference validator passed all 8 |
| Expected count 12 from the delivery note, one row deleted | the row count check fails |
| `format="mixed"` on batch 2 site C | 2 of 4 dates wrong: 01-06-2023 becomes 2023-01-06, 08-06-2023 becomes 2023-08-06 |
| Missing score B-023, this delivery only | 66.2 (what the unchanged cleaner writes) |
| Missing score B-023, both deliveries | 70.95 |
| For comparison, first delivery only | 71.5 |

The median has no correct answer here. The written rule was made for one delivery
and does not say. A strong answer notices that the program already chose "this
delivery" without anyone deciding, names who should decide, and notes that the
validator encodes the same choice, so its pass cannot settle it. Do not tell
learners which rule is right.

The delivery note supplies an expectation from outside the files. It can also be
wrong. Credit learners who say so.

## Final task A

Use `instructors/files/transfer_candidate.csv`, saved as `data/candidate.csv`.
`B-009` appears twice and `B-014` is missing. The starter validator learners have
already checks ID uniqueness, so ask them to decide before running it. This is
near transfer: same project, and the uniqueness idea has been seen.

## Final task B

The record checks `candidate.csv` and plots `master_dataset.csv`. It does not
support the plot. A good next step validates the file the plot reads, or shows the
two files are identical, then regenerates the plot. Still untested: whatever the
validator does not check, the plot code, and the scientific claim.
