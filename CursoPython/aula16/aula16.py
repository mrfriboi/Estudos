#  For in
#  For in é um loop que percorre um iterável
# range(start, stop, step)

# texto = "Python"
#
# for letra in texto:
#     print(letra)


# for n in range(10):
#     print(n)
#

# for n in range(20, 10, -1):
#     print(n)

# for n in range(100):
#     if n % 8 == 0:
#         print(n)
#
texto = "Python"
nova_string = ""
# continue -> pula para o próximo loop
# break -> para o loop
for letra in texto:
    if letra == "t":
        #continue
        nova_string += letra.upper()
    elif letra == "h":
        nova_string += letra.upper()
       # break
    else:
        nova_string += letra



print(nova_string)