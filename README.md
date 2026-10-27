# London Crime Explorer

### Interactive Crime Analytics Dashboard | Python • Streamlit • Plotly • GeoPandas

An interactive data analytics dashboard exploring patterns in recorded crime across London boroughs between July 2024 and June 2025.

Developed as an extension of my MSc Statistics for AI & Data Science coursework, this project transforms crime and population datasets into interactive visualisations to support exploratory analysis and geographic comparisons.

## Project Overview

The London Crime Explorer enables users to investigate recorded crime patterns through an interactive web application.

The project combines data processing, statistical analysis and geospatial visualisation to make complex datasets easier to explore and interpret.

## Key Features

- **Borough-level analysis:** Explore recorded crime across London boroughs.
- **Interactive filtering:** Select individual boroughs to investigate local crime patterns.
- **Monthly crime trends:** Visualise how recorded crime changes over time.
- **Crime category analysis:** Compare the distribution of different crime types.
- **Population-adjusted rates:** Explore recorded crime rates using 2021 Census population data.
- **Geospatial visualisation:** Examine geographic patterns at Lower Layer Super Output Area (LSOA) level when geographical data is available.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and application development |
| Pandas | Data cleaning, aggregation and analysis |
| Streamlit | Interactive dashboard interface |
| Plotly | Interactive data visualisations |
| GeoPandas | Geospatial data processing |
| Git & GitHub | Version control and project management |

## Data Sources

The analysis uses:

- Modified police-recorded street-crime data covering July 2024–June 2025.
- 2021 Census population data.
- LSOA geographical boundaries for optional mapping.

The original datasets were supplied for academic coursework.

**Note:** Source datasets and generated data files are not included in this repository.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/mishamxlik/london-crime-explorer.git
cd london-crime-explorer
```

### 2. Install dependencies

Python 3.10+ is recommended.

```bash
pip install -r requirements.txt
```

### 3. Prepare the data

Place the required source files in the `source_data/` directory:

- `cw1-street-outcome.csv`
- `LSOA_data.csv`

Then run:

```bash
python prepare_data.py
```

The preparation script generates the aggregated datasets required by the dashboard.

### 4. Launch the dashboard

```bash
streamlit run app.py
```

The application will open in your browser.

### Optional: Enable Geographical Mapping

Place `LSOA_England_geom.gpkg` in the `source_data/` directory to enable the geographical map.

## Analytical Considerations

- Crime rates use resident population as the denominator and should not be interpreted as individual risk estimates.
- Recorded crime may be affected by reporting practices and differences in police recording.
- Dataset modifications and geographical coverage may influence the analysis.
- Comparisons should be interpreted within the limitations of the available data.

## Project Status

**Current:** Functional local Streamlit dashboard with interactive crime