produto = float(input('Qual o preço do produto que voce deseja?'))
promocao = produto*(5/100)
valordescontado = produto-promocao
print('O produto que você escolheu recebe 5% de desconto e o total ficou R${:.2f}.'.format(valordescontado))
###################
produto = float(input('Qual o preço do produto que você deseja?'))
promocao = produto - (produto*5/100)
print('O produto que você escolheu recebe 5% de desconto e o total ficou R${:.2f}.'.format(promocao))
