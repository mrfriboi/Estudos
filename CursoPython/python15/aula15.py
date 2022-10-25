# lendo string com while

frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
nova_string = ''

print(frase)
input_do_usuario = (input('Qual letra quer por maiuscula: ')).lower()

#iteração <- iterar
while contador < tamanho:
    letra = frase[contador]
    if letra == input_do_usuario:
         nova_string += input_do_usuario.upper()
    else:
        nova_string += letra

    contador += 1


#    print(frase[contador], contador)
 #   nova_string += frase[contador]

  #  print(nova_string)

print(nova_string)


