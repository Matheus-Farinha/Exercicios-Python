soma = 0
cont = 0
for c in range(1, 7):
    n = (int(input('Digite o {} valor:'.format(c))))
    if n % 2 == 0:
        soma += n  # SOMA TODOS OS NÚMEROS PARES.
        cont += 1  # CONTA QUANTOS NÚMEROS SÃO PARES.
print('Você informou {} número(s) par(es)'.format(cont), end='')
print(' e a somatória deles deu {}.'.format(soma))

