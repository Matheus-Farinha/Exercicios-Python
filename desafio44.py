pagamento = float(input('Digite o valor do produto: R$'))
opcao1 = pagamento * (10 / 100)
opcao2 = pagamento * (5 / 100)
opcao4 = pagamento * (20 / 100)
juros = pagamento + opcao4
desconto1 = pagamento - opcao1
desconto2 = pagamento - opcao2
print('ESCOLHA UMA FORMA DE PAGAMENTO\n'
      '[1] À VISTA (DINHEIRO OU CHEQUE).\n'
      '[2] À VISTA NO CARTÃO.\n'
      '[3] 2X NO CARTÃO.\n'
      '[4] 3X OU MAIS NO CARTÃO.')
forma = int(input('Qual a opção desejada?'))
if forma == 1:
    print('Você recebeu 10% de desconto, o total ficará em R${:.2f}.'.format(desconto1))
elif forma == 2:
    print('Você recebeu 5% de desconto, o total ficará em R${:.2f}.'.format(desconto2))
elif forma == 3:
    print('Pagando em duas vezes você não paga juros,', end='')
    print(' e o total ficará em R${:.2f} por parcela.'.format(pagamento / 2))
elif forma == 4:
    totalparc = int(input('Em quantas vezes deseja parcelar no cartão?:'))
    preco = (juros * pagamento) / totalparc
    print('Pagando em {} vezes você recebe 20% de juros,'.format(totalparc), end='')
    print(' e o total ficará em R${:.2f} por parcela.'.format(juros / totalparc))
else:
    print('Você errou o dígito, escolha uma opção entre 1 e 4.')
