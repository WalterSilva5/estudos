#include <iostream>
#include <string.h>
using namespace std;

typedef struct pessoa{
	char nome[100];
	int idade;
}t_pessoa;

int main(int argc, char *argv[])
{
	t_pessoa pessoa[10];//array com 10 pessoas estruturadas
	pessoa[0].idade = 22;
	strcpy(pessoa[0].nome, "walter");
	
	cout<<pessoa[0].nome<<endl;
	cout<<pessoa[0].idade<<endl;
	
	return 0;
}