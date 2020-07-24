import pandas as pd
import glob


def strip_right(df):
    df.columns = df.columns.str.replace("( ).*","")
    

files = glob.glob('/file_path/*.csv')

# Substitui as tabelas originais
for file in files:
    try:
        df = pd.read_csv(file, sep=';', encoding='latin-1')
        df.set_index('Data', inplace=True)
        strip_right(df)
        df.to_csv("{}".format(file), sep=';', quotechar='"', decimal=',', encoding='utf-8')
        print("funcionou " + file)
    except Exception as e:
        print("erro " + file)
        print(e)

# Para gerar uma tabela paralela à original usar:
#for file in files:
#    df = pd.read_csv(file, sep=';', encoding='latin-1')
#    df.set_index('Data', inplace=True)
#    strip_right(df)
#    filename = file[:-4]
#    df.to_csv(filename + "_updt.csv", sep=';', quotechar='"', decimal=',', encoding='utf-8')
#    print(filename)