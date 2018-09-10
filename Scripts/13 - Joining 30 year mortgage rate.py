import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

# mortgage --> Taxa de juros sobre um empréstimo
# para comprar um pedaço de terra !!!
api_key = "yQaxzc5rcgC8Hyt8SSdz"

# get the mortgage for 30 years..function


def mortgage_30y():
    df = quandl.get('FMAC/MORTG', trim_start="1975-01-01", authtoken=api_key)
    # % CHANGE....
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    df.rename(columns={'Value': 'M30'}, inplace=True)
    df = df.resample('D').mean()
    df = df.resample('M').mean()
    return df


def get_hpi_data():
    df = pd.read_pickle('states_pct_change.pickle')
    return df


def HPI_benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df.rename(columns={'Value': str('United States')}, inplace=True)
    # % CHANGE... ((novo - velho)/velho) * 100.0
    df['United States'] = (df['United States'] - df['United States'][0]) / df['United States'][0] * 100.0

    return df

df_mortgage = mortgage_30y()
HPI_data = get_hpi_data()
HPI_bench = HPI_benchmark()

# Juntar HPI com m29y
states_HPI_M30 = HPI_data.join(df_mortgage)

print(states_HPI_M30.corr()['M30'].describe())
