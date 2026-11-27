"""
backup_clean_and_merge.py - instructor fallback for the coastal water quality data.

A correct, deliberately plain reference: explicit per-site handling so it is easy to
read and explain. Produces data/master_dataset.csv (60 rows) with the canonical schema.
Crucially, it parses site C dates as day-month-year, the trap the lesson is built around.

Run from inside the coastal-water-quality folder:  python clean_and_merge.py
"""
import pandas as pd

# Per-site config: how each raw file maps onto the canonical schema, and its date format.
SITES = {
    "A": {
        "file": "data/site_A.csv",
        "rename": {"SiteID": "sample_id", "Collection_Date": "date",
                   "WaterQualityScore": "score", "pH": "pH", "Temperature_C": "temp_c"},
        "date_format": "%Y/%m/%d",      # 2023/01/05
    },
    "B": {
        "file": "data/site_B.csv",
        "rename": {"id": "sample_id", "date": "date",
                   "score": "score", "ph": "pH", "temp": "temp_c"},
        "date_format": "%b %d %Y",      # Jan 5 2023
    },
    "C": {
        "file": "data/site_C.csv",
        "rename": {"StationID": "sample_id", "DateTime": "date",
                   "Quality_Index": "score", "pH_Level": "pH", "Water_Temp": "temp_c"},
        "date_format": "%d-%m-%Y",      # 05-01-2023 = 5 January (day-month-year!)
    },
}
CANONICAL = ["site", "sample_id", "date", "score", "pH", "temp_c"]


def clean_site(site, cfg):
    df = pd.read_csv(cfg["file"]).rename(columns=cfg["rename"])
    df["site"] = site
    # Parse dates with the site's known format, then store ISO. Explicit format = no guessing.
    df["date"] = pd.to_datetime(df["date"], format=cfg["date_format"]).dt.strftime("%Y-%m-%d")
    # Fill missing score with this site's median (spec rule). Leave pH/temp_c blank.
    df["score"] = df["score"].fillna(df["score"].median())
    return df[CANONICAL]


def main():
    merged = pd.concat([clean_site(s, cfg) for s, cfg in SITES.items()], ignore_index=True)
    merged.to_csv("data/master_dataset.csv", index=False)
    print(f"Wrote data/master_dataset.csv with {len(merged)} rows.")


if __name__ == "__main__":
    main()
