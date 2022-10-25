# For / Else em python

nomes = ['João', 'Maria', 'José', 'Pedro' , 'Lucas' , 'Bianca']

comeca_com_j = False

# for valor in nomes:
#     if valor.startswith('J'):
#         print(f'O nome {valor} começa com J')
#     else:
#         print(f'O nome {valor} não começa com J')

for valor in nomes:
    if valor.lower().startswith('j'):
        print('existe um nome q começa com J')
        break

else: # for suporta else
    print('Não existe um nome que começa com J')