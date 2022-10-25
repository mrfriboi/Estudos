# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, True, 'Lucas Rodrigues']  # lista
# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#
# print(lista[5])
#
# lista[5] = 'Qualquer coisa'
#
# print(lista[5])
#
# print(lista[0:3]) # vai do 0 ao 3, não incluindo o 3
#
# print(lista[:3]) # vai do 0 ao 3, não incluindo o 3
#
# print(lista[3:]) # vai do 3 ao final
#
# print(lista[-1]) # ultimo elemento
#
# print(lista[::2]) # vai do 0 ao final, pulando de 2 em 2
#
# print(lista[::-1]) # vai do final ao 0, pulando de -1 em -1

l1 = [1, 2, 3]
#l1.extend(l2) # adiciona a lista l2 a lista l1
l1.extend('a') # adiciona a string 'a' a lista l1

# l2 = [4, 5, 6]
# print(l2)
# # l2.append('b') # adiciona o elemento 'b' a lista l2
# l2.insert(0, 'c') # adiciona o elemento 'c' na posição 0 da lista l2
# l2.pop(-1) # remove o ultimo elemento da lista l2
#
# l3 = l1 + l2
#
# print(l1)
# print(l2)
# print(l3)

# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l2)
# del (l2[3:5]) # remove os elementos da posição 3 a 5
# print(l2)
# l2.insert(0, 'Banana') # adiciona o elemento 'Banana' na posição 0 da lista l2
# print(l2)
# del (l2[0]) # remove o elemento da posição 0 da lista l2
# print(l2)
# print(max(l2))
# print(min(l2))
#
# l3 = list(range(1, 10)) # cria uma lista de 1 a 9
# print(l3)
#
# soma = 0
# for valor in l3: # percorre a lista l3
#     soma = soma + valor
#     print(f'{soma} + {valor} = {soma}')
#
# print(soma)

# l2 = ['string' , True , 10 , -20.5]
#
# for elem in l2:
#     print(f'{elem} é do tipo {type(elem)}')

# -----------------JOGO DA FORCA-------------------
secreto = 'perfume'
digitadas = []
chance = 10

while True:

    if chance > 0:
        print(f'Você tem {chance} chances')
    else:
        print('Game Over')
        break

    letra = input('Digite uma letra: ').lower()

    if len(letra) > 1: # se o usuário digitou mais de uma letra
        print('Digite apenas uma letra')
        continue # volta para o inicio do loop

    secreto_temporario = ''

    if letra in digitadas:
        print('vc já acertou essa letra')
        continue

    digitadas.append(letra)
    print(digitadas)

    if letra in secreto:

        print(f'Acertou a letra "{letra}"')

    else:
        print(f'Errou, nao tem a letra "{letra}"')
        digitadas.pop() # remove o ultimo elemento da lista digitadas
        chance -= 1

    for letra_secreta in secreto: # percorre a string secreto

        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta

        else:
            secreto_temporario += '*'

    print(secreto_temporario)

    if secreto_temporario == secreto: # verificar se acertou tudo
        print('Você ganhou!')
        break