#include <iostream>
using namespace std;

class Carro{
	public:
		int n1, n2;
		
		Carro(int n1){
			this->n1 = n1;
			this->n2 = 30;
		};
	
		Carro(int n1, int n2){
			this->n1 = n1;
			this->n2 = n2;
		};
		
};


int main(int argc, char *argv[])
{
	Carro carro(10);
	Carro carro2(10, 20);
	
	cout<<carro.n1<<endl;
	cout<<carro.n2<<"\n--\n"<<endl;
	
	cout<<carro2.n1<<endl;
	cout<<carro2.n2<<endl;
	
	return 0;
}