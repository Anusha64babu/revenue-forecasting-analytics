import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Revenue Forecasting Dashboard", layout="wide")

st.title("📊 Revenue Forecasting & Financial Performance Analytics")

# Load data
historical = pd.read_csv("data/revenue_data.csv", parse_dates=["date"])
forecast = pd.read_csv("data/forecast.csv", parse_dates=["ds"])

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Months", len(historical))
col2.metric("Avg Monthly Revenue", f"${historical.revenue.mean():,.0f}")
col3.metric("Latest Revenue", f"${historical.revenue.iloc[-1]:,.0f}")

st.subheader("📈 Historical Revenue Trend")
fig, ax = plt.subplots()
ax.plot(historical.date, historical.revenue)
ax.set_xlabel("Date")
ax.set_ylabel("Revenue")
st.pyplot(fig)

st.subheader("🔮 Revenue Forecast (Next 12 Months)")
fig2, ax2 = plt.subplots()
ax2.plot(historical.date, historical.revenue, label="Actual")
ax2.plot(forecast.ds, forecast.yhat, label="Forecast", linestyle="--")
ax2.legend()
st.pyplot(fig2)

st.subheader("📋 Forecast Table")
st.dataframe(forecast.tail(12))
