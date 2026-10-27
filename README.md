# London Crime Explorer

An interactive Streamlit dashboard extending an MSc Statistics for AI & Data Science coursework analysis.

## Run locally

1. Install Python 3.10+.
2. Run `pip install -r requirements.txt`.
3. Run `streamlit run app.py`.

The included `data/` directory contains aggregated data ready for the dashboard, so the original 172 MB crime file is **not** required to run the basic charts.

## Optional geographical map

Place `LSOA_England_geom.gpkg` in `source_data/` to enable the borough-level LSOA map. The GeoPackage is not included in the download to keep it small.

## Rebuild the aggregates

Place `cw1-street-outcome.csv` and `LSOA_data.csv` in `source_data/` and run `python prepare_data.py`.

## Notes

- The crime dataset covers July 2024–June 2025; population figures are from the 2021 Census.
- Crime rates use resident population as denominator and are **not** risk estimates for individual residents.
- Dataset modifications, reporting bias and geographic data coverage may affect interpretation.
- This project currently runs locally; **AWS integration and public deployment have not yet been completed**.
