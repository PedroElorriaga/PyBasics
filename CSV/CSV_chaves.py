import csv

with open('advertising.csv', 'r')as arqv:
    arquivo_csv = [x for x in csv.DictReader(arqv)]

with open('ArquivoRead.txt', 'w')as arqv:
    writter = csv.writer(
        arqv,
        delimiter=',',
        quotechar='"',
        quoting= csv.QUOTE_ALL
    )

    writter_keys = csv.writer(
        arqv,
        delimiter=',',
        quotechar='-',
        quoting= csv.QUOTE_ALL
    )

    chaves = [x for x in arquivo_csv[0].keys()] 
    writter_keys.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in arquivo_csv:
        writter.writerow(
            [
            dado['TV'],
            dado['Radio'],
            dado['Jornal'],
            dado['Vendas']
            ]            
        )