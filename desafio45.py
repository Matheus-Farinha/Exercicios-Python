import random
jokenpo = str(input('PEDRA, PAPEL OU TESOURA?').upper())
pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print(jokenpo)
print(pc)
if jokenpo == pc:
    print('Houve empate, jogue de novo.')
elif jokenpo == 'PEDRA' and pc == 'PAPEL':
    print('O pc venceu.')
elif jokenpo == 'PAPEL' and pc == 'PEDRA':
    print('Você venceu.')
elif jokenpo == 'TESOURA' and pc == 'PEDRA':
    print('O pc venceu.')
elif jokenpo == 'PEDRA' and pc == 'TESOURA':
    print('Você venceu.')
elif jokenpo == 'TESOURA' and pc == 'PAPEL':
    print('Você venceu.')
elif jokenpo == 'PAPEL' and pc == 'TESOURA':
    print('O pc venceu.')
################
from random import randint
itens = ('papel', 'pedra', 'tesoura')
computador = randint(0, 2)
print(''' ESCOLHA :
        [0] PAPEL
        [1] PEDRA
        [2] TESOURA''')
decisao = int(input('Qual é a sua jogada?:'))
print('Pc jogou {}.'.format(itens[computador]))
print('Você jogou {}.'.format(itens[decisao]))



