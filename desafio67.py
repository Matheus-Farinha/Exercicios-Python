tabuada = 1
while tabuada >= 0:
    tabuada = int(input('Digite um número para ver sua tabuada: '))
    for c in range(1, 11):
        if tabuada < 0:
            break
        print(f'{tabuada} x {c} = {tabuada * c}')


