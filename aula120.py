# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# comandos: listar, desfazer, refazer, clear, encerrar
import os

user_input = ''
todo = []
desfazer = []

while True:
    print('Comandos: listar(l), desfazer(d), refazer(r), limpar(c), encerrar(e)')
    user_input = input('Digite uma tarefa ou comando: ')

    if user_input == 'l':
        if todo == []:
            print('Nada a listar!')
        else:
            print('Suas tarefas: ', todo)
    
    if user_input == 'd':
        if todo == []:
            print('Nada a desfazer!')
        else:
            last_value = todo[-1]
            last_index = todo.index(last_value)
            desfazer.append(todo[last_index])
            todo.remove(last_value)
            print('Desfeito!')
            print()

    if user_input == 'r':
        if desfazer == []:
            print('Nada a refazer!')
        else:
            last_value = desfazer[-1]
            last_index = desfazer.index(last_value)
            todo.append(desfazer[last_index])
            desfazer.remove(last_value)
            print(todo)
            print(desfazer)
            print()
    
    if user_input == 'c':
        os.system('cls')

    if user_input == 'e':
        print('Encerrando...')
        break
    
    if user_input != 'l' and user_input != 'd' and user_input != 'r' and user_input != 'c' and user_input != 'e':
        todo.append(user_input)
    else:
        continue
