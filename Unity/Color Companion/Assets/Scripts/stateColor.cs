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
        state = new Color(0, 255, 0, 256);
    }

    // Update is called once per frame
    void Update()
    {
        stateImage.color = state;
    }
}
