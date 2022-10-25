num = input("Digite um numero inteiro: ")


# saber se é inteiro
if num.isdigit():
    num = int(num)
    print(f'O numero {num} é inteiro')
    if num % 2 == 0:
        print(f"O {num} é par")
    else:
        print(f"O {num} é impar")

else:
    print(f"{num} não é um numero inteiro")

