conti = conth = contm = 0
while True:
    print('*-' * 10, 'CADASTRE UM INDIVÍDUO', '*-' * 10)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()
    idade = int(input('Digite sua idade: '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if idade > 18:
        conti += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm += 1
    if continuar == 'N':
        break
print(f'Existem {conti} pessoas que tem mais de 18 anos.')
print(f'Foram cadastrados {conth} homens.')
print(f'Existem {contm} mulheres com menos de 20 anos.')




