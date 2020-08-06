import pandas as pd

df1 = pd.read_csv('ceara.csv',sep=';',encoding='latin-1')

df1['Data'] = pd.to_datetime(df1['Data'], format='%m/%Y')

df1.set_index('Data', inplace = True)
df1.to_csv("ceara.csv", sep=';', quotechar='"', decimal='.', encoding='utf-8')