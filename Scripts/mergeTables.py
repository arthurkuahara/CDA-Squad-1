import pandas as pd

df1 = pd.read_csv('/file_path/file.csv',sep=';',encoding='latin-1')
df2 = pd.read_csv('/file_path/file.csv.csv',sep=';',encoding='latin-1')

df3 = pd.merge(df1, df2, how='left', on='Data')
df3.set_index('Data', inplace = True)

df3.to_csv("/file_path/file.csv", encoding='utf-8', sep=';', quotechar='"', decimal=',')