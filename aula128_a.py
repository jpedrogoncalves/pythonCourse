# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 22)
p2 = Pessoa('Camila', 23)
p3 = Pessoa('Laura', 10)
dados = [vars(p1), vars(p2), vars(p3)]
# print(dados)

caminho_arquivo = 'aula128_a.json'

# pro dump ser feito somente nesse arquivo

def fazer_dump():
    with open(caminho_arquivo, 'w', encoding='utf8') as file:
        print('fazendo dump')
        json.dump(dados, file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    fazer_dump()
