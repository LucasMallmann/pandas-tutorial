import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

df = pd.read_csv('newcsv2.csv')


df.rename(columns={'ThreeBed_HPIS': 'Value'}, inplace=True)

df['Date'] = pd.to_datetime(df.Date)
df.sort_values(by='Date', inplace=True)

df.set_index('Date', inplace=True)
# df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0

print(df.head())
df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
df.plot()

plt.grid(True)
plt.show()
