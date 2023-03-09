from time import sleep

info = dict()
lista = list()

for i in range(0,3):
    info["nome"] = str(input('Digite o nome completo: '))
    info["nota"] = float(input('Digite a nota: '))
    info["aprovado"] = False
    lista.append(info.copy())

print(lista)
for dado in lista:
    sleep(0.1)
    if dado['nota'] > 6:
        dado['aprovado'] = True

    print()
    if dado['aprovado']:
        print(f'Aluno {dado["nome"]:}')
        print(f'\tO Aluno foi aprovado!')
        print(f'Sua nota foi: {dado["nota"]}')
    
    else:
        print(f'Aluno {dado["nome"]:}')
        print(f'\tO Aluno foi reprovado!')
        print(f'Sua nota foi: {dado["nota"]}')

    print()