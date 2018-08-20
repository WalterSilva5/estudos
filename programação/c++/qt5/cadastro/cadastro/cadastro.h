#ifndef CADASTRO_H
#define CADASTRO_H

#include <QMainWindow>

namespace Ui {
class cadastro;
}

class cadastro : public QMainWindow
{
    Q_OBJECT

public:
    explicit cadastro(QWidget *parent = 0);
    ~cadastro();

private:
    Ui::cadastro *ui;
};

#endif // CADASTRO_H
