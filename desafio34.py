salario = int(input('Qual o valor do seu salário atualmente?'))
dez = salario * (10/100)
quinze = salario * (15/100)
somadez = salario + dez
somaquinze = salario + quinze
if salario > 1250:
    print('Você recebeu um aumento de 10% em seu salário, e receberá R${:.2f} a mais, totalizando {:.2f}'.format(quinze, somaquinze))
else:
    print('Você recebeu um aumento de 15% em seu salário, e receberá R${:.2f} a mais, totalizando {:.2f}'.format(quinze,somadez))


