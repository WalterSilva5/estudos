package _1_Arrays;

class CriaPessoa{
    public String nome;
    public int idade;
}


class ArrayDePessoas{
    CriaPessoa[] pessoas = new CriaPessoa[1];
}


public class Pessoa {
    public static void main(String[] args){
        ArrayDePessoas Lista = new ArrayDePessoas();
        CriaPessoa[] pessoas = new CriaPessoa[1];
        Lista.pessoas[0] = new CriaPessoa();
        Lista.pessoas[0].nome = "walter";
        Lista.pessoas[0].idade = 22;

        System.out.println(Lista.pessoas[0].nome);
    }
}
