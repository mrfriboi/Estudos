# Variaveis

# nome = "Lucas Rodrigues"
# idade = 23
# altura = 1.80
# e_maior = idade > 18
#
# print("Nome:", nome)
# print("Idade:", idade)
# print("Altura:", altura)
# print("É maior de idade?", e_maior)
from turtledemo.chaos import f

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)

imc_duas_casa_decimais = round(imc, 2)

if imc < 18.5:
    resposta_imc = (f"{nome} você está abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    resposta_imc = (f"{nome} você está no peso ideal")
elif imc >= 25 and imc <= 30:
    resposta_imc = (f"{nome} você está com sobrepeso")


print(f"Seu nome é: {nome}, e você tem, {idade} anos e seu IMC é: {imc:.2f}")
print(resposta_imc)