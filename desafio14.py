temperatura = float(input('Informe a temperatura em ºC:'))
farehait = temperatura * 1.8 + 32
kelvin = temperatura + 273.15
print('A temperatura {:.2f}ºC corresponde em {:.2f}F e corresponde a {:.2f}K.'.format(temperatura, farehait, kelvin))
