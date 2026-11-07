"""
backup_validate_data.py - complete instructor reference validator.

All checks are implemented. Use this to generate real transcripts for the
lesson, to demo a full validator to a learner who is stuck, or as an answer
key when reviewing learner implementations of validate_data.py.

The expected values come from the raw site files and the documented source
formats, never from the cleaner's code. That keeps the validator independent
of the script it is testing.

The date check does NOT just verify "parses without error and falls in 2023".
That weaker check passes on a misparsed file, because a wrong month-day reading
of site C's dates still produces a valid-looking 2023 date. Instead this
re-parses each raw site file with its documented format and compares the result
to the merged file, sample_id by sample_id.

Run from inside the coastal-water-quality folder:

    python backup_validate_data.py [path/to/merged.csv]

Exit status: 0 when every check passes, 1 when any check fails.
"""
import sys
import pandas as pd

PATH = sys.argv[1] if len(sys.argv) > 1 else "data/master_dataset.csv"
EXPECTED_ROWS = 60
CANONICAL_COLUMNS = ["site", "sample_id", "date", "score", "pH", "temp_c"]

# How each raw file is laid out, per its documentation. These are source facts.
RAW_SITES = {
    "A": {"file": "data/site_A.csv", "id": "SiteID", "date": "Collection_Date",
          "date_format": "%Y/%m/%d", "score": "WaterQualityScore",
          "pH": "pH", "temp_c": "Temperature_C"},
    "B": {"file": "data/site_B.csv", "id": "id", "date": "date",
          "date_format": "%b %d %Y", "score": "score",
          "pH": "ph", "temp_c": "temp"},
    "C": {"file": "data/site_C.csv", "id": "StationID", "date": "DateTime",
          "date_format": "%d-%m-%Y", "score": "Quality_Index",
          "pH": "pH_Level", "temp_c": "Water_Temp"},
}

failures = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}{(' - ' + detail) if detail and not condition else ''}")
    if not condition:
        failures.append(name)


def load_expected():
    """Rebuild the correct per-sample facts from the raw files."""
    rows = {}
    for site, cfg in RAW_SITES.items():
        raw = pd.read_csv(cfg["file"])
        dates = pd.to_datetime(raw[cfg["date"]], format=cfg["date_format"])
        site_median = pd.Series(
            pd.to_numeric(raw[cfg["score"]], errors="coerce")
        ).median()
        for i, sample_id in enumerate(raw[cfg["id"]]):
            rows[str(sample_id)] = {
                "site": site,
                "date": dates.iloc[i].strftime("%Y-%m-%d"),
                "score": raw[cfg["score"]].iloc[i],
                "pH": raw[cfg["pH"]].iloc[i],
                "temp_c": raw[cfg["temp_c"]].iloc[i],
                "site_median": site_median,
            }
    return rows


def same(a, b):
    """Equal values, or both missing."""
    if pd.isna(a) and pd.isna(b):
        return True
    if pd.isna(a) or pd.isna(b):
        return False
    return abs(float(a) - float(b)) < 1e-9


def main():
    try:
        df = pd.read_csv(PATH)
    except FileNotFoundError:
        print(f"Could not find {PATH}. Create the merged file first.")
        sys.exit(1)

    check("row count is 60", len(df) == EXPECTED_ROWS, f"found {len(df)}")

    missing_cols = [c for c in CANONICAL_COLUMNS if c not in df.columns]
    check("all canonical columns present", not missing_cols, f"missing {missing_cols}")
    if missing_cols:
        print()
        print(f"{len(failures)} check(s) failed:", ", ".join(failures))
        print("Stopping: the remaining checks need every canonical column.")
        sys.exit(1)

    expected = load_expected()
    by_id = {str(r.sample_id): r for r in df.itertuples(index=False)}

    ids_seen = df["sample_id"].astype(str).value_counts()
    missing_ids = sorted(set(expected) - set(ids_seen.index))
    extra_ids = sorted(set(ids_seen.index) - set(expected))
    duplicate_ids = sorted(ids_seen[ids_seen > 1].index)
    check(
        "every original sample_id is present exactly once",
        not missing_ids and not duplicate_ids and not extra_ids,
        f"missing {missing_ids}, duplicated {duplicate_ids}, unexpected {extra_ids}",
    )

    wrong_site = sorted(
        sid for sid, exp in expected.items()
        if sid in by_id and str(by_id[sid].site) != exp["site"]
    )
    check(
        "every sample_id carries its source site",
        not wrong_site,
        f"{len(wrong_site)} wrong, e.g. {wrong_site[:3]}",
    )

    wrong_dates = sorted(
        sid for sid, exp in expected.items()
        if sid in by_id and str(by_id[sid].date) != exp["date"]
    )
    check(
        "every sample's date matches the raw source",
        not wrong_dates,
        f"{len(wrong_dates)} mismatch(es), e.g. {wrong_dates[:3]}",
    )

    numeric = pd.to_numeric(df["score"], errors="coerce")
    bad_scores = sorted(
        df.loc[numeric.isna() | ~numeric.between(0, 100), "sample_id"].astype(str)
    )
    check(
        "every score is a number within 0-100 (none blank or text)",
        not bad_scores,
        f"{len(bad_scores)} bad, e.g. {bad_scores[:3]}",
    )

    bad_score_values = []
    for sid, exp in expected.items():
        if sid not in by_id:
            continue
        got = pd.to_numeric(pd.Series([by_id[sid].score]), errors="coerce").iloc[0]
        want = exp["site_median"] if pd.isna(exp["score"]) else exp["score"]
        if not same(got, want):
            bad_score_values.append(sid)
    check(
        "observed scores are unchanged and missing scores use the site median",
        not bad_score_values,
        f"{len(bad_score_values)} wrong, e.g. {sorted(bad_score_values)[:3]}",
    )

    bad_other = []
    for sid, exp in expected.items():
        if sid not in by_id:
            continue
        row = by_id[sid]
        if not (same(row.pH, exp["pH"]) and same(row.temp_c, exp["temp_c"])):
            bad_other.append(sid)
    check(
        "pH and temp_c keep their source values (blanks stay blank)",
        not bad_other,
        f"{len(bad_other)} changed, e.g. {sorted(bad_other)[:3]}",
    )

    print()
    if failures:
        print(f"{len(failures)} check(s) failed:", ", ".join(failures))
        sys.exit(1)
    print("All 8 checks passed.")


if __name__ == "__main__":
    main()
