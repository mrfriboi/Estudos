import math

string = ['01234567890123456789012345678901234567890123456789']
string_vazia = []

print(math.ceil(len(string[0]) / 10))

retorno = [string[0][i:i+10] for i in range(0, len(string[0]), 10)]
retorno = '.'.join(retorno)
print(retorno)

# bot para notificar palavra em site