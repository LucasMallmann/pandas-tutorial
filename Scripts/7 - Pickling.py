import pandas as pd
import quandl
import pickle

api_key = "yQaxzc5rcgC8Hyt8SSdz"


def states_list():
    states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return states[0][0][1:]

# Grab the data from the internet


# grab_state_data()

# agora posso carregar sem precisar acessar o quandl novamente
pickle_in = open('states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)


# Esse é o pickle do Pandas. É mais rápido
HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
