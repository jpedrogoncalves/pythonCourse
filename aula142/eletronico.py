from log import LogPrintMixin, LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

# usando Herança Múltipla pra colocar algo que não é da família
# de Eletrônico dentro de Smartphone que vai adicionar uma funcionalidade
# a mais (log)
class Smartphone(Eletronico, LogFileMixin):
    # prefira composição ao invés de herança
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)
        
    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)

