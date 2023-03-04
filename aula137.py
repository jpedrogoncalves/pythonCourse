# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        # preciso criar o endereco dentro da classe cliente
        # para que quando eu apague o cliente, todos os endereços sejam apagados
        # garbage collector
        
        # criando a instância de endereco dentro da classe Cliente
        # ou seja: quando o cliente for apagado, o endereço também é apagado
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        # só é apagado depois que o código termina
        # ou seja, mesmo depois que o cliente é apagado, tenho acesso
        # ao endereço que foi inserido externamente
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('apagando ', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('apagando ', self.rua, self.numero)

cliente1 = Cliente('maria')
cliente1.inserir_endereco('Av. Brasil', 54)
cliente1.inserir_endereco('Rua São Francisco', 238)

endereco_ext = Endereco('Av. Moura', 12312)
cliente1.inserir_endereco_externo(endereco_ext)

cliente1.listar_enderecos()

del cliente1

print(f'RUA: {endereco_ext.rua}, NÚMERO: {endereco_ext.numero}')

print('#'*50)
