using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class andar : MonoBehaviour {
	public float forca=2.5f;
    public RigidBody2D bola;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if(input.GetKeyDown(KeyCode.Space))
        {
            bola.addForce(new Vector2(0,forca*Time.deltaTime), ForceMode2d.Impulse);
        }
	}
    /*
        depois de adicionar essa classe ao objeto alvo devemos definir tambem
        na tabela inspector onde vai aparecer uma aba com o nome da classe do script
        vai ter uma linha com o nome bola
        no parametro dessa linha devemos arrastar o arquivo da bola da aba Hierachy/cena
        (ao lado do inspector) ate o parametro da classe na aba inspector
     */
}
