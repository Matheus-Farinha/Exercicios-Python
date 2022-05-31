import random
escolha = int(input('Escolha um número de 1 a 5:'))
n = [1, 2, 3, 4, 5]
escolhido = random.choice(n)
n = int
if escolha == escolhido:
    print('Parabéns voce adivinhou!')
else:
    print('Tente novamente!')
print(escolhido)
