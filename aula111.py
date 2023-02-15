alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
from itertools import groupby

# alunos = ['a','a','a','a','a','a','a','a','a', 'b', 'c']
# valores precisam estar ordenados

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)

# for aluno in alunos_agrupados:
#     print(aluno)

# print()

grupos = groupby(alunos_agrupados, key=ordena)
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
