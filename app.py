import os
from alpha_vantage.timeseries import TimeSeries

KEY = os.getenv('AV_KEY') 

ts = TimeSeries(key=KEY, output_format='pandas')

data = ts.get_monthly_adjusted('AAPL')

print(data) 
