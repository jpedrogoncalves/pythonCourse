# list comprehensions com mais de um for
lista = []
for x in range(10):
    for y in range(3):
        lista.append((x,y))

# o lado esquerdo do for, é para o mapeamento
lista = [(x,y) for x in range(3) for y in range(3)]
print(lista)
lista = [[(x, letra) for letra in 'klasdas'] for x in range(3)]
print(lista)
