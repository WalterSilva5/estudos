#include <iostream>

using namespace std;

int main(int argc, char *argv[]){
	int vetor[100];
	
	for(int i=0; i<=100; i++){
		vetor[i]=i+1;
	}
	for(int x=0; x<=100; x++){
		cout<<vetor[x]<<"-";
	}
}