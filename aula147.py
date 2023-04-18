# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f'({self.x}, {self.y})'

    def __repr__(self):
        class_name = type(self).__name__
        # class_name = self.__class__.__name__ => mesma coisa

        # representação do objeto
        return f'{class_name}(x={self.x!r}, y={self.y!r})'
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Ponto(new_x, new_y)

    def __gt__(self, other):
        resultado_self = self.x + self.x
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

# * maneiras de chamar o repr
# print(repr(p1))
# print(f'{p1!r}')
# print(p2)

if __name__ == '__main__':
    p1 = Ponto(4, 2) # 6
    p2 = Ponto(6, 4) # 10
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que P2', p1 > p2)
    print('P2 é maior que P1', p2 > p1)

