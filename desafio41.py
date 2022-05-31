from datetime import date
atual = date.today().year
atleta = float(input('Digite o ano do seu nascimento:'))
ano = atual - atleta
if ano <= 9:
    print('A sua categoria é mirim!')
elif ano <= 14:
    print('Sua categoria é infantil!')
elif ano <= 19:
    print('Sua categora é júnior!')
elif ano <= 20:
    print('Sua categoria é sênior!')
else:
    print('Sua categoria é master!')
