"""
date_review.py - a candidate date transformation for site C, for Episode 0.

This is deliberately faulty teaching code. It is not what every agent writes.
Read it, predict its output, then run it. It reads the raw file and prints
output. It does not change any data.

    python date_review.py
"""
import pandas as pd

raw = pd.read_csv("data/site_C.csv")
candidate = pd.DataFrame({
    "sample_id": raw["StationID"],
    "date": pd.to_datetime(raw["DateTime"], format="mixed").dt.strftime("%Y-%m-%d")
})
print("Rows:", len(candidate))
print(candidate.head(2).to_string(index=False))
