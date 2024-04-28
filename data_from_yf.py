#pip install yfinance
import yfinance as yf

# Get the data
data = yf.download(tickers="TCS", period="500d", interval="1D")  #for day intervel
#data = yf.download(tickers="MSFT", period="5d", interval="1m")    #1 minute interval
print(data.head(5))
data.columns
#data.to_csv("data_from_yf.csv")