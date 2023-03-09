from dados import dados
import json

with open('JSON/ArqvJson.json', 'w') as arqv:
    json.dump(dados, arqv, indent=4)