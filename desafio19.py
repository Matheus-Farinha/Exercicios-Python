import random
aluno1 = str(input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro aluno:'))
aluno4 = str(input('Quarto aluno:'))
print('O aluno escolhido para apagar o quadro foi {}.'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))
###########################
import random
aluno1 = str(input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro aluno:'))
aluno4 = str(input('Quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
####################
from random import choice
aluno1 = str(input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro aluno:'))
aluno4 = str(input('Quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O escolhido foi {}.'.format(escolhido))