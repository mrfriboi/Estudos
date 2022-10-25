# repetiçào while

# while True:  # loop infinito
#     nome = input("Digite seu nome: ")
#     print(f"Olá {nome}")

# x = 0
#
# while x < 10:
#
#     if x == 3:
#         x += 1
#         #continue
#         break # sai do loop
#     print(x)
#     x += 1
#
#
# print("Fim")


#  ----------------------------------------------------------------------------------------------------------------------

# x = 0
# while x < 10:
#     y = 0
#     while y < 5:
#         print(f" X vale ({x}) e Y vale ({y}) ")
#         y += 1
#
#     x += 1
# print("Fim")

#  ----------------------------------------------------------------------------------------------------------------------

while True:
    print()
    num1= input("Digite um numero: ")
    num2= input("Digite outro numero: ")
    operador = input("Digite um operador: ")  # +, -, *, /
    sair = input("Digite S para sair ou N para continuar: ").upper()

    if sair == "S":
        break


    if not num1.isdigit() or not num2.isdigit():  # se não for inteiro
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operador == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operador == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operador == "/":
        print(f"{num1} / {num2} = {num1 / num2}")


    else:
        print("Operador invalido")
