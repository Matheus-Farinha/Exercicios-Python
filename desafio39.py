idade = float(input('Digite a sua idade:'))
tempomais = (idade - 18) * 12
tempomenos = ((idade - 18) * 12) * -1
if idade == 18:
    print('Está na hora de se alistar.')
elif idade < 18:
    print('Ainda vai se alistar.')
    print('Faltam {} meses para você se alistar.'.format(tempomenos))
else:
    print('Já passou o tempo de você se alistar!')
    print('Já passou {} meses que você deveria se alistar.'.format(tempomais))

