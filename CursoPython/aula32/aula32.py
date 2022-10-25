lista = [
    ['P1' , 13],
    ['P2' , 14],
    ['P3' , 15],
    ['P4' , 16],
    ['P5' , 17],
]

#def func (item): # item é um parâmetro de entrada que aceita um único argumento
#    return item[1]  # retorna o valor da segunda posição do array


#lista.sort(key=func, reverse=True) # ordena a lista de acordo com a função definida em key e inverte a ordem em reverse

#lista.sort(key=lambda item: item[1], reverse=True) # ordena a lista de acordo com a função definida em key e inverte a ordem em reverse

#print(lista)

print(sorted(lista, key=lambda item: item[1], reverse=True)) # ordena a lista de acordo com a função definida em key e inverte a ordem em reverse
