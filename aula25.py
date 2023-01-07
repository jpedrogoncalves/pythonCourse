"""
Exercício:
    Peça ao usuário para digitar seu nome;
    Peça ao usuário para digitar sua idade;
    Se o nome e idade forem digitados:
        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Se nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        Exiba:
            "Desculpe, você deixou campos vazios"
"""
user_name_input = input('Insira seu nome: ')
user_age_input = input('Insira sua idade: ')

if user_name_input and user_age_input:
    reverse_name = user_name_input[::-1]
    spaces = ' ' in user_name_input
    name_len = len(user_name_input)
    print(f'Seu nome é: {user_name_input}')
    print(f'Seu nome invertido é: {reverse_name}')
    
    if spaces:
        print(f'"{user_name_input}" contém espaços')
    else:
        print(f'"{user_name_input}" NÃO contém espaços')
        
    print(f'Seu nome contém {name_len} letras.')
    print(f'A primeira letra do seu nome é: {user_name_input[0]}')
    print(f'A última letra do seu nome é: {user_name_input[name_len-1:name_len]}')
else:
    print("Desculpe, você deixou campos vazios")
