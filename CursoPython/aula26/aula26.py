# DESAFIO CPG VALIDADOR

"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""


cpf = input('Digite seu cpf: ')

cpf_limpo = (cpf[:-2].replace('.', '').replace('-', ''))

cpf_para_comparar = ((cpf.replace('.', '').replace('-', '')))

indice = 10

soma = 0

soma2 = 0

indice2 = 11

c = 0

# for i maior que 19

#print(cpf_limpo)

for i in range(19):

    if i < 9:
        multi = int(cpf_limpo[i]) * indice
        soma = multi + soma
        #print(f' aqui {cpf_limpo[i]} * {indice}')
        indice -= 1

    if i == 9:
        modulo = 11 - (soma % 11)

        if modulo > 9:
            cpf_limpo += '0'
        else:
            print('cpf invaldio')
            continue

    if i >= 9:


        multi2 = int(cpf_limpo[c]) * indice2

        soma2 = multi2 + soma2

        #print(f'{cpf_limpo[c]} * {indice2}')

        indice2 -= 1

        c += 1

       # print(soma2)
        if indice2 == 1:
            modulo2 = 11 - (soma2 % 11)
            cpf_limpo += str(modulo2)
            print(f'CPF {cpf_limpo}')


    if cpf_limpo == cpf_para_comparar:
        print(f'CPF valido: {cpf}')



###########FORMA DO PROFESSOR#############

# # Loop infinito
# while True:
#     # cpf = '16899535009'
#     cpf = input('Digite um CPF: ')
#     novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
#     reverso = 10                        # Contador reverso
#     total = 0
#
#     # Loop do CPF
#     for index in range(19):
#         if index > 8:                   # Primeiro índice vai de 0 a 9,
#             index -= 9                  # São os 9 primeiros digitos do CPF
#
#         total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação
#
#         reverso -= 1                    # Decrementa o contador reverso
#         if reverso < 2:
#             reverso = 11
#             d = 11 - (total % 11)
#
#             if d > 9:                   # Se o digito for > que 9 o valor é 0
#                 d = 0
#             total = 0                   # Zera o total
#             novo_cpf += str(d)          # Concatena o digito gerado no novo cpf
#
#     # Evita sequencias. Ex.: 11111111111, 00000000000...
#     sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
#
#     # Descobri que sequências avaliavam como verdadeiro, então também
#     # adicionei essa checagem aqui
#     if cpf == novo_cpf and not sequencia:
#         print('Válido')
#     else:
#         print('Inválido')