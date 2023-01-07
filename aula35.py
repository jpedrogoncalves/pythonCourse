string = 'Camila Martins'
string_len = len(string)
nova_string = ''
contador = 0

while contador < string_len:
    letra = string[contador]
    nova_string += f'*{letra}'
    contador += 1
nova_string += '*'
print(nova_string)