def saudacao(saudacao, nome):
    print(f'{saudacao}, {nome}')

saudacao('OI', 'Paulo')

def soma(n1, n2, n3):
    return n1 + n2 + n3
print(soma(1, 2, 3))

def somador(n1, porcetagem):
    return (n1 * (porcetagem/100)) + n1
print(somador(50, 100))

def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n
print(fizzBuzz(15))