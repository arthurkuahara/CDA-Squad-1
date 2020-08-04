import pandas as pd
import glob

files = glob.glob('/file_path/*.csv')

valores_faltantes = []
for file in files:
    try:
        df1 = pd.read_csv(file, sep=';', decimal=',', thousands='.', encoding= 'latin-1')
        df1 = df1.replace(['-'], [None])
        if df1['Data'][-1:].item() == "Fonte":
            df1.drop(df1.tail(1).index, inplace=True)

        for i in range(3):
            for column in df1.columns:
                if df1[column][-1:].item() == None:
                    df1.drop(df1.tail(1).index, inplace=True)

        df1['Data'] = pd.to_datetime(df1['Data'], format='%m/%Y')

        df2 = df1[(df1.Data >= "2011-01-01")]

        # columns_to_drop = []  
        consecutive_nulls = 0
        for column in df2.columns[1:]:
            consecutive_nulls = 0
            for value in df2[column]:
                try:
                    if consecutive_nulls == 4:
                        valores_faltantes.append(file)
                        valores_faltantes.append(column)
                        # columns_to_drop.append(column)
                        break
                    elif value == None:
                        consecutive_nulls += 1
                    else:
                        consecutive_nulls = 0
                except:
                    pass    
            # print(column, consecutive_nulls)
        # print(columns_to_drop)
        
        # df3 = pd.DataFrame(df2, columns = ['Data'])
        # for column in columns_to_drop:
        #     df3 = df3.join(df2[column])

        # df2 = df2.drop(columns=columns_to_drop)
        # df3 = df3[(df3.Data >= "2011-01-01")]

        # columns_to_drop_2 = []
        # consecutive_nulls = 0
        # for column in df3.columns[1:]:
        #     consecutive_nulls = 0
        #     for value in df3[column]:
        #         try:    
        #             if consecutive_nulls == 4:
        #                 columns_to_drop_2.append(column)
        #                 break                 
        #             elif value == None:
        #                 consecutive_nulls += 1                
        #             else:
        #                 consecutive_nulls = 0
        #                 pass
        #         except:
        #             pass
        #     print(column, consecutive_nulls)
        # print(columns_to_drop_2)

        # df2['Data'] = df2['Data'].apply(lambda x: x.strftime('%m/%Y'))
        # df3['Data'] = df3['Data'].apply(lambda x: x.strftime('%m/%Y'))
        df2.set_index('Data', inplace = True)
        # df3.set_index('Data', inplace = True)

        df2.to_csv("{}".format(file), encoding='utf-8', sep=';', quotechar='"', decimal=',')
        # df3.to_csv("/home/alan/cda/teste/tarefa 13 - 2011.csv", encoding='utf-8', sep=';', quotechar='"', decimal=',')
    except Exception as e:
        print(file, e)

print(valores_faltantes)