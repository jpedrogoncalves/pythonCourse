# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# * __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# * object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        # ? print('antes de criar a instância')
        # * se new não retornar nada, o python nem vai tentar chamar o 
        # * init, porque ele nem existe
        instancia =  super().__new__(cls)
        # ? print('depois')
        # ? instancia.x = 213
        return instancia

    def __init__(self, x):
        self.x = x
        print('init')

    def __repr__(self):
        return 'A()'
    
a = A()
# * o que o python está fazendo:
# a = object.__new__(A)
# a.__init__()

# * para resolver o AttributeError, utilizamos o match 
# * na assinatura do método, com a própria quantidade de 
# * argumentos, ou, usamos args e kwargs na assinatura
# * de __new__
print(a.x)
