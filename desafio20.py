import random
aluno1 = str(input('Nome do primeiro aluno:'))
aluno2 = str(input('Nome do segundo aluno:'))
aluno3 = str(input('Nome do terceiro aluno:'))
aluno4 = str(input('Nome do quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação é: ', lista)
################
import random
aluno1 = str(input('Nome do primeiro aluno:'))
aluno2 = str(input('Nome do segundo aluno:'))
aluno3 = str(input('Nome do terceiro aluno:'))
aluno4 = str(input('Nome do quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem escolhida foi:', lista)
###################
from random import shuffle
aluno1 = str(input('Nome do primeiro aluno:'))
aluno2 = str(input('Nome do segundo aluno:'))
aluno3 = str(input('Nome do terceiro aluno:'))
aluno4 = str(input('Nome do quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem escolhida foi: ', lista)
