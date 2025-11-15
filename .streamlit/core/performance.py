# core/performance.py
import pandas as pd
import numpy as np

def compute_performance(prices, weights, risk_free=0.02):
    returns = prices.pct_change().dropna()
    port_ret = (returns * weights).sum(axis=1)
    cum = (1 + port_ret).cumprod()

    ann_return = cum.iloc[-1] ** (252 / len(port_ret)) - 1
    ann_vol = port_ret.std() * np.sqrt(252)
    sharpe = (ann_return - risk_free) / ann_vol if ann_vol > 0 else 0

    return {
        "ann_return": ann_return,
        "ann_vol": ann_vol,
        "sharpe": sharpe,
        "cum_curve": cum
    }

