# continue, break, else no for
for i in range(10):
    if i == 2:
        print('i é igual a 2...')
        continue
    
    if i == 8:
        print('i é igual a 8 XO')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('For executado com sucesso.')
