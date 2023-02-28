# atributos de classe
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = ? também muda o valor do atributo

    def get_nascimento(self):
        return Pessoa.ano_atual - self.idade
        
p1 = Pessoa('Joao', 22)
p2 = Pessoa('Maria', 25)

# está atrelado a classe, e muda para todas as instâncias.
# Pessoa.ano_atual = 2

print(Pessoa.ano_atual)
print(p1.get_nascimento())
print(p2.get_nascimento())
