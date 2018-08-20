#include <iostream>
/*
o metodo strcat concatena duas strings, adicionando
o conteudo da segunda string ao final da primeira
*/
using namespace std;

void my_strcat(char* dest, char* orig);
int my_strlen(char* palavra);

int main(int argc, char *argv[]){
    char * nome1 = new char[100];
    char * nome2 = new char[100];

    cout<<"nome1: ";
    cin>>nome1;
    cout<<"nome2: ";
    cin>>nome2;

    my_strcat(nome1, nome2);

    cout<<nome1;
    return 0;
}

int my_strlen(char* palavra){
    //conta a quantidade de caracteres da string no parametro
    int cont = 0;
    while(palavra[cont]!='\0'){
        cont ++;
    }
    return cont;
}

void my_strcat(char* dest, char* orig){
    int tam1 = my_strlen(dest);
    int tam2 = my_strlen(orig);

    for (int i = 0; i<tam2; i++){
        *(dest+tam1+i)=orig[i];
    }
}

