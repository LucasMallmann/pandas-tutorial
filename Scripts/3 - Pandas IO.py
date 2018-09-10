import quandl
import pandas as pd

##quandl.get("FMAC/HPI_AK", authtoken="yQaxzc5rcgC8Hyt8SSdz")
df = pd.read_csv('ZILL-Z77006_3B.csv')

#print(df.head())
df.set_index('Date', inplace=True)

df.columns = ['ThreeBed_HPIS']
print(df.head())

df.to_csv('newcsv2.csv')
