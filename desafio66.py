cont = soma = total = 0
while True:
    numero = int(input('Digite um número (999 para parar): '))
    cont += 1
    soma += numero
    if numero == 999:
        soma -= 999
        cont -= 1
        break
print(f'A soma dos {cont} valores resultou em {soma}.')

