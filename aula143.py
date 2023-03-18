# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.
from abc import ABC, abstractmethod

class Log(ABC):
    # isso transforma Log em uma classe 100% abstrata
    # ou seja, não pode ser usada diretamente.
    # para usar a abc, temos que fazer outra classe herdá-la
    @abstractmethod
    # DEVEMOS manter a assinatura do método IGUAL!
    def _log(self, msg): ...    
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    # o método abstrato DEVE ser implementado em toda classe que herdar
    # da abc (Log, nesse caso)
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_error('oi!')
