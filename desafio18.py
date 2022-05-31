import math
angulo = float(input('Digite um ângulo:'))
sen = math.radians(angulo)
sen1 = math.sin(sen)
cos = math.radians(angulo)
cos1 = math.cos(cos)
tg = math.radians(angulo)
tg1 = math.tan(tg)
print('O seno é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}'.format(sen1, cos1, tg1))
#print('O seno é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}'.format(math.ceil(sen), math.ceil(cos), math.ceil(tg)))
#############
from math import sin, cos, tan, floor, radians
angulo = float(input('Digite um ângulo:'))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))
#print('O seno é {:.3f}, o cosseno é {:.3f} e a tangente é {:3.f}'.format(sen, cos, tg)) TIRA O FLOOR DO IMPORT Q FUNCIONA
print('O seno é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}'.format(floor(sen),floor(cos), floor(tg)))
#################
import math
angulo = float(input('Digite um ângulo:'))
sen = sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('O seno é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}.'.format(sen, cos, tg))






