import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

api_key = "yQaxzc5rcgC8Hyt8SSdz"


def states_list():
    states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return states[0][0][1:]


def grab_state_data():
    states = states_list()
    # DataFrame object
    main_df = pd.DataFrame()

    # abbv = abreviation
    for abbv in states:
        query = 'FMAC/HPI_' + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [str(abbv)]
        # This is the pct_change...according to the START [0] !!!
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    # Salvar em um arquivo pickle para ler depois
    pickle_out = open('states_pct_change.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


# The entire US
def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df.rename(columns={'Value': str('United States')}, inplace=True)
    # também queremos o PCT_CHANGE
    df['United States'] = (df['United States'] -
                           df['United States'][0]) / df['United States'][0] * 100.0
    return df


def plot_dfs():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    # grab_state_data()
    benchmark = HPI_Benchmark()
    HPI_data = pd.read_pickle('states_pct_change.pickle')

    HPI_data.plot(ax=ax1)
    benchmark.plot(ax=ax1, color='k', linewidth=10)
    plt.legend().remove()
    plt.show()


def main():
    HPI_data = pd.read_pickle('states_pct_change.pickle')

    # Isso vai gerar uma correlação entre os dataframes
    HPI_States_Correlation = HPI_data.corr()
    print(HPI_States_Correlation)

    print(HPI_States_Correlation.describe())
    plot_dfs()


if __name__ == '__main__':
    main()
