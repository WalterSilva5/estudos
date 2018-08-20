/********************************************************************************
** Form generated from reading UI file 'cadastro.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CADASTRO_H
#define UI_CADASTRO_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_cadastro
{
public:
    QWidget *centralWidget;
    QPushButton *pushButton;
    QTextEdit *textEdit_2;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QPlainTextEdit *plainTextEdit;
    QMenuBar *menuBar;
    QMenu *menuCadastro;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *cadastro)
    {
        if (cadastro->objectName().isEmpty())
            cadastro->setObjectName(QStringLiteral("cadastro"));
        cadastro->resize(400, 300);
        centralWidget = new QWidget(cadastro);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(280, 200, 93, 28));
        textEdit_2 = new QTextEdit(centralWidget);
        textEdit_2->setObjectName(QStringLiteral("textEdit_2"));
        textEdit_2->setGeometry(QRect(150, 80, 201, 41));
        QFont font;
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        textEdit_2->setFont(font);
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(30, 40, 91, 31));
        label->setFont(font);
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(30, 90, 91, 31));
        label_2->setFont(font);
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(60, 150, 291, 41));
        label_3->setFont(font);
        plainTextEdit = new QPlainTextEdit(centralWidget);
        plainTextEdit->setObjectName(QStringLiteral("plainTextEdit"));
        plainTextEdit->setGeometry(QRect(150, 30, 201, 41));
        plainTextEdit->setFont(font);
        cadastro->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(cadastro);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 400, 26));
        menuCadastro = new QMenu(menuBar);
        menuCadastro->setObjectName(QStringLiteral("menuCadastro"));
        cadastro->setMenuBar(menuBar);
        mainToolBar = new QToolBar(cadastro);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        cadastro->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(cadastro);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        cadastro->setStatusBar(statusBar);

        menuBar->addAction(menuCadastro->menuAction());

        retranslateUi(cadastro);

        QMetaObject::connectSlotsByName(cadastro);
    } // setupUi

    void retranslateUi(QMainWindow *cadastro)
    {
        cadastro->setWindowTitle(QApplication::translate("cadastro", "cadastro", nullptr));
        pushButton->setText(QApplication::translate("cadastro", "cadastrar", nullptr));
        textEdit_2->setHtml(QApplication::translate("cadastro", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>", nullptr));
        label->setText(QApplication::translate("cadastro", "Login", nullptr));
        label_2->setText(QApplication::translate("cadastro", "Senha", nullptr));
        label_3->setText(QApplication::translate("cadastro", "status", nullptr));
        menuCadastro->setTitle(QApplication::translate("cadastro", "Cadastro", nullptr));
    } // retranslateUi

};

namespace Ui {
    class cadastro: public Ui_cadastro {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CADASTRO_H
