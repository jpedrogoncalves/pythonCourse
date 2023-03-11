# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#   
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)
class A:
    ...
    def who_i(self):
        print('A')

class B(A):
    ...
    # def who_i(self):
    #     print('B')
class C(A):
    ...
    def who_i(self):
        print('C')
# a ordem importa! (geralmente a primeira classe tem chances de dar certo)
class D(B,C):
    ...
    # def who_i(self):
    #     print('D')

d = D()
d.who_i()
print(D.mro())
print(D.__mro__)
# MRO: D -> B -> C -> A -> object
