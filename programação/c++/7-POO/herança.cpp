#include <iostream>
using namespace std;

class Animal{
	public:
		string raca;
		int patas;
};


class Cachorro : public Animal{
	public:
		bool rabo;

		Cachorro(string raca="viralata", int patas = 4, bool rabo=1){
			this->raca = raca;
			this->patas = patas;
			this->rabo = rabo;
		}
};


int main(int argc, char *argv[])
{
	Cachorro rex("pastor alemao", 4, 1);
	
	cout<<rex.raca;
	return 0;
}