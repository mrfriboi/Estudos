# desempacotando listas

lista = ['Luiz', 'Maria', 'João', 4,4,4,4,45,5,5,4,4,4]

#n1, n2, n3 = lista

n3, n4, *outra_liata, ultimo_valor = lista # * poe tudo q sobrou/ coloca o ultumo valor na ultima variavel

print(n3, n4, outra_liata, ultimo_valor)

