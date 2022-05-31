pt = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
decimot = pt + (10 - 1) * razao
while decimot + razao <= decimot + razao:
    for c in range(pt, decimot + razao, razao):
        print(c)
    print('Acabou')
    break
##############
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = pt
cont = 1
while cont <= 10:
    print('{}➝'.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')