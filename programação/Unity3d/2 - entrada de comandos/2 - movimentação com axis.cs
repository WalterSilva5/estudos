using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class andar : MonoBehaviour {
	private 	float vel = 4.5f;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		float H = Input.GetAxis("Horizontal");
		transform.Translate(new Vector3(H*Time.deltaTime,0,0));
	}
    /*
    antes de usar essa movimentação "horizontal" é necessario criala no unity
     */
}
