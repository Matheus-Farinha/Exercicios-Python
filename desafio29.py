multa = float(input('Digite aqui a velocidade em que você estava:'))
if multa > 80:
    print('Você foi multado!')
ultrap = (multa - 80) * 7
print('Você vai pagar o valor de R${:.2f}'.format(ultrap))
