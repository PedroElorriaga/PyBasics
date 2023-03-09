import pandas as pd

pd.set_option('display.max_rows', None) #Mostra todas linhas

with open('ADV.txt', 'w') as arqv:
    arquivo_csv = pd.read_csv("advertising.csv")
    arqv.write(str(arquivo_csv))
