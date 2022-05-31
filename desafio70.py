totaldin = contp = 0
preco = 0
cont = 0
menor = 0
barato = ''
while True:
    produto = str(input('Digite o produto que comprou: '))
    preco = float(input('Digite o valor do produto:R$ '))
    cont += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        contp += 1
    totaldin += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
        print('-=' * 10)
    if continuar == 'N':
        break
print(f'O total deu R${totaldin:.2f}.')
print(f'Na lista existe(m) {contp} que custa(m) mais de R$1000,00.')
print(f'O produto mais barato é {barato} que custa {menor}.')

