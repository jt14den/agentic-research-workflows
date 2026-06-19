# CLAUDE.example.md

This is a reference Living Spec for the coastal-water-quality project. You will build
your own `CLAUDE.md` with `/init` in Episode 2 and grow it as you go. Use this only if
you get stuck or want to compare. (Claude Code auto-loads `CLAUDE.md`, not this file.)

---

# Project: Coastal Water Quality Trends

## Goal
Clean and merge three messy site files into `data/master_dataset.csv`, then analyse the
trend in water quality score over time by site.

## Canonical schema (the merged file must use these names)
- `site` (A, B, or C)
- `sample_id` (original station ID)
- `date` (ISO `YYYY-MM-DD`)
- `score` (0-100)
- `pH` (~6.5-8.5)
- `temp_c` (Celsius)

## Rules of the road
- Use `pandas` for data handling and `matplotlib` for plots.
- Site C dates are day-month-year (`05-01-2023` is 5 January). Parse them explicitly;
  do not let the tool guess the format.
- Fill missing `score` with the site median. Leave missing `pH`/`temp_c` blank and note
  them; do not invent values.

## No-go zones (the AI must not do these)
- Do not drop any sample rows. The merged file must have 60 rows.
- Do not rename or alter the raw files in `data/site_*.csv`.
- Do not change a value to make a check pass.

## Verification gates (how we know it is done)
- `python validate_data.py` passes.
- 60 rows, all six canonical columns present.
- All dates fall in 2023; site C's January samples are in January, not May.
- `score` values are within 0-100.
