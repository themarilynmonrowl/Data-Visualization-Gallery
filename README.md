# Data Visualization Gallery

A small gallery of Python scripts demonstrating common charts using **real-world sample datasets** where possible, with **synthetic fallbacks** to ensure the scripts always run (even offline). Plots are rendered with **matplotlib** only.

## How to Use

```bash
# (Recommended) create a virtual environment
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run any script
python scatter_penguins.py
python bar_airlines.py
python line_flights_sales.py
```

## Scripts

### 1) `scatter_penguins.py` — Scatter plot (Age vs Height analogue)
- **Primary data source:** `seaborn.load_dataset("penguins")` → plots **Flipper Length vs Body Mass** (biologically realistic correlation).
- **Fallback:** Generates synthetic age vs. height style data if the dataset can't be downloaded.
- **Chart type:** Scatter.

### 2) `bar_airlines.py` — Bar chart (Flights per Airline)
- **Primary data source:** Plotly Express sample **airline flights** dataset (loaded via `plotly.express.data`), counting flights per airline. If an airport column is present (e.g., `origin`), the script picks the most common airport and shows flights **at that airport**.
- **Fallback:** Randomized flight counts for 5 sample airlines.
- **Chart type:** Vertical bar.

### 3) `line_flights_sales.py` — Line chart (Sales Trend)
- **Primary data source:** `seaborn.load_dataset("flights")` (monthly passengers over years), used as a **proxy for sales** to illustrate seasonal trends and growth.
- **Fallback:** Synthetic monthly sales with trend + seasonality + noise.
- **Chart type:** Line.

## Reproducibility & Offline Use

- When online, scripts pull small **public sample datasets** from `seaborn` or `plotly.express`.  
- If the download fails (e.g., offline, proxy restrictions), the scripts **automatically switch** to internally generated synthetic data.
- All plots are produced with **matplotlib** for broad compatibility.

## Requirements

See `requirements.txt`. Only common, well-supported libraries:
- `matplotlib`, `pandas`, `numpy` for plotting and data handling
- `seaborn` and `plotly` are used **only** to fetch public sample datasets
