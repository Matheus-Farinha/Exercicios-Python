reta1 = float(input('Digite o comprimento da primeira reta:'))
reta2 = float(input('Digite o comprimenro da segunda reta:'))
reta3 = float(input('Digite o comprimento da terceira reta:'))
if reta1 < reta3+reta2 and reta2 < reta1+reta3 and reta3 < reta2+reta1:
    print('Dá para fazer um triangulo.')
else:
    print('Não da pra fazer um triangulo.')
