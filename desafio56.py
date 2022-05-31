#menorvinte = 0
#contidade = 0
#for c in range(1, 5):
   # nome = str(input('Qual o nome da {}ª pessoa?'.format(c)))
   # idade = int(input('Qual a idade da {}ª pessoa?'.format(c)))
   ## sexo = str(input('Qual o sexo da {}ª pessoa?'.format(c)))
   # if idade < 20 and sexo == 'feminino':
   #     menorvinte += 1
   # print('Existe(m) {} mulher(es) menor(es) de vinte anos.\n'.format(menorvinte))
   # if maisvelho != idade and sexo == 'masculino':
   #     maisvelho = idade
   # if maisnovo < idade:
   #     maisnovo = maisvelho
   # print('O homem mais velho tem {} anos.'.format(idade))
##########################
somaidade = 0
homemvelho = 0
nomevelho = 0
contmulher = 0
for c in range(1, 5):
    nome = str(input('Qual o nome da {}ª pessoa?'.format(c))).strip()
    idade = int(input('Qual a idade da {}ª pessoa?'.format(c)))
    sexo = str(input('Qual o sexo da {}ª pessoa?[M/F]:'.format(c))).strip()
    somaidade += idade
    if sexo == 'Mm' and c == 1:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1
mediaidade = somaidade / 4
print('A média da idade desse grupo é de {}.'.format(mediaidade))
print('A idade do homem mais velho é {}, e seu nome é {}.'.format(homemvelho, nomevelho))
print('Existem {} mulher(es) com menos de 20 anos.'.format(contmulher))




