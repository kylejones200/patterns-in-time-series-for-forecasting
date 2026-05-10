# Patterns in Time Series for Forecasting Time series data is a sequence of numbers where the order of the
sequence matters. Each number in the sequence carries context based on...

### Patterns in Time Series for Forecasting
Time series data is a sequence of numbers where the order of the sequence matters. Each number in the sequence carries context based on what came before it and, potentially, what might follow.

There is information encoded within the structure of the sequence that we decode it to make better predictions.


<figcaption>Photo by <a class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Jez Timms</a> on <a class="markup--anchor markup--figure-anchor"


#### Recognizing Patterns in Sequences
Let's begin with a simple example. Consider the following sequence:

1, 1, 2, 2, 1, 1, 2, ?

What comes next? If you were to identify a repeating pattern, you might reasonably conclude that the next value will be 2. That conclusion relies on recognizing the symmetry of the numbers and their repetitive nature. Importantly, we also know what the next number won't be --- something completely unexpected, like a billion. This is an inherent part of forecasting: we leverage patterns and previous observations to rule out unlikely scenarios.

While the human brain is naturally good at recognizing such patterns, the challenge becomes more significant when sequences are long, noisy, or lack obvious structure. This is where systematic methods, like statistical models and machine learning algorithms, come into play.

#### Basic Forecasting Techniques
At its core, time series forecasting is about using what we know to predict what comes next. Let's explore some foundational approaches, starting with the most straightforward method:

**The Naive Forecast**

The naive approach assumes that the most recent value in the time series will persist. For instance, in the previous sequence, the last observed value was 2, so we would forecast the next value as 2. This method serves as a baseline or benchmark --- simple but surprisingly effective for short-term predictions in stable systems.

For example:

- If yesterday's temperature in Houston was 85°F, the naive forecast for today would be 85°F.
- If the stock price of a company closed at \$100 yesterday, we predict the price will close at \$100 today.

While naive forecasts are (never) perfect but they are a useful starting point. In many real-world systems, short-term values don't deviate drastically from the most recent observations --- if the temperature was 85°F yesterday, it is unlikely to be 1,000,000°F today (though it may feel like that in Houston).

#### Using the Mean: A Step Toward Statistical Modeling
Another straightforward method is to assume that the next value will be the mean of all previous values in the sequence. Mathematically, this method calculates the average and projects it forward. However, this approach introduces a key assumption: that the series will "revert to the mean" over time.

Let's examine why this is problematic with a concrete example: the weather in Houston, Texas.

The Weather in Houston

If we were to plot the average monthly temperatures for a year, we would see a clear seasonal pattern --- a bell curve. Summers are hot, winters are cooler, and the temperatures transition smoothly over the months.


Now, what if we applied the naive forecast method and assumed that the temperature next month will be the same as this month? We would be wrong, but likely by only a small margin because temperatures don't change dramatically within a month. This is shown in the mean+1 (green line) of the graph below.


<figcaption>Average temp in Houston</figcaption>


On the other hand, if we used the mean of the entire year to predict next month's temperature, we would be more wrong. Why? Because we've ignored the structure of the seasonal pattern. Houston's winter months will have temperatures far below the annual average, and summer months will be far above it. The overall mean is the purple line on the graph (about 70 degrees).

This reveals a insight: patterns matter, and not all values in a time series are *equal*. Simply averaging across all observations fails to capture important differences within the data. The blue dots represent the spread of average temperatures between 2000 and 2014.


#### Incorporating Seasonality and Structure
So how do we account for differences across time? A more informed approach would be to recognize patterns embedded within the data and forecast based on those. For example, if we wanted to predict next January's temperature, we wouldn't use the annual average. Instead, we would consider the average of previous Januaries.

This is a simple but powerful improvement to the naive method. It introduces the concept of seasonality: the idea that certain values in a time series repeat in predictable cycles. By segmenting the data into smaller, meaningful groups --- like months or quarters --- we can capture these seasonal effects and make better predictions.

For example, to forecast next February's temperature, we should look at the average of past Februaries --- not the temperature from yesterday. To predict next year's sales in Q1, we should look at the historical Q1 sales from previous years.

This approach still relies on averages, but it does so intelligently, respecting the natural differences that occur over time (seasonality). It's a step closer to uncovering the underlying structure of the time series.

