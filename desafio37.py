numero = int(input('Digite um número:'))
print('''Escolha umas das bases para conversão:
[1] para transformar em binário.
[2] para transformar em octal.
[3] para transformar em hexadecimal.''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('{} convertido em binário é {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido em octal é {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido em hexadecimal é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Você digitou um número inválido, digite um número entre 1 e 3.')
