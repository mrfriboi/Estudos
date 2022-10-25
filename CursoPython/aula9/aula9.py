# <, ==, !=, >, >=, <=  Operadores relacionais
# len(obj) Retorna o tamanho de um objeto

usuario = input("Digite seu usuario (minimo 6 caracteres): ")
usuarioLength = len(usuario)

if usuarioLength < 6:
    print("Usuario muito curto")
else:
    print("Logado")