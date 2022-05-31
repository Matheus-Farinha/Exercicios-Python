import math

numero = int(input('Digite um número para saber seu fatorial: '))
fatorial = math.factorial(numero)
print(fatorial)
###############
numero = int(input('Digite um número para ver seu fatorial: '))
c = numero
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))