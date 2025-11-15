import pandas as pd
import numpy as np
from scipy.optimize import minimize

def optimize_markowitz(prices, target_vol=None, max_weight=0.4):
    """
    Optimisation Markowitz pour un portefeuille.
    prices : pd.DataFrame avec les prix historiques
    target_vol : volatilité cible optionnelle
    max_weight : poids max par actif
    """
    returns = prices.pct_change().dropna()
    mean_ret = returns.mean() * 252
    cov = returns.cov() * 252
    n = len(returns.columns)

    def port_vol(w):
        return np.sqrt(np.dot(w.T, np.dot(cov, w)))

    def neg_sharpe(w):
        vol = port_vol(w)
        return - (w @ mean_ret) / vol if vol > 0 else 1e6

    w0 = np.ones(n) / n
    bounds = [(0, max_weight)] * n
    constraints = [{"type": "eq", "fun": lambda w: w.sum() - 1}]

    if target_vol:
        constraints.append({"type": "eq", "fun": lambda w: port_vol(w) - target_vol})

    res = minimize(neg_sharpe, w0, method="SLSQP", bounds=bounds, constraints=constraints)

    if res.success:
        return pd.Series(res.x, index=returns.columns)
    else:
        return pd.Series(np.zeros(n), index=returns.columns)
