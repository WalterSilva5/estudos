#include <iostream>
#include <string.h>
using namespace std;

class Pessoa{
	public:
		char nome[100];
		int idade;
};


int main(int argc, char *argv[])
{
	Pessoa p1;
	
	p1.idade =22;
	strcpy(p1.nome, "walter");
	
	cout<<p1.nome<<endl;
	cout<<p1.idade<<endl;
	
	
	return 0;
}