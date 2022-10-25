def saudacao(msg='Olá', nome='Mundo'): # msg e nome são parametros padrão
    print(msg)
    print(nome)

saudacao('OI', 'Paulo')
saudacao('OI')



def divisao(n1, n2):
    if n2 == 0:
        return 'Não é possível dividir por 0'

    return n1 / n2

dividir = divisao(10, 60)

if dividir:
    print(dividir)
else:
    print("não é possivel dividir por 0")

