#include <iostream>
using namespace std;

class Pessoa{
	public:
		string nome;
		
	
};

int main(int argc, char *argv[])
{
	Pessoa usuario;
	Pessoa* pusuario = &usuario;
	
	pusuario->nome = "walter";
	cout<<pusuario->nome;
	return 0;
}