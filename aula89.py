# isinstance
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'joao'}]

for item in lista:
    if isinstance(item, set):
        item.add(5)        
        print(item)
    if isinstance(item, str):
        print(item.upper())
