import yfinance as yf

def fetch_data(ticker: str, start_date=None, end_date=None):

    
    return yf.download(ticker, start_date, end_date)
