using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class variaveis : MonoBehaviour {

	// Use this for initialization
	public float vel = 0.1f;
	public Renderer quad;

	void Start () {
		
	}

    // Update is called once per frame
    void Update () {
		Vector2 offset = new Vector2(vel * Time.deltaTime, 0);
		/*isso significa que o objeto vai se mover na velocidade vel*Time.deltaTime
		 * no eixo X
		 */

		quad.material.mainTextureOffset += offset;
    }
}
