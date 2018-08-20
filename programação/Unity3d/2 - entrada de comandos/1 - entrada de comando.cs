/*
as entradas de comandos sao lidas atraves do if 

ex if(input algum comando do teclado){
    executa uma ação;
}
 */

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class andar : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown(KeyCode.RightArrow))
		{
			transform.Translate(new Vector3(vel * Time.deltaTime, 0, 0));
		}
      	//direita
        {
			transform.Translate(new Vector3(-vel* Time.deltaTime, 0, 0));
		}//esquerda

        /*
        ao pressionar a tecla direita(right arrow)
        é somado 0.1f a posicao do personagem
        quanto mais clicamos mais ele anda
         */
	}
}

// podemos ainda usar os elementos do menu edit/projec settings/input