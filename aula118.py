# JSON
# https://www.youtube.com/watch?v=XmCrArtfjaQ
# JSON - JavaScript Object Notation
# lembra um dicionário do python
# salvar ou transportar dados
# aceita 6 tipos de dados:
# - boolean
# - int/float
# - null
# - strings
# - array
# - objetos (mais de um valor)
import json

# pessoa = {
#     'nome' : 'João',
#     'sobrenome' : 'Pedro',
#     'sobrenome' : [
#         {'rua 1' : 'R1', 'numero' : 32},
#         {'rua 2' : 'R2', 'numero' : 33},
#     ],
#     'altura' : 1.67,
#     'numeros_preferidos' : (6, 9),
#     'dev' : True,
#     'nada' : None
# }

# with open('aula118.json', 'w', encoding='utf-8') as json_file:
#     # dump x dumps
#     # dump - salva no arquivo
#     # dumps - salva numa string
    
#     # para não "traduzir" os acentos para tabela ascii.
#     # não recomendado por questões de compatibilidade
#     # json.dump(pessoa, json_file, ensure_ascii=False)
    
#     json.dump(pessoa, json_file, indent=2)

# convertendo do arquivo pro python
with open('aula118.json', 'r', encoding='utf8') as json_file:
    pessoa = json.load(json_file)
    print(type(pessoa))
