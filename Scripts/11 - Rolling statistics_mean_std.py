import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


def main():
    HPI_data = pd.read_pickle('states_pct_change.pickle')

    ax1 = plt.subplot2grid((2, 1), (0, 0))
    ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

    # TX12MA --> Texas Moving Average for 12 months. using the rolling_mean
    HPI_data['TX12MA'] = HPI_data['TX'].rolling(window=12, center=False).mean()
    
    # STD DEVIATION --> Calculate standard_deviation
    # Std --> how spread is the data from the mean?
    HPI_data['TX12STD'] = HPI_data['TX'].rolling(window=12, center=False).std()

    # Ploting the data
    HPI_data[['TX', 'TX12MA']].plot(ax=ax1)
    HPI_data[['TX12STD']].plot(ax=ax2)
    plt.legend(loc=4)
    print(HPI_data[['TX', 'TX12MA', 'TX12STD']].head())
    plt.show()

if __name__ == '__main__':
    main()
