from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_janelaPrincipal as Ui_MainWindow
from model.Pessoa import Funcionario

class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        self.tela.botaoEntrar.clicked.connect(self.exibirConteudo)
        
    def exibirConteudo(self):
        login = self.tela.entradaNome.toPlainText()
        senha = self.tela.entradaSenha.toPlainText()
        funcionarios = Funcionario().listarTodosOsFuncionarios()
        print(funcionarios)        
        self.tela.labelErro.setText("logado!")
