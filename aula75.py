"""
dicionários em python (dict)
dicionários são estruturas de dados do tipo
par de 'chave' e 'valor'.
Chaves podem ser consideradas como o 'índice'
que vimos na lista, e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos {} ou a classe dict para criar dicionários.

Imutáveis: str, int, float, bool, tuple
Mutável: dict, list

"""
pessoa = {
    'nome': 'João Pedro',
    'sobrenome' : 'Alencar',
    'idade': 21,
    'altura': 1.68,
    'enderecos' : [
        {'rua' : 'tal tal', 'numero' : 123},
        {'rua' : 'tal tal', 'numero' : 123},
    ],
    }
# pessoa = dict(nome='João', sobrenome='Alencar')
# print(pessoa, type(pessoa))
print(pessoa['enderecos'])

for chave in pessoa:
    print(f'{chave} : {pessoa[chave]}')
