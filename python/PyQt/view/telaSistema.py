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
        self.EntradaNome = QtWidgets.QPlainTextEdit(self.login)
        self.EntradaNome.setGeometry(QtCore.QRect(80, 60, 691, 61))
        self.EntradaNome.setObjectName("EntradaNome")
        self.botaoEntrar = QtWidgets.QPushButton(self.login)
        self.botaoEntrar.setGeometry(QtCore.QRect(590, 150, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.botaoEntrar.setFont(font)
        self.botaoEntrar.setObjectName("botaoEntrar")
        self.labelErro = QtWidgets.QLabel(self.login)
        self.labelErro.setGeometry(QtCore.QRect(140, 320, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelErro.setFont(font)
        self.labelErro.setObjectName("labelErro")
        janelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaPrincipal)

    def retranslateUi(self, janelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        janelaPrincipal.setWindowTitle(_translate("janelaPrincipal", "Sistema De Debitos"))
        self.botaoEntrar.setText(_translate("janelaPrincipal", "Entrar"))
        self.labelErro.setText(_translate("janelaPrincipal", "teste"))



