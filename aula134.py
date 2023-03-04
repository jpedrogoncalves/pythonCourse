# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções:
#   (sem underline) = public
#       pode ser usado em qualquer lugar
#_  (um underline) = protected
#       não deve ser usado fora da classe
#       ou suas subclasses, mas pode ser usado
#       em qualquer lugar do código, inclusive em métodos públicos.
#__ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python:
#           _ClassName__attr_name or _ClassName__methodname
#       só deve ser usado na classe em que foi declarado
from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'protegido'
        self.__private = 'PRIVADO!'

        self._metodo_protected()

    def metodo_publico(self):
        # self._metodo_protected()
        print(self.__private)
        self.__metodo_private()
        return 'metodo publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        return '__metodo_private'

f = Foo()
# print(f.public)
# print(f.metodo_publico())
# print(f._protected)
# print(f._metodo_protected())

# gera um erro, para que não possa ser acessado fora da classe
print(f.__metodo_private())
# para ser acessado fora da classe, é necessário fazer da seguinte forma:
# print(f._Foo__metodo_private())
