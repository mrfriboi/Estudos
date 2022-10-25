def func(*args): # *args é um parâmetro de entrada que aceita qualquer número de argumentos
    print(args)
    print(args[0])
    print(args[-1]) # -1 é o último argumento
    print(len(args)) # len é a função que retorna o tamanho de um array
    args = list(args) # converte o argumento em uma lista
    args[0] = 'Novo valor' # altera o primeiro argumento
    print(args)

lista = [1, 2, 3, 4, 5] #lista de numeros
n1, n2, *n = lista # n1 = 1, n2 = 2, n = [3, 4, 5]
print(n1, n2, n) # n é um array

lista2 = [1, 2, 3, 4, 5] #lista de numeros
print(*lista2) # imprime os elementos do array desempacotando-o
print(*lista2, sep="-") # imprime os elementos do array desempacotando-o separando-os por -

func(1, 2, 3, 4, 5)

def func2(*args):
    for v in args:
        print(v)

lista3 = [1, 2, 3, 4, 5] #lista de numeros
print(func2(*lista3))

def func3(**kwargs): # **kwargs é um parâmetro de entrada que aceita qualquer número de argumentos
    print(kwargs)
    print(kwargs['nome'])
    print(kwargs['cidade'])

    idade = kwargs.get('idade') # get é uma função que retorna o valor de uma chave

    if idade: # se idade existe
        print(f'Idade: {idade}')
    else:
        print('Idade não encontrada')


print(func3(nome='Paulo', cidade='São Paulo'))