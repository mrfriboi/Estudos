# contador acumulador

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1

else:  # executa quando o loop termina, se der ruim no loop, não executa
    print("Fim")
    
