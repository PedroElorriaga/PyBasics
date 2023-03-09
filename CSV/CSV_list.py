import csv

with open('advertising.csv', 'r') as arqv:
    arquivo_csv = csv.reader(arqv)
    next(arquivo_csv)
    for linha in arquivo_csv:
        print(linha)