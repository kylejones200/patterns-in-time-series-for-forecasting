#!/usr/bin/env python3
"""Forecast patterns (beehive demo) — Polars + DuckDB rewrite."""

import logging
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import polars as pl
from core import add_forecasts, plot_forecasts

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
OUTPUT_DIR = Path(__file__).parent.parent / "images"
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    rng = np.random.default_rng(42)
    n = 48
    start = datetime(2024, 1, 1)
    dates = [start + timedelta(hours=i) for i in range(n)]
    df = pl.DataFrame(
        {
            "time": dates,
            "temperature": rng.normal(35, 2, n).tolist(),
            "weight": (50 + np.cumsum(rng.normal(0.2, 0.1, n))).tolist(),
            "bee_traffic": (np.sin(np.linspace(0, 3 * np.pi, n)) * 50 + 200).tolist(),
        }
    )
    result = add_forecasts(df, date_col="time", value_col="weight", sma_window=6)
    logging.info(f"Rows with forecasts: {result.height}")
    logging.info(f"Naive non-null: {result['naive_forecast'].drop_nulls().len()}")
    logging.info(f"SMA non-null:   {result['sma_forecast'].drop_nulls().len()}")
    plot_forecasts(
        result,
        date_col="time",
        value_col="weight",
        title="Forecasting Hive Weight",
        output_path=OUTPUT_DIR / "beehive_forecast.png",
        sma_window=6,
    )
    logging.info(f"Done. Figures saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
