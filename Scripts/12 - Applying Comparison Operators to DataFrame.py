import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl
##style.use('fivethirtyeight')
style.use('ggplot')


# 6212.42 parece ser um dado errado. Não está certo
altura_ponte = {'metros': [10.26, 10.31, 10.27, 10.22,
                           10.23, 6212.42, 10.28, 10.25,
                           10.31]}

df = pd.DataFrame(altura_ponte)

# Achar a standard deviation
df['STD'] = df['metros'].rolling(window=2, center=False).std()

# pegar a média da std deviation
# pegar a coluna metros na linha std
media_std = df.describe()['metros']['std']

# agora que tenho a média std, posso redefinir o dataframe
# data_frame = data_frame where data_frame_std é MENOR QUE A MÉDIA DA STD
df = df[ (df['STD'] < media_std) ]

##print(df[['metros', 'STD']])
print(df)
print('\n')
print(media_std)

plt.ylabel('metros')
plt.xlabel('pontos')

df['metros'].plot()
plt.show()
