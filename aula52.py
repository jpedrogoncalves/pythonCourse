"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
lista = []
option = ''
import os

while True:
    option = input('[i]nserir / [a]pagar / [l]istar / 0 - Encerrar: ').lower()

    if option == 'i':        
        user_input_list = input('Insira o produto a ser inserido: ')
        if user_input_list != "":
            os.system('cls')
            lista.append(user_input_list)
            print(lista)
        else:
            print('Por favor, insira um valor válido!')        
    elif option == 'a':        
        for index, name in enumerate(lista):
                print(index, name)
                
        user_errase_list = input('Insira o produto que você deseja apagar da lista: ')

        if user_errase_list in lista:            
            for index, name in enumerate(lista):
                if user_errase_list == name:
                    lista.pop(index)
                    print(lista)
        else:
            print('O índice não existe na lista!')
    elif option == 'l':
        if lista == []:
            print('Nada para listar')
        else:
            os.system('cls')
            for index, name in enumerate(lista):
                print(index, name)
    elif option == '0':
        print('Encerrando...')
        break
    else:
        print('Opção inválida. Insira novamente...')
        continue
