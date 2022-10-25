# dicionario
# d1 = {'nome': 'João', 'idade': 20}
# print(d1['nome'])
# print(d1['idade'])
#
#
# d2 = dict(nome='João', nome2='pedro')
# print(d2['nome'])
# d2['nome3'] = 'Maria'
# print(d2['nome2'])
# print(d2)
# print('--------------------')
# if 'nao existe' in d2:
#     print('nao existe')
#
# d2['nao existe'] = 'Pedro'
#
# if 'nao existe' in d2:
#     print(d2['nao existe'])
# print('oi')
#
# d3 = {
#     'str': 'valor',
#     123: 'valor2',
#     (1, 2, 3): 'tupla',
# }
#
# d3.update({'nomedachave': 'novo valor'})
#
# if d3.get('nomedachave') is not None:
#     print(d3.get('nomedachave'))
#
# del d3['nomedachave']
#
# print(d3)
#
# print('str' in d3)
#
# print('valor' in d3.values())
#
#
d4 = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
}

# for k in d4:
#     print(k)
#
# for v in d4.values():
#     print(v)

# for i in d4.items():
#     print(i[0], i[1])
#     print(i)

# for a , b in d4.items():
#     print(a, b)

# clientes = {
#     '1': {
#         'nome': 'João',
#         'idade': 20,
#     },
#     '2': {
#         'nome': 'Maria',
#         'idade': 25
#     },
#     '3': {
#         'nome': 'Pedro',
#         'idade': 30
#     },
# }
#
# for clientes_k, clientes_v in clientes.items(): # items() retorna uma lista de tuplas
#     print(f'Cliente {clientes_k}')
#     for dados_k, dados_v in clientes_v.items(): # items() retorna uma lista de tuplas dentro de outra tupla
#         print(f'\t{dados_k} = {dados_v}')

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d5 = dict(lista)
print(d5)