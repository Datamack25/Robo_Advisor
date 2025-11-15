# core/optimizer.py
import pandas as pd
import numpy as np
from scipy.optimize import minimize

def optimize_markowitz(prices, target_vol=None):
    returns = prices.pct_change().dropna()
    mean_ret = returns.mean() * 252
    cov = returns.cov() * 252
    n = len(returns.columns)

    def vol(w):
        return np.sqrt(w.T @ cov @ w)

    def neg_sharpe(w):
        return -(w @ mean_ret) / vol(w)

    w0 = np.ones(n) / n
    bounds = [(0, 0.4)] * n
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1}]

    if target_vol:
        cons.append({"type": "eq", "fun": lambda w: vol(w) - target_vol})

    res = minimize(neg_sharpe, w0, method="SLSQP", bounds=bounds, constraints=cons)
    return pd.Series(res.x, index=returns.columns)
