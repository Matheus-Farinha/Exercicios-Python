frase = str(input('Digite seu nome:'))
frasemenor = frase.lower()
frasemaior = frase.upper()
frase1 = frase.replace(' ', '')
tabela = frase.split()
frase2 = str(frase[0])
print('Seu nome em letra maiúscula é:', frasemaior)
print('Seu nome em letra minúscula é:', frasemenor)
print('Seu nome tem {} caracteres.'.format(len(frase1)))
#print('Seu primeiro nome é {} e tem {} letras.'.format(tabela[0], len(str(frase.find(' '))) ERRADA
#################################
nome = str(input('Qual o seu nome completo:')).strip()
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} caracteres.'.format(nome.find(' ')))
















