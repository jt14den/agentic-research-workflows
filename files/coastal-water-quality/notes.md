# Research Notes

## Context

This dataset supports a study of coastal water quality trends in the Santa Monica Bay watershed. Weekly samples were collected at three sites by different field teams using different data collection tools, which created inconsistencies in the raw files.

## Questions we want to answer

- Is water quality improving or declining across the monitoring period?
- Are there meaningful differences between sites?
- What is the relationship between temperature and water quality score?

## Data decisions to document

- How missing values are handled (imputation strategy, or dropped?)
- Which date format is used as the standard
- What the canonical column names are in the merged file

## Next steps

1. Inspect each file for inconsistencies
2. Define a cleaning and merging strategy
3. Validate the merged output against known site counts
4. Generate summary plots for each site
