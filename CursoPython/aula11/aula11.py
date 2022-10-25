# formatando valores com modificadores de formatação
# :s -> string
# :d -> inteiro
# :f -> float
# :.2f -> float com 2 casas decimais
#:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

# > - ESQUERDA
# < - DIREITA
# ^ - CENTRO

num1 = 1
num2 = 20
divisao = num1 / num2

print(f"{divisao:.2f}")
print("{:.2f}".format(divisao))

print(f"{num1:0>10}")  # 000000001

num3 = 1150
print(f"{num3:0<10}")  # 1150000000
print(f"{num3:.2f}")  # 1150.00 virou float


num4 = 1929
print(f"{num4:^10}")  # '   1929   '

nome = "Lucas Rodrigues"
total = 50-len(nome)
print(total)
print(f'{nome:#^{total}}')  # ##########Lucas Rodrigues##########
print(nome.ljust(20, '#'))  # Lucas Rodrigues#####
print(nome.lower())  # lucas rodrigues
print(nome.upper())  # LUCAS RODRIGUES
print(nome.title())  # Lucas Rodrigues


