# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes derivadas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Overload = Sobrecarga de métodos
# Override = Sobreposição de métodos
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    # se não colocarmos o tipo de dado que o método retornará
    # por padrão, o método retorna None (Type Hinting)
    @abstractmethod
    # -> bool = somente para mostrar que tipo de dado retorna
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('Email: enviando...', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando...', self.mensagem)
        return False

# dizendo que notificação é str:
# a classe Notificacao também é um tipo!
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('enviada')
    else:
        print('não enviada')

notificacao_email = NotificacaoEmail('Testando Email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)

"""
    quebramos o Princípio da substituição de liskov
    porque o método enviar() de Notificacao retorna BOOL
    mas os métodos enviar das subclasses retornam None, e 
    isso quebra a aplicação.

    para correção, basta adicionar o tipo de retorno na
    assinatura do método, e retornar algo.
"""

# n = NotificacaoEmail('testando notificação')
# n.enviar()
# n = NotificacaoSMS('testando notificação')
# n.enviar()
