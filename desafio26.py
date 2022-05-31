frase = str(input('Escreva uma frase importante:'))
print(frase.count('a'))
print(frase.find('a'))
print(frase.rfind('a'))
####################
frase = str(input('Escreva uma frase importante:')).upper().strip()
print(frase.count('A'))
print(frase.find('A') + 1)
print(frase.rfind('A') + 1)



