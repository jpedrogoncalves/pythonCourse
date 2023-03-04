# @property - um getter
# getter - um método para obter um atributo
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo 🤯🤯🤯
# geralmente é usada nas seguintes situações:
#   -como getter
#   -p/ evitar quebrar código cliente
#   -p/ habilitar setter
#   -p/ executar ações ao obter um atributo
# código cliente: é o código que usa seu código
 
# class Caneta:
#     def __init__(self, cor):
#         # private, protected, public
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR:')
#         return self.cor_tinta

# # código cliente:
# caneta = Caneta('Azul')
# print(caneta.get_cor())

class Caneta:
    def __init__(self, cor):
        # private, protected, public
        self.cor_tinta = cor
    
    # método que se comporta como atributo
    @property
    def cor(self):
        print('property:')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123123

# código cliente:
caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)
