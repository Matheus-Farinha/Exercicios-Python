casa = float(input('Qual o valor da casa que deseja comprar?R$'))
salario = float(input('Qual é o seu salário?R$'))
tempo = int(input('Em quanto tempo pretende pagar a casa?'))
prestacao = (3 / 10) * salario
valor1 = casa / tempo
valor2 = valor1 / 12
if prestacao <= valor2:
    print('O empréstimo será negado!')
else:
    print('O empréstimo foi aprovado!')
print('Você vai pagar o valor de R${:.2f} por mês se pagar em {} anos.'.format(valor2, tempo))
