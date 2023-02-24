import os
# criando arquivos com python
# usamos a função open para abrir
# um arquivo python (ele pode ou não existir)
# modos:
# r (read), w (write), x (create)
# a (escreve no final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context Manager - with (abre e fecha)
# métodos úteis:
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# vamos falar sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# vamos falar sobre o módulo json, mas:
# json.dump = gera um arquivo json
# json.load
# sempre que for usar o read, readline/s mover o cursor (seek para o início do arquivo)

# ao usar caminhos com diretórios, trocar '\' por '\\'
# caminho_arquivo = 'E:\\code\\pythonCourse\\'
# caminho_arquivo += 'aula117.txt'
caminho_arquivo = 'aula117.txt'

# arquivo = open(caminho_arquivo, 'w')
# ...
# arquivo.close()
# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0,0)
#     # sem o seek não dá certo, pois o cursor está no final do arquivo
#     print(arquivo.read())

# print('-' * 30)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:
    arquivo.write('1\n')
    arquivo.write('2\n')
    arquivo.write('3\n')
    arquivo.write('atenção\n')

# os.remove(caminho_arquivo)
os.rename(caminho_arquivo, 'aula117_rename.txt')
caminho_arquivo = 'aula117_rename.txt'
os.rename(caminho_arquivo, 'aula117.txt')
