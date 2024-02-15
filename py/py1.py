import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import yfinance as yf
import datetime as dt
import json as js

from prophet import Prophet
from yahoo_fin.stock_info import get_analysts_info, get_balance_sheet, get_cash_flow, get_data, get_day_gainers, get_day_losers, get_day_most_active, get_futures

# Here begins the code

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: white;'>MY STOCKS <br> RESUME AND PRICE PREDICTION</h1>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    selected_tickers = st.multiselect(
        'Which Stocks do you want to see?',
        ['MSFT', 'AAPL', 'GOOGL', 'BLK']
    )

    try:
        start_date, end_date = st.date_input(
            "Select your vacation for next year",
            (dt.date.today() - dt.timedelta(days=5 * 365), dt.date.today()),
            (dt.date.today() - dt.timedelta(days=5 * 365)),
            dt.date.today(),
            format="YYYY.MM.DD",
        )
    except ValueError:
        st.error("Please select both start and end dates.")

    button_clicked = st.button('Make Changes')

if button_clicked:
    if selected_tickers:
        # Fetch historical data for selected tickers
        historical_data = {}
        for ticker_symbol in selected_tickers:
            ticker = yf.Ticker(ticker_symbol)
            historical_data[ticker_symbol] = ticker.history(period='1d', start=start_date, end=end_date)

        # Creating a DataFrame
        df = pd.concat(historical_data.values(), keys=historical_data.keys(), axis=1)

        print(historical_data)

        # Creating a DataFrame
        df = pd.concat(historical_data.values(), keys=historical_data.keys(), axis=1)

        print(df.tail())
        print(df.columns)

        # Create a copy of the original DataFrame
        filtered_columns = [(company, attribute) for company, attribute in df.columns if 'Dividends' not in attribute and 'Stock Splits' not in attribute]
        new_df = df[filtered_columns].copy()

        # Modify column names in the new DataFrame
        new_columns = [f"{company}_{attribute}" for company, attribute in new_df.columns]
        new_df.columns = new_columns

        # Plotting the data
        st.write("## Data")
        st.dataframe(new_df)

        # Display area chart for combined Close price data
        combined_close_data = pd.DataFrame()
        for ticker_symbol in selected_tickers:
            combined_close_data[ticker_symbol] = df.loc[:, ticker_symbol]['Close']

        st.write("## Combined Historic Close Data")
        st.area_chart(combined_close_data)

        # Start forecasting with Prophet
        for ticker_symbol in selected_tickers:
            # Preparing the data for Prophet
            df_prophet = df.loc[:, ticker_symbol][['Open', 'High', 'Low', 'Close', 'Volume']].reset_index()
            df_prophet.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
            df_prophet['ds'] = df_prophet['ds'].dt.tz_localize(None)

            # Creating the Prophet model
            model = Prophet()
            model.fit(df_prophet)

            # Making the forecast
            future = model.make_future_dataframe(periods=365)
            forecast = model.predict(future)

            # Plotting the forecast
            st.write(f'## 1 YEAR FORECAST FOR {ticker_symbol}')
            fig = model.plot(forecast)
            plt.xlabel('Date')
            plt.ylabel('Close Price')
            st.pyplot(fig)
    else:
        st.error("PLEASE SELECT A STOCK")