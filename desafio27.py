nome = str(input('Digite seu nome completo:'))
nome1 = nome.split()
primeira = nome1[0]
ultima = nome1[-1]
print(primeira, ultima)
###############
nome = str(input('Digite seu nome completo:')).strip()
nome1 = nome.split()
print('Seu primeiro nome é {}.'.format(nome1[0]))
print('Seu segundo nome é {}.'.format(nome1[len(nome1)-1]))

