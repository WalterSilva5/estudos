using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pular : MonoBehaviour
{
	public float forca = 500f;
	public bool liberaPulo = false;
	public int duplo = 2;
	public Rigidbody2D bola;
	// Use this for initialization
	void Start()
	{

	}

	// Update is called once per frame
	void Update()
	{
		if (duplo > 0)
		{
			if (Input.GetKeyDown(KeyCode.Space))
			{
				bola.AddForce(new Vector2(0, forca * Time.deltaTime), ForceMode2D.Impulse);
			}
		}

	}

	void onCollisionEnter2D(Collision2D outro)
	{
		if (outro.gameObject.CompareTag("chao"))
		{
			duplo = 2;
			liberaPulo = true;
		}
	}

	void OnCollisionExit2D(Collision2D outro)
	{
		if (outro.gameObject.CompareTag("chao"))
		{
			liberaPulo = false;
		}
	}
	/*
    essa função verifica a colisao de um objeto com outro
    se a tag do outro obejto for "bloco"
    o objeto com a tag bloco que esta em colisão é destruido
     */
}
