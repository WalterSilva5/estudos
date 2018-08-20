using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class variaveis : MonoBehaviour {

	// Use this for initialization
	void Start () {
		print("pegou");
	}

    // Update is called once per frame
    void Update () {
        transform.localScale += new Vector3(0.1f, 0.1f, 0);
        //o objeto cresce no eixo x e y na velocidade 0.1f
    }
}
