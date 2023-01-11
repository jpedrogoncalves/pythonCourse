# Desempacotamento em chamadas de métodos e funções
string = 'ABCD'
lista = ['Camila', 'João', 1, 2, 3, 'Laura']
tupla = 'python', 'é', 'legal'
salas = [
    ['Maria', 'Helena'],
    ['Camila',],
    ['João', 'Pedro', 'Laura', (0, 10, 20, 30, 40)],
]


# a,b, *_, c= lista

# print(a, c)

# for nome in lista:
#     print(nome, end=' ')

# print()
# print(*lista)
# print()
# print(*string, sep='-')
print(*salas, sep='\n') # desempacotamento na chamada de funções, em *salas
