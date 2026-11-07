# Research Notes

> Synthetic teaching dataset. The study described here is made up for the lesson.
> The sites, the study context and the questions below are fiction. Do not cite
> them as real research.

## Context

This fictional dataset stands in for a study of coastal water quality trends. Weekly samples were collected at three sites by different field teams using different data collection tools, which created inconsistencies in the raw files.

## Questions the fictional study asks

- Does the water quality score show a visible pattern over the monitoring period?
- Do the sites look different from each other?
- How do temperature and water quality score appear to relate?

These are descriptive questions. The lesson does not teach the statistics needed to answer them with confidence.

## Data decisions to document

- How missing values are handled. In this exercise the rule is fixed: a missing score takes the median of that site's observed scores. A real study would justify its own method.
- Which date format is the standard. The exercise uses ISO `YYYY-MM-DD`.
- What the canonical column names are in the merged file.

## Next steps

1. Inspect each file for inconsistencies.
2. Define a cleaning and merging strategy.
3. Check the merged output against known site counts and the raw files.
4. Generate summary plots for each site.
