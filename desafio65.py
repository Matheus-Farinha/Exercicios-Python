##########################
resp = 's'
soma = quant = media = maior = menor = 0
while resp in 's':
    numero = int(input('Digite um número: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if resp == 'n':
        break
    resp = str(input('Quer continuar? [s/n]')).strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))


