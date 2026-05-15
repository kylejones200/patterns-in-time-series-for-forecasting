# Description: Short example for Patterns in Time Series for Forecasting.


# Simulated beehive data

import numpy as np
import pandas as pd


def main():
    date_range = pd.date_range(start="2024-01-01", periods=48, freq="H")
    data = {
        "temperature": np.random.normal(35, 2, len(date_range)),
        "weight": 50 + np.cumsum(np.random.normal(0.2, 0.1, len(date_range))),
        "bee_traffic": np.sin(np.linspace(0, 3 * np.pi, len(date_range))) * 50 + 200,
    }
    df = pd.DataFrame(data, index=date_range)
    df.index.name = "time"
    df.head()

    # Naive Forecast
    df["naive_weight"] = df["weight"].shift(1)
    # Moving Average Forecast
    df["sma_weight"] = df["weight"].rolling(window=6).mean()
    # Plotting forecasts
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["weight"], label="Actual Weight", color="brown")
    plt.plot(df.index, df["naive_weight"], label="Naive Forecast", linestyle="-")
    plt.plot(
        df.index, df["sma_weight"], label="6-Hour SMA Forecast", linestyle="--", color="red"
    )
    plt.title("Forecasting Hive Weight")
    plt.xlabel("Time")
    plt.ylabel("Hive Weight (kg)")
    plt.legend()
    plt.savefig("beehive_forecast.png")
    plt.show()


if __name__ == "__main__":
    main()
