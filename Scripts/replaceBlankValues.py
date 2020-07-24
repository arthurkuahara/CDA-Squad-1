import pandas as pd
import glob
from sklearn.impute import KNNImputer

files = glob.glob('/file_path/*.csv')

for file in files:
    df = pd.read_csv(file, sep=';', index_col=0)

    imp = KNNImputer(n_neighbors=5)
    idf = pd.DataFrame(imp.fit_transform(df))

    idf.index = df.index
    idf.columns = df.columns

    idf = idf.round(2)
    idf.to_csv("{}".format(file), encoding='utf-8', sep=';', quotechar='"', decimal='.')