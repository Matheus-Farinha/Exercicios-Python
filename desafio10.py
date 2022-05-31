total = float(input('Me diga quantos reais você tem na sua carteira:R$'))
dolar = total / 3.27
print('Você consegue comprar US${:.3f} com seus R${}.'.format(dolar, total))
