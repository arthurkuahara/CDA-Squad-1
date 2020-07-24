import pandas as pd
import glob

files = glob.glob('/file_path/*.csv')

for file in files:
    df = pd.read_csv(file, sep=';', index_col=0, thousands='.')
    columns = df.columns
    for column in columns:
        df[column] = df[column].astype(str).str.replace('.', '')
        count0 = 0
        for value in df[column]:
            try:   
                if "," in value:
                    df[column] = df[column].str.replace(',', '.')
                    float(df[column][count0])    
            except:
                pass
            count0 += 1

    df.to_csv("{}".format(file), encoding='utf-8', sep=';', quotechar='"', decimal='.')
    print(file)