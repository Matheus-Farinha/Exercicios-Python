cidade = str(input('Qual cidade você mora?'))
print(cidade.startswith('Santo'))
###################
cidade = str(input('Qual cidade você mora?')).strip()
print(cidade[:5].upper() == 'SANTO')
