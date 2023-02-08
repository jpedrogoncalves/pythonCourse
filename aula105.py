# decoradores com parâmetros
# essa função retorna a fábrica de funções

# decorators_factory tem a função de pegar os parametros do decorador
# functions_factory tem a função de pegar a função que vai executar
# aninhada é a função que vai ser executada

def decorators_factory(a=None, b=None, c=None):
    def functions_factory(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            # 'print('Aninhada')' só é exibido, quando soma (aninhada) é executada!
            print(f'Parâmetros do decorador: {a=}, {b=}, {c=}')
            print('Aninhada')
            res = func(*args, **kwargs)
            # decoração pode alterar o resultado
            return res
        # aninhada = soma
        return aninhada
    return functions_factory


# nesse momento, o python já executa a função decoradora
# -> terminal: Decoradora 1
# @functions_factory
# soma é passada para func de decoradora
@decorators_factory(1,2,3)
def soma(x, y):
    return x + y

# multiplica = decorators_factory(lambda x, y: x * y)
multiplica = decorators_factory(1, 2, 3)(lambda x, y: x * y)

dez_vezes_cinco = multiplica(10, 5)
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
