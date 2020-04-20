using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ParserScript : MonoBehaviour
{
    public InputField userIn;
    private string theInput;

    public void OnSubmit()
    {
        theInput = userIn.text;
        Debug.Log("You wrote" + theInput);
    }

    void Start()
    {

    }

    void Update()
    {


    }
}
 