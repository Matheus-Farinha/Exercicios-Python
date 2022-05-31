viagem = float(input('Qual a distância em km tem sua viagem? '))
passageml = viagem * 0.45
passagemc = viagem * 0.50
if viagem > 200:
    print('Você irá pagar R${:.2f}.'.format(passageml))
else:
    print('Você irá pagar R${:.2f}.'.format(passagemc))