# app/main.py
import streamlit as st
import pandas as pd
from core.asset_universe import tickers
from core.data_loader import load_prices
from core.optimizer import optimize_markowitz
from core.performance import compute_performance
from core.risk_profiles import map_profile_to_risk
from utils.plot_utils import plot_cumulative_returns

st.set_page_config(page_title="🤖 RoboAdvisor IA", layout="wide")
st.title("🤖 RoboAdvisor Intelligent – Allocation Optimisée")

# --- INPUTS UTILISATEUR ---
budget = st.number_input("Budget (€)", min_value=1000, value=50000, step=1000)
risk_profile = st.selectbox("Niveau de risque", ["Conservateur", "Modéré", "Agressif"])
selected_tickers = st.multiselect("Sélectionnez les actifs", tickers, default=["AAPL", "MSFT", "GOOGL"])

if len(selected_tickers) == 0:
    st.warning("Veuillez sélectionner au moins un actif")
    st.stop()

# --- CHARGEMENT DES DONNÉES ---
with st.spinner("Téléchargement des données..."):
    prices = load_prices(selected_tickers)

# --- RISQUE CIBLE ---
risk_target = map_profile_to_risk(risk_profile)

# --- OPTIMISATION ---
with st.spinner("Optimisation Markowitz…"):
    weights = optimize_markowitz(prices, target_vol=risk_target)

st.subheader("Allocation du portefeuille")
st.dataframe(weights)

# --- PERFORMANCE ---
perf = compute_performance(prices, weights)
st.metric("Rendement annualisé", f"{perf['ann_return']:.2%}")
st.metric("Volatilité", f"{perf['ann_vol']:.2%}")
st.metric("Sharpe", f"{perf['sharpe']:.2f}")

# --- GRAPHIQUE DE LA PERFORMANCE ---
fig = plot_cumulative_returns(prices, weights)
st.plotly_chart(fig, use_container_width=True)
