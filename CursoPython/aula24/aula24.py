# operacao ternaria

logged_user = True

msg = 'Você está logado' if logged_user else 'Você não está logado'

print(msg)

idade = 19

e_de_maior = idade >= 18

msg = 'Você é maior de idade' if (e_de_maior) else "náo é de maior"

print(msg)

idade_input = input('Digite sua idade: ')

msg = 'voce digitou um numero' if (idade_input.isnumeric()) else "voce digitou algo que não é um numero"

print(msg)


