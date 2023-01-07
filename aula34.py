# whiles aninhados
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
#   coluna é declarado dentro do while, pois se fosse declarado fora, não ia ser executado da forma esperada
    coluna = 1 
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    
    linha += 1

print('Acabou')
