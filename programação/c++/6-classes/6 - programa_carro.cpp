#include <iostream>
#include <string.h>

using namespace std;

class Carro{
	private:
		string nome;
		int placa;
		
	public:
		string getNome(){
			return this->nome;
		}
		void setNome(string nome){
			this->nome = nome;
		}		
		
		int getPlaca(){
			return this->placa;
		}
		void setPlaca(int placa){
			this->placa = placa;
		}
};

int main(int argc, char *argv[])
{
	Carro mod1;
	mod1.setNome("Caminhonete");
	mod1.setPlaca(123);
	
	cout<<mod1.getNome()<<endl;
	cout<<mod1.getPlaca();
	
	
	return 0;
}
