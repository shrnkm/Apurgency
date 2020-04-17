using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class stateColor : MonoBehaviour
{
    private Image state;

    void Start()
    {
        state = GetComponent<Image>();
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.S))
        {
            state.color = new Color(255, 0, 0);
        }
    }
}
