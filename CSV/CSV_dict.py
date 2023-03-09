import csv

with open('advertising.csv', 'r') as arqv:
    arquivo_csv = csv.DictReader(arqv)
    for linha in arquivo_csv:
        print(linha)