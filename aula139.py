# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# herança: (nome_da_super_classe)
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def print_nome_classe(self):
        print(self.nome,self.sobrenome,self.__class__.__name__)
    
class Cliente(Pessoa):
    def print_nome_classe(self):
        print('esse método vai ser executado 1º')


class Aluno(Pessoa):
    ...

# MRO = Method Resolution Order
# sequência em que os métodos são procurados
# nesse caso: Cliente, Pessoa, bultins.object
# quando ele encontra o método, ele já executa e nem checa
# nas outras classes

c1 = Cliente('João', 'Pedro')
a1 = Aluno('Camila', 'Martins')
c1.print_nome_classe()
a1.print_nome_classe()

# help(Cliente)
