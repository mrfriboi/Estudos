# # list comprehension
# #
# lista = [1, 2, 3, 4, 5]
# lista2 = [i * 2 for i in lista]
# print(lista2)
#
# lista3 = [i / 2 for i in lista]
# print(lista3)
#
# exemplo = [v * 2 for v in lista]
# exemplo2 = [(v, v2) for v in lista for v2 in range(3)]
#
# print(exemplo2)

# lista3 = ['Paulo', 'Maria', 'Pedro', 'João']
# exemplo4 = [v.replace('a', '@').upper() for v in lista3]
# print(exemplo4)

# tupla = (
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# )
#
# exemplo5 = [(y, x) for x, y in tupla]
# print(exemplo5)

# exemplo6 = dict(exemplo5)
# print(exemplo6)

l3 = list(range(100))
print(l3)

ex6 = [v for v in l3 if v % 2 ==0]
print(ex6)

ex7 = [v for v in l3 if v % 3 ==0 if v % 8 ==0]
print(ex7)

ex8 = [v if v % 3 ==0 else 'não é' for v in l3]
print(ex8)