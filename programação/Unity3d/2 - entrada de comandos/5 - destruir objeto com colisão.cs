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

	}

    void onCollisionEnter2D(Collision2D outro){
        if(outro.gameObject.CompareTag("bloco")){
            Destroy(outro.gameObject);
        }
    }
    /*
    essa função verifica a colisao de um objeto com outro
    se a tag do outro obejto for "bloco"
    o objeto com a tag bloco que esta em colisão é destruido
     */
}
