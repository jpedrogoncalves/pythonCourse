"""
Flag - marcar um local
none = não valor
is e is not
id = identidade
"""

# id
# v1 = 'a'
# print(id(v1))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça')
else:
    print('não faça')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')
