reta1 = float(input('Digite o valor da primeira reta:'))
reta2 = float(input('Digite o valor da segunda reta:'))
reta3 = float(input('Digite o valor da terceira reta:'))
if reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta1+reta2:
    print('Pode ser formado um triângulo.')
else:
    print('Não pode ser formado um triângulo.')
if reta1 == reta2 == reta3:
    print('É um triângulo equilátero.')
elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print('É um triângulo isóceles.')
elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
    print('É um triângulo escaleno.')
#################
reta1 = float(input('Digite o valor da primeira reta:'))
reta2 = float(input('Digite o valor da segunda reta:'))
reta3 = float(input('Digite o valor da terceira reta:'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode ser formado um triângulo', end='')
    if reta1 == reta2 == reta3:
        print(' EQUILÁTERO.')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print(' ESCALENO.')
    else:
        print(' ISÓCELES.')
else:
    print('Não pode ser formado um triângulo.')
