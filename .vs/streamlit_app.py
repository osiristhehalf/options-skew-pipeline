# streamlit_app.py
import streamlit as st
import pandas as pd
from signal_engine import get_skew_signals, tickers

st.title("Options Skew Signal Dashboard")

threshold_skew = st.slider("Minimum Vol Skew", 0.0, 0.5, 0.1)
threshold_convexity = st.slider("Minimum Convexity", 0.0, 1.0, 0.3)

results = []
for ticker in tickers:
    signal = get_skew_signals(ticker)
    if signal and signal['vol_skew'] > threshold_skew and signal['convexity'] > threshold_convexity:
        results.append({'Ticker': ticker, **signal})

df = pd.DataFrame(results)
st.dataframe(df)

if st.button("Export to CSV"):
    df.to_csv("skew_signals.csv", index=False)
    st.success("Exported skew_signals.csv")
    