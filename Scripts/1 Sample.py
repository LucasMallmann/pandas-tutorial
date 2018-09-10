import pandas as pd

stats = {'Day': [1, 2, 3, 4, 5, 6],
         'Visitors': [43, 53, 68, 98, 102, 200],
         'Rate': [85, 20, 46, 92, 85, 100]}

df = pd.DataFrame(stats)
df.set_index('Day', inplace=True)
print(df.head())
