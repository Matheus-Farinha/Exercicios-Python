num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor:'))
num3 = int(input('Digite o terceiro valor:'))
if num1 > num2 and num1 > num3:
    print('O maior número é {}'.format(num1))
if num2 > num1 and num2 > num3:
    print('O maior número é {}'.format(num2))
if num3 > num1 and num3 > num2:
    print('O maior número é {}.'.format(num3))
if num1 < num2 and num1 < num3:
    print('O menor valor é {}.'.format(num1))
if num2 < num1 and num2 < num3:
    print('O menor valor é {}.'.format(num2))
if num3 < num1 and num3 < num2:
    print('O menor valor é {}.'.format(num3))
