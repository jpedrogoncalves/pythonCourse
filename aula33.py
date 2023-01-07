# continue!
contador = 0

while contador < 100:
    contador += 1

    if contador % 2 == 0:
        continue
    print(f'Números Ímpares: {contador}')


print('is over!')
