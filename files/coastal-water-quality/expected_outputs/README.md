# Expected outputs

What a correct run produces. Use this to check your own work and as an instructor
reference. The data are synthetic. The rules here belong to the exercise.

## `data/master_dataset.csv`

- 60 rows (3 sites x 20 weekly samples). No rows dropped.
- Six columns: `site`, `sample_id`, `date`, `score`, `pH`, `temp_c`.
- Every `sample_id` appears once, with its source site (A, B or C).
- Dates in ISO `YYYY-MM-DD`, all within 2023, roughly 2023-01-05 to 2023-05-18.
  - Common mistake: site C dates (`05-01-2023` is 5 January, day-month-year) parsed
    without an explicit format. Do not rely on eyeballing the date range. A partial
    misparse (some rows swapped, some correct by accident, since a day over 12 cannot
    be a month) can still show a January minimum. Compare site C's dates with the raw
    file sample by sample, or re-parse with the explicit `%d-%m-%Y` format and diff.
- `score` is numeric, present and within 0-100.
  - Observed scores are unchanged.
  - Exercise rule: a missing score takes the median of that site's observed scores.
    A004 = 72.0, B-006 = 71.5, SC002 = 71.6. A real study would have to justify its
    own method. Any alternative method belongs in a separate extension, not here.
- Missing `pH` and `temp_c` values stay missing. All other values are preserved.

## Trend plot

- One labelled line per site, `score` (y) over `date` (x), January to mid-May 2023,
  dates in order.
- Sanity check: all three lines look like a continuous weekly series across the full
  range. If site C's points look scattered or out of order, that is the date-parsing
  bug above. A partial misparse rarely bunches neatly at one edge.

## `validate_data.py`

- The starter has most checks written and the date check left for you. It exits with
  an error until you finish that check.
- After you write it, every check passes on a correct merge.
- A correct validator fails on a file where site C dates were misparsed, where a row
  was dropped, where a score is blank, nonnumeric or outside 0-100, where a site
  label is wrong, or where an imputed value is not the site median.
- The instructor reference (`instructors/files/backup_validate_data.py`) has eight
  checks. `instructors/files/test_validators.py` tests it against good and bad files.

## Feb-onward filter (Episode 3 challenge)

- `data/feb_onward.csv`: 48 rows (12 January rows removed). The canonical
  `data/master_dataset.csv` stays at 60 rows.
