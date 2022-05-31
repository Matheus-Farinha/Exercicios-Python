numero = int(input('Digite qualquer número:'))
if numero // 1 and numero // numero:
     print('Esse número é primo.')
else:
    print('esse número não é primo.')
###############
numero = int(input('Digite um número qualquer:'))
divisiveis = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        divisiveis += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes.'.format(numero, divisiveis))
if divisiveis == 2:
    print('O número é primo.')
else:
    print('O número náo é primo.')
