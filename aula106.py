# ordem dos decoradores:
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def new_function(*args, **kwargs):
            res = func(*args, **kwargs)
            res_final = f'{res} {nome}'
            return res_final
        return new_function
    return decorador

# a ordem, é de baixo pra cima
@parametros_decorador(nome='terceiro')
@parametros_decorador(nome='segundo')
@parametros_decorador(nome='primeiro')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
