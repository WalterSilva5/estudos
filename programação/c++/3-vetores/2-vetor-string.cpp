#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char** argv)
{
	setlocale(LC_ALL,"portuguese");
	char nome[] = "walter";
	char sobrenome[]={'s','i','l','v','a','\0'};
	cout<<"Nome: "<<nome<<" "<<sobrenome<<endl;
	
	int tamanho = strlen(nome)+strlen(sobrenome);
	cout<<"Tamanho do nome: "<<tamanho;
	
	bool letra = isalpha(nome[0]);
	cout<<"O caractere é "<<letra;
	return 0;
}