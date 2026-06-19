"""
validate_data.py - checks for the merged coastal water quality dataset.

This validator is INTENTIONALLY INCOMPLETE. Two checks are written for you; the
rest are stubs marked TODO. In the validation episode you will implement the stubs
(yourself or with AI help that you review) so the validator actually proves the
merged file is trustworthy.

Run it after you create data/master_dataset.csv:

    python validate_data.py
"""
import sys
import pandas as pd

PATH = "data/master_dataset.csv"
EXPECTED_ROWS = 60
CANONICAL_COLUMNS = ["site", "sample_id", "date", "score", "pH", "temp_c"]

failures = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}{(' - ' + detail) if detail and not condition else ''}")
    if not condition:
        failures.append(name)


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

    # Check 3 (TODO): dates parse and all fall within 2023.
    #   Hint: pd.to_datetime(df["date"]) should not raise, and every year should be 2023.
    #   The point of this check is to catch site C's day-month-year dates being misread.
    print("[TODO] dates parse and all fall in 2023 - implement this check")

    # Check 4 (TODO): no sample_id was lost - every original ID appears exactly once.
    #   Hint: compare the set of sample_ids in the merge to the raw site files.
    print("[TODO] every original sample_id is present exactly once - implement this check")

    # Check 5 (TODO): score values are plausible (within 0-100).
    #   Hint: ignore blanks, then check the min and max.
    print("[TODO] score values fall within 0-100 - implement this check")

    print()
    if failures:
        print(f"{len(failures)} check(s) failed:", ", ".join(failures))
        sys.exit(1)
    print("All implemented checks passed. (Remember: the TODO checks are not done yet.)")


if __name__ == "__main__":
    main()
