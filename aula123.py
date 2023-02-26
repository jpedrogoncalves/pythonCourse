# class - Classes são moldes para criar novos objetos
# as classes geram novos objetos (instâncias) que 
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de 
# classes.
# string = 'João' # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('João', 'Pedro')
# p1.nome='João'
# p1.sobrenome='Pedro'

print(p1.nome)
print(p1.sobrenome)
