def backtest_portfolio(prices, weights):
    """
    Backtest simple : cumulative returns
    """
    returns = prices.pct_change().dropna()
    port_returns = (returns @ weights)
    cum_returns = (1 + port_returns).cumprod()
    return cum_returns

