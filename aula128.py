# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = ? também muda o valor do atributo

    def get_nascimento(self):
        return Pessoa.ano_atual - self.idade
        
dados = {'nome': 'Joao', 'idade': 22}
p1 = Pessoa(**dados)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Joasd'

# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# del p1.__dict__['outra']
# print(p1.__dict__)
print(vars(p1))
