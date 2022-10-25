# Exercise

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

ano_atual = int(2022)
nascimento = ano_atual - idade

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

print(f"Seu nome é: {nome}, tem {altura}m de altura e {peso}kg.")
print(f"{nome }nasceu em {nascimento} e tem {idade} anos")
print(f"{nome}, seu IMC é: {imc:.2f}")
print(resposta_imc)
