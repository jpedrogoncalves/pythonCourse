# Funções decoradoras e decoradores com classes
def adiciona_repr(cls):
# ? meu_repr() recebe self, pra poder funcionar como se estivesse dentro da
# ? classe.
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls    

# * class Time(SuperTime, MyReprMixin): = herança
# ? composição é mais recomendado que herança, e é preferível usar. (abaixo)

# * decoradores
@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

# * class Planeta(MyReprMixin): = herança
# ? composição é mais recomendado que herança, e é preferível usar. (abaixo)

# * decoradores
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

# ! funciona, mas não é preferível usar pois fica muito distante da definição da função
# ! então usamos Syntax Sugar

# Time = adiciona_repr(Time)

brasil = Time('Brasil')
eua = Time('E.U.A.')

# Planeta = adiciona_repr(Planeta)

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(eua)
print(terra)
print(marte)
