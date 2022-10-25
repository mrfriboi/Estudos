# isdigit, isnumeic, isdecimal -> checam se pode ser convertido

num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(f'A soma de {num1} + {num2} é {num1 + num2}')
else:
    print("Não é um numero")

