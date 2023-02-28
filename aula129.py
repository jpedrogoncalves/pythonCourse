# métodos de classe + factories
# são métodos onde 'self' será 'cls' ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    # o decorator abaixo que 'transforma' o método abaixo
    # em um método de classe.
    # cls = classe
    # não temos acesso à instância dentro dos classmethod

    # gerando novas instâncias a partir do classmethod

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

    # uso do classmethod
    # 
    
p1 = Pessoa('João', 22)
p2 = Pessoa.criar_com_50_anos('João')
p3 = Pessoa('Anonima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()
