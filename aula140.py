# super() é a super classe na sub classe
# Classe Principal(Pessoa):
#   -> super class, etc
# Classes filhas:
#   -> sub class, etc
# class MinhaString(str):
#     def upper(self):
#         # super() retorna temporariamente a super classe
#         # ou seja, você pode chamar métodos da super classe (no caso, str)
#         print('chamou Upper')
#         retorno = super().upper()
#         print('depois do Upper')
#         return retorno
#         # super()

# string = MinhaString('slow')
# print(string.upper())
class A:
    atr_A = 'valor A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atr_B = 'valor B'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atr_C = 'valor C'
    def metodo(self):
        super(B, self).metodo() # A
        super(C, self).metodo() # B
        print('C')

# a classe C herda os atributos da classe pai
c = C('atributo', 'Qualquer')
# print(c.atr_A)
# print(c.atr_B)
# print(c.atr_C)
print(c.atributo)
print(c.outra_coisa)
