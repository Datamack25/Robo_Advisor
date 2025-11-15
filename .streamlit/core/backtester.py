# core/backtester.py
import pandas as pd

def backtest(prices, weights, initial_capital=10000):
    returns = prices.pct_change().dropna()
    port_ret = (returns * weights).sum(axis=1)
    cum_value = (1 + port_ret).cumprod() * initial_capital
    return cum_value

