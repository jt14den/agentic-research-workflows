# Expected outputs

What a correct run should produce. Use this to check your own work and as an
instructor reference. Exact values may vary slightly with your missing-value
strategy, but the structure and the sanity checks should hold.

## `data/master_dataset.csv`

- **60 rows** (3 sites x 20 weekly samples). No rows dropped.
- **Six columns:** `site`, `sample_id`, `date`, `score`, `pH`, `temp_c`.
- **Dates** in ISO `YYYY-MM-DD`, all within 2023, roughly 2023-01-05 to 2023-05-18.
  - Common mistake: site C dates (`05-01-2023` = 5 January, day-month-year) parsed
    without an explicit format. Don't rely on eyeballing the date range to catch
    this: a partial misparse (some rows swapped, some accidentally correct, since a
    day value over 12 can't be mistaken for a month) can still show a January
    minimum. Compare site C's dates against the raw file sample by sample, or
    re-parse with the explicit `%d-%m-%Y` format and diff the result.
- **`score`** values within 0-100. Missing scores filled with the site median (a few
  per the raw files); `pH` and `temp_c` may still contain blanks if you chose not to
  impute them.

## Trend plot

- One line per site, `score` (y) over `date` (x), Jan to mid-May 2023.
- Sanity check: all three lines should look like a continuous weekly series across
  the full date range. If site C's points look scattered or out of order, rather
  than the whole line cleanly shifted to one edge, that's the date-parsing bug
  above — a partial misparse rarely bunches neatly at one edge.

## `validate_data.py`

- After you implement the TODO checks, all five should pass against a correct merge.
- A correct validator should FAIL on a file where site C dates were misparsed, where a
  row was dropped, or where a score is outside 0-100.
