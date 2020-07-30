import pandas as pd
df = pd.read_csv('/file_path/file.csv', sep=';', index_col=0)

for column in df:
    df[column] = df[column].rolling(12, center=True, min_periods=1).mean()
    df[column] = df[column].round(2)

df.to_csv('/file_path/file-movel.csv', sep=';', quotechar='"', decimal='.', encoding='utf-8')