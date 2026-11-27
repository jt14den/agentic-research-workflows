# Entry check (10 minutes, no AI)

Work alone. "I am not sure" is a useful answer. This sorts out what support you
need. It does not exclude you.

You are in a folder named `coastal-water-quality`.

1. What does the path `data/site_A.csv` mean? Which file would it mean if you ran
   the same command from the folder above?
2. Run `python date_review.py`. What did it print?
3. In `python validate_data.py data/candidate.csv`, which part is the program and
   which part is the input you gave it?
4. For this command, say what is read and what is written:
   `cp data/master_dataset.csv data/candidate.csv`
5. What does this change in `df`, and what does it leave alone?

   ```python
   df["score"] = df["score"].fillna(df["score"].median())
   ```

6. Four samples per site arrive from three sites. How many rows should a merged
   file have?
