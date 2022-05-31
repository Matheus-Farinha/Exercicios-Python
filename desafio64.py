numero = 0
cont = 0
soma = 0
while numero != 999:
    numero = int(input('Digite algum número: '))
    if numero < 999:
        cont += 1
        soma += numero
        if numero == 999:
            soma -= 999
    else:
        print('ENCERROU! {} foi a soma dos números digitados.'.format(soma))
print('Foram digitados {} números, e a soma de todos eles resultou'.format(cont), end='')
print(' em {}.'.format(soma))
###############
