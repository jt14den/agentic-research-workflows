# Coastal Water Quality Monitoring

> **Synthetic teaching dataset.** These files were created for this lesson. The
> sites, numbers, and "issues" are made up to be realistic, not real measurements.
> Do not cite this data.

A multi-site water quality dataset from three monitoring stations along the Southern
California coast, collected weekly from January to May 2023. This is the project you
work in throughout the lesson: you will clean and merge the files, validate the
result, run a small trend analysis, and document the whole thing.

## Sites

| Site | Location | File |
|---|---|---|
| A | Malibu Creek outflow | `data/site_A.csv` |
| B | Santa Monica Bay nearshore | `data/site_B.csv` |
| C | Ballona Creek estuary | `data/site_C.csv` |

## Research goal

Combine the three site files into a single clean dataset, then answer: **is the
water quality score trending up or down over the monitoring period, and does it
differ by site?**

## Known issues (the reason this needs cleaning)

- Column names differ across sites (`SiteID` vs `id` vs `StationID`, and the score
  column is `WaterQualityScore` vs `score` vs `Quality_Index`).
- Date formats differ across sites: site A uses `2023/01/05` (year/month/day), site B
  uses `Jan 5 2023`, and **site C uses `05-01-2023` (day-month-year)**. That last one
  is a trap: read carelessly, `05-01-2023` looks like 1 May but means 5 January.
- Some missing values in the score, pH, and temperature columns.

## Canonical schema for the merged file

Target file: `data/master_dataset.csv`, one row per sample, with these columns:

| Column | Meaning |
|---|---|
| `site` | A, B, or C |
| `sample_id` | the original station ID (e.g. `A001`, `B-001`, `SC001`) |
| `date` | ISO format, `YYYY-MM-DD` |
| `score` | water quality score, expected range 0-100 |
| `pH` | expected range roughly 6.5-8.5 |
| `temp_c` | water temperature in Celsius |

## What "done" looks like

- 60 rows in `data/master_dataset.csv` (3 sites x 20 weekly samples), no rows dropped.
- All dates parsed correctly (site C's January samples must not land in May).
- A documented strategy for the missing values.
- A trend plot of `score` over `date`, one line per site.
