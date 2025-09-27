"""
Line Chart using real-world time series (seaborn 'flights' dataset).
Interprets monthly passengers as 'sales' to demonstrate time trends.

Falls back to synthetic monthly sales if dataset download is unavailable.

Usage:
    python line_flights_sales.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    try:
        import seaborn as sns
        df = sns.load_dataset("flights")  # columns: year, month, passengers
        # Build a proper datetime index
        # Map month names to numbers if needed
        month_map = {m:i for i, m in enumerate(
            ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], start=1)}
        if df["month"].dtype == object:
            df["month_num"] = df["month"].map(lambda m: month_map.get(str(m)[:3].title(), 1))
        else:
            df["month_num"] = df["month"]
        dates = pd.to_datetime(dict(year=df["year"], month=df["month_num"], day=1))
        ts = pd.Series(df["passengers"].to_numpy(), index=dates).sort_index()
        title = "Monthly 'Sales' Trend (flight passengers proxy)"
        ylabel = "Sales (units)"
        return ts, title, ylabel
    except Exception:
        # Synthetic fallback: 3 years of monthly data with seasonality + noise
        rng = np.random.default_rng(42)
        periods = 36
        dates = pd.date_range("2022-01-01", periods=periods, freq="MS")
        base = np.linspace(200, 500, periods)
        season = 80 * np.sin(np.linspace(0, 6*np.pi, periods))
        noise = rng.normal(0, 30, periods)
        values = base + season + noise
        ts = pd.Series(values, index=dates)
        title = "Monthly Sales Trend (synthetic fallback)"
        ylabel = "Sales (units)"
        return ts, title, ylabel

def main():
    ts, title, ylabel = load_data()
    plt.figure(figsize=(10, 6))
    plt.plot(ts.index, ts.values, marker="o")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
