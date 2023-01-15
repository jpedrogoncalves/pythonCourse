# retorno de valores das funções (return)
def soma(x,y):
    if x > 10:
        return 11, 20
    return x + y # indica pro python que a função acabou

soma1 = soma(2,2)
soma2 = soma(3,3)

# se não usar return, dá TypeError, pois a função retorna None
print(soma1 + soma2)
print(soma(11, 33))
