#include <iostream>
using namespace std;

Class carro{
	   char nome[100];
	   char cor[20];
	   char placa[20];
	   double preco;
};


void bubbleSort( Carro carros[], int tam){
	int i, j, aux;
	for(int i = tam; i>=0; i--){
		for(int j = 1; j<=i; j++){
			if(vet[j-1]>vet[j]){
				aux = vet[j-1];
				vet[j-1]=vet[j];
				vet[j] = aux;
			}
		}
	}
	
}
int main(int argc, char *argv[])
{
	Carro carros[3];
	for(i=0; i<3; i++){
		cout<<"Nome: ";
		cin>>carros[i].nome;
		cout<<"Preço: ";
		cin>>carros[i].preco;
		cout<<endl;
	}
	return 0;
}