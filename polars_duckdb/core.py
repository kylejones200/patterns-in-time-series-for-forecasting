"""Time series forecast patterns using Polars and DuckDB."""

import duckdb
import polars as pl
import matplotlib.pyplot as plt
from pathlib import Path


def add_forecasts(
    df: pl.DataFrame,
    date_col: str,
    value_col: str,
    sma_window: int = 6,
) -> pl.DataFrame:
    """Add naive (LAG) and SMA forecasts via DuckDB window functions."""
    return duckdb.sql(f"""
        SELECT
            *,
            LAG("{value_col}", 1) OVER (ORDER BY "{date_col}")
                AS naive_forecast,
            AVG("{value_col}") OVER (
                ORDER BY "{date_col}"
                ROWS BETWEEN {sma_window - 1} PRECEDING AND CURRENT ROW
            ) AS sma_forecast
        FROM df
        ORDER BY "{date_col}"
    """).pl()


def plot_forecasts(
    df: pl.DataFrame,
    date_col: str,
    value_col: str,
    title: str,
    output_path: Path,
    sma_window: int = 6,
):
    dates  = df[date_col].to_list()
    actual = df[value_col].to_list()
    naive  = df["naive_forecast"].to_list()
    sma    = df["sma_forecast"].to_list()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, actual, label="Actual",                      color="brown",  linewidth=1.5)
    ax.plot(dates, naive,  label="Naive Forecast",              color="#4A90A4",linewidth=1.2)
    ax.plot(dates, sma,    label=f"{sma_window}-Period SMA",    color="red",    linewidth=1.2, linestyle="--")
    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel(value_col)
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches="tight")
    plt.close()
