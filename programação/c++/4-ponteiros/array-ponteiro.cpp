#include <iostream>

using namespace std;

int main(int argc, char** argv)
{	
	int* parray = new int[10];
	*(parray) = 10;
	cout<<*(parray)<<endl;
	*(parray+1)=20;
	cout<<*(parray+1);
	delete[] parray;
	parray = NULL;
	return 0;
}