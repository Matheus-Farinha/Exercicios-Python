dias = float(input('Quantos dias foram aulugados o seu veículo?'))
km = float(input('Quantos km você rodou com o carro?'))
precodia = dias * 60
precokm = km * 0.15
total = precodia + precokm
print('O preço a se pagar é de R${}'.format(total))
############################
dias = float(input('Quantos dias foram alugados o seu veículo?'))
km = float(input('Qauntos km você rodou com o carro?'))
total = (dias * 60) + (km * 0.15)
print('O preço a se pagar é de R${}'.format(total))
