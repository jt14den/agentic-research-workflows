"""
validate_data.py - checks for the merged coastal water quality dataset.

This validator is INTENTIONALLY INCOMPLETE. Most checks are written for you. One
check, the date check, is a stub marked TODO. In the validation episode you will
write it from the source documentation (yourself, or with AI help that you review).

An unfinished check counts as a failure. The script exits with an error until you
finish it, so a finished-looking run never hides missing work.

Run it after you create data/master_dataset.csv:

    python validate_data.py [path/to/merged.csv]
"""
import sys
import pandas as pd

PATH = sys.argv[1] if len(sys.argv) > 1 else "data/master_dataset.csv"
EXPECTED_ROWS = 60
CANONICAL_COLUMNS = ["site", "sample_id", "date", "score", "pH", "temp_c"]

# Raw file layout, from the documentation in README.md. These are source facts.
RAW_SITES = {
    "A": {"file": "data/site_A.csv", "id": "SiteID", "score": "WaterQualityScore"},
    "B": {"file": "data/site_B.csv", "id": "id", "score": "score"},
    "C": {"file": "data/site_C.csv", "id": "StationID", "score": "Quality_Index"},
}

failures = []
incomplete = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}{(' - ' + detail) if detail and not condition else ''}")
    if not condition:
        failures.append(name)


def todo(name):
    print(f"[INCOMPLETE] {name} - not written yet")
    incomplete.append(name)


def main():
    try:
        df = pd.read_csv(PATH)
    except FileNotFoundError:
        print(f"Could not find {PATH}. Create the merged file first.")
        sys.exit(1)

    # Check 1 (written for you): row count invariant - no rows lost in the merge.
    check("row count is 60", len(df) == EXPECTED_ROWS, f"found {len(df)}")

    # Check 2 (written for you): all canonical columns are present.
    missing_cols = [c for c in CANONICAL_COLUMNS if c not in df.columns]
    check("all canonical columns present", not missing_cols, f"missing {missing_cols}")
    if missing_cols:
        print("Stopping: the remaining checks need every canonical column.")
        sys.exit(1)

    # Check 3 (written for you): every raw sample_id appears exactly once, with its
    # site. The raw files say which site each ID belongs to.
    expected_site = {}
    for site, cfg in RAW_SITES.items():
        for sample_id in pd.read_csv(cfg["file"])[cfg["id"]]:
            expected_site[str(sample_id)] = site
    seen = df["sample_id"].astype(str).value_counts()
    problems = (
        sorted(set(expected_site) - set(seen.index))
        + sorted(seen[seen > 1].index)
        + sorted(set(seen.index) - set(expected_site))
    )
    check("every sample_id appears exactly once", not problems, f"problems: {problems[:3]}")
    wrong_site = sorted(
        str(sid) for sid, site in zip(df["sample_id"], df["site"])
        if expected_site.get(str(sid)) != site
    )
    check("every sample_id carries its source site", not wrong_site,
          f"{len(wrong_site)} wrong, e.g. {wrong_site[:3]}")

    # Check 4 (written for you): every score is a number between 0 and 100.
    # Blank or text scores fail. They are not skipped.
    numeric = pd.to_numeric(df["score"], errors="coerce")
    bad = df.loc[numeric.isna() | ~numeric.between(0, 100), "sample_id"]
    check("every score is a number within 0-100", bad.empty,
          f"{len(bad)} bad, e.g. {list(bad.astype(str))[:3]}")

    # Check 5 (written for you): a missing raw score is filled with its site's median
    # of the observed scores. Observed scores stay exactly as they were.
    wrong_scores = []
    for site, cfg in RAW_SITES.items():
        raw = pd.read_csv(cfg["file"])
        raw_scores = pd.to_numeric(raw[cfg["score"]], errors="coerce")
        median = raw_scores.median()
        merged = df.set_index(df["sample_id"].astype(str))["score"]
        for sample_id, raw_score in zip(raw[cfg["id"]], raw_scores):
            want = median if pd.isna(raw_score) else raw_score
            got = pd.to_numeric(pd.Series([merged.get(str(sample_id))]), errors="coerce").iloc[0]
            if pd.isna(got) or abs(got - want) > 1e-9:
                wrong_scores.append(str(sample_id))
    check("observed scores unchanged; missing scores use the site median",
          not wrong_scores, f"{len(wrong_scores)} wrong, e.g. {wrong_scores[:3]}")

    # Check 6 (TODO, you write it): every sample's date matches the raw source.
    #   Use the source documentation in README.md for each site's date format.
    #   Do not copy the format from clean_and_merge.py: that script is the thing
    #   you are testing, and it may contain the mistake.
    #   Hint: "parses without error and falls in 2023" is NOT enough. A misparsed
    #   site C date (05-01-2023 read as month-day) still looks like a valid 2023 date.
    #   Re-parse each raw site file with its documented format and compare the
    #   result to the merged file, sample_id by sample_id.
    todo("every sample's date matches the raw source")

    print()
    if failures:
        print(f"{len(failures)} check(s) failed:", ", ".join(failures))
    if incomplete:
        print(f"{len(incomplete)} check(s) not written yet:", ", ".join(incomplete))
    if failures or incomplete:
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
