import json

with open('JSON/ArqvJson.json', 'r') as arqv:
    dados = json.load(arqv)

for key, value in dados.items():
    print(f'Carro {key}: \n')
    for k,v in value.items():
        print(f'\t{k}: {v}')