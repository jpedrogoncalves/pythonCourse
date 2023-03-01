# method v. @classmethod v. @staticmethod
# method = self, método de instância;
# @classmethod = cls, método de classe
# @staticmethod = método de classe (❌self, ❌cls)

class Connection:
    # método de instância
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter = configura o valor de um atributo
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y

# c1 = Connection()
c1 = Connection.create_with_auth('joao', '123')
# c1.set_user('João')
# c1.set_password(123)
print(c1.user)
print(c1.password)
print(Connection.soma(2,3))
