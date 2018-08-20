#include <iostream>
#include <string.h>
using namespace std;

class Conta{
	public:
		int numero;
		double saldo;
		string deposito(double valor){
			if (valor>0){
				saldo+=valor;
				return "Valor depositado com sucesso";
			}
			else{
				return "Valor do deposito deve ser maior que zero";
			}
		}
	
};

int main(int argc, char *argv[])
{
	Conta banco;
	banco.numero = 1;
	banco.saldo = 100;
	cout<<banco.saldo<<endl;
	cout<<banco.numero<<endl;
	cout<<banco.deposito(15.2)<<endl;;
	cout<<banco.saldo<<endl;	
	
	return 0;
}

