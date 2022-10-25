# # sets
# # add (adiciona elementos)
# # Update (atualiza elementos)
# # clear (limpa o set)
# # discard (remove elementos)
# # union | une (uniao de sets)
# # intersection & (intersecao de sets)
# # difference - (diferenca de sets)
# # symmetric_difference ^ (diferenca simetrica de sets) , ou seja, os elementos que estao em um set e nao em outro
#
# # s1 = set ()
# # s1.add(1)
# # s1.add(2)
# # s1.add(3)
# #
# # print(s1)
# #
# # s1.discard(2) # remove o elemento 2
# #
# # print(s1)
# #
# # s1.update('python') # atualiza o set com o elemento 'python'
# #
# # print(s1)
# #
# #
# # s1.update([1, 2, 3, 4, 6 ,5]) # atualiza o set com o elemento [1, 2, 3, 4, 6 ,5]
# #
# # print(s1)
#
# # da pra usar para excluir os duplicados de uma lista
# # lista = [1,1 , 1, 2,  2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(lista)
# # lista = (set(lista))
# # lista = list(lista)
# # print(lista)
#
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
#
# s2_list = list(s2)
# print(s2_list)
# s3 = s1 | s2 # uniao de sets
# # or
# # s3 = s1.union(s2) # uniao de sets
#
# print(s3)
#
# s4 = s1 & s2 # intersecao de sets
# # and
# # s4 = s1.intersection(s2) # intersecao de sets
#
# print(s4)
#
# s5 = s1 - s2 # diferenca de sets
# # -
# # s5 = s1.difference(s2) # diferenca de sets
# print(s5)
#
# s6 = s1 ^ s2 # diferenca simetrica de sets
# # ^
# # s6 = s1.symmetric_difference(s2) # diferenca simetrica de sets
# print(s6)
#
s1 = {1, 2, 3, 4, 5}

if 2 in s1:
    print('existe' )