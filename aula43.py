"""
Faça um jogo para o usuário adivinhar a palavra secreta.
    -Você vai propor uma palavra secreta qualquer, e vai 
    dar a possibilidade para o usuário digitar apenas uma letra.
    -Quando o usuário digitar uma letra, você vai conferir se
    a letra digitada está na palavra secreta.
        -se a letra digitada estiver na palavra secreta, exiba a letra
        -se a letra digitada não estiver na palavra secreta, exiba *

Faça a contagem de tentativas do usuário.
"""
import os

secret_word = 'perfume'
formated_word = ''
user_letter_input = ''
try_count = 0
condition = True
right_letters = ''

while condition:
    user_letter_input = input('Digite uma letra: ')
    try_count += 1

    if len(user_letter_input) > 1:
        print('Apenas uma letra por vez!')
        try_count += 1
        print(f'{try_count} tentativas já realizadas!')
        continue

    if user_letter_input in secret_word:
        right_letters += user_letter_input

    word = ''
    for secret_letter in secret_word:
        if secret_letter in right_letters:
            word += secret_letter
        else:
            word += '*'

    print(word)

    if word == secret_word:
        os.system('cls')
        break

    print(f'{try_count} tentativas já realizadas!')

print(f'A palavra secreta era: {secret_word}, e você usou {try_count} tentativas.')