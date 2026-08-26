import pandas as pd
import streamlit as st
import yfinance as yf


@st.cache_data
def download_stock_data(ticker, start_date, end_date):
    return yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False,
    )


st.title("Stock Data Dashboard")
st.write(
    "Enter a stock ticker and date range to view historical data from Yahoo Finance."
)

ticker = st.text_input(
    "Stock ticker",
    placeholder="AAPL",
).strip().upper()
start_date = st.date_input("Start date", value=pd.Timestamp("2020-01-01").date())
end_date = st.date_input("End date", value=pd.Timestamp.today().date())

if not ticker:
    st.info("Enter a stock ticker to begin.")
    st.stop()

if start_date >= end_date:
    st.error("The end date must be after the start date.")
    st.stop()

st.write(f"Fetching data for **{ticker}** from {start_date} to {end_date}...")

try:
    with st.spinner("Downloading stock data..."):
        data = download_stock_data(ticker, start_date, end_date)
except Exception as error:
    st.error(f"Unable to fetch data for {ticker}: {error}")
    st.stop()

if data.empty:
    st.warning("No data was found for that ticker and date range.")
    st.stop()

st.success(f"Data for {ticker} fetched successfully.")
st.line_chart(data["Close"])