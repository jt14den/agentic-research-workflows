import pandas as pd

SITES = {
    "A": {
        "file": "data/site_A.csv",
        "rename": {"SiteID": "sample_id", "Collection_Date": "date",
                   "WaterQualityScore": "score", "pH": "pH", "Temperature_C": "temp_c"},
        "date_format": "%Y/%m/%d",
    },
    "B": {
        "file": "data/site_B.csv",
        "rename": {"id": "sample_id", "date": "date",
                   "score": "score", "ph": "pH", "temp": "temp_c"},
        "date_format": "%b %d %Y",
    },
    "C": {
        "file": "data/site_C.csv",
        "rename": {"StationID": "sample_id", "DateTime": "date",
                   "Quality_Index": "score", "pH_Level": "pH", "Water_Temp": "temp_c"},
        "date_format": "%d-%m-%Y",
    },
}
CANONICAL = ["site", "sample_id", "date", "score", "pH", "temp_c"]


def clean_site(site, cfg):
    df = pd.read_csv(cfg["file"]).rename(columns=cfg["rename"])
    df["site"] = site
    df["date"] = pd.to_datetime(df["date"], format=cfg["date_format"]).dt.strftime("%Y-%m-%d")
    df["score"] = df["score"].fillna(df["score"].median())
    return df[CANONICAL]


def main():
    merged = pd.concat([clean_site(s, cfg) for s, cfg in SITES.items()], ignore_index=True)
    merged.to_csv("data/master_dataset.csv", index=False)
    print(f"Wrote data/master_dataset.csv with {len(merged)} rows.")


if __name__ == "__main__":
    main()
