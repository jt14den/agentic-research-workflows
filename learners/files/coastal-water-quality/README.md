# Coastal Water Quality Monitoring

A multi-site water quality dataset from three monitoring stations along the Southern California coast, collected weekly from January to May 2023.

## Sites

| Site | Location | File |
|---|---|---|
| A | Malibu Creek outflow | `data/site_A.csv` |
| B | Santa Monica Bay nearshore | `data/site_B.csv` |
| C | Ballona Creek estuary | `data/site_C.csv` |

## Research goal

Combine the three site files into a single clean dataset suitable for trend analysis. Each site used different field collection software, resulting in inconsistent column naming, date formats, and some missing observations.

## Known issues

- Column names differ across sites (e.g. `SiteID` vs `id` vs `StationID`)
- Date formats differ across sites (e.g. `2023/01/05` vs `Jan 5 2023` vs `05-01-2023`)
- Water quality score column has different names (`WaterQualityScore`, `score`, `Quality_Index`)
- Some missing values in score, pH, and temperature columns

## Output target

A single merged file `data/master_dataset.csv` with standardized column names, consistent date formatting, and a documented strategy for handling missing values.
