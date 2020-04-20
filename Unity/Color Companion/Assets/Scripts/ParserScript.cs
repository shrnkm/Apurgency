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
        //stateColor = GetComponent<Image>();
        
        theInput = userIn.text;
        Debug.Log("You wrote: " + theInput);
        if (theInput == "red")
        {
            //stateColor.color = new Color(255, 0, 0, 2);
            stateColor.state = new Color(255, 0, 0, 2);
        }

    }

    void Start()
    {

    }

    void Update()
    {


    }
}
 