import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = "yQaxzc5rcgC8Hyt8SSdz"


def main():
    HPI_data = pd.read_pickle('states_pct_change.pickle')

    fig = plt.figure()
    ax1 = plt.subplot2grid((2, 1), (0, 0))
    ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

    texas_alaska_correlation = pd.rolling_corr(HPI_data['TX'], HPI_data['AK'], 12)
    # texas_alaska_correlation = HPI_data['TX'].rolling(window=12).corr()

    # Plotar os originais
    HPI_data['TX'].plot(ax=ax1, label='TX HPI')
    HPI_data['AK'].plot(ax=ax1, label='AK HPI')
    ax1.legend(loc=4)

    # Plotar a correlação
    texas_alaska_correlation.plot(ax=ax2, label='texas_alaska_correlation')

    plt.legend(loc=4)
    plt.show()


if __name__ == '__main__':
    main()
