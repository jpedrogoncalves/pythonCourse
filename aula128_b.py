# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
from aula128_a import Pessoa

file_path = 'aula128_a.json'
with open(file_path, 'r', encoding='utf8') as json_file:
    pessoas = json.load(json_file)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

print(p1.nome)
print(p1.idade)

print(p2.nome)
print(p2.idade)

print(p3.nome)
print(p3.idade)
