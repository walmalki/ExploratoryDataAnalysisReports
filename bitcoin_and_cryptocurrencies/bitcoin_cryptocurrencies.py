import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('coinmarketcap_06122017.csv')
profile = ProfileReport(df, title='Bitcoin & Cryptocurrencies | Data Analysis')
profile.to_file('index.html')