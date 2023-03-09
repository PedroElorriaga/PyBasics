from time import sleep

perguntas = [
    {
        'Pergunta' : 'Em qual ano, o Corinthians foi campeão mundial?',
        'Alternativas' : ['2013', '2015', '2012', '2005'],
        'Resp' : '2012'
    },
    {
        'Pergunta' : 'Qual jogador fez um gol de cabeça na final do mundial?',
        'Alternativas' : ['Cassio','Renato Augsto','Emerson Sheik','Paolo Guerreiro'],
        'Resp' : 'Paolo Guerreiro'
    },
    {
        'Pergunta' : 'Qual jogador marcou um Hat trick no segundo jogo das quartas de finais da copa do Brasil de 2022?',
        'Alternativas' : ['Yuri Alberto','Renato Augusto','Roger Guedes','Giuliano'],
        'Resp' : 'Yuri Alberto'
    },
]

for cadaPergunta in perguntas:
    print(f'Pergunta: ', cadaPergunta['Pergunta'])

    alternativas = [x for x in cadaPergunta['Alternativas']]
    for i,cadaAlternativa in enumerate(alternativas):
        sleep(0.1)
        print(f'\t{i}) ',cadaAlternativa)   
    print()

    escolha_user = input('Digite sua escolha: ')
    escolhaInt = None
    qtd_alternativas = len(cadaAlternativa)
    acerto = False

    if escolha_user.isnumeric():
        escolhaInt = int(escolha_user)

    if escolhaInt is not None:
        if escolhaInt >= 0 and escolhaInt < qtd_alternativas:
            if alternativas[escolhaInt] == cadaPergunta['Resp']:
                acerto = True

    if acerto:
        print('Acertou')

    else:
        print('Errou')

