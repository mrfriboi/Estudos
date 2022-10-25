# Informações:
# 1.	Pode-se utilizar qualquer linguagem de programação à escolha do candidato (até mesmo pseudo-linguagem)
# 2.	Não utilize nenhuma função específica de uma linguagem, mantenha-se somente aos fundamentos da lógica de programação. (Permitidos utilizar "if", "switch", "for", "while" e similares)
# 3.	NÃO é necessário tratar os parâmetros da função para caso eles não sejam o que a função esteja esperando, a função irá SEMPRE receber valores válidos para a sua execução nominal.
# 4.	NÃO é necessário declarar as variáveis parâmetros da função, estas estarão declaradas por padrão já com um valor neles. (Não peça para o usuário inserir um valor, este já é passado para a função)
#
# Crie uma função que receba 3 parâmetros: Um número, um array de números e um booleano.
#
# Se o booleano for VERDADEIRO a função deve retornar o array de números que ela recebeu com cada um de seus números internos MULTIPLICADO pelo número dado à função (como o 1 parâmetro)
#
# Já se o booleano for FALSO a função deve retornar o array de números que ela recebeu com cada um de seus números internos SOMADO pelo número dado à função (como o 1 parâmetro)
#
# Exemplos de comportamento esperado da função:
# Considere "F" o nome da função
# Considere "( )" como os parâmetros enviados à função
# Considere tudo depois de "=>" como o valor retornado da função
#
# F( 5, [ 1, 2, 3 ], true)  => [ 5, 10, 15 ]
#
# F( 10, [ 9, 18, 27 ], false)  => [ 19, 28, 37 ]
#
# F( 3, [ 4, 6, 8 ], true)  => [ 12, 18, 24 ]
#
# F( 4, [ 7, 9, 13 ], false) => [ 11, 13, 17 ]
#
# Na entrevista passaremos um exercício equivalente para análise em tempo real.

# funcao que recbe tres parametros: um numero, um array de numeros e um booleano

# def multiplica_ou_soma(numero, array_numeros, booleano):
#     if booleano:
#         return [numero * index for index in array_numeros]
#     else:
#         return [numero + index for index in array_numeros]

def multiplica(numero, array, boolean):
    novoarray = []
    if boolean:

        for item in array:
            conta = numero * item
            novoarray.append(conta)
        return novoarray
    else:
        for item in array:
            conta = numero + item
            novoarray.append(conta)
        return novoarray

print(multiplica(10, [9, 18, 2], False))


