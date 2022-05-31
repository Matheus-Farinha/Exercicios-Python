import math
catop = float(input('Qual o comprimento do cateto oposto?'))
catadj = float(input('Qual o comprimento do cateto adjascente?'))
hipotenusa = math.hypot(catop, catadj)
print('O comprimento da hipotenusa resulta em {:.3f}'.format(math.ceil(hipotenusa)))
####################
from math import (hypot, ceil)
catop = float(input('Qual o valor do cateto oposto?'))
catadj = float(input('Qual o valor do cateto adjascente?'))
#hipotenusa = (catop ** 2 + catadj ** 2) ** (1/2)
hipotenusa = hypot(catop, catadj)
print('O comprimento da hipotenusa resulta em {:.3f}'.format(ceil(hipotenusa)))


