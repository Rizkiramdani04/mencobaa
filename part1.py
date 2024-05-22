import yfinance as yf
import streamlit as st

st.write("""
## Simple Stock Price App
 
Shown are the stock and closing

"""
)
ticker='GOOGL'
#memasukan data
ticker=yf.Ticker(ticker)
#memasukan histori
tickerdf=ticker.history(period='1d',start='2010-5-31',end='2021-5-31')

st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)