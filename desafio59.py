valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print('Digite qual operação deseja realizar:\n'
      '[1] somar\n'
      '[2] multiplicar\n'
      '[3] maior\n'
      '[4] novos números\n'
      '[5] sair do programa.')
    escolha = int(input('Digite a operação desejada: '))
    if escolha == 1:
        print('A soma dos números escolhidos foi de {}.'.format(valor1 + valor2))
    elif escolha == 2:
        print('A multiplicação dos dois números resultou em {}.'.format(valor1 * valor2))
    elif escolha == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('O maior número é {}.'.format(maior)[:-2])
    if escolha == 4:
        valor11 = int(input('Digite outro valor: '))
        valor22 = int(input('Digite outro valor: '))
    if escolha == 5:
        print('Acabou!')
print('Fim do programa!')




