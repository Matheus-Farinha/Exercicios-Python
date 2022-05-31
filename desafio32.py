ano = int(input('Digite um ano qualquer:'))
resultado = ano % 4
if resultado == 1:
    print('O ano digitado não é bissexto!')
else:
    print('O ano digitado é bissexto!')
