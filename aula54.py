"""
split e join com list e str
split - separa uma string 
join - une uma string
    strip corta os espaços do começo e fim da string
    rstrip corta os espaços do fim da string
    lstrip corta os espaços do começo da string
"""
frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

# conteudo_separado = frase.split() # split() usa qualquer espaço em branco
# print(lista_palavras)

lista_frases_crua = frase.split(',') # split() usa qualquer espaço em branco
lista_frases = []

for i, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[i].strip())

print(lista_frases_crua)
print(lista_frases)

# separador.join(iteravel)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
