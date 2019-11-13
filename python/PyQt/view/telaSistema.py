# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSistema.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        janelaPrincipal.setObjectName("janelaPrincipal")
        janelaPrincipal.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(janelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QFrame(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login.setObjectName("login")
        self.botaoEntrar = QtWidgets.QPushButton(self.login)
        self.botaoEntrar.setGeometry(QtCore.QRect(680, 180, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.botaoEntrar.setFont(font)
        self.botaoEntrar.setObjectName("botaoEntrar")
        self.labelErro = QtWidgets.QLabel(self.login)
        self.labelErro.setGeometry(QtCore.QRect(40, 280, 741, 271))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelErro.setFont(font)
        self.labelErro.setText("")
        self.labelErro.setObjectName("labelErro")
        self.entradaNome = QtWidgets.QTextEdit(self.login)
        self.entradaNome.setGeometry(QtCore.QRect(170, 20, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.entradaNome.setFont(font)
        self.entradaNome.setObjectName("entradaNome")
        self.entradaSenha = QtWidgets.QTextEdit(self.login)
        self.entradaSenha.setGeometry(QtCore.QRect(170, 100, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.entradaSenha.setFont(font)
        self.entradaSenha.setObjectName("entradaSenha")
        self.labelNome = QtWidgets.QLabel(self.login)
        self.labelNome.setGeometry(QtCore.QRect(20, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.labelSenha = QtWidgets.QLabel(self.login)
        self.labelSenha.setGeometry(QtCore.QRect(20, 100, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelSenha.setFont(font)
        self.labelSenha.setObjectName("labelSenha")
        janelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaPrincipal)

    def retranslateUi(self, janelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        janelaPrincipal.setWindowTitle(_translate("janelaPrincipal", "Sistema De Debitos"))
        self.botaoEntrar.setText(_translate("janelaPrincipal", "Entrar"))
        self.entradaNome.setHtml(_translate("janelaPrincipal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.entradaSenha.setHtml(_translate("janelaPrincipal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.labelNome.setText(_translate("janelaPrincipal", "LOGIN"))
        self.labelSenha.setText(_translate("janelaPrincipal", "SENHA"))
