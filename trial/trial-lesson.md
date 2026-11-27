# Trial lesson: can you use this program again?

About 45 minutes. This time is a guess. Work at your own pace and note the time at
the start of each part.

You have `coastal-water-quality`, which holds the three site files, a working
`clean_and_merge.py` that was supplied to you, and `validate_data.py` with one
check missing. You may ask an AI agent to explain things. Where a step says
**by hand**, write or edit it yourself. You may use the Python documentation.

The data are synthetic.

## Part 1. Break it down (8 minutes)

Before you open `clean_and_merge.py`, and without asking the agent:

1. Write the steps needed to turn three site files into one checked file.
2. What happens the same way for every site? What differs?
3. What goes in? What should come out? What must not change?

Now read `clean_and_merge.py`. Find `clean_site` and `SITES`. Which of your
"same" items are in the function, and which of your "differs" items are in the
table? What would you change in your list, or in the program?

Pick the line that fills a missing score. Write what it changes and what it must
preserve. Then run the program and test your prediction.

## Part 2. Check it (15 minutes)

1. Run `python validate_data.py`. Read what is unfinished.
2. Study a worked example before you write anything. This finished check from
   `validate_data.py` tests that every sample ID has the right site. A label
   above each part says what that part is for.

   ```python
   # Purpose: get the expected values from the raw files
   expected_site = {}
   for site, cfg in RAW_SITES.items():
       for sample_id in pd.read_csv(cfg["file"])[cfg["id"]]:
           expected_site[str(sample_id)] = site

   # Purpose: match each merged row to its expected value by ID, and keep
   # the ones that differ
   wrong_site = sorted(
       str(sid) for sid, site in zip(df["sample_id"], df["site"])
       if expected_site.get(str(sid)) != site
   )

   # Purpose: report the differences, so a person or a program can act
   check("every sample_id carries its source site", not wrong_site,
         f"{len(wrong_site)} wrong, e.g. {wrong_site[:3]}")
   ```

   Why match by ID and not by row position? Say what could go wrong.
3. Find each site's date format in `README.md`. **By hand**, finish the date
   check. Take expected values from the raw files, not from the cleaner.
4. Run it until the correct output passes.
5. **By hand**, add a `# Purpose:` label above each part of your date check. Use
   your own words for what the part is for, not a restatement of the code. For
   each part, write one thing that could go wrong if it were missing or wrong.
6. Make a bad copy that your check should reject:

   ```bash
   python -c "
   import pandas as pd
   good = pd.read_csv('data/master_dataset.csv')
   raw = pd.read_csv('data/site_C.csv')
   wrong = pd.to_datetime(raw['DateTime'], format='mixed').dt.strftime('%Y-%m-%d')
   lookup = dict(zip(raw['StationID'], wrong))
   c = good['site'] == 'C'
   good.loc[c, 'date'] = good.loc[c, 'sample_id'].map(lookup)
   good.to_csv('data/candidate.csv', index=False)
   "
   python validate_data.py data/candidate.csv
   echo $?
   ```

7. What did the number printed by `echo $?` tell another program? What would a `0`
   not tell you?
8. Delete `data/candidate.csv`.

## Part 3. Reuse it (17 minutes)

A second delivery arrives. Its delivery note says:

> Samples from 25 May to 15 June 2023. Four samples from each of the three sites.
> Same instruments and file formats as the first delivery. One score is missing.

1. Set up a separate folder. From inside `coastal-water-quality`:

   ```bash
   mkdir ../batch2-run
   ```

   If the folder already exists, stop and ask. Then:

   ```bash
   mkdir ../batch2-run/data
   cp clean_and_merge.py validate_data.py ../batch2-run/
   cp ../batch2/site_*.csv ../batch2-run/data/
   cd ../batch2-run
   ```

2. **Predict** before you run anything. Which steps will work unchanged? What
   will fail? What might run and still be wrong?
3. Run the cleaner and then the validator. Compare with your prediction.
4. Something expects the first delivery. **By hand**, change the validator so the
   expected row count is an input. For example, this reads it from the command
   and keeps 60 when none is given:

   ```python
   EXPECTED_ROWS = int(sys.argv[2]) if len(sys.argv) > 2 else 60
   ```

   Also correct the check's printed name. Run:

   ```bash
   python validate_data.py data/master_dataset.csv 12
   ```

5. Why not count the rows in the raw files to get the expected number? Test your
   answer: save a copy of `data/site_A.csv`, delete its last row, rerun the
   cleaner and the validator with `12`, then restore the file and rerun the
   cleaner. What did the delivery note give you that the files could not?
6. Look at the filled score for the missing value. The project rule says: fill a
   missing score with the median of that site's observed scores. Which scores is
   that: this delivery, or all deliveries so far? Calculate both **by hand or
   with your own short code**. The first delivery is in
   `../coastal-water-quality/data/`.
7. Does the rule settle it? Choose one: use this delivery, use all data so far, or
   stop and ask the person who owns the rule. Give your reason, say who should
   decide, and say what would have to change in the cleaner **and** the validator.
   You do not need to make that change. If the rule is not settled, mark the
   output as provisional.

## Part 4. Name it (5 minutes)

At the top of your copy of `clean_and_merge.py`, **by hand**, write a short note
for the next person:

- what it expects to find, and where you must run it from
- what it writes
- what it assumes, including the date formats and the median decision
- one thing it does not check

Would you keep the name `clean_and_merge.py`? Say why.
