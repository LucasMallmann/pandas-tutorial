import pandas as pd
import quandl

quandl.get("FMAC/HPI_AK", authtoken="yQaxzc5rcgC8Hyt8SSdz")
# print(df.head())
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(fiddy_states[0])
for abbv in fiddy_states[0][0][1:]:
    print("FMAC/HPI_" + str(abbv))
