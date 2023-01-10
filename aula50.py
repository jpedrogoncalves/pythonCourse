# tuplas - tuple - lista imutável 
# mais rápido que listas
nomes = 'João', 'Laura', 'Camila'
tupla = ('valor1', 'valor2', 'valor3')
lista = [1,2,3,4]
lista_tupla = tuple(lista)
# nomes[1] = 'Zé' # iria dar erro, pq a tupla é imutável (TypeError)
print(nomes, type(nomes))
print(tupla)
print(lista_tupla)
