class usuarios(object):
    def __init__(self, login, passworld):
        self.usuario = {
            'login': login,
            'senha': passworld,
        }
        self.lista = [self.usuario]
