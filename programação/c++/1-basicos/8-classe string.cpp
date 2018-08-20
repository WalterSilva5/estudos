#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	string nome = "walter";
	
	nome.erase(0,3);
	cout<<nome;
	return 0;
}