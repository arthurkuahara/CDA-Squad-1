import pandas as pd
import glob

files = glob.glob('ceara.csv')

for file in files:
    df = pd.read_csv(file, sep=';', index_col=0)

    for column in df:
        df[column] = df[column].rolling(12, center=True, min_periods=1).mean()
        df[column] = df[column].round(2)

    filename = file[:-4] + "-media.csv"

    df.to_csv(filename, sep=';', quotechar='"', decimal='.', encoding='utf-8')