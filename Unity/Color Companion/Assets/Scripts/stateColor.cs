using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class stateColor : MonoBehaviour
{
    public static Color state;
    public Image stateImage;

    void Start()
    {
        state = new Color(255, 0, 255, 250);
    }

    // Update is called once per frame
    void Update()
    {
        stateImage.color = state;
    }
}
