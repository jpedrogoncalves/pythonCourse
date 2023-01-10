# iteráveis dentro de iteráveis
salas = [
    ['Maria', 'Helena'],
    ['Camila',],
    ['João', 'Pedro', 'Laura', (0, 10, 20, 30, 40)],
]

print(salas[0][1])
print(salas[1][0])
print(salas[2][2])
print(salas[2][3][2]) # 20
