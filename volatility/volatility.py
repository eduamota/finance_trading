import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    
    tickers = prices.ticker.unique()

    variability = {}
    top = {}
    
    for ticker in tickers:
        
        df_ticker = prices[prices.ticker == ticker].copy()
        df_ticker['price_shift'] = df_ticker.price.shift()
        df_ticker.dropna(inplace=True)
        df_ticker['log_return'] = np.log(df_ticker.price_shift / df_ticker.price)
        std = df_ticker.log_return.std()
        var = (std*252)**0.5
        variability[ticker] = var
       
        if 'ticker' not in top:
            top['ticker'] = ticker
            top['variability'] = var
            
        if var > top['variability']:
            top['ticker'] = ticker
            top['variability'] = var
        
    return top['ticker']


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()