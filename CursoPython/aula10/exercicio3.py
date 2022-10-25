nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print(f"Seu nome {nome} é curto")

elif tamanho_nome <= 6:
    print(f"Seu nome {nome} é normal")
else:
    print(f"Seu nome {nome} é longo")