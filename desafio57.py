sexo = 'M' or 'F'
while sexo == 'M' or 'F':
    frase = (str(input('digite qual o seu sexo. [M/F]').upper()))
    if frase != 'M':
        if frase != 'F':
            print('Você digitou um dado inválido,', end='')
            print(' digite M ou F.')
######################
sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('O dado foi digitado errado. Digite M ou F:')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
