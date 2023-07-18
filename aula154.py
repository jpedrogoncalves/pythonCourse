# Classes decoradoras (Decorator Classes)
class Multiplicar:
    def __init__(self, func):
        # ? o init está recebendo uma função.
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args, **kwargs):
        # print(args, kwargs)
        result = self.func(*args, **kwargs)
        return result * self._multiplicador

# é uma classe que está decorando a soma
# ! @Multiplicar() - dessa forma muda o comportamento da classe
# ! pois está executando o __init__ da classe.
@Multiplicar
def soma(x, y):
    return x + y

# * os argumentos passados em __call__ são da função soma
dmd = soma(2, 2)
print(dmd)
