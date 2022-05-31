pt = int(input('Qual o primeiro termo da PA:'))
razao = int(input('Qual a razão da PA:'))
for c in range(0, 10):
    pt += razao
    print(pt)
#############
pt = int(input('Digite o primeito termo:'))
razao = int(input('E a razão:'))
decimot= pt + (10 - 1) * razao
for c in range(pt, decimot + razao, razao):
    print('{}'.format(c), end='🠖')
print('Acabou')