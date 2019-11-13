from model.dao import DAO

class Pessoa(object):
    def __init__(self, nome):
        self.__nome = ""
        if nome is not None:
            self.nome = nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

class Funcionario(Pessoa):
    def __init__(self, nome = None, senha = None , nivelDeAcesso = None):
        super().__init__(nome)
        self.__nivelDeAcesso = 0
        self.__senha = 0
        if senha is not None and nivelDeAcesso is not None:
            self.nivelDeAcesso = nivelDeAcesso
            self.senha = senha
        
    @property
    def nivelDeAcesso(self):
        return self.__nivelDeAcesso 
    @nivelDeAcesso.setter
    def nivelDeAcesso(self, nivelDeAcesso):
        self.__nivelDeAcesso = nivelDeAcesso
    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def listarTodosOsFuncionarios(self):
        funcionarios = DAO.listarTodos("Funcionario")
        return funcionarios
    def buscarFuncionario(self):
        pass
class Cliente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

