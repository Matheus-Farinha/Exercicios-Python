cont = 0
pessoas = 0
for c in range(1, 8):
    nascimento = int(input('Qual o ano você nasceu {} pessoa:'.format(c)))
    if nascimento <= 2004:
        cont += 1
    elif nascimento >= 2004:
        pessoas += 1
print('Existem {} pessoas que atingiram a maioridade'.format(cont), end='')
print(', e existem {} que ainda não atingiram a maioridade.'.format(pessoas))