import pandas as pd
import streamlit as st

st.write("""
# Welcome to my first streamlit app!

This is a simple app that demonstrates how to use Streamlit to create interactive web applications with Python. You can use this app to display data, create visualizations, and interact with your data in real-time.

# About this app

This app will be using Yahoo Finance API to get stock data and display it in a simple and interactive way. You can enter a stock ticker symbol, and the app will fetch the latest stock data for that symbol and display it in a table.

""")
# Select ticker symbol
ticker = st.text_input("Enter a stock ticker symbol (e.g. AAPL, MSFT, GOOGL):")

# Select date range

start_date = st.date_input("Start date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End date", "today")

