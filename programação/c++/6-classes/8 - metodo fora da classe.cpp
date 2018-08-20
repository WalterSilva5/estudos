#include <iostream>
using namespace std;

class Pessoa{

	public:
	   	int idade;
		string nome;
				
		int getIdade();
		void setIdade(int idade);

};


//esse metodo pertence a classe pessoa e esta declarado fora
int Pessoa::getIdade(void){
	return this->idade;
}

void Pessoa::setIdade(int idade){
	this->idade = 22;
}

int main(int argc, char *argv[])
{
	Pessoa usuario;
	Pessoa* pusuario = &usuario;
	
	pusuario->nome = "walter";
	pusuario->setIdade(22);
	cout<<pusuario->getIdade();
}