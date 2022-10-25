# variavel = 'valor'
#
# def func():
#     print(variavel)
#
# def func2(arg=None): # arg é um parâmetro de entrada que aceita qualquer número de argumentos
#     agr = arg.replace('a', 'e')
#     return agr
# func()
#
# outra_variavel = func2(arg=variavel) # outra_variavel recebe o retorno da função func2
#
# print(outra_variavel)
#
def func3(args=None):
    return args

def func2(args=None):
    return args

def func1 (funcao1, funcao2):
    return funcao1(), funcao2()

print(func1(func2, func3))