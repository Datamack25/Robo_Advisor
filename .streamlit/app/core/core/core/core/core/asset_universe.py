import pandas as pd

# Exemples d'actifs avec ESG score et secteur
ASSETS = pd.DataFrame({
    "Ticker": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
    "ESG": [85, 88, 82, 75, 70],
    "Sector": ["Tech", "Tech", "Tech", "Tech", "Auto"]
}).set_index("Ticker")
