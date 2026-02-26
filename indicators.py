import pandas as pd
import numpy as np


def calculate_rsi(data, window=14):
    delta = data['Close'].diff()  # Calculate the difference between consecutive closing prices
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()  # Calculate average gains
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()  # Calculate average losses
    rs = gain / loss  # Calculate relative strength
    rsi = 100 - (100 / (1 + rs))  # Calculate RSI
    return rsi


def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    exp1 = data['Close'].ewm(span=short_window, adjust=False).mean()  # Short-term EMA
    exp2 = data['Close'].ewm(span=long_window, adjust=False).mean()  # Long-term EMA
    macd = exp1 - exp2  # Calculate MACD
    signal = macd.ewm(span=signal_window, adjust=False).mean()  # Signal line
    return macd, signal


def calculate_bollinger_bands(data, window=20, num_sd=2):
    rolling_mean = data['Close'].rolling(window=window).mean()  # Moving average
    rolling_std = data['Close'].rolling(window=window).std()  # Standard deviation
    upper_band = rolling_mean + (rolling_std * num_sd)  # Upper Bollinger Band
    lower_band = rolling_mean - (rolling_std * num_sd)  # Lower Bollinger Band
    return upper_band, lower_band


def calculate_moving_average(data, window=14):
    return data['Close'].rolling(window=window).mean()  # Simple Moving Average