#### The Goal of Time Series Analysis
Ultimately, our reason for using time series is to forecast values that we haven't seen yet/don't yet know. Whether it's detecting seasonality, identifying trends, or quantifying the impact of external factors, these tools allow us to move beyond simple heuristics and make precise, data-driven forecasts.

While humans can intuitively recognize small-scale patterns, real-world time series data --- such as financial markets, climate trends, or sensor readings --- are more complex and voluminous than humans can keep in their heads. To manage this complexity, we need systematic approaches that can:

1\. Recognize patterns automatically (e.g., cycles, trends, and outliers).

2\. Differentiate meaningful patterns from noise.

3\. Scale predictions to larger datasets without relying on manual inspection.

In the weather example, we understand that seasons drive temperature changes. But what if we were analyzing power demand, stock prices, or traffic patterns? The challenge is to identify the hidden relationships, extract meaningful patterns, and apply them to future predictions.

#### Next Steps
Time series data has information encoded in the order of the values, which means that recognizing patterns with the order of numbers is useful for making accurate predictions.

The naive forecast and mean-based approaches provide simple benchmarks but fail to account for important structure, like seasonality.

Incorporating known patterns --- such as monthly trends in weather --- improves forecast accuracy. The ultimate goal of time series analysis is to develop tools that scale, automate pattern recognition, and help us make data-driven forecasts.

These techniques are simple to use and understand. They form the foundation for more advanced time series forecasting methods.

#### Beehive Example
You want to predict tomorrow's weight of the hive. You decide to use a Naive Forecast where you assume tomorrow's weight equals today's weight and you calculate a Simple Moving Average to smooth out short-term noise.



#### Related Posts
This article is part of a series of posts on time series forecasting. Here is the list of articles in the order they were designed to be read.

1.  [[Time Series for Business Analytics with Python](https://medium.com/@kylejones_47003/time-series-for-business-analytics-with-python-a92b30eecf62?source=your_stories_page-------------------------------------)]
2.  [[Time Series Visualization for Business Analysis with Python](https://medium.com/@kylejones_47003/time-series-visualization-for-business-analysis-with-python-5df695543d4a?source=your_stories_page-------------------------------------)]
3.  [[Patterns in Time Series for Forecasting](https://medium.com/@kylejones_47003/patterns-in-time-series-for-forecasting-8a0d3ad3b7f5?source=your_stories_page-------------------------------------)]
4.  [[Imputing Missing Values in Time Series Data for Business Analytics with Python](https://medium.com/@kylejones_47003/imputing-missing-values-in-time-series-data-for-business-analytics-with-python-b30a1ef6aaa6?source=your_stories_page-------------------------------------)]
5.  [[Measuring Error in Time Series Forecasting with Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd?source=your_stories_page-------------------------------------)]
6.  [[Univariate and Multivariate Time Series Analysis with Python](https://medium.com/@kylejones_47003/univariate-and-multivariate-time-series-analysis-with-python-b22c6ec8f133?source=your_stories_page-------------------------------------)]
7.  [[Feature Engineering for Time Series Forecasting in Python](https://medium.com/@kylejones_47003/feature-engineering-for-time-series-forecasting-in-python-7c469f69e260?source=your_stories_page-------------------------------------)]
8.  [[Anomaly Detection in Time Series Data with Python](https://medium.com/@kylejones_47003/anomaly-detection-in-time-series-data-with-python-5a15089636db?source=your_stories_page-------------------------------------)]
9.  [[Dickey-Fuller Test for Stationarity in Time Series with Python](https://medium.com/@kylejones_47003/dickey-fuller-test-for-stationarity-in-time-series-with-python-4e4bf1953eed?source=your_stories_page-------------------------------------)]
10. [[Using Classification Model for Time Series Forecasting with Python](https://medium.com/@kylejones_47003/using-classification-model-for-time-series-forecasting-with-python-d74a1021a5c4?source=your_stories_page-------------------------------------)]
11. [[Measuring Error in Time Series Forecasting with Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd?source=your_stories_page-------------------------------------)]
12. [[Physics-informed anomaly detection in a wind turbine using Python with an autoencoder transformer](https://medium.com/@kylejones_47003/physics-informed-anomaly-detection-in-a-wind-turbine-using-python-with-an-autoencoder-transformer-06eb68aeb0e8?source=your_stories_page-------------------------------------)]
