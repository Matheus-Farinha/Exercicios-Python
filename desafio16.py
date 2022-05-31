import math
n = float(input('Escolha um número:'))
inteiro = math.trunc(n)
print('O número que você escolheu foi {:.3f}, e o seu número inteiro é {}.'.format(n, inteiro))
#print('O número que voce escolheu foi {:.3f}, e o seu numero inteiro é {}'.format(n, math.flor(intero))) <PARA ARREDONDAR NA FUNÇÃO
#####################
from math import trunc
n = float(input('Escolha um número:'))
inteiro = trunc(n)
print('O número que você escolheu foi {:.3f}, e o seu número inteiro é {}.'.format(n, inteiro))
###############
import math
n = float(input('Escolha um número:'))
print('O número que vocé escolheu foi {:.3f}, e o seu número inteiro é {}.'.format(n, math.trunc(n)))
##################
from math import trunc
n = float(input('Escolha um número:'))
print('O número que você escolheu foi {:.3f}, e o seu número inteiro é {}.'.format(n, trunc(n)))

