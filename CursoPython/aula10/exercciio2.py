hora = input("Digite a hora: ")

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:

        print("Hora deve estar entre 0 e 23")

    else:
        if hora >= 0 and hora <= 11:
            print("Boa dia")
        elif hora >= 12 and hora <= 17:
            print("Boa tarde")
        elif hora >= 19 and hora <= 23:
            print("Boa noite")
else:
    print("Hora invalida")