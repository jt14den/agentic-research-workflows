"""
backup_inspect_data.py - instructor fallback for the audit step.
Reports columns and missing-value counts for each raw site file.

Run from inside the coastal-water-quality folder:  python inspect_data.py
"""
import glob
import pandas as pd

for file in sorted(glob.glob("data/site_*.csv")):
    print(f"\n--- {file} ---")
    df = pd.read_csv(file)
    print("Columns:", list(df.columns))
    print("Rows:", len(df))
    print("Missing values per column:")
    print(df.isnull().sum())
