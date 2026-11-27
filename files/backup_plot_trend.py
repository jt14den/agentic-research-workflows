"""
backup_plot_trend.py - instructor fallback for the capstone analysis step.
Plots water quality score over time, one line per site, to fig/score_trend.png.

Run from inside the coastal-water-quality folder, after creating the merged file:
    python plot_trend.py
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # no display needed
import matplotlib.pyplot as plt

df = pd.read_csv("data/master_dataset.csv", parse_dates=["date"])
os.makedirs("fig", exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 5))
for site, sub in df.sort_values("date").groupby("site"):
    ax.plot(sub["date"], sub["score"], marker="o", label=f"Site {site}")

ax.set_xlabel("Date")
ax.set_ylabel("Water quality score")
ax.set_title("Water quality score over time by site")
ax.legend()
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig("fig/score_trend.png", dpi=120)
print("Wrote fig/score_trend.png")
# Sanity check the date trap: every site should span January to mid-May.
print(df.groupby("site")["date"].agg(["min", "max"]))
