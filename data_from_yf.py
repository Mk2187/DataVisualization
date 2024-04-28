#pip install yfinance
import yfinance as yf

# Get the data
data = yf.download(tickers="MSFT", period="500d", interval="1D")
print(data.head(5))
data.columns
data.to_csv("dta_from_yf.csv")