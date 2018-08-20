using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Variaveis : MonoBehaviour
{

	/*
        podemos fazer conversão com cast explicito
        ex:
            int n2 = (float) n1;
        ou o cast por classe por ex:
            int n2 = n.toString()
     */

	// Use this for initialization
	int n = 22;
	string n2;
	void Start()
	{
		n2 = n.ToString();
		print(n2);

	}

	// Update is called once per frame
	void Update()
	{

	}
}
