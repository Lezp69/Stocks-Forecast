# Stock Price Prediction and Visualization App

This Streamlit web application allows users to visualize historical stock prices, combine them for comparison, and predict future prices using the Prophet forecasting model.

## Features

- **Historical Data Visualization**: View historical stock prices for selected tickers.
- **Combination of Stock Prices**: Compare historical closing prices of multiple stocks.
- **Prophet Forecasting**: Utilizes the Prophet library to forecast future stock prices for selected tickers.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- yfinance
- prophet
- yahoo_fin

Install the required dependencies using the following command:

```bash
pip install pandas numpy matplotlib seaborn streamlit yfinance prophet yahoo_fin
```
## Usage
1. Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/stock-price-prediction-app.git
```
2. Navigate to the project directory:
```bash
cd stock-price-prediction-app
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```
4. Select the stocks you want to visualize and predict, along with the date range.
5. Click the "Make Changes" button to update the visualization and prediction based on your selections.
