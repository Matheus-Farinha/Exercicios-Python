print('*-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('*-' * 20)
pi = computador ='P' or 'I'
resultado = 'Par' or 'Ímpar'
cont = 0
while pi != resultado:
    from random import randint
    valor = int(input('Diga um valor: '))
    sorteado = randint(0, 10)
    pi = str(input('Ele é par ou ímpar [P/I]?: ')).upper().strip()
    print('+' * 20)
    cont += 1
    soma = sorteado + valor
    if soma % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Ímpar'
    if pi == 'I':
        computador = 'P'
    elif pi == 'P':
        computador = 'I'
    print(f'Você jogou {valor} e o computador jogou {sorteado}.', end='')
    print(f' Total resultou em {soma} e esse número é {resultado}.')
    if pi == 'I' and resultado == 'Ímpar':
        print('Você venceu.')
        print('Vamos jogar novamente...')
        print('+' * 20)
    elif pi == 'P' and resultado == 'Par':
        print('Você venceu.')
        print('Vamos jogar novamente...')
        print('+' * 20)
    else:
        cont -= 1
        print('Você perdeu!')
        print(f'GAME OVER! Você venceu com {cont} tentativas.')
        print('+' * 20)
        break



