# exercícios com funções

# crie uma função que multiplique todos os argumentos
# não nomeados recebidos
# retorne o total para uma variável e mostre o valor
# da variável

# crie uma função que fala se um número é par ou ímpar
# retorne se o número é par ou ímpar

# def multiplication(*args):
#     total = 1
#     for i in args:
#         total *= i
#     return total

# numbers = 1, 2, 3, 4, 5
# m = multiplication(*numbers)
# print(m)

def number(number):
    if number % 2 == 0:
        return f'O número: {number} é par'
    return f'O número: {number} é ímpar'

numbers = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for i in numbers:
    a = number(i)
    print(a)
