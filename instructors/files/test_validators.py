"""
test_validators.py - test the validator itself against known-good and known-bad files.

A validator that passes everything is worse than none. This script builds one good
file and several deliberately broken ones in a temporary copy of the project, then
checks that the validator passes the good file and fails each bad one.

Run from the agentic-research-workflows folder:

    python instructors/files/test_validators.py

Exit status: 0 when every case behaves as expected, 1 otherwise.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent / "learners" / "files" / "coastal-water-quality"
VALIDATOR = HERE / "backup_validate_data.py"
CLEANER = HERE / "backup_clean_and_merge.py"


def run(cmd, cwd):
    return subprocess.run([sys.executable, *cmd], cwd=cwd, capture_output=True, text=True)


def bad_cases(good):
    """Each case is one independent copy of the good file with one seeded error."""
    wrong_dates = good.copy()
    c = wrong_dates["site"] == "C"
    # Swap month and day, the way a guessing parser would read 05-01-2023.
    wrong_dates.loc[c, "date"] = pd.to_datetime(
        wrong_dates.loc[c, "date"]).dt.strftime("%Y-%d-%m")
    yield "site C dates read month-first", wrong_dates

    blank = good.copy()
    blank.loc[blank["sample_id"] == "A001", "score"] = None
    yield "blank score", blank

    text = good.copy().astype({"score": object})
    text.loc[text["sample_id"] == "A001", "score"] = "unknown"
    yield "nonnumeric score", text

    all_a = good.copy()
    all_a["site"] = "A"
    yield "every site label is A", all_a

    zero = good.copy()
    zero.loc[zero["sample_id"] == "A004", "score"] = 0
    yield "wrong imputation (0 instead of site median)", zero

    yield "dropped row", good.iloc[:-1].copy()

    changed = good.copy()
    changed.loc[changed["sample_id"] == "A001", "score"] = 99.0
    yield "observed score changed", changed

    filled = good.copy()
    filled.loc[filled["pH"].isna(), "pH"] = 7.0
    yield "missing pH invented", filled


def main():
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "project"
        shutil.copytree(PROJECT, work)
        run([str(CLEANER)], work)
        good = pd.read_csv(work / "data" / "master_dataset.csv")

        result = run([str(VALIDATOR)], work)
        passed = result.returncode == 0
        print(f"{'ok  ' if passed else 'BAD '} good file passes the validator")
        ok &= passed

        for name, frame in bad_cases(good):
            path = work / "data" / "candidate.csv"
            frame.to_csv(path, index=False)
            result = run([str(VALIDATOR), str(path)], work)
            rejected = result.returncode == 1
            print(f"{'ok  ' if rejected else 'BAD '} rejects: {name}")
            ok &= rejected
    print()
    print("All validator tests behaved as expected." if ok else "Some validator tests failed.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
