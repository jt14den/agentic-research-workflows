"""
backup_validate_data.py - complete instructor reference validator.

All five checks implemented. Use this to generate real transcripts for the
lesson, to demo a full validator to a learner who is stuck, or as an answer
key when reviewing learner implementations of validate_data.py.

Crucially, the date check does NOT just verify "parses without error and falls
in 2023" - that weaker check passes even on a misparsed file, because a wrong
month-day reading of site C's dates still produces a valid-looking 2023 date.
Instead this re-parses each raw site file with its known date format and
compares the result to master_dataset.csv, sample_id by sample_id.

Run from inside the coastal-water-quality folder: python backup_validate_data.py
"""
import sys
import pandas as pd

PATH = "data/master_dataset.csv"
EXPECTED_ROWS = 60
CANONICAL_COLUMNS = ["site", "sample_id", "date", "score", "pH", "temp_c"]

RAW_SITES = {
    "A": {"file": "data/site_A.csv", "id_col": "SiteID", "date_col": "Collection_Date", "date_format": "%Y/%m/%d"},
    "B": {"file": "data/site_B.csv", "id_col": "id", "date_col": "date", "date_format": "%b %d %Y"},
    "C": {"file": "data/site_C.csv", "id_col": "StationID", "date_col": "DateTime", "date_format": "%d-%m-%Y"},
}

failures = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}{(' - ' + detail) if detail and not condition else ''}")
    if not condition:
        failures.append(name)


def expected_dates():
    """Reconstruct the correct sample_id -> date mapping from the raw files."""
    expected = {}
    for cfg in RAW_SITES.values():
        raw = pd.read_csv(cfg["file"])
        parsed = pd.to_datetime(raw[cfg["date_col"]], format=cfg["date_format"])
        for sample_id, date in zip(raw[cfg["id_col"]], parsed):
            expected[str(sample_id)] = date.strftime("%Y-%m-%d")
    return expected


def main():
    try:
        df = pd.read_csv(PATH)
    except FileNotFoundError:
        print(f"Could not find {PATH}. Create the merged file first.")
        sys.exit(1)

    check("row count is 60", len(df) == EXPECTED_ROWS, f"found {len(df)}")

    missing_cols = [c for c in CANONICAL_COLUMNS if c not in df.columns]
    check("all canonical columns present", not missing_cols, f"missing {missing_cols}")

    expected = expected_dates()
    actual = dict(zip(df["sample_id"].astype(str), df["date"].astype(str)))
    mismatches = sorted(
        sid for sid, exp_date in expected.items()
        if actual.get(sid) != exp_date
    )
    check(
        "every sample's date matches the raw source",
        not mismatches,
        f"{len(mismatches)} mismatch(es), e.g. {mismatches[:3]}",
    )

    ids_seen = df["sample_id"].astype(str).value_counts()
    missing_ids = sorted(set(expected) - set(ids_seen.index))
    duplicate_ids = sorted(ids_seen[ids_seen > 1].index)
    check(
        "every original sample_id is present exactly once",
        not missing_ids and not duplicate_ids,
        f"missing {missing_ids}, duplicated {duplicate_ids}",
    )

    scores = pd.to_numeric(df["score"], errors="coerce").dropna()
    check(
        "score values fall within 0-100",
        not scores.empty and scores.between(0, 100).all(),
        f"min {scores.min() if not scores.empty else 'n/a'}, max {scores.max() if not scores.empty else 'n/a'}",
    )

    print()
    if failures:
        print(f"{len(failures)} check(s) failed:", ", ".join(failures))
        sys.exit(1)
    print("All 5 checks passed.")


if __name__ == "__main__":
    main()
