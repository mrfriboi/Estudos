# PSlit, join, enumerate em python
# Split - divide uma string em uma lista de strings
# Join - junta uma lista de strings em uma string
# Enumerate - retorna um enumerate
#
#string = "O rato roeu a roupa do rei de roma, esse rato é brabo"

# lista_1 = string.split(' ') # divide a string em uma lista de strings separadas por espaço ou qualquer outro caracter entre parenteses
#
# lista_2 = string.split(',') # divide a string em uma lista de strings separadas por vírgula
#
# palavra = ''
# contagem = 0
#
# for valor in lista_1: # percorre a lista
#     # print(f'A palavra {valor} apareceu {lista_1.count(valor)} x na frase') # conta quantas vezes a palavra aparece
#
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
# print(f'A palavra que mais apareceu foi: {palavra}, que apareceu {contagem} x na frase')


#--------join--------
# lista = [ "O", "rato", "roeu", "a", "roupa", "do", "rei", "de", "roma" ]
# ou
# string = "O rato roeu a roupa do rei de roma"
# lista = string.split(' ')
# string_join = ' '.join(lista)
#
# # print(lista)
# #
# # print(string_join)
#
# for indice,valor in enumerate(lista): # percorre a lista e retorna um enumerate
#     print(f'{indice} - {valor}. lista = {lista[indice]}')

lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for v in lista:
    print(v [0], v [1], v [2])

lista_nome = [
    [0, 'João'],
    [1, 'Maria'],
    [2, 'Pedro'],
]

for indice, nome in lista_nome:
    print(f'{indice} - {nome}')