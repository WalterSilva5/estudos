//classe cs:

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class variaveis : MonoBehaviour {

	// Use this for initialization
	void Start () {
    }

    // Update is called once per frame
    void Update () {
        transform.Translate(new Vector3(0.001f, 0, 0));
        //o metodo para transformação de deslisar é o Translate

        /*essa linha de cima faz o boneco andar pra direita
        o 0.001f é a velocidade que o boneco anda pra direita 

        pra atribuir esse movimento basta jogar essa classe no personagem arrastando no unity
         *//

         /*
         os parametros que a classe Vector3(x, y, z)
         são as posições de movimentação no eixo
          */
    }
}
