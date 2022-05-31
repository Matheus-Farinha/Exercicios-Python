frase = str(input('Digite uma frase qualquer:'))
espaco = frase.replace(' ', '')
invertida = espaco[::-1]
if frase == invertida or espaco == invertida:
    print('A palavra é {}, ela invertida é {}, e são palíndromos.'.format(espaco, invertida))
else:
    print('As palavras não são palíndromos.')
##################
frase = str(input('Digite uma frase qualquer:'))
palavras = frase.split() #SEPARA CADA PALAVRA EM LISTA.
junto = ''.join(palavras) # TIRA O ESPAÇO ENTRE AS PALAVRAS.
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)



