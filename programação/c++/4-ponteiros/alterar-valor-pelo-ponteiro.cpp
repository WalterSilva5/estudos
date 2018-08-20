#include <iostream>

using namespace std;

void alteraValor(int* ponteiro);
int main(){
	int variavel =10;
	int* ponteiro;
	
	ponteiro = &variavel;
	
	alteraValor(ponteiro);
	cout<<variavel;
}

void alteraValor(int* ponteiro){
	*ponteiro = 20;
}