n = int(input('Digite a tabuada que deseja efetuar:'))
for c in range(0, 11):
    m = c * n
    print(c, 'x', n, '=', m)
#########
num = int(input('Digite a tabuada que deseja efetuar:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))