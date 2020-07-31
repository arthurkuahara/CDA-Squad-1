import pandas as pd
import glob

files = glob.glob('/filepath/*.csv')

for file in files:
    df = pd.read_csv(file, sep=';', index_col=0)

    for column in df:
        df[column] = df[column].rolling(12, center=True, min_periods=1).mean()
        df[column] = df[column].round(2)


    df.to_csv("{}-movel".format(file), sep=';', quotechar='"', decimal='.', encoding='utf-8')