from random import randint
from operator import itemgetter

bd = {
    'user1' : randint(1,6),
    'user2' : randint(1,6),
    'user3' : randint(1,6),
    'user4' : randint(1,6),
}

format_bd = dict()
format_bd = sorted(bd.items(), key=itemgetter(1), reverse=True)
format_bdList = list()
format_bdList.append(format_bd.copy())
for i in format_bdList:
    print(f'O Jogador vencedor foi {i[0][0]}, tirou {i[0][1]}')
